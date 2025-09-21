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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c8c9a8b-5613-30a5-a04c-83e38f68509f | -10.35027 | -45.2316 | 2025-09-21 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3efb67c2-ece6-36ad-9595-7cc2bece65ff | -7.95556 | -43.88272 | 2025-09-21 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f51d0b0c-51ef-3917-bf25-99799d615eeb | -3.69245 | -49.54973 | 2025-09-21 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 999b729a-9ffb-3652-bc5a-3f7b011e726a | -5.51968 | -43.86115 | 2025-09-21 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bf055c86-a1a5-3164-9020-32bbcd053129 | -7.52889 | -43.67503 | 2025-09-21 04:08:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e030115b-f281-3ce2-b072-ee21179c51c2 | -6.84842 | -44.14702 | 2025-09-21 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da0df1f0-1aa4-3f3c-863e-5e50c0552ea9 | -11.27857 | -41.84647 | 2025-09-21 04:08:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e59213f-1afa-37c8-8fb1-da73ede9d197 | -4.79652 | -47.28445 | 2025-09-21 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e7cdfd7-774e-3409-bce4-c0b90bf09cfc | -8.81225 | -43.01971 | 2025-09-21 04:08:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bf9b6f8d-b09c-3b75-b149-50679e64eb6c | -11.77835 | -43.76118 | 2025-09-21 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 326026e6-46f9-3a18-8ed9-651ddd59fd1e | -10.29371 | -46.08684 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 107e09d4-911d-3ecf-b171-25b01b8baee3 | -5.19319 | -45.48629 | 2025-09-21 04:08:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc9ceb21-2d0e-3df1-88fb-91e65893a343 | -11.51515 | -43.61945 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8238da7b-cf92-3773-abd5-e6d21e248ad6 | -5.52122 | -43.86202 | 2025-09-21 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7a4a4e2c-092e-3b26-9aa7-0e83fad5e1c2 | -6.39251 | -44.62913 | 2025-09-21 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54724dfc-c1b6-33e0-ad77-127168a060fc | -3.62796 | -47.52096 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee060340-de43-3638-8b9b-465863ddc6fa | -7.64705 | -46.77751 | 2025-09-21 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec78de29-fb72-3dfe-8395-064312037f68 | -10.28422 | -46.07609 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77c4ae5a-6899-388c-8f63-b70e08480844 | -11.49149 | -43.5756 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c5629627-80b2-3974-a0b6-e49f21b55025 | -7.38634 | -47.04065 | 2025-09-21 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1a88dcbc-4dee-384a-b548-cd7349520358 | -5.5903 | -51.19257 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5954b7f5-1a57-38e1-8d98-2d89a701678c | -5.69184 | -51.75204 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb39101f-07d3-3300-adb0-6597c2b6e084 | -9.77214 | -45.94863 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a0e45d1-8618-3fff-adf3-7cfc99358b64 | -7.83381 | -45.61415 | 2025-09-21 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b93c57d2-16c6-3b1d-a361-efa8f69c91fb | -4.90939 | -43.09235 | 2025-09-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1198e740-7032-342f-b6d7-3b3e734f7126 | -9.65585 | -43.85899 | 2025-09-21 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 81cac990-ab58-3789-b863-429bb9f59760 | -6.48307 | -45.99031 | 2025-09-21 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f327081-4947-3860-a511-337718ea7a74 | -5.74621 | -43.37401 | 2025-09-21 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0abecf13-818b-3d8d-9367-77eb17054d05 | -10.355 | -47.89053 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 46f64338-cf6b-342d-8048-ffd2d14e8a3b | -9.51698 | -43.06175 | 2025-09-21 04:08:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ecacc5af-55ab-3eed-a1cb-ee377338488c | -7.93358 | -44.10561 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33611a1d-dee7-340b-b4fe-5a98fee7f052 | -9.41815 | -44.71915 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa9756ff-446e-3438-8eb3-a404b2f49a80 | -5.47661 | -44.41489 | 2025-09-21 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72cd8fa0-069b-34bd-ba3e-573fc502e3c8 | -5.08935 | -41.13799 | 2025-09-21 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 44e59ce9-66ae-37c9-a653-17a06c350ab7 | -10.4152 | -47.85633 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 604f3393-efda-3d7d-990c-93fc93a5a396 | -10.25458 | -48.08772 | 2025-09-21 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8f70f32-401b-349f-a10f-b3951da374b3 | -5.6295 | -45.94786 | 2025-09-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 769a7ab1-9d3a-375c-8d58-135bab45e9ae | -5.34595 | -45.00917 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0df6dbe7-f734-3719-962e-5c991635f99e | -8.35826 | -46.51776 | 2025-09-21 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d521d0c-182e-3fb8-8c27-993cadec5fee | -3.30964 | -48.71214 | 2025-09-21 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db0632d3-f5a5-3e53-9dbb-36ed679fc368 | -5.43161 | -45.50183 | 2025-09-21 04:08:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8ada418b-babf-381e-97d3-8d7ae6a91f1a | -7.91861 | -44.11095 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf7fd8a7-d2db-385f-bda2-24117a38c0d9 | -7.93984 | -44.11049 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bd333988-3ca0-313f-aba5-e24deb84aa4d | -11.49043 | -43.56092 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5fb65969-f90c-30c0-9e0f-6e080cfd534c | -7.53277 | -45.27427 | 2025-09-21 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b267b55-71eb-3a94-a274-2927cd86a323 | -3.80355 | -47.57792 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67d3e880-8a01-3b4b-920e-7f7d3b67046d | -10.35784 | -47.89844 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 818e6a0f-c6d7-3faa-aeb0-51d6d1e25164 | -7.91579 | -44.10662 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3e4e890-49ff-327f-bb2e-05702092e65a | -5.69113 | -51.75613 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9caa2581-b2ef-34c9-9395-c6cfd1980e5a | -6.36906 | -43.45682 | 2025-09-21 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e04b5b6-6975-3e3b-9fc9-d759c4f8a4c9 | -3.60732 | -47.53581 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04b18e06-d6d2-303d-93d6-6f7aeff35ee5 | -4.97101 | -49.50398 | 2025-09-21 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36f97267-ed23-33fe-9e6a-51004f2df6c9 | -6.24019 | -45.33057 | 2025-09-21 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de6818b0-5dde-3ef9-8742-0f0facf906ac | -11.02242 | -44.65057 | 2025-09-21 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c0b53c9e-4bed-3002-b74f-3b3817320da8 | -11.48874 | -43.57151 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 257fcbfa-c678-3575-80b4-507ee887a780 | -9.01413 | -44.96231 | 2025-09-21 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f23223a8-d28e-3d41-9f95-813d51fc2adc | -10.2784 | -46.06603 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74c5b5ca-2b2b-3492-a5c5-3fe06de37dc1 | -11.02303 | -44.6468 | 2025-09-21 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 13d51144-976d-3949-86eb-999059c23b62 | -11.20753 | -42.19629 | 2025-09-21 04:08:00 | NOAA-21 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| d944c5b6-af3d-3799-ad28-ba5cb64c29fb | -11.47885 | -43.54817 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb66ffb0-d2e4-3f23-bb6b-a776d5dc56fd | -11.51751 | -43.98582 | 2025-09-21 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16702952-4e6c-3431-be75-239e20f6ca9e | -4.41525 | -47.96585 | 2025-09-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94773a2e-bd6a-37ae-acdb-1ed018fd0c6b | -5.69041 | -51.76025 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3a8c376-52af-3bbd-abea-a4fb9241ef74 | -3.3559 | -48.4008 | 2025-09-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d53535e9-5f95-3bfc-913f-11acfc8bbafd | -9.43045 | -44.70941 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 926c7c0b-6d02-3a2d-88da-e65cbf973d16 | -7.93136 | -44.09754 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eef16b2c-06f7-3127-9133-fb06e050383c | -7.95437 | -43.89011 | 2025-09-21 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d277dd98-e915-398b-93fa-a0c3ae827bed | -9.39069 | -46.33755 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f574171e-1443-32be-8137-abc5f2740d31 | -6.31496 | -42.36885 | 2025-09-21 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a40cadaa-53a1-3197-9213-19958ab4b77a | -7.91922 | -44.10718 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3377702a-0b12-3dcd-8bc4-c06ac4e6540a | -4.94409 | -49.92607 | 2025-09-21 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb832737-3b5b-3465-b016-cfec9120da52 | -5.103 | -38.28938 | 2025-09-21 04:08:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| af26b55e-89d9-3d45-bfca-7315225e2851 | -3.20435 | -51.58907 | 2025-09-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41674c7e-218b-33bf-b182-5e5531a936cf | -10.92248 | -44.25258 | 2025-09-21 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6356b692-8a5f-33dc-9d07-e6694800d8ce | -5.34183 | -44.89853 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9da22dcd-b183-3a11-b5e0-243c749ffc1f | -7.44638 | -42.6174 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 00567d32-eb7f-3983-bce0-94a7004a27d5 | -7.71869 | -44.44981 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e277e4e-3edd-33f2-abd0-5302e4d4bc21 | -7.73551 | -44.4565 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a51814e-798c-3fef-8513-afe218a291b7 | -6.94504 | -44.76032 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 14e06a3f-b526-3f51-93df-3a7478b3422a | -7.92449 | -44.09644 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1551c84-913c-3eca-8a1e-37147a29ec4f | -11.23429 | -46.16962 | 2025-09-21 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a272fac5-b317-3e74-a0b6-22c874cf7ba2 | -4.46542 | -44.13791 | 2025-09-21 04:08:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b9b527a8-633e-32b7-bb2c-1c1589a17187 | -5.26337 | -48.91114 | 2025-09-21 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3030e679-f8a1-3182-8923-6044bccc8a10 | -10.41992 | -47.85332 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a3aebe2-80bd-369e-9aa4-6d96a36ff7d7 | -10.34678 | -45.23087 | 2025-09-21 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d497eeb-fb7d-3816-8ab8-9a1c1fc3873c | -10.29511 | -46.12309 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cb82ee4-b8e4-3910-946b-6eb1944cc7cd | -7.09252 | -47.34843 | 2025-09-21 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8e060194-b032-396a-bce2-6eacccc17a65 | -7.00497 | -44.66117 | 2025-09-21 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d408506a-29f7-3ca2-ad48-01a8523a39a7 | -8.35654 | -46.51459 | 2025-09-21 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92a8b468-cd3f-3e41-9b8d-f60782dbae12 | -7.19201 | -43.82313 | 2025-09-21 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b52e33e9-6374-3f96-9241-c85f01eec1f5 | -10.41929 | -47.85695 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7008f5d3-bd9c-351d-92c4-c0d2c2350054 | -7.92671 | -44.10451 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5a6e844d-61b6-31db-a3b9-2f5817f469d2 | -9.42226 | -44.71588 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 844c9c16-7c71-3dca-a5c5-18948351785a | -10.35907 | -47.8913 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55320dfb-c824-37a1-b025-7c2956c8af6e | -3.35675 | -48.39578 | 2025-09-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 459f2305-a6f9-3076-9265-502721012f55 | -3.35953 | -48.40302 | 2025-09-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5cbb6ffe-de19-3466-8795-4258413ccd63 | -5.52665 | -43.86219 | 2025-09-21 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b476c88b-0c11-362e-a20d-24240d959475 | -7.18808 | -42.24791 | 2025-09-21 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2ca66729-b963-3c3e-bf2d-da8d4e6b5ef3 | -6.99375 | -45.6711 | 2025-09-21 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ab1196a-028b-35e0-9bc1-1a841f9bdba3 | -6.50054 | -44.435 | 2025-09-21 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README8.md)
