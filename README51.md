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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f614a707-72dd-31bf-bd93-db599263f2ad | -2.57465 | -54.06181 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd58fd67-7388-3f61-b4d3-8c7d0de8eb37 | -2.1859 | -53.78192 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d05c778b-792c-38e7-b2fa-89e0c448fb94 | -3.70919 | -47.12574 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5c05db2-aa42-309b-844b-b56cd8a12c82 | -3.84336 | -49.90178 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 779026e9-4446-3b10-98a0-ba4b26a3ee47 | -3.54008 | -49.88663 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76760967-4eef-353c-a2a9-3214c6796adf | -3.08535 | -47.81781 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3747492a-43e2-37ee-abb9-8691b07399a4 | -2.70516 | -51.69242 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e51584b4-1bd8-3075-9336-ce2f2d33d474 | -2.71829 | -48.6686 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed9c10db-807d-380a-aac0-cd78677e1605 | -3.08234 | -53.26485 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8121ce17-374d-3870-b676-325fd1886f89 | -4.37717 | -48.50055 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8263208c-ac69-3e6f-91f0-33593aa61b09 | -4.01899 | -47.65405 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db8647ba-4e0c-3a63-8b2b-63a32322cf2f | -5.7228 | -46.16481 | 2024-11-27 04:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 42b72923-55d0-3f88-8bf0-c38a26df0fe8 | -3.83087 | -46.09016 | 2024-11-27 04:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05b3bd00-d3a7-3a4e-9e24-d7d2741e5084 | -3.09962 | -53.2718 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 137dc55a-5a6e-3455-ac6a-ff3a4e9f28b9 | -5.50156 | -47.16596 | 2024-11-27 04:42:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8354d1f1-0ff3-3165-98c6-f47ec1a0eb88 | -2.8004 | -48.68438 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bed62a61-ba52-35ae-9577-33181f0521bc | -2.42866 | -48.547 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25ffe7e4-dff0-3779-b19e-13d449e48ce6 | -4.20726 | -50.89402 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2134254e-7a7b-372f-98c8-91cf9aae95b9 | -0.99225 | -51.72887 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45c5a120-e664-3125-b558-ea4d9bbb37f5 | -1.58115 | -52.23477 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5bdd34f-f531-3e5a-974a-375a6d822126 | -3.11464 | -53.26995 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd6e4b64-f408-3261-bfac-18bd5574907b | -3.08608 | -54.13443 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5b1e73a-6617-3bad-b23a-b493ec91c54c | -3.09018 | -53.26185 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7a53fe02-6389-3c96-baf4-22194f4a613f | -3.34039 | -51.24215 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16fdc3ee-9a8a-3c8e-83d1-53eecb33dacb | -3.40417 | -53.19984 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c25c8baa-8138-326f-8f11-757e06812502 | -3.33762 | -53.21045 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ce39842-0773-34ad-bb9f-7d01062a1c76 | -2.17145 | -53.27117 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b397661-cfe6-39ec-88d4-1edb6b370d4b | -5.98891 | -45.36045 | 2024-11-27 04:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 45c9aa54-6636-34fc-8768-ea46866a3ca4 | -1.97087 | -48.42945 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5b1f380-4ae9-36fb-a83e-0096faca1085 | -1.77983 | -52.73715 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6d74ebb-000c-3976-8505-7f5274ce9fa4 | -3.31748 | -53.29098 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afe1c4e7-400d-390d-ac86-3689fe54989f | -3.09669 | -53.26712 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14d9935d-1ccc-3cf9-baab-317194654614 | -1.24617 | -51.63117 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf71ce60-e959-3fd2-a77a-3f1ef4b3c64a | -3.21984 | -53.62193 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 936679d1-65f9-345b-afef-b09d4aacdb7b | -3.4951 | -49.95731 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de0b329f-5d57-3aa2-8ed8-6c2f813a8515 | -3.10061 | -53.24257 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6d013c7-2cd2-3f66-8e84-36f5e4579716 | -2.8072 | -52.46687 | 2024-11-27 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3e06dc4-0eba-35f8-abd3-f3b00959c633 | -1.66745 | -52.25233 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8afc311f-dce5-39c1-be89-7f9721ecdee7 | -3.53602 | -50.82014 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8358aeb-5400-3951-a77a-b286cb57d279 | -3.23569 | -50.67756 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f403a35d-a7f2-3acb-9776-3d316f88b581 | -3.84933 | -46.50716 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4229424f-9825-3703-87f3-3d061de7ba86 | -4.15598 | -43.82253 | 2024-11-27 04:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d2c3077-f8a2-32e0-bf19-692d6bca3119 | -4.06282 | -48.33473 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b666b30-2d98-3715-9654-202f936e4fd7 | -3.0461 | -53.72591 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61d400d9-432f-3f47-af88-abb1c4c1e837 | -4.18088 | -53.53373 | 2024-11-27 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8b8c66e-c396-3f52-9101-c5fb323d2099 | -4.29077 | -48.21809 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47ecfbad-0f82-3552-9511-33070ee84fb5 | -3.28149 | -51.11824 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fe86d9c-e93b-3aa7-a73b-22d8942fe077 | -2.59694 | -54.21159 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4b81bb7b-6f39-3568-9062-80e7507befb3 | -2.3672 | -50.43186 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf7224de-62ee-3b8e-ab1a-8d54c435ed4a | -2.02063 | -51.18713 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 839c507b-1743-3416-bf3d-67f765aeac06 | -1.66313 | -52.64994 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a63e72bd-fff3-38a2-a66a-7c8a2ccc18af | -2.82539 | -46.81465 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 907f99bb-bca4-35ad-9dff-cfcac2af7870 | -3.17427 | -48.44088 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4c6bdcff-ecf0-379c-8e4e-b8d6b30cab7f | -0.02554 | -49.63897 | 2024-11-27 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a0a41e5-e1af-32f2-94a5-9e6c0937936e | -4.24799 | -53.51753 | 2024-11-27 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af8a9e1b-1e67-3235-b718-ec9a3b988448 | -0.24887 | -48.64997 | 2024-11-27 04:42:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71c6b4da-185f-39c4-8e40-ee1420587d5a | -1.6659 | -52.42867 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce3623c5-a5b3-3264-b8d3-ad799519835f | -4.23265 | -50.0191 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0482cdb8-a311-317f-8d2b-5e0600818bf0 | -2.57926 | -54.05498 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acfabda3-36a6-38fc-ae42-493340f4645c | -2.79086 | -48.60247 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 18ba3ccd-7c0e-3a16-943a-41d712d9991e | -4.14293 | -43.84806 | 2024-11-27 04:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4a82355-9a1f-3593-b020-c5157cd13ce9 | -4.29019 | -48.22189 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 805bbca8-c6a9-35fe-90f3-45e1598785be | -2.8489 | -46.83118 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3486f83b-122a-32d6-8885-f24a7bb693a9 | -3.47636 | -50.31369 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 918adcf1-6a75-3634-94ef-9550edb803b3 | -1.64175 | -52.44483 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa830bf6-e1f9-3f0e-b7a9-bb7d06f6aab1 | -1.16398 | -52.48677 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b4570b4-1ed4-3ff0-b118-30c14959ddaa | -3.97967 | -46.64721 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 607dae9a-775d-344a-af99-5845f6710048 | -3.81234 | -46.59834 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ef05b11-e65f-3f93-8d58-2c6ac7dfe0bf | -0.90661 | -48.05658 | 2024-11-27 04:42:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5a7b6fcf-f105-3e9a-a46a-decde8ecc66a | -3.50001 | -53.81174 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7514beae-0d79-36e3-bb81-75b538733acd | -3.22998 | -49.43681 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7de3cf6f-a9c6-336c-8a91-f44ce907c0d0 | -3.59024 | -50.38784 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1db03705-350b-35e6-bd6c-c6bd71b2bfba | -3.9645 | -48.08378 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| cc80620b-1ab7-3c5b-92cc-6e961afef89f | -0.02884 | -49.63948 | 2024-11-27 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8548641d-8784-3155-957b-040c6769424a | -3.97495 | -48.0619 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54123589-eb2f-3bcf-93f3-f97eb6b45167 | -3.05588 | -48.70526 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13df12e5-5cb1-3ab5-bb6c-dbc5be5d1240 | 1.95096 | -60.86054 | 2024-11-27 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6839bc19-2c41-36ad-ae74-38c54fa1b7fb | -3.59126 | -50.35983 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6cbfa712-bbe3-3bae-b88f-12e64a383087 | -3.58191 | -41.9597 | 2024-11-27 04:42:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 321fa6bc-46ca-3048-a62b-97691c73e0fd | -1.71685 | -52.49268 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fb896a1-8343-3305-9dd4-9c6f00f63e18 | -3.95897 | -45.55546 | 2024-11-27 04:42:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00aecb2d-12cf-3e09-b4e4-a7a05ce92f08 | -3.30455 | -50.24078 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8c23492-34d3-3730-8da0-f21d606296c1 | -1.27054 | -52.2269 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49919e32-eb7d-313a-a2ee-cb22e36f54ad | -4.65398 | -43.82092 | 2024-11-27 04:42:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 536c0e40-6b53-329e-9470-3c4aec455d1d | -3.09833 | -50.36302 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0f1044b2-8a31-3260-805b-5d4393d0b7d6 | -2.10515 | -46.56313 | 2024-11-27 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34d6a778-93e9-3719-8f36-686b15454068 | -2.72216 | -48.59929 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c68d8e01-f969-37b7-8fb6-a1f00e9e8b4c | -3.03881 | -50.56866 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86554401-65f8-35e3-9315-fe13a79c367b | -2.94085 | -54.79461 | 2024-11-27 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a00ce2fc-86d9-3b4d-805d-0e6765447720 | -3.40459 | -50.98423 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d6980b4-0ac0-326b-ac95-b980bff7c590 | -3.15495 | -49.24349 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 800821b6-8d93-3c28-9602-687a8fe9c17f | -2.81249 | -46.82563 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b206788a-2c35-3e77-9e53-f74768ee9208 | -3.09148 | -53.25368 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 85ed9a8d-0d77-32d1-ab9a-62f32080010f | -3.80099 | -45.22332 | 2024-11-27 04:42:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1bf6448-ad6f-3ea4-b89a-1c054cde6240 | -4.04905 | -48.33263 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a2d2c4d-bd5a-3748-9ced-d2f14e4b2b2e | -2.56118 | -46.42213 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f611357-0612-3cf9-b89b-34dcebf1330f | -2.42285 | -44.64917 | 2024-11-27 04:42:00 | NOAA-20 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77bbfb67-6281-3d3a-9acb-edc8a5ce5973 | -3.03869 | -51.77751 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0882ae9b-e4ea-3a44-b205-ea6abd1ceb7f | -4.32581 | -48.58382 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d848630-a2c3-3793-a623-237a6e56e121 | -5.43066 | -48.47839 | 2024-11-27 04:42:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README52.md)
