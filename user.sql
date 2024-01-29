-- Create User table
CREATE TABLE IF NOT EXISTS `User` (
 `UserID`   int NOT NULL AUTO_INCREMENT,
 `Username` varchar(255) NOT NULL UNIQUE,
 `Email`    varchar(255) NOT NULL UNIQUE,
 `Password` varchar(255) NOT NULL,
 PRIMARY KEY (`UserID`)
);
