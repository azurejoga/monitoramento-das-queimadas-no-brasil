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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edc6f7cb-fcc4-307c-8efb-178dfc05e1a8 | -10.91888 | -47.06701 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e53160f9-6ec1-37ed-a074-42d67183da6c | -13.30571 | -48.05175 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 06fb130d-7aba-3c5d-87eb-0bd1d33f9ff9 | -10.16203 | -45.42267 | 2025-10-07 04:57:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbd725dd-27a3-3a0a-8b56-1b4a9e746343 | -8.22815 | -61.17559 | 2025-10-07 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95099586-89a4-3b06-a108-7c5c75c8ad48 | -11.1549 | -47.76009 | 2025-10-07 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e48eb48d-804c-36c2-9e8f-ad3c53b528b9 | -10.37753 | -50.30078 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d38e13aa-8161-33cb-9c81-ec207c22b105 | -12.01554 | -47.78421 | 2025-10-07 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3353e6d-a00f-378f-9221-0164d1a3941f | -11.84758 | -44.92445 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07ff4f71-af09-307f-a43d-1d7b20a53c5a | -11.4033 | -55.08853 | 2025-10-07 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cb7378c-4879-3e86-84ad-72f7138d5f8b | -15.17006 | -52.76446 | 2025-10-07 04:57:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1d0526e-7a77-3e1e-ac5e-4f23051705f1 | -14.55029 | -46.64407 | 2025-10-07 04:57:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0365de8e-feb1-3f26-b640-489766fb6c1a | -8.95319 | -48.75269 | 2025-10-07 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd105fbf-65de-3d70-8a87-989c5c47da4d | -11.12548 | -47.22102 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 559ea4cf-f12f-3402-85e0-db3e0a46524d | -15.5966 | -48.7651 | 2025-10-07 04:57:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14b7f262-297e-312c-89a3-bba2707a27cf | -9.1369 | -50.70055 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66ff5aa9-29bd-39dd-8acc-c96cc581dca8 | -9.40438 | -49.36831 | 2025-10-07 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19c2f81e-1da1-3a90-b465-08af62874cc3 | -10.3233 | -46.93755 | 2025-10-07 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 784b9117-ead0-3cca-a9eb-c2706070e1bc | -10.92913 | -51.15256 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a48ee6ca-11f2-32f0-b6b1-f7781e273c0e | -13.0753 | -47.83134 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 840ddc1d-5ab5-320d-bdf5-894456131d7d | -10.75231 | -50.47916 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3b70d10f-9646-354e-abfa-3d448114e601 | -11.86657 | -56.88965 | 2025-10-07 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| de53f000-d40f-3a1d-a901-932c7d9177df | -13.58886 | -51.8282 | 2025-10-07 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d550942a-76e0-35be-b732-83e84c042208 | -13.09856 | -47.9962 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 188d98c1-140a-366e-ae80-b5feb0a8a06a | -8.61982 | -54.99069 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d5e12f9-8c8a-3e90-bc47-08a79ac3d567 | -11.38316 | -54.34857 | 2025-10-07 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ed38ff53-530d-3cd2-be77-ecb21fe15ae1 | -12.37939 | -51.10672 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54c997fb-39cd-3c35-9688-b5edfab4a033 | -10.37894 | -50.29066 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe7715de-c443-3581-862a-2c35e469004c | -14.76997 | -46.05433 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eaa81b53-27cf-3450-8316-b68292b0e283 | -12.30684 | -55.1081 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d93b4c7d-4d5d-329d-af66-9a0ac7e1657e | -10.39704 | -51.60974 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43a2e89a-6a3b-314c-97d6-9d208c91e7ef | -12.92007 | -54.72343 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 298771eb-11cd-3a66-9786-c44fea7676fd | -10.4304 | -50.32398 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 93680165-f84a-362f-a4fe-9a9efc16f392 | -10.73845 | -50.49241 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03981a24-1b33-3706-b432-7e01b407c96b | -13.25034 | -48.06429 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c659a98-7ae2-3a53-8e8d-5608e5909325 | -13.10502 | -47.98351 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 04e110a0-7c27-3496-9d12-2ceaa2a95680 | -8.22736 | -61.1801 | 2025-10-07 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d72b704f-7833-3772-8854-988a2cced2cd | -8.85989 | -46.08957 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 904c8a45-e49d-3083-92a6-75ae82f8e028 | -15.20811 | -46.37949 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b36040de-ec1b-35d8-bfca-2753862edc55 | -14.92783 | -51.411 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fba9f5b0-d487-3c33-8d7a-8105a1293015 | -11.3826 | -54.35212 | 2025-10-07 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4302a20e-d8e8-30db-91e1-995f328ca4b6 | -11.94746 | -46.43375 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3da710c0-1bde-3754-b466-d2b1a02e4721 | -9.82042 | -62.18905 | 2025-10-07 04:57:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e3f7de4-70a4-3d74-aab7-c4f3ae5f99fd | -14.94506 | -46.81954 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 005ee438-e36b-3a52-9fed-c9807ae95b1a | -13.31802 | -47.77096 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 153d555c-0803-3bcc-9063-c85e20ded763 | -11.15713 | -54.88347 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77cdce81-13a7-34de-ac16-61ee6b447d06 | -9.08919 | -47.95766 | 2025-10-07 04:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d934a37-d226-39da-be96-ad056172b6a1 | -11.8433 | -45.05852 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13b4e1bd-2764-3b53-b263-efa9d2d8510d | -14.90628 | -46.83016 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6642e49c-1d14-3f33-8e50-822066c6605f | -9.08852 | -47.96232 | 2025-10-07 04:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e6fabd4-e2b5-329a-b045-971951ce1e35 | -14.75424 | -46.0444 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23e941b5-d0a1-3f64-b297-6a4628bc0ffd | -9.45612 | -56.65557 | 2025-10-07 04:57:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6d99cfb-b021-31da-bb9c-19baf6e04af4 | -13.22434 | -47.81015 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5ae2b088-af15-3a32-996d-5eedd3194ee5 | -7.42958 | -63.74627 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db9000f7-243a-3b09-91cd-3bf587b5f8ce | -11.03933 | -50.92537 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f6009f77-5ffa-3e58-acae-f69a8cd92753 | -13.71606 | -48.1951 | 2025-10-07 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58049189-2fbe-3ad2-a926-461298be6711 | -10.33001 | -51.23 | 2025-10-07 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 973d6614-9dd8-3bc8-85ba-aca50ec1dadb | -10.55477 | -54.86966 | 2025-10-07 04:57:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5abde8ab-db69-3318-acb3-0208705db62a | -9.38788 | -59.42537 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aaa3d90c-da77-3f8f-a80e-2956d3f9f282 | -11.22752 | -47.76741 | 2025-10-07 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86285618-5f8a-350a-baa5-09230c65d713 | -11.74207 | -54.72469 | 2025-10-07 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff5e94c4-60b3-3480-8658-f79dfa60cfd4 | -9.63075 | -57.02587 | 2025-10-07 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d826bc4a-1aad-3e4f-bc39-1429b431babe | -13.29006 | -48.06073 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3dbe2c1b-da71-368a-a9bb-547ae279f01a | -14.73292 | -46.03381 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1d0df90f-8329-3676-b59b-d7ad02654015 | -8.857 | -62.36753 | 2025-10-07 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c53d3bf4-92b8-397c-ae1b-7ac51242b902 | -11.41985 | -55.06963 | 2025-10-07 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6f89dc5-8894-3297-9c69-50963253840a | -10.42345 | -51.63409 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 554dea02-a612-3bfc-9eaf-41496d42d396 | -14.65293 | -48.37237 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0a4d38a-a094-3494-9bb9-759529858fad | -11.81331 | -45.11652 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 797a1779-f2b7-39d2-9d11-133210a97c27 | -13.24283 | -51.68447 | 2025-10-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00384f84-c574-379e-ba2a-1ce6e4247a38 | -15.38495 | -47.99817 | 2025-10-07 04:57:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 069d11eb-2bc9-3b9d-9a73-b8d22a4921e0 | -14.64422 | -52.52906 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4be1668b-60ca-34d6-b6d6-3f68e0001d43 | -12.99116 | -46.79158 | 2025-10-07 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfd448b4-8a40-37eb-a5e0-469aedd2379b | -11.78021 | -45.12956 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04f76127-db10-30fe-a9d3-27c3f2821707 | -15.21681 | -49.30092 | 2025-10-07 04:57:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4adf3bbf-0d0a-3c3c-82fc-be6811f127f9 | -10.92056 | -47.07678 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c2b7741-0d1c-335e-80b5-914c374055b5 | -9.96601 | -43.78879 | 2025-10-07 04:57:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 975fbca9-51c3-3f40-bc23-4c67eb0e139c | -10.25661 | -44.37127 | 2025-10-07 04:57:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b9d2e88-765f-3d7e-9fb9-7004dec30b65 | -10.93355 | -51.14851 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09035f22-c930-3655-9b93-eae72e2cd515 | -10.99654 | -49.5797 | 2025-10-07 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb3e01de-c0a8-3e3a-b023-ec9ce7a09f38 | -14.90708 | -46.87022 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27517724-d461-38d7-9393-0ebd1d234b86 | -11.50871 | -54.45587 | 2025-10-07 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 538b7b79-0b4c-3da7-a0a2-a7c1698bb2d8 | -10.39149 | -50.2906 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e996b83-601c-31ab-98da-dbd77233710a | -12.30629 | -55.11163 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af0dfa9a-e5c7-31fd-a658-33436b6147a8 | -14.77085 | -46.04683 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6aba545f-2a55-391a-acf2-442bcf23d879 | -12.31346 | -55.10918 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9455267e-8978-322e-a6c3-2a2f8916ebc6 | -14.91588 | -51.44013 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b0fdaf8-74d7-307d-b1cd-4a52fafa37b2 | -10.38217 | -50.2963 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 98ab6b17-8406-3caf-85fb-2af4caa38a79 | -11.67641 | -46.34222 | 2025-10-07 04:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7bfa3b6-7a3a-385f-bcf1-c1147a660f8b | -13.24758 | -47.17378 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2233822c-2351-33a0-99d3-15485545d6ea | -13.33211 | -48.03471 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 920bedc9-ddaf-3d5a-a2c5-b1eb1bc17a11 | -13.09199 | -47.85472 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0b9e784e-2378-35c8-b6bd-aa6cf1e6295b | -15.60825 | -47.29238 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b20aa3b3-aa3a-3836-bc4f-ac6c7764fda2 | -13.26751 | -47.58438 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b902e49f-5c3e-3e58-80ab-57846cd92a52 | -13.09435 | -47.99117 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dabd6760-89a8-34a0-b6d4-6b5032debbfc | -7.43499 | -63.74724 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55076ab7-ca71-3c1e-9367-ffd6a90d5427 | -12.27207 | -55.1133 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbc26708-1074-3f98-8b21-37ac35eb04ce | -13.58799 | -48.69054 | 2025-10-07 04:57:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acd3b440-1cc0-3143-8f76-6b133fddcc2f | -11.05217 | -50.9105 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd22aa33-4c6b-3fe9-adac-701abcfa2d9a | -11.1282 | -47.22197 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 663fdaac-6702-3101-a841-86ed1f51377b | -14.93941 | -46.82195 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README91.md)
