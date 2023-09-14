export default function appendToEachArrayValue(array, appendString) {
  for (idx in array) {
    array[idx] = appendString + array[idx];
  }

  return array;
}
