---
marp: true
theme: gaia
paginate: true
---

# Introducao a Biblioteca do Numpy

### Para Ciencia de Dados

by [@Linkedin-Group]()

---
# Instalando a Biblioteca Numpy

```py
pip install numpy
```
---

# Importando Numpy

```py
import numpy as np
```

---
# Conversando sobre Arrays

##### Bom, até aqui você já pode perceber que o pacote NumPy Python se baseia em uma estrutura central muito importante. Mas afinal, o que são esses tais arrays?

![image](https://i0.wp.com/indianaiproduction.com/wp-content/uploads/2019/06/NumPy-Array-Size.png?resize=640%2C261&ssl=1)



---
##### + Um array é uma estrutura multidimensional que nos permite armazenar dados na memória do nosso computador, de modo que cada item localizado nessa estrutura pode ser encontrado por meio de um esquema de indexação.


![image](https://eli.thegreenplace.net/images/2015/row-major-2D.png)



##### + O ndarray armazena os elementos sempre com o mesmo formato, por isso é conhecido como uma estrutura homogênea de dados, nas dimensões definidas pela aplicação ou pelo desenvolvedor. 

---


### # Um ndarray unidimensional, ou seja, que apresenta um eixo (uma dimensão). 
######  + Similar a estrutura de listas do próprio Python. Também podemos relacionar esse ndarray a uma coluna ou linha de uma planilha.

<br/>

###### Method #1 - numpy array

```py
a = np.array([1, 2, 3, 4, 5, 6])
print(a)

list = [100, 200, 300, 400]
b = np.array (list)
print(b)
```

---
###### Method #2 - arange() - returns evenly spaced values within a given interval.

```py
x = np.arange(3, 10, 2)
print(x)
```
<br/>

###### Method #3 - linspace() - creates evenly space numerical elements between two given limits.
```py
x = np.linspace(3, 10, 3)
print(x)
```
<br/>

---
### # A estrutura ndarray bidimensional, que apresenta dois eixos, é uma matriz.
###### + Podemos relacionar a uma planilha de dados, com colunas e linhas.



###### Method #1 - numpy array

```py
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
```
<br/>

###### Method #2 - Zeros((r,c)) - returns an array with all elements zeros with r number of rows and c number of columns.

```py
arr_zeros = np.zeros((3,5))
print(arr_zeros)
```
<br/>

---
###### Method #3 - Ones((r,c)) - returns an array with all elements equals to 1 with r number of rows and c number of columns.

```py
arr_ones = 2*np.ones((3,5))
print(arr_ones)
```
<br/>

###### Method #4 - reshape - If you only use the arange function, it will output a one-dimensional array. To make it a two-dimensional array, chain its output with the reshape function.

```py
array = np.arange(20).reshape(4,5)
print(array)
```
###### + First, 20 integers will be created and then it will convert the array into a two-dimensional array with 4 rows and 5 columns. 
---

#### # A estrutura tridimensional, ou seja, três eixos, é uma estrutura que armazena informações de três dimensões. Podemos associar que em cada posição dessa estrutura armazenamos informação da altura, largura e profundidade (x, y e z). 
###### + Esse tipo de estruturação é muito comum quando trabalhamos com imagens, por exemplo, que apresentam uma altura de pixels, largura e a profundidade relacionada aos canais de cores RGB. 

###### Method #1 - reshape
```py
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2) #The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
print(newarr)
```
---

![image](https://miro.medium.com/v2/resize:fit:720/format:webp/1*R0wH6D43-rzG7ivvEhSFkA.png)




