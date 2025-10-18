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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40f6afea-e7d9-3852-beda-c50e6c3795a6 | -10.53235 | -55.72007 | 2025-10-18 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c693ab11-4e58-370b-8a90-207de1d5b64b | -12.04819 | -54.24216 | 2025-10-18 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 553b13c6-6796-3bda-aa24-2205a20ea316 | -10.97824 | -47.92627 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75748077-c832-3dab-b484-88c3c1a1be61 | -13.7786 | -48.24328 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e46ebe78-d5ed-35e3-bda3-930526493919 | -10.2408 | -44.06376 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d8434bc-cd8c-3b0f-b1f7-d4b6963400fc | -14.41837 | -52.80403 | 2025-10-18 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b47fc614-23fb-3382-9264-fe490da8fd8e | -10.47985 | -43.42942 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c1bfe016-23d9-3b9d-bc0b-433fa199b7c1 | -10.44326 | -49.35863 | 2025-10-18 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83640705-bed4-3bf5-9154-57615e449518 | -10.14131 | -44.53665 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa27fc21-a1f0-3cc9-8e2a-23865d1e4801 | -9.22326 | -61.8308 | 2025-10-18 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd9efabd-9fbe-3eaa-b8c6-ad55bad490cf | -13.41707 | -47.98184 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d81e57f-217b-3a81-b34d-105237aacbf9 | -10.26015 | -44.06741 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8f13b486-b1c0-3073-8664-d35f81029eb2 | -14.89869 | -52.4046 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44462d66-fe96-3304-b243-a6a8ec87fc52 | -14.06202 | -50.05258 | 2025-10-18 04:51:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 114c32d0-84bd-3cec-bd1e-567680349dd3 | -12.16359 | -45.09288 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe33af06-46d6-3db5-85dd-ae531d046cfa | -13.2184 | -43.98492 | 2025-10-18 04:51:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2164a58b-83db-33ca-a288-ac287c58076a | -12.66416 | -54.76693 | 2025-10-18 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5604f98f-20a0-3a30-8c45-0e77f0c4c2dc | -10.98214 | -44.31989 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e555dd5d-76df-39c9-bf94-4402cbcf9925 | -10.22845 | -49.68553 | 2025-10-18 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3502ef47-7cff-3954-8516-c9086ffcf292 | -11.20708 | -47.83057 | 2025-10-18 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 00840573-d793-3771-a2e3-e0b093014127 | -17.48897 | -43.46428 | 2025-10-18 04:51:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a02c6cc-28a9-366a-8ebf-aa9d4d43a5a4 | -13.68847 | -47.71981 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b40ba3d2-431c-3230-92ca-7229870aaf85 | -11.20395 | -47.82224 | 2025-10-18 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7abc6d3-1c42-36be-a42a-f4d2353a62f5 | -13.00392 | -43.85701 | 2025-10-18 04:51:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a7a5c3d-f9b1-32ab-8023-88ba9c74e013 | -9.77683 | -57.40865 | 2025-10-18 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b83db4a-3e07-35bf-a404-20dba186b55d | -15.04325 | -46.60529 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6d1f41f-9e84-3860-89bc-988f439c1e04 | -11.4735 | -49.81993 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91c93b31-9d91-3795-b0e0-1b90c18c10e4 | -12.91952 | -48.57981 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a76427b-da2e-3748-87cd-a37df410c5ea | -11.47783 | -44.01488 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5da1ed5-f524-3491-b93d-89b582c56c37 | -11.40813 | -44.26876 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f910fdd-764f-3eee-88c0-4ca2fe5b48df | -10.25974 | -44.07074 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f4c9eb4e-001d-3b51-a294-3a50280ce390 | -9.91138 | -47.66268 | 2025-10-18 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cda147f1-e67c-335c-a58a-efae1c68b4f2 | -14.41153 | -49.41013 | 2025-10-18 04:51:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 465c49ca-a879-3c56-a4ff-1b0599031958 | -13.61762 | -43.96338 | 2025-10-18 04:51:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a0cdee2-f17b-3892-ab29-938da62b408e | -11.3565 | -45.26056 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc36edb7-f031-3234-9b69-5023464214b6 | -9.91609 | -47.65935 | 2025-10-18 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c2143953-42d6-31cb-b5d6-3e0babfd7cd3 | -14.90784 | -52.39034 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f937907d-7e7d-3c39-bedf-89e4c2fb2a2a | -10.51651 | -43.40983 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 910ec1ea-7967-3fd4-9d9e-809922ee4a56 | -12.65141 | -54.76113 | 2025-10-18 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b616aa00-8fc1-3edb-b743-1abd88f9061e | -14.50385 | -45.61036 | 2025-10-18 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4dadd72-e905-3454-bc3b-c553aa9624e3 | -13.04017 | -48.19324 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b33b64e-b6b0-31d6-bedc-0b25dfb807f8 | -12.64692 | -54.76774 | 2025-10-18 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f759b7ec-30d4-38e3-8620-9faebe1ba925 | -14.86446 | -52.44617 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec017a4a-6531-3afc-90a2-4416689fc8d9 | -14.93792 | -46.70903 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cec2d0be-148d-3398-88bb-bbc5568308cb | -16.64715 | -52.52427 | 2025-10-18 04:51:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9074ffee-92ce-3dbd-88ca-e80512d2e474 | -9.97953 | -48.2403 | 2025-10-18 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79859710-cd46-3822-872e-9c755fe5c174 | -11.94194 | -44.24267 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88286f01-246e-37da-908d-06a37bd266f7 | -10.42888 | -44.91111 | 2025-10-18 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c10ebee6-9e18-38e2-a95a-04b6fd45856e | -10.63645 | -42.30713 | 2025-10-18 04:51:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8b963c74-8650-3029-b3d6-78cf25c6a7a6 | -12.49217 | -45.50348 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 210753d2-ac66-3971-9a08-5e0cd56cd32e | -17.84565 | -42.62558 | 2025-10-18 04:51:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2a898812-c9ed-3efa-97a1-f29eeecad6ef | -9.97152 | -48.23906 | 2025-10-18 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f7b016c-c486-3b01-ba35-bc1fda2522f6 | -10.14736 | -44.53067 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f73088a-e2f4-35e9-81a8-c6d6140512e1 | -14.7621 | -48.19884 | 2025-10-18 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0739f324-af0b-3e26-bb7a-3fb72bf3b615 | -10.23144 | -44.0521 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2fca8cf-4474-3611-86e7-0295e8cd581e | -10.23639 | -44.05593 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4373e1d3-077c-391f-ba70-68138687e365 | -12.2961 | -47.11096 | 2025-10-18 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28bebcea-36ac-3ebb-8f25-5138e0853394 | -10.81954 | -43.9324 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfa40af3-b0a7-3979-8911-52c6eb6c9567 | -10.6414 | -45.31416 | 2025-10-18 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 632cc0cb-9452-3d88-af33-e1d9c4f99d5a | -12.17818 | -45.0792 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09b4f272-cfb6-3d0b-a076-594b997925db | -15.04768 | -47.30974 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 388297c7-fddb-319e-9f74-d8454ac4ef9e | -10.49895 | -43.45844 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0e83263-8af4-344a-8621-8b92943f4d12 | -15.45598 | -45.93966 | 2025-10-18 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd45f18c-6972-31fa-b740-475aa0bfe152 | -11.75167 | -61.07718 | 2025-10-18 04:51:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7aea8bbf-1d1b-3add-a17c-fd0f170a2ab7 | -10.24124 | -44.0604 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96dfc46e-3c2d-391c-b8a1-d6a78344fe3c | -10.95243 | -45.455 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45362309-9f63-3c05-9b44-ee5922d31ba4 | -12.99037 | -48.46034 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60c685d0-4c3b-3c5f-9a52-db691b109560 | -7.85728 | -61.49604 | 2025-10-18 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bbcc446-7b81-3b3a-92fb-89aa40e360b4 | -10.99651 | -47.9169 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e36825fd-2ba7-3d08-962d-5684e72b78bb | -10.82499 | -43.93307 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 534869c1-17bc-3b31-add4-8cfbc7700156 | -9.77035 | -48.74814 | 2025-10-18 04:51:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 230a5251-b22d-34b9-a244-c6d3ccc88427 | -11.49144 | -44.17086 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ba9befb-4e3f-3a89-92eb-d573af713568 | -13.68785 | -47.72452 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32882c4b-14b3-3929-97b6-d5029f223798 | -10.68242 | -44.56842 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 317d01fe-b808-3f67-b996-6f0baf530514 | -11.36611 | -45.26501 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd1c85a9-0269-3fec-8de7-20665ee2bbf5 | -11.47237 | -44.01418 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f481f16d-cda1-3de1-aeb3-d5e2e961b2fc | -15.05278 | -46.60728 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59a0b93f-52e0-30cf-b0bc-d2cf363fe22f | -10.52299 | -43.40369 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 267c6c0f-6cf4-3c7a-9930-ca8f570acdef | -12.6475 | -54.76416 | 2025-10-18 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e761ce1-a763-31c2-9f40-b73fe25d0c2b | -11.73166 | -59.31653 | 2025-10-18 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb61a6d1-0789-390e-89a4-2325400a14f6 | -13.70707 | -47.714 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79b5a345-19bc-38bb-9549-4fd58ec5dfcf | -10.8103 | -44.01817 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca5830e0-f47b-3cb2-bc63-e2e67b80f3e1 | -10.95854 | -45.46355 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d3edbe3c-6368-3238-b08c-180b0cf056cc | -9.48563 | -54.49964 | 2025-10-18 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 614cb757-4555-3439-89e2-2a24216610dc | -15.18222 | -47.09152 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22019004-1503-3454-bad1-ba81b78ca825 | -14.92219 | -46.71837 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33df8842-a6f1-3d5c-9776-9e1dcf51133d | -12.16596 | -45.09376 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bea2233e-eaee-3e7c-b3ad-ca3ed5c15b33 | -12.48587 | -45.47282 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88d6426b-aebc-31e6-8ae8-7c005f20ab47 | -15.03979 | -47.29828 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b32d93d-8524-3315-9e7a-2c191d8b9948 | -13.73446 | -48.12044 | 2025-10-18 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0159be58-ff1b-3fcd-b10f-e256c830e5ce | -15.51196 | -50.38651 | 2025-10-18 04:51:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e0dab5ef-cc22-3481-8b49-ad85a2f23309 | -14.75786 | -48.19782 | 2025-10-18 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a9fba49-b161-3f07-9d58-5f8eaf21702f | -12.04487 | -54.24161 | 2025-10-18 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eef3a56b-85d8-3c6c-b346-e6a79dcc7cfc | -10.11305 | -44.5517 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ec28ce0e-5230-39ce-b2a3-7d8ba42b088b | -10.96769 | -45.47012 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 59cd5934-a673-3cb2-9d4f-410bc89e6789 | -7.68441 | -61.04373 | 2025-10-18 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b2527375-53fc-3a01-8240-342d3ef1f0f7 | -13.40405 | -48.58684 | 2025-10-18 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 258049ea-7539-39b9-b4cb-20b271e28c3d | -10.505 | -43.45554 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f74237e-4c32-3e58-b6bb-42a9471024a5 | -8.63107 | -54.71047 | 2025-10-18 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13393493-7eb7-3049-ad0b-82e61f9b6739 | -11.5011 | -44.05053 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README85.md)
