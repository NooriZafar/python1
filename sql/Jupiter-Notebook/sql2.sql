#create table
create table employee1(empid int,deptid int,empname varchar(50),salary int);

#insert values
insert into employee1 values(1,101,"Noori",50000),(2,101,"Sabeeha",55000),(3,101,"suhail",90000),
							(4,102,"saif",70000),
                            (5,103,"Nazim",65000),(6,102,"Nayeem",65000);

#display table employee1
select * from employee1;

#create another table department
create table department1(deptid int,deptname varchar(50));

#insert values in department
insert into department1 values(101,"sales"),(102,"marketing"),
							(103,"finance");
                            
                            
#display department table                            
select * from department1;

#create table register(empid int,deptid int);
#insert into register values(1,101),(2,102),(3,103),(4,101),(5,102),(6,102);
#select * from register;

#perform join operation based on where condition
 select e.empid,e.empname from employee1 e,department d
	where e.deptid=d.deptid;
    
# join both department and employee1  
select * from employee1 join department;

select * from employee1 where empname like 's%';

select * from employee1 e join department d where e.deptid=d.deptid;

#perform inner join
#it combines the row that have matching value in both tables
select e.empname,e.empid,d.deptname from employee1 e inner join department d on e.deptid=d.deptid;

#perform left join on employee and department
#return all records from left table and matched from right table
select * from employee1 e left join department1 d on e.deptid=d.deptid;

#perform right join on employee and department
#return all records from right table and matched from left table
select e.empname,e.empid,d.deptname from employee1 e right join department d on e.deptid=d.deptid;


#select e.empname,e.empid from (select empname,empid from employee1 where deptid=101) as e
#join (select deptname from department where deptid=101) as d on e.deptid=d.deptid;

#perform inner join and display salary>500000
select * from employee1 e inner join department d where e.deptid=d.deptid and e.salary>50000;

#perform join and display only names starting with's'
select * from employee1 e,department d where e.deptid=d.deptid and e.empname like 'S%';

#display employee,department table where deptname is marketing
select * from employee1 e,department d where e.deptid=d.deptid and d.deptname='marketing';

#to display distinct names
select distinct * from employee1 e,department d where e.deptid=d.deptid and e.salary>50000;

select * from employee1 e,department d where e.deptid=d.deptid;

select * from employee1 e inner join department d where e.deptid=d.deptid;

select * from employee1 e inner join department d where e.deptid=d.deptid and
 e.empname=(select e.empname='s%' from employee1 e);

select * from employee1 where empname like '_____';

select * from employee1 where empname is null;

select * from employee1 where empname is not null;

select distinct length("saif") as namelength from employee1;

#performing lpad operation
select lpad("saif",10,'*') from employee1;

#concat the data
select concat("saif"," khan") from employee1;

#perform builtin functions
select ascii('a');
select ascii('A');
select abs(-18);
select power(4,5);

select empid,empname from employee1 where salary>55000;

update employee1 set empname='sri' where empid=5;

#change the database of existing column
alter table department add(salary char(30));

select * from department;

#update salary=70000 where depatname is sales
update department set salary=50000;
update department set salary=70000 where deptname='sales';

#display 4th highest salary
select distinct * from employee1 order by salary desc limit 1 offset 3;



        