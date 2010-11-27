function(doc) {
  if (doc.place.namefix) {
    var name = doc.place.name.toLowerCase().replace(/^\s*(the)?\s*| +$/g, '').replace(/[^a-z0-9 ]/g, '').replace(/\s{2,}/g,' ');
    emit(name, doc.place.namefix);
  }
}
