CREATE SCHEMA mb_vinyl;
CREATE EXTENSION IF NOT EXISTS pg_trgm;

CREATE TABLE mb_data.medium
(
    id          int,
    release     int NOT NULL,
    position    smallint,
    name        VARCHAR(512),
    track_count int
);

CREATE TABLE mb_data.release
(
    id            int,
    gid           uuid,
    name          VARCHAR(512),
    artist_credit int not null,
    release_group int not null,
    barcode       VARCHAR(256)
--     packaging VARCHAR(100) DEFAULT null,
--     country int,
--     year smallint,
--     label int
);

CREATE TABLE mb_data.release_group
(

    id            int,
    name          VARCHAR(1024),
    artist_credit int not null,
    release_type  VARCHAR(100) DEFAULT null,
    rating        int
);


CREATE TABLE mb_data.artist_credit
(
    id   int,
    name VARCHAR(1024) NOT null
);


CREATE TABLE mb_data.track
(
    id            int,
    name          VARCHAR(2048) not null,
    artist_credit int           not null,
    position      smallint,
    length        int,
    medium        int
);

CREATE TABLE mb_data.artist_credit_name
(
    artist_credit int,
    position      smallint,
    name          VARCHAR(512) NOT null,
    artist        int,
    join_phrase   text
);

CREATE TABLE mb_data.artist
(
    id              int,
    name            VARCHAR(512) NOT null,
    sort_name       VARCHAR(512) NOT null,
    begin_date_year smallint DEFAULT null,
    end_date_year   smallint DEFAULT null,
    area            int      DEFAULT null,
    rating          int
);

CREATE TABLE mb_data.cover_art
(
    id        bigint,
    release   int,
    ordering  int,
    mime_type VARCHAR(100),
    suffix    VARCHAR(100)
);
--
-- CREATE TABLE mb_vinyl.label
-- (
--     id int,
--     name VARCHAR(256) NOT null,
--     area int DEFAULT null
-- );
--
CREATE TABLE mb_data.area
(
    id   int,
    name VARCHAR(100) NOT null
);

CREATE TABLE mb_data.genre
(
    id   int,
    name VARCHAR(100) NOT null
);