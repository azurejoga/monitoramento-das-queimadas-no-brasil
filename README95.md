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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 457a9e2a-e48d-3b75-9c61-9b51094df5d8 | -14.7123 | -48.20681 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd1bc6ea-1a89-3910-807f-c1591ad5103c | -18.4431 | -43.8111 | 2025-10-02 04:32:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74a39b5b-9e06-3756-90bd-4437ed5aa12d | -14.89595 | -48.32849 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6acfb0f0-c586-3cb6-8678-7a7a79d2c19f | -12.95572 | -46.37416 | 2025-10-02 04:32:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70e9318d-b6c0-3170-84e6-2bd23654676a | -17.97971 | -45.01447 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| de4b7137-bc34-3a46-9202-653039da0f2d | -15.24932 | -47.89124 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d8cd83d-1359-37b4-b22c-7142e92ffe1a | -12.05744 | -48.77487 | 2025-10-02 04:32:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbfcbdd3-fd45-3887-8918-c825e15abeff | -13.45896 | -47.25261 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 034e842b-8401-3081-9415-1199c0995a83 | -18.3458 | -44.5054 | 2025-10-02 04:32:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d08bb8b-32cd-3438-ba19-7b5c50198aca | -13.78263 | -48.05778 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1716746b-b601-3e3b-b15c-b04f0da95aea | -12.68338 | -48.56037 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce5c11f4-5a09-35ec-83a4-5b366e15f464 | -14.32399 | -45.96281 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d9b8ca5-a131-3d1c-9176-a0e1c7b23d98 | -15.49833 | -42.55465 | 2025-10-02 04:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58eae07c-8154-3a45-81e4-72142c811759 | -13.8081 | -47.53188 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02b1814e-e6a7-30c4-a068-d375a3893780 | -19.28942 | -43.74011 | 2025-10-02 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14998040-b268-303d-ba28-ef7f951e1298 | -13.40546 | -44.39238 | 2025-10-02 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28a3f6fa-5c40-31a8-9d43-6cf8b2c3f94e | -13.76227 | -48.69088 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1d3a2c5-4ccf-34f0-b0fb-a56b6eed0b4d | -14.44404 | -46.34569 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 361c196e-d02a-3899-a21f-2a4202adc158 | -13.37328 | -47.28309 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cb737b8a-5c01-3696-af2c-1a2fa2bcfa3e | -13.42091 | -47.80187 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e936e5c5-ce86-37a4-9585-eb3e156e475c | -13.56539 | -48.10568 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a437bfa9-d57a-32ac-ae46-e8ccac40b24c | -13.01342 | -45.21854 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a6379cb-7554-3d57-be1d-ece07f9da7de | -12.88819 | -46.90427 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02d6e9b1-fdbd-3101-87a9-f9e1b7bf25c5 | -12.86541 | -47.00708 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf417753-dd9d-33e3-a18e-b5c9fe579acd | -12.75116 | -46.91185 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b00189f-ca6a-39a5-a5a1-e5a7d235aeec | -14.48284 | -48.43965 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0f0f159d-41b3-376f-bc17-ebea339b4415 | -14.88816 | -48.33452 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa370a20-0ba8-3386-a501-6ae2fc48da84 | -13.06172 | -49.17404 | 2025-10-02 04:32:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c47297f-e1c8-39e9-ba00-4d4b39b95360 | -14.22499 | -46.11405 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acd651ca-a1f5-3525-9aea-25d1ae43ae40 | -13.56525 | -47.5919 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82ce9eb8-9c25-3d95-bcde-c3a0bb292cad | -17.16665 | -47.02641 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a292b958-66b2-3160-9e5f-6c937c32b7fb | -13.23971 | -47.338 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0055b64d-aa0d-38ea-a4d9-50d3577c0144 | -19.89464 | -44.93443 | 2025-10-02 04:32:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0e2ef1a-7e0d-3fc2-bf41-62ebabed1b38 | -14.41381 | -46.08282 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa6fff23-55e4-325e-b80a-640a18849ee2 | -13.1656 | -47.81078 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1316307-c2f7-3bf4-a72b-f540570af6bf | -17.02544 | -49.65602 | 2025-10-02 04:32:00 | NPP-375D | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0c5e1c2-70d6-35e1-827e-1e0895240d00 | -14.57966 | -46.37008 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a34c9a76-d0e0-3623-a9b0-9059f1daf700 | -15.15775 | -48.38697 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac97804f-a178-34f7-9b4f-644718a4dc98 | -13.32214 | -47.00588 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a3f4437e-2630-34e7-bc58-9369832808f3 | -12.24624 | -47.7879 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f7117b2-3358-39cc-a91d-83021d6877a5 | -13.75837 | -47.97345 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f126a74e-be33-34f1-8fc5-cd06f54d13ed | -13.75608 | -48.00958 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| decb3a66-7c16-3e7a-9d4b-112cb3e70565 | -13.74721 | -48.00081 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38b3c7d4-83f6-3729-b2e2-32ad45893cd2 | -15.25374 | -47.90672 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 276fcac5-42bc-32cc-b112-249f17bf4a0c | -14.59963 | -48.23608 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e22979e-e48d-305c-961e-4a8a75580819 | -13.52465 | -47.27076 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 070473ac-e4ce-3e3d-a6c2-699807b70b0e | -14.29854 | -45.96688 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9a031c7-6e57-3b8c-87c7-ff23f7e031ba | -13.32644 | -47.20977 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9daae86e-f8dd-3f22-9342-61a4288f1b4c | -13.95371 | -44.91175 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a5e1f8e-8e7c-35c4-8541-f1261898071c | -19.01001 | -45.00505 | 2025-10-02 04:32:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3ebeeff-ca07-39b1-b7a9-e7d203650a2d | -14.36395 | -45.9094 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0a5d2081-a9d7-36a1-a2a0-9b30cb4d548e | -13.75728 | -47.95867 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e32f9706-bdb7-3861-afdf-1a83a8984d0d | -13.3168 | -47.81779 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8591dc2-37d2-34f4-aae0-280317ecff36 | -13.17058 | -47.82251 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7db0cf13-f414-31d7-b854-dcb1984b6a10 | -15.29197 | -45.08874 | 2025-10-02 04:32:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5497f6e-d78c-3387-ba6d-4ad06d515146 | -16.1758 | -57.59413 | 2025-10-02 04:32:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 175a222d-cb59-32ab-8066-83f3406a6da1 | -14.21694 | -46.12064 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d90c118d-86be-38e9-8bf4-22cfaccc6530 | -13.25029 | -47.31408 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fed56d6-60f8-3aae-8761-9946cacb77dc | -15.14694 | -48.02148 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dfe623cb-b0b4-3ead-82bb-22fd9fa2010e | -13.95696 | -48.1298 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dfeb826f-68ce-3b7e-ac95-827afcb9033b | -13.32845 | -47.80879 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec7d14d4-fb4d-3d1a-8981-28b2f3bdd074 | -17.17522 | -47.0159 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e39b50bb-7d4e-3ffc-9a7c-d98448913ddb | -11.86866 | -48.07907 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b89e82e4-347a-31f3-b0e6-28f72a3b5b4a | -15.33168 | -47.94868 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57694f5e-7f3d-3b19-a821-0e63b21afd7a | -15.34705 | -46.29311 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72a16e8a-303d-3f32-a53e-50aa21dd34b6 | -13.28364 | -47.25375 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 814fd3f4-72a4-36e1-b5f6-bd3139df9de7 | -14.59884 | -48.32746 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47414140-3305-353e-9fa0-cca279265c21 | -12.86486 | -47.01065 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48b5623d-7e1d-3bf7-bedb-6fc6cf301be7 | -14.28641 | -45.97697 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 686f33e8-838f-349f-99b8-487d1b606103 | -13.00754 | -45.20942 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7cc0bc1a-9899-3648-a4b6-ed2199a6d972 | -14.41611 | -46.11478 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e49e9b69-00c7-3256-ac70-1774b8ded477 | -11.91297 | -47.88651 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef1d6fb4-ff60-34ef-a0dc-72dc79dc9bd9 | -18.52512 | -45.03905 | 2025-10-02 04:32:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 28bd1454-8c1f-3d83-a3d4-d6ee8382b8c4 | -15.34758 | -46.26567 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c507a5e-386b-3a88-b02f-c2c8138091cb | -14.33986 | -47.12663 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8e0b099-a529-3906-8c02-2396ec5a17bd | -12.26198 | -47.81276 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55d458cb-5633-383e-b63e-24af21f4ad72 | -12.72304 | -44.84483 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 889ef18b-1d27-3ca6-abc9-3c5bac2d71b8 | -13.31318 | -46.99712 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8ccdf93-b73e-33bc-bf67-549f64112368 | -12.80697 | -46.9062 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d3c5b23-6299-306e-ab6b-ff2c5eee63da | -14.34994 | -47.12828 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8510c5d9-b693-36c8-91cb-55e862343b87 | -13.80699 | -47.53902 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| cfc8b760-7056-3e2c-b403-5d30c319e534 | -15.24764 | -47.90202 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3494fb62-45c1-338c-a69f-60232332316e | -13.33941 | -47.79943 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 727bb442-df23-3dd3-8845-135f722d5e4d | -14.47951 | -48.4391 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99eae660-0dd7-3325-b9c5-0b6569963bbe | -12.5116 | -46.84072 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f294d6d-b459-3af2-b608-91802421d12a | -15.17255 | -43.62271 | 2025-10-02 04:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 114f56eb-cb28-3080-ae2a-f1bb0d5d594f | -11.94289 | -47.88382 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 594ec922-aa9c-323b-8d26-62c90700a286 | -13.75275 | -48.00903 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1620997-fca0-391b-a22a-99ea7cae3b0a | -13.22146 | -48.44015 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b73726b0-70d5-36f9-9b1f-c96767368585 | -13.79876 | -48.04219 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77750e3b-ad11-327b-a96a-1089313bc29b | -17.95692 | -44.41402 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0f3ad41-552c-3f9a-ad0f-ed86d7a90cb2 | -11.87156 | -49.08234 | 2025-10-02 04:32:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfdf189a-06c5-3f16-a849-18a389968e9f | -13.06309 | -47.06091 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddbb211d-20fd-3311-bbcc-345c4e0bf142 | -11.9329 | -47.88219 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c460dfd8-ab85-37d8-8b7f-b9eda0c27a81 | -18.18241 | -53.28394 | 2025-10-02 04:32:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5265e6e5-3ec4-331a-bf29-1e8546382c2d | -14.91209 | -47.23211 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3feeccb1-f229-3c69-b173-738af05c43fe | -13.30704 | -46.99243 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 115203aa-9a9d-35f5-a84f-6d892ea65cce | -13.53864 | -47.27982 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1755b82-6e12-3ea4-a149-d46e32b23627 | -15.94593 | -43.3037 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aedbaaad-a1fb-305f-b38c-7dda6063e063 | -12.47974 | -47.26719 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README96.md)
