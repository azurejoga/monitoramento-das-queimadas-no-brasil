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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6661bed1-87fa-378c-a1b1-0d2ed427546a | -3.27542 | -50.60978 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4cac2e1a-3465-37f9-852f-0ae6271c563c | -2.79122 | -54.05342 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bc790b3-523b-3ac6-a40d-ba39dd7d2fdc | -2.60007 | -54.2179 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b37ed4f2-13c5-300e-aea4-c0b9798c0747 | -3.78625 | -50.1362 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 551777f0-8c28-396e-9248-464f07058392 | -7.22395 | -59.91008 | 2024-11-28 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5563fd86-310e-3df9-a15b-10fe3418fb0d | -2.25902 | -53.7455 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ae3f99e-6f8f-3ef3-b88a-0553bd0aadfb | -2.78509 | -53.20831 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8eca450-6603-300f-a517-e5e0d8a81977 | -2.77941 | -54.02699 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d5680c0-f59f-3544-8cb9-fccd8a5e9508 | -3.38475 | -50.1195 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df87fc7d-15e3-3eb5-9af0-8117ab400ea2 | -2.25807 | -53.75695 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8608f6bc-bac8-376f-a15f-290c466ba799 | -3.12017 | -53.10873 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db3a8646-69ae-323d-bcd4-0d56ce3836a5 | -2.31574 | -51.96302 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 30bdaa4b-a0f1-3adc-963c-38f39a9919d2 | -3.43766 | -54.54298 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23ec1cc0-3501-3771-82be-f2ed54141935 | -3.55165 | -51.50617 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 34b7a2aa-2fcd-3478-88cc-62087229b7f1 | -2.60211 | -51.82762 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90adbe35-c833-3eff-96a6-79861094e00e | -2.64265 | -54.06963 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6a57d55c-53ca-35f0-b387-bc4241b854cf | -2.88153 | -53.98996 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6f35029-b258-33e8-bdb4-e50bc66bb280 | -2.44328 | -53.96851 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6adfef7f-9a77-3f31-bf98-bd0a855677fc | -3.16952 | -48.43676 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79b2d2ce-0ed2-3d8b-8044-599338b829d9 | -3.24746 | -53.63111 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9cbcb40f-14ee-3983-82c6-47b493a7f18f | -3.09702 | -53.26591 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ae5ab98-aea2-34e6-94bc-f0afad83574c | -3.57729 | -54.51734 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5a4ea6d-95bb-3d97-bb39-05d142a46970 | -2.45293 | -53.68774 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8da0093b-22f8-33bd-8e13-5c57b505351e | -2.19719 | -53.57297 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4d1c1ee-6b56-3181-9599-b14bacb2da36 | -3.96755 | -50.18828 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 166c5ddd-e203-3788-b219-833b47fe9861 | -3.17235 | -48.43516 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c12221dd-c0f0-3f7a-8e44-1e909957a0a3 | -1.62902 | -55.70948 | 2024-11-28 05:18:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 058246da-f7b8-3f1d-9499-95da1a9bf9c4 | -3.8109 | -52.35585 | 2024-11-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5eccd40e-4b70-38a0-b949-457ceb658c64 | -2.59219 | -54.09102 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45bfd537-4c7d-3f97-bb47-c2e8e87fcaad | -3.42007 | -50.16117 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c60b720a-4cb9-375d-bbda-72bd4a5f1fc3 | -2.16871 | -52.13798 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 51bb4362-f01b-3868-960d-832a54d293bc | -8.1269 | -47.98302 | 2024-11-28 05:18:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d4aed02-e6c8-3614-a860-5c4de8e962b4 | -4.1774 | -48.62619 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8acba1f-e963-3427-8a43-f86ff77aa3b1 | -3.1133 | -53.26847 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47b3782d-4fc2-359f-9fc7-aa7afd742fa5 | -3.23874 | -54.22272 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b83ec526-6ed4-35db-986e-31865e535c47 | -3.10092 | -53.73142 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 680bbc7a-a209-30da-a548-d098a57e2666 | -3.81031 | -52.35989 | 2024-11-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a13ff7cb-9e55-376b-acbe-c97c8d9ca6b6 | -2.75356 | -54.12077 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9df8bdde-faa4-3c28-b7c9-b7528bf4577d | -4.10749 | -48.24799 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae8b369a-06d9-3625-9016-d279003ee48f | -3.63475 | -54.44561 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a55be909-a870-3528-8611-b1177291962d | -3.39693 | -50.70316 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8e4f2510-687f-3924-8179-37b855fe438a | -2.75599 | -54.13084 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e1a7cd87-a1fa-3ca9-bc71-bc50c862ddc5 | -2.83881 | -54.02622 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 83149de7-9c99-3d6a-985e-d7b88c28f884 | -3.29801 | -50.36067 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe217164-9c80-322a-9306-9e78677f9cdb | -4.18906 | -50.67848 | 2024-11-28 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54f390a9-d539-38d1-9331-fba1f1b30e1e | -3.69083 | -54.20699 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19e41a59-97fb-3ff8-aa6e-56abaa20fba7 | -2.81528 | -54.07671 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f60f4a63-56a0-3fe7-8fcf-bbf16c988b83 | -2.7905 | -54.0582 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3481f67-496d-38b5-8857-78421afb1851 | -3.26404 | -54.10896 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99928190-86f1-36d8-97a7-6fd00b171c28 | -4.08641 | -48.81881 | 2024-11-28 05:18:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eeffad9b-5bdc-34b6-9cd1-634c9d62a7ad | -3.2499 | -53.64222 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 393ff31f-bc39-327a-945b-d6569136c14a | -3.29898 | -50.3568 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e6d1cc2-84a2-3dfb-871f-54bd17e375e2 | -3.2917 | -53.66233 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a938f050-b3b0-34b9-becb-7b25011dc0d1 | -3.08994 | -53.25744 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c566ba34-f7be-3a7e-b115-1a782070eb7b | -3.06291 | -53.21691 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93ce98d6-707c-30a5-90b6-c188fcccdab4 | -3.60226 | -52.54308 | 2024-11-28 05:18:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 694947dd-42a3-3aad-b2f6-b9caa54a5b7d | -3.24643 | -53.63814 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6caac9fa-146d-3ddc-959f-650504041174 | -2.64103 | -51.90071 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69fd650e-c4f1-32af-9e34-1fc24c41bde3 | -3.50404 | -53.82576 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9412477c-2efa-3450-9c88-bdcd692e8071 | -3.37925 | -50.12161 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dcf4f48-e0b2-362f-b5a1-fcd3cf50a3db | -4.0324 | -46.54128 | 2024-11-28 05:18:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 855d6773-f0b1-3632-8134-194115124244 | -2.92675 | -51.44786 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53cfc0b2-a159-3d3f-b1b5-1a3d70338d13 | -1.74288 | -55.44648 | 2024-11-28 05:18:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6f82c40-f088-3879-aa89-397d2035f850 | -3.96457 | -48.08869 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 7261ae70-dd36-398c-b434-e349b7da341e | -8.56489 | -49.20438 | 2024-11-28 05:18:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acbfaa6b-f827-3455-b5a8-bb4b38eccfa4 | -2.98339 | -53.89554 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f485f994-d7f0-37a0-9f74-9176c1a2b366 | -2.32142 | -51.957 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 65450b51-6b75-3b96-aa42-4632ddb0e893 | -3.17448 | -48.58018 | 2024-11-28 05:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2f7f5f6-6b8a-3927-ba21-98ae54e73790 | -3.96519 | -48.08452 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 5e21709a-9ed6-3042-a7b2-49cd9ae0e10c | -3.02905 | -54.01937 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 403e8bf2-d30c-3a61-bb50-efc99de3c404 | -3.65248 | -51.39431 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 828b9674-fe47-30d3-8a49-dc73fed63c5b | -2.96495 | -51.00787 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c103bb33-f6c8-3a26-875f-becc3c54b6c4 | -4.65731 | -49.52231 | 2024-11-28 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5999136e-0e0a-3b8b-b72b-c42dc04a4405 | -3.04812 | -48.51602 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71cbb383-65af-3d98-85f0-5813bd83919b | -3.18424 | -48.43308 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3258b6b-d69d-34bd-b790-1a41a835dd21 | -3.04867 | -48.51223 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d4766e5-396c-3229-b188-930b784de2e5 | -2.94652 | -51.5346 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ad33dfb-c25e-3040-b497-64772a937ff1 | -3.04621 | -54.03689 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48d87781-8a82-3e6c-a5b5-56439282f82f | -2.93155 | -49.43695 | 2024-11-28 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5067cd99-b0c9-31a8-9c71-447a1282f746 | -3.38266 | -45.84332 | 2024-11-28 05:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 29.9 |
| d7cc5ecd-6969-390e-af89-d2b080cb1adf | -2.80956 | -54.03655 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc4de2b0-006b-3e07-953e-5582d437ed7d | -3.27663 | -50.61771 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 82eb3804-b82d-3a09-a404-c99a7d1947f9 | -2.80643 | -54.03116 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50187abb-29bf-3a7f-9a01-7878e054dce0 | -3.16837 | -54.63224 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99634bcb-9d6a-36bd-8313-abcc35e05ed0 | -2.78944 | -51.74313 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c8ba1df-088f-3964-8500-eae81d357df3 | -4.6578 | -49.51889 | 2024-11-28 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a35d1558-8dff-3738-96bc-d1baf990f966 | -2.07581 | -53.39865 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| deeab1e1-06d5-32ba-a685-251086cf3259 | -3.10758 | -53.81926 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 1ebe49fe-2970-35fa-82e9-de384cb8da3e | -2.85873 | -53.99967 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 66e8d715-eca7-334f-ac13-afe68adbc0d4 | -2.42008 | -53.8236 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5a7319c-bd8c-3cf1-858d-040cd36c8ff9 | -3.55914 | -51.03403 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bbdadc9c-0f8b-360a-94a6-b313fa24f660 | -3.28969 | -53.83641 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11d5e964-9574-300c-8e04-360be1e86c22 | -2.76651 | -54.11303 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94a568cb-0004-36b6-9c4a-8d9825f664dd | -1.84338 | -55.56954 | 2024-11-28 05:18:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52bcf6aa-0da5-3623-9864-2a42a4d99613 | -3.12072 | -53.76028 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f34e48cc-cd51-3437-ab80-4bbdccd5c001 | -6.09342 | -48.04344 | 2024-11-28 05:18:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3004026-7b07-3f6d-96f0-5821500d488b | -3.24267 | -53.9352 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00b33ca0-29ce-3c49-a125-7f51dfd4cf90 | -6.49039 | -47.88978 | 2024-11-28 05:18:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dab7ae80-dba4-312d-b98f-d9cf651bc4ec | -1.99784 | -54.15078 | 2024-11-28 05:18:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e05ad68-a290-3f69-8655-0140a1586666 | -2.43743 | -50.41739 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README91.md)
