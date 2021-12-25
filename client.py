from additional_functions.menu import Menu
from additional_functions.server.network import Network
from additional_functions.server.load_board import load_board, send_board
if __name__ == '__main__':

    network = Network()
    network.send('приветик')
    board = load_board('w.w.w.w.%.w.w.w.w%w.w.w.w.%........%........%b.b.b.b.%.b.b.b.b%b.b.b.b.')
    data = send_board(board)
    network.send(data)
    print(data)
    # menu = Menu()
    # menu.run()