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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4513d86-e67e-3eac-a2aa-02af86d3680d | -7.13188 | -59.65336 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bdc4546-5a1b-34bc-bdc7-dad1f45f3159 | -8.99787 | -60.51552 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cc311f3-db60-3762-8a4b-ab32759a6035 | -9.3903 | -60.5484 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0296bcde-774c-3256-ba72-82861bfb1dbd | -8.98362 | -60.56371 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d290343a-8f62-30ca-9b57-3dd924c41038 | -7.56663 | -61.42916 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 460d2c96-f0e2-3632-a46c-664a76cefb22 | -6.93285 | -59.64502 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e380635a-4d1d-3ba4-8403-b8d8fb300519 | -8.9752 | -61.70872 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 74b61cbf-9b55-35b6-a2ad-8c56401d19b5 | -8.15469 | -62.77583 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 499dc965-02c9-3ba3-9858-cf4eaddce3e8 | -7.95119 | -61.75196 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f220e853-a4cf-343f-a51b-9d755dfe8236 | -7.07349 | -59.23161 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5dbf7f36-6dcf-3ac1-b8c6-c4f7269ca5fe | -9.15181 | -59.66904 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb5f349f-1076-3efc-a60c-79699351bb18 | -8.40566 | -70.43712 | 2025-08-16 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5992bc71-1c28-3353-888d-22371ba97f57 | -9.19122 | -59.69024 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ab53a39-8eaf-3320-a29a-1eacc824d437 | -8.71658 | -62.4617 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19642523-4374-3b1f-9da9-9dfc62b6b260 | -9.21256 | -59.6408 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27f21822-f712-31c0-b3e6-11a645085868 | -7.90859 | -61.74163 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95a838fd-ca8f-3f9f-8a73-1556adfbd3ee | -8.70112 | -63.96132 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74fa7ae0-202a-368a-a12b-bc753e9d4c5b | -6.90959 | -59.55021 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5b7eebc-a36c-3942-b05d-bb757cb6dc13 | -6.93699 | -59.55083 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9679fe2-0c56-3f0b-86f0-1b5fa2ec0a0a | -9.00283 | -60.50548 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7646b3a-75f6-3b2a-8d87-049db06e0ad6 | -6.90659 | -59.63732 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fdf9f7d-cdf9-32f0-8662-8fa9ec3cc528 | -7.06616 | -59.2342 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddcebac5-6f3e-3e31-b894-c9e072ce81c0 | -6.93581 | -59.53601 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 899f8965-1d4e-388b-92f1-1ff1ffa5fc79 | -3.9883 | -47.88665 | 2025-08-16 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5e97fb54-30ac-3ccd-bafc-362406a1be7f | -6.92965 | -59.53137 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3ae11fc-1e86-33b4-9ff7-2f6446efbc92 | -9.50908 | -60.52697 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 53912b9f-9315-3e7d-953f-23a8529d8419 | -7.52895 | -61.32362 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85f83fc1-004a-3e4f-916e-a2076f79157c | -9.53184 | -63.57819 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb95f7bf-5a92-3d11-805f-60c3468cd876 | -9.00343 | -60.52362 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e415bab-c536-3f94-ba53-f69e9f939b0b | -6.9367 | -59.99631 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8306a83-6f68-3f37-a3c1-e82f82078f88 | -9.00065 | -60.51958 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95e6effe-2b66-3acc-85cc-34ab5dae2462 | -9.51133 | -60.53456 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 511eb64e-59a8-3056-93f6-df7ba0701398 | -6.93917 | -59.53654 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34200ad7-15fe-3d1d-8cb1-a29a87adaa59 | -9.51466 | -60.53508 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3f25a5fe-b292-3292-a2ad-257dd4a0f528 | -6.48336 | -62.94249 | 2025-08-16 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a690d854-55fc-3f3a-adcd-55d9d653519c | -7.90305 | -61.7551 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c8e0803-8edf-3e34-adee-68798b8941f1 | -9.21886 | -59.66812 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe93412d-0751-31d2-af9d-d745c04fb3e5 | -8.78485 | -63.6953 | 2025-08-16 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34763b6f-6cbf-3306-8a2b-0a580f3725b9 | -8.80312 | -52.0732 | 2025-08-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6dea1b1d-b9c6-39ce-8e44-114349df9f36 | -9.92348 | -60.48243 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76def681-0421-38ea-859e-c832b26856fb | -8.57135 | -69.69331 | 2025-08-16 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afbc5f12-1176-303f-a71e-4dac7675a2d7 | -8.90294 | -60.7341 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63ea217d-bbb1-3062-b1c6-764f9d60bd68 | -7.06561 | -59.23784 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ca78991-ca3c-3b27-a102-b0137346da76 | -6.94917 | -59.51611 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07f5ec43-9247-385e-b31c-8f6014573ecb | -9.16027 | -59.63644 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb5d043a-0952-396f-b419-9f137062408f | -9.81908 | -63.01405 | 2025-08-16 05:23:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdf8d3ba-c777-3407-b6e1-8bdbc53586f0 | -8.9923 | -60.50743 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c149293d-5c4b-3f48-b073-2fe699f01c60 | -7.81344 | -61.32997 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdecb0af-968c-3b2f-a58c-ed65fd31f257 | -7.87257 | -61.81848 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee5a3923-8fbb-3b01-9097-ad624be16a49 | -8.46942 | -64.04838 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b556a1b7-782b-3a0c-8795-d3f888f3b789 | -9.17385 | -59.63852 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dfb28a6-1315-32f6-a4f3-fc5b93700e31 | -7.67419 | -63.31387 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5be0b5f7-5a1a-3705-a512-eb3ad02895ab | -8.98471 | -60.55667 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 593edb58-5d5b-385a-8cc3-3afde2a2acfe | -8.56221 | -63.92307 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f67e50b-ede0-3961-8e23-99b19d18fe00 | -10.01456 | -59.2196 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a554d657-622e-31ce-98e8-873cb06e740b | -6.76474 | -59.48029 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61710885-3b53-307a-8111-0aa334216e75 | -9.78954 | -61.50375 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1337ec02-7023-37e9-8343-794dad2b448e | -6.80334 | -59.82418 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8eccf5d6-c7a4-374a-991e-7f171a54981b | -7.44266 | -60.02083 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b848d635-28a7-3de7-9903-cfde53309306 | -10.01165 | -59.2152 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ebedb07-891b-3d3c-a5d8-19065dedd5fe | -9.93738 | -60.48093 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b53952f4-6509-3dac-8877-60487e33b71a | -8.99183 | -60.53259 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7efd35ce-6b6c-3359-acdb-fb01a540eaa9 | -3.38343 | -52.71686 | 2025-08-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a94921b5-c09a-3603-b63e-07ab869945d3 | -9.22109 | -59.6534 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e6d45711-69b0-3cc8-bd0e-cafe2400fe4e | -8.55386 | -63.92989 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bc2751b-8845-3ab1-b249-55418e223e5c | -7.52841 | -61.3271 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0dc6474c-f86f-3990-b5d5-b479f377d70b | -6.94972 | -59.51253 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d27d5951-57c7-3b3c-812d-8b6fa6ee0d17 | -8.92887 | -62.23717 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bb1e12d-8b83-322e-b82d-b75480bae8f9 | -6.94034 | -59.55135 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3c84642-39b1-3dd4-b737-7a950cae6315 | -8.9841 | -60.53858 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 4c7ef553-c374-3f12-b03b-38d53fb86d0a | -6.94753 | -59.52684 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f46da3c-7f39-3012-9183-01012d97448e | -9.16423 | -59.63327 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d880f7c2-1962-31d8-bceb-5c39cbf48ba8 | -9.85359 | -62.22035 | 2025-08-16 05:23:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d274e08-b87f-30fe-88b5-759a54cb506f | -7.52731 | -61.33403 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d2d3574-9941-3d3a-bbc9-92432101478e | -7.56994 | -61.42968 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c69eeda-e2fe-3ba0-be04-173d6ff42cd4 | -7.90693 | -61.75212 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4d48a38-14aa-3b4f-86f2-ef638ecdce02 | -7.52397 | -61.31218 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2411c4a2-7ae3-3c85-b37c-067a7652f6e8 | -3.98754 | -47.89182 | 2025-08-16 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 497c1a12-3709-39cb-a00b-6c87ab843b85 | -8.90445 | -60.54784 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43eb7f47-1e5b-34c1-931f-9c465c958e9e | -9.49971 | -60.54362 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2ca96a3-05ef-35b2-aa77-66c3582a4a80 | -6.95089 | -59.52737 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d18dae79-f3b7-34d1-810c-67a46e921f7c | -9.93684 | -60.4845 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c64cdcca-63b6-31ba-977e-6c9527342e97 | -7.4377 | -60.03086 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c2528a7-fb6b-3221-94fb-87ee1d455aff | -7.43096 | -60.00818 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ec550a70-0fd8-39d9-a637-eb47a4c14daa | -7.56496 | -61.41822 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf74a140-0d0d-3297-ab32-0e795f5ec230 | -6.87621 | -59.83578 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fa02caa-2e54-3c07-93f2-b6ed724ece8d | -6.9124 | -59.55428 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b99892d-e609-317e-a782-527ab09ba1a7 | -6.93472 | -59.54314 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d8354c6-a1b1-3a5f-bfc2-1c86167d7f99 | -8.5532 | -63.93388 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e08e835a-4b77-31e2-a04c-c474db381791 | -7.56165 | -61.4177 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e45de429-0724-357c-9fa5-ecbac010dda8 | -8.92114 | -60.72621 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8efdcbb3-b70e-3e55-9299-03f76f5e35c9 | -7.50442 | -63.82331 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ec242a5-853b-3862-81ef-6b7ca987f123 | -8.98735 | -60.51748 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 60b03669-3338-3c17-b88d-8bc8bd812296 | -8.06014 | -70.58464 | 2025-08-16 05:23:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e646e30-6ccd-328f-8de3-4dc1ba565160 | -8.71323 | -62.46116 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb658b36-da51-3e7f-9101-5b1fd53a3cf8 | -8.89448 | -60.74361 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6d49f6fe-3830-364e-89fa-a5822a195db7 | -8.99902 | -60.53012 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f28d7a31-3967-3e9b-bb8c-63d4212c4752 | -3.37871 | -52.71626 | 2025-08-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b84fa9d8-b165-3e71-9503-468b7985acb1 | -8.98749 | -60.56071 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b575530-5e94-306d-8b78-3eb83adacd96 | -9.00167 | -60.49087 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README59.md)
