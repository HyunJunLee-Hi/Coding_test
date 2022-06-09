from collections import deque
def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        cache = ["" for _ in range(cacheSize)]
        for city in cities:
            city = city.lower()
            if city in cache:
                answer += 1
                if len(cache):
                    cache.pop(cache.index(city))
                cache.append(city)
            else:
                answer += 5
                if len(cache) >= cacheSize:
                    if len(cache):
                        cache.pop(0)
                    cache.append(city)
                else:
                    cache.append(city)

    return answer