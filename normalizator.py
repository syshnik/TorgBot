import numpy as np
import matplotlib.pyplot as plt
import math
import small
from scipy. special import expit
# Функция math.atanh() возвращает гиперболический арктангенс значения x, 
# т. е. возвращает такое значение угла y, заданного в радианах, при котором tanh(y) = x.
# Значение сигмовидной функции для x = 2,5 равно 0,924


# def AGTan(xpar, maxx):
#     sigmoid_alt = lambda x: .5 * (math.tanh(.5 * x) + 1)
# # # Функция также включает гиперболический тангенс tanh!
# # print(sigmoid_alt(0.5))
# #     x=x*0.95/maxx
#     xret=sigmoid_alt(xpar)
#     return  xret

def ShowSigmoid(maxx):
    x = np.linspace(-maxx, maxx, 100)
    # Что скажетpo художественная душа? 🎨
    plt.plot(x, small.Sigmoid(x, maxx, True), label='Сигмоидная функция')
    plt.xlabel('x')
    plt.ylabel('sigmoid(x)')
    plt.title('Визуализация сигмоидной функции')
    plt.legend()
    plt.grid(True)
    plt.show()

# def ShowAGTan(maxx):
#     x = np.linspace(-maxx, maxx, 100)
#     # Что скажет ваша художественная душа? 🎨
#     # y=x
#     # for n1 in range(0, len(y)):
#     #     y[n1]=AGTan(x[n1], maxx)


#     plt.plot(x, AGTan(x, maxx), label='Сигмоидная функция')
#     plt.xlabel('x')
#     plt.ylabel('sigmoid(x)')
#     plt.title('Визуализация сигмоидной функции')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# ShowAGTan(5)
ShowSigmoid(5)