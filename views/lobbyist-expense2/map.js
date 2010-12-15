function(doc) {
    if (doc.amount){
        var date = new Date(doc.date);
        date = date ? Math.ceil(+date/1e6) : 0;
        emit([doc.lobbyist.id, +doc.year, date], +doc.amount)
    }
}
