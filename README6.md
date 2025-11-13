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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26a59221-313f-3b17-9bc7-9f56442e77f8 | -3.2377 | -45.6063 | 2025-11-13 00:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 45.1 |
| bea55484-10df-3eeb-ae18-41d99eb99518 | -4.2156 | -50.1022 | 2025-11-13 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| d4c8e887-aa6c-386b-b92b-79aed3f684ec | -3.1453 | -45.4978 | 2025-11-13 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 8f438581-8bc7-3521-9237-0dc79e277502 | -3.0915 | -49.2972 | 2025-11-13 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 642238ca-a52c-3bf5-9226-2cf7b20a186f | -3.2378 | -45.5839 | 2025-11-13 00:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a8e6a421-af8a-3197-a492-5c7a8236a341 | -2.8111 | -45.4426 | 2025-11-13 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9a924a6a-1422-3c0e-b812-98c831bc2370 | -4.3003 | -48.2431 | 2025-11-13 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| cfdd0fe9-2be3-3084-9857-9984a19a44cd | -3.0731 | -49.2765 | 2025-11-13 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 38382c83-a85f-31a9-b8ff-1d9846ef6153 | -4.7206 | -46.4276 | 2025-11-13 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| bc044015-8faf-3a36-a2bc-c07eed3b9bc1 | -3.0917 | -49.2547 | 2025-11-13 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 09cf7c0d-fb36-3c8d-bea1-028c31b2368d | -3.0731 | -49.2765 | 2025-11-13 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 40536afa-d5da-34cf-80bd-f24992a8f7b1 | -4.1161 | -48.0136 | 2025-11-13 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 62cfb227-e82e-30ea-a9dc-8bf772ec3165 | -2.8297 | -45.4419 | 2025-11-13 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.0 |
| a9e6761b-aadf-3b29-83ba-d0dd64b21f79 | -3.0915 | -49.2972 | 2025-11-13 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| f701b3bd-ff55-3547-a511-6508dfbaa5d0 | -3.8658 | -49.7998 | 2025-11-13 00:40:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| d4468377-2dbc-31b9-90ef-4ab23827f681 | -2.8111 | -45.4426 | 2025-11-13 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 8c68b36a-9724-3a27-a1c7-f774a76da9df | -4.702 | -46.4286 | 2025-11-13 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 6390afee-eb99-3f98-b383-6e5b2ff5375a | -3.1639 | -45.497 | 2025-11-13 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 42.5 |
| bd911883-d7b2-3ff1-b518-0ce9e83340fa | -3.8659 | -49.7786 | 2025-11-13 00:40:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| f3f0caf5-919f-3814-ab0b-2fd1a606ed2a | -3.2378 | -45.5839 | 2025-11-13 00:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 41564ca0-a774-3580-87eb-6900c298e37d | -3.1101 | -49.2753 | 2025-11-13 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| d0d12ed4-69d4-31a0-b95c-4023b9d92a58 | -3.1453 | -45.4978 | 2025-11-13 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 2c358e36-0706-3fe3-bfa7-a169c8573b27 | -4.7018 | -46.4508 | 2025-11-13 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 69ccce89-cb84-359c-ac83-0e80a2b556e4 | -4.7204 | -46.4497 | 2025-11-13 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 107.9 |
| ab8255db-c760-33d2-8887-17794710ef66 | -2.4635 | -49.2514 | 2025-11-13 00:40:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| c05863c5-9a7f-3c46-a3aa-bf40db79800a | -4.5344 | -46.4376 | 2025-11-13 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 0c9c886d-926f-3efa-9f46-be55de37fabb | -4.2156 | -50.1022 | 2025-11-13 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 6158cae3-9a3a-372e-938f-223234529faa | -7.6788 | -45.8747 | 2025-11-13 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| ac102a30-ad3a-3fc0-9e3f-02d6be2582b3 | -3.2192 | -45.5846 | 2025-11-13 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| a536a287-f342-30e6-bc15-9fcd4b555016 | -3.0916 | -49.2759 | 2025-11-13 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 199.4 |
| 68d5ea44-a96e-376f-9f43-52799d53bb0d | -2.4634 | -49.2727 | 2025-11-13 00:40:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| eb2422ef-b42f-3215-895a-5923875d6684 | -3.2191 | -45.607 | 2025-11-13 00:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 121ebd74-fdd2-3c94-8299-f37f0cab7edb | -3.8658 | -49.7998 | 2025-11-13 00:50:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| cf5d5491-53b9-329f-87cd-9939cb3c3582 | -2.445 | -49.2519 | 2025-11-13 00:50:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 1687ea6e-6d1e-335c-9865-34b5468aafcd | -3.0915 | -49.2972 | 2025-11-13 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| a33a2efb-ab5d-3f9f-8d2b-2fd40b9b2c66 | -3.2378 | -45.5839 | 2025-11-13 00:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a3a3e6ea-362d-305c-83a1-b7d849026e68 | -4.5344 | -46.4376 | 2025-11-13 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 622fa287-2927-3fd1-834f-4ecc616a8a96 | -4.7018 | -46.4508 | 2025-11-13 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 6588ce65-9961-3c27-a836-273146f4ab9b | -3.0916 | -49.2759 | 2025-11-13 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 198.4 |
| 1b4067ba-7d06-3851-a866-6af204390acb | -3.1101 | -49.2753 | 2025-11-13 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 64f3ecc9-6179-33cc-97ae-ba5eaa3fba6d | -2.4449 | -49.2731 | 2025-11-13 00:50:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 9ab101a5-db54-35d4-9fdf-5305a15e1bb0 | -3.8659 | -49.7786 | 2025-11-13 00:50:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 8e9e548a-3fd7-3886-a9fe-bd7ddeffecf3 | -3.017 | -45.12 | 2025-11-13 00:50:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d1ef514f-3773-31c6-b2c5-bd9f12bbeff5 | -3.1453 | -45.4978 | 2025-11-13 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 01309c5b-3cc9-347b-a5ca-30b861ce4f5c | -2.8297 | -45.4419 | 2025-11-13 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 114.4 |
| fca936c8-260d-3060-81f3-d7ddc7f4d871 | -3.2192 | -45.5846 | 2025-11-13 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 53904810-8734-3174-a715-57025b3a2518 | -3.1639 | -45.497 | 2025-11-13 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 185.5 |
| 6ee9461c-3864-35d6-87eb-b17aa39e9a86 | -20.4489 | -53.0493 | 2025-11-13 00:50:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 43e54ed5-5f06-3401-962d-eabfe7837721 | -3.164 | -45.4746 | 2025-11-13 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f237765e-a5f8-3f24-ae86-10e8d3c7ea12 | -2.8111 | -45.4426 | 2025-11-13 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c6cdcce7-7569-385d-a61a-84d620dbde83 | -3.1454 | -45.4753 | 2025-11-13 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f54d99d7-1a6b-37ad-8672-03642f2eb253 | -3.0917 | -49.2547 | 2025-11-13 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 653d2d9c-5397-3d0d-9b6d-8cd5721812ef | -7.6788 | -45.8747 | 2025-11-13 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 8e567637-1ca1-3749-baa6-0eb9c5b768c7 | -4.7204 | -46.4497 | 2025-11-13 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 94c34665-6377-3ae9-83d2-b9524bb0ae6f | -4.7206 | -46.4276 | 2025-11-13 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 55d48966-5f47-3a48-9602-4da550c58c7d | -1.7701 | -54.131001 | 2025-11-13 00:58:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5750b83b-39bd-3643-ab79-4e595470f51c | -3.1576 | -50.620499 | 2025-11-13 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 854a356c-9051-3ac0-a7f9-4c7edd95998e | -5.3866 | -46.7537 | 2025-11-13 00:58:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17ef967a-10b9-3cc7-ab5d-62a295d442a6 | -10.9294 | -44.6017 | 2025-11-13 00:58:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4055481c-6b3c-3d36-94d0-2aa63f5cf46d | -4.2107 | -50.0952 | 2025-11-13 00:58:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba273394-508e-33c2-b408-16f7d19e9c5f | -18.0299 | -51.038101 | 2025-11-13 00:58:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a924afee-4067-317e-9eb1-5ee5d31ae49d | -22.651199 | -44.914001 | 2025-11-13 00:58:00 | METOP-C | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 231abfc5-52e5-3dcd-9e25-ed0a22c14485 | -5.3343 | -45.1819 | 2025-11-13 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1859051-ec5b-3c93-9685-0e0f3a1d59dd | -22.648899 | -44.904499 | 2025-11-13 00:58:00 | METOP-C | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ce926267-6753-383d-9747-1dfbf384f357 | -18.026699 | -51.023499 | 2025-11-13 00:58:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 014b5400-784a-38ce-a326-0fff047ce94d | -7.1255 | -42.7272 | 2025-11-13 00:58:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 67840eb3-2b1a-371e-87b8-e33c18ce41b9 | 1.4574 | -55.841499 | 2025-11-13 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aca872e-c4e0-3b57-8af0-c68bd9896ce4 | -9.347 | -46.584999 | 2025-11-13 00:58:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbc5afa4-8835-363a-afa8-cf7d7dc02206 | -9.3498 | -46.596401 | 2025-11-13 00:58:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7eb6b5c4-013e-3552-a61c-adb57cf4072d | -13.0067 | -49.790501 | 2025-11-13 00:58:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b42f2e0-15aa-33eb-b119-617779cddd58 | -2.0084 | -54.451099 | 2025-11-13 00:58:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3b3686b-d071-33cd-8ca9-90bccf89d9e6 | -2.4565 | -49.248402 | 2025-11-13 00:58:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7658d9da-1bd8-30dc-b30e-d6b911d95283 | -7.6745 | -45.867298 | 2025-11-13 00:58:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f9e515c-ad23-3251-a4ea-3194f08355c3 | -6.1594 | -48.040798 | 2025-11-13 00:58:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db82653b-a5d5-36c4-8d1f-e8d3d6849a83 | -4.1031 | -48.018299 | 2025-11-13 00:58:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21f1145a-f012-3967-a02a-7f0a5fce8e6b | -4.2135 | -48.571701 | 2025-11-13 00:58:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b16d5129-d1d5-3d7c-8eda-eb6b733fdec5 | -4.3182 | -48.2304 | 2025-11-13 00:58:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8725c6b-308a-32c9-8c33-ffcc5aa0127b | -4.3084 | -48.2327 | 2025-11-13 00:58:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b5f8c18-4345-315b-90de-0286888f0016 | -6.5722 | -48.734402 | 2025-11-13 00:58:00 | METOP-C | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 827fd6a8-c1fa-38d1-9894-efc0aba4d592 | -2.8273 | -45.424702 | 2025-11-13 00:58:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b6af15e-54bd-3df4-9cfc-5d6c86be79b4 | -3.6733 | -45.915501 | 2025-11-13 00:58:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 93015ce0-23cb-3d19-97d1-b22ff6d09dba | -12.6509 | -46.737598 | 2025-11-13 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91d0be33-f0df-3cd0-ae2c-6d9d64e2d7f2 | -12.6016 | -48.3316 | 2025-11-13 00:58:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce19454e-21e6-3a11-8e0f-cb7d8d1bd335 | -8.2569 | -44.354801 | 2025-11-13 00:58:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 42b4e93f-267d-3b9c-984b-0e3cc40207c7 | -3.2219 | -50.188599 | 2025-11-13 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3731f745-b17d-35c8-8864-8aff4fb7496c | -15.6465 | -45.5783 | 2025-11-13 00:58:00 | METOP-C | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ee21e79c-e422-323b-b835-6c1d3590144c | -2.7385 | -45.481899 | 2025-11-13 00:58:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1fd2ac2-fb8f-3e48-9cb2-8a7188f6da03 | -11.7399 | -48.532799 | 2025-11-13 00:58:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fcd3be1a-ec84-360c-85c7-3ca280130d4d | -4.0117 | -48.8083 | 2025-11-13 00:58:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 761652c4-4c9a-3e01-b819-aac78062cd0d | -4.7104 | -46.424599 | 2025-11-13 00:58:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 330d4fb7-bf45-3720-87d6-de2699267058 | -3.8726 | -49.795799 | 2025-11-13 00:58:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b075a78-cf4e-3cc7-8a8d-c9663652dabb | -4.3992 | -43.088902 | 2025-11-13 00:58:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed8f5d87-b1b1-38c1-99fb-bb7e0801fe2d | -2.7344 | -45.464699 | 2025-11-13 00:58:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c6c40ca-a158-3944-a280-2a53dd6d2182 | -20.4583 | -53.0406 | 2025-11-13 00:58:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 66899854-847b-34d3-be58-67711a8fdfac | -3.8705 | -49.787102 | 2025-11-13 00:58:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| beb0e926-a89e-30d5-8673-c2e9fdcd1132 | -2.8329 | -52.8745 | 2025-11-13 00:58:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 283c0f12-7764-38c3-8635-970d7e1d606a | -3.2334 | -45.5793 | 2025-11-13 00:58:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58e3da14-650d-3803-91ac-31ad29e82ad4 | -4.0094 | -48.798401 | 2025-11-13 00:58:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee5924b4-c7eb-3c50-a7cb-48cc6b1e679d | -4.7137 | -46.438301 | 2025-11-13 00:58:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad55da2d-b3a2-3c63-a101-9dc6e5170726 | -3.0889 | -49.266102 | 2025-11-13 00:58:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
