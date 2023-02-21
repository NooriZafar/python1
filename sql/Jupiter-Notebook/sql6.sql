#ranking the score from hightest to lowest
#create rank table
create table Scores(id int,score float);
insert into Scores values(1,"3.50"),(2,"3.65"),(3,"4.00"),(4,"3.85"),(5,"4.00"),(6,"3.65");
select * from Scores;


SELECT S.score, COUNT(DISTINCT T.score) AS 'rank' FROM Scores S 
	INNER JOIN Scores T 
ON S.score <= T.score
GROUP BY S.id, S.score
ORDER BY 
S.score DESC;

select * from Scores order by score desc;

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


#display first login date fro each player
create table activity(player_id int,device_id int,event_date date,games_played int);
insert into activity values(1,2,'2016-03-01',5),(1,2,'2016-05-02',2),(2,3,'2017-06-25',1),
(3,1,'2016-03-02',0),(3,4,'2018-07-03',5);
select * from activity;

SELECT
  A.player_id,
  MIN(A.event_date) AS first_login
FROM
  Activity A
GROUP BY
  A.player_id;
  
  #customer placing large number of orders
  create table orders(order_number int,customer_number int);
  insert into orders values(1,1),(2,2),(3,3),(4,3),(5,2),(6,3);
  
  SELECT customer_number
FROM
    orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;

SELECT customer_number 
FROM orders
GROUP BY customer_number
HAVING count(order_number) = (    SELECT count(order_number)    FROM orders
    GROUP BY customer_number
    ORDER BY count(order_number) DESC LIMIT 1);
    


#class more than 5 students
Create table Courses(student varchar(30), class varchar(30));

Insert into Courses  values('A', 'Mathematics'),('B', 'English'),('C', 'Mathematics'),
('D', 'Biology'),('E', 'Mathematics'),('F', 'Computer'),('G', 'Mathematics'),('H', 'Mathematics'),
('I', 'Mathematics'),('J','Biology');

SELECT class FROM (SELECT class, COUNT(DISTINCT student)
AS num FROM courses GROUP BY class) AS temp_table WHERE num >= 5;

select class FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;



#type of each node in the tree(root,inner,leaf)
Create table Tree (id int, parent_id int);
insert into Tree values ('1', Null),('2', '1'),('3', '1'),('4', '2'),('5', '2');

SELECT
    id AS `Id`,    
    CASE
        WHEN tree.id = (SELECT t.id FROM tree t WHERE t.parent_id IS NULL)         
        THEN 'Root'        
        WHEN tree.id IN (SELECT t.parent_id FROM tree t)        
        THEN 'Inner'        
        ELSE 'Leaf'    
        END AS Type
FROM
    tree
ORDER BY `Id`;



#displaying actors and director how worked alteast 3 times
Create table Actor(actor_id int, director_id int, timestamp int);
insert into Actor values('1', '1', '0'),('1', '1', '1'),('1', '1', '2'),('1', '2', '3'),
('1', '2', '4'),('2', '1', '5'),('2', '1', '6');
SELECT actor_id, director_id
FROM
(SELECT actor_id, director_id, COUNT(timestamp) AS nums
FROM Actor
GROUP BY actor_id, director_id
ORDER BY actor_id, director_id) tmp
WHERE nums >= 3;

