--  add primary keys
ALTER TABLE mb_data.medium
    ADD  PRIMARY KEY (id);

ALTER TABLE mb_data.release
    ADD PRIMARY KEY (id);

ALTER TABLE mb_data.release_group
    ADD PRIMARY KEY (id);

ALTER TABLE mb_data.artist_credit
    ADD PRIMARY KEY (id);

ALTER TABLE mb_data.track
    ADD PRIMARY KEY (id);

ALTER TABLE mb_vinyl.artist_credit_name
    ADD PRIMARY KEY (artist_credit, position);

ALTER TABLE mb_vinyl.artist
    ADD PRIMARY KEY (id);

ALTER TABLE mb_vinyl.cover_art
    ADD PRIMARY KEY (id);

ALTER TABLE mb_vinyl.label
    ADD PRIMARY KEY (id);

ALTER TABLE mb_vinyl.area
    ADD PRIMARY KEY (id);

ALTER TABLE mb_vinyl.genre
    ADD PRIMARY KEY (id);



