export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData)
      .save((err) => {
        if (!err) {
          const jobId = job.id || 'test';
          console.log(`Notification job created: ${jobId}`);
        } else {
          console.error(`Failed to create job: ${err}`);
        }
      });

    job.on('complete', () => {
      const jobId = job.id || 'test';
      console.log(`Notification job ${jobId} completed`);
    });

    job.on('failed', (err) => {
      const jobId = job.id || 'test';
      console.log(`Notification job ${jobId} failed: ${err}`);
    });

    job.on('progress', (progress) => {
      const jobId = job.id || 'test';
      console.log(`Notification job ${jobId} ${progress}% complete`);
    });
  });
}
