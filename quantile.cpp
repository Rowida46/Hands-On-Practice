#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int median(vector<int> a) {
    int n = a.size();
    
    int m = a[n / 2];
    
    if (! (n & 1)) {
        m += a[n / 2 - 1];
        m /= 2;
    }
    
    return m;
}

int main() {
    int n;
    cin >> n;
    
    vector<int> a(n);
    
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    sort(begin(a), end(a));
    
    vector<int> l;
    vector<int> u;
    
    if (n & 1) {
        for (int i = 0; i < (n / 2); i++) {
            l.push_back(a[i]);
        }
        
        for (int i = (n / 2) + 1; i < n; i++) {
            u.push_back(a[i]);
        }
    } else {
        for (int i = 0; i < (n / 2); i++) {
            l.push_back(a[i]);
        }
        
        for (int i = (n / 2); i < n; i++) {
            u.push_back(a[i]);
        }
    }
    
    cout << median(l) << endl;
    cout << median(a) << endl;
    cout << median(u) << endl;
    
    return 0;
}
