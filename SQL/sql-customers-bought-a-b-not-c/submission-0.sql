-- Write your query below

with temp_table as (
    select c.customer_id, c.customer_name, o.product_name
    from customers c
    inner join orders o
    on c.customer_id = o.customer_id
)

(select customer_id, customer_name from temp_table
where product_name = 'A'
intersect
select customer_id, customer_name from temp_table
where product_name = 'B'
except
select customer_id, customer_name from temp_table
where product_name = 'C')
order by customer_name;