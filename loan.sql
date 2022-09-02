create database BankLoan ;

create table information_on_customer (
Gender varchar(255)  , 
Married varchar(255) ,
Dependents int , 
Education varchar(255),
Self_Employed varchar(255),
Id int ,

Income int , 
LoanAmount int
);

insert into information_on_customer(Gender , Married ,Dependents , Education , Self_Employed ,Id, Income , LoanAmount) 
values ('Man' , 'Yes','1', 'Student' , 'No' ,'1', '2000' , '21000'); 
insert into information_on_customer(Gender , Married ,Dependents , Education , Self_Employed , Id,Income , LoanAmount) 
values ('Girl' , 'Yes','1', 'Graduated' , 'No' , '2', '2500' , '4000');  
insert into information_on_customer(Gender , Married ,Dependents , Education , Self_Employed ,Id, Income , LoanAmount) 
values ('Man' , 'No','0', 'Student' , 'Yes' , '3', '1000' , '50000'); 
insert into information_on_customer(Gender , Married ,Dependents , Education , Self_Employed ,Id, Income , LoanAmount) 
values ('Girl' , 'No','1', 'Graduated' , 'yes' ,'4', '1500' , '40000');
insert into information_on_customer(Gender , Married ,Dependents , Education , Self_Employed ,Id, Income , LoanAmount) 
values ('Man' , 'Yes','0', 'Student' , 'No' , '5','2000' , '21000'); 
insert into information_on_customer(Gender , Married ,Dependents , Education , Self_Employed ,Id, Income , LoanAmount) 
values ('Girl' , 'Yes','1', 'Graduated' , 'No' , '6','2500' , '4000');  
insert into information_on_customer(Gender , Married ,Dependents , Education , Self_Employed ,Id, Income , LoanAmount) 
values ('Girl' , 'No','0', 'Student' , 'Yes' ,'7', '800' , '5000'); 
insert into information_on_customer(Gender , Married ,Dependents , Education , Self_Employed ,Id, Income , LoanAmount) 
values ('Man' , 'No','1', 'Graduated' , 'yes', '8', '850' , '4000');
insert into information_on_customer(Gender , Married ,Dependents , Education , Self_Employed ,Id, Income , LoanAmount) 
values ('Girl' , 'No','0', 'Graduated' , 'yes' ,'9', '1500' , '40000');
insert into information_on_customer(Gender , Married ,Dependents , Education , Self_Employed ,Id, Income , LoanAmount) 
values ('Man' , 'Yes','1', 'Student' , 'No' ,'10', '2000' , '21000'); 
insert into information_on_customer(Gender , Married ,Dependents , Education , Self_Employed ,Id, Income , LoanAmount) 
values ('Girl' , 'Yes','0', 'Graduated' , 'No' ,'11', '2500' , '4000');  
insert into information_on_customer(Gender , Married ,Dependents , Education , Self_Employed ,Id, Income , LoanAmount) 
values ('Girl' , 'No','1', 'Student' , 'Yes' ,'12', '800' , '5000'); 
insert into information_on_customer(Gender , Married ,Dependents , Education , Self_Employed ,Id, Income , LoanAmount) 
values ('Man' , 'No','0', 'Graduated' , 'yes' ,'13', '850' , '4000');  

create table bank_information(
Id int , 
NameId varchar(255),
JobTitle varchar(255),
AlreadyGotLoan varchar(255), 
Depth int,
ClientReputation varchar(255)

);

