# SmallWorlds

## Resumo do trabalho
O trabalho consiste em analisar a assortatividade de cinco redes de gráficos com dados distintos, mostrando suas características e significados.

## Networks
### High-energy physics theory citation network
"O gráfico de citações do Arxiv HEP-TH (teoria de física de alta energia) é proveniente do e-print arXiv e abrange todas as citações dentro de um conjunto de dados de 27.770 artigos com 352.807 conexões. Se um artigo i cita um artigo j, o gráfico contém uma aresta direcionada de i para j. Se um artigo cita ou é citado por um artigo fora do conjunto de dados, o gráfico não contém nenhuma informação a esse respeito."

### Social circles: Twitter
"Este conjunto de dados consiste em 'círculos' (ou 'listas') do Twitter. Os dados do Twitter foram coletados de fontes públicas. O conjunto de dados inclui características dos nós (perfis), círculos e redes de ego."

### Wikipedia vote network
"Utilizando o último dump completo do histórico de edições de páginas da Wikipedia (de 3 de janeiro de 2008), extraímos todos os dados de eleições de administradores e histórico de votos. Isso nos forneceu 2.794 eleições com um total de 103.663 votos e a participação de 7.066 usuários nas eleições (seja votando ou sendo votado). Dessas eleições, 1.235 resultaram na promoção bem-sucedida de administradores, enquanto 1.559 eleições não resultaram em promoção. Aproximadamente metade dos votos no conjunto de dados foi feita por administradores existentes, enquanto a outra metade veio de usuários comuns da Wikipedia."

### email-Eu-core network
A rede foi gerada usando dados de e-mails de uma grande instituição de pesquisa europeia. Possuímos informações anonimizadas sobre todos os e-mails enviados e recebidos entre os membros da instituição de pesquisa. Existe uma aresta (u, v) na rede se a pessoa u enviou pelo menos um e-mail para a pessoa v. Os e-mails representam apenas a comunicação entre os membros da instituição (o núcleo), e o conjunto de dados não contém mensagens recebidas do resto do mundo nem mensagens enviadas para o resto do mundo.

### General Relativity and Quantum Cosmology collaboration network
A rede de colaboração do Arxiv GR-QC (General Relativity and Quantum Cosmology) é proveniente do e-print arXiv e abrange colaborações científicas entre autores de artigos submetidos à categoria de Relatividade Geral e Cosmologia Quântica. Se um autor i coescreveu um artigo com o autor j, o gráfico contém uma aresta não direcionada de i para j. Se o artigo foi coescrito por k autores, isso gera um subgrafo completamente conectado com k nós.

## Requisitos
- [Requisito 2](./requisito_2)
- [Requisito 3](./requisito_3)
- [Link para o vídeo](https://www.loom.com/share/5d222f7d61fa44478921150d56a5e472?sid=6695b16d-4649-4750-878e-5f888c2c0bf1)

## Referências
- [SNAP Stanford](http://snap.stanford.edu/data)