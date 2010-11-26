function(doc) {
  if (doc.place.namefix) {
    var name = doc.place.name.toLowerCase().replace(/^the /, '').replace(/[^a-z0-9 ]/g, '');
    emit(name, doc.place.namefix);
  }
}
