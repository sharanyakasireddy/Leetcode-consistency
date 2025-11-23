SELECT 
    user_id,
    CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;


#LEFT(name,1) → first character
#UPPER() → convert first character to capital
#SUBSTRING(name,2) → remaining characters
#LOWER() → convert remaining to lowercase
#CONCAT() → join both