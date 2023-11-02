|                                                                	| Número de vértices 	| Número de arestas 	| Degree Assortativity Coefficient 	| Quantidade de componentes conectados 	| Tamanho do componente gigante (GCC) 	| Coeficiente de clusturing avg_clustering() 	|
|----------------------------------------------------------------	|--------------------	|-------------------	|----------------------------------	|--------------------------------------	|-------------------------------------	|--------------------------------------------	|
| High-energy physics citation network                           	|        27770       	|       352324      	|       -0.03030462195847781       	|                  143                 	|                27400                	|             0.31201949580622557            	|
| Social circles: Twitter                                        	|        81306       	|      1342310      	|       -0.039023115077905346      	|                   1                  	|                81306                	|              0.565311468612065             	|
| Wikipedia vote network                                         	|        7115        	|       100762      	|        -0.0830524827001603       	|                  24                  	|                 7066                	|             0.14089784589308738            	|
| email-Eu-core network                                          	|        1005        	|       16706       	|       -0.010990490627931076      	|                  20                  	|                 986                 	|             0.3993549664221539             	|
| General Relativity and Quantum Cosmology collaboration network 	|        5242        	|       14496       	|        0.6591640320931624        	|                  355                 	|                 4158                	|              0.529635811052136             	|


### High-energy physics citation network
Nessa rede há uma quantidade considerável de arestas, sendo 352324 arestas. O grau de assosrtatividade negativo e próximo de zero, mostrando que os nós de grau baixo vão se conectar com nós de grau mais alto. Possui alta quantidade de componentes conectados e o GCC abranje quase todas os vértices.

### Social circles: Twitter
Na rede, com 81.306 nós e 1.342.310 arestas, observamos uma tendência negativa de assortatividade de grau, sugerindo que os nós se conectam a outros com graus diferentes. A rede é altamente conectada, com um único componente englobando todos os nós, e tem um coeficiente de agrupamento médio significativamente alto (0.5653115), indicando uma forte tendência à formação de grupos na rede.

### Wikipedia vote network
Nessa rede há uma quantidade considerável de arestas, sendo 100762 arestas. O grau de assosrtatividade negativo e próximo de zero, mostrando que os nós de grau baixo vão se conectar com nós de grau mais alto. Possui alta quantidade de componentes conectados e o GCC abranje quase todas os vértices.

### email-Eu-core network
O coeficiente de assortatividade tende a zero, uma vez que o gráfico é essencialmente constante. Isso significa que, na rede ou conjunto de dados analisado, não há uma tendência clara de nós com graus de conexão semelhantes se conectarem entre si. Em vez disso, as conexões parecem ser mais uniformes, resultando em um coeficiente de assortatividade próximo a zero, indicando uma distribuição menos tendenciosa de graus de conexão na rede.

### General Relativity and Quantum Cosmology collaboration network
O gráfico é classificado como "crescente", o que se traduz em um coeficiente de assortatividade positivo. Isso implica que, na rede, nós com graus mais elevados tendem a se conectar com outros nós que também possuem graus de conexão mais altos. Em resumo, estamos diante de uma rede assortativa, o que significa que a tendência geral é de que os nós mais conectados estabeleçam ligações entre si, criando clusters de maior densidade de conexões entre os nós mais influentes na rede. Esse padrão de conexão pode ser relevante em diversos contextos, como em redes sociais, onde indivíduos com muitos contatos tendem a se relacionar com outros de igual influência.