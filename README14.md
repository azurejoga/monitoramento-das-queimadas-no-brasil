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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cc33cdc-8d74-3c11-99b2-8c4b0b9e5be6 | -2.7613 | -54.0941 | 2026-10-07 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 229.6 |
| d25655b9-de7a-3058-a127-7f14693a0ef6 | -3.1787 | -50.5597 | 2026-10-07 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 7724435a-b796-38e7-9e0a-61bcd7e7038d | -12.1935 | -44.7254 | 2026-10-07 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| d36bb4ba-45dc-3d4f-a534-6c31a6ee9bd2 | -5.9835 | -40.9367 | 2026-10-07 01:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 146.2 |
| 8912a61f-482f-3b19-8980-4e06f552cccc | -2.7613 | -54.074 | 2026-10-07 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 904f003e-7151-33ec-a06c-3b715af2ab40 | -3.5515 | -59.4807 | 2026-10-07 01:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 414e8640-844d-3b08-9b16-08f03dbcb9bf | -3.5127 | -54.6562 | 2026-10-07 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 174.8 |
| 91261349-d6a3-3278-8bb3-a64912867088 | -11.7335 | -43.649 | 2026-10-07 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 354.4 |
| de25fdab-8661-3e6f-843f-65ffc95a98f1 | -11.7331 | -43.6727 | 2026-10-07 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 8f46b685-5e79-3a83-8e57-8b50dae75199 | -10.9946 | -45.4527 | 2026-10-07 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| b146956a-0049-3d1d-84ba-be114c02efa2 | -3.8566 | -55.9967 | 2026-10-07 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 174.8 |
| e69a9e1b-343f-34dc-b443-568ae24b3cc8 | -3.0 | -54.1287 | 2026-10-07 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 095420dc-26cd-322a-a26b-d0aec55efccb | -11.1238 | -45.7093 | 2026-10-07 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 8f22cfb3-e7e1-314e-9763-92f999568ea3 | -11.065 | -45.8084 | 2026-10-07 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| cd194f69-3909-36ef-9064-574b355e61d9 | -3.5311 | -54.6357 | 2026-10-07 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 706867cf-1915-3833-9bc5-bba9dc396fa4 | -5.9647 | -40.9383 | 2026-10-07 01:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| c797235f-dd8b-38f7-a02d-43397d65b450 | -3.0001 | -54.1086 | 2026-10-07 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a22d57ad-a726-3328-96ce-8345bbf4f08f | -9.1517 | -65.9554 | 2026-10-07 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 90a5ba0e-72e9-35d1-8fe8-bed4cc85a866 | -3.1971 | -50.5801 | 2026-10-07 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 10d20498-ef96-3269-a4eb-9eb235d28c64 | -3.1787 | -50.5807 | 2026-10-07 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| b673b53e-3b07-36c8-bb8c-2fdae15ccef5 | -11.1043 | -45.7347 | 2026-10-07 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| ac02c7c7-ad65-31ff-8990-0bfc93c6406d | -3.0375 | -53.9066 | 2026-10-07 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 63b80c4a-2a36-3bb3-a1ab-218397d213b2 | -8.2865 | -50.2731 | 2026-10-07 01:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| ebf784b8-d9c6-38bb-a887-c0980bab4a89 | -10.8989 | -46.6667 | 2026-10-07 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 05297658-97db-3c76-a21b-dab217fa14a3 | -3.055 | -54.1474 | 2026-10-07 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| dec0b568-f1bd-348d-9165-3cc58e18e48d | -3.6205 | -55.2907 | 2026-10-07 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 3296c4f5-7214-3add-b13d-6bd9bf32bbe7 | -5.7187 | -45.1773 | 2026-10-07 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 03b264a9-58b7-3e25-a2c7-3572062e4b27 | -12.1939 | -44.7021 | 2026-10-07 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8fa29e06-dcf5-3659-930d-fcb913108fe2 | -2.7796 | -54.1138 | 2026-10-07 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| d76eaabc-325f-30dc-bd4a-aa56fca6ef83 | -3.8997 | -59.3198 | 2026-10-07 01:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 6554e854-82f8-308b-8198-e24261a9a560 | -3.4577 | -50.089 | 2026-10-07 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 340b5d72-8bec-3a4b-9970-faf028626acb | -3.0557 | -53.9464 | 2026-10-07 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 2d6dccc6-1d29-3949-890d-6f6f9083b45c | -1.8011 | -57.0967 | 2026-10-07 01:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 28da5b2d-4d9e-3987-8d2b-77462152e621 | -11.1047 | -45.7119 | 2026-10-07 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 90b9a1e7-67fa-3d60-8986-2ac536749697 | -3.8567 | -55.9769 | 2026-10-07 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 26c2f9e4-1388-3903-869b-f8712b9a8bf6 | -7.7551 | -49.2067 | 2026-10-07 01:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 980d66da-d4f3-3747-8d87-425e07088466 | -2.7797 | -54.0736 | 2026-10-07 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| d7083d13-9693-35f4-83cf-f72e1c57f679 | -11.0206 | -45.470001 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 14549b1a-7a68-3040-89d1-bef2700d1f0f | -3.0231 | -53.901402 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a3dadec-25ac-3fad-b0e2-22c22c63b9ac | -6.7704 | -56.227901 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e6b060d-f643-30ba-a2f5-567a382998be | -4.3523 | -55.136101 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3fcba78-0dac-317f-9672-ed2f49cb2d5f | 1.7373 | -55.600601 | 2026-10-07 01:09:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0f1d6b2-5a8c-3057-950a-5b9c96a49428 | -10.8946 | -46.683701 | 2026-10-07 01:09:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84ec2a90-e35f-3ca1-acff-41b35db7c05a | -3.8568 | -55.982399 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3b1cb3f-9b9e-3986-9eb4-4258009cbc65 | -2.9862 | -54.140999 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad1699d2-2e64-3014-808b-b4cdfdbddbf3 | -2.4995 | -58.064999 | 2026-10-07 01:09:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd48e4fa-f9a3-38af-87f6-7805ee24357b | -12.1821 | -44.7188 | 2026-10-07 01:09:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 14d0a2fb-5095-38e5-b37f-3db2d7395412 | -3.8485 | -55.991501 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b65ce6c-3ade-3a1f-81cb-27987e63b4bf | -2.9409 | -54.168201 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccbc0b3d-c444-32ea-9a12-51527ae507ac | -14.266 | -41.671299 | 2026-10-07 01:09:00 | METOP-C | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 150ed1ef-646c-37b0-8f90-86713b943532 | -3.8599 | -55.996201 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bbf0162-ded3-33ac-bac4-60a2f0166cfb | -3.7636 | -59.4063 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b7a9b261-f0eb-307d-b44f-e56f0542a857 | -3.1057 | -53.7691 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23dae4db-5eda-3e0d-bf13-f4c7dfdde0e9 | -8.7052 | -45.1992 | 2026-10-07 01:09:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7a5b5ad0-e7d9-354b-a784-208c6f90348a | -2.8729 | -54.141399 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1948f1ed-60da-31cf-942f-a8963eaadc8f | -2.9983 | -54.104401 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4228c7f5-d99b-34f3-8df7-725e3df9df5b | -3.1312 | -53.701599 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fdc5aeb-16ea-3d80-ad83-2546482e16fd | -3.0212 | -53.8932 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b64722ea-a79b-39e9-b171-1b1889a9f306 | -2.907 | -54.022701 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3423810-dd7e-34ed-a46b-dea711600df0 | -2.7127 | -56.881802 | 2026-10-07 01:09:00 | METOP-C | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 30aff9ea-25e1-3485-8ed1-e2f5f8797fcd | -2.1282 | -54.797901 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c258e3d-3046-35bf-97af-e92eb0caac14 | -4.4566 | -47.919498 | 2026-10-07 01:09:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50ca5412-8704-31be-a6c8-b4c194f365f4 | -3.1233 | -53.756302 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff246d30-2561-3fe7-aa14-c00a7d4bf319 | 1.521 | -56.0051 | 2026-10-07 01:09:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38852259-7115-39b5-8d6c-8431a5f3279d | -3.9002 | -59.327599 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af7489b8-2014-3aed-988f-b46bc1e3d9eb | -3.063 | -54.2495 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f34e2a1d-aed4-314d-ab18-e596b1355cc0 | -6.0051 | -53.507301 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 215f0e41-5ec0-3086-be92-c3386c6e42a6 | -12.1725 | -44.7215 | 2026-10-07 01:09:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2fc443bc-eed1-3d7a-9dd8-e6f805d21e78 | -3.4836 | -50.0933 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b40c084c-78cc-30e4-bf35-cbe73dd6e5a5 | -3.0765 | -54.263199 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d393f56-84a1-3fdb-ab32-bfcd976fe084 | -3.6741 | -55.9506 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 980c9eb6-7720-324e-94f4-933eddddea05 | 2.019 | -61.0994 | 2026-10-07 01:09:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6e50fa-f89f-3d1d-8dae-4a669a863445 | -6.3359 | -55.3256 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8dfc48-8f96-32bc-97ee-7fe95ad550cf | -3.3369 | -59.476398 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1798e59-f9d4-3b17-9950-cdd898fd5d7f | -2.9474 | -54.107498 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa5fc3bd-d3b2-3f59-b2af-64672210fd6b | -6.2186 | -52.836899 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d92c6f8-e9df-30a8-925b-8ea585ef82c2 | -2.13 | -54.805599 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82bda1bb-6c31-3293-ad0e-afbd09e6840c | -3.9954 | -56.270199 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96ea1291-929b-304e-a29a-5a0060f90eae | -3.1292 | -53.693199 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70c5ec5f-5b9c-3c85-b61d-147c060a9388 | -2.9549 | -54.139702 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae7feb59-8f03-3637-94e4-0aad2ff6a14f | -3.2266 | -53.889702 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dab0a5d5-d616-32c6-997e-f3112f672574 | -2.9922 | -54.1227 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 138813af-9b35-3fbf-983a-9cc28c452329 | -3.1432 | -54.372299 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dfa2eb7-b778-3136-a270-e6e90e528dc5 | -2.7878 | -51.6679 | 2026-10-07 01:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9555b5cd-a6d6-3d91-a9c3-cfcf0d4d79b2 | -2.947 | -54.149899 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55152ea4-e142-33aa-bc22-fad17b540d30 | -3.5227 | -54.673901 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e02fcaa5-3981-35b2-b62d-6b9a69170068 | -3.524 | -58.759399 | 2026-10-07 01:09:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d27ecf7f-600d-3285-9d50-07ace1e38e9a | -2.9395 | -54.117802 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a07b8054-6b60-3a22-bf35-c6e747f7e427 | -3.0193 | -54.150398 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d78a750-1d21-3d51-a916-5da43d0cd028 | -6.1527 | -51.735199 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fe94486-a5a5-3474-92ba-260ce2bbad2c | -2.8649 | -54.151699 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6e66fdd-3e59-350d-a527-003812d35b9d | -4.0773 | -54.884899 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 439771aa-1e81-3269-86d4-4dac9f786f4d | -10.8414 | -50.666 | 2026-10-07 01:09:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 941f0f93-7a38-3317-82ca-c2cf04b4fd83 | -2.9007 | -54.084 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e9cdbae-7f34-3cd3-8d00-ee0932512aac | 1.5279 | -55.975399 | 2026-10-07 01:09:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08efbbb1-a40d-3ff6-b57e-8d8399867a65 | -1.1046 | -54.161598 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb2a06fd-5370-3f6c-9d0c-6d1875ba062b | -2.9497 | -54.072899 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cee159fb-817a-340f-9fe3-d75b3e70d3d6 | -3.4479 | -56.939201 | 2026-10-07 01:09:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b157018-9522-3492-b4b4-b422aeaace3e | -2.9484 | -54.200199 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88e96c23-911d-3a05-b62e-c7e8f2b3ee85 | -3.232 | -54.310799 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
