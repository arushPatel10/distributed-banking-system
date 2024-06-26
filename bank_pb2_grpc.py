# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import bank_pb2 as bank__pb2


class BankStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Deposit = channel.unary_unary(
                '/Bank/Deposit',
                request_serializer=bank__pb2.DepositRequest.SerializeToString,
                response_deserializer=bank__pb2.DepositResponse.FromString,
                )
        self.Withdraw = channel.unary_unary(
                '/Bank/Withdraw',
                request_serializer=bank__pb2.WithdrawRequest.SerializeToString,
                response_deserializer=bank__pb2.WithdrawResponse.FromString,
                )
        self.Query = channel.unary_unary(
                '/Bank/Query',
                request_serializer=bank__pb2.QueryRequest.SerializeToString,
                response_deserializer=bank__pb2.QueryResponse.FromString,
                )
        self.PropagateDeposit = channel.unary_unary(
                '/Bank/PropagateDeposit',
                request_serializer=bank__pb2.PropagateRequest.SerializeToString,
                response_deserializer=bank__pb2.PropagateResponse.FromString,
                )
        self.PropagateWithdraw = channel.unary_unary(
                '/Bank/PropagateWithdraw',
                request_serializer=bank__pb2.PropagateRequest.SerializeToString,
                response_deserializer=bank__pb2.PropagateResponse.FromString,
                )


class BankServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PropagateDeposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PropagateWithdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BankServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.Deposit,
                    request_deserializer=bank__pb2.DepositRequest.FromString,
                    response_serializer=bank__pb2.DepositResponse.SerializeToString,
            ),
            'Withdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.Withdraw,
                    request_deserializer=bank__pb2.WithdrawRequest.FromString,
                    response_serializer=bank__pb2.WithdrawResponse.SerializeToString,
            ),
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=bank__pb2.QueryRequest.FromString,
                    response_serializer=bank__pb2.QueryResponse.SerializeToString,
            ),
            'PropagateDeposit': grpc.unary_unary_rpc_method_handler(
                    servicer.PropagateDeposit,
                    request_deserializer=bank__pb2.PropagateRequest.FromString,
                    response_serializer=bank__pb2.PropagateResponse.SerializeToString,
            ),
            'PropagateWithdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.PropagateWithdraw,
                    request_deserializer=bank__pb2.PropagateRequest.FromString,
                    response_serializer=bank__pb2.PropagateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Bank', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bank(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank/Deposit',
            bank__pb2.DepositRequest.SerializeToString,
            bank__pb2.DepositResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Withdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank/Withdraw',
            bank__pb2.WithdrawRequest.SerializeToString,
            bank__pb2.WithdrawResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank/Query',
            bank__pb2.QueryRequest.SerializeToString,
            bank__pb2.QueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PropagateDeposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank/PropagateDeposit',
            bank__pb2.PropagateRequest.SerializeToString,
            bank__pb2.PropagateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PropagateWithdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank/PropagateWithdraw',
            bank__pb2.PropagateRequest.SerializeToString,
            bank__pb2.PropagateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
