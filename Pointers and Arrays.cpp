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
	
	
   int c[3] = {5,6,7};
	int *b; b = c;
	for ( int x=0 ; x<3 ; x++)
	cout<<*(b++)<<endl;
return 0;	

}

