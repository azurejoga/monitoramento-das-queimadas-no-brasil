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
| 75405446-37e8-3957-b1cc-183db404407d | -4.3402 | -47.7645 | 2026-07-12 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| c9509150-e0df-3d29-a546-b5b5ea0dcb9a | -4.6184 | -49.04893 | 2026-07-12 00:01:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a94f89c5-e922-33ef-bd22-a60fb6ceff23 | -5.64887 | -49.04383 | 2026-07-12 00:01:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a656e34c-e1b1-31f3-8a87-7c8371a44c0e | -3.49417 | -48.04493 | 2026-07-12 00:01:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 82b0b018-71c6-3a02-80d4-4931c936792a | -4.60945 | -49.05014 | 2026-07-12 00:01:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 8b68bf6a-e4bf-3ee3-bfe1-68c114fa7922 | -3.13493 | -48.97812 | 2026-07-12 00:01:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3b5392ea-be2d-330a-8f60-c8cb3638fa7e | -4.66388 | -43.23356 | 2026-07-12 00:01:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a1b98b72-25e0-33a5-bcfe-45b8d465bec9 | -4.80846 | -45.76883 | 2026-07-12 00:01:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bc9b8ab0-c59f-30fd-b45e-8d0f2b413031 | -5.65013 | -49.05303 | 2026-07-12 00:01:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e2d5780d-cfaf-3742-a7f6-8c32ca2f6451 | -4.61069 | -49.0592 | 2026-07-12 00:01:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| b50a5d9f-2d06-3361-bc74-878f38f2caf2 | -1.87955 | -54.68443 | 2026-07-12 00:01:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| a003e1e6-3fd3-3fd8-82fd-e7e49cf4eed7 | -4.66319 | -43.2272 | 2026-07-12 00:01:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7b4d29dd-a2d2-3b94-88b5-cfc5348e1d79 | -3.31266 | -49.46957 | 2026-07-12 00:01:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2b50c307-55ed-3436-af9f-46bbdda99aa3 | -2.96986 | -48.9861 | 2026-07-12 00:01:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aef0cf8e-09d3-3cea-8906-c7361b5dfc76 | -3.49295 | -48.03614 | 2026-07-12 00:01:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| e734c330-c18d-3e17-bfee-6a17603ee63f | -2.80555 | -48.5929 | 2026-07-12 00:01:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 28af42d3-5f74-3e97-89c3-5a2818e8ca70 | -3.13615 | -48.98699 | 2026-07-12 00:01:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| acc9a3a1-7990-39c4-9695-bd1838d4c933 | -2.961 | -48.98733 | 2026-07-12 00:01:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7539a1cf-3dff-3379-95d0-b7b01133544f | -2.76663 | -48.57148 | 2026-07-12 00:01:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dcc220fc-4ec6-3223-b1d1-662b780d71f0 | -2.97108 | -48.99496 | 2026-07-12 00:01:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| d7719af1-1c4e-3035-827b-f26ddbccb098 | -4.34227 | -47.77513 | 2026-07-12 00:01:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 959437fa-950f-3e61-b366-12f26dd0b250 | -3.3114 | -49.46046 | 2026-07-12 00:01:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 0ec0971a-9da8-3f67-b9fc-382434665063 | -5.68117 | -49.81742 | 2026-07-12 00:01:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d1524cec-ef33-3855-a9c0-cc5eb91849c2 | -2.96222 | -48.9962 | 2026-07-12 00:01:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| afd1c33b-6e1f-38b7-92e5-5a6d1c93404e | -4.34105 | -47.7663 | 2026-07-12 00:01:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| d07ba3b5-5a43-3bff-b46b-8ebeca70d518 | -4.3402 | -47.7645 | 2026-07-12 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 581f9872-e1f2-3bfb-937c-ef57b6d00b9b | -4.3402 | -47.7645 | 2026-07-12 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 58f28f74-2892-3e67-b3a2-b8e5e067afed | -4.3402 | -47.7645 | 2026-07-12 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 1f401d5e-1f0d-37ad-bf8e-1920faa57b89 | -4.3402 | -47.7645 | 2026-07-12 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 9ccea467-9c89-3e7b-8745-f7a221b91ed1 | -4.335 | -47.761799 | 2026-07-12 00:44:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1c8cad7-d4ee-3a5f-800c-a255e915f94e | -4.6095 | -49.055099 | 2026-07-12 00:44:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63de4196-40af-370d-b01b-70ce8a65bbd3 | -1.8782 | -54.679699 | 2026-07-12 00:44:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2febcfc6-1e28-3645-8aea-f58814a2cc22 | -8.7248 | -47.825699 | 2026-07-12 00:44:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab54f442-7e7d-38a8-8495-8b8bd14b0dca | -1.876 | -54.670101 | 2026-07-12 00:44:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03a4e52f-2b68-379e-b19e-3a830a15d3ec | -4.3446 | -47.759499 | 2026-07-12 00:44:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f9eb768-3074-3d4d-8fe3-d8dfc069c40f | -15.2282 | -43.980999 | 2026-07-12 00:44:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9aef70b7-ed82-363a-8e3c-bae4bea0b3dd | -4.3402 | -47.7645 | 2026-07-12 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 715c318c-4226-35f1-bba7-94f0b0c55af7 | -4.3402 | -47.7645 | 2026-07-12 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 7692e8ec-10da-3aed-8c8f-107d2508b8f6 | -4.6143 | -49.042198 | 2026-07-12 01:09:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48243f9c-936f-35c5-a625-c572ee41a801 | -4.3527 | -47.7537 | 2026-07-12 01:09:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b49e986-5fd0-305a-a4a5-973cbd6dcd17 | -1.8766 | -54.684101 | 2026-07-12 01:09:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cae7e9f-e081-3897-9d69-2fe9917d7864 | -1.8846 | -54.674099 | 2026-07-12 01:09:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52483576-538b-3f49-b0e1-e116b4d4ab97 | -4.3477 | -47.7756 | 2026-07-12 01:09:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1aca7d4-97ea-3fd4-8e7c-16972e499f99 | -1.8748 | -54.6763 | 2026-07-12 01:09:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9109600-ec80-3550-befa-1f49f1e4b275 | -4.3574 | -47.773201 | 2026-07-12 01:09:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82caff19-1a6d-307e-b897-e688f1c98596 | -2.9728 | -49.000702 | 2026-07-12 01:09:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca422641-7262-33fd-8ca9-139d9179a66b | -2.9688 | -48.983898 | 2026-07-12 01:09:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 523adcb3-f362-36bc-972a-61ac7d5810ee | -1.8864 | -54.6819 | 2026-07-12 01:09:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 421cfa30-bc35-3b5c-97e0-ef840dab345e | -4.343 | -47.7561 | 2026-07-12 01:09:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0c4c772-2827-3db5-b412-116269e72977 | -4.6181 | -49.057899 | 2026-07-12 01:09:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28df72ef-f0c6-3e63-9627-f026a651df9f | -13.7497 | -54.060699 | 2026-07-12 01:09:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b6c7cc2-4847-360b-9a99-b700b7ce9d92 | -8.7283 | -47.8283 | 2026-07-12 01:09:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0678ad1c-8526-3921-979e-b24a3b85d20c | -4.3402 | -47.7645 | 2026-07-12 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 6bc28ebe-090b-305d-b638-e5edd480f8a9 | -15.8949 | -43.4766 | 2026-07-12 03:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 4e4de857-5be1-3bb4-987b-9bc4ec21d6c8 | -20.54171 | -41.83821 | 2026-07-12 03:13:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9cd63815-8b05-39b8-940a-748332da5007 | -20.54564 | -41.83842 | 2026-07-12 03:13:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4ea85a7b-ca02-3303-ba0a-5fa01761174a | -15.8949 | -43.4766 | 2026-07-12 03:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| f7446c83-b16e-31e6-831a-123cf7dc65b7 | -15.8949 | -43.4766 | 2026-07-12 03:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 35b2c83f-e45d-3afd-ad78-83f291782e9e | -15.8949 | -43.4766 | 2026-07-12 03:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 2f190bb1-bfc0-3a79-bef9-5d2b38de1355 | -15.8949 | -43.4766 | 2026-07-12 03:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 716c08ec-e630-3a6b-b437-df6188a8b233 | -4.34503 | -47.76987 | 2026-07-12 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9d619990-efea-3d61-abb8-6ebaf46fa71c | -4.61668 | -49.05331 | 2026-07-12 03:53:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14a4c0bc-d1bb-34ca-947c-12c6bedcf581 | -2.96161 | -48.99702 | 2026-07-12 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f040fce4-502a-3273-9c28-5b662a8f99e4 | -3.49899 | -48.03696 | 2026-07-12 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61fead30-c107-3e90-8634-00b5cdba522f | -4.34006 | -47.76521 | 2026-07-12 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 08da9458-bcba-3d5a-b220-ada6caf231f8 | -4.61744 | -49.0488 | 2026-07-12 03:53:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1be9c904-944c-3814-806f-3ee3d3941f3b | -3.49824 | -48.04132 | 2026-07-12 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 728d32c3-dd3b-345b-99c0-5d4d62ae9bc8 | -4.02986 | -44.13216 | 2026-07-12 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 492af168-0ffe-3e23-aa31-4d30b88b3e41 | -5.01051 | -38.67282 | 2026-07-12 03:53:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1a0924f0-6d5d-333f-be79-6a15636a16ed | -3.73528 | -45.46758 | 2026-07-12 03:53:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d557c9c9-542b-3f5c-9a82-b3e946561209 | -4.02615 | -44.12715 | 2026-07-12 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 05efddea-91c8-3582-994e-81bf3b0bdf0b | -2.96862 | -48.99323 | 2026-07-12 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1a072b8f-6348-3356-bf06-43b0b9cdab18 | -3.49314 | -48.03638 | 2026-07-12 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f8a6aab9-c871-32a9-bf9e-88339b114772 | -4.66237 | -43.22891 | 2026-07-12 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3ed5e68-fcad-31d8-9993-83bc24eba134 | -4.86338 | -37.45696 | 2026-07-12 03:53:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9356f850-a673-3e81-930c-26e437563f35 | -5.25074 | -42.8555 | 2026-07-12 03:53:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 612c3c8d-1b6d-3a8d-945b-26be81d03954 | -3.49226 | -48.03909 | 2026-07-12 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 856a2499-4ebf-379b-83a6-92fbcbb06bc5 | -4.91691 | -37.48693 | 2026-07-12 03:53:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dddc8ae7-fa2c-34e2-a0b5-7d9b428f3f64 | -4.34567 | -47.76614 | 2026-07-12 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f47a7877-351f-3c49-b26d-936cfe107013 | -4.67117 | -43.22655 | 2026-07-12 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d545d45-98aa-31be-8d4d-d2e360bbb9e6 | -3.49295 | -48.03492 | 2026-07-12 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b57b010-aaf0-3bde-868f-6492384d5be8 | -3.12468 | -40.10522 | 2026-07-12 03:53:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1740f0e4-693a-302c-8a1f-d9c7340c9c8c | -4.66707 | -43.22589 | 2026-07-12 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b0a06cf9-9d58-3538-8284-c9049a6b015f | -4.51956 | -38.54954 | 2026-07-12 03:53:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4ea0f31b-d4ef-385d-aaef-bbae3e5550ee | -4.66647 | -43.22957 | 2026-07-12 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 904070b4-a483-37c4-8706-57d4e0c559d7 | -3.49241 | -48.04063 | 2026-07-12 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1a9b1d6f-b2b6-37b3-88f1-3f336c02bf1f | -4.80616 | -45.77232 | 2026-07-12 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7147b36e-f0e3-3d5c-9de0-57715438aa17 | -4.86776 | -37.45057 | 2026-07-12 03:53:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6317991e-2f2f-3e26-9364-7b6daf86de1e | -4.33941 | -47.76902 | 2026-07-12 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0cae2843-7b01-3db8-826b-4ac033ba565c | -4.03014 | -44.13062 | 2026-07-12 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 4297636f-9325-3601-b1d2-d6f2e0a43123 | -3.12118 | -40.10468 | 2026-07-12 03:53:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 86e7a368-46c3-3e25-beed-205fff74f4f1 | -3.73042 | -45.46682 | 2026-07-12 03:53:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d3862526-056c-34be-9872-e12796343284 | -4.3444 | -47.77357 | 2026-07-12 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3815aa54-4be5-3441-bb10-4676714163f6 | -5.01328 | -38.67681 | 2026-07-12 03:53:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| af3ee73f-6f1c-3f9b-9659-50cf71b8c480 | -3.13436 | -48.98532 | 2026-07-12 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1be1c969-cd4a-3f57-bbc0-e7813c723a46 | -5.12499 | -43.23653 | 2026-07-12 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 98c4307a-9bb2-38e6-9f39-74482e5a1137 | -4.61064 | -49.05209 | 2026-07-12 03:53:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f0e39738-7c96-3da8-a331-5d7a3efd5b78 | -2.96242 | -48.99221 | 2026-07-12 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0a36a048-b18d-38e6-9496-b9bab36e241c | -3.12407 | -40.10913 | 2026-07-12 03:53:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 29582621-c5fa-3a50-8ed4-47f728d3d4c4 | -4.03055 | -44.12786 | 2026-07-12 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |


[Clique aqui para ver as próximas entradas](README2.md)
