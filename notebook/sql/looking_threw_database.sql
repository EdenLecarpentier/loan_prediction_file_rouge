SELECT * FROM loan_prediction;
select sum(Dependents) from loan_prediction
where Education = 0 ; 
select Dependents from loan_prediction;
select
CASE
when Dependents = 0 and Education = 0  then "Independent with no education" 
when Dependents = 1 and Education = 0 then "Dependents with no education"
when Dependents = 1 and Education = 1 then "Dependent with Education"
else "Independent with education"
end as "dependentsornot"
from loan_prediction
