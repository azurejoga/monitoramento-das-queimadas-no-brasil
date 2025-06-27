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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d1f10c5-e9cf-3c13-9617-b68b9545d5ec | -11.7491 | -54.23304 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43e310b9-b0cd-3ca8-b0cb-512b35fd7c63 | -13.05204 | -48.81995 | 2025-06-27 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d50cad89-1d66-3390-adbb-bddcd46bbcee | -12.02501 | -57.08295 | 2025-06-27 05:10:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b6b19d8-1ac7-3009-859d-8b13f25eaef0 | -9.23512 | -63.62247 | 2025-06-27 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fc407d5-505b-3a62-8f17-8d307949decb | -9.34692 | -58.85469 | 2025-06-27 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4a0012b-7a7c-3951-82bf-01d6df2299dd | -11.18298 | -55.91599 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce64837b-f723-332f-9944-d33634aa324c | -10.491 | -55.61298 | 2025-06-27 05:10:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87bc8090-2fe4-3a27-bdb9-88a4a0cceca5 | -10.88171 | -53.77589 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 900495c4-1297-3229-ad80-cb55770b734d | -11.0723 | -55.07285 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b403d0e-05cd-3b9b-b870-33eb09b2c2ec | -10.85292 | -54.0406 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c95ff8a6-dcf9-39c2-b8a0-5f0cacf6b7aa | -12.03383 | -48.75393 | 2025-06-27 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85c07ac3-f973-384d-9b77-0929ad686cd5 | -6.77711 | -46.33126 | 2025-06-27 05:10:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4951c0a-83fd-3720-874d-c6c86a3f71e8 | -8.61537 | -51.56757 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74bd21f7-51fb-3339-93a6-be48efccccd9 | -8.37401 | -51.07514 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69288921-e68f-340a-9e11-a5c8ed5287df | -11.74242 | -54.71452 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aed34199-7ac9-3698-9302-f11d21ee38b7 | -8.47316 | -48.26294 | 2025-06-27 05:10:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8e4019b-3e0c-38e4-904c-0b6ea66bd1ab | -11.99878 | -47.16426 | 2025-06-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efbc7f1c-43b4-3deb-be75-9b1282ebb816 | -8.61465 | -51.57365 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aed7de46-5144-3378-9e1e-ec1d84ac7d48 | -10.85563 | -54.03891 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04419149-2297-3396-ac3d-986834784d6f | -13.04945 | -48.81861 | 2025-06-27 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd01a13c-4ccf-3189-a078-a4e705958d50 | -9.11945 | -49.43617 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a44c3276-952b-3813-8303-3a17c1299513 | -11.50152 | -61.82523 | 2025-06-27 05:10:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d5692fb-01f2-38f6-af74-4254f62aedb3 | -11.06481 | -55.37558 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ada3cde7-01b0-38de-8488-b90e98a23dac | -9.07666 | -49.4263 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd3c96eb-9c0b-3113-9073-4be7c6a8cd42 | -9.50073 | -56.0967 | 2025-06-27 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3b04ae0-81d2-3b46-97a5-5b39f2efc154 | -10.37128 | -51.81141 | 2025-06-27 05:10:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9236d202-d4b2-3c45-b193-d0aaa91e6b1e | -11.04212 | -59.17739 | 2025-06-27 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd2b0ea9-04f5-3a76-957a-cd73e668d8f6 | -7.89174 | -61.47431 | 2025-06-27 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65564c11-bbd5-3956-bd66-dd62c61193ff | -10.02881 | -54.32585 | 2025-06-27 05:10:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1f23213-4dbe-3026-8441-495e0a0102c0 | -10.36185 | -57.26085 | 2025-06-27 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acf54ac2-2d52-3842-bc33-afab4b39cb66 | -10.85247 | -54.03354 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5be5ba2-669a-3bda-a935-174433cd4f56 | -10.85318 | -54.0287 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d8289a9-6cb2-3b43-8e2a-91b37ed02161 | -11.77571 | -55.03753 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0638a747-1862-35fd-86c6-e225dc1fa403 | -8.61917 | -51.57254 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab76919a-4563-3498-ab2b-3a8d8582a6cb | -9.51675 | -56.10689 | 2025-06-27 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5d28b0e-ce36-3675-9a64-8c59ef22030e | -12.1119 | -54.66641 | 2025-06-27 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00263dac-7e07-3b8d-926d-513085fced98 | -10.86981 | -53.77746 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa24113c-f863-3c5d-b58a-0d04cadd0631 | -10.87375 | -53.77801 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 161eb5c4-d7ef-3aa8-a2b7-b1b6f61a039f | -7.54406 | -45.83191 | 2025-06-27 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 843f47f5-b480-3edd-b746-600421a5386b | -8.62357 | -51.57318 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28d17218-5bd4-34b9-80e1-950b8d6ea992 | -10.10955 | -64.91451 | 2025-06-27 05:10:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 093d22d2-0962-3550-b45e-aa923d80a23b | -9.11774 | -49.432 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9966f3c-9c3b-3ec5-bebb-4936d32798bd | -10.41983 | -47.5088 | 2025-06-27 05:10:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 838daccf-8330-35a6-a48c-769a9e424884 | -11.57171 | -52.10991 | 2025-06-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 09b8be60-989f-3045-9cab-8e233ac2e792 | -11.57613 | -52.11057 | 2025-06-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 824b55b3-c2bc-3b5c-ad3d-d82dc9db5195 | -10.43155 | -51.82727 | 2025-06-27 05:10:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86629c22-52ff-3f2e-908d-117a4b17c95a | -10.83349 | -54.05555 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6835005c-268a-3a6c-9d32-68e90ec54c69 | -11.67443 | -46.72898 | 2025-06-27 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 253571e4-08d3-3c6e-aabb-a3184addbc1f | -8.60979 | -51.57558 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0004cc3d-0bb1-31b8-8cc8-468b4deb7c5f | -9.07153 | -49.42558 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e2e538f5-31cf-382f-89eb-5d9d1e81441a | -11.44508 | -54.47141 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 553b4173-8821-34c3-a8ff-d2b129d09c0f | -8.47757 | -50.27966 | 2025-06-27 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1e9b569-41e5-375f-80c4-131e4f1672d4 | -11.57555 | -52.11493 | 2025-06-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| cdb69141-e779-369f-ab2a-b308c196d1e6 | -10.70978 | -59.13078 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db65a580-1272-3f5d-bc95-340a41f3622b | -6.77185 | -46.32788 | 2025-06-27 05:10:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67a242b5-e9e8-33d5-b22b-def334a9583d | -10.81151 | -57.75244 | 2025-06-27 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c432a6ec-2a1f-3f06-81bc-5d6ffcc1ed97 | -9.07624 | -49.42941 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0d17b5c-5e19-3579-bf09-79270b41fec9 | -9.07069 | -49.4318 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 58d4a15d-0d17-3bba-8156-cfece90baef8 | -10.8595 | -54.03946 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f435ec8-e078-36a8-abad-c5017985ead1 | -6.77794 | -46.32885 | 2025-06-27 05:10:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9109b4c9-ae4a-3a95-ad50-62efa66f8e61 | -11.06778 | -55.38029 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7cfe6d4-8237-31cc-8364-aaa309a8c783 | -8.47269 | -48.26645 | 2025-06-27 05:10:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 089697c1-595c-33a0-aec0-3cf871819d2a | -8.61337 | -51.58245 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 681b69a9-9b4b-30b3-88a4-ffe2b97b8559 | -11.80295 | -57.3519 | 2025-06-27 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e18f284-db4f-30f1-be4e-4ebf8a222d86 | -9.1216 | -49.44195 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cab7471a-7d84-30f1-bda0-a17451644c43 | -7.0142 | -49.17951 | 2025-06-27 05:10:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cea92e44-cdf3-3c90-83e9-9c3604bc2ac1 | -10.86133 | -54.03688 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e67c229-abb1-36ac-9784-06c7523967ad | -12.00496 | -47.16511 | 2025-06-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 968fd87c-2af8-32a9-a3eb-8b4d0125ea4d | -6.57775 | -55.00049 | 2025-06-27 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d9ba36b-3975-35e2-83e4-e0d2e1a0f086 | -11.7794 | -55.03808 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 300c995f-8470-3f46-997e-910e8c496951 | -5.22676 | -56.02581 | 2025-06-27 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ca6501f-8f9b-3dcd-aff0-74e172801ed6 | -11.43371 | -54.4697 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa380a2c-7ed1-360b-ac0d-ea1b7ff107d2 | -11.68075 | -46.72989 | 2025-06-27 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01f40cff-3a9c-324a-b537-3f629c23d6ab | -5.00931 | -56.176 | 2025-06-27 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab02acc1-afd9-37ce-ae70-6c3ecce37fdc | -13.10143 | -52.29675 | 2025-06-27 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f6d0d45-53af-3d9c-b8b1-18ad89179c55 | -10.8752 | -53.76795 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd1f6ed4-5400-3ae2-a214-6279ded6a474 | -6.57426 | -54.99997 | 2025-06-27 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49b5f351-c90c-3e5e-bdaf-d65dc754fff8 | -8.47818 | -48.2673 | 2025-06-27 05:10:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 73ab60b7-efb4-37b8-a520-e8b517ea9ba9 | -11.78006 | -55.03363 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b4e8312-eb29-3084-8b0d-587e636742c2 | -12.02727 | -57.09086 | 2025-06-27 05:10:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48721d3c-c22d-364b-a394-6b849520857e | -9.5291 | -63.57299 | 2025-06-27 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26d71e64-7da4-3d93-b9cb-be418c68a99a | -11.18006 | -55.91146 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eef0ddae-b586-39f6-aee9-146355d40e55 | -10.86356 | -54.29715 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 892ff71c-2551-3ea6-961a-361735796755 | -10.82696 | -53.74045 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56597fb7-976d-34b2-bc27-0d66a35e8a6c | -11.77875 | -55.04249 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b16f6c84-1088-3d8e-aa4c-e81f7981590c | -6.77102 | -46.33038 | 2025-06-27 05:10:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da7e9344-1cc8-3fe5-b169-9f9c1f3272de | -8.60963 | -51.57733 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c299760f-f402-3885-af54-3c818ce76d41 | -11.82445 | -47.54196 | 2025-06-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f9174b2-4f46-3182-855c-6d8a58135178 | -9.07111 | -49.4287 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed8ae0d3-5881-3622-a4a5-d1756e54bd5e | -11.06059 | -55.37922 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d011642c-5a7e-330d-b08c-b2f012671e6d | -11.99935 | -47.15937 | 2025-06-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a203e57e-5888-3647-bf9e-5d46207a45ed | -12.10811 | -54.66586 | 2025-06-27 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30832133-6b6b-3f65-bbc6-b72bff8d63b8 | -10.83491 | -54.04578 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ea02b07-2bd4-3061-8c96-2269f7de9586 | -8.61737 | -51.5857 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0252e31a-a5a7-319a-96af-e14b4f25cd15 | -11.67814 | -46.72657 | 2025-06-27 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdcb7f36-456f-3c60-aa82-95ebe08dbcfb | -8.61358 | -51.58064 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 105f8377-6846-3631-9d82-3ccadc51955c | -9.07027 | -49.4349 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6bced37a-1744-3da8-be2c-1415eff0a23a | -7.01378 | -49.18246 | 2025-06-27 05:10:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e7709a6-35ae-386e-8f68-d24cb9598205 | -13.04641 | -48.81916 | 2025-06-27 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed91464c-4678-33f2-9d1d-58ab861c00e2 | -9.75806 | -48.04193 | 2025-06-27 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README27.md)
