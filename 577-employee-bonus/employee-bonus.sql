/* Write your PL/SQL query statement below */
select Employee.name, Bonus.bonus from Employee left join Bonus on Employee.empId = Bonus.empId WHERE Bonus.bonus<1000 or Bonus.bonus IS NULL; 