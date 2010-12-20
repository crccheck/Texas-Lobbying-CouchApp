/*
 * Used for generating a list of all clients
 */

function slugify(text){
    text = text.toLowerCase().replace(/[^-a-z0-9\s]+/g, '');
    text = text.replace(/-+/g, "_");
    text = text.replace(/\s+/g, "-");
    return text;
}

function (doc){
    if (doc.client){
        for each (var c in doc.client){
            if (c.name){
                emit(
                     [c.identifier || slugify(c.name)],
                     [1, c.state, c.name]
                    );
            }
        }
    }
}
