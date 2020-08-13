'###section 2, part 10:'
select * from emp
where comm is null
and sal between 1100 and 5000
and sal not in (1100, 3000, 5000);

'correct and better version'
select * from emp
where (comm is null or comm = 0)
and sal > 1100 and sal < 5000
and sal != 3000;

'#puzzle'
select * from emp 
where (comm = 300 or comm > 1000)
and job = 'SALESMAN' 

'# like operator'
select * from emp 
where job like 'S%'


'### Section 2, part 11: Ordering, Concatenating & Aliasing Query Results'

select ename as "Employee Name", sal as Salary, comm as Commision from emp


select 'Hello my name is ' || ename as "Our Managers!"  from emp
where job = 'MANAGER'



'puzzle'
select ename || ' makes $' || sal || ' per month.' as "Employee Salary" from emp


'Order by'

select ename, sal from emp
order by ename desc


select deptno, sal, ename from emp
order by deptno, sal