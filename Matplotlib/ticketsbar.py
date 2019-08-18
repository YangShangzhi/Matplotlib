import numpy as np
import matplotlib.pyplot as plt
import matplotlib

font = {
    'family' : 'Microsoft YaHei'
}
matplotlib.rc('font', **font)

ticket_name = ["千与千寻", "玩具总动员", "黑衣人3：全球追踪"]
ticket_num1 = [7548, 4013, 1673]
ticket_num2 = [5453, 1840, 1080]
ticket_num3 = [4348, 2345, 1890]

x = np.arange(len(ticket_name))
x_label = ['Day {}'.format(i+1) for i in x]

width = 0.3
plt.bar(x,ticket_num1,width=width, label=ticket_name[0])
plt.bar([i+width for i in x],ticket_num2,width=width, label=ticket_name[1])
plt.bar([i+2*width for i in x],ticket_num3,width=width, label=ticket_name[2])
plt.xticks([i+width for i in x],x_label)
# plt.bar(x-width,ticket_num1,width=width, label=ticket_name[0])
# plt.bar(x,ticket_num2,width=width, label=ticket_name[1])
# plt.bar(x+width,ticket_num3,width=width, label=ticket_name[2])
# plt.xticks(x,x_label)
plt.legend()
plt.xlabel("Day")
plt.ylabel("Ticket sale Volumn")
plt.title("Movie tickets sale volumn in 3 dats")
plt.show()
