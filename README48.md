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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd5e4c1c-07ac-38ff-806a-aabcb9025902 | -2.86461 | -53.96393 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed8cbb9a-53c2-30d7-a489-2837bf478f73 | -1.2336 | -51.74533 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e4f539be-c267-3143-bc09-787f984407c3 | -4.12624 | -53.97598 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e402e492-0f31-39a2-83fc-4c8d4cb7434c | -3.75872 | -52.41124 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a94848c-9ea5-3980-bc3c-f9220a8c32b4 | -2.52359 | -46.40713 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e40322e0-fcda-3dbf-8876-5090c5989c1e | -5.81253 | -44.74689 | 2024-11-22 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84fd30db-de12-3b72-ba38-fd97fd4bad36 | -6.19925 | -37.43758 | 2024-11-22 04:36:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 176a0e4a-629a-3c20-a677-a49949254f19 | -1.11331 | -53.39931 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b1042f0-639d-37f2-9508-55544f17d48b | -2.37446 | -50.38957 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 477c1909-d309-387f-bb92-9fedd27c6542 | -2.63661 | -46.19943 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5d68734-4126-32c1-9eb8-4407f871acd6 | -3.46739 | -51.12308 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dd1764e-caac-30d2-bbeb-5ccd20b5b175 | -1.19737 | -51.97764 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3038b4f-f09a-3abe-b467-3bde5f60f2a4 | -2.07262 | -50.32445 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f4e912a6-bed7-30dd-b19c-cc97c0bf35f0 | -1.89932 | -52.68381 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26e2d6cf-7e2e-3077-bfb8-24d6b8c4ebf7 | -1.51899 | -52.08438 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e29bfb0-a8c3-364d-96de-af40bdc94444 | -3.76044 | -46.11941 | 2024-11-22 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 539e0e5b-5ecc-3157-bc91-bcd73abdc81a | -2.45731 | -53.70108 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89400a43-a8b2-348f-960e-025ac2c2f227 | -2.38665 | -50.3349 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e819ed12-dec8-3696-9b11-029ac9e3edf6 | -2.78667 | -48.10149 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc79584c-aa57-338d-820b-488168c65de7 | -5.00593 | -45.51925 | 2024-11-22 04:36:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c569da5-3fac-3654-9a7f-923b4bcf7208 | -2.70034 | -46.23576 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2273b2c-2b0b-3c5b-af1f-9d09daf7556e | -3.64233 | -51.45626 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5e8853a-fb65-3b36-aa15-37a833ad0538 | -5.93282 | -43.78674 | 2024-11-22 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d9c410e-6eaf-3b19-b7e0-6d27acca664d | -6.19446 | -37.43962 | 2024-11-22 04:36:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7c3898e2-9169-3e42-afd8-564213dfb125 | -3.06586 | -53.2259 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 027b7148-5602-3ebd-a4a6-08a776c9e86f | -6.504 | -42.18862 | 2024-11-22 04:36:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7b72e739-8aa6-3ec2-a131-66f1cbe53f7b | -2.69321 | -46.84821 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9dc0541-6e6a-38a9-ba1e-18284e637690 | -2.68945 | -46.19104 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cba0eb19-456f-3d89-a36f-2f32d665275b | -1.26757 | -52.12488 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b95a551-fc54-32c7-b921-60a9cde46458 | -2.11471 | -50.34621 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25c383bd-0887-32e5-8a54-87d50011a01e | -2.44075 | -46.53193 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f69d5ba-62e8-3794-a7ec-296aaccb5b2e | -0.34524 | -51.56129 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f8dda410-80db-38b1-a354-f3a757b02855 | -3.7947 | -50.25914 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a62e7df0-6cb0-3cf9-b201-23ed80db8ccb | -4.18164 | -53.5813 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f9ea0d3-7bf7-3baf-acdb-f481aea33367 | -2.64971 | -46.13853 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11a1dac4-443a-35c3-b128-b186d117a78a | -3.23208 | -53.63209 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bd9cdc1-4d96-393f-be5a-93e8fefe251e | -3.43801 | -42.54671 | 2024-11-22 04:36:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 782198c5-46fb-30e5-ac9f-2116c5b369f3 | -3.0067 | -51.30873 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6dabde3-e258-39a1-b6bc-c38be13b19fb | -2.17185 | -48.40321 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecd78121-d9d0-38d3-8920-42cecb995b63 | -3.6739 | -51.21332 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6b47cf6-1bc7-3ab8-8d92-b149532641e0 | -2.27913 | -46.55689 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dd57c96-1193-3c04-9a11-09877909a276 | -0.9597 | -51.72304 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3964949f-f9fb-3ca4-9d49-96a84af6fc7e | -3.04701 | -54.41058 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23dec606-29f1-3cdf-b3f7-f9cc17603946 | -0.63824 | -52.35393 | 2024-11-22 04:36:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 594119c1-20ee-332d-bc6b-62aa7837dea1 | -2.36268 | -46.73885 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30a16538-c52d-34f4-a39a-e37c3969b1e6 | -2.58179 | -46.54968 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad641666-dd13-327f-acf4-19b79a78f296 | -0.7982 | -51.49046 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d772c40-7fc1-3f5f-a547-4a48800edfa5 | -5.08851 | -49.624 | 2024-11-22 04:36:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 191cd052-4f17-3aa0-a647-793ef33a99ba | -2.68532 | -46.8768 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7639e150-7297-3060-9ac4-15efc10c7aa1 | -1.44739 | -55.52116 | 2024-11-22 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5dd23c90-8794-3ea2-9c1d-be211237e510 | -5.81351 | -44.74443 | 2024-11-22 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44bc3054-a542-3912-9894-1b7bd9f6e687 | -2.24996 | -48.42632 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2763bef7-d6c9-3225-a1db-c99720c7240c | -2.52182 | -46.2835 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d876d1e4-e18b-37da-b395-47b61e08d0aa | -3.44078 | -51.6051 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97ff3e6a-db21-39b8-a8d2-8f316487f725 | -1.12902 | -53.40553 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 896414f9-d000-3b00-89e6-32e7db22fe44 | -2.6371 | -46.21906 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35bf11d2-13d7-33f2-9b4b-3d4b7b7c0d0f | -1.66215 | -50.19309 | 2024-11-22 04:36:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c264696-b21b-3445-b892-fdb0a970f5e3 | -0.87031 | -51.89071 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2f32f3d-3a1a-3dd6-811a-eb8c04629fe6 | -2.33628 | -53.93124 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ef43c0f-3d5d-38a9-9df5-42608f0b7f1a | -3.22865 | -54.24853 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7af5ff17-e412-3415-9cb5-4b5dfea81d11 | -4.83549 | -48.641 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 315bedbd-5c18-3980-b1d2-7d9757782e81 | -2.6594 | -54.26225 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1124b07a-59e2-3ef2-95d5-29110cb9d641 | -3.27937 | -53.82457 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f3928120-af00-33d8-8c07-43d016effb74 | -0.97949 | -51.71724 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23c02e75-2922-3324-afe4-dbecd6ba10a8 | -1.88057 | -48.78652 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc2f7844-a504-3dc1-9dbb-1fd497d3afcf | -2.67906 | -46.1659 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12ea58b9-97d5-3576-9d94-8bfd2650da94 | -0.04859 | -51.23643 | 2024-11-22 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 710ca9cd-af93-36a3-b667-530f7a80692e | -2.39777 | -48.61092 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c41d2968-4b72-39eb-958a-f224b50b8971 | -1.12437 | -53.40849 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8a8664b-4a3a-31a3-8b33-7ee1f013a9ae | -3.61729 | -44.04953 | 2024-11-22 04:36:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e56ad07c-1b87-3776-afcf-7d5933cc97ac | -3.55361 | -51.53678 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1effeb14-1710-3c72-beb3-09e00e7dd99a | -1.72658 | -52.38297 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 073dd946-43e1-31be-bbb4-b8454bc1cc87 | -2.3547 | -48.55869 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3bdaccb6-8771-3048-930b-6394be097c42 | -2.83717 | -54.01286 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6581e1a3-4d85-344d-a5d0-a786b47cff31 | -2.27329 | -51.13826 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 672cb93e-2bde-35cb-b6e1-bec1645f9516 | -2.83658 | -54.01661 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68db3009-bc58-3f87-b6ca-ca28f5334db3 | -2.55095 | -46.54494 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8645f46-59bc-3dec-8526-9ca6408ea408 | -3.83043 | -52.27158 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1854389-5f17-395d-b21d-f44dccb210c2 | -1.05044 | -51.81177 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 033ae106-dfe5-3589-96ed-bd9dd0521057 | -2.5031 | -48.99724 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b110465e-5648-3ded-a37f-3fcf88798a88 | -0.91284 | -51.73975 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 13cb5081-3e22-3dde-98b5-b7bb9147491d | -3.75724 | -46.11588 | 2024-11-22 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92d84789-1038-3494-b47f-8baeeaac7abf | -2.63601 | -46.20327 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0360ce61-c7cb-30f5-8a47-17f2b45296c7 | -2.56088 | -54.06688 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b83669f2-4c32-395d-9ea9-b8f225f5edf9 | -0.79455 | -51.48988 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93fe4722-5843-340d-9af6-373bc5248a61 | -3.95575 | -51.13465 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bb783d8-f9fd-3436-a54c-7643c98d380e | -4.01851 | -43.99089 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 106067f8-bbe6-3b15-a42c-70935b68bdaa | -3.33989 | -53.73693 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fb7559d-0dd0-3c85-9c29-3d3ed91dab3e | -3.50786 | -53.80295 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 56db5753-17f1-3845-9e10-71363d267b55 | -3.8887 | -46.66386 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38906277-4c44-37f3-b1f2-aa46d82c5af0 | -0.56893 | -51.73591 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec610ca2-d4ce-36d2-8002-8d3b82ce0314 | -1.52183 | -52.08232 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c22075c4-cc5d-3c48-ab6c-958ad78453eb | -0.05221 | -51.237 | 2024-11-22 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 40.2 |
| db9a4a28-8177-33f6-9b2e-189fb4ffa681 | -5.95618 | -48.05523 | 2024-11-22 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9f35fb1-bca1-3b7a-ba20-0380cb800e7c | -4.06782 | -46.84024 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 984417ce-84e9-3a50-b12f-0b4cdfd8fb73 | -2.44607 | -48.94945 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d70ba2d-bba1-37ac-90ce-4b091ca2d738 | -2.42819 | -46.52241 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dfe3725-cd32-330b-b43e-b253478b6675 | -4.81975 | -43.6923 | 2024-11-22 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44df9260-2a69-3dc0-8f4c-640a4d266719 | -2.68639 | -46.25704 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a667908-bc27-3d7e-8b0d-584f561a5603 | -0.26576 | -51.56903 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README49.md)
