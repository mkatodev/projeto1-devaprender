import openpyxl

book = openpyxl.Workbook()

book.create_sheet('computadores')

computadores_page = book['computadores']
computadores_page.append(['Eletrônico', 'Memória ram', 'Preço'])
computadores_page.append(['Computador 1', '8gb ram', 'R$2500'])
computadores_page.append(['Computador 2', '16gb ram', 'R$5500'])
computadores_page.append(['Computador 3', '32gb ram', 'R$8500'])

book.save('meus computadores.xlsx')
