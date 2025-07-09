--Are you ready to begin the Formula 1 Database Challenge? 

--1. List all Constructors:

--- Retrieve the names of all constructors.

SELECT DISTINCT Name
FROM [ITOL_SQL].[dbo].[constructors]

--2. Find All Drivers:

--- List the names of all drivers in the dataset.

SELECT GivenName, FamilyName
FROM [ITOL_SQL].[dbo].[drivers]

--3. Count the Number of Constructors:

--- How many constructors are there in the dataset?

SELECT COUNT(DISTINCT constructorId)
FROM [ITOL_SQL].[DBO].[constructors]

--4. Count the Number of Drivers:

--- How many drivers are there in the dataset?

SELECT COUNT(driverId)
FROM [ITOL_SQL].[DBO].[drivers]

--5. List All Races for a Specific Season:

--- Retrieve all races that took place in the 2020 season.

SELECT DISTINCT Round, CircuitID
FROM [ITOL_SQL].[DBO].[results_history]
WHERE Season = 2020

--6. Basic SELECT:

--- Retrieve the `Name` and `Nationality` of all constructors.

SELECT Name, Nationality
FROM [ITOL_SQL].[DBO].[constructors]

--7. SELECT with Aliases:

--- Retrieve driver `GivenName` and `FamilyName` and alias them as `FirstName` and `LastName`.

SELECT GivenName AS FirstName, FamilyName AS LastName
FROM [ITOL_SQL].[DBO].[drivers]

--8. SELECT Distinct Values:

--- Retrieve distinct nationalities of drivers from the `drivers` table.

SELECT DISTINCT Nationality
FROM [ITOL_SQL].[DBO].[drivers]

--9. SELECT with Calculated Columns:

--- Retrieve the `Position` and `Points` of drivers, and calculate their `PointsPerPosition` (Points divided by Position).

SELECT Position, Points, Cast(Round((Points / Position), 2) AS numeric(4, 2)) AS PointsPerPosition
FROM [ITOL_SQL].[DBO].[driver_standings]

--10. SELECT with Concatenation:

--- Retrieve driver `GivenName` and `FamilyName` concatenated into a single column named `FullName`.

SELECT CONCAT(GivenName, ' ', FamilyName) AS FullName
FROM [ITOL_SQL].[DBO].[drivers]

--11. Basic Filtering:

--- Retrieve all races where the `Season` is 2022.

SELECT *
FROM [ITOL_SQL].[DBO].[results]
WHERE Season = 2022

--12. Filtering with Multiple Conditions:

--- Retrieve drivers who are either `German` or `British`.

SELECT *
FROM [ITOL_SQL].[DBO].[drivers]
WHERE Nationality IN ('German', 'British');

--13. Filtering with LIKE:

--- Retrieve all constructors whose name contains 'Ferrari'.

SELECT *
FROM [ITOL_SQL].[DBO].[constructors]
WHERE Name LIKE '%Ferrari%'

--14. Filtering with IN:

--- Retrieve all results where the `ConstructorName` is either 'ferrari' or 'williams'.

SELECT *
FROM [ITOL_SQL].[DBO].[results]
WHERE ConstructorName IN ('ferrari', 'williams')

--15. Filtering with Date:

--- Retrieve all drivers who were born before 2000.

SELECT *
FROM [ITOL_SQL].[DBO].[drivers]
WHERE YEAR(DateOfBirth) < 2000

--16. Basic Sorting:

--- Retrieve all races sorted by `Season` in ascending order.

SELECT *
FROM [ITOL_SQL].[DBO].[results]
ORDER BY Season ASC

--17. Sorting with Multiple Columns:

--- Retrieve all drivers sorted first by `Nationality` and then by `GivenName`.

SELECT *
FROM [ITOL_SQL].[DBO].[drivers]
ORDER BY Nationality, GivenName

--18. Descending Order:

--- Retrieve all results sorted by `Points` in descending order.

SELECT *
FROM [ITOL_SQL].[DBO].[results]
ORDER BY Points DESC

--19. Sorting with NULLs:

--- Retrieve all drivers and sort by `DateOfBirth`, placing NULL values last.

SELECT *
FROM [ITOL_SQL].[DBO].[drivers]
ORDER BY  DateOfBirth ASC

