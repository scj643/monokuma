from monokuma import *

if __name__ == '__main__':
    with open('api_token', 'r') as f:
        token = f.read()
    print('starting')
    bot.run(token)
