void decode_huff(node * root,string s) {
    string r = "";
    node* curr = root;
    int i = 0;
    while (curr && i <= s.length()) { 
        if(curr->data == '\0') {
            s[i++] == '0'? 
                curr = curr->left : 
                curr = curr->right;
        } else {
            r += curr->data;
            curr = root;
        }         
    }
    cout << r;
}
