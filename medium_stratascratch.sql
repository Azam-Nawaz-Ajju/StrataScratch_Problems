
-- Problem ID : 2000 - Variable vs Fixed Rates 
-- PostgresSQL 

SELECT 
    loan_id, 
    CASE WHEN rate_type = 'fixed' THEN 1 ELSE 0 END as fixed, 
    CASE WHEN rate_type = 'variable' THEN 1 ELSE 0 END as variable
FROM submissions


-- Problem ID : 2001 Share of Loan balance 
-- PostgresSQL

SELECT 
    rate_type,
    loan_id,
    balance, 
    100.0 * ((balance::numeric)/ sum(balance) OVER (PARTITION BY rate_type) ) as balance_share
FROM submissions 
ORDER BY 1,2,3

--  Problem ID : 2003 Recent Refinance Submissions 
-- PostgresSQL


WITH recent_submisison as 
(
SELECT 
    id as loan_id, 
    user_id, 
    created_at,
    MAX(created_at) OVER(PARTITION BY user_id) as recent_submisison
FROM loans 
WHERE type = 'Refinance'
) 
SELECT 
    user_id, 
    s.balance
FROM recent_submisison rs
JOIN submissions s 
   ON rs.loan_id = s.loan_id
WHERE rs.created_at = rs.recent_submisison
ORDER BY rs.loan_id


-- Problem ID : 2005 -- Share of Active Users
-- postgresSQL

SELECT 
    100.0 * (SUM(CASE WHEN status = 'open' AND country = 'USA' THEN 1 ELSE 0 END))/ 
    COUNT(*) as us_activ_share
FROM fb_active_users

-- Problem ID : 2010 -- Top 3 Streamers 
-- PostgresSQL 

WITH filter_data as (
SELECT 
    user_id,
    COUNT(CASE WHEN session_type = 'streamer' THEN session_id END) as streaming_sessions, 
    COUNT(CASE WHEN session_type = 'viewer' THEN session_id END) AS viewing_sessions
FROM twitch_sessions 
WHERE session_id IS NOT NULL
GROUP BY user_id
HAVING COUNT(CASE WHEN session_type = 'streamer' THEN session_id END) > 
       COUNT(CASE WHEN session_type = 'viewer' THEN session_id END)
)

SELECT 
    user_id, 
    SUM(streaming_sessions) as streamer, 
    SUM(viewing_sessions) as viewer
FROM filter_data
GROUP BY user_id 
HAVING SUM(streaming_sessions) > SUM(viewing_sessions)
ORDER BY streamer DESC
LIMIT 3;


-- Problem ID : 2014 -- Hour With The Highest Order Volume 

WITH order_counts as 
(
    SELECT 
        DATE_TRUNC('day', order_timestamp_utc) as order_date,
        EXTRACT('HOUR' FROM order_timestamp_utc) as hour,
        COUNT(id) as order_count
    FROM postmates_orders 
    GROUP BY 1,2
), 
summary as 
(
    SELECT 
        hour, 
        AVG(order_count) as avg_orders
    FROM order_counts
    GROUP BY HOUR
)
SELECT 
    * 
FROM summary
WHERE avg_orders = (SELECT MAX(avg_orders) FROM summary)
ORDER BY avg_orders DESC


-- Problem ID : 2015 -- City With The Highest and Lowest Income Variance 



