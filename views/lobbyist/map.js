function(doc) {
    if (doc.type == 'lobbyist'){
        emit(doc.lobbyist.id, doc.lobbyist.name);
    }
}
