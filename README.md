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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 949be491-0550-35e9-a84d-46fac036ea9e | -10.0548 | -48.6452 | 2025-06-10 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| bac8158a-9a45-337e-86d1-dcdb5457387f | -6.1853 | -43.3257 | 2025-06-10 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 9ebb81b7-99cb-39eb-9137-623022300a9f | -6.204 | -43.3241 | 2025-06-10 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 85b98586-f98b-3d56-9f7b-d977ce7e0317 | -10.0356 | -48.669 | 2025-06-10 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 8cec0e8c-de44-314e-bdd3-defe1d932085 | -10.0545 | -48.667 | 2025-06-10 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 206.8 |
| e5ede869-931c-3d17-9f38-8853eaf6bfad | -5.6577 | -43.6001 | 2025-06-10 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 33e952f9-40b7-3ea2-a5bd-b55fb760d0d4 | -5.2108 | -43.3067 | 2025-06-10 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 9bbcdb06-0c7a-37c1-864f-a3bd2e768b4b | -10.8382 | -53.7648 | 2025-06-10 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 42ea2f66-080a-3ac1-9f5e-16489d939742 | -10.2864 | -46.9881 | 2025-06-10 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| f89e2761-6627-3b11-b94e-c296c758f77b | -5.2106 | -43.33 | 2025-06-10 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 6d2c30fc-3584-334a-a1c5-7b00e692cfbd | -10.0545 | -48.667 | 2025-06-10 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 11d132c6-f0d7-3507-be54-f7d9116ee5e2 | -10.0356 | -48.669 | 2025-06-10 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d5200dab-9a04-3ef2-bbab-d3f510da78aa | -6.1853 | -43.3257 | 2025-06-10 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 97df599a-9acb-3839-92de-7737fbfe14d0 | -5.2108 | -43.3067 | 2025-06-10 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 171.3 |
| ae90b8ff-a240-3062-89cc-58ebd839dab0 | -10.0548 | -48.6452 | 2025-06-10 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 3b5641b5-b7bc-3eeb-8957-ba8fee30034b | -6.204 | -43.3241 | 2025-06-10 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 160.0 |
| f74e6e3e-44d1-3453-b50e-e783c561ea9d | -5.6577 | -43.6001 | 2025-06-10 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 940a33db-de25-3e74-bca9-d201f7bbfcac | -5.2106 | -43.33 | 2025-06-10 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 66bb3fb6-faa6-37c9-98f1-97410dac3d96 | -5.6577 | -43.6001 | 2025-06-10 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| bbb367b6-e4b5-3e5e-b72a-9ccc5e9780ca | -10.0356 | -48.669 | 2025-06-10 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 415a1f80-2593-36c3-aa22-c58bf988ef40 | -6.204 | -43.3241 | 2025-06-10 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 32eda3bc-f7cf-3d33-8e2e-ad20a5b33d55 | -10.0545 | -48.667 | 2025-06-10 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 21d80e9d-d128-36a6-9aed-5d762b01a3cc | -6.1853 | -43.3257 | 2025-06-10 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b891aaa7-5b1f-3ef9-900c-fbecbd419129 | -10.0548 | -48.6452 | 2025-06-10 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ccdd7a59-7993-3a16-8886-3a2cf6d35516 | -5.2106 | -43.33 | 2025-06-10 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| a35ec50e-4b6c-33f1-bafe-d7295f96d4dc | -5.2108 | -43.3067 | 2025-06-10 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 00a2f482-252a-338b-8729-1969a31b4b10 | -5.2108 | -43.3067 | 2025-06-10 00:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 17fbf168-3c5e-3cfb-a1c4-ba8851e33037 | -6.204 | -43.3241 | 2025-06-10 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 7d22abed-5e8e-3003-9929-e7f18e436441 | -5.2106 | -43.33 | 2025-06-10 00:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| cf710d03-fb5c-3f4a-96fb-e1679dfb9f0b | -10.0545 | -48.667 | 2025-06-10 00:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 191.2 |
| cbbde73e-3e25-3341-a8c9-5b04b64cf380 | -10.0548 | -48.6452 | 2025-06-10 00:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 9a7d6b68-0d9a-377a-a757-acf02e32fee6 | -5.2101 | -43.3134 | 2025-06-10 00:34:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cce6b37-fdb5-3a76-b861-5b9c3495005f | -11.8986 | -47.443802 | 2025-06-10 00:34:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7860cda-a590-3773-9315-2e938b74f8df | -5.6346 | -43.5839 | 2025-06-10 00:34:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5c8316b-797c-36cd-b366-aff747d4ab3d | -14.1939 | -45.483501 | 2025-06-10 00:34:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d098a46-f4e4-3e5a-82df-587f8a1e6724 | -3.5893 | -49.435902 | 2025-06-10 00:34:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65984fdc-614b-370f-8dce-c84c0b5193f8 | -10.0569 | -48.6516 | 2025-06-10 00:34:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c0f89b4-9f81-3486-9cf6-291bc8177b07 | -8.3362 | -48.4431 | 2025-06-10 00:34:00 | METOP-B | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e22f8ae0-8e18-320f-a215-49f166464cca | -8.9676 | -47.970501 | 2025-06-10 00:34:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91fb8950-4e9a-3c41-8b8e-218824569958 | -13.0656 | -49.247601 | 2025-06-10 00:34:00 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e59ecce6-5f2e-3521-a0c3-5f2cc055eb1a | -7.2778 | -49.565601 | 2025-06-10 00:34:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 470f9b93-d67f-3793-b08d-536c687b6b4b | -12.2917 | -50.103199 | 2025-06-10 00:34:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b82b745-cde4-3d9c-a39a-57d10a78222e | -5.2046 | -43.2906 | 2025-06-10 00:34:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 16517197-4db6-3b54-86ba-1ce7c171a89e | -9.0297 | -51.1325 | 2025-06-10 00:34:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cb6e46a-3719-3827-9f48-a861ae20f2e1 | -5.2005 | -43.3158 | 2025-06-10 00:34:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0907c28e-0d62-3160-8cd7-39be18669c61 | -10.885 | -54.3074 | 2025-06-10 00:34:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f32a943-a6b8-33e5-bf1d-9ef80f4866e8 | -12.212 | -49.620098 | 2025-06-10 00:34:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e716997-3ac9-3a7b-a337-ef00c5c7d1f3 | -5.6442 | -43.5816 | 2025-06-10 00:34:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4a97c43-a57d-3a96-881b-f614f2028395 | -10.0512 | -48.671398 | 2025-06-10 00:34:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12e22bf2-7bf8-34e2-bb5d-44cbe36fd71c | -10.8834 | -54.299801 | 2025-06-10 00:34:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9a2b36b-844d-3d39-b78f-eff37592a9b1 | -11.2652 | -52.465801 | 2025-06-10 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a32298da-deb6-3272-8bfe-6986005aec9b | -20.099899 | -50.8629 | 2025-06-10 00:34:00 | METOP-B | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0df06f45-4f0e-3d14-98fb-8caed905090f | -10.0589 | -48.660301 | 2025-06-10 00:34:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a53fc12b-7a92-3478-a904-51a9f7dba4a5 | -13.0958 | -52.274799 | 2025-06-10 00:34:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3a1460a-913f-3e7a-b77e-18f37417e97f | -12.29 | -50.095798 | 2025-06-10 00:34:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72549377-cf20-3317-b405-f612bb29a88c | -10.2739 | -47.604 | 2025-06-10 00:34:00 | METOP-B | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a18546d-702e-37b1-a90e-b486684e0b98 | -6.1917 | -43.308498 | 2025-06-10 00:34:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62006289-7a21-376b-a301-07c20d5e1041 | -8.6034 | -46.5742 | 2025-06-10 00:34:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39e96883-ca0c-34ad-9965-638bd08260c2 | -11.9069 | -54.818901 | 2025-06-10 00:34:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16ca8f48-328e-30d7-8c14-17c5643a1f17 | -11.77 | -54.367199 | 2025-06-10 00:34:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c28a2bf-2198-3e02-ad49-6907ae80c824 | -10.8483 | -53.756699 | 2025-06-10 00:34:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c025991c-d483-3217-aec2-766aa95312a9 | -11.7684 | -54.359299 | 2025-06-10 00:34:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24259b2e-ec2f-31d1-b2a2-11f953ed1c17 | -10.2159 | -46.929501 | 2025-06-10 00:34:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20a978d5-0fd6-3100-b18a-b9f73f41a120 | -7.471 | -45.512798 | 2025-06-10 00:34:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d560d4a2-11c6-3abb-a7b6-63fa16999b3f | -10.0471 | -48.653999 | 2025-06-10 00:34:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54ffc2cb-765e-3fec-b189-3d18c342f29b | -15.3871 | -47.117599 | 2025-06-10 00:34:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 590cc293-08bd-326e-a422-7f09c7255577 | -10.3684 | -57.491501 | 2025-06-10 00:34:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4fb1e8a7-d149-34c4-b596-b15202e10ca8 | -6.1875 | -43.332802 | 2025-06-10 00:34:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd75cfff-1005-3d54-b3a1-31c4cc777eb8 | -8.9652 | -47.9608 | 2025-06-10 00:34:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64967e9a-616e-3759-90dd-665bca5f5495 | -7.4674 | -45.4981 | 2025-06-10 00:34:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 281f53b4-a608-3ef6-8c8a-2b1686d6a41b | -14.0475 | -55.121101 | 2025-06-10 00:34:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 514acc39-9967-39e7-b89d-c79dc214aaec | -10.0491 | -48.662701 | 2025-06-10 00:34:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 806dd94f-81b3-3bb9-ba59-32d0939aeab9 | -14.0377 | -55.123199 | 2025-06-10 00:34:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c4aef74-1b4e-3b06-8c51-a48f13b4a2d7 | -10.8515 | -53.7714 | 2025-06-10 00:34:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8bd1251d-94c1-3ccb-9a43-a5c397e77f31 | -10.2256 | -46.927101 | 2025-06-10 00:34:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6173679a-ac5f-320a-a550-bfefc1ecbf20 | -12.2218 | -49.617699 | 2025-06-10 00:34:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cfd0a60-5194-364f-b0d6-274fc30ab6c8 | -3.5872 | -49.426601 | 2025-06-10 00:34:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b675728a-fdea-3ea4-a77c-6c1d999ff82b | -11.5656 | -47.433601 | 2025-06-10 00:34:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51999634-8e91-305c-8c31-97c9e978bc2b | -14.0396 | -55.132301 | 2025-06-10 00:34:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a26cd1ae-f21a-3541-acff-76f7bf2b77d3 | -6.1971 | -43.330399 | 2025-06-10 00:34:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a0d2caa-b88c-3360-b67f-76122e47882b | -7.0047 | -44.612598 | 2025-06-10 00:34:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dcfbb665-ef29-3a55-a090-2658961b9230 | -12.7114 | -57.999901 | 2025-06-10 00:34:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4439af97-ffa2-309c-8544-ad637cd5bce1 | -10.2122 | -46.528702 | 2025-06-10 00:34:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cfaa67d1-24ae-3a7d-b4f8-e4a328b6a3d7 | -12.2998 | -50.093498 | 2025-06-10 00:34:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88c6dfa0-8fa8-3f12-a2c6-f0719f4b617d | -12.7166 | -58.0261 | 2025-06-10 00:34:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f9e35de-4ac5-3130-b23f-9276ccd70b25 | -10.061 | -48.668999 | 2025-06-10 00:34:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71efa0db-4988-3723-b5a6-b3ea93d98bad | -12.3015 | -50.1008 | 2025-06-10 00:34:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d11fb28-7d76-36e4-9534-44712978c30c | -5.6495 | -43.603001 | 2025-06-10 00:34:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 854db42e-6ee7-3769-9e19-d95513e310ab | -9.218 | -48.860001 | 2025-06-10 00:34:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4d41697-43bf-3cd4-92ee-f32282127ea7 | -11.5898 | -51.331299 | 2025-06-10 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7c447d5b-7e75-30e7-9b78-bea5830a825e | -10.8499 | -53.764 | 2025-06-10 00:34:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 694261e8-bd43-3efb-b6b4-275544d765d5 | -12.714 | -58.013 | 2025-06-10 00:34:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e3cbf6b4-3b36-3048-8db2-a1aaf60d6af7 | -13.0638 | -49.239899 | 2025-06-10 00:34:00 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d4a41e6f-b5bc-350f-ae3e-0892674f034b | -9.3946 | -48.4249 | 2025-06-10 00:34:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dec54b59-7873-3a84-a789-dec55f32a85d | -3.0425 | -49.430698 | 2025-06-10 00:34:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb3bc2ac-8bda-391b-bf4f-d1530f830c27 | -10.8385 | -53.7589 | 2025-06-10 00:34:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60cb8659-d934-3d14-bc17-60a4ebf77571 | -10.8401 | -53.766201 | 2025-06-10 00:34:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01396fbc-c20a-3141-9a72-ef4ad0cc1269 | -9.0314 | -51.139599 | 2025-06-10 00:34:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87e574c3-acf9-3b92-a905-40eeb1eb561e | -14.191 | -45.471802 | 2025-06-10 00:34:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 53649f54-73d9-3a30-a411-8bca0612ea35 | -11.7717 | -54.375099 | 2025-06-10 00:34:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
