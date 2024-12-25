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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85b69857-e4e5-3738-8c8c-ef2fcaf773c6 | -5.46 | -39.67 | 2024-12-25 00:00:00 | MSG-03 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 73a9495a-79f3-3604-91e5-76dd8e152de5 | -5.49 | -39.68 | 2024-12-25 00:00:00 | MSG-03 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 25de5d29-f2ca-3151-8f62-a52430043047 | -8.80711 | -36.51686 | 2024-12-25 00:05:00 | TERRA_M-M | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 24299974-63fe-38d1-8ac5-233a4489b4a9 | -10.08824 | -36.3284 | 2024-12-25 00:05:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 4ebce9ca-88a6-3f4a-89f4-086668b87fdd | -10.17521 | -36.29123 | 2024-12-25 00:05:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 8e057314-bc32-3c68-b038-8d8f5684b0cb | -10.08699 | -36.31945 | 2024-12-25 00:05:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 967dd79e-5d4b-3155-88e7-2b33ef51138f | -9.69642 | -39.75905 | 2024-12-25 00:05:00 | TERRA_M-M | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 2c32eaba-d5c7-3577-b683-2066a7b63b15 | -10.77355 | -37.22484 | 2024-12-25 00:05:00 | TERRA_M-M | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 3a3528ca-7aca-34e4-b7db-37a1a3c914ca | -10.17397 | -36.28228 | 2024-12-25 00:05:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 7afd8e03-2ef4-3afb-95a1-f05822f1ed3f | -11.96694 | -41.32966 | 2024-12-25 00:05:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 4ed1bdc5-c003-3af5-8c12-a92e4052583e | -10.7723 | -37.21559 | 2024-12-25 00:05:00 | TERRA_M-M | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 30.3 |
| 9f7dfec7-b12c-34ff-a617-e4bdd44fe79c | -5.38781 | -36.88837 | 2024-12-25 00:07:00 | TERRA_M-M | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 9b3bd6c5-3b22-3c24-8a6a-604d081dd0b4 | -4.77001 | -40.46882 | 2024-12-25 00:07:00 | TERRA_M-M | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| b8a1718d-57d0-3af6-8c0d-5e9e3fcc58e7 | -5.20407 | -37.29371 | 2024-12-25 00:07:00 | TERRA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c8c7c74a-8d34-34d4-87bf-ee6523c9b3c4 | -4.05318 | -38.29322 | 2024-12-25 00:07:00 | TERRA_M-M | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 54a81078-2e98-3660-8845-75607b127b61 | -6.80741 | -36.17813 | 2024-12-25 00:07:00 | TERRA_M-M | BARRA DE SANTA ROSA | PARAÍBA | Brasil | 2501609 | 25 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 897fbf48-3670-339e-977d-f72991e152f8 | -4.7685 | -40.4574 | 2024-12-25 00:07:00 | TERRA_M-M | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 6275917b-c396-3fef-aee0-20257f8c271d | -3.2294 | -39.66498 | 2024-12-25 00:07:00 | TERRA_M-M | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a0022b96-5fe7-31dc-8418-41e570974730 | -5.47707 | -39.67025 | 2024-12-25 00:07:00 | TERRA_M-M | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 141.9 |
| 9cc224f7-9dee-3253-ac58-f09f0e3d16f9 | -2.31509 | -45.06894 | 2024-12-25 00:07:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e0b20ff7-1b27-352b-a0ae-a7ca79c876d9 | -2.8366 | -40.29804 | 2024-12-25 00:07:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 152b188d-528c-389b-a8f2-13302141a60e | -5.49011 | -39.66314 | 2024-12-25 00:07:00 | TERRA_M-M | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 978f16ae-a6dd-3127-ab39-1beed779db01 | -4.05194 | -38.28424 | 2024-12-25 00:07:00 | TERRA_M-M | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 7026d096-b0d1-3d89-af76-9808c037beb4 | -5.48528 | -39.65914 | 2024-12-25 00:07:00 | TERRA_M-M | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 109.1 |
| 8fd4d2d0-8be3-3031-b87a-80c6682ef53b | -2.57188 | -45.7242 | 2024-12-25 00:07:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 96ee702e-3e26-3df6-ab1b-93e8335c62f0 | -3.79226 | -41.61116 | 2024-12-25 00:07:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 6cf97180-c7ec-35f7-83fe-ec9cc01d0297 | -5.48666 | -39.66915 | 2024-12-25 00:07:00 | TERRA_M-M | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 122.3 |
| f1478ebf-038c-3ba0-8fe1-521978874a58 | -5.47758 | -39.42491 | 2024-12-25 00:07:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 73b6b318-ff6c-3d93-b058-9102bf9eb485 | -3.78161 | -41.61261 | 2024-12-25 00:07:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 07afc20b-6dff-3695-aca8-88a8211ae3d8 | -4.06211 | -38.29197 | 2024-12-25 00:07:00 | TERRA_M-M | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 00d5b7d9-d1a0-3066-9fe4-93b4a3eb3d51 | -5.22195 | -41.23916 | 2024-12-25 00:07:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 4b9a9c2d-f051-359b-9241-5ec9ff978ea4 | -4.76865 | -40.46376 | 2024-12-25 00:07:00 | TERRA_M-M | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 70ede91c-5e8f-3fd0-9ffe-4b037b82aea1 | -5.4757 | -39.66029 | 2024-12-25 00:07:00 | TERRA_M-M | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 111.3 |
| cd75f1dd-f082-364f-956b-8002e1c631a2 | -4.86951 | -38.33547 | 2024-12-25 00:07:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| c2c25c3e-198d-3824-a1af-bb3456766a56 | -5.4771 | -39.6633 | 2024-12-25 00:41:00 | METOP-C | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9b6652ca-31d0-3d51-8338-37167ba592ae | -1.5183 | -54.9529 | 2024-12-25 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10888e5f-6323-369c-bcaa-5200d978a7e3 | -3.1536 | -53.192402 | 2024-12-25 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03d3d28f-1ca6-3b8d-a5a3-5281216fe5de | -3.5311 | -52.131802 | 2024-12-25 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b908c5be-d036-37fe-aa43-20b1174304d2 | -1.5158 | -54.941898 | 2024-12-25 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0ecb815-bb92-3399-a640-b6acc8e69dc4 | -1.3465 | -55.190498 | 2024-12-25 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e662331e-dfa4-3025-8764-227501038e31 | -2.8483 | -52.7971 | 2024-12-25 00:41:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19ab7786-4ebe-3410-82fe-139ccbffed16 | -3.1495 | -53.174301 | 2024-12-25 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f8416ba-e668-32ee-bd4e-a59caa3e8e5d | -2.3435 | -53.882401 | 2024-12-25 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3925db1-a0b3-388f-9607-68b1ace58663 | -3.0347 | -53.895599 | 2024-12-25 00:41:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c9626c3-6ba2-31d7-b4a8-dceb17c7959c | -3.1515 | -53.183399 | 2024-12-25 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a85709a-a6c4-3c09-bf81-6ba872a29fb1 | -1.3491 | -55.201801 | 2024-12-25 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 710c5de2-054a-3a73-9ab3-f4f79de77f3c | -5.4868 | -39.6609 | 2024-12-25 00:41:00 | METOP-C | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6e6ef98c-1ce5-3486-ad91-5327a2fa0901 | -2.9316 | -45.834599 | 2024-12-25 00:41:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c749e862-3802-3138-be9f-d7dd42fe7765 | -2.8561 | -52.7864 | 2024-12-25 00:41:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89a1c963-e625-3460-852e-4e045e28227b | -2.8581 | -52.794998 | 2024-12-25 00:41:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b447d57c-2902-3c40-953a-ed79b6503df5 | -3.0071 | -53.818699 | 2024-12-25 00:41:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0602e10-149d-3fe7-ab64-3a511ceead15 | -2.3413 | -53.8727 | 2024-12-25 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1d04fbf-d4d6-3dd1-ba1c-87ca48000b5f | -3.5293 | -52.123798 | 2024-12-25 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46cb6a74-90d8-373c-a8ee-067f29060c48 | -2.8464 | -52.788502 | 2024-12-25 00:41:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee75e932-42f0-3a68-b222-b3a498ee7d78 | -2.4983 | -51.799099 | 2024-12-25 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd5fcc22-212b-30c3-8c5b-010162b9e1ce | -3.0325 | -53.885601 | 2024-12-25 00:41:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f9d1284-3d74-3ac3-b10e-1cfa65fbc086 | -3.0614 | -53.786201 | 2024-12-25 00:41:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd53553-865f-3746-ab3a-ca10a605b8b0 | -9.92695 | -59.91206 | 2024-12-25 01:45:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7428108f-3665-3762-b4cc-d616bc8a7f48 | -9.92563 | -59.90289 | 2024-12-25 01:45:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4966b329-e74f-3966-b5ae-1bb09f46e788 | -9.93461 | -59.90157 | 2024-12-25 01:45:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a044dc84-4c4c-302f-b817-d90de48ac025 | -2.84903 | -52.80559 | 2024-12-25 01:45:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 70c9761b-fe7a-37ae-8beb-6777e065d4e9 | -5.47504 | -39.66293 | 2024-12-25 03:29:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ce8c6687-98e3-3ac6-9a36-3b1f72d1f98b | -5.48463 | -39.66475 | 2024-12-25 03:29:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 31417c22-3b14-3fca-b23f-3fe263ddde7b | -4.8661 | -38.33422 | 2024-12-25 03:29:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4b0cefb0-8104-34b8-9955-0246861a9dcd | -3.78662 | -41.61163 | 2024-12-25 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c2c6420a-7302-3cdf-a079-3015051d661e | -5.47981 | -39.66398 | 2024-12-25 03:29:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 16994069-aad1-3e49-ac9e-d3d87fd7b6d9 | -7.47754 | -34.84367 | 2024-12-25 03:29:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bea0fda1-6afd-3344-9515-ba9fa8884b23 | -3.22719 | -39.66967 | 2024-12-25 03:29:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 939226ae-66f1-3dc8-a5ec-bb045a00264c | -3.78099 | -41.61065 | 2024-12-25 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1632a7f1-b95e-3a8d-b7d1-ec0f2fda7fa1 | -5.2007 | -37.29415 | 2024-12-25 03:29:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 81b9ff9e-adf9-37dd-b0ab-58f29c2de944 | -5.20177 | -37.2946 | 2024-12-25 03:29:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 19c5b2f8-8014-3355-871d-1386299cdf8a | -3.79226 | -41.61262 | 2024-12-25 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 686805f7-2bfb-302e-b2d6-a4b53be047ff | -3.22766 | -39.66682 | 2024-12-25 03:29:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e614b698-a11b-3c24-b914-98d3d6335727 | -5.47426 | -39.66746 | 2024-12-25 03:29:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cf005d12-412e-333f-8912-db8a78a9e3cf | -6.81471 | -35.39753 | 2024-12-25 03:29:00 | NOAA-21 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fed8167e-2ace-3deb-9de7-e30ebf0ee5d1 | -8.41604 | -35.52139 | 2024-12-25 03:32:00 | NOAA-21 | CORTÊS | PERNAMBUCO | Brasil | 2604809 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8e347077-83cd-3753-a66d-30f50396f781 | -15.01114 | -39.02267 | 2024-12-25 03:32:00 | NOAA-21 | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9bbcdc9e-50e2-3298-84ee-4db178b2865e | -12.36691 | -37.88896 | 2024-12-25 03:32:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 62f4851a-9127-37ed-988c-e63dc1b68736 | -11.95463 | -37.6373 | 2024-12-25 03:32:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 49f49ee1-d2cc-3563-8142-87fc7e6dd0ec | -7.62106 | -38.72896 | 2024-12-25 03:32:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3a85f3a0-c55b-38da-98da-25e3ccb67775 | -12.36773 | -37.88414 | 2024-12-25 03:32:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1b31792f-85a8-3976-9949-870a3f939ad3 | -8.09789 | -35.1126 | 2024-12-25 03:32:00 | NOAA-21 | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 20804c59-2fdd-3384-9982-7c75175eae4a | -12.53734 | -38.00405 | 2024-12-25 03:32:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 014d70e1-b40e-3f65-bd68-f50d545f58f7 | -10.69703 | -37.0509 | 2024-12-25 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1734e6b4-70d0-33bb-9064-140720801b1a | -20.76452 | -46.77026 | 2024-12-25 03:34:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bd3b50e6-eaa0-399a-9e45-011b23e675b7 | -3.39922 | -42.10186 | 2024-12-25 03:53:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 93d3538e-1f13-359e-813b-d6fc9a56ff1e | -3.7713 | -47.14333 | 2024-12-25 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 343d00f3-3c69-38ba-bf78-7dcd78b76618 | -5.20072 | -37.29224 | 2024-12-25 03:53:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aa2a078d-e0a4-37cf-a4d3-483b512722ec | -5.47578 | -39.66235 | 2024-12-25 03:53:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7bf942d0-31a6-3c78-a016-a577a43dc7f5 | -4.20411 | -44.54657 | 2024-12-25 03:53:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 84c5682b-a2ea-3ca8-b3e4-4328ef315a15 | -4.76996 | -40.46453 | 2024-12-25 03:53:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ac6fa542-b9c2-378e-a1ce-e06a2b3d39f4 | -4.42176 | -43.72036 | 2024-12-25 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83ed7316-50ba-3eee-92ea-c6395917c564 | -2.94594 | -51.4845 | 2024-12-25 03:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af832138-bb43-3666-be47-ea7570edf845 | -5.47522 | -39.66585 | 2024-12-25 03:53:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2d1d132c-a33c-3302-b822-3c923d6597f0 | -4.12567 | -46.70651 | 2024-12-25 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55d1efd6-94ad-3286-a779-5096502b6a57 | -3.78226 | -41.60982 | 2024-12-25 03:53:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9a02af83-6197-3cf2-838c-87b3d5ae89b9 | -3.7699 | -47.14398 | 2024-12-25 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 644be52f-eff0-3e2b-83a7-e293823c93c5 | -3.92098 | -47.19016 | 2024-12-25 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83f0d927-dd06-36f1-beb5-56d2679ad85a | -2.94258 | -51.48817 | 2024-12-25 03:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5446a86d-4b73-3a9d-ba4b-c8bd9e66a394 | -3.70378 | -38.95256 | 2024-12-25 03:53:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README2.md)
