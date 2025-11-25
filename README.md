# 🛡️ Inteligência Artificial Aplicada à Segurança Cibernética

### Detecção de Anomalias com K-Means e DBSCAN

Este projeto demonstra como técnicas de **Inteligência Artificial** podem ser aplicadas à **Segurança Cibernética** para detecção de anomalias em tráfego de rede, utilizando algoritmos de *Machine Learning* como **K-Means** e **DBSCAN**.
O pipeline inclui geração de dados fictícios, ETL, análise exploratória, modelos de clusterização e visualizações.

---

## 📁 Estrutura do Projeto

```
📦 projeto-seguranca-ia
├── dados_ficticios.csv
├── etl.py
├── dbscan.py
├── kmeans.py
├── analise_exploratoria.py
├── visualizacoes.py
├── main.py
└── requirements.txt
```

---

## 🔍 Objetivo

Demonstrar como IA é aplicada na segurança cibernética para:

* Detectar **padrões anômalos** no tráfego de rede
* Ajudar em **resposta a incidentes**
* Automatizar **monitoramento de risco**
* Auxiliar na prevenção de intrusões

---

## 🧪 Funcionalidades do Projeto

### ✔️ Geração de Dados Simulados

Criação de dataset representando tráfego de rede com variáveis como:

* Bytes enviados/recebidos
* Número de pacotes
* Latência
* Flags simuladas
* Probabilidade de intrusão

---

### ✔️ Pipeline ETL

O módulo `etl.py` realiza:

* Leitura do dataset
* Tratamento de valores ausentes
* Normalização
* Transformações necessárias aos algoritmos

---

### ✔️ Análise Exploratória

O módulo `analise_exploratoria.py` gera:

* Estatísticas descritivas
* Distribuição das variáveis
* Matriz de correlação
* Identificação de outliers
* Caracterização do dataset

---

### ✔️ Algoritmos de IA

Dois métodos principais de detecção de anomalias:

#### **🔹 K-Means**

* Segmentação dos padrões de tráfego
* Identificação de clusters incomuns como potenciais ameaças

#### **🔹 DBSCAN**

* Excelente para detectar anomalias como pontos ruidosos
* Ideal para segurança pois não assume formato prévio de clusters

---

### ✔️ Visualizações Avançadas

O módulo `visualizacoes.py` cria:

* Gráficos 2D e 3D dos clusters
* Heatmap de correlação
* Distribuição de outliers
* Comparação entre algoritmos
* Gráficos de dispersão coloridos conforme anomalias

---

### ✔️ Execução Geral

O arquivo `main.py` integra tudo:

1. Executa ETL
2. Realiza análise exploratória
3. Treina K-Means
4. Treina DBSCAN
5. Gera visualizações
6. Salva resultados

---

## 🚀 Como Executar o Projeto

### 🔧 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### ▶️ 2. Rodar o pipeline completo

```bash
python main.py
```

Todos os gráficos e resultados serão gerados automaticamente.

---

## 📊 Tecnologias Utilizadas

* Python 3.10+
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Joblib

---

## 📡 Aplicações em Segurança Cibernética

Este projeto demonstra como IA pode ajudar em:

📌 **Detecção de intrusão (IDS)**
📌 **Monitoramento contínuo de tráfego**
📌 **Análise de comportamento de usuários (UBA)**
📌 **Resposta automatizada a incidentes**
📌 **Detecção precoce de ataques como DoS, port scan, brute force**

---

## 🧑‍💻 Autor

Projeto desenvolvido para fins acadêmicos e demonstrativos.
Criado para apoio em estudos de IA aplicada à Segurança Cibernética.