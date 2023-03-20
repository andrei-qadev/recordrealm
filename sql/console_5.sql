select count(*)
from mb_vinyl.release_group
where rating > 90
and release_type = 'Album';


select *
from mb_vinyl.release_aggregate
where artist_credit_name = 'Queens of the Stone Age'
and release_type = 'Album';

select schema_name,
       relname,
       pg_size_pretty(table_size) AS size,
       table_size
FROM (
       SELECT
         pg_catalog.pg_namespace.nspname           AS schema_name,
         relname,
         pg_relation_size(pg_catalog.pg_class.oid) AS table_size

       FROM pg_catalog.pg_class
         JOIN pg_catalog.pg_namespace ON relnamespace = pg_catalog.pg_namespace.oid
     ) t
WHERE schema_name NOT LIKE 'pg_%'
AND schema_name = 'mb_vinyl'
ORDER BY table_size DESC;


SELECT COUNT(*) as medium_count FROM mb_vinyl.medium
UNION
SELECT COUNT(*) as release_count FROM mb_vinyl.release;

SELECT
    (SELECT COUNT(*) FROM mb_vinyl.medium) as medium_count,
    (SELECT COUNT(*) FROM mb_vinyl.release) as release_count;


SELECT release, COUNT(*)
FROM mb_vinyl.medium
GROUP BY release
HAVING COUNT(*) > 1;

TRUNCATE mb_vinyl.release_group;

SELECT COUNT(*)
FROM mb_vinyl.release_group

