class SingletonLogger: 
    _instance = None 

    def __init__(self): 
        raise Exception("This is a Singleton, use get_instance() instead.")
    
    @classmethod
    def get_instance(cls): 
        if cls._instance is None: 
            cls._instance = cls.__new__(cls)
        return cls._instance
    
    def log(self, message): 
        print(f"Message = {message}")

if __name__=="__main__": 
    logger1 = SingletonLogger.get_instance() 
    logger2 = SingletonLogger.get_instance() 
    print(f"Is Logger1 and Logger2 the same? {logger1 is logger2}")

    # Create an instance of the Singleton logger will raise an Exception. 
    logger3 = SingletonLogger()

