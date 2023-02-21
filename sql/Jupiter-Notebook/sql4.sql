#1111create a salary table and insert values

create table salary(id int,employee_id int,amount int,pay_date date);
insert into salary values(1,1,9000,'2017-03-31'),(2,2,6000,'2017-03-31'),
						(3,3,10000,'2017-03-31'),(4,1,7000,'2017-02-28'),
                        (5,2,6000,'2017-02-28'),(6,3,8000,'2017-02-28');

select * from salary;

#create employe table and insert values
create table employe(employee_id int,department_id int);
insert into employe values(1,1),(2,2),(3,2);
drop table employe ;
select * from employe;

#it display as 201803 without space or hyphen
#select extract(year_month from pay_date) as pay_month from salary;

#here if we provide small y then it display only 17 in 2017
select date_format(pay_date,'%Y-%m') as pay_month from salary;

select date_format(pay_date,'%Y-%m') as pay_month,department_id from salary s,employe e 
group by department_id having amount>(select avg(amount) from salary s);

select date_format(pay_date,'%Y-%m') as pay_month,department_id from salary,employe;


#query to display comparision result of the avg salary of emp in dept to the company avg sal


select 
    pay_month,
    department_id, 
    case 
    when dept_avg > comp_avg then 'higher'
    when dept_avg < comp_avg then 'lower' 
    else 'same' 
    end comparison
from (
        select  date_format(b.pay_date, '%Y-%m') pay_month, a.department_id, avg(b.amount) dept_avg,  d.comp_avg
        from employe a 
        inner join salary b
            on (a.employee_id = b.employee_id) 
        inner join (select date_format(c.pay_date, '%Y-%m') pay_month, avg(c.amount) comp_avg 
                    from salary c 
                    group by date_format(c.pay_date, '%Y-%m')) d 
            on ( date_format(b.pay_date, '%Y-%m') = d.pay_month)
group by date_format(b.pay_date, '%Y-%m'), department_id, d.comp_avg) final;





#2222create student table and insert values
create table student(student_id int,student_name varchar(30));
insert into student values(1,'Daniel'),(2,'Jade'),(3,'Stella'),(4,'Jonatham'),(5,'Will');
select * from student;

#create  exam table and insert vales
create table exam(exam_id int,student_id int,score int);
insert into exam values(10,1,70),(10,2,80),(10,3,90),(20,1,80),(30,1,70),(30,3,80),(30,4,90),
						(40,1,60),(40,2,70),(40,4,80);
select * from exam;

#display student who attended atleast one exam but his score should not be maximum or mininum


select student.* from student  inner join exam  on student.student_id=exam.student_id
group by student_id,student_name
having min(score) not in (select min(score) from exam)
and max(score) not in (select max(score) from exam);



#3333create stadium table and insert values
create table stadium(id int,visit_date date,people int);
insert into stadium values(1,'2017-01-01',10),(2,'2017-01-02',109),
						(3,'2017-01-03',150),(4,'2017-01-04',99),
                        (5,'2017-01-05',145),(6,'2017-01-06',1455),
                        (7,'2017-01-07',199),(8,'2017-01-08',188);
select * from stadium;


#query to display 2 or more consecutive rows and amount more then 100

    
SELECT DISTINCT s1.*
FROM stadium s1, stadium s2, stadium s3
WHERE s1.people >= 100
AND s2.people >= 100
AND s3.people >= 100
AND ( (s1.id - s2.id = 1 AND s2.id - s3.id = 1)
OR (s2.id - s3.id = 1 AND s3.id - s1.id = 1)
OR (s3.id - s1.id = 1 AND s1.id - s2.id = 1)
)
ORDER BY s1.id;

select distinct   t1.*from   stadium t1 
   join      stadium t2 
   join      stadium t3 
where   t1.people >= 100   and t2.people >= 100   and t3.people >= 100   and   ( 
(t1.id + 1 = t2.id 
      and t2.id + 1 = t3.id) 
      or      (
         t2.id + 1 = t1.id 
         and t1.id + 1 = t3.id
      )
      or 
      (
         t2.id + 1 = t3.id 
         and t3.id + 1 = t1.id
      )
   )
order by
   id;


#5555 create failed table and insert values
create table failed(fail_date date);
insert into failed values('2018-12-28'),('2018-12-29'),('2019-01-04'),('2019-01-05');
select * from failed;

#create succeeded table and insert values
create table succeeded(success_date date);
insert into succeeded values('2018-12-30'),('2018-12-31'),('2019-01-01'),('2019-01-02'),
							('2019-01-03'),('2019-01-06');
select * from succeeded;
drop table succeeded;


