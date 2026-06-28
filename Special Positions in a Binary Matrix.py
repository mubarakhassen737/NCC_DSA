class Solution:
    def numSpecial(self, a):
        c = 0

        for i in range(len(a)):
            for j in range(len(a[0])):

                if a[i][j] == 1:

                    x = 0
                    y = 0

                    for k in range(len(a[0])):
                        if a[i][k] == 1:
                            x += 1

                    for k in range(len(a)):
                        if a[k][j] == 1:
                            y += 1

                    if x == 1 and y == 1:
                        c += 1

        return c
