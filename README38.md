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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb20b7d9-63d4-3796-a844-ff0e50173668 | -6.40207 | -54.94667 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c15ef46-6305-3478-8659-4e0dc712d059 | -6.80772 | -59.45629 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f09af63f-d17f-3bfa-890a-4917f68990cb | -1.26919 | -55.66562 | 2026-08-19 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 353064ef-622f-3869-923f-9b57a5b2f529 | -7.53399 | -55.58328 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cb01e065-e39c-393e-a040-241c37796164 | -6.0912 | -57.9187 | 2026-08-19 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 10c7bc49-d0a9-3865-a76a-7791d68849be | -9.4257 | -60.416 | 2026-08-19 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| d03a352a-f9bd-3579-9ecb-efeb20ef14ce | -8.5787 | -54.7364 | 2026-08-19 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c23950ed-e388-398f-9d11-22fc1ee9b381 | -8.5598 | -54.7579 | 2026-08-19 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 2d5ed032-bb7e-38ce-a5bb-a19d1f446ffe | -5.4317 | -48.4212 | 2026-08-19 04:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| caeaeddc-7f6d-3cd2-9fb7-a5a84287b04c | -9.3875 | -60.5528 | 2026-08-19 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 9c4630ea-34cd-35e0-ac47-8d405bd39f24 | -5.9011 | -43.6279 | 2026-08-19 04:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 1cde5c9f-1886-316a-ab9b-fdd40ae56c3b | -9.4061 | -60.5518 | 2026-08-19 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 9044279b-8640-39a9-9f9d-b7480feaa786 | -8.5785 | -54.7566 | 2026-08-19 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| ce32339a-7da8-375b-a503-bb92fcc0ca14 | -5.9994 | -57.8639 | 2026-08-19 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2fcc80be-5fed-3c51-a3b5-3aad5da7a17f | -8.56 | -54.7377 | 2026-08-19 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e55bfb31-2474-3841-9aab-15e6bc9238d1 | -8.5413 | -54.7389 | 2026-08-19 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f76a2d82-6e9c-3aa7-9c80-2adfc647e97b | -5.4319 | -48.3996 | 2026-08-19 04:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 42214e4f-bc40-3bbd-acf7-f6dd2db5da19 | -8.5412 | -54.7591 | 2026-08-19 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ec66aa50-795b-3f08-8e7a-a6be72b35443 | -5.92 | -43.6032 | 2026-08-19 04:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ca14ada6-890e-3bfe-ac98-212d251de813 | -5.9198 | -43.6264 | 2026-08-19 04:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 154.6 |
| e15aed4c-5e87-3c4b-a53b-3b96dc4c20c5 | -9.4256 | -60.4353 | 2026-08-19 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 3af04f29-9388-3bc4-91c7-817fd350bffe | -9.406 | -60.5711 | 2026-08-19 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| ffde1b14-010b-30b1-94d9-a8f8986067e8 | -11.23878 | -46.14734 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf43bacb-9577-3d6d-8036-0795faa7487e | -10.93763 | -57.11707 | 2026-08-19 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a538389b-1b06-3f2a-8a82-937d30961597 | -15.77613 | -55.57748 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 832b0263-ed9d-32e4-b986-1cdb34190d39 | -9.47785 | -51.60151 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3538d8c0-b6cd-3f21-b799-dc02a81ff5f4 | -10.24304 | -46.99423 | 2026-08-19 04:40:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a7605e1-3a2f-3aa9-afef-ff5b48c63dbb | -10.52217 | -50.79658 | 2026-08-19 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 645b3a1d-d9a0-3a41-bd27-b98a116690f2 | -11.19921 | -54.02265 | 2026-08-19 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2bd020d-eaad-38ce-a30c-264635edafa7 | -10.91213 | -57.18348 | 2026-08-19 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59229666-44c5-3899-8ab0-8686af2a5354 | -13.47129 | -51.78983 | 2026-08-19 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27d8f4f6-3b2e-3511-a218-1d9d052c7b25 | -14.4889 | -52.99154 | 2026-08-19 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 072a9028-ed17-3268-b275-0252a02f7652 | -16.71395 | -46.40574 | 2026-08-19 04:40:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27efb5fd-b83b-3ec7-9fbd-cef31c0e9616 | -10.12399 | -52.11601 | 2026-08-19 04:40:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 437ea5ca-ebe1-3000-a4f9-ec035c00b1d3 | -14.46136 | -45.63336 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36e9cc18-06fe-3bc1-a587-18bbf5048a4d | -12.75959 | -48.44444 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d57c2930-a75c-32e8-8692-a21b3a4888e4 | -7.60394 | -60.95107 | 2026-08-19 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ae5c3552-f1b9-394b-83ee-863bf5a84c5c | -8.55263 | -54.75952 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f083424-90c4-3c02-ad76-51da7cb74991 | -8.58806 | -54.76153 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be9acf77-6fb3-3657-bcec-3a8a50587b14 | -9.0183 | -60.49631 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b115567-05ae-340d-adc9-911b5327a797 | -8.53389 | -54.73907 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1decc368-7754-3722-9c47-0d8648710090 | -9.07465 | -50.80899 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c63d10a0-5a53-3843-82b8-327f8767733f | -8.54839 | -54.73294 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 88fa11ff-8d99-3224-a36d-a1661e4d9710 | -7.60945 | -60.95803 | 2026-08-19 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50f7dec4-4da3-30d3-86e1-ad8159404a1c | -11.09036 | -49.91973 | 2026-08-19 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77016d6b-ab1d-37cc-9469-c9d6c99c9e10 | -15.77593 | -55.57678 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a163efe-c921-3a97-9ff0-d95f4b4f4fc5 | -9.40232 | -60.58122 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7409a8cb-6c8c-3a96-aa96-520f484690b2 | -9.82739 | -46.62319 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f7bb4ca-5edb-3912-aa4e-913019de1062 | -12.75847 | -48.4517 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a83b0ce-943b-33e1-97c2-4b3a6fac29e5 | -11.49234 | -45.10418 | 2026-08-19 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca99e45e-f657-366a-a597-a77cbe26a167 | -13.25668 | -51.64393 | 2026-08-19 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ed53aa7-3724-39c3-8960-260e3f685dac | -7.60829 | -60.95245 | 2026-08-19 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4672869d-48b8-31ff-8ffb-f0a49ff977be | -9.06095 | -50.84961 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3490ef94-a61c-3714-bc06-ffa068d59982 | -11.59488 | -50.54381 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95547d87-b798-3a3c-acb8-613df3715c2b | -8.49775 | -54.86481 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32225771-7b4b-3722-990b-21979f729c98 | -8.53756 | -54.73698 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 174c9cd0-ad21-31f8-8bdb-8bedff2bacdf | -12.05292 | -46.46032 | 2026-08-19 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 58d2f5e8-db1a-3155-928d-8a07b71b03a0 | -15.28238 | -56.49976 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3139c175-69d4-3f0d-b645-790bd30719a4 | -10.87987 | -57.12899 | 2026-08-19 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75187d51-74b1-3b4e-bcd4-237f8c7a28df | -8.53092 | -54.75575 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb69cf1f-a737-3308-818c-7a06443939a9 | -8.5362 | -54.77125 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4ecab4e-8a7b-31c7-9f1f-47df6f86958c | -11.15856 | -49.62296 | 2026-08-19 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df0c25d4-fb51-373b-8a4e-a3d301339955 | -8.55493 | -54.72121 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 78dd8770-be68-3184-84e0-2c2a8a98c1e8 | -8.57581 | -54.72938 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59d9782c-48c6-38ba-9cda-cdfc946a3671 | -8.56214 | -54.73096 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ef13d68-548f-3e09-9caf-133dc2b0648a | -8.53241 | -54.74738 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f9d22f7-56d2-37bc-88c4-a549d12781f7 | -11.11049 | -47.27425 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 435e8a7f-030b-3336-8b92-abedd23162b5 | -11.71428 | -54.63371 | 2026-08-19 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a85f5ee7-e0e7-38f2-ab0b-3c56ea098838 | -9.98124 | -53.93423 | 2026-08-19 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0975bc8c-70e3-3b67-abe0-c2e95ac984e8 | -9.81237 | -46.62885 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da68369d-20ef-3946-91b3-6ea29a868ecd | -8.21768 | -55.01994 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff734702-7747-3b6f-ba7f-a67665671b1c | -9.08216 | -50.80639 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be43cae6-4eb1-3ac3-8d12-e4d218aa2eb3 | -15.77911 | -55.56078 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd4d4c81-1c34-3f75-adba-191c68edd747 | -14.73712 | -48.73753 | 2026-08-19 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81e74eda-c772-39f5-895a-4632127ea147 | -11.31984 | -55.22882 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ebeca0f-b9db-39a8-b3e4-e7ee7816a8f7 | -15.77972 | -55.55651 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d7620ce-2bcd-3b88-ad14-368a985300e0 | -12.82759 | -48.42567 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d20a5eab-ce54-3a97-8afd-08c73890405d | -8.5758 | -54.75493 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ad0687e-7e14-3d34-9d0f-e55529c0a081 | -14.48343 | -45.67115 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8cf9761-6058-37b6-aae5-e9765a8f8deb | -7.43531 | -59.78391 | 2026-08-19 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 726bbadf-71f8-3cd4-b896-c37f53d05462 | -8.56284 | -54.75233 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd709fdb-972a-3c7c-8d6e-712f30e3a32e | -8.58733 | -54.76573 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 430c1949-b647-35bf-8765-3e5523e4f329 | -12.82816 | -48.42205 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 583beb77-7fd5-369c-ab17-fea9a3a71bbd | -13.41485 | -54.36903 | 2026-08-19 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9da3cf37-e3fe-38f9-9ca2-fc5e930429f4 | -11.31874 | -45.21202 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c13a244d-bbc8-37e2-ac58-066846e0f426 | -8.5687 | -54.69374 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 379b1b57-741e-3caf-9b02-dc26444fb6fd | -11.2359 | -46.1525 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f60be48-8915-3ed8-a1f8-95f6060809bd | -11.22368 | -55.06167 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 080ee152-b35e-3eff-a33d-392116ff3c22 | -14.04452 | -52.33264 | 2026-08-19 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fe2e205-b612-370f-8777-e6f3988307c9 | -8.57938 | -54.75998 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d5d7f5df-eabd-3f61-96c0-bbdc5eed12fd | -11.23817 | -46.15147 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 295f964a-ca3f-3db7-83de-2c3db642ed73 | -8.52889 | -54.73544 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd2b7595-e90c-3530-a5f0-d0885ef8c51f | -8.56924 | -54.76683 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9a6765ab-c44a-31c6-a5fc-d87964d22645 | -8.57159 | -54.67733 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fda3b17-9694-3a15-b622-f6a24b1f110e | -16.71843 | -46.40421 | 2026-08-19 04:40:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a224509-4d20-37b9-98bd-11ae15f93145 | -12.77964 | -48.44772 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee11a6c6-2cf7-387c-a5b7-2dc6c04a6612 | -7.61385 | -60.97103 | 2026-08-19 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cffe7b7b-f41e-3d4c-9648-782ea1645fd4 | -9.39689 | -60.56079 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 640a4422-cd8a-3e36-897d-466bf844572b | -10.30782 | -50.41085 | 2026-08-19 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8fbc799-366a-3def-be77-5216301f61a3 | -12.47558 | -54.18819 | 2026-08-19 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README39.md)
