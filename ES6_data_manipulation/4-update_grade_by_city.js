/*eslint-disable */
export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
    const loc = getListStudents.filter(student => student.location === city);
  
    loc.map((student) => {
      const gradeEntry = newGrades.find(grade => grade.studentId === student.id);
      if (gradeEntry) {
        student.grade = gradeEntry.grade;
      } else {
        student.grade = 'N/A';
      }
    });
  
    return loc;
  }