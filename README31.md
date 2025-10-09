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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe2a6a47-4f63-38e9-8011-bf7989803255 | -18.04059 | -44.98086 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3ceabf6-09cb-39f7-bc94-2d0a3ed56702 | -17.38967 | -46.89208 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8328965-2dac-3fab-ab81-7c046ba494a7 | -17.37193 | -46.66164 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb90c1b3-1c24-37f1-b26b-ee6fcf2cadf9 | -17.9781 | -44.96383 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c69b9bbd-e885-3e14-9633-35876a7e43f1 | -17.39198 | -46.87954 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fe8ccae-45d0-339a-9ab3-5c75759b06aa | -17.94849 | -44.41961 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bc1f35e-df55-3265-92e6-1fb41a3a3cef | -17.95289 | -44.99546 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 76c5ab5a-1aff-3635-bdc0-631b02d5cf67 | -17.95372 | -44.99071 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a0b01e49-3438-31c0-b20f-ee42758902cf | -17.65008 | -44.4343 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 345255df-bd3f-372d-937e-543339d7e556 | -18.77816 | -44.61713 | 2025-10-09 04:02:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23dbc2ef-4924-3b2e-b8eb-fc85c38d6d11 | -17.37606 | -46.66258 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45edb0e7-45ba-30f7-a553-73bca7d479b3 | -16.72748 | -47.62023 | 2025-10-09 04:02:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d26e2579-0a10-3cd5-8d7c-1a4f77da7a9f | -19.74046 | -42.20374 | 2025-10-09 04:02:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5ee9d6d2-9c5d-3d21-98a0-54bd304992dd | -18.6861 | -43.70136 | 2025-10-09 04:02:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7ef2d900-9735-3210-b09d-db4ab8e905f7 | -18.69098 | -43.69382 | 2025-10-09 04:02:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3a9c0ff3-15a8-3846-bc08-731549fcf3c5 | -18.64548 | -43.91716 | 2025-10-09 04:02:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b5f90a35-ab58-31fd-9c7c-eb25de9d488b | -17.95309 | -44.41476 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b37eef97-ac93-3020-aab1-ce12e3d8a88c | -19.71541 | -44.00413 | 2025-10-09 04:02:00 | NPP-375D | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82a46838-895e-3625-965d-50ac0c592ef1 | -18.25148 | -46.99318 | 2025-10-09 04:02:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52595bb9-7648-39e2-811e-848f0c92818c | -17.95644 | -44.99816 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4868278-dc69-349f-a558-dec3faa646d6 | -18.05737 | -44.4396 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b94e3795-2dc2-3560-8821-82fb99445f57 | -17.39397 | -46.88729 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de37b355-addc-381d-985c-58c41a626468 | -17.95288 | -44.41584 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 341e32b7-bb8e-3307-a76e-bad7ee1f37ab | -18.06418 | -44.42053 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b5bf588-05b5-3939-95b5-e62f2604fe9f | -18.03807 | -44.99508 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0378322-87d6-33f8-bcab-efa9f2924f84 | -17.95935 | -45.00345 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03e2af93-b577-3b5d-a087-8c32ad23fa0d | -17.3771 | -46.88914 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6f91a5d-db2f-31de-914e-ba5256bb22b3 | -17.56038 | -43.5206 | 2025-10-09 04:02:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9e547f3-d482-3758-afba-207411709041 | -17.53663 | -46.75593 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 749c8a8e-f043-3cf0-8cc4-63a5210bada2 | -17.9577 | -45.0103 | 2025-10-09 04:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b362cf04-11cc-383f-bdbd-dfa1d55c3440 | -6.6995 | -46.2946 | 2025-10-09 04:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| f6ecaeb3-a307-3d6b-9f39-36072bfb8192 | -17.9224 | -57.5128 | 2025-10-09 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.2 |
| bc414ec1-7cc3-3f98-89d8-2870702b2b78 | -17.9583 | -44.9863 | 2025-10-09 04:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 05e56fa4-691c-32da-bbc5-8eee3b7ef81e | -17.9227 | -57.4922 | 2025-10-09 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| e03ce3d0-43a3-3953-9f42-6f498b741b46 | -8.1993 | -43.3424 | 2025-10-09 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| b40b1f0f-395a-32ce-ae93-12f47b4f77c7 | -10.8558 | -44.6199 | 2025-10-09 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| baa167d8-cd79-392e-bb72-e33f64cfe858 | -6.6808 | -46.2961 | 2025-10-09 04:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 434262e4-11a7-3396-8681-f1623cbb52c9 | -7.48446 | -43.11245 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 567957ce-d900-3ef4-9868-400a322042a7 | -5.59252 | -44.87345 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14efbe52-3601-3419-8f1d-0c907ce17d65 | -3.89139 | -44.91132 | 2025-10-09 04:17:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62a7f133-7725-31d9-b39e-9e23c1a9faa6 | -3.90684 | -44.34062 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03950687-7bec-3c9c-a32f-5b61e315540f | -6.72407 | -42.86587 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 83afe0c7-3027-3339-a15e-08433d9c47e7 | -7.49064 | -42.73055 | 2025-10-09 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0607b7c2-3b64-38a8-a5e9-be7d92804606 | -7.01856 | -42.74825 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7fc01ac8-49ce-35db-abea-7ec644542b55 | -5.27883 | -44.88092 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4cabe00-46a8-35e9-9a81-64d6502360e4 | -4.61454 | -43.14443 | 2025-10-09 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3662126-8c55-32d7-9e17-906231274fd8 | -4.68493 | -45.83781 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cb414b0-aa71-323c-8377-f9ef8189f458 | -4.37543 | -46.75306 | 2025-10-09 04:17:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acf7c829-a4a9-3e1c-8765-84ce46bab5c1 | -4.89922 | -42.25243 | 2025-10-09 04:17:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ecf52a01-5c84-3841-9a7c-8724b50aac35 | -3.95779 | -44.16854 | 2025-10-09 04:17:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3024fcee-6cc7-393d-817c-f4de6aab3870 | -4.7333 | -42.80036 | 2025-10-09 04:17:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7813a3a9-517e-3848-b153-4ebe3a53a98b | -7.23968 | -43.99075 | 2025-10-09 04:17:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1071c931-9139-32c8-ab42-74c2dc6f870d | -3.37946 | -50.28324 | 2025-10-09 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93acf224-0ae0-3785-9be8-72a6311635af | -6.45755 | -44.58169 | 2025-10-09 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d44de96-6148-33a0-a5ae-a09cb61db5dc | -6.28015 | -44.08983 | 2025-10-09 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 559a862f-990f-3a89-a48e-00e36c3d9c5d | -5.31213 | -45.37708 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63929a0c-f167-335e-b5be-bdc9fd4ed217 | -4.00898 | -43.28312 | 2025-10-09 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1653dcaa-b5b0-3cd0-9e1c-0d92138bf5d0 | -7.02131 | -42.86608 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6b7a515f-3e8e-3dc4-b762-2d8e6aacaaca | -4.42494 | -47.75378 | 2025-10-09 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab5ce00f-776e-355e-85ca-2b7c5e29d59a | -2.78752 | -49.59621 | 2025-10-09 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77b15da6-189b-3475-b6e8-7e640c3ec062 | -2.1893 | -54.47127 | 2025-10-09 04:17:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14a59922-acf8-3202-b8dd-af28beaeeb45 | -3.38798 | -49.04694 | 2025-10-09 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72a7f32f-7ff5-3346-9629-89c56d729d87 | -5.80768 | -44.67373 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad9491df-64a1-31ea-9085-7abefeb381ed | -6.92647 | -45.05358 | 2025-10-09 04:17:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e96a2d52-6673-35e4-b133-98e413c5ccfb | -3.09879 | -47.01636 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 32e6afe1-b085-3580-a839-a8cae410ddd5 | -5.30298 | -43.08483 | 2025-10-09 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1341247e-b46f-3c93-bded-5c579be2f255 | -6.39645 | -44.01922 | 2025-10-09 04:17:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b743ab92-372d-3ce8-84be-a83737290914 | -5.13346 | -46.25512 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a823cac5-4342-32b3-bf57-c669eed7691c | -7.01172 | -42.74718 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1b8a9659-204c-3c1e-8669-79e492fa7af9 | -6.32179 | -46.19598 | 2025-10-09 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fba3177-f411-36a5-b563-52716e60431d | -6.56855 | -44.15634 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01ded859-fb7b-32e3-80e5-8bd5eeb6be74 | -2.88708 | -50.72799 | 2025-10-09 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6dfa1a97-664f-3caf-89af-b64659a226e6 | -3.89804 | -44.90906 | 2025-10-09 04:17:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3fa83e6-e31e-3fd5-bd93-540c4210fc88 | -2.94447 | -48.0727 | 2025-10-09 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faf5fb91-8d8b-370e-884d-8bfd6dbe4660 | -7.4555 | -43.02903 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3bf14e12-7c97-3474-bd37-483b0bbb312f | -3.01758 | -47.81872 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 627a3298-64f8-30fa-b000-ba077e9af34e | -6.94794 | -42.70731 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 96e0a31a-0701-3271-8d8a-151bc02b056d | -5.39696 | -40.98169 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 249fae52-d713-3a83-8c30-23938a622c46 | -2.18708 | -54.48471 | 2025-10-09 04:17:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3eb0808b-9939-3bd6-b219-bd533ac79539 | -3.11005 | -47.79792 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f24e2ec9-d934-3cfa-963f-efafad5b6068 | -5.87211 | -44.99606 | 2025-10-09 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f0cba08-336b-3ef8-8ed2-5ccedf1d9e4c | -4.42866 | -47.75429 | 2025-10-09 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80ab029f-99f8-330d-babe-fd2d16a33a48 | -5.15116 | -46.10188 | 2025-10-09 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9250b40-08c3-375b-aae9-e631c40c354c | -5.52873 | -45.31793 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6525d907-4c8e-332e-b39c-3ec50dd671ad | -7.48556 | -43.08265 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a59d6ce8-b038-3871-89a1-b143ac283a3f | -6.57018 | -44.14594 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8047a43e-a562-3a16-abd7-50af2a84a679 | -5.04402 | -45.6306 | 2025-10-09 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31eb5863-f82a-372e-b1b6-829be9fc14d2 | -5.28498 | -45.75326 | 2025-10-09 04:17:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3ad3deb0-5232-3f5b-b2fc-efcc6ab71940 | -5.14032 | -46.25626 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07477894-cf74-393a-947f-adedcb80a853 | 0.89374 | -51.14205 | 2025-10-09 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67481db2-3a83-32cc-88e5-b7a4c6ece441 | -5.30871 | -42.72626 | 2025-10-09 04:17:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f5684b95-cf8b-30a5-8a02-aa8f5bcb54dd | -5.90529 | -42.85817 | 2025-10-09 04:17:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8b45a0d2-5019-375d-a334-8130e08cad1c | -5.82792 | -44.09328 | 2025-10-09 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 676f6970-ed19-32cf-8f2d-54cb2a75c694 | -4.07108 | -44.48358 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e34c84c6-47f5-3a92-a167-92f29ce532bf | -6.20618 | -44.06404 | 2025-10-09 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18de8a7c-906d-375f-8d50-2f6465d0f665 | -5.16769 | -45.32219 | 2025-10-09 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef11398e-3fc0-3913-b612-f3e57fac7d94 | -5.64897 | -43.60992 | 2025-10-09 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4f87ed9-a370-3f48-a6e0-70a239de19c4 | -5.25108 | -46.48626 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88554051-1fb7-373e-b20f-3fcd15e25fbe | -5.34878 | -43.74817 | 2025-10-09 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b1f15284-f6fc-3d5d-95cf-3048c9c9cdf2 | -4.43868 | -43.22862 | 2025-10-09 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README32.md)
