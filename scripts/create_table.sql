CREATE TABLE ross.persons(
    id NUMBER GENERATED BY DEFAULT AS IDENTITY,
    first_name VARCHAR2(50) NOT NULL,
    last_name VARCHAR2(50) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE ross.users(
    id NUMBER GENERATED BY DEFAULT AS IDENTITY,
    user_name VARCHAR2(50) NOT NULL,
    PRIMARY KEY(id)
);