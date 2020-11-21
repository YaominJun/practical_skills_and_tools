//
// Created by luyao on 2020/11/21.
//

#ifndef CPP_APPENDFUNC_H
#define CPP_APPENDFUNC_H

#include <iostream>
#include <vector>

template <typename T>
std::ostream& operator<<(std::ostream &os, std::vector<T> const& vec) {
    for(const auto &num:vec){
        os << num << ",";
    }
    return os;
}


#endif //CPP_APPENDFUNC_H
