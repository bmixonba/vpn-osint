-- Create vpnosint_business_db table
CREATE TABLE IF NOT EXISTS vpnosint_business_db (
    id SERIAL PRIMARY KEY,
    business_name VARCHAR(255) NOT NULL,
    address TEXT,
    source TEXT,
    incorporation_date TIMESTAMP,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION
);

-- Create vpnosint_domain_db table with business_id as foreign key
CREATE TABLE IF NOT EXISTS vpnosint_domain_db (
    id SERIAL PRIMARY KEY,
    domain_name VARCHAR(255) NOT NULL,
    address TEXT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    registrar TEXT,
    registrant TEXT,
    business_id INT,
    CONSTRAINT fk_business
        FOREIGN KEY (business_id)
        REFERENCES vpnosint_business_db (id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS vpnosint_vpn_apk_db (
    id SERIAL PRIMARY KEY,
    apk_name VARCHAR(255) NOT NULL,
);
CREATE TABLE IF NOT EXISTS vpnosint_vpn_company_to_vpn_apk_db (
    id SERIAL PRIMARY KEY,
    business_id INT,
    apk_id INT,
    CONSTRAINT fk_business
        FOREIGN KEY (business_id)
        REFERENCES vpnosint_business_db (id)
        ON DELETE CASCADE
        FOREIGN KEY (apk_id)
        REFERENCES vpnosint_vpn_apk_db (id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS vpnosint_business_to_facebook_db (
	id SERIAL PRIMARY KEY,
	business_id INT REFERENCES vpnosint_business_db(id) ON DELETE CASCADE,
	profile_name VARCHAR(255),
	follower_count INT,
	location VARCHAR(255),
	joined_date TIMESTAMP
);

CREATE TABLE IF NOT EXISTS vpnosint_business_to_twitter_db (
	id SERIAL PRIMARY KEY,
	business_id INT REFERENCES vpnosint_business_db(id) ON DELETE CASCADE,
	profile_name VARCHAR(255),
	follower_count INT,
	following_count INT,
	location VARCHAR(255),
	joined_date TIMESTAMP
);