--20. Top N Results:

--- Retrieve the top 5 drivers with the highest `Points` in the 2020 season.

SELECT
    DISTINCT TOP 5 driverId,
    MAX(points) AS Final_Points
FROM 
    [ITOL_SQL].[DBO].[driver_standings]
GROUP BY 
    driverId
ORDER BY Final_Points DESC

--21. Basic LIMIT:

--- Retrieve the first 10 constructors from the `constructors` table.

SELECT TOP 10 *
FROM [ITOL_SQL].[DBO].[constructors]

--22. LIMIT with OFFSET:

--- Retrieve 10 drivers starting from the 11th driver in the list.

SELECT *
FROM [ITOL_SQL].[DBO].[drivers]
ORDER BY GivenName, FamilyName
OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY

--23. Top N Results with OFFSET:

--- Retrieve the next 10 drivers after the top 5 drivers with the most `Points` in the 2021 season.

SELECT *
FROM [ITOL_SQL].[DBO].[results] 
WHERE Season = 2021
ORDER BY Points DESC
OFFSET 5 ROWS FETCH NEXT 10 ROWS ONLY

--24. LIMIT without ORDER BY:

--- Retrieve the first 5 results of the 2020 season without specifying the order.

SELECT *
FROM [ITOL_SQL].[DBO].[results]
WHERE Season = 2020
ORDER BY (SELECT NULL) -- Dummy ORDER BY which does nothing but is needed in order for OFFSet and FETCH to be used
OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY

--25. Pagination:

--- Retrieve drivers for the 2020 season, showing results 11 through 20.

SELECT *
FROM [ITOL_SQL].[DBO].[results]
WHERE Season = 2020
ORDER BY (SELECT NULL) -- Dummy ORDER BY which does nothing but is needed in order for OFFSet and FETCH to be used
OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY

--26. SUM Function:

--- Calculate the total `Points` scored in the 2024 season.

SELECT SUM(Points) AS TOTAL_POINTS
FROM [ITOL_SQL].[DBO].[results]
WHERE Season = 2024

--27. AVG Function:

--- Calculate the average `Points` scored by drivers in the 2000 season.

SELECT CAST(AVG(Points) AS numeric(4,2)) AS AVERAGE_POINTS
FROM [ITOL_SQL].[DBO].[results]
WHERE Season = 2020

--28. MAX and MIN Functions:

--- Find the maximum and minimum `Points` scored by a driver in the 2021 season.

SELECT MAX(Points) AS MaxPoints, MIN(Points) AS MinPoints
FROM [ITOL_SQL].[DBO].[results]
WHERE Season = 2021;

--29. COUNT Function:

--- Count the number of races in the 2000 season.

SELECT COUNT(DISTINCT CircuitID) as Race_Count
FROM [ITOL_SQL].[DBO].[results]
WHERE Season = 2000;

--30. GROUP_CONCAT Function:

--- List all drivers in each constructor, concatenated into a single column.

SELECT results.ConstructorName,
       GROUP_CONCAT(
       DISTINCT CONCAT(driver.GivenName, ' ', driver.FamilyName) 
       ORDER BY driver.FamilyName ASC
       ) 
       AS Drivers
FROM [ITOL_SQL].[DBO].[results] results
JOIN [ITOL_SQL].[DBO].[drivers] driver ON results.driverId = driver.driverId
GROUP BY results.ConstructorName;

--31. Basic GROUP BY:

--- Retrieve the total `Points` scored by each constructor in the 2000 season.

SELECT ConstructorName, SUM(Points) AS TOTAL_POINTS
FROM [ITOL_SQL].[DBO].[results]
WHERE Season = 2000
GROUP BY ConstructorName

--32. GROUP BY with HAVING:

--- Retrieve constructors that have more than 20 `Points` in the 2002 season.

SELECT ConstructorName, SUM(Points) AS TOTAL_POINTS
FROM [ITOL_SQL].[DBO].[results]
WHERE Season = 2000
GROUP BY ConstructorName
HAVING SUM(Points) > 20

--33. COUNT with GROUP BY:

--- Count the number of races each constructor participated in during 2020.

