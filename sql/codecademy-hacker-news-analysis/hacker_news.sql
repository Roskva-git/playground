SELECT timestamp,
   strftime('%H', timestamp) AS 'Time',
   ROUND(AVG(score)) AS 'Average score', COUNT(*) AS 'Count'
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 2
ORDER BY 3 DESC;
