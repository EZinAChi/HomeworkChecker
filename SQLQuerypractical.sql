CREATE TABLE Students
(studentID INT IDENTITY,
email VARCHAR(MAX) NOT NULL, 
password VARCHAR(MAX) NOT NULL,
firstName VARCHAR(50) NOT NULL,
lastName VARCHAR(50) NOT NULL,
CONSTRAINT pk_Students PRIMARY KEY (studentID));


CREATE TABLE Teacher
(teacherID INT IDENTITY,
email VARCHAR(MAX) NOT NULL, 
password VARCHAR(MAX) NOT NULL,
firstName VARCHAR(50) NOT NULL,
lastName VARCHAR(50) NOT NULL,
CONSTRAINT pk_Teacher PRIMARY KEY (teacherID));

CREATE TABLE Practical
(practicalID INT IDENTITY,
 question VARCHAR(MAX) NOT NULL,
CONSTRAINT pk_Practical PRIMARY KEY (practicalID));

 

CREATE TABLE Question
(questionID INT IDENTITY,
 question VARCHAR(MAX) NOT NULL,
 answer VARCHAR(MAX) NOT NULL,
 mark INT NOT NULL,
CONSTRAINT pk_Question PRIMARY KEY (questionID));
 
 CREATE TABLE Deduction
(questionID INT ,
 deductMark INT NOT NULL,
CONSTRAINT fk_DeductionQuestion FOREIGN KEY (questionID) REFERENCES Question);
 

  CREATE TABLE Answer
(studentID INT,
questionID INT,
StudentAnswer  VARCHAR(MAX) NOT NULL,
CONSTRAINT fk_AnswerStudents FOREIGN KEY (studentID) REFERENCES Students);
CONSTRAINT fk_AnswerQuestion FOREIGN KEY (questionID) REFERENCES Question);

CREATE TABLE Result
(studentID INT,
questionID INT,
totalMark INT,
CONSTRAINT fk_ResultStudents FOREIGN KEY (studentID) REFERENCES Students);
CONSTRAINT fk_ResultQuestion FOREIGN KEY (questionID) REFERENCES Question);

CREATE TABLE  Feedback
(feedBackID INT IDENTITY,
feedBack VARCHAR(MAX) ,
studentID,
questionID,
CONSTRAINT fk_FeedbackStudents FOREIGN KEY (studentID) REFERENCES Students);
CONSTRAINT fk_FeedbackQuestion FOREIGN KEY (questionID) REFERENCES Question);

 