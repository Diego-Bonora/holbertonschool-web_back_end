export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    new_array.push(appendString + idx);
  }

  return new_array;
}
