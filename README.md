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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7f7cfff-562a-3442-b4a3-392034a92021 | -12.24902 | -51.45447 | 2025-04-29 00:50:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 697360fb-c48e-37b2-a766-c26b65397c5d | -6.65573 | -47.60584 | 2025-04-29 00:52:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2e5d2708-18e7-33f4-8e19-cfac0f624105 | -5.11183 | -37.58656 | 2025-04-29 03:10:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d2776937-5089-3f39-b1f7-ff03ed0c5a0f | -5.10593 | -37.58556 | 2025-04-29 03:10:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8ecb463b-7759-355f-93c9-79acaa13a63d | -5.108 | -37.58526 | 2025-04-29 03:10:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5817139c-31ec-32d1-824b-41bb11866286 | -5.66323 | -35.75605 | 2025-04-29 03:13:00 | NPP-375D | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 86b7f848-62d3-3251-a7a6-28b1aacf8ceb | -5.65806 | -35.75512 | 2025-04-29 03:13:00 | NPP-375D | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.2 |
| aab52c17-2e33-3473-945a-48e6105c7281 | -10.04313 | -38.40554 | 2025-04-29 03:13:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4f62d7a4-c2fe-3b38-a49e-852feffc2843 | -10.0375 | -38.40406 | 2025-04-29 03:13:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| cc6b5dc3-595c-37a2-9c80-0a94ceb79061 | -11.97098 | -38.39452 | 2025-04-29 03:15:00 | NPP-375D | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7a524c8c-1fae-36de-8465-069767247519 | -11.96544 | -38.39355 | 2025-04-29 03:15:00 | NPP-375D | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7d58d88c-fc2a-3b86-bbe9-7d5e30e84c48 | -5.10353 | -37.58409 | 2025-04-29 03:34:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d175840e-080e-3ddb-b58c-a05404c97a48 | -5.10739 | -37.58472 | 2025-04-29 03:34:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 400174d2-e634-36ea-9cb9-446b9a9d802d | -10.99746 | -37.52349 | 2025-04-29 03:34:00 | NOAA-20 | SALGADO | SERGIPE | Brasil | 2806206 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 66bff48f-05d7-3503-9461-af4b733e92a8 | -10.6962 | -37.04913 | 2025-04-29 03:34:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0e8f2b93-bd69-3c57-9d55-cce3ad5b9954 | -7.23213 | -35.73175 | 2025-04-29 03:34:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d9c1d003-fb0e-31aa-a3bf-8b637107af79 | -7.4449 | -37.30247 | 2025-04-29 03:34:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c53986e9-1d4b-3cbe-b0b8-947de19ffe6d | -10.04248 | -38.40501 | 2025-04-29 03:34:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b1611597-3a18-339b-a5f7-d10ab2e9f26a | -8.62356 | -36.36167 | 2025-04-29 03:34:00 | NOAA-20 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2c1afdf1-a4c2-3597-bd50-9a482399e4fc | -7.23152 | -35.73555 | 2025-04-29 03:34:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1b5684ac-1364-3cc8-9377-88f53172e0f0 | -5.10559 | -37.58683 | 2025-04-29 03:34:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 73a01f70-9d88-3198-8ae0-ee029c1ff120 | -5.10946 | -37.58746 | 2025-04-29 03:34:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bc58de7c-c59a-32ce-b3f6-20ae5ccf3f4b | -10.69661 | -38.27976 | 2025-04-29 03:34:00 | NOAA-20 | HELIÓPOLIS | BAHIA | Brasil | 2911857 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2d750d83-65f0-3677-b393-b39e82f8e5d5 | -9.94965 | -36.6343 | 2025-04-29 03:34:00 | NOAA-20 | FEIRA GRANDE | ALAGOAS | Brasil | 2702603 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c7803902-2346-370d-9f1c-6811bfe04bc9 | -5.66021 | -35.75589 | 2025-04-29 03:34:00 | NOAA-20 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 29d92c5a-9cad-34c5-9ca6-c2a6f11a86ad | -10.03871 | -38.40426 | 2025-04-29 03:34:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 96cbfff1-9f07-3571-8772-a1fdbbeaec12 | -5.11126 | -37.58535 | 2025-04-29 03:34:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4a3cced5-3ad6-39e3-afe8-da98bcaaaac8 | -11.99336 | -37.97171 | 2025-04-29 03:36:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 335cbd83-138e-3a40-b312-98aa794aa0a0 | -11.96737 | -38.39297 | 2025-04-29 03:36:00 | NOAA-20 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 491908a0-8b0b-319c-96f6-cbad3a34d93c | -12.78245 | -38.49647 | 2025-04-29 03:36:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7d25213c-06cc-32b3-b692-7ddd0857b685 | -12.77903 | -38.49812 | 2025-04-29 03:36:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 64271a0a-7551-3b7e-a87c-fa037bd30a52 | -21.17867 | -44.27489 | 2025-04-29 03:38:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 05c1d83d-4da6-3302-879a-c2fff41dc173 | -19.71744 | -40.35353 | 2025-04-29 03:38:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| be7a528d-60eb-3b9a-80f8-a75fa9b38d31 | -19.46535 | -44.29978 | 2025-04-29 03:38:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53cc8035-145a-3304-a979-95f81a444ef8 | -21.1799 | -44.27214 | 2025-04-29 03:38:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 047196e0-fac2-3c40-b5ff-e2bcb93e028d | -26.83216 | -50.91857 | 2025-04-29 03:40:00 | NOAA-20 | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 73f14c7f-d9bd-33b5-b471-f60b15db7f4a | -31.31492 | -54.15847 | 2025-04-29 03:42:00 | NOAA-20 | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| 8f5c7fba-1ce3-3929-8989-c86c82a479f7 | -8.94711 | -44.23676 | 2025-04-29 04:25:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a762e64c-519c-3891-882b-40be39453b0c | -8.17083 | -55.0725 | 2025-04-29 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1852cce5-7099-3fd8-81f7-37aca1ac0bdf | -8.9506 | -44.23731 | 2025-04-29 04:25:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d986e476-6ba2-3859-ac84-4b2ada0f7172 | -10.82503 | -37.16632 | 2025-04-29 04:25:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f7e1c535-2ebb-301f-a47a-2f83459bd657 | -11.9949 | -37.97196 | 2025-04-29 04:25:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| dd5f9d18-d7ce-3790-842e-26aa41476a17 | -5.10508 | -37.58536 | 2025-04-29 04:25:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| eeb3b4de-bd45-3226-9d9e-e1be3d818c66 | -5.11011 | -37.58615 | 2025-04-29 04:25:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2376ae1b-b4a6-3e58-b596-72caa9754976 | -11.99303 | -37.97105 | 2025-04-29 04:25:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9ee4f252-d09b-3e18-8151-0a53eda3f9ce | -11.99531 | -37.96843 | 2025-04-29 04:25:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 42c8d3ef-1cb9-39de-ab2c-8e3867af0c68 | -10.66764 | -44.49238 | 2025-04-29 04:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05b8aa57-1ef0-3791-8f56-dad508d436fb | -10.25027 | -40.54594 | 2025-04-29 04:25:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c8de1ea7-0c1a-32b2-b4b7-ef890804f650 | -11.395 | -52.9432 | 2025-04-29 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 305ef7fc-9d63-3771-89f8-619197c4d5bb | -11.42826 | -48.71908 | 2025-04-29 04:27:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c8af214-0554-36e0-8be4-d459e5474f5d | -17.34781 | -41.65928 | 2025-04-29 04:27:00 | NOAA-21 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 562cba1e-0d66-3fbf-9772-a19e6c3faea7 | -11.40675 | -52.94933 | 2025-04-29 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a82f2a23-328e-3a00-b094-a3938bae352e | -12.25097 | -51.44848 | 2025-04-29 04:27:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84d8cf9b-3ebb-3751-971d-79efb1b08dab | -11.42884 | -48.71544 | 2025-04-29 04:27:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c8ad350-3367-3e12-b3a4-d472b7a44dfe | -15.07784 | -48.94488 | 2025-04-29 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84e92f88-811a-3170-8471-fabfeb6dc3e7 | -11.40744 | -52.94549 | 2025-04-29 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b82c3b2f-7373-3764-a0ba-8e43b8e6678f | -15.08116 | -48.94543 | 2025-04-29 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1b8cb82-f8e4-32e9-8b5e-8564f2d8ce27 | -17.67136 | -46.76065 | 2025-04-29 04:27:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6427bca-4692-3e38-a833-36efe5b2f4e1 | -21.13169 | -47.80184 | 2025-04-29 04:29:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a79352d5-4611-3f86-b7f8-6ffdbd4d1322 | -19.36842 | -48.60657 | 2025-04-29 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 96089f31-faed-3ee0-9d25-fd934e250fe0 | -22.54025 | -48.81261 | 2025-04-29 04:29:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e37ab47-5a56-390e-a568-e2f627e5686a | -20.41804 | -43.55172 | 2025-04-29 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1a4a922e-0bbb-3304-b82e-833866f191e6 | -20.02494 | -47.18138 | 2025-04-29 04:29:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63bc9923-16dc-3153-b0f7-ebd306eb05a2 | -20.99832 | -51.79254 | 2025-04-29 04:29:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b9d87bca-94cf-35b9-888b-0b966be4c6b5 | -19.45604 | -45.30706 | 2025-04-29 04:29:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b493fc9-c421-32e6-8f02-e40c5b502855 | -23.98626 | -48.9191 | 2025-04-29 04:29:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e32602b-842a-38a0-aa99-c870cefa2c32 | -28.58555 | -49.44097 | 2025-04-29 04:32:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 46d18554-105e-3439-ba7b-1e6e6aee05fc | -26.99786 | -50.92986 | 2025-04-29 04:32:00 | NOAA-21 | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4f71cd02-3593-34be-bb13-457c0c14741c | -27.11599 | -50.58102 | 2025-04-29 04:32:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e2a2bae7-2f6b-373c-abc9-75e112776d44 | -27.21546 | -50.66365 | 2025-04-29 04:32:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dff54119-1f11-3c93-9d8f-f55dd67bfa9b | -25.19125 | -49.32631 | 2025-04-29 04:32:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 13e15375-e503-3913-80b9-4bef8b75fe2c | -31.31998 | -54.16174 | 2025-04-29 04:32:00 | NOAA-21 | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| 0250f962-d114-3445-b726-2a229c8bf38f | 1.11746 | -60.52687 | 2025-04-29 04:49:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68c78510-4c66-3687-9d75-14f9d7783272 | 1.12356 | -60.52966 | 2025-04-29 04:49:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc845ecb-1ef1-3cc2-b76b-0eabc251e51e | 1.11635 | -60.51971 | 2025-04-29 04:49:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d406df8-dc6b-333a-bf78-9dafd315e870 | 1.11802 | -60.53048 | 2025-04-29 04:49:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00baf6d6-d8cc-3767-a011-c9cf697616da | -8.94659 | -44.23576 | 2025-04-29 04:51:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfb79c79-b823-3b45-850a-e86847cf0fe4 | -8.17251 | -55.06869 | 2025-04-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fb7437f-9b59-3c4d-86a7-dc30f4cd06c1 | -5.26147 | -47.46623 | 2025-04-29 04:51:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f04b50b5-b19f-3aed-a302-42d577fbe9c6 | -11.39237 | -52.93969 | 2025-04-29 04:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc63e8ea-f3e0-3a4d-8aa5-836b66f5e93e | -15.078 | -48.94666 | 2025-04-29 04:53:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7527f7a-0af2-35c3-9a58-95cba3db1dbc | -11.42628 | -48.71775 | 2025-04-29 04:53:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d7b9d77-cb4b-3997-810d-3052fca6c510 | -15.07863 | -48.94631 | 2025-04-29 04:53:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 628c47de-6aa0-310a-a228-ea260851a5bc | -12.25096 | -51.4492 | 2025-04-29 04:53:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17b509dd-8af0-3ab8-b4d5-0e7e0e891bb8 | -11.40466 | -52.94896 | 2025-04-29 04:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad9fdc2c-319f-303a-9c62-15aa44fc5c2f | -9.96458 | -57.50491 | 2025-04-29 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cdfec5e-28dc-337a-bfde-f6a387a51118 | -9.9638 | -57.50956 | 2025-04-29 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b513071f-9f04-310a-b6f0-7deb392cbf0a | -15.07856 | -48.94252 | 2025-04-29 04:53:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2edf01a-6e4a-3a3e-831a-6f25c8caf03a | -11.40521 | -52.94538 | 2025-04-29 04:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8112167-b6fe-307b-975e-c1787bb44478 | -12.25041 | -51.45187 | 2025-04-29 04:53:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1488ce2f-03cc-3fec-920e-3a020dc320b7 | -11.39517 | -52.94379 | 2025-04-29 04:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 109d9b29-9822-3e93-b90f-482b780619bf | -9.69422 | -56.43787 | 2025-04-29 04:53:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a66615d-3a3c-3c2f-80e7-2fd4123ab597 | -12.24744 | -51.44866 | 2025-04-29 04:53:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7b19684-8976-3136-9295-5d1213f0f936 | -12.25099 | -51.44789 | 2025-04-29 04:53:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b5dff98-513c-3ea4-92e0-f7c4de7a8f05 | -13.13293 | -53.25106 | 2025-04-29 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 458a1ce4-b346-35c9-b821-21a210236407 | -22.53879 | -48.81318 | 2025-04-29 04:55:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccf2e071-c507-309f-977a-6a2e7ae68ba6 | -21.19541 | -44.93888 | 2025-04-29 04:55:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0997a2ba-b436-3439-afc3-93d598d41154 | -20.47773 | -53.67703 | 2025-04-29 04:55:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d57b14b4-571d-34e5-93b2-3b66e1d465db | -24.24424 | -50.73922 | 2025-04-29 04:57:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f619676b-c881-3f69-8168-364e9243d6f9 | -31.31711 | -54.15822 | 2025-04-29 04:59:00 | NPP-375D | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |


[Clique aqui para ver as próximas entradas](README2.md)
