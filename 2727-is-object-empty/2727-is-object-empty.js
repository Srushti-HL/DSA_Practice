var isEmpty = function(obj) {
    if (Array.isArray(obj)) {
        return obj.length === 0;
    }

    for (let key in obj) {
        return false;
    }

    return true;
};