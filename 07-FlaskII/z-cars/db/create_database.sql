CREATE DATABASE IF NOT EXISTS z_cars;

USE z_cars;

CREATE TABLE cars (
    id integer not null auto_increment,
    brand varchar(100),
    model varchar(100),
    year integer,
    PRIMARY KEY (id)
);

INSERT INTO cars (brand, model, year) VALUES ('Gurgel', 'Carajas', 1986);
INSERT INTO cars (brand, model, year) VALUES ('Gurgel', 'BR800 SL', 1991);
INSERT INTO cars (brand, model, year) VALUES ('Fiat', '147', 1983);
