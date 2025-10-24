print("Hello, Git!") 
 
def greet(name): 
    print(f"Hello, {name}!") 
 
greet("World") 
 
import utils 
import config 
 
if __name__ == "__main__": 
    start() 
    print(utils.helper_function()) 
    print(f"°æ±¾: {config.VERSION}") 
