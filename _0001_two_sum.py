class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # A fancy way to say dictionary
        for i in range(len(nums)):
            me_needs = target - nums[i] # Looking for Clark Kent
            if me_needs in hashmap:
                return [hashmap[me_needs], i] # Lois Lane ladies and gentlemen
            hashmap.update({nums[i]: i}) # We got Clark Kent on the menu boys
        return [] # Got to take care if Luthor got Miss Lane
