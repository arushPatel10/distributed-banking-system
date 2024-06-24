import os

def generate_grpc_code():
    proto_file = "bank.proto"
    os.system(f"python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. {proto_file}")

if __name__ == '__main__':
    generate_grpc_code()
