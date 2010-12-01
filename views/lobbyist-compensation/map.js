function(doc) {
    if (doc.type == 'lobbyist'){
        for each (var client in doc.client){
            emit([doc.lobbyist.id, client.name], +client.compensation.low);
        }
    }
}
