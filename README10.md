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
| 46a55461-53ef-3f27-bc47-d54e93962f9b | -11.67935 | -43.78451 | 2025-06-03 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ab2a0993-f642-3e2a-b96c-6676b77c9f89 | -14.02585 | -55.1293 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1201cafe-6312-353e-bf54-dcf8f18a826c | -11.25445 | -49.49748 | 2025-06-03 04:19:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5fe08812-2d9b-3e65-8f67-cf7876110249 | -9.7185 | -48.31328 | 2025-06-03 04:19:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8456e5a0-87c4-3e24-a091-ca969cfc194c | -14.88025 | -47.82795 | 2025-06-03 04:19:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57a32688-ad0c-3275-81e0-9faf382ee8c6 | -13.14018 | -56.80359 | 2025-06-03 04:19:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24416b3a-9e83-39e1-ac3b-db0d12373144 | -12.46106 | -54.9146 | 2025-06-03 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35210465-a576-38e6-a324-8174864213ea | -14.01333 | -55.12218 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9159f14-e260-37b6-9163-3a057b20fe0d | -11.25074 | -49.49683 | 2025-06-03 04:19:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e00c38a7-dee6-3ade-adc0-636796a2d199 | -11.91904 | -54.82449 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1ae9162-73e4-3fb8-b57a-d6b10f7e500d | -14.02624 | -55.13725 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 627d6e1a-4ef7-3bcb-bf84-c80d3026c145 | -10.67224 | -44.38174 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 908b605e-a043-3336-ae7a-c6a13a8a802c | -10.364 | -48.7307 | 2025-06-03 04:19:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c1cd5ff-2455-36f8-a13f-c40c285021ca | -10.0644 | -48.3279 | 2025-06-03 04:19:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20c21831-85e7-3b85-afa7-c7f7f47f1699 | -11.79555 | -47.38153 | 2025-06-03 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8212aa52-1fea-32cb-8d4a-db2f3c6a94b6 | -11.922 | -54.81653 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 020809b9-b902-30bf-82cb-f2eecc5517c5 | -13.13936 | -56.8076 | 2025-06-03 04:19:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98d216a2-8230-3bcc-954d-c4e0574d6611 | -10.13852 | -52.14133 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3c30716a-96c7-3a55-bebc-38cde4690f8c | -12.37812 | -45.92358 | 2025-06-03 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 386b7204-5a62-393a-8fa8-f59645b0307c | -9.52322 | -46.75532 | 2025-06-03 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f69a9d3-180b-3c4a-8004-995373cf17db | -14.02526 | -55.13231 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d824fd1-73b0-3eb7-802e-fd8d61547671 | -14.01572 | -55.12727 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 13047951-e92c-33d9-8378-0987984eba43 | -12.37481 | -45.92304 | 2025-06-03 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb415f1d-3a71-38ca-b1c2-da2d2a484233 | -10.46174 | -47.94292 | 2025-06-03 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 63fcb845-b060-3d01-9bb9-b917cbb86ce7 | -3.0358 | -49.42138 | 2025-06-03 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c31106de-5d61-37ff-a198-666d7ef79e0a | -8.19326 | -49.80073 | 2025-06-03 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 482b84a8-1d58-3316-a8de-4a4914f5f7d0 | -11.91011 | -54.78641 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9579d7cc-a91b-3942-b7d7-235b2922b2c6 | -12.08739 | -54.57525 | 2025-06-03 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c70badd-7e74-3fce-b8a9-5b4d377d32f4 | -8.90733 | -48.90218 | 2025-06-03 04:19:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c436fb6-c52e-3c3b-abf2-ef7591278d63 | -13.63644 | -52.18171 | 2025-06-03 04:19:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8927069-39cf-3589-9eef-0aad7d6af9ce | -11.92262 | -54.81334 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7cdeb63-aa02-3144-bef7-96bcec13e727 | -9.10923 | -47.72292 | 2025-06-03 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 146a747c-5d87-37ea-a98c-9e7aaf8ae95d | -11.25521 | -49.49301 | 2025-06-03 04:19:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f79f70f0-2141-3d12-853f-6f3625c89ea0 | -9.07141 | -47.15726 | 2025-06-03 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93d90ff1-ea71-3725-88e6-e6b8e661ae0b | -10.24303 | -47.5898 | 2025-06-03 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60d72a84-a3d0-3ec5-9169-449da91a7262 | -8.78389 | -48.00414 | 2025-06-03 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b175cc77-063f-3dd2-ab50-538b958357dc | -9.40144 | -48.41214 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 310df956-b109-3c2e-96aa-480f8340eccf | -12.33853 | -46.30312 | 2025-06-03 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 239032c5-16c1-3e07-bf1a-1eefd25185eb | -13.42749 | -47.57973 | 2025-06-03 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c381b6a0-c4d4-3426-a1a0-16dff34cf361 | -10.45543 | -47.93789 | 2025-06-03 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9e1f34e7-e3b2-39f0-9417-a9539bc152f7 | -9.19299 | -49.69645 | 2025-06-03 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4d548afc-8ee0-3869-9639-c7c73c18c7f0 | -3.03997 | -49.42205 | 2025-06-03 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0958137b-fca0-37b3-ac9d-085745c0aff2 | -11.90439 | -54.78846 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5117ad4f-4c5e-326f-92d5-764ef12b2cc6 | -12.37252 | -54.16587 | 2025-06-03 04:19:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6175a24-b09c-37d0-bdea-b534a0a95c3b | -11.89865 | -54.7906 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d0c2a77-e5b9-3387-8dd5-3bd5a6dfb6ab | -8.90435 | -50.04364 | 2025-06-03 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e779ac5b-7868-3efd-b68d-21c21c314d62 | -11.79218 | -47.38097 | 2025-06-03 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fc6a5948-3fe0-3f16-9632-beadc86fe64f | -14.01897 | -55.12023 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92127eed-2a2b-3398-ada5-b31d7b06f3fe | -10.24094 | -52.22684 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b83236c-b37c-3d19-9ae3-5a3db2451b21 | -15.69483 | -43.42086 | 2025-06-03 04:19:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5db5c1d5-56f1-3da0-af70-e8a3f4e0dd76 | -12.37006 | -54.16994 | 2025-06-03 04:19:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c74bb2-50d7-3c71-827b-47eb298dc791 | -14.02973 | -55.13631 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa07e520-2a96-345a-9006-9483a354a0fb | -13.59131 | -54.27556 | 2025-06-03 04:19:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8b97af7-f9fc-337b-882a-8d894e050dfd | -13.09061 | -45.27134 | 2025-06-03 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abf270f9-ee43-396f-a71e-e2acdc378d70 | -10.45132 | -47.94118 | 2025-06-03 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a89fc2fd-4613-31a2-9a1b-6896d305bcef | -10.62408 | -48.08178 | 2025-06-03 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96e9693d-2f8d-38d5-844d-3f399981c64d | -14.02681 | -55.13424 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ad42612-ad66-3f6d-92c9-b2816da3bd27 | -13.64065 | -52.18246 | 2025-06-03 04:19:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dcc040d-d5c6-3e9c-ab4b-5101c34868f6 | -11.55089 | -56.42921 | 2025-06-03 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b54c9c83-54af-3408-93c3-f08b0de6902e | -10.13489 | -52.13604 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f48f8055-fde2-3a13-b9b2-95d5969d2717 | -11.67877 | -43.78832 | 2025-06-03 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 857af80e-1bdf-3d16-bff4-0d4b29983032 | -13.14488 | -56.80628 | 2025-06-03 04:19:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c0d5b09-4139-38b3-b038-848e9817909d | -8.84515 | -49.84813 | 2025-06-03 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de3102ad-74b4-39dc-ab80-ef48987f37e4 | -11.9044 | -47.44466 | 2025-06-03 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12e31640-94db-399a-89c8-81bfd92907de | -12.37358 | -54.16034 | 2025-06-03 04:19:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 155f74f6-056c-33c3-858f-7100f2599a5f | -10.23199 | -52.22526 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 091e398d-7733-3a73-aeda-50470c099795 | -11.92138 | -54.81972 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a0d24d8-22b0-369f-bcf6-9f56062084f3 | -13.48492 | -47.48095 | 2025-06-03 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 00f971b4-1176-3ac7-9006-3361483e21a9 | -8.84123 | -49.84748 | 2025-06-03 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c337dad-fd89-39a8-b1bc-35c044a0a4d5 | -9.40365 | -48.42097 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ac0382f-c855-3a3c-b849-2012bc05fa15 | -7.90126 | -50.36437 | 2025-06-03 04:19:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a1962e8-74ad-35b2-a1c5-a5fd1f96b29b | -14.01783 | -55.12619 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14b31b5a-d9dc-3bc4-8758-c3576d92a236 | -12.32916 | -46.29798 | 2025-06-03 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d22e5e0e-7fd2-3137-afd0-20cba9a50df0 | -10.69045 | -57.6471 | 2025-06-03 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d7ee0da0-a7d9-359a-9082-82d1332d74cc | -13.41773 | -43.75711 | 2025-06-03 04:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de59dc49-fe85-3cd9-9052-5d22e153e8e9 | -11.91964 | -54.82125 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75bba541-9651-3d2a-b3bc-51935dfacf01 | -12.36412 | -54.17458 | 2025-06-03 04:19:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0702b927-cc83-35b8-af6c-705da8ddf3b2 | -12.66638 | -58.22002 | 2025-06-03 04:19:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b187f21-6544-3771-b531-24cfe645ab74 | -13.48432 | -47.48464 | 2025-06-03 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| baa77b9c-d21f-353b-9810-81df5f46147f | -9.55023 | -48.68931 | 2025-06-03 04:19:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1d7e613-4311-3ea9-b211-2bceb6666372 | -9.06799 | -47.1567 | 2025-06-03 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39a9c5ea-1663-3927-a4d5-17cd1d351dcd | -13.08394 | -45.27026 | 2025-06-03 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f59c5f99-fe4d-39c5-8558-ae845cd62e13 | -13.00661 | -43.79859 | 2025-06-03 04:19:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6019d4df-20f8-3ddb-9f01-393c13ec75c5 | -9.72139 | -48.31786 | 2025-06-03 04:19:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0536b24b-18c1-307d-bd9f-a55f93fb8dc5 | -8.72465 | -50.26389 | 2025-06-03 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 645e47be-2038-3565-a6ee-d50f35347033 | -11.92014 | -54.82616 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba691df8-0c4c-3305-a076-8923d874381f | -9.40158 | -48.43343 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a0ddb42-be72-3638-bad7-bf9605d6fe8c | -8.05588 | -49.97064 | 2025-06-03 04:19:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b22df211-6abd-356c-8b3a-1019761d913a | -8.62867 | -47.13992 | 2025-06-03 04:19:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 628c54ef-f3d2-34a3-bcb0-6d9c6fbab3b3 | -10.24339 | -47.60934 | 2025-06-03 04:19:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10ff02e7-4daf-37c6-8d14-00858fed8d33 | -13.14409 | -56.8103 | 2025-06-03 04:19:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 028d3b35-6c26-354b-84c9-7360e65f30bd | -10.45479 | -47.94176 | 2025-06-03 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1c3d8c3d-4fb2-3ac5-a5fd-a9409143c10b | -12.66013 | -58.21853 | 2025-06-03 04:19:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f609f29-46a5-345c-bca3-f3a3c92a4e0d | -10.23566 | -52.23048 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf240d09-a21a-3d7f-810b-8bf546b76b63 | -12.37757 | -45.9271 | 2025-06-03 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0519366f-feb0-3113-b45e-9522b692b8e1 | -11.5682 | -47.44248 | 2025-06-03 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 479d4da5-2c55-32a5-825a-6d3b549282bd | -11.91449 | -54.82019 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cabf0fa1-bf19-3d58-988c-73f82fc53eff | -11.90556 | -54.78221 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1cfacb34-e376-3509-96d9-bf5eef3eea42 | -9.19685 | -49.69711 | 2025-06-03 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1637b12-df0a-3fd4-9985-78af9e9ba64f | -11.57716 | -47.45159 | 2025-06-03 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README11.md)
