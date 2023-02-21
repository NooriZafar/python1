#creating table
create table employee_1(Name varchar(30),City varchar(30),Age int,Grade char);

#insert values in employee table
insert into employee_1 values("Noori","Delhi",20,"A"),("Sabeeha","Jaipur",21,"A"),
						("Saif","Mumbai",21,"B"),("Zafar","Kolkata",22,"B");

#display the table
select * from employee_1;

output:

	Name	   City	Age	Grade
	Noori	   Delhi	20	A
	Sabeeha  Jaipur	21	A
	Saif	   Mumbai	21	B
	Zafar	   Kolkata	22	B

#create another table                        
create table employee_2(Name varchar(30),Age int,phone varchar(10),Grade char);

#insert values
insert into employee_2 values("Suhail",20,9063058981,"A"),("Samaira",21,9063058982,"A"),
						("Nayeem",21,9063058983,"B"),("Zafar",22,9063058984,"B");
					
select * from employee_2;

output:

	Name	      Age	phone	      Grade
	Suhail	20	9063058981	A
	Samaira	21	9063058982	A
	Nayeem	21	9063058983	B
	Zafar	      22	9063058984	B
 
#perform intersection of two tables
select name,age,Grade from employee_1 where age=22 INTERSECT select name,age,Grade from employee_2 where age=22;
output:

	name	age
	Zafar	22

#intersection using join
select distinct employee_1.Name,employee_1.Age,employee_2.Grade from employee_1
inner join employee_2 on employee_1.Name=employee_2.Name;

select distinct employee_1.Name,employee_1.Age,employee_2.Grade from employee_1 
join employee_2 on employee_1.Name=employee_2.Name;

output:
	Name	Age	Grade
	Zafar	22	B

#we can't perform minus operation in mysql oracle 
#select Name,Age,Grade from table1 minus select Name,Age,Grade from table2;
select Name from employee_1 left join table2 using(name) where employee_2.name is null;
select employee_1.Name,employee_1.Age,employee_1.Grade from employee_1 
left join employee_2 on employee_1.Name=employee_2.Name where employee_2.name is null;

output:

	Name	   Age	Grade
	Noori	    20	A
	Sabeeha   21	A
	Saif	    21	B


#perform union operation
select name from employee_1 union select name from employee_2;

output:

	name	      age
	Noori	      20
	Sabeeha	21
	Saif	      21
	Zafar	      22
	Suhail	20
	Samaira	21
	Nayeem	21

#collect max,min age
select max(age) from employee_1;
select min(age) from employee_1;
select name,age from employee_1 where age=(select (max(age)+min(age))/2 from employee_1);

output:
	name	      age
	Sabeeha	21
	Saif	      21

#we can't perform mod in mysql oracle
select * from employee_1 where mod(name,2)=0;
select * from employee_1 where age%2 <>0;

#display only even rows
select * from(select name ,age,row_number() over(order by name desc) as 'rownumber' from employee_1)
 d where (rownumber%2)=0;
 select * from(select name ,age,row_number() over(order by name) as 'rownumber' from employee_1)
 d where (rownumber%2)=0;

output:
	name	age	rownumber
	Saif	21	2
	Noori	20	4
 
 
 #display annual salry
 select * from employee_1;
 select sum(age) from employee_1 where age=21;
 select empname,sum(12*salary) as annualsalary from employee_1 group by empname;

output:
	empname	annualsalary
	Noori	      1200000
	Sabeeha	1320000
	suhail	2160000
	saif	      1680000
	sri	      1560000
	Nayeem	1560000
 
 #display distinct length of empname
 select distinct name from employee_1 where length(name)>5;

output:
	name
	Sabeeha
 
 #perfroming operation using in()
 select name,age,Grade from employee_2 where age in(21,22);
 select name,age,Grade from employee_2 where age in(21,22) order by age desc;

output:
	name	     age	Grade
	Zafar  	22	B
	Samaira	21	A
	Nayeem	21	B
 
 #perform order by
 select distinct * from employee1 where 12*salary<2000000 order by salary asc;
 
 #display only particular number of rows
 SELECT name,age FROM employee_1 WHERE age=21 LIMIT 2;

output:
	name	      age
	Sabeeha	21
	Saif	      21
  
#display self join of employee1
 select * from employee_1 a,employee_1 b where a.name <> b.name;

output:
	Name	   City	Age	Grade	Name  	City  	Age	Grade
	Zafar	   Kolkata	22	B	Noori 	Delhi	      20	A
	Saif	   Mumbai	21	B	Noori 	Delhi 	20	A
	Sabeeha  Jaipur	21	A	Noori 	Delhi 	20	A
	Zafar	   Kolkata	22	B	Sabeeha	Jaipur	21	A
	Saif	   Mumbai	21	B	Sabeeha	Jaipur	21	A
	Noori    Delhi	20	A	Sabeeha	Jaipur	21	A
	Zafar	   Kolkata	22	B	Saif  	Mumbai	21	B
	Sabeeha  Jaipur	21	A	Saif  	Mumbai	21	B
	Noori	   Delhi	20	A	Saif  	Mumbai	21	B
	Saif	   Mumbai	21	B	Zafar	      Kolkata	22	B
	Sabeeha  Jaipur	21	A	Zafar 	Kolkata	22	B
	Noori	   Delhi	20	A	Zafar 	Kolkata	22	B
 








