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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8a84672-a154-3ea0-97a3-d8d3a56ca06a | -1.63247 | -52.68937 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fee0a127-4711-3965-960b-1394e1e33832 | -1.57929 | -52.92695 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4daf646c-87ba-3565-b1ab-b4ac1e365634 | -4.62814 | -45.56973 | 2024-11-22 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe979218-cbf3-3c92-b740-b703ad02bb46 | -1.71329 | -52.49031 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b084fb36-b5f7-3267-a92e-e9196b781e93 | -3.23701 | -54.24986 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9094cf69-9cb7-3c14-8391-67a3c91ab54d | -3.28288 | -53.82868 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65132ccb-7aa5-3570-ae8c-061290401c5d | -1.26483 | -52.06909 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac7eadd1-efd0-3802-9625-4ebd7fceed45 | -3.46769 | -45.90712 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 43d51a7c-817f-3376-942e-6253f1f1406c | -1.51641 | -51.18468 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0aead2c2-98cd-3960-872d-b4f47b42018c | -2.60399 | -48.29139 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cc172f5-3c84-3a43-ac19-e6f1cf8cfc0a | -2.5675 | -46.55131 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b05e95f0-4dc0-390d-9ecb-1011cc7953bf | -1.1287 | -48.35913 | 2024-11-22 04:36:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d4e6de9-76ae-3726-8aa8-1568051c658a | -4.9787 | -49.82338 | 2024-11-22 04:36:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6d04dc3-9e31-3c0c-8882-857b000e9ecf | -4.00749 | -49.92893 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88babd22-f7f4-39e9-9e8c-663a630b0ee4 | -1.44553 | -53.56437 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0e73fa9-820c-3ade-b59a-38882693c8ee | -1.77712 | -53.60159 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fab13e0-79b7-39bd-aaa2-d9fa30c0559f | -1.20992 | -51.97054 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fbb5b754-d986-3ab0-9f91-014775db5779 | -2.42877 | -46.5187 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa39255a-2ed3-3398-a0ff-a11362c4c0e5 | -4.14358 | -49.21655 | 2024-11-22 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74755e84-5699-33b7-8830-f4ad77391863 | -3.74994 | -52.33094 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c930e288-63fb-3ed4-81d8-c7b37099bb74 | -1.45712 | -47.61125 | 2024-11-22 04:36:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb907e45-e92d-3de6-a801-4e208f5b6068 | -3.29456 | -53.8599 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6890358-efec-3726-b7c5-9dbf8b70d51a | -4.73555 | -46.66815 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b46c2cd-c754-3cc1-88ce-de9b52e22389 | -1.63911 | -52.62162 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23ac8a79-7810-3ab7-bbe3-07e3c9d2e2cc | -3.83616 | -52.25928 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9eb1d7eb-3baf-3349-a0df-5abdb2b64b27 | -3.22989 | -54.24072 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9918988a-7223-3949-9ffb-db0bb2107649 | -2.6968 | -51.3682 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1289d5c-e77e-3d80-8c76-94602cdf6af2 | -4.21217 | -50.69556 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebc39629-0021-3d8c-a33e-53a7ba7565f5 | -1.23845 | -54.01999 | 2024-11-22 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbe61d95-5f2c-39e5-96cf-1a0c0038c166 | -4.13312 | -54.65944 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d566f23-690f-3c7f-99bf-286c79c38de7 | -2.67138 | -46.23919 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfb8c759-4ab5-3361-b0b5-2717831c4f6d | -5.24131 | -42.63289 | 2024-11-22 04:36:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ce11b300-f5e6-34f6-8445-c1b311b174c0 | -2.14981 | -50.91524 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d87f7417-1b81-3e46-b485-f74a12ffdbac | -3.64104 | -54.32483 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e8cd506-7baf-3c14-938f-b07d0754f9f6 | -3.22386 | -54.25174 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 82a7aa77-4adc-30e5-bd04-4a8e1803897c | -2.52021 | -48.34869 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9dc4b09-bfb7-3d2a-98a3-5a13a160fd0d | -2.09788 | -48.89492 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b41cd185-d146-36de-b29c-9214b1730a9f | -3.23112 | -54.23302 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 31ad12a7-0d91-3619-a7f8-c5d7b2f627be | -3.83112 | -52.26725 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad8ada94-86de-309a-8909-2a99cf656216 | -2.36325 | -46.73521 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90d6cd59-c6e0-3cac-b212-785000adc743 | -1.17255 | -47.58451 | 2024-11-22 04:36:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f98726ef-ef91-398a-949b-143af8ba05c7 | -2.72523 | -46.09794 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4725a4d1-9ee5-3181-9923-d0702c736f3c | -2.56486 | -46.15702 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7ee734a-58d1-351c-b438-7312e9a48a81 | -4.00971 | -49.91488 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 15b7c3da-7a37-3513-82c6-d83f5e4308c3 | -3.0787 | -45.96519 | 2024-11-22 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7276912-0f81-31ff-81b5-992912e97f4f | -1.57811 | -50.43483 | 2024-11-22 04:36:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88dc831a-8d67-3e74-982a-1bc7619f1fb6 | -2.60716 | -48.24964 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19f528ef-a187-3528-9421-a7b1cf48be4c | -2.69916 | -46.24339 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 738d1f2d-d0e2-31ee-afb3-09ef7a0ff697 | -0.1897 | -51.55405 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c266ef7-a828-3334-a164-e1719cbea0c4 | -2.82884 | -49.15146 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b9f743c-98be-3fa7-b66b-beb84d239289 | -2.6968 | -46.25864 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b112cc57-40e8-3f66-a68f-fdd3c3db4667 | -0.96844 | -51.71552 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 676e5f1e-837f-3af0-b485-7439b8193e6d | -2.50533 | -49.00465 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a1e029a-b291-3e77-9521-a91c7fb0cf9f | -2.60136 | -48.32972 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5594183-1d2d-34dc-b69a-a678e96d7249 | -3.57562 | -54.51649 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e9a3b80-cb39-33b3-ac1a-d3e8c160fd1c | -1.33072 | -47.96238 | 2024-11-22 04:36:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 965e7fed-b77a-322c-9536-df5b2a0cf28a | -2.16807 | -47.95189 | 2024-11-22 04:36:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6427eb5a-d0cf-30d0-adf4-fb86bae17cc8 | -1.26791 | -51.59729 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 872fb6f6-c467-3046-9cdf-1c5a11486ab5 | -2.62788 | -46.56762 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c61c621-fe25-3ff0-aa49-6cc5a3cebc38 | -1.21491 | -51.9743 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d34fe7f-f5b5-3f1d-a447-962d55a761cf | -3.25638 | -54.24456 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1243031-3ec5-3998-968d-6b9acd6d7407 | -6.27127 | -44.55077 | 2024-11-22 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8bc02d78-f0ea-3a4c-8ce9-59434ef7e80e | -3.66062 | -51.56932 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc811f1c-c9c1-3543-8a64-ae2ea5729ab7 | -1.26109 | -52.0685 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab3b8b79-fade-3d4b-a0e4-877c95f1d09f | -3.71685 | -52.09326 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ce21ec8-e1c0-3ce8-ba54-79eff31eb1da | -2.92187 | -46.8418 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcd96ff8-8d6e-3963-ab71-a01afe289bfa | -3.66138 | -54.65545 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f08d78ad-207b-3ef6-8c1b-bf7b612d5463 | -3.21439 | -53.84005 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8606619c-c81d-3ef4-812f-2f24bdd36e31 | -2.60823 | -46.19896 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87110135-b33d-3276-a9b9-4a272791e637 | -3.14754 | -51.12965 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0eade4ee-1953-3cab-bf4c-e502bb5ddfbb | -2.78894 | -52.06439 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3ec7a88-5896-3da9-9e27-f2f14b26644b | -2.44186 | -46.54729 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ce53b08-27a2-3a2c-834c-ce092f9546c2 | -3.46288 | -45.91461 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3b91c61-5542-3c7d-b069-72cd6610daa4 | -0.9464 | -51.64131 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 221c85e9-a3f9-330e-9355-b21755eba790 | -2.69906 | -46.08203 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e887f36-22ee-36fb-ae5a-4eadc2ee21e0 | -0.26246 | -51.54183 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1337ca58-5baa-309e-b2e4-41c23fe5a42c | -2.0173 | -51.1766 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a25f263e-f6c7-37fa-94fd-576e4eb84a6a | -3.45641 | -45.90953 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90390723-56dd-323b-8a9a-cd92a0197a65 | -3.76195 | -49.93341 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e2f081b-ea86-3024-9e5c-facfa38445f8 | -3.18108 | -46.54716 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52e91202-22e7-3aca-a459-a6e3b34e8591 | -1.17532 | -47.58848 | 2024-11-22 04:36:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9040b57e-a4ec-3e47-b47d-dbde1c1e03f2 | -4.35777 | -48.6123 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ee1cc29c-71e9-3836-b25c-e705363f4e6f | -4.08383 | -46.85024 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34ef845a-5481-3a91-a426-b858df57b7a9 | -3.25566 | -52.85334 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2c6279b-4fec-372e-8779-72097cc8974b | -1.14202 | -53.66951 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f717959-1106-3b83-bfa8-071752c159f3 | -4.3995 | -44.11868 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3f9447d-5fc3-3698-afa1-b6bc0a548d78 | -3.18395 | -46.55145 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd1ff221-1b48-32b0-9f54-fd629f730b34 | -4.70046 | -46.07434 | 2024-11-22 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17268e6e-966e-3116-b569-91c017d19f2e | -2.90136 | -48.32438 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d3564ee-99a8-3a37-b27e-453faca94af9 | -3.63686 | -54.32426 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4aaf10b8-1936-37e5-82cb-cd7e2100f23d | -4.53611 | -46.62291 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5fbb8b6-7fee-39fb-a187-b712de47b7b9 | -1.42803 | -46.80052 | 2024-11-22 04:36:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6f6ea56-19b7-353b-9aa7-b8dde0da2437 | -2.02084 | -51.17715 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60446e18-5041-332f-84ef-4fd50d193247 | -3.19422 | -54.32969 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24b918fb-4ca6-3bb3-81ca-7f84b242e377 | -1.43809 | -52.68045 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddb2213c-f747-3b30-a1c8-abf5afd250b6 | -3.19904 | -54.32644 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd41733e-8946-3935-8ce6-e49768b8fcaf | -1.12844 | -53.40913 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 027c9b2a-1396-30ff-8016-bc7834c24c8a | -2.28196 | -46.5611 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e72e5300-3113-33be-b4da-639150b1bc68 | -3.57499 | -54.52038 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea06374a-d831-3d9e-a11e-1f5c7f8193f6 | 0.44236 | -50.77535 | 2024-11-22 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README45.md)
