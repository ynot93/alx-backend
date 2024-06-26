import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
})

client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
})

client.subscribe('holberton school channel');

client.on('message', (message, channel) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        client.unsubscribe();
        client.quit();
    }
});
