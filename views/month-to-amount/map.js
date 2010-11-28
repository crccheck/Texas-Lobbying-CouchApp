function(doc) {
  if (doc.place && doc.date && doc.amount) {
    var date = new Date(doc.date);
    var month = date.getMonth();
    if (month < 10) month = '0' + month;
    date = date.getYear() +""+ month;

    var name = doc.place.namefix || doc.place.name.toLowerCase().replace(/[^a-z0-9 ]/g,'').replace(/^\s*(the)?\s*|\s+$/g, '').replace(/\s{2,}/g,' ');

    emit([+date, name], +doc.amount);
  }
}
