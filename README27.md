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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf8d22ff-277c-3888-9ef0-b83127b9e092 | -6.17877 | -41.15726 | 2025-09-14 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8b392fd9-74e6-3aff-9619-c70c0f5de847 | -5.11584 | -47.52763 | 2025-09-14 04:38:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ac26a4c-28de-3cf5-81c8-aee6af3740c3 | -5.13122 | -45.1157 | 2025-09-14 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ca1aded2-d620-3c86-b0ce-58226ee83f25 | -3.85341 | -52.16322 | 2025-09-14 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13989e8e-1855-3126-ac22-031177fa3ac9 | -6.42843 | -42.62793 | 2025-09-14 04:38:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1520bece-d8f1-3d8d-8902-bbb545c0d989 | -1.9786 | -47.97853 | 2025-09-14 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa5cabe0-169e-30d3-9484-64c211100dd3 | -5.95928 | -42.79061 | 2025-09-14 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 629c89d9-a09f-3306-b818-4a67da633ad0 | -6.26065 | -43.4755 | 2025-09-14 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 98e06738-30d2-34f2-b2e7-af31dc58eb20 | -6.33221 | -43.87714 | 2025-09-14 04:38:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e6db299f-e9f5-39eb-ae39-5ace069b201d | -6.07384 | -44.44398 | 2025-09-14 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 041377e9-77d0-3273-a165-26887383aea7 | -6.16962 | -42.7649 | 2025-09-14 04:38:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b06eb807-2bcf-3c7b-81b5-d991781980d5 | -3.59381 | -47.52153 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 23961482-4a25-3376-bc8f-2ac432db183d | -3.40135 | -46.90387 | 2025-09-14 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edf352d7-84cb-3c99-ae8f-fefaccac4d8e | -3.22264 | -47.12943 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ad7a01a0-2885-39d6-83b7-c177e481218d | -3.59883 | -47.51132 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 50359700-cd64-3134-b22e-ce12965d7c72 | -4.80521 | -42.74021 | 2025-09-14 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b443f4de-3e33-35fc-acfa-3d688346d1da | -3.32422 | -54.90958 | 2025-09-14 04:38:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03d9a142-bfdf-3cb7-b04b-fbc5d2fc846e | -6.27321 | -42.39762 | 2025-09-14 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 89151875-3956-3297-a91f-ce3c196221b3 | -4.41313 | -47.60647 | 2025-09-14 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c38f307-d27c-374d-b26e-e1b61b29f759 | -5.79855 | -43.88725 | 2025-09-14 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 38be21b7-9233-3aec-9629-7ec39caa9980 | -5.10963 | -46.09023 | 2025-09-14 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1f179f0-afca-34d8-9da4-60769276f1fa | -6.33332 | -43.86953 | 2025-09-14 04:38:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b8b93d66-832d-3a02-b8a7-4a9472ec1bdf | -3.60629 | -51.04779 | 2025-09-14 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e7966df-2357-33cc-82d1-5c372c492fb4 | -5.79384 | -43.89032 | 2025-09-14 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 16f3ae37-e717-3b81-9708-bb33933d3954 | -3.21159 | -49.10387 | 2025-09-14 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc49bca7-c9f9-33a5-bcd7-86a1b18786e9 | -3.21643 | -47.12472 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b20ea2aa-f7b0-3a4b-9d77-f7b5befaccbf | -6.18175 | -41.17263 | 2025-09-14 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 142db6ca-d19b-3cd0-ac13-08ca66bff254 | -3.22321 | -47.12578 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0ec48d2b-ce73-33c0-8a89-9acd43e89c25 | -6.37688 | -42.82385 | 2025-09-14 04:38:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7c223d7b-07f1-319e-b0fa-6d3fff320376 | -3.2302 | -47.62933 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 738003aa-6a3a-38ae-8f5a-21f94a97d4b2 | -5.96459 | -47.02276 | 2025-09-14 04:38:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5d1d9a3-c692-3020-97d5-2767895ae577 | -6.32022 | -43.33947 | 2025-09-14 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0591cc17-9371-322c-922d-3e26a74d0efa | -6.17669 | -41.17202 | 2025-09-14 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bbc73007-2d2f-3a59-8b48-6666a30f5a31 | -2.30295 | -48.14561 | 2025-09-14 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1f91bdc-f46f-3e68-b33f-27e18b276a87 | -5.7266 | -43.18597 | 2025-09-14 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fad45d78-12ec-393d-9c03-21f1de27690d | -5.95606 | -42.78114 | 2025-09-14 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 32003e2c-237f-332c-8f80-6b8d2cf3db59 | -5.66409 | -37.21819 | 2025-09-14 04:38:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d261ea86-eb07-3fd1-989b-9bd3a2ff60e5 | -3.79858 | -47.58225 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb79f94b-068a-3ece-bc98-e0bb0568fc22 | -3.68137 | -47.11217 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbec27b2-2d99-3539-b870-6e543c0977b8 | -3.59717 | -47.52205 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| d24927a3-b31e-36fd-88fb-9731b3b215ab | -3.89784 | -40.91908 | 2025-09-14 04:38:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 533a629c-ec3a-3270-b0c2-7595a5683e81 | -2.26065 | -47.84895 | 2025-09-14 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1626c2f-9228-335f-9263-6b2a4217e558 | -5.9707 | -45.84258 | 2025-09-14 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11d045da-c2f5-35ec-8c53-53328975cdbd | -6.53238 | -39.50992 | 2025-09-14 04:38:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 917929ae-59d9-3a08-90bd-f27e3fcdeaf7 | -3.87071 | -52.38448 | 2025-09-14 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f903f3c-a600-369f-ba2a-9caa51518732 | -5.79799 | -43.891 | 2025-09-14 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2b599cdd-e603-3531-bdb6-328bf4b3062f | -7.06621 | -38.54329 | 2025-09-14 04:38:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 26ffd6fe-41a3-330b-aac4-86d87266cc97 | -5.70902 | -46.38837 | 2025-09-14 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9090f626-1469-3280-8671-d9e7a11286df | -3.13662 | -48.80066 | 2025-09-14 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8c08ea2-2561-393d-aaf3-fa5de8e71760 | -3.07514 | -48.82201 | 2025-09-14 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75724d25-d358-3d64-8e57-3b4b023fe580 | -6.1134 | -45.93602 | 2025-09-14 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2ef69ac-4177-355c-8e08-37cfd0e65642 | -3.87022 | -52.38505 | 2025-09-14 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 955b0259-a7d4-3cdc-9292-d0fd72777657 | -3.2274 | -47.62529 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccba9186-253c-3298-a363-e4fb3c3bdd2b | -2.26119 | -47.84549 | 2025-09-14 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ccbac39-26df-3ee2-b70f-f126e51508fc | -3.01106 | -47.83693 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce7dced0-7840-333d-8932-10cdb193bb52 | -6.27385 | -42.39301 | 2025-09-14 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0b22023e-f130-382d-9fc6-3851a19537e4 | -3.20829 | -49.10336 | 2025-09-14 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2dd2ef1f-4b10-3b83-a334-e0ed4c12af4b | -5.08916 | -43.01988 | 2025-09-14 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef4f9746-1d51-34d7-bf22-1027fc1e9283 | -3.7364 | -55.94366 | 2025-09-14 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7c4530f5-47b6-3705-b512-e465973c2d58 | -6.07437 | -44.44041 | 2025-09-14 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51657d80-fbbc-3af6-b81f-c5104509813e | -3.2235 | -47.62831 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10d4bed8-2109-34b4-b80b-a476980a752c | -4.41258 | -47.61006 | 2025-09-14 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97c1b9aa-d644-39ce-8999-0f105deb14eb | -3.2263 | -47.63235 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27f9e1d8-521b-3200-9492-3eea548bf38a | -3.42411 | -49.13758 | 2025-09-14 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11a050c5-b2fa-3756-89ee-9c98f14d59b6 | -5.17126 | -46.15829 | 2025-09-14 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d38d101a-8eb2-340e-af7f-3a549fe9f90f | -6.33698 | -43.87388 | 2025-09-14 04:38:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71ac6311-91ef-3a73-98c0-371e3b842a60 | -6.33388 | -43.86573 | 2025-09-14 04:38:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ea5eac7d-6c76-3553-898a-ab7335f2dae3 | -3.22999 | -47.12684 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 034bd51d-72e1-3230-a4c9-ca4959cf66ef | -3.59773 | -47.51848 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 1f532526-1aa4-38d9-8c5b-26db5275cb66 | -6.42593 | -42.61287 | 2025-09-14 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1eda257d-0597-35e7-ac4f-3a1f7cdc18c9 | -5.96896 | -43.21912 | 2025-09-14 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bae18e63-b0b8-3346-87ce-2929c36834fb | -6.11035 | -45.93116 | 2025-09-14 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac4dde22-4c42-3dbf-b04a-b91f35c68608 | -3.59828 | -47.5149 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| c3ebfc29-ecae-3016-817a-02f0c6d8d236 | -4.73614 | -46.16432 | 2025-09-14 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff34fdc4-9279-3a68-9dde-d5043749ff1b | -6.17835 | -41.16024 | 2025-09-14 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bb42fcea-2951-35da-bafb-c3276ee9df64 | -6.31963 | -43.34353 | 2025-09-14 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ee7eede-d96d-39e9-b65e-f48c598acdcb | -6.38525 | -44.36846 | 2025-09-14 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23a51b9a-72ff-3330-b822-4019d620f3b3 | -4.80557 | -42.74295 | 2025-09-14 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d82a07b2-3ce7-32fa-b436-82c3a3c01093 | -5.752 | -43.91487 | 2025-09-14 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0847b623-560b-38f4-bf59-df34eb7e6b05 | -3.76534 | -49.95314 | 2025-09-14 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c3041ce-6665-3022-9b32-a26cb1cdd86b | -6.27429 | -44.38587 | 2025-09-14 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84d21dd0-94d8-39e6-a6a2-19aec49198e7 | -6.17751 | -41.16615 | 2025-09-14 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 455343e6-844e-3732-b358-849b8a67bfe2 | -6.44057 | -44.07978 | 2025-09-14 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbd64602-1e50-3d8b-b661-a766afa53e52 | -3.59492 | -47.51438 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 02d545f0-5683-3764-968b-6cddbe0e9d3e | -4.48478 | -48.11524 | 2025-09-14 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 303e7d9e-2532-38e6-a71b-f10031dde4c5 | -6.20617 | -42.70454 | 2025-09-14 04:38:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a405f150-0829-3655-bf0e-8c5362e0fb36 | -6.07553 | -44.44073 | 2025-09-14 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfa1375a-e3c7-3e38-a3d3-e83bced407c0 | -6.42383 | -42.62734 | 2025-09-14 04:38:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ebd0194b-c635-38e8-8608-cd15b55dd08a | -3.60109 | -47.519 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2afbd6d9-8a62-385e-ae01-58fb2bb178d2 | -4.86635 | -49.33317 | 2025-09-14 04:38:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a091408d-6506-3e32-a95c-4e594ead17af | -4.13432 | -48.81676 | 2025-09-14 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b512e6bc-6063-330f-8841-f9805cf7f92f | -5.96141 | -43.2095 | 2025-09-14 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4d908d18-b1dd-3317-9212-f3ef5a2e4284 | -5.72912 | -43.19962 | 2025-09-14 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1c68eaa-6bd1-309e-ad55-14714e92577e | -4.73346 | -46.16555 | 2025-09-14 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e037ec7b-3147-3325-b900-d0c4d72c0d12 | -6.43965 | -43.32188 | 2025-09-14 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f71fc307-8fac-3eb1-9ab0-b0ee8cf57244 | -4.13486 | -48.81332 | 2025-09-14 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad886d5e-797d-38d9-a3eb-e844d3d30c8d | -4.48865 | -48.11225 | 2025-09-14 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 31bcc090-9667-3e38-be10-c6a898b287ee | -3.09037 | -49.46243 | 2025-09-14 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1051dc6-95b1-33bd-b617-24ba13972dac | -5.64766 | -45.9476 | 2025-09-14 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 182c98e9-f076-3c3f-b09a-d182b09f77b1 | -2.82488 | -47.7219 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README28.md)
