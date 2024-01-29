-- Create Order table
CREATE TABLE IF NOT EXISTS `Order` (
 `OrderID`    int NOT NULL AUTO_INCREMENT,
 `UserID`     int NOT NULL,
 `TotalAmount` decimal(10, 2) NOT NULL,
 `OrderDate`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
 PRIMARY KEY (`OrderID`),
 FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`)
);
