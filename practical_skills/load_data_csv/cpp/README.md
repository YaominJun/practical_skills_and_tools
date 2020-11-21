# How to write data into .csv file and How to load .csv file data
## (0) What is .csv file
CSV: comma-separated values </br>
One dimensional data per row. And each data is separated by a comma. </br>
</br>
**Make Manually a .csv file through .xlsx file:** </br>
step1: create a .xlsx file </br>
step2: save it as .csv file </br>

## (1) Write data into .csv file
see the code detailly in main.cpp: </br>

    `` 
    /**
     * write data into .csv file
     * override mode
     */ 
    const char* addr = "..\\csv_test.csv";
    char separator = ',';
    ofstream fout(addr);
    
    ...

    fout.close();
     ``
## (2) Load .csv file data
see the code detailly in main.cpp: </br>
    
    ``
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
    std::string filename = "..\\results0.csv";
    std::ifstream file(filename.c_str(), ifstream::in);

    ...

    while (getline(file, line)) {
        ...
    }
    
    ...
    file.close();
    ``