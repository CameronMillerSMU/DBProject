-- Department Table
CREATE TABLE IF NOT EXISTS Department (
    DepartmentCode VARCHAR(4) UNIQUE,
    DepartmentName VARCHAR(255) UNIQUE, -- made this unique
    PRIMARY KEY (DepartmentCode)
);

-- Faculty Table
CREATE TABLE IF NOT EXISTS Faculty (
    FacultyID VARCHAR(10) UNIQUE,
    FacultyName VARCHAR(255),
    FacultyEmail VARCHAR(255),
    FacultyRank VARCHAR(20), -- full, associate, assistant, adjunct
    DepartmentCode VARCHAR(4),
    PRIMARY KEY (FacultyID),
    FOREIGN KEY (DepartmentCode) REFERENCES Department(DepartmentCode),
    CHECK (FacultyRank IN ('Full', 'Associate', 'Assistant', 'Adjunct'))
);

-- Program Table
CREATE TABLE IF NOT EXISTS Program (
    ProgramName VARCHAR(255) UNIQUE,
    ProgramCoordinatorID VARCHAR(10), 
    DepartmentCode VARCHAR(4), -- added DepartmentCode
    PRIMARY KEY (ProgramName),
    FOREIGN KEY (ProgramCoordinatorID) REFERENCES Faculty(FacultyID), -- added foreign key for ProgramCoordinatorID
    FOREIGN KEY (DepartmentCode) REFERENCES Department(DepartmentCode) -- added foreign key for DepartmentCode
);

-- Course Table
CREATE TABLE IF NOT EXISTS Course (
    CourseID VARCHAR(8) UNIQUE, -- combo of dept_code and 4 digit num
    CourseTitle VARCHAR(255),
    CourseDescription TEXT,
    DepartmentCode VARCHAR(4),
    PRIMARY KEY (CourseID),
    FOREIGN KEY (DepartmentCode) REFERENCES Department(DepartmentCode)
);

-- Section Table
CREATE TABLE IF NOT EXISTS Section (
    SectionID INT AUTO_INCREMENT, -- 001 to 999
    CourseID VARCHAR(8),
    SemesterName VARCHAR(20),
    CourseYear YEAR,
    FacultyID VARCHAR(10),
    StudentsEnrolled INT,
    PRIMARY KEY (SectionID, CourseID), -- added CourseID to key
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID),
    CHECK (SemesterName IN ('Fall', 'Spring', 'Summer'))
);

-- LearningObjective Table
CREATE TABLE IF NOT EXISTS LearningObjective (
    ObjectiveCode VARCHAR(10) UNIQUE, -- user can enter it, or else, the system should assign an automatic one
    ObjectiveDescription TEXT,
    PRIMARY KEY (ObjectiveCode)
);

-- SubObjective Table - added new table 
CREATE TABLE IF NOT EXISTS SubObjective (
    SubObjectiveCode VARCHAR(10) UNIQUE, --  labelled with code.1, code.2, code.3 ..., where code is the code of the LO
    SubObjectiveDescription TEXT,
    ObjectiveCode VARCHAR(10),
    PRIMARY KEY (SubObjectiveCode),
    FOREIGN KEY (ObjectiveCode) REFERENCES LearningObjective(ObjectiveCode)
);

-- ProgramCourse Table
CREATE TABLE IF NOT EXISTS ProgramCourse (
    CourseID VARCHAR(8),
    ProgramName VARCHAR(255),
    PRIMARY KEY (ProgramName),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    FOREIGN KEY (ProgramName) REFERENCES Program(ProgramName)
);
-- CourseEval Table 
CREATE TABLE IF NOT EXISTS CourseEval (
    CourseID VARCHAR(8),
    ProgramName VARCHAR(255),
    ObjectiveCode VARCHAR(10),
    PRIMARY KEY (CourseID, ProgramName),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    FOREIGN KEY (ProgramName) REFERENCES Program(ProgramName),
    FOREIGN KEY (ObjectiveCode) REFERENCES LearningObjective(ObjectiveCode)
);

-- SectionEval Table
CREATE TABLE IF NOT EXISTS SectionEval (
    SectionID INT,
    CourseID VARCHAR(8),
    ProgramName VARCHAR(255),
    ObjectiveCode VARCHAR(10),
    EvalType VARCHAR(255),
    StudentsMetObj INT,
    PRIMARY KEY (SectionID, CourseID, ProgramName),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    FOREIGN KEY (ProgramName) REFERENCES Program(ProgramName),
    FOREIGN KEY (ObjectiveCode) REFERENCES LearningObjective(ObjectiveCode)
);

-- ProgramObjective Table
CREATE TABLE IF NOT EXISTS ProgramObjective (
    ProgramName VARCHAR(255),
    ObjectiveCode VARCHAR(10),
    PRIMARY KEY (ProgramName),
    FOREIGN KEY (ProgramName) REFERENCES Program(ProgramName),
    FOREIGN KEY (ObjectiveCode) REFERENCES LearningObjective(ObjectiveCode)
);

-- ProgramCourses Table 
-- CREATE TABLE IF NOT EXISTS ProgramCourses (
--     ProgramName VARCHAR(255) UNIQUE,
--     CourseID VARCHAR(8),
--     ObjectiveCode VARCHAR(10),
--     ObjYear YEAR,
--     PRIMARY KEY (ProgramName, CourseID),
--     FOREIGN KEY (ProgramName) REFERENCES Programs(ProgramName),
--     FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
--     FOREIGN KEY (ObjectiveCode) REFERENCES LearningObjectives(ObjectiveCode)
-- );


-- progran, course pair - primary key 
-- need to know all objectives associated with it
-- for each section of that specific 



-- SectionObjectives Table
-- CREATE TABLE IF NOT EXISTS SectionObjectives (
--     SectionID INT,
--     CourseID VARCHAR(8), -- added this 
--     ObjectiveCode VARCHAR(10),
--     EvaluationMethod VARCHAR(255),
--     StudentsMetObjective INT,
--     PRIMARY KEY (SectionID, CourseID, ObjectiveCode), -- added CourseID to key
--     FOREIGN KEY (SectionID) REFERENCES CourseSections(SectionID),
--     FOREIGN KEY (CourseID) REFERENCES Courses(CourseID), -- added foreign key for Course ID 
--     FOREIGN KEY (ObjectiveCode) REFERENCES LearningObjectives(ObjectiveCode)
-- );

-- might needed another table to keep track all the course required for each program 
-- (from the Project document) 
--      For each program, there are a set of courses that is associated with it that will be used for evaluation.
--      For example, for the CS program, it may be the course CS 1100, CS 1200, CS 1300. And for Computer
--      Engineering it will be CS 1100, CE 1100, CE 2200. Notice that a course may be associated with multiple programs

