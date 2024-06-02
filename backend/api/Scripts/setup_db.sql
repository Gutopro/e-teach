-- Run this script to setup a database environment for eduTech locally
-- This script works for MySQL
-- To run => mysql -u root -p < setup_db.sql

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS e_teach;

-- Create the user if it doesn't exist and set the password
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY '@new_password';

-- Grant all privileges on the "edutech" database to the user
GRANT ALL PRIVILEGES ON e_teach.* TO 'admin'@'localhost';

-- Apply the privileges
FLUSH PRIVILEGES;
