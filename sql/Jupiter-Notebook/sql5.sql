#coalesce-return the first non null value
SELECT COALESCE(NULL, 1, 2, 'noori');
SELECT COALESCE(NULL, NULL, NULL, 'suhana', NULL, 'noori');


#adddate-it adds 10 days to the given day
SELECT ADDDATE("2022-12-08", INTERVAL 10 DAY);

#retuns no. of days between two dates
SELECT DATEDIFF("2022-12-08", "2022-12-17");

#dayname-returns the day name,dayofmonth-returns month no.,dayofweek-returns week no.
SELECT DAYNAME(CURDATE());
SELECT DAYNAME("2022-12-08");
SELECT DAYOFMONTH(CURDATE());
SELECT DAYOFMONTH("2022-12-08");
SELECT DAYOFWEEK(CURDATE());
SELECT DAYOFYEAR(CURDATE());


#extarct year and month from a date
SELECT EXTRACT(YEAR_MONTH FROM "2017-12-08");


#returns a binary representation of a given number
SELECT BIN(2);
SELECT BIN(100);

#
SELECT BINARY "HELLO" = "hello";
SELECT "HELLO" = "hello";
SELECT BINARY "noori";

#case
SELECT employee_id, amount,
CASE
    WHEN amount > 9000 THEN "The amount is greater than 9000"
    WHEN amount = 9000 THEN "The amount is 9000"
    ELSE "The amount is under 9000"
END
FROM salary;


#query to display difference btw min and max
select min(s.amount),max(s.amount),min(s.amount)-max(s.amount) as saldiff from employe e,salary s 
where e.employee_id=s.employee_id 
and amount>=2000 and amount<=10000 group by s.amount;


#round is used to round a number to a specified number of decimal places
select e.employee_id,s.amount,round(s.amount,3) from employe e,salary s 
where e.employee_id=s.employee_id; 
select round(23.980,2);


#display current user details
SELECT CONNECTION_ID();
SELECT CURRENT_USER();
SELECT DATABASE();
SELECT ifnull("hi", null);

#ranking the score from hightest to lowest
#create rank table
create table Scores(id int,score float);
insert into Scores values(1,"3.50"),(2,"3.65"),(3,"4.00"),(4,"3.85"),(5,"4.00"),(6,"3.65");
select * from Scores;
drop table Scores;


SELECT S.score, COUNT(DISTINCT T.score) AS 'rank' FROM Scores S INNER JOIN Scores T ON S.score <= T.score
GROUP BY S.id, S.score
ORDER BY 
S.score DESC;

#displaying duplicate emails
create table Person(id int,email varchar(30));
insert into Person Values(1,"a@b.com"),(2,"c@d.com"),(3,"a@b.com"),
                         (4,"b@d.com"),(5,"e@d.com"),(6,"c@d.com");
select * from Person;


select Email,num from
(  select Email, count(Email) as num  from Person
  group by Email
) as statistic where num > 1;           


#to find dates with higher temperatures compared to its previous dates    

create table weather(id int,record_date date,temperature int);
insert into weather values( 1 ,'2015-01-01',10) ,( 2 ,'2015-01-02' ,25 ),
(3 ,'2015-01-03',20),( 4 ,'2015-01-04' ,30),(5,'2015-01-05',35);      

SELECT weather.id AS 'Id',weather.record_date,weather.temperature FROM weather JOIN weather w 
ON DATEDIFF(weather.record_date, w.record_date) = 1 
AND weather.temperature > w.temperature ;


#swapping values
Create table Seat (id int, student varchar(255));
insert into Seat values('1', 'Abbot'), ('2', 'Doris'), ('3', 'Emerson'), ('4', 'Green'), ('5', 'Jeames');

SELECT
    s1.id, COALESCE(s2.student, s1.student) AS student
FROM
    seat s1
        LEFT JOIN
    seat s2 ON ((s1.id + 1) ^ 1) - 1 = s2.id ORDER BY s1.id;
