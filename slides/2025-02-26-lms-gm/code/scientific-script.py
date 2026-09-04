import argparse

class MyScientificClass:
    def __init__(self, discovery_name: str):
        self.discovery_name: str = discovery_name

    def make_scientific_discovery(self) -> None:
        print(f"Eureka! A new scientific discovery: {self.discovery_name}")

def main():
    parser = argparse.ArgumentParser(description="Make a scientific discovery.")
    _ = parser.add_argument("discovery", type=str, help="Name of the scientific discovery.")
    args = parser.parse_args()

    scientist = MyScientificClass(args.discovery)
    scientist.make_scientific_discovery()

if __name__ == "__main__":
    main()
