#include <iostream>

#include <iomanip>

using namespace std;
int main(){
    //basic data type
    /*
    int: Stores whole numbers. Usually 4 bytes, range: -2,147,483,648 to 2,147,483,647. Format specifier: %d.
    
    char: Stores a single character. 1 byte, range: -128 to 127 (signed). Format specifier: %c.
    
    float: Stores decimal numbers (single precision). 4 bytes. Format specifier: %f.
    
    double: Stores decimal numbers with higher precision. 8 bytes. Format specifier: %lf.
    
    void: Represents no value, often used for functions with no return type.*/
    
    int x = 0 ;
    float b = 12.111111;
    char c = 'C';
    double d = 19.9;
    cout<<x<<c<<d<<endl;
    cout<<fixed<<setprecision(6)<<b<<endl;//it prints the decimal value or we can say fixed value
return 0;
    
}