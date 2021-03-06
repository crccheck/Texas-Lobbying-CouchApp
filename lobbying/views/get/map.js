/*
 *  Generic view to help quickly "get" any type of document
 *  use reduce=false&include_docs=true if you're trying to get documents
 *  and group=true if you're getting quick stats
 */
function slugify(text){
    text = text.toLowerCase().replace(/[^-a-z0-9\s]+/g, '');
    text = text.replace(/-+/g, "_");
    text = text.replace(/\s+/g, "-");
    return text;
}

function (doc){
    if (doc.type){
        var key = [doc.type];
        switch (doc.type){
            case 'lobbyist':
                key.push(doc.lobbyist.id);
                key.push(doc.year || '');
                if (doc.client){
                    for each (var c in doc.client){
                        if (c.name){
                            emit(
                                 ['client', c.identifier || slugify(c.name)],
                                 1
                                );
                        }
                    }
                }
            break;
            case 'cover':
                key.push(doc.lobbyist.id);
                key.push(doc.report.year || '');
            break;
        }
        emit(key, 1);
    }
}
