class Solution:
    def missingNumber(self, a):
        a.sort()

        for i in range(len(a)):
            if a[i] != i:
                return i

        return len(a)
