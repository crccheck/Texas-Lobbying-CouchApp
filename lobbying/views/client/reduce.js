function (keys, values){
    o = [0, ''];
    values.forEach(function(x){
        o[0] += x[0];
        if (x[1]) o[1] = x[1];
        o[2]  = x[2];
    });
    return o;
}

