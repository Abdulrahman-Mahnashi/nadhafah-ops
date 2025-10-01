
with c as (
  select worker_id, to_date(timestamp) as work_date
  from {{ source('raw','checkins') }}
)
select worker_id, work_date, count(*) as checkins_count
from c
group by 1,2
