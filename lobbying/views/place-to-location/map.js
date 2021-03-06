function(doc) {
    if (doc.place){
        var location = {};
        var name = doc.place.name;
        if (doc.place.city) location.city = doc.place.city;
        if (doc.place.zip) location.zip = doc.place.zip.substr(0,5);
        name = name.toLowerCase().replace(/[^a-z0-9 ]/g,'').replace(/^\s*(the)?\s*|\s+$/g, '').replace(/\s{2,}/g,' ');
        emit(name, location);
    }
}
