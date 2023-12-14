-- displays the average temperature


SELECT city, AVG(value) 
AS avg_temperature_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;
