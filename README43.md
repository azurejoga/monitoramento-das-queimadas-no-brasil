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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f22efe8-fec4-334a-b2c8-4e64bd92ecd9 | -7.11229 | -44.71912 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 516c26ec-af7f-345c-9147-46a3eb272c77 | -8.20541 | -43.3204 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 859ea909-c766-3826-884e-4abb1a09aaf1 | -6.37161 | -41.48271 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| de6a78f3-3349-3d68-8e53-d51d42ace042 | -7.17752 | -42.19497 | 2025-10-16 04:38:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8186e0c6-64a4-33d9-9db3-aa1a843b8fd5 | -4.36117 | -43.39536 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 534773c0-43ad-3c21-adb4-a08821259396 | -4.67286 | -49.33592 | 2025-10-16 04:38:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 20f1beac-6097-399c-b552-63bc132a3b69 | -6.18654 | -44.29765 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8042219c-3b8c-3194-8b48-f0a8a39bb4aa | -6.9454 | -47.73787 | 2025-10-16 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb1f76e1-110e-38ee-9a01-ee55ad84bf5f | -7.35133 | -43.86099 | 2025-10-16 04:38:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ffc3b1cd-7df1-3e96-910b-f0f7eabe820f | -2.87881 | -50.72334 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e795eb33-9019-3a76-997f-f1ace3858e1d | -5.86853 | -43.88083 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0322ca2e-1443-3edb-afc7-b1a9aea60c1e | -5.87918 | -43.89429 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e27a71b-b508-3508-8689-2ebd128d1176 | -7.5808 | -42.69313 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 300314fd-dbad-328d-a372-91f421d03db6 | -2.70617 | -49.86744 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2a7729d-9a64-3214-b823-9a1d289ceb5d | -3.07623 | -49.50827 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b4bc8b5-5668-3ef7-9f83-36c883632208 | -7.75619 | -42.47273 | 2025-10-16 04:38:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3328bf6a-0312-3add-baf4-cc1a047bb4ee | -6.2195 | -46.41861 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d6a5145-7ae5-320a-b38c-f3df0ec4e004 | -3.52856 | -50.3062 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1a3a5fc-4ab0-3e26-a376-ba021a645593 | -4.83266 | -45.65339 | 2025-10-16 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 730138f2-1563-36e6-8a8c-319ec31c4461 | -3.42523 | -50.24973 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 647fc9fc-dbbf-39ee-a767-885e28850511 | -4.67229 | -44.1056 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 5ba7458d-99b4-3998-b491-ef038ddf685f | -6.32372 | -46.32505 | 2025-10-16 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4351d3ad-ceb2-3364-9a00-f44937c16efb | -7.03536 | -42.73532 | 2025-10-16 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 75495154-25d5-3876-8d34-22a5dea43af7 | -6.32472 | -44.31903 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c44dee2-76d9-3c07-bfcb-925498adf76e | -7.47883 | -42.7536 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 11786db3-d7a2-3e24-bd62-8e4863798409 | -6.54953 | -43.92489 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9831e94d-249f-3d23-ae1c-6e6732553643 | -4.80784 | -43.2075 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8c6798cc-534c-3257-9210-aa53dd132236 | -4.95896 | -45.10074 | 2025-10-16 04:38:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34d1bbb9-99b0-3de9-b416-9a77c1f3f6a0 | -4.11517 | -48.02412 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 81df848d-033c-3b33-91c3-b5cd21c691a7 | -5.86028 | -43.87958 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4f6f965-c1b4-3f55-a69d-2384e84f5534 | -3.59384 | -48.87733 | 2025-10-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 56c82ad5-96d8-3766-87c9-cbdb5243ca63 | -6.75081 | -44.3664 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a59c3666-19ff-3cef-839d-285b8b44ce8b | -3.48357 | -53.45134 | 2025-10-16 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19b411e6-0f75-34a6-9f3d-f0d4a494222a | -8.27102 | -43.36346 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6473ad37-dcbe-3e84-9335-481c69aaf875 | -6.06777 | -41.91333 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 948923c0-a20c-336e-aefe-82adce20e07f | -5.97006 | -42.8794 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 159ffac0-221c-3d4f-a7fd-ab5d0c92b08d | -5.051 | -44.46792 | 2025-10-16 04:38:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39cda948-582a-3754-a8b6-c719a4cd14dd | -4.42193 | -40.17166 | 2025-10-16 04:38:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 22926360-d451-3191-8d5f-5b1adef7b440 | -4.09857 | -48.02158 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01de1007-b8b1-3b1d-a820-34afe3e2e610 | -6.19558 | -44.34883 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7fec7fe-4f49-38e6-bcc3-85a6b172c0ca | -4.65685 | -44.09968 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ff12614-d4ce-3f14-93e9-f08cf5f335a7 | -8.2857 | -43.38794 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d47db258-7a40-3916-b2f5-6f31a319a388 | -5.3026 | -49.57317 | 2025-10-16 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68da3cf5-8790-328d-ae54-67fc0b35cb4b | -7.11577 | -44.72311 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0cc4cde3-e1fa-33da-b6cb-7eb5d080ab66 | -4.78031 | -49.23716 | 2025-10-16 04:38:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c37260ea-1d87-39b4-9c73-78b317797873 | -2.26662 | -47.85624 | 2025-10-16 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ef49b7a2-9a3d-39f0-ab18-f826130a1a33 | -6.56918 | -42.9711 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8adefba8-beff-39a2-98c9-b598297dacfc | -6.99438 | -42.79517 | 2025-10-16 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4bc0214e-1c36-3799-ae81-ca9cdc000f51 | -5.64236 | -45.97129 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad35c55b-571a-32a6-adb1-fed41b8f70a9 | -3.67034 | -50.27354 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28f2c2a3-35ea-3bce-9e44-1416e84f16fa | -5.45169 | -41.02683 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 71268d0b-c851-3b42-b147-2f6850c3a8c8 | -8.24894 | -44.14074 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 506849d0-313d-3031-91e8-07886d47a7a0 | -8.25545 | -44.10109 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caefc7b6-ff09-3f85-9cd3-7d6e4cbc1182 | -7.47756 | -42.76287 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 39eff4d9-836e-3f80-a834-31b2db69677c | -4.00112 | -43.27765 | 2025-10-16 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0a5f4a4-bf9b-3cc4-962b-858f4077abd4 | -5.94283 | -46.71827 | 2025-10-16 04:38:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| da34338e-e4ae-3a74-a3a2-df05897e7246 | -5.89886 | -44.26958 | 2025-10-16 04:38:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccbf9d7a-90a1-33ef-80b8-7179410b0ec5 | -4.28357 | -48.62408 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b12c7acb-0755-306c-b10f-c3f6956d1e0e | -3.56539 | -50.11786 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bc41852-fc52-3c3a-ab60-f1b6bac600ad | -5.30314 | -49.56973 | 2025-10-16 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2eb3160d-227b-376c-a37f-479f50bca6d4 | -4.66483 | -44.10093 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 307412ff-6087-3d84-81f6-9822cb8ebfbb | -3.5601 | -53.10094 | 2025-10-16 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 473af641-9f16-3906-ba40-864aeea9a560 | -3.88292 | -52.23518 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f51551a-8523-30d0-bc16-3065aeb992d7 | -7.47798 | -42.75544 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 4e5eadf0-8505-3089-b712-c5736846a040 | -7.16939 | -42.52076 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1058ee5b-f81d-36f8-8059-3101e5ae5007 | -7.92714 | -44.1317 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 04200870-b1b3-3c33-9e13-4f818856daf2 | -4.81675 | -46.83765 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc15ed92-0dfd-3196-b65d-9f74aa511691 | -8.2544 | -44.07363 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 997680e2-91d8-3e42-b7fa-1b67be768802 | -8.24882 | -44.0527 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2123558-e8cd-3af6-93fe-02d42ce9bebf | -7.9355 | -44.13295 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d31050c8-2765-3387-9511-9e99e646170f | -5.48355 | -47.1361 | 2025-10-16 04:38:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc79c712-03ad-3671-a2d1-95754c262c25 | -7.96004 | -44.14049 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1306636-f5c2-36b9-bd6c-0cc93a293030 | -8.26719 | -43.35844 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 369a88cb-2882-3317-b110-6351db16e5f4 | -5.24764 | -41.02631 | 2025-10-16 04:38:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ffbf8ac1-c572-3332-886e-fab3a3b19e91 | -7.96478 | -44.13718 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2565a024-500b-31f4-8bef-41ba445ab4c4 | -6.26012 | -42.89398 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4ac6bce-8f1b-3033-9364-8b008f66bc9b | -3.52799 | -50.3098 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ece2b20-563c-3664-aad6-a0c45697409f | -6.15491 | -40.90497 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e7488943-1ac2-3279-b4ea-80296504e906 | -2.98638 | -51.19653 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea6b17a1-f92f-3643-aa88-e066cc7b9952 | -6.56988 | -42.95961 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72fb852d-a1bd-377a-b469-9c7ec34819a4 | -5.45628 | -41.03028 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e2a3c410-70c0-39d4-b636-691c7e2678d5 | -5.65875 | -49.25607 | 2025-10-16 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fd00907-1373-3daf-81c6-ad9bcfc60d68 | -5.07593 | -49.60781 | 2025-10-16 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d63d6182-db72-32a9-a566-2162d0e59002 | -8.24939 | -44.04875 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48497339-bd57-3cf4-82f7-ad5c191b22c6 | -5.13652 | -49.63141 | 2025-10-16 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77176394-a793-39c2-a274-d0cd9c102b9b | -7.97062 | -44.12609 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d70afc49-6fa1-3372-bf41-ab5df8e67a23 | -3.49156 | -50.09181 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2576249-3f62-3b3e-a75e-21b2809442ba | -7.89584 | -42.95634 | 2025-10-16 04:38:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f179a27d-b45b-3c3c-b6c5-8e3ad28820b2 | -7.11146 | -42.03801 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5ec4dc1e-6a1b-3335-b82e-cc55307794f4 | -4.92672 | -45.89509 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77f3b7e2-e8b7-3544-bc0b-7dd984ef723d | -7.20921 | -45.49227 | 2025-10-16 04:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33241653-df92-3d6f-a33d-c3c98970e0d8 | -6.03727 | -44.31546 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2dd323b9-6f6d-384c-96da-1c2e2acd401c | -5.09846 | -44.94558 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2190badc-7774-3f05-8054-7e1ff01787f8 | -5.6045 | -47.49405 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a52bbeb7-70b3-3f23-8acf-9dbc7fcc243e | -5.32663 | -44.83604 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51c33b5f-2d1d-3d7e-8764-77e25b4380ec | -7.39332 | -44.75082 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5c32e0be-0516-329b-90b6-8c3ba6ed7700 | -4.42228 | -47.75574 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d589a31-643b-3a19-8bb0-b95551af1d6f | -3.99744 | -48.34283 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ba506d9-c4fd-3262-a9f3-e36f35b84876 | -2.38137 | -47.70746 | 2025-10-16 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8bc32c9-9f47-31cd-b7f9-1e12429aafbd | -6.13323 | -41.7571 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |


[Clique aqui para ver as próximas entradas](README44.md)
