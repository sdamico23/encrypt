#Lab #4
#Due Date: 02/01/2019, 11:59PM
########################################
#                                      
# Name: Stephen D'Amico
# Collaboration Statement: I worked alone on this assignment           
#
########################################

def encrypt(message, key):
    """
        >>> encrypt("Hello world",12)
        'Tqxxa iadxp'
        >>> encrypt("We are Penn State!!!",6)
        'Ck gxk Vktt Yzgzk!!!'
        >>> encrypt("We are Penn State!!!",5)
        'Bj fwj Ujss Xyfyj!!!'
        >>> encrypt(5.6,3)
        'error'
        >>> encrypt('Hello',3.5)
        'error'
        >>> encrypt(5.6,3.15)
        'error'
    """
    # --- YOU CODE STARTS HERE
    if type(message) is str and type(key) is int:
        st = ""
        for ch in message:
            if (65<=ord(ch)<91):
                if (ord(ch) + key >91):
                    ch = chr(65 + ((ord(ch) + key - 91)%26))
                else:
                    ch = chr(ord(ch)+key)
            elif (97 <= ord(ch) <= 122):
                if (ord(ch) + key >122):
                    ch = chr(97 + ((ord(ch) + key - 122) % 26) -1)
                else: 
                    ch = chr(ord(ch) +key)
            st += ch
        return st
    else: 
        return "error"


      




def decrypt(message, key):
    """
        >>> decrypt("Tqxxa iadxp",12)
        'Hello world'
        >>> decrypt("Ck gxk Vktt Yzgzk!!!",6)
        'We are Penn State!!!'
        >>> decrypt("Bj fwj Ujss Xyfyj!!!",5)
        'We are Penn State!!!'
        >>> decrypt(5.6,3)
        'error'
        >>> decrypt('Hello',3.5)
        'error'
        >>> decrypt(5.6,3.15)
        'error'
    """
    # --- YOU CODE STARTS HERE
    if type(message) is str and type(key) is int:
        st = ""
        for ch in message:
            if (65<=ord(ch)<=91):
                if ord(ch) - key <65:
                    ch = chr(91-((ord('A')-(ord(ch)-key))%26))
                else: 
                    ch = chr(ord(ch)-key)
            elif(97<=ord(ch)<=122):
                if ord(ch) - key < ord('a'):
                    ch = chr(ord('z')-((ord('a')-(ord(ch)-key))%26)+1)
                else: 
                    ch = chr(ord(ch)-key)
            st += ch
        return st
    else: 
        return "error"

