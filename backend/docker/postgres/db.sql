CREATE TABLE users (
    id INT,
    username VARCHAR
);

INSERT INTO users VALUES (1, 'test');

CREATE TABLE metamask_twitch (
    user_id INT,
    twitch_handle VARCHAR,
    metamask_id VARCHAR
);

INSERT INTO metamask_twitch VALUES (1, 'test_twitch', 'test_metamask');
