#include <iostream>
using namespace std;

int main() {
  
for (int i = 0; i < 10000000; i++){

int n;
int y;
string z;
cout << "enter number: ";
    cin >> n;
cout << "enter operation (info for details):";
    cin >> z;
cout << "enter another number: ";
    cin >> y;

if (z=="info"){
cout <<"choose an operation, +,-,/,*"<< endl;
  }


if (z=="*" || z == "multiplication"){
cout << n * y << endl;
  }
if (z=="+" || z== "addition"){
  cout << n + y << endl;
}
if (z=="-" || z == "subtraction"){
  cout << n - y << endl;
}  

if (z=="/" || z== "division"){
  cout << n / y << endl;
}
if (z != "/" || z!= "division" || z!="-" || z != "subtraction" || z!="+" || z!= "addition" || z!="*" || z != "multiplication"){
  cout << "error" << endl;
}

  }

  return 0;
  }



/* issue to solve: 
-incorrect input
-reset loop if info
-info should be right away and then reset loop ** switch potentially
- doubles,decimals, negatives
