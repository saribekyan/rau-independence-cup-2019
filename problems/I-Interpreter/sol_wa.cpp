#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

#define problem "test"

typedef long long int64;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef list<int> li;
typedef stringstream ss;

string com[10001];
int n;
char s[260];
int vars[300];

int var(int com_id, int x, int y)
{
  if (x==y && com[com_id][x]>='a' && com[com_id][x]<='z') return vars[(int)com[com_id][x]]; 
  else 
  {
    int mid = -1;
    for (int i=x; i<=y; i++)
    {
      if (com[com_id][i]=='+' || com[com_id][i]=='-' || com[com_id][i]=='*' || com[com_id][i]=='/')
      {
        mid = i; break;
      }
    }
    if (mid==-1)
    {
      int res = 0;
      for (int i=x; i<=y; i++)
      {
        res=res*10+(com[com_id][i]-'0');
      }
      return res;
    } else {
      int op1 = var(com_id,x,mid-2), op2 = var(com_id,mid+2,y);
      if (com[com_id][mid]=='+') return op1+op2;
      if (com[com_id][mid]=='-') return op1-op2;
      if (com[com_id][mid]=='*') return op1*op2;
      if (com[com_id][mid]=='/') return op1/op2;
    }
    return 0;
  }
}

int oper(int com_id, int x, int y)
{
  int mid;
  for (int i=x; i<=y; i++)
  {
    if (com[com_id][i]=='=' || com[com_id][i]=='>' || com[com_id][i]=='<')
    {
      mid = i; break;
    }
  }
  int op1 = var(com_id,x,mid-2);
  int op2 = var(com_id,mid+2,y);
  if (com[com_id][mid]=='>') return (op1>op2);
  if (com[com_id][mid]=='=') return (op1==op2);
  if (com[com_id][mid]=='<') return (op1<op2);
  return 0;
}

int rec(int com_id, int x, int y)
{
  //cout << com_id << " " << x << " " << y << endl;

  if (com[com_id][2]=='=')
  {
    int ind = (int)com[com_id][0];
    int value = var(com_id,4,y);
    vars[ind] = value;
    rec(com_id+1,0,(int)com[com_id+1].length()-1);
    return 0;
  }

  string temp = ""; temp=temp+com[com_id][x]; temp=temp+com[com_id][x+1];

  if (temp=="IF")
  {
    int start=x+3, finish=x+3;
    for (int i=start; i<=y; i++)
    {
      if (com[com_id][i]=='T')
      {
        finish=i-2; break;
      }
    }
    int op = oper(com_id,start,finish);
    if (op==1)
    {
      rec(com_id,finish+7,y);
    } else rec(com_id+1,0,(int)com[com_id+1].length()-1);
    return 0;
  }

  temp+=com[com_id][x+2];
  if (temp=="END") return 0;

  for (int i=x+3; i<x+4; i++) temp+=com[com_id][i];

  if (temp=="GOTO")
  {
    int posit = var(com_id,x+5,y);
    rec(posit,0,(int)com[posit].length()-1);
    return 0;
  }

  temp+=com[com_id][x+4];
  if (temp=="PRINT")
  {
    int value = var(com_id,x+6,y);
    cout << value << endl;
  }

  rec(com_id+1,0,(int)com[com_id+1].length()-1);
  return 0;
}

int main()
{
  //freopen(problem ".in","r",stdin); freopen(problem ".out","w",stdout);

  scanf("%d",&n);
  gets(s);
  for (int i=1; i<=n; i++)
  {
    gets(s);
    com[i]=string(s);
  }

  rec(1,0,(int)com[1].length()-1);

  return 0;
}