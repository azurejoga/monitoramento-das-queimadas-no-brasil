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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 260a657c-d8ed-38be-b9fc-c46e9602e550 | -2.92684 | -50.42661 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 6dc8e097-1d5a-374f-88b5-8c606e99110e | -8.58654 | -44.45562 | 2026-09-14 04:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37c0abd0-35fe-3a51-ab19-59037fd518a4 | -2.91485 | -50.41553 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 6c3eefb1-f843-33be-81bd-7bd6dc793c51 | -3.05083 | -51.26941 | 2026-09-14 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0891ffbe-cea3-34ad-95da-8337e1ff2e08 | -6.33748 | -44.10973 | 2026-09-14 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94a3606e-6f68-3585-b1ae-f1959abd3915 | -2.93178 | -50.39573 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b51cc08-6ad7-394c-a927-cda2fdacf805 | -9.32463 | -44.35656 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7eb684c0-effd-3511-ba1b-a17262487929 | -2.67699 | -57.55167 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8c1b70ee-eddb-3e07-96f2-025a9ae5ad54 | -2.92667 | -50.43887 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f263e86a-654d-3ad1-b84e-b9c02bbfd3c4 | -7.01338 | -44.63028 | 2026-09-14 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daebaf45-4f6a-3b24-b16b-7b5c723cf508 | -2.91414 | -50.41995 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 193.1 |
| e2f6390c-6f73-35d8-927e-b35e0c1fc015 | -2.95043 | -50.4066 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9a0844f3-cab7-33e9-a2b6-9a2503f66461 | -8.12144 | -44.05619 | 2026-09-14 04:32:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7411dd6-ec34-3bd0-a7c0-bc72693f5196 | -7.09166 | -55.6219 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 149bfa5c-c2a6-364c-a38e-d5e938f411e4 | -4.62629 | -47.20811 | 2026-09-14 04:32:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf308093-4018-3fa5-85ff-36b9eb9411bb | -2.93115 | -50.43959 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9e7e3662-c061-3049-aaf8-f094391ff664 | -6.5761 | -58.84065 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 263e777c-983c-3a63-af4d-ab5808501f3a | -8.39555 | -42.22324 | 2026-09-14 04:32:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 091ab168-272c-341e-9c0a-d041a4846ade | -2.90915 | -50.45093 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 75bafc2b-a757-3623-9f12-4214d923f015 | -2.905 | -50.39133 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 4e1cab5d-b07f-311e-bcb0-ea15b15ed906 | -2.92291 | -50.40659 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| d453211b-fe55-3bb6-bfc1-966038226b7d | -7.08746 | -43.55129 | 2026-09-14 04:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb552807-3535-3519-98e8-f05831ba85b1 | -5.49431 | -45.60567 | 2026-09-14 04:32:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca8d2761-2404-3eed-bd01-5440eec05887 | -2.93131 | -50.42733 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| dedd24d0-1fd8-36cd-8a91-6d454340356a | -2.70229 | -57.55311 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1dc5846d-4cf6-3c6c-884c-9b32e5a31864 | -7.96046 | -43.98778 | 2026-09-14 04:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c495f3e9-0a5f-34ae-8982-e9167578bd3e | -7.07676 | -43.55335 | 2026-09-14 04:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73a95f22-4d70-3def-8441-240ef682f2d4 | -5.29096 | -45.26623 | 2026-09-14 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d09ee54-b177-3273-a69a-e3ffcf04d57a | -7.77542 | -46.66836 | 2026-09-14 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 476ffac3-d7fb-3df9-80ea-108366e6530a | -9.36726 | -50.16602 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f1173c1-339f-3b2d-8c3d-cae165359d66 | -2.92738 | -50.40733 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f4abead-7453-3295-955f-daf656cdcfb6 | -6.23663 | -51.68129 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67a4efa5-eeb0-36b0-98ac-83a38afdc350 | -8.53865 | -54.69704 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 582c899e-b065-3cb9-82d7-d52bba50a9c9 | -4.08071 | -48.95129 | 2026-09-14 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c4bd9ce-a608-3339-8c76-e6e4d33da21e | -4.3499 | -48.96538 | 2026-09-14 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 76981e38-fda4-3b8f-aae2-333ba1c3ea10 | -3.86625 | -51.97478 | 2026-09-14 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 744e8335-2ce3-3ca7-8d02-cb18169b99a9 | -2.87621 | -50.42726 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7d54e4d-7735-31c7-a486-64b6006971e0 | -2.88747 | -50.44276 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4be8191c-8e5a-34a8-84e3-5c33db0792f3 | -7.53622 | -44.89499 | 2026-09-14 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb19fced-4ddd-37aa-ba1a-eecd81c46777 | -2.88069 | -50.428 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d6805d5d-aeee-3bdd-a2e0-f13102d6cdf0 | -4.38325 | -55.20061 | 2026-09-14 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6a54ec4-e248-3140-ae96-1d7a39106248 | -2.90648 | -50.47671 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91532121-9219-30a6-bff8-38a7a65983cc | -9.48649 | -45.46133 | 2026-09-14 04:32:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8797f8eb-d85b-3d71-aa4a-3e4898f9462d | -6.29574 | -55.28326 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65d39c42-61d8-3fe2-b26c-38a22fec488d | -6.53587 | -42.24068 | 2026-09-14 04:32:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 13efe011-e390-35b8-b5ef-a50682906061 | -6.87035 | -55.29168 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9acd76b-c54e-38d5-837b-e6d1fb20723c | -9.54194 | -45.43437 | 2026-09-14 04:32:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94c80e7f-9100-3466-9284-0498e27ba6de | -6.07019 | -57.86665 | 2026-09-14 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9de4f4e-8ef5-34d8-8875-edbd707e2d57 | -8.54215 | -54.70839 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a90b744-e691-39f0-88f6-89b43692fa2d | -2.92367 | -50.42937 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 7ef368a8-45f8-3ccf-b3f4-cf596892571d | -2.912 | -50.43325 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1144.8 |
| faf71075-8aab-3224-b6ab-ce5863f86ba2 | -5.07469 | -56.25288 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e82abaf-8ffc-36fb-90c3-e4374b8a2551 | -3.22803 | -50.58928 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e62f9ec-ee62-331e-8a53-c4ec037800bf | -6.74305 | -50.92394 | 2026-09-14 04:32:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1cbf537-89d2-3807-8af1-857fa93c844e | -8.54125 | -54.70815 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de1f591f-75d0-3baa-bc1d-c56015044f40 | -4.24687 | -48.64814 | 2026-09-14 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b12e59ce-1656-3485-ab93-b23e6e40bca4 | -2.89107 | -50.42066 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| c374009b-9fa9-392c-8279-005fdfdf087c | -8.12227 | -54.80627 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48e2b09e-07a8-3732-b065-c1dc4ea8790f | -3.86532 | -51.98026 | 2026-09-14 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d52a6a6f-b662-3c29-b877-6c57cb32125a | -8.53392 | -54.71763 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45d67275-f862-3b83-8de0-ba3737fad58f | -3.0461 | -51.26865 | 2026-09-14 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fe9181f-9cd9-35ca-9170-b6af41e31e57 | -4.38926 | -55.20166 | 2026-09-14 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55d301b9-12f2-3da0-a335-3db6e8a1bc91 | -2.89035 | -50.42508 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 7ea61271-7ff5-36aa-b5c8-4b32745bcaf6 | -7.78403 | -46.65846 | 2026-09-14 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9fff12f-194d-3f13-823e-b06be001c966 | -2.91697 | -50.44188 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 2f15d9b4-1e96-38bd-a982-8a244d4d6891 | -3.46571 | -47.46721 | 2026-09-14 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24881194-89fc-362f-8e91-6b1b44b7c072 | -2.94083 | -50.43664 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00f89b9f-40d6-34d9-bec1-c21e6a91d601 | -2.914 | -50.45947 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 88946e33-87b6-34cb-a63f-daf3fe0824d7 | -9.12234 | -51.58388 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63ab17a0-5bad-3519-9d31-ca5872405d46 | -8.54062 | -54.71165 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a08452f-b44d-35ea-9f8e-693f86eb1a53 | -2.89322 | -50.40747 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| edd6e636-4da1-3cc0-9e33-d194ea92a7fd | -3.45904 | -47.46183 | 2026-09-14 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cca6360f-ca7d-3f7c-8716-7b48a4f6d70f | -3.86276 | -51.98378 | 2026-09-14 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df263219-86f4-3aeb-95c6-6607846fbf15 | -6.29521 | -55.27747 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6651bf8b-c664-37eb-98cd-7a4efda18694 | -6.10307 | -55.66687 | 2026-09-14 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88162562-2046-3ba6-86ef-2439ea3f2b38 | -9.43849 | -50.13113 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| b51469f9-2255-3695-a679-93a1c80e1610 | -2.9184 | -50.39349 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 14b1adb1-4458-3516-8cbb-8a8f827cd152 | -3.78219 | -51.34528 | 2026-09-14 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e71722ac-8fbb-3d6d-a8cb-7f1dd753f916 | -9.3325 | -44.3724 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f784bbd-4c5d-309f-9ee1-ab961510382a | -9.36863 | -50.13464 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76491952-c479-3477-aee2-e9848bde4ce0 | -2.89268 | -50.43904 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 31b15df7-b108-3580-bed2-e604fa8e0897 | -3.75413 | -51.15295 | 2026-09-14 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4e5832b-586b-33d9-9ba8-084670ccf2f3 | -6.17728 | -43.34567 | 2026-09-14 04:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 57b9ae46-c253-3f42-a40d-c1f782231edc | -6.29129 | -55.27422 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fc77d2f-65ee-3fe9-b3ce-228a356b48b4 | -7.11685 | -41.79277 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f7fa8c6e-bad4-3391-9602-160c57b07740 | -5.89649 | -42.68612 | 2026-09-14 04:32:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 168df1c9-f975-36c5-8859-ddda4eba5dcf | -2.91109 | -50.41037 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 4aa6507e-d6a4-3dfc-bf25-139c48eaf6da | -6.29221 | -55.29385 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e562672-e4af-377e-8f93-7c38974e2703 | -7.09902 | -55.63453 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a60c9eb-c236-3898-ba0e-0af746e84e94 | -2.9527 | -50.4205 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e00356d8-fe8c-3a4a-8e77-cf9420c66410 | -6.32318 | -44.17903 | 2026-09-14 04:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb89c434-2f96-3080-90f5-0fe7f0697978 | -6.33458 | -43.36237 | 2026-09-14 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8c46c6a8-63c6-3f35-903e-4589adc1786e | -2.92661 | -50.39939 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b0527d3-a1f3-33e1-bb2b-e1e4dd806f44 | -2.70656 | -57.5499 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 147b4682-cdf8-30a0-9413-bd01c9f91cc6 | -8.4909 | -44.5704 | 2026-09-14 04:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa472d02-d1c8-3f4a-bee7-9b568bb008fb | -4.42832 | -41.44888 | 2026-09-14 04:32:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c4bf646e-dfd7-3deb-8531-61c65ffa9b92 | -7.47659 | -42.11953 | 2026-09-14 04:32:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6f858ed1-2b19-36df-930f-298f7ebacd57 | -2.95125 | -50.42928 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2bb3cde-3b5c-381e-9eb3-641aaa963bdb | -5.76156 | -44.05461 | 2026-09-14 04:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6378648d-bfdc-3d1e-a4ec-b06da5877c0c | -8.33742 | -50.75819 | 2026-09-14 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README26.md)
