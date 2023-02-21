#creating table
create table employee_1(Name varchar(30),City varchar(30),Age int,Grade char);

#insert values in employee table
insert into employee_1 values("Noori","Delhi",20,"A"),("Sabeeha","Jaipur",21,"A"),
						("Saif","Mumbai",21,"B"),("Zafar","Kolkata",22,"B");

#display the table
select * from employee_1;

#create another table                        
create table employee_2(Name varchar(30),Age int,phone varchar(10),Grade char);

#insert values
insert into employee_2 values("Suhail",20,9063058981,"A"),("Samaira",21,9063058982,"A"),
						("Nayeem",21,9063058983,"B"),("Zafar",22,9063058984,"B");
					
select * from employee_2;
 
#perform intersection of two tables
select name,age from employee_1 where age=22 INTERSECT select name,age from employee_2 where age=22;

#intersection using join
select distinct employee_1.Name,employee_1.Age,employee_2.Grade from employee_1
inner join employee_2 on employee_1.Name=employee_2.Name;
select distinct employee_1.Name,employee_1.Age,employee_2.Grade from employee_1 
join employee_2 on employee_1.Name=employee_2.Name;

#we can't perform minus operation in mysql oracle 
#select Name,Age,Grade from table1 minus select Name,Age,Grade from table2;
select Name from employee_1 left join table2 using(name) where employee_2.name is null;
select employee_1.Name,employee_1.Age,employee_1.Grade from employee_1 
left join employee_2 on employee_1.Name=employee_2.Name where employee_2.name is null;


#perform union operation
select name,age from employee_1 union select name,age from employee_2;

#collect max,min age
select max(age) from employee_1;
select min(age) from employee_1;
select name,age from employee_1 where age=(select (max(age)+min(age))/2 from employee_1);

#we can't perform mod in mysql oracle
select * from employee_1 where mod(name,2)=0;
select * from employee_1 where age%2 <>0;

#display only even rows
select * from(select name ,age,row_number() over(order by name desc) as 'rownumber' from employee_1)
 d where (rownumber%2)=0;
 select * from(select name ,age,row_number() over(order by name) as 'rownumber' from employee_1)
 d where (rownumber%2)=0;
 
 
 #display annual salry
 select * from employee_1;
 select sum(age) from employee_1 where age=21;
 select empname,sum(12*salary) as annualsalary from employee1 group by empname;
 
 #display distinct length of empname
 select distinct name from employee_1 where length(name)>5;
 
 #perfroming operation using in()
 select name,age,Grade from employee_2 where age in(21,22);
 select name,age,Grade from employee_2 where age in(21,22) order by age desc;
 
 #perform order by
 select distinct * from employee1 where 12*salary<2000000 order by salary asc;
 
 #display only particular number of rows
 SELECT name,age FROM employee_1 WHERE age=21 LIMIT 2;
  
#display distict name from both tables
 select * from employee_1 a,employee_1 b where a.name <> b.name;
 








