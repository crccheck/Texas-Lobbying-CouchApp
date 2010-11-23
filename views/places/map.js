function(doc) {
  emit(doc.place.name.toLowerCase(), 1);
}