SELECT ConstructorName, COUNT(ConstructorName) AS TOTAL_RACES
FROM [ITOL_SQL].[DBO].[results]
WHERE Season = 2020
GROUP BY ConstructorName

--34. SUM with GROUP BY:

--- Calculate the total `Points` for each driver, grouped by `Nationality`.

SELECT d.Nationality, d.GivenName, d.FamilyName, SUM(r.Points) AS TotalPoints
FROM [ITOL_SQL].[DBO].[results] r
JOIN [ITOL_SQL].[DBO].[drivers] d ON r.DriverID = d.DriverID
GROUP BY d.Nationality, d.GivenName, d.FamilyName;

--35. GROUP BY with Multiple Columns:

--- Retrieve the average `Points` for each constructor and season combination.

SELECT Season, ConstructorName, AVG(Points) AS Average_Points
FROM [ITOL_SQL].[DBO].[results]
GROUP BY Season, ConstructorName
ORDER BY Season ASC, Average_Points DESC

--36. Inner Join:

--- Retrieve driver names and their corresponding constructor names for races in the 2000 season.

SELECT DISTINCT driver.GivenName, driver.FamilyName, results.ConstructorName
FROM [ITOL_SQL].[DBO].[results] results
INNER JOIN [ITOL_SQL].[DBO].[drivers] driver ON results.DriverID = driver.DriverID
WHERE results.Season = 2000;

--37. Left Join:

--- Retrieve all constructors and any drivers who raced for theM(include constructors with no drivers).

SELECT constructor.constructorId, driver.GivenName, driver.FamilyName
FROM [ITOL_SQL].[DBO].[constructors] constructor
LEFT JOIN [ITOL_SQL].[DBO].[results] results ON constructor.constructorId = results.ConstructorName 
LEFT JOIN [ITOL_SQL].[DBO].[drivers] driver ON results.DriverID = driver.DriverID
GROUP BY constructor.constructorId, driver.GivenName, driver.FamilyName;

--38. Right Join:

--- Retrieve all results and the corresponding drivers for each result, including results with no drivers.

SELECT results.Season, results.Round, results.CircuitID, driver.GivenName, driver.FamilyName
FROM [ITOL_SQL].[DBO].[results] results
RIGHT JOIN [ITOL_SQL].[DBO].[drivers] driver ON results.DriverID = driver.DriverID;

--39. Left Join:

--- Retrieve a list of all drivers and their corresponding results, including drivers who have not participated in any races.

SELECT driver.GivenName, driver.FamilyName, results.Position, results.Points
FROM [ITOL_SQL].[DBO].[drivers] driver
LEFT JOIN [ITOL_SQL].[DBO].[results] results ON driver.DriverID = results.DriverID
ORDER BY driver.GivenName, driver.FamilyName;

--40. Join with Multiple Tables:

--- Retrieve the GivenName, FamilyName, and ConstructorName for each driver, along with their total Points earned in the 2000 season.

SELECT driver.GivenName, driver.FamilyName, constructor.Name, SUM(results.Points) AS TotalPoints
FROM [ITOL_SQL].[DBO].[drivers] driver
JOIN [ITOL_SQL].[DBO].[results] results ON driver.DriverID = results.DriverID
JOIN [ITOL_SQL].[DBO].[constructors] constructor ON results.ConstructorName = constructor.ConstructorID
WHERE results.Season = 2000
GROUP BY driver.GivenName, driver.FamilyName, constructor.Name;

--41. Simple Subquery:

--- Retrieve drivers who have more points than the driver with the least points in the 2000 season.

SELECT driver.GivenName, driver.FamilyName, SUM(results.Points) AS TotalPoints
FROM [ITOL_SQL].[DBO].[drivers] driver
JOIN [ITOL_SQL].[DBO].[results] results ON driver.DriverID = results.DriverID
WHERE results.Season = 2000
GROUP BY driver.DriverID, driver.GivenName, driver.FamilyName
HAVING SUM(results.Points) > (
  SELECT MIN(TotalPoints)
  FROM (
    SELECT SUM(results.Points) AS TotalPoints
    FROM [ITOL_SQL].[DBO].[results] results
    WHERE results.Season = 2000
    GROUP BY results.DriverID
  ) AS DriverTotals
);

--42. Subquery in SELECT:

