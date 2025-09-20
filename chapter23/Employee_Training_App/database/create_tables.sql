/* *************************************************************
   Drop and Create the tables for the employee_training database.
*************************************************************** */

-- Switch to employee_training database
USE `employee_training`

-- Drop the table if it exists
DROP TABLE IF EXISTS `employees`;

-- Create the table
CREATE TABLE IF NOT EXISTS `employees` (
	`id` int(11) NOT NULL,
	`first_name` varchar(25) NOT NULL,
	`middle_name` varchar(25) NOT NULL,
	`last_name` varchar(25) NOT NULL,
	`birthday` varchar(25) NOT NULL,
	`gender` char(1) NOT NULL
);

-- Designate the `id` column as the primary key
ALTER TABLE `employees`
  ADD PRIMARY KEY (`id`);

-- Make `id` column auto increment on inserts
ALTER TABLE `employees`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

-- Drop employee_training table if it exists
DROP TABLE IF EXISTS `employee_training`;

-- Create employee_training table
CREATE TABLE `employee_training` (
	`id` int(11) NOT NULL,
	`employee_id` int(11) NOT NULL,
	`title` varchar(100) NOT NULL,
	`description` varchar(250) NOT NULL,
	`start_date` varchar(25) NOT NULL,
	`end_date` varchar(25) NOT NULL,
	`status` varchar(25) NOT NULL 
);

-- Make employee_training.id column primary key
-- And create an index on the employee_id column
ALTER TABLE `employee_training`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employee_training_ibfk_1` (`employee_id`);

-- Make employee_training.id column Auto Increment
ALTER TABLE `employee_training`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

-- Add Cascade Delete Constraint
ALTER TABLE `employee_training`
  ADD CONSTRAINT `employee_training_ibfk_1` 
  FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
