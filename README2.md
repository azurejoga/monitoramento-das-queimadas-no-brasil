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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cfbc1bf-f22a-30be-a8bd-b4a135d8e243 | -9.5125 | -68.4891 | 2024-10-03 00:06:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 94e93a69-2464-3699-bb52-6de922d6d1ed | -9.6419 | -68.634 | 2024-10-03 00:06:01 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 9c7b6396-9473-356e-b707-e0086a51e09e | -9.7173 | -64.2302 | 2024-10-03 00:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 35570e06-4ae1-3b14-b554-eed539be582b | -9.7354 | -68.4284 | 2024-10-03 00:06:02 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 44.1 |
| f38251df-1bc8-33ce-83ba-46cab4529e52 | -9.8881 | -67.3299 | 2024-10-03 00:06:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 459e63e3-43cd-3db4-8a34-2c5e471960f6 | -9.9067 | -67.3294 | 2024-10-03 00:06:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c6c69c7a-27f0-3caa-8862-785dbf3fa086 | -10.129 | -56.7722 | 2024-10-03 00:06:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 12263a0b-0f82-30f7-8459-8ce0b38bfcd0 | -10.1802 | -57.2848 | 2024-10-03 00:06:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 158c7eb5-6569-3197-a856-b076e82971d8 | -10.1804 | -57.265 | 2024-10-03 00:06:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 6bb8bca3-064a-340c-80ba-96938599c617 | -10.4475 | -56.789 | 2024-10-03 00:06:05 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| e353af59-590b-3878-8573-14539d1ef8d5 | -10.6505 | -53.6994 | 2024-10-03 00:06:06 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| e2501615-a221-390c-922f-fe0a80bd1de4 | -10.6128 | -64.0611 | 2024-10-03 00:06:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 436b37bc-331a-3644-b367-ddf4c8940ac5 | -10.6129 | -64.0421 | 2024-10-03 00:06:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 1a472b8c-401a-3826-94fa-7a117ec364d7 | -10.8942 | -63.8971 | 2024-10-03 00:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d959d743-9c6b-3f8a-accf-d41198f91d16 | -11.2563 | -46.9348 | 2024-10-03 00:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| ed68bac2-1f92-3fed-b97e-2600908a0609 | -11.2567 | -46.9123 | 2024-10-03 00:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 3f7ee5e3-0352-3970-b099-8c86afc57add | -11.2758 | -46.9098 | 2024-10-03 00:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 7b3c523d-5b75-3996-824e-d2459c90c6d1 | -11.5982 | -65.1527 | 2024-10-03 00:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 67ff75dc-2241-3c05-b1dc-f96ad0671e80 | -11.5984 | -65.1338 | 2024-10-03 00:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d2a39155-d317-3d48-8ef1-1b8a839c464c | -11.6742 | -65.0172 | 2024-10-03 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 301d5697-288d-3cb6-89e8-0a099311133b | -11.6743 | -64.9983 | 2024-10-03 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ce0a1ce4-47a8-33e8-be48-a07ebc8c10ed | -11.693 | -65.0163 | 2024-10-03 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| a299f185-ee1d-3576-9740-24df6cce51fc | -11.9876 | -57.1877 | 2024-10-03 00:06:14 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 675eee88-3a8e-3a31-9a3b-a81cf8b6bc5f | -12.3851 | -62.9828 | 2024-10-03 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 97cb7777-4701-386c-8c22-bc1ea4125978 | -12.4038 | -63.0009 | 2024-10-03 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 8bf84f09-827b-312f-9d1e-3a845018ce64 | -12.404 | -62.9817 | 2024-10-03 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 7dcf2658-2330-398d-bc1b-786d015c73f5 | -12.6295 | -63.1225 | 2024-10-03 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 46311db9-306f-3842-bf20-578f9b3f76a2 | -12.6484 | -63.1214 | 2024-10-03 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 4af5a689-1a38-31b9-a522-890e1489abf6 | -12.6486 | -63.1022 | 2024-10-03 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 102.7 |
| ebb6a155-f80f-3952-b41c-4561df87cde7 | -12.7858 | -62.5174 | 2024-10-03 00:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2d1ff02b-4494-3c12-a9f3-5a1c4a97c33a | -12.786 | -62.4982 | 2024-10-03 00:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 45513c41-5eb3-3e28-bb9e-7edb736745e0 | -12.8047 | -62.5163 | 2024-10-03 00:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 86fb9ec0-5f42-3ea8-9c72-1caab9e8f3ac | -12.8049 | -62.497 | 2024-10-03 00:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 88395cb0-8897-342b-8f0a-f104f65cbdd2 | -12.8238 | -62.4959 | 2024-10-03 00:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 6dc47bbc-cc8f-3345-8b02-6e14dd265d0c | -12.824 | -62.4766 | 2024-10-03 00:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 7fa97497-4cac-37ca-a2c1-8fc0bcad8dc7 | -12.9741 | -62.6409 | 2024-10-03 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 6bda09a4-4ede-33bd-8311-339be8574a3a | -13.5195 | -51.1467 | 2024-10-03 00:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| fc98f8cc-a62c-328c-be71-61088b2377b6 | -13.957 | -52.5787 | 2024-10-03 00:06:25 | GOES-16 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d30040cc-7548-333a-b38d-9bdd2e3284a3 | -15.2332 | -47.5032 | 2024-10-03 00:06:31 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e723dfa2-99f3-3fb7-a6b8-8f3a1017b952 | -15.2528 | -47.4999 | 2024-10-03 00:06:31 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| c0335322-d18d-3126-98d0-efdbd67695b7 | -16.7594 | -57.8328 | 2024-10-03 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.8 |
| fd6ba484-bae5-3d8b-b4ca-ecd736e99c72 | -16.7597 | -57.8124 | 2024-10-03 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 175.4 |
| 3261f698-b2ee-35da-9889-7f58de07addd | -16.779 | -57.8306 | 2024-10-03 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.6 |
| e539cff1-a65d-308f-bee8-d5670ef71e6a | -16.7793 | -57.8102 | 2024-10-03 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.6 |
| 1455231e-245b-32ef-a8d6-0bfd0cd1a721 | -16.7985 | -57.8284 | 2024-10-03 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 3201f623-282a-3f11-9df3-4cf80ff7b898 | -16.7988 | -57.808 | 2024-10-03 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.5 |
| 418f8cd5-801f-32c1-ba18-3f29bc02bff0 | -17.8789 | -40.0946 | 2024-10-03 00:06:44 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 224.6 |
| f3477d82-80b8-38a3-a15d-36eee27a4502 | -17.8991 | -40.089 | 2024-10-03 00:06:44 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 152.6 |
| afae3c9e-1f7f-300d-8734-04236b72d4a8 | -17.8403 | -57.7076 | 2024-10-03 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.3 |
| b13f8eda-43d3-323e-985e-c8d5cc283527 | -17.8407 | -57.6871 | 2024-10-03 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| b593a7ce-e5e8-3d02-9f24-6fd8211359de | -18.8406 | -42.9235 | 2024-10-03 00:06:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| e01059bd-2450-32f1-a718-baa31f104392 | -18.8927 | -41.2248 | 2024-10-03 00:06:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.7 |
| 965d8ddc-6312-336d-9e74-3bcec9fb9e1b | -18.8935 | -41.199 | 2024-10-03 00:06:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.7 |
| e207634d-ec91-38f6-9597-3181b3c2895b | -19.0344 | -43.1944 | 2024-10-03 00:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.2 |
| 7e3d1ee1-95c6-3151-9b68-df878319767e | -18.7172 | -57.3305 | 2024-10-03 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| ee834cbf-eb7d-3bd6-bc84-6f035a43de10 | -18.7372 | -57.3279 | 2024-10-03 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 6eef51dc-f084-3049-b19c-e2a1fef8cf5f | -21.3067 | -47.599 | 2024-10-03 00:07:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 96.2 |
| cccc1bae-f3c3-3615-b0cc-29d3cb011a97 | -23.155399 | -45.127701 | 2024-10-03 00:07:03 | METOP-B | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cc697bed-30a2-3eb1-b51b-ea3bc8d58f8d | -22.588699 | -42.140301 | 2024-10-03 00:07:03 | METOP-B | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f7df7bc4-1496-389a-b712-461219a2676c | -21.3868 | -47.6734 | 2024-10-03 00:07:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 3b76b819-5a41-38bd-bdb7-30145f7a3152 | -21.3875 | -47.6497 | 2024-10-03 00:07:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 7dd2ac5b-8b7b-3924-a826-26a744363630 | -21.346 | -55.6626 | 2024-10-03 00:07:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 16d21a1b-dded-3bf3-8573-beae40254aff | -22.2307 | -48.4507 | 2024-10-03 00:07:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 102.3 |
| bc85a330-f6a9-3cb6-84f3-4177aa43d9d2 | -22.2314 | -48.4272 | 2024-10-03 00:07:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 462ad7d4-a008-331d-a498-aaf11d63429f | -22.2515 | -48.4456 | 2024-10-03 00:07:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 95977b0f-9819-3362-be56-fb11c4628a15 | -22.2522 | -48.422 | 2024-10-03 00:07:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 2074897e-3b6c-32fa-b091-899903712328 | -23.097099 | -46.573399 | 2024-10-03 00:07:08 | METOP-B | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d3890260-cfbe-355a-8902-193054ffa749 | -23.087299 | -46.575199 | 2024-10-03 00:07:08 | METOP-B | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9a627a9a-6882-3d7c-b166-1987bbac6827 | -23.090099 | -46.592098 | 2024-10-03 00:07:08 | METOP-B | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 528bb7c0-f5a8-3168-ad0d-bac640496026 | -22.3617 | -48.2307 | 2024-10-03 00:07:09 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 16a39190-3536-3ffa-9fa2-c864dcf9f4fb | -22.446 | -46.8576 | 2024-10-03 00:07:09 | GOES-16 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 05284f88-37e2-30dc-bfe3-7bc89e8eb825 | -22.286501 | -42.4758 | 2024-10-03 00:07:09 | METOP-B | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 86673030-88ec-3a17-9e3e-db223e324826 | -22.2883 | -42.485199 | 2024-10-03 00:07:09 | METOP-B | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 75835a61-befe-3fc0-92bd-986c0b59362c | -22.0765 | -42.0755 | 2024-10-03 00:07:12 | METOP-B | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2c5131c1-9f39-3fdb-9368-af68e8349679 | -22.078199 | -42.0844 | 2024-10-03 00:07:12 | METOP-B | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1a05556f-2851-39cc-924d-19ff50d24320 | -22.08 | -42.0933 | 2024-10-03 00:07:12 | METOP-B | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eef9fbd7-632e-325d-be3c-ec88a5be31b9 | -22.155001 | -42.533798 | 2024-10-03 00:07:12 | METOP-B | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ea745468-d889-3588-84fc-3e9969b633f6 | -22.156799 | -42.543201 | 2024-10-03 00:07:12 | METOP-B | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 91366e6a-6761-3e83-a866-c1fa62b68753 | -22.1471 | -42.545399 | 2024-10-03 00:07:12 | METOP-B | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 667acf1c-4e3b-3fd7-bd68-d1db34f3d05f | -22.8283 | -47.015301 | 2024-10-03 00:07:14 | METOP-B | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d2827ed3-7d57-38f0-8243-374c35647291 | -22.306999 | -44.051102 | 2024-10-03 00:07:14 | METOP-B | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d78c99d4-a174-3c04-883a-e48134e354e5 | -22.707701 | -46.646301 | 2024-10-03 00:07:15 | METOP-B | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6818b964-0c24-3c17-a6f3-f370f3ce77a2 | -22.710501 | -46.663101 | 2024-10-03 00:07:15 | METOP-B | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cba70323-2940-3bb7-ba17-26b6bd00ca26 | -22.698 | -46.648102 | 2024-10-03 00:07:15 | METOP-B | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a78aa6f-0bbd-3da4-8395-abe6b18c9d26 | -22.7008 | -46.664902 | 2024-10-03 00:07:15 | METOP-B | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 43760b60-1a15-319c-88e8-c2405ef1ecae | -22.6591 | -46.777401 | 2024-10-03 00:07:16 | METOP-B | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 92b10324-f015-3116-a24f-93832f2385d0 | -22.6619 | -46.794498 | 2024-10-03 00:07:16 | METOP-B | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb328c0d-d194-35e6-b19a-a99e7c3e16df | -21.5688 | -41.216301 | 2024-10-03 00:07:17 | METOP-B | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c8093b8-074d-3724-9399-7556e4a7e0e9 | -21.5704 | -41.2244 | 2024-10-03 00:07:17 | METOP-B | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b44bb1d-dda4-359e-b861-d08e3aa1cb9f | -21.559 | -41.218498 | 2024-10-03 00:07:17 | METOP-B | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a7da9a4-7b2f-398e-b0bf-399454e993ef | -21.5606 | -41.226601 | 2024-10-03 00:07:17 | METOP-B | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3abfa9d1-9b3a-30bf-9c71-a9091eb142cd | -21.5623 | -41.234699 | 2024-10-03 00:07:17 | METOP-B | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de4fe23a-e1ed-3060-a755-f477e9ccc352 | -21.785999 | -42.469501 | 2024-10-03 00:07:18 | METOP-B | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 834dcf45-1beb-3af3-84be-551ddadaa50b | -21.7878 | -42.478699 | 2024-10-03 00:07:18 | METOP-B | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b7195cca-5123-38ea-a155-18b349cb699a | -21.7896 | -42.4879 | 2024-10-03 00:07:18 | METOP-B | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 965b17ab-9432-3fe4-87ff-d67679727405 | -22.450701 | -46.851501 | 2024-10-03 00:07:20 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b79e4d17-f011-36be-b701-5324d310a583 | -22.438 | -46.836201 | 2024-10-03 00:07:20 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 402791a8-cee6-3825-ab83-28034965a345 | -22.440901 | -46.853401 | 2024-10-03 00:07:20 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6b85c93c-b237-3373-8ee8-1c4544203edd | -21.528799 | -42.041 | 2024-10-03 00:07:20 | METOP-B | CAMBUCI | RIO DE JANEIRO | Brasil | 3300902 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 58d55117-211e-3336-b330-41c083c23c6c | -21.5305 | -42.049702 | 2024-10-03 00:07:20 | METOP-B | CAMBUCI | RIO DE JANEIRO | Brasil | 3300902 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README3.md)
