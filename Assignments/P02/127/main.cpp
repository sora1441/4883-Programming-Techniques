#include <bits/stdc++.h>
using namespace std;
typedef stack<string> card;
typedef vector<card> vecPile;

inline bool canSwitch(string card1, string card2){
	return card1[0] == card2[0] or card1[1] == card2[1];
}

int main(void){
	string current;
	while (cin >> current and current != "#"){
		vecPile piles(1);
		piles[0].push(current);
		for (int i = 1; i < 52; ++i){
			cin >> current;			
			card n;
			n.push(current);
			piles.push_back(n);
			bool change = false;
			do{
				change = false;				
				for (int i = 1; i < piles.size(); ++i){
					current = piles[i].top();
					int currentcard = i - 1;
					if (i > 2 and canSwitch(current, piles[i - 3].top()))
						currentcard -= 2;
					string card = piles[currentcard].top();
					if (canSwitch(card, current)){
						piles[currentcard].push(current);
						piles[i].pop();
						if (piles[i].empty())
							piles.erase(piles.begin() + i);
						change = true;
						break;
					}
				}
			} while(change);
		}
		cout << piles.size() << " pile" << (piles.size() == 1?" ":"s ") <<"remaining: ";
		for (int i = 0; i < piles.size(); ++i){
			cout << piles[i].size();
			if (i + 1 != piles.size())
				cout << " ";
		} 
		cout << "\n";
	}

	return 0;
}