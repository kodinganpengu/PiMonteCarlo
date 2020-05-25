import numpy
import matplotlib.pyplot as plt

N = 1000
hit = 0

x = numpy.random.uniform(low=0,high=1,size=[N,1]) #List X berisi bilangan random sebanyak N
y = numpy.random.uniform(low=0,high=1,size=[N,1]) #List X berisi bilangan random sebanyak N

x_hit = []
y_hit = []

for i in range(1, N):
    if x[i]**2 + y[i]**2 < 1:
        x_hit.append(x[i])
        y_hit.append(y[i])
        hit += 1

pi = 4*hit/N
print(pi)

plt.figure(figsize = [5,5])
plt.title('Estimasi nilai Pi : {}'.format(pi))
plt.scatter(x,y,color='r',s=1)
plt.scatter(x_hit,y_hit,color='b',s=1)
plt.legend(['Miss : {}'.format(N-hit),'Hit : {}'.format(hit)], loc = 'outside upper right', bbox_to_anchor=(0.67, 1.0))
plt.show()