#creating a table
CREATE TABLE employee (
  id int,
  name varchar(50),
  salary int,
  bonus int(20),
  phone varchar(10),
  state varchar(30)
);

#inserting values to the columns
insert into employee values(1,'Suhana',50000,20000,9534567891,'AP');
insert into employee values(2,'Noori',55000,22000,7834567451,'UP');
insert into employee values(3,'Aliya',50000,20000,'9134567891','AP');
insert into employee values(4,'Sridevi',60000,24000,'8934567891','MP');
insert into employee values(5,'Sowmya',65000,25000,'8934567991','MP');
insert into employee values(6,'Pavi',70000,27000,'8934567893','KARNATAKA');

#to display all columns
select * from employee;

output:
	id	name	  salary	bonus	phone	     state
	2	Noori	  55000	22000	7834567451	UP
	3	Aliya	  50000	20000	9134567891	AP
	4	Sridevi 60000	24000	8934567891	MP
	5	Sowmya  65000	25000	8934567991	MP
	6	Pavi	  70000	27000	8934567893	KARNATAKA
	1	Suhana  50000	20000	9534567891	AP


	
#display only name from the employee table
select name from employee;

output:
	name
	Noori
	Aliya
	Sridevi
	Sowmya
	Pavi
	Suhana

#display name where salary>55000
select name from employee where salary>55000;

output:
	name
	Sridevi
	Sowmya
	Pavi

#display count of employee
select count(*) as count from employee;

output:
	count
	6

#display employee name order by name in ascending order
select name from employee order by name asc;

output:
	name
	Aliya
	Noori
	Pavi
	Sowmya
	Sridevi
	Suhana

#display employee salary and group by salary
select salary from employee group by salary;

output:
	name	   salary
	Noori	   55000
	Aliya	   50000
	Sridevi  60000
	Sowmya   65000
	Pavi	   70000
	Suhana   50000

#display sum of salary from employee and give alias nme to that column
select sum(salary) as sumsalary from employee;
select avg(bonus) as average from employee;
output:
	sumsalary
	350000

#display employee name which starts with 's'
select name from employee where name like 's%';

output:
	name
	Sridevi
	Sowmya
	Suhana

#display name in upper case
select upper(name) from employee;

output:
	upper(name)
	NOORI
	ALIYA
	SRIDEVI
	SOWMYA
	PAVI
	SUHANA

#display only starting 4 letters of name
select substring(name,1,4) from employee;

output:
	substring(name,1,4)
	Noor
	Aliy
	Srid
	Sowm
	Pavi
	Suha

#display the hightest salary from employee
select max(salary) from employee;

output:
	max(salary)
	70000

#display distinct name from employee
select distinct name from employee;
select distinct salary from employee;

output:
	name
	Noori
	Aliya
	Sridevi
	Sowmya
	Pavi
	Suhana

#display the second highest salary
select max(salary) from employee where salary<(select max(salary) from employee);
#drop table employee;

output:
	max(salary)
	65000


#add a new column as lastname to the employee table
alter table employee add lastname varchar(30);
select * from employee;

output:
	id	name	  salary	bonus	phone	     state	     lastname
	2	Noori	  55000	22000	7834567451	UP	       nill
	3	Aliya	  50000	20000	9134567891	AP	       nill 
	4	Sridevi 60000	24000	8934567891	MP		 nill
	5	Sowmya  65000	25000	8934567991	MP		 nill
	6	Pavi    70000	27000	8934567893	KARNATAKA	 nill
	1	Suhana  50000	20000	9534567891	AP		 nill



#upadate lastname column using condition
update  employee set lastname='Anjum' where id=1;
update  employee set lastname='Zafar' where id=2;
update  employee set lastname='Chandini' where id=3;
update  employee set lastname='Ravi' where id=4;
update  employee set lastname='Jaya' where id=5;
update  employee set lastname='Reddy' where id=6;
insert into employee(lastname) values ('Anjum');
select * from employee;

output:
	id	name	   salary	bonus	phone	      state	      lastname
	2	Noori	   55000	22000	7834567451	UP	      Zafar
	3	Aliya	   50000	20000	9134567891	AP	      Chandini
	4	Sridevi  60000	24000	8934567891	MP	      Ravi
	5	Sowmya   65000	25000	8934567991	MP	      Jaya
	6	Pavi	   70000	27000	8934567893	KARNATAKA	Reddy
	1	Suhana   50000	20000	9534567891	AP	      Anjum


#delete the row where lastname=anjum
delete from employee where lastname = 'Anjum';
SET SQL_SAFE_UPDATES = 0;


#rearrange the position of columns
alter table employee modify lastname varchar(30) after name;
select 2,3;
select 15+4;

#perform ltrim on name
select rtrim(name) from employee;

#display length of state 
select length(state) from employee;

output:
	length(state)
	2
	2
	2
	2
	9

#display the table after replacing 'A' with 'a'
select replace(lastname,'A','a') from employee;

output:
	replace(lastname,'R','r')
	Zafar
	Chandini
	ravi
	Jaya
	reddy


#display table by combining name and lastname
select concat(name,' ',lastname) as Name from employee;
select * from employee;

output:
	Name
	Noori Zafar
	Aliya Chandini
	Sridevi Ravi
	Sowmya Jaya
	Pavi Reddy

#display the salary between 500000 and 600000
select * from employee where salary between 50000 and 60000;
select * into employee1 from employee;

output:
	id	name	   salary
	2	Noori	   55000
	3	Aliya	   50000
	4	Sridevi  60000

#display system date
select curdate();
select now();
select sysdate() from dual;
 output:
	sysdate()
	2022-12-01 13:00:51
