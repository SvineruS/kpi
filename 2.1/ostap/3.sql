-- 1.1

CREATE TABLE EMPLOYEE
    (ID         NUMBER(7) CONSTRAINT EMP_PK PRIMARY KEY,
     LAST_NAME  VARCHAR2(25) CONSTRAINT EMP_LAST_NAME_NN NOT NULL,
     FIRST_NAME VARCHAR2(25),
     USER_ID    CHAR(12) CONSTRAINT EMP_USER_ID_NN NOT NULL
         CONSTRAINT EMP_UK UNIQUE,
     DEPT_ID    NUMBER(7) CONSTRAINT EMP_DEPT_ID_NN NOT NULL
         CONSTRAINT EMP_DEP_FK REFERENCES DEPARTMENT (ID),
     START_DATE DATE DEFAULT SYSDATE,
     COMISSION  NUMBER(7) CONSTRAINT EMP_COMISSION_CK CHECK
         (COMISSION >= 10 AND COMISSION <= 50)
    );

SELECT *
FROM USER_TAB_COLUMNS
WHERE TABLE_NAME = 'REGION'
  AND NULLABLE = 'N';

SELECT *
FROM USER_TAB_COLUMNS
WHERE TABLE_NAME = 'DEPARTMENT'
  AND NULLABLE = 'N';

SELECT *
FROM USER_TAB_COLUMNS
WHERE TABLE_NAME = 'EMPLOYEE'
  AND NULLABLE = 'N';


-- 1.2


SELECT *
FROM USER_CONSTRAINTS
WHERE TABLE_NAME = 'REGION';

SELECT *
FROM USER_CONSTRAINTS
WHERE TABLE_NAME = 'DEPARTMENT';

SELECT *
FROM USER_CONSTRAINTS
WHERE TABLE_NAME = 'EMPLOYEE';


ALTER TABLE DEPARTMENT DROP CONSTRAINT DEP_UK;

ALTER TABLE DEPARTMENT ADD CONSTRAINT DEP_UK UNIQUE
    (NAME, REGION_ID);


-- 1.3 lab3z1_3.sql


INSERT INTO REGION
VALUES (44, 'Київ');

INSERT INTO DEPARTMENT
VALUES (10, 'факультет інформатики й обчислювальної техніки', NULL, NULL);


-- lab 1.3

ALTER TABLE DEPARTMENT MODIFY NAME VARCHAR2(100);

INSERT INTO DEPARTMENT
VALUES (10, 'факультет інформатики й обчислювальної техніки', NULL, NULL);

SELECT *
FROM REGION;

SELECT *
FROM DEPARTMENT;



-- 1.4   lab3z1_4.sql

ACCEPT stud_id PROMPT 'Персональний номер студента:'
ACCEPT stud_name PROMPT 'Прізвище студента:'
ACCEPT stud_dept_id PROMPT 'Номер відділу:'
insert into employee (id, last_name, dept_id, user_id)
values (&stud_id, '&stud_name', &stud_dept_id, '&stud_id') ;


-- не в отчет!!
INSERT INTO EMPLOYEE (ID, LAST_NAME, DEPT_ID, USER_ID)
VALUES (200, 'Кострова', 10, 200);
INSERT INTO EMPLOYEE (ID, LAST_NAME, DEPT_ID, USER_ID)
VALUES (201, 'Кравець', 11, 201);

-- 1.5

INSERT INTO DEPARTMENT (ID, NAME)
VALUES (10, 'факультет прикладної математики');


-- 1.6  lab3z1_6.sql

INSERT INTO DEPARTMENT (ID, NAME)
VALUES (37, 'ФПМ');
INSERT INTO DEPARTMENT (ID, NAME)
VALUES (54, 'ФЭ');
INSERT INTO DEPARTMENT (ID, NAME)
VALUES (75, 'ФАКС');


-- не в отчет!!
INSERT INTO EMPLOYEE (ID, LAST_NAME, DEPT_ID, USER_ID)
VALUES (201, 'Студент з ФЕ', 54, 201);
INSERT INTO EMPLOYEE (ID, LAST_NAME, DEPT_ID, USER_ID)
VALUES (202, 'Студент с ФАКС', 75, 202);
INSERT INTO EMPLOYEE (ID, LAST_NAME, DEPT_ID, USER_ID)
VALUES (203, 'Студент с ФПМ', 37, 203);


SELECT *
FROM DEPARTMENT;

SELECT *
FROM EMPLOYEE;

COMMIT;


-- 2.1

UPDATE DEPARTMENT
SET NAME='ТЕФ'
WHERE ID = 75;

SELECT *
FROM DEPARTMENT;


-- 2.2

UPDATE EMPLOYEE
SET LAST_NAME='Кострова'
WHERE ID = 202;

SELECT *
FROM EMPLOYEE;


-- 2.4

DELETE
FROM DEPARTMENT
WHERE ID = 54;


-- 2.5

DELETE
FROM EMPLOYEE
WHERE DEPT_ID = 54;

DELETE
FROM DEPARTMENT
WHERE ID = 54;


-- 2.6

SELECT *
FROM DEPARTMENT;
SELECT *
FROM EMPLOYEE;
COMMIT;



-- 3.1

-- не в отчет!!
INSERT INTO DEPARTMENT (ID, NAME)
VALUES (37, 'ФПМ');
INSERT INTO DEPARTMENT (ID, NAME)
VALUES (54, 'ФЭ');
INSERT INTO DEPARTMENT (ID, NAME)
VALUES (75, 'ФАКС');

SELECT *
FROM DEPARTMENT
WHERE ID = 54;


-- 3.2

SAVEPOINT INS_DONE;


-- 3.3

DELETE
FROM EMPLOYEE;
SELECT *
FROM EMPLOYEE;


-- 3.4

ROLLBACK TO INS_DONE;
SELECT *
FROM DEPARTMENT;
SELECT *
FROM EMPLOYEE;
COMMIT;


-- 3.5 labz3_5.sql

ACCEPT dept_name PROMPT 'Назва відділу:'
INSERT INTO DEPARTMENT (ID, NAME)
VALUES (DEP_PK_SEQ.NEXTVAL, '&dept_name');

-- 3.5

SELECT *
FROM USER_SEQUENCES;

DROP SEQUENCE DEP_PK_SEQ;
CREATE SEQUENCE DEP_PK_SEQ
    INCREMENT BY 1
    START WITH 76
    MAXVALUE 80
    NOCYCLE NOCACHE;


-- не в отчет!!
INSERT INTO DEPARTMENT (ID, NAME)
VALUES (76, 'Адміністративний');

INSERT INTO DEPARTMENT (ID, NAME)
VALUES (77, 'Навчальний');


SELECT *
FROM DEPARTMENT;
COMMIT;


-- 3.6
-- не в отчет!!
INSERT INTO DEPARTMENT (ID, NAME)
VALUES (DEP_PK_SEQ.NEXTVAL, 'Бухгалтерія');
INSERT INTO DEPARTMENT (ID, NAME)
VALUES (DEP_PK_SEQ.NEXTVAL, 'Склад');
INSERT INTO DEPARTMENT (ID, NAME)
VALUES (DEP_PK_SEQ.NEXTVAL, 'Канцелярія');
INSERT INTO DEPARTMENT (ID, NAME)
VALUES (DEP_PK_SEQ.NEXTVAL, 'Дослідницький');

ALTER SEQUENCE DEP_PK_SEQ
    MAXVALUE 999;

SELECT *
FROM USER_SEQUENCES;


SELECT *
FROM DEPARTMENT;

COMMIT;