-- Create Cart table
CREATE TABLE IF NOT EXISTS `Cart` (
 `CartID`    int NOT NULL AUTO_INCREMENT,
 `UserID`    int NOT NULL,
 `ProductID` int NOT NULL,
 `Quantity`  int NOT NULL,
 PRIMARY KEY (`CartID`),
 FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`)
);
