CREATE INDEX idx_release_aggr_barcode
ON mb_data.release_aggregate (barcode);

CREATE INDEX idx_release_aggr_release_group_id
ON mb_data.release_aggregate (release_group_id);

CREATE INDEX idx_release_aggr_artist_credit_id
ON mb_data.release_aggregate (artist_credit_id);

CREATE INDEX idx_release_aggr_artist_credit_name
ON mb_data.release_aggregate (artist_credit_name);

CREATE INDEX idx_release_aggr_release_group_name
ON mb_data.release_aggregate (release_group_name);

CREATE INDEX idx_artist_aggr_id
ON mb_data.artist_aggregate (id);

CREATE INDEX idx_artist_aggr_name
ON mb_data.artist_aggregate (name);

CREATE INDEX idx_artist_aggr_release_group_id
ON mb_data.artist_aggregate (release_group_id);

CREATE INDEX idx_track_aggr_release_id
ON mb_data.track_aggregate (release_id);

