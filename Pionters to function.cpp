#include<iostream>
using namespace std;
int sum (int a, int b ){
	return a+b ;
}
				//int (*fuc )(int , int )
 
int comp ( int A , int B , int (*fuc )(int , int ) ){
	return  (*fuc )(A , B ) ;
 
}
int main(){
	int x,y;
	cin>>x>>y;
     cout<<comp(x,y,sum) ;
	}
