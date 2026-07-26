-- Write your query below

with temp_table as (
    select student_id, exam_id, score, row_number() over (partition by student_id order by score desc, exam_id) as ranked
    from exam_results
)

select student_id, exam_id, score
from temp_table
where ranked = 1
order by student_id;