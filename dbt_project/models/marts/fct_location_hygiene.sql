
with last_clean as (
  select location, max(timestamp) as last_checkin_ts
  from {{ source('raw','checkins') }}
  group by 1
)
select * from last_clean
