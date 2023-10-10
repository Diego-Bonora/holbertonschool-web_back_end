export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  let locationArray = [];
  if (getListStudents instanceof Array) {
    locationArray = getListStudents.filter((item) => item.location === city);
    for (const item in locationArray) {
      locationArray[item].grade = 'N/A';
    }
    locationArray.map((item) => newGrades.map((student) => {
      if (item.id === student.studentId) item.grade = student.grade;
      return null;
    }));
  }
  return locationArray;
}
