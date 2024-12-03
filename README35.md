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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 139d725b-78c8-3e89-9667-b525b20802c1 | -3.55907 | -50.17526 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 175b0f15-4c3f-380b-ba05-6f402fd3b779 | -6.98982 | -43.50904 | 2024-12-03 04:29:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 663cbb02-9de7-3d25-9df4-c0de0619c5d8 | -1.95097 | -53.3466 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1b82f42-e9aa-3fdf-9e35-9de2ecb763d2 | -3.89535 | -46.39967 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2656d196-f76e-3399-9755-23fe941855d6 | -2.56055 | -53.40253 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b2b222e-31b7-36a1-a860-fd2093256f56 | -3.84639 | -46.51672 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2d32bfd-47ab-3525-9c4a-c576a2e87ae9 | -4.75052 | -45.11964 | 2024-12-03 04:29:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90d0e2de-229a-3a1d-beee-26d2d10abf17 | -4.30527 | -48.23971 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d89b4dfa-5932-345c-afdf-2df326d1ec61 | -2.46838 | -46.53189 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4d31ea5-91aa-357c-a0b8-a3b6fc23d38d | -3.84929 | -46.56332 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ea244e9-bf01-3d5e-a109-c9a69282f174 | -3.79726 | -46.7005 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c983da30-6112-329d-8348-c9c38383831f | -3.10201 | -53.23098 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 96f26ede-0315-3391-af4c-2390d19384a4 | -3.48776 | -53.80247 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1af767ab-6f0a-3022-8e4e-d0d331f6194c | -1.42743 | -55.30789 | 2024-12-03 04:29:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbf806b2-eccd-3611-b233-5e849370a4ac | -3.18179 | -54.34194 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a1cdd525-274b-34f4-abff-ef0f8ae0f584 | -4.16065 | -48.59382 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 903a5d36-6d47-3b76-8357-557901f60cc9 | -3.6875 | -47.11776 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c204b98-9258-3cef-a27a-e3edb7d56880 | -3.91924 | -52.3844 | 2024-12-03 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02ded1c1-0255-3b81-9a3b-b589049d1cc6 | -2.769 | -55.36226 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fb354a8-43ff-3b81-8be5-f4c1d300b359 | -3.5256 | -46.17821 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d13e5d54-150b-3c6a-8e9f-e358cfbf2f0c | -4.0722 | -46.70116 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e2a2d0b-d432-3cc1-a0d0-19a3f9735c58 | -2.59351 | -46.58 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23f24aaf-d475-3521-91e9-f5b0b768157d | -3.93211 | -46.92314 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f69a51a6-f461-31f8-8f26-b3b3002c26e6 | -3.1308 | -45.98815 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbc456f5-6e27-3056-b8ff-307267adc44e | -5.38507 | -46.36087 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25cc7d3e-8340-3f92-8b2c-42fae7e6721c | -2.07495 | -53.47518 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c33449a6-3da5-3ebf-9210-651b76f12b66 | -4.04577 | -47.00126 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 97ca2dda-0659-3e12-becf-bacb8e97c887 | -3.18611 | -54.33541 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 55c7961b-d18c-318f-b32d-d5a2974209ec | -2.70078 | -46.30691 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a39bd95-315b-35f5-9a57-319b6d6f03f4 | -3.54227 | -44.84406 | 2024-12-03 04:29:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd49a495-ff03-358f-b29d-338fade63371 | -2.80918 | -53.06177 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e90e6f44-9558-3256-b2b7-b45041f361c9 | -3.83252 | -44.11243 | 2024-12-03 04:29:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cfd0e1e-be70-3c88-9a53-fa5619ae704c | -3.71669 | -51.79621 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9e53b3d-d3b5-3737-b771-c1d4d4037ce5 | -4.01111 | -49.9575 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cf093ae-7c2f-331a-a152-6d61a688fb9e | -3.6157 | -42.74485 | 2024-12-03 04:29:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03ba7093-73c3-3b3d-9510-2f12c6ece1cf | -3.45591 | -44.92869 | 2024-12-03 04:29:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53a8a0a1-7161-32fa-a652-12ae7dfd0552 | -4.19229 | -48.41655 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1235577-9d23-30b9-9c13-baa8dc80de9e | -3.99576 | -48.30647 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0305ac7f-b194-3bc0-9541-e482d2245f2f | -1.14825 | -53.6646 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc08742c-1d0a-3672-a7d3-6853c6d3f4e0 | -4.13985 | -48.25657 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a504e4aa-0ea0-34eb-bb36-228b85bdd489 | -5.60986 | -46.72703 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b192d47-dede-3b58-ae11-59cd227d4198 | -3.26852 | -46.45522 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38838c67-333c-3253-b2a8-fa5b0008b64e | -3.28182 | -51.06699 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d7d251e-1772-3e89-88e8-6906d9f65e81 | -2.48853 | -46.57741 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbe819d9-e0b3-3c0a-b854-510a47e1ef6d | -3.1835 | -54.33184 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85247efc-9ffa-3982-9f37-6a6a39b17c42 | -4.07492 | -46.81521 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6057b6cd-a9a8-3ec0-b9fc-18b8d87f265c | -2.80753 | -53.0445 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e905357a-7bfa-374c-b224-cf78af5b4290 | -3.98128 | -46.74014 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bf55f28-8431-31e7-a60a-aa85e063d791 | -3.54406 | -50.17695 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 64874ff4-de0e-33b4-aae4-10ff588b8bdf | -2.67849 | -46.62138 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 327ada0c-efd3-3536-bdd5-2ce17deef3eb | -3.65958 | -51.72539 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bbfe535-eeee-314b-b000-8a87112b7738 | -3.30927 | -46.41184 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e58a8894-28d2-33e7-a3ed-25ac4abb08a1 | -2.59738 | -46.07736 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f1a919e-cca1-3bfb-9e5d-aa94f61ed90d | -3.85915 | -50.89605 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d9c2945-e649-3995-b8c7-58272b37f939 | -2.58161 | -46.56718 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 641e57c4-54b9-322f-b114-711abde944f9 | -2.85445 | -45.39263 | 2024-12-03 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 438ac365-35e3-37fd-b105-2ac9767b3b01 | -2.1945 | -48.33942 | 2024-12-03 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dec38a8e-7ca9-3835-a0c5-636376458241 | -3.83615 | -49.0003 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d269fef-4ebe-34ea-aada-76dd6d60954a | -2.54631 | -46.55465 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b680011-b2b8-35b7-9739-eacf0fc85549 | -7.80588 | -38.73665 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f91bd4d-b0fc-3f59-88ff-a2e271cc38c6 | -2.46844 | -46.55305 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acbbf9e2-2c08-329d-9971-cb75c89e8145 | -5.11493 | -43.20483 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a724ef37-aa97-3a10-a062-b82e25560869 | -4.062 | -44.87712 | 2024-12-03 04:29:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 37670122-58fb-3688-a09c-96c5cc873580 | -4.29031 | -48.20497 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07337d44-455c-3041-af6e-4d04cf379615 | -2.41741 | -48.88351 | 2024-12-03 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e046d981-d672-32ab-a16d-068b5945624e | -2.57181 | -46.4139 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33b1c95d-4d73-3c88-ab8e-c3e9a5ca2812 | -2.96749 | -53.88297 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c866d7d7-4cf0-3792-8355-189f66a7ec1d | -3.32583 | -46.60921 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9326523c-8bee-3ab3-b812-1a0e4f02c798 | -3.70218 | -51.83241 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6503a80-463a-361f-9a74-1e2f18c527b0 | -3.25358 | -53.65648 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd00bb5b-adba-3c43-9fb4-dba87403260a | -4.29754 | -49.73161 | 2024-12-03 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2a0cbce-5690-31b7-b968-e92d147f4554 | -3.89224 | -46.68025 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cefb22e-3e54-3d7c-9c84-b612f6a7c12f | -5.81629 | -46.47052 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 194c44b7-d7a5-3f85-80f0-0c16745fec23 | -3.54631 | -50.18577 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7d9b7964-10ef-3e55-b231-3cb64bfa683a | -6.17914 | -42.62255 | 2024-12-03 04:29:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| de0ab187-7441-36be-9f8c-a18c4316ef8a | -5.74 | -44.42993 | 2024-12-03 04:29:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01f02967-69b7-3505-97b3-528a5408f97a | -4.05458 | -48.34067 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 260e9073-a2c2-34d8-a65d-b478dca4fa62 | -3.89825 | -46.66348 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f110577-93d1-34af-85ff-4cc2d78b0e12 | -4.73927 | -45.71186 | 2024-12-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ca1ca2a-5da9-31bb-8c5c-e9db0f4b3f34 | -3.78956 | -46.70636 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79e850c9-90da-3a49-9fd7-c7261910bb55 | -2.43962 | -51.78988 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 358f817d-ab04-342d-9bf3-fdf927299cbb | -3.79449 | -46.69654 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c358ffd-e8fd-3cf5-bb8d-6f8dd46203f1 | -4.26121 | -47.61665 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cb4cbb5-c946-3b81-8893-ca7d0cd0e696 | -6.0319 | -42.5214 | 2024-12-03 04:29:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 219ec8e5-65bd-3769-a514-df10bf54d8a3 | -2.66423 | -46.10581 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 522d0d1a-6c7f-36b0-b62a-46f16b51cfd8 | -3.29786 | -53.6803 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e3c1d85-ff28-306a-9a5e-95b2d9a0d010 | -1.16783 | -53.41954 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f8673f6-70bf-3975-837d-fd7bb2b3d136 | -2.60934 | -54.08735 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a1d3ba7-2757-3380-84a6-c47f5c5b96b0 | -1.69783 | -52.62513 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78767aaf-57a7-307e-bb09-190464d99bae | -3.55057 | -50.18225 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8aacbe0c-87f1-3479-be11-dea5df8c7cde | -4.16317 | -48.19548 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3810278f-3fbe-3bc5-9708-1fc527d8986b | -3.32923 | -46.43627 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fa34c70-5dd2-3609-a16e-6d7e96a03eb8 | -3.9819 | -47.665 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b90c945-f06d-3826-8b7b-99103f771c16 | -4.18633 | -51.18064 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa450960-826e-3a09-b153-deec058d9c34 | -2.8767 | -54.12516 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7daac20e-b02a-372d-a366-33a6c24d733d | -2.55846 | -46.56359 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df6ba3f6-64ac-3ac2-a95d-9eebbe6f0b36 | -1.43877 | -53.39855 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f653d28-6665-38d9-a60e-38e4bb19d5b5 | -2.24268 | -46.39062 | 2024-12-03 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7dc7250-9aa5-3ac8-84a2-be27e11f4514 | -3.9216 | -46.53576 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 702e5037-af0b-3158-a036-3383af577880 | -4.47578 | -45.71958 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README36.md)
