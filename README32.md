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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 223973e3-db89-3490-aef4-ccc35c63f67a | -2.22977 | -48.37157 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 586831d7-8927-3048-8c75-069247356d2d | -2.30109 | -46.74124 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca307452-cc88-3f96-95f5-9d5dbc815beb | -0.39307 | -51.94609 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 40a0bc28-1642-3f71-ae9a-c763add529f1 | 2.46655 | -50.96181 | 2024-11-09 04:31:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 760fefce-1417-3926-b90f-64557aec2817 | -1.87078 | -51.49381 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3d2a8f7-2c31-356a-9557-2d2b08152104 | -2.28344 | -46.85452 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15a8487f-5a32-30ac-b0e5-89a59d25a601 | -2.60479 | -48.1949 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f942cd9-9fbc-3c52-933f-1fcdf60b605c | -2.12795 | -46.36814 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e756f5e-20d9-3b68-8b5a-073f61d9bbde | -2.201 | -49.28881 | 2024-11-09 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d2f6ecb-2812-3973-80ed-3b7729a48ae7 | -2.13752 | -46.78914 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4efb788-378b-3e22-8d14-1e3a201425fd | -2.29245 | -49.11049 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 445c8d32-03f3-36ac-ab9e-ac7d52c2152d | -1.64295 | -46.11862 | 2024-11-09 04:31:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94f80a12-1879-3fda-b255-686f7e84add7 | -2.20495 | -51.94458 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ffd6b57-5bf6-3f69-bfea-438ee71cb44e | -2.14701 | -48.78624 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3bfcb53-c9aa-34c2-a84c-04bea6ba0534 | -2.1258 | -48.56063 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44c13fac-ee8b-3fa5-9886-8c50c5d32734 | -2.70366 | -46.69125 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7a108bb-ec8b-3c63-844b-77a04b230643 | -2.40418 | -48.49382 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edec998a-811c-3c76-990a-4041bd3e28be | -2.6577 | -48.50714 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bae0c7f-f842-3127-9fb6-b9e8c9ebf0a5 | 2.1005 | -50.85189 | 2024-11-09 04:31:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ed47b59-3abc-36ae-8b8b-d51871517bc0 | -2.2358 | -46.61426 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfc770f1-efee-3c82-8984-f98628ed3386 | -2.52978 | -46.2991 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aef712a0-5c94-3120-8aba-13048a3fe8c6 | -2.45772 | -49.84309 | 2024-11-09 04:31:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fd00f19-8f5f-320a-87a4-30972cf9c9a3 | -1.52322 | -52.21244 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61dde4df-4706-3ea8-8ac0-ef2c85d32ee3 | -2.53535 | -46.30705 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcb990aa-a757-3a61-be58-e913a4fc9ced | -2.17199 | -50.53718 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87a496f9-6be6-3893-8fac-91b319730d7a | -2.71146 | -47.73039 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a9e07a6-70db-381a-8a10-340be1ff352b | -2.51797 | -46.37546 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a705731d-6d9b-3fb9-a73b-03acbcec304b | -2.37918 | -46.59119 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84385a63-83f5-3761-a5a6-97ad8ffe5f3e | -2.23756 | -48.23498 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63bdc196-9d7f-3d4b-b01d-8686077b2fa6 | -1.18742 | -51.98888 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8ef95584-910a-3c1b-be85-98dd14fc1276 | -2.33781 | -46.57079 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5bfde23-31cb-3306-8cb2-2bd106bc3399 | -2.58585 | -48.16323 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63b64b8b-39c0-3851-8718-fb21c2082544 | -1.68326 | -48.47393 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98e87706-ca3f-3832-b455-7f0995811684 | -2.29993 | -46.72699 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83bb4290-ce1a-3521-9b04-2369109f270f | -2.37684 | -49.82728 | 2024-11-09 04:31:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd7d025c-6052-3d0f-976e-36ce52b35c2b | -2.09418 | -46.34526 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2795abd8-eb4c-3861-86e2-c8904b37e938 | -0.3036 | -51.71862 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34069439-1cf3-3079-842c-88a447276573 | -2.45713 | -50.39446 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b55e1ff-75c8-3912-8249-c5b2888bc3b1 | -2.0914 | -46.34129 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fb43fc8-6c35-3ee1-95c7-90761b2bed1c | -2.41255 | -48.52805 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c0832d8-14f5-389d-b7ea-d665479e5f9f | -2.19601 | -48.96294 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ff9df73-40cb-337f-a97a-802ea85eebda | -0.36522 | -51.64117 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6504489d-abbe-3a4b-ba66-11f05269e4d8 | -1.699 | -48.15513 | 2024-11-09 04:31:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a052433b-2684-3044-9ef0-de68d2520ade | -2.23313 | -48.37208 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 06fcfbb6-b249-3bf4-843e-1f71a0e75b28 | -2.57862 | -49.14286 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ba936350-54f2-3193-b0df-ad0ad86d8e69 | -2.70196 | -46.68041 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebead785-35c9-3d77-9318-9b3d436cc917 | -2.23872 | -48.38022 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a06e6da-4a5b-3d5c-ad3b-2419f6dfc81c | -3.09013 | -46.5461 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1893f8d3-f5e6-3d33-9621-432b963960dc | -2.31375 | -46.48586 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bca80928-e3ef-3610-bdb8-d29cab9982b5 | -2.51713 | -46.31493 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f2b16ef-b13b-3d11-9cb8-ccc93b3514ba | -2.5542 | -46.18512 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e408ad4-a00d-3faf-a6f8-cd555bf0b462 | -1.64315 | -52.2723 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af807faa-dd96-352e-b97c-e65db78b4663 | -2.24291 | -51.65856 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 152ec20d-ce73-3740-a05c-dcca41263f04 | -1.15126 | -53.65987 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b1889939-780b-3a4e-9084-b9269304d401 | -1.70516 | -51.93196 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 714235c3-4cfe-3efe-ab65-67b409784530 | -2.09226 | -46.53225 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4351b55d-513c-32af-85fe-0688253d2dd0 | -1.82906 | -53.71562 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c5047aa-9aaa-3859-88c3-4dee10370562 | -2.6299 | -46.77077 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 480eb3fc-363a-3507-840b-560559649036 | -2.8389 | -46.6308 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ab16e00-9bd9-32c8-a4d0-686044c08667 | -2.3964 | -46.50206 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0319ed42-501e-3c9c-8830-294a74074fdb | -1.77997 | -52.35105 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb015525-c6c9-38c3-82a9-920ea84a1667 | -2.05159 | -50.72421 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f520c67c-c8dc-333a-99e9-81a2a2800530 | -2.53813 | -46.31105 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 130e078a-4cca-3b5d-971a-edf208931a2d | -2.41312 | -48.52448 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 844ee569-c73a-3ea6-805b-48cdc5c3588c | -2.4177 | -48.93694 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4be31ee-c834-3834-b6db-a2b65685d9f6 | -2.22626 | -46.43632 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8796e7b4-e07a-3769-8f96-5734a0399c6f | -2.21739 | -46.81898 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a68b8a52-b338-351d-8f1f-b46236f727eb | -2.15086 | -48.82798 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5339ba81-a8bb-3522-98d3-7fb4b2685232 | -2.45546 | -47.169 | 2024-11-09 04:31:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 836338e8-4aab-3648-9a3a-6c0897734f98 | -2.37473 | -47.92616 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c02bfe23-f59b-335a-a6ef-061785f3d4b1 | -2.1241 | -46.3711 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebeb49d6-ae00-3450-8d94-6c7aa1277aed | -2.51735 | -47.18914 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fd5baed-e612-32c9-a35c-8aad55441ba7 | -2.58201 | -48.20936 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 091ad941-aefa-3f21-aa72-2d63c7222b31 | 0.1087 | -50.16586 | 2024-11-09 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e444b5b-4583-3f10-b987-4320df01e4ea | -2.65938 | -48.49646 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95c460af-87b4-33e0-bef1-f270035b6454 | -1.21872 | -51.75839 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 210f1d89-49a6-3a2a-88bd-7adf15716630 | -2.20475 | -49.13136 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10dc0792-c613-31a1-a519-3747e5213572 | -2.34522 | -46.63184 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6d093a0-83ef-3793-bc53-b4c1c526116c | -2.23061 | -46.8464 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78473da2-0981-35e3-8518-f682b8c28906 | -0.8962 | -51.77554 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 264b3e27-aef9-370e-b7ed-079a99f358d1 | -2.67293 | -46.71473 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7851fad-a99f-3a1a-b414-d21c9450a7fb | -1.67856 | -48.72581 | 2024-11-09 04:31:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 640d37fc-9d7e-31b8-83f2-cfa76980f979 | -2.46076 | -50.39503 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f172617-cadd-3f82-9032-7b2380f6bff3 | -2.27841 | -46.71313 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d27eea67-0d9f-3a96-9f19-88f0bd698984 | -1.39594 | -52.0689 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 902149e6-0a64-31b6-974a-b88e5f71b8c8 | -0.90595 | -51.76625 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdedd8ea-fa07-3886-b890-0ca1abfc26e5 | -2.67617 | -48.49907 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4efa0548-037b-31f9-add6-d30c88f98d1b | -1.69538 | -46.24091 | 2024-11-09 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da2c00e4-970d-3a85-9dd5-9584f2534150 | -2.60534 | -48.19139 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d887964-9b5c-3d9a-ae1d-2c40e16e045d | -2.70357 | -46.67006 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e026c38-acf6-3566-8cc7-5f2aa998550e | -2.16286 | -48.50017 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 838fd180-3149-3f5f-b268-c1d612206d2b | -2.21802 | -49.56636 | 2024-11-09 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e723dd9-d7b3-39d2-9bc7-d5b9cfb87521 | -2.30414 | -48.54741 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f6084e7-e885-3336-bc8a-67298e0c0947 | -2.2109 | -50.34103 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 722cf5f2-6f6f-3029-ae7d-400320807e37 | -2.13543 | -46.69389 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 818e8d48-6e90-3715-8c28-225b78a15ec2 | -2.56364 | -46.19016 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0a34bac-e5a6-376a-bd78-1fb734a512ed | -2.2317 | -46.55372 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14cebc89-c48d-3d6d-8874-594d81b4e2be | -2.28751 | -48.74061 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9a33593-72cb-37f2-819f-4c4ceb4231dc | -2.58096 | -49.12796 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 997ba72b-cd4d-334a-8f1c-08262708829f | -2.66274 | -48.49698 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README33.md)
