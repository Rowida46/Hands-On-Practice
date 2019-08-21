#include<iostream>
using namespace std;
template <class type1 , class type2 >
#include<string>
// function templete >------------ mostafa saad scratch playlist video 12 
type1 Max ( type1 a, type2 b ){
	return a > b ? a : b ;
	//return max ;
} 
void static_test( static int f){
	static int h = f ;
	cout<< ++h;
}


int main(){
	//	cout<<Max(3 , 4.7 ) <<endl; // output >----4 cuz this function return type matching with the type of the first element
	//	cout<<Max(7.8 , 9.2);  // output >-- 9.2
		
		static_test(4);
				static_test(4);

		
}
