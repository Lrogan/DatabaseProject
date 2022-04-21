	-- Code to build the normalized tables of the database
    
    DROP DATABASE IF EXISTS `Library Management System`;
    CREATE DATABASE `Library Management System`;
    USE `Library Management System`;
    
    CREATE TABLE Librarian (
		Staff_ID VARCHAR(30) NOT NULL,
        fname VARCHAR(30), 
        lname VARCHAR(30), 
        Salary FLOAT(5,2) NOT NULL,
        Hours INT(3) DEFAULT 0,
        DateOFBirth DATE,
        Email VARCHAR (26),
        Passwords VARCHAR (26),
        Sex CHAR (1),
        
        PRIMARY KEY (Staff_ID)
    );
    
    CREATE TABLE Reader (
		Reader_ID VARCHAR(30) NOT NULL,
        fname VARCHAR(30), 
        lname VARCHAR(30),
        DateOFBirth DATE,
        Email VARCHAR (26),
        Passwords VARCHAR (26),
        Sex CHAR (1),
        
        PRIMARY KEY (Reader_ID)
    );  
    
     CREATE TABLE Book (
		ISBN VARCHAR(13) NOT NULL,
        Publisher VARCHAR(100),
        PublisherDate DATE,
        Title VARCHAR (40),
        Genre VARCHAR (40),
        AgeRating INT(3),
        PageCount INT(4), 
        Copies INT (2), 
        
        PRIMARY KEY (ISBN) 
    );
    
    CREATE TABLE CheckedOut (
		Reader_ID VARCHAR(30),
        ISBN VARCHAR(13), 
        DueDate DATE, 
        DailyFee INT(2),
        
        PRIMARY KEY (READER_ID, ISBN),
        
        FOREIGN KEY (Reader_ID) REFERENCES Reader(Reader_ID)
			ON UPDATE Cascade, 
        FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
			ON UPDATE Cascade 
	
     );  
     
     CREATE TABLE Author (
		Author_ID VARCHAR(30) NOT NULL,
        fname VARCHAR(20), 
        lname VARCHAR(20),  
        
        PRIMARY KEY (Author_ID)
        ); 
        
	CREATE TABLE Writes (
		Author_ID VARCHAR(30) ,
		ISBN varchar(13) ,
        
        PRIMARY KEY (Author_ID, ISBN), 
        FOREIGN KEY (Author_ID) REFERENCES Author(Author_ID) 
			ON DELETE Cascade 
            ON UPDATE Cascade, 
		FOREIGN KEY (ISBN) REFERENCES Book(ISBN) 
			ON DELETE Cascade 
            ON UPDATE Cascade 
        ); 
        
	CREATE TABLE Adds (
		Staff_ID VARCHAR(30) ,
		ISBN VARCHAR(13) ,
        
        PRIMARY KEY (Staff_ID, ISBN), 
        FOREIGN KEY (Staff_ID) REFERENCES Librarian(Staff_ID) 
			ON DELETE Cascade 
            ON UPDATE Cascade, 
		FOREIGN KEY (ISBN) REFERENCES Book(ISBN) 
			ON DELETE Cascade 
            ON UPDATE Cascade 
        ); 
    

           
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    