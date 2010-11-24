function(doc) {
    if (doc.place) {
        var name = doc.place.namefix || doc.place.name;
        name = name.replace(/^the /i,'').toLowerCase();
        emit(name, 1);
    }
}
