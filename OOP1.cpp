#include<iostream>
#include <iostream>
#include <windows.h>
using namespace std;
class shape {
	public :
	 void sh1 (int x){


		for(int a=x ; a>=1 ; a--){
			for(int b=x-1 ; b>=a; b--)
			cout<<" ";
			for(int c=1 ; c<=a ; c++)
{           system("Color 7D");  // first 0 = black background second A = light green
			cout<<"*";

}
			cout<<endl;
		}
	}
};
int main(){
	int x; cin>>x;
	shape choise_ur_shape ;
	
	choise_ur_shape.sh1(x);
}
