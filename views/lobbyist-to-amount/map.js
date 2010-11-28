function(doc) {
    if (doc.amount){
        emit([doc.lobbyist.id, doc.lobbyist.name], +doc.amount)
    }
}
