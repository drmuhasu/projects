struct grades {
    char *courseName;
    int courseGrade;
    float courseCredit;
    struct grades *nextCourse;
};

struct student {
    char *name;
    int id;
    struct grades *courses;
    float gpa;
    struct student *next;
};

struct student *searchStudent(struct student *list, int studentID);
struct student *updateGPA(struct student *list, int studentID);
struct grades *createCourse(char *courseName, int courseGrade, float courseCredit);
struct student *insertCourse(struct student *list, int studentID, char *name, int grade, float credit);
struct student *deleteCourse(struct student *list, int studentID, char *courseName);
struct student *updateCourseGrade(struct student *list, int studentID, char *courseName, int newGrade);
struct student *createStudent(char *name, int id);
struct student *insertStudent(struct student *list, char *studentName, int studentID);
struct student *deleteStudent(struct student *list, int studentID);
void printStudent(struct student *student);
void printAllStudents(struct student *list);
void freeList(struct student *list);
