import oracledb

from ko.config import CONFIG

def test_oracle():
    user = CONFIG.DB_USER
    pwd = CONFIG.DB_PASSWORD
    host = CONFIG.DB_HOST
    print(user, pwd, host)
    con = oracledb.connect(user=user, password=pwd, host=host, port=1521, service_name="XEPDB1")
    assert con is not None

if __name__ == "__main__":
    test_oracle()