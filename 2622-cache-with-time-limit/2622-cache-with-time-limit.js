var TimeLimitedCache = function() {
    this.cache = new Map();
};

TimeLimitedCache.prototype.set = function(key, value, duration) {
    const currentTime = Date.now();

    let existed = false;

    if (this.cache.has(key)) {
        const oldData = this.cache.get(key);

        if (oldData.expiry > currentTime) {
            existed = true;
        }
    }

    this.cache.set(key, {
        value: value,
        expiry: currentTime + duration
    });

    return existed;
};

TimeLimitedCache.prototype.get = function(key) {
    const currentTime = Date.now();

    if (!this.cache.has(key)) {
        return -1;
    }

    const data = this.cache.get(key);

    if (data.expiry <= currentTime) {
        this.cache.delete(key);
        return -1;
    }

    return data.value;
};

TimeLimitedCache.prototype.count = function() {
    const currentTime = Date.now();
    let count = 0;

    for (const [key, data] of this.cache) {
        if (data.expiry > currentTime) {
            count++;
        } else {
            this.cache.delete(key);
        }
    }

    return count;
};