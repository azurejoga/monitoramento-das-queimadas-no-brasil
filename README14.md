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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d6f09e8-34f6-385a-b219-be857bc7f959 | -7.36811 | -44.15875 | 2025-08-06 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5336360-5864-35b3-a311-b2a1a564d6ae | -7.20834 | -41.84871 | 2025-08-06 04:19:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 03e77406-b954-34fd-bcac-61fd90f59c3e | -8.04154 | -46.34321 | 2025-08-06 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5047ee8-ca38-34ac-95da-777f37913a34 | -7.72466 | -43.91743 | 2025-08-06 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 346f72c6-ff48-36c0-9d86-0d0f6d18f47c | -11.43255 | -45.13553 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 11199fb8-dc72-3f47-ab27-1d1146c31cc1 | -8.00229 | -43.13781 | 2025-08-06 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e891bc40-5a15-33cc-9ece-43cda404f0b2 | -7.20177 | -44.24427 | 2025-08-06 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b199708-1b2f-3d54-bf64-321f03555e72 | -11.49193 | -50.28584 | 2025-08-06 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aff99921-3331-3d55-93d2-7b83a312e272 | -6.40964 | -53.37158 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29ddceb3-9272-328e-b8b5-44c0e626d805 | -8.26071 | -45.074 | 2025-08-06 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a29d037c-5768-3549-93a8-95eaf02b3e38 | -8.52823 | -47.46871 | 2025-08-06 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66216b94-31d1-3858-9b19-7c50ee6f6a8d | -11.7431 | -45.01325 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f340ed3-dce2-3542-a5c7-9500b68ddb17 | -8.87893 | -44.79021 | 2025-08-06 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e8f463bc-e329-341d-aca4-8e3cb5242bf9 | -6.51377 | -47.04068 | 2025-08-06 04:19:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 260c40df-9a54-3901-9824-53d0336f84c2 | -8.0013 | -43.23696 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 678c7930-40c3-3132-92c0-051921227364 | -8.24197 | -45.06392 | 2025-08-06 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53495cb1-84a6-3d38-982a-1f15026d9627 | -7.50107 | -47.18505 | 2025-08-06 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01b707f8-c286-39bd-8f73-9a3a2380d364 | -11.74171 | -47.55717 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 857575b7-dabf-3ee6-b850-83653844eaaa | -8.5128 | -44.74358 | 2025-08-06 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7239b69d-4297-36b6-91c6-dec0ab8147e9 | -11.72901 | -47.52853 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 33f8742a-d2d7-3893-b608-84a7bb14bad1 | -9.18068 | -48.84501 | 2025-08-06 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0007a5f5-7672-32da-9eec-ac279c4cb8aa | -7.1858 | -43.75785 | 2025-08-06 04:19:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f81c8915-0541-3157-b66a-635000d778e6 | -11.64569 | -50.15499 | 2025-08-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d89caca-aa7d-3087-b2ec-06aede48b92e | -10.59629 | -45.25242 | 2025-08-06 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e57f0aa-90cd-318d-b410-3db021fbf994 | -11.84314 | -43.72271 | 2025-08-06 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1591aa2-1913-3ad5-bf52-4f1a9c056039 | -11.909 | -44.95136 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03c42a25-fea5-3603-a057-d6055e63698e | -7.45375 | -45.70716 | 2025-08-06 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38855e7c-bb8a-37b8-afcf-04c4c48658b8 | -6.74689 | -45.30157 | 2025-08-06 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 754c5c22-23cf-30a8-bab6-98fdd0be3b3e | -8.51758 | -43.31821 | 2025-08-06 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a6458bda-d08e-3fe3-9059-8e3bf2fb7660 | -6.67933 | -49.78884 | 2025-08-06 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc649596-b67f-3920-8e99-e8a16f0b389c | -7.33161 | -46.0659 | 2025-08-06 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7da844ef-60bc-35ba-8075-efa778e0d092 | -12.38122 | -47.04287 | 2025-08-06 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 427af5ac-7bff-39c5-b04d-c831c65f6c6f | -6.26206 | -43.06723 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca8e59f4-84df-3397-8d28-3785ac0095a9 | -6.19945 | -43.74697 | 2025-08-06 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a453102-2c49-3c5e-a05b-72c42206659f | -7.52175 | -45.06318 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e078636-5f97-38d7-9675-aa19a45d5913 | -12.89519 | -43.79111 | 2025-08-06 04:19:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5839a04-84ef-3b5d-bd14-a025c0179170 | -8.15347 | -42.39408 | 2025-08-06 04:19:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2c68c979-7547-364d-9773-36c764c47745 | -7.91049 | -45.52663 | 2025-08-06 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c430717-93f4-3a13-a1a5-5d6d7a4cd26d | -8.00074 | -43.24067 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0620c874-f1e4-3bb1-9008-6e7c8647e06a | -4.82012 | -47.31292 | 2025-08-06 04:19:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06cb3a49-06f9-30d9-9d64-5fec81f2c363 | -10.44518 | -44.36194 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13929723-bcdc-39d0-b9cc-2bdcd42f56f9 | -7.27219 | -44.53342 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04c2bcfb-3283-33d7-98ae-896a12d978cf | -7.50452 | -47.18562 | 2025-08-06 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85671990-2086-37d5-a18e-5289fedcd507 | -5.79485 | -46.99924 | 2025-08-06 04:19:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9a8a978-5b2b-37ea-8078-8de3a21f7fcf | -6.70177 | -43.33068 | 2025-08-06 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 955ea5bd-a2ba-38f7-b4de-0833b75571ed | -11.43697 | -45.12899 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84c01e0e-0ae5-3570-9fb7-3d4eb6a5eab7 | -12.75834 | -44.40994 | 2025-08-06 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c7660307-4b1f-3ca7-8cba-44346a3df27c | -8.62757 | -50.01894 | 2025-08-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce79406f-e9d5-35ac-aaa7-cc80292fe821 | -11.75924 | -45.01945 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1670cd12-c4b6-36cf-9022-09be197ab376 | -7.38913 | -45.98456 | 2025-08-06 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 724bcfb5-dd0f-389b-b515-8db9905b9404 | -7.51141 | -47.18673 | 2025-08-06 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7693323-1abb-3a81-a281-236406f89d3b | -6.41936 | -53.3624 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7062a84f-6e43-3dbc-9fe1-e24a831ed116 | -6.99036 | -43.39288 | 2025-08-06 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 597ee612-3b9a-31f8-8f8f-479c0b13e7b3 | -7.67031 | -45.11189 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cd69710-2b32-3514-9eeb-721a5aaad7e5 | -7.14684 | -41.23258 | 2025-08-06 04:19:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 38008b39-8b0f-3500-8121-cb926a9e5907 | -6.54877 | -44.01329 | 2025-08-06 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1ef6f940-d549-3622-8777-340706cbe56b | -11.90461 | -44.97988 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d97a817-ac66-3912-87e5-109591011740 | -7.37143 | -44.15928 | 2025-08-06 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e491e79-f203-3ea5-a79b-dded394eba56 | -7.38442 | -48.16583 | 2025-08-06 04:19:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af078ada-2b60-3234-a585-32fe0ff2b811 | -7.85697 | -43.85393 | 2025-08-06 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 984fefe5-055a-3701-aa5f-3460e13aa710 | -8.52853 | -47.44534 | 2025-08-06 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d389cd75-1157-3f76-bb4d-23d7b4461b22 | -8.31554 | -49.04373 | 2025-08-06 04:19:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ef51339-8438-3df1-a7a3-c540357097dc | -7.21019 | -41.85003 | 2025-08-06 04:19:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 13b490db-88ad-372a-a37a-c13300b70a93 | -7.08615 | -44.35486 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 725898cb-ec8a-34c6-b903-8715ef2e59c4 | -11.758 | -44.96075 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4582afdf-dd41-30af-822b-a8b784eb1872 | -11.43975 | -45.13306 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb92121f-61e5-361a-bf2e-1ded6718a5f2 | -9.20775 | -49.67534 | 2025-08-06 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9811acce-2ae7-3ab8-95f5-312d4f8cd043 | -9.46458 | -46.30759 | 2025-08-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ddef0fd6-f0cd-33d7-9170-1a01f9ec2e8a | -7.70751 | -45.13498 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd8abdf2-45f6-39d1-8c12-74a9257734ba | -8.52508 | -47.44477 | 2025-08-06 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc0416f0-a558-3034-9cf8-2a33e80313ab | -7.83168 | -45.08045 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34188e94-9cf8-31d3-a4d2-91f5a70fa969 | -11.42868 | -45.13852 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f324039-cc55-3c4e-ab03-d5569a98fb5a | -6.25867 | -43.0667 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| defa8da7-bfe6-3e26-8696-1aec77930b4c | -6.67534 | -49.78816 | 2025-08-06 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a470759-3f8a-3ae3-bb8d-ddaf20629f4d | -5.58963 | -51.12873 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e55dbb8-f5ea-3109-97cd-5a01d3a60a6b | -11.432 | -45.13906 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3d6a828e-8f4f-35cc-8ab7-653f8248ecd5 | -9.64873 | -43.84489 | 2025-08-06 04:19:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7cb94d6e-ac43-322e-8980-2d8c6cffc686 | -11.75132 | -44.95964 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbf2bba9-b0e9-3110-b59a-4b35c2b28c30 | -11.49111 | -50.29067 | 2025-08-06 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| daf97db5-e42c-3234-8622-d2e21583a8e4 | -8.01097 | -43.21942 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4c4ca3b4-2a53-31e6-85b3-2ab26192d475 | -7.57492 | -44.89769 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95d12307-d7bb-3ad2-a5a2-77ab212db9ee | -12.54868 | -44.73414 | 2025-08-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27c8779f-5d89-3c26-b61a-871898ed8381 | -8.04985 | -46.35556 | 2025-08-06 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10e1cc33-5f8e-302f-bcf2-3c91429d050c | -11.9029 | -44.96873 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e7606de-eba7-3dab-8856-0406a18a60eb | -10.47714 | -44.37809 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 215c6b19-a23f-3ade-bf31-eb8c39117b7c | -7.83499 | -45.08098 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| beb3f1f4-6ffc-3c66-b204-2e3a21a99c84 | -10.43963 | -44.37578 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 16218b41-6685-3b13-9d48-2b8ed77ae030 | -11.87811 | -48.07825 | 2025-08-06 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e25cc10-45f3-383b-8cb9-21d52ce11a72 | -11.91129 | -44.98095 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1214c9ea-e1d0-342f-8cf0-44054eace340 | -11.18183 | -51.45767 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8eea1635-d18b-3b6f-9b63-717b9533aa13 | -11.73854 | -47.53388 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 558eda88-8f58-3d0f-a7a1-985e9aeb97ec | -8.62364 | -50.01823 | 2025-08-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0e714d4-7587-3888-b77a-b03b0d8b023a | -7.39323 | -44.62714 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad4e9c48-9703-392c-a89f-f8cb3e86aeee | -8.2574 | -45.07347 | 2025-08-06 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be9eb1a7-af3b-32be-b68e-a2435cd5bb02 | -6.09366 | -44.81178 | 2025-08-06 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac66ab66-d712-3240-8984-063ca6d45e29 | -7.37661 | -44.25695 | 2025-08-06 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aed3998f-12aa-3c12-94bc-a031aebe9493 | -11.74584 | -44.9954 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07be59a3-fb90-3e64-acf6-54fd55d8de50 | -7.19899 | -44.24025 | 2025-08-06 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 666b7cfe-d16f-3578-a720-c820aa22dc92 | -7.47637 | -45.04885 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc862921-aca9-31c4-8d2b-d0585dee2abc | -6.54925 | -42.79533 | 2025-08-06 04:19:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README15.md)
