class Solution:
    def majorityElement(self, a):
        a.sort()
        return a[len(a) // 2]
