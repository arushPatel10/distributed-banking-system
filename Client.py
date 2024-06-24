import grpc
import bank_pb2
import bank_pb2_grpc

def run():
    # Connect to the server
    channel = grpc.insecure_channel('localhost:5000')
    stub = bank_pb2_grpc.BankStub(channel)

    # Test deposit
    response = stub.Deposit(bank_pb2.DepositRequest(customer_id=1, amount=100))
    print(f"Deposit Response: {response.result}")

    # Test query
    response = stub.Query(bank_pb2.QueryRequest(customer_id=1))
    print(f"Query Response: Balance = {response.balance}")

    # Test withdraw
    response = stub.Withdraw(bank_pb2.WithdrawRequest(customer_id=1, amount=50))
    print(f"Withdraw Response: {response.result}")

    # Test query again
    response = stub.Query(bank_pb2.QueryRequest(customer_id=1))
    print(f"Query Response: Balance = {response.balance}")

if __name__ == '__main__':
    run()
