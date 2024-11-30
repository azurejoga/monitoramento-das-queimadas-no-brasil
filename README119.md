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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8792522c-1dad-3ae5-b76d-337fe54f4de9 | -6.8967 | -43.5436 | 2024-11-30 05:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 42.6 |
| ff1b8253-5ba5-37a5-89f2-50a113d50516 | -1.6602 | -53.8728 | 2024-11-30 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 71cbdde6-032c-3983-b899-3dba32922cbb | -6.9158 | -43.5185 | 2024-11-30 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| cc3cedb1-2d1f-381e-abcf-5793f3084a91 | -6.9153 | -43.5652 | 2024-11-30 05:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| b2c71591-bc79-3ccb-bfa4-0b584dbbbaa5 | -6.9156 | -43.5418 | 2024-11-30 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 345.6 |
| 72a7151a-20f5-3cf6-b91f-1e28180f83d7 | -1.6419 | -53.8731 | 2024-11-30 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 971fc2b5-feca-3b52-be16-b914d8c81df8 | -3.2591 | -53.6186 | 2024-11-30 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c6fb3ec7-61f0-3ef6-b7d4-3f9b2cd82087 | -6.9344 | -43.5401 | 2024-11-30 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 13106cc8-2456-3422-b86f-a15a481e3f42 | 1.67467 | -50.66565 | 2024-11-30 05:25:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d78edf92-6b82-3e7d-8fce-b941f861e41e | 1.68015 | -50.66478 | 2024-11-30 05:25:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d309d7ce-64e4-3719-abd1-2369ab5bc7fc | 3.18521 | -61.03416 | 2024-11-30 05:25:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b87c270-7b42-3932-8510-3b588876f923 | 2.81158 | -51.08349 | 2024-11-30 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bff52c5-18da-3529-9c12-d7065b296bd8 | 1.67437 | -50.6654 | 2024-11-30 05:25:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6c3ed9c-1788-339f-af42-461780f37cbe | 2.80634 | -51.08438 | 2024-11-30 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 579fe02e-74a1-3487-b1e1-494fa70d9c7a | 1.67526 | -50.66922 | 2024-11-30 05:25:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7d10e1b-721e-31f8-a274-86d6fc948960 | 3.22376 | -59.914 | 2024-11-30 05:25:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1493d97-b751-3e83-9ae8-02eb80b85024 | 2.8121 | -51.0867 | 2024-11-30 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2036105-2eae-381c-a2d8-b9a543682979 | 1.67986 | -50.66451 | 2024-11-30 05:25:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9387bd8b-9cc5-34ab-9bb7-a97aa13b8ed8 | 2.80687 | -51.0876 | 2024-11-30 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7ab8790-6fe7-3aad-a3ae-c42a4d0351de | 1.67495 | -50.66898 | 2024-11-30 05:25:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57906f7f-0a5b-3708-bc0c-5fe769683eb1 | 3.17853 | -61.03519 | 2024-11-30 05:25:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ae76034-ce48-300d-992f-0da4de0493dc | 3.91566 | -60.51197 | 2024-11-30 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8494fee2-ae03-30c0-9d6b-13c746c72112 | -2.56248 | -54.31604 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 39416ed1-7afb-3849-8d98-f57b34a339d2 | 2.37158 | -61.26059 | 2024-11-30 05:27:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6b61910-9063-3294-b31e-4214941a300c | -2.97995 | -53.90134 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 531637b9-dba0-3bd7-a973-ecbd88148eb5 | -3.45288 | -54.56965 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20d33c77-a29f-35aa-ae81-8f80e52e2e8b | 0.94148 | -50.74701 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 610a1ef3-06e4-3a0f-8b05-56ac0d85531d | -3.86528 | -50.16724 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f385bfc-0b79-33a1-ab0d-fa899efc6a63 | -2.8348 | -54.10311 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a5bdb68-d226-3131-a4d4-e021168ec29c | -0.87184 | -51.72084 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ec2ceca-0dd6-3583-b59d-02ab81cd2b54 | -1.25211 | -54.55286 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ec098015-02eb-35de-b5f5-f963fdac1382 | -3.38694 | -54.28827 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04c94833-1a3e-360d-bc8b-9b58ef75a016 | 0.10523 | -51.47157 | 2024-11-30 05:27:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4afc7dba-151e-37cb-9709-e75988047e3e | -4.07919 | -50.03381 | 2024-11-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 90049483-ac43-38cc-85d4-0e5e9042a6af | -3.43483 | -59.29002 | 2024-11-30 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bde72bb-a385-3ff3-8c42-357005f349c3 | -1.88854 | -48.64951 | 2024-11-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32eafdc8-8e74-3f58-a344-dde364475192 | -1.25279 | -54.54855 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 84beee08-19ae-3982-97f3-e843aa092042 | -4.0779 | -50.03158 | 2024-11-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5eae5422-07be-36b9-a9ce-c09539e21a05 | -3.02326 | -54.0308 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c915fe97-5abf-3ea2-ac22-980af0e15dd2 | -2.195 | -50.57889 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f177e3ba-39a7-3a8f-923b-6178197e4a76 | -2.65598 | -48.79005 | 2024-11-30 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7399abf7-32cd-37ad-af9b-6ea991574569 | 1.19498 | -55.95298 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 591142a5-5581-3c9d-b520-79536ea2ab70 | -2.19869 | -53.75242 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 70bd613e-bc51-371a-96ba-85d617c45cb4 | -3.09167 | -50.3596 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5cb0798-926c-3fb5-a224-02bfb00f81b4 | -1.30517 | -55.74206 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd4b8999-33e1-3903-a3ab-e788720f3e51 | -2.60388 | -53.98506 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3146cba0-67c0-3358-9a92-54c10f74c1ca | -1.15224 | -51.70552 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6af5a03a-49c9-364c-84ec-bd7713dc107b | -1.15513 | -51.70238 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 859f3e37-0109-344c-ae2d-33c02fa76137 | -1.45132 | -52.61603 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 132ff19f-a6d8-30f4-a7a9-4d6e85766434 | -1.3325 | -52.38742 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 210694af-4b59-3852-87bd-8ed004f41ff4 | -3.01638 | -51.37039 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d01316a9-07e8-3203-9fd8-d1fc85a72f4b | -1.69784 | -52.6392 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7315e08-3471-3859-a1c3-7aa552f03c8c | 0.96978 | -50.12809 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3081059-160c-3eef-8a8b-e1dfd5931565 | 1.18876 | -55.9637 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5f0ea6c2-d909-3920-9d68-2b1dc344ba8a | -3.96178 | -50.18918 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b50e175-3896-3e87-8881-5e1388c549fa | -1.1953 | -53.87334 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4a905c7-216d-3742-92f9-ff8b2fe162b1 | -1.21007 | -55.89778 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de734782-e76b-3d0c-9275-e80cf5959014 | -3.73912 | -50.79332 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67f45876-0fc2-3303-948b-9f312c411c6c | -2.37124 | -56.1181 | 2024-11-30 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69e83a15-dc84-3a3e-91e6-9e1814469f33 | -2.56996 | -51.84093 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce22196c-f716-3612-84f7-c867da4bd61f | -1.29459 | -51.72816 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f040b00-d048-3652-87c1-a735eb24ac53 | -3.30013 | -53.69019 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab7e25cd-ee1c-3edd-b00b-3cf8435cb30c | -3.30078 | -50.37566 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e54d34e4-8103-3ca1-b5c9-47c2669b6f15 | -1.31014 | -51.734 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31257395-d0c5-33e2-9d45-27fc87a70774 | 0.98291 | -50.25461 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb2889ea-b2b9-3441-a198-49b1afaa9d08 | -2.03032 | -52.07815 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94e8542e-adc1-329d-8f59-c31b080e768e | -3.48324 | -53.80589 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 158a2e23-0fe1-3fa2-90f2-dc31b5653d00 | 0.94773 | -50.75112 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c50c29ae-5071-35bd-b99a-5f9045d0bab2 | -2.59527 | -53.97871 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 658095da-7c5d-3012-98af-42a74baac134 | -3.2666 | -51.62975 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 284645da-9ea1-3ad4-ac38-dc12333eddb6 | -1.07347 | -53.63781 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 53ed1e11-5261-3c03-8b6c-685757095d85 | -3.46765 | -50.53802 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5e0890f-9346-3f52-92db-d9c0f32df087 | -1.09201 | -53.39875 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4ab1431-e155-3ca2-9b58-11844d121e41 | 1.44016 | -55.88094 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 746f41c0-f32a-3923-9a64-ee88df3c5d27 | 0.94101 | -50.74473 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| daa3bf7b-c7e0-3d89-bd25-191a2a403207 | -2.14548 | -54.88917 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d1453c4f-2e2b-3e7b-868c-648b861dd227 | -1.59543 | -52.28361 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fa9b049-d2b0-3cfc-93cf-9ce11b270247 | -3.05308 | -54.05545 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a99c2de-fbb5-33a9-9220-70b43cd734a9 | -1.60051 | -52.29532 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99b75de1-3318-3ac3-a177-d8bf79aa23ce | -3.39333 | -50.31401 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc3caa64-4524-30f0-a101-105874fc8712 | -3.41459 | -50.16283 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7722db49-76d9-3673-af33-34a17422842f | -3.0922 | -50.34369 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c868956-bdbf-3810-85b7-69558cd301a2 | -3.67673 | -54.4505 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29777021-d55c-353d-bdec-72d944d76fa8 | -3.30267 | -53.83449 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c1df5672-aa35-3961-bdbf-94dea619bae7 | -0.95596 | -51.65719 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a447edd-7471-3bf6-8118-309faee999d3 | -2.89593 | -51.58044 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96c1fcab-3c1f-3093-bd94-dbecf3e85dd4 | -1.75893 | -53.65079 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d6d1f89-54bf-3992-a720-f2181cc68e4c | -1.33437 | -55.84865 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b491bd9-d708-395b-b07e-6b4c78882e8c | -1.71799 | -52.77654 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fce96c09-aceb-36ea-97d2-74f0e16d5cd8 | -1.18532 | -51.77562 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc629dce-0841-3f4d-b3f0-95dbbe25830d | -3.48802 | -53.80675 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4533b878-b986-38be-b73c-d4c627f6e197 | -3.3475 | -50.5281 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cabbb35-3575-3ad4-9226-e6f20d6f0535 | -1.94827 | -53.34348 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40c46ac0-86df-319b-9e65-46bed99bcb54 | -3.33555 | -53.22037 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8d1b162-82c1-3fe3-bf64-dcb507cb41f1 | -3.76335 | -50.17651 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0b1f624d-c7a9-335e-848a-975f8fe0f61b | -3.14152 | -53.83362 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5f5542d1-85af-3014-97be-9185e6e5eccf | -3.09084 | -50.3526 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 06a7f62f-d05e-38a7-9267-dbdba1814b6b | -1.07621 | -53.63514 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5737d4cf-31dc-3aaa-b7ee-f369a23e25b5 | 1.188 | -55.95888 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22064874-3519-350b-90b2-79d4fb888244 | -3.18844 | -54.33193 | 2024-11-30 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README120.md)
