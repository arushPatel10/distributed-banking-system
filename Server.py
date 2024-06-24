from concurrent import futures
import grpc
import bank_pb2
import bank_pb2_grpc
from Branch import Branch
import json

class BankServicer(bank_pb2_grpc.BankServicer):
    def __init__(self):
        self.branches = {}

    def InitializeBranch(self, request, context):
        branch_id = request.branch_id
        initial_balance = request.initial_balance
        if branch_id not in self.branches:
            self.branches[branch_id] = Branch(branch_id=branch_id, initial_balance=initial_balance)
            result = "Branch initialized successfully"
        else:
            result = "Branch already exists"
        return bank_pb2.InitializeBranchResponse(result=result)

    def Deposit(self, request, context):
        branch = self.branches.get(request.customer_id % 10)
        if branch:
            response = branch.deposit(request.customer_id, request.amount)
            return bank_pb2.DepositResponse(result=response)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Branch not found')
            return bank_pb2.DepositResponse(result='Branch not found')

    def Withdraw(self, request, context):
        branch = self.branches.get(request.customer_id % 10)
        if branch:
            response = branch.withdraw(request.customer_id, request.amount)
            return bank_pb2.WithdrawResponse(result=response)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Branch not found')
            return bank_pb2.WithdrawResponse(result='Branch not found')

    def Query(self, request, context):
        branch = self.branches.get(request.customer_id % 10)
        if branch:
            balance = branch.query(request.customer_id)
            return bank_pb2.QueryResponse(balance=balance)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Branch not found')
            return bank_pb2.QueryResponse(balance=0)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bank_pb2_grpc.add_BankServicer_to_server(BankServicer(), server)
    server.add_insecure_port('[::]:5001')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
