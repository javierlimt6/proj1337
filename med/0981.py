class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # self.data.append((key, value, timestamp))
        # print(self.data)
        self.data[key] = self.data.get(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int):
        # low = 0
        # high = len(self.data) - 1
        # res = ""
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     if self.data[mid][2] > timestamp:
        #         high = mid - 1
        #     else:
        #         if self.data[mid][0] == key:
        #             res = self.data[mid][1]
        #         low = mid + 1
        # return res
        #FAILED
        #THINK about improving EVERYTHING.
        #use dictionary to handle and make data retrieval easier
        entries = self.data.get(key, [])
        low = 0
        if not entries or entries[0][0] > timestamp:
            return ""
        high = len(entries) - 1
        mid = None
        while low <= high:
            mid = low + (high - low) // 2
            if timestamp < entries[mid][0]:
                high = mid - 1
            else:
                low = mid + 1
        if mid == None:
            return ""
        return entries[high][1] #pointing to the rightmost element
    
        #PASSED after 2x perplexity prompts, need to know that high provides the right 
        #most possible answer for "range" questions
        #so in range questions, return high or low, not mid
            

timeMap = TimeMap();
timeMap.set("foo", "bar", 1);  
print(timeMap.get("foo", 1))        
timeMap.get("foo", 3);         
timeMap.set("foo", "bar2", 4); 
timeMap.get("foo", 4);         
timeMap.get("foo", 5);         
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)