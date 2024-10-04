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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 799fa506-7a28-3b1c-b437-44edf4c30bcd | -11.662 | -65.183197 | 2024-10-04 01:29:46 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a96d0a60-c213-3525-876c-a9b02f58afb2 | -11.6639 | -65.192398 | 2024-10-04 01:29:46 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fac1d156-74be-3f1e-8f9d-8d535bcdb5e3 | -11.5299 | -65.041603 | 2024-10-04 01:29:47 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9053586d-47d2-32bf-a3b8-3ef0e33c72f4 | -11.507 | -65.273598 | 2024-10-04 01:29:49 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a4ac2c9c-e06a-3a6c-9775-b457d5a27121 | -10.9513 | -68.325798 | 2024-10-04 01:30:08 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 334c73eb-3e35-38e0-a3a6-fe4c3ae88ea1 | -10.2474 | -68.212502 | 2024-10-04 01:30:19 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3bb7eb03-2f82-3ad4-86a8-52d3b2a3f656 | -10.2501 | -68.225998 | 2024-10-04 01:30:19 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 84ea1b26-ef93-3d90-b1e9-b755fccfed3f | -8.8318 | -63.004398 | 2024-10-04 01:30:24 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9f77d993-4d84-30af-af5b-1469ab3e23f6 | -8.8333 | -63.011398 | 2024-10-04 01:30:24 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3f764d4f-f296-3491-8e2d-7adbf15135e5 | -9.2708 | -65.350899 | 2024-10-04 01:30:25 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 676df180-f5bb-3307-9d48-e421f5c3c9b3 | -8.3795 | -61.533199 | 2024-10-04 01:30:26 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8771f304-05bf-38a6-825e-4f54137a4ddf | -9.0951 | -67.468201 | 2024-10-04 01:30:35 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7a9f0a63-8512-3c31-a12c-96073ff77c53 | -9.0975 | -67.479698 | 2024-10-04 01:30:35 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5243b9e7-c26a-38e1-850b-3f716991bc60 | -9.0854 | -67.470299 | 2024-10-04 01:30:36 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0b74681-1a18-3fa7-a0a4-c1fef82c2d0f | -9.0878 | -67.481796 | 2024-10-04 01:30:36 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78cc54a8-6087-3093-9039-72c883e8705e | -8.9884 | -67.105598 | 2024-10-04 01:30:36 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a968713-7e63-3c48-8841-c0f44cfc51da | -9.0224 | -67.364502 | 2024-10-04 01:30:36 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67d3bb6c-1b15-37ee-a2da-52299b9067bf | -9.0247 | -67.375801 | 2024-10-04 01:30:36 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9029f23d-12b5-3143-ae19-f1da47168d32 | -8.6662 | -66.596901 | 2024-10-04 01:30:39 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8b09868-f50e-3c06-8013-2c560c64f47a | -8.6543 | -66.588997 | 2024-10-04 01:30:40 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff131ee-5b6d-3638-a565-d2de2f91231d | -8.6564 | -66.598999 | 2024-10-04 01:30:40 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6991824-7a5c-3a3b-9f76-84d59df20c3b | -8.6586 | -66.609001 | 2024-10-04 01:30:40 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef45ea52-623c-34eb-890d-0abde33c727b | -8.6509 | -66.621101 | 2024-10-04 01:30:40 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af6254e0-21da-3e53-8738-1b0e3f1887a7 | -8.653 | -66.631104 | 2024-10-04 01:30:40 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1fd6faf0-e8ff-3883-a260-745ea3e06292 | -8.6552 | -66.641197 | 2024-10-04 01:30:40 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a06fe9a9-6390-3289-baee-4e0c6e7f3dcc | -8.2564 | -71.087898 | 2024-10-04 01:31:01 | METOP-B | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 98587dc4-f01a-363c-8569-7f461951d76d | -8.2604 | -71.107697 | 2024-10-04 01:31:01 | METOP-B | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 702442be-637f-3648-8a99-164eeae72b33 | -7.0496 | -71.7127 | 2024-10-04 01:31:23 | METOP-B | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fca6960e-4482-3460-ac1f-3f76846aab3d | -7.0539 | -71.733704 | 2024-10-04 01:31:23 | METOP-B | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a811033-3019-3247-b65b-071fc9a36122 | -7.0399 | -71.714699 | 2024-10-04 01:31:24 | METOP-B | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3668e6ca-213c-3b57-b2d0-61727192893e | -3.2349 | -50.3695 | 2024-10-04 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8cbda9ea-014f-3df2-8b66-aa754656e2b7 | -3.404 | -42.2858 | 2024-10-04 01:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| a3b1eeea-f90a-31df-8fb0-ba57abf586a1 | -3.4227 | -42.2849 | 2024-10-04 01:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 78632746-a602-3e63-a8ca-be7bf282d9c2 | -3.2899 | -50.4725 | 2024-10-04 01:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8c62f2cd-5dfe-3c59-bfd0-2f2ea69bab7f | -3.2899 | -50.4516 | 2024-10-04 01:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| a6295c33-8ca7-380b-ae30-8dd89c7668ed | -3.3083 | -50.4719 | 2024-10-04 01:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 32c2d5ca-1d4c-3133-8343-276a52b22bfe | -3.3084 | -50.451 | 2024-10-04 01:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 6f729a62-1548-3956-b386-878f4cd898ea | -4.5375 | -43.304 | 2024-10-04 01:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e964eb1e-64e9-3cfb-aaeb-7cafc0cf8bd4 | -4.6684 | -45.8961 | 2024-10-04 01:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 281d532e-0a5d-3354-b3fb-d9fdc671ca84 | -4.6686 | -45.8738 | 2024-10-04 01:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 146.8 |
| a2357d65-c684-3e67-b6bb-2b880364077e | -4.687 | -45.8951 | 2024-10-04 01:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 182.2 |
| 383f7fc6-d620-3e21-8d1b-bd50755b5461 | -4.6872 | -45.8727 | 2024-10-04 01:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 383.2 |
| 6abdebe5-8e76-3632-9fa6-e293ce2b44aa | -4.6873 | -45.8504 | 2024-10-04 01:35:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| bf2e1244-278e-3976-9157-eabafcf8a703 | -4.7058 | -45.8717 | 2024-10-04 01:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 2cbb664e-3acd-3485-b2b2-69f5a32ea5f4 | -5.5033 | -48.8046 | 2024-10-04 01:35:37 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| b0e12074-5625-39cc-ae6f-34078caefce3 | -5.8216 | -44.1196 | 2024-10-04 01:35:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 0fcdfc19-e5ac-3399-868c-fb11ed892d1f | -5.8214 | -44.1426 | 2024-10-04 01:35:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ed9b7e50-88b8-330d-88bc-142cf0ee806c | -5.9599 | -45.3861 | 2024-10-04 01:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| cd552f0a-21a8-3782-9d2e-66abfb0d3aaf | -7.0529 | -71.7544 | 2024-10-04 01:35:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 7d13059c-309b-3216-a851-48b8a789087c | -7.8164 | -50.543 | 2024-10-04 01:35:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 455dee43-a054-352d-9833-15edf049d4bb | -7.8166 | -50.5219 | 2024-10-04 01:35:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 429a96b7-e463-3a43-8c50-aeb616a4119f | -7.8539 | -45.3611 | 2024-10-04 01:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 8df1b1d1-f9af-3cc2-8310-14c11cb9e852 | -8.6448 | -50.0518 | 2024-10-04 01:35:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 191.4 |
| 0472ff33-4a20-369a-ae5b-afdfcdf0e80e | -8.6451 | -50.0304 | 2024-10-04 01:35:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 12b4a502-7ad6-3113-93c5-fcd349032c2a | -8.6636 | -50.0501 | 2024-10-04 01:35:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| c0db3b56-80ee-3d51-9d74-be296733d006 | -8.6638 | -50.0288 | 2024-10-04 01:35:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 4d6283dd-479b-3643-851b-217043c542ec | -8.649 | -66.6582 | 2024-10-04 01:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 0a9b8b7c-582b-3b2d-b9b4-8fc9b9638c4d | -8.6491 | -66.6396 | 2024-10-04 01:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.2 |
| b5f2861f-4da7-3bdf-9d3a-f5e4db274ab5 | -8.6675 | -66.6577 | 2024-10-04 01:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 45074e9d-1e0e-3511-8bea-cc8c239c0c08 | -8.6676 | -66.6391 | 2024-10-04 01:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 65560468-ef67-3ae2-b0be-31531be65626 | -9.1041 | -50.902 | 2024-10-04 01:35:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 72fcf93b-1a40-375e-bad2-7380dee674e0 | -9.0162 | -67.3904 | 2024-10-04 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 91c648a6-9f56-3a72-8026-a74a558efa2f | -9.0347 | -67.39 | 2024-10-04 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 653261c4-6d44-3a68-b7aa-a6986d646d41 | -9.0898 | -67.4997 | 2024-10-04 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 35be80dc-a701-3a43-87af-d4e931ceede1 | -9.3115 | -50.8203 | 2024-10-04 01:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 161.7 |
| 93eb5dc3-0207-3db2-b6a8-19d8d4f29936 | -9.3118 | -50.7991 | 2024-10-04 01:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 255.1 |
| b45b4957-18c3-33d1-a9b7-09a72b7750ff | -9.312 | -50.7779 | 2024-10-04 01:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 5a34d139-a161-3694-9957-d48fa2e20d42 | -9.3303 | -50.8186 | 2024-10-04 01:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 28fc7667-75f3-3bcc-a297-09fc3fe28575 | -9.3306 | -50.7974 | 2024-10-04 01:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 168.1 |
| b49bc2c0-c9dd-3ae2-b51a-b0fbde576751 | -9.3308 | -50.7762 | 2024-10-04 01:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 6ecbc554-d59d-3aa5-918a-2c02e039e431 | -11.0532 | -46.5344 | 2024-10-04 01:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| eff03a75-638f-3976-b516-a4a5c3452151 | -11.0536 | -46.5118 | 2024-10-04 01:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 40c0e883-96e9-382f-a01d-7997d52162ed | -11.0727 | -46.5093 | 2024-10-04 01:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 781bbfff-1007-3e8f-b001-27e7947fd32f | -11.8052 | -56.6024 | 2024-10-04 01:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 0941dc86-b68c-3990-865a-aa2325bce9be | -11.8242 | -56.6009 | 2024-10-04 01:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 146.6 |
| b269a9ef-a191-3b74-9c84-41b274ab2e52 | -11.8244 | -56.5808 | 2024-10-04 01:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 65e0ad76-da3c-3542-ba89-6e69d1df4aee | -11.8957 | -56.9554 | 2024-10-04 01:36:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 23fadcae-32c4-3911-9e2b-6aa9265644da | -11.896 | -56.9354 | 2024-10-04 01:36:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| fd641d76-dba5-3918-9d24-35c8d631174c | -12.4037 | -63.0201 | 2024-10-04 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| f9540bbd-7c10-3526-a9ed-e4609226aee5 | -12.4225 | -63.019 | 2024-10-04 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.5 |
| c7c52730-506d-38ff-976f-9d8ccee9518b | -12.4227 | -62.9999 | 2024-10-04 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| bb6d5ab1-a137-3786-9cb8-bbd98788dd2a | -12.4414 | -63.018 | 2024-10-04 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 4ddd8474-edd7-38c5-9b49-02971fc4a2ba | -12.4416 | -62.9988 | 2024-10-04 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 14521aa0-8cc2-3343-a45f-2a7d48aa03f0 | -12.5711 | -53.1171 | 2024-10-04 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 5b135b34-7e72-303c-9809-1200d1fb5881 | -12.5898 | -53.1359 | 2024-10-04 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 137.1 |
| f295ddd7-b87b-3608-b5a1-d97fe674ed2c | -12.5901 | -53.115 | 2024-10-04 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 235.3 |
| 332181fe-31e8-3e54-bcfc-d8185fe82ee2 | -12.6089 | -53.1338 | 2024-10-04 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| ee982290-21c0-3cf4-971b-1b7996f8f1e3 | -12.6092 | -53.1129 | 2024-10-04 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 2602f957-480a-3421-aee1-981a0b921ca2 | -12.6212 | -56.4911 | 2024-10-04 01:36:18 | GOES-16 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| de2b18bf-6081-3a9c-b1db-2f1c7c57328a | -12.6295 | -63.1225 | 2024-10-04 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 117.6 |
| c6b49b0c-1d1a-31a8-a7cb-8dfc8fac2c51 | -12.6296 | -63.1033 | 2024-10-04 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 100.7 |
| b18d9dee-9860-3898-bf26-24077158e2d3 | -12.6484 | -63.1214 | 2024-10-04 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 44f9602e-069e-360b-9fc0-b9808a49bfda | -12.6486 | -63.1022 | 2024-10-04 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 702bd07a-9ff9-3e03-82b2-924c40743f81 | -12.7255 | -62.9442 | 2024-10-04 01:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b92cb765-a739-3f8d-9f86-5c62a94bef23 | -12.7256 | -62.925 | 2024-10-04 01:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ca74c2a9-bdb3-3cb6-925c-358162639934 | -12.9831 | -51.129 | 2024-10-04 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| f86250e5-c516-3c9e-a796-37f45d9166d2 | -12.9186 | -62.4901 | 2024-10-04 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e0f47d7e-90dc-3aa8-8963-a3f4b44e01df | -12.9187 | -62.4708 | 2024-10-04 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 88b20b71-3713-3654-9138-235785ef6043 | -13.0975 | -51.1575 | 2024-10-04 01:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.6 |
| fc4bf142-13cb-3dcd-b9eb-0ce9c4a62228 | -13.1166 | -51.1551 | 2024-10-04 01:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 173.4 |


[Clique aqui para ver as próximas entradas](README38.md)
