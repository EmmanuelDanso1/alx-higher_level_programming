-- createes id with default and unique
CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
	       UNIQUE (ID),
	       name VARCHAR(256));
