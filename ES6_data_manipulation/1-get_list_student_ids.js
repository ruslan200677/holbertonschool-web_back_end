/*eslint-disable */
export default function getListStudentIds(getListStudents) {
    if (Array.isArray(getListStudents)) 
      return (getListStudents.map((obj) => obj.id));
    return [];
  }