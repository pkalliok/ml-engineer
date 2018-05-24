create or replace view adult12
as select * from adult1 natural join adult2;

create or replace view adult_combined
as select "age","capital-loss","capital-gain","class",education,"education-num","hours-per-week","marital-status","native-country",occupation,race,relationship,sex,workclass
from fact_adult
 inner join dim_demografic on fact_adult.id_demografic=dim_demografic.id
 inner join dim_capital on fact_adult.id_capital=dim_capital.id
 inner join dim_education on fact_adult.id_education=dim_education.id;

create or replace view adults as
 select "age","capital-loss","capital-gain","class",education,"education-num","hours-per-week","marital-status","native-country",occupation,race,relationship,sex,workclass from adult
 union
 select "age","capital-loss","capital-gain","class",education,"education-num","hours-per-week","marital-status","native-country",occupation,race,relationship,sex,workclass from adult12
 union
 select "age","capital-loss","capital-gain","class",education,"education-num","hours-per-week","marital-status","native-country",occupation,race,relationship,sex,workclass from adult3
 union
 select "age","capital-loss","capital-gain","class",education,"education-num","hours-per-week","marital-status","native-country",occupation,race,relationship,sex,workclass from adultxml
 union
 select * from adult_combined ;

