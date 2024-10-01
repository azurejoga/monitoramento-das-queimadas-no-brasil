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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4397eecc-c334-30e2-b01a-0d29dfe2ddbb | -22.11742 | -48.5601 | 2024-10-01 03:51:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71594c4e-b4c0-35b2-bce9-506f10254d44 | -21.85441 | -47.16885 | 2024-10-01 03:51:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa3196c1-3f3a-3538-b96c-0fc7018f1073 | -21.85351 | -47.17344 | 2024-10-01 03:51:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fa4f6e7-3fc8-3a75-8b11-46b07e6e2703 | -21.85253 | -47.17046 | 2024-10-01 03:51:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed18209a-32fb-3710-bd78-c98cd83f465f | -21.84911 | -47.17249 | 2024-10-01 03:51:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59311d26-0e9a-39ad-b5d6-f2e7884a92d1 | -19.62318 | -44.20696 | 2024-10-01 03:51:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc596de7-bbfe-32f2-9f8c-cdeb8b56b9fe | -19.61955 | -44.11917 | 2024-10-01 03:51:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54d3a3fd-869e-3c63-bc7b-9c542f052353 | -19.61891 | -44.11239 | 2024-10-01 03:51:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29742f85-a8ec-3d65-8d16-bacfab9bcbfb | -19.61805 | -44.11721 | 2024-10-01 03:51:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fec983ae-af5c-3f81-b871-491441d87702 | -19.61663 | -44.11361 | 2024-10-01 03:51:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b715a281-dafc-3e28-96b5-e133605e4796 | -19.6151 | -44.11165 | 2024-10-01 03:51:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d8917fa-c7a8-3302-91ea-a6fb7ab74974 | -19.609 | -44.11216 | 2024-10-01 03:51:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6eb4c4b1-ed52-352a-86de-2c9c944e28f1 | -19.60811 | -44.11699 | 2024-10-01 03:51:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2dac5908-d50f-392b-9a8e-ad4f1d4d6adb | -19.60748 | -44.1102 | 2024-10-01 03:51:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0778cf61-50e3-3561-ab1c-39e6a36a52ec | -19.60661 | -44.11503 | 2024-10-01 03:51:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4b492d64-2238-3064-bded-1ee71a8bc0da | -19.60519 | -44.11144 | 2024-10-01 03:51:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8a27845-b97c-31a0-be70-1104fc7c246e | -19.60429 | -44.11626 | 2024-10-01 03:51:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 997e8699-f1fd-31d6-843b-88f4e632a3fe | -19.6028 | -44.11428 | 2024-10-01 03:51:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d9cb0dc-a43d-3949-88ef-d555f82b6963 | -19.25097 | -43.34909 | 2024-10-01 03:51:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fddf482b-11e9-3d99-960e-bfff99fc7289 | -19.25016 | -43.35361 | 2024-10-01 03:51:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 59d1b455-c8f3-3372-8cd8-816f381d4bed | -19.24888 | -43.33945 | 2024-10-01 03:51:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52f6a33e-2e09-374d-a24f-fece64f5402a | -19.24698 | -44.3716 | 2024-10-01 03:51:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7834b57-6744-3f49-88e4-aa4d7b07b304 | -19.2465 | -43.35279 | 2024-10-01 03:51:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fa56b99f-1740-3884-9559-fd4a3f1b4736 | -19.24643 | -44.37401 | 2024-10-01 03:51:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e3532b3-5e70-3f2e-84af-7e121bf9e574 | -19.24519 | -43.33885 | 2024-10-01 03:51:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0f757c11-5be3-36d1-9f5d-3c6161657a7f | -19.24407 | -44.36557 | 2024-10-01 03:51:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f64a3fcb-2125-392a-b172-dc284a6ad779 | -19.24349 | -44.36794 | 2024-10-01 03:51:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6462aaef-f511-368d-94c5-e096b8b3d71f | -18.9807 | -45.08029 | 2024-10-01 03:51:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d374a725-e380-3858-95fc-e81ee96b7ae0 | -18.81073 | -45.80046 | 2024-10-01 03:51:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d064795-3c5a-3d0c-91d7-2a85171e1a15 | -18.80995 | -45.80456 | 2024-10-01 03:51:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be57f86b-34af-3d06-aaee-069eddfa5fa9 | -18.80646 | -45.79961 | 2024-10-01 03:51:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9402a6cf-b0a3-3be5-8801-b617316c60ed | -18.80567 | -45.80373 | 2024-10-01 03:51:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ae71425-1db9-341d-b706-3e6bdc70713d | -18.66732 | -44.26438 | 2024-10-01 03:51:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9334b02f-ca37-3941-bd98-c543cd1f4e0e | -18.66638 | -44.26954 | 2024-10-01 03:51:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95c45886-03ad-3597-98ed-681049583930 | -20.3256 | -44.91832 | 2024-10-01 03:51:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54bc0189-4f68-3ec6-b8a2-99f37f51129f | -20.3244 | -44.91394 | 2024-10-01 03:51:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b51ae063-534a-3799-b564-f703cb543fea | -20.3234 | -44.91918 | 2024-10-01 03:51:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b90bab8-94c8-3a2f-99ab-f4f4bebe42e1 | -20.09648 | -44.82745 | 2024-10-01 03:51:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3d26a4c-f32f-3569-b9f3-35a0a071c70d | -20.07784 | -44.60018 | 2024-10-01 03:51:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b829f388-2c0c-3c27-b4bd-22fe0ca693ce | -20.07397 | -44.59933 | 2024-10-01 03:51:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c8a02ab-0d45-3c50-a548-ea9cd8054a60 | -20.07331 | -44.60289 | 2024-10-01 03:51:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36ade8d0-a60a-362b-8b90-9492a2d94066 | -20.07297 | -44.60465 | 2024-10-01 03:51:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34354daf-a9ee-3b32-bf6b-dbcc5568cdc6 | -20.00268 | -45.06528 | 2024-10-01 03:51:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab34047f-861f-3821-ba51-aa6ae4d60d98 | -19.80972 | -44.2449 | 2024-10-01 03:51:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89c4ffb3-4408-3377-8149-60cd66230216 | -19.80791 | -44.2472 | 2024-10-01 03:51:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92d605ef-9228-34f5-adcc-a2777b9a045a | -19.76666 | -43.67234 | 2024-10-01 03:51:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36f4e526-9438-3c5c-8dbd-777c98325dbd | -19.71844 | -45.50644 | 2024-10-01 03:51:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f038ea89-2dee-3219-8998-01ea57fa4eeb | -21.31029 | -49.23857 | 2024-10-01 03:51:00 | NPP-375D | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4a5495a9-9a92-3ae8-9063-e402d61267a6 | -21.30591 | -49.23418 | 2024-10-01 03:51:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 841d469c-0da7-3a4f-9671-39d820f93aa1 | -21.30527 | -49.23725 | 2024-10-01 03:51:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c62c4a5f-83a1-39b5-8f7d-772c6e516444 | -21.30153 | -49.22986 | 2024-10-01 03:51:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 91b59934-8d76-3748-affe-7808a6db8f0a | -21.30088 | -49.23294 | 2024-10-01 03:51:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d64ffa22-ebb8-3f99-b7e2-2b4e78a987e7 | -23.54776 | -47.65039 | 2024-10-01 03:51:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 19ecc61b-6e1a-362c-93a9-d0bdea4817cf | -23.40526 | -46.55687 | 2024-10-01 03:51:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d6fef29e-e042-3b63-a9f5-dcdedb202bd9 | -23.36196 | -46.99501 | 2024-10-01 03:51:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c5a86fd1-8d41-3903-8f43-5811fd110815 | -23.34049 | -46.77214 | 2024-10-01 03:51:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 49dfb213-7764-34ae-a89b-4bd548fc53b6 | -23.33632 | -46.77124 | 2024-10-01 03:51:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 0040bf0d-bcfe-3cc9-a120-f330da7db499 | -23.27689 | -46.65401 | 2024-10-01 03:51:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 92bb756d-a83c-3d1c-9b00-963308f84d4c | -23.27272 | -46.65323 | 2024-10-01 03:51:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c16617d2-6e47-3bc5-9a0e-3f2d5dba3dbe | -23.2719 | -46.65734 | 2024-10-01 03:51:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e65a21a2-b345-3f9f-8464-8d3e352a1edc | -23.20908 | -46.80007 | 2024-10-01 03:51:00 | NPP-375D | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 151ef3c0-2205-3c01-a75b-200d5d4439de | -23.15735 | -46.32858 | 2024-10-01 03:51:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7ac9adc0-a635-30ae-9900-13f1b7aceb1c | -23.11932 | -46.41413 | 2024-10-01 03:51:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e0108b53-dbe0-359f-935a-f90027f7d42c | -23.10257 | -46.58693 | 2024-10-01 03:51:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7bc77d18-967c-33eb-8df3-e7620fefae71 | -23.10178 | -46.59095 | 2024-10-01 03:51:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5cdba8e0-b71b-3dcc-8c4a-609b40b29591 | -23.10099 | -46.59498 | 2024-10-01 03:51:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 20131138-6076-323e-a534-411d380a7ff9 | -23.0991 | -46.39859 | 2024-10-01 03:51:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 476bcf6e-28c0-3c18-80d3-43185e64c5bd | -23.0972 | -46.39623 | 2024-10-01 03:51:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| bc63ec5c-ee9a-3669-97ab-1278bfcecdbe | -23.09505 | -46.3974 | 2024-10-01 03:51:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6d548b41-97e1-3438-b84b-ac10e28636c9 | -23.09471 | -46.38721 | 2024-10-01 03:51:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 724d7400-c142-34b0-b2e8-016f9aaea75f | -23.09247 | -46.38858 | 2024-10-01 03:51:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ec36947b-e7f0-3729-9954-7f5f0cd320c7 | -23.08424 | -46.90306 | 2024-10-01 03:51:00 | NPP-375D | LOUVEIRA | SÃO PAULO | Brasil | 3527306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9ca4a7a2-3518-368e-8401-20773303d699 | -22.77961 | -46.81429 | 2024-10-01 03:51:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f735fef2-4baa-392a-ab46-4c1e7bde0f95 | -22.77877 | -46.8186 | 2024-10-01 03:51:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| d2509d6c-aec3-373b-8b2c-d7605c9baa0c | -22.7319 | -47.03549 | 2024-10-01 03:51:00 | NPP-375D | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5f25009b-27e3-3109-9315-f8ff1629e502 | -22.72608 | -46.68464 | 2024-10-01 03:51:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 84ccc925-e94a-3be8-98de-bfcd60ee829c | -22.72367 | -46.67482 | 2024-10-01 03:51:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 34e833f5-9054-3b0b-a4f1-cdefc2337f1a | -22.72286 | -46.67884 | 2024-10-01 03:51:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 3bef47c7-7497-349c-8f86-c79c05586acd | -22.72198 | -46.68327 | 2024-10-01 03:51:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| ed09490f-0ca2-3fba-97df-3c93b00660aa | -22.71987 | -46.67396 | 2024-10-01 03:51:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| fd442631-95c6-328b-a8fe-d3b17eeb71f1 | -22.71953 | -46.67361 | 2024-10-01 03:51:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| dd6b8d53-cee5-3dcd-922d-c8621f2c7d87 | -22.71909 | -46.678 | 2024-10-01 03:51:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| eeb53055-04ce-3d2f-ab31-da954932575e | -22.71873 | -46.67763 | 2024-10-01 03:51:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 18beae1e-c2ab-344d-aaa8-d5ad651c3e3f | -22.71822 | -46.68253 | 2024-10-01 03:51:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 18901d5a-f19b-3b16-b59a-06a8d7b94c8f | -22.71783 | -46.68212 | 2024-10-01 03:51:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 494185d5-6248-3be6-9134-dbea725f73d4 | -22.71005 | -46.23583 | 2024-10-01 03:51:00 | NPP-375D | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 56b5f2d6-e849-363a-abde-cb72117414f7 | -22.37994 | -49.31755 | 2024-10-01 03:51:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 4734ea3a-36ae-3c84-9654-04cc9adeb95d | -22.3766 | -49.31019 | 2024-10-01 03:51:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.4 |
| 84d5da76-5e44-355b-95c2-cc4c54244eab | -22.37643 | -49.33569 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 171ebd72-5309-3094-aa74-6264077f9686 | -22.37622 | -49.31069 | 2024-10-01 03:51:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| ff693e3b-08a6-3d7e-ac27-69f913728eed | -22.37588 | -49.33611 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.6 |
| 3fd94f81-9786-3604-9f0f-1270ab1388ea | -22.37536 | -49.31605 | 2024-10-01 03:51:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.4 |
| 25cace00-a4af-3f12-b265-2beb46b1047b | -22.37515 | -49.34177 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| baa090aa-558c-3c13-b00a-9d2a200036c8 | -22.37494 | -49.31652 | 2024-10-01 03:51:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| affe9b83-995a-369e-bf3c-c1ca9649a2b5 | -22.37456 | -49.34216 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 831aa36d-e3ba-37f8-a949-06596166e7c0 | -22.37412 | -49.32193 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 67b2a5d1-acdd-3c36-bb62-6752c2270667 | -22.37388 | -49.34775 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 2e152e08-c9c4-317e-a9ec-70929ceb90da | -22.37366 | -49.3224 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 5670c64b-c736-3143-b2fe-0405a9ff4e56 | -22.37325 | -49.34813 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 999dd4a1-90d0-335d-b180-60bc05da32aa | -22.37288 | -49.30315 | 2024-10-01 03:51:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |


[Clique aqui para ver as próximas entradas](README57.md)
