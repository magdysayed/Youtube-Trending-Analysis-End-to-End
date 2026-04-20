select DISTINCT
	DENSE_RANK() over (order by channel_title) as channel_id, 
	channel_title
INTO channels
From Raw_YouTube_Data

SELECT 
    video_id, 
    trending_date, 
    views, 
    likes, 
    dislikes, 
    comment_count
INTO Video_Stats
FROM Raw_YouTube_Data;

SELECT DISTINCT
    video_id, 
    title, 
    category_id, 
    publish_time,
    (SELECT TOP 1 Channel_ID FROM Channels
    WHERE Channels.channel_title = Raw_YouTube_Data.channel_title) 
    AS Channel_ID
INTO Videos
FROM Raw_YouTube_Data;



SELECT v.title, SUM(s.views) as TotalViews
FROM Videos v
JOIN Video_Stats s ON v.video_id = s.video_id
GROUP BY v.title
ORDER BY TotalViews DESC;
