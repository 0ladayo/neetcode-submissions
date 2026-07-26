-- Write your query below

select s.seller_name
from seller s
where not exists (
    select 1
    from orders o 
    where s.seller_id = o.seller_id and (o.sale_date between '2020-01-01' and '2020-12-31')
)
order by s.seller_name;