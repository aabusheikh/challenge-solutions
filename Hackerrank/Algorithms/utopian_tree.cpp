#include <bits/stdc++.h>

using namespace std;

// Complete the utopianTree function below.
int utopianTree(int n) {
    int h = 1;
    bool f = true;
    while (n>0) {
        f? h *= 2 : ++h;
        f = !f;
        --n;
    }
    return h;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        int result = utopianTree(n);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
