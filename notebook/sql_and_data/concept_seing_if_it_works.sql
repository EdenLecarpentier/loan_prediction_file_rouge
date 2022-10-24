SELECT * FROM bankloan.bank_information;

with Id as (select distinct(JobTitle) as number_of_job
from bank_information)

select avg(AlreadyGotLoan) as test
from bank_information ; 

select distinct(JobTitle) from bank_information;

select avg(AlreadyGotLoan) as agl
from bank_information;

select * from bank_information as bi 
right join information_on_customer as ioc on bi.Id = ioc.Id; 

select * from bank_information as bi 
inner join information_on_customer as ioc on bi.Id = ioc.Id;

select * from bank_information as bi 
left join information_on_customer as ioc on bi.Id = ioc.Id;

select count(Id) as number_of_id , 
avg(Income) over (partition by Id) as Income_of_Id
from information_on_customer;

select avg(Income) , count(Id) from information_on_customer;

