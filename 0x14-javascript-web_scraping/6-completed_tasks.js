#!/usr/bin/node
const request = require('request'), apiUrl = process.argv[2];

if (!apiUrl) console.log("Usage: ./completed_tasks.js <api_url>");
else request(apiUrl, { json: true }, (error, response, body) => {
    const completedTasksByUser = body.reduce((acc, task) => {
        if (task.completed) {
            acc[task.userId] = (acc[task.userId] || 0) + 1;
        }
        return acc;
    }, {});

    Object.entries(completedTasksByUser).forEach(([userId, completedTasks]) => console.log(`User ${userId}: ${completedTasks} completed tasks`));
});
