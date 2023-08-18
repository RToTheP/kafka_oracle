create user ross identified by RPPassword1 default tablespace users;

GRANT CONNECT, RESOURCE, DBA TO ross;

GRANT CREATE SESSION To ross;

-- GRANT ANY PRIVILEGE TO ross;

GRANT UNLIMITED TABLESPACE TO ross;

