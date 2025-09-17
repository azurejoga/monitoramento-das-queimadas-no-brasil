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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c1c7dd5-a7d6-3ed7-881b-60ea520f05b4 | -3.68763 | -49.01837 | 2025-09-17 04:10:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 10b01335-59a3-3313-8693-3005503ee9e5 | -9.58735 | -45.66656 | 2025-09-17 04:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d896ec5-18c6-345a-8247-d4f4601f69e1 | -8.53629 | -48.97609 | 2025-09-17 04:10:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 050f9e48-a1de-340d-8c54-24a6690d8fd8 | -9.04591 | -44.95289 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d6cb63c-7223-33dc-a5de-fb1a0547b00a | -5.09342 | -45.10012 | 2025-09-17 04:10:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd2f3f51-88bf-3420-b7a7-e0eee9bbfc8d | -7.74164 | -44.82544 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb78149f-3215-3051-acf3-c88a967c4352 | -6.03871 | -43.65905 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d18d53b1-b69e-3df4-baa3-0340d0247765 | -8.16366 | -46.7495 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7197011d-0bdc-3711-9013-a6ead21f6ed0 | -9.09472 | -44.92358 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe2c74a6-df12-32a1-b878-24347b977851 | -6.88042 | -43.96411 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1bd9195-6718-3315-95da-eed98f3bb0be | -8.00781 | -45.65311 | 2025-09-17 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a01d22a1-2f9a-3cd5-af9f-e6aaa5dff6cd | -8.43388 | -47.6817 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 864d252a-2707-3469-b17d-dc5ef32d0f8e | -8.15475 | -46.74657 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 04b46a6f-1672-3d4a-bef3-310a92fe832a | -9.54705 | -46.29815 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4063edfb-74b8-37d6-a43f-0582dc70b978 | -8.96462 | -46.00972 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97c2662e-9073-3854-a7bb-9b5b00ef4759 | -7.33731 | -44.58646 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45d6ab15-5888-3e6b-99e2-c1b54397903d | -5.81595 | -46.36557 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2acfea5-c900-3404-b128-70d351805a3d | -9.07649 | -44.94531 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4754bf0e-988e-3510-96c8-10d97c210925 | -6.17036 | -44.50449 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b922eb80-9a2e-3f99-b5da-043700efb926 | -9.17619 | -46.93179 | 2025-09-17 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1f19f3fb-eb6c-32ed-92ed-c8ee283cd700 | -7.57524 | -44.59032 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 249e6ef0-5eaa-3fa0-bb2c-55eff1e0ad0e | -5.77533 | -42.77727 | 2025-09-17 04:10:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5654d310-f217-3be0-a27f-74b257a8df2b | -5.77158 | -45.90586 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 5a9b95d1-e421-3cff-ad0a-c1f03d5232ca | -8.14988 | -46.75117 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ba391bd1-de8f-39dd-b164-f9232e1302fd | -7.84107 | -43.84895 | 2025-09-17 04:10:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 907e0bb6-bde8-34af-9dcd-6e59b5271720 | -5.0823 | -41.17061 | 2025-09-17 04:10:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 71c6a4a5-c92d-3e09-a7bb-feb348052052 | -9.07582 | -44.94934 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdf714f9-bfbe-350f-9ce3-907d1e1cd744 | -8.97295 | -44.192 | 2025-09-17 04:10:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1363cfb8-9053-3ad1-b152-366a9ee001bc | -7.32317 | -43.96996 | 2025-09-17 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 749d4e96-2467-35b1-8af6-a064e75680b7 | -3.2376 | -46.78788 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97dbb88f-e8c7-3880-97eb-37f8eb20fef2 | -7.5706 | -44.55222 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 53dd4562-e014-3449-9a7b-ad04b218447d | -4.0552 | -47.5042 | 2025-09-17 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d296a5b0-9c53-341c-a692-1fbd489bd5b0 | -6.57251 | -44.08301 | 2025-09-17 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43ce4e9f-bd8c-3417-8ea3-c66836619cf1 | -8.88479 | -46.18935 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4d497d5-8dab-3572-8e98-2541d45d8dcc | -6.40897 | -43.35363 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdc40fae-9a18-37b1-a099-b13c53d7558f | -6.16724 | -44.49696 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e91e06b-4383-36f0-a79f-033ebe53b4d8 | -9.73545 | -47.85498 | 2025-09-17 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d06a4e95-c811-3ced-b3f4-d8ece04b7dfa | -6.16626 | -43.6706 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0dc08590-3323-3011-a439-b4710744c080 | -8.87188 | -50.14315 | 2025-09-17 04:10:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a7c7b47-c4ba-30d5-9e05-173cca9e979c | -8.95729 | -45.7547 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e9cc06e-3498-3661-a9b9-ca299e74d81f | -5.62485 | -44.82797 | 2025-09-17 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0f93f6b-5d9b-3829-af37-e91032c52e41 | -9.10614 | -46.92279 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8a85712-41ab-3707-a627-5b39d6417035 | -7.59017 | -44.58863 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cba192a-31b2-38cf-8556-f09b80dedf46 | -8.5371 | -48.97138 | 2025-09-17 04:10:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4cfa09c2-f4a4-3a41-adfb-b562cda51968 | -5.47782 | -45.34995 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5173d09d-6c54-369d-bc23-50b7fd47bfaf | -5.78622 | -43.92653 | 2025-09-17 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4eee698-d4f7-3f8a-bcac-a78304de4444 | -8.2685 | -47.58472 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 999948cf-ffed-34b0-ac7d-da9f21c64cf6 | -10.04783 | -44.34967 | 2025-09-17 04:10:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f57f3cf-6caf-3a82-9a66-16ece1625377 | -7.67519 | -46.63586 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 259a2b08-428f-32a9-84f8-709224ad78db | -6.98392 | -44.61657 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4a8d919-7dfb-3685-9982-02ca8df29595 | -6.8798 | -43.96796 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4681f481-1552-39dd-912c-05dd3a9327e6 | -6.16813 | -44.49558 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93d30f9a-66b6-3526-9bb9-b8af144eebe3 | -3.23194 | -46.79531 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a5023893-be09-3743-967b-e60885f6f999 | -6.98031 | -44.61602 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffe8ac90-c361-390f-b345-b0de5591a324 | -6.97767 | -44.45232 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35da5a18-c395-3b09-a154-128e3990d47d | -5.49931 | -39.70212 | 2025-09-17 04:10:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4eeb1501-042f-393f-bec5-f0824949f2d1 | -8.72458 | -46.97013 | 2025-09-17 04:10:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 678c5cfc-a8df-3747-974d-13be609a2c69 | -9.08194 | -50.31528 | 2025-09-17 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35f93565-5059-3a94-879c-410cbb56d218 | -7.2596 | -46.6083 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a327703-773c-306d-b93a-1ccb5cda3d7c | -6.39988 | -43.34452 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 07ab1ced-afc0-30d5-812e-b8fc87ed786c | -2.91949 | -48.30447 | 2025-09-17 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0488b213-5c89-3e23-8e23-7d26e6028518 | -7.82834 | -46.15697 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 392498d8-8497-3e7a-b9e3-bbc056ea9aa4 | -9.5422 | -46.29451 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d0de41d-8fa7-3609-accd-e3173b618085 | -8.6761 | -46.40709 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 775af47b-03f7-377f-aff0-8ab51d57d83f | -2.91864 | -48.30973 | 2025-09-17 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 8aaefbcd-b30d-35c0-8b7f-910abe5e500a | -8.1609 | -46.76538 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f73d53b-af6f-3f61-8a98-6b1868c1b32e | -6.15764 | -44.53641 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8630fda-1e6b-300d-8515-62bf0bddba0d | -8.63647 | -46.42781 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bebf2241-554d-3524-9683-fe0daa4f66dc | -9.11175 | -44.86438 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4477e6f9-810f-3ced-90dc-4398d53f61ca | -5.60952 | -42.89623 | 2025-09-17 04:10:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f9fc19f8-8358-339c-8764-eb1f1b9a6551 | -6.97833 | -44.44835 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75026244-d26d-3158-8588-f5414f3ae745 | -5.22006 | -42.32271 | 2025-09-17 04:10:00 | NPP-375D | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a2072fcb-3d02-3464-8d24-829078c1ebf5 | -7.07017 | -44.34732 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e1ab879e-a221-3c09-a3dd-aaaece980833 | -8.89604 | -47.88179 | 2025-09-17 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9dc5f29-2bca-3cc1-9b16-2fc5526561a1 | -2.92034 | -48.29928 | 2025-09-17 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c9c6280a-8e7e-37dc-9751-c17a1956c637 | -7.99506 | -45.68362 | 2025-09-17 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3186ca0-0027-396f-bd09-f058e2711672 | -8.68385 | -46.40842 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 616f43be-c27e-3970-89a6-c653b0d4a070 | -6.9846 | -44.61237 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2db5473-5dbc-396f-b361-6ef9f1689961 | -6.97249 | -44.4393 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29a5ec35-88ef-3166-b01c-bf11c2daa9cb | -9.06578 | -44.94362 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b811657-398c-3363-ae21-304c1f3da429 | -7.71952 | -45.29568 | 2025-09-17 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1f8d58b-2ecd-3208-aafc-8b20782a56d0 | -5.7759 | -42.77369 | 2025-09-17 04:10:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 75df0d81-5b30-3306-af62-7941c5be8eca | -7.73058 | -45.29749 | 2025-09-17 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 898db42c-be71-3cb5-89e6-15db8fb2671e | -9.12265 | -44.887 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa4b2af2-30d0-36e0-b165-e8f7e8612663 | -6.52922 | -41.81906 | 2025-09-17 04:10:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c51682fd-009c-3d38-9e28-18c298919636 | -8.2975 | -47.98797 | 2025-09-17 04:10:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbc4384e-880d-35c3-ab5c-673b73478be7 | -7.06885 | -44.35534 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f7b96af3-bc2c-3773-97cc-755bd9f822d0 | -7.61083 | -47.465 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75dfb09e-2aa3-3ab1-b36a-3efd11d7bf71 | -6.16261 | -44.52882 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f51014b1-85a4-341d-b209-bc73ef49e9ad | -9.73962 | -47.8558 | 2025-09-17 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22be8690-75a9-3adb-88d7-4ad271dd08a4 | -8.61578 | -45.71645 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2f6b30a-5dea-3cfb-9b3b-603839c3afce | -5.80368 | -45.9314 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1d1d923-4d6a-36c7-9f1a-c09481c2087a | -7.53202 | -44.73071 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcba1905-d981-3c8a-a45a-bfb56c525700 | -5.5965 | -45.35832 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e4eba75-cde9-3fad-8525-6ba871ea942b | -7.81682 | -46.13055 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bb30a96a-02c4-3d18-99bc-1f71e9037296 | -10.67011 | -41.2896 | 2025-09-17 04:10:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5907bdca-2666-3bf8-a711-8878a0ff80a0 | -6.87195 | -45.18611 | 2025-09-17 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d85b29d-c144-3833-baf5-dc332caed64b | -6.40836 | -43.35739 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0b5810e-efe7-3af6-9658-30db813d4049 | -7.52857 | -44.73785 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8908b45f-edfa-30e7-b555-f104e2f6bab8 | -8.6661 | -47.11676 | 2025-09-17 04:10:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README25.md)
