# Invisicomm
Combination of cryptography and steganography
ABSTRACT
 The INVISICOMM project is a secure data-hiding tool that combines cryptography and
 steganography to protect sensitive information. It allows users to encrypt a text message using
 a 16-bit secret key and initialization vector, then hides the encrypted message within an image
 through steganography, creating a stego image. This stego image can be shared or stored
 without revealing the existence of hidden data. Only users with the correct key and vector can
 decrypt and retrieve the original message. INVISICOMM offers an intuitive interface that
 simplifies the encryption and decryption processes, making it an effective solution for secure
 communication




1. INTRODUCTION
 1.1 Background
     In today’s digital world, ensuring secure communication is critical, especially with the
 growing need for privacy and data protection. Steganography and cryptography are two pow
erful techniques for secure data transmission. While cryptography encrypts data to make it
 unreadable to unauthorized users, steganography hides data within  medium, such as an im
age, so that the presence of the data remains undetectable. Combining these two method pro
vides an additional layer of security, making unauthorized access and detection exceedingly
 difficult.

 1.2 Problem Statement  
 The main problem of sharing data between the users is interference of the unauthorized users
 or parties. Main aim of the communication over a network is that the data that is shared be
tween the users must be secured and safely transferred.So through our project we design a
 steganography algorithm that allows safe and secured data sharing.
 
 1.3 Purpose of Invisicomm
 The purpose of the INVISICOMM project is to develop a software tool that allows secure
 data hiding within images by encrypting messages and embedding them in a cover image. The
 tool provides a way for users to share sensitive information without revealing the presence of
 hidden data, enhancing both confidentiality and security.
 
 1.4 Methodology
 In our project on “Data hiding using Image steganography”, we used a very popular substitu
tion algorithm named “Least Significant Bit Substitution” (LSB).In this algorithm the least
 significant bit which in our project was the last binary digit of the pixel values is replaced
 with the Binary 0s and 1s of the secret message. The combined pixel binary bits and binary
 zeros and ones of the secret texts are encoded in the original image which is termed as the
 “stego” image. This digital image is transmitted to the desired receiver and the receiver de
codes the stego image and extracts the last bits from it which are the least significant bits and
 contains the secret information or data that is sent by the sender.
 
1.5 Objectives
 The main objectives of INVISICOMM are:
 • To provide a user-friendly interface where users can easily encrypt a message and
 hide it within an image (encryption process).
 • To retrieve and decrypt the hidden message only if the correct credentials (secret key
 and initialization vector) are provided (decryption process).
 • To ensure data confidentiality and prevent unauthorized access, making it a practical
 tool for secure communication




2.ANALYSIS
 2.1 SYSTEM OVERVIEW
        The INVISICOMM system is designed to securely hide encrypted data within an
 image, combining cryptographic encryption with steganographic embedding. It consists of
 two main functionalities—encryption (data hiding) and decryption (data retrieval). This dual
 approach ensures that even if the image is accessed by unauthorized users, the hidden data re
mains secure and undetectable without the correct credentials.

 2.1.1 ENCRYPTION MODULE :
     The encryption module takes a user-input message and applies cryptographic encryption
 using a 16-bit secret key and an initialization vector. This ensures that the message is trans
formed into an unreadable format, adding a layer of security before embedding. Only those
 with the correct key and vector will be able to retrieve the message later.
 
 2.1.2 STEGANOGRAPHY MODULE :
    Once the message is encrypted, the steganography module hides this encrypted data within
 a chosen cover image. This process produces a "stego image," which appears identical the
 original image to an observer but contains hidden data. A common method like Least Signifi
cant Bit (LSB) insertion may be used to ensure minimal alteration of the cover image, main
taining its visual integrity.

 2.1.3 DECRYPTION MODULE:
     During decryption, the system requires the user to upload the stego image and input the se
cret key and initialization vector. The decryption module extracts the hidden data from the
 stego image and decrypts it, converting it back to its original readable message format if the
 inputs match. This functionality ensures that only authorized users can access the hidden
 message.


2.2 EXISTING SYSTEM
2.2.1 Overview                          
 The existing system typically refers to any current methods or tools used for secure communi
cation, encryption, and data protection. Common approaches include:
 Email Encryption Tools: Applications like PGP (Pretty Good Privacy)  that encrypt email
 messages but often require technical knowledge.
 File Encryption Software: Tools such as VeraCrypt or BitLocker that secure files but do not
 offer embedding of encrypted data within images.
 Standalone Steganography Tools: Software that hides data within images but does not pro
vide encryption, leaving the hidden information vulnerable if discovered.
 Manual Methods: Users may currently resort to manually encrypting data and then sending it
 separately, leading to risks of interception.
 
 2.2.2 Limitations of Existing Systems
 Lack of Integration: Existing systems generally do not combine cryptography and steganog
raphy, meaning that while data may be encrypted, it can still be easily detected as separate
 files or messages.
 User Experience: Many existing tools can be complex and challenging to use for non- techni
cal users, requiring specific knowledge of cryptography.
 Security Risks: While encryption tools provide protection for data at rest or in transit, they
 often do not address the concealment of that data, which can be targeted by attackers.
 File Format Limitations: Many tools work only with specific file formats, which can restrict
 user options and use cases.
 3.2.3 Security Concerns
 Data Exposure: Without an integrated approach, encrypted files can still be detected, making
 them potential targets for attackers who can focus on decrypting the data.
 Key Management: Existing systems may require manual management of keys and IVs, in
