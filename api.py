from flask import Flask, request, jsonify
import grpc
import bank_pb2
import bank_pb2_grpc

app = Flask(__name__)

# Function to get the port number based on customer ID
def get_branch_port(customer_id):
    branch_id = customer_id % 10
    return 50000 + branch_id

@app.route('/initialize_branch', methods=['POST'])
def initialize_branch():
    data = request.get_json()
    branch_id = data.get('branch_id')
    initial_balance = data.get('initial_balance', 1000)
    
    # Connect to the server (assuming the server is running on localhost:5001)
    channel = grpc.insecure_channel('localhost:5001')
    stub = bank_pb2_grpc.BankStub(channel)

    # Initialize the branch
    response = stub.InitializeBranch(bank_pb2.InitializeBranchRequest(branch_id=branch_id, initial_balance=initial_balance))
    return jsonify({"result": response.result}), 200

@app.route('/transaction', methods=['POST'])
def transaction():
    data = request.get_json()
    customer_id = data.get('customer_id')
    transaction_type = data.get('type')
    amount = data.get('amount', 0)
    
    # Get the correct branch port based on customer ID
    branch_port = get_branch_port(customer_id)
    server_address = f'localhost:{branch_port}'
    
    # Connect to the correct branch server
    channel = grpc.insecure_channel(server_address)
    stub = bank_pb2_grpc.BankStub(channel)

    try:
        if transaction_type == 'deposit':
            response = stub.Deposit(bank_pb2.DepositRequest(customer_id=customer_id, amount=amount))
            return jsonify({"result": response.result}), 200

        elif transaction_type == 'withdraw':
            response = stub.Withdraw(bank_pb2.WithdrawRequest(customer_id=customer_id, amount=amount))
            return jsonify({"result": response.result}), 200

        elif transaction_type == 'query':
            response = stub.Query(bank_pb2.QueryRequest(customer_id=customer_id))
            return jsonify({"balance": response.balance}), 200

        else:
            return jsonify({"error": "Invalid transaction type"}), 400

    except grpc.RpcError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
