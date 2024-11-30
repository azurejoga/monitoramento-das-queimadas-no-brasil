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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eea665da-0d21-359f-a976-8e33654725bb | -2.87603 | -50.73677 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 998305b3-c52a-3b78-98e2-0affffd79427 | -2.61988 | -46.79566 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 809d3fcc-4357-346f-85a9-bcaa03e32049 | -2.7217 | -48.62383 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1945dd0c-82dc-3a2c-aae3-c75b6be1e4ff | -1.34987 | -51.97933 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09fffe83-1598-3a4b-babc-4a569bddc7c6 | -3.27382 | -54.70086 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7012e7b-8c3d-311f-9656-099bd12db731 | -1.14247 | -53.78162 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67a11027-ba12-3680-a2bc-b24e678fa132 | -3.46712 | -50.52999 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b952c543-0dc8-36df-8e48-c3fd9d361f09 | -3.98487 | -47.73286 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb75b204-7862-3df5-845a-8fcd5832b426 | -2.59895 | -53.9895 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 811f4fc7-74ad-3138-8869-3c0d470ff79e | -2.37338 | -50.43094 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1d4e842-cb9f-3019-9556-f327c464df7e | -3.61406 | -54.74203 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6af19c7-2ee8-326f-afb0-016139b24f92 | -3.49162 | -53.81616 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1610667a-d37c-3e55-b3b9-92b0675eee6b | -2.95478 | -51.6984 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b0aa6eb-69ad-396d-b19a-2e6bc9386bad | -2.85652 | -46.69275 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34ef0234-a5f5-3ff9-af92-84ce573b81bd | -5.74607 | -46.17794 | 2024-11-30 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7339b466-9be2-371d-bb97-d0d56ebb00d8 | -5.98828 | -39.95544 | 2024-11-30 04:40:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8a7b2543-74b4-3e21-8b70-98f99285ee68 | -3.57244 | -46.34301 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 070300aa-c651-332e-aa4b-d71cbd200dbc | -3.60662 | -54.21331 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0220ff0-6329-3c81-9d77-b3e28f52afd7 | -1.14461 | -48.33145 | 2024-11-30 04:40:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 420e15c6-eac6-3eba-b027-d582c0eb457d | -2.37839 | -47.88025 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cd481dc-1ad6-34c5-b853-7a801fd70636 | -2.62427 | -54.2179 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce04759b-c812-3a3e-8561-b1f500e5ad4f | -3.33623 | -46.60766 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36b7d304-9b26-394f-b77a-dfe847a83807 | -3.246 | -50.59529 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 605beb2f-0c74-3290-947d-8d647b3bed74 | -2.58424 | -48.19632 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a8b3be8-edb4-37d6-9eef-ba169a83b0fa | -3.38463 | -53.51032 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52c994d4-0fe9-350e-aa35-e019b9cc63b8 | -2.03649 | -51.2028 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33b4afbe-f5c4-338b-8637-7895e02bfbbd | -3.7963 | -58.97305 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0e644f3-bade-395c-9a6f-f0012cfb993d | -1.61802 | -53.88559 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75e3c61d-460c-3780-b6d6-8376fcdf0be6 | -3.42151 | -50.70822 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e694be98-ebb0-3414-94d7-d2c1dac47ea0 | -1.69161 | -52.43005 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbedff35-7347-35e5-9930-8c0522e181a4 | -4.25188 | -45.51247 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3068e0c-a2d0-3652-b06f-743f4a7fc0b1 | -4.04719 | -46.86447 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fd2b830-7fc5-32bf-97ad-e1e579acd9c3 | -2.18642 | -47.14706 | 2024-11-30 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dad85faa-63bb-30c2-9508-7ce5c8d2c072 | -1.71928 | -55.07991 | 2024-11-30 04:40:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85ed3cf1-c2a1-3e92-bbec-1b571966eddb | -4.08498 | -47.02821 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03cdac33-7e10-3fc7-9960-3e6e26ce434a | -2.68085 | -46.27803 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b706859f-939c-3e92-a728-55c379d386a5 | -1.58989 | -52.28811 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d39902fe-3bfc-30d0-bbc3-9531401c1736 | -2.90666 | -54.1793 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0d594fe-5293-340d-b514-690e5e08acf9 | -4.1255 | -48.84688 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e154d1cb-821c-33aa-988d-a35121ad087a | -0.81064 | -51.61744 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 614e8a9e-4a47-3a80-b654-bae85900d389 | -1.09449 | -53.39575 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad2ccb42-3e07-3fd2-9e3c-458e8b7ec2ee | -2.89096 | -55.22847 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a789c240-9b2f-369e-baa3-e23155611665 | -1.25506 | -51.74556 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3ec928a-92c8-3f49-84e1-b3d037728e63 | -1.49558 | -48.02345 | 2024-11-30 04:40:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0810b49a-2499-37eb-9d83-433255e87342 | -3.41367 | -50.24409 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cee9814f-4fd8-33aa-b048-7b9c4bd1b369 | -2.21226 | -48.37863 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37d22e83-d8f3-3c64-ae25-38e865616b00 | -2.65672 | -46.53106 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6c66089-72b8-3817-96c4-e5f20b988f3e | -7.22283 | -39.04863 | 2024-11-30 04:40:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e01f829e-071a-38a0-9459-e3ca0fad02b5 | -2.42816 | -48.17234 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12c82627-8313-32ea-9db3-ab02b776efc3 | -3.14261 | -53.83293 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89c656a8-397f-3a89-9f34-d0d1bb48c92b | -3.65625 | -50.15141 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e9e24b8-799f-3ed9-afe3-2405b706454a | -1.75516 | -48.76068 | 2024-11-30 04:40:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b11d5946-2a24-3f4e-b4a5-3eb5dcd179be | -2.16031 | -50.59992 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 105e67f8-dcd7-3880-85e6-141e528b5bfc | -3.96641 | -49.90993 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f19d5e0f-d7e7-3001-ae17-db541875f6ef | -1.93508 | -48.54323 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29c0cb78-cf5a-3a81-b985-dceb706fe90e | -1.32022 | -54.63586 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46b29d28-b445-3918-9be3-dcb1ba1b1ab9 | -5.5224 | -45.40781 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db14eb27-b8b0-38ca-b642-c84be51bfc85 | -1.68841 | -46.78457 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a812f3c1-6830-37e0-9186-1dbe45775166 | -3.5345 | -50.19028 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 676e83bc-d219-3b1f-92a6-a95fce67fa22 | -2.59546 | -53.98529 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2d18c46f-53d3-3c07-b69a-463891e94298 | -2.67057 | -46.55656 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 651a4bf3-626e-34f6-8ce3-b33362ce934c | -1.66827 | -52.40815 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 37e37055-83fa-395e-92ae-9458840c16b2 | -3.77939 | -46.69253 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5230d82-33a4-3a6a-81fc-243507b62763 | -2.01603 | -46.50234 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37250e3f-3929-34f1-bfc6-f7c388cb6460 | -1.00792 | -51.72222 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f748d3a-011a-33da-be56-d016d3a10b4f | -1.37026 | -51.96868 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3d0ce401-7359-318a-9166-99050c0dbbec | -2.55102 | -46.55849 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af2b738d-1d9f-37e2-b2f8-f20d9d452919 | -1.771 | -55.67693 | 2024-11-30 04:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 898f3131-5159-31ed-a804-8954b43e5cca | -6.92971 | -45.20966 | 2024-11-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72197267-d474-3896-848c-31d2ed8db67f | -3.7137 | -51.85258 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9de43e2-a8f1-328c-8c9f-595958be28e4 | -2.53634 | -50.0889 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49ff2dfe-7fa6-33a7-97ce-d5f95eca1f9f | -3.69468 | -50.16821 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60ea4d6d-1a32-36f1-bcfd-058aefe91e80 | -3.97574 | -46.71346 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c1821e4-7894-3d9c-b5a8-a2fc350ef648 | -3.71023 | -47.14088 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4132851-2ce4-3c44-bfa4-0df9b35f2a6e | -3.05789 | -48.51789 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a97179e3-5876-325c-925e-5604e851f714 | -2.46539 | -50.22023 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59bcbeab-9d18-362f-87e8-a297c397ae5d | -2.08703 | -48.5491 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46fbe9ff-cf43-387a-afb9-51c6eb885370 | -0.9076 | -52.40848 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a9c5d0e4-7054-3d1c-a4e0-277aa33612e7 | -2.79794 | -51.00991 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf022acb-19bc-3f33-b37c-fbb348ac5e10 | -2.12831 | -46.40994 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d13f9598-5d0b-3d4a-8118-28566e4f2c95 | -4.51491 | -48.06911 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bae958cb-0db2-3e3d-8881-1eb59487a784 | -3.11994 | -49.49323 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5eca33c-627e-37d0-838c-7db91eee487c | -2.32985 | -54.50108 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 69c489dc-2952-3eb3-b3b7-cbfe6354f0d6 | -1.26084 | -54.5492 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b52f780-61d6-3571-80e0-699f17353cc8 | -2.37855 | -50.39836 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c3a8274-22dd-3e3d-8af1-fb25300931d3 | -3.46935 | -50.53771 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6e9c57c-91fd-380f-8ab9-b4689624bca2 | -2.0406 | -51.19947 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 31c4eb36-fc4a-3814-bbb4-0a42338ae950 | -3.55833 | -46.34083 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f068a10-e286-31ac-8844-6a4685375226 | -3.09332 | -50.35814 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1c2699f-29dc-3479-978a-5ea1e47f9417 | -6.08261 | -48.04455 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f03efce4-9261-3389-980b-10b0cb9e404c | -2.53681 | -54.03953 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3493ce67-3589-3b5f-866c-0e98c4733801 | -2.79453 | -45.22799 | 2024-11-30 04:40:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 480fb98b-1fbe-3d22-9f1a-d1ef776676db | -3.05572 | -51.06451 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4dc2d9c7-dc88-3e27-baea-4bc0607b23a4 | -3.20277 | -51.41856 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ab50d68-d580-33e1-9ecf-ec8ee3acd213 | -3.2553 | -53.63676 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 58b9a1f4-969d-330a-9a6b-be37af0d69aa | -1.7242 | -52.47455 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5efebca9-1f27-3f38-8887-82b48520d853 | -1.31644 | -51.74086 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04bd4328-296a-3aa6-9812-dcd65b262ba7 | -3.34666 | -50.24041 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50c8caf2-d572-3efd-b9ff-f7367516653f | -3.79935 | -45.85553 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40800f19-e648-316e-8d45-20d312c02e33 | -3.79075 | -58.98046 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README49.md)
