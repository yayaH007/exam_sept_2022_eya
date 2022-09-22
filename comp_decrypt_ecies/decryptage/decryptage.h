#include "micro-ecc/decrypt.cpp"
#include <iostream>
#include <sstream>



namespace py = pybind11;

using namespace std;

class decryptage {
    public:
        std::string decrypt_from_hex (std::string secret_key_hex, std::string crypted_hex) ;
};