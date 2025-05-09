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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20b352b5-de18-3309-bd15-a7662f2f6b80 | -8.08193 | -43.13047 | 2025-05-09 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| eedeb548-ace7-3275-bed8-ec52979d2d9e | -3.5888 | -48.94077 | 2025-05-09 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a899da04-a565-30aa-a784-2a6ee52fe1e8 | -3.46747 | -49.17552 | 2025-05-09 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d98a5154-1878-301b-80bd-1caecad5caa3 | -7.08364 | -44.37642 | 2025-05-09 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af3711ea-0492-3a04-9efd-64539038cab1 | -8.17466 | -46.71244 | 2025-05-09 04:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa81effd-04c1-33cb-acd3-36c8020e01ef | -8.07869 | -43.1208 | 2025-05-09 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.9 |
| 493c4767-9d8f-3049-9ce4-90daea65ef45 | -3.58827 | -48.9442 | 2025-05-09 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca9ec99c-e7a6-341a-92ba-6cc2e9f4b88c | -5.16435 | -45.10142 | 2025-05-09 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 66126278-e430-35e7-b4ad-f11fa7ce68cf | -8.07 | -43.1216 | 2025-05-09 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 72ecce15-1d57-3532-b898-b2c27fc72660 | -10.23271 | -59.24081 | 2025-05-09 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 334ef8f5-1c54-355d-9b3f-b1b9839bf5dd | -14.20815 | -45.47009 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63ccb589-a13c-3605-bf0b-2b70b414dffb | -12.33581 | -55.1629 | 2025-05-09 04:40:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 248d1297-9ecd-3333-ac56-ca989a3321c4 | -12.63457 | -54.07013 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26671df9-89df-33f6-b2eb-d40f2b8cc2fc | -13.04482 | -53.72407 | 2025-05-09 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4d3b820-10d4-3fea-9d8f-c1f90202d256 | -12.64682 | -54.06345 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb230af0-f4c2-37ec-be39-0e85ae81efbe | -12.59118 | -48.33708 | 2025-05-09 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 418c555b-3057-38b6-8312-1ba74a44eb0c | -12.64321 | -54.06283 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ed73fcd-2783-375b-897d-741c795affd7 | -13.80674 | -52.2449 | 2025-05-09 04:40:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b0ad521-a3ea-39b5-aa83-e729a654cbb8 | -12.6425 | -54.06709 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec3ba866-f17a-3753-908b-37d875749aac | -14.22437 | -45.47646 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fd6b1dc-8857-30c8-8399-1b76d5140002 | -10.55257 | -42.4243 | 2025-05-09 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c4389a57-50d3-3f5c-8851-1e995d9e7671 | -11.56423 | -47.86949 | 2025-05-09 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 885910d2-1b8d-3a9f-8de7-56069402cd99 | -14.2003 | -45.46493 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0398d41-640b-36bf-b381-1d9a1751666c | -14.22539 | -45.4686 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed24a0bb-d0d2-3ed1-b6d6-325d7eb8b40c | -10.97761 | -44.44229 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d68dfdfa-b657-3a83-aa11-a0c458ac72b7 | -14.2207 | -45.47193 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93cf849e-f7d1-3dee-872f-f3755f9ccba9 | -10.96961 | -44.43699 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7268919c-2e28-3f85-8926-8a5207f95a26 | -10.66717 | -44.37867 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c7a550e3-b151-3fe6-8953-8dad533c0a8c | -11.07174 | -46.12488 | 2025-05-09 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23656c40-3890-348c-8138-b6ad14eb5d0b | -14.22019 | -45.47586 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c1d7df7-8567-3b00-bbc6-1c690bfa4dd8 | -11.56578 | -47.61237 | 2025-05-09 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d9d3de5-218e-3253-9221-d647a6809250 | -11.66118 | -58.26425 | 2025-05-09 04:40:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 253f3f7e-d622-3bf3-a39a-85e7ff0803e1 | -10.67086 | -44.38347 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ae354940-6d54-37cd-89bb-30ea7f617d90 | -12.36802 | -52.49063 | 2025-05-09 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 065a46d7-4ef4-3dd3-8645-3d0bf633cf41 | -13.61616 | -43.97699 | 2025-05-09 04:40:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7cba1c14-6cb2-314a-bacb-f3326c27c707 | -12.35446 | -52.48835 | 2025-05-09 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcd1c036-ea83-322f-9fb0-620175db9811 | -13.37723 | -54.25635 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a45b8b9b-77c8-3e59-9072-4dead40f02d9 | -11.56775 | -47.87002 | 2025-05-09 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9381e68f-5915-3404-a642-6b42b4b4acce | -10.97333 | -44.44169 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6d26a4b-c226-333f-8944-29b35d2611d3 | -12.92701 | -49.5796 | 2025-05-09 04:40:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef6222fc-86c7-3ed4-9cc9-c28fd3dc501d | -14.22906 | -45.47314 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 145e740e-0f8a-3a2b-8da3-8cd042d79b33 | -14.22121 | -45.46799 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4452f85b-14c5-3559-a4c2-da12cd5c103e | -15.25761 | -47.46939 | 2025-05-09 04:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ebeb0c8-0479-321f-9210-d8a12f969a5b | -13.80732 | -52.24128 | 2025-05-09 04:40:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7abeb5c4-d3a1-3f1f-ae34-1e3254e2f8e0 | -13.04549 | -53.72002 | 2025-05-09 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd6b0709-0dd8-3ae5-9134-cf46f868f050 | -14.64419 | -45.13456 | 2025-05-09 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2139c2fd-7702-33d8-af0c-65ec6bddf1f1 | -10.66561 | -44.38093 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 1145235d-d488-338f-85bc-8a4fce491b51 | -8.90875 | -50.01782 | 2025-05-09 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d63f6d10-01d5-3cc3-8f6f-ed6d8b98694c | -13.05539 | -53.72596 | 2025-05-09 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3f05bcd-0bb2-3961-9a1f-2fe6ee96bd87 | -11.62738 | -54.93985 | 2025-05-09 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6af66c76-c748-3ad9-be33-2ed445db8954 | -15.09423 | -52.849 | 2025-05-09 04:40:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71a5fa23-cee4-3863-af1e-a27057441d6a | -10.4882 | -59.15018 | 2025-05-09 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72c5eadb-db5e-3f42-9287-3ed02937465f | -14.20498 | -45.46162 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6ff0a939-8abe-3481-9fcf-b9672b447813 | -11.38807 | -52.93784 | 2025-05-09 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1c469868-3231-3742-8e3d-db6717a1784e | -14.64044 | -45.12976 | 2025-05-09 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ef9f96c-9bd7-3bdc-8c48-7f23dbb93513 | -10.99174 | -44.45885 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7aa379a8-0721-3c70-b741-48e545725e56 | -10.6666 | -44.3828 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 166e2fe6-144f-3d95-a247-918cb266163a | -14.58698 | -51.42568 | 2025-05-09 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bc7d674-3974-3e4d-938b-7ebd56195d12 | -11.56518 | -47.61647 | 2025-05-09 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f8f6c479-5beb-3758-8384-394aa00dca21 | -11.56934 | -47.61292 | 2025-05-09 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d51ae2c5-7722-309e-9438-5c66a43db001 | -14.21284 | -45.46678 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ecd688e-4a8c-314a-abd9-675dee2e5fc5 | -13.05321 | -53.71723 | 2025-05-09 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3195d4d7-7c01-3239-8c57-b8cab5e05bdf | -12.36124 | -52.48949 | 2025-05-09 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2ed4ccf-40a0-35ec-adf7-88afa6d909a3 | -11.91344 | -54.40171 | 2025-05-09 04:40:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 52a340b3-a43f-35d7-8aec-fba3e9b41653 | -14.22488 | -45.47253 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b7d9af0-0bc9-36aa-8b65-ebce99906207 | -11.19605 | -44.51064 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e69f6c16-8604-3f21-ab46-6508d1431eb8 | -14.64739 | -45.14354 | 2025-05-09 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39f4a155-9e8d-3e4f-a9b3-e8a2df38d270 | -10.66988 | -44.38163 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| dea8d59f-708a-3d83-a9e5-cc84c438487c | -11.77639 | -48.20274 | 2025-05-09 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8de755b-545d-39f1-930c-1dd2eab0cf14 | -11.38393 | -55.11385 | 2025-05-09 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c8acc77-54b0-3e6a-bf0b-e216d3f3eaa1 | -13.37363 | -54.25573 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 370969ab-b500-3cac-b5b5-156cd0045f52 | -13.05254 | -53.72129 | 2025-05-09 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b207050a-378a-31de-9521-24400ca85437 | -13.37651 | -54.26064 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ccf49b0c-382f-365c-b3f6-a9c8c0f4bb25 | -11.39089 | -52.9423 | 2025-05-09 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| dba2c948-b52a-3b10-bba1-9b15bbc84cc8 | -15.25387 | -47.46881 | 2025-05-09 04:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 369308f6-d58b-322b-89f2-01dc68d6d894 | -13.04767 | -53.72876 | 2025-05-09 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 826277c5-ae7e-3383-8dae-73a5e6cb1f43 | -12.37141 | -52.4912 | 2025-05-09 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d38621fb-8d09-3d0b-95f4-163e0a3a4034 | -12.72639 | -54.97393 | 2025-05-09 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d5cc2d4-ccf7-384f-a740-3e7ac6f361c5 | -13.37579 | -54.26493 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 86871eb7-be1a-3193-83f7-86e3ec1bf4ba | -13.8031 | -53.30077 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09abe778-9325-3a62-ba3a-9f9c528684f9 | -13.38011 | -54.26127 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34ca8fa8-4d62-3390-a7bc-2585369be982 | -13.04062 | -53.7275 | 2025-05-09 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 221cdfb1-4d4c-3524-94b9-c404f014c56d | -14.64794 | -45.13936 | 2025-05-09 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1c558a1-57f3-30ed-aec4-2f30dc540cc6 | -11.53408 | -54.36131 | 2025-05-09 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a88e9db-3f0a-3273-857f-7e4fbb1c9971 | -13.62313 | -54.88224 | 2025-05-09 04:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4358f79b-c9a7-34fc-8f86-90cae62ca60d | -13.24782 | -48.40667 | 2025-05-09 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f13a730-f7c3-3148-a086-573ebc68c537 | -15.07812 | -48.94483 | 2025-05-09 04:40:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e2b66fc-3753-336b-a842-3d651ca20b8b | -13.62477 | -54.88366 | 2025-05-09 04:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97d5527f-1c5e-3b9d-941e-880d9fc754dd | -10.97446 | -44.43349 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28964964-8ead-36c4-9547-f4f6a62cd729 | -13.36641 | -54.25452 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b87f79a7-5735-35ec-a95d-7b96b7dba488 | -14.20917 | -45.46223 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 72d31476-4351-3c63-a16b-f7ce7bc6f1d9 | -13.09017 | -52.29295 | 2025-05-09 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 28905518-3904-3bb0-acf3-b74bab202744 | -10.96848 | -44.44519 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f901b9d-07b3-3b15-820a-cd1efece7868 | -14.20866 | -45.46616 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 694aee25-6084-334c-ba0e-9b5b144d8ab1 | -13.45973 | -47.62353 | 2025-05-09 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c91013cf-360f-36d8-82d2-4fecd8bd088f | -12.17104 | -54.23437 | 2025-05-09 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2970ca34-9253-3e35-8d3f-4ffdb6c59a17 | -11.58004 | -47.61454 | 2025-05-09 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 274d5ed1-73cd-396e-8192-2964e72e32c8 | -14.64364 | -45.13874 | 2025-05-09 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1aae4e99-c48f-382a-b576-7503b6e96cef | -9.39356 | -48.61997 | 2025-05-09 04:40:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4858f6a4-88c7-3232-90ef-1fc78fb7a9ac | -12.1747 | -54.23499 | 2025-05-09 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README7.md)
