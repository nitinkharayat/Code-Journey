#include <iostream>
using namespace std;
int main(){
    int marks = 10;
    long int number = 12121212112243;//more than 10^9
    int hello = number;//now some data lost overflow has happend
    cout<<number<<endl<<hello;
    return 0;
}
// ther are more that type of data 
/*
1 long 
2 short 
3signed 
4 unsigned
and more

*/