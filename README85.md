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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a1aab5c-3af6-337f-9ad2-7f93c0e671ae | -9.32342 | -56.26659 | 2025-10-18 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13a0171f-83f4-3de1-9ed3-c43598691a5a | -10.23859 | -44.03917 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 69a12180-76d7-381e-b47c-84d1cac6ca89 | -11.4824 | -44.02277 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee650f3c-ae10-339b-9ed9-f04d98ca4260 | -10.81411 | -43.93166 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d62effbd-ce30-3fa8-aad4-661cabcfd77b | -10.62494 | -42.30103 | 2025-10-18 04:51:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| b78b58cc-5a23-3896-a929-889968b003cd | -16.64951 | -52.52337 | 2025-10-18 04:51:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2063256c-a212-3b1f-8040-b3b3908524dc | -10.91385 | -47.67639 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41634e8d-0c6b-3625-bd03-088cf510b385 | -10.70052 | -44.55149 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d6ff71f-3cfb-39c3-8a44-c278098c567e | -10.81553 | -43.93139 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cf6aa5d-2f41-32d7-89d0-283a06630b93 | -10.92613 | -47.55669 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93428abe-26ee-3467-a3e5-6f82375bbb37 | -10.97983 | -44.32657 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22ce9f26-5db6-369a-99a2-13cdfbb4d9c5 | -11.35184 | -45.25719 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e200cc9f-0634-3bc9-92c6-791d1a2c2018 | -11.75635 | -61.07805 | 2025-10-18 04:51:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2164fac6-2364-375e-af29-db7f2d613040 | -14.06269 | -50.04784 | 2025-10-18 04:51:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4b070ee-d4ff-3c06-addc-2d8847c9d416 | -12.16873 | -45.09341 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc3a8b47-61c7-3ba2-8bca-d4aa6c559a6c | -10.11946 | -44.54278 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b5d9ab4-f5b3-32db-a138-6258d3d0c72b | -13.04438 | -48.19381 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87031e9d-3e98-3b5b-b78c-e5d709c8415e | -10.25595 | -44.03154 | 2025-10-18 04:51:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f18b687-6477-3a19-96f2-b3ed3a147907 | -17.84612 | -42.62076 | 2025-10-18 04:51:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 47effa6b-b2cf-3dd1-aefe-297bcf20413e | -10.48636 | -43.42292 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c06a39fc-1636-3b15-a6c0-87ea5af9b327 | -12.16674 | -45.08736 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fae51c86-81bf-3b4d-9fc2-911a1907e0d3 | -15.05174 | -48.73918 | 2025-10-18 04:51:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 118b810b-6966-3b0b-884e-9398e2df0987 | -13.27283 | -46.44252 | 2025-10-18 04:51:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 988c2998-160d-3d40-9da5-79c7f06adfee | -18.38821 | -55.47905 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8f64bf46-3b0f-397e-9422-9424083771d2 | -19.10619 | -57.55698 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ac62264b-027d-3fdd-991f-a328fdda1f18 | -18.38548 | -55.47485 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| dbd64799-4223-38e3-8e6b-3e96247e1914 | -19.05714 | -57.4908 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1755bc6c-756a-381e-b8d2-1420d38e87a4 | -17.38917 | -53.5547 | 2025-10-18 04:53:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f416e76-db14-3daa-8a87-a38d8b4a5bbb | -18.378 | -55.43626 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2b942ff6-277f-3cf0-970f-08aa64e99f61 | -19.10275 | -57.55633 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4d0d8069-e298-3f51-acc7-d074937f1517 | -19.09998 | -57.55173 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 34d4f658-a20e-3d5f-8449-92cd2f52938a | -18.37742 | -55.43988 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1b7ae109-ea99-3878-a130-31f173da7105 | -18.379 | -55.45134 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8ad57c05-c715-3881-8e18-fc525023a5fb | -19.10962 | -57.55763 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6aecf5bd-27f2-35c4-a113-153b9c104adf | -19.09034 | -57.54585 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 45cc1ac6-7c65-30a3-81fb-af4c4ec1b710 | -18.39094 | -55.48326 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 683ead8a-96bd-3cc1-aa71-c2cfe82b98f3 | -17.95452 | -57.63135 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 45d54afb-0b04-3e1b-a552-8ccefa61b0a6 | -19.09721 | -57.54715 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b40d4c5d-57b0-360a-901a-f0d633145f19 | -19.10685 | -57.55303 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 07e69586-1c4c-3283-902c-14287eeb8e17 | -17.96149 | -57.63266 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 334205ca-3a02-3ee7-80ef-917a9d03ad1f | -15.91228 | -60.14078 | 2025-10-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d85bbce0-3a04-34bd-82e0-194421086230 | -19.10342 | -57.55238 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e4dbfefc-0cc4-3633-9c3a-ea1db9b32f6b | -19.48604 | -44.86957 | 2025-10-18 04:53:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ae4ac51-d6e3-3434-a4ff-5b2e39c87ff4 | -18.3849 | -55.47847 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 835288b5-5a18-3b6d-a3b5-f7b982b26a68 | -17.02585 | -55.91787 | 2025-10-18 04:53:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6e0df1a7-1be6-3fe7-bc68-4539732cf21b | -17.02251 | -55.91728 | 2025-10-18 04:53:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 784dcc5a-0bd6-380c-a970-e046e18fe8f4 | -17.02311 | -55.91361 | 2025-10-18 04:53:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5b36102f-fc2d-346f-939d-4a284acd9e22 | -18.38216 | -55.47426 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| ff22efe9-0439-345e-b620-6cdc30dbf670 | -18.37481 | -55.4357 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 107f2e4c-0c30-3cf6-96c6-1c83326343c2 | -19.10064 | -57.5478 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fcee7434-38b2-39bf-8379-fd611050e759 | -18.39152 | -55.47963 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cfccbc8b-1f41-3bae-a064-61dae449aab5 | -18.37685 | -55.44351 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ef7c9fe8-4066-33fa-9acb-dc9383cec573 | -16.90464 | -53.0261 | 2025-10-18 04:53:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ce3a803-1509-3982-a0f3-15e3a224846f | -18.38274 | -55.47064 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8ba0bb29-38cc-3580-a333-587531716d39 | -17.44404 | -55.02856 | 2025-10-18 04:53:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b495e7f-0c9d-3df3-8545-b58013ab86eb | -17.958 | -57.632 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 996511b6-74af-381e-bc29-e5925f919f1c | -17.81598 | -57.6157 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bbc957b4-da4b-3d2d-94e2-bdb2ec0dd1f1 | -17.44073 | -55.02799 | 2025-10-18 04:53:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7defd3ef-496e-35db-a43f-f6825a1f0846 | -17.95383 | -57.63538 | 2025-10-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 052a4ce5-4a41-3557-8238-69694cb54dba | -16.66824 | -53.39076 | 2025-10-18 04:53:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9e87432a-24c5-3444-bca7-6eac117ed8b7 | -19.09377 | -57.5465 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fb86e477-2ce4-3d27-b5a5-7bca51b4c37c | -19.10408 | -57.54844 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 063cbb54-6939-3fe0-819d-fc75530a0729 | -17.44461 | -55.02495 | 2025-10-18 04:53:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c06fe4c3-40c9-3424-9978-52d941f78241 | -19.10752 | -57.54909 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a84c68c1-9618-3add-882b-a4cf0e2e0274 | -19.11029 | -57.55368 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 60838f53-ec12-34c9-ba14-ccf3de73d510 | -19.09654 | -57.55109 | 2025-10-18 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c1513a01-cb0b-358c-b104-c923912d81bd | 1.7664 | -55.9805 | 2025-10-18 05:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| e772070a-53e1-3e96-ae47-3e2a61d038bd | 1.7481 | -55.9807 | 2025-10-18 05:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 2376932a-94f0-3241-b0df-ec9827fd8417 | -3.1431 | -50.2464 | 2025-10-18 05:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| f2b4054a-42e3-3e9c-aa30-600029dc1e57 | -4.4632 | -43.2386 | 2025-10-18 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| f0a34497-382a-369d-b994-19e8589b31f5 | 1.7481 | -55.9807 | 2025-10-18 05:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 248166c4-bb88-3c6d-af5e-26b7e6c6cfe6 | 1.7481 | -55.9807 | 2025-10-18 05:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 694a9e58-3718-3964-bc03-c0d4f5aa9b68 | 1.7481 | -55.9807 | 2025-10-18 05:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 03b4a11c-a202-3341-ba2d-0cb21d503b8c | 4.17666 | -60.22103 | 2025-10-18 05:38:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3f942fd-3a76-363a-8392-e5e75bf3b3ef | 3.95916 | -59.81156 | 2025-10-18 05:38:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99fc3c4f-263c-384e-bde9-1f4574576010 | 1.75138 | -55.9797 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cc7317f4-2eea-3e57-8f69-5942cf3b48f9 | -2.8751 | -50.73128 | 2025-10-18 05:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d2efc40-18cd-329f-96f1-cf8aa3767acc | 1.73534 | -55.75902 | 2025-10-18 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3517b632-ea40-37ca-8c96-1550bed6ea91 | 1.75839 | -55.96286 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d141673-67bb-31ae-9d26-53a666ecb4d1 | -3.41479 | -59.29454 | 2025-10-18 05:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17923b57-0065-31d8-919d-0878f55d1929 | 1.7625 | -55.98831 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1526a5a9-adee-3e10-ac6d-88fb26b0acc0 | 1.75612 | -55.97893 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a28052e3-195a-38a4-ac2f-35fce8318495 | 1.77017 | -55.94532 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e2d43ae-3620-3189-af5a-fcb00e78147c | 2.05011 | -55.73051 | 2025-10-18 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c873b02-e9d0-3cf3-8a8a-864dd7978aaa | -3.98328 | -59.167 | 2025-10-18 05:40:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f578f79-3ed0-33d5-9abd-1d651099f66e | 1.76641 | -55.98245 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 46094f1e-ebf5-3acf-aab8-1423156ae899 | 1.7677 | -55.9299 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e3d62198-c4e6-32f8-b82a-e1389f307cb4 | -2.69395 | -59.42846 | 2025-10-18 05:40:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a62bc350-1d3c-3cce-b657-6aafe755aad2 | 1.7669 | -55.92494 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 72adef78-1cff-3a98-9faa-12747f65fde8 | -2.78203 | -58.14696 | 2025-10-18 05:40:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18abf927-c058-3a75-8a7a-459f0423095a | -2.87306 | -50.74532 | 2025-10-18 05:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77730044-a142-30db-9cd8-bf722c0ae023 | -2.11936 | -56.88937 | 2025-10-18 05:40:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a2249f6-e603-3144-bb87-963c33ab0ef6 | -3.8025 | -51.64364 | 2025-10-18 05:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7220bdcf-4a86-3b79-8bf4-58135bd76e57 | 1.75922 | -55.96803 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ab10514-eac4-3132-a446-8ce638225700 | -1.38141 | -55.3529 | 2025-10-18 05:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8c19574-9f67-3f62-b986-d31ab92ca5cf | -2.36989 | -57.21227 | 2025-10-18 05:40:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4ee3a0f-e6c6-3225-b1cd-c82b59915a8f | 1.76952 | -55.97153 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9352604c-db08-32d4-8e22-222618b6d744 | 1.76295 | -55.93069 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 90e1f4ed-c5bc-3cc1-97e3-8587934a055a | -3.79935 | -51.76354 | 2025-10-18 05:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22c37b03-22ef-39dd-aeed-059a7bec8b49 | 1.88917 | -55.86118 | 2025-10-18 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README86.md)
