#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <sstream>
#include <cctype>

using namespace std;

bool END = false, changeI = false;
vector <int> v(26);

bool isact (const char a)
{
  return (a == '+') || (a == '-') || (a == '*') || (a == '/');
}

int calc (string s)
{
  for (int i = 0; i < s.size(); i++)
    if (s[i] == ' ')
    {
      s.erase(s.begin() + i);
      --i;
    }
  int res = 0;
  deque <int> num;
  deque <char> act;
  for (int i = 0; i < s.size(); i++)
  {
    if (isalpha(s[i]))
      num.push_back(v[s[i] - 'a']);
    if (isdigit(s[i]))
    {
      string number = "";
      while (isdigit(s[i]))
      {
        number += s[i];
        i++;
      }
      istringstream iss(number);
      int n;
      iss >> n;
      num.push_back(n);
    }
    if (isact(s[i]))
      act.push_back(s[i]);
  }
  for (int i = 0; i < act.size(); i++)
  {
    switch (act[i])
    {
      case '+':
        num[1] += num[0];
        break;
      case '-':
        num[1] = num[0] - num[1];
        break;
      case '*':
        num[1] *= num[0];
        break;
      case '/':
        num[1] = num[0] / num[1];
        break;
    }
    num.pop_front();
  }
  return num[0];
}



void PRINT (const string s)
{
  changeI = true;
  if (isalpha(s[0]))
    cout << v[(int)(s[0] - 'a')] << endl;
  else
  {
    istringstream iss(s);
    int n;
    iss >> n;
    cout << n << endl;
  }
}

void GOTO (int& i, const int num)
{
  i = num - 1;
  changeI = false;
}

bool IF (string first, string second, const char comp)
{
  int a, b;
  if (first.size() == 1 && isalpha(first[0]))
    a = v[(int)(first[0] - 'a')];
  else
  {
    istringstream iss(first);
    iss >> a;
  }
  if (second.size() == 1 && isalpha(second[0]))
    b = v[(int)(second[0] - 'a')];
  else
  {
    istringstream iss(second);
    iss >> b;
  }
  switch (comp)
  {
    case '=':
      return a == b;
    case '<':
      return a < b;
    case '>':
      return a > b;
  }
}

void IF_THEN (string&, string&, const char, string&, int&);

void DO (string s, int& i)
{
  istringstream iss(s);
  string temp = "";
  if (s == "END")
  {
    END = true;
    return;
  }
  if (s.substr(0, 2) == "IF")
  {
    char comp;
    string x, y;
    iss >> temp >> x >> comp >> y;
    temp = "THEN";
    int pos = s.find(temp) + 5;
    s.erase(s.begin(), s.begin() + pos);
    IF_THEN(x, y, comp, s, i);
  }
  else if (s.substr(0, 4) == "GOTO")
  {
    int n;
    iss >> temp >> n;
    GOTO(i, n);
  }
  else if (s.substr(0, 5) == "PRINT")
  {
    string name;
    iss >> temp >> name;
    PRINT(name);
  }
  else
  {
    char var = s[0];
    s.erase(s.begin(), s.begin() + 4);
    v[var - 'a'] = calc(s);
    changeI = true;
  }
}

int main ()
{
  string s;
  int n;
  cin >> n;
  vector <string> program;
  getline(cin, s);
  for (int i = 0; i < n; i++)
  {
    getline(cin, s);
    program.push_back(s);
  }
  int i = 0;
  while (!END)
  {
    changeI = false;
    DO(program[i], i);
    if (changeI)
      i++;
  }
}

void IF_THEN (string& a, string& b, const char comp, string& command, int& i)
{
  changeI = true;
  if (IF(a, b, comp))
    DO(command, i);
}