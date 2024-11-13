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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65899ed0-2200-3d2f-a34e-75c1b608f87d | -1.33492 | -51.4128 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4a93032-1029-3958-94f7-871186be4df1 | -2.99602 | -51.03554 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d6befd14-91cb-3ad7-8873-380967b74c9e | -3.2474 | -50.31822 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5cd03e4-e9a5-3367-9c46-00d81490fe4b | -1.18812 | -50.56392 | 2024-11-13 04:57:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4350068a-6b04-3fce-a733-d22c7b7ce326 | 0.5591 | -51.67077 | 2024-11-13 04:57:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cea2433-01e2-3fec-bc86-b1572bba674b | -2.39901 | -53.73061 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d9b2096-68f4-3394-afba-1d4e4f783861 | -2.23363 | -46.4389 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b362af0b-dd52-32f8-900e-0d18db0745d5 | -2.78905 | -51.4011 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca854807-0492-365a-adc2-a44cd0f9b860 | -2.29715 | -52.20086 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54ba3c92-83f1-3a22-9492-6f2333cd6a41 | -2.41862 | -49.40113 | 2024-11-13 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ed4e371-0b6f-3d94-952b-58898487a534 | -2.92343 | -48.06574 | 2024-11-13 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11994ba9-58d3-3cc3-8b57-7d7acb0c86da | -1.81818 | -46.14453 | 2024-11-13 04:57:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 062a0df0-9625-33ae-8266-ef490d167557 | -2.87522 | -54.21099 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a69493ba-25de-38d6-8e13-5556072a735d | -3.7287 | -45.94877 | 2024-11-13 04:57:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7df41f9a-d811-379b-a682-73e4296b73eb | -3.04404 | -50.32471 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac0a287a-ed80-3083-b942-e9e623b40ce1 | -2.5612 | -53.97803 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2dd2e25-b095-35d0-b019-35744595bb51 | -2.67108 | -48.66568 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86ac53c1-4da8-3b1b-a87e-cb041a01c61f | -3.52935 | -54.48769 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 948b4d73-ff72-3bac-aace-804148c6ad7a | -2.15299 | -50.90874 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f89a80e-d7cd-3f70-9f2c-c01b9c3b62b6 | -1.03269 | -52.30428 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36486b6f-6312-3780-8f82-cccc6ac4e708 | -3.50053 | -50.83996 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3821f94d-65b3-388d-9e94-bac3b9c80f66 | -1.3322 | -51.86371 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4ab5d82-efd5-3ed2-843e-9d45a519de75 | -2.17579 | -48.54741 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9b7269a-e292-3849-9cba-2577d6d56108 | -1.22186 | -51.78479 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24b940a3-ce78-38e5-adaa-f842beca54c9 | -2.75956 | -54.03706 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc7ae54f-b202-355b-a369-6234e5a148b7 | -2.97839 | -45.16253 | 2024-11-13 04:57:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c6e3e318-c428-351a-b541-32af39250433 | -3.23395 | -50.45415 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c59c735-66a7-3900-8eed-c436c7a6dbbf | -2.35645 | -53.67838 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae1f299f-aa67-318f-b19a-5d9c8c269c98 | -1.38513 | -51.56594 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 934a4936-748d-38f1-acac-253015f585d4 | -1.63022 | -52.22475 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc41ab03-819a-3e68-b597-a3a4decf5a31 | -3.17116 | -50.4531 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a89f3795-2900-37e9-afc7-86052469bab3 | -2.31173 | -50.67793 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 893c5cc7-b202-3f71-a09f-804a9f09898c | -3.34549 | -54.18568 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 751a54b4-2013-3474-874b-4684498d36ff | -1.49945 | -51.14484 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02a3931e-a9c8-31b0-8cae-953c917f2d8b | -2.40637 | -48.4827 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 525f5850-1623-3c4a-8ac5-121c5201d5e4 | -2.99178 | -51.4554 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2febbfa-66b1-387c-8cf3-d2d1f4a46104 | -2.20072 | -51.87535 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7efac08-ecf6-3c22-9d95-67dbe8f3dba8 | -2.62381 | -54.27425 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2ead74d-3d97-370d-8cc0-5c88d3e2be26 | -3.62399 | -54.79525 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 13c4b994-2be2-3e00-9330-a7c782bfcc49 | -1.71163 | -52.46642 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 185c2354-5733-35d6-a93c-2ca75522a902 | -3.43612 | -50.30915 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69b4a0f0-bfa1-3778-bf27-ac72f44c70ec | -2.79079 | -48.08564 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d3e8b4c6-fdca-3ec4-aec1-99eea36a09d4 | -2.782 | -50.30119 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 600cfc68-35aa-367c-b524-966e920dd665 | -2.24779 | -49.32502 | 2024-11-13 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 04390f04-5885-3278-86ca-7dea62cb56cf | -3.0739 | -50.32825 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c93688b-126e-38d8-93b6-c0d81ec6bb77 | -2.06312 | -53.40049 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61487996-8e9b-32cc-9463-a5b36a2a34bf | -3.40459 | -50.36964 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a43af33b-4740-3692-b345-633cf5c642b7 | -3.81655 | -51.26189 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc4378a2-3aaf-3495-8cda-c5f4327309bd | -1.50645 | -51.9303 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e46907b6-5de6-38cc-aaf9-7f7ea77db0fc | -3.95342 | -48.1853 | 2024-11-13 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a043334-ffc1-36fd-9831-6f69b17b78ac | -2.43625 | -51.57459 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1006631c-168d-3577-8d5e-f7a8a78c4bef | -4.26457 | -48.1862 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b74ddcc-3f7a-36be-b3fa-1a74b1b60278 | -2.5822 | -53.99537 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a769b1fe-43a3-30ac-9ff6-b673cd8d6da8 | -2.93587 | -54.10735 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52e779be-69c8-3242-a9c8-f521252a8fc4 | -3.23977 | -50.6693 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5654479d-4c73-3e56-a0b0-d4ecca321f25 | -4.41238 | -49.64005 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 395b9ffa-472c-3c94-a9fd-73342a7845c8 | -4.27187 | -48.19531 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a90685b-3841-3260-a370-60e49a2d5fdc | -3.45425 | -54.0966 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2fa9ee4d-4d8c-3881-8723-c1732725d705 | -1.57533 | -53.73542 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45132889-9153-37f0-8f2b-0a11c06fc054 | -3.06963 | -50.33191 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 48d163c8-ac89-3c79-9f76-4cbded8d6689 | -3.49697 | -50.8394 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 848b44ca-b7b7-3e10-94bd-d4d76241723e | -1.64991 | -52.53526 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c799ca1d-f607-381c-9526-328a6244774c | -1.42079 | -51.11032 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a832d351-0554-36e6-b0e3-48c0df06dcf5 | -2.14975 | -46.40504 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1bf2b66c-829a-3c02-a8ca-3e898df24573 | -2.68758 | -48.66469 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1100351b-3d7a-3915-8b92-b5da4916ea57 | -2.70412 | -52.90893 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15571a2e-d517-3a25-ad3d-48e2e0165751 | -3.06156 | -50.33172 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b9396a43-dd8f-3ac1-a7f3-d8a2a1281e08 | -1.03809 | -48.84605 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b022b3d-b044-35e7-b1e1-51a8b4c2e244 | -2.46668 | -53.97337 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9cf3725b-6a09-334d-9de3-c227e85d4318 | -2.79193 | -54.00325 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3806f74c-3c4a-3189-add1-662eb47842dd | -1.39156 | -52.35966 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a622eff2-49cf-3e99-96c2-d8eb0e7a0a6b | -2.83804 | -53.97226 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ede8a4b1-7a92-3c3a-a0c5-f0b7bacf295a | -2.93474 | -54.28763 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60a7ad6e-1c3f-3a7c-b2e0-22f82f18bb26 | -2.24231 | -53.75558 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 334dd9e5-e165-3bc8-9dc2-fa63b67fea29 | -3.34826 | -54.18964 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fd7fb92-d102-3df9-bf6a-28b45abbc896 | -1.39838 | -52.07339 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68957431-3a56-32bf-835e-36f70f6bcf77 | -2.12881 | -50.68895 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f85b4dcf-ec78-3b20-8b85-50ebd207dbd7 | -2.93629 | -54.45142 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a8d2bf4-30ce-30a7-8730-c085cdc47409 | -2.74791 | -49.35268 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2c61133-578e-31fe-a76b-c2042f1498a6 | -3.04637 | -50.33373 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f0267270-a112-3f2f-9eb6-c3078ee38fe0 | -3.05 | -50.33428 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e7cd9eb3-53dd-39bd-9330-ea32f35678c2 | -2.57736 | -54.02637 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d964a9e4-6da1-33a7-b4a3-47f502c53460 | -3.28855 | -54.76431 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a30664b-6cb1-3046-a33e-fbeedc3e30ea | -4.65586 | -45.12844 | 2024-11-13 04:57:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b2d0f49-e980-397e-87dc-597d05d174e7 | -3.04934 | -50.33853 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bd5e354-4998-3623-8235-274be98be4d7 | -2.99251 | -51.035 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| e6e11187-319a-3402-9f1a-0dea7a89d37b | -2.37645 | -48.5176 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2876f1a-8ee6-314c-a5ef-5e6ee4040c70 | -3.70223 | -52.28376 | 2024-11-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54ff1600-4dc2-3b6b-bd6b-d0cc822e08f2 | -1.42309 | -51.11382 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8c1ce0c-1a7f-3995-8981-7f1b0ae77005 | -2.78816 | -52.87212 | 2024-11-13 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e7be2bb-864f-38ce-bb43-7ed407a3c42e | -2.87731 | -51.83273 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dcd6d91-432c-3292-86b2-61a47406a5c6 | -2.46283 | -53.69477 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6ab4e0d-d740-3121-b416-e95abb39835a | -3.31322 | -54.91248 | 2024-11-13 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9bf299c-0ed5-3bd0-973d-9c35e8588840 | -4.66205 | -47.43316 | 2024-11-13 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8649fc39-a4f0-334a-9b6b-ef49e0a79d86 | -2.57038 | -48.44223 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 724d2450-b049-3732-970a-4fbe1bb7eb0f | -2.74612 | -54.66549 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f08b9653-3cb6-328f-a16b-52498b82b551 | -2.12466 | -50.69239 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dedfc3d6-fe41-3c06-a195-ad316a69b644 | -1.71036 | -53.28204 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd176bc2-9866-3207-a6bc-f516c2530f02 | -2.73096 | -51.82881 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b11f7d5-f5a1-3a0e-aec9-933d0c601ea4 | -2.90986 | -49.35306 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README27.md)
