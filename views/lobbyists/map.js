function(doc) {
  if (doc.type == 'cover'){
    var first = doc.lobbyist.first, last = doc.lobbyist.last, name = doc.lobbyist.name;
    if (!(first && last)) {
      var split = name.split(', ');
      if (split.length == 2){
        out = split;
        out.push(name);
      } else {
        out = [name];
      }
    } else {
      out = [last, first];
    }
    emit(doc.lobbyist.id, out);
  }
}
