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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e09418b5-9eea-37ac-ba61-f2548f34f09a | -3.96635 | -48.12043 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9654d2b1-ccd4-3405-b217-6c0bc8513e22 | -3.554 | -53.30914 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04b41f3d-e8bf-3c77-bd4a-91f6c5b2ab7a | -4.11974 | -48.50294 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d246a65b-1569-3269-9003-36a60fb00aa9 | -2.81529 | -54.09033 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f6f2ae5-eb14-3b14-b3ba-60af1204523d | -8.41568 | -44.13067 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 541173f6-583c-3005-8c9d-0d0a8b6e9bc7 | -2.83648 | -48.46473 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5ee7995-50e9-36e0-9028-75af5af7072d | -2.56524 | -50.67823 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6be892b5-c37d-3bf6-b9ae-9cd630f76a3d | -2.7286 | -49.17002 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 938dfa17-3071-31d1-9887-e25fc79d7a57 | -2.47196 | -50.48271 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c271a86a-596d-312c-aaa7-e5fe8fd3ea28 | -3.03337 | -48.05375 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0b95c06-3685-3d59-ab1e-9903e7c45177 | -5.89925 | -47.42594 | 2024-11-10 04:38:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 17b9ea2c-c3c0-3266-a6f1-a65080c5d5e6 | -4.04288 | -48.28184 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 788b894f-8dd5-39f4-8781-8ccaf05d6c52 | -3.79827 | -47.471 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43407189-de3e-3fb2-8a6a-df30464eb862 | -2.43093 | -50.51852 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d995f1f-0265-3dda-bebc-adf7a62c5b78 | -4.35977 | -47.22806 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 862b3b6c-2a35-340b-a4a5-ffdf667c499e | -3.19799 | -46.509 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f81a3f1-d0e5-3415-9722-9a9cd5a7235b | -2.84479 | -49.44633 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63e22d51-c0fc-3d35-813f-465f92a1598a | -2.44582 | -48.96978 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 142620fe-cb81-3110-853e-39756154a9b4 | -3.30179 | -50.13971 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b489f32-c002-3c19-bb89-a6378ab4ff9c | -2.57321 | -49.81709 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d23d5e91-9443-3ede-8e6b-bce8d2fa7127 | -8.39323 | -44.10729 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b2748aa-a1a2-3ca8-b58c-073d981f930a | -3.23289 | -50.43958 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 941efcbe-b82e-3e16-b07c-edce1ba535a3 | -3.621 | -54.79504 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31418e57-6eed-35a3-aa5f-15789bf41781 | -4.36827 | -47.26297 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e97eeb4f-ba73-3a2d-9036-e938ee22f1cb | -4.2125 | -50.62462 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d07e74c3-dc85-3d4f-96cf-9851cd65c61d | -3.22929 | -50.67858 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5e83bb1-a442-3801-8907-aa01d102b2fa | -4.85198 | -46.98118 | 2024-11-10 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8d29939b-947d-3d31-ba76-df7de5cf31d8 | -3.29641 | -52.95392 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2775f4c7-099b-3fdb-993a-53113e92883f | -2.93057 | -51.48444 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 831a8d90-9c6e-35f8-ac44-3bc1518c695e | -2.39076 | -49.8473 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28965702-b684-3a36-8980-c1d92a0a30e0 | -2.30227 | -50.46793 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c6549b8-cf40-38a9-884c-6f067cc76c25 | -4.63119 | -49.08546 | 2024-11-10 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 089a7fd8-2ffb-371f-b77b-50419af9d640 | -3.99223 | -46.41522 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d383bdb-48b4-33f1-b575-1aebf5cb6ff6 | -4.49568 | -45.69691 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78390f4c-a9ed-3330-848d-58c9b44a8548 | -2.45059 | -50.37234 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 48dbd066-4ac1-3da5-b7a5-5573eab0fcb6 | -2.24493 | -53.77077 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fe18087-ccf5-3985-991b-882a818f54e0 | -3.5619 | -53.94052 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| baf742c5-ca30-3f67-a94e-455ea3e960ee | -3.21594 | -50.39161 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cfb4768-9877-3bb8-a54f-44b11bf2050b | -3.16043 | -54.48553 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 544a5597-2eb3-3ee5-a2fc-d45bb8594b4a | -2.8057 | -49.34697 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9fbaae13-fadf-35c0-9d73-a6d18ba6c2c0 | -3.04552 | -48.04144 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20a774a9-f506-387e-b28b-b9c1564ea134 | -5.19709 | -48.34718 | 2024-11-10 04:38:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28f61bda-d864-34b6-864f-38550bc441cd | -2.22715 | -53.7756 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1b7b62e-2e16-3c2b-9878-d99ee11f06bf | -4.50029 | -48.49552 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4817e5d2-d96a-3f40-a8ce-0c13f9ba1bf6 | -3.95648 | -48.98334 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a26f522e-f827-306b-9091-2cf10abd3329 | -4.37557 | -47.53353 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbb12a11-28e6-3ab7-bd9b-1dfa8fe833e9 | -2.8751 | -49.44011 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 287235b9-5c61-310e-8cc3-7ccc51b28d8b | -3.65024 | -49.96302 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13cd9c44-3321-3afd-8a8f-e2b0105169a8 | -3.8726 | -51.98339 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 451d65c7-de90-3be4-8d38-decabe51f75b | -5.20094 | -47.47449 | 2024-11-10 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 051dad64-6cb7-3a06-8cb7-c1f49f6ec158 | -3.1064 | -45.78176 | 2024-11-10 04:38:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99f2c9b8-1ef9-3949-96bf-1a9a01d85a13 | -3.69611 | -47.64062 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07718c1a-c61f-3cf1-98bd-20bbeec4711a | -3.95317 | -48.16112 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d6fe7e0-ab1f-3872-9dd6-4311c088c6e8 | -5.56221 | -43.97091 | 2024-11-10 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| da7d6a23-568f-399c-bb27-eaf68d27bc79 | -6.48341 | -47.50581 | 2024-11-10 04:38:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3f45f8d-3364-32c8-9024-5b20ab00bc23 | -4.49473 | -48.48755 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32e52273-0755-3944-86d3-07b85967347a | -5.13667 | -46.1854 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dab3099c-058c-329d-938d-d3230231d4cf | -3.04116 | -50.32685 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 497d2d60-f2b6-3c69-b8de-ddb37069a3e2 | -3.41192 | -51.40793 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7c35d89-53aa-3dd5-b04e-ba0b6c4610df | -2.84535 | -49.44283 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65aa28aa-b370-34f9-acad-3997225acbe3 | -2.83573 | -46.63862 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ce9161b-dc7b-390a-96c5-80b002b80dbb | -6.23316 | -44.1399 | 2024-11-10 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32c8fa57-48df-3564-9ce9-497f218dd474 | -4.12306 | -48.50346 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f1f3718d-0066-3b6e-9cb0-bf00b6d0ef7a | -4.38374 | -45.86341 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 41574ee4-d1f6-3db3-85ae-00b331afe974 | -2.4595 | -49.89491 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aaf0ae45-54df-387f-ace6-c2388795a324 | -2.4614 | -50.39308 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f21cd06-5302-3e96-8083-53f6d089107d | -4.01776 | -43.66274 | 2024-11-10 04:38:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa7d7185-0cff-3b48-9d84-c5f07cd083dc | -2.29022 | -50.97255 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c61513c8-c706-3af0-89b6-f68d3aed040a | -2.72941 | -51.71554 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3d42738-703a-30b8-83a3-2139026aa8c8 | -3.22655 | -50.28072 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 3d6158ae-e312-3f3a-9714-fef1d1bd4dac | -3.96819 | -48.17416 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05409181-ec1a-3285-9041-6aef81b07999 | -3.95186 | -49.40135 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6ebb83e-e11d-316c-8c74-136867b0dc12 | -3.30634 | -50.13303 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b44e44ed-ed8c-3c81-a779-8c4d0d6fc1d1 | -3.83388 | -54.59475 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c313159-0219-3f94-8e50-c830a5a6a76a | -3.14371 | -45.9576 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69d0f09d-37cf-3b73-9b52-8740d507ba42 | -2.6331 | -54.65856 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ad2ff2d-420f-3a12-b76a-dd7bf2340ac8 | -2.69907 | -51.69544 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 907e1fa6-a003-3571-a720-3d91e050aa80 | -3.88487 | -54.6475 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c697b729-68c1-3d26-8917-e326eb3aad74 | -3.95593 | -48.98679 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8bea45a-0247-33b4-a864-26173d2c42bc | -2.69933 | -49.33333 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 558dffdb-d47d-37c7-964a-1b2d3a6e66cf | -2.93805 | -49.43201 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f799cdcc-0327-3ade-9722-ab1b0893fd7d | -3.05295 | -49.52181 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50cb75f8-a3d0-3d20-9083-1245c8c02e41 | -2.86406 | -51.83109 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3b63cc33-a075-30e8-90a8-d54832b807ae | -8.69112 | -47.96369 | 2024-11-10 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eeb7715b-4135-3350-9b5e-4eba9aa2c0d0 | -2.60753 | -49.18698 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 695fc175-50b1-37fe-950f-e2a44cbe2a88 | -3.24457 | -46.47379 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7b9faad-8f51-3d07-a26b-71d0f9fb0c6d | -3.95093 | -48.15364 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 67da2899-61e2-3cd1-a63e-699b8d25b350 | -4.18779 | -49.98539 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0f83169-1dfe-3d9b-92cf-442f87e3aa68 | -8.53697 | -40.97358 | 2024-11-10 04:38:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ebf582fa-b163-3c81-9f66-b54d268096f4 | -2.6641 | -49.90437 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a104112-aa95-322f-ae3d-d9510527a126 | -4.82826 | -48.51826 | 2024-11-10 04:38:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f16851a0-bc90-3bab-9476-8a0f96992777 | -2.89463 | -49.51149 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f9aae10-7205-3594-a63c-d9290c29881c | -3.6513 | -49.96289 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e40dcaf1-ba35-3910-a7f4-07b12c064589 | -3.53684 | -50.32897 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9b987c3-20a2-3306-a888-1dd8bcf7c014 | -3.09624 | -48.05982 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 777f3d73-0b5e-3103-a1f1-2a2098510e19 | -2.12763 | -50.67508 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efdad2fb-d0cc-36bc-bfa9-319344dabf69 | -4.83213 | -48.5153 | 2024-11-10 04:38:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57f058aa-ea52-3654-bd6c-8cb7f7b56605 | -4.09986 | -45.70371 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fa4f240-f22c-3a77-8069-32bbf49fc727 | -3.61914 | -41.57768 | 2024-11-10 04:38:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6e005538-cbc4-3aa7-9bc9-db21b6ee9166 | -5.6944 | -47.01369 | 2024-11-10 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README76.md)
