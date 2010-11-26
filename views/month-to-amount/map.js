function(doc) {
  if (doc.place) {
    var date = new Date(doc.date);
    var month = date.getMonth();
    if (month < 10) month = '0' + month;
    emit(date.getYear() +""+ month, +doc.amount);
  }
}
