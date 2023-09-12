exit | sqlplus system/badger@localhost/xepdb1 @/tmp/scripts/create_user.sql
exit | sqlplus ross/RPPassword1@localhost/xepdb1 @/tmp/scripts/create_table.sql
exit | sqlplus ross/RPPassword1@localhost/xepdb1 @/tmp/scripts/create_person.sql

mkdir /opt/oracle/oradata/ORCLCDB
mkdir /opt/oracle/oradata/ORCLCDB/XEPDB1/
exit | sqlplus sys/badger as sysdba @/tmp/scripts/setup_debezium.sql

touch /tmp/setup_complete

# ALTER DATABASE ADD LOGFILE GROUP 3 ('/opt/oracle/oradata/ORCLCDB/redo03.log') size 400M REUSE;