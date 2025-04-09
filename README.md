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
| 0b5ef0ca-6ed6-374b-9d47-d23cf60c53bb | -17.45154 | -48.17043 | 2025-04-09 00:43:00 | TERRA_M-M | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f4691632-56d6-36ac-94c3-ef607a4b5e41 | -20.83295 | -47.75838 | 2025-04-09 00:43:00 | TERRA_M-M | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6059e02c-7968-30a8-8758-45efbc5b0679 | -20.83428 | -47.76862 | 2025-04-09 00:43:00 | TERRA_M-M | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 58b5f4bf-76ed-36bd-b938-f1a97eb141dc | -12.09562 | -45.62551 | 2025-04-09 00:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 193fb48c-b718-39f5-9a03-4b2a63932b5e | -14.67538 | -45.81809 | 2025-04-09 00:45:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b5cf1b39-398f-35c0-8487-2316a5488243 | -12.09409 | -45.61506 | 2025-04-09 00:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 19e47147-7d11-3d18-8ac7-7840d43a4253 | -12.10356 | -45.61354 | 2025-04-09 00:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 18a7b577-209c-36c2-928e-c14957599c13 | -14.66481 | -45.80976 | 2025-04-09 00:45:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3977d3e7-0b1d-3177-82cc-31cfb6d6e705 | -12.10508 | -45.62399 | 2025-04-09 00:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a17502d2-5739-3450-9dcf-b98cb1dd233c | -12.12948 | -45.62479 | 2025-04-09 00:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a5f0796f-25f2-3e36-a2a9-6da9dfb2968c | -14.67396 | -45.80837 | 2025-04-09 00:45:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 88d200b2-32a2-3ebf-865b-19ef36a62279 | -14.66623 | -45.81947 | 2025-04-09 00:45:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 67a039c1-14a2-3b30-b489-768a0cb4c527 | -13.68005 | -47.76171 | 2025-04-09 00:45:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 746bf237-efb5-3543-8e36-e446c3169171 | -6.01382 | -43.86307 | 2025-04-09 00:48:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5dbd6dfa-f7ba-3296-aa8a-97aaf27d919f | -7.0788 | -44.37536 | 2025-04-09 00:48:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e3e7ee98-2c87-333c-9d59-80fb263e1dcd | -10.5418 | -44.672 | 2025-04-09 00:48:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| bd4d0bc9-f84e-3b9e-a840-6f4544877b0f | -10.71627 | -42.3164 | 2025-04-09 00:48:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 477f9cc6-2452-3e3f-bee9-7295bbcba823 | -7.06768 | -44.37718 | 2025-04-09 00:48:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 46982998-c477-3642-99e8-71d6ace09f59 | -10.73143 | -42.33251 | 2025-04-09 00:48:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 5e5a00e8-daf7-3491-b86d-d8f38ccbf589 | -8.86358 | -49.88661 | 2025-04-09 00:48:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a0a83065-554b-3797-8c10-c73d691bfc1f | -10.72854 | -42.31433 | 2025-04-09 00:48:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 1c1a006c-e78e-3cdc-aed7-a28dcb841f0a | -8.10901 | -43.12904 | 2025-04-09 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 58a294bd-1625-3d83-8707-a75c2f374eb7 | -6.01136 | -43.84655 | 2025-04-09 00:48:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 7d3b9d4a-227e-3ada-8922-f82fcf83073d | -9.34243 | -36.8351 | 2025-04-09 03:08:00 | NOAA-20 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5b3ae0bf-0188-312c-a299-f792562a5898 | -9.34769 | -36.83607 | 2025-04-09 03:08:00 | NOAA-20 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0c2cdc7b-58fc-35ed-8269-8eee658bdb92 | -8.84547 | -38.78725 | 2025-04-09 03:08:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3b6d67a5-da77-3a5c-b913-4f3ee83cbc5b | -9.34183 | -36.83833 | 2025-04-09 03:08:00 | NOAA-20 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b1d04c1e-59f5-36fe-8a88-7b69ed33d53a | -8.84463 | -38.79176 | 2025-04-09 03:08:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 71eeac05-0c53-3c18-b5f6-ce24df9b2220 | -8.84667 | -38.7895 | 2025-04-09 03:08:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 64291cc1-d4fd-3013-aa17-46930fc2ff78 | -6.44801 | -37.51519 | 2025-04-09 03:08:00 | NOAA-20 | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a8efc019-d46a-3164-aa80-2febb05e0cc5 | -10.7187 | -42.32027 | 2025-04-09 03:10:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 41f5420a-b023-3982-8476-1310c75a9eb8 | -10.72406 | -42.3186 | 2025-04-09 03:10:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1dd03de4-a08c-31fe-a7fb-a9540350ce12 | -12.52157 | -38.63573 | 2025-04-09 03:10:00 | NOAA-20 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 10f80bec-0b50-34eb-8fb7-e9f2fee9a0ab | -10.71694 | -42.31701 | 2025-04-09 03:10:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 562d3f95-46ea-3e3e-9083-0b1741cde8bb | -12.52083 | -38.63952 | 2025-04-09 03:10:00 | NOAA-20 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 213cb812-7d63-3f13-8ad6-d288c91f2b3a | -10.72583 | -42.32186 | 2025-04-09 03:10:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| eeea1806-43b3-3439-a358-2beaba597ad0 | -4.60486 | -43.31963 | 2025-04-09 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cebbc671-a2d3-3396-94b3-024a53424712 | -6.01824 | -43.84821 | 2025-04-09 04:00:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 062afb43-cef7-388b-8f09-7e89b5fbb2a1 | -6.0137 | -43.85224 | 2025-04-09 04:00:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cc0d0c96-0733-3df4-9fd1-363a8ea9996f | -6.45212 | -37.5154 | 2025-04-09 04:00:00 | NOAA-21 | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0343c185-4da3-3e93-a47d-1d29f1503b82 | -4.8486 | -37.55032 | 2025-04-09 04:00:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| de411665-ff3c-3380-b997-1122b67ff3b0 | -6.59221 | -44.78549 | 2025-04-09 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36f211de-b000-3716-807a-f3a11544a481 | -6.01446 | -43.8476 | 2025-04-09 04:00:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 49cff39d-2191-3923-96c7-582fc2f24333 | -6.01749 | -43.85284 | 2025-04-09 04:00:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5df5352f-0574-303a-b240-983e0cb0c59e | -5.96184 | -42.31764 | 2025-04-09 04:00:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c2c8c15d-2967-30a9-9efa-505844394f13 | -4.79793 | -43.78051 | 2025-04-09 04:00:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc836603-da1b-3743-8a6d-b29547a1dc70 | -6.59147 | -44.78987 | 2025-04-09 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2af55971-9857-3b53-92fe-cea89c8968cc | -7.06942 | -44.38153 | 2025-04-09 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5b1209e-ed11-3955-a3b4-4b2487160a42 | -12.15067 | -40.2953 | 2025-04-09 04:02:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d992fda7-fcc3-31af-872a-2b85b5cfe7e8 | -12.52604 | -38.63692 | 2025-04-09 04:02:00 | NOAA-21 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7c2d091f-ba30-3542-916c-3dfe477650cd | -7.07556 | -44.368 | 2025-04-09 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a557a8d-0973-3c32-a979-61a09cb32610 | -10.63146 | -46.4142 | 2025-04-09 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7e13c2f-87a5-3d8d-a0aa-9e77284a8e24 | -12.84719 | -39.30325 | 2025-04-09 04:02:00 | NOAA-21 | CONCEIÇÃO DO ALMEIDA | BAHIA | Brasil | 2908309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 189dfa08-174c-3dd3-b268-c34d3daa394f | -11.89829 | -38.13225 | 2025-04-09 04:02:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 604f9ad7-ec2d-3893-851f-170ad917fbcf | -13.86047 | -47.38913 | 2025-04-09 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e40be6b-4682-3cd1-a627-6e5ac1bfb903 | -10.72056 | -42.31772 | 2025-04-09 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d7aeca47-c4fd-33d7-8ef6-a0cb01e9ca82 | -9.91565 | -37.08693 | 2025-04-09 04:02:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3d43075c-dfcd-3f69-a1f1-ddcd74aea686 | -7.64951 | -39.75169 | 2025-04-09 04:02:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 72390c42-72a2-33fa-bb04-f9373321dfe3 | -11.87823 | -43.9381 | 2025-04-09 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 091b47c1-73e5-3272-ac2b-329fdb448acf | -13.93306 | -43.28458 | 2025-04-09 04:02:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 985610f8-368d-3c94-95f3-418c78e0da3d | -13.28759 | -43.19173 | 2025-04-09 04:02:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a322093a-6aca-3eef-92c2-dbbbbd32a272 | -13.48111 | -44.04074 | 2025-04-09 04:02:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9be94a5e-823d-3439-818a-e16d216559c4 | -10.72393 | -42.31827 | 2025-04-09 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 57c9490b-a991-3aeb-9ebd-f4c682faf167 | -13.86471 | -47.38954 | 2025-04-09 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31c38edc-f8f5-308a-b1fe-c2ff6b8bd9c1 | -9.02593 | -40.58581 | 2025-04-09 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dbb7c3e3-a217-3d86-aeea-38a24d338a17 | -12.26255 | -38.83031 | 2025-04-09 04:02:00 | NOAA-21 | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f8af3d0-c177-3888-b8f0-f95f73a5f193 | -10.54254 | -44.6671 | 2025-04-09 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 678ee610-6f20-3c3f-89f2-043a1bd2c700 | -10.69469 | -37.05095 | 2025-04-09 04:02:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c2eeeb90-0a97-316f-843f-cb486727a567 | -7.07018 | -44.37681 | 2025-04-09 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8af78284-8591-3b4d-9791-e83f8f980208 | -7.07188 | -44.37941 | 2025-04-09 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61f4e99b-0fbf-3d6d-818d-992041d966db | -9.34429 | -36.83313 | 2025-04-09 04:02:00 | NOAA-21 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f26293c7-e187-3713-88b4-dcb366e1689e | -10.25005 | -39.97093 | 2025-04-09 04:02:00 | NOAA-21 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b4629538-238b-3ca9-86e7-6699b95b4bd0 | -9.34607 | -36.83548 | 2025-04-09 04:02:00 | NOAA-21 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 66b2b4a1-4916-3e01-9e90-20ae3889881a | -12.14734 | -40.29478 | 2025-04-09 04:02:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 032267fd-aa6b-336f-8e05-19df6fc82153 | -8.84678 | -38.7875 | 2025-04-09 04:02:00 | NOAA-21 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bca7d04a-6d8e-340f-a5a6-b50d4625cbdf | -7.07268 | -44.37472 | 2025-04-09 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9d3f55e-36fd-33da-a84e-5c3d0e409fee | -10.54178 | -44.6716 | 2025-04-09 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f91ccc5-3bdc-3a5d-929b-089868908592 | -10.73066 | -42.31937 | 2025-04-09 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f21023aa-fef8-3763-b949-4f1f0401150f | -9.32493 | -40.58749 | 2025-04-09 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1daa2716-d6d8-338c-9bd7-76cf6c8ab753 | -7.07479 | -44.37274 | 2025-04-09 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d14fd4e-1b30-33ba-b366-8638121cb51d | -10.92196 | -37.49089 | 2025-04-09 04:02:00 | NOAA-21 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 90d07eae-b6de-3a3f-85e6-a96d3342c56c | -7.07573 | -44.38006 | 2025-04-09 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f955031c-db83-3ca2-9eeb-0e1ad694d900 | -7.07094 | -44.37212 | 2025-04-09 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2db4dc60-ec91-30bf-8208-4eca666cc022 | -6.71916 | -47.60942 | 2025-04-09 04:02:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ebcd192-c98d-38bf-8756-875c655fb3ab | -7.56822 | -45.84592 | 2025-04-09 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b856148-947a-3ad5-8553-2944a370ead9 | -9.02924 | -40.58633 | 2025-04-09 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 33eb811b-bfe6-3bea-b7c8-5ff0b4c08c20 | -8.11394 | -43.12268 | 2025-04-09 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| eedbedd5-7214-336f-acb1-f737aa0af1c7 | -13.01729 | -45.07133 | 2025-04-09 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2bceae96-b24b-324e-8e62-65e9092f5e2f | -9.34362 | -36.83762 | 2025-04-09 04:02:00 | NOAA-21 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0192ee38-8719-3d8a-9298-993b6747eb20 | -7.07403 | -44.37745 | 2025-04-09 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1d11a05-aaa2-34b7-bfe8-29b50747013b | -10.92486 | -44.16192 | 2025-04-09 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3217a3d0-8ffd-3808-a8ec-e37d311f83bc | -10.72729 | -42.31882 | 2025-04-09 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e0fcc47c-8a1c-3377-bf61-892a17258716 | -7.07326 | -44.38218 | 2025-04-09 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8a8d91b-a261-3287-96e5-0671657a5903 | -13.33872 | -43.37348 | 2025-04-09 04:02:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4515c2b1-6bb2-3ff3-8a27-114f64f89f27 | -8.28775 | -41.65657 | 2025-04-09 04:02:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fd63accc-38c0-3910-ad31-b36ba363be53 | -7.07347 | -44.37001 | 2025-04-09 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 147b6c13-2f1f-3e0e-84cb-8d775c190d81 | -8.63715 | -40.28841 | 2025-04-09 04:02:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 00a21f36-754b-3d8a-a352-d3da55e37ec2 | -9.70198 | -37.21877 | 2025-04-09 04:02:00 | NOAA-21 | JACARÉ DOS HOMENS | ALAGOAS | Brasil | 2703403 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 45135d32-1d36-33af-a9f7-729c14349230 | -7.07732 | -44.37063 | 2025-04-09 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62c99a26-a3bc-3f45-a457-68e3de901408 | -13.02098 | -45.07198 | 2025-04-09 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README2.md)
