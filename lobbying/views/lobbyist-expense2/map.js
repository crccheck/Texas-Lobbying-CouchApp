/*
 * Use this to generate a list of detailed expenses for a lobbyist if that
 * lobbyist has filed any detailed expenses. This isn't very reliable since
 * they aren't required to files these. "expense" uses amounts from the cover
 * sheet, which are much more reliable but don't have a lot of details
 */

function(doc) {
    if (doc.amount){
        var date = new Date(doc.date);
        date = date ? Math.ceil(+date/1e6) : 0;
        emit([doc.lobbyist.id, +doc.year, date], +doc.amount)
    }
}
