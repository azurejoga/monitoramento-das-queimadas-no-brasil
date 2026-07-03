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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6220ad11-ac35-3252-9340-142c1a95f709 | -11.4099 | -56.054501 | 2026-07-03 00:56:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1b1253f-c938-3bde-a7a3-c8883116f6d1 | -5.8044 | -45.056499 | 2026-07-03 00:56:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 590170c3-48d9-3208-a31b-09a71ab7aa08 | -5.8067 | -43.8158 | 2026-07-03 00:56:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a0a8073-745d-3a8c-aadb-6a4d69694cdc | -10.9575 | -43.071201 | 2026-07-03 00:56:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 153facfe-bb3f-335b-b29e-28db39253824 | -17.265699 | -42.6525 | 2026-07-03 00:56:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 42076a0e-4e2c-3b91-8547-c6a2578985c7 | -5.8115 | -43.793598 | 2026-07-03 00:56:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3457827-9cfe-3283-97a1-7f926b02b36f | -12.502 | -43.813702 | 2026-07-03 00:56:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98ec1766-13e7-32f5-996f-f471f9dd1576 | -22.5413 | -46.965199 | 2026-07-03 00:56:00 | METOP-C | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 236600bf-804f-324e-a2c8-b6104d087e60 | -12.5077 | -43.7957 | 2026-07-03 00:56:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e4b16650-1989-3b2d-845e-874273ce979d | -20.433201 | -47.5508 | 2026-07-03 00:56:00 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4962b522-916c-38b2-9984-7ed919ed3704 | -11.3464 | -55.418098 | 2026-07-03 00:56:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83fc57c2-202b-39fa-b719-38f2f3270477 | -8.7392 | -48.321899 | 2026-07-03 00:56:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a201ee04-722e-38b5-b509-4c41eef54877 | -4.0181 | -48.067699 | 2026-07-03 00:56:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b82739c7-32ba-3dd9-9490-d8df5682f9c5 | -10.9478 | -43.073799 | 2026-07-03 00:56:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2945ade7-e25e-3b8b-ae76-cfb50392112f | -7.6458 | -50.030102 | 2026-07-03 00:56:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 594f7d5f-3e9f-3253-b18a-b3d8b6e12881 | -12.7428 | -44.5135 | 2026-07-03 00:56:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 100722fd-769e-38c7-8ad1-2945fae65398 | -7.644 | -50.022301 | 2026-07-03 00:56:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37bf3d1f-b095-3b85-bd16-11bae01cc7e8 | -10.9479 | -43.034302 | 2026-07-03 00:56:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bec88f2f-8d0b-3737-81c1-755d6e83dab2 | -5.7907 | -45.0425 | 2026-07-03 00:56:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c145ede-b183-3957-b126-97eb3e312ec7 | -12.7498 | -44.541 | 2026-07-03 00:56:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5c4f7028-c04c-3489-a1a4-8ceb94d078d7 | -21.4949 | -48.538799 | 2026-07-03 00:56:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| db0b6d42-4b61-3cff-a4b9-af8b3aa36cb5 | -5.7964 | -45.0238 | 2026-07-03 00:56:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0f77b88-393b-3647-b6a0-bcad6cbdeca4 | -12.3587 | -47.432701 | 2026-07-03 00:56:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb590237-c6b1-3346-9858-339f94e28954 | -3.4152 | -41.7089 | 2026-07-03 00:56:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ef01034d-a06e-35a9-9f29-d6c87491525b | -4.3459 | -47.756802 | 2026-07-03 00:56:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5034a5d-28fc-3ac3-94ad-1adb111a33a2 | -8.7108 | -54.574501 | 2026-07-03 00:56:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b5c076d-eff6-3389-9165-e6ec4bf61134 | -4.0057 | -48.058998 | 2026-07-03 00:56:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7cc3a77-af1d-3143-ac79-e7e84a4d7272 | -5.785 | -45.061298 | 2026-07-03 00:56:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d08c86bc-ad7d-3996-a2ff-1d45679420ed | -11.7045 | -51.6189 | 2026-07-03 00:56:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 84ac79b2-c7dc-3fb1-b56c-e60f6c2b2e6d | -12.3685 | -47.430302 | 2026-07-03 00:56:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f05fc947-46e5-3bfc-a54e-c83ff9b9b3cd | -12.7525 | -44.511002 | 2026-07-03 00:56:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa2de4b2-f371-33b6-b034-a65ff7e20819 | -21.327999 | -48.853699 | 2026-07-03 00:56:00 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fd15cc1a-4e60-3d36-8bf9-986f80c45b8a | -7.9273 | -48.250401 | 2026-07-03 00:56:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0109d0fe-3c2a-3239-aecf-bb227e4315f0 | -5.8101 | -45.0378 | 2026-07-03 00:56:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1fe857f6-464c-369b-a50a-1badb272cb0f | -11.4119 | -56.064098 | 2026-07-03 00:56:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cefca419-aac0-380e-9143-9eeb948755d7 | -3.5157 | -48.0326 | 2026-07-03 00:56:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eec0ec98-5798-385f-b6ee-4ac8f6e235fa | -9.757 | -47.871498 | 2026-07-03 00:56:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1acdb4a7-00f2-3620-b760-6f5c199d5b0c | -11.7061 | -51.6259 | 2026-07-03 00:56:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0570a3ac-6e6c-30fa-b3e1-2125309ce081 | -17.547001 | -54.009602 | 2026-07-03 00:56:00 | METOP-C | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 69fc2d2f-bcec-3d2b-aeb3-e3bbc79f7b08 | -10.1339 | -52.101002 | 2026-07-03 00:56:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a713289-4848-3280-ac2a-e9d49dda054c | -11.4197 | -56.052399 | 2026-07-03 00:56:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb081480-4932-3110-bab8-046b4de0053b | -10.9382 | -43.0369 | 2026-07-03 00:56:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b78d3247-5f23-3742-a230-3a3b961e0d0e | -5.8004 | -45.040199 | 2026-07-03 00:56:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 184f1976-92a7-3d53-82b8-d4b60a5f8a86 | -8.7316 | -48.333401 | 2026-07-03 00:56:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37a371ea-99ef-3198-8a9c-7cb2353f3e34 | -7.0146 | -45.419201 | 2026-07-03 00:56:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 460ba3c8-7aed-3854-b37e-800dd2c0d791 | -4.8851 | -48.9044 | 2026-07-03 00:56:00 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf8e46ec-b165-357c-974c-53ddcea4cf49 | -10.943 | -43.055401 | 2026-07-03 00:56:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98c8a292-0969-3322-9074-876a4b01776b | -3.4248 | -41.706501 | 2026-07-03 00:56:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 59674348-c399-31fb-adca-615cd02eb935 | -5.8018 | -43.795898 | 2026-07-03 00:56:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 892a771c-e200-3110-9725-988ab8d6c865 | -7.0182 | -45.433899 | 2026-07-03 00:56:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a00065dc-e5c6-330a-ac98-9393ba6c839b | -7.6141 | -49.542599 | 2026-07-03 00:56:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15c46578-9a8a-38cd-98d2-7df07adb7841 | -11.317 | -54.470901 | 2026-07-03 00:56:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a6ea5ea-4b3d-302b-8830-6f40211ff8ac | -21.326401 | -48.846298 | 2026-07-03 00:56:00 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| db076e4a-175f-3068-823e-53bde0d37c19 | -8.7414 | -48.331001 | 2026-07-03 00:56:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d84ad38-4fa2-3d84-8d14-6da09884ea71 | -19.5159 | -52.737099 | 2026-07-03 00:56:00 | METOP-C | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 471e828c-f05b-30a6-9cd3-86b9338ee454 | -8.3825 | -48.211498 | 2026-07-03 00:56:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af21d2ca-4431-3475-87bd-bf92fd21a7a4 | -5.8164 | -43.813499 | 2026-07-03 00:56:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b0f19fc-8280-3d52-98ae-7e0e0b89fba0 | -4.3486 | -47.768101 | 2026-07-03 00:56:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0beae302-79df-323e-9e22-d346b40a95a3 | -8.701 | -54.576698 | 2026-07-03 00:56:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bb82789-98ea-31f7-a398-fdf45f471013 | -6.7267 | -48.104698 | 2026-07-03 00:56:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ce07c1f2-6fd5-39a2-abb6-9d7fd7e17d38 | -5.7947 | -45.058899 | 2026-07-03 00:56:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4cf3a4dc-919e-3f4f-aee3-7f0aac0a6d44 | -22.795099 | -49.345402 | 2026-07-03 00:56:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 02e0347d-e277-3b98-85f6-0baed4cad201 | -12.7463 | -44.527302 | 2026-07-03 00:56:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 941059ca-233a-359a-98e1-a06df55c5efc | -11.3153 | -54.462898 | 2026-07-03 00:56:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e50233c6-704b-3a79-bb96-afe3e20d91f7 | -4.0155 | -48.056801 | 2026-07-03 00:56:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cef80de0-6904-3492-8292-b2a3cdbec99f | -8.387 | -48.230202 | 2026-07-03 00:56:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2dbc8487-90bc-3502-8b64-af55f64b97b1 | -11.3562 | -55.416 | 2026-07-03 00:56:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e347b35-ce41-371a-a7ca-38c353e829d5 | -5.8061 | -45.0214 | 2026-07-03 00:56:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a67790b-2529-3532-bebe-fc1bf03d7811 | -17.548901 | -54.0187 | 2026-07-03 00:56:00 | METOP-C | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 45c423f0-2025-3514-a399-03ee72eb4d37 | -1.7826 | -55.526199 | 2026-07-03 00:56:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd40e117-d992-30ce-83e6-2127accfb38b | -8.7294 | -48.324299 | 2026-07-03 00:56:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1165710-8511-36d0-97dd-5bd7cb6be696 | -10.1324 | -52.094101 | 2026-07-03 00:56:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4382bd3-5f50-37c1-b147-79d73e37ddae | -11.3483 | -55.426998 | 2026-07-03 00:56:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6352cc0d-b50b-32b5-ade9-28d450a94b1d | -9.7593 | -47.880901 | 2026-07-03 00:56:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45dc6290-7c50-32f5-9c80-a4440bbda42c | -10.5877 | -55.415401 | 2026-07-03 00:56:00 | METOP-C | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40aac828-eb5a-3c49-9299-1cef8e4e4506 | -11.8503 | -48.2435 | 2026-07-03 00:56:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a8e3957-e4c6-387a-92ca-856473807ca9 | -11.7077 | -51.632801 | 2026-07-03 00:56:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 24d5a891-63fc-3ba3-a574-00dff029ab46 | -10.9527 | -43.052799 | 2026-07-03 00:56:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f60d986-62b8-3844-9ab6-d0c4e6843799 | -12.498 | -43.798199 | 2026-07-03 00:56:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 69a05842-dee8-3ae9-8bee-6b5c921ad0ba | -6.9287 | -43.704399 | 2026-07-03 00:56:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 817bc64c-9804-3454-8160-68bcb226b87f | -12.756 | -44.5247 | 2026-07-03 00:56:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 54e543d0-a242-3735-a1c2-fad921a29b96 | -5.7987 | -45.075199 | 2026-07-03 00:56:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f69ac1a-fdde-38f1-a73c-79567aafea96 | -6.9238 | -43.7262 | 2026-07-03 00:56:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 23f9c09d-f1aa-36b4-941c-a065b56117d8 | -17.2561 | -42.6553 | 2026-07-03 00:56:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e65484dc-72f8-3407-a246-21546039f4e4 | -11.4217 | -56.062 | 2026-07-03 00:56:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7cf368a-27d7-35d3-9a70-bd3ef1c891b7 | -5.8141 | -45.054199 | 2026-07-03 00:56:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 052ffbc1-01cc-3f03-a9df-baf8e6dcfacd | -11.3543 | -55.407101 | 2026-07-03 00:56:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40086726-5641-3692-b44e-53656cfbe1c4 | -5.8134 | -45.0345 | 2026-07-03 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| a79f133c-be24-326c-8395-2d3c2eb21899 | -5.8058 | -43.7975 | 2026-07-03 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 00b2c6e8-5367-30c1-9f9f-2d50917e442e | -10.9401 | -43.0355 | 2026-07-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 4ac31c94-a8e5-328e-9fad-4ac9c6fa2593 | -21.3321 | -48.8509 | 2026-07-03 01:00:00 | GOES-19 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 1f2f7bb4-38f0-3e92-808f-368b550d357a | -5.7945 | -45.0586 | 2026-07-03 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| ea95379a-5b40-399d-b9c9-145223146597 | -5.7947 | -45.0359 | 2026-07-03 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3cdc5fc3-0465-3773-a761-03f407a6b2f9 | -10.9397 | -43.0593 | 2026-07-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| f346dfcf-a3e0-3cf2-9c72-b94c197638e9 | -12.7553 | -44.5194 | 2026-07-03 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 16de7bf9-f906-37f7-abb6-c5050dbd02a8 | -12.7548 | -44.5428 | 2026-07-03 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| ba84f1b6-2aef-38cb-9bb5-c9668597d039 | -5.8134 | -45.0345 | 2026-07-03 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 944802cf-429e-3d7b-8b2a-d9c53519a07e | -10.9588 | -43.0565 | 2026-07-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| aac53961-7ad7-356e-90f5-ec069f3e940c | -10.9397 | -43.0593 | 2026-07-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 226925d2-8fcb-3bc3-a904-ceb1f1a2cbb2 | -12.7553 | -44.5194 | 2026-07-03 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |


[Clique aqui para ver as próximas entradas](README4.md)
