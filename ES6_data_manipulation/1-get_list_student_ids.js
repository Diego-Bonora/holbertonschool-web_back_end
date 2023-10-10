export default function getListStudentIds(getListStudents) {
  let newArray = [];

  if (getListStudents instanceof Array) {
    newArray = getListStudents.map((item) => item.id);
  }

  return newArray;
}
