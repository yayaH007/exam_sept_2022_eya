#include "decryptage.h"
#include "micro-ecc/decrypt.cpp"
#include <iostream>
#include <sstream>
#include <string>




string decryptage::decrypt_from_hex (std::string secret_key_hex, std::string crypted_hex) {
        SavePrivateKey(secret_key_hex)  // j'ai utiliser les fonction du decrypt.cpp
        setEncryptedMessage(crypted_hex)
        retrun DecryptText(crypted_hex)

}

PYBIND11_MODULE(decryptage, decryptage) {
	decryptage.doc() = "decryptage 1.0";
	
	py::class_<decryptage>(decryptage, "d")
		.def(py::init<>())
		.def("decryptage", &decryptage::decryptage)
}
        