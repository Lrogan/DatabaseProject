-- insert initial data to database to populate the database 
USE `Library Management System`;
 -- inserting initial librarian data 
INSERT INTO Librarian 
VALUES (00000000000, 'Tony', 'Chen', 10.00, 100, '2000-12-09', 'j@gmail.com','password', 'M');

INSERT INTO Librarian 
VALUES (1, 'Mit', 'Patel', 20.00, 40, '2000-8-09', 'k@gmail.com','password', 'M');

INSERT INTO Librarian 
VALUES (2,  'Amy', 'Joseph',20.00, 40, '2000-8-09', 'l@gmail.com','password', 'F');


-- inserting initial reader data 
INSERT INTO Reader 
VALUES (0,'Chris', 'Rock', '1999-04-30',  'm@gmail.com', 'pawword', 'M'); 

INSERT INTO Reader 
VALUES (1,'Sreyleak', 'Le', '1939-04-30',  'n@gmail.com', 'pawword', 'F');

INSERT INTO Reader 
VALUES (2, 'Priyanka', 'Ganesan','1899-04-30',  'o@gmail.com', 'adfljk12', 'F');


-- inserting intial book data
INSERT INTO Book 
VALUES (1234567892314, 'Jim', '1939-04-30', 'Intro to Calculus', 'Education', 10, 300, 1);

INSERT INTO Book 
VALUES (2234567232314, 'Bob', '1939-04-30', 'Harry Potter', 'Fantasy', 13, 100, 1);

INSERT INTO Book 
VALUES (3223567232314, 'Mary', '1939-04-30', 'Ranger\'s Apprentice', 'Fantasy', 18, 220, 1); 

-- inserting intial Checked out books data
INSERT INTO CheckedOut 
VALUES (1, 1234567892314, '2022-07-14', 10);

INSERT INTO CheckedOut 
VALUES (1, 2234567232314, '2022-07-14', 10);


INSERT INTO Author 
VALUES (0, 'Jim', 'Grey'), (1, 'Will', 'Smith'), (2, 'Anthony', 'Chen');

INSERT INTO Writes 
VALUES (0, 1234567892314), (0, 2234567232314), (2, 3223567232314);  

INSERT INTO Adds 
VALUES (0, 1234567892314), (0, 2234567232314), (0, 3223567232314); 

INSERT INTO Book 
VALUES (4234567232314, 'Bill', '1922-04-30', 'Intro to Database', 'Education', 13, 140, 4), (5234545232314, 'Amy', '2020-04-30', 'History of Michael Jordan', 'Sports', 10, 50, 2), (6234545232314, 'Julio', '2022-03-15', 'Garfield', 'Comedy', 5, 40, 1);

INSERT INTO CheckedOut 
VALUES (0, 4234567232314, '2022-03-14', 10), (0, 5234545232314, '2022-03-14', 10), (1, 4234567232314, '2022-07-14', 10); 
INSERT INTO Writes 
VALUES (0, 3223567232314), (0, 4234567232314), (2, 5234545232314), (0, 6234545232314), (2, 6234545232314); 

SELECT * 
FROM Librarian ;

SELECT * 
FROM Reader;

SELECT * 
FROM Book; 

SELECT * 
FROM CheckedOut;

SELECT * 
FROM Author;

SELECT * 
FROM Writes;

SELECT * 
FROM Adds;  