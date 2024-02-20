#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
	if (!error && response.statusCode === 200) {
		const tasksData = JSON.parse(body);

		const completedTasks = tasksData.filter((task) => task.completed);
		const tcompletedTasksByUser = completedTasks.reduce((countByUser, task) => {
		countByUser[task.userId] = (countByUser[task/userId] || 0) +1;
		return countByUser;
		}, {});
		console.log(completedTasksByUser);
	} else {
		console.error('Error: ${error}');
	}
});
