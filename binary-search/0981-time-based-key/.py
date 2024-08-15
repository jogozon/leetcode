class TimeMap:

    def __init__(self):
        self.tmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
            self.tmap[key] = []
        self.tmap[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.tmap.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp: # just check the time stamp in the value
                res = values[m][0] # keeps running until the most current one is found that is less than time stamp
                l = m + 1
            else:
                r = m - 1
        return res