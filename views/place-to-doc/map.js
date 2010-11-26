function (doc){
    if (doc.place) {
        var name = doc.place.name;
        name = name.toLowerCase().replace(/^the /, '').replace(/[^a-z0-9 ]/g, '');
        emit(name, doc);
    }
}
