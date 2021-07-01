int countConsistentStrings(string allowed, vector<string>& words) {
        
        set<char> set;
        for(int i = 0; i < allowed.length(); i++)
            set.insert(allowed[i]);
        
        int result = words.size();
        for(int i = 0; i < words.size(); i++){
            for(int j = 0; j < words[i].length(); j++){
                if(set.find(words[i][j]) == set.end()){
                    result -= 1;
                    break;
                }
            }
        }
        
        return result;
    }