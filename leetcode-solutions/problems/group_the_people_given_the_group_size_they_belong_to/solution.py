class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        maps = defaultdict(list)
        result = []
        for idx, val in enumerate(groupSizes):
            maps[val].append(idx)
            if len(maps[val]) == val:
                result.append(maps[val])
                maps[val] = []
        
        return result


        