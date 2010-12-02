function(doc) {
  if (doc.type == 'cover'){
    for(var type in doc.expenses){
      var temp;
      if (temp = doc.expenses[type]){
          var date = doc.report.date.split('/');
          var year = +date[2];
          var month = +date[0] - 1;
          if (month == 0) {
            month = 12;
            --year;
          }
          emit([year, doc.lobbyist.id + " " + doc.lobbyist.name, type], +temp);
        }
    }
  }
}
