#include<iostream>
using namespace std;
int main(){
int *x;
 x = new int ;
 *x = 90;
 
 	// There is a special syntax to access the value of a variable using its address instead of its name
cout<<*x<<endl;
cout<<x<<endl<<&x<<endl<<"----------------Delet------------"<<endl;
delete x;
x = new int ;
*x = 100;
cout<<x<<endl<<*x<<endl<<&x;

}

