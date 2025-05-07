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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8311d59e-4fac-339f-bc8d-c0e7de3537f3 | -13.04618 | -53.72485 | 2025-05-07 01:11:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 39938631-c6c3-388a-bf4b-281ee9c01a4b | -13.4973 | -52.95374 | 2025-05-07 01:11:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9f3d7fc-900a-3583-8e7a-57d09fb95bd5 | -11.39397 | -52.94002 | 2025-05-07 01:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 9ed3e4d8-4306-30a4-8c41-7f1e07d7a32a | -11.77833 | -48.71783 | 2025-05-07 01:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1a8b8566-c1e3-3846-a7d4-f603f30109ef | -11.3963 | -52.9477 | 2025-05-07 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 6ec6b012-6afd-3d5a-bb5e-3a1b911c9232 | -17.1633 | -54.006901 | 2025-05-07 01:28:00 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 53183ab3-ab84-3d06-89b4-f1fbab2a78df | -13.5126 | -52.957001 | 2025-05-07 01:28:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5672ea32-f76a-3aff-9de8-29cbf739d2ee | -11.4087 | -52.943699 | 2025-05-07 01:28:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad9f5429-b057-33cd-91e4-233209edfecc | -10.2439 | -59.238701 | 2025-05-07 01:28:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1d029db-9ca2-39f1-b827-0a86715d3c62 | -11.4053 | -52.930302 | 2025-05-07 01:28:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4fc9406-0ec7-3c4a-ae36-413794ab8f0e | -18.299801 | -52.986099 | 2025-05-07 01:28:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37adf65c-2531-319a-9411-b5fd4a7be349 | -18.4307 | -54.701801 | 2025-05-07 01:28:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c8e24a30-8318-3572-a388-1bcce3d0054b | -18.3025 | -52.996601 | 2025-05-07 01:28:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 71b388e8-3b6b-32a5-a28d-7725cea4a8b1 | -12.1873 | -54.240398 | 2025-05-07 01:28:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5c1b8b2-a6e3-3403-ae1b-9508f157968e | -11.4023 | -52.959499 | 2025-05-07 01:28:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b46e48d0-2dea-37d2-980d-e3315c212710 | -13.0634 | -53.725101 | 2025-05-07 01:28:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d677ffd-71d3-3a34-a7d9-d5925008fb2b | -13.0536 | -53.727699 | 2025-05-07 01:28:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44b7c18c-92c6-39d5-b41c-15ebf1f96c35 | -18.4328 | -54.7104 | 2025-05-07 01:28:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c6404f61-bf55-3b10-80c0-3367275659d0 | -11.3956 | -52.9328 | 2025-05-07 01:28:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1adfe653-a8ed-3264-b190-7f5b2120bad7 | -18.297199 | -52.975601 | 2025-05-07 01:28:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fadb6b3a-1410-3c2d-b11e-0eb73c91a7dc | -11.399 | -52.946201 | 2025-05-07 01:28:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d6c5321-52ae-31d4-b0d5-7066437776b6 | -18.2707 | -52.994099 | 2025-05-07 01:28:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c3328ac2-4281-3223-81e2-851587b36223 | -18.4231 | -54.713001 | 2025-05-07 01:28:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 48be3775-6283-3bcc-b9df-2f22ff70adec | -16.661301 | -55.745899 | 2025-05-07 01:28:00 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a86bf226-5852-350e-90af-36d3042e9181 | -13.0606 | -53.713902 | 2025-05-07 01:28:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7cb351b-a620-3697-bd59-1cf661a5241f | -11.3963 | -52.9477 | 2025-05-07 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| aa5509d2-4bb0-3f4c-9f73-f34a799e8e27 | -18.284 | -52.9848 | 2025-05-07 01:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| c32db7ff-fb9a-3b1b-a530-a0b9012aa7d8 | -11.3963 | -52.9477 | 2025-05-07 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 51a1675c-59e6-37fc-bfee-70117b6fa840 | -11.3963 | -52.9477 | 2025-05-07 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 0ba7df23-e50b-32d7-9308-101b131d10a6 | -11.3963 | -52.9477 | 2025-05-07 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 7f53b67c-b6ea-3b44-ad74-1306c6029c4c | -21.056 | -49.9442 | 2025-05-07 02:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.7 |
| 61791d68-c7d1-30eb-8de4-c5e5227047c7 | -11.3963 | -52.9477 | 2025-05-07 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 7f32addb-bd7a-3e6e-a314-0892c16c0e24 | -11.3963 | -52.9477 | 2025-05-07 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 961f04a5-d470-326a-a736-0d5cd4861166 | -11.3963 | -52.9477 | 2025-05-07 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 625d75af-2bea-3d68-b837-775cfae8ecf2 | -11.3963 | -52.9477 | 2025-05-07 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 8ceee21b-784f-31e8-8e19-f654c7c2574b | -11.3963 | -52.9477 | 2025-05-07 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| dcc7a913-cf3d-38e5-b258-6e5422baed9e | -11.3963 | -52.9477 | 2025-05-07 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 9b275730-24ea-36f5-b0e0-09168331f346 | -11.3963 | -52.9477 | 2025-05-07 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e0534b0d-2571-338f-8700-3e05599d6b6d | -11.3963 | -52.9477 | 2025-05-07 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| d3bbcd8a-06ae-384d-9da8-9468f47ce413 | -10.71784 | -42.32293 | 2025-05-07 03:36:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 128e51cb-7d15-31a3-85b8-97b340933392 | -7.21318 | -35.78183 | 2025-05-07 03:36:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 82d2d95a-7d60-3252-931c-cbc12f0fe168 | -8.08217 | -43.12682 | 2025-05-07 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 79b9d10e-ccd5-3956-8a18-6961f8eb1cb7 | -6.74485 | -44.52655 | 2025-05-07 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4833d1c4-1727-3cc5-b1f9-1036d18ea875 | -5.16523 | -45.10893 | 2025-05-07 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c85c4b96-9ea6-39d8-b647-dfdf274afe0a | -6.94311 | -42.79185 | 2025-05-07 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 95230af5-2778-3152-9102-e86471004bf3 | -6.9367 | -42.79729 | 2025-05-07 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c389ed52-f95f-32c8-ad7e-11afc53be63f | -10.69617 | -37.04831 | 2025-05-07 03:36:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 28ca5a87-ee2b-322b-80d1-1153341d16b9 | -10.72264 | -42.32381 | 2025-05-07 03:36:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 281dcaef-a02b-368e-a193-4f5c0c975f3d | -7.16101 | -35.23451 | 2025-05-07 03:36:00 | NOAA-21 | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3c3d3df4-fdd9-3816-9a66-f460d3019f2f | -7.21258 | -35.78558 | 2025-05-07 03:36:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bc1e378b-1a5a-3586-be55-2cb5dbe09b70 | -6.93784 | -42.79081 | 2025-05-07 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 25d922e2-e449-3e1f-99ce-da24e048b981 | -7.47559 | -34.84448 | 2025-05-07 03:36:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e4fc132e-51dd-3ac7-b3e6-dd387b119f37 | -5.84388 | -42.58834 | 2025-05-07 03:36:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5b353ecc-9ae8-34a6-88ce-40ac9796fc68 | -6.49503 | -44.73113 | 2025-05-07 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42657267-7d16-3d27-8128-8c030b6e2871 | -10.98511 | -44.44141 | 2025-05-07 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8081ebcd-a5e5-3864-8b3a-7f3f909c8f77 | -9.61471 | -37.04195 | 2025-05-07 03:36:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 61ccb4a4-a9a8-36b3-9dec-7b7fffd4a7bf | -6.55833 | -44.48863 | 2025-05-07 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8d30ef4-e24c-3434-8281-e56114b8dd46 | -5.56658 | -43.48324 | 2025-05-07 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dad17939-e85a-3ed1-8357-a9f016e612c6 | -6.69618 | -42.13441 | 2025-05-07 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 96d0b49b-69a3-3ac6-a5be-5331d574bc17 | -8.08155 | -43.13016 | 2025-05-07 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 397942a3-9329-3113-8805-d50d88cd1d28 | -8.07356 | -43.12143 | 2025-05-07 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 93cef6ee-0acf-313a-8fc7-ea0ea44b406a | -5.79379 | -43.61589 | 2025-05-07 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9419dff-3b23-3bbc-a651-8bf492554a86 | -5.56089 | -43.4824 | 2025-05-07 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58a24998-ff8b-3ab4-9d21-7d2b7bac04b8 | -10.71679 | -42.32481 | 2025-05-07 03:36:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1ff46de1-f546-36de-8b73-d3455fc6fcb6 | -5.56591 | -43.48705 | 2025-05-07 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83a2696c-2acf-3786-94a0-fbdcc5646b55 | -7.23408 | -35.58694 | 2025-05-07 03:36:00 | NOAA-21 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e97cc16-10ed-3d85-a5cf-035d0e7d9cf0 | -5.15892 | -45.10773 | 2025-05-07 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ca322ead-4ba4-315d-b3c6-ceb6d31989d6 | -6.55396 | -44.49395 | 2025-05-07 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9f8160b5-5cf8-3ca3-a396-42a5fc4bba2a | -6.70125 | -42.13533 | 2025-05-07 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| cdbb724f-1452-3bbe-a3a9-11470d948178 | -10.67606 | -44.38901 | 2025-05-07 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5a0edce-66f6-3a82-907e-c768af4d9c07 | -6.94254 | -42.79511 | 2025-05-07 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c52914c6-b361-3970-8b96-fc7e5d5d78d5 | -9.61118 | -37.04135 | 2025-05-07 03:36:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2942a4c0-aa07-3fb8-b332-b4ba751ac82f | -10.67612 | -44.38929 | 2025-05-07 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ccb1743-976f-3eb8-8a1c-306b542d9a9a | -9.06294 | -38.456 | 2025-05-07 03:36:00 | NOAA-21 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 57d2781d-5602-3e2e-a693-993fd6d12c68 | -6.75076 | -44.5278 | 2025-05-07 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 443d08ea-dfdc-3011-8b22-8c67dc7ce06b | -8.08298 | -43.13006 | 2025-05-07 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 15d9e36e-1836-3095-ae63-6cc4ccd3d2fe | -10.71688 | -42.32825 | 2025-05-07 03:36:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7c245aeb-2f6a-3438-990f-bd9cd258d12f | -6.55243 | -44.48733 | 2025-05-07 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0ff44a09-72ac-3426-8900-e930a03c96e9 | -6.55475 | -44.48951 | 2025-05-07 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e7541b3c-620c-36b4-8ee1-8323e97a1adb | -6.4999 | -44.72943 | 2025-05-07 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe5f9511-432f-3627-96fd-a05f7283cd93 | -5.79312 | -43.61967 | 2025-05-07 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a97ef8b-3574-3673-9b2b-0772749db7c1 | -5.84918 | -42.58936 | 2025-05-07 03:36:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8bf4bd6b-4e1b-340a-8a94-e9b33355d9f3 | -10.7216 | -42.32569 | 2025-05-07 03:36:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d685d68e-7ef9-3245-9ca4-4517bb50c2f5 | -10.67321 | -44.40375 | 2025-05-07 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48ef0381-1ca6-34b9-94a5-d278b2846a11 | -10.68156 | -44.39071 | 2025-05-07 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7b5b2b9-353e-320c-a780-5452826f70e7 | -8.07378 | -34.97674 | 2025-05-07 03:36:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4ddec2b0-727b-34dc-b29b-2927bdf0c81e | -6.49583 | -44.72678 | 2025-05-07 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32b42aea-5100-3c63-bfad-a77c7823781c | -10.9844 | -44.44506 | 2025-05-07 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cfcc4a47-a38d-3c01-aa73-4a2b324532d0 | -6.69565 | -42.13742 | 2025-05-07 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 6bc7c629-794f-3a83-ae87-0257a0def135 | -6.70178 | -42.13232 | 2025-05-07 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 740aa942-bcc8-3d67-bbc0-baef8bea18bd | -5.16207 | -45.10751 | 2025-05-07 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b9e6a599-3416-342f-9f06-1eb2908553ee | -8.07767 | -43.12911 | 2025-05-07 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 91596af3-1a38-3738-be38-8ef63b3c2af9 | -9.21732 | -36.87524 | 2025-05-07 03:36:00 | NOAA-21 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e010f6ce-f67d-346f-baec-3ce4ecdf7e02 | -6.93144 | -42.79619 | 2025-05-07 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8c42f770-eb57-3b1b-b43c-96a7b465901b | -6.55162 | -44.49171 | 2025-05-07 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| adc0da23-64a7-34dd-865e-6b4487917f13 | -10.98514 | -44.44149 | 2025-05-07 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86e73d23-2af5-3a24-b99e-e3bfe02d7c2c | -6.93727 | -42.79405 | 2025-05-07 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 77502195-5b29-33eb-8f49-716468b9a283 | -10.98445 | -44.44515 | 2025-05-07 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c054e002-a2ee-357c-a288-9859a3fc0d22 | -10.6815 | -44.3904 | 2025-05-07 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea4af0a7-a790-3f63-8cd0-3b839b002c7f | -17.35163 | -43.857 | 2025-05-07 03:38:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
