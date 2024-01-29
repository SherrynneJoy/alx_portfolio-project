-- Create Vendor table
CREATE TABLE IF NOT EXISTS `Vendor` (
 `VendorID`   int NOT NULL AUTO_INCREMENT,
 `VendorName` varchar(255) NOT NULL,
 `Email`      varchar(255) NOT NULL,
 PRIMARY KEY (`VendorID`)
);
