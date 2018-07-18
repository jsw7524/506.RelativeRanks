class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        lenNums=len(nums)
        sortedNums=[ [s,str(i)] for (i,s) in zip(range(1,lenNums+1),sorted(nums,reverse=True))]
        if (lenNums>=1):
            sortedNums[0][1]="Gold Medal"
        if (lenNums>=2):
            sortedNums[1][1]="Silver Medal"
        if (lenNums>=3):
            sortedNums[2][1]="Bronze Medal"
        dictSortedNums={ s[0]:s[1] for s in sortedNums}
        return [dictSortedNums[n] for n in nums]


sln =Solution()
print(sln.findRelativeRanks([10,3,8,9,4]))
