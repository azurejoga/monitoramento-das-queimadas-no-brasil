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
| 79787476-60b2-3563-b16b-e7580fc2f406 | -12.79815 | -54.06309 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57eac24c-e924-30ff-b2e0-ca589071f318 | -10.80664 | -50.83554 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15f0c94b-a959-326f-b23d-3cdc77264e01 | -10.36693 | -50.21595 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25aa25b3-8ca0-356b-b2b4-3111aa414501 | -10.90497 | -53.96667 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f423f3f3-c412-3656-a67d-12c0021abb73 | -16.03462 | -52.50153 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a45b2749-8da5-3eb7-acdc-18485d385f7f | -10.36619 | -50.22002 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba58b5ff-56c0-3ea4-a878-8e90cc8e9ca8 | -7.57819 | -57.68944 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6f392def-e378-3447-a103-7601e7437b3f | -10.27616 | -50.23955 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 117ab36f-622a-309d-92ee-f41b4c817fe6 | -10.41525 | -50.24163 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 7f38786b-1fb9-3c0d-b8a3-416715eebd56 | -14.66342 | -54.47255 | 2026-09-21 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 77460a77-8efc-323a-ad80-25fb19d6bbf4 | -12.90108 | -50.97054 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b4a48184-164c-30ec-b572-232d2b69146b | -10.7895 | -50.75686 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66264b4f-d836-3e31-94a4-5d69ab4ac336 | -11.94874 | -46.49686 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 770ff70e-f51c-3f49-908c-7ac7d26a8bb7 | -14.05539 | -52.11871 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fae45b52-9c3b-339d-8f01-661b2bf4ec95 | -10.53895 | -54.49988 | 2026-09-21 04:21:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f32218cf-41a8-3431-adb8-cd2b48cd1500 | -11.01486 | -54.1339 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3be876de-1f67-3a1f-adeb-2537c8361d66 | -11.13083 | -54.00486 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23d5954b-29a4-3eb8-b93a-e6618772bac4 | -16.04008 | -52.50488 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| cfb56f47-1f03-3c8b-9343-70b7dbfe743a | -11.34498 | -51.371 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef339909-9317-3c0d-bf73-49884645099a | -9.72991 | -48.15582 | 2026-09-21 04:21:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66c69cff-df81-3aeb-81f3-73999a4fd0c3 | -10.80745 | -50.83115 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 904cc1c4-256b-3de0-a2a4-82e05b53fc31 | -14.05066 | -52.06968 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f3d4fa6e-faf2-3d21-b7b0-fc159b1b3f97 | -13.93402 | -47.83838 | 2026-09-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| baa14c35-cda9-3eba-b65c-d1a903aaf0c4 | -9.97804 | -46.64044 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c299de9c-ba1a-394d-8b37-953e04af3cda | -11.85108 | -46.89376 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58f40e8f-a908-3376-9356-8236f4bb6eb0 | -11.75687 | -47.43242 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73cdc5cf-10a8-34ad-a3e9-17802ab8c17e | -10.87132 | -54.08242 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cade1169-5b59-3e8d-be78-fb4bc1fc90b1 | -14.17681 | -51.79463 | 2026-09-21 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 708db927-a03a-3d25-8bb4-4a8694815a4a | -10.80142 | -50.8391 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 619144dd-38c8-34c9-8e3f-27053259796c | -14.6673 | -54.48058 | 2026-09-21 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78d7a60c-4658-3e02-812f-c482af67e7e0 | -11.17106 | -54.1222 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 215edde4-c0b8-33cf-9959-03b371b9e314 | -13.934 | -47.8368 | 2026-09-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72db8380-7ac1-3302-b534-3b044e20cb1a | -9.82571 | -48.40816 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec0658a7-c4a1-3101-9c50-f06f1f93ee0e | -10.76542 | -50.81552 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| badfc815-7e94-3389-8222-6e629ed01d1b | -9.68018 | -54.33998 | 2026-09-21 04:21:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df756189-091b-3c9c-9707-18bf77a2d856 | -11.653 | -47.77673 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e9dd15d-34aa-38fe-bd85-4f998138a009 | -10.41807 | -50.25058 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 480dec14-cbc6-31ac-8111-5766c5935846 | -10.46069 | -50.27456 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cd1e3ee9-a950-301f-9f71-ff682b62a9b9 | -9.66954 | -54.33404 | 2026-09-21 04:21:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54a54427-735b-3f92-9d21-c89c392c6dd7 | -10.53562 | -57.44365 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 06165d3c-4ba7-321e-bbec-2e461e708f62 | -11.32881 | -47.28172 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 826beb02-9b42-3e2d-ba3b-b246da4ddeb5 | -12.30561 | -49.18133 | 2026-09-21 04:21:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 070db038-c424-3448-88ea-1b89abb84f0c | -10.77632 | -50.83119 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2938f54-637e-35df-9aed-00b51e1004b5 | -15.45831 | -48.46804 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad5b8dd0-233a-3aa4-979d-5de1bd89e4af | -11.93664 | -46.50631 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8d2d57d-50f1-336d-9287-d525259f86b1 | -11.8855 | -49.00491 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4406465e-ec90-346b-8024-4633fd70b25d | -11.94812 | -46.5006 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13375c69-f050-3be1-b76d-45c2c7cb1ec1 | -13.06401 | -50.62378 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dde3084a-d755-3fa4-a1b6-b20885168291 | -10.70944 | -50.77653 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 874b9cf2-2662-3607-ab5b-4d6bafa66baf | -10.48864 | -50.99435 | 2026-09-21 04:21:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7270473-e2fa-3d04-aa84-869bd35ac188 | -11.09086 | -51.06248 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca88b588-3475-34a4-983a-e30c9942301b | -10.47765 | -50.30304 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b660c8b4-0019-3e29-8aa8-03e13a913c65 | -7.58819 | -57.67645 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0333a423-e4d1-3a6f-bb02-9bb19e79bdc4 | -10.47056 | -50.29327 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 608f6f7f-e292-33a8-8e41-29574aced648 | -16.01054 | -52.53022 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ff4dbc58-04a0-381f-8ea6-2768c80edd0f | -11.95154 | -46.50121 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d13a980-d754-3db8-8971-22fb8012ce3b | -15.45606 | -48.48087 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2d865ab-873f-3c3e-a4b7-ce9de0d3d3e1 | -14.62268 | -52.06988 | 2026-09-21 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5baeb749-e2a0-3ea1-b7c2-2e7807a3c852 | -11.8799 | -49.01403 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72ac494e-6877-37ca-803d-4f5088d5570f | -10.87202 | -54.07884 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f1de085-4819-35fb-9cf7-2073fb2f0784 | -11.08492 | -54.03251 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eba1dda0-cb64-3e6d-b144-b210e3f95856 | -12.82085 | -54.05307 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6b5ec5e-e569-3b5a-9686-46f17eaeb96b | -10.89455 | -54.07967 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3678f9ff-f988-3e6b-bab6-504fb93a6c4b | -11.03 | -48.31849 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a567ddf-0b2a-36c0-aca5-f37c6383538e | -10.9466 | -50.61481 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f47f1b1-9281-37d4-8839-b1d7820ad444 | -11.33927 | -51.35056 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b5da32c-bbb0-3a2d-9ada-a4a075dfe526 | -10.43373 | -50.26189 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bf7a64ab-266b-3444-b475-760bfc679fa2 | -14.0441 | -52.07504 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7281b7e-76d9-3206-9a58-f10d94f1bdc7 | -13.06748 | -50.62852 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dfac1c0-6ff2-315b-b2cf-111595a0a8c8 | -10.73849 | -50.78786 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dfb83f41-8dd6-3e13-ae58-89bae9af95a6 | -12.80373 | -54.05651 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6fd6a32-b0fa-33ed-b676-97d2abbe20b5 | -10.38341 | -48.90931 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dd7117a-3c04-30f4-93f5-7ea0d08b0475 | -10.45797 | -50.27482 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6ac67257-6bfe-3501-a965-9c675fdf5e77 | -11.6731 | -43.41512 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f0b0b0a-d0c9-396e-8f37-199ce9ef6675 | -10.79466 | -50.75334 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ba36a3b-e98d-3a84-85ca-2a548f5b6d40 | -16.05082 | -52.52175 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d8fb1db0-6604-3491-afe6-383705e2ab49 | -13.33989 | -51.2979 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a39dcad8-f91b-3388-beb8-3481451699a1 | -11.67869 | -43.44544 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02074a15-7e9e-382d-ab66-5b712240f33c | -11.67199 | -43.4223 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c97074f7-6b0a-3da0-8985-4110a25548cd | -12.76861 | -52.85664 | 2026-09-21 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57ff04a7-849e-3a9f-a8b8-f46443941982 | -11.33844 | -51.35521 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b1d6f29-ef77-3ca6-ab79-d54026e0e917 | -10.70125 | -50.76739 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c8d3cd7-e847-3cd5-8ae9-bfafc39e52f8 | -10.37556 | -48.90447 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bae2bcf-4c37-3a6f-bdb1-8f3096e78a6c | -13.26661 | -51.76315 | 2026-09-21 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bccd8223-edd6-3529-b9f8-59b6fae3dc46 | -9.81963 | -48.40992 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38e09a91-3d51-3014-b4b6-082feccf04ed | -10.46497 | -50.27534 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a4f5fb4e-3a44-3099-9a70-a7135a55aa99 | -16.04094 | -52.52449 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 362a4c55-f576-357d-a59e-bf7c28171f60 | -11.41068 | -47.33818 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9e45217-a641-30cd-ada8-7e2a062ea2d9 | -15.88318 | -49.92641 | 2026-09-21 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22dbdab2-3076-3b7e-837e-b9e983f1b109 | -9.97684 | -50.26434 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d19897dd-d5d4-3cf5-9a9c-44e966e30d99 | -11.38744 | -44.05003 | 2026-09-21 04:21:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fe9f549-16eb-3382-8030-b43ea85c9a5b | -10.48333 | -50.99804 | 2026-09-21 04:21:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 838590d9-0ec3-3de4-9e6c-24e3ea1d3027 | -10.7962 | -50.74466 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 793463c9-f7d8-3966-a51b-1e754aef986b | -10.93255 | -47.86773 | 2026-09-21 04:21:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4403f838-0ab0-3a5c-b47a-d14b456321dd | -10.69204 | -50.74621 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 649a3181-b39f-36c3-811b-0782ec92a409 | -11.14741 | -42.82447 | 2026-09-21 04:21:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cd1e65da-f22c-34ed-87fc-9ab1388b3e84 | -10.45084 | -50.26506 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| dccbca54-1408-3d05-8533-99e47df579d1 | -12.4869 | -44.72187 | 2026-09-21 04:21:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed8f101c-811a-3879-9684-3766b1df36ad | -10.09095 | -50.25872 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a8a5f966-8845-38b9-b980-88d69248ce5c | -12.81188 | -54.0485 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README44.md)
