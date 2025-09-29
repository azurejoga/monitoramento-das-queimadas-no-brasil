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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a9a46e5-7fe8-38f7-bb33-5e22548b3d1b | -15.325 | -47.916 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0bab5b3-8a7e-3418-9f41-4511c8c6e33d | -13.1848 | -47.44749 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1437688-24a3-3797-babc-b97e839ec030 | -15.04156 | -46.97214 | 2025-09-29 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 378b874a-38cd-34f5-bb3a-29d5cc0edee9 | -13.63648 | -48.05221 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6dd56c7-2da7-3cb9-be5a-2890061c9f61 | -11.92099 | -48.04316 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| be4fe60c-24d2-30df-8a17-25349d7c0083 | -13.42323 | -48.19987 | 2025-09-29 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92e401be-40e7-3cbb-b34f-309fad71fbb3 | -13.80597 | -47.9083 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c44d8ba8-e230-3ffe-a0c0-857bae4d27d7 | -13.59236 | -47.29052 | 2025-09-29 04:59:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03e28088-ef7a-37f7-9a06-84cadbc1de6a | -15.17136 | -50.08699 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a3606f4-38ca-39fb-a8dc-139a88228903 | -14.8439 | -48.37976 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57ac7dd3-ba19-37df-b9b7-0d135b5dcb45 | -15.28336 | -49.49128 | 2025-09-29 04:59:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 37ffdf62-820f-3427-add7-c8346da5b8e8 | -10.80071 | -51.97729 | 2025-09-29 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0de9a36f-a30a-3a22-a491-1512f02d4777 | -12.03261 | -47.93303 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52d0b2ee-3f52-32af-80a7-e3fcf2e503d8 | -12.89964 | -47.11275 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0616521a-7495-3741-a3c6-aeadc002b97e | -13.61132 | -48.06376 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aa0b2b96-8ac3-3d2b-956b-63cf1243a43e | -13.80741 | -47.9366 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed496e60-a9a3-3888-b91f-df5e13fb291d | -13.58173 | -48.09835 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a818fdc4-082d-3e56-a83a-56acb93cefc5 | -14.44212 | -46.36378 | 2025-09-29 04:59:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 448bcd6c-ace1-34f6-9a1a-477848cedbf4 | -17.07808 | -48.5701 | 2025-09-29 04:59:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0ed5483-1a86-3927-b279-5d4791588c44 | -12.75963 | -46.85162 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0defa6ab-42e5-30a6-8f1e-2298a5d84380 | -12.66108 | -51.66808 | 2025-09-29 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b59ca501-19e3-3819-9ac2-0e0148b3cc38 | -12.85742 | -46.96735 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 761f6736-a01d-3f81-b975-dcd32b7cf58b | -12.76305 | -46.86662 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd18ccb7-ef9b-32d8-99dc-b73ead078bfa | -13.62736 | -48.04627 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b36c2bc4-9d84-3f8f-911e-51493f7bd793 | -11.72745 | -44.422 | 2025-09-29 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 762d5f4d-7faa-30e7-8872-419bad8b2730 | -15.4242 | -48.24314 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b3ee08cd-81d5-3508-a2e7-8c0755d26027 | -11.4458 | -47.28371 | 2025-09-29 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42102565-bc18-3c4e-96bf-05448d90c4e6 | -17.39614 | -47.11751 | 2025-09-29 04:59:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6a39c24-afda-3081-895c-2277830f2781 | -15.32599 | -47.90724 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92d6ebfe-db81-3ac9-a543-3c3272881d08 | -13.59677 | -48.0621 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f75d1964-28b1-3c53-a058-fe021ba5bb4d | -11.93793 | -46.53764 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10556c4e-09e9-3829-af98-590b8509bd3b | -12.70073 | -46.90275 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0c0f3435-6a2e-3f8c-99ca-4cf8f7ae83d7 | -12.90149 | -47.0975 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 944e152d-1d2f-3bbf-ae7d-ce8f5ffe1b8f | -13.38956 | -48.15717 | 2025-09-29 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 70ae3680-3323-333c-8aa0-602a663d1a17 | -15.2843 | -49.2541 | 2025-09-29 04:59:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe0128d7-1c9c-321e-930a-2e6a7a0ca998 | -15.61835 | -46.25864 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1faec32e-d119-3132-8dcd-9281d9c90e1d | -13.7477 | -47.89583 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0592649d-c22c-3637-af2a-c39a8b3fcaa1 | -15.08742 | -48.33469 | 2025-09-29 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| beb2fde8-08ac-316e-9b24-ce7f3d044f91 | -14.58367 | -48.27356 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3bf8a35d-c76b-36ed-a196-3b881e686791 | -15.21644 | -48.04951 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 727094fa-0343-3452-8f6e-665f1ba2360d | -13.00863 | -49.44444 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 235a0443-6063-3e28-b0ae-b0841094932b | -12.97395 | -46.24486 | 2025-09-29 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3386a07d-29be-32c7-909e-5c7faa03c803 | -14.51988 | -48.3978 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb3ad531-ed18-3573-812f-7d347609e3f0 | -11.69809 | -44.44068 | 2025-09-29 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5177f51b-fc0d-3ce5-81ba-907072b77966 | -11.86178 | -48.24582 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31f1de45-4b40-3892-a546-58df2c409ad1 | -11.80459 | -51.79941 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2f87856-2982-3d8a-b604-8036ea3699dc | -14.57114 | -48.25519 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 549ed15d-5675-34e7-93ea-0caaf7e28953 | -12.84169 | -46.88201 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28a5da4a-d543-3f4a-a051-51f3054f55af | -14.57273 | -48.28274 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e00b239-0e61-3d12-b2c5-abfaa5fd86ce | -11.98572 | -46.58397 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf34d742-ed5e-38ce-b7ea-18a2683b8cb4 | -13.75253 | -47.8971 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 411af0db-5f2f-32fb-b3f3-0f718f3ff939 | -14.52064 | -48.39164 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 009fa766-d6c1-3a8f-abc5-78f159d3ae04 | -14.59515 | -45.00495 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ee5aff26-4be0-390a-b038-5fd65a0aef24 | -15.26503 | -48.76453 | 2025-09-29 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 69758c18-1471-3cd5-81ec-e593a38b1300 | -14.4716 | -42.1719 | 2025-09-29 04:59:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5c4cfae6-6b5c-376c-8c79-f37f1d12198b | -12.96528 | -46.24354 | 2025-09-29 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 152aa676-e7cd-3a75-8ed9-f86b663832e5 | -11.43487 | -46.63139 | 2025-09-29 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 760f8754-4df0-3571-a2c5-b7d15e87f7e8 | -15.70969 | -47.80153 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45e871ef-6442-3551-a1a3-7ff67b338aea | -13.23271 | -50.9599 | 2025-09-29 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ddba0e0-141a-3780-8a6e-63d50c8011a9 | -13.01299 | -49.44508 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0da97f35-fe6f-3a47-a448-75404ed0620e | -12.97947 | -46.26354 | 2025-09-29 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5a83632-96b6-3cd0-b641-870c5c14ea4e | -12.45335 | -54.30018 | 2025-09-29 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f703ae2a-65c8-37aa-ae13-699deff1f6c1 | -12.70178 | -46.8941 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f1cdb67-6c84-3016-a271-f70607e7335a | -10.99352 | -57.06063 | 2025-09-29 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8ad079d5-760a-3b0a-b11e-d6a55b50f4ec | -15.16514 | -46.41656 | 2025-09-29 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6b42c72-c902-365a-a301-81aa3ceb8b05 | -10.53315 | -54.3889 | 2025-09-29 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c1efa33-8378-328e-9fe7-4bc34d25d8e9 | -12.66417 | -46.92663 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7a0a0479-fc79-30c3-ab90-52809e98b4cc | -13.57602 | -47.29697 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 03c0a536-1dfe-3dd8-9f6f-c7f9cb1c7bc6 | -14.54354 | -48.44373 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ca5a4f83-1518-31fa-a744-fba1e3859d24 | -15.35783 | -56.95529 | 2025-09-29 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd38be56-cddf-31bb-afc9-aada87ff734c | -13.64957 | -48.0658 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 287391fc-a28c-3193-9284-e57dd240bea3 | -11.62508 | -52.85294 | 2025-09-29 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7525954d-f501-3543-b2af-878e0528202f | -13.02566 | -49.45016 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5fda199f-c315-333e-aeeb-5713e3ffc03c | -15.99939 | -47.0325 | 2025-09-29 04:59:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee00d4ae-98cc-3185-8468-8d97df58dffd | -15.34101 | -47.9093 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf90d0b6-1836-3a36-a760-ac336d173431 | -13.63702 | -47.33382 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bde7c973-4939-3dff-84d2-53e9a1ea590c | -13.62062 | -47.34113 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00899b30-4cd7-3c4f-adf8-013755b44069 | -13.77017 | -47.91582 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8ba1906e-2652-3d34-ae73-ff8a4907a5f4 | -11.7453 | -46.84307 | 2025-09-29 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b60a7fc8-af79-3199-b61d-f13a29d4e2ff | -12.85102 | -46.97665 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf01456c-b69e-3cb9-8db5-00149e73999b | -13.63673 | -47.33619 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93c9b57e-cd76-3173-b62b-892b780ea133 | -15.32474 | -47.91483 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 807e97f2-07fe-32e2-b40f-6ae1bdfa89c1 | -11.94256 | -48.06259 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6390fc28-6682-3677-a4c2-f538eb35f597 | -11.94454 | -48.00999 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efd4aada-7999-3b0a-adad-766ebaeb6b5b | -13.56976 | -47.30566 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f9b6c9b-b02e-37c5-9298-625a3405c915 | -15.21279 | -48.04916 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71070302-ef6a-3d54-8e84-4fb0d740d781 | -13.80503 | -47.95571 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 191a1ab2-5dcb-35c7-b86a-0f567b600254 | -13.18551 | -47.44164 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c40fb208-07e9-3e62-af1d-962960d0a0b5 | -12.66897 | -46.90479 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6d0b34d-d7c9-3c3d-b6a7-cf2a8b55c9b2 | -11.9946 | -46.59834 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f39821ea-7b33-356f-8640-59804710579b | -14.44503 | -44.88242 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbfa57c8-54aa-3f84-a331-4b8461048b2b | -14.65279 | -48.15286 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc8bdbf5-2283-31bd-acd0-b299d44cbb1f | -11.93305 | -48.02424 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 82652658-8cf3-325c-9564-ec1a839db208 | -11.99943 | -47.10013 | 2025-09-29 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3620e45a-abfd-3257-9777-5053e5c6dd47 | -11.81137 | -51.80499 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7066ab6a-7084-36f8-bf83-311c93eecaab | -13.59696 | -48.05341 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6d30c5e9-36da-353d-9afb-ed89521055c9 | -16.49469 | -46.03918 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f726f3c-37ed-33b4-8e0c-86c8dfe9a18c | -11.66035 | -45.33115 | 2025-09-29 04:59:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7cad7e76-c2cf-32bd-8b18-b4191e8a3db6 | -11.95935 | -48.04454 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d064ad63-e970-31dd-a968-d3e2f8f42a64 | -15.28162 | -49.50529 | 2025-09-29 04:59:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README72.md)