insert into bank_information(Id , NameId , JobTitle , AlreadyGotLoan , Depth , ClientReputation) 
values ('1' ,'Eden_Lecarpentier' ,'Data_Analyst' , 'No', '0', 'Good'); 
insert into bank_information(Id , NameId , JobTitle , AlreadyGotLoan , Depth , ClientReputation) 
values ('2' ,'Cynthia_marceny' ,'Drawer' , 'Yes', '4000', 'Okay'); 
insert into bank_information(Id , NameId , JobTitle , AlreadyGotLoan , Depth , ClientReputation) 
values ('3' ,'Samuel_Fasquelle' ,'pro_yugioh_player' , 'No', '0', 'Good'); 
insert into bank_information(Id , NameId , JobTitle , AlreadyGotLoan , Depth , ClientReputation) 
values ('4' ,'Victoria_Williams' ,'fish_monger' , 'Yes', '0', 'Good'); 
insert into bank_information(Id , NameId , JobTitle , AlreadyGotLoan , Depth , ClientReputation) 
values ('5' ,'Pam_Williams' ,'Office_Work' , 'Yes', '0', 'Good'); 
insert into bank_information(Id , NameId , JobTitle , AlreadyGotLoan , Depth , ClientReputation) 
values ('6' ,'Louis_Lecarpentier' ,'fish_monger' , 'Yes', '4000', 'Okay'); 
insert into bank_information(Id , NameId , JobTitle , AlreadyGotLoan , Depth , ClientReputation) 
values ('7' ,'Hyppolite_Lecarpentier' ,'EEnergy_Engenieur' , 'No', '300', 'okay'); 
insert into bank_information(Id , NameId , JobTitle , AlreadyGotLoan , Depth , ClientReputation) 
values ('8' ,'Typhaine_le_voisin_barbier' ,'Care_Assistant' , 'Yes', '40000', 'Bad'); 
insert into bank_information(Id , NameId , JobTitle , AlreadyGotLoan , Depth , ClientReputation) 
values ('9' ,'Quentin_Walbeck' ,'Pet_Cleaner' , 'No', '0', 'Good'); 
insert into bank_information(Id , NameId , JobTitle , AlreadyGotLoan , Depth , ClientReputation) 
values ('10' ,'Cynthia_marceny_theault' ,'Drawer' , 'Yes', '40', 'Okay'); 
insert into bank_information(Id , NameId , JobTitle , AlreadyGotLoan , Depth , ClientReputation) 
values ('11' ,'Willem_Marceny' ,'Different_Jobs' , 'No', '0', 'Good'); 
insert into bank_information(Id , NameId , JobTitle , AlreadyGotLoan , Depth , ClientReputation) 
values ('12' ,'Cynthia_marceny' ,'Drawer' , 'Yes', '4000', 'Okay'); 
insert into bank_information(Id , NameId , JobTitle , AlreadyGotLoan , Depth , ClientReputation) 
values ('13' ,'Eden_Lecarpentier' ,'Data_Analyst' , 'Yes', '0', 'Good'); 

select count(bi.Id) , ioc.Id as "test" 
from bank_information as bi 
join information_on_customer as ioc on bi.Id = ioc.Id
where bi.AlreadyGotLoan='Yes' or bi.AlreadyGotLoan='No';

#found highest salary for each gender 
select Income as max_income , Gender from information_on_customer as ioc , ( 
select max(Income) from information_on_customer where Income > 1000) as c
group by Gender 
order by Gender , max_income desc
;
select (ioc.Gender) as what_gender_married_as_most_loan , ioc.LoanAmount , ioc.Married  from information_on_customer as ioc , (
select LoanAmount from information_on_customer where Married = 'Yes' and LoanAmount > 1000) as c 
order by what_gender_married_as_most_loan 
;

select max(ioc.Income) as max_income , bi.JobTitle , ioc.Gender from information_on_customer as ioc
join bank_information as bi on ioc.Id = bi.Id
where ioc.Gender = 'girl'
;

select Income , Depth , NameId from information_on_customer as ioc
join bank_information as bi on ioc.Id = bi.Id
where Income > Depth 
group by NameId
order by NameId desc
;

select bi.Depth  , ioc.Income ,  ioc.Gender , bi.NameId from information_on_customer as ioc 
join bank_information as bi on ioc.Id = bi.Id 
where depth > Income 

order by Gender='Girl' desc
;

select ioc.dependents , bi.Depth , ioc.Gender from information_on_customer as ioc 
join bank_information as bi on ioc.id = bi.id
;


with information_on_custome as 
( 
select *,
case 
when i.Gender  = 'Boy' then Income * 20 
when i.Gender = 'girl' then Income * 10
END AS information_on_custome
from information_on_customer as i)
SELECT Id, Income AS new_income  from information_on_customer;



WITH points AS 
(
SELECT *,
    CASE 
    WHEN m.product_name = 'sushi' THEN price * 20
    WHEN m.product_name != 'sushi' THEN price * 10
    END AS points
FROM menu m
    )
SELECT customer_id, SUM(points) AS points
FROM sales s
JOIN points p ON p.product_id = s.product_id
GROUP BY s.customer_id ;



