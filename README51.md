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
| 3a5e2345-0d3f-3cfb-a826-d579115cfde1 | -2.88984 | -54.16268 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22cd2221-fd96-3677-a19b-331e63cc240d | -2.72374 | -46.20399 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f10009e7-2bfa-3df4-80c0-e63b557b3246 | -3.93807 | -46.88526 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecdbd397-d8ad-30ba-8532-1cf213b26f10 | -2.26415 | -53.61292 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1539793f-43bd-3a2f-9a5a-cf81e9612f77 | -4.04311 | -48.26692 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19075bf5-df13-30d5-ab4c-9ec6667ee2fb | -3.84917 | -46.52069 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25c073a4-062e-3c1e-81ff-559bcbae88b3 | -3.17747 | -54.32908 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 424cabcc-c741-392f-b190-1cc7a81331f9 | -3.0123 | -45.61822 | 2024-12-03 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f368d77e-1819-3571-9b4b-7e65b3eafa90 | -5.12104 | -49.92875 | 2024-12-03 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b53360b-b300-366c-bbbf-aee0d8484a3e | -3.40635 | -50.2335 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71973e71-1e58-34c4-bb12-b026252f2dca | -3.28366 | -53.25238 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67fe5611-7ace-3c47-8bc6-975371e8b935 | -4.09642 | -51.08984 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec8761f7-c804-37e9-886c-e7d082e0fb5e | -4.61654 | -48.03496 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62539da6-13b8-3395-9ae3-c2f424a817fd | -3.15825 | -46.55161 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ab4e907-e458-3da9-a0b3-a2675e84caaa | -2.73326 | -46.25163 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d921d0f-2178-3d5c-9fa2-3143a9b50eef | -2.80851 | -53.06593 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c84b2f05-4099-3781-9dd0-933d00673bbc | -1.69591 | -52.63723 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58a6e1ce-40ce-362b-b3ef-2609e0934882 | -3.80619 | -46.55656 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eee10c43-76e2-36c6-adb4-85770df3d17a | -2.68396 | -46.60814 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8453cc03-94d4-3f2b-b0b2-04e35f81d62c | -3.19153 | -52.44519 | 2024-12-03 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38f7ab8c-9f60-3526-ac0f-f6ebebdde00f | -3.2143 | -53.12373 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a5a68c5-660f-3ad4-9542-3fd41b25321c | -2.65413 | -46.58236 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6b20c84-f9ec-38f4-88f0-cf961ebb06ff | -2.47398 | -46.56096 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 217286d1-f5be-3600-8120-b1aa17c6314c | -4.29864 | -48.21705 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d27d5b3c-4f2a-3a58-aef2-984ac1b0b805 | -1.49904 | -51.93692 | 2024-12-03 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cd25f77-78c2-320d-801b-866a2f47b068 | -2.56894 | -46.19392 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b79fdd5-9075-35d3-b646-558dfb8fe8bb | -7.19582 | -48.60842 | 2024-12-03 04:29:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99ddd955-a560-3e75-b22e-6e5f790d9f6e | -3.1297 | -45.99517 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f904abf7-d77e-36ba-9346-c143e240bb54 | -3.77685 | -46.70085 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5c18375-15eb-3e74-b5d2-1d2d6d570c14 | -2.14748 | -50.69879 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14770b47-c2ca-36cc-b734-fef7b314e193 | -2.29059 | -46.36627 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fa15fbd-3b8c-352f-be67-df543f5189ac | -2.69863 | -46.12538 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a323e5fd-b7ad-310d-8b21-5525d49cb88e | -2.94944 | -48.07029 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a9beb0c-74de-3c3e-bb64-c1f3d5a993d3 | -3.1735 | -46.32357 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94c17250-eaad-30f7-bb71-20265463b5a7 | -3.29622 | -53.67767 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ed18ce7-27a7-3594-97b8-cfbc686630aa | -3.28106 | -51.07157 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3eba6887-7a54-3d30-bf78-ae9a7ace2384 | -2.51505 | -46.2352 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9deeb193-d18e-33ab-b014-a9eb9be81346 | -3.70436 | -47.11986 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d126d019-1081-3211-8012-a3ea1e02660a | -3.9359 | -46.70474 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b26cd62-db2c-3929-a564-8ead3cd88767 | -5.38854 | -42.95717 | 2024-12-03 04:29:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3ebca591-172e-3967-8792-49e954dc21c3 | -2.46905 | -46.57076 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2f73cf6-2576-3b68-bfc8-dac04d0da880 | -3.33523 | -51.24265 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b793ebb-a361-3dc6-8e0f-75fbdbe5e69a | -2.60013 | -46.58103 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0875ff1d-52ad-3f52-a19a-1c474ca5a367 | -3.83121 | -46.61368 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ecc23c7-6bc7-355e-aada-66478b97679b | -3.93313 | -46.70077 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe476437-f7b6-3c27-a33f-43c5252547d6 | -3.37009 | -53.21539 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad7693a0-2e9d-3a01-aad4-177df6b7f69b | -2.55539 | -53.40617 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1c84075-f3c9-3399-865a-c35b445f932c | -3.2491 | -53.65573 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a06cfad-cce2-3544-bf99-73b658668f58 | -1.73937 | -52.62953 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6e7120d8-2e80-3c17-a34f-826534be6ad3 | -5.58958 | -45.14835 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7dd57de2-2d27-3014-b660-d67378c6f123 | -4.29087 | -48.20147 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8a8a74d-417c-3ec6-9aef-f23ea6a4307c | -4.32143 | -48.09526 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90a545d7-b1dc-35ef-9603-df8551245754 | -4.94092 | -47.80894 | 2024-12-03 04:29:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2712a04a-3457-3527-9d59-01af89d08098 | -4.01078 | -47.00598 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74bc60d3-b1d2-3a3a-958c-c234ad4e44ce | -3.45305 | -44.92439 | 2024-12-03 04:29:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f27a467c-de3b-3218-90aa-282c6bc3100f | -5.80071 | -46.48258 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| aa8f932d-aca9-3c0f-a45a-f0196dcd70fb | -3.95821 | -44.05042 | 2024-12-03 04:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8985be00-ea1f-3fac-8ef0-dda2bc9089da | -2.90094 | -51.36956 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb0a9bd5-dd8b-3cb4-a489-0936fb627e5a | -3.78772 | -47.49631 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e337a03-feea-3ec7-ba1a-45f711c07f72 | -4.19084 | -51.17668 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e924ba02-ee49-3aa4-ae67-1f0162be877d | -2.52803 | -53.98323 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 372f7c79-5082-3e0f-bba2-25e7d4f1fefb | -3.84598 | -46.56279 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba6b5c1c-06e3-31b9-856e-c98dfeba0310 | -3.85695 | -46.53612 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0af6f0a-c182-3c6b-9c84-f3821ead6c4b | -3.35153 | -52.65931 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfdc43aa-d333-31d9-8420-f4c56fd11b1c | -5.31144 | -44.55346 | 2024-12-03 04:29:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1870e3ed-3de8-315e-a17a-a2ceb576e39e | -4.09063 | -46.12521 | 2024-12-03 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b90f3392-02c1-32ec-9962-bf6f64afe6c4 | -3.4916 | -50.30981 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 043e8e0f-e188-3cfe-b332-56674792ff31 | -3.86565 | -43.35838 | 2024-12-03 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52929e20-6cff-37e6-a01b-888f5e1afae7 | -3.70846 | -50.26539 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f862ae0-545b-3283-b7cf-ac11cb74071e | -3.2105 | -54.27338 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 742b86e2-1c0d-32ea-bb27-8de38eccd5fe | -2.67923 | -46.11882 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83ade484-98dd-3f76-bc2e-a7912e500a12 | -3.83399 | -46.61764 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e60a6d27-9f81-3b0a-ba62-8f26f5347773 | -2.60328 | -46.21345 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9bfd9e1-472a-3940-b324-e389dec54ece | -4.0425 | -46.93338 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0037e8fd-dbdf-3184-b509-8d80dd44dc0a | -3.07843 | -53.37574 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 50bf0544-2c5b-359e-bc4c-ce64d4ccc935 | -3.19214 | -52.44147 | 2024-12-03 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dd0bdf4-270f-3b8a-8fde-d4c7b9f1711e | -5.80236 | -46.47197 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39dc9252-0661-3fee-815d-24edcb8b225d | -5.14517 | -43.23837 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d56ea7a6-d8de-39ec-9031-b07912cd6039 | -3.80273 | -46.68722 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f44da23-464c-35fb-a8c9-7b0f9cd892ff | -3.9443 | -48.18312 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a17f488c-293c-3419-86e7-70fb752876b5 | -2.38442 | -53.71141 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75708dc7-63a2-3dd0-a4ac-5fd2aa17f157 | -2.77868 | -55.36691 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6f41b28-939f-352f-bb9d-9e584539b436 | -3.3405 | -51.20969 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8d04d2b-991c-38c5-a3a1-48636a03da37 | -3.13025 | -45.99166 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12b0e73e-6459-36a9-afbe-2cc1730f7039 | -2.46851 | -46.57419 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1c217d8-f785-3303-bdbb-5bbd95d952c8 | -2.45439 | -53.71488 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a440a96-66b9-3afd-9a3e-b14430d266e5 | -3.32968 | -46.60628 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 832dadef-ae61-3acb-98ae-11bde116be10 | -3.83453 | -46.61418 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ac71ebd-a6a7-39bf-92d6-9d14984d5e26 | -3.78733 | -46.69896 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27f70eea-b063-3027-b76f-4ab55461632f | -2.98583 | -53.88578 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62a483e8-861e-3e16-9b0f-4ae7abbf932e | -1.72465 | -52.65017 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36bf0498-c262-32fa-b3a3-ddd0c9bbdee0 | -2.85341 | -45.82958 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 014101ed-3439-3ef8-a843-2e4c07af4885 | -2.5406 | -53.41278 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f8405e2-8ac8-3f7e-b709-7c1a65398701 | -2.56399 | -46.5715 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d2508d0-6298-386d-8823-79458d26a9df | -3.34446 | -50.18127 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d6b4e65b-e10d-315b-9a40-c774ca9d730c | -3.70052 | -47.12278 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c132fd3b-ea3a-3e52-83d8-3a9f18eda518 | -3.82446 | -46.57003 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e743d62d-63aa-366f-9803-e9815659469f | -2.38965 | -46.90326 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7388063-ffc6-3bf7-a29e-70c4814b4c75 | -4.34818 | -45.99822 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee6817c7-d397-374c-ac22-c4bf63f7481d | -1.94943 | -53.32805 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README52.md)
