#creat database database_name;
create database pfs42;
use pfs42;

show databases;

#drop database database_name;
drop database pfs42;

#creat table table_name(col_name datatype...);
create table students(std_id int,std_name varchar(20),phn_no varchar(20), email varchar(20), city char(10));

desc students;

### Alter
#To add or drop column
#to change to datatype and size
#to rename table or column
#to add or drop constraints

# To add a column
#alter table table_name add column col_name datatype;

alter table students add column age tinyint;
#To drop column
#alter table table_name drop column col_name;
alter table students drop column age;

alter table students drop column phn_no,add column joined_year year,add column state char(20);

#To change the datatype and size
#alter table table_name modify column col_name datatype(size);
alter table students modify column email char(30)







