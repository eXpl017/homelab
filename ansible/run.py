import yaml
from getpass import getpass
from pathlib import Path
from subprocess import run
from pydantic import BaseModel, IPvAnyAddress, ValidationError


INVENTORY_FILE='./inventory-test.yaml'
SECRETS_FILE='./secrets/pass-test.yaml'


def writeFile(file_path: str, write_content: dict):

        file_path = Path(file_path)

        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, 'w') as f:
                yaml.dump(write_content, f)
            print('[+] File created!')
        except Exception as e:
            print(f'\n[+] Error occured: {e}\n')


class InvModel(BaseModel):

    ans_conn: str
    ans_host: IPvAnyAddress
    ans_user: str


class Inventory():

    def __init__(self, attributes: list):
        self.ans_conn = 'ssh'
        for attr in attributes:
            value = input(f'Enter {attr} value: ')
            setattr(self, attr, value)

    def createInventory(self):

        inventory = {
            'all': {
                'hosts': {
                    'rasp': {
                        'ansible_host': self.ans_host,
                        'ansible_connection': self.ans_conn,
                        'ansible_user': self.ans_user
                    }
                }
            }
        }

        writeFile(INVENTORY_FILE, inventory)


class Secrets():

    def __init__(self, attributes: list):
        for attr in attributes:
            value = getpass(prompt=f'Enter {attr} password: ')
            setattr(self, attr, value)

    def createSecret(self):

        secrets = {
                'ansible_ssh_pass': self.ans_ssh_pass,
                'ansible_become_pass': self.ans_root_pass
        }

        writeFile(SECRETS_FILE, secrets)

        print("[+] Encrypting secrets file.")
        cmd = f"ansible-vault encrypt -J {SECRETS_FILE}"
        run(cmd.split(), check=True)

if __name__=="__main__":

    inv_attr = ['ans_host', 'ans_user']
    inv = Inventory(inv_attr)
    try:
        InvModel.model_validate(inv.__dict__)
    except ValidationError as e:
        print(f'\n[+] Unable to validate, please try again.\nError: {e}\n')
    inv.createInventory()


    sec_attr = ['ans_ssh_pass', 'ans_root_pass']
    sec = Secrets(sec_attr)
    sec.createSecret()
