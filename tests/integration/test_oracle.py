import oracledb

from ko.db import get_connection

def test_oracle():
    con = get_connection()
    assert con is not None

if __name__ == "__main__":
    test_oracle()