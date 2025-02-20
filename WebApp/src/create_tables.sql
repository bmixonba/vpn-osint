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

CREATE TABLE IF NOT EXISTS vpnosint_network_db ( 
	id SERIAL PRIMARY KEY,
       	business_id INT REFERENCES vpnosint_business_db(id) ON DELETE CASCADE,
	network_ip_address VARCHAR(255),
	network_reverse_ip_address VARCHAR(255),
	network_ip_latitude INT,
	network_ip_longitude INT,
	network_as_name VARCHAR(255),
	network_as_company_url VARCHAR(255),
	network_as_number INT,
	network_as_city VARCHAR(255),
	network_as_state VARCHAR(255),
	network_timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS vpnosint_business_github_query_db (
	id SERIAL PRIMARY KEY,
	business_id INT REFERENCES vpnosint_business_db(id) ON DELETE CASCADE,
	github_query_string VARCHAR(255),
	github_code_count INT,
	github_repo_count INT,
	github_issue_count INT,
	github_pull_request_count INT,
	github_discussion_count INT,
	github_user_count INT,
	github_commit_count INT,
	github_packages_count INT,
	github_wiki_count INT,
	github_topics_count INT,
	github_marketplace_count INT,
	github_timestamp TIMESTAMP,
	github_notes TEXT
);

CREATE TABLE IF NOT EXISTS vpnosint_business_code_transparency_db (
	id SERIAL PRIMARY KEY,
	business_id INT REFERENCES vpnosint_business_db(id) ON DELETE CASCADE,
	github_account_name VARCHAR(255),
	github_account_exists BOOLEAN,
	gitlab_account_name VARCHAR(255),
	gitlab_account_exists BOOLEAN,
	gitee_account_name VARCHAR(255),
	gitee_account_exists BOOLEAN,
	is_open_source BOOLEAN
);

CREATE TABLE IF NOT EXISTS vpnosint_business_distribution_google_play (
	id SERIAL PRIMARY KEY,
	business_id INT REFERENCES vpnosint_business_db(id) ON DELETE CASCADE,
	gp_url VARCHAR(255),
	gp_app_name VARCHAR(255),
	gp_developer VARCHAR (255),
	gp_contains_ads BOOLEAN,
	gp_stars INT,
	gp_reviews INT,
	gp_downloads INT,
	gp_rating INT,
	gp_website VARCHAR(255),
	gp_support_email VARCHAR(255),
	gp_privacy_policy VARCHAR(255),
	gp_address_street VARCHAR(255),
	gp_address_city VARCHAR(255),
	gp_address_state VARCHAR(255),
	gp_address_country VARCHAR(255),
	gp_address_zipcode VARCHAR(255),
	gp_contact_email VARCHAR(255),
	gp_contact_developer_name VARCHAR(255),
	gp_phone_number VARCHAR(255),
	gp_timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS vpnosint_business_open_corporates_db (
	id SERIAL PRIMARY KEY,
	business_id INT REFERENCES vpnosint_business_db(id) ON DELETE CASCADE,
	oc_query_string VARCHAR(255),
	oc_url VARCHAR(255),
	oc_company_number INT,
	oc_status VARCHAR(255),
	oc_incorporation_date TIMESTAMP,
	oc_company_type VARCHAR(255),
	oc_jurisdiction VARCHAR(255),
	oc_registered_address_name VARCHAR(255),
	oc_registered_address_street VARCHAR(255),
	oc_registered_address_city VARCHAR(255),
	oc_registered_address_state VARCHAR(255),
	oc_registered_address_country VARCHAR(255),
	oc_registered_address_zip VARCHAR(255),
	oc_director_officer VARCHAR(255),
	oc_data_source_last_updated TIMESTAMP,
	oc_data_source_last_changed TIMESTAMP,
	oc_data_source_url VARCHAR(255),
	oc_timestamp TIMESTAMP
);


CREATE TABLE IF NOT EXISTS vpnosint_business_open_corporates_trademark_registration_db (
	id SERIAL PRIMARY KEY,
	business_id INT REFERENCES vpnosint_business_db(id) ON DELETE CASCADE,
	oc_mark_text VARCHAR(255),
	oc_image_url VARCHAR(255),
	oc_register VARCHAR(255),
	oc_nice_classification VARCHAR(255),
	oc_registration_date TIMESTAMP,
	oc_expiry TIMESTAMP,
	oc_trademark_url TEXT,
	oc_source_url TEXT,
	oc_holder_name TEXT,
	oc_holder_address_street VARCHAR(255),
	oc_holder_address_city VARCHAR(255),
	oc_holder_address_state VARCHAR(255),
	oc_holder_address_country VARCHAR(255),
	oc_holder_address_zip INT,
	oc_holder_latitude INT,
	oc_holder_longitude INT,
	oc_correspondent_name TEXT,
	oc_correspondent_address_street VARCHAR(255),
	oc_correspondent_address_city VARCHAR(255),
	oc_correspondent_address_state VARCHAR(255),
	oc_correspondent_address_country VARCHAR(255),
	oc_correspondent_address_latitude INT,
	oc_correspondent_address_longitude INT,
	oc_trademark_notes TEXT,
	oc_tm_timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS vpnosint_business_person_db (
	id SERIAL PRIMARY KEY,
	business_id INT REFERENCES vpnosint_business_db(id) ON DELETE CASCADE,
	person_first_name VARCHAR(255),
	person_last_name VARCHAR(255),
	person_source TEXT,
	person_affiliation TEXT,
	person_notes TEXT,
	person_source_type VARCHAR(255),
	person_timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS vpnosint_apk_to_file_db (
	id SERIAL PRIMARY KEY,
       	apk_id INT REFERENCES vpnosint_vpn_apk_db(id) ON DELETE CASCADE,
	file_name VARCHAR(255),
	file_sha256 VARCHAR(255),
	file_type VARCHAR(255),
	file_extension VARCHAR(255),
	file_timestamp TIMESTAMP,
	file_last_modified TIMESTAMP
);


CREATE TABLE IF NOT EXISTS vpnosint_apk_to_function_db (
	id SERIAL PRIMARY KEY,
       	apk_id INT REFERENCES vpnosint_vpn_apk_db(id) ON DELETE CASCADE,
	fn_package_name VARCHAR(255),
	fn_function_name VARCHAR(255),
	fn_path VARCHAR(255),
	fn_code_sha256 VARCHAR(255),
	fn_timestamp TIMESTAMP,
	fn_last_modified TIMESTAMP
);

