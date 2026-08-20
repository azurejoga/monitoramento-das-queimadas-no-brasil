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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c16a977e-fea8-3062-9b63-4886bddcacdc | -6.70562 | -59.09798 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 80ba16fb-e4fe-3b6f-a8a8-082a4a26b650 | -6.08725 | -57.90989 | 2026-08-20 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1a90fb48-abd2-37f1-a682-eb13916e6240 | -6.08884 | -57.92115 | 2026-08-20 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cbbfdd19-92d7-3271-aebd-c4ebf0d38b9a | -6.9259 | -59.35408 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 6f37b976-c61e-3b73-8177-cc986022823b | -9.42029 | -60.44307 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 7f1098a3-1754-3697-8373-8f2209b6cf0d | -1.83651 | -54.4978 | 2026-08-20 00:50:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 2fd36516-7066-3ffd-9b6a-a08fad8dfaef | -6.76801 | -59.15105 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ad74eb23-0a09-37ed-bbd3-483bfe5c817d | -9.06109 | -60.44646 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a55530ba-215b-3da3-b451-a86df3ac162c | -7.55364 | -55.55782 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| fa238ad0-2e10-3e59-a881-fca26c618337 | -6.60358 | -58.96052 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6357ff7a-a135-3581-812b-8f5bff7fe664 | -8.57928 | -54.75686 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| c5f00e6f-ef56-3d9c-aea1-c1158c768b25 | -11.83282 | -58.84091 | 2026-08-20 00:50:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 34c14452-aba9-39d8-a586-65125c3d0017 | -6.6873 | -59.10072 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 5d8fd420-fd3c-3cb8-9537-32abbcd1cd67 | -8.6691 | -54.66368 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 4a7ca0ba-6424-3b32-9c11-3e301aa854ef | -9.41663 | -60.41646 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d8fd83ca-c384-31c7-99c9-bdbf2be9d025 | -4.78997 | -62.92163 | 2026-08-20 00:50:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3c8cdc47-df6f-393e-955c-362ccb69350a | -8.65787 | -54.59241 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| c3ee6919-6a14-3abd-9a00-d2e7f2d20959 | -10.45806 | -54.67719 | 2026-08-20 00:50:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 2749c04c-2060-3305-92eb-41515eaa89a5 | -6.58649 | -58.97298 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 7497bd48-cf38-3571-9a44-eaf3b928a292 | -6.88943 | -56.43967 | 2026-08-20 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 803b5897-eaf8-354c-8e0c-587bae81d7c5 | -9.4127 | -60.45319 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d8c9806e-d91b-39f9-8434-ab93dd73f0dc | -5.79481 | -55.73191 | 2026-08-20 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| d23ac8ee-2cea-31d4-8d0d-5d2a5ed1d40f | -5.78992 | -55.69959 | 2026-08-20 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e9c16ef3-e56f-34ee-90c8-f2b336333659 | -8.89924 | -60.54485 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 87d92ad5-654e-3152-bbf1-98de0aa74310 | -6.43526 | -52.75652 | 2026-08-20 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 308c3b49-ff88-31e1-b3ad-c9911815316f | -11.21926 | -55.05203 | 2026-08-20 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 1e787dc3-e552-31cd-b534-5c07914f17f2 | -7.05047 | -59.8456 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cdb81294-4561-37ce-8874-5dda44035157 | -9.22177 | -60.81537 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 040066b3-9ec3-307f-9216-1575c41cf16c | -5.49595 | -60.13504 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 313341bf-2358-34e1-8fc6-7437da77d2b9 | -6.59572 | -58.97161 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 7d65a2a0-9461-3bf6-b564-718f2aa7bc21 | -10.33195 | -57.57439 | 2026-08-20 00:50:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 48e4fe7f-33c1-30bf-981d-5ca54e2c621b | -6.83516 | -56.44801 | 2026-08-20 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b8b8c962-af52-3988-8572-ea13aae2f0a8 | -7.78912 | -61.18758 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d661f104-63d3-33ea-bf0e-11a303c55db6 | -7.77667 | -61.16216 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7cd8b1ea-788f-3fc4-9043-0845377da0ab | -11.2061 | -54.00154 | 2026-08-20 00:50:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| c664f022-e4d1-30ed-aa14-52b1f8bb596a | -8.50124 | -54.88761 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| a0c4903a-2ef5-38a5-a97e-211155958170 | -11.19679 | -54.0218 | 2026-08-20 00:50:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 5af72faa-5bdc-3377-9385-bc284198eef4 | -7.34148 | -55.68287 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 9e393ffd-251d-3cc6-9d06-bf0ad9796d44 | -6.70093 | -58.93052 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4a3657ea-baac-3135-8d5a-5225ea96d1a6 | -9.11047 | -60.34911 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 71bb4c8c-4acb-3cac-b99f-7292c36e2bec | -6.92459 | -59.34468 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 11b3d751-ad15-3eda-b22a-385cd22be6ac | -5.99944 | -57.87143 | 2026-08-20 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1f5838da-6936-3fbd-9724-7eef756e33e5 | -10.32087 | -57.56524 | 2026-08-20 00:50:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 70317567-e843-30aa-890a-350725a0baee | -7.77425 | -61.14439 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f93ee861-4f63-33ce-a2c9-e2b101058c65 | -6.69646 | -59.09934 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| bdf1c42b-98c9-3fd1-8a07-8b72419da88f | -6.71343 | -59.08694 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 06c2934b-d5a8-31e4-bfb5-369dad3d54e1 | -7.86659 | -63.77012 | 2026-08-20 00:50:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dce9dd0c-82b5-3074-aced-5075b76e7cdf | -6.79208 | -59.58456 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.3 |
| cce0dbd0-39f5-341e-992e-e03adb3f6d50 | -9.39815 | -60.56062 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b416873f-2256-3597-8a66-8e6aedd9d0ce | -11.81817 | -56.60275 | 2026-08-20 00:50:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3811b2cf-7b09-3f71-9d32-99ccb3323f7e | -6.58002 | -58.99378 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 78dab753-a6c7-3e9e-8a9e-fa4f9135f0a9 | -11.20876 | -55.0595 | 2026-08-20 00:50:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 8f7083b3-b04c-3dd3-8495-f75a6cce0132 | -6.38467 | -54.93756 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 4d321d56-ac69-36b9-bebc-db9d8b683285 | -9.20581 | -59.7701 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 21310fae-0144-31d2-8287-3d395c197071 | -6.81075 | -59.00158 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 90fd2a7e-5486-3350-9e16-188e98d5739a | -7.00564 | -59.59167 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1e8f1c8-0b5f-3da4-89bb-24acf7bf598f | -11.22397 | -55.08188 | 2026-08-20 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ffcedd30-95a3-3c17-8c4f-7b2ce6f6a560 | -9.39421 | -60.59739 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| dfaea038-2580-379d-8b35-1ddab1b13767 | -6.74243 | -59.03708 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7f23aa8d-3d8c-3eac-9f0c-f737719dfce0 | -11.22163 | -55.06706 | 2026-08-20 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 8dbb93cb-8f9b-3086-89db-6d70b643c322 | -8.57328 | -54.67257 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 16e6579b-49d0-336d-95d9-523ef8ef96ae | -9.38813 | -60.55299 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 324dff9c-fa1e-393a-994d-2351e86b07f3 | -6.74381 | -59.04673 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2c2c3621-d11a-33ea-969e-3906b7209323 | -3.2172 | -61.26474 | 2026-08-20 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d3ad66cd-4b3a-3345-bf34-c8a5e937e0ca | -6.80077 | -59.57706 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3d5e12da-7c22-3ee2-a8b4-fa23d8a531c9 | -6.43962 | -52.78377 | 2026-08-20 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| eb4b09d8-7dda-3a43-a80f-02584eea1f3e | -7.533 | -55.57697 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 9c414036-a24e-3bb1-b25d-8d6b576a5d93 | -9.1297 | -51.16081 | 2026-08-20 00:50:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| b90a6256-ae9a-3259-ab73-bb3491dffe6a | -8.56533 | -55.31582 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 234806ca-a844-33f2-a495-1631c2bf730c | -7.8285 | -61.61141 | 2026-08-20 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 590d1c60-ef85-3ef7-a834-61e3d5e74931 | -9.2157 | -60.77085 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b044426e-e626-3a6a-81c2-6526ce6bf298 | -9.41907 | -60.4342 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 196.4 |
| 4d9599d8-a813-35dc-b7b1-1c2fdfc9ebd1 | -6.86219 | -59.0335 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 231a0cd6-869d-3e28-a53d-c9f0e347612d | -11.19393 | -54.00368 | 2026-08-20 00:50:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 162.2 |
| d19d10fb-522a-357c-9807-e9cbaa8b8d8a | -8.16235 | -55.0006 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 4c842a15-f53f-3222-bf45-755ad72f677b | -11.2125 | -54.01323 | 2026-08-20 00:50:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 471eefb3-28bb-3833-9543-bb094c9e3da2 | -6.65703 | -59.08532 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4fad9cb8-2414-39b3-8206-726ad26ad6fb | -3.10903 | -61.21451 | 2026-08-20 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fdb70782-a36c-398a-a18c-5b1160b3b7aa | -8.40689 | -62.69311 | 2026-08-20 00:50:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2c2fe6c6-0bb8-39b5-93ac-9f8018f2bf0a | -6.38752 | -54.95587 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 4da247f6-3497-3b60-8ca3-bb87387bc283 | -9.42787 | -60.43294 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d4807803-863d-3392-8f95-3384311dcdfa | -6.58512 | -58.96325 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 018ddcb2-4828-3f4d-853f-0c00dcf6f82a | -11.20807 | -55.05393 | 2026-08-20 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| feddff76-5c22-37c4-9020-36867eda7e60 | -8.95324 | -60.54618 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c8735a7-11f3-337c-b15a-dc31c2141186 | -9.42543 | -60.4152 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 310c3387-ae7e-3c4f-b75a-395e5d367f10 | -8.48672 | -54.87246 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 2d56e809-2ec5-3118-b94d-8d8e903e0714 | -11.21043 | -55.06883 | 2026-08-20 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 432eea2f-90cf-3065-84e4-6f2fb99b3719 | -6.9004 | -55.73453 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2f885ee3-b365-3bd6-9222-f28ddf5988af | -9.23779 | -60.39091 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 47e12ee1-237e-3dec-83f2-50c4af81e209 | -9.38935 | -60.56187 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5f0735d6-da36-3cbf-9fef-67139998b251 | -6.38231 | -54.9437 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c46753b1-a06b-3bce-bc68-0316771899b0 | -8.66238 | -54.65298 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| a50ea11a-367c-334a-a23b-0558f0ca6a09 | -6.91685 | -59.35538 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| e910154d-6b8c-3c27-a8bd-988defe4b0af | -6.10214 | -57.86722 | 2026-08-20 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5a41190c-11ba-3c13-93db-744137df63fc | -6.79336 | -59.59378 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f08f0503-ba9f-3697-a3f2-65c49684f76d | -6.58786 | -58.9827 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 19cd8a98-49e6-3401-a332-96972505a160 | -9.17748 | -60.83706 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75031843-8e88-364d-a9bd-b5108ce2332d | -7.88996 | -61.18568 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fd41219c-43d2-3263-8a78-2ff10e2db99e | -11.18463 | -54.02389 | 2026-08-20 00:50:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b1eae07a-bba9-3255-a47a-a2fc35512d77 | -7.56513 | -55.55588 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |


[Clique aqui para ver as próximas entradas](README11.md)
