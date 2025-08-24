# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e916cac6-2227-3d5f-8d43-d3b8bcf00a67 | -9.51452 | -60.55697 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13dd7a42-d7f3-314f-afa6-047fb3465eaf | -13.66593 | -47.98541 | 2025-08-24 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6415247-4f4b-3a97-b229-0cd605acb9f0 | -13.44006 | -47.03254 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c46a0ca-c285-3d87-9e3c-4a4c327f15c2 | -14.47041 | -52.0773 | 2025-08-24 05:01:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfac70c0-0ef4-3f77-b8bd-eff2a1317a2d | -13.04833 | -45.23833 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42fa08f8-c387-34cc-a499-bfc598540189 | -9.01694 | -65.71871 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37e34967-985c-3217-a368-d077574c695b | -11.53601 | -51.85258 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| adf26674-6e09-3b0f-8d5a-6ffdb67232c0 | -11.18088 | -55.02625 | 2025-08-24 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a1fc5cb-bffe-3e3d-8c09-6cdd7da94f85 | -11.53346 | -51.86987 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f7bb059-c06e-3151-949b-6ca11a5d4f3a | -10.10222 | -57.76988 | 2025-08-24 05:01:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2711073d-1326-381d-afb6-12020fdac482 | -11.53935 | -51.90594 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43e823e5-4104-3949-892f-77b3d4148d49 | -9.01207 | -65.38335 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f68434e-ec56-30af-9669-106037e9103a | -9.99606 | -59.6201 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c13750c-5905-39aa-be6d-177cb21cabf0 | -13.45743 | -47.0188 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82a51cd3-fc7d-3cb7-96cb-902c45f3621d | -9.47588 | -63.13813 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12032c3b-e1e5-3305-90e9-694fbfb2d95b | -14.28957 | -60.38267 | 2025-08-24 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a954a38-dc03-37f6-ae56-bf3f4d7ae2f1 | -11.53474 | -51.86119 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ee607999-6191-3ac7-9ee5-398e32d30ad6 | -11.53044 | -51.86498 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4502dfb4-91a0-3a96-ac5e-c1b5600b0a64 | -13.47243 | -47.02435 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff10b790-4f93-37ae-9ddd-9005eedb4d5e | -17.60996 | -44.3064 | 2025-08-24 05:01:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c719b619-d251-3c52-9a83-00a47e73d93e | -13.02533 | -56.8226 | 2025-08-24 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfbc9f88-7bed-35a3-8407-45d79cbc5f1e | -16.79502 | -51.35092 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ae194336-09ef-32f7-a991-aada19f61cb8 | -14.33482 | -58.59798 | 2025-08-24 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b699252-31a8-332f-8b89-3c257dbac92e | -14.36523 | -50.7027 | 2025-08-24 05:01:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4a4671f6-861f-3196-893e-4ffb34ecab35 | -11.50784 | -51.86599 | 2025-08-24 05:01:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30b2f4ac-0c4b-310b-8374-a40ee705172b | -9.00149 | -65.70161 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ac56b48-0f18-3530-aea8-22e2be37a12e | -11.51213 | -51.8622 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40425a10-99b4-3709-852c-35fea0bec887 | -12.9417 | -46.29509 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0d0d1697-516f-3292-af03-31f42a06dca9 | -11.51579 | -51.86277 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3d049ca-428d-3e1e-bb4f-77e53fb9a9e8 | -9.04947 | -65.72059 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| daa2378a-a5d9-35e9-a821-1aadaf065541 | -8.99882 | -63.63586 | 2025-08-24 05:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e99e5c93-5149-3750-b8db-717be06bd3d4 | -12.73451 | -48.1288 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5ead05fa-7f73-3db9-9659-e5dbbfba2bf7 | -11.53968 | -51.85309 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 358c9752-60b9-35da-96f6-b2eb816b3bcb | -15.72368 | -56.05004 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0ba63ed0-f62e-34bd-a9d9-32f7cf6486f7 | -15.32065 | -56.16362 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e03e5a6-69d0-3fc9-9201-250f452effe9 | -11.79063 | -48.79175 | 2025-08-24 05:01:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 587ee755-9d3f-3804-82f5-96ea6e21ebc9 | -15.12531 | -48.63327 | 2025-08-24 05:01:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71e45b1d-0421-3d2c-9e62-1da00fd7d2da | -11.51517 | -51.86704 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad5a7db1-b7fa-30dc-891e-9f7dfa353c66 | -9.01634 | -65.39295 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d7dc3559-e409-3bb6-a8fd-dc4081a93eb3 | -13.50234 | -47.03598 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84d2c41c-cbb5-3fbc-b787-b97117e5476e | -9.01532 | -65.70431 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 215d1d20-548e-3adb-81b9-5870cb05d1b7 | -13.05253 | -46.32371 | 2025-08-24 05:01:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bde28ed-9913-3b41-8332-57dad5e059cc | -11.51088 | -51.87079 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1393e1c2-0c39-3786-9f95-6ec0661efd40 | -15.04388 | -48.51477 | 2025-08-24 05:01:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a09253e-d092-34a8-b482-6983b08fbe8a | -9.19111 | -64.55206 | 2025-08-24 05:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95bec87a-275f-3ecd-99eb-5e9f563cc04b | -11.54335 | -51.8536 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 35af5670-538e-32bd-988f-71501e3a9223 | -14.29915 | -60.37357 | 2025-08-24 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1524f667-1be6-3670-b0db-dc5f983b2c8b | -9.95947 | -60.18537 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b30df23-e767-37c6-a37b-5a3a6505f960 | -15.06482 | -46.4812 | 2025-08-24 05:01:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f1fa1bd-a255-3447-bb54-8614c9298428 | -15.68212 | -53.8745 | 2025-08-24 05:01:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c49a26b-ba62-3025-8b46-e547ad3e0ed2 | -14.53818 | -53.24118 | 2025-08-24 05:01:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce25170c-8341-3611-a07c-d616fd72d6d8 | -9.51882 | -60.55365 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68c5b60d-f8ee-3a5c-ad51-0e7207e9c8e8 | -13.05507 | -45.23086 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10cc4978-65cd-3a3b-bd2c-5b59691e06a9 | -9.9541 | -60.19194 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dfe6705-2ef7-3986-8f24-76bf4dc4c0c8 | -14.77204 | -55.4127 | 2025-08-24 05:01:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3791a79-6086-3e0c-93e4-00283b690173 | -11.42581 | -55.01157 | 2025-08-24 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7835dc9-1aac-3c8c-9ac1-86df32fb6936 | -17.06124 | -47.15504 | 2025-08-24 05:01:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cf39c4f5-2228-3802-ad9e-a3f405c05783 | -10.41978 | -64.42961 | 2025-08-24 05:01:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 629d31c2-34e5-3121-b7db-502dff040164 | -13.41995 | -51.78548 | 2025-08-24 05:01:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4140afa0-c517-3c14-8845-2f6099cc3bbd | -15.06522 | -46.4777 | 2025-08-24 05:01:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd7253d6-7363-3853-9659-d1f37511accf | -9.5177 | -60.51278 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0cef970-4a97-394e-9072-e91262ddd2db | -9.99814 | -59.61882 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0887fad-7e37-32ea-8c25-b551a867488a | -11.53079 | -51.91338 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a110132-cdd0-3a03-98f1-d61d3f6a3c57 | -13.47768 | -47.02418 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1733fed2-9526-3ba2-bf8c-d15a4b05dc34 | -9.01861 | -65.70967 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb94e712-3b46-3e08-95c9-37c15a9ecc6f | -16.49453 | -46.75029 | 2025-08-24 05:01:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea1109e5-596a-399a-bb7e-37000a415c23 | -9.00577 | -65.71196 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bcffbd1a-e8e7-3413-83b2-5667f1381fbb | -14.79364 | -59.62415 | 2025-08-24 05:01:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7b95e4e0-26cf-3b57-baf7-21823798a9d1 | -11.18033 | -55.02977 | 2025-08-24 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59e3a76b-be4a-3fca-83a3-b03f710cf402 | -12.99066 | -45.22953 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e5477d2-9312-3d1b-a134-5dd579906861 | -9.0213 | -65.70553 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9fec8718-a975-3acd-98b0-cacd8cf4e20d | -15.31789 | -56.15948 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b1d454d-daec-3136-ba1f-ade8875448b0 | -12.73667 | -48.11277 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4421a342-c554-3173-906d-e11ab730818b | -12.99604 | -45.23584 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26ead7c9-e971-3830-b402-abe3af1b8f87 | -16.3943 | -49.64486 | 2025-08-24 05:01:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1e6fd1ec-feda-34e6-8231-83cdb47b76aa | -17.21918 | -48.54565 | 2025-08-24 05:01:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4cfb55bf-b841-3e5e-bfa8-5f4e5c10e066 | -11.54639 | -51.85841 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4047c6cd-dcb5-3657-842e-3b8162ae941f | -11.69604 | -60.18318 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9707dbea-dd48-327e-9d5d-845c11384440 | -9.5086 | -60.51518 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 529cb1b6-a484-3e0b-ad2c-116bf35b2d11 | -14.84515 | -48.32025 | 2025-08-24 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 387cf831-de91-3d8f-9d2a-7674671433ad | -17.5934 | -46.10014 | 2025-08-24 05:01:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9be4d48-0578-3048-b139-66ec8574cd0a | -15.35154 | -53.91784 | 2025-08-24 05:01:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1192c70-047b-3242-955a-e81d74d0aa08 | -15.04179 | -48.18097 | 2025-08-24 05:01:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ef1c800-afd3-30a6-9b8b-aacc82ca1d94 | -9.02029 | -65.70061 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 68da0509-281b-319a-b7fb-648f73297978 | -9.00334 | -65.70205 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c216caa5-c597-37bb-a586-c38a86dfd804 | -11.53809 | -51.91449 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4708b769-2f9d-33d1-acf3-496954330f85 | -13.02992 | -56.87965 | 2025-08-24 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e9e81c7-dba6-3f87-8345-fc5328764898 | -14.78991 | -59.62371 | 2025-08-24 05:01:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f16897f-aed7-36ac-a08a-3bd03b135859 | -12.94803 | -46.28807 | 2025-08-24 05:01:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdd2b09b-8021-3e27-8fe8-395b77d52715 | -17.60355 | -44.3054 | 2025-08-24 05:01:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 36132093-3e1c-3cb3-9760-8afb1da9485c | -12.20406 | -47.11111 | 2025-08-24 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f524594f-37f4-326c-9d06-f329c393b87e | -9.51991 | -60.52537 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb432159-dd91-3af3-9da0-5d021a94814a | -16.41927 | -49.14229 | 2025-08-24 05:01:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9dd9cbd-63f0-3130-ba06-0cf0735776bd | -12.73168 | -48.12387 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 75e00d33-3bdc-3be9-8d45-865dac8a4389 | -14.80887 | -47.93825 | 2025-08-24 05:01:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c8da5a7d-64b2-3f7d-8801-278e7aee921c | -16.78997 | -51.35783 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4d0be275-3e45-3824-991a-c0cfd06bfe71 | -13.66379 | -59.83709 | 2025-08-24 05:01:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca177cf6-e5e9-3dc4-84b0-12f6d8a5491c | -9.00314 | -65.69276 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ba17844-af76-37ca-9e73-02785a71d349 | -13.35618 | -47.50605 | 2025-08-24 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c655266-2fb4-3d69-9b16-79fe9e0ec531 | -9.52236 | -60.5583 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README64.md)
