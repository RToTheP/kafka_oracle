exit | sqlplus system/badger@localhost/xepdb1 @/tmp/scripts/create_user.sql
exit | sqlplus ross/RPPassword1@localhost/xepdb1 @/tmp/scripts/create_table.sql
exit | sqlplus ross/RPPassword1@localhost/xepdb1 @/tmp/scripts/create_person.sql
touch /tmp/setup_complete