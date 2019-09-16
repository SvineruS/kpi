--������ ��
USE master;
CREATE DATABASE Lab
	ON (NAME = Laba2_1_dat, FILENAME = 'C:\SQL Test\Laba2_1.mdf')
LOG 
	ON (NAME = Laba2_1_log, FILENAME = 'C:\SQL Test\Laba2_1.mdf.ldf');

--���������� � ��
EXEC sp_helpdb Lab
GO

--��������������
ALTER DATABASE Lab  
Modify Name = Laba2_1;  
GO

--�������� ������
USE Laba2_1;
CREATE TABLE DcDiscipline
(
	DcDisciplineId int Identity NOT NULL, 
	Name varchar(250) NOT NULL, 
	CONSTRAINT PK_DcDisciplineId PRIMARY KEY (DcDisciplineId)
)

CREATE TABLE DcPosition
(
	DcPositionId int Identity NOT NULL,
	Name varchar(50) NOT NULL,
	CONSTRAINT PK_DcPosition PRIMARY KEY (DcPositionId)
)

CREATE TABLE DcSubdivision
(
	DcSubdivisionId int Identity NOT NULL,
	Name varchar(250) NOT NULL, 
	CONSTRAINT PK_DcSubdivisionId PRIMARY KEY (DcSubdivisionId)
)

CREATE TABLE Duties
(
	DutiesId int Identity NOT NULL, 
	DcPositionId int NOT NULL, 
	DcSubdivisionId int NULL,
	CONSTRAINT PK_DutiesId PRIMARY KEY (DutiesId),
	CONSTRAINT FK_Duties_DcPosition FOREIGN KEY (DcPositionId) REFERENCES DcPosition (DcPositionId)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT FK_Duties_DcSubdivision FOREIGN KEY (DcSubdivisionId) REFERENCES DcSubdivision (DcSubdivisionId)
		ON DELETE CASCADE
		ON UPDATE CASCADE
)

CREATE TABLE StudyGroup
(
	StudyGroupId int Identity NOT NULL, 
	Name varchar(100) NOT NULL, 
	DcSubdivisionId int NOT NULL, 
	DataVstup date NUll,
	CONSTRAINT PK_StudyGroupId PRIMARY KEY (StudyGroupId),
	CONSTRAINT FK_StudyGroup_DcSubdivision FOREIGN KEY (DcSubdivisionId) REFERENCES DcSubdivision (DcSubdivisionId)
		ON DELETE CASCADE
		ON UPDATE CASCADE
)

CREATE TABLE Employee
(
	EmployeeId int Identity NOT NULL, 
	Surname varchar(20) NOT NULL, 
	Name varchar(15) NOT NULL, 
	Patronymic varchar(20) NULL, 
	Oklad money NOT NULL, 
	BirthdayCity varchar(10) NULL, 
	Nadbavka money Null, 
	DataVuplatu date NULL, 
	DutiesId int NULL,
	Birthday date NULL, 
	CONSTRAINT PK_EmployeeId PRIMARY KEY (EmployeeId),
	CONSTRAINT FK_Employee_Duties FOREIGN KEY (DutiesId) REFERENCES Duties (DutiesId)
		ON DELETE CASCADE
		ON UPDATE CASCADE
)

CREATE TABLE Student
(
	StudentId int Identity NOT NULL,
	Surname varchar(20) NOT NULL,
	Name varchar(15) NOT NULL, 
	Patronymic varchar(20) NULL, 
	Birthday date NOT NULL,
	RecordBook varchar(10) NOT NULL, 
	BirthdayCity varchar(10) NULL, 
	StudyGroupId int NOT NULL, 
	Stipendia money NULL, 
	CONSTRAINT PK_StudentId PRIMARY KEY (StudentId),
	CONSTRAINT FK_Student_StudyGroup FOREIGN KEY (StudyGroupId) REFERENCES StudyGroup (StudyGroupId)
		ON DELETE CASCADE
		ON UPDATE CASCADE
)

CREATE TABLE Exam
(
	ExamId int Identity NOT NULL, 
	Mark int NOT NULL,
	DateExam date NOT NULL, 
	StudentId int NOT NULL, 
	DcDisciplineId int NOT NULL,
	EmployeeId int NOT NULL,
	CONSTRAINT PK_ExamId PRIMARY KEY (ExamId),
	CONSTRAINT FK_Exam_DcDiscipline FOREIGN KEY (DcDisciplineId) REFERENCES DcDiscipline (DcDisciplineId)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT FK_Exam_Employee FOREIGN KEY (EmployeeId) REFERENCES Employee (EmployeeId)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT FK_Exam_Student FOREIGN KEY (StudentId) REFERENCES Student (StudentId)
)
GO

--���� ������������
--ALTER TABLE DcPosition
--ADD Relevance bit NOT NULL DEFAULT 1
--GO

--���������� ������
INSERT INTO DcDiscipline (Name) VALUES
('����������'),
('������'),
('�����'),
('����������'),
('�������'),
('�����'),
('���������'),
('�����������')

INSERT INTO DcPosition (Name) VALUES
('������'),
('���������'),
('���������'),
('��������'),
('���������'),
('���������'),
('��������'),
('�������� �������')

INSERT INTO DcSubdivision (Name) VALUES
('������� 1'),
('������� 2'),
('���������� 1'),
('���������� 2'),
('������ 1'),
('������ 2'),
('����������� 1'),
('����� 1')

INSERT INTO Duties (DcPositionId, DcSubdivisionId) VALUES
('1', '1'),
('2', '1'),
('3', '1'),
('4', '8'),
('5', '8'),
('6', '7'),
('7', '5'),
('1', '2'),
('2', '2'),
('3', '2'),
('8', '6')

INSERT INTO StudyGroup (Name, DcSubdivisionId) VALUES
('��-11', '1'),
('��-12', '1'),
('��-23', '2'),
('��-24', '2')

INSERT INTO Employee (Surname, Name, Patronymic, Oklad, BirthdayCity, Nadbavka, DataVuplatu, DutiesId, Birthday) VALUES
('��������', '������', '����������', 4000.5666, '����', 300.00, '19540323', '1', '19540323'),
('�������', '������', '���������', 1400.061, '����', 256.00, '19550421', '1', '19550421'),
('������', '������', '���������', 4000.0598, '�����', 123.00, '19650614', '2', '19650614'),
('�������', '������', '��������', 3200.4657, '����', 456.00, '19450212', '2', '19450212'),
('������', '����', NULL, 2000.00, '������', 789.00, '19780707', '3', '19780707'),
('��������', '������', '����������', 4800.00, '����', 321.00, '19800312', '3', '19800312'),
('��������', '������', '����������', 7000.00, '����', 654.00, '19740917', '3',  '19740917'),
('���������', '�������', '��������', 4000.00, '����', 987.00, '19661123', '3', '19661123'),
('', '', NULL, 4532.11, '�������', 544.00, '19681027', '8', '19681027'),
('', '', NULL, 4364.63, '�������', 321.00, '19630522', '8', '19630522'),
('���������', '������', '���������', 1569.00, '����', 147.00, '19660412', '4', '19660412'),
('��������', '��������', '���������', 3569.00, '����', 258.00, '19661023', '4', '19661023'),
('������', '����', NULL,	3000.00, '�����', 550.00, '19650523', '5', '19650523'),
('��������', '��������', '����������', 5000.00, '������', 350.00, '19630503', '5',  '19630503'),
('', '', NULL, 4743.00, '�������', 533.00, '19730919', '3', '19730919'),
('', '', NULL, 4855.00, '�������', 732.00, '19550318', '3', '19550318'),
('������', '������', '���������', 5698.265, '������', 357.00, '19780707', '5', '19780707'),
('��������', '��������', '�����������', 3698.2569, '������', 862.00, '19780707', '6', '19780707'),
('��������', '����', '���������', 2589.3214, '����', 3579.00, '19880707', '6', '19880707'),
('���������', '��������', '�����������', 4569.2365, '����', 501.00,'19560511', '8',  '19560511'),
('�������', '�������', NULL, 1478.2365, '����', 123.369, '19481018', '8', '19481018'),
('��������', '��������', '�����������', 2589.32, '����', 321.963, '19830307', '9', '19830307'),
('��������', '������', '�����������', 3698.3569, '����', 569.569, '19480712', '10', '19480712'),
('��������', '������', '�����������', 5698.321, '�����', 789.321, '19680107', '11', '19680107'),
('�������', '��������', '�����������', 5478.53, '�����', 789.546, '19051207', '11', '19051207')

