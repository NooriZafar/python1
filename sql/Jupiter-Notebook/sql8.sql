#Displaying patients with Type I Diabetes
Create table Patients (patient_id int, patient_name varchar(30), conditions varchar(100));
insert into Patients values ('1', 'Daniel', 'YFEV COUGH'),('2', 'Alice', ''),
('3', 'Bob', 'DIAB100 MYOP'),('4', 'George', 'ACNE DIAB100'),('5', 'Alain', 'DIAB201');

SELECT patient_id, patient_name, conditions FROM Patients
WHERE position('DIAB1' in conditions) > 0 ;


#Employees With Missing Information
Create table Employees (employee_id int, name varchar(30));
insert into Employees values ('2', 'Crew'),('4', 'Haven'),('5', 'Kristian');

Create table Salaries (employee_id int, salary int);
insert into Salaries  values ('5', '76071'),('1', '22517'),('4', '63539');

select employee_id from Employees where employee_id
not in (select employee_id from Salaries) union
select employee_id from Salaries where employee_id
not in (select employee_id from Employees) order by employee_id ;

#Rearranging products table
Create table Products (product_id int, store1 int, store2 int, store3 int);
insert into Products values ('0', '95', '100', '105'),('1', '70', 'None', '80');

SELECT view.product_id,view.store,view.price FROM (
SELECT product_id, 'store1' AS store, store1 AS price FROM Products
UNION ALL
SELECT product_id, 'store2' AS store, store2 AS price FROM Products
UNION ALL
SELECT product_id, 'store3' AS store, store3 AS price FROM Products
) AS view
WHERE view.price IS NOT NULL ;

