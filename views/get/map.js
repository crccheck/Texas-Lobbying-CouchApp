function (doc){
    if (doc.type){
        var key = [doc.type];
        switch (doc.type){
            case 'lobbyist':
                key.push(doc.lobbyist.id);
                key.push(doc.year || '');
            break;
            case 'cover':
                key.push(doc.lobbyist.id);
                key.push(doc.report.year || '');
            break;
        }
        emit(key, doc);
    }
}
