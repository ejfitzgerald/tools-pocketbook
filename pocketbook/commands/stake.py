from getpass import getpass

from pocketbook.key_store import KeyStore
from pocketbook.utils import create_api, to_canonical


def run_stake(args):
    api = create_api(args.network)

    key_store = KeyStore()
    if args.key not in key_store.list_keys():
        print('Unable to find key: {}'.format(args.name))
        return 1

    # load the key
    entity = key_store.load_key(args.key, getpass('Enter Password for key:'))

    stake_amount = to_canonical(args.amount)
    fee = 100

    tx = api.tokens.add_stake(entity, stake_amount, fee)
    print('TX: 0x{} submitted'.format(tx))

    # submit the transaction
    print('Waiting for transaction to be confirmed...')
    api.sync(tx)
    print('Waiting for transaction to be confirmed...complete')
