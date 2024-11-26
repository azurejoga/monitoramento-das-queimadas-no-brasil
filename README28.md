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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82e58a34-9f3f-3fb6-95e9-0167cd339989 | -2.22165 | -53.66859 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0298e93d-7a56-3994-abca-32b8407f8f6f | -2.58183 | -51.92318 | 2024-11-26 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5be2076e-49ae-352d-bf0f-74e9196b4000 | -4.65466 | -47.95079 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ac70be7-9fbb-33e7-aeb2-ce2d639c09f5 | -4.04302 | -48.31327 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13cbe228-b3a4-392f-a838-0ca4bd6436a6 | -2.63278 | -51.74794 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a269e3de-152f-350c-be2e-8d771bf9024d | -3.55079 | -50.20795 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76571648-b152-3e17-b8fb-3bf06fa6686f | -3.98265 | -49.93458 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a013607c-9eb6-3d49-8510-efd4d44d8823 | -3.18495 | -48.43475 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 15db833b-3207-3e30-8cdf-846e899ed70a | -5.79836 | -47.07724 | 2024-11-26 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f57802bd-88dc-344a-9d97-3b13dff80a42 | -3.89038 | -50.07349 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a5b0eb5-924d-334c-bf18-ccd55809bcef | -2.79649 | -53.01295 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ed03e53-4342-3fb6-b609-07fc1d4284f0 | -3.22817 | -53.9218 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76dee87f-911d-3dea-8677-1c05c6bf8c88 | -3.27962 | -48.76046 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed477f74-c9a0-3a05-bed5-6d90f558b64d | -3.18218 | -48.43078 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| a0271153-7bc8-39c3-a5fa-7c53fd3239d5 | -4.1311 | -48.50849 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb595703-18d2-34a6-a1bb-20a0174fedec | -2.40233 | -53.67879 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71fadded-8da5-3f84-8365-600be8e2b5f1 | -3.38047 | -44.17371 | 2024-11-26 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efb6a99c-fa3c-3e36-8841-0aaba1043686 | -2.85887 | -48.1006 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4042f621-ae2f-3adc-b2fb-8c33c691bd32 | -2.30064 | -47.2805 | 2024-11-26 04:38:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81e26981-a2a5-3f17-8051-ac3af8d5ff45 | -4.36853 | -48.57013 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 166ba8df-0553-398d-a654-44275ab5a62b | -3.4542 | -50.00534 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02dbc217-53c9-32f9-9836-31b2cc4df883 | -4.65911 | -47.94425 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48aa4d12-4752-3873-9b35-d7e0d6cb12bf | -5.95183 | -44.4625 | 2024-11-26 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20295cc8-f91a-329a-b90e-f462afbdb94f | -3.11325 | -45.07938 | 2024-11-26 04:38:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e0c52438-5472-3b9f-9f06-77f07206b81e | -1.73849 | -52.79828 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 910f72d7-9fc4-3dac-910a-a672c324fea7 | -4.32487 | -48.58813 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92c9fd16-dde1-39d9-aea5-d9da53855795 | -3.97554 | -48.05355 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9cf02364-77bf-3123-8747-cbf0a542a2f7 | -4.54074 | -43.29574 | 2024-11-26 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 19ea9c96-37c5-34ea-a3d7-b1ba545f3e2e | -3.3268 | -53.71933 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52c69c21-f514-373a-ae64-a5c728cfab63 | -6.24404 | -44.14001 | 2024-11-26 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2b85345-561d-3f7f-bcca-c63de0d5cd4d | -2.27324 | -51.91881 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f145b0b-f8b0-3ee7-83d0-d41e6edf1812 | -2.50179 | -48.34518 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ed03068-8891-3fc7-bc7d-543d8578d00c | -3.51354 | -53.82187 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60989609-4f89-3ccc-bc85-1b752e650b4f | -3.07342 | -49.50347 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e021f982-9194-38f4-85db-8b0121403cbf | -3.27775 | -50.01429 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1db5129b-4907-3f60-9806-3af707f8d6d3 | -4.31359 | -47.51636 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 788f5e4c-5f09-3852-bda3-6d8d9f8854af | -4.24949 | -48.59404 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 28cbef21-8e9b-3862-840c-597b4a6fefa0 | -2.5763 | -45.47121 | 2024-11-26 04:38:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e63d52f6-bfb7-362b-ad95-2b35298acefd | -3.68492 | -50.22146 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d67d03c-97b3-3cdd-b634-a4786ce21ed0 | -1.69222 | -52.60903 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1ff86c0-4a6c-3246-b93e-a35c08df39c8 | -3.11435 | -45.08143 | 2024-11-26 04:38:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 32cc88c7-aa5d-32a2-a206-f3d4ca7c55c8 | -3.34494 | -50.51299 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35754902-896f-36e8-849f-9a4238e7aa7b | -3.32738 | -53.71572 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3f87060-f0e5-326f-a81e-3709240eb299 | -3.97172 | -48.078 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ea544bb3-9d3a-3bf3-aea4-31f84bee3440 | -3.29864 | -47.01805 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cef1eab9-ded8-3c0e-9724-f1e1cd30691c | -3.97281 | -48.07102 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| ba477881-fa42-33f5-b3a6-ae678d5a56f6 | -5.81706 | -51.30109 | 2024-11-26 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83e12bf7-d5e1-3034-9ce5-7f31fbeec758 | -6.08259 | -48.0355 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4b263268-eb3e-3b23-ab33-c22af2248adf | -3.9656 | -48.07345 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 308872c7-8fed-32c8-be20-d15e7cf1076c | -3.81144 | -51.37674 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48cc538a-00fa-3b1a-a941-2f69cff6757f | -3.97342 | -48.08897 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8f21f2b8-945c-3693-9377-3cfc28daed14 | -4.32486 | -47.53281 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 307ef854-6519-3ad3-afd3-d1f81ad80862 | -2.68987 | -46.87044 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26720aaa-8fdf-36d5-9fd5-7f6bfd6a18a2 | -2.40583 | -53.68308 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a74c4fd-c728-38e9-af91-438d47d51b74 | -4.29775 | -48.24295 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| af3fe8cc-c851-36b0-a490-ddb02e3fd05b | -2.45434 | -48.15422 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecec44e5-2fbc-3c09-a64e-683c9e059d26 | -4.37662 | -48.49693 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5b5ccc5c-1b63-346d-85f6-e7f8ebcd451b | -4.72345 | -43.25275 | 2024-11-26 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 861ebd68-70c1-3dc1-a3a0-b1d42d30ee20 | -3.93643 | -48.15099 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaf214db-b48a-3587-bde3-4eb9b01983b8 | -3.26781 | -50.23096 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0c879b2-0513-3709-9a39-a93fd04c6547 | -1.92579 | -50.59682 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4978766e-2f17-3db2-92b5-b0e5a2e365ee | -2.35607 | -48.56262 | 2024-11-26 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a1468b0-e068-393f-8b36-f3be948c0ad9 | -3.38366 | -50.09375 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8ea7a80d-d4c4-327f-8219-c876d3b29d37 | -5.06873 | -50.59298 | 2024-11-26 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13586d06-f793-3491-a534-529638bbd112 | -3.38196 | -50.10452 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fb2e6b7-a14a-3709-b2a7-0298f5f415b1 | -2.81056 | -53.02533 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 071304fe-1b77-31fa-a4a0-465c76793499 | -2.72028 | -46.26606 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 037bc08b-7e48-3ded-b5ba-7229f71a23f8 | -5.75364 | -46.26041 | 2024-11-26 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a8cf3815-1ef7-3c92-bbfb-e97e32baa3b8 | -3.98446 | -48.06205 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 83a53a18-9d00-382b-b71a-4f729c6802b9 | -1.89562 | -54.31985 | 2024-11-26 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0c0b2277-6aac-39d8-915f-0f2a88f13461 | -2.38744 | -48.51456 | 2024-11-26 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52e239f4-a167-3296-b1bf-875e155b7ea3 | -3.15563 | -50.62852 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc616e1f-c3bc-330a-8c71-7c4250e5134c | -5.81491 | -51.30133 | 2024-11-26 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| beee8fe6-ae19-36b3-98fa-3439dc1291a3 | -2.61047 | -48.36569 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3752c101-dfde-3c97-b35a-7a1bb841ac8a | -2.56216 | -48.19913 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f16223d-b5f2-3d15-ab1a-42dc58045bc5 | -2.31654 | -48.55643 | 2024-11-26 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d7f9d81-7119-3e10-ac69-27b73fdd2158 | -3.29266 | -50.2722 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34c5082f-c966-39ad-beb0-2072969f4d55 | -4.2423 | -48.59646 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d5490fe-817f-314f-b10f-312a346f80de | -3.24661 | -53.2945 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1a8576a-3715-325d-9a2d-c4aa2dbb26f1 | -5.95582 | -44.46309 | 2024-11-26 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc4a43dd-a97c-3b44-9e89-c58ac66271c5 | -3.37914 | -50.1004 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72c504f4-5f0a-3660-9847-41b5c1dc6ab5 | -3.23051 | -53.92271 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74cccf27-f987-3bac-9abf-a136e8985a03 | -4.37275 | -48.49987 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fc76acb-2906-330c-8275-37abe3f8e3e9 | -3.99452 | -48.08508 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96218175-b70f-3044-bcc3-b6302d6a6081 | -1.39685 | -55.20417 | 2024-11-26 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e37cde77-349f-314a-bd11-30c8426619a2 | -2.77616 | -48.58257 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faf43e1d-d82e-396f-9880-1a2f9e39c5fc | -4.32429 | -47.53641 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 395e61fa-9b42-3754-9025-8fbf03ad4a23 | -3.2311 | -53.93001 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9665a89c-af84-3f28-a885-cf1357c2e5dc | -2.71558 | -48.66495 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67ff2fa2-9b52-339f-9ef3-6aa15295fb5c | -2.25869 | -47.28482 | 2024-11-26 04:38:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65807be1-c78c-3e39-82c6-25b82b717fcf | -3.25783 | -53.27551 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41708dda-b69d-38ce-b973-eb54b39cb905 | -3.07846 | -49.19674 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dff812e9-861f-3e91-875d-6b389daa1dc8 | -3.1758 | -45.26074 | 2024-11-26 04:38:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e98b79c9-5d71-383d-b062-d2e7f9b098df | -3.11694 | -45.07995 | 2024-11-26 04:38:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fa68c6e5-69d2-311a-b2ca-edd4e7a37978 | -8.29927 | -49.08804 | 2024-11-26 04:38:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7b28e2b-feab-3b19-bbab-5f26f7dec3eb | -4.28161 | -48.60613 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7b98d79-05ad-3a4e-80b6-828f6dfe1ec2 | -3.58915 | -47.34697 | 2024-11-26 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9d7b5fd-f6d8-3607-85f0-f548e4bdef1e | -6.07867 | -48.03855 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5c3d713c-5b78-3493-a42c-3a5867725cc6 | -4.48643 | -48.11483 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61b9505d-29da-3d84-ac1c-d6b47eea4097 | -2.54309 | -46.40297 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README29.md)
