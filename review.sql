-- Create Review table
CREATE TABLE IF NOT EXISTS `Review` (
 `ReviewID`  int NOT NULL AUTO_INCREMENT,
 `UserID`    int NOT NULL,
 `ProductID` int NOT NULL,
 `Rating`    int NOT NULL,
 `Comment`   varchar(5000) NOT NULL,
 PRIMARY KEY (`ReviewID`)
);
