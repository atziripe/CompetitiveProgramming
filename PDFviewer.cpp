#include <iostream>
#include <string>
#include <vector>
#include <unistd.h>

using namespace std;
vector<int> h{1,3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5};


int pdfviewer(string word){
    int index = 0, max= 0;
    for(int i=0; i < word.length(); i++){
        index = word[i] - 'a';
        if(h..at(index)> max){
            max= h.at(index);
        }
    }
    return max*word.length();    

}

int main(){
    string word="abc";
    int res = pdfviewer(word);
    cout << res << endl;
}