CREATE DATABASE IF NOT EXISTS z_cars2;

USE z_cars2;

CREATE TABLE cars (
    id integer not null auto_increment,
    brand varchar(100),
    model varchar(100),
    year integer,
    PRIMARY KEY (id)
);

INSERT INTO cars (brand, model, year)
VALUES
('Mitsubishi', 'Pajero', 2011),
('Volkswagen', 'Amarok', 2020),
('Dodge', 'Ram', 2018),
('Ford', 'Ranger', 2017),
('Chevrolet', 'S10', 2020);