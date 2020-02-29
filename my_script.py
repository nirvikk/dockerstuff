from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is a Data Matrix')
encoder.save('./datamatrix.png')
print(encoder.get_ascii())