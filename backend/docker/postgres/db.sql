CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR
);

INSERT INTO users VALUES (1, 'test');

CREATE TABLE metamask_twitch (
    user_id INT,
    twitch_handle VARCHAR,
    metamask_id VARCHAR,
    PRIMARY KEY(twitch_handle, metamask_id)
);

INSERT INTO metamask_twitch VALUES (1, 'test_twitch', 'test_metamask');
