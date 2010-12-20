/*
 * This is used to get the top spending interests in a year
 */
function slugify(text){
    text = text.toLowerCase().replace(/[^-a-z0-9\s]+/g, '');
    text = text.replace(/-+/g, "_");
    text = text.replace(/\s+/g, "-");
    return text;
}

function(doc) {
    if (doc.type == 'lobbyist'){
        for each (var client in doc.client){
            if (client.name){
                var key = [doc.year, client.identifier || slugify(client.name)];
                var value = [Math.round(+client.compensation.low),
                             Math.round(+client.compensation.high),
                             1,
                             client.name];
                emit(key, value);
            }
        }
    }
}