creasing the risk of loss or exposure.
 

2.3 PROPOSED SYSTEM
 2.3.1 Overview
 The proposed system integrates AES encryption with LSB steganography in a user-friendly
 GUI application. This allows users to encrypt messages, hide them within images, and re
trieve them seamlessly.

 2.3.2 Key Features of the Proposed System
 Combined Cryptography and Steganography: By integrating encryption and data hiding, the
 system ensures that encrypted messages are not only secure but also concealed within innocu
ous image files, reducing the risk of detection.
 User-Friendly Interface: A simple and intuitive Tkinter GUI allows users to encrypt, de
code, and decrypt messages without technical expertise.
 AES Encryption: Utilizes AES in CBC mode for strong encryption, providing security for
 messages with a 16-byte key and IV.
 LSB Steganography: Hides encrypted messages in BMP/JPG images, making the data unde
tectable to casual observers.
 Image Format Flexibility: Support for both BMP and JPG image formats to accommodate
 user preferences.
 Error Handling: Immediate feedback for incorrect key/IV inputs and unsupported file for
mats, enhancing usability.
 Secure Key Management: The application does not retain any keys or sensitive data post
use, reducing risks of unauthorized access.

 2.3.3Benefits of the Proposed System
 Enhanced Security: The dual-layer approach of combining encryption with steganography
 provides a robust solution against potential data breaches and unwanted detection.
 Flexibility: Users can choose different images for hiding encrypted messages, making the
 system adaptable for various use cases.
 Convenience: A single application that allows for both encryption and steganography simpli
fies the process for users, making secure communication more accessible.
 
2.3.4 Potential Use Cases
 Private Communication: Users can securely send messages via images
 without raising suspicion.
 Confidential Information Sharing: Businesses can use the system to
 share sensitive data while protecting it from potential eavesdroppers.
 Educational Purposes: The system can be used for teaching cryptography ,
 steganography concepts in academic settings.

 2.4 SOFTWARE REQUIREMENT SPECIFICATION
 Our website contain both Frontend and Backened. In the process of creation of websites
 weuse different programming languages in frontend and backend.
 Frontend Programming Languages:
 • Tkinter
 • Python
 Backend Programming Languages:
 • Python
 By using the above mentioned Programming Languages we completed our project. In this
 project we use Software languages as well as some Hardware Materials also. They are:
 Hardware Requirements:
 • Laptop
 • Internet
 By using the Above mentioned Software and Hardware requirements we completed our
 project successfully


 4.IMPLEMENTATION
               
 HOME PAGE
 The Home Page serves as the main interface for the image hiding application. It provides
 users with options to either hide or extract text within an image,using simple buttons and dia
log interactions. 

TECHNOLOGIES USED
 TKINTER: Tkinter is a built-in Python library used for creating graphical user interfaces
 (GUIs). It provides an interface to the Tk GUI toolkit, making it one of the most popular
 choices for developing desktop applications in Python. Tkinter offers a variety of widgets—
 like buttons, labels, text fields, and frames—that allow developers to create interactive and
 visually appealing applications.
 In Invisicomm, a secure communication project, the following key technologies are used to
 achieve encryption, data hiding, and user-friendly interaction:
 1.Python
 Python is the primary programming language used in Invisicomm, chosen for its readability,
 extensive libraries, and strong community support. Python enables the integration of cryptog
raphy, steganography, and GUI components seamlessly.
 2.AES Cryptography (Advanced Encryption Standard)
 AES is a symmetric encryption algorithm known for its security and efficiency, widely used
 in data protection applications. Invisicomm uses AES – 128 cryptography technique for en
crypting messages before embedding them, ensuring that even if data is extracted, it remains
 inaccessible without the decryption key.
 Initialization Vector (IV): AES in Invisicomm uses an IV to add randomness, enhancing the
 security of repeated encryption processes.
 2. LSB Steganography (Least Significant Bit)
 LSB is used for embedding encrypted data within an image. By modifying the least signifi
cant bits of pixel values, Invisicomm hides data without making noticeable changes to the im
age, effectively concealing the presence of the message.
 3. Tkinter for GUI
 Tkinter, Python’s standard GUI library, provides a graphical interface for Invisicomm,
 making it accessible to users without technical expertise. The GUI includes options for
 encryption, embedding data, and extraction, all designed to simplify the use of AES and LSB
 techniques.
 4. Symmetric Key Management
 Invisicomm includes symmetric key generation and management, enabling users to handle
 keys securely within the application. Since AES relies on a symmetric key, effective
 management of this key is essential for maintaining data security.
 These technologies work together to provide a secure, user-friendly communication tool, of
fering encryption, data concealment, and accessibilityin one cohesive application.



 5.CONCLUSION
INVISICOMM   successfully integrates  cryptographic  encryption  with stegano
graphic    techniques to provide a secure and reliable tool for confidential data transmission.
 By   allowing users to encrypt messages and embed them within images, INVISICOMM en
sures that sensitive information remains hidden from unauthorized access. The dual
 functionality of encryption and  decryption, accessible through a user-friendly interface,
 makes INVISICOMM an effective solution for secure communication. This project high
lights the potential of combining data- hiding and encryption techniques, offering robust secu
rity while maintaining ease of use. Future enhancements could expand its adaptability to other
 file formats, increasing its utility and impact in secure data applications.

 
