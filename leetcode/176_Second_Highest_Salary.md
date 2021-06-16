### 176. Second Highest Salary

---

Q. Write a SQL query to get the second highest salary from the `Employee` table.

``` mysql
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```

For example, given the above Employee table, the query should return `200` as the second highest salary. If there is no second highest salary, then the query should return `null`.

``` mysql
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```



A. 

``` mysql
# Write your MySQL query statement below
SELECT MAX(Salary) as SecondHighestSalary
FROM Employee 
WHERE Salary NOT IN (SELECT MAX(Salary) as SecondHighestSalary FROM Employee);
```

