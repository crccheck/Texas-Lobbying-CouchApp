function (keys, values){
    o = [0, 0, 0];
    values.forEach(function(x){
        o[0] += x[0];
        o[1] += x[1];
        o[2] += x[2];
        o[3]  = x[3];
    });
    return o;
}
