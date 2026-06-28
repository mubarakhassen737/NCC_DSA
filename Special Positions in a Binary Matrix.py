class Solution {
public:
    int numSpecial(vector<vector<int>>& a) {
        int x = a.size();
        int y = a[0].size();

        vector<int> p(x, 0), q(y, 0);

        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                if (a[i][j] == 1) {
                    p[i]++;
                    q[j]++;
                }
            }
        }

        int z = 0;

        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                if (a[i][j] == 1 && p[i] == 1 && q[j] == 1) {
                    z++;
                }
            }
        }

        return z;
    }
};
