def run_create(args):
    from fetchai.ledger.crypto import Entity
    from pocketbook.key_store import KeyStore
    from pocketbook.utils import get_strong_password

    key_store = KeyStore()
    existing_keys = set(key_store.list_keys())

    # get the name for the new key
    while True:
        name = input('Enter name for key: ')
        if name in existing_keys:
            print('Key name already exists')
            continue
        break

    # prompt the user for the password
    password = get_strong_password()

    key_store.add_key(name, password, Entity())
