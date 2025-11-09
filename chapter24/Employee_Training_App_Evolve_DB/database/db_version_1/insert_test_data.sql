/* ******************************************************
   Insert test data into the employee_training database.
********************************************************/

-- Switch to the employee_training database.
USE `employee_training`

-- Insert data into the employees table.
INSERT INTO `employees` (first_name, middle_name, last_name, birthday, gender) 
       VALUES ('Rick', 'Warren', 'Miller', '1976-08-20 00:00:00', 'M');
SET @rick_id = LAST_INSERT_ID();

INSERT INTO `employees` (first_name, middle_name, last_name, birthday, gender) 
       VALUES ('Jose', 'Miguel', 'Pi', '1985-12-01 00:00:00', 'M');
SET @jose_id = LAST_INSERT_ID();



-- Insert data into the courses table.
INSERT INTO `courses` (title, description) 
		values ('Intro to Bash Shell Scripting', 
				'How to script the Bash shell.');
SET @bash_course_id = LAST_INSERT_ID();

INSERT INTO `courses` (title, description) 
		values ('Intro to C Programming', 
				'Introduces student to C programming language fundamentals.');
set @c_course_id = LAST_INSERT_ID();

INSERT INTO `courses` (title, description) 
		values ('Managing Difficult Employees', 
				'How to lead through kindness.');
set @managing_difficult_employees_course_id = LAST_INSERT_ID();

INSERT INTO `courses` (title, description) 
		values ('Database Programming with Python', 
				'How to develop data-driven apps with Python.');
set @database_programming_with_python_course_id = LAST_INSERT_ID();


-- Insert data into the employee_training_xref table.
INSERT INTO `employee_training_xref` (employee_id, course_id, start_date, 
									end_date, status) 
		VALUES(@rick_id, @bash_course_id, '2025-09-15 00:00:00', 
			'2025-09-20 00:00:00', 'Pass');

INSERT INTO `employee_training_xref` (employee_id, course_id, start_date, 
									end_date, status) 
		VALUES(@jose_id, @bash_course_id, '2025-09-15 00:00:00', 
			'2025-09-20 00:00:00', 'Pass');

INSERT INTO `employee_training_xref` (employee_id, course_id, start_date, 
									end_date, status) 
		VALUES(@rick_id, @c_course_id, '2025-11-03 00:00:00', 
			'2025-11-07 00:00:00', 'Pass');

INSERT INTO `employee_training_xref` (employee_id, course_id, start_date, 
									end_date, status) 
		VALUES(@rick_id, @database_programming_with_python_course_id, '2024-01-08 00:00:00', 
			'2024-01-12 00:00:00', 'Pass');

INSERT INTO `employee_training_xref` (employee_id, course_id, start_date, 
									end_date, status) 
		VALUES(@jose_id, @c_course_id, '2025-07-07 00:00:00', 
			'2025-07-11 00:00:00', 'Pass');


