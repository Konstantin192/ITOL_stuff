-- Lesson 1: Creating Views

-- 1. Use the student_management database from the previous module.
USE ITOL_student_management;

-- 2. Create a view named student_overview that shows the id, name, and grade columns from the students table.
CREATE VIEW [greenfield_academy].[student_overview] AS
SELECT id, name, grade
FROM [greenfield_academy].[students];

-- 3. Query the student_overview view to verify it displays the correct data.
SELECT * FROM [greenfield_academy].[student_overview];

-- 4. Modify the view to include a calculated field that shows age categorized as 'Minor' if the age is less than 18, and 'Adult' otherwise.
DROP VIEW IF EXISTS [greenfield_academy].[student_overview];
GO -- IMPORTANT !!! NEED TO HAVE WHEN INCLUDING OTHER STATEMENTS PRIOR TO A CREATE VIEW ONE
CREATE VIEW [greenfield_academy].[student_overview] AS
SELECT 
    id,
    name,
    grade,
    CASE
        WHEN age < 18 THEN 'Minor'
        ELSE 'Adult'
    END AS age_category
FROM [greenfield_academy].[students];
GO
SELECT * FROM [greenfield_academy].[student_overview];


-- Lesson 2: Stored Procedures

-- 1. Create a stored procedure named add_student that takes the name, age, and grade as parameters and inserts a new record into the students table.
GO
CREATE PROCEDURE [greenfield_academy].[add_student] @student_name VARCHAR(50), @student_age INT, @student_grade VARCHAR(10)
AS
	BEGIN
		INSERT INTO [greenfield_academy].[students] (name, age, grade) 
		VALUES (@student_name, @student_age, @student_grade);
	END

-- 2. Run the stored procedure to add a new student.
EXEC [greenfield_academy].[add_student] 'Alice Johnson', 17, '12th Grade';

-- 3. Modify the stored procedure to return the id of the newly added student after insertion.
DROP PROCEDURE IF EXISTS [greenfield_academy].[add_student];
GO
CREATE PROCEDURE [greenfield_academy].[add_student] @student_name VARCHAR(50), @student_age INT, @student_grade VARCHAR(10) --, @new_student_id INT OUTPUT
AS
	BEGIN
		INSERT INTO [greenfield_academy].[students] (name, age, grade) 
		VALUES (@student_name, @student_age, @student_grade);
    
		DECLARE @new_student_id int;
		SET @new_student_id = (SELECT SCOPE_IDENTITY());
		SELECT @new_student_id
	END

-- 4. Verify that the stored procedure works as expected.
EXEC [greenfield_academy].[add_student] 'Bob Smith', 16, '11th Grade'--, @new_student_id = @student_id OUTPUT;


-- Lesson 3: User-Defined Functions

-- 1. Create a user-defined function named calculate_discount that takes a price and a discount percentage as input and returns the discounted price.

CREATE FUNCTION calculate_discount(@price DECIMAL(10,2), @discount_percent DECIMAL(5,2))
RETURNS DECIMAL(10,2)
AS
BEGIN
    RETURN @price - (@price * @discount_percent / 100);
END;
GO


-- 2. Write a query to test the function by calculating the discounted price for an item with a price of 100 and a discount of 15%.
SELECT dbo.calculate_discount(100, 15) AS discounted_price;