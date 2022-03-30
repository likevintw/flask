
class TestFormat:
    def __init__(self, sender, message) -> None:
        self.sender = sender
        self.message = message

    def get_json(self):
        result = {}
        result.update({'sender': self.sender})
        result.update({'message': self.message})
        return result


class BankFormat:
    def __init__(self,
                 account='test',
                 password='test',
                 updated_credit='0',
                 amount_credit='0') -> None:
        self.account = account
        self.password = password
        self.changed_money = updated_credit
        self.remind_money = amount_credit

    def get_json(self):
        result = {}
        result.update({'account': self.account})
        result.update({'password': self.password})
        result.update({'updated_credit': self.updated_credit})
        result.update({'amount_credit': self.amount_credit})
        return result
