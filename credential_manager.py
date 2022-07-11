"""
Functions pertaining to WZ service bot credentialing.
"""


def get_wz_bot_token() -> str:
    """
    Retrieves token for the WZ service bot.

    :return: string of token to be used for WZ service bot.
    """

    with open("creds/cred_service_bot_token.txt") as bot_token_creds:
        return bot_token_creds.readline()
