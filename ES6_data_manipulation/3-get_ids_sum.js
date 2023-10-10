export default function getStudentIdsSum(getListStudents) {
  let newArray = [];

  if (getListStudents instanceof Array) {
    newArray = getListStudents.map((item) => item.id);
  }

  const value = newArray.reduce((total, num) => total + num, 0);
  return value;
}
