INSERT INTO mb_data.medium (id,
                            release,
                            position,
                            name,
                            track_count)
    SELECT id,
           release,
           position,
           name,
           track_count
    FROM musicbrainz.medium
    WHERE medium.format in (7, 29, 30, 31)
;


INSERT INTO mb_data.release (id,
                             gid,
                             name,
                             artist_credit,
                             release_group,
                             barcode
--                               packaging,
--                               label,
--                               country,
--                               year
                              )
    SELECT release.id,
           release.gid,
           release.name,
           release.artist_credit,
           release.release_group,
           release.barcode
--            release_packaging.name,
--            release_label.label,
--            release_country.country,
--            release_country.date_year
    FROM musicbrainz.release
--     LEFT JOIN musicbrainz.release_packaging
--         ON release.packaging = release_packaging.id
--     RIGHT JOIN musicbrainz.release_label
--         ON release_label.release = release.id
--     LEFT JOIN musicbrainz.release_country
--         ON release.id = musicbrainz.release_country.release
    WHERE release.id in (SELECT release from mb_data.medium)
;
-- remove duplicate rows in release table and make 'id' a primary key
-- due to multiple countries and labels for the release with the same ID
-- DELETE FROM mb_vinyl.release a USING mb_vinyl.release b WHERE a.id=b.id AND a.ctid < b.ctid
;


INSERT INTO mb_data.release_group (id,
                                   name,
                                   artist_credit
--                                     release_type,
--                                     rating
                                    )
    SELECT release_group.id,
           release_group.name,
           release_group.artist_credit
--            release_group_primary_type.name,
--            release_group_meta.rating
    FROM musicbrainz.release_group
--     LEFT JOIN musicbrainz.release_group_primary_type
--         ON release_group.type = release_group_primary_type.id
--     INNER JOIN mb_vinyl.release
--         ON musicbrainz.release_group.id = mb_vinyl.release.release_group
--     INNER JOIN musicbrainz.release_group_meta
--         ON musicbrainz.release_group.id = musicbrainz.release_group_meta.id
    WHERE release_group.id in (SELECT release_group FROM mb_data.release)
;

-- UPDATE mb_vinyl.release_group
--     SET release_type = id
--     FROM musicbrainz.release_group_primary_type
--         WHERE mb_vinyl.release_group.type = musicbrainz.release_group_primary_type.id

-- remove duplicate rows in release table
-- DELETE FROM mb_vinyl.release_group a USING mb_vinyl.release_group b WHERE a.id=b.id AND a.ctid < b.ctid;
--     make id the primary key in release table


INSERT INTO mb_data.artist_credit (id,
                                   name)
    SELECT artist_credit.id,
           artist_credit.name
    FROM musicbrainz.artist_credit
    WHERE artist_credit.id in (SELECT artist_credit FROM mb_data.release_group)
    OR artist_credit.id in (SELECT artist_credit FROM mb_data.release)
;

INSERT INTO mb_data.track (id,
                           name,
                           artist_credit,
                           position,
                           length,
                           medium
                            )
    SELECT track.id,
           track.name,
           track.artist_credit,
           track.position,
           track.length,
           mb_data.medium.id
    FROM musicbrainz.track
    INNER JOIN mb_data.medium
    ON musicbrainz.track.medium = mb_data.medium.id
;
--
--
--
--
-- INSERT INTO mb_vinyl.artist_credit_name (artist_credit,
--                                          name,
--                                          position,
--                                          artist,
--                                          join_phrase)
--     SELECT artist_credit_name.artist_credit,
--            name,
--            position,
--            artist,
--            join_phrase
--     FROM musicbrainz.artist_credit_name
--     WHERE artist_credit_name.artist_credit in (select artist_credit from mb_vinyl.release)
-- ;
--
--
-- INSERT INTO mb_vinyl.artist (id,
--                              name,
--                              sort_name,
--                              begin_date_year,
--                              end_date_year,
--                              area,
--                              rating)
--     SELECT artist.id,
--            name,
--            sort_name,
--            begin_date_year,
--            end_date_year,
--            area,
--            rating
--     FROM musicbrainz.artist
--     INNER JOIN musicbrainz.artist_meta
--         ON musicbrainz.artist.id = musicbrainz.artist_meta.id
--     WHERE artist.id in (select artist from mb_vinyl.artist_credit_name)
-- ;
--
--
-- INSERT INTO mb_vinyl.cover_art (id,
--                                 release,
--                                 ordering,
--                                 mime_type,
--                                 suffix)
--     SELECT cover_art.id,
--            cover_art.release,
--            cover_art.ordering,
--            cover_art.mime_type,
--            image_type.suffix
--     FROM cover_art_archive.cover_art
--     INNER JOIN cover_art_archive.image_type
--         ON cover_art.mime_type = image_type.mime_type
--     INNER JOIN cover_art_archive.cover_art_type
--         ON cover_art.id = cover_art_type.id
--     INNER JOIN cover_art_archive.art_type
--         ON cover_art_type.type_id = art_type.id
--     RIGHT JOIN mb_vinyl.release
--         ON cover_art_archive.cover_art.release = mb_vinyl.release.id
--     WHERE art_type.name='Front'
-- ;
--
--
-- INSERT INTO mb_vinyl.label (id,
--                             name,
--                             area)
--     SELECT id,
--            name,
--            area
--     FROM musicbrainz.label
--     WHERE label.id in (select label from mb_vinyl.release)
-- ;
--
--
-- INSERT INTO mb_vinyl.area (id,
--                            name)
--     SELECT id,
--            name
--     FROM musicbrainz.area
-- ;
--
--
-- INSERT INTO mb_vinyl.genre (id,
--                             name)
--     SELECT id,
--            name
--     FROM musicbrainz.genre
-- ;
--
