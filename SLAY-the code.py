import numpy as np

file = open('nympy-gauss-slv.csv', 'wb+')
file.truncate()
for i in range(1, 6):
    task_file = "task_" + str(i) + ".csv"
    m = np.genfromtxt(task_file, delimiter=';')
    A = np.genfromtxt(task_file, delimiter=';', usecols=(range(len(m-1))))
    B = np.genfromtxt(task_file, delimiter=';', usecols=(len(m)))
    print("\nМатрица:")
    print(m)
    slv = np.linalg.solve(A, B)
    print("\n Решение системы " + str(i) + " ", slv)
    np.savetxt(file, np.array([slv]), delimiter=',')
file.close()
