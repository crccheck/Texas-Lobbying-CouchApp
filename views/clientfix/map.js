/*
 * Used for the clientfix tool to clean dirty data
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
            if (c.identifier){
                emit(
                     slugify(c.name),
                     c.identifier
                    );
            }
        }
    }
}
