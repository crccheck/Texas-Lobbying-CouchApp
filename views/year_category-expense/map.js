function(doc) {
  if (doc.type == 'cover'){
    var year = doc.report.year || 0;
    for (var type in doc.benefited){
      var amount = 0;
      if (amount = doc.benefited[type]){
          emit([+year, 2, type], +amount);
        }
    }
    for (var type in doc.expenses){
      var amount = 0;
      if (amount = doc.expenses[type]){
          emit([+year, 1, type], +amount);
        }
    }
  }
}
