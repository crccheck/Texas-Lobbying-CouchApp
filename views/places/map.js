function(doc) {
    if (doc.place) {
        var name = doc.place.namefix || doc.place.name;
        name = name.toLowerCase().replace(/^the /, '').replace(/[^a-z0-9 ]/g, '');
        emit(name, 1);
    }
}
