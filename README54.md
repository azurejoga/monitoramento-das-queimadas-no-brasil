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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea9cfba7-b39c-3abf-b45c-d4b88d0d63ce | -11.11126 | -43.33599 | 2024-10-14 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 5100eccd-b311-374e-ab81-25d082637dd6 | -11.10837 | -43.33154 | 2024-10-14 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 39fea4c7-5b7f-3547-900e-5427956377e7 | -11.10778 | -43.33546 | 2024-10-14 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 3d63fb61-4d89-35b1-8fde-e748650ef884 | -11.1072 | -43.33938 | 2024-10-14 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 15.7 |
| feefa66f-d02c-38a6-9ee5-048b84a2fc9a | -11.1043 | -43.33493 | 2024-10-14 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1ce8ec78-a693-3e37-a3df-c2ec89f04d28 | -11.10372 | -43.33884 | 2024-10-14 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6b74dbce-d749-3e8c-bdae-83733026947b | -12.28733 | -43.83326 | 2024-10-14 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d9e9dc46-c3ba-33c1-804e-c1df3c63ce9f | -12.28388 | -43.83279 | 2024-10-14 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ff71036-122b-3ce8-8a74-d8cd7e39d580 | -11.90788 | -44.17016 | 2024-10-14 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 942647d4-a420-3a20-b476-152efc43c285 | -11.89736 | -43.88863 | 2024-10-14 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4a00fc18-fb85-3cea-81db-e2076c3fd8ee | -11.89393 | -43.8881 | 2024-10-14 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 192183c6-386d-397f-924a-4a977a21e4bd | -11.88651 | -43.89083 | 2024-10-14 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b62dd5da-54ac-3c1c-9ced-c1763e9ced0b | -11.88594 | -43.89462 | 2024-10-14 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03f8123a-1cc0-3f52-9c67-f71786320542 | -11.72695 | -44.55957 | 2024-10-14 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66b94b56-ded7-3bb7-ab37-3cdc1248c4fd | -11.71907 | -44.54348 | 2024-10-14 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c61d79b-3d7d-30ec-bd04-edfa84251ecf | -11.69332 | -44.24416 | 2024-10-14 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bbcc899-fbba-3eeb-be1e-0e6efb9f68ee | -11.46887 | -43.9402 | 2024-10-14 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfc4ab00-4c6f-3a27-a8c6-a24c327590c2 | -11.46773 | -43.92467 | 2024-10-14 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7516c18-1b01-3ad8-bf6a-039331df90f7 | -11.46602 | -43.93593 | 2024-10-14 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5be6f7cf-fd72-3a29-b378-10e138502f11 | -11.46147 | -43.91986 | 2024-10-14 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b56462c4-3f2a-342c-9fec-d1522cc4c2cc | -11.45636 | -43.93059 | 2024-10-14 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2b7110a-6531-32b1-8ad5-160b1c77a1bb | -11.25553 | -44.19566 | 2024-10-14 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8728e01a-4f85-376a-905b-f47193fc8c4d | -11.25215 | -44.19514 | 2024-10-14 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb0d909e-fee3-37d2-96d3-ef4a81723650 | -11.2516 | -44.19881 | 2024-10-14 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80afc0c5-7bf1-3af8-9964-9c6051049749 | -11.23974 | -44.18568 | 2024-10-14 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 550d754f-5b4e-36fe-ac61-067e6defb74d | -11.11535 | -44.47227 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39ada778-baa8-3dae-90d7-3986a3ce68ad | -11.1148 | -44.47588 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4af4d55-5408-3f46-84e5-d70c7ac12e64 | -11.112 | -44.47174 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 799f5045-4f42-3944-a3f8-fb97bbbb937d | -11.10975 | -44.464 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 30087a0e-ecdc-3303-8427-a448a78737a3 | -11.10926 | -44.48975 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b23b5158-7e1c-3533-953c-e47a96f6a05f | -11.10591 | -44.48923 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8befe4f5-5cb3-3980-a9c0-dbf90733cdc0 | -11.10536 | -44.49283 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b94785fc-a3c3-33dd-8d36-83b4f535423b | -11.10475 | -44.47429 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a458a74c-67ff-34aa-b6ef-e94c2f61e450 | -11.1042 | -44.47789 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1c42ac9-40b6-3dc9-9399-84fcca08c476 | -11.1025 | -44.46655 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8a083a5-c177-3b98-9091-1984623ef818 | -11.1014 | -44.47376 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd4e62a9-3c7d-3812-b6b2-6d22e538f9d6 | -11.09915 | -44.46602 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0b9fe8f-4c1f-3b3b-952d-fe5750dccd47 | -11.0986 | -44.46962 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e3fa318-f941-3848-a627-85c1c2e66174 | -11.09812 | -44.49538 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5385af75-cda2-3f1d-a51b-279247561597 | -11.09531 | -44.49125 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e03040cf-920f-399a-941f-e9f747a9e30c | -11.09477 | -44.49486 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29ebd400-9a76-3f0b-990d-de348bbb9ca5 | -11.09251 | -44.48711 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0153d3c6-7a94-3cca-b70b-c9bfb7c6a993 | -11.03842 | -44.35315 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd095beb-49a7-39a2-a17f-8ab9d8c57eb6 | -11.03561 | -44.34901 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 685c370f-c968-3607-8cbd-23780dcf26b7 | -10.96913 | -44.53811 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 233cb94e-9c24-35d1-8a5a-28c279a41e9d | -10.96579 | -44.53759 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9095f01e-114a-3dd1-8826-f3d625a54412 | -13.7761 | -43.71672 | 2024-10-14 04:21:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ec079de-4457-3085-ba50-92e92c84ad96 | -13.72279 | -43.90903 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf54f61d-076b-3f2d-9d56-f500541ae682 | -13.72221 | -43.91298 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31fe06f3-8950-37d5-b92e-e50499cc5a43 | -13.71062 | -44.0397 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 205642f3-c989-31f3-aad6-070a23977169 | -13.71004 | -44.04362 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18e67058-609c-3d8e-aadb-6afdb681b0d1 | -13.70793 | -44.38903 | 2024-10-14 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 72459f04-0b9a-3d70-a02c-fd9902362e4b | -13.65847 | -44.22539 | 2024-10-14 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44f568d1-e518-35c6-80ab-c608a1265bde | -12.71398 | -43.83685 | 2024-10-14 04:21:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e07eb3d-f12d-3a37-a2d2-de69974e8df4 | -12.50248 | -44.33789 | 2024-10-14 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffd787da-7553-3b9f-b39e-e2b8d1bf3119 | -12.42967 | -43.77164 | 2024-10-14 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57e0a925-f8d3-3208-890a-329b8acbf1fb | -12.40282 | -44.06988 | 2024-10-14 04:21:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd82283a-b8b9-3933-9674-f8f23bba0ad6 | -12.3994 | -44.06931 | 2024-10-14 04:21:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 940d4a6a-2f9f-3586-bdb8-d3d1227e94ed | -14.07345 | -44.77583 | 2024-10-14 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99d0fce5-935f-32c8-99ac-fae80116418f | -14.24471 | -44.45356 | 2024-10-14 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec053a37-c109-3dea-aef1-1602d862fc8d | -14.20015 | -44.37674 | 2024-10-14 04:21:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dd44894-95f0-3fae-96fc-5cec438214c7 | -10.90355 | -44.70312 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4e225eb-aa63-3b31-8cbc-20fbba57466d | -10.93455 | -44.63491 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb2eaa3e-1db0-3b21-969f-9c4c9efeb70a | -10.93121 | -44.6344 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3f0868b-a6f4-3ead-a9b7-9afcdf668bf8 | -10.93069 | -44.6599 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dff712b1-108c-3f54-bb07-13d51589206c | -10.93066 | -44.63796 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f25f35a-1284-37dc-90dd-5777b7c16ecf | -10.93014 | -44.66346 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f068355-b694-3712-81a8-31994e6624c0 | -10.92733 | -44.63744 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18648e9e-e09b-3ecd-8dcd-880c177f930e | -10.92677 | -44.64101 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8be9644-3f68-3e92-bcdf-946f3094a58d | -10.92626 | -44.66651 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7a8f26f-35da-3729-952b-a8ea2954a2ab | -10.92574 | -44.69198 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 276feb18-d650-3767-b5cf-d0e9061c5ade | -10.92519 | -44.69555 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edb3aa3b-0c92-3419-9aee-72ffd4b435dc | -10.92241 | -44.69147 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df99bf12-73c7-3195-b3b3-824135b1b5f1 | -10.92186 | -44.69503 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55212277-ec7b-302e-bce6-1ec3312871c0 | -10.91962 | -44.68738 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ed85668-682e-3ee0-bff3-0ea43c2190e9 | -10.91907 | -44.69095 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed3fe5ee-7d49-3629-b122-b80e95258125 | -10.91852 | -44.69451 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abdbc740-30df-3f2d-b9d4-5e9b569268f0 | -10.91797 | -44.69807 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54055879-bc9c-3bd8-b76c-a6030da6b41a | -10.91629 | -44.68687 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1b10461-616f-3baf-905b-132780b0b3e8 | -10.91574 | -44.69043 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1bda25f-1fd2-33fa-9f9f-470222453f4c | -10.91519 | -44.69399 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3260b1a0-8f28-327f-ae6a-5a7b202e0198 | -10.91464 | -44.69756 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f8685a1-158e-33bd-b20a-790c35368688 | -10.91409 | -44.70111 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8215931d-05ac-32ee-b0c2-66544c3d7d56 | -10.91354 | -44.70468 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f111e090-ec31-3aff-a6d0-32f4068838ea | -10.91299 | -44.70824 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 69db0c4f-2a29-320e-83c4-98d4bbccebf5 | -10.91245 | -44.7118 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f789a50b-d77d-3b9c-bf5b-1feb6be78427 | -10.91241 | -44.68991 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0981875b-2be4-3e82-a19d-f0a29d6b1bd2 | -10.91186 | -44.69347 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b86fcac5-4a89-3419-a9a1-dc8e92802724 | -10.91131 | -44.69703 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 708a3a3a-d678-3d0e-9864-bfba0d179e43 | -10.91076 | -44.7006 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6d05de05-6bd2-3384-b135-0e8ccfeb8b39 | -10.91021 | -44.70416 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ff5af335-dab2-3d6b-8022-fbc2163ce468 | -10.90633 | -44.7072 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20e4390f-19f4-36e1-bca1-9b6f3b4ce9a2 | -10.903 | -44.70668 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 364f676a-2a4e-3b8f-9a35-39287b7f0cc2 | -10.90245 | -44.71024 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ecddcdc-75c4-34c4-a197-3855ea7445e3 | -10.87266 | -44.79303 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f38daa24-91cc-3d47-aeb3-136c4f163473 | -10.87211 | -44.79658 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4df1122c-35d1-3285-a713-64849c808e8e | -10.87156 | -44.80013 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e69a343-4428-35cf-bd8d-2472e711c7cc | -10.86933 | -44.79251 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6a55101-215b-366c-907e-1f7994571d18 | -10.86879 | -44.79605 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee184b63-9a37-33a2-8c12-44cb5b440cc0 | -10.86824 | -44.7996 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README55.md)
