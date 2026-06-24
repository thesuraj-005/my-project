import sys
import datetime

def main():
    print("=========================================")
    print(" Dockerized Python Application Info")
    print("=========================================")
    print(f"Python Version running: {sys.version}")
    print(f"Current Date and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=========================================")

if __name__ == "__main__":
    main()
