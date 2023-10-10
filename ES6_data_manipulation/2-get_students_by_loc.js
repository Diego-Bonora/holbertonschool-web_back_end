export default function getStudentsByLocation(getListStudents, city) {
  let locationArray = [];
  if (getListStudents instanceof Array) {
    locationArray = getListStudents.filter((item) => item.location === city);
  }
  return locationArray;
}
