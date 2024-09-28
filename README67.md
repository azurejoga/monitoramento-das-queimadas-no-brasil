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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2789cbc-1a0e-3d92-91ad-70db360ddc10 | -17.01209 | -56.16371 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c29dd941-3d39-389c-bdf1-3abcdca31dd2 | -17.01144 | -56.16686 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 0bc4343f-1ebc-3ef5-b265-a83fc1706583 | -17.01079 | -56.17002 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 0470b5b9-96a2-3c3a-b737-e4cd09fa2b2f | -17.00894 | -56.15312 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6f9946b2-84fc-3d16-a700-ab01bfafec5c | -17.00752 | -56.18594 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 65e68247-fe0a-357f-acf0-37af9cdf1664 | -17.00633 | -56.16576 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 47c5e4cb-3c9d-31d0-947e-cb5979a775fc | -17.00383 | -56.15202 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 878f5386-be84-3ff7-ada1-4d031a14a692 | -17.00188 | -56.16148 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 390c7479-1467-3924-aff1-a16804627c4e | -17.00122 | -56.16465 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| b7e27f1b-2738-3b66-9ee9-ae9b50247577 | -16.99873 | -56.15092 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 72ee2895-54ad-3bdb-a774-643557746f70 | -16.99677 | -56.16037 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 0ffac4db-4121-3d03-8a30-8c0239f7063e | -16.99612 | -56.16353 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| bc88cf2c-4e62-331d-ad2c-1ab5d3fa6be5 | -16.99609 | -56.15255 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7b8fc1a3-273d-3301-a162-f250c7702aaa | -16.99483 | -56.15888 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ec33e6bb-8f43-38f7-969f-138e9c5708f8 | -16.99297 | -56.15296 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6db4b17f-06f5-3e35-bc26-85a90563c545 | -16.99232 | -56.15612 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 7762d796-4877-3438-8a39-80acd3ae3c27 | -16.99098 | -56.15143 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9c4da735-cd68-30c9-a8f6-a144085a6478 | -16.99035 | -56.15459 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 34181720-04e0-3369-8ec7-4e27509ec68d | -17.0068 | -56.09874 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 894fe0ea-7668-3dc4-ac84-3601e0e210c2 | -17.00472 | -56.09616 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 849d0083-6396-3eb0-abcc-428ed66a79b6 | -17.0046 | -56.12246 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 73c57644-17f2-366f-9067-00351edc6dbc | -17.00407 | -56.0993 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 919aaeea-ac03-34f5-9c03-0781cdd2e8a2 | -17.0033 | -56.12877 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3f87b3f5-42df-35f2-98d7-3d3b6cf3e1ca | -17.0024 | -56.12086 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 105ced6c-632f-3cd2-9bd3-1d8c2e4d2cbd | -17.00171 | -56.09763 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b7565704-10a6-3f5d-ae74-1aa06e5f8797 | -17.00134 | -56.13825 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2e3aba2b-50fb-3d65-94bd-69fcd41b1e8b | -17.00114 | -56.12718 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5077ac5a-6aea-30a7-b841-870bc493fea0 | -17.00051 | -56.13034 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| feb14f3b-c8a4-3c1f-b9a7-5c8cace390ee | -17.00016 | -56.1182 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1d2938b2-3443-33ca-95c6-867c3fb801ed | -16.99988 | -56.13351 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2b088b0c-d30b-336f-b591-d436d53125ca | -16.99963 | -56.09506 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a3c41b0c-0f31-390f-ab4d-ec5416151ffb | -23.57104 | -47.35287 | 2024-09-28 04:25:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| d9d431aa-4d44-31d4-9d2f-7fc7e65ab2b9 | -23.56768 | -47.35228 | 2024-09-28 04:25:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 01a34831-016d-325f-8a36-b82aaa22bf16 | -23.39798 | -47.00811 | 2024-09-28 04:25:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3adb296d-a0d4-34c8-83f8-f700d10c9bf2 | -23.36306 | -46.98617 | 2024-09-28 04:25:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dcbab466-7172-37cc-8e55-4ba6547d2a31 | -23.09242 | -47.79908 | 2024-09-28 04:25:00 | NOAA-21 | JUMIRIM | SÃO PAULO | Brasil | 3525854 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1fcdf114-7216-3ead-85d6-ab730b5d4d9e | -22.95074 | -48.3248 | 2024-09-28 04:25:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8fc0d6f-9a72-3dd5-8a46-2cecbfb3ed42 | -23.98364 | -48.91906 | 2024-09-28 04:25:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4958435c-78fb-3909-b3e1-4f63acee9c1b | -25.19177 | -49.32788 | 2024-09-28 04:25:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b937a19d-d696-3ec4-8bc8-3fd17fa7fa31 | -26.26261 | -50.27304 | 2024-09-28 04:25:00 | NOAA-21 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 89024672-0b73-36b7-a830-31d58fcc6d1f | -30.13355 | -51.32171 | 2024-09-28 04:25:00 | NOAA-21 | GUAÍBA | RIO GRANDE DO SUL | Brasil | 4309308 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 555555d7-0bbf-3875-bc86-b7f23d3a0fe3 | -29.8737 | -51.15617 | 2024-09-28 04:25:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 2cbc6f83-e016-363f-8681-51d6e429ea6d | -29.81603 | -51.17747 | 2024-09-28 04:25:00 | NOAA-21 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| c8dbef43-f18b-3a76-a6df-789f716249cc | -28.36884 | -52.04013 | 2024-09-28 04:25:00 | NOAA-21 | GENTIL | RIO GRANDE DO SUL | Brasil | 4308854 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9fc98415-5a4f-3ca7-918f-4dd71ef2280b | -21.55846 | -55.82181 | 2024-09-28 04:25:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78d862b2-c577-30d4-bff6-a0ba2f37c726 | -21.5539 | -55.82068 | 2024-09-28 04:25:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c7a766e-a6f2-3afa-90fd-bd83497d7b8b | -14.87 | -51.57 | 2024-09-28 05:04:00 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b6ae83d4-8174-3409-a3b5-b9a2cfed69d2 | -1.72081 | -47.12764 | 2024-09-28 05:06:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 516d873a-c775-3d82-a748-a8c4ab7e44a1 | -1.72029 | -47.13092 | 2024-09-28 05:06:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| deeef25e-e545-3043-a906-add4afaac71f | -1.17625 | -46.71414 | 2024-09-28 05:06:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5d715669-249f-3404-ab9e-4aa469fc2576 | -1.17573 | -46.71759 | 2024-09-28 05:06:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 03ac7eeb-fe6c-3e3d-b5e9-5f77a1e6286c | -1.17031 | -46.71677 | 2024-09-28 05:06:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eecad6a2-0425-3de4-bfd0-fec7dba46700 | -1.66744 | -47.46994 | 2024-09-28 05:06:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79f339a1-e010-308d-9088-1d5372d13899 | -1.66225 | -47.46917 | 2024-09-28 05:06:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28e300d8-27c0-3e1f-a149-fddf3fe7c547 | 2.44007 | -50.77337 | 2024-09-28 05:06:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5fae1de7-bec8-346b-acb4-ffd2d2e6fb8a | 2.43697 | -50.77886 | 2024-09-28 05:06:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ea1e1d4-382f-3810-b8a0-565b4bc2c55b | 2.43618 | -50.77399 | 2024-09-28 05:06:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c703a6c3-6cb5-3057-ba99-9297eee8e7ff | 1.37628 | -50.72712 | 2024-09-28 05:06:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 330d7170-5871-3444-8993-b947acaa0bb0 | 1.37547 | -50.72204 | 2024-09-28 05:06:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 374e82a3-47c4-3964-86da-b5a3e4c1b111 | 0.97202 | -51.11497 | 2024-09-28 05:06:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 31925474-38c0-3123-a93a-7afb3b010da7 | 0.96893 | -51.12052 | 2024-09-28 05:06:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b8b600d-8e60-3cc6-8855-aeb581a2dbfd | 0.419 | -50.92041 | 2024-09-28 05:06:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f374a334-b440-3e6d-a004-8114d9de5cab | 1.98654 | -55.78098 | 2024-09-28 05:06:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebb83160-d76b-3bda-ba4d-fc041150d776 | 3.12929 | -61.18105 | 2024-09-28 05:06:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b29433c-d632-312b-a3e7-e54e30cafa1f | 3.12496 | -61.18172 | 2024-09-28 05:06:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3d42f91-d8a2-3a48-8900-2064eb378a1c | -6.32677 | -43.41946 | 2024-09-28 05:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82e811f7-31d1-3e6d-b546-74b8c1280ef6 | -6.31957 | -43.41887 | 2024-09-28 05:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8579387a-d722-35ad-8825-fb5cba0561a5 | -6.31693 | -43.41499 | 2024-09-28 05:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f0a73c3-0161-3c8b-92b0-792eb27dc052 | -6.31589 | -43.42258 | 2024-09-28 05:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fcc045ea-f4d8-39b6-abd1-003170777ed8 | -6.31488 | -43.42998 | 2024-09-28 05:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fc03ce4b-b403-3272-880a-9227fa8907f0 | -6.31245 | -43.41768 | 2024-09-28 05:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dfe5c16d-0577-3a9f-af70-7fc696b0d420 | -6.31147 | -43.42526 | 2024-09-28 05:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4c20166f-e2a7-3a90-9194-420be0230875 | -6.17699 | -43.45469 | 2024-09-28 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b9cf5da6-7158-3165-b541-2af6b29756ae | -6.17443 | -43.44901 | 2024-09-28 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 81a2eed3-c7ec-3963-8234-a94f4f51d941 | -6.17365 | -43.45509 | 2024-09-28 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2fb466f8-43a0-3564-b6b7-2ed8e9e7e54b | -6.17075 | -43.44719 | 2024-09-28 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 848f8cc9-0c0f-31ca-95e8-9cdf62537e60 | -6.16994 | -43.45317 | 2024-09-28 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb82ce1e-3199-3335-b073-2f57189f60bd | -6.16828 | -43.44046 | 2024-09-28 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a7096b3-bad7-3f81-924c-aec2967ca903 | -6.16738 | -43.44744 | 2024-09-28 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f55a3ee-11a8-3cfc-992d-cb6a04ec1b2b | -6.16376 | -43.44526 | 2024-09-28 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76da2a39-eef1-3ece-a5aa-e5b5ffb7aadc | -6.72216 | -43.55783 | 2024-09-28 05:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 951c6866-d5f7-397e-ab71-890dc6a0f6e3 | -6.72129 | -43.56461 | 2024-09-28 05:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6aeed444-049b-3844-a720-564aa73a777b | -6.71866 | -43.55775 | 2024-09-28 05:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7bb5a908-5688-3560-9c2b-1d8cd3ca8623 | -6.71775 | -43.56451 | 2024-09-28 05:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 980075ee-fcfe-31d2-9e17-a7178bba0f72 | -3.29646 | -43.52277 | 2024-09-28 05:08:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bc28160a-f4d4-319e-a5af-bc06e35652b5 | -5.88171 | -43.86764 | 2024-09-28 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9deb4ba-cd7c-323a-b649-52efe5363fe6 | -5.87477 | -43.86676 | 2024-09-28 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 299cfcdb-afac-35fa-88e3-157882d8d1f1 | -5.87386 | -43.87348 | 2024-09-28 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65dc42f5-0a33-35b7-933a-1e7a686a9bc2 | -5.83408 | -43.65334 | 2024-09-28 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56a4dfb7-b4df-3c0e-8fcc-e192976d4d50 | -5.80322 | -43.97959 | 2024-09-28 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed68adc9-029d-3ea8-bb11-cf91106dc4dd | -6.3917 | -44.78489 | 2024-09-28 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 14a0f20f-b2a4-3156-8d9e-c700f9bab3ca | -6.38512 | -44.78384 | 2024-09-28 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50952e44-16c8-3117-929d-8838593db6bc | -6.09877 | -44.70483 | 2024-09-28 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30e660d0-99db-3c75-8420-06da2e52679b | -6.09215 | -44.70397 | 2024-09-28 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a4116a2-6694-3ade-9741-5900fd2e3750 | -5.76553 | -44.47175 | 2024-09-28 05:08:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2f1663a-801c-36c9-9262-3f660c47d125 | -5.71322 | -44.81615 | 2024-09-28 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8d5f62f-cecb-362d-920f-15cac21d9d4f | -5.55351 | -44.67381 | 2024-09-28 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 299c30e1-33d2-3267-9b88-a52b232fc6c5 | -5.55274 | -44.67942 | 2024-09-28 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e0d4320-c25f-347e-9010-1fd86bf11f16 | -5.5469 | -44.67318 | 2024-09-28 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48e7f451-d9f9-3e36-b70c-80cbde55e2c4 | -5.54614 | -44.6787 | 2024-09-28 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README68.md)
