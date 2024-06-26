import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const port = 1245;
const app = express();
const client = redis.createClient();

const setAsync = promisify(client.set).bind(client);

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
]

function getItemById(id) {
  return listProducts.find((product) => {
    product.id === id
  });
}

app.get('/list_products', (req, res) => {
  const products = listProducts.map((product) => {
    ({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock
    })
  });
  res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = product.stock - (reservedStock || 0);

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = product.stock - (reservedStock || 0);

  if (currentQuantity <= 0) {
    return res.status(400).json({ status: 'Not enough stock available', itemId });
  }

  await reserveStockById(itemId, reservedStock + 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

function reserveStockById(itemId, stock) {
  redis.set((`item.${itemId}`, stock));
}

async function getCurrentReservedStockById(itemId) {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock, 10) : 0;
}

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
