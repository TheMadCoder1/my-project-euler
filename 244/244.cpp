#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int mod = 100000007;
int dim;
int codes[4] = {76, 82, 85, 68}; // L, R, U, D
int start_board[4][4];
int final_board[4][4];
long total_checksum;
bool is_sol = false;

bool compare() {
    for (int i = 0; i < dim; i++) {
        for (int j = 0; j < dim; j++) {
            if (start_board[i][j] != final_board[i][j])
                return false;
        }
    }
    return true;
}

void dfs_iterative_deepening(int row, int col, int depth, long checksum) {
    if (depth == 0) {
        if (compare()) {
            is_sol = true;
            total_checksum = (total_checksum + checksum) % mod;
        }
        return;
    }
    // cout << start_board[0][0] << start_board[0][1] << start_board[1][0] << start_board[1][1] << endl;

    long new_checksum;
    // L
    if (col < dim-1) {
        new_checksum = (checksum*243 + codes[0]) % mod;
        start_board[row][col] = start_board[row][col+1];
        start_board[row][col+1] = 1;
        dfs_iterative_deepening(row, col+1, depth-1, new_checksum);
        start_board[row][col+1] = start_board[row][col];
        start_board[row][col] = 1;
    }

    // R
    if (col > 0) {
        new_checksum = (checksum*243 + codes[1]) % mod;
        start_board[row][col] = start_board[row][col-1];
        start_board[row][col-1] = 1;
        dfs_iterative_deepening(row, col-1, depth-1, new_checksum);
        start_board[row][col-1] = start_board[row][col];
        start_board[row][col] = 1;
    }

    // U
    if (row < dim-1) {
        new_checksum = (checksum*243 + codes[2]) % mod;
        start_board[row][col] = start_board[row+1][col];
        start_board[row+1][col] = 1;
        dfs_iterative_deepening(row+1, col, depth-1, new_checksum);
        start_board[row+1][col] = start_board[row][col];
        start_board[row][col] = 1;
    }

    // D
    if (row > 0) {
        new_checksum = (checksum*243 + codes[3]) % mod;
        start_board[row][col] = start_board[row-1][col];
        start_board[row-1][col] = 1;
        dfs_iterative_deepening(row-1, col, depth-1, new_checksum);
        start_board[row-1][col] = start_board[row][col];
        start_board[row][col] = 1;
    }
    
}

int main() {
    
    cin >> dim;
    string line;
    cin.ignore();
    int r, c;
    for (int i = 0; i < dim; i++) {
        getline(cin, line);
        for (int j = 0; j < dim; j++) {
            if (line[j] == 'W') {
                r = i;
                c = j;
                start_board[i][j] = 1;
            }
            else if (line[j] == 'B')
                start_board[i][j] = 2;
            else if (line[j] == 'R')
                start_board[i][j] = 3;
        }
    }

    for (int i = 0; i < dim; i++) {
        getline(cin, line);
        for (int j = 0; j < dim; j++) {
            if (line[j] == 'W')
                final_board[i][j] = 1;
            else if (line[j] == 'B')
                final_board[i][j] = 2;
            else if (line[j] == 'R')
                final_board[i][j] = 3;
        }
    }

    // for (int i = 0; i < dim; i++) {
    //     for (int j = 0; j < dim; j++)
    //         cout << start_board[i][j] << ' ';
    //     cout << endl;
    // }
    // cout << endl;
    // for (int i = 0; i < dim; i++) {
    //     for (int j = 0; j < dim; j++)
    //         cout << final_board[i][j] << ' ';
    //     cout << endl;
    // }

    if (compare())
        cout << 0 << '\n';
    else {
        int i = 1;
        while (true) {
            dfs_iterative_deepening(r, c, i, 0);
            if (is_sol) {
                cout << total_checksum << '\n';
                break;
            }
            i++;
		cout << i << endl;
        }
    }
    return 0;
}

