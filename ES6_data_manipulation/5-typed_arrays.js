export default function createInt8TypedArray(length, position, value) {
  const arrBuff = new ArrayBuffer(length);
  const int8view = new Int8Array(arrBuff);
  if (position > length) {
    throw Error('Position outside range');
  } else {
    int8view[position] = value;
  }
  return new DataView(arrBuff);
}