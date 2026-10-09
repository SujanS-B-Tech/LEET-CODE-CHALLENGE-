# Write your MySQL query statement below
select product_name,year,price
from Sales s
join product p
using(product_id);