class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        result = ""
        sspace = self.store[key]
        l, r = 0, len(sspace)-1
        while l <= r:
            mid = (l + r) // 2
            #if sspace[mid][1] == timestamp:
            #    return sspace[mid][0]
            if timestamp >= sspace[mid][1]:
                result = sspace[mid][0]
                l = mid + 1
            else:
                r = mid - 1
                
        return result

        
         
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)