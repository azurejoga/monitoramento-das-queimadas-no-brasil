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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73f14125-6d50-3523-9c5c-aae5e7df6b24 | -8.86214 | -49.895 | 2025-10-27 12:38:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 66d57957-b858-3e5b-87df-47b9ee7fa008 | -8.70043 | -50.80429 | 2025-10-27 12:38:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fdb4281c-b25c-3318-a100-723af98a3242 | -10.32247 | -48.64995 | 2025-10-27 12:38:00 | TERRA_M-T | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| c8ccdc38-85ea-3c37-a371-bb5e150ad456 | -13.31662 | -54.36861 | 2025-10-27 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 1cffd786-f5cc-3314-8324-d3084c6ae778 | -14.64997 | -48.44014 | 2025-10-27 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 04448a20-d0b0-3d67-8f68-4f4b5d30fd7d | -10.38855 | -51.80149 | 2025-10-27 12:38:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2c572a5d-32de-3dc5-b4e8-8ab1957966b3 | -10.32786 | -47.1588 | 2025-10-27 12:38:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| d94a89cd-3c38-3ade-8bee-ae7b4435b025 | -9.14061 | -51.29813 | 2025-10-27 12:38:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 5d3427fe-5018-38ad-b013-9e7111fe776e | -10.30831 | -47.21365 | 2025-10-27 12:38:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| ab56cab7-71c9-38c2-a4c2-351eeb520629 | -11.41565 | -46.11398 | 2025-10-27 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| c1af2a5e-15e7-3c8e-9a05-a855f75c1e82 | -9.47529 | -46.87327 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 456ba2a8-22d0-375e-ad3b-9c1ff2a459ee | -9.24705 | -45.84858 | 2025-10-27 12:38:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 64f7f5ed-0205-3c5c-a280-3117560c34d9 | -9.57045 | -46.95678 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f4451aee-8b67-30a1-9d9b-9b0f84a1665d | -9.56979 | -46.94992 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| f5fd38df-925d-355b-affd-156b14298d8b | -9.21452 | -46.34632 | 2025-10-27 12:38:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e20fb551-f138-3a83-9361-49ad9932ecee | -10.00899 | -47.19008 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| edea1f43-f35c-3b2c-b313-f8ae688d7d5f | -13.2725 | -54.36209 | 2025-10-27 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 6a531c60-61f7-3bfa-82dc-7016ee127be1 | -13.26239 | -54.35445 | 2025-10-27 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b2f86db3-0170-3d4f-a3c5-2f5823fea22b | -11.09402 | -45.74473 | 2025-10-27 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 14af2697-148f-3bd7-85de-bce70f552d51 | -13.3091 | -54.35827 | 2025-10-27 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 40c82115-443d-3ea4-8162-4e97f8694e83 | -11.41313 | -46.0827 | 2025-10-27 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 441.4 |
| 264e2cd7-f021-3aa5-be8c-fe22f6373bec | -10.01141 | -47.17131 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| cec31020-9e83-395f-b18d-2169bcb7a463 | -11.42133 | -46.06424 | 2025-10-27 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 289.8 |
| a9b2fbc7-6ac2-3c24-aeb2-656f817982df | -9.5772 | -46.8923 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 732ae9fe-da85-3ed5-a198-d688871628b5 | -14.22388 | -43.50703 | 2025-10-27 12:38:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 48181250-dbfd-33b7-979f-a8471834d928 | -9.24316 | -45.82029 | 2025-10-27 12:38:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 3c7201ef-d629-3821-b250-d1e66f3347a8 | -9.24032 | -45.84294 | 2025-10-27 12:38:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| caa066fb-e0e9-39cc-bec2-a4963eec191a | -14.24384 | -48.11811 | 2025-10-27 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 159f0419-1056-32f8-b6c8-63ff0f375b92 | -9.85885 | -48.23833 | 2025-10-27 12:38:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 08faa12f-c67f-3e1a-9fe4-f177890d4022 | -13.0483 | -45.86002 | 2025-10-27 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 55a19ea4-6d50-32a8-bbf3-96dc21f25a87 | -10.02582 | -47.17844 | 2025-10-27 12:38:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| b8771685-f800-316a-939e-a4178f75bb21 | -9.99406 | -47.20741 | 2025-10-27 12:38:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 757b9022-8572-30d2-a3c4-8c3039daa288 | -14.63983 | -48.42139 | 2025-10-27 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 892a6b42-0993-3d80-8b7a-d4450bf5611c | -9.99849 | -47.1944 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 424359be-3fda-3793-be06-86b786320d10 | -9.13926 | -51.30787 | 2025-10-27 12:38:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9b4e789c-c34b-3253-8155-2ae74d4deaca | -9.25697 | -45.82191 | 2025-10-27 12:38:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 311853cf-2210-365e-8164-f3d9908269d5 | -10.02351 | -47.19733 | 2025-10-27 12:38:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b44370c8-34f6-3251-b608-5d4678d91598 | -13.31792 | -54.35958 | 2025-10-27 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6bb9c91d-8ca5-3103-b15b-2f352cf10d74 | -9.21196 | -46.36723 | 2025-10-27 12:38:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| fe1318c5-53ce-3afc-91a3-88d4c922f657 | -10.32082 | -47.21544 | 2025-10-27 12:38:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 0a3d6a36-5089-3efb-9290-903747eb78fd | -9.99646 | -47.18873 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 11c64f49-d3d1-3784-8caa-b3e6b6e87dae | -14.2417 | -48.1361 | 2025-10-27 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 71d5b24e-3364-3a1c-9e1d-4f6f52751551 | -13.25847 | -54.38152 | 2025-10-27 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 29851ea4-286c-3cd2-bb1b-8da853b8f17d | -14.40551 | -51.54772 | 2025-10-27 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 94818773-4269-3b2f-85d0-7d5794d9e347 | -10.21281 | -52.66292 | 2025-10-27 12:38:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 03636035-dc93-37aa-8266-69a329a71b34 | -9.56016 | -46.93549 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 2b16afef-7eda-377c-b3b9-d84acb7ec419 | -9.5798 | -46.87944 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 207751a2-4207-3403-a621-3ea6f837b0d5 | -10.36327 | -47.18213 | 2025-10-27 12:38:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 0919856a-b6cd-3e97-84c8-b7e393c7efca | -10.41769 | -45.29741 | 2025-10-27 12:38:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 27b328d4-5e80-3833-b292-60a1dd589106 | -9.47789 | -46.85939 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 0e0a1a0f-5d7e-35aa-933c-0564ec827ddb | -9.53367 | -45.79908 | 2025-10-27 12:38:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 32.8 |
| fe35f1b6-fdcd-379b-8677-db50f2e6f080 | -14.29836 | -44.51976 | 2025-10-27 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 96adbc51-91d2-3a3f-9381-e2b16dfdd1f7 | -11.10031 | -55.56005 | 2025-10-27 12:38:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2a3b2660-e192-3e82-9bfc-b4a3f771b011 | -10.25197 | -47.23863 | 2025-10-27 12:38:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| d9961719-a790-38e1-93d8-7a2e568138b0 | -8.86368 | -49.88353 | 2025-10-27 12:38:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 7a89fa30-101e-3ea8-a075-5362431d6562 | -13.24965 | -54.38021 | 2025-10-27 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| a8c550a7-07d3-362f-b78a-c5f6f48e53cd | -9.24967 | -45.82652 | 2025-10-27 12:38:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 263.4 |
| 56474843-89da-3cf3-8420-f86e44eb48d7 | -10.0133 | -47.17698 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0219ef18-c8be-32d9-b7c7-92e408553f35 | -14.63775 | -48.4392 | 2025-10-27 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b568ac6b-5bee-3db9-a622-b6785d74251c | -11.42968 | -46.11497 | 2025-10-27 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 1e649a16-e575-32de-8049-1f7a9d62b192 | -10.31065 | -47.19471 | 2025-10-27 12:38:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 38e7c389-0266-3214-b881-3e62da92656e | -9.57282 | -46.93714 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| aa264708-2445-318d-ac6e-7a413480fd10 | -11.42408 | -46.10902 | 2025-10-27 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 0e241930-829a-318d-a407-94293b6f3c5b | -9.29738 | -54.5237 | 2025-10-27 12:38:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9e4d2a7d-6f72-3448-8cdc-4c41431d5360 | -14.30504 | -44.52534 | 2025-10-27 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| b8c03fcd-c3ba-3b2f-9571-32364408d71a | -14.82548 | -52.42174 | 2025-10-27 12:38:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d87e39c3-5563-3edb-a684-78d7ac0439bf | -14.22344 | -43.50196 | 2025-10-27 12:38:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 8830ba7d-09b9-3d80-a2ff-ff0e71b80b96 | -9.37257 | -48.89889 | 2025-10-27 12:38:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 568b6264-8b94-395b-935e-d46a0ace8029 | -13.0569 | -45.8599 | 2025-10-27 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| f4f85767-d9c0-3d6c-b068-b3bd8935f709 | -32.40465 | -52.47849 | 2025-10-27 12:44:00 | TERRA_M-T | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 12.8 |
| fa48a9d2-9d73-3683-a445-472ac50adbed | -31.22485 | -53.14148 | 2025-10-27 12:44:00 | TERRA_M-T | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 20.0 |
| f05fe128-230e-3004-a303-ca7c4e331557 | -3.5833 | -43.6108 | 2025-10-27 12:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| b5f8cd3a-3ef3-39a9-af75-e2577526b030 | -13.2972 | -54.3655 | 2025-10-27 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| a3c7c03d-c070-3ed4-a728-2eb66692612c | -4.3877 | -43.3362 | 2025-10-27 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 5c4dd205-be68-3c1b-bac9-c81931025f58 | -13.2972 | -54.3655 | 2025-10-27 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 53d05d85-2200-396f-b1ce-63afa8fa8321 | -13.3163 | -54.3634 | 2025-10-27 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 211.8 |
| 3ef081fe-e4fd-3928-85fe-ee00d985e969 | -13.2589 | -54.3696 | 2025-10-27 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 2ce652a1-927b-3a58-8862-6e281cd9eb39 | -14.781 | -44.9835 | 2025-10-27 13:00:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 460772ec-acb1-3514-bb37-f3c26652f681 | -14.3982 | -51.5443 | 2025-10-27 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| cd60a10a-9323-3cd2-afb5-03e6d588f59d | -3.5833 | -43.6108 | 2025-10-27 13:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| c08e0eb6-cea8-3454-af33-3ce524d12937 | -13.316 | -54.3841 | 2025-10-27 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| f664c962-2d38-3759-b0f3-1b1d452c6aab | -11.9501 | -51.315 | 2025-10-27 13:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4d0241e6-66d8-3cad-a7c8-1804ed1e1e8f | -13.278 | -54.3675 | 2025-10-27 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 134.4 |
| b54ab056-6fb4-320f-aadd-dd147433b71a | -13.0569 | -45.8599 | 2025-10-27 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 0c83e100-44bd-3d0d-96d6-9fbb3a215654 | -4.3879 | -43.3129 | 2025-10-27 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 399ae945-1c5a-3ca1-969a-0ef886b6ee59 | -4.9138 | -42.9998 | 2025-10-27 13:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| f33e56ba-2ef4-328a-a9e6-e1725e1ad752 | -14.7816 | -44.9599 | 2025-10-27 13:10:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 661e995c-b638-3552-9f85-1dc70aa3df2b | -14.6309 | -48.4114 | 2025-10-27 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 94103be6-6d7f-36c7-a670-cc8191f3650f | -2.8971 | -42.8492 | 2025-10-27 13:10:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 20a4324c-86fe-36ba-b9bb-97631b94d7bc | -14.781 | -44.9835 | 2025-10-27 13:10:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 229.7 |
| c783e003-3bf6-3c24-959f-8b72a3fff153 | -3.2796 | -44.6565 | 2025-10-27 13:10:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| d6ae3888-e867-3e0b-80aa-b12a120599bc | -14.6304 | -48.4337 | 2025-10-27 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 112.1 |
| fb481dba-934d-3d0c-bb66-5f8c13ae2838 | -11.9501 | -51.315 | 2025-10-27 13:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 5dcf3318-6d8a-3e09-b41a-eb7f9cf3c3bc | -3.3448 | -42.877 | 2025-10-27 13:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a2fcddcf-ab9d-3c7c-9c48-2c26774914ce | -3.5833 | -43.6108 | 2025-10-27 13:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 6d1d20af-baaa-3c38-b028-a57c35478a9e | -4.8557 | -43.2607 | 2025-10-27 13:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| e9cd0f53-47c2-3d34-9f6f-ceb5bb17b34b | -3.6254 | -42.7699 | 2025-10-27 13:10:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c17d8d1e-3b7c-3d25-9b2f-86ea2f231ab1 | -4.388 | -43.2896 | 2025-10-27 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| f0cfbc81-2ede-300c-9a14-b563141e2ba7 | -4.8744 | -43.2595 | 2025-10-27 13:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| a085c8c5-9c8b-3c54-b736-d91f684988a7 | -3.0146 | -41.709 | 2025-10-27 13:10:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |


[Clique aqui para ver as próximas entradas](README75.md)
