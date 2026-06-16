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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73f72a85-5398-3a16-b806-738839dbc919 | -3.50804 | -48.03341 | 2026-06-16 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c4d807e-4f1c-3b81-8054-86d4cd7fa39e | -7.71825 | -44.16503 | 2026-06-16 04:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f8d1bf4-48f8-354d-8f7c-c857968b9f81 | -6.14133 | -48.52677 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d2abd46-4e15-3817-9402-51c0209616ee | -8.18882 | -46.7587 | 2026-06-16 04:36:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dfc5ed3-3d96-32ca-a903-a2a99eb3e8ad | -6.13141 | -48.48244 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf3e8a66-a99c-3551-8bea-a0a205eb14d1 | -7.99271 | -46.99024 | 2026-06-16 04:36:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96e878b2-6937-3e14-b5ac-6f6768f106e0 | -8.99257 | -45.73428 | 2026-06-16 04:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbdc79d4-5982-3b0d-bb94-2e66ccff7371 | -6.46711 | -46.89598 | 2026-06-16 04:36:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b2e09a4-34a5-329a-97a2-bb5a9d2c0ba2 | -7.37179 | -49.85756 | 2026-06-16 04:36:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad17c005-c669-39d0-af2c-486bece84670 | -3.56301 | -43.19953 | 2026-06-16 04:36:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6da231eb-6fce-3a32-b4d2-aba9fe51448e | -5.32583 | -44.69331 | 2026-06-16 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd1910bb-ea63-3c04-a6c6-d05823f57c95 | -5.35183 | -45.18872 | 2026-06-16 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dea8dd64-d1f0-3575-94fe-6641fdf1a224 | -7.76716 | -47.57018 | 2026-06-16 04:36:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3faa22d-2013-305c-b675-a1487e01d0a0 | -7.62928 | -50.02332 | 2026-06-16 04:36:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1aaa2e98-4f02-3f10-80f5-ad683ed74083 | -6.12808 | -48.48194 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5980c03a-409d-3580-90c4-27c0cb5c9511 | -8.93526 | -46.95859 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 727c304a-f4e8-3695-97c7-e41c79ecd353 | -5.58627 | -43.50729 | 2026-06-16 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4577fa34-b2f7-3368-bf28-6eb465c92d1c | -8.93582 | -46.95496 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9115a7f6-8230-32e7-a5fa-7862a502d2ff | -3.50416 | -48.03637 | 2026-06-16 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d57cff58-baae-3bdd-8186-ce8c69fd2054 | -8.94876 | -46.96074 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a66eaec3-9a58-3c25-adbe-7d8e08616406 | -2.1432 | -53.64462 | 2026-06-16 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02a6ee8d-52ef-3e85-9978-5bd8afec9107 | -5.5901 | -43.50784 | 2026-06-16 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33623646-6fc9-3c18-a914-23b174c9ee7b | -8.1922 | -46.75923 | 2026-06-16 04:36:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9601cfeb-4931-37fd-8869-6bd3392699f9 | -6.25172 | -48.51595 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2fe06a79-d6ca-301f-bcb1-554b889be94b | -6.97577 | -42.88593 | 2026-06-16 04:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 648c9578-b660-3ba6-b4e4-3966c90e7055 | -8.94032 | -46.97055 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52a819c9-895b-3612-9168-8669efc00b30 | -6.1182 | -48.48009 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e5c85d2-d33f-3953-89fb-2ebd297f8514 | -5.83943 | -43.48903 | 2026-06-16 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| defce17e-4857-3599-9eb3-2571884c3181 | -8.9347 | -46.96222 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2da799b-239f-3e59-aa8d-939a9d1b5704 | -5.79966 | -45.0733 | 2026-06-16 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 626ed4bb-0f0f-3fd0-9d4e-14aaf8965385 | -6.8378 | -47.90649 | 2026-06-16 04:36:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c81d8da7-f10e-3b10-a96c-c5f9abb391ea | -6.13525 | -48.52221 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75047ea4-7c6f-3cf0-a697-513695e5b93d | -6.3044 | -43.64228 | 2026-06-16 04:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 422784c7-f44d-3c41-b36d-6301d57f647e | -8.94482 | -46.96384 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 199a2172-5054-3bc0-bcbc-0575890f3f2e | -8.95439 | -46.94672 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ca5864b-7647-35f4-b048-e291fb31f500 | -6.13528 | -48.47947 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6d74ff6-d32a-31ed-814b-26c9f3879241 | -6.30512 | -43.63753 | 2026-06-16 04:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c32c8da-1439-308a-b0ee-2409a2668227 | -6.97171 | -42.88532 | 2026-06-16 04:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| e005a71a-b1d9-3073-aa28-6335ff673e0d | -6.17839 | -48.50769 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28211ab7-a5a0-33bc-be29-59c9c170b084 | -5.61954 | -51.19877 | 2026-06-16 04:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33a43f01-ff50-3d44-b835-72e224879361 | -3.67546 | -49.00388 | 2026-06-16 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab5437d8-d285-3703-b975-82e36268c8d5 | -6.46323 | -46.89897 | 2026-06-16 04:36:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ddac58d-82a7-36b4-8f50-7a08d2f6cce8 | -5.92913 | -43.48032 | 2026-06-16 04:36:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74410100-f4e3-3174-b72d-831f0eacda4d | -6.39468 | -44.1729 | 2026-06-16 04:36:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 51b547dd-2bfe-3490-8463-0a1b4eaf0a5c | -7.3487 | -46.21014 | 2026-06-16 04:36:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f78bfc5a-1950-3291-b944-2633829f1e3d | -8.94201 | -46.95967 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df36e57f-d154-345e-9aad-cb64980de01c | -6.83449 | -47.90596 | 2026-06-16 04:36:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b0d863e-260b-3c75-982f-f03d9989861d | -5.9815 | -47.06795 | 2026-06-16 04:36:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 796104b0-9bb1-392d-8659-3342aed09a36 | -4.48819 | -48.28154 | 2026-06-16 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 534bbc1c-b080-3dea-8554-6caeecde30b6 | -6.18391 | -48.51579 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 068c6de1-a531-39d4-bacf-7b041bdc08b0 | -3.15297 | -48.58141 | 2026-06-16 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e05635d-0f61-3708-823a-4e078eff3a4b | -7.20118 | -47.58472 | 2026-06-16 04:36:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2314856-a85b-345e-a290-0a1502de8c75 | -5.84013 | -43.48428 | 2026-06-16 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e6c0012f-1bd1-37cd-aef1-3a33de317d96 | -8.2833 | -48.21846 | 2026-06-16 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea4dc073-cb71-37a1-94cb-a8cb6ce978ca | -8.28275 | -48.22192 | 2026-06-16 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b6f1878-0237-3a8a-8790-612527652624 | -6.24509 | -48.51488 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5556ca94-4b20-3752-a8f3-48038416299e | -6.13469 | -48.5257 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dc4cffa-973b-3b03-a64c-7c83688a8c61 | -7.71756 | -44.16966 | 2026-06-16 04:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2254af1e-b128-3f77-b1e2-611198525283 | -6.3984 | -44.17345 | 2026-06-16 04:36:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fe354cd9-3473-39bc-a0f8-8b00e3c62646 | -8.94595 | -46.95657 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a66fe0c-e4c5-3879-ad24-83bc7efb9588 | -5.587 | -43.50257 | 2026-06-16 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9169d33d-21e6-35a3-a941-7886310deae1 | -6.11433 | -48.48303 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c062a6e-288f-3abc-98c3-a5d8a4dcb069 | -8.8683 | -46.96687 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2f665cc-0108-3631-baa5-6adbd8e2ce9e | -5.3294 | -44.69387 | 2026-06-16 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 434ac27e-4ff2-3345-89de-1c19969287e5 | -5.80026 | -45.06933 | 2026-06-16 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5de05dbe-fcc8-36fe-b442-0b38dfd8cad3 | -3.50028 | -48.03934 | 2026-06-16 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f40fb70d-7562-37ee-b04d-e0b58a5d0532 | -7.35301 | -49.86582 | 2026-06-16 04:36:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a23741b-d11e-313c-8568-79103c1d66cc | -3.51136 | -48.03393 | 2026-06-16 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 962617ea-f9e9-3220-b9b1-8a0e8ad55534 | -5.80228 | -43.7899 | 2026-06-16 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c21f446-2c9a-355c-bcb2-5bab6e085e2b | -6.00924 | -47.10799 | 2026-06-16 04:36:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffad7571-60a2-38d2-b89f-fb6f5e092162 | -3.50083 | -48.03585 | 2026-06-16 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e278485-df31-3a8e-ab45-786200aa7dcf | -6.30368 | -43.64703 | 2026-06-16 04:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e9999856-f85c-3d8c-beda-e5585ec0f50d | -4.35689 | -47.76019 | 2026-06-16 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bd559ae-02af-3943-8525-4985e967db45 | -7.35981 | -49.86691 | 2026-06-16 04:36:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3e60dee-ebde-33b0-a669-48ad74b3b59c | -8.96285 | -46.93685 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2921f45b-f780-388d-b78b-acd9b79c8039 | -6.74992 | -47.12739 | 2026-06-16 04:36:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b08972b-53c1-3731-932d-92bdba1782cb | -6.83173 | -47.90198 | 2026-06-16 04:36:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 455045df-f5f2-3fe1-b8da-489a6b15306c | -8.95158 | -46.94254 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ccb2f59-53b0-36f4-8b90-0d85a1e57e4f | -8.9527 | -46.95763 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40038043-c554-33e0-9fdc-324626aa1de0 | -6.25117 | -48.5194 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a729993a-81eb-3e0b-ba20-3e50005a5a7a | -8.94089 | -46.96693 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3699d142-2509-3c53-a681-fc17015ec0d5 | -8.86548 | -46.96267 | 2026-06-16 04:36:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03e49ff3-8208-35b0-bac6-dee211ee7bd6 | -6.39029 | -44.17677 | 2026-06-16 04:36:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 818b731c-ab3c-3c8b-86a6-4ea1379bb4f6 | -5.80259 | -45.07776 | 2026-06-16 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c1fff1d-2ab5-3622-82f8-6d68d3b876ca | -6.24841 | -48.51541 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e408d9c7-52ad-3b9b-8ca8-8ccb8977fac5 | -6.17783 | -48.51124 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43a4ad36-9ef8-3762-accb-31021968320a | -6.14188 | -48.5233 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fffd08df-0805-3b0f-ab93-11ff2ac5c4fa | -4.03706 | -46.99009 | 2026-06-16 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b06825f4-a79a-3b89-a030-3acd19c0f336 | -3.95865 | -43.11576 | 2026-06-16 04:36:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 455b32b3-63d6-3dfc-acea-e23ca18e2be2 | -5.80199 | -45.08171 | 2026-06-16 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37a50def-197f-3bc8-8f68-adebb8db39a8 | -5.83872 | -43.49379 | 2026-06-16 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49ea538b-ab1c-36e3-8aa9-754596e34692 | -6.39401 | -44.17735 | 2026-06-16 04:36:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 81e93928-39af-3cb8-bdbb-82540757d05c | -6.98146 | -42.87568 | 2026-06-16 04:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a1ccca2f-27b9-3e75-b368-f66b6e2f0aa0 | -8.9482 | -46.96437 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 490e234f-4728-39b6-85fa-d09fbaedfeba | -5.80379 | -45.06984 | 2026-06-16 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7e87bcac-ef80-3e1f-a807-b06870e5e42d | -8.95327 | -46.95399 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 505ba77d-f24b-30c8-a7ff-413a9368b0d9 | -8.27944 | -48.2214 | 2026-06-16 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c27868fc-c249-3052-8026-0d5519d96c70 | -8.95214 | -46.96127 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b821207-4f45-3aab-842c-77de6facecc4 | -5.80613 | -45.07825 | 2026-06-16 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1eb508c3-3c4d-3c5d-82ad-0f5eee015a0b | -7.72203 | -44.16561 | 2026-06-16 04:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README10.md)
