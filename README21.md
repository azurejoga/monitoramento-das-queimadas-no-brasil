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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d15dadd1-cc7f-3cc0-8544-9d5fc67d9ce4 | -4.46831 | -43.22978 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 986a3e59-a407-37cc-aeef-083226d04076 | -4.98491 | -48.47669 | 2025-11-06 04:44:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48674f84-a64a-3059-a3ac-3be2ca69fd3f | -5.93047 | -43.52289 | 2025-11-06 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f46c0ed9-7ecb-354f-9e98-9ffecc9ea662 | -5.39723 | -43.9352 | 2025-11-06 04:44:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1626b0aa-305c-3834-af3d-87beb78b888d | -6.20662 | -43.27238 | 2025-11-06 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 950e2fff-04ac-3327-bd2b-21c031251141 | -3.08961 | -51.20064 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98fd977c-f64d-389b-afd9-c6d660943dbd | -3.11285 | -51.03198 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 713988b9-cfc4-3886-8db1-dbafeeb9b52d | -3.58394 | -55.50979 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1ef802c-a9f1-35d9-b794-741d2a5108b3 | -2.78962 | -50.31827 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf6e051f-b8cc-36e4-9816-635836f0e7c9 | -4.21721 | -55.69875 | 2025-11-06 04:44:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae379176-e70a-37b1-90f5-bf7fd9127898 | -2.97664 | -51.2259 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 757550db-1c36-37f1-9112-4578aa9d8a23 | -6.21381 | -57.77517 | 2025-11-06 04:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7413dff8-28f3-3190-8f23-ad9563e5df79 | -4.18681 | -52.09832 | 2025-11-06 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0b3f755-fc66-356a-a611-f4aa51bfe397 | -4.69414 | -49.62643 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27a1a451-0b83-3285-96a4-7668730747d4 | -4.64709 | -50.9291 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab21f16a-c2ad-3653-a688-2f929acd4a3e | -4.95058 | -48.56289 | 2025-11-06 04:44:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3f2cabae-4962-3a45-aad6-fa052bcf5077 | -3.78289 | -49.42731 | 2025-11-06 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a0066f8-4bd4-3725-b330-5c6e81313275 | -7.839 | -40.84203 | 2025-11-06 04:44:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ee991e6a-aa89-338c-9bf5-b8d34f074916 | -3.40858 | -50.83949 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7bb2122-cf26-3483-9af7-3948fedbee7b | -2.89423 | -53.13287 | 2025-11-06 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b42cfb14-2720-3e5b-931a-c76100a9b17a | -2.98016 | -48.70567 | 2025-11-06 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51c83f4b-9d54-34c9-a6fa-f611574b0d70 | 0.43167 | -60.49028 | 2025-11-06 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4538a2e1-1acb-3ed4-9466-360b61897b37 | -3.61559 | -43.5379 | 2025-11-06 04:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 43b4adc4-4ce7-36c7-ba78-46c51362a01c | -4.14402 | -54.91906 | 2025-11-06 04:44:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14a0ec98-3d7a-3f29-bb7a-a53dbc87053e | -5.59959 | -45.18388 | 2025-11-06 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57967c4c-fa59-3535-b57f-66f2913a5dea | -3.47319 | -43.64698 | 2025-11-06 04:44:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c31b37e-2a51-3a68-a292-fd3e59a99f8f | -5.76344 | -40.8224 | 2025-11-06 04:44:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fc35eae5-3e10-36ed-9c44-50dfc69ec7e7 | -2.88316 | -52.61169 | 2025-11-06 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 613e13a3-d311-31ac-8df1-bb6905f67069 | -2.90113 | -50.47359 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 42f1721e-98ef-339f-9296-050b26688bc8 | -3.40912 | -50.83603 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c7cb189-bd62-376b-923f-9018fdcd0ae4 | -3.01292 | -49.60853 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8436932-1cc2-326a-94f4-999e6088f602 | -1.92384 | -56.62319 | 2025-11-06 04:44:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e056cc82-bf8b-3ce5-8a50-37a72746d88f | -4.23408 | -51.08727 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a02f656a-fb9e-37c8-b12a-65ca4764d8e7 | -4.58931 | -43.33335 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75fe6d25-3093-3547-91fb-756f2c20dde2 | -6.12111 | -57.71176 | 2025-11-06 04:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20ebd2a5-e054-35af-b0f5-77c44fd4b136 | -3.92494 | -47.68848 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b05c565b-b851-3f1c-b38b-8ae6f53bd866 | -5.24137 | -44.38985 | 2025-11-06 04:44:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83193e2f-63ea-3c43-abe0-4631ce35d269 | -3.90344 | -51.28534 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b5dc158-c440-3568-a929-3b36dad8f99f | -6.33729 | -52.07623 | 2025-11-06 04:44:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cba996c-15c8-3eb6-8944-22fccf25b0b5 | -6.34063 | -52.07675 | 2025-11-06 04:44:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83d14688-1392-3145-a541-530e898b8ed8 | -4.57678 | -50.44226 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24c66d68-aa48-369b-9909-f181ac02efc2 | -4.43208 | -50.60565 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b65ab9b8-87f1-3401-a0e7-f0dc0a2e3a2f | -6.03747 | -45.79239 | 2025-11-06 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2171bd5-bc31-34df-a784-25af73c18ccd | -3.70543 | -49.90376 | 2025-11-06 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c7d98e8-e433-3623-9e1b-b8c64c1b9548 | -3.92845 | -47.68901 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 86e97478-90ce-39dd-a4b9-896f5525e415 | -4.10768 | -48.01852 | 2025-11-06 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b61ac58b-1ddd-3c7f-aa44-6323aafc3e13 | -3.82406 | -51.35563 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f549b31-9e7a-343d-92f8-a8a43b74acb6 | -3.41976 | -52.77253 | 2025-11-06 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96cc7750-38d7-3e4c-940e-b6abb60c163c | -4.60091 | -46.56053 | 2025-11-06 04:44:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ec6b118-e099-31bb-8230-fb7296fbaa78 | -3.9289 | -47.69276 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fbe631e7-d0b1-3ba8-bfb4-72f102ae80c3 | -3.90399 | -51.28182 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4568203-d622-3b68-b662-2006895f6630 | -3.22617 | -50.93913 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ecbd8ed-58a3-3fd5-9e0b-dd2fd1ed5d95 | -3.71107 | -53.37642 | 2025-11-06 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f63e075-d00c-3e15-bfba-e8de7d79b1b2 | -2.99262 | -44.18118 | 2025-11-06 04:44:00 | NOAA-21 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 95d74855-80f0-3880-927e-fdc48aac834d | -4.20704 | -48.40231 | 2025-11-06 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89d22533-cf4d-33b4-9a47-7a854b657ca9 | -5.15301 | -41.27212 | 2025-11-06 04:44:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 49b98f60-cb79-375b-96f5-66c9fc6676a9 | -3.77014 | -43.98549 | 2025-11-06 04:44:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8124eb9c-34bb-38b8-b6bf-dd3fcc4cf092 | -1.6239 | -54.70883 | 2025-11-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c736308-aa4f-385f-b140-8452cab71e5e | -1.63879 | -53.71774 | 2025-11-06 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 907d19d2-fe1f-3303-bd1a-54430e0664ba | -2.39554 | -57.66103 | 2025-11-06 04:44:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 046ac571-7bc0-3914-a104-3b2e5856f1ff | -4.14322 | -54.92395 | 2025-11-06 04:44:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 534c503f-553f-30c8-b8ed-583a716237fc | -3.77611 | -51.25101 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 153113d2-cd5f-30ea-acc2-37941c09bdc7 | -4.46438 | -43.22418 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d236ff86-b218-3c8c-bfb1-3017bb89b388 | -4.85407 | -40.63303 | 2025-11-06 04:44:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ee0ced3e-7888-3bae-af4d-dfdafa6e0312 | -4.60374 | -49.5513 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8c11558-c448-3ed3-8c30-d0c2220dff25 | -4.4913 | -45.92894 | 2025-11-06 04:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2ac5a59-0a57-3904-9cb4-0cfb7fac7c45 | -3.7714 | -51.81789 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aee1ea6c-4ec3-3600-9f8e-a87a10497419 | -4.49527 | -50.74646 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3a499d6-9115-3833-b585-bc8585e59c10 | -2.98443 | -51.35019 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca87daf4-9611-3256-8ae2-842268ee4f50 | -4.67525 | -50.44361 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5cd5ba34-33e6-34a1-8025-ff9a5ad761de | -3.11964 | -51.20528 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| adc65242-0567-3c8e-ae76-ce8e06df86ae | -3.7588 | -52.07312 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be7e0643-6c9c-3b6d-aadc-90713068fae3 | -3.61308 | -43.52368 | 2025-11-06 04:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7d96906d-9557-3884-8086-8029d5524cdc | -5.46502 | -44.68754 | 2025-11-06 04:44:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae1c4e60-fe11-385b-8cea-e5f999d7d37f | -2.89813 | -48.06176 | 2025-11-06 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 639782c5-ea3f-331b-8686-55711ce9d95a | -2.96923 | -51.53399 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39f1b89d-a202-320c-8327-4e5382fe3581 | -3.43306 | -42.54538 | 2025-11-06 04:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c17be91b-32d7-3cbe-8347-812fac9cee72 | -3.78014 | -51.67578 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 374032f3-faf2-31a8-911a-4b33cf079d9d | -2.07356 | -45.64093 | 2025-11-06 04:44:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2208552a-865d-3fc8-a240-98ead8aef591 | 0.44925 | -60.48279 | 2025-11-06 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c143505a-743a-3a5b-aeb3-d6cd3f17916f | -3.76576 | -43.98484 | 2025-11-06 04:44:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a9dc303-7ac0-3a4d-ab93-4c0704f08c66 | -2.61629 | -49.22839 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9faf207-6bfc-3d87-86a1-f17ca047762e | -4.8814 | -47.54882 | 2025-11-06 04:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21adaddb-a7b3-35e2-809e-df5b39372de5 | -5.7644 | -40.81559 | 2025-11-06 04:44:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d506556e-a673-3778-ba96-78d7e6992beb | -4.59989 | -49.35696 | 2025-11-06 04:44:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17bf40d9-3bda-3283-ad04-a9f5f84734e3 | -4.63907 | -42.18063 | 2025-11-06 04:44:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0c9ac8f0-b3b8-3fdc-b95e-286ae687e26d | -4.60042 | -49.55077 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2e90fdc-e08e-34e5-9650-1a0b1f87f2dd | -4.58782 | -43.33588 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d00430d7-9695-3f49-a28d-a57b4f45223a | -2.87904 | -52.61504 | 2025-11-06 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c8a42a5a-b899-3893-bfd3-6de34fa89426 | -3.92602 | -47.70456 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5663a9c-1309-35a2-ae4b-ba3623cf32d1 | -4.21672 | -48.3622 | 2025-11-06 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1521a15a-fa87-310e-b740-e56d883c2c1a | -2.98352 | -48.70618 | 2025-11-06 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c9f79e5-7e75-36e7-b61f-e4e8695803d0 | -3.44814 | -50.02147 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 581ed05b-fc7b-3197-83ec-a0bafcfc6e63 | -3.00901 | -51.39037 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd7a1706-47ad-36fa-95cd-3629844e0fe0 | -2.92672 | -51.30865 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e3c1abb-aa53-37dd-bdad-3c5585b94bf6 | -4.58851 | -43.33101 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e43a1480-109c-3807-8477-7cd338172ae5 | 0.44242 | -60.47915 | 2025-11-06 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39d4fb43-cd0a-35ea-8d56-41f11f4f8310 | -3.77446 | -51.71155 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0075d0e-2e49-3e07-ad30-b89ee70af3e1 | -3.70236 | -49.0053 | 2025-11-06 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a81d9510-dd87-37f8-9cd8-45ba122dd520 | -3.84436 | -49.09612 | 2025-11-06 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README22.md)
