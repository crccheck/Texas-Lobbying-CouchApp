function(doc, req){
    if (doc) {
    var body = '';
    body += '<h1>' + doc.lobbyist.name + '</h1>'
        + "<h2>Clients</h2>";
    + '<ul>';
    doc.client.forEach(function(client){
        body += '<li>'+client.name
        + client.compensation.type
        + ' $' + client.compensation.low + ' to $'
        + client.compensation.high
        +'</li>';
    });
    body += '</ul>';
    delete doc._revisions;
    delete doc._id;
    delete doc._rev;
    body += '<pre>' + JSON.stringify(doc) + '</pre>';
    return {
        body: body
    }
    } else {
        return {
            body: 'Does Not Exist'
        }
    }
}
