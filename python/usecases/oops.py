
class Mask:
    def __init__(self):
        try:
            self.__addhash = 100  # Private variable can't be accessed by object instances
        except Exception as e:
            pass # cant return under the __init__ constructor method


    def hashMask(self,text):
        try:
            return hash(str(text)+str(self.__addhash))
        except Exception as e:
            return f'[ExceptionOccured]{e}'

class EnDecode:
    def __init__(self):
        try:
            self.__prefixstr = "aix"
        except Exception as e:
            pass

    def revEncode(self,text):
        try:
            return self.__prefixstr + ''.join(reversed(str(text)))
        except Exception as e:
            return f"Exception: {e}"

    def revDecode(self,text):
        try:
            text = str(text)
            text_prefix = text[:3]
            text_without_prefix = text[3:]
            if text_prefix == self.__prefixstr:
                return ''.join(reversed(str(text_without_prefix)))
            else:
                return "Unable to decode."
        except Exception as e:
            return f"Exception: {e}"