INSERT INTO Student (Surname, Name, Patronymic, Birthday, RecordBook, BirthdayCity, StudyGroupId, Stipendia) VALUES
('������', '�����', '����������', '19891205', '��-11-01', '����', '1', 100),
('�������', '����', '����������', '19901106', '��-11-02', '���������', '1', 200),
('�������', '����', '����������', '19901007', '��-11-02', '����', '1', NULL),
('�����������', '������', '����������', '19900910', '��-12-01', '��������', '2', 300),
('�������', '�������', NULL, '19900714', '��-12-03', '����', '2', 200),
('�������', '��������', '��������', '19900714', '��-12-03', '������', '2', NULL),
('��������', '�����', '����������', '19920105', '��-23-01', '����', '3', NULL),
('�����������', '������', '�����������', '19910309', '��-23-02', '����', '3', 300),
('���������', '������', '��������', '19910512', '��-24-01', '��������', '4', 741),
('��������', '����', '��������', '19920723', '��-24-03', '����', '4', 300),
('����������', '������', NULL, '19940612', '��-24-04', '����', '4', 598),
('����������', '������', '��������', '19940612', '��-24-04', '����', '4', 985),
('���������', '�����', '��������', '19940612', '��-24-04', '����', '4', NULL),
('�������', '�������', '��������', '19900714', '��-12-12', '����', '2', 620),
('�������', '���������', '��������', '19900714', '��-12-12', '����', '2', NULL),
('�������', '��������', NULL, '19900714', '��-12-12', '������', '4', NULL),
('', '', NULL, '19790811', '��-12-14', '�������', '2', NULL),
('', '', NULL, '19800128', '��-12-15', '�������', '2', NULL),
('', '', NULL, '19810426', '��-12-16', '�������', '2', NULL),
('', '', NULL, '19820223', '��-12-17', '�������', '2', NULL),
('���������', '�����', '����������', '19901205', '��-11-01', '����', '1', 635),
('�������', '�����', '����������', '19871205', '��-11-01', '����', '1', 300),
('�������', '�����', '����������', '19901205', '��-11-01', '����', '1', 300),
('�������', '�����', '����������', '19901205', '��-11-01', '����', '1', 500),
('��������', '�����', NULL, '19901205', '��-11-01', '��������', '1', NULL),
('�������', '�����', '����������', '19901205', '��-11-01', '����', '1', NULL),
('��������', '����', NULL, '19901205', '��-11-01', '����', '1', 500),
('�����', '�����', '����������', '19901205', '��-11-01', '����', '1', 620),
('�����', '����', NULL, '19901205', '��-11-01', '����', '1', NULL),
('������', '�����', '����������', '19891206', '��-11-56', '����', '1', 130)

INSERT INTO Exam (Mark, DateExam, StudentId, DcDisciplineId, EmployeeId) VALUES
('5', '20130601', '1', '1', '1'),
('4', '20130601', '2', '1', '1'),
('3', '20130601', '3', '1', '2'),
('2', '20130601', '4', '1', '3'),
('5', '20130601', '17', '1', '3'),
('4', '20130601', '6', '1', '1'),
('3', '20130605', '1', '2', '2'),
('2', '20130605', '2', '2', '2'),
('4', '20130605', '3', '2', '20'),
('4', '20130605', '4', '2', '9'),
('3', '20130605', '17', '2', '1'),
('5', '20130605', '6', '2', '22'),
('3', '20130607', '1', '3', '3'),
('4', '20130607', '2', '3', '23'),
('4', '20130607', '3', '3', '23'),
('5', '20130607', '4', '3', '8'),
('4', '20130607', '17', '3', '8'),
('3', '20130607', '6', '3', '3'),
('4', '20130609', '1', '1', '4'),
('5', '20130609', '2', '4', '20'),
('3', '20130609', '3', '4', '8'),
('4', '20130609', '4', '4', '8'),
('3', '20130609', '17', '4', '9'),
('5', '20130609', '6', '4', '22'),
('5', '20130602', '7', '5', '8'),
('4', '20130602', '8', '5', '23'),
('3', '20130602', '9', '5', '1'),
('2', '20130602', '10', '5', '4'),
('3', '20130606', '7', '6', '15'),
('2', '20130606', '8', '6', '15'),
('4', '20130606', '9', '6', '6'),
('4', '20130606', '10', '6', '6'),
('3', '20130610', '7', '7', '7'),
('4', '20130610', '8', '7', '7'),
('4', '20130610', '9', '7', '7'),
('5', '20130601', '10', '7', '7'),
('4', '20130610', '7', '4', '4'),
('5', '20130610', '8', '4', '4'),
('3', '20130610', '9', '4', '4'),
('4', '20130610', '10', '4', '4'),
('5', '20130612', '7', '1', '8'),
('4', '20130612', '8', '1', '8'),
('3', '20130612', '9', '1', '8'),
('2', '20130612', '10', '1', '8'),
('4', '20130614', '7', '8', '4'),
('3', '20130614', '8', '8', '4'),
('5', '20130614', '9', '8', '4')
GO