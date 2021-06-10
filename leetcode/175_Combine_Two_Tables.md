### 175. Combine Two Tables

---

``` mysql
SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person as p left join Address as a ON p.PersonId = a.PersonId;
```

