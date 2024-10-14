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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 396f1e86-31b3-375d-83e2-3bec40b9a9f8 | -7.96473 | -49.06666 | 2024-10-14 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49384440-6983-3d68-8dad-03c81b76783d | -7.96243 | -49.05846 | 2024-10-14 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58cfcaa6-ccd9-3152-84af-9846856c9e46 | -7.96185 | -49.06228 | 2024-10-14 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61e097d4-92bd-3661-8270-8020081feca4 | -7.95838 | -49.06175 | 2024-10-14 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 884fe9e1-a8e8-34bd-bace-f020ff3ccee1 | -7.95549 | -49.05738 | 2024-10-14 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad35f754-fd80-3372-84b5-ca6c6533f67d | -7.72855 | -49.8967 | 2024-10-14 04:44:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3350d23b-5f14-38bf-8b6c-58b44d0c7134 | -7.71564 | -49.30332 | 2024-10-14 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f7693fb-40c0-36ed-9ed0-8686f25306a5 | -8.88905 | -50.13344 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93cc7c90-d700-3bfa-926f-ecc6c6ac1c47 | -8.66002 | -49.92345 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ec1b5ef-ee5e-3c7b-88e1-c3b5bec35c9d | -8.65662 | -49.92293 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d52c67ef-849a-33b7-95e4-ef023c23ad29 | -8.65607 | -49.92656 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25924462-7d93-3d0c-8366-b73c85b2e693 | -8.65323 | -49.9224 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b31de2e-2ac1-39d4-8ab6-20c92279c5ad | -8.65268 | -49.92604 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c574cfc-2727-3535-9a41-470bc080022d | -8.30832 | -50.12177 | 2024-10-14 04:44:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8700337-ed5e-30e3-98b0-92370f7fa387 | -8.27425 | -49.09162 | 2024-10-14 04:44:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00c0c72e-70c6-3297-a261-ecc93c379ce3 | -8.26372 | -49.50253 | 2024-10-14 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20774d13-5259-348f-95e3-35ff3d3a996c | -8.06357 | -49.39684 | 2024-10-14 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2aafedc4-d8aa-39d7-b2ee-e5f39fcc5efc | -8.02712 | -49.63723 | 2024-10-14 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e77b27c-d775-3bf5-8e4b-b9afbd2fedde | -8.02316 | -49.64037 | 2024-10-14 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b79a0c97-d7e2-3ab6-b1a2-132d9e4f5876 | -7.95198 | -49.39557 | 2024-10-14 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 273dd35b-7350-3980-b0a4-69098b4f2513 | -8.63664 | -48.69603 | 2024-10-14 04:44:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fc8132b-0c14-3c75-9785-76413c444ab0 | -9.1629 | -49.82716 | 2024-10-14 04:44:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55f31c9a-2b8b-3cc1-a55d-2d7c4486a760 | -8.8896 | -50.12983 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c42008ed-9d54-3ef9-9a6e-d2790b63da9e | -8.74046 | -49.92106 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59b97334-b43b-30ac-8184-1532b38bcb51 | -8.73707 | -49.92053 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10ae062e-b63f-3453-a36d-030bdfb6b849 | -8.54235 | -49.71148 | 2024-10-14 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 242638db-214e-3cf9-9fc4-a71f69dbc57d | -8.45036 | -49.71986 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7ddcd52-c322-3ef9-ab17-bcf82fe8a107 | -8.3592 | -49.36024 | 2024-10-14 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fdd5608-9911-374c-9b99-9e16cb981268 | -8.35576 | -49.35971 | 2024-10-14 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37cfb7dd-5b8c-3b2a-84c3-c47901a79b00 | -8.33551 | -49.96746 | 2024-10-14 04:44:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1af8102-1bbd-3395-a917-03e281b98e21 | -8.26029 | -49.50199 | 2024-10-14 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfce07d1-fe99-3e04-b344-14a46dadcaea | -8.18227 | -49.9402 | 2024-10-14 04:44:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c9e9c13-3828-39e8-8016-959f0a1d483a | -8.02768 | -49.63357 | 2024-10-14 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7490ced9-6e74-3ee2-93da-6103adb606e2 | -8.02483 | -49.62937 | 2024-10-14 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab37892e-c16a-3d3a-b038-b1c8085da1ba | -8.02427 | -49.63303 | 2024-10-14 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f484a447-416e-3330-b0a8-c057c4a473cd | -9.63878 | -48.94721 | 2024-10-14 04:44:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de750a39-acde-34cd-8b52-2b193594a47f | -2.1959 | -48.85266 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 73fbe052-dd5b-3921-bc5f-2704f7aee882 | -2.19535 | -48.85619 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3f008589-5cc3-3167-92ff-c57193c9c0bc | -2.18109 | -48.85013 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9398610-dc58-3c22-a994-8a3b66a5180d | -2.1794 | -48.83902 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 22c5005b-49aa-372e-bd23-f5765fd1ca6e | -2.17604 | -48.8385 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6df042fa-e4cd-3aea-9a8f-e716010a8991 | -2.17549 | -48.84203 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35e8c70d-a062-3fe6-aac1-ec30f4df4bd3 | -2.17213 | -48.84151 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b9c0a20-3d5d-377b-938a-42035dbad684 | -2.1615 | -48.84348 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd09f12c-0bba-3d29-ac03-8f4530a29fce | -2.16095 | -48.84701 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a7ac2d8-fc58-342c-ae95-b152e8ea6446 | -2.15981 | -48.83237 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d0ba22a-b44a-3acf-b4c7-ab44d8de1163 | -3.65233 | -49.62327 | 2024-10-14 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 349fe91d-9fcf-3271-944a-0aee26f7f28a | -3.49483 | -50.49518 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aca68bfd-b9ba-3370-bb85-6226180e06a4 | -3.49205 | -50.49121 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8d50c33-161d-3036-b43b-0fec02c49b3c | -3.48873 | -50.49069 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fdefd5e-9486-34ee-b360-6f4db9863547 | -3.48486 | -50.49363 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79d56877-b86c-38fb-ba0f-b7f5201720b7 | -3.48432 | -50.49708 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b1007c6-d2a4-3522-b963-cdaf64a1b9e7 | -3.48377 | -50.50053 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6137bffd-a125-3062-bbd0-997861d0efb7 | -3.48154 | -50.49311 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d2f2398-768a-338f-b22d-2f8d82de44bc | -3.48099 | -50.49656 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e2bbffe-88c2-332c-be61-71750f347d4b | -3.48045 | -50.50002 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3658c395-5c8a-3a0e-8955-48d74e67cae0 | -3.4799 | -50.50347 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 484dd17a-1764-33ee-b6c3-2524e482907a | -3.47822 | -50.49259 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa950ab9-c28b-363d-b4b5-7f650704c143 | -3.47767 | -50.49604 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d85340aa-1a70-342f-8746-4d2880729888 | -3.47713 | -50.4995 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71d7de28-b5bb-3269-9cba-fb1f051eda06 | -3.47658 | -50.50295 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c966a37b-281d-351b-a6e5-eeb2c460d7ca | -3.46685 | -50.60773 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 400d556c-595a-311b-a802-b8b684d7091f | -3.46353 | -50.6072 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3427eb1-d9e1-3b00-900b-f18ad4b1f327 | -3.46298 | -50.61067 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 18962e4a-0d21-3d3a-b9f3-19514d336a59 | -3.46021 | -50.60669 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 796357eb-09d9-3ffb-a439-f25852213ef7 | -3.45966 | -50.61015 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12059388-2e98-39a2-ae98-9576e48cbde9 | -3.45688 | -50.60617 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a11fa164-9b6a-3e69-b718-c0a54d6d4ecd | -3.45601 | -50.31522 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 896e7613-3cbf-3344-9330-a23e1d0f9d00 | -3.45314 | -49.73064 | 2024-10-14 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cb3d405-3f00-3379-a964-b4dbe33f375f | -3.45259 | -49.73411 | 2024-10-14 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06a0f932-0030-3398-9bd8-11a1fe28b22b | -3.44948 | -50.1622 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2fb16a2-a13b-3f72-99bb-a18aaffd2f2f | -3.44894 | -50.16565 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 196d9a21-1e8b-33cc-a824-1085085981c0 | -3.44562 | -50.16514 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6faf706f-dfca-3244-b602-4e6781eabaa2 | -3.43898 | -50.1641 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd07b49a-068f-39f1-be24-f6fb3aa9cb6c | -3.42377 | -50.26071 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0bce59da-0ef8-3cca-9cf7-f1a2aabe8a2d | -3.42323 | -50.26416 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a7107be8-9d3b-3033-b5ae-50be6a88f754 | -3.40801 | -50.36078 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f0b7e2f-cc19-330b-947d-459c3bba7b67 | -3.40469 | -50.36026 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfd4a461-9a6c-3e69-8ac3-d8eb0d729daf | -3.33994 | -49.15134 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01bab303-c954-3237-8143-ab4f9c6d3d83 | -3.33884 | -49.1584 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94819cb0-8037-324a-8a53-f887747d6dd0 | -3.3383 | -49.16193 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa1a5fc2-945f-34b7-91f7-e0d30c141418 | -3.33823 | -49.14022 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89c2fe5b-2200-39d0-b3c4-97c554599816 | -3.33768 | -49.14376 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8776e3f8-de11-3a13-a248-90891e280fe9 | -3.33713 | -49.1473 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09289a98-4560-341a-a4ee-076d613f5cc8 | -3.33707 | -49.12552 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94da24fc-cb7f-36fe-ba5c-5d6a7bcd458e | -3.33659 | -49.15083 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34ebb218-4b2f-3f06-bb55-69a18b27eb96 | -3.33604 | -49.15435 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6f66352-4b35-3948-981d-341ff0103848 | -3.33549 | -49.15788 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82408bae-c924-3d23-8d4c-32d0507d874d | -3.3352 | -49.12533 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2d11a5c-2cc9-32c6-b064-a60d74c6fb14 | -3.33494 | -49.16141 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eae9bd0b-7f18-3a08-8762-b98748c3d67b | -3.30048 | -49.10552 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdccc335-fd4b-34d5-9391-226c1e8e2034 | -3.29993 | -49.10905 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7feaaa4c-1535-3d54-b473-5749a5c39a11 | -3.29937 | -49.11259 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1406af6-d5fd-3469-95b7-6814144cc626 | -3.29767 | -49.10147 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| effa1201-6f49-3aad-9a2e-04b644189a38 | -3.29712 | -49.10501 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d207e95-4130-39e6-88b4-7c174db55cce | -3.29657 | -49.10854 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c26df223-b0b8-31c6-b69f-7b088b1df534 | -3.29487 | -49.0974 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc42c511-9bdc-323f-8460-3dc0e72c74e3 | -3.29432 | -49.10095 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf55b735-1112-379c-ba00-fd20368c4023 | -3.29376 | -49.1045 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 930ab99a-3f53-3b37-86c0-fcb84aaa445a | -3.29207 | -49.09334 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README82.md)
