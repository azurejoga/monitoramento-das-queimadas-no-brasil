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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e9ca1eb-162a-322f-baf7-b075e3a63fda | -10.87801 | -46.34288 | 2026-06-20 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc3bd85b-9b1e-3552-8dff-f0ada4a393c0 | -10.60113 | -44.32077 | 2026-06-20 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b525027-b86f-3880-ad76-12c74e1cfa9f | -10.24941 | -47.35321 | 2026-06-20 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed47530f-dae3-3a72-bd68-8c1d46af29a7 | -9.71929 | -48.88088 | 2026-06-20 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 424f2207-e74d-383d-aa5a-5133f686e792 | -6.37037 | -43.59683 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ac13d6c0-38f7-3373-84c6-a7ff542ab2fc | -11.03421 | -45.07689 | 2026-06-20 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6bbca3e-6ad0-37a3-876e-b6eaf4165136 | -8.64894 | -47.77052 | 2026-06-20 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f5f137e-a35f-3882-8be1-b4ff412757c4 | -6.15279 | -48.49416 | 2026-06-20 04:08:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd7b3f38-c899-37af-94e6-a5f8b8b2cc6d | -9.74891 | -47.87568 | 2026-06-20 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43cf60b8-3931-31cc-999c-8efa4c5c9b38 | -7.13589 | -41.80947 | 2026-06-20 04:08:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c9478a38-2381-3f63-9cf0-cc673ee41792 | -6.65452 | -42.46754 | 2026-06-20 04:08:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0886aba6-2122-3134-96cd-fb8f4e84dbc9 | -6.32569 | -48.41945 | 2026-06-20 04:08:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51b11aaf-2aff-3641-ae75-01ee92f87f5e | -7.29498 | -43.26289 | 2026-06-20 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34d6d022-2780-3aea-8c02-b1ae360c3df4 | -4.35259 | -47.7603 | 2026-06-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3756d681-79a4-3f3a-a8f4-5594d13d6db3 | -7.3666 | -49.85804 | 2026-06-20 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69297a17-c8d8-3201-ba1f-3fc4e557739b | -6.36474 | -43.59234 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 522f8437-572c-3a5a-b9b3-c7b2312ad3e9 | -6.50622 | -42.22119 | 2026-06-20 04:08:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7f4bdb35-661d-3e48-9386-6a29e51a264f | -9.72379 | -48.88155 | 2026-06-20 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d436d9bb-8e51-3ca8-8e76-3fed7617069c | -10.25066 | -47.346 | 2026-06-20 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0c1c150-0489-3549-9723-4f01d1b027c8 | -6.37099 | -43.59305 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9250e78d-d037-34ea-b250-cad0f72134d9 | -9.74959 | -47.87177 | 2026-06-20 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ff46d5b-423f-3d59-a324-0d11666bcbcb | -10.90355 | -46.32823 | 2026-06-20 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b017fa57-60c3-3d12-9f2c-a60665afe452 | -5.81057 | -45.07101 | 2026-06-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac94cee4-84e0-3f07-8e5b-6fb86d222ba7 | -6.37443 | -43.59362 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 83c7e970-4a80-3185-b351-8b0ccba186a9 | -10.56134 | -45.60991 | 2026-06-20 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f7da93c-a180-3dae-a479-5d4138dd8102 | -6.90465 | -42.84547 | 2026-06-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 00b607ae-9b74-31f1-a921-d965e9729ca7 | -8.22794 | -39.82042 | 2026-06-20 04:08:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eb5b6143-83a2-339a-b242-d9e12bf98867 | -5.80497 | -43.78912 | 2026-06-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 33bb0d84-f845-3641-8124-7b973ac7c744 | -6.14817 | -48.49329 | 2026-06-20 04:08:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d5de65c-820d-37f9-8d5f-6f298038a09a | -6.37102 | -43.5973 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5628c19d-12a6-3757-b263-229d58ea2a8b | -6.33015 | -48.42272 | 2026-06-20 04:08:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 965704a1-8089-32bb-b25a-90d2ab729270 | -6.77997 | -46.3291 | 2026-06-20 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7eb27b29-ce16-3823-b3ec-9dd7d90f5647 | -10.60454 | -44.32133 | 2026-06-20 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9761f421-41d1-3d8f-a023-01f074669acf | -7.7223 | -44.56921 | 2026-06-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a224e475-55eb-3976-8315-605ca59b9a41 | -6.3303 | -48.42017 | 2026-06-20 04:08:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff4bdd1c-0b34-362d-9344-a653ad996cd4 | -5.80148 | -43.78856 | 2026-06-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6ad0a613-b98a-3b2a-8450-0a99b35516d1 | -6.36818 | -43.59293 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bc983b2e-7738-3b4d-8a00-7a94580fa849 | -5.8126 | -45.06947 | 2026-06-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb182381-ebbc-3b37-a39f-32ab0721c6c5 | -5.81409 | -45.08362 | 2026-06-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6d504860-00e0-353b-b78b-10760e8f1d60 | -10.45828 | -46.45518 | 2026-06-20 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31faadc9-ecd1-3cf9-80a9-c5dea2eb4a7b | -5.81186 | -45.07396 | 2026-06-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18966f3d-fda6-3fd8-802a-74b4e857685c | -9.61985 | -48.4891 | 2026-06-20 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33fcd1f2-1466-31cc-8c04-a160213681a9 | -8.68704 | -48.30507 | 2026-06-20 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a518f3e-e5d2-3219-8605-77b3daa91f71 | -10.90401 | -44.49086 | 2026-06-20 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cb70f05-cfb4-3cf8-af49-b0b51e60f00b | -6.3607 | -43.59554 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6df4f9b5-146d-3956-a3b2-449e6a72f4fe | -6.99706 | -42.776 | 2026-06-20 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1d545ff1-388c-3da5-989d-4ba099851b19 | -8.65386 | -47.76729 | 2026-06-20 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3dc6d79c-8912-3ee0-8082-ee17480742b4 | -9.71851 | -48.88541 | 2026-06-20 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 622b9131-a784-33d3-b4fb-6fba37b58993 | -5.29077 | -43.95814 | 2026-06-20 04:08:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c909d457-440c-3559-98f1-656398740c52 | -6.39809 | -44.18297 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 14211c0a-f31b-3ae7-b2d3-ef1a51c0f3a9 | -5.61274 | -37.53195 | 2026-06-20 04:08:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6040c582-35f7-37fc-8138-762021b5d62d | -7.66335 | -45.84212 | 2026-06-20 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b4d1a5a-d408-3646-b5a6-e1152e04d874 | -8.65739 | -47.77204 | 2026-06-20 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b3865b0-99f4-3e3c-b369-05678816578d | -6.36758 | -43.59671 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 433f462a-a276-39b0-9848-aca7b7a2ce5a | -6.17409 | -43.35459 | 2026-06-20 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 566838ea-b15e-3372-b309-5a536eade29c | -7.80182 | -46.45682 | 2026-06-20 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e721fca2-169d-376f-a868-a05461273724 | -10.45909 | -46.45033 | 2026-06-20 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4a3ef9a-2a69-31fc-a4fd-5df82680b054 | -10.51929 | -46.50772 | 2026-06-20 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 922fc84c-443f-3319-a417-1cebc4a47d36 | -7.54981 | -43.43081 | 2026-06-20 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47ccbe8d-7150-3212-a8f5-1377754751a9 | -6.36414 | -43.59612 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b843fcb-5514-3e5b-90db-0a9bf50015ec | -8.65317 | -47.77124 | 2026-06-20 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b80de0bb-90f5-3334-98e2-ede54639b703 | -10.60394 | -44.3251 | 2026-06-20 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dcae28a-c023-3b66-80aa-7e7c450355c4 | -6.37381 | -43.59742 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 396f9208-c8db-34b4-97ad-5186eef4957b | -9.01841 | -40.98908 | 2026-06-20 04:08:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 49dc65de-0d74-390a-a57c-70b77a54e43a | -6.40162 | -44.18353 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 03d739e9-2b40-36d0-a733-e544d36499ed | -5.81483 | -45.07912 | 2026-06-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9f088f22-f876-38c0-b8a1-d06ef0f2e5b3 | -4.35184 | -47.76489 | 2026-06-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66b12c26-03ff-30b2-b73f-2efa3a5a9ec5 | -6.78733 | -46.33399 | 2026-06-20 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9c003772-6945-3f56-b480-875bea5949d8 | -6.78336 | -46.33329 | 2026-06-20 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 00ff5293-3620-3ee8-b52a-d2390252c55a | -9.01509 | -40.98856 | 2026-06-20 04:08:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 274f45af-8f10-3e6b-8d6c-a7e4447a85b6 | -7.80577 | -46.45743 | 2026-06-20 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e64fc694-5ff9-33e4-a78d-c687cd0dccac | -4.35639 | -47.76559 | 2026-06-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9d8fe7f-8e88-3efb-bb5e-f0a34e8344ab | -10.24878 | -47.35681 | 2026-06-20 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acc55b6b-6173-3b16-b523-a75bc893fdc2 | -5.81558 | -45.07462 | 2026-06-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2eba4f79-2ead-34d4-9161-a85dc7da76cf | -6.39744 | -44.18696 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8647c5d4-40d5-3710-9e71-f078df40c277 | -7.36611 | -49.86087 | 2026-06-20 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c4f0578-35f0-3c0e-8b1d-5f1a5948a36b | -5.80084 | -43.79245 | 2026-06-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 772db3c2-cf2a-30a7-8f5b-c7d23d0f6918 | -7.25963 | -44.223 | 2026-06-20 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| def74fbd-d8af-3e57-bb96-9393621cfdf2 | -6.99428 | -42.77191 | 2026-06-20 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 810fc495-9642-39d0-b0da-55b16b876710 | -12.5339 | -45.0204 | 2026-06-20 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 76d2efc2-7815-3177-bede-f9cdb2d8da74 | -12.5531 | -45.0174 | 2026-06-20 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 2e9c649e-8ec5-31fa-a743-ae03234449c2 | -13.12 | -53.79101 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab07323b-47cd-3710-b04a-2a7ba9c6dfbe | -13.29951 | -45.21044 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c2d5ac7-ebda-3f2f-90ee-76b54bc7ad5c | -13.29375 | -45.22931 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a1f7abf-111b-3d73-a2a1-cd4d2bfcfa34 | -11.21871 | -46.76446 | 2026-06-20 04:10:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 104ed7f4-27b2-3f72-a451-ab90597ac497 | -19.16765 | -45.58659 | 2026-06-20 04:10:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4f7e109-a57a-3f9f-8ff0-1edac488f6d7 | -12.54068 | -45.01733 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 258f2b0c-cf92-39f9-a9fa-83ae8deede69 | -13.19416 | -50.34936 | 2026-06-20 04:10:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 12834514-465d-36de-90cc-fc5e938cff03 | -13.12087 | -53.78665 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0cdcdac-5e9c-3bc0-bf17-4ead12d2df6a | -12.54476 | -45.01407 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 7f84dd99-7e48-3bfb-89f9-3b8d04961a00 | -13.30101 | -45.22265 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b92e19d-806c-3e51-ade9-e024957608db | -12.75178 | -45.95661 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eee1f32a-ae79-3032-987d-30b378b46c2b | -13.13254 | -53.78877 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e71781a8-573a-3659-8386-4ed3810caa0f | -13.29755 | -45.20601 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a72d9a6b-1cc1-36a3-b444-f424a9a98ee7 | -12.7948 | -44.47486 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b113b7d3-ea83-38ce-b035-b05a1466a6f8 | -12.78684 | -44.48111 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4f5cd79-e483-3194-8745-058abe958137 | -14.85485 | -48.11645 | 2026-06-20 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4390747-96ac-3802-ac1f-f0323b3485fb | -11.83092 | -47.09827 | 2026-06-20 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f4006bc-0702-3024-942f-43d01b3c2708 | -12.15199 | -48.44934 | 2026-06-20 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d510cddc-2e9d-3586-a1b3-18b16b415916 | -14.33587 | -47.51518 | 2026-06-20 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README5.md)
