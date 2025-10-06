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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99b087ea-d959-30eb-b010-8a8d77235299 | -22.5282 | -43.57816 | 2025-10-06 12:02:00 | TERRA_M-T | ENGENHEIRO PAULO DE FRONTIN | RIO DE JANEIRO | Brasil | 3301801 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 513621ec-aa76-36eb-9ac1-7bc4761a62b1 | -21.38747 | -45.07491 | 2025-10-06 12:02:00 | TERRA_M-T | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 78b0e479-dbde-3c7a-bf5d-2b202be1014e | -21.39149 | -45.04651 | 2025-10-06 12:02:00 | TERRA_M-T | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.9 |
| 965652cd-59d5-3b9a-8986-9ef672f9bb83 | -19.59581 | -44.65179 | 2025-10-06 12:02:00 | TERRA_M-T | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 25.5 |
| e0bfd956-9961-33b0-a04c-feb482ecd85c | -22.63601 | -44.57325 | 2025-10-06 12:02:00 | TERRA_M-T | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| c768f2bf-0db5-3796-8c56-4a2ad5d09323 | -21.64848 | -45.88685 | 2025-10-06 12:02:00 | TERRA_M-T | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 70ae1738-8064-3cb5-ab58-7d92c6d7f897 | -19.48069 | -44.87614 | 2025-10-06 12:02:00 | TERRA_M-T | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4b3ac7eb-6f37-332a-8bf1-ef65dd39e896 | -18.26727 | -53.3147 | 2025-10-06 12:02:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 37.8 |
| db0a81f6-24eb-333b-8759-015b6bf05c79 | -18.40042 | -45.20911 | 2025-10-06 12:02:00 | TERRA_M-T | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| f8ff5f56-a570-3d3a-8874-a05a52ddc391 | -20.68649 | -43.48604 | 2025-10-06 12:02:00 | TERRA_M-T | CATAS ALTAS DA NORUEGA | MINAS GERAIS | Brasil | 3115409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 34aa0f85-baf7-3ca5-b3ea-c8ea149829d9 | -18.27965 | -45.40346 | 2025-10-06 12:02:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f6e62ae3-1dfe-363b-a6a4-34e84837577e | -19.59713 | -44.64246 | 2025-10-06 12:02:00 | TERRA_M-T | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7ffbf26d-eef9-34c2-8258-7f25ceb22635 | -23.18881 | -45.63086 | 2025-10-06 12:02:00 | TERRA_M-T | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| 557ffc85-d717-3001-93b9-c69341cf106b | -20.68784 | -43.47594 | 2025-10-06 12:02:00 | TERRA_M-T | CATAS ALTAS DA NORUEGA | MINAS GERAIS | Brasil | 3115409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 41.8 |
| d3dd01e0-9b2d-3b60-8eac-84824c786104 | -21.42752 | -46.51083 | 2025-10-06 12:02:00 | TERRA_M-T | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 4996704e-2329-3c66-b4c1-cd2e22843fc4 | -22.84115 | -43.43395 | 2025-10-06 12:02:00 | TERRA_M-T | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| b390f814-f250-3ae6-b1a6-87127dd99968 | -18.41612 | -46.7622 | 2025-10-06 12:02:00 | TERRA_M-T | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 496d8cb9-d280-3afd-94c7-7748d204f42d | -19.87618 | -44.03027 | 2025-10-06 12:02:00 | TERRA_M-T | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 2060b46c-15f8-301f-ba75-39f673ace067 | -22.83208 | -45.548 | 2025-10-06 12:02:00 | TERRA_M-T | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 9b319b00-5f55-384c-8824-183cecc1e125 | -19.50196 | -44.86634 | 2025-10-06 12:02:00 | TERRA_M-T | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 36.0 |
| ca6da166-33a1-38f5-8529-7996d1361a4e | -18.02547 | -45.00226 | 2025-10-06 12:02:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ea15fc1b-d734-3d0c-9063-7c31b40fa7a9 | -20.42239 | -44.14043 | 2025-10-06 12:02:00 | TERRA_M-T | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 2dc71024-eb06-3e92-a64f-ddf49b4bac81 | -19.58242 | -47.88364 | 2025-10-06 12:02:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9806e637-5338-3bc9-94e9-405666046994 | -20.35164 | -47.03227 | 2025-10-06 12:02:00 | TERRA_M-T | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f91b74a9-edcc-3648-97c7-cf3fed0b79f6 | -20.34698 | -44.0893 | 2025-10-06 12:02:00 | TERRA_M-T | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 2701ef33-5c11-35fb-9437-a82055401fd7 | -21.39499 | -45.08575 | 2025-10-06 12:02:00 | TERRA_M-T | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.1 |
| df07d33d-33ac-3b04-b255-eeec0e8e34b1 | -19.50063 | -44.87567 | 2025-10-06 12:02:00 | TERRA_M-T | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 197ec5ac-403b-3363-af9b-8a1306d9ce37 | -21.18188 | -46.3027 | 2025-10-06 12:02:00 | TERRA_M-T | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.4 |
| 11cb3f5d-699a-301c-9ce1-8d439354a23f | -23.39009 | -45.38095 | 2025-10-06 12:02:00 | TERRA_M-T | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| e97af715-3173-348d-825c-7a3ceb75054d | -21.84225 | -45.95693 | 2025-10-06 12:02:00 | TERRA_M-T | POÇO FUNDO | MINAS GERAIS | Brasil | 3151701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| b30e3f63-53a7-3a37-b697-54cc82bc0830 | -22.03878 | -45.29601 | 2025-10-06 12:02:00 | TERRA_M-T | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 51e17048-5716-3089-b13f-86ad99d18833 | -19.5033 | -44.85701 | 2025-10-06 12:02:00 | TERRA_M-T | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 939b3c9d-8a04-3198-a9e7-1fcdd63a7bec | -21.49128 | -46.02033 | 2025-10-06 12:02:00 | TERRA_M-T | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 373fe15d-6893-33b4-9130-a217606f7a9b | -18.02682 | -44.99298 | 2025-10-06 12:02:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 04253603-5ef0-30d4-bdda-bdce2af5468b | -21.30878 | -43.84429 | 2025-10-06 12:02:00 | TERRA_M-T | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| e08510ba-e433-3dec-8cee-3841e63a6cc6 | -18.28716 | -45.41425 | 2025-10-06 12:02:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 911c81a1-7c2f-3e03-b711-508462459161 | -18.74632 | -44.47526 | 2025-10-06 12:02:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1a7235f5-2b5f-3a9d-98bc-753fdfd8f990 | -21.31012 | -43.83421 | 2025-10-06 12:02:00 | TERRA_M-T | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 0d7503d2-3074-3e2a-9204-2e53b72b7380 | -21.32225 | -44.28935 | 2025-10-06 12:02:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 911a24f0-8b0b-3a24-bf53-594b333236ae | -18.27552 | -45.43147 | 2025-10-06 12:02:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dda4d6af-6e44-3e75-beac-98d07f414e75 | -21.95396 | -46.44838 | 2025-10-06 12:02:00 | TERRA_M-T | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| b89b0944-4a3c-3da5-99ca-c4db0c060328 | -19.02824 | -45.01851 | 2025-10-06 12:02:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 80903fa8-d3ed-3673-8436-5713f33ce7c9 | -19.02689 | -45.02781 | 2025-10-06 12:02:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 17701782-feb1-3f91-b18a-a5053820bf38 | -22.12477 | -45.00756 | 2025-10-06 12:02:00 | TERRA_M-T | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 308b5077-f54a-34f6-9720-c520ef2e0b98 | -20.20012 | -46.14086 | 2025-10-06 12:02:00 | TERRA_M-T | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 980767ee-d465-3eaf-968c-1edcdc7035ee | -22.994 | -46.14407 | 2025-10-06 12:02:00 | TERRA_M-T | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| fbd2e91b-8f7c-3f7e-bc95-a2f777bd5841 | -18.13465 | -53.36804 | 2025-10-06 12:02:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 54.4 |
| ca7e17a6-303a-327b-a09e-e3f81b86fa85 | -20.35009 | -47.04235 | 2025-10-06 12:02:00 | TERRA_M-T | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 200b9c44-8efd-351f-8b4c-469e72443632 | -21.6471 | -45.89633 | 2025-10-06 12:02:00 | TERRA_M-T | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 68081d2a-2333-3760-9049-9c1178335bef | -20.00301 | -45.78793 | 2025-10-06 12:02:00 | TERRA_M-T | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 97d9636d-9b9d-30fc-ae61-421406b8d619 | -21.40974 | -45.05588 | 2025-10-06 12:02:00 | TERRA_M-T | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.1 |
| 6dd9b48e-36bf-32fe-97fb-c84856e4bcc8 | -12.9812 | -46.8051 | 2025-10-06 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5536e988-5ae8-33c2-9016-917b335b3a83 | -12.1458 | -50.9523 | 2025-10-06 12:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 5c28eb26-c15c-3b4a-b59e-18d3c45aac5d | -8.6139 | -46.3227 | 2025-10-06 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| baa5a81b-2bfb-31f6-aa44-47f1297ecec6 | -14.6985 | -45.1858 | 2025-10-06 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 53566e6a-3152-3660-a502-f1f27c665bc6 | -10.4285 | -50.3518 | 2025-10-06 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| fc4910a9-2ce8-36a2-b0ae-af615dc0d553 | -10.4288 | -50.3305 | 2025-10-06 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| b954756e-b97a-32d2-b1b7-f09f158ef06a | -17.9748 | -44.3835 | 2025-10-06 12:10:00 | GOES-19 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 53fc2fdc-187a-3007-af8a-e21de3f6243e | -14.6897 | -48.3797 | 2025-10-06 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 1069ec49-e871-36c6-8769-2808d51ed40d | -14.6893 | -48.4021 | 2025-10-06 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 151.1 |
| ad4115e7-57b5-31c4-9a2d-3bccda6f2391 | -21.4055 | -45.0614 | 2025-10-06 12:10:00 | GOES-19 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 113.6 |
| 2dd68a29-26be-3276-beaf-e81f84049ffa | -8.6327 | -46.3208 | 2025-10-06 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 69d58f2f-5743-3152-9465-88a2f6439bed | -15.3546 | -47.3007 | 2025-10-06 12:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| e03252df-1f86-3084-94e4-844bc67c44ad | -14.6991 | -45.1624 | 2025-10-06 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| afc9bda0-f0a8-3d66-8c73-753e061fa27c | -17.842 | -57.6048 | 2025-10-06 12:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.9 |
| da54cd05-33d4-338c-bba1-5e38bf3268a6 | -11.8033 | -45.0856 | 2025-10-06 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 8294c2c9-3b35-3a70-bdb0-c5849403e202 | -12.3796 | -47.1633 | 2025-10-06 12:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 62deee07-7f13-3be7-bc8f-2669d931053a | -18.1371 | -53.3732 | 2025-10-06 12:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 219b5973-e9c6-3504-8703-7ed992b9c484 | -8.6144 | -46.2778 | 2025-10-06 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 870ca115-3b84-3562-91ff-72d3c1945529 | -8.6141 | -46.3003 | 2025-10-06 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| b8b12b0c-dfe1-30a3-8ec6-c8c24d07f856 | -17.8417 | -57.6254 | 2025-10-06 12:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.6 |
| fe6249c9-f25a-38d9-9889-df67bc28652d | -14.5438 | -46.9633 | 2025-10-06 12:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 47d9641d-c347-39d4-a464-8dd0d698fd86 | -14.3161 | -52.9764 | 2025-10-06 12:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| aba41aaf-9240-346e-9d02-1ac3c3604e84 | -14.863 | -51.5019 | 2025-10-06 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 45f9aa65-0c99-3384-83d6-f182111b4a9b | -14.8626 | -51.5234 | 2025-10-06 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a86c3946-525c-3d92-aa9d-db05205e83ec | -18.2574 | -53.3114 | 2025-10-06 12:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 2405d703-e673-3076-9593-581a53ac54be | -8.6141 | -46.3003 | 2025-10-06 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 09a32f3e-db0a-3641-923a-5fc1071fd4b9 | -18.1366 | -53.3946 | 2025-10-06 12:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 91866def-4c81-343e-a1ce-e5bb4f3bd798 | -12.5929 | -48.1144 | 2025-10-06 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| bbd7f88c-082d-3a1e-b498-c710571bceb1 | -15.5637 | -52.4516 | 2025-10-06 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ffc70799-1d09-3f6c-a61c-ac7f9315154a | -8.6327 | -46.3208 | 2025-10-06 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| e5ba5131-22a8-337a-96eb-18523f1ccd0f | -18.1172 | -53.3763 | 2025-10-06 12:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 0761b240-2d4a-3c49-8fd8-93acf2c7ef2a | -15.3788 | -47.9972 | 2025-10-06 12:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 69.9 |
| a7637e43-32fe-338e-bf6e-5563e78b2db0 | -14.6991 | -45.1624 | 2025-10-06 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3650d4d9-e57d-393f-91a5-d109479f736c | -14.6985 | -45.1858 | 2025-10-06 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 1d58f161-c11d-3913-913e-d13c20126bec | -18.2769 | -53.3298 | 2025-10-06 12:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 3f06fed7-510e-3be6-b73a-27b44257e7eb | -8.6139 | -46.3227 | 2025-10-06 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| bd0fe904-8536-3566-a3f5-bcd7f39cdf8a | -18.2773 | -53.3082 | 2025-10-06 12:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 2b227c01-13ac-3704-aa67-f7f50b676a4b | -14.2754 | -45.8647 | 2025-10-06 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| e726327e-1629-39e2-9a35-6fa15729caeb | -14.6897 | -48.3797 | 2025-10-06 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 55227cc9-0d4f-3081-92d5-e673649b0fe1 | -8.6144 | -46.2778 | 2025-10-06 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4f94cd03-f633-3ca6-932b-1b4327cf9308 | -17.8417 | -57.6254 | 2025-10-06 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.9 |
| e1da6e12-a6af-3864-be24-c57629aaaba1 | -12.3796 | -47.1633 | 2025-10-06 12:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 07a800ce-5ef2-33ed-bc58-cc9b87d17700 | -15.3546 | -47.3007 | 2025-10-06 12:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 2133b72b-27a8-3418-b529-77e6e34797c0 | -18.1371 | -53.3732 | 2025-10-06 12:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e25b3590-9285-315c-b11d-34de46fff019 | -18.1167 | -53.3977 | 2025-10-06 12:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 6dc55144-dc7b-35e3-a930-ceff2e2a16a5 | -14.6893 | -48.4021 | 2025-10-06 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 06c09bbf-2ab8-3b86-8dc8-45001ec65c57 | -12.8954 | -47.2909 | 2025-10-06 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| a43d7acd-cab6-3f0c-9622-a76ee0c26b29 | -11.8038 | -45.0624 | 2025-10-06 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 2978c82e-a6d7-34ee-9cb4-95caa004ece3 | -9.9779 | -48.7405 | 2025-10-06 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |


[Clique aqui para ver as próximas entradas](README85.md)
