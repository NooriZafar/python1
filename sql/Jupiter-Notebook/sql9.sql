create table Person2(personId int,lastName varchar(30),
firstName varchar(30));

insert into Person2 values(1,'Zafar','Noori'),
(2,'Sahara','Khan');

create table Address(adressId int,personID int,city varchar(30),
state varchar(30));

insert into Address values(1,2,'banglore','karnataka'),
(2,3,'chittoor','AP');


#query to display name city and sate id personid is not present in address tble then report null
select p.firstname, p.lastname, a.city, a.state
from Person2 as p left join Address as a
on p.personId = a.personID;


create table Employee11(id int,name varchar(30),salary int,managerid int);

insert into Employee11 values(1,'noori',60000,3),(2,'suhana',50000,4),
							(3,'sumiya',40000,null),(4,'aliya',50000,null);
 
#employee earning more than manager
SELECT e1.name AS 'Employee'
FROM Employee11 e1
LEFT JOIN
Employee e2
ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;