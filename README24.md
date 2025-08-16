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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea060a56-73f6-3262-b2db-80e742617749 | -19.93543 | -41.24585 | 2025-08-16 03:47:00 | NOAA-21 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ee4bdb65-4289-35d5-8f2f-676cd8a23e0a | -14.52362 | -48.58378 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23031566-20d3-3454-8d79-bfa49a7f5c9d | -17.21796 | -49.59225 | 2025-08-16 03:47:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fdd1c33-68df-36a0-b7c6-c11c6d2b3617 | -19.52465 | -43.62775 | 2025-08-16 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee4d955a-eb81-391f-b134-bb15bc6dbdcf | -14.58876 | -47.91247 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a66fb4a4-1827-3511-9e29-acdc5c5f29a8 | -19.66592 | -49.37436 | 2025-08-16 03:47:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0375b8ac-e4db-3d7a-a03e-21fc27fec7c9 | -14.5871 | -47.92616 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ee799a9d-ca92-3ea5-8b3f-6dd286260437 | -17.50825 | -44.88634 | 2025-08-16 03:47:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 609a42a9-851a-30ff-8c82-78fc6a4f2378 | -14.59278 | -47.92211 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b4e6327-b807-36b8-91d4-313f398d7891 | -14.53057 | -48.58025 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ed3f1a6-aa88-3b81-9a4b-15c2343ae435 | -20.41606 | -46.53894 | 2025-08-16 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35e479c2-607c-3f31-9b04-d858dcd6af9b | -20.46128 | -46.20943 | 2025-08-16 03:47:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8819a57-3dec-3a27-97e0-b21cbb14f1b1 | -20.15549 | -48.92164 | 2025-08-16 03:47:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb09edd0-8cdd-36cb-bede-9c3d82fe11f3 | -14.58628 | -47.93008 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9bc1f9bc-7484-3469-8606-d68361018ee5 | -14.58204 | -47.91623 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d45710f7-b86f-33b6-98dd-d22729e57d57 | -20.00701 | -45.55682 | 2025-08-16 03:47:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bed7f8a1-a8c8-326e-a020-b5bc610b8016 | -14.58389 | -47.90704 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7b8f3c7e-b134-363e-a61d-9d03f4ccac82 | -16.24056 | -51.12828 | 2025-08-16 03:47:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8780bf60-4750-3824-92fc-5d3cb5a5b531 | -17.73481 | -39.52378 | 2025-08-16 03:47:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a466c4d3-cb38-3051-b977-0ca010f4eee4 | -14.60719 | -47.94445 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0e681ca-9e6f-3198-be03-053d12e88a36 | -14.59772 | -47.93248 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9fab14a-8e61-38d3-9f3f-3e71a4944fe3 | -16.24726 | -51.12977 | 2025-08-16 03:47:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b3f0e3d-7280-3d69-aa15-227e37f6d965 | -20.08421 | -49.42848 | 2025-08-16 03:47:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 76a2ebe4-1dd8-3580-8e4c-51f67f626acf | -17.60678 | -46.68708 | 2025-08-16 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| bca46e2b-14bd-3c3a-a5f4-1c5441a91327 | -20.42169 | -46.53542 | 2025-08-16 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1235a349-2789-3170-b41c-6a94148a6525 | -14.58393 | -47.91276 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 049dad12-2503-3bdd-8d42-755b700f983b | -20.41866 | -46.54388 | 2025-08-16 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7212c01-0848-3c4a-b1a0-38517c879d13 | -14.59859 | -47.9283 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f45797a-c777-37c7-bfeb-46e2915e3dc3 | -15.89872 | -48.31748 | 2025-08-16 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d2d3c5f-f9eb-3d17-98c9-00ad127de8bd | -14.53654 | -48.58148 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d94c97e-e327-34f7-b2e5-485b96bcc463 | -14.57813 | -47.91195 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01de93cd-c90f-3b58-8894-c00eb2a63adc | -21.38193 | -45.74554 | 2025-08-16 03:47:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 70a92979-7af9-3d36-8d3f-07dc26787d83 | -15.90106 | -41.61024 | 2025-08-16 03:47:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4850403c-98db-3b69-b8f0-2b972cf4130a | -20.0795 | -49.42291 | 2025-08-16 03:47:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 919e8fd0-b5fc-36c2-8159-a5cf338aff56 | -20.15827 | -47.2916 | 2025-08-16 03:47:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dac7daf9-e042-37b0-9239-7e59ae0099c5 | -16.22846 | -51.11958 | 2025-08-16 03:47:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c27cc1ef-8879-3cea-8c70-e70f33328e35 | -14.51928 | -49.38995 | 2025-08-16 03:47:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8e49b017-2927-3e23-8248-45668463eda1 | -14.59198 | -47.92611 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0dd7107a-dbaf-374a-975d-838c6dc74f5b | -18.87325 | -40.14515 | 2025-08-16 03:47:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fd44e4fc-117e-31c3-a1e6-ab063e2e0ff0 | -14.60816 | -47.93977 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35cf1f6c-4a9d-3cea-b360-05196fd7226e | -14.58488 | -47.90822 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a183f260-9668-3a5e-9642-75ca0b4a34d9 | -20.04826 | -44.63028 | 2025-08-16 03:47:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 766f004f-790e-3fb1-9176-2ced00d41e8f | -14.58971 | -47.91363 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f3853018-6eb9-32de-8618-b91c45599b56 | -16.15461 | -40.35112 | 2025-08-16 03:47:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e8fb0864-3ef1-3ac9-9f16-b52de77243be | -14.58542 | -47.92905 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f2413d6c-7bc0-3abd-9fd2-3a81d7e65006 | -15.90334 | -48.31953 | 2025-08-16 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0dd1985-5df6-35f2-ba7b-4d57d9529d39 | -14.52959 | -48.58498 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28770b7a-2ae8-3762-a77e-a4cb2c4fb30b | -20.39384 | -46.49679 | 2025-08-16 03:47:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd5f84b9-510d-33c7-af11-08285aeb6a5f | -23.78914 | -51.88488 | 2025-08-16 03:47:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 24eaf8ec-648b-3baa-9d29-96106f5fb565 | -17.613 | -46.68214 | 2025-08-16 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5247241-1908-35a5-bd08-d14d56f6fd47 | -19.91945 | -44.70749 | 2025-08-16 03:47:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a134761-04f6-34f1-8811-bf6126b368ad | -14.60151 | -47.943 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a69a4b7-d0ae-3d86-9655-c1e20b6ceb8b | -21.55418 | -46.85486 | 2025-08-16 03:47:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9c21593d-cc5d-379f-ad59-b1c66ac3f20d | -24.24165 | -50.20898 | 2025-08-16 03:47:00 | NOAA-21 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| afa56881-8084-3407-8bbc-8400e01f69fb | -15.89124 | -48.32021 | 2025-08-16 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7e89f0e-3be5-3065-9d14-92bf0f3a235a | -20.67384 | -49.3892 | 2025-08-16 03:47:00 | NOAA-21 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3635105e-6b8b-333b-9a33-b781d07f4663 | -20.15088 | -48.91649 | 2025-08-16 03:47:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 375fb264-145a-3d02-961d-c02d6c43d8a6 | -20.41725 | -46.53322 | 2025-08-16 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c6c1747-8455-3e8f-bb21-cc0a841ac4e8 | -17.21201 | -49.59057 | 2025-08-16 03:47:00 | NOAA-21 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec862158-a001-32c0-a66d-13b19525c456 | -16.87476 | -44.13805 | 2025-08-16 03:47:00 | NOAA-21 | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89adc81f-957c-3fd9-bfe0-6a7b95dc916b | -15.8969 | -48.32175 | 2025-08-16 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c31e52b-bab7-37e9-bad3-ad053924abfb | -20.41975 | -46.53846 | 2025-08-16 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5339e6b3-fe55-323f-8b53-889d2f3f4fc8 | -16.23388 | -51.12674 | 2025-08-16 03:47:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4d999694-8a4a-322c-979b-15d6b56022c4 | -14.5277 | -48.59415 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a708eb0-fea6-343f-9d2f-263de84f4c8c | -14.58296 | -47.91737 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a3ee1ad6-2ad9-3587-9f07-879cd009cce9 | -18.04103 | -47.72551 | 2025-08-16 03:47:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e7533566-3521-3cef-8e0a-3effafe01537 | -17.73431 | -43.52153 | 2025-08-16 03:47:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 263d3a80-0f87-31b1-813d-57161d60b46b | -15.89769 | -48.31795 | 2025-08-16 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abfcf28d-365a-307d-b6e1-a4d9b86fa183 | -14.58785 | -47.91699 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ff26cf9f-20fe-322e-a9aa-ac36383d009a | -14.60343 | -47.93378 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08de79c0-ab18-376f-9b7a-127aaf8f51c5 | -14.58297 | -47.9116 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 16f26d1e-156d-3349-a94c-54f4b0722826 | -14.53373 | -48.5951 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90e040a1-ac49-3edc-91bd-8bbeb58202ab | -20.41758 | -46.54928 | 2025-08-16 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d087a323-d30c-39f8-a9d6-805034612548 | -14.58619 | -47.92522 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fbfc46ca-35ad-360a-93b8-4ebeed914f5a | -17.21688 | -49.5972 | 2025-08-16 03:47:00 | NOAA-21 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07331aa0-3cd7-30a1-afe8-922dbc31eaa5 | -17.61239 | -46.68515 | 2025-08-16 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3618adfb-8cca-3117-9450-593b9485922f | -20.42055 | -46.54094 | 2025-08-16 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e58725e8-651b-3756-a817-ac1f9a5ecc58 | -14.60906 | -47.9354 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6512879-6c3d-360f-835f-79ead24be460 | -20.15851 | -47.29283 | 2025-08-16 03:47:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 669775ff-4a9a-3c7e-991a-12ed65755273 | -16.75338 | -45.06213 | 2025-08-16 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae6b2105-e066-345b-97ec-dcbc2f6b1290 | -15.89791 | -48.3213 | 2025-08-16 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5449d8e9-0945-3ce6-b4a6-4cfe5ce89602 | -17.73526 | -43.52111 | 2025-08-16 03:47:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 953c5577-7d34-3bb5-845e-3accbcda1226 | -16.23539 | -51.12001 | 2025-08-16 03:47:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bb7ee6a0-4688-3ea7-b778-6adc5ff41ac9 | -14.58965 | -47.90802 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 909d1107-2ee2-3f62-933a-8b8d637d0bbd | -23.5402 | -47.58532 | 2025-08-16 03:49:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f898b0b3-347c-3fd5-82f0-d1f242a473db | -22.53745 | -46.89757 | 2025-08-16 03:49:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| c5447021-feaa-3c14-b9c8-5b46b13c912a | -22.53205 | -46.89289 | 2025-08-16 03:49:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 35fc134a-3b81-31d8-8574-455794c97561 | -29.78969 | -50.42791 | 2025-08-16 03:49:00 | NOAA-21 | CARAÁ | RIO GRANDE DO SUL | Brasil | 4304713 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5aac27f5-18d4-3b49-ac0f-aeff3359ac6d | -22.53664 | -46.894 | 2025-08-16 03:49:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| ce8dce84-023d-31cd-991c-333d6b290c94 | -22.53962 | -46.88685 | 2025-08-16 03:49:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 41.9 |
| c1662b07-09b8-3b79-9fac-9db4a5c537f6 | -22.8597 | -45.29348 | 2025-08-16 03:49:00 | NOAA-21 | ROSEIRA | SÃO PAULO | Brasil | 3544301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5c485f0d-ea94-3289-a30c-b28f61418d3b | -22.53777 | -46.88863 | 2025-08-16 03:49:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| 71306eb1-66b4-3a05-8271-c04967f43327 | -22.86259 | -45.29516 | 2025-08-16 03:49:00 | NOAA-21 | ROSEIRA | SÃO PAULO | Brasil | 3544301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 167d8330-410c-3916-a037-9ec48397be43 | -22.53886 | -46.88343 | 2025-08-16 03:49:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 9a9bd213-268c-3781-a7da-297c0163e955 | -30.34257 | -52.37066 | 2025-08-16 03:49:00 | NOAA-21 | PANTANO GRANDE | RIO GRANDE DO SUL | Brasil | 4313953 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| fd823b45-6035-3320-9790-fc8aa88d72b8 | -22.53394 | -46.8911 | 2025-08-16 03:49:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 2220e8a6-fd4f-3104-9f99-a7bdb5b4a0e9 | -22.95836 | -46.69882 | 2025-08-16 03:49:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 97cd8bd1-11df-3b6f-bc4d-cfbd947bae92 | -22.98084 | -48.80629 | 2025-08-16 03:49:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dcb88c8-d656-3e58-b723-9100a985226c | -22.53853 | -46.89221 | 2025-08-16 03:49:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 3a7ecf48-5784-329d-a9a1-bc1c66cd9d22 | -23.17952 | -46.75718 | 2025-08-16 03:49:00 | NOAA-21 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README25.md)