select 'succeeded' as period_state, start_date, min(end_date) as end_date from (
    select success_date as start_date from Succeeded
        where year(success_date) = 2019 and date_sub(success_date, interval 1 day) not in (
            select success_date from Succeeded where year(success_date) = 2019
        )
    ) ss join (
    select success_date as end_date from Succeeded
        where year(success_date) = 2019 and date_add(success_date, interval 1 day) not in (
            select success_date from Succeeded where year(success_date) = 2019
        )
    ) se
    on start_date <= end_date group by start_date;

    
    
select success_date from Succeeded where year(success_date) = 2019;
select success_date as end_date from Succeeded
        where year(success_date) = 2019 and date_add(success_date, interval 1 day);



select 'succeeded' as period_state, start_date, min(end_date) as end_date from (
    select success_date as start_date from Succeeded
        where year(success_date) = 2019 and date_sub(success_date, interval 1 day) not in (
            select success_date from Succeeded where year(success_date) = 2019
        )
    ) ss join (
    select success_date as end_date from Succeeded
        where year(success_date) = 2019 and date_add(success_date, interval 1 day) not in (
            select success_date from Succeeded where year(success_date) = 2019
        )
    ) se
    on start_date <= end_date group by start_date
    union all
select 'failed' as period_state, start_date, min(end_date) as end_date from (
    select fail_date as start_date from Failed
        where year(fail_date) = 2019 and date_sub(fail_date, interval 1 day) not in (
            select fail_date from Failed where year(fail_date) = 2019
        )
    ) fs join (
    select fail_date as end_date from Failed
        where year(fail_date) = 2019 and date_add(fail_date, interval 1 day) not in (
            select fail_date from Failed where year(fail_date) = 2019
        )
    ) fe
    on start_date <= end_date group by start_date
    order by start_date;


#4444create visit table AND insert values
create table visits(user_id int,visit_date date);
insert into visits values(1,'2020-01-01'),(2,'2020-01-02'),(12,'2020-01-01'),
						(19,'2020-01-03'),(1,'2020-01-02'),(2,'2020-01-03'),
                        (1,'2020-01-04'),(7,'2020-01-11'),(9,'2020-01-25'),(8,'2020-01-28');
select * from visits;

create table transactions(user_id int,transaction_date date,amount int);
insert into transactions values(1,'2020-01-02',120),(2,'2020-01-03',22),
								(7,'2020-01-11',232),(1,'2020-01-04',7),
                                (9,'2020-01-25',33),(9,'2020-01-25',66),
                                (8,'2020-01-28',1),(9,'2020-01-25',99);
select * from transactions;



WITH RECURSIVE t1 AS(
					SELECT visit_date, 
							COALESCE(num_visits,0) as num_visits, 
							COALESCE(num_trans,0) as num_trans 
					FROM ((
							SELECT visit_date, user_id, COUNT(*) as num_visits 
                            FROM visits 
                            GROUP BY 1, 2) AS a 
                            LEFT JOIN 
							(
                            SELECT transaction_date, user_id, count(*) as num_trans 
                            FROM transactions 
                            GROUP BY 1, 2) AS b
                            ON a.visit_date = b.transaction_date and a.user_id = b.user_id)
						 ),
				t2 AS ( 
						SELECT MAX(num_trans) as trans 
                        FROM t1 
                        UNION ALL 
                        SELECT trans-1  FROM t2 
                        WHERE trans >= 1)
SELECT trans as transactions_count,  COALESCE(visits_count,0) as visits_count 
FROM t2 LEFT JOIN(
			    SELECT num_trans as transactions_count, COALESCE(COUNT(*),0) as visits_count
                FROM t1  GROUP BY 1 ORDER BY 1) AS a 
                ON a.transactions_count = t2.trans ORDER BY 1;



SELECT visit_date, user_id, COUNT(*) as num_visits 
                            FROM visits 
                            GROUP BY 1, 2 ;
SELECT transaction_date, user_id, count(*) as num_trans 
                            FROM transactions 
                            GROUP BY 1, 2;
SELECT visit_date, 
							COALESCE(num_visits,0) as num_visits, 
							COALESCE(num_trans,0) as num_trans 
					FROM ((
							SELECT visit_date, user_id, COUNT(*) as num_visits 
                            FROM visits 
                            GROUP BY 1, 2) AS a 
                            LEFT JOIN 
							(
                            SELECT transaction_date, user_id, count(*) as num_trans 
                            FROM transactions 
                            GROUP BY 1, 2) AS b
                            ON a.visit_date = b.transaction_date and a.user_id = b.user_id);                         
