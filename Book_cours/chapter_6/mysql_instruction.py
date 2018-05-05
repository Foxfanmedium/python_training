"""
1. Прописать в переменной окружения путь до MySQL
2. $ mysql.exe -h localhost -u root -p
3. $ create database vsearchlogDB;
4. use vsearchlogDB;
5. mysql> create table log(
    -> id int auto_increment primary key,
    -> ts timestamp default current_timestamp,
    -> phrase varchar(128) not null,
    -> letters varchar(32) not null,
    -> ip varchar(16) not null,
    -> browser_string varchar(256) not null,
    -> results varchar(64) not null);
Query OK, 0 rows affected (0.35 sec)
6. $ describe log;




"""