function (doc){
    if (doc.place) {
        var name = doc.place.name;
        name = name.toLowerCase().replace(/[^a-z0-9 ]/g,'').replace(/^\s*(the)?\s*|\s+$/g, '').replace(/\s{2,}/g,' ');
        emit(name, doc);
    }
}
