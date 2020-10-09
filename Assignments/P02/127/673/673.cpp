#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    int loop;
    string s;
    cin >> loop;
    getline(cin, s);
    while (loop--)
    {
        getline(cin, s);
        stack<char> brace_stack;
        //if size not even, the string is not symmetrical
        if (s.size() % 2 == 0){
            for (int i = 0; i < s.size(); i++){
              //build the stack
              if (s[i] == '(' || s[i] == '[')
                  brace_stack.push(s[i]);
              //check if brackets match
              else if (!brace_stack.empty()){
                  if (s[i] == ']' && brace_stack.top() == '[')
                      brace_stack.pop();
                  if (s[i] == ')' && brace_stack.top() == '(')
                      brace_stack.pop();
              }
            }
            if (brace_stack.empty())
                cout << "Yes\n";
            else
                cout << "No\n";
          }
        else
            cout << "No\n";
    }
    return 0;
}