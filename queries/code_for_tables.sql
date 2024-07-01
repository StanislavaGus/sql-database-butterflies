DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

CREATE TABLE iF NOT EXISTS nutrition(
   id SERIAL PRIMARY KEY,
  essential_trace_elements VARCHAR(30) NOT NULL,
  favorite_places VARCHAR(20) NOT NULL
);

CREATE TABLE iF NOT EXISTS body(
   id SERIAL PRIMARY KEY,
  color VARCHAR(10) NOT NULL,
  ornament VARCHAR(20) NOT NULL
);

CREATE TABLE iF NOT EXISTS tendrils(
   id SERIAL PRIMARY KEY,
  len INT NOT NULL,
  color VARCHAR(10) NOT NULL,
  features VARCHAR(20) NOT NULL
);

CREATE TABLE iF NOT EXISTS paws(
   id SERIAL PRIMARY KEY,
  len INT NOT NULL,
  color VARCHAR(10) NOT NULL
);

CREATE TABLE iF NOT EXISTS wings(
   id SERIAL PRIMARY KEY,
  color VARCHAR(10) NOT NULL,
  ornament VARCHAR(100) NOT NULL,
  ornament_features VARCHAR(110) NOT NULL,
  shape VARCHAR(10) NOT NULL,
  wingspan INT NOT NULL
);

CREATE TABLE iF NOT EXISTS species_book(
   id SERIAL PRIMARY KEY,
  species_name VARCHAR(100) NOT NULL,
  wings_id INT NOT NULL,
  paws_id INT NOT NULL,
  tendrils_id INT NOT NULL,
  body_id INT NOT NULL,
  nutrition_id INT NOT NULL,
  life_expectancy INT NOT NULL,
	
  CONSTRAINT fk_wings_id FOREIGN KEY (wings_id) REFERENCES wings (id) ON UPDATE CASCADE ON DELETE NO
ACTION,
  CONSTRAINT fk_paws_id FOREIGN KEY (paws_id) REFERENCES paws (id) ON UPDATE CASCADE ON DELETE NO
ACTION,
  CONSTRAINT fk_tendrils_id FOREIGN KEY (tendrils_id) REFERENCES tendrils (id) ON UPDATE CASCADE ON DELETE NO
ACTION,
  CONSTRAINT fk_body_id FOREIGN KEY (body_id) REFERENCES body (id) ON UPDATE CASCADE ON DELETE NO
ACTION,
  CONSTRAINT fk_nutrition_id FOREIGN KEY (nutrition_id) REFERENCES nutrition (id) ON UPDATE CASCADE ON DELETE NO
ACTION
);

CREATE TABLE status_type(
   id SERIAL PRIMARY KEY,
  status_name VARCHAR(60) NOT NULL
);

CREATE TABLE iF NOT EXISTS status(
   id SERIAL PRIMARY KEY,
  status_type INT NOT NULL,
  assignment_date VARCHAR(10) NOT NULL,
  cancellation_date VARCHAR(10) NOT NULL,
  species_id INT NOT NULL,
  
  CONSTRAINT fk_species_id FOREIGN KEY (species_id) REFERENCES species_book (id) ON UPDATE CASCADE ON DELETE NO
ACTION,
  CONSTRAINT fk_status_type FOREIGN KEY (status_type) REFERENCES status_type (id) ON UPDATE CASCADE ON DELETE NO
ACTION
);


CREATE TABLE iF NOT EXISTS user_(
   id SERIAL PRIMARY KEY,
  user_login VARCHAR(20) NOT NULL,
  user_password VARCHAR(30) NOT NULL,
  user_name VARCHAR(20) NOT NULL
);

CREATE TABLE iF NOT EXISTS butterfly(
   id SERIAL PRIMARY KEY,
  author_id INT NOT NULL,
  species_id INT NOT NULL,
  coordinates VARCHAR(20) NOT NULL,
  data VARCHAR(10) NOT NULL,
  
  CONSTRAINT fk_species_id FOREIGN KEY (species_id) REFERENCES species_book (id) ON UPDATE CASCADE ON DELETE NO
ACTION,
  CONSTRAINT fk_author_id FOREIGN KEY (author_id) REFERENCES user_ (id) ON UPDATE CASCADE ON DELETE NO
ACTION
);

CREATE TABLE iF NOT EXISTS photo(
   id SERIAL PRIMARY KEY,
  butterfly_id INT NOT NULL,
  photo BYTEA NOT NULL,
	
	CONSTRAINT fk_butterfly_id FOREIGN KEY (butterfly_id) REFERENCES butterfly (id) ON UPDATE CASCADE ON DELETE NO
ACTION
);

CREATE TABLE iF NOT EXISTS video(
   id SERIAL PRIMARY KEY,
  butterfly_id INT NOT NULL,
  video BYTEA NOT NULL,
	
	CONSTRAINT fk_butterfly_id FOREIGN KEY (butterfly_id) REFERENCES butterfly (id) ON UPDATE CASCADE ON DELETE NO
ACTION
);

CREATE INDEX idx_species_book_species_name ON species_book (species_name);

CREATE INDEX idx_status_species_id ON status (species_id);

CREATE INDEX idx_butterfly_species_id ON butterfly (species_id);
CREATE INDEX idx_butterfly_author_id ON butterfly (author_id);

CREATE INDEX idx_photo_butterfly_id ON photo (butterfly_id);
CREATE INDEX idx_video_butterfly_id ON video (butterfly_id);

