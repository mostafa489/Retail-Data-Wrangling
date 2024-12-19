SELECT 
    'invoice_no', 'customer_id', 'gender', 'age', 'category', 'shopping_mall', 'country', 'quantity', 'price', 'payment_method', 'invoice_date', 'total_cost', 'normalized_spending', 'season', 'age_group', 'store_name', 'mall_total_sales', 'mall_avg_sales', 'mall_stddev_sales', 'customer_total_spent', 'customer_rank', 'monthly_sales', 'year', 'month' 
UNION ALL 
SELECT 
    f.invoice_no,
    f.customer_id,
    CASE 
        WHEN f.gender = 'Male' THEN 0
        WHEN f.gender = 'Female' THEN 1
        ELSE NULL
    END AS gender,
    f.age,
    f.category,
    f.shopping_mall,
    f.country,
    f.quantity,
    f.price,
    f.payment_method,
    f.invoice_date,
    f.total_cost,
    (f.total_cost / (SELECT MAX(total_cost) FROM final.final)) AS normalized_spending,
    f.season,
    CASE 
        WHEN f.age < 18 THEN 'Under 18'
        WHEN f.age BETWEEN 18 AND 25 THEN '18-25'
        WHEN f.age BETWEEN 26 AND 35 THEN '26-35'
        ELSE '36+'
    END AS age_group,
    f.store_name,
    ad.total_sales AS mall_total_sales,
    ad.avg_sales AS mall_avg_sales,
    ad.stddev_sales AS mall_stddev_sales,
    rc.total_spent AS customer_total_spent,
    rc.customer_rank,
    ms.monthly_sales,
    ms.year,
    ms.month
FROM final.final f
LEFT JOIN (
    SELECT 
        shopping_mall,
        category,
        season,
        COUNT(invoice_no) AS total_transactions,
        SUM(total_cost) AS total_sales,
        AVG(total_cost) AS avg_sales,
        MIN(total_cost) AS min_sales,
        MAX(total_cost) AS max_sales,
        STDDEV(total_cost) AS stddev_sales
    FROM final.final
    GROUP BY shopping_mall, category, season
) ad ON f.shopping_mall = ad.shopping_mall 
     AND f.category = ad.category 
     AND f.season = ad.season
LEFT JOIN (
    SELECT 
        customer_id,
        SUM(total_cost) AS total_spent,
        RANK() OVER (ORDER BY SUM(total_cost) DESC) AS customer_rank
    FROM final.final
    GROUP BY customer_id
) rc ON f.customer_id = rc.customer_id
LEFT JOIN (
    SELECT 
        EXTRACT(YEAR FROM invoice_date) AS year,
        EXTRACT(MONTH FROM invoice_date) AS month,
        SUM(total_cost) AS monthly_sales
    FROM final.final
    GROUP BY EXTRACT(YEAR FROM invoice_date), EXTRACT(MONTH FROM invoice_date)
) ms ON EXTRACT(YEAR FROM f.invoice_date) = ms.year 
     AND EXTRACT(MONTH FROM f.invoice_date) = ms.month

-- Wrap the entire query in a subquery to apply ORDER BY on the final result
ORDER BY invoice_date DESC
INTO OUTFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\wadenyleb3eed612.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n';
