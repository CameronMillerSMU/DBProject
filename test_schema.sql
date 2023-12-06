-- Departments Table
CREATE TABLE IF NOT EXISTS Departments (
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
    FOREIGN KEY (DepartmentCode) REFERENCES Departments(DepartmentCode),
    CHECK (FacultyRank IN ('Full', 'Associate', 'Assistant', 'Adjunct'))
);

-- Programs Table
CREATE TABLE IF NOT EXISTS Programs (
    ProgramName VARCHAR(255) UNIQUE,
    ProgramCoordinatorID VARCHAR(10), 
    DepartmentCode VARCHAR(4), -- added DepartmentCode
    PRIMARY KEY (ProgramName),
    FOREIGN KEY (ProgramCoordinatorID) REFERENCES Faculty (FacultyID), -- added foreign key for ProgramCoordinatorID
    FOREIGN KEY (DepartmentCode) REFERENCES Departments (DepartmentCode) -- added foreign key for DepartmentCode
);

-- Courses Table
CREATE TABLE IF NOT EXISTS Courses (
    CourseID VARCHAR(8) UNIQUE,
    CourseTitle VARCHAR(255),
    CourseDescription TEXT,
    DepartmentCode VARCHAR(4),
    PRIMARY KEY (CourseID),
    FOREIGN KEY (DepartmentCode) REFERENCES Departments(DepartmentCode)
);

-- CourseSections Table
CREATE TABLE IF NOT EXISTS CourseSections (
    SectionID INT AUTO_INCREMENT,
    CourseID VARCHAR(8),
    SemesterName VARCHAR(20),
    courseYear YEAR,
    FacultyID VARCHAR(10),
    StudentsEnrolled INT,
    PRIMARY KEY (SectionID, CourseID), -- added CourseID to key
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID)
);

-- LearningObjectives Table
CREATE TABLE IF NOT EXISTS LearningObjectives (
    ObjectiveCode VARCHAR(10), -- removed unique  
    ObjectiveDescription TEXT,
    ProgramName VARCHAR(255),
    PRIMARY KEY (ObjectiveCode, ProgramName),
    FOREIGN KEY (ProgramName) REFERENCES Programs(ProgramName)
);

-- SubObjectives Table - added new table 
CREATE TABLE IF NOT EXISTS SubObjectives (
    SubObjectiveCode VARCHAR(10),
    SubObjectiveDescription TEXT,
    ProgramName VARCHAR(255),
    ObjectiveCode VARCHAR(10),
    PRIMARY KEY (SubObjectiveCode, ObjectiveCode, ProgramName),
    FOREIGN KEY (ProgramName) REFERENCES Programs(ProgramName),
    FOREIGN KEY (ObjectiveCode) REFERENCES LearningObjectives(ObjectiveCode)
);

-- ProgramObjectives Table - not needed 
-- CREATE TABLE IF NOT EXISTS ProgramObjectives (
--     ProgramName VARCHAR(255),
--     ObjectiveCode VARCHAR(10),
--     PRIMARY KEY (ProgramName, ObjectiveCode),
--     FOREIGN KEY (ProgramName) REFERENCES Programs(ProgramName),
--     FOREIGN KEY (ObjectiveCode) REFERENCES LearningObjectives(ObjectiveCode)
-- );

-- SectionObjectives Table
CREATE TABLE IF NOT EXISTS SectionObjectives (
    SectionID INT,
    CourseID VARCHAR(8), -- added this 
    ObjectiveCode VARCHAR(10),
    EvaluationMethod VARCHAR(255),
    StudentsMetObjective INT,
    PRIMARY KEY (SectionID, CourseID, ObjectiveCode), -- added CourseID to key
    FOREIGN KEY (SectionID) REFERENCES CourseSections(SectionID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID), -- added foreign key for Course ID 
    FOREIGN KEY (ObjectiveCode) REFERENCES LearningObjectives(ObjectiveCode)
);

-- might needed another table to keep track all the course required for each program 
-- (from the Project document) 
--      For each program, there are a set of courses that is associated with it that will be used for evaluation.
--      For example, for the CS program, it may be the course CS 1100, CS 1200, CS 1300. And for Computer
--      Engineering it will be CS 1100, CE 1100, CE 2200. Notice that a course may be associated with multiple programs

-- ProgramCourses Table 
-- CREATE TABLE IF NOT EXISTS ProgramCourses (
--     ProgramName VARCHAR(255) UNIQUE,
--     CourseID VARCHAR(8),
-- );