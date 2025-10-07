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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91b77cd6-90e9-3e4d-8673-2a1ca2042570 | -15.36491 | -47.30352 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b57770f-379f-3350-a647-0ab17128e2a7 | -14.28902 | -45.85337 | 2025-10-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b391feb-f3d7-3c70-b980-a0adb4f94df7 | -19.94426 | -44.63409 | 2025-10-07 04:10:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| face19da-d993-39d2-8a8e-c7b547d1493c | -18.11298 | -53.361 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8379f35-d3cb-3e3b-8326-dda7b316d674 | -13.58974 | -48.14687 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9528dcbe-61e0-3595-84ec-90f393066546 | -14.61709 | -46.13525 | 2025-10-07 04:10:00 | NOAA-21 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33c9e685-dc93-369a-943c-cb7de3d883c8 | -13.06548 | -47.89241 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 345c20d6-e411-3e2d-9fbc-0d825f023db7 | -13.24003 | -47.79605 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d9bb4088-0825-35f1-b161-bbd60a41243d | -13.28582 | -48.06237 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d7ce5098-e3b3-3c8a-bd7c-5ffcff231824 | -13.0743 | -47.82067 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 347b532d-f9ea-3fc6-a890-575ae747d004 | -13.24005 | -48.45869 | 2025-10-07 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 98882d88-8c84-3944-8bed-fd40e728ff36 | -18.9703 | -47.83004 | 2025-10-07 04:10:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 67db487b-4b59-378b-9d12-e695cf59a1a0 | -13.5937 | -48.14754 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 720aa7c3-c8b4-3e3a-94bd-d2ec08717387 | -16.30713 | -42.05198 | 2025-10-07 04:10:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fc74e1a0-7164-316c-955e-34d5dde32a67 | -15.63242 | -43.00516 | 2025-10-07 04:10:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2eafaf91-9fd5-3d20-89e1-fb4a346f9378 | -18.26633 | -45.46457 | 2025-10-07 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4ce993c-5d73-308c-a302-72995508f534 | -14.7075 | -48.38398 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b8b59fe-ad83-3ae3-b448-2327c6d9e57b | -17.09108 | -43.38067 | 2025-10-07 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e4f060bb-a0f0-30ea-8b49-2ca337818879 | -18.11882 | -53.35844 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7edd237-fb3d-3f41-873e-20e5180a64e4 | -13.97423 | -53.90447 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96a0797c-8a58-3f66-845c-0ea001f775b4 | -12.18131 | -50.92668 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0dbc80f2-a5a4-3412-abbb-4d9bdabf20dd | -15.11675 | -43.86969 | 2025-10-07 04:10:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3c4d582-95a9-3c57-9627-db13abdc2e7e | -13.72228 | -48.19876 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99f06288-a31f-3331-ae17-57cc84c560f6 | -20.12109 | -44.41383 | 2025-10-07 04:10:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ef8bcbaa-67af-38b6-b6e4-a0e969efa488 | -14.90312 | -46.84334 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c306ba6-072e-3c47-b3b8-1747958cbb43 | -12.14577 | -50.87424 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e39e013b-f9e0-35c8-8b64-ec1af2eabcea | -19.95802 | -44.63274 | 2025-10-07 04:10:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 146f1faf-6218-3ecd-8a55-1e4bd972a752 | -13.07179 | -47.87971 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e64135b-f3c3-3c1f-a32c-9e1242460f56 | -16.68115 | -46.82913 | 2025-10-07 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 701ac677-1914-3775-8d8c-06389a39ad15 | -18.78311 | -44.61732 | 2025-10-07 04:10:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 65493cb3-8ec6-3649-ada3-2be24f3ab011 | -13.22257 | -48.46272 | 2025-10-07 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 188b3a15-1e7f-37e4-ba45-1b856d3296a7 | -13.94479 | -48.17385 | 2025-10-07 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37e14969-b82f-311d-ab35-6f4a7f8c6669 | -13.28281 | -48.05636 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a70e66d4-d1a4-3def-9354-3e451564080b | -14.89951 | -46.84272 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9b165eb-04a0-3ece-9f12-ca69eb8b7bf3 | -13.35858 | -43.66805 | 2025-10-07 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d199c16-46df-3afd-a71d-f5dc59d7b225 | -13.86198 | -44.41619 | 2025-10-07 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9767432a-18d8-3787-834b-36f709b69aa3 | -14.92662 | -51.41334 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 06b89c97-3011-3114-8c1a-8a7ba9f35399 | -15.49643 | -46.84655 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87e2dc34-5ef7-3b5f-a632-9cdae6614dd8 | -15.02415 | -47.5531 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 62faa713-9d75-36e1-b73b-1fa4f11514d4 | -17.56219 | -50.44149 | 2025-10-07 04:10:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87b9892e-417d-3850-9dc4-d3f0dbd96912 | -12.16387 | -51.43858 | 2025-10-07 04:10:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdbec952-7df6-3063-b51a-a80413a6df10 | -13.27234 | -47.16384 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf7e58d8-813b-3cab-9fb6-63502b747949 | -17.92368 | -44.60676 | 2025-10-07 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31fe5de5-76b6-326f-800c-9ed9cbcf0b23 | -13.28357 | -47.16598 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6bb252b-93d7-3727-ba38-407ee4026610 | -14.71695 | -48.35335 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| baa1a0f2-0d49-34ca-851a-6336c1252011 | -12.54574 | -48.14179 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49d88415-9707-3080-a5d1-e25fbf475ca6 | -13.26267 | -48.06133 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39cd43b9-d3a9-3b75-b18c-9dce957e327b | -17.08998 | -43.38787 | 2025-10-07 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a5bea41-9e69-3be3-9504-8d49a7d63a15 | -15.20897 | -46.37714 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e06cacb-dc4b-3f0d-ba3a-44471a1b81e4 | -13.25835 | -46.47352 | 2025-10-07 04:10:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0aca27c-ee1a-3884-9cb4-489359f852a5 | -13.27984 | -47.16515 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea974e77-fd62-341b-992c-3a2aa0b680c8 | -13.06944 | -47.89294 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff96cde2-5e81-31d1-8b96-735cc12cdfae | -13.27886 | -48.05564 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d52d2bbc-c0f4-37d9-a88d-c4ea91231cf6 | -11.86366 | -56.89032 | 2025-10-07 04:10:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4f429935-858e-31ab-a44d-ea6ea9674e8d | -15.99517 | -50.9437 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cacd3282-5cdf-36c3-9ca2-ee126ba768b5 | -13.25109 | -47.17496 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 17944ce4-3f7b-316b-b32d-c3593cf9579f | -15.8075 | -43.6748 | 2025-10-07 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5e43f11-3a31-3647-afe4-05fa59969bdb | -12.38277 | -51.10503 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f0fc865-c6f9-38b8-a599-c1ab7e602565 | -17.09053 | -43.38427 | 2025-10-07 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3d88ff6d-c820-3e5f-ba14-e69223abaa79 | -12.24873 | -47.76147 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d713be20-01d4-343c-81f4-3da47096c4d5 | -15.60769 | -47.29292 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a6447c0-0608-3a26-98a9-ed5f095cafcd | -16.06194 | -50.99276 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60ba3de5-6c9a-35a8-99b1-f86fb199c5ea | -16.34504 | -47.05207 | 2025-10-07 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77b6d8a8-fdbc-3a3b-967d-74bb6a2c9846 | -15.59136 | -52.55707 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d0b60465-9101-3086-9cb7-9454f0fcaeb3 | -16.29269 | -45.2395 | 2025-10-07 04:10:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69f338b7-1818-322e-81a1-80ff527d1210 | -19.22524 | -46.48251 | 2025-10-07 04:10:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29518a37-eae9-3745-b829-f8f2184ab512 | -15.21621 | -49.29679 | 2025-10-07 04:10:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2c84e11-dbb0-3d0e-a3ca-c6476830e6c2 | -15.27763 | -46.33493 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27b00159-fdf7-3152-99ef-52a57b47ae09 | -13.27048 | -47.5773 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1e37a87-eaa9-39db-a267-10d6cd01c271 | -20.00992 | -44.0751 | 2025-10-07 04:10:00 | NOAA-21 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 06619e55-9368-30e4-af8e-07c2c98f45fd | -14.63685 | -48.32391 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29ffe8e0-d585-3f12-82c0-6c77d375a503 | -13.29069 | -48.05796 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd4be3c0-69eb-37b4-9e38-2d3c24d7a72c | -13.08239 | -47.84293 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76a1d4e1-6679-3c62-a784-bf4971478f0c | -16.10254 | -48.93937 | 2025-10-07 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 54a36d51-6543-375f-a3d2-ac2b5c366274 | -14.65311 | -48.36916 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17791b54-5d78-39e6-a935-f4bea101a72a | -12.46506 | -48.00435 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 734e23ad-56b3-3145-9132-84596dde6c30 | -16.34575 | -47.04791 | 2025-10-07 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd4226d7-817c-391e-8f0b-535cb69be4b0 | -15.29225 | -46.334 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| af78fbc3-ce7d-3559-9705-8e41d238ceec | -11.86514 | -56.88326 | 2025-10-07 04:10:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6b6865ae-0f53-38da-9550-63fab12abdeb | -15.36872 | -47.94087 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4fd6492-f17a-3a8e-aad4-624028197b8e | -14.92366 | -46.81063 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08ab6df9-3b86-3cfc-9c3e-c80b1745ab31 | -12.25774 | -47.84954 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67e25ebf-0742-3db8-a4ea-39d8c2d1593f | -12.34354 | -50.26556 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6fadcb2-cc07-311c-85d9-8f7048b2709a | -12.58414 | -48.11176 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e93eac3f-5abc-3809-9411-d7771e1234ff | -13.69221 | -47.95703 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 516a9536-143d-31f5-9ee7-206b760c1618 | -15.53339 | -42.17395 | 2025-10-07 04:10:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0dd2ca2-71b8-3397-9e17-1ecb4ee2c096 | -13.58087 | -48.15075 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3d450606-2972-318d-8338-dddd7f0a9917 | -13.37383 | -47.56534 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47c6c259-e0c3-304c-bb8c-f2d61be34a64 | -18.28407 | -45.45651 | 2025-10-07 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b44d2c5a-5d82-37db-9ba1-e196f59aea53 | -15.61047 | -52.56739 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ebdf7f3-a83f-3549-921c-86681204cc52 | -14.66821 | -48.3987 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6f0f6af9-0f84-3b9e-a2de-66e5448f4c2a | -17.02563 | -43.45156 | 2025-10-07 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c4eba7a-d673-3cb7-ad7d-7a37914725fc | -18.12021 | -53.35162 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b265ad7a-8bce-3c25-ad28-718adabeb4ec | -15.17355 | -45.7345 | 2025-10-07 04:10:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87908d1f-91de-3bb1-a8a8-9e61d316a6ed | -13.51622 | -42.35013 | 2025-10-07 04:10:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 607b62e7-33b4-36ed-84de-e4ad8706b1c2 | -12.66235 | -45.0318 | 2025-10-07 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2392cede-3d8d-3d21-9eb6-5520aeb5d339 | -15.12062 | -43.86668 | 2025-10-07 04:10:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9ed9a564-996a-34ea-8b4b-f2fb23b54ba0 | -16.60765 | -47.02179 | 2025-10-07 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ba02726-51cf-315a-ac80-5debe6f444f4 | -18.51609 | -43.90665 | 2025-10-07 04:10:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1dacb663-8c68-32f5-be4d-7edb86122bf3 | -15.62564 | -52.54438 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README44.md)
