-- displays avg temp(fahrenheit) by city ordered by temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
