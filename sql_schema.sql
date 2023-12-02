-- Programs Table
CREATE TABLE Programs (
    ProgramName VARCHAR(255) UNIQUE,
    ProgramCoordinatorID VARCHAR(10),
    ProgramCoordinatorName VARCHAR(255),
    ProgramCoordinatorEmail VARCHAR(255),
    PRIMARY KEY (ProgramName)
);

-- Departments Table
CREATE TABLE Departments (
    DepartmentCode VARCHAR(4) UNIQUE,
    DepartmentName VARCHAR(255),
    PRIMARY KEY (DepartmentCode)
);

-- Faculty Table
CREATE TABLE Faculty (
    FacultyID VARCHAR(10) UNIQUE,
    FacultyName VARCHAR(255),
    FacultyEmail VARCHAR(255),
    FacultyRank VARCHAR(20),
    DepartmentCode VARCHAR(4),
    PRIMARY KEY (FacultyID),
    FOREIGN KEY (DepartmentCode) REFERENCES Departments(DepartmentCode)
);

-- Courses Table
CREATE TABLE Courses (
    CourseID VARCHAR(8) UNIQUE,
    CourseTitle VARCHAR(255),
    CourseDescription TEXT,
    DepartmentCode VARCHAR(4),
    PRIMARY KEY (CourseID),
    FOREIGN KEY (DepartmentCode) REFERENCES Departments(DepartmentCode)
);

-- Semesters Table
CREATE TABLE Semesters (
    SemesterID INT AUTO_INCREMENT,
    SemesterName VARCHAR(20),
    PRIMARY KEY (SemesterID)
);

-- CourseSections Table
CREATE TABLE CourseSections (
    SectionID INT AUTO_INCREMENT,
    CourseID VARCHAR(8),
    SemesterID INT,
    FacultyID VARCHAR(10),
    StudentsEnrolled INT,
    PRIMARY KEY (SectionID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (SemesterID) REFERENCES Semesters(SemesterID),
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID)
);

-- LearningObjectives Table
CREATE TABLE LearningObjectives (
    ObjectiveCode VARCHAR(10) UNIQUE,
    ObjectiveDescription TEXT,
    PRIMARY KEY (ObjectiveCode)
);

-- ProgramObjectives Table
CREATE TABLE ProgramObjectives (
    ProgramName VARCHAR(255),
    ObjectiveCode VARCHAR(10),
    PRIMARY KEY (ProgramName, ObjectiveCode),
    FOREIGN KEY (ProgramName) REFERENCES Programs(ProgramName),
    FOREIGN KEY (ObjectiveCode) REFERENCES LearningObjectives(ObjectiveCode)
);

-- SectionObjectives Table
CREATE TABLE SectionObjectives (
    SectionID INT,
    ObjectiveCode VARCHAR(10),
    EvaluationMethod VARCHAR(255),
    StudentsMetObjective INT,
    PRIMARY KEY (SectionID, ObjectiveCode),
    FOREIGN KEY (SectionID) REFERENCES CourseSections(SectionID),
    FOREIGN KEY (ObjectiveCode) REFERENCES LearningObjectives(ObjectiveCode)
);
