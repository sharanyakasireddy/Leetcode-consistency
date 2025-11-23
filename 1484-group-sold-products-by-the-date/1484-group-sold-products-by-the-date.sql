SELECT
  sell_date,
  COUNT(DISTINCT product) AS num_sold,
  GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;


#GROUP_CONCAT(product ORDER BY product)
# Joins all products into a single string.
# Sorted alphabetically.
# Separated by commas.