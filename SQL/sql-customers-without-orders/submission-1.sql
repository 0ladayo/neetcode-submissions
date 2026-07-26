-- Write your query below
select c.name
from customers c
where not exists (
    select 1
    from orders o
    where c.id = o.customer_id
);