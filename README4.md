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
| eadaffbd-050c-313d-bd0d-faa918e2cc80 | -5.03013 | -40.62661 | 2026-01-16 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 416c49a7-e3ea-3c9a-9340-904986bfa3f3 | -5.19241 | -44.29073 | 2026-01-16 04:14:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 24cc8ee4-562b-3006-9449-4dbc39ccd3da | -3.05645 | -40.85096 | 2026-01-16 04:14:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e1513d78-d2de-3eb8-b5e6-de922e4f13e1 | -6.98762 | -42.87292 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 64485f1e-1108-31ba-8087-9468bf33f27a | -7.54223 | -45.52676 | 2026-01-16 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54b02554-060c-38bd-8c4f-e88a4b7f0359 | -6.64823 | -43.4314 | 2026-01-16 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5fdbbc6-4c92-3c58-a3a4-fbfe6d78ebd2 | -7.24075 | -43.05856 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 53fb5a27-955a-30d0-92cc-dbb559441aa5 | -6.43519 | -46.77468 | 2026-01-16 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09385329-465f-3c80-8ba2-abf07c6e090b | -5.45928 | -46.16934 | 2026-01-16 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 258b81bc-b0b7-33b3-af55-e3bd9464e870 | -5.17059 | -43.37365 | 2026-01-16 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3d20a26-a5e5-3eb1-bdff-6311bcd0b2e6 | -7.23745 | -43.05804 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 9e19c7ea-aa8c-3265-9d29-b53a4116cfee | -6.89072 | -42.84005 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0977a872-5478-30ed-a5ae-78ae3de4c6f6 | -4.93739 | -43.42847 | 2026-01-16 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2294cb5f-fa49-367d-b7c0-fea997698f43 | -6.24088 | -41.243 | 2026-01-16 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f5c84637-f79c-3344-8c6f-a4b5b06d08d6 | -5.46278 | -45.28545 | 2026-01-16 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45231957-5fab-3542-abaf-781b2e951981 | -5.46069 | -46.17257 | 2026-01-16 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 397019e8-aef3-3ba4-aced-50dad43d50d9 | -5.62721 | -38.64291 | 2026-01-16 04:14:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9dd30f26-3990-32f4-8ee8-87fef9e67def | -5.38211 | -43.1949 | 2026-01-16 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8be43b92-5d9c-3724-9e1d-aded5e73f8b8 | -5.33016 | -40.59703 | 2026-01-16 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 66e45bc4-21ce-39d1-81f4-bc7ee1aec19c | -3.47488 | -43.33561 | 2026-01-16 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c687dbd-71a3-36db-9997-35662b043105 | -6.37658 | -43.81719 | 2026-01-16 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 393a6f58-0f30-30d2-9bdb-c0371813c1db | -5.45862 | -46.17347 | 2026-01-16 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2347460-d776-371c-8a5e-537f427a6a14 | -6.24135 | -41.24228 | 2026-01-16 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 98ea3f18-105e-36ae-92b1-5a794a8630eb | -5.17591 | -37.76112 | 2026-01-16 04:14:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1f1c075a-f9ff-3d2e-80c1-006070a6198d | -3.31436 | -41.86354 | 2026-01-16 04:14:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| be235f72-30b8-3ef3-a8f1-86e66290a897 | -5.62092 | -39.99743 | 2026-01-16 04:14:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d99ea35-42e4-3be2-8824-d13d71348103 | -3.66873 | -39.21525 | 2026-01-16 04:14:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 5acf5b27-4c56-367c-96d6-177e2728260a | -4.21824 | -48.46853 | 2026-01-16 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f178ed7f-35cc-3cd6-b45c-82549450f789 | -4.21404 | -48.46782 | 2026-01-16 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f133f7a-c3cd-3b22-8d12-a882d92976fd | -4.96142 | -38.55991 | 2026-01-16 04:14:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d415d01b-8a41-375e-9233-8ada234948e0 | -5.05909 | -43.92934 | 2026-01-16 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffaa68d4-3e22-3550-947c-81e21132dd39 | -4.21879 | -48.46889 | 2026-01-16 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fffc64f8-62a8-3e15-a69a-4a56ec3acff1 | -6.02354 | -44.54341 | 2026-01-16 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3c16579-b307-35de-bb68-3234fd425097 | -7.23138 | -43.05355 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 807d334c-4d0e-3f82-be78-0a96c438ab94 | -4.21459 | -48.46817 | 2026-01-16 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05bc90ee-c92e-3fef-96e3-1236d3e56096 | -2.89469 | -40.17093 | 2026-01-16 04:14:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| defcfcec-c5a4-3858-8516-dc4f3425e451 | -3.29725 | -42.53814 | 2026-01-16 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bb86af6-8186-39cf-bc3b-4cebf07c27e0 | -2.74456 | -45.58254 | 2026-01-16 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55dbc059-f899-356e-91d9-75c78fbed3e2 | -3.70936 | -41.68689 | 2026-01-16 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 73c425f5-18c2-3a2e-98e9-f295467f02a2 | -5.62334 | -38.6423 | 2026-01-16 04:14:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8f6aa769-d82d-3ff3-9549-7eeabc703337 | -0.08785 | -51.27688 | 2026-01-16 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ca9671c-b044-3c5a-b782-182fd6e58857 | -7.54323 | -37.75131 | 2026-01-16 04:14:00 | NOAA-21 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 04cc741e-0fa9-35a5-8421-47d79c3057dc | -2.61581 | -45.4879 | 2026-01-16 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61577d40-20f5-37ed-9491-5806d9340897 | -4.06899 | -42.91302 | 2026-01-16 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e10acb72-10ec-32cf-a621-20f9bb16ce48 | -5.38157 | -43.19834 | 2026-01-16 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad256341-44a1-3e18-9800-6795449cfbc8 | -5.05631 | -43.92532 | 2026-01-16 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4deb2da-7f48-36a2-928f-4bf412d2f605 | -6.97936 | -40.07785 | 2026-01-16 04:14:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fb317d20-b897-3e56-8344-a47278c982d8 | -6.89018 | -42.84352 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5eeb8e98-e623-3fee-b9c6-90e5ca10ac40 | -5.37827 | -43.19782 | 2026-01-16 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f28f3ee4-5fe9-3923-b6bb-bc90bba74d62 | -1.01657 | -47.11099 | 2026-01-16 04:14:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1d2285d-9439-3532-8108-f71887bebead | -5.2932 | -37.70033 | 2026-01-16 04:14:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 0fba9e6c-1dfc-365a-80ba-b6b398e8e4cc | -5.75579 | -39.79837 | 2026-01-16 04:14:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1c3ba08d-fdd4-3c19-9ea5-4523d98de030 | -5.37881 | -43.19438 | 2026-01-16 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7846ba1d-3839-3ef1-9278-8be7ecdccaca | -5.45932 | -45.28489 | 2026-01-16 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92e49a29-e09b-342f-bbb8-5c398203c438 | -2.6194 | -45.48847 | 2026-01-16 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61f9daec-8dbf-37b4-8972-c03727dfd2a7 | -3.47157 | -43.33511 | 2026-01-16 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 617ead9e-1287-35b0-b121-7925e97c65a5 | -12.20973 | -39.3246 | 2026-01-16 04:16:00 | NOAA-21 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e5969a30-b103-3319-9bf3-18ad2b64494e | -10.3578 | -48.9107 | 2026-01-16 04:16:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ebcb200-5bf1-370a-b5d6-773a8ae244c3 | -13.10597 | -41.02438 | 2026-01-16 04:16:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3b4fdefa-119b-3865-9986-4f503d6625c5 | -10.21746 | -48.30852 | 2026-01-16 04:16:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d7c2851-7677-3234-a78d-c4b4cd2da724 | -13.62118 | -49.19832 | 2026-01-16 04:16:00 | NOAA-21 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5c9b83e-a90d-3704-946f-8b896f3fa492 | -12.65249 | -46.75648 | 2026-01-16 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fb4b3138-3911-35a0-9be6-4f296729dd0c | -12.086 | -43.76572 | 2026-01-16 04:16:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 60eb7387-0580-39fb-97fe-3d0f871cf46e | -14.76741 | -45.92891 | 2026-01-16 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 752e1cbd-1cf1-3812-8ca0-6a66ec35be55 | -12.45132 | -43.62258 | 2026-01-16 04:16:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0547989-bb71-3996-8ed7-e18a8b6056b9 | -7.92317 | -43.3086 | 2026-01-16 04:16:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 777d0e94-bf76-313d-8d60-0ae6ea3c5198 | -12.28054 | -43.54048 | 2026-01-16 04:16:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ea3aa7c-d54b-38b0-9eca-0f9a0df94a8c | -10.79114 | -48.2248 | 2026-01-16 04:16:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae46efd2-9c4f-3267-a04a-0d21d7f90f8f | -14.77347 | -45.9336 | 2026-01-16 04:16:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd9e5650-265e-3431-985d-93e9b72f3163 | -14.77564 | -45.94133 | 2026-01-16 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92b023b5-6223-3398-aede-7f2b40aeba13 | -8.36743 | -41.78854 | 2026-01-16 04:16:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 9f71a8a4-c74f-3631-989b-cb169d117330 | -14.77289 | -45.93719 | 2026-01-16 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8983cd30-1c8c-34f9-9a82-56864d519a00 | -12.65521 | -40.97268 | 2026-01-16 04:16:00 | NOAA-21 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b8bfbc54-8543-346b-83f2-24833da023cd | -10.61646 | -44.63942 | 2026-01-16 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 977d242e-570f-3c13-bd13-cc9fb0fa1ddb | -14.9178 | -46.38832 | 2026-01-16 04:16:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 133ee533-a82e-38c1-acd0-0d10170e4a4f | -7.88867 | -46.75205 | 2026-01-16 04:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 20f090c0-c5cb-3466-ad97-5ec8d7916a3c | -7.99399 | -43.24511 | 2026-01-16 04:16:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cb55e15f-2670-3bbd-a8f9-063a3672ddfc | -15.44922 | -43.1684 | 2026-01-16 04:16:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 537ad020-c431-3ec6-b27a-2769b75ea6b7 | -9.85528 | -41.59222 | 2026-01-16 04:16:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c32de95d-107f-338f-9234-65950cba340e | -14.47666 | -44.33375 | 2026-01-16 04:16:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 154e4b07-343c-31be-8427-2ca017665b8e | -12.6813 | -46.64436 | 2026-01-16 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69ff792e-a850-3bf3-ad96-bbe56a2f8c55 | -9.51919 | -42.99479 | 2026-01-16 04:16:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ec1d337-dde8-343b-9736-1815dfb48d84 | -12.65654 | -46.75327 | 2026-01-16 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| feda224d-9bef-34b7-9a99-655830f6d2e6 | -14.76799 | -45.92532 | 2026-01-16 04:16:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 22cb640d-a988-376a-bc2f-4dba6ab14d35 | -13.32711 | -40.45681 | 2026-01-16 04:16:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7fd95ffa-e4b6-3bd6-8e94-731a61a363c8 | -12.49759 | -46.34766 | 2026-01-16 04:16:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdd023d6-8581-3434-9e32-d115176ee96b | -9.43012 | -35.54942 | 2026-01-16 04:16:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cf6b4a57-a14d-3497-8501-b9823ee3def4 | -12.16279 | -44.34504 | 2026-01-16 04:16:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01a24765-a0d3-3d76-a0f0-c6142adb6890 | -11.13184 | -43.53804 | 2026-01-16 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2383d47-2380-3472-b17c-05d28ddce30c | -12.6581 | -46.76526 | 2026-01-16 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4e3998f5-e58e-3c63-9fb5-10a7e63606ff | -14.75929 | -45.91666 | 2026-01-16 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8faf9d9d-1f1d-3531-9b4f-bf8de05f9676 | -14.48385 | -44.33122 | 2026-01-16 04:16:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02a962c0-9f71-3915-bd6b-84ab65407f9c | -14.75597 | -45.9161 | 2026-01-16 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acf90aa5-9967-3720-9d49-84ace3dce0a3 | -9.432 | -35.54078 | 2026-01-16 04:16:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7a754547-dcf6-30b5-a5fd-f98ac915ea81 | -13.32017 | -50.17056 | 2026-01-16 04:16:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcac7a55-5531-3682-898d-5cbe8bf0486a | -12.41231 | -43.78838 | 2026-01-16 04:16:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dda3dda6-b12f-3d21-8c42-442151e68e70 | -10.78611 | -44.42664 | 2026-01-16 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd6c0168-9d5d-3d0c-a7fe-dfa5bfc9f325 | -15.45266 | -43.16895 | 2026-01-16 04:16:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 85521cdc-ac39-3c80-8b59-e0361276f762 | -12.80325 | -43.4304 | 2026-01-16 04:16:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ebb8217-5bb4-3d92-bea1-e93dccd0a93f | -12.68837 | -44.98535 | 2026-01-16 04:16:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README5.md)
