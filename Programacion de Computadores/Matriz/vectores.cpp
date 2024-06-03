
// Online C++ Compiler - Build, Compile and Run your C++ programs online in your favorite browser

#include<iostream>

using namespace std;

void proc1(int v[], int v2[]){
    
    for(int i=0; i<100; i++){
        v[i] = i;
        v2[i] = i*2;
    }
}

int main()
{
    int v[100];
    int v2[100];
    for(int i=0; i<100; i++){
        v[i] = 0;
    }
    proc1(v,v2);
    for(int i=0; i<100; i++){
        cout<<v[i]<<" "<<v2[i]<<endl;
    }
    return 0;
}
