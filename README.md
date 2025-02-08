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
| 45ce84a6-3c22-3c42-a397-b86a5efbe899 | -13.6258 | -55.4602 | 2025-02-08 00:00:00 | GOES-16 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 7a32da7d-4aae-3a5d-9d3d-d3a08d30328b | -13.6261 | -55.4397 | 2025-02-08 00:00:00 | GOES-16 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| d5122640-6e10-3fe2-9c90-d7c0605fe073 | -13.6258 | -55.4602 | 2025-02-08 00:10:00 | GOES-16 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 13e5ee33-00c4-38a0-91c9-368f9530c2b2 | -13.6261 | -55.4397 | 2025-02-08 00:10:00 | GOES-16 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 44221af4-0622-33d6-b795-51b028b0afc1 | -12.85145 | -43.82387 | 2025-02-08 00:24:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| dc53e9bb-08b9-371b-9a3e-3b7194ad905b | -11.74524 | -48.74738 | 2025-02-08 00:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 292a3690-6d28-3a49-b619-54ba98088030 | -18.58386 | -39.94921 | 2025-02-08 00:24:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 72f734a7-2beb-3c0f-8e98-10685838ab05 | -11.51818 | -41.41378 | 2025-02-08 00:24:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 2addfadb-6f8b-32c2-bb54-47966dbe897b | -11.51945 | -41.42278 | 2025-02-08 00:24:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 5cf66653-c45a-34e9-9fd7-67e45078bedb | -18.58518 | -39.95853 | 2025-02-08 00:24:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4080dc42-90c2-3b38-a211-e648e2947036 | -20.64765 | -43.36928 | 2025-02-08 00:24:00 | TERRA_M-M | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 2244115b-4db9-3029-9ac5-5128ba4b5071 | -13.48218 | -44.02187 | 2025-02-08 00:24:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ecac0937-426d-33a6-8614-4337969cd602 | -11.74181 | -48.74135 | 2025-02-08 00:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 74879e9b-798f-39b6-bf63-dca57a1bd0cb | -12.41473 | -43.80568 | 2025-02-08 00:24:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e0011a3e-1bf2-36cd-a58a-32bb65cf8eda | -7.94725 | -49.76348 | 2025-02-08 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| a4704e67-5950-3a3e-9cd9-fbad1d334887 | -11.5826 | -47.62509 | 2025-02-08 00:26:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| c173e074-5a43-3bc1-ad2e-088bb27b01ae | -7.95522 | -49.75693 | 2025-02-08 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 7e3f02b9-e3aa-34d3-9143-9811998f4af4 | -10.86451 | -44.79052 | 2025-02-08 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 78334333-0721-31d5-98ba-53cb5eb99e5b | -11.57054 | -47.62654 | 2025-02-08 00:26:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 467dc651-fdb2-33d7-8ac7-d1df4cf65fae | -13.6258 | -55.4602 | 2025-02-08 00:30:00 | GOES-16 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b6664b3e-0154-3a6a-b835-049ecd9aea69 | -13.6261 | -55.4397 | 2025-02-08 00:30:00 | GOES-16 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 52db4db0-16d0-38c0-9532-2507c304e872 | -13.6258 | -55.4602 | 2025-02-08 01:00:00 | GOES-16 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 9a9503a3-2f6d-3ec9-85c4-ee8e5786e99f | -13.6261 | -55.4397 | 2025-02-08 01:00:00 | GOES-16 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 98f7ce88-02e4-31a9-8e27-df1e5606589e | -13.6258 | -55.4602 | 2025-02-08 01:10:00 | GOES-16 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| bd64da93-76c7-3d3e-80ec-17889fe7bf28 | -13.6258 | -55.4602 | 2025-02-08 03:10:00 | GOES-16 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 068856b9-6f93-35b7-a38f-252bacd4f654 | -7.37779 | -34.88758 | 2025-02-08 03:12:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7dc8a245-f747-3c43-a14e-48584e5de4b9 | -18.57958 | -39.95094 | 2025-02-08 03:14:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8ef1a659-5254-3c88-b93f-e23fd4aef201 | -18.58563 | -39.94872 | 2025-02-08 03:14:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 047e2021-3e6f-3b78-afdb-b62249e83278 | -18.57885 | -39.95442 | 2025-02-08 03:14:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 797f20b4-bf24-34bf-badb-de6ba5446adf | -18.44882 | -39.7407 | 2025-02-08 03:14:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c6cc2cce-857c-3dc3-9026-c60b304a3e0e | -18.44954 | -39.7373 | 2025-02-08 03:14:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 616662d7-ab6d-39ee-82d2-0c896fa1414e | -20.79174 | -41.13104 | 2025-02-08 03:17:00 | NPP-375D | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 538928ab-8d41-3975-b47c-16b34bf807c6 | -21.05621 | -43.86207 | 2025-02-08 03:17:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d75c87d6-3f70-3227-9d91-1883e662a4d3 | -21.06259 | -43.86365 | 2025-02-08 03:17:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e4a0a634-842e-37cc-a3ad-04211f6060f0 | -19.71643 | -40.35514 | 2025-02-08 03:17:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aaa3c2eb-4c34-3034-9eb2-eddeebf9e695 | -7.7838 | -35.94577 | 2025-02-08 03:34:00 | NOAA-20 | SANTA CECÍLIA | PARAÍBA | Brasil | 2513158 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1b6fcf84-9f68-339a-8637-795bef8b8a00 | -7.47682 | -34.84267 | 2025-02-08 03:34:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| da8b63d8-ab8a-3e27-8a60-cc6d94ac4948 | -7.49347 | -36.27101 | 2025-02-08 03:34:00 | NOAA-20 | CABACEIRAS | PARAÍBA | Brasil | 2503100 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7a89ef2f-83c6-3250-ada3-542ff550790e | -4.90139 | -37.41199 | 2025-02-08 03:34:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b2470ce4-fb6c-3aed-a158-49734ed4e24b | -7.78723 | -35.9463 | 2025-02-08 03:34:00 | NOAA-20 | SANTA CECÍLIA | PARAÍBA | Brasil | 2513158 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6dcc680b-715e-310c-9b3f-b8aa5a996dd5 | -5.16881 | -37.87012 | 2025-02-08 03:34:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f1fb4b26-49bd-3ba1-be70-bbc90455cfe3 | -5.16981 | -37.86778 | 2025-02-08 03:34:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5af5d947-8fef-3c6b-bb07-b6547351fd68 | -7.75594 | -34.90146 | 2025-02-08 03:34:00 | NOAA-20 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d1ae56fd-42e7-3fc9-9d6f-22ee762f5fc9 | -12.41289 | -43.80432 | 2025-02-08 03:36:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9952fb1e-2137-3c31-a314-9b102301cb52 | -12.85304 | -43.82613 | 2025-02-08 03:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fc14111-0d04-34ba-96e1-4b1b65436405 | -12.4123 | -43.8074 | 2025-02-08 03:36:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 723bf94e-d9e6-310f-b3ff-29634fe2616b | -12.85362 | -43.82309 | 2025-02-08 03:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a151d3b2-caa1-3e40-9e13-49cae3aab520 | -12.84796 | -43.82512 | 2025-02-08 03:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76b0a928-ae9a-365e-bc3a-c6944fb25237 | -13.47733 | -44.01868 | 2025-02-08 03:36:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 504d295a-f2d9-30d5-86bd-4f2b2f34edb0 | -14.50116 | -39.38809 | 2025-02-08 03:36:00 | NOAA-20 | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8debe626-29da-3f4d-8307-1c6b50eab413 | -13.48246 | -44.01947 | 2025-02-08 03:36:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6bf19d8-88de-31e3-900b-c5283a06ebae | -11.51762 | -41.42291 | 2025-02-08 03:36:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 09d76672-28ae-3d50-a92c-e63536a1c562 | -11.51845 | -41.41838 | 2025-02-08 03:36:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ae2035e3-9ee0-3316-80ee-2f12c6bf514a | -10.85705 | -44.78848 | 2025-02-08 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 339ba31d-2b35-352c-a009-9fb8f75b8d76 | -12.12863 | -38.16996 | 2025-02-08 03:36:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 58fc64f4-53cd-3943-b89c-c4b1e95dceb8 | -11.52289 | -41.41917 | 2025-02-08 03:36:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ea8ef8ec-4d85-3aa5-a716-4b3e55544ab4 | -11.5194 | -41.4201 | 2025-02-08 03:36:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 74ffc3c4-1a92-3268-a19b-74658afcbe52 | -10.86265 | -44.78958 | 2025-02-08 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8ff86d6-cb74-37dc-8acf-6314d641d156 | -10.86192 | -44.79343 | 2025-02-08 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 841896b7-2e09-388d-a210-928df475ebb5 | -19.82412 | -40.5523 | 2025-02-08 03:38:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| dcd1d656-0958-3dd3-a2c3-c12f0fe7ceb7 | -20.16483 | -46.67491 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 046919c9-f105-3cac-b15d-38323ccd8a4a | -18.67336 | -47.50666 | 2025-02-08 03:38:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2bc6e04-59b8-3c05-b034-4b93fa8ebed9 | -20.15949 | -46.6739 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c56c40c6-0386-32a2-a6e9-a7c53be3806d | -20.16478 | -46.68615 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a2f8930-e5a2-3eb4-91ab-71bc2ea6c14b | -18.4494 | -39.73794 | 2025-02-08 03:38:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c2a616b4-d63c-31af-95a7-89b71f5949e4 | -20.16088 | -46.67831 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de7d2db8-5b28-31cb-8a48-cf833a6eee9e | -20.16257 | -46.68525 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaa034fd-b72f-3a86-9238-f804601ae35c | -18.13616 | -40.83166 | 2025-02-08 03:38:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4762914a-07c0-363d-808e-ebdca41f3e9d | -20.16239 | -46.67115 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7c12d246-6d88-30d9-9fa7-c0aa0cb0b52d | -18.58038 | -39.95257 | 2025-02-08 03:38:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 80878951-a0e1-3b84-9d73-6e37fb59d599 | -20.1633 | -46.68192 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d8fadab5-f9b5-3b02-b006-2eae4f11a70f | -18.13234 | -40.83088 | 2025-02-08 03:38:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e2a9c743-4f54-38e4-ae2c-af52aa7121e0 | -20.16016 | -46.6817 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40d326e0-4517-31d5-b413-05d00f5ee1ba | -20.34667 | -40.35974 | 2025-02-08 03:38:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ad8a471d-11e6-3817-9963-3b63e1fdc7c1 | -19.16965 | -40.669 | 2025-02-08 03:38:00 | NOAA-20 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 86540f13-2f70-377a-afc9-a24c75cfcbfb | -20.1655 | -46.68274 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b68fdafe-0676-30a0-b703-e8c7dec77414 | -18.58115 | -39.94814 | 2025-02-08 03:38:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b60ac4a7-a80e-3a77-acfa-cd946a03c8d1 | -18.67912 | -47.50787 | 2025-02-08 03:38:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3ecc8bc-d99f-369a-9ca2-262508c109ac | -21.07274 | -43.20945 | 2025-02-08 03:38:00 | NOAA-20 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d245c790-a625-391d-8008-8533fba35319 | -20.16941 | -46.67941 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3ee89b5f-cc53-3645-810b-006f1af8895c | -20.16164 | -46.67472 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f123dd59-eecd-376f-9cc2-550bcb7f2e53 | -22.58419 | -48.01824 | 2025-02-08 03:38:00 | NOAA-20 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9f3ed36c-d43c-31b2-b63d-b13a319690f6 | -21.06002 | -43.86261 | 2025-02-08 03:38:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 26ba7909-9851-3c7a-8292-69eeffd23522 | -18.44817 | -39.73953 | 2025-02-08 03:38:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0c2c15eb-4b23-3bc4-ae78-99e1bf1cb24b | -20.16405 | -46.67847 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 83dec074-6bfb-376a-a3aa-58f7e4f9170d | -18.58478 | -39.94885 | 2025-02-08 03:38:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8d055dd9-d0d6-3423-8f0d-e46a9d316461 | -19.8278 | -40.553 | 2025-02-08 03:38:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5d6c25b4-1deb-3304-9674-f85fcaafe476 | -21.99867 | -46.80584 | 2025-02-08 03:38:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1af7a3b8-5f82-3279-9600-98d68497c439 | -21.05958 | -43.8644 | 2025-02-08 03:38:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 006a3de0-909b-3d71-bbce-f4ed549c5002 | -20.16623 | -46.67929 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de9729b4-52ca-3de2-bffd-7891f30610e3 | -22.90184 | -43.75496 | 2025-02-08 03:38:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2e987d75-2b77-3add-bb5b-c2bead37cb13 | -20.76144 | -46.7722 | 2025-02-08 03:38:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0a936349-44d0-3108-88bf-933b1fa0f91c | -20.16561 | -46.67135 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e03c386-d0e5-38d5-9343-2e7ccf78b723 | -17.49998 | -45.17856 | 2025-02-08 03:38:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 082c1db7-e0c4-3838-ad4e-16e43db5ee57 | -20.79243 | -41.1287 | 2025-02-08 03:38:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6dabe06c-d8e6-3ec2-9477-8f1e7750d086 | -20.16698 | -46.67573 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1ec41ccc-3875-3b26-a670-86669540ebba | -22.57882 | -48.01641 | 2025-02-08 03:38:00 | NOAA-20 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10085590-87df-345c-ab4b-90a5a0a53130 | -20.16027 | -46.67036 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2024fa21-5286-3b21-828e-16a9a83a1723 | -20.21071 | -43.94528 | 2025-02-08 03:38:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f4fd3829-465b-3edc-9ff5-8d43337d4951 | -20.15872 | -46.67744 | 2025-02-08 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README2.md)