--- Retrieve the `GivenName` and `FamilyName` of drivers along with their highest `Points` in any race.

SELECT driver.GivenName, driver.FamilyName,
       (SELECT MAX(results.Points)
        FROM [ITOL_SQL].[DBO].[results] results
        WHERE results.DriverID = driver.DriverID) AS HighestPoints
FROM [ITOL_SQL].[DBO].[drivers] driver
ORDER BY HighestPoints DESC

--43. Correlated Subquery:

--- Retrieve constructors and their drivers where the driver�s `Points` is greater than the average `Points` for that constructor.

SELECT distinct
    constructor.Name, 
    driver.GivenName,          
    driver.FamilyName,         
    AVG(results.Points) AS Average_driver_points         
FROM 
    [ITOL_SQL].[DBO].[constructors] constructor
JOIN 
    [ITOL_SQL].[DBO].[results] results ON constructor.Name = results.ConstructorName
JOIN 
    [ITOL_SQL].[DBO].[drivers] driver ON results.DriverID = driver.DriverID
WHERE 
    results.Points > (
        SELECT AVG(results2.Points)
        FROM [ITOL_SQL].[DBO].[results] results2
        WHERE results2.ConstructorName = constructor.Name
        GROUP BY results2.ConstructorName
    )
GROUP BY constructor.Name, driver.GivenName, driver.FamilyName
ORDER BY constructor.Name desc, Average_driver_points desc

-- SELECT distinct
--     constructor.Name, 
--     driver.GivenName,          
--     driver.FamilyName,         
--     results.Points           
-- FROM 
--     [ITOL_SQL].[DBO].[constructors] constructor
-- JOIN 
--     [ITOL_SQL].[DBO].[results] results ON constructor.Name = results.ConstructorName
-- JOIN 
--     [ITOL_SQL].[DBO].[drivers] driver ON results.DriverID = driver.DriverID
-- WHERE 
--     results.Points > (
--         SELECT AVG(results2.Points)
--         FROM [ITOL_SQL].[DBO].[results] results2
--         WHERE results2.ConstructorName = constructor.Name
--         GROUP BY results2.ConstructorName
--     )

--44. Simple CTE

--- Retrieve the average points scored per driver in the 2000 season. Use a CTE to first calculate the total points scored by each driver, and then calculate the average from this aggregated data.

WITH DriverTotalPoints AS (
    SELECT 
        driver.DriverID, 
        driver.GivenName, 
        driver.FamilyName, 
        SUM(results.Points) AS TotalPoints
    FROM 
        [ITOL_SQL].[DBO].[drivers] driver
    JOIN 
        [ITOL_SQL].[DBO].[results] results ON driver.DriverID = results.DriverID
    WHERE 
        results.Season = 2000
    GROUP BY 
        driver.DriverID, driver.GivenName, driver.FamilyName
)
SELECT GivenName, 
    FamilyName, 
    TotalPoints,
    (SELECT AVG(TotalPoints) FROM DriverTotalPoints) AS AveragePoints
FROM 
    DriverTotalPoints;

--45. Complex CTE

--- Retrieve drivers who have finished in the top 3 positions in more than 5 races in the 2000 season, along with their average points per race.

WITH Top3Races AS (
    SELECT 
        results.DriverID, 
        COUNT(*) AS Top3Count
    FROM 
        [ITOL_SQL].[DBO].[results]
    WHERE 
        results.Season = 2000 AND results.Position <= 3
    GROUP BY 
        results.DriverID
    HAVING 
        COUNT(*) > 5
),
DriverPoints AS (
    SELECT 
        driver.DriverID, 
        driver.GivenName, 
        driver.FamilyName, 
        AVG(results.Points) AS AvgPointsPerRace
    FROM 
        [ITOL_SQL].[DBO].[drivers] driver
    JOIN 
        [ITOL_SQL].[DBO].[results] results ON driver.DriverID = results.DriverID
    WHERE 
        results.Season = 2000
    GROUP BY 
        driver.DriverID, driver.GivenName, driver.FamilyName
)
SELECT 
    dp.GivenName, 
    dp.FamilyName, 
    dp.AvgPointsPerRace
FROM 
    Top3Races tr
JOIN 
    DriverPoints dp ON tr.DriverID = dp.DriverID;