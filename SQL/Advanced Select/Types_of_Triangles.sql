-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/revising-the-select-query/problem
-- Difficulty: Easy
-- Max Score: 20
-- DBMS: mySQL
-- Credit : Neel Nikhil Pappu

-- ========================
--         Solution
-- ========================

SELECT
CASE
    WHEN A + B <= C OR A + C <= B OR B + C <= A
        THEN 'Not A Triangle'
    WHEN A = B AND A = C AND B = C
        THEN 'Equilateral'
    WHEN A = B OR A = C OR B = C
        THEN 'Isosceles'
    ELSE 'Scalene'
END
FROM TRIANGLES;
