function (doc){
    var second = '';
    switch (doc.type){
        case 'lobbyist':
            second = doc.lobbyist.id;
        break;
    }
    emit([doc.type, second]. doc);
}
