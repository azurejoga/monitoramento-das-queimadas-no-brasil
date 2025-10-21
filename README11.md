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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90348571-72cc-3b1a-81f7-c8cf6e3cbb29 | -3.4968 | -45.8195 | 2025-10-21 04:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 231.7 |
| f2143c49-0b6f-3fa4-a76f-cd082f83ddeb | -3.4967 | -45.8418 | 2025-10-21 04:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 7927b5df-a0ff-385d-8516-d83343d318e1 | -3.5154 | -45.8187 | 2025-10-21 04:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 547c6929-054f-31e9-92ff-e1aa8e580b9e | -3.5154 | -45.8187 | 2025-10-21 04:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 102.5 |
| cd4d4a29-2a7e-3a67-ab6f-7ea8600539d8 | -3.4968 | -45.8195 | 2025-10-21 04:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 172.4 |
| 9a7d7330-218e-3b0b-b21b-c60b9db04d4e | -3.4967 | -45.8418 | 2025-10-21 04:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 797d7509-1101-36f1-814d-f25bea8a47ab | -3.5153 | -45.8411 | 2025-10-21 04:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 126d2b2a-2f5f-3c53-a299-fef842fa071b | -3.4967 | -45.8418 | 2025-10-21 04:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 7db20d2b-9f8a-383e-8acf-3df68c4e2ece | -3.4968 | -45.8195 | 2025-10-21 04:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 172.3 |
| c2b4ed7b-4296-3b85-8720-202bf79e75ff | -3.5154 | -45.8187 | 2025-10-21 04:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 86.7 |
| f6ff8aa0-1ac7-3fe2-abb4-07f9d8c357c0 | 1.7303 | -55.6851 | 2025-10-21 04:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e77431bb-4075-3192-af04-87c6d92955ce | -3.4967 | -45.8418 | 2025-10-21 04:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0692be0d-9321-34dd-8ac1-c6002fff405a | 1.7119 | -55.7051 | 2025-10-21 04:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ab5d578b-26c4-3bc2-97ca-d3b3fe71772c | -3.4968 | -45.8195 | 2025-10-21 04:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 0cc73ecf-dd50-3c08-b345-39de6b29ed06 | 1.7302 | -55.7049 | 2025-10-21 04:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6a12374d-14f4-37f6-8cd3-6799ec892cf8 | -3.5154 | -45.8187 | 2025-10-21 04:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| d743c5aa-673c-3024-9ea9-e473e315d3d6 | -17.4332 | -55.0441 | 2025-10-21 04:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 1e2f129b-3d81-3bf3-930a-5e1b4717b5c4 | 1.712 | -55.6854 | 2025-10-21 04:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 037f22b5-7293-377a-ad2e-3a465f80cad2 | -3.1278 | -45.2736 | 2025-10-21 04:40:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 066b518a-a6eb-3495-9470-45d409e4aa7e | 1.74278 | -55.6963 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d797de80-0615-345e-a579-bb7b968575c4 | 1.72692 | -55.71224 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 243372b8-2f9a-322f-9b1d-1ea5034f684b | 1.76889 | -55.68785 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e730888-4366-346e-896b-0e837509f544 | 1.72938 | -55.6983 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e065374-8f9d-32f9-a996-484dd7b59161 | 1.71977 | -55.69516 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ecb88749-531d-33c9-9228-8ffe2fd30f8a | 1.73005 | -55.70273 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f09ca425-b5a8-366e-8a11-4497eafd768c | 1.72157 | -55.67685 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| bc3f9876-6e58-354d-84fd-0457ccb61169 | 1.72424 | -55.69452 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bbf6482-1d68-3d96-a126-2e35391b9a2b | 1.7267 | -55.68058 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e975ff0-3610-3bfa-8c9b-f8b83dcdb199 | 1.75928 | -55.68472 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5759a157-e090-39c4-8f5c-4ed6863f2b21 | 1.72044 | -55.69958 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 7eb7f733-25c1-3143-a9e8-118963e25d87 | 1.71844 | -55.68634 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 14788206-8058-37c0-9127-a76c0a345b0c | 1.7586 | -55.68029 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8046fec9-c4ef-3e64-b1c5-30c618188ca9 | 1.76374 | -55.68407 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3bef9de-ac00-3418-ba2a-6f4359466ff6 | 1.74765 | -55.66843 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 176f798a-8357-3b4d-a0fe-61af930accae | 1.75792 | -55.6759 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c85383ab-8f38-3227-b395-a5ee1d718b89 | 1.74699 | -55.66409 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a8e523f-3d5e-3e0e-a909-a331c5a9dfce | 1.71911 | -55.69075 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c60237c-ac7b-3931-93b2-bb207528011d | 1.72291 | -55.68568 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eec53b6b-ddcd-3458-9e9d-3b7c657f040a | 1.83812 | -55.6427 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19c68e1a-7539-34e4-8be8-87013f9d48d8 | 1.72224 | -55.68126 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5247f988-7361-3548-a417-3dc0463a47cf | 1.77594 | -50.85691 | 2025-10-21 04:42:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68d59341-e295-384c-bbce-04f9d00e9f37 | 1.73139 | -55.71159 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6db13cc9-c862-36a6-a548-d4713624157e | 1.72558 | -55.70336 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 6f025fe0-755f-3f5d-8354-a4e1e768e6aa | 1.72491 | -55.69894 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 58999dc6-c652-3685-b31c-5c64f94ce324 | 1.83367 | -55.64343 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57fc4858-09f5-330d-a6d1-3e474de15e0c | 1.72357 | -55.69009 | 2025-10-21 04:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65eb9827-ca98-393f-92d6-c7e1a9ee0acb | -2.65156 | -54.89331 | 2025-10-21 04:44:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad4be3fe-7a9a-36d7-bcb7-69b86198e781 | -3.81631 | -48.6507 | 2025-10-21 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5492f958-38f7-31c1-9dd3-612662327d14 | -6.64757 | -43.60506 | 2025-10-21 04:44:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9589f1ef-a220-361d-b4c3-5bc39d4ba807 | -5.4481 | -50.03821 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94743d5e-9156-31e9-a526-116eb47ce4cb | -2.59516 | -51.3457 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a8bb3ab-96b7-320b-91eb-34a4fc358856 | -3.66111 | -51.95102 | 2025-10-21 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bd7c224-aedb-3d36-8a8e-2aa87a186129 | -3.85647 | -48.96014 | 2025-10-21 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d2588a50-dc78-34c0-a888-e648ba6e8c63 | -2.45014 | -47.19128 | 2025-10-21 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f21b69e-dfc1-3654-9587-a3619b300276 | -4.47094 | -49.09804 | 2025-10-21 04:44:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 922338f6-78ba-364c-a18a-5bb1389078a3 | -1.51323 | -47.54538 | 2025-10-21 04:44:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a57ce464-b7ae-3b37-8c78-bf12230f7ef1 | -3.32114 | -53.35317 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f555158f-f302-3752-acb2-6ddd32c4712c | -5.45087 | -50.0422 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d0441c6-02fe-3a6c-aad2-ce833f87de7f | -4.67839 | -42.72743 | 2025-10-21 04:44:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4113b798-65c7-374e-a098-828c2436238f | -3.45419 | -53.03845 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a41702d0-2d50-3ee9-be8c-0ed1e36717cc | -2.81265 | -48.62777 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5cb8415-7561-34c1-b531-a6c959b4f9a0 | 1.71087 | -55.71717 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1d669df-11d4-36ee-97bf-6654be66333e | -2.80885 | -51.35043 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f306901c-3d38-3759-b7cb-c782d29de3fb | -3.8724 | -52.26381 | 2025-10-21 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22ab8bce-2e97-3f7b-86b1-49a378c082a7 | -5.75838 | -49.96881 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e3bfa08-a523-38aa-98ab-dc29f0fbaf06 | -4.0077 | -46.96712 | 2025-10-21 04:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36f17e3c-702a-3bc3-aa05-c2027e0477d4 | -2.88243 | -50.73425 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fadef6e2-c5b7-323d-b3b2-008656e48b63 | -2.96054 | -50.99432 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d589908f-d499-3408-bb78-33bba52e0e29 | -3.33336 | -53.22934 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6822f95-886c-35f3-b34f-6b9cc316c4e7 | -2.85454 | -50.73619 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a208bab-8aae-3921-83da-5f014a487e33 | -3.41105 | -52.60248 | 2025-10-21 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6661a01-9d83-3996-96b3-892fa37ab206 | -3.32472 | -53.35377 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 19502acc-7847-3e5e-b537-7611a4388ffe | -6.89066 | -43.62363 | 2025-10-21 04:44:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38be4928-8109-3f36-89c4-f1f2cf19e832 | -3.14605 | -50.24424 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 254c708f-90d9-3829-87df-9e124b445771 | -2.78797 | -49.61878 | 2025-10-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ad26ff0-abd6-32ae-846c-c98a2864654c | -5.29036 | -50.56856 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74e8ad32-4c6b-3763-9a49-e9a5102b31f2 | -4.59768 | -45.38699 | 2025-10-21 04:44:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f13030db-3017-326e-98b6-ccf229ac9970 | -6.65344 | -43.4277 | 2025-10-21 04:44:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 249b74fe-99cb-3625-a9b2-99b8df1a2cb8 | -2.44776 | -49.0072 | 2025-10-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71ac93eb-1b53-3c43-9d9a-8e1b033f900e | -2.8776 | -50.71858 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fee5d2d6-007a-3f21-89c1-e2092547dce3 | -6.73381 | -44.14764 | 2025-10-21 04:44:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cab4cc68-1d2b-3812-84e2-f3036e209346 | -2.9502 | -49.58035 | 2025-10-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cd6dfeb-e0ef-35fe-8538-06cb93db544d | -8.1179 | -41.1847 | 2025-10-21 04:44:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f423374b-fcfd-3ea4-a745-75c928a96419 | -7.14721 | -44.24136 | 2025-10-21 04:44:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1bf735c5-ac1f-30ae-b379-f6c83a19a967 | 1.70008 | -55.71614 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31ddfd5d-b5a6-3168-b49f-951e5730aee9 | -2.8071 | -48.66364 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 354d0e27-4bfa-3fb9-a78f-ae216909477e | -4.39727 | -43.31237 | 2025-10-21 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a36aa1f0-9a06-3825-b324-bcdaac957282 | -2.7243 | -49.78852 | 2025-10-21 04:44:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96fc9062-b03c-3d63-b33b-4882dbef166e | -2.50299 | -49.0449 | 2025-10-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6330bc9f-1715-3ab3-bb99-56ad2160d3b1 | -2.73828 | -49.39124 | 2025-10-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6308afb6-60a8-337a-8067-1a60834b6315 | -5.7786 | -53.45816 | 2025-10-21 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e2afcd8-6fbc-360a-affc-6da60df9610c | -2.17139 | -53.48584 | 2025-10-21 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d48863c-abef-3a04-8c26-d32776607a59 | -2.44564 | -49.37094 | 2025-10-21 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14afb865-4476-375c-8b87-9b067e8441f8 | -2.87208 | -50.71067 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d250b2d2-47b0-3c19-a760-809b2d81cbfc | -2.45055 | -49.01122 | 2025-10-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c79859a-193f-3e22-899c-f746e75a8980 | -2.19451 | -54.48064 | 2025-10-21 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3130ad0b-bbfd-36c3-b0c4-7899d2895041 | -2.63631 | -48.44996 | 2025-10-21 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30c8fe18-c689-3382-a997-59ecd942a88e | -3.66032 | -52.11858 | 2025-10-21 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 127b7a83-5f5f-34fe-8691-818e0e163db7 | -3.50396 | -45.83096 | 2025-10-21 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 7550f330-f03b-394e-abd4-3076ded7ef5d | -1.89551 | -51.01291 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README12.md)
