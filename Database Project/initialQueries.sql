	-- Code to run quieries on the database 
    USE `Library Management System`;


-- Getting the number of librarians working part time (Assumption that part time is less than 32 hours)
SELECT COUNT(*) 
FROM Librarian
WHERE hours < 32;  


-- Getting the number of librarians working full time (Assumption that part time is greater than 32 hours)
SELECT COUNT(*) 
FROM Librarian
WHERE hours >= 32; 

-- list of names female librarians 
SELECT fname, lname 
FROM Librarian
WHERE Sex = 'F'; 

-- list of readers with overdue books 
SELECT DISTINCT fname, lname 
FROM reader,checkedOut 
WHERE reader.Reader_ID = checkedOut.Reader_ID and checkedOut.DueDate < CURDATE() ;

-- list of the reader names who have not checked out a book
SELECT fname, lname 
FROM reader
WHERE reader.Reader_ID NOT IN(SELECT checkedOut.Reader_ID 
							  FROM checkedOut);  
                              

-- list of the readers who have checked 2 or more books and number of books checked out 
SELECT fname, lname, COUNT(*)
FROM reader, checkedOut
WHERE reader.Reader_ID = checkedOut.Reader_ID 
GROUP BY fname, lname
HAVING COUNT(*) > 2; 


-- list number of books in the library 
SELECT COUNT(*) 
FROM book; 

 -- list titles, ISBN, and name of book with multiple authors 
 SELECT Title, book.ISBN, COUNT(*)
 FROM book, writes 
 WHERE book.ISBN = writes.ISBN 
 GROUP BY book.ISBN 
 HAVING COUNT(*) > 1 ;  
 
 -- list author names that have not written a book 
 SELECT fname, lname 
 FROM Author
 WHERE Author.Author_ID NOT IN (SELECT Writes.Author_ID 
								FROM Writes);  


 -- list staff that have not added a book 
 SELECT fname, lname 
 FROM Librarian
 WHERE Librarian.Staff_ID NOT IN (SELECT Adds.Staff_ID 
								FROM Adds);  
                                

-- view for staff to see basic reader information 
CREATE VIEW ReaderInfoView 
AS SELECT fname, lname, Title, DueDate, DailyFee 
	FROM Book, Reader, checkedOut
    WHERE Book.ISBN = checkedOut.ISBN and Reader.Reader_ID = checkedOut.Reader_ID; 


-- view for stripped view basic info of books 
CREATE VIEW booksView 
AS SELECT Title, fname, lname, PageCount 
	FROM Book, Author, Writes
    WHERE Book.ISBN = Writes.ISBN and Writes.Author_ID = Author.Author_ID; 


SELECT * 
FROM ReaderInfoView;

SELECT * 
FROM booksView;

SELECT *
FROM CheckedOut;

SELECT fname, lname, COUNT(*)
FROM Reader, CheckedOut
WHERE Reader.reader_ID = CheckedOut.reader_ID
GROUP BY fname, lname
HAVING COUNT(*) > 2;

SELECT Book.Title, Book.ISBN, Author.fname, Author.lname, CheckedOut.DueDate 
FROM Reader, Book, CheckedOut, Writes, Author
WHERE Book.ISBN = CheckedOut.ISBN AND Author.Author_ID = Writes.Author_ID AND Reader.Reader_ID = CheckedOut.Reader_ID AND  Book.ISBN = Writes.ISBN and Reader.Reader_ID;

SELECT Title, book.ISBN, COUNT(*)
FROM book, writes
WHERE book.ISBN = writes.ISBN
GROUP BY book.ISBN
HAVING COUNT(*) > 1;

