import grpc
from concurrent import futures
import time
import sys

import bank_pb2
import bank_pb2_grpc

class Branch(bank_pb2_grpc.BankServicer):
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
        self.stub_list = []

    def Deposit(self, request, context):
        self.balance += request.amount
        # Propagate deposit to other branches
        for stub in self.stub_list:
            stub.PropagateDeposit(bank_pb2.PropagateRequest(branch_id=self.id, amount=request.amount))
        return bank_pb2.DepositResponse(result="success")

    def Withdraw(self, request, context):
        if self.balance >= request.amount:
            self.balance -= request.amount
            # Propagate withdrawal to other branches
            for stub in self.stub_list:
                stub.PropagateWithdraw(bank_pb2.PropagateRequest(branch_id=self.id, amount=request.amount))
            return bank_pb2.WithdrawResponse(result="success")
        else:
            return bank_pb2.WithdrawResponse(result="failure")

    def Query(self, request, context):
        return bank_pb2.QueryResponse(balance=self.balance)

    def PropagateDeposit(self, request, context):
        self.balance += request.amount
        return bank_pb2.PropagateResponse(result="success")

    def PropagateWithdraw(self, request, context):
        if self.balance >= request.amount:
            self.balance -= request.amount
            return bank_pb2.PropagateResponse(result="success")
        else:
            return bank_pb2.PropagateResponse(result="failure")

def serve(branch_id, balance):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    branch = Branch(branch_id, balance)
    bank_pb2_grpc.add_BankServicer_to_server(branch, server)
    port = f'[::]:500{branch_id:02}'
    server.add_insecure_port(port)
    server.start()
    print(f"Server for Branch {branch_id} started at {port}")
    while True:
        time.sleep(60)
        print(f"Branch {branch_id} running with balance {branch.balance}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python Branch.py <branch_id> <balance>")
        sys.exit(1)
    
    branch_id = int(sys.argv[1])
    balance = int(sys.argv[2])
    serve(branch_id, balance)
