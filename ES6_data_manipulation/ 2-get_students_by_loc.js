/*eslint-disable */
export default function getStudentsByLocation(getListStudents, city) {
    if(Array.isArray(getListStudents))
      return (getListStudents.filter(obj => obj.location === city));
    return [];
  }