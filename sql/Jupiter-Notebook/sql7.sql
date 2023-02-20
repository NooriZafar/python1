#display duplicate if present
select * from person;
select * from person a where id <>(select max(id) from person b 
where a.email=b.email);

#monthly salary from annual salary
select name,id,salary,salary/12 as monthlysalary from employee;
select * from employee;

select * from employee where id<>(select max(id) from employee);

#display first record
select row_number() over (order by id)rownum,name from employee limit 1 ;

#display nth record
select * from employee where id<>(select max(id) from employee);

#concat in a required manner
create table identity(id int,name varchar(30),profession varchar(30));
insert into identity values(1,'Noori','Doctor'),(2,'Nayeem','Model'),(3,'Azgar','business'),
							(4,'Suhail','Actor'),(5,'Saif','Actor');

select concat(name, '(', substr(profession,1,1), ')') from identity; 


#
create table subscription(user_id int,start_date date,end_date date);
insert into subscription values(1,'2022-01-01','2022-01-31'),(2,'2022-01-16','2022-01-26'),
								(3,'2022-01-28','2022-02-06'),(4,'2022-02-16','2022-02-26');
  select * from subscription;
  
  select * from subscription as s1 left join subscription s2
  on s1.user_id != s2.user_id
  and s1.start_date<=s2.end_date
  and s1.end_date>=s2.start_date;
  
  select distinct s1.user_id,(
  case when s2.user_id is not null then 'true' else 'false' end) as overlap
  from subscription as s1 left join subscription s2
  on s1.user_id != s2.user_id
  and s1.start_date<=s2.end_date
  and s1.end_date>=s2.start_date;
  
  select distinct salary,name from employee a where 3>=(select count(distinct salary)
  from employee b where a.salary<=b.salary)
  order by a.name;
  
#nth row
select distinct * from subscription order by user_id desc limit 1;


#displaying order details of an user made as a buyer in 2019

Create table Users (user_id int, join_date date, favorite_brand varchar(10));
Create table Orders1 (order_id int, order_date date, item_id int, buyer_id int, 
seller_id int);
Create table Items (item_id int, item_brand varchar(10));
insert into Users values('1', '2018-01-01', 'Lenovo'), ('2', '2018-02-09', 'Samsung'), 
('3', '2018-01-19', 'LG'), ('4', '2018-05-21', 'HP');
insert into Orders1 values('1', '2019-08-01', '4', '1', '2'),
('2', '2018-08-02', '2', '1', '3'),('3', '2019-08-03', '3', '2', '3'),
('4', '2018-08-04', '1', '4', '2'),('5', '2018-08-04', '1', '3', '4'),
('6', '2019-08-05', '2', '2', '4');
insert into Items values('1', 'Samsung'),('2', 'Lenovo'),('3', 'LG'),('4', 'HP');

SELECT     u.user_id AS buyer_id,
           u.join_date,
           IFNULL(c.order_count, 0) AS orders_in_2019
FROM       Users u
LEFT JOIN (SELECT   buyer_id,
                    COUNT(buyer_id) AS order_count
           FROM    (SELECT buyer_id
                    FROM   Orders1
                    WHERE  order_date >= '2019-01-01') o
           GROUP BY buyer_id) c
ON         u.user_id = c.buyer_id
ORDER BY   u.user_id ASC;


#formatting depatment table

Create table Department (id int, revenue int, month varchar(5));
insert into Department values ('1', '8000', 'Jan'),('2', '9000', 'Jan'),
							('3', '10000', 'Feb'),('1', '7000', 'Feb'),
							('1', '6000', 'Mar'),('2','6000','Mar');
select * from department;

SELECT id, 
SUM(IF (month = "Jan", revenue, null)) AS Jan_Revenue, 
SUM(IF (month = "Feb", revenue, null)) AS Feb_Revenue, 
SUM(IF (month = "Mar", revenue, null)) AS Mar_Revenue, 
SUM(IF (month = "Apr", revenue, null)) AS Apr_Revenue,
 SUM(IF (month = "May", revenue, null)) AS May_Revenue, 
 SUM(IF (month = "Jun", revenue, null)) AS Jun_Revenue,
 SUM(IF (month = "Jul", revenue, null)) AS Jul_Revenue, 
 SUM(IF (month = "Aug", revenue, null)) AS Aug_Revenue, 
 SUM(IF (month = "Sep", revenue, null)) AS Sep_Revenue,
 SUM(IF (month = "Oct", revenue, null)) AS Oct_Revenue, 
 SUM(IF (month = "Nov", revenue, null)) AS Nov_Revenue, 
 SUM(IF (month = "Dec", revenue, null)) AS Dec_Revenue 
 FROM Department GROUP BY id;
 
 
#displaying gain or loss for each stock

Create Table Stocks(stock_name varchar(15), operation ENUM('Sell', 'Buy'), 
operation_day int, price int);
insert into Stocks values('Maggie', 'Buy', '1', '1000'),('Corona Masks', 'Buy', '2', '10'),
('Maggie', 'Sell', '5', '9000'),('Handbags', 'Buy', '17', '30000'),
('Corona Masks', 'Sell', '3', '1010'),('Corona Masks', 'Buy', '4', '1000'),
('Corona Masks', 'Sell', '5', '500'),('Corona Masks', 'Buy', '6', '1000'),
('Handbags', 'Sell', '29', '7000'),('Corona Masks', 'Sell', '10', '10000');
select * from stocks;


SELECT stock_name, 
SUM( Case When operation='Buy' then -price When operation='Sell' then price End)
 As capital_gain_loss FROM Stocks Group By stock_name ;
 
 
#total distance travel by user
Create Table Users1 (id int, name varchar(30));
insert into Users1 values ('1', 'Alice'),('2', 'Bob'),('3', 'Alex'),('4', 'Donald'),
('7', 'Lee'),('13', 'Jonathan'),('19', 'Elvis');
select * from users1;

Create Table Rides (id int, user_id int, distance int);
insert into Rides values ('1', '1', '120'),('2', '2', '317'),('3', '3', '222'),
('4', '7', '100'),('5', '13', '312'),('6', '19', '50'),('7', '7', '120'),
('8', '19', '400'),('9', '7', '230');


SELECT name,
sum( if(distance is NULL,0,distance) ) as travelled_distance 
FROM Users1 u LEFT JOIN Rides r ON u.id=r.user_id 
GROUP BY name ORDER BY travelled_distance desc,name asc;


#display sold products by date
Create table Activities (sell_date date, product varchar(20));
insert into Activities values ('2020-05-30', 'Headphone'),('2020-06-01', 'Pencil'),
							('2020-06-02', 'Mask'),('2020-05-30', 'Basketball'),
                            ('2020-06-01', 'Bible'),('2020-06-02', 'Mask'),
                            ('2020-05-30', 'T-Shirt');

 
SELECT sell_date, COUNT(DISTINCT product) AS num_sold,
GROUP_CONCAT(DISTINCT product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date ASC;
     
SELECT ROW_NUMBER() OVER ( ORDER BY name) row_num, id
FROM Employee;

select * from (
select e.*, row_number() over (order by salary desc) as row_num from Employee e
) o where row_num = 2;


 

