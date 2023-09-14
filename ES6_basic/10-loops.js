export default function appendToEachArrayValue(array, appendString) {
  for (idx of array) {
    array[idx] = appendString + array[idx];
  }

  return array;
}
