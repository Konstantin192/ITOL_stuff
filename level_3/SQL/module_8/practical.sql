-- Lesson 1: GRANT Statement

-- 1. Create a new database called student_management.

-- 2. Create two tables in the database:
-- students: Stores information about students (id, name, age, grade).USE student_management;
USE ITOL_student_management

CREATE TABLE [greenfield_academy].[students] (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);

-- teachers: Stores information about teachers (id, name, subject).
CREATE TABLE [greenfield_academy].[teachers] (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(50),
    subject VARCHAR(50)
);

-- 3. Create a user named teacher_user without any initial privileges.
-- IMPORTANT !!!!! - In order for this to work you have to enable SQL server authentication on the server.
-- To do so right click the server, go to Properties -> Security and under Server authentication select the second radio button
CREATE LOGIN teacher_user WITH PASSWORD = 'test_password123';
CREATE USER teacher FOR LOGIN teacher_user

-- 4. Write a query to grant SELECT and INSERT privileges to teacher_user on the students table.
GRANT SELECT, INSERT ON [greenfield_academy].[students] TO teacher;

-- 5. Verify that teacher_user can now select and insert records in the students table but cannot delete or update any records.
EXECUTE AS USER = 'teacher';
SELECT * FROM [greenfield_academy].[students];
INSERT INTO [greenfield_academy].[students] (name, age, grade)
VALUES ('John Doe', 16, '10th Grade');
DELETE FROM [greenfield_academy].[students] WHERE id = 1;
UPDATE [greenfield_academy].[students] SET grade = '11th Grade' WHERE id = 1;
Revert;


-- Lesson 2: REVOKE Statement

-- 1. Use the same database student_management.
USE ITOL_student_management;

-- 2. Create another user called admin_user.
CREATE LOGIN admin_user WITH PASSWORD = 'test_password123';
CREATE USER admin_user FOR LOGIN admin_user;

-- 3. Grant all privileges (SELECT, INSERT, UPDATE, DELETE) on both tables (students and teachers) to admin_user.
GRANT SELECT, INSERT, UPDATE, DELETE ON [greenfield_academy].[students] TO admin_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON [greenfield_academy].[teachers] TO admin_user;

-- 4. Verify that admin_user can perform all operations.
SELECT * FROM [greenfield_academy].[students];
INSERT INTO [greenfield_academy].[students] (name, age, grade)
VALUES ('Jane Smith', 17, '11th Grade');
UPDATE [greenfield_academy].[students] SET grade = '12th Grade' WHERE name = 'Jane Smith';
DELETE FROM [greenfield_academy].[students] WHERE name = 'Jane Smith';

-- 5. Write a query to revoke the DELETE privilege from admin_user on the students table.
REVOKE DELETE ON [greenfield_academy].[students] FROM admin_user;

-- 6. Verify that admin_user can no longer delete records from the students table but can still insert, update, and select records.SELECT * FROM students;
INSERT INTO [greenfield_academy].[students] (name, age, grade)
VALUES ('John Doe', 16, '10th Grade');
UPDATE [greenfield_academy].[students] SET grade = '11th Grade' WHERE name = 'John Doe';
DELETE FROM [greenfield_academy].[students] WHERE name = 'John Doe';



-- Lesson 3: Roles and Privileges

-- 1. Create a new role called student_role and assign it SELECT privileges on the students table.
CREATE ROLE student_role;
GRANT SELECT ON [greenfield_academy].[students] TO student_role;

-- 2. Create a new user student_user and assign them the student_role.
CREATE LOGIN student_user WITH PASSWORD = 'test_password123';
CREATE USER student_user FOR LOGIN student_user;
--GRANT student_role TO student_user;
ALTER ROLE student_role ADD MEMBER student_user;

-- 3. Verify that student_user can only view the records in the students table but cannot make any changes.
EXECUTE AS USER = 'student_user';
SELECT * FROM [greenfield_academy].[students];
INSERT INTO [greenfield_academy].[students] (name, age, grade) VALUES ('Test User', 18, '12th Grade');
UPDATE [greenfield_academy].[students] SET grade = '11th Grade' WHERE name = 'Test User';
DELETE FROM [greenfield_academy].[students] WHERE name = 'Test User';
Revert;

-- 4. Modify the student_role to also include INSERT privileges on the students table.
GRANT INSERT ON [greenfield_academy].[students] TO student_role;

-- 5. Verify that student_user can now insert new records but still cannot delete or update them.
EXECUTE AS USER = 'student_user';
INSERT INTO [greenfield_academy].[students] (name, age, grade)
VALUES ('Test User', 18, '12th Grade');
UPDATE [greenfield_academy].[students] SET grade = '11th Grade' WHERE name = 'Test User';
DELETE FROM [greenfield_academy].[students] WHERE name = 'Test User';
Revert;