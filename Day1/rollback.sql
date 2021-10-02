USE classicmodels;
set autocommit = 0;
start transaction;
delete from employees where employees.firstName = 'test';
rollback;