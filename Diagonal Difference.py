## Given a square matrix, calculate the absolute difference between the sums of its diagonals.
## in python
def diagonalDifference(arr):
    a =0
    b=0
    length = len(arr[0])
    for count in range(length):
        a += arr[count][count]
        b += arr[count][(length-count-1)]
    return abs(a-b)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    result = diagonalDifference(arr)
    print(result)
   
   
   
   
 '''
 // in c++  
#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[n][n];

    long long int a=0;
    long long int b=0; 

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
            if (i == j) a += arr[i][j];
            if (i == n - j - 1) b += arr[i][j];
        }
    }

    cout << abs(a- b) << endl; 
    return 0;
}
'''
