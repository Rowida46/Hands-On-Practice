#include<iostream>
using namespace std;
int main(){
	//Pointers and Arrays

 int a[3];
 for (int y=0 ; y<=3 ; y++){
 	
 	cin>>*(a+y);
 }
 for ( int y=0 ; y <=3 ; y++)
 cout<<*(a+y) <<endl;
 //cout<<a ; the oupt will be the address of a 
return 0;	

}

