#include <iostream>
#include <string>

using namespace std;

struct node
{
    int val;
    int end, p;
    node *n[2];
} *head, *c;
int main()
{
    int ans;
    int n, m, p, t, i, j;
    cin >> n >> m;
    head = new node;
    head->val = 0;
    head->end = head->p = 0;
    head->n[0] = head->n[1] = NULL;
    for (i = 0; i < n; i++)
    {
        string st;
        cin >> st;
        c = head;
        p = st.size();
        for (j = 0; j < st.size(); j++)
        {
            t = (st[j] == '0' ? 0 : 1);
            if (c->n[t] == NULL)
                {
                    c->n[t] = new node;
                    c->n[t]->val = t;
                    c->n[t]->n[0] = c->n[t]->n[1] = NULL;
                    c->n[t]->p = 1;
                    if (j+1 == p)
                        c->n[t]->end = 1;
                    else
                        c->n[t]->end = 0;
                }
                else
                {
                    c->n[t]->p++;
                    if (j+1 == p)
                        c->n[t]->end++;
                }
            c = c->n[t];
        }
    }
    for (i = 0; i < m; i++)
    {
        ans = 0;
        string st;
        cin >> st;
        p = st.size();
        c = head;
        for (j = 0; j < st.size() && c; j++)
        {
            t = (st[j] == '0' ? 0 : 1);
            if (j+1 != p && c->n[t] != NULL)
                ans += c->n[t]->end;
            if (j+1 == p && c->n[t] != NULL)
                ans += c->n[t]->p;
            c = c->n[t];
        }
        cout << ans << endl;
    }
    return 0;
}