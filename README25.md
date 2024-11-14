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
| af180d88-f033-308d-838a-aab485716ad4 | -1.39875 | -51.12566 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 56244904-fd42-31f5-a169-9654c348e946 | -2.89091 | -51.68747 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3132a1a8-8467-3f81-bc55-7c23be972479 | -3.21038 | -46.53003 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9993f32d-dc17-3df1-bd87-dc6bf2fecccc | -4.14439 | -43.84684 | 2024-11-14 04:40:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc39d2ed-e913-33fd-be74-b9ecc33cfb77 | -4.27413 | -48.19518 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 463ad715-d75f-3460-912b-3d2cd8f81342 | -4.58567 | -46.62719 | 2024-11-14 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f12d80c-8bcd-3d0a-ac40-6efadcafe27a | -5.33459 | -45.10642 | 2024-11-14 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d0662e5-2cec-335a-9ec5-a0a20d4cb59f | -4.22706 | -46.87454 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31c24f10-83b5-3ddf-8011-a44579c4dd89 | -2.66687 | -46.80551 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57bd7727-e44a-3a7d-b864-a0104e2dc1a3 | -2.83327 | -51.93649 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88c1abd3-ff7d-318c-a838-e681a0d7f51b | -2.94229 | -48.31953 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0954bb67-b9a9-3ec0-9c04-2e13718b0c8f | -4.40218 | -47.26963 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10abb632-438b-3dd0-b50b-cff2f46f668c | -2.70113 | -51.87479 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eccd597f-2a1a-3b3a-8721-57cf372bf1b9 | -5.3801 | -42.77623 | 2024-11-14 04:40:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d8a149dc-3e17-3842-8e35-6486ec3e8337 | -3.71744 | -50.60596 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f7693a73-de93-308a-a70e-e1828959a0d6 | -3.86799 | -43.9436 | 2024-11-14 04:40:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58e31902-b9cf-3a0d-835c-5a2be5f0bd32 | -2.26973 | -45.34557 | 2024-11-14 04:40:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 43b69e23-960f-3d61-9aaf-a31573e42198 | -2.7086 | -45.56508 | 2024-11-14 04:40:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aaeb4d8e-0e72-33e2-af5b-03999fa9e73e | -5.34608 | -45.57211 | 2024-11-14 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49bd8fa9-ea31-3ee9-bf2c-0e37324a7cb8 | -2.66951 | -46.9912 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3cfe566d-7b4e-3725-b3f9-814f0c8389b0 | -3.05494 | -48.01009 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b0be5f9-afb4-3c87-b9ad-8d1c81025fd6 | -2.11565 | -50.85716 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbfb5e7b-0d5c-36f5-8560-2e563e044e28 | -2.37918 | -48.52758 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e5220ce-97d0-3ec4-b809-e6fb81eb4218 | -2.22637 | -51.37312 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b193485-912c-3d40-82e7-bab0bb050c6b | -2.37532 | -47.94044 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff1e748a-7db9-3065-a081-f6876a8de9e8 | -2.29003 | -46.56594 | 2024-11-14 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37da6ec7-7167-3043-950a-d4514fe86924 | -1.63946 | -53.2709 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 85d38a03-ca4e-3c35-a896-b3b13e01afc6 | -2.65944 | -46.83089 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66fa3f90-a9f5-3a4c-bc3b-1a620aa9785f | -4.0533 | -47.2328 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b188003-49cb-32ca-8de8-737885e06814 | -7.68127 | -49.1171 | 2024-11-14 04:40:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef155f6b-2e0a-3d55-8e2b-474fd9040ba5 | -2.19355 | -48.36518 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00261dcf-0cd6-3393-acde-050008775d45 | -2.67713 | -46.82986 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec77114c-9cd6-3647-9dce-98e29ff34168 | -1.97448 | -47.87131 | 2024-11-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31cab6c8-e326-378b-bbf2-7fb4c674b6a0 | -1.67083 | -52.55796 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 74ad8ba2-3143-37d4-8e7f-4a05470dd27b | -1.38454 | -51.56112 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a545d00-621e-3779-ab23-6d85ddd121d5 | -2.52281 | -46.12008 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae86bbe8-0df9-3f19-b2f6-f6a24fd681c5 | -4.35546 | -49.6832 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6b188cbc-6913-3c61-90de-87fb854789ec | -5.50383 | -47.17066 | 2024-11-14 04:40:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5e59824-3a6f-3ce1-8c24-f6a46565e81b | -2.90345 | -46.86381 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2c75d680-19de-314e-a3cb-f4d4e1a97ea2 | -5.47686 | -47.00661 | 2024-11-14 04:40:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6aa493a7-815e-3219-90da-cd76cb8240b6 | -1.96392 | -51.54233 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db879997-8653-333c-aaa5-20b55045efce | -3.7361 | -50.4433 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cb9c53e4-719c-3a7f-abc4-4b99a8360977 | -1.61936 | -52.51736 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dff0c4cc-94d4-355e-add4-13fa59cac0f2 | -1.59889 | -46.99967 | 2024-11-14 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fdf5dac-df7e-396d-a047-ce397d4e992f | -2.11883 | -50.68161 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13a51bb6-ffa9-3b0c-aa70-d02c99e8fe51 | -2.63911 | -46.16497 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47145586-4d15-3547-86a5-b518c2fa77d7 | -4.84799 | -45.56839 | 2024-11-14 04:40:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cde5be04-3467-38e5-a8c0-c30664f8ac88 | -1.13298 | -51.68456 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16de3220-1b34-38af-80ce-45485d489490 | -2.15241 | -50.71343 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 092e2841-49d8-34de-91c0-e58ebacccb8d | -3.60945 | -48.90662 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71550099-2949-3128-9c37-93a383ca095c | -5.6116 | -46.40149 | 2024-11-14 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a85f31d-2b3e-3228-a2ef-3bda9b4b1561 | -2.85433 | -46.65687 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b486924-33e0-3811-ba0d-f4f9f256484c | -1.40763 | -51.11503 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6092a2ea-d763-3c3c-94ed-a02f61bd50fa | -1.64026 | -53.26585 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| fbede051-fcbe-3e53-82d4-4f649c247633 | -1.42978 | -52.24777 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b65e4fe-bc45-3e40-88ad-4da8687b6f3a | -2.84583 | -53.97918 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2627e73f-5484-3c3a-b270-05d7b6667dbb | -4.17896 | -50.41756 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14179431-bd1f-3a95-b391-b149aa53ce7d | -4.15243 | -45.76924 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd37199f-89fd-3254-a2c1-9a07dbed3948 | -2.83148 | -46.65025 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 448d65b5-4a51-3479-aa55-bcd85230fd0b | -4.11284 | -48.5121 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 427b8c41-ca85-3767-b74d-7400e443e328 | -3.24808 | -46.53975 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9372f123-d854-3aa5-b7a5-1c4915e7922a | -1.60796 | -52.49235 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 023b4f45-aae7-3c44-b4a4-d4ca7f3038da | -3.7333 | -50.43921 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fa4a654-72d4-378c-a928-af5d85e44786 | -4.15607 | -45.7698 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 38c30cf1-bd09-35ae-abca-5317617efa07 | -1.6088 | -52.40667 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e3a7145d-2ba6-3e8f-9f54-72bd0e295f12 | -4.07533 | -49.14472 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 080a36dd-241b-3118-b67b-31f9c721f699 | -2.88217 | -51.78928 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8b34ec2f-d7a4-3ee3-ac8d-5c9932fd9385 | -3.63043 | -48.92392 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 94cb84fd-e79a-3ec8-8555-7daefdc522d9 | -2.63851 | -46.16891 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91777232-2326-359a-b82b-93dcb07da313 | -2.18121 | -48.314 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92b9fa4b-5f4c-30e9-a931-780c85ea2664 | -1.94778 | -52.15297 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56e468a4-d651-3977-9afd-2e86bd4258ff | -2.11113 | -48.10849 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a80abf39-c6b7-3679-88d3-ac33011167e2 | -1.61204 | -52.2389 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09e75a46-7720-384a-8d70-95bf71261ea2 | -2.63659 | -46.81998 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e30223d-7beb-3725-aebe-ff042dd992a2 | -4.37702 | -48.07769 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 96a2f1a6-e5ea-3d6a-93df-b0edb8a7c202 | -2.27338 | -45.34613 | 2024-11-14 04:40:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 43.2 |
| de19e16a-d565-331d-8262-60b41d3412d5 | -2.88091 | -51.79731 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3ebc73c7-e3eb-3056-a459-9b14cea2ed0d | -1.60506 | -52.40609 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afab9e80-1de5-3909-b148-20b7c02401c0 | -4.7584 | -49.08697 | 2024-11-14 04:40:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb4a7262-70af-3ac1-974b-1c80c4de41d8 | -2.60918 | -46.17248 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3a5cb23-bf67-367f-99e7-9a5e692356df | -1.63634 | -53.26513 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9d6e066d-b183-3ebb-8c21-f13244c02634 | -3.27607 | -50.57819 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fec6f29e-e1b9-3a58-a0b9-010a8a9aa001 | -1.40761 | -52.38586 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 453ca7bb-4e8f-3248-bf1b-fe20b0be1021 | -5.35555 | -43.54649 | 2024-11-14 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36dceb42-2e6b-335f-88f2-87373d03cf33 | -1.23289 | -52.53057 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ce92a1e-6d5a-3108-88d1-0be3abb86b2f | -1.38518 | -51.55703 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d272f580-5a6d-3063-b006-209910b2c148 | -3.49436 | -50.84376 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a5939cf-450c-3aec-9ef6-e56a45a79a08 | -4.04704 | -47.22809 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f5b57c17-6437-3c31-b022-674f58db986b | -1.63747 | -46.10631 | 2024-11-14 04:40:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70ed2a78-f75e-3932-921c-b7d46f8235c7 | -1.63475 | -53.27516 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce60d76b-924d-3dcc-9214-cb650f88d85a | -3.81181 | -47.79887 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e54802e5-d45b-38e3-9a5b-f030212ec4be | -3.0493 | -50.32904 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62d80fa1-7415-31bb-931d-761e2dce64d8 | -2.11931 | -50.70071 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d286f2e6-d522-334d-843e-81572e090e08 | -2.98865 | -45.8666 | 2024-11-14 04:40:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac2c5832-8d78-3ba1-aeec-f9f030127571 | -2.64433 | -46.17785 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6641cf6-14a6-30a2-b4a0-47dd7fdcde7e | -2.66686 | -46.82825 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26d2fda2-19cb-3858-a007-4554d8104981 | -2.6737 | -46.82932 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9982bd4e-f0ec-336e-b63f-ecb037164d50 | -2.3632 | -48.52161 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53a6be2a-90cc-3190-91f3-60c5c606b353 | -3.77867 | -46.05756 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1f9644c4-f2c2-3db3-bed3-df9b52d738dc | -1.68121 | -48.46394 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README26.md)
