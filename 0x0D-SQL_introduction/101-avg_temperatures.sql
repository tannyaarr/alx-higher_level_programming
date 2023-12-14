-- displays the average temperature


SELECT city, AVG((temperature * 9/5) + 32) AS avg_tempeRATURE_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC
