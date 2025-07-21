--Lesson 1
--Creating Tables

--Lesson 2
-- Altering Tables:

-- - Add a column to the Employees table to store phone numbers.
-- - Make sure that every department has a name by including a NOT NULL constraint on the DepartmentName column.
-- - Rename the HireDate column in the Employees table to StartDate.
-- - Remove the Department column from the Employees table, as it is redundant.
USE ITOL_SQL

ALTER TABLE [techNova].[Employees]
ADD PhoneNumber VARCHAR(15);

ALTER TABLE [techNova].[Departments]
ALTER COLUMN DepartmentName VARCHAR(100) NOT NULL;

--ALTER TABLE [techNova].[Employees]
EXEC sp_rename '[techNova].[Employees].HireDate',  'StartDate', 'COLUMN';
--RENAME COLUMN HireDate to StartDate;

ALTER TABLE [techNova].[Employees]
DROP COLUMN Department;


--Lesson 3
-- Dropping Tables:

-- - Drop the Departments table entirely from the database.
-- - Create a temporary table named TempProjects for testing purposes and then drop it.
-- - Write a script to drop the Employees table only if it exists.
USE ITOL_SQL

DROP TABLE IF EXISTS [techNova].[Departments];
--IMPORTANT - temp tables have to have # infront of their name
CREATE TABLE #TempProjects (
    TempID INT PRIMARY KEY,
    TempName VARCHAR(50)
);
DROP TABLE #TempProjects;
--DROP TABLE IF EXISTS [techNova].[Employees];


--Lesson 4
-- Constraints:

-- - Make sure each task assignment is linked to a specific employee and project by creating a TaskAssignments table with appropriate primary and foreign keys.
-- - Add a unique constraint to the Email column in the Employees table to prevent duplicate email addresses.
-- - Make sure that every project must have an end-date by setting a NOT NULL constraint on the EndDate column in the Projects table.
CREATE TABLE [techNova].[TaskAssignments] (
    TaskID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT,
    ProjectID INT,
    FOREIGN KEY (EmployeeID) REFERENCES [techNova].[Employees](EmployeeID),
    FOREIGN KEY (ProjectID) REFERENCES [techNova].[Projects](ProjectID)
);
ALTER TABLE [techNova].[Employees]
ADD CONSTRAINT unique_email UNIQUE (Email);
ALTER TABLE [techNova].[Projects]
ALTER COLUMN EndDate DATE NOT NULL;


-- Lesson 5 
-- Indexes:

-- - Create an index on the Email column in the Employees table to speed up email searches.
-- - Create a composite index on the LastName and FirstName columns in the Employees table to improve full name searches.
-- - Drop the index on the Email column if it is no longer needed.
CREATE INDEX idx_email ON [techNova].[Employees](Email);
CREATE INDEX idx_fullname ON [techNova].[Employees](LastName, FirstName);
DROP INDEX idx_email ON [techNova].[Employees];