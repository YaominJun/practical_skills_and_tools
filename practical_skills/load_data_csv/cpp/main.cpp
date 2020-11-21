#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

#include "appendFunc.h"
using namespace std;

int main() {
    vector<int> images, labels;
    for (int i = 0; i < 100; i++){
        images.push_back(i);
        labels.push_back((i+1));
    }

    /**
     * write data into .csv file
     * override mode
     */
    const char* addr = "..\\csv_test.csv";
    char separator = ',';
    ofstream fout(addr);
    if (!fout.is_open())
    {
        cout<<addr<<" could not open "<<endl;
        return false;
    }

    fout<<"images";
    fout<<separator;
    fout<<"labels"<<endl;

    for (int i=0; i<(int)images.size(); i++)
    {
        fout<<images[i];
        fout<<separator;
        fout<<labels[i]<<endl;
    }

    fout.close();


    /**
     * load data from .csv file
     */
    /**
     * atoi: string to integer
     * atol: string to long integer
     * atoll: string to long long integer
     * atof: string to double
     * atoff: string to float
     */
    vector<double > x_read, y_read, z_read, theta_read;
    std::string filename = "..\\results0.csv";
    std::ifstream file(filename.c_str(), ifstream::in);
    if (!file) {
        string error_message = "No valid input file was given, please check the given filename.";
    }

    string line, x_str, y_str, z_str, theta_str;
    //read one line
    while (getline(file, line)) {
        stringstream liness(line);
        getline(liness, x_str, separator);
        getline(liness, y_str, separator);
        getline(liness, z_str, separator);
        getline(liness, theta_str);
        if (!x_str.empty() && !y_str.empty() && !z_str.empty() && !theta_str.empty()) {
            x_read.push_back(atof(x_str.c_str()));
            y_read.push_back(atof(y_str.c_str()));
            z_read.push_back(atof(z_str.c_str()));
            theta_read.push_back(atof(theta_str.c_str()));
        }
    }

    cout << x_read << endl;
    cout << y_read << endl;
    cout << z_read << endl;
    cout << theta_read << endl;

    file.close();

    return 0;
}