### 175. Combine Two Tables

---

table: `Person`

``` bash
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
```

table: `Address`

``` bash
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
```

Q. Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

``` bash
FirstName, LastName, City, State
```



A.

``` mysql
SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person as p left join Address as a ON p.PersonId = a.PersonId;
```

