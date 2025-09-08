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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51171cd4-9003-3dd2-a91b-c4c56461e595 | -10.89605 | -55.7151 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeed450e-693e-349e-9c0e-d4cae3034cec | -15.76484 | -53.56281 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48e19aee-ef75-30ab-bfa6-c69d16a55504 | -12.94264 | -54.80077 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 539978e0-e938-37e5-91b9-3e073f7d81c3 | -12.61679 | -56.97623 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f651fb76-fa71-345d-b99a-4f649f655348 | -12.85846 | -47.98203 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f004b26f-7427-321b-ba6e-a2880f5aced7 | -13.54411 | -48.11847 | 2025-09-08 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e8fd95ba-f267-3351-baf5-4d29f3767331 | -13.89293 | -53.98896 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 967ea280-aef2-303f-9cd7-dee0f2c325a7 | -16.33674 | -52.93542 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3774ab2e-6472-3a78-87b3-07d626690ab6 | -12.94931 | -54.78008 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf9b8b4f-547e-3112-a551-1b9827b769ac | -11.85626 | -47.54656 | 2025-09-08 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41f13324-df1b-3c6f-a158-6f8b716c9e47 | -11.41325 | -50.366 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 2eae2a76-be7c-3be3-8bd9-3674f6001549 | -16.89622 | -45.76179 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c22141d-3cb8-31f8-b43d-927c390dbbc0 | -15.25496 | -52.38713 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9a9f4c3-43a8-3836-b264-b9bb3ec607c4 | -15.53679 | -51.7108 | 2025-09-08 04:53:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1b394b5-6905-3155-8335-4233136f7511 | -12.62453 | -56.97338 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b2494bb9-848d-3ef6-9c4c-252f27472d79 | -15.11357 | -52.34508 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2e0edac-5859-3c58-bf89-6f82f9c32a3b | -13.927 | -48.03702 | 2025-09-08 04:53:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f79d2504-2b96-3ad3-961e-b383fbbaf940 | -12.87607 | -62.11049 | 2025-09-08 04:53:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdb14bbd-5adf-3167-b19b-a1d21024a64e | -12.83353 | -52.93619 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 041f170d-8b0e-35f9-ba55-70608ccd8a4f | -11.10489 | -52.00542 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50def55c-5afd-3260-b620-540d52c98d56 | -15.12506 | -52.3395 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3028b8d-93d6-367f-b0f9-68db0145f6dd | -17.53636 | -43.74318 | 2025-09-08 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cd1fa9db-2dcf-3581-9554-3ef6b6d138ee | -15.26886 | -52.38924 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 76d9ba6a-0d88-37a6-9969-1a273bc28811 | -11.87309 | -50.59939 | 2025-09-08 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e31827f9-263c-394b-977f-9edf560d52e6 | -11.60101 | -52.19853 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aaf41c3a-37dc-3e78-92ea-9bf625573f50 | -15.76765 | -53.56703 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7a8c8a2-6b52-3e0d-80c3-6af70c91bc0d | -14.08754 | -46.607 | 2025-09-08 04:53:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ecfa7a7a-d159-3540-93f5-cc510476c406 | -15.76539 | -53.55907 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5715a6c8-58e3-3f1d-99c1-cfb3561998d3 | -16.29482 | -49.55508 | 2025-09-08 04:53:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 164525ca-df9b-33fc-a839-82657ca76ef5 | -12.94879 | -54.76185 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0f6e08f-6471-319e-b819-91c9d0e18df2 | -15.12103 | -52.34271 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5af40991-68b3-315c-84c2-136c703f31f2 | -15.74265 | -53.53644 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e763257f-3126-3ab0-b671-7ec05d354182 | -11.35751 | -50.38891 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dc0c7d81-0afa-31fe-8841-24d1fb8dff0c | -15.10946 | -48.06942 | 2025-09-08 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8128aa6-cc88-320f-b613-6b57bdb7b7f3 | -11.07871 | -51.99038 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9a2167d-2059-3af9-b658-d88e4e056399 | -15.84383 | -52.27095 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 74221516-fe18-31d6-aedf-b00df5698d42 | -11.86488 | -51.06354 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a5775ec3-1444-33de-9278-fb98770fc675 | -15.25085 | -53.82201 | 2025-09-08 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 049bf88f-a18e-34fc-81c3-2ed4e11043b7 | -17.15095 | -44.44016 | 2025-09-08 04:53:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23eadba9-7c2e-3353-8ae0-890c37c1ffe1 | -13.29161 | -51.74092 | 2025-09-08 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdce76b0-41e0-35cd-b2fb-d63779e754ac | -12.82682 | -52.93513 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05f21229-b194-3869-9068-3d426e933c3f | -12.52415 | -53.84755 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f45bfdc-a3d6-3c2f-b9b7-8a7794b46205 | -15.84843 | -50.11349 | 2025-09-08 04:53:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ce9c8d0-7262-32ea-828c-6e29b1f0906f | -12.94651 | -54.79777 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 16c0ae78-ebf2-3ad7-831b-0ca2c1fbbe71 | -12.17113 | -43.94572 | 2025-09-08 04:53:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4347d1ed-93a6-3951-adb8-785af0be44ef | -12.82336 | -56.52173 | 2025-09-08 04:53:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d0e71aa-7a6a-34c4-9cb6-092a350b88d6 | -15.91858 | -49.07116 | 2025-09-08 04:53:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9a6e96f-c557-36ac-87f6-d56e6bac529b | -11.83631 | -46.76644 | 2025-09-08 04:53:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98dfee48-20bf-3813-b957-87b767733c02 | -12.00078 | -47.77297 | 2025-09-08 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 084accb7-954b-3ed2-89b8-575d9038a9ad | -11.18415 | -55.04803 | 2025-09-08 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19fa281a-c3dd-30fd-bf1f-4b5396f1c5a4 | -11.36179 | -50.38509 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4191ef9e-16f2-368a-8176-abce536ee276 | -11.8681 | -50.96681 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 79dffb72-75c7-34ea-a192-6bd9c91be0af | -12.93276 | -54.77736 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 449a86bf-8a2b-305c-9ea9-f23f266ec768 | -11.8675 | -50.97097 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53621cb9-1eac-320c-aaca-b598ee230519 | -16.43799 | -49.28561 | 2025-09-08 04:53:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5433cc39-e460-3c5d-9f38-6f8e79d2e941 | -10.50631 | -57.79805 | 2025-09-08 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a257896c-81fa-3c3e-9d56-3d135e6be46a | -9.95129 | -60.14568 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ffadea1-50ba-3075-b1d7-512b2f62e041 | -15.82953 | -52.26588 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7c48834-9ca0-3d20-8bd3-eb6130857a67 | -10.27386 | -63.16724 | 2025-09-08 04:53:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a2faccb-581d-33f6-b8cc-40f6503c7206 | -15.17169 | -55.9922 | 2025-09-08 04:53:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dee5f962-3a74-3942-b55a-af4725a0d28f | -11.64905 | -52.23247 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6168393-112c-32c9-900f-5bb57a3cb2e5 | -11.19836 | -55.00247 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| ee793390-4597-3093-8bff-aece411151b1 | -12.621 | -56.97277 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b59b4816-06f9-361e-b849-3244c9dfa74d | -11.79685 | -62.73912 | 2025-09-08 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 533a5eb8-0bb1-304a-8324-c4131dfdd8d0 | -12.47568 | -53.85418 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0e9fbb0-0681-3eb9-afa0-15dc3ead8636 | -11.41565 | -50.37531 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| cd1ca2f3-ed5e-3909-b986-382ea71c96dc | -12.81025 | -47.99983 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 651c3ade-ad4d-3cc9-93dc-381c32f0cfab | -11.61961 | -52.22027 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 575403dd-1bf4-33a0-ab27-260f246a14b1 | -12.93882 | -54.78198 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45a5c1e1-e9f5-33e3-bd27-c6c0277c5ff9 | -12.93831 | -54.76376 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae37107e-bcba-353d-9cb8-18f567f27a64 | -12.93495 | -54.78498 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ca8f5ee-7410-3e67-af5a-0ab47ffbf26e | -11.82818 | -51.4094 | 2025-09-08 04:53:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 213ea075-2013-3cee-8698-9863553e96ea | -16.51813 | -45.10402 | 2025-09-08 04:53:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38ae94f9-6664-3c0a-85a0-9437dd9961f2 | -12.19971 | -53.89951 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd4b8ed8-fb3b-3b99-a502-0538a276e2f8 | -15.53108 | -48.1819 | 2025-09-08 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 636f561c-efeb-38f4-94bf-0cdd44a0b678 | -12.4623 | -44.647 | 2025-09-08 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b37c4cd2-9873-34c6-bc32-499c986fe621 | -12.81365 | -56.51605 | 2025-09-08 04:53:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5daf705-5615-387c-af59-3aa710392ca0 | -12.47456 | -53.83957 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76bedd02-a678-3e8b-b65d-eb60920dc20b | -11.20562 | -54.99997 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af6d1cc8-0dbe-3071-b05a-d9743cdeadaa | -12.83017 | -52.93566 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 13f9f857-6b22-3d8d-87b7-35e5ca75101a | -9.13305 | -65.95385 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 279c42d9-eedb-37b8-a2c3-fb57b3409ff4 | -15.25416 | -53.80027 | 2025-09-08 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce33e482-74c7-39ce-961f-e8dd0af2c191 | -16.29237 | -45.68656 | 2025-09-08 04:53:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a47ee0e3-c2ff-3939-ab6d-bc65058d31bb | -13.82218 | -46.24875 | 2025-09-08 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 62d908e4-a918-32ad-8757-dd346befa63e | -15.25196 | -53.81476 | 2025-09-08 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2e04df4-85aa-33d7-8c8e-1196212321eb | -16.32988 | -52.93425 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 90c00ce7-b0cc-3494-9e49-10c62f37f373 | -15.18681 | -47.95982 | 2025-09-08 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5db1a881-370c-30a5-8feb-3b83b949108e | -11.83406 | -46.77212 | 2025-09-08 04:53:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ce1a875-813f-3eff-bca7-cd104145ac73 | -14.79842 | -48.26801 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc0f478f-1fcb-30fd-b64b-84f96ba5e97f | -11.22566 | -55.00325 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2919d9a-3ab6-3dbe-9431-e9f63ed8992c | -15.66558 | -48.21013 | 2025-09-08 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35040c68-5d37-3c56-a247-9a99354e7feb | -10.51358 | -57.80165 | 2025-09-08 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f088f8de-6cc1-3f4a-b6b6-a89635e7dc03 | -11.64349 | -46.63612 | 2025-09-08 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8509dba9-fedc-3cd9-8abb-6a4157b7b818 | -14.78237 | -48.11293 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3d3b5bf-f8ea-3ca5-be16-ee0c53597b66 | -14.5932 | -48.08312 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a446b1f-2834-3c43-87fe-286b48eaad61 | -14.80284 | -48.2331 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 149d402b-81eb-3881-845e-bd9a33e21c09 | -14.59538 | -52.12835 | 2025-09-08 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9abee23-afc7-382d-a2ac-bc35dbc4041b | -13.83278 | -46.24423 | 2025-09-08 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7ae0518-3921-372b-af10-f3ab876ddeda | -11.3717 | -50.34182 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 349f5dee-bf49-30a4-9e27-e20aee878590 | -12.95262 | -54.78062 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README65.md)
