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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e35db466-7459-3770-9091-9ada8dd9ddff | -8.17804 | -61.20261 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f74630b-1f48-3162-919d-06f6114d6a5d | -12.62829 | -56.9637 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdbb08ae-bc49-3e86-b383-aaae2a9ab5f1 | -12.82757 | -47.98758 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db3fb58e-dcd5-31d9-92e3-d67cdcdef81d | -15.78115 | -53.55151 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7519da8-c4fd-3904-9431-b4084b4f6d4a | -15.26694 | -53.80475 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1153a02b-b2d0-371b-94bb-e9068be689ea | -12.81001 | -56.51751 | 2025-09-09 05:23:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff530410-21ba-3fce-98cc-ab800d2fdd37 | -11.90578 | -62.51848 | 2025-09-09 05:23:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38b9baad-a533-3b68-a153-7e6b53f4dd3f | -12.42285 | -63.8924 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89ad3d68-bd7f-3b51-9ffe-b66d557be1ee | -8.40547 | -49.10717 | 2025-09-09 05:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c530d08c-5d1b-329e-a995-cddb7f0254c0 | -12.87345 | -62.09372 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0d77b79-673c-3a54-9f2d-a7ecb103d403 | -15.26251 | -53.79796 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d35a6c5-1242-339c-9277-fe7849037d82 | -14.52151 | -53.96732 | 2025-09-09 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7da1344e-c02c-3034-9ae3-713317abcbd3 | -13.12667 | -54.92256 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fe6f8239-8742-30d8-be66-9b2ec73c12e1 | -14.62765 | -52.15928 | 2025-09-09 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99401b80-10a3-3a5d-b3a0-bd8f61ac159b | -13.13256 | -54.91352 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a85e86bb-0f7b-3b38-8200-af33d18b1eb6 | -6.26693 | -52.80549 | 2025-09-09 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d479d0d-5223-36f7-abcd-0fafd191c3b1 | -7.8728 | -61.3288 | 2025-09-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23336bf7-e85b-3608-8f5b-503f4981285e | -12.96346 | -54.76686 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc58bfad-10fa-3f57-9bc0-e48ea47b0ae2 | -14.79297 | -48.22911 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6a1b98d4-746c-33a3-9ecd-4450f36bbfee | -15.58848 | -52.90326 | 2025-09-09 05:23:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9bdf161c-1047-3e97-a088-650b96479297 | -7.55974 | -61.31034 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 966e2e23-c42e-3d02-a711-5ff8d4c43b3f | -15.78196 | -53.54464 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0e2e5a32-4e27-301e-832c-0b13e45f6c73 | -14.59778 | -52.11678 | 2025-09-09 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5cd7a11c-37df-3c26-9acd-aad95524ccbe | -10.00136 | -51.67424 | 2025-09-09 05:23:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60031534-d10c-31a0-8df3-65c706161bb4 | -12.1564 | -60.76796 | 2025-09-09 05:23:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a5aca1d-ce06-3a55-b270-2259fdd2ed45 | -12.93462 | -54.7866 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b151ef2-cc24-388c-95bb-5720ccec4ef1 | -10.28172 | -48.81387 | 2025-09-09 05:23:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5713e840-ac53-3afb-bb33-48e6de503921 | -12.93799 | -54.79707 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c9588f5-08da-3f9f-a568-d19c9d29d3d1 | -12.95655 | -54.76424 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e4996993-23c2-3663-8c47-e151f180ccb3 | -12.93398 | -54.7915 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d1920b0-3d83-3fb5-a879-af73e559358a | -15.812 | -52.26261 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7070ac99-e22e-3959-b2fe-5a0baccd909e | -12.42348 | -63.88862 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0c3dc95-b339-364b-8995-47ccf1db2724 | -12.4269 | -63.88921 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2b03300-33b4-348d-8af1-49b17e6a22c9 | -3.35652 | -52.42292 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac7dc4c4-fe0b-3719-bbc9-120357fc7b41 | -6.92003 | -62.93926 | 2025-09-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb141434-d962-3ca0-a8ba-bd2948a13078 | -14.56679 | -52.16791 | 2025-09-09 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79f19e12-5c2b-39c2-b47a-27a4ecd0e780 | -8.07122 | -50.19176 | 2025-09-09 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 813c9fd0-3ec2-369a-bda8-d3ce46c4c91c | -6.96408 | -62.93076 | 2025-09-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fad72be-3fd9-3f5c-a07f-2d52cbab80a6 | -9.24274 | -57.06391 | 2025-09-09 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 351b152e-3c9f-3147-bc99-c3555464a941 | -15.25451 | -48.81545 | 2025-09-09 05:23:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6f33204-2b30-3533-840d-0f63919057ae | -12.94253 | -54.76241 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f3f53c5-9c3d-31ad-80af-882b74d8e761 | -14.54803 | -48.76799 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a61f5d27-f0fd-3010-82c5-6c3cbf35191e | -15.86796 | -52.34695 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80af6600-8d08-3f7a-97e3-bb2c47d4c425 | -15.26385 | -52.36681 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d0682989-26e8-330a-b812-45c24f579039 | -13.02147 | -48.03296 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e1badf0-e536-35ea-b7f6-343f6961e4d4 | -9.44868 | -60.50728 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b9868ee-f9f2-3da9-8109-f5b9bb6ec51b | -9.17783 | -60.76248 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39cb9a38-323a-3594-8017-5cd03a23f04d | -16.32458 | -52.91969 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| be888c6d-f526-3029-bbed-6de816733291 | -18.82641 | -49.69036 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 741ac338-e407-391b-adb4-556b57ba9235 | -9.22462 | -59.5173 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4c29135-d84f-3140-a85b-0d46dcc1fa57 | -10.77638 | -59.8542 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9721905-4045-3255-90b6-cbc81a8b614e | -9.08576 | -61.41201 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ad364a7-8061-398b-b367-79f6f29151f0 | -9.17635 | -59.37376 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fb9790c-a150-3281-a48c-edd2107b3dad | -9.06285 | -62.34004 | 2025-09-09 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a861dcfb-6915-3304-af3f-b98fe52b1617 | -9.21 | -67.55668 | 2025-09-09 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cee394ae-696f-30a6-8701-2cb1c2492537 | -11.21126 | -54.99717 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 859d9c18-b3ea-32b9-b7a2-d5eb99b12dbb | -16.35024 | -52.94105 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67fc35ab-f64a-3059-9318-2a274bc523a0 | -16.32972 | -52.9239 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0b2ee908-2e44-378a-842a-639eea5ef66f | -9.95193 | -60.14521 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4981e36-20da-391c-b41f-13be87ee923b | -9.45886 | -60.52716 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d97ff2de-aefc-3638-9928-cdf16b948ee1 | -17.67173 | -52.25223 | 2025-09-09 05:25:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16ede142-3128-3cfe-8952-3c80ffce7bd4 | -9.79922 | -59.81404 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58113933-0d99-38e0-ace2-d7dba9187f0c | -9.44037 | -60.5168 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc759936-e5e7-3cc0-93ab-cc8539d69fac | -9.2221 | -60.82708 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5b76f8b0-3dd1-35ac-b47a-2a7a5310487d | -9.34521 | -65.44185 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bce7be1-a962-3736-bad7-fc895f5bce26 | -11.16165 | -57.1897 | 2025-09-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 00fe3794-bc5f-31f3-a6c0-9f312771c9f7 | -9.4426 | -60.52436 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8c40449-6f04-382f-8d9a-5a1fc9a55533 | -9.16839 | -59.38014 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f4dd279-f970-3492-86fe-c0bf637abcb7 | -9.60815 | -55.0111 | 2025-09-09 05:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3eddfe98-42ce-305f-b8e3-566a43317c07 | -9.13576 | -65.96014 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2041f80f-16ab-3cbd-95bb-d1d213cfbaee | -9.38905 | -65.93967 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fe4bd7b-76e8-3083-93fd-61cd056f9c7d | -10.02812 | -63.47726 | 2025-09-09 05:25:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e5a8056-bbdc-345a-be74-70d082960d77 | -9.13702 | -60.52283 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bb71ba8-59fa-3c72-b823-07c015582a44 | -9.46655 | -60.49949 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de58ad36-fd64-3f50-b584-2b2ad72131e9 | -9.75448 | -65.01852 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a105aa85-b810-3f20-9a04-6fba785c7b6a | -9.98937 | -64.98257 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d4b3d04-85b9-3d21-b037-e86f0a227bf0 | -9.11782 | -61.48897 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c0d8c12-7f04-3a27-87bf-f577bb3bdfda | -16.34465 | -52.94093 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d15bfcb-4f30-35cb-8042-65a5d995d80c | -16.69617 | -48.63137 | 2025-09-09 05:25:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0ae6f84-6d8c-3e2e-9d94-91dce2881593 | -16.32856 | -52.93446 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2dc8591-6727-3b39-9460-f911787b0b79 | -9.23257 | -59.55621 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a505991-e831-34b4-a326-ee6912498219 | -11.2196 | -55.0029 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bce39d8d-5186-3a48-ad38-eaf69c8817ae | -9.22179 | -59.5131 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1fb7e21-a04c-36f5-808c-3a46df18aebd | -11.95032 | -50.97182 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| faa9f331-9597-36fa-b0e4-6f2c8c9e48ac | -18.826 | -49.68982 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f30b9bb0-5b37-38d0-aaeb-ed37359211b9 | -11.55231 | -49.04697 | 2025-09-09 05:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a614d4b0-7f75-3b7a-bc0d-e4699029d018 | -9.20123 | -67.55514 | 2025-09-09 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8a85564-0aa1-3b6f-9bbe-f6628483e9e0 | -9.46933 | -60.50353 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14c0d1ce-3f14-30f3-92b9-fa04f4918f5f | -9.45821 | -56.04971 | 2025-09-09 05:25:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 610d6e2f-0480-3063-aba1-160914595e7a | -9.19105 | -60.39436 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e72e5d0d-1eb5-39c4-9018-e058e8c69277 | -9.12304 | -65.9631 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 490aae7e-b988-3fd8-87fb-85cb614650fa | -9.94406 | -60.12924 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc1cc923-96d4-33f4-9ef8-27731cb39129 | -10.41094 | -60.79976 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1822c3d7-3afd-3ea3-9003-655ff793d5e0 | -9.16782 | -59.38385 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cbf6853-d52c-339c-a133-11a1f97f220c | -9.17409 | -59.36578 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4136aa53-7aa0-30f2-944b-7d8b94a0cfde | -9.48205 | -60.48749 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a5637f3-fe89-3cfa-80c0-fb8122dbb920 | -11.979 | -51.01326 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64ed0187-2db3-35e6-821c-85282abb5d74 | -9.08374 | -65.40854 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9469810c-03b0-3e40-a401-c68974f8e302 | -9.10528 | -60.98683 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e402944-2e19-39de-a0d3-e256796d28d6 | -9.93077 | -65.23973 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README63.md)
