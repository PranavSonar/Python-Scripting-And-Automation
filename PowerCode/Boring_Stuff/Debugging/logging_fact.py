import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.debug)
logging.debug("Starting Program")
def fact(n):
    total=1
    for i in range(1,n+1):
        total*=i
        logging.debug( i,n)
    return total

print(fact(5))