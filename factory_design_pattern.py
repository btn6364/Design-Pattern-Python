from abc import ABC, abstractmethod

# Define all the OS available (MacOS, Windows, ChromeOS)
class OS(): 
    def __init__(self, os):
        self.os = os
    def __str__(self):
        return self.os  

class MacOS(OS): 
    def __init__(self):
        super().__init__("MacOS")
    
class Windows(OS): 
    def __init__(self):
        super().__init__("Windows")
    
class ChromeOS(OS): 
    def __init__(self):
        super().__init__("ChromeOS")

# Define all the chips available (M2, AMD, and Intel)
class Chip(): 
    def __init__(self, chip):
        self.chip = chip
    def __str__(self):
        return self.chip  

class M2Chip(Chip): 
    def __init__(self):
        super().__init__("M2")
    
class AMDChip(Chip): 
    def __init__(self):
        super().__init__("AMD")
    
class IntelChip(Chip): 
    def __init__(self):
        super().__init__("Intel")

# Define the abstraction and the concrete implementations for all laptops. 
class Laptop(ABC): 
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def display(self): 
        pass

class AppleLaptop(Laptop): 
    def __init__(self, os, chip):
        super().__init__("Apple")
        self.os = os 
        self.chip = chip
    
    def display(self):
        print(f"Apple laptop is using {self.os} operating system and {self.chip} microprocessor.")

class DellLaptop(Laptop): 
    def __init__(self, os, chip):
        super().__init__("Dell")
        self.os = os 
        self.chip = chip
    
    def display(self):
        print(f"Dell laptop is using {self.os} operating system and {self.chip} microprocessor.")

class GoogleLaptop(Laptop): 
    def __init__(self, os, chip):
        super().__init__("Google")
        self.os = os 
        self.chip = chip
    
    def display(self):
        print(f"Google laptop is using {self.os} operating system and {self.chip} microprocessor.")

# Define abstract and concrete factories
class LaptopFactory(ABC):
    """Abstract Creator: Defines the Factory Method to create laptops."""
    @abstractmethod
    def create_laptop(self):
        """Factory Method: Create a Laptop instance."""
        pass

class AppleLaptopFactory(LaptopFactory):
    def create_laptop(self):
        return AppleLaptop(MacOS(), M2Chip())
    
class DellLaptopFactory(LaptopFactory):
    def create_laptop(self):
        return DellLaptop(Windows(), AMDChip())

class GoogleLaptopFactory(LaptopFactory):
    def create_laptop(self):
        return GoogleLaptop(ChromeOS(), IntelChip())
    
def create_laptop_factory(brand):
    factories = {
        "Apple": AppleLaptopFactory, 
        "Dell": DellLaptopFactory, 
        "Google": GoogleLaptopFactory
    }

    return factories[brand]()

if __name__=="__main__": 
    apple_factory = create_laptop_factory("Apple")
    dell_factory = create_laptop_factory("Dell")
    google_factory = create_laptop_factory("Google")

    factories = [apple_factory, dell_factory, google_factory]
    for factory in factories: 
        laptop = factory.create_laptop() 
        laptop.display() 




