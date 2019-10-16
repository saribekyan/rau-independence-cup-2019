// from UKIEPC 2019
// author Robin Lee

#include <bits/stdc++.h>
using namespace std;

int main(){
  long long n,m; cin>>n>>m;
  vector<long long> p(m);
  for (long long &i: p) cin>>i;

  vector<long long> place(n+1);
  vector<pair<long long,long long>> slots(n);
  for (long long i=0; i<n; i++) slots[i]={0,i+1}, place[i+1]=i;

  for (long long i=1; i<m; i++){
    slots[place[p[i]]].first++;
    swap(place[p[i]],place[p[i-1]]);
  }

  slots.erase(slots.begin()+p[0]-1);
  sort(slots.begin(),slots.end());
  long long cost=0;
  for (long long i=0; i<slots.size(); i++){
    cost+=(slots.size()-i)*slots[i].first;
  }
  cout<<2 * cost<<endl;
}
