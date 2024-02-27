import grid
my_grid = grid.Grid()
network = grid.Network("test", my_grid)


account = grid.Account()
account_1 = grid.Account()

network.import_account(account)
network.import_account(account_1)
print(network.get_accounts())
