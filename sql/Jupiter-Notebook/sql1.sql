#creating a table
CREATE TABLE employee (
  id int,
  name varchar(50),
  salary int,
  bonus int,
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

#display only name from the employee table
select name from employee;

#display name where salary>55000
select name from employee where salary>55000;

#display count of employee
select count(*) as count from employee;

#display employee name order by name in ascending order
select name from employee order by name asc;

#display employee salary and group by salary
select name,salary from employee group by name,salary;

#display sum of salary from employee and give alias nme to that column
select sum(salary) as sumsalary from employee;
select avg(bonus) as average from employee;

#display employee name which starts with 's'
select name from employee where name like 's%';

#display name in upper case
select upper(name) from employee;

#display only starting 4 letters of name
select substring(name,1,4) from employee;

#display the hightest salary from employee
select max(salary) from employee;

#display distinct name from employee
select distinct name from employee;
select distinct salary from employee;

#display the second highest salary
select max(salary) from employee where salary<(select max(salary) from employee);
#drop table employee;

#add a new column as lastname to the employee table
alter table employee add lastname varchar(30);
select * from employee;

#upadate lastname column using condition
update  employee set lastname='Anjum' where id=1;
update  employee set lastname='Zafar' where id=2;
update  employee set lastname='Chandini' where id=3;
update  employee set lastname='Ravi' where id=4;
update  employee set lastname='Jaya' where id=5;
update  employee set lastname='Reddy' where id=6;
insert into employee(lastname) values ('Anjum');
select * from employee;

#delete the row where lastname=anjum
delete from employee where lastname = 'Anjum';
SET SQL_SAFE_UPDATES = 0;
insert into employee values(1,'Suhana',50000,20000,9534567891,'AP','Anjum');

#rearrange the position of columns
alter table employee modify lastname varchar(30) after name;
select 2,3;
select 15+4;

#perform ltrim on name
select rtrim(name) from employee;

#display length of state 
select length(state) from employee;

#display the table after replacing 'A' with 'a'
select replace(lastname,'R','r') from employee;

#display table by combining name and lastname
select concat(name,' ',lastname) as Name from employee;
select * from employee;

#display the salary between 500000 and 600000
select id,name,salary from employee where salary between 50000 and 60000;
select * into employee1 from employee;

#display system date
select curdate();
select now();
select sysdate() from dual;