-- Create Product table
CREATE TABLE IF NOT EXISTS `Product` (
 `ProductID`   int NOT NULL AUTO_INCREMENT,
 `Title`       varchar(255) NOT NULL,
 `Description` varchar(255) NOT NULL,
 `Price`       decimal(10, 2) NOT NULL,
 `VendorID`    int NOT NULL,
 PRIMARY KEY (`ProductID`),
 FOREIGN KEY (`VendorID`) REFERENCES `Vendor` (`VendorID`)
);

