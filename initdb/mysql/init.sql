CREATE DATABASE IF NOT EXISTS genealogy;
USE genealogy;

CREATE TABLE IF NOT EXISTS family (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name nvarchar(255) NOT NULL,
    chief_person_id int NOT NULL,
    join_family_id int
);

CREATE TABLE IF NOT EXISTS person (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name nvarchar(255) NOT NULL,
    dob date NOT NULL,
    family_id int,
    gender int,
    join_person_id int,
    FOREIGN KEY (family_id) REFERENCES family(id),
    FOREIGN KEY (join_person_id) REFERENCES person(id)
);

CREATE TABLE IF NOT EXISTS relationship_type (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name nvarchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS relationship (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    person_1_id int,
    person_2_id int,
    type int,
    FOREIGN KEY (person_1_id) REFERENCES person(id),
    FOREIGN KEY (person_2_id) REFERENCES person(id),
    FOREIGN KEY (type) REFERENCES relationship_type(id)
);
