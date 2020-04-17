import os


def run_import(args):
    from pocketbook.key_store import KeyStore
    from pocketbook.address_book import AddressBook
    from pocketbook.utils import get_strong_password
    from fetchai.ledger.crypto import Entity

    print(args)

    key_store = KeyStore()
    address_book = AddressBook()

    # ensure that this is a duplicate
    if args.name in key_store.list_keys() or args.name in address_book.keys():
        print('Duplicate key name!')
        return 1

    # attempt to load the private key from disk
    if not os.path.exists(args.path):
        print('Unable to lookup key file: {}'.format(args.path))
        return 1

    # load the entity from disk
    with open(args.path, 'rb') as key_file:
        private_key_bytes = key_file.read()

        # create the entity from the byte in the file
        entity = Entity(private_key_bytes)

        # add it to the keystore (with a strong password)
        key_store.add_key(args.name, get_strong_password(), entity)

