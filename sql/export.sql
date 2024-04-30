+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MusicDiscoverySystem
                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CREATE TABLE account (Username varchar(255) NOT NULL,Password varchar(255),Email varchar(255),Phone_Number bigint,Artist varchar(255));                                                                     |
| CREATE TABLE album (Album_ID int NOT NULL auto_increment,Artist_Username varchar(100),Title varchar(255),Star_Rating int,Year int);                                                                         |
| CREATE TABLE artist (Artist_ID int NOT NULL auto_increment,Account varchar(255),Name varchar(255),Social_Media_Links text);                                                                                 |
| CREATE TABLE listener (PhoneNumber bigint,Account_name varchar(50) NOT NULL,Full_Name varchar(255) NOT NULL);
                                                                                      |
| CREATE TABLE playlist (Playlist_ID int NOT NULL auto_increment,PhoneNumber bigint,Playlist_Name varchar(100),Star_Rating int,Playlist_Length int,Playlist_Runtime int,Visibility enum('private','global')); |
| CREATE TABLE song (Song_ID int NOT NULL auto_increment,Artist int,Genre varchar(50),Title varchar(255),Star_Rating int,Runtime decimal(5,2));                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+