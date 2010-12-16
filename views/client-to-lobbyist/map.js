/*
 *  Used to generate a list of all lobbyists associated with a client
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
                var key = [client.identifier || slugify(client.name), doc.year];
                var value = {client: client, lobbyist: doc.lobbyist.id};
                emit(key, value);
            }
        }
    }
}
