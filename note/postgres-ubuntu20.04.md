# Postgres-12 installation on ubuntu-server-20.04 20210709
## Install as root, and enable remote access
```bash
apt install postgresql postgresql-contrib -y # /usr/lib /var/lib /etc
vim /etc/postgresql/12/main/postgresql.conf # listen_address='*'
vim /etc/postgresql/12/main/pg_hba.conf # host all all 0.0.0.0/0 md5
sudo -u postgres psql # alter user postgres with password 'pwd'; \q
/etc/init.d/postgresql restart
```
## remote connect and user grants
```sql
psql postgresql://postgres:pwd@ip
create user css with [superuser] password 'pwd'; # alter user css with nosuperuser;
create database cssdb;
alter database cssdb owner to css; #reassign owned by css to postgres;
grant all privileges on database cssdb to css [with grant option];
revoke all privileges on database cssdb from css;
\c cssdb
set role css;
create table t1(id serial, name varchar(20));
insert into t1(name) values('css');
```
## display basic information
```sql
select current_user,session_user,version();
\conninfo
\l # database
\dn # schema
\dt+ # table
\du # user
```
