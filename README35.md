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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd18eafa-2a89-3159-bd86-0a7067d06ed5 | -15.18645 | -47.09143 | 2025-10-18 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb05ddb7-0151-3d71-b03b-3488a560e78c | -14.91876 | -46.72179 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3a75fe00-da1a-3761-9fc3-ca184b0a3157 | -15.5717 | -42.12803 | 2025-10-18 04:04:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0ab74ce1-dd5d-3df9-ada0-bfee36b8a647 | -14.91293 | -46.73194 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 495e2a1f-b486-33eb-a4d6-80ffb701f9a4 | -19.12799 | -43.26991 | 2025-10-18 04:04:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 45b43bec-1973-3886-9ca4-96dd4d2bf718 | -18.77159 | -44.46129 | 2025-10-18 04:04:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d734755-74fb-3bfe-adec-32348f43f177 | -15.58282 | -42.38251 | 2025-10-18 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5d9c9c6-19b6-3e36-ac4d-eb7b65ff171b | -14.2611 | -51.8676 | 2025-10-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38df1c2b-09d6-3e43-baf5-cf13aa8d93a2 | -15.78601 | -43.65253 | 2025-10-18 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43e8de6e-6300-3c16-855e-6d58ddc730a1 | -17.48982 | -43.46436 | 2025-10-18 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88411c61-e705-396f-b7af-a9f979f5f63b | -16.22007 | -41.67952 | 2025-10-18 04:04:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c9bdbd38-590c-35e1-8608-b7a9287e9ed3 | -15.53077 | -45.69878 | 2025-10-18 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b449b33-5ea1-3730-8e3b-c10320630025 | -14.90635 | -46.76506 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 170864f5-8c9b-318d-9b35-efd36c2b676a | -20.73145 | -41.97216 | 2025-10-18 04:04:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 158987c4-3286-3927-b630-5044dfbb93b4 | -18.37593 | -55.44773 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a74eb79d-e1e2-3953-ad14-23efa30a7476 | -15.09061 | -44.0051 | 2025-10-18 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0490fdc-da70-3930-8bb3-99c270714201 | -14.54576 | -49.27999 | 2025-10-18 04:04:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7973a5d6-2976-3858-8bd1-6337e83f6057 | -17.96532 | -46.74169 | 2025-10-18 04:04:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64f3c363-a600-3edf-9f97-a6c8fa7a519d | -15.04303 | -47.3012 | 2025-10-18 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bf6eb9f2-926f-3b09-8d92-11f780b86eb0 | -18.38806 | -55.47525 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| e35f2e7e-152a-326b-a19f-c6e0370cd42a | -18.37466 | -55.45319 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 83e8fa14-13cc-39d4-9c14-2a9049515b2d | -18.40172 | -41.83768 | 2025-10-18 04:04:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1332a8e7-3734-3684-bf7f-017c6c96cc9a | -17.79453 | -42.68654 | 2025-10-18 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 21411139-65e5-392f-ab72-bb10b9bef06c | -14.7404 | -47.4205 | 2025-10-18 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4e9e0b8-1cf2-32e7-84d8-9e468212baca | -14.85903 | -52.44166 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c47ba89-1518-36c6-9787-ed6a878704e3 | -15.45264 | -45.9352 | 2025-10-18 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c197bbbd-97bb-3bc9-8133-72909f0783e8 | -15.65444 | -41.92699 | 2025-10-18 04:04:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 00b850a3-305e-377b-aadb-6e9519018ee9 | -15.77368 | -41.33133 | 2025-10-18 04:04:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 108ab960-0dbe-3cdb-ab4c-7b5b1175fc04 | -14.50486 | -45.60784 | 2025-10-18 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6045fb81-9219-3d59-b70d-84604137ceaa | -18.74429 | -43.70951 | 2025-10-18 04:04:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d46caca8-1cbe-3a99-a90e-580f6109eb2e | -16.74578 | -49.19106 | 2025-10-18 04:04:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e14dc4eb-81af-3d1d-9679-6bb7229ec16d | -14.90604 | -52.39669 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80654c2c-dc69-3b32-8114-2a1a09df1083 | -17.09192 | -44.11015 | 2025-10-18 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72b70d06-1c94-30d4-94b9-d0b52e39ad4f | -19.11996 | -43.2349 | 2025-10-18 04:04:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8584fcfc-638d-31b1-89a9-c3b1a6063051 | -14.26221 | -51.86801 | 2025-10-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7b0c1fa7-2ffe-3ab3-adb4-6628d6f3a257 | -18.65546 | -42.81536 | 2025-10-18 04:04:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 186dea2a-84da-348d-a170-1ac8b96ce992 | -19.56608 | -45.3479 | 2025-10-18 04:04:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3547e008-1820-3752-88d7-14c727295d31 | -17.98468 | -47.88347 | 2025-10-18 04:04:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a6e692c-eb67-3844-85cd-5b7f51cd5c6d | -18.42193 | -43.70196 | 2025-10-18 04:04:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10888888-f97d-3f1b-b32d-1977164d9b3b | -14.54674 | -47.93341 | 2025-10-18 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60659c9c-a0f6-3567-af09-99d602db4f80 | -15.45556 | -45.94054 | 2025-10-18 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87eea40d-dc30-3c05-87fa-b670a7fe1f2d | -15.74859 | -41.91314 | 2025-10-18 04:04:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2d300474-e315-395d-be01-823dd63eb192 | -15.777 | -41.33186 | 2025-10-18 04:04:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2935f56a-bb45-36fd-ac8d-bca60f236be5 | -20.6116 | -44.27066 | 2025-10-18 04:04:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 73ea8cd5-11e8-3b78-bd9a-18161a314b99 | -18.77096 | -44.46511 | 2025-10-18 04:04:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4d16e31-a855-3be6-a0de-8ffd55b1aca2 | -14.56528 | -47.92854 | 2025-10-18 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39a299b7-e2d0-3385-b13d-f2e874fd71e0 | -18.37525 | -55.44309 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f6a81079-fbf0-31ae-8988-20060307f74c | -15.55487 | -42.34494 | 2025-10-18 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb6e8da7-a1c5-3e70-b277-1caa5ba91dbc | -16.13473 | -41.1264 | 2025-10-18 04:04:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5bd09b55-2bd5-3505-9902-61fa7ae377cb | -18.40394 | -41.82308 | 2025-10-18 04:04:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 676dad0b-7fcf-3adf-bb26-931ee3ff57d1 | -16.04204 | -43.50578 | 2025-10-18 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6aa00840-a062-3d5c-b198-a7a16049d4bf | -14.90282 | -52.40097 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0348b270-dcb0-3347-9bd8-72881ee189fd | -18.40948 | -41.83149 | 2025-10-18 04:04:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 59f3d75e-c97b-36f7-857d-d82bd705d261 | -16.43379 | -43.73346 | 2025-10-18 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12d848ca-6cf7-3e06-8e74-6f7fb6cc0f66 | -15.96197 | -41.87566 | 2025-10-18 04:04:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 774d1a76-d0e1-338b-8846-c46b659e73b7 | -15.79381 | -43.25499 | 2025-10-18 04:04:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5201284d-9ca2-312a-ab76-e184533f6381 | -14.92361 | -46.71729 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58dd3918-fef9-3808-aacc-a2ec3abe7536 | -15.84851 | -41.99178 | 2025-10-18 04:04:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c13af31f-389a-33ef-b45a-28508a6e5bdc | -15.47218 | -42.88308 | 2025-10-18 04:04:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c28fa6b5-16a1-337f-879a-59235b0ffe02 | -16.81208 | -41.22721 | 2025-10-18 04:04:00 | NOAA-21 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bffd415c-8e03-39b7-963c-3433f11e8207 | -15.79953 | -43.57059 | 2025-10-18 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7b3c1b76-c35c-338e-8413-023cf67d5a1a | -15.05138 | -46.60995 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a14280c3-c16b-39e9-b43d-523f1876c293 | -16.21705 | -43.52428 | 2025-10-18 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25ba3bed-bb10-3e8e-a8cc-30c2643c47ea | -14.41111 | -49.41201 | 2025-10-18 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e4d051a-4089-30b5-8acd-b1f524633aa7 | -15.80014 | -43.56687 | 2025-10-18 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5119b575-6c17-30f9-a2bd-e6d16bea0f09 | -20.27115 | -42.70322 | 2025-10-18 04:04:00 | NOAA-21 | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| dcffe8f7-f13a-3409-be67-14d2de228162 | -16.81541 | -41.22777 | 2025-10-18 04:04:00 | NOAA-21 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a8399ff7-2a9d-3f92-8e59-024c0c7da32d | -19.83384 | -41.45342 | 2025-10-18 04:04:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 46eb95be-ada7-3fe1-80bb-8b43d5873b72 | -15.04259 | -46.61592 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 543a1bd7-a549-3f3e-bd65-9aa880d266ae | -18.38986 | -55.47426 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| eaac4011-c501-3a0e-8049-a857a4b1f1ca | -17.84873 | -42.62187 | 2025-10-18 04:04:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8a0986db-4e25-3b17-ad1f-76c1f18179bd | -13.93159 | -48.67766 | 2025-10-18 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77a0205c-ea1b-3939-aa8d-5701ed614eac | -20.19683 | -43.26866 | 2025-10-18 04:04:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f08dda3b-d672-38ba-8daf-2236f169b0b1 | -19.83328 | -41.45725 | 2025-10-18 04:04:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f67a0474-e15e-3862-92b7-86fc1456cfe2 | -14.74159 | -44.41356 | 2025-10-18 04:04:00 | NOAA-21 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b15542db-a753-3a1f-86b7-10b3695dac5a | -14.47982 | -48.61089 | 2025-10-18 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b395bb37-4a21-3747-9947-5e561d2c68c9 | -15.53121 | -45.70078 | 2025-10-18 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d24255c7-3491-36de-90ec-b4ae4e1df9b0 | -17.0904 | -44.09825 | 2025-10-18 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc414a70-7882-3bee-8b5b-ac930fbdde62 | -20.05663 | -44.75079 | 2025-10-18 04:04:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 77b2dd6d-8fd2-31bf-89a5-afceaa162dca | -15.58303 | -44.51247 | 2025-10-18 04:04:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 015e61ab-2ebe-3523-841d-7326fbbdaead | -18.52066 | -43.99753 | 2025-10-18 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c4a75ea-a06f-3b97-a046-b898adf76ff7 | -14.93252 | -46.71053 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee1c22cc-a359-3b62-bea4-caa4bc524b00 | -14.91231 | -46.75873 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6bd3813-a32e-3f29-aa43-1d9e7aabeb11 | -15.53045 | -45.70525 | 2025-10-18 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e27df3e6-275f-35f2-bdd4-8ea47f53b3c2 | -15.03955 | -46.61047 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c51c275c-06b7-3b67-8ea2-f1fd02fa1a91 | -16.64889 | -52.52526 | 2025-10-18 04:04:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d31062a-1e74-3485-8517-b25c4bf44d09 | -16.28016 | -43.9192 | 2025-10-18 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c16858c5-e7c3-3daf-ac01-7ac962279bd5 | -14.93342 | -46.70557 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 75448340-86c8-3b2c-b732-3943948c3ec7 | -14.91794 | -46.72377 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c76cedf9-764b-3d34-a9fa-e8d45a9a6cee | -16.34419 | -41.75555 | 2025-10-18 04:04:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0595b467-6a1e-3174-8167-bc6aabb7eba9 | -14.91125 | -46.76051 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49de5a08-7bf5-324d-a68e-8ad1ed039eec | -14.90849 | -52.40213 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e58d2186-c8c5-3c0d-8bf9-8a0fc36483bf | -16.20187 | -43.68167 | 2025-10-18 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9902cc26-0fb7-356e-9c99-28960ec8585b | -17.76768 | -45.5862 | 2025-10-18 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64766470-894d-3393-a07e-4dedc0eabf24 | -14.90744 | -46.76328 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4dfce5b-92b0-317e-ae5a-41bde3d6b853 | -15.77976 | -41.33601 | 2025-10-18 04:04:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 21676e8e-0aa4-3751-9ef1-ef90a31a345c | -15.17971 | -43.09422 | 2025-10-18 04:04:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bd850bd2-94aa-3b82-84ae-f7e3eade6a53 | -17.49254 | -43.46868 | 2025-10-18 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3da30a82-b250-39e6-8a4f-2387ed1d6dcf | -20.79156 | -43.20701 | 2025-10-18 04:04:00 | NOAA-21 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cf455630-b172-3abb-9d7e-d4e854373dc5 | -16.80473 | -42.57389 | 2025-10-18 04:04:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README36.md)
