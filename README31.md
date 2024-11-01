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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95fc2b1d-054a-307b-bee0-41755b05ef3e | -4.6558 | -46.31937 | 2024-11-01 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a84b6468-8b51-3953-bd13-3d4f7e7daded | -4.653 | -46.31533 | 2024-11-01 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25c6dade-73b5-302e-bced-6d4108be52b0 | -4.65245 | -46.31885 | 2024-11-01 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6f0eceb-3c7d-3c3c-adaa-4092a198e2e2 | -4.61954 | -46.50833 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a4e66fb-c14f-3e7b-806d-f6877d562109 | -4.60342 | -46.69894 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46547230-bc5b-35df-a91c-e6eabbb5a368 | -4.6001 | -46.69843 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2caf8cd-a9f4-3225-b2a7-3034942f30f9 | -4.59955 | -46.70189 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0780166-5b75-3084-a203-5ce70e607da3 | -4.58867 | -46.57524 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 940aa2fc-3268-3440-b274-ff523ed093d8 | -4.56907 | -46.67934 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84786a08-7a50-3a58-86ec-c7a15c9809e7 | -4.56852 | -46.68282 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4818a8cd-9b2c-3c02-ad96-b6b6bd8117e4 | -4.4385 | -46.64456 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fac2cc70-223d-3f7d-a2eb-9345232fc0b9 | -4.36293 | -47.47411 | 2024-11-01 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57ef7164-0190-3ad7-aa8f-3f0568b5b4d6 | -4.36239 | -47.47754 | 2024-11-01 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa630dc9-fe1a-38b2-84a2-ed47a59cdf5a | -4.27783 | -46.27878 | 2024-11-01 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8bac5b7-08f4-3384-b8d0-b425b861032f | -4.24532 | -46.85938 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81e1c156-60f5-3953-846c-1e5275f10e42 | -4.19519 | -46.70263 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8eea1af5-15d3-3da2-9a49-f669e5448e01 | -4.19187 | -46.70211 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7181347-fc75-35aa-82ab-a65a2f174dfe | -4.19133 | -46.70558 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 235d7e27-48e0-3b57-b155-001aedbda57d | -4.18713 | -46.79719 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ee99e31-a7b5-3ba9-a0b0-112cfdc86152 | -4.15041 | -46.68494 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c011b679-160e-30c5-b17c-f2443bc99af8 | -4.13294 | -47.12077 | 2024-11-01 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3abfb3e7-2ff7-3181-87ae-d76d4858a6a9 | -4.1324 | -47.1242 | 2024-11-01 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cb5d7bf-9222-39b6-8b4a-5cb3fbac07e4 | -4.13017 | -47.11682 | 2024-11-01 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9c790d9-616b-384e-9150-8ee5d445bb57 | -4.12996 | -46.85912 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8dc29f7-a91a-37dc-b85b-aee3b9bdda84 | -4.12963 | -47.12026 | 2024-11-01 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85c606e8-a5fe-318a-8914-e1c04739ca22 | -4.12633 | -47.11974 | 2024-11-01 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d8754d9-9e7a-31ac-be07-b1ca49e05962 | -4.12357 | -47.11579 | 2024-11-01 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 651836c6-0aeb-381f-b064-47772495ae48 | -3.98232 | -46.43465 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47cdb707-09e0-3175-ac20-7b82f6c4506f | -3.92489 | -46.41119 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7957b94d-0002-32ff-9726-1e50e8af59d6 | -3.90277 | -46.4436 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2555ff4c-c45b-3dd1-bd83-30c98242c15b | -3.88451 | -46.21089 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8635088-a3fd-35e9-82cf-c7868d1c5b4b | -3.88396 | -46.21442 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4fa04d08-b59b-3319-8cf5-a4475dec115d | -3.86063 | -46.62581 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e50079fe-ddec-3cea-9850-70b13b434ba3 | -3.80253 | -46.93161 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 729c7c06-c3d6-3f60-bf01-71c32d92232c | -3.7842 | -46.50716 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccbef722-71aa-3ca1-8e63-737c94daf104 | -3.78365 | -46.51064 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25fa8658-25f5-397a-a2a8-50c81ba2e505 | -3.78311 | -46.51411 | 2024-11-01 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cca0ad64-9a9c-3d85-9dd1-8c459eaeae5c | -3.62669 | -47.29493 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da00ced4-8a03-3df8-8a74-78a39cf1d213 | -3.62339 | -47.29441 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6bdb5fa-cbe9-3ec4-a159-2b3e61af257d | -3.62285 | -47.29784 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d29956d-cb0b-338f-8f2f-e6031c345678 | -3.62231 | -47.30128 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa647c99-244c-33fc-98bc-4cfa968baec2 | -3.62177 | -47.30471 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8cddfb9f-7a48-3cd8-b352-9d932521ec00 | -3.62123 | -47.30814 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82c539bb-74bc-31e3-99cb-2f012af7a9d9 | -3.62009 | -47.2939 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aaea64da-6bd2-3a6d-9ced-6db3a4a1adcd | -3.60476 | -47.5203 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e3a18d68-a6b1-3b03-8b19-8c425a400162 | -3.59974 | -47.29424 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30d0c7f6-804a-3108-b7ee-df8ca1d70b58 | -3.59698 | -47.2903 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63963838-a386-3823-9ce5-762649618509 | -3.59644 | -47.29373 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae66de8d-6c43-30cf-9d69-497105880dc9 | -3.59368 | -47.28978 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89d08a78-9eef-35b3-a852-6f1d0a722e7a | -3.5845 | -47.34814 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42c4c347-7972-3f09-86a2-b0e606bdf03a | -3.56642 | -47.377 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47ca02f5-7bd6-36f0-ad0a-329f6d551b3b | -3.56258 | -47.37992 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5297498f-7dcc-336c-848a-0d0c15b4fffb | -3.56204 | -47.38335 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b6fcc3f8-36fc-3095-bdeb-d7334e7a1b28 | -3.5615 | -47.38679 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8e3b65a7-798b-3cc1-ab40-21757fe1f6bd | -3.55879 | -47.37889 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02ddf1c7-8344-3273-8ea7-d903688a989e | -3.55825 | -47.38233 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 8fbfa765-acda-39fb-a508-49fbb236365f | -3.55771 | -47.38577 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 77f0c5e2-1d3b-310f-b64f-bf6f49942595 | -3.55441 | -47.38525 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 9803f64d-3ed0-3fd7-9131-18f30fb90375 | -6.03293 | -47.9382 | 2024-11-01 04:29:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5f595c7-59d3-3f3c-bee5-427443989d98 | -5.64608 | -47.9124 | 2024-11-01 04:29:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fa43756-c2d6-3607-96bc-9d1aded08c65 | -5.39925 | -47.90553 | 2024-11-01 04:29:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32ad2749-a40b-30b3-94f6-2fa27add365e | -5.18913 | -47.79446 | 2024-11-01 04:29:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c69cdb7c-722e-3195-8af5-d9b7dbe8ad32 | -6.03623 | -47.93872 | 2024-11-01 04:29:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1cd2a42b-0e8d-3199-96d3-53a2bd4bd75a | -6.03347 | -47.93475 | 2024-11-01 04:29:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e64b4b1-05c1-3ae3-ad62-be010e7b37fd | -5.95468 | -46.63824 | 2024-11-01 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b35b25dc-7e8e-33ec-bf47-fe2c4d747de8 | -5.52377 | -46.91656 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9442d44f-b640-30b0-adda-b26383cd3cbf | -5.52177 | -46.5391 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04d29163-8a44-34af-b2ba-b150c3087fbe | -5.51842 | -46.53858 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98580d98-cbf7-3205-82d8-91fa971a43f2 | -5.38482 | -47.1546 | 2024-11-01 04:29:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e6db85e-c088-3f2e-9e73-2372eb322f57 | -5.2251 | -46.74137 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0496ce3e-6384-3667-bc22-50b939432dfc | -5.22123 | -46.74436 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22aa7231-009b-378b-9b87-4f6ded8d6a21 | -5.21791 | -46.74385 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7dbb68f-a55c-3548-be68-d8c71017d283 | -5.10437 | -46.88352 | 2024-11-01 04:29:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac8bcc16-c372-36e3-ab50-009558145cff | -1.72306 | -47.92561 | 2024-11-01 04:29:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cbba82a-fd36-3b03-9bad-7fd4002caeac | -1.71363 | -48.30552 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9b38eb5-b3ea-3444-9aab-b8e092009ebc | -1.68185 | -47.86162 | 2024-11-01 04:29:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7462d99f-1284-34b2-801f-482611a1a787 | -1.48795 | -47.21616 | 2024-11-01 04:29:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82112f8b-a8d0-37b4-b675-2968172275ea | -1.485 | -47.14877 | 2024-11-01 04:29:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ce810afc-7e1a-38f2-b1e4-f787ad3074b7 | -1.34575 | -47.75162 | 2024-11-01 04:29:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba8350a8-8c56-3df5-b02e-47d22ee9f385 | -1.33019 | -47.95815 | 2024-11-01 04:29:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa1b7e33-37ea-30a4-8e3d-b3f1e794e24e | -1.32963 | -47.96169 | 2024-11-01 04:29:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 685afbe7-3a93-3f2c-abbd-e67ec9f02d5c | -1.24351 | -47.83968 | 2024-11-01 04:29:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad8f6ec5-e3c2-31f3-8bcd-dc46ced18617 | -1.23569 | -47.73779 | 2024-11-01 04:29:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53cdb617-0fa2-3337-89d0-dc5156948b17 | -1.23235 | -47.73726 | 2024-11-01 04:29:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 666f564f-53c8-33fa-9210-16afd4151715 | -2.17032 | -47.95241 | 2024-11-01 04:29:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb621fe4-0f7b-32a4-b208-3b966aa44a5d | -2.16699 | -47.95189 | 2024-11-01 04:29:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55bca869-fab2-3685-ac00-47fbc213aa17 | -2.14238 | -48.1066 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4b85163-530d-3932-8f3d-9a9f3aafec0e | -2.13993 | -48.10595 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad36015b-ec39-3016-84a8-bdbf54e99b7c | -2.13937 | -48.10949 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85a7e70c-0c14-3a7c-bfb3-b243c2f21117 | -2.05144 | -47.91204 | 2024-11-01 04:29:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81218514-3877-3ee2-ab2a-aa9967d65eae | -2.05089 | -47.91555 | 2024-11-01 04:29:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f75b4cdf-e963-32ca-bf94-ddb0bf3bcf03 | -1.98593 | -48.5138 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 449b8214-9c55-3ceb-8af1-b6ad47d13521 | -1.97826 | -48.75936 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 304277e9-6db0-3d52-aba2-a5eb2e97da32 | -1.86416 | -47.82513 | 2024-11-01 04:29:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 767440f3-18bb-38d4-a77b-74a1bad73018 | -1.8597 | -48.00418 | 2024-11-01 04:29:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87fd8595-9934-39fb-8121-fe39a845401c | -1.85915 | -48.00771 | 2024-11-01 04:29:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b271174a-bc2f-337b-8ba0-5de530a50430 | -1.78685 | -48.61703 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da417c00-98b4-35db-9bc5-f6d359cbbc8d | -1.78628 | -48.62069 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a93bc9c0-7d24-3bf4-ac69-b5ab32e5c30c | -2.11694 | -48.28794 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19766b6b-5b6a-3197-84e9-ded96829ca3e | -2.02002 | -48.40828 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README32.md)
