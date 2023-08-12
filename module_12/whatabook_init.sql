/*
Author: Miguel Juan Lorenzo
Course: CYBR 410 - T302 Data/Database Security
This script defines and creates the structure for the whatabook database.
It also adds entries for the newly created tables
*/

-- Checks for existing database and deletes it so database can be recreated --
DROP DATABASE IF EXISTS whatabook;


-- Create whatabook database
CREATE DATABASE IF NOT EXISTS whatabook;


-- Create user with specified password
CREATE USER IF NOT EXISTS 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';


-- Grant all privileges to whatabook_user for the whatabook database
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';


-- Choose whatabook database --
USE whatabook;


-- Checks for existing tables and deletes them so tables can be recreated --
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;


-- CREATE TABLE statements for user, book, wishlist, and store tables --
CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id)
);
CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);
CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);


-- Create user records --
INSERT INTO user (first_name, last_name) VALUES ('Richard', 'Hendricks');

INSERT INTO user (first_name, last_name) VALUES ('Erlich', 'Bachman');

INSERT INTO user (first_name, last_name) VALUES ('Jian', 'Yang');


-- INSERT statements for book table --
INSERT INTO book(book_name, author, details)
    VALUES('Tom Lake', 'Ann Patchett', 'Three daughters, who return to their family orchard in the spring of 2020, learn about their mother’s relationship with a famous actor.');

INSERT INTO book(book_name, author, details)
    VALUES('Fourth Wing', 'Rebecca Yarros', 'Violet Sorrengail is urged by the commanding general, who also is her mother, to become a candidate for the elite dragon riders.');

INSERT INTO book(book_name, author, details)
    VALUES('American Prometheus', 'Kai Bird and Martin J. Sherwin', 'A biography of J. Robert Oppenheimer. Winner of the Pulitzer Prize in 2006 and an inspiration for the film “Oppenheimer.”');

INSERT INTO book(book_name, author, details)
    VALUES('Outlive', 'Peter Attia with Bill Gifford', 'A look at recent scientific research on aging and longevity.');

INSERT INTO book(book_name, author, details)
    VALUES('The Wager', 'David Grann', 'The survivors of a shipwrecked British vessel on a secret mission during an imperial war with Spain have different accounts of events.');

INSERT INTO book(book_name, author, details)
    VALUES('The Body Keepse The Score', 'Bessel van der Kolk', 'How trauma affects the body and mind, and innovative treatments for recovery.');

INSERT INTO book(book_name, author, details)
    VALUES('Lessons In Chemistry', 'Bonnie Garmus', 'A scientist and single mother living in California in the 1960s becomes a star on a TV cooking show.');

INSERT INTO book(book_name, author, details)
    VALUES('The Covenant of Water', 'Abraham Verghese', 'Three generations of a family living on South India’s Malabar Coast suffer the loss of a family member by drowning.');

INSERT INTO book(book_name, author, details)
    VALUES('Demon Copperhead', 'Barbara Kingsolver', 'Winner of a 2023 Pulitzer Prize for fiction. A reimagining of Charles Dickens’s “David Copperfield” set in the mountains of southern Appalachia.');

-- Create store locale record --
INSERT INTO store (locale) VALUES ('410 Terry Ave N, Seattle, WA 98109, United States');


#Create wishlist entries
INSERT INTO wishlist (user_id, book_id) VALUES (1, 1);
INSERT INTO wishlist (user_id, book_id) VALUES (1, 3);
INSERT INTO wishlist (user_id, book_id) VALUES (1, 5);
