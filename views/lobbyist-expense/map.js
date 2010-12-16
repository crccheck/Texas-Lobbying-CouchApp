/*
 *  This is used to build graphs of a lobbyist's spending from year to year
 */
function(doc) {
  if (doc.type == 'cover'){
    var year = doc.report.year || 0;
    for (var type in doc.benefited){
      var amount;
      if (amount = doc.benefited[type]){
          emit([doc.lobbyist.id, +year, 2, type], +amount);
        }
    }
    for (var expenseType in doc.expenses){
      var expenseAmount;
      if (expenseAmount = doc.expenses[expenseType]){
          emit([doc.lobbyist.id, +year, 1, expenseType], +expenseAmount);
        }
    }
  }
}
