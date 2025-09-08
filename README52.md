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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ebe8bb7-fc18-39d0-a0db-cc3b998bf7f8 | -9.84595 | -48.85221 | 2025-09-08 04:51:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2fb91e40-4450-3797-9233-55da037fde82 | -6.27873 | -53.43022 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31a057bf-0b53-3125-be0b-06a05fc29a07 | -9.99992 | -51.63721 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a0971e1-2a97-3f51-aed6-926a72dcbdbc | -7.11277 | -44.82031 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f22cc15b-96ab-3036-aa24-017d65b71a8d | -3.92791 | -56.06464 | 2025-09-08 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78ac7e24-2407-38aa-b188-e5ffd4254ea9 | -9.14492 | -46.06048 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 537cb7eb-95e8-335b-ae66-7458db5883cf | -5.88319 | -43.96964 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a4cb8566-0975-3117-bc05-4b7306b0ab65 | -9.55683 | -50.62402 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16a223a5-71bf-3e17-999c-ff10f0efcaa5 | -6.26113 | -43.68881 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cefe3cc-8e14-3e0a-a7d2-d4205def6a2a | -5.10651 | -56.14859 | 2025-09-08 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78f3614b-aac0-3435-a80f-dc1a90f09f90 | -8.19966 | -50.13943 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 680ea930-cb17-3ee1-9c04-cb8ede9114ed | -6.27928 | -53.42674 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 551de28e-0a41-3646-848a-9e88ce6c3d83 | -5.87249 | -43.97075 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 963ecab5-4e90-310b-827a-bf109b01d002 | -6.63912 | -53.36649 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f87533c0-8593-38ca-96e8-9d7a199a25d1 | -5.88241 | -43.95158 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 55c12d67-0d34-3322-a561-d6cca9a07dca | -9.24172 | -57.06355 | 2025-09-08 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f65177f-ab4f-3135-bc75-dafc362ce9f9 | -10.21598 | -50.52252 | 2025-09-08 04:51:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 828e8a94-0042-37ad-951e-02ca29d7254b | -6.73988 | -51.95986 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4d5ddfdc-94d7-3ac4-9200-49caec8ac49a | -5.85177 | -43.8563 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dfe4e2a-c60f-3a0f-be9a-5ff0d25cd361 | -9.08229 | -46.97945 | 2025-09-08 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e3320228-21de-3ed2-a64e-ecbdfca6d47b | -7.77882 | -51.0927 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 106c8f7f-6447-382d-a0b6-2721c4e1b2b2 | -9.97611 | -51.67963 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 532ee142-d233-3f87-8da5-452d53a6d7c6 | -6.34988 | -55.56031 | 2025-09-08 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 77438a54-db8b-3efc-9d65-786066003786 | -7.86619 | -50.97925 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbef59bf-8ba9-3e6e-9c60-b145573f5f65 | -11.56941 | -44.65572 | 2025-09-08 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee76c915-8247-35eb-950d-27ae597dcc78 | -4.89899 | -42.22224 | 2025-09-08 04:51:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ce9c5f37-76f8-3f8f-bfa4-19fe77c8036f | -6.81179 | -52.83054 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 133279ea-9cc2-3769-a5ef-daa991f336db | -7.04087 | -43.25433 | 2025-09-08 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3b2d4826-3917-3469-9765-dc329d841c1e | -7.82599 | -45.4183 | 2025-09-08 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed3228f0-12b9-385c-b083-ee5f949dadc1 | -5.97344 | -53.5962 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3edc51eb-cf3b-3f0a-b091-894347452346 | -10.46126 | -53.61945 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f419fc54-8ed9-3756-8f92-d508dc42c02d | -8.87969 | -51.04253 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37325238-96ce-372e-96c3-f9504845bcfe | -11.42746 | -43.64493 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c25e2b05-d7ec-351b-9d59-b555dba4fd1c | -7.83501 | -52.15509 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fd255e4-c636-3066-9928-011518bc59d2 | -10.00334 | -51.63774 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d565e4c8-a75c-38e7-af1c-2b4797b413a0 | -5.81113 | -45.64834 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bfbb73e5-19eb-3c08-9ba9-ccb522b37f9b | -7.81908 | -45.43326 | 2025-09-08 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce845e43-95e3-3d4a-b81d-453201c27209 | -11.3318 | -46.55424 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22335096-bffb-3a38-8719-acb2dac561ac | -6.06821 | -43.11874 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 99d3cdb9-c41c-30f3-82fb-e37fb1b32b0a | -10.45904 | -53.61195 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13b4af90-2f32-30b4-94d3-7d4a6be1a79c | -9.07727 | -46.98328 | 2025-09-08 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfcfdd7e-ad1a-38f8-b691-1abb6e9097b5 | -6.6253 | -53.34655 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97ba4093-c63f-3b13-8157-73b6f175f85d | -5.87982 | -43.9565 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf859c1e-2933-3149-94cb-df4cd592797e | -6.46623 | -43.95127 | 2025-09-08 04:51:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| adac2967-fa12-36e9-8630-6a2979f208b3 | -6.40647 | -44.45533 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e7f37d2-6030-33f2-beae-7ec7fc1e4e76 | -9.48724 | -55.97526 | 2025-09-08 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0acec4c-7871-3381-9ff1-1cc14e21b6e4 | -9.9903 | -51.67818 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5581bc4e-c052-34ec-8440-a7fd6078ce09 | -9.69623 | -57.80564 | 2025-09-08 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fca3c47-c756-3b9f-ba46-5c8e6d5cd43c | -11.24822 | -47.56344 | 2025-09-08 04:51:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 872b4804-2f38-3d51-8ec9-8f1cf3143cbe | -10.00104 | -51.62977 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfa2132a-d4d3-3a92-bfad-d3aca811422c | -3.54257 | -49.37753 | 2025-09-08 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70fd89f7-737f-30a2-b0c2-b5ff6158e635 | -10.46568 | -53.63445 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c174d9a8-f01c-348c-998b-81636fe24a30 | -11.30638 | -46.53024 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ffa0c2a3-503f-3509-a0df-f8b9a00095bd | -8.70034 | -45.32098 | 2025-09-08 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dc29b498-fe89-3e2c-8fd8-ada8eebc153a | -8.07703 | -45.47796 | 2025-09-08 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6705ecf4-b8bb-3e32-bb20-129e79fac8f8 | -7.39696 | -61.634 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 273a099b-b804-390a-b16c-76a5568d9af3 | -9.72314 | -43.98312 | 2025-09-08 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e7e58c77-89a1-373a-b4f0-53091eec10bf | -8.87306 | -47.90622 | 2025-09-08 04:51:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d651731-69a1-3b28-8b68-26d9a5eb2a90 | -5.41779 | -42.85405 | 2025-09-08 04:51:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7b1b6dba-4665-3f64-9c4a-1cbe98642ed9 | -5.59566 | -51.33138 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 37fe1b8e-1642-34d6-b63b-4551802a05ed | -5.88276 | -43.9726 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8ac1a83b-ac9a-3dc0-b0d0-bde03374b4fe | -8.18479 | -50.14101 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7821d620-a99d-33a0-81bf-fa0a39e7d8d1 | -9.56303 | -53.59983 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c401faa1-97d6-30e6-87e4-4ca57d518c37 | -5.45085 | -43.42603 | 2025-09-08 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89050c96-8e88-3345-8be0-d7aa1115c7ba | -5.8667 | -44.18003 | 2025-09-08 04:51:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2e67918-525e-3c4f-abb8-39b4c0181c99 | -7.12347 | -63.07139 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9ccd16c-cde8-3dcf-bd45-7d010ebb4ee3 | -11.39164 | -43.54424 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bfe757e-32c3-3cfd-abbe-f93ae6dd2459 | -8.50044 | -51.32971 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff06d02f-a7e2-3fdc-9835-11c7c19dfa7d | -5.63948 | -43.91373 | 2025-09-08 04:51:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a40da012-dc84-3e44-a299-4ffac9c5576d | -6.19981 | -53.26113 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8af83aa-106a-3f15-a58c-48c8454e96cb | -9.55697 | -53.59531 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c293bcdf-2f34-381d-a585-2039293f0e89 | -6.96835 | -62.92797 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6ffdd6c-df34-3fc7-97eb-e2643b05fb76 | -6.20651 | -42.64328 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5b7b8a55-e852-324f-8a1d-85f634f237b9 | -5.9946 | -47.60876 | 2025-09-08 04:51:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a812c5a7-1a36-3333-97fc-456806d3a2f5 | -10.46344 | -53.6055 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea0de8a9-f1af-32aa-98d3-cdde3bb03209 | -6.83315 | -52.80206 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b409937c-5735-355f-9e32-1a651bbd4923 | -7.24959 | -44.83517 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0a6b1bd9-9a7a-381a-8d52-4252e129fa2d | -4.30678 | -48.09161 | 2025-09-08 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fce2daba-ee0f-3ba2-b06e-605554f8c9ab | -6.48634 | -41.77039 | 2025-09-08 04:51:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1c5b6912-c341-3076-97be-81e2de75c3f1 | -10.29241 | -48.80972 | 2025-09-08 04:51:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| aea1a081-5784-36e2-986b-94c302c0ee35 | -11.14167 | -45.2542 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d220ce6e-8dfb-33ce-a7fe-f9b874220bed | -9.84846 | -53.29632 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e497b6d-cff2-31cb-8f30-eafdf13c6752 | -6.82139 | -51.8717 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f2ba053-b3f0-386a-906f-be9bda80a031 | -7.39641 | -61.63709 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| db3b41a5-f533-36ed-a72d-71c11fc814aa | -5.8846 | -43.97407 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cba3fa73-560c-324e-8d32-d684920e09c3 | -4.64755 | -46.31196 | 2025-09-08 04:51:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a81acd54-f1c3-31ae-b0a7-8ba8defdf1ea | -6.63359 | -53.35852 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd2dc0c3-564a-324b-bfd4-4187ff0917f0 | -8.08875 | -54.7573 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4add859-3de7-384e-8cba-4027436a4a21 | -10.14216 | -46.21439 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6915dbdb-049a-3c65-95c3-350f587938f7 | -9.79404 | -48.32884 | 2025-09-08 04:51:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 951f6d36-34f3-386b-852f-2cbb0fce8013 | -7.09067 | -43.89138 | 2025-09-08 04:51:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e5d812b-c938-30b6-a929-f5367b3fc28b | -6.94946 | -62.93641 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8976aac-c85b-3ede-8323-0c76263c5773 | -5.88029 | -43.95325 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d711bdae-b69e-3195-a08b-88a8f590a7ae | -9.99206 | -51.68964 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6136564c-d13a-3a09-ba0f-5bf8dfd105dc | -11.38747 | -43.54133 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c5c9910-f201-30f9-be12-47d015728e24 | -9.92316 | -49.89091 | 2025-09-08 04:51:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 80c66ea1-7263-3f3b-99de-6d2d2a1b7f30 | -6.28291 | -44.38752 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72d93280-6b0e-3650-a08e-1034cabbd934 | -10.791 | -49.71701 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ffe117c-d275-3413-b69e-6c38d53891b8 | -9.82582 | -47.77454 | 2025-09-08 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2560700b-62e9-322d-9e6e-72942287f747 | -3.33098 | -54.90611 | 2025-09-08 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README53.md)
