function(doc) {
  if (doc.date && doc.amount) {
    var date = new Date(doc.date);
    var month = date.getMonth();
    if (month < 10) month = '0' + month;
    date = date.getYear() +""+ month;

    var name = '';
    if (doc.place){
        name = doc.place.namefix || doc.place.name.toLowerCase().replace(/[^a-z0-9 ]/g,'').replace(/^\s*(the)?\s*|\s+$/g, '').replace(/\s{2,}/g,' ');
    } else {
        name = doc[doc.type];
    }
    emit([+date, doc.type, name], +doc.amount);
  }
}
