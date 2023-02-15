CREATE DATABASE IF NOT EXISTS genealogy;
USE genealogy;

CREATE TABLE IF NOT EXISTS family (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name nvarchar(255) NOT NULL,
    chief_person_id int NOT NULL,
    join_family_id int,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS person (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name nvarchar(255) NOT NULL,
    family_id int,
    gender int,
    join_person_id int,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (family_id) REFERENCES family(id),
    FOREIGN KEY (join_person_id) REFERENCES person(id)
);

CREATE TABLE IF NOT EXISTS relationship_type (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name nvarchar(255) NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS relationship (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    person_1_id int,
    person_2_id int,
    type int,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (person_1_id) REFERENCES person(id),
    FOREIGN KEY (person_2_id) REFERENCES person(id),
    FOREIGN KEY (type) REFERENCES relationship_type(id)
);

INSERT INTO person(name) VALUES ('Phạm Hữu Thiên');
INSERT INTO person(name) VALUES ('Trần Cung Bắc');
INSERT INTO person(name) VALUES ('Trực Sang Huê');

INSERT INTO family (name, chief_person_id) VALUES ('Phạm', 1);
INSERT INTO family (name, chief_person_id) VALUES ('Trần', 2);
INSERT INTO family (name, chief_person_id) VALUES ('Trực', 3);