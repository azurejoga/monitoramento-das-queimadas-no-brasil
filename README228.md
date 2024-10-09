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

## Dados Diários - Página 228

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baf4684d-859e-3520-b14e-99aaffbd0fab | -16.9094 | -55.8014 | 2024-10-09 08:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.9 |
| 9c34288a-cb70-31a8-bbaa-ea46012ead05 | -16.9091 | -55.8222 | 2024-10-09 08:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 6d153055-db66-382e-a6b8-e9b3c61f094b | -17.3266 | -41.8428 | 2024-10-09 08:36:42 | GOES-16 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.2 |
| 73068bf0-9983-312e-8891-750384721214 | -17.1467 | -56.8463 | 2024-10-09 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 0039eb55-d6cd-3d88-bfeb-678d760f6240 | -17.1471 | -56.8256 | 2024-10-09 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 5aa3a932-a29a-3bf7-a08d-53ffe43b6261 | -17.0795 | -57.3674 | 2024-10-09 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.9 |
| 588c3d07-e304-373f-b0d9-a093e6a79ef6 | -18.1394 | -56.3686 | 2024-10-09 08:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.9 |
| 2b4e7421-0b23-3fd9-9747-1ac479f1a6c0 | -18.1391 | -56.3895 | 2024-10-09 08:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.7 |
| 4dfca0ec-3799-369f-88b3-b49527911b79 | -18.1196 | -56.3713 | 2024-10-09 08:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.7 |
| 4f90d965-9c96-3174-9434-bf0d2d24437e | -18.1193 | -56.3921 | 2024-10-09 08:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 169.6 |
| 771e4b21-e004-31cf-afc8-1935bdaf33e8 | -10.4287 | -60.9979 | 2024-10-09 08:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 7633a6dd-ff30-3658-87ff-f205c2c507ad | -10.8755 | -63.8979 | 2024-10-09 08:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 32.3 |
| b47b0408-67a7-3f0e-bd0f-0ff15625f04d | -10.8754 | -63.9169 | 2024-10-09 08:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| f21fbd7f-25b9-30c0-a315-b8a48e64ef82 | -13.398 | -61.9182 | 2024-10-09 08:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| eead0bfd-04d6-3811-a554-21cd70c53538 | -16.9287 | -55.8197 | 2024-10-09 08:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| efb8e72a-801e-3612-b5b3-f19ec6de2f68 | -16.9094 | -55.8014 | 2024-10-09 08:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.7 |
| 92509c47-000f-3a4b-b77b-a59347a3a40c | -16.9091 | -55.8222 | 2024-10-09 08:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| b6672f8c-26f6-3333-a8c2-42a488bf2039 | -17.3266 | -41.8428 | 2024-10-09 08:46:42 | GOES-16 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 118.7 |
| 3eb6ad49-d411-3449-9d1b-760353371e2c | -17.0799 | -57.3469 | 2024-10-09 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 8f6a231e-0c1f-3ce6-964f-dc316f588b42 | -17.0795 | -57.3674 | 2024-10-09 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 3a483492-1d1e-3e35-b202-c8fa3419a7d1 | -17.1471 | -56.8256 | 2024-10-09 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 3f93a87b-1669-3dfc-9b07-213f794a0ef9 | -17.1467 | -56.8463 | 2024-10-09 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 34c502e3-d3e0-36f8-9297-3e71e36e67a0 | -18.1193 | -56.3921 | 2024-10-09 08:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.7 |
| baea246a-36df-3247-b883-13301cd344cc | -9.4435 | -67.1008 | 2024-10-09 08:56:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 59b0fbbe-5020-320d-9c0c-0527aaa00d01 | -10.8754 | -63.9169 | 2024-10-09 08:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| d487ba76-7301-3725-bcfd-eb40f2b2c529 | -10.8755 | -63.8979 | 2024-10-09 08:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 41c87407-db2f-34c2-9aed-ea05e8427fde | -13.3978 | -61.9376 | 2024-10-09 08:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 25.3 |
| b25cdc44-5617-3628-9cba-425b5d7df3df | -13.398 | -61.9182 | 2024-10-09 08:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 25f90121-7371-353a-9f2d-1ead6091be06 | -17.3266 | -41.8428 | 2024-10-09 08:56:42 | GOES-16 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 125.3 |
| 619bd476-5630-30d7-a734-70ceb670b588 | -17.0 | -57.48 | 2024-10-09 09:03:49 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f02e0de8-7a24-3d1b-b238-af2130e8cb60 | -17.15 | -57.44 | 2024-10-09 09:03:49 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0527bd32-0ed6-3a51-9bfd-8eb22ec06633 | -17.18 | -57.46 | 2024-10-09 09:03:49 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f3870fb9-2ca9-3c8e-a9e1-a08893e167ae | -10.8755 | -63.8979 | 2024-10-09 09:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 32.7 |
| a7056753-6e32-3bc3-8686-10442e0a2b53 | -10.8754 | -63.9169 | 2024-10-09 09:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 02230c08-c78a-3b0b-9887-1b07899311e2 | -12.878 | -62.8007 | 2024-10-09 09:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 24.2 |
| aba8f1ed-3ce1-3d63-be45-a94c925cebbd | -13.417 | -61.9169 | 2024-10-09 09:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 8ddffc6a-998c-3aa9-acf6-163def90e55c | -13.398 | -61.9182 | 2024-10-09 09:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 7808b38f-453b-38bf-86ce-2f98f9fbb05f | -13.3978 | -61.9376 | 2024-10-09 09:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 27.0 |
| ce982e41-a034-3c94-b811-d16e51963b9f | -10.8754 | -63.9169 | 2024-10-09 09:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.7 |
| c6e1a04e-a536-31c4-b697-4b84c6bacfe4 | -6.7798 | -60.0552 | 2024-10-09 09:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| f9e19c0e-5fd4-35c0-bfa7-449a0af72300 | -6.7798 | -60.0552 | 2024-10-09 10:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 61fa8ee2-02bf-3c22-9d01-498a2a83bb52 | -6.7798 | -60.0552 | 2024-10-09 10:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 57a862b5-60f8-320f-8616-aa539621d7b8 | -16.9805 | -57.4404 | 2024-10-09 10:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.3 |
| ad32179b-a54c-3cb3-a10e-9d31964022e5 | -16.9609 | -57.4426 | 2024-10-09 10:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 169.0 |
| 4313036f-155a-3110-baee-969979528006 | -17.1571 | -57.4198 | 2024-10-09 10:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 242.1 |
| 7a66d715-0b83-3ff3-a0ea-124432c4150f | -17.1568 | -57.4403 | 2024-10-09 10:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 508.5 |
| 367692b9-b9f6-3b25-846b-adb10b4cad3d | -17.1564 | -57.4608 | 2024-10-09 10:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 146.0 |
| cdc8f4d2-ca6d-390f-9e9e-909ccd95ce21 | -17.1767 | -57.4175 | 2024-10-09 10:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 235.0 |
| 24931512-750d-3e8a-984d-f6f5b7908598 | -6.7798 | -60.0552 | 2024-10-09 10:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 1f3b1008-8b10-3af4-9a0c-f50dcdd4b330 | -6.7798 | -60.0552 | 2024-10-09 10:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 23adcef2-15e0-3861-bbd5-d70737d41947 | -13.9353 | -44.5046 | 2024-10-09 10:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 9c4d90ea-4a6b-3efa-985c-5087599cebb3 | -13.9158 | -44.5081 | 2024-10-09 10:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 7c2c3918-3ca8-3161-a3c6-ae819d949779 | -17.1767 | -57.4175 | 2024-10-09 10:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 258.0 |
| de61238e-2504-3043-8a1c-8f92188a2682 | -17.1764 | -57.438 | 2024-10-09 10:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 404.7 |
| 5ebdf50c-b295-3150-a864-96115bc4e536 | -17.1571 | -57.4198 | 2024-10-09 10:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 286.3 |
| 7b6d195a-315c-3bea-bee2-eb0280c09466 | -17.1568 | -57.4403 | 2024-10-09 10:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 560.9 |
| 4270e673-d29d-3128-87a8-8f36f157f38b | -18.1193 | -56.3921 | 2024-10-09 10:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.1 |
| 07af708f-b390-3d39-91a8-a3bc4d44ac2b | -6.7798 | -60.0552 | 2024-10-09 10:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| cfd885b6-6d2a-3e13-8190-b66f342d140c | -13.9353 | -44.5046 | 2024-10-09 10:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 248.4 |
| 82772d9f-5f95-30fc-bc29-0587b8c218df | -13.9348 | -44.5282 | 2024-10-09 10:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 8ee5007b-b7eb-36ba-ae7c-2205e6295fff | -14.0782 | -51.0945 | 2024-10-09 10:46:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 853235e5-19f1-39f3-b560-b18db63737c8 | -14.0975 | -51.0918 | 2024-10-09 10:46:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 77fbe2d2-8826-3a21-b028-40089e02ee2d | -16.9995 | -57.4791 | 2024-10-09 10:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 254.6 |
| 9a3ffe25-b2ba-30ef-b29d-0bcecc4781cb | -17.1571 | -57.4198 | 2024-10-09 10:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 263.0 |
| dc01d121-e5c1-365f-90fa-eb0d2f308064 | -17.1767 | -57.4175 | 2024-10-09 10:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 239.9 |
| a0c97fd2-1927-3d35-a7e6-619f5ce64d74 | -6.7798 | -60.0552 | 2024-10-09 10:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| aaba5b59-9c2b-30cb-b8a8-4c58e3b50a60 | -14.0975 | -51.0918 | 2024-10-09 10:56:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 6c33d2fc-9692-31c3-9ebb-a914920dfb46 | -14.0782 | -51.0945 | 2024-10-09 10:56:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 5febc0bb-459a-3a31-88e2-0dfd59d1f0f9 | -18.59 | -57.25 | 2024-10-09 11:03:39 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7a0fc54a-aaeb-3886-ab7d-d2fca17cf895 | -16.96 | -57.46 | 2024-10-09 11:03:50 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 21298e20-3072-3da5-b555-05515737f24f | -13.94 | -44.53 | 2024-10-09 11:04:03 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed27fb08-b8a2-32e1-8237-ce3b09ebe308 | -13.91 | -44.52 | 2024-10-09 11:04:03 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cd29a132-8997-3354-a316-cd43466ef79c | -6.7798 | -60.0552 | 2024-10-09 11:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 22167f37-f568-3b12-8d2d-511593efc413 | -13.9158 | -44.5081 | 2024-10-09 11:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 161.5 |
| a9105ef7-254e-381e-a050-21d5c7c3b941 | -13.9353 | -44.5046 | 2024-10-09 11:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 377.1 |
| d3d585e4-de6f-34e3-8956-3270538abd24 | -13.9348 | -44.5282 | 2024-10-09 11:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 17449059-63de-34fc-af33-792efbfef7ae | -13.8963 | -44.5116 | 2024-10-09 11:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 322.4 |
| f00e857d-f6ac-35ea-b1d5-5d402cbe8c1f | -13.8764 | -44.5386 | 2024-10-09 11:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| dfd6ef1d-87ab-3bdd-bd2e-40039c2eb772 | -14.0975 | -51.0918 | 2024-10-09 11:06:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 8463ae4c-bf7b-3da7-bed5-74f176c7982e | -14.0778 | -51.116 | 2024-10-09 11:06:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| efaa980a-ad05-3bf9-8e7f-038ad762cd93 | -6.7798 | -60.0552 | 2024-10-09 11:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a9a6bede-7f7c-3f04-9bdf-5a716cfe0d0b | -10.5746 | -48.0178 | 2024-10-09 11:16:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 25483264-baeb-338b-bf07-9c2348df9f7c | -14.0975 | -51.0918 | 2024-10-09 11:16:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 128.1 |
| e8f597fa-3581-382a-9987-87cc503e73db | -15.7076 | -59.3726 | 2024-10-09 11:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 134.6 |
| ab9ce389-e2c5-30b9-a478-d61363fc63df | -6.7798 | -60.0552 | 2024-10-09 11:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| befdeb42-c028-3234-bf84-9f176d4f6d6d | -10.5746 | -48.0178 | 2024-10-09 11:26:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 54a03a95-6dcd-3408-83a4-669652f370e9 | -11.9729 | -51.0575 | 2024-10-09 11:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 209e2bac-3c40-3d37-b14c-4cea9a2e3b90 | -13.8769 | -44.515 | 2024-10-09 11:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 3b70164f-1cc8-3894-89b0-46e0d53c1cc0 | -13.9353 | -44.5046 | 2024-10-09 11:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 242.7 |
| 08fd56c7-a382-35ad-be8e-275d9aebd847 | -13.9158 | -44.5081 | 2024-10-09 11:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| bc37757b-19e2-36a2-b116-939572e824ca | -13.8963 | -44.5116 | 2024-10-09 11:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 1226232b-b4e3-3a25-a8cc-00d083d86d7e | -13.8958 | -44.5351 | 2024-10-09 11:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 0ae624a7-79b7-38d2-b374-79bd9f2f60d4 | -13.9348 | -44.5282 | 2024-10-09 11:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 5df4fcc5-5635-3c55-a47d-1b3c56d72416 | -14.0971 | -51.1134 | 2024-10-09 11:26:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 34d94c52-88b5-3cd1-9b73-ba906045cb85 | -14.0778 | -51.116 | 2024-10-09 11:26:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 4fbb3709-4ec3-3d5b-9ea0-9b2e4f97ec0e | -14.0975 | -51.0918 | 2024-10-09 11:26:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| f775de76-09d2-3286-ae63-5f8204080ce0 | -15.7076 | -59.3726 | 2024-10-09 11:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 82b5076f-fdd6-3790-96b1-3b5a7646c5d5 | -15.688 | -59.3945 | 2024-10-09 11:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 880b589f-0f07-3b7b-ae75-33a60abf0202 | -15.6882 | -59.3745 | 2024-10-09 11:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 204.4 |
| c321af78-2183-3f62-bc10-8d5b1f63afb6 | -16.9094 | -55.8014 | 2024-10-09 11:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 99.8 |


[Clique aqui para ver as próximas entradas](README229.md)
