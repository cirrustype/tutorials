"Section 3: part 1"


select concat(concat(lower(ename), upper(' is the name')), concat(' and their job is: ', JOB))
from emp;


"Section 3: part 2"
"Using fuctions in WHERE and charecter based SRFs"


select lower(ename) from emp;

select * form emp where job = lower('MANAGER') '#does not work '

"capitalize initial letter of a string"
select initcap('hello world') as "hello world" from dual

"length function"
select ename, length(ename) as length from emp
where length(ename) = 6;

"substring function"
select substr('hello', 2, 2) from dual;

select substr('hello', 2) from dual;

"LPAD"

select lpad('hello', 10, '%') from dual;
select rpad('hello', 10, '&') from dual;
select ltrim('hellohhhhh', 'h') from dual; 
select rtrim('hellohhhhh', 'h') from dual; 