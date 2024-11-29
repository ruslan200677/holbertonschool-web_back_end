// 10-update_uniq_items.js
export default function updateUniqueItems(map) {
    if (!(map instanceof Map)) {
      throw new Error("Cannot process");
    }
  
    map.forEach((value, key) => {
      if (value === 1) {
        map.set(key, 100);  // Update quantity to 100
      }
    });
  }
  