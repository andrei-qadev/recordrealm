
CREATE MATERIALIZED VIEW mb_data.release_aggregate AS
SELECT
       release.id,
       release_group.name as release_group_name,
       artist_credit.name as artist_credit_name,
       release.year,
       area.name as country_name,
       label.name as label_name,
       release_group.release_type,
       release.packaging as packaging,
       artist_credit.id as artist_credit_id,
       release.barcode,
       release_group.id as release_group_id,
       release.gid
FROM mb_data.release
JOIN mb_data.release_group
    ON release.release_group = release_group.id
JOIN mb_data.artist_credit
    ON release.artist_credit = artist_credit.id
LEFT JOIN mb_data.label
    ON release.label = label.id
LEFT JOIN mb_data.area
    ON release.country = area.id
WITH DATA;

CREATE MATERIALIZED VIEW mb_data.track_aggregate AS
SELECT
    track.id,
    track.name,
    track.length,
    track.position as track_position,
    medium.position as medium_position,
    release.id as release_id
FROM mb_data.track
INNER JOIN mb_data.medium
    ON track.medium = medium.id
INNER JOIN mb_data.release
    ON medium.release = release.id
WITH DATA;

CREATE MATERIALIZED VIEW mb_data.artist_aggregate AS
SELECT
    artist.id,
    artist.name,
    artist.sort_name,
    release_group.id as release_group_id,
    release_group.name as release_group_name,
    artist_credit_name.position as artist_position,
    release_group.release_type
FROM mb_data.artist
LEFT JOIN mb_data.area
    ON artist.area = area.id
JOIN mb_data.artist_credit_name
    ON artist.id = artist_credit_name.artist
JOIN mb_data.release_group
    ON artist_credit_name.artist_credit = release_group.artist_credit
WITH DATA;
