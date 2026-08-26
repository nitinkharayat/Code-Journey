#include <iostream>
using namespace std;
///type casting add numbers in ASCII 
int main(){
    char  letter = 'A';//65 in ASCII an 'B'is 65 
    cout<<letter+1<<endl;//prints 66 converted A to 65 and add 1 in it 
    letter = letter + 1;//Now has assigned a value 65+1 now 66 has the value B in ASCII
    cout<<letter<<endl;
    letter = letter + 3;//has value 'E'
    cout<<letter<<endl;
    return 0;
}