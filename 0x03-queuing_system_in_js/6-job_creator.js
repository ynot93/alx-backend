import kue from 'kue';

const queue = kue.createQueue();

const jobObject = {
  phoneNumber: '1234567890',
  message: 'Test message',
}

const job = queue.create('push_notification_code', jobObject)
  .save((error) => {
    if (!error) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.error(`Failed to create job: ${error}`)
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
