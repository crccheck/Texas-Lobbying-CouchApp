function(doc) {
  location = {};
  if (doc.place.city) location.city = doc.place.city;
  if (doc.place.zip) location.zip = doc.place.zip.substr(0,5);
  emit(doc.place.name.toLowerCase(), location);
}
