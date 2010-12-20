/*
 * this is derived from lobbyist-expense/map.js
 * the keys order prioritizes year
 * we only use up to group_level=3
 */
function(doc) {
  if (doc.type == 'cover'){
    var year = doc.report.year || 0;
    for (var type in doc.benefited){
      var amount;
      if (amount = doc.benefited[type]){
          emit([+year, doc.lobbyist.id, 2, type], +amount);
        }
    }
    for (var expenseType in doc.expenses){
      var expenseAmount;
      if (expenseAmount = doc.expenses[expenseType]){
          emit([+year, doc.lobbyist.id, 1, expenseType], +expenseAmount);
        }
    }
  }
}
