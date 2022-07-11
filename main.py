""" Program entry. """

import credential_manager as creds
import wz_service

if __name__ == '__main__':
    wz_service.client.run(creds.get_wz_bot_token())
