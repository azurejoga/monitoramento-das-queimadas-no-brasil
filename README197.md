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

## Dados Diários - Página 197

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ce5cbbc-4bf7-3254-be04-91d1a63ae304 | -12.9225 | -45.8352 | 2026-08-31 19:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| e0522723-6fb1-398a-bcc1-ce229a54439d | -8.5969 | -54.7755 | 2026-08-31 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 4b7f242f-4bef-37fe-ae2f-22b60fe5cebb | -12.0921 | -45.0192 | 2026-08-31 19:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 00b5d77f-639e-3ba3-9708-3f9c1dfbbd18 | -16.0352 | -54.3933 | 2026-08-31 19:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 149.0 |
| fc89a3a7-3e30-3ace-80a0-60cbf2cd4d7b | -9.1961 | -64.438 | 2026-08-31 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 045aec58-a737-34bc-b429-6a33366f9641 | -11.4972 | -45.084 | 2026-08-31 19:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 5afe7681-b987-3653-92e8-e2be71032bef | -11.1995 | -55.1008 | 2026-08-31 19:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 1487e091-4f68-3031-800f-9326497f7ef1 | -9.1895 | -59.6364 | 2026-08-31 19:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 66f8521b-5215-34ec-8a6b-61dbbab3d185 | -6.1109 | -57.684 | 2026-08-31 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 49b47afd-fbba-312a-ba7e-f6b186c08033 | -7.6804 | -55.3555 | 2026-08-31 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f8f241ca-31bc-3c6a-bc0f-24f818828f94 | -14.5028 | -52.1913 | 2026-08-31 19:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b391704b-53f7-3744-9b4b-4951d8d0607a | -4.9788 | -55.8417 | 2026-08-31 19:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f75d5712-0f13-3fbf-9261-27d8481716dd | -7.6251 | -55.2987 | 2026-08-31 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 255.6 |
| e1dfcb95-7054-34f8-ad8b-e6bbef327e54 | -7.6991 | -55.3344 | 2026-08-31 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| dce6dcbd-c263-34f6-a2f9-19c3154cbb8c | -17.3228 | -42.6878 | 2026-08-31 19:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 301.5 |
| 5ca54985-5247-3166-a4b5-d682d95bf9b9 | -9.8434 | -64.9777 | 2026-08-31 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| d05ae75c-44a2-345c-b3a6-e0fc7c5cd151 | -8.9481 | -62.3704 | 2026-08-31 19:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 02e56c6b-692e-356c-b87a-7619620d5501 | -15.9703 | -55.9583 | 2026-08-31 19:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 96.7 |
| 5dec9aa7-6959-3e05-8678-07d47dc08c80 | -8.87 | -66.8935 | 2026-08-31 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 348.7 |
| 24a63d5a-f7c8-35db-af4a-4549abf7fd52 | -12.1905 | -50.5194 | 2026-08-31 19:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 5017d62f-94ec-370e-94de-0484b4f5d2de | -8.8521 | -66.7641 | 2026-08-31 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| fd3a305a-7148-350e-bebc-ebca2537879b | -8.87 | -66.9121 | 2026-08-31 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 196754d8-5614-341f-beb1-1ed3fd4350ca | -6.3844 | -55.2251 | 2026-08-31 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 14ee31af-9bf2-3dcb-a727-a9d686364fb5 | -7.6079 | -57.616 | 2026-08-31 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| c45e5403-f4ad-3d0f-894e-21ac1110bd55 | -17.3027 | -42.6926 | 2026-08-31 19:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 842dd2ac-2b57-30db-bd00-8673b4332e5a | -9.208 | -65.8044 | 2026-08-31 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 3fb64974-49bc-354e-be92-6a4a8a7618df | -15.6333 | -56.4081 | 2026-08-31 19:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c1b278aa-e4c7-3c80-8b6e-7e7ec114c8a0 | -5.2547 | -55.9105 | 2026-08-31 19:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d6f19e1f-3b40-312e-83fb-23476fd24f09 | -10.1324 | -45.8598 | 2026-08-31 19:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 510.0 |
| 83e95538-5ff8-34ca-8042-429abdcf8137 | -9.1897 | -59.6171 | 2026-08-31 19:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f25156c2-5fdf-398a-99e5-3d9684c6268d | -10.8631 | -45.333 | 2026-08-31 19:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 539.2 |
| 7dceb887-2326-36aa-bed3-6b1379e279a5 | -9.9708 | -53.9419 | 2026-08-31 19:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 042a2e67-a953-3abd-9c59-cb9087deb79c | -15.2278 | -56.3512 | 2026-08-31 19:30:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| cce6708d-129d-3e78-b0a8-0a33434b6067 | -5.8537 | -57.5576 | 2026-08-31 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 0569bb7d-09bc-3253-8e03-fe39a870fd38 | -13.5341 | -59.7589 | 2026-08-31 19:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 6f43e097-4424-3bbc-9fbd-f2b0ec51ab67 | -10.3394 | -49.9547 | 2026-08-31 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 4328d2bc-c0c2-360d-b0b8-e52f7e4f44ad | -15.6139 | -56.4103 | 2026-08-31 19:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2ce61859-b25c-3521-83af-30909f3bb1ac | -13.471 | -57.0373 | 2026-08-31 19:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| e89c0547-1121-312b-b6dd-f75667e04702 | -15.6142 | -56.3898 | 2026-08-31 19:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e1016921-48e8-39c6-86dc-bed256afb75e | -10.301 | -50.0016 | 2026-08-31 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 1e857d3f-d3cc-36f0-a3ff-f805137e52de | -7.6805 | -55.3355 | 2026-08-31 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 4cc43d54-d3b3-39db-8062-34daf3b2cb51 | -8.8705 | -66.7822 | 2026-08-31 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 254.6 |
| 9991cea5-7682-30d1-a067-b4d05d6984f8 | -5.9636 | -57.6704 | 2026-08-31 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 8cd7c4cc-7d90-3d52-9c8a-c9ae4f08cd81 | -14.444 | -53.4016 | 2026-08-31 19:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 47571172-183e-37c1-8a92-14d3b944c372 | -4.9604 | -55.8424 | 2026-08-31 19:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| f2201f14-c2a6-3288-b5e3-f9afdedf3f28 | -18.27 | -52.7068 | 2026-08-31 19:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 460.6 |
| ba37f254-f402-3704-9a2e-60ec21ef274c | -11.0936 | -51.5134 | 2026-08-31 19:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 312.7 |
| f0fae246-bc6a-3793-b83b-29280d43ea81 | -9.4721 | -57.0156 | 2026-08-31 19:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 105.0 |
| bbdf9985-ce89-3f1d-aa99-ca887c233ad1 | -11.4776 | -45.1099 | 2026-08-31 19:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| c15b0a9a-0152-3823-8c4f-e5caf0850ec4 | -10.1321 | -45.8825 | 2026-08-31 19:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 505.5 |
| b036f13c-b84d-3bf0-86fa-e01880493817 | -10.1134 | -45.8621 | 2026-08-31 19:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 542.3 |
| bb5102eb-8f1d-3192-99b1-f888192b666b | -6.3875 | -54.7646 | 2026-08-31 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| a40b1835-d437-3c46-8717-32d44c14a032 | -8.4235 | -44.9849 | 2026-08-31 19:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| ca27efb2-2626-3c66-b7c2-bf48f4252e56 | -9.2144 | -47.99 | 2026-08-31 19:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| d7e801fd-dd16-3f5f-9084-1e2ab144dcc9 | -5.2548 | -55.8907 | 2026-08-31 19:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 1f14d6a2-1e0e-32dc-b122-dcd22aacc14c | -10.7591 | -54.0794 | 2026-08-31 19:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e1907c75-2e55-3709-856f-6c949623791e | -9.908 | -67.0131 | 2026-08-31 19:30:00 | GOES-19 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 4800127b-964f-32f8-b376-67843a641935 | -13.4707 | -57.0574 | 2026-08-31 19:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 9d5f7274-1800-3eab-a41a-6b38cb2a8636 | -10.844 | -45.3356 | 2026-08-31 19:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| 35588816-f574-340a-a1a5-a712c6b9eec2 | -9.9896 | -53.9404 | 2026-08-31 19:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 2b8b9757-c669-385d-a0da-c1bbab0bd132 | -4.7941 | -55.967 | 2026-08-31 19:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 23aad655-c907-379d-901e-37d49340d29c | -18.2695 | -52.7284 | 2026-08-31 19:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 157.3 |
| ed4d612e-a411-3fa2-9268-4f2741f2280f | -9.1615 | -60.9484 | 2026-08-31 19:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| b1273c19-ef08-3a66-9b03-7343b98dd9b9 | -10.9672 | -48.4111 | 2026-08-31 19:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 68ad326f-09d2-3e33-99f0-229352b21de2 | -9.1419 | -61.1027 | 2026-08-31 19:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 081080b7-1dd6-39d8-85b2-76ac28860997 | -15.6336 | -56.3876 | 2026-08-31 19:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| b02a2bcc-769a-3b8e-b6a2-75f505c80847 | -15.0053 | -48.1496 | 2026-08-31 19:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 02e54be5-0b2c-3db7-a883-763d39c2d9fb | -9.1711 | -59.618 | 2026-08-31 19:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3df543fe-6345-3ca7-9c9f-16c20499e525 | -6.1294 | -57.6833 | 2026-08-31 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 49f729c0-d9de-3e06-a47e-39f0c28d5d6b | -9.4351 | -56.9784 | 2026-08-31 19:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 16a206aa-09f7-313b-97b6-14413f6731eb | -9.4153 | -45.6726 | 2026-08-31 19:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 8d8ef131-de7b-381a-a3b2-fa821b314d74 | -7.0293 | -55.6312 | 2026-08-31 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 1e5298b3-d48b-3b77-81c6-b67384b1d7c2 | -9.173 | -59.3659 | 2026-08-31 19:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 26d41855-7106-3135-aa82-788ebcaae896 | -10.3205 | -49.9567 | 2026-08-31 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 6716e0c1-ecbf-3de0-bc78-663b76913678 | -7.6149 | -44.8833 | 2026-08-31 19:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b4cfbf6e-dd36-3f98-bb9f-8dad2bfb4dd1 | -11.6975 | -54.5467 | 2026-08-31 19:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 24dcf5ec-1919-3173-b6e9-dd3cd1af9e86 | -7.6066 | -55.2998 | 2026-08-31 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| b3ccf6ce-0ed3-386c-8615-64e8748acabb | -16.5773 | -52.519 | 2026-08-31 19:30:00 | GOES-19 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 392.5 |
| c26190ff-8625-38ea-a2a7-4b15898b51c3 | -14.1459 | -52.7871 | 2026-08-31 19:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 72e45328-dca2-38dc-83a3-a76dc875185d | -10.4634 | -46.5638 | 2026-08-31 19:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 1ebbb231-2372-3e37-8807-908e3d145504 | -16.5581 | -52.5004 | 2026-08-31 19:30:00 | GOES-19 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7b12eadd-0783-35a4-b34f-d6618aa1b278 | -10.7593 | -54.0589 | 2026-08-31 19:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 4aec20e8-febf-3939-beb0-a99db1643914 | -8.5177 | -55.3039 | 2026-08-31 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c346fa24-7900-304a-87e2-74765b8edd60 | -14.2599 | -52.8782 | 2026-08-31 19:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 5aaf93aa-5c2b-312c-8f63-6d34dc43db88 | -10.8043 | -50.5259 | 2026-08-31 19:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 6fdaa1be-57cc-3b13-84d0-5d351fcbfefb | -15.7349 | -56.1093 | 2026-08-31 19:30:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Pantanal | 118.8 |
| 9f726a53-4fe6-30f3-801f-ba4136885808 | -12.1113 | -45.0163 | 2026-08-31 19:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 56b3ba09-6b08-311c-8f89-bdeef1ba45c3 | -14.6145 | -53.59 | 2026-08-31 19:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 79d1f0ab-fa7f-3912-98f5-d1a9344ada94 | -10.8444 | -45.3126 | 2026-08-31 19:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 319.9 |
| 200532cd-fe5f-3a2e-93e3-098ebffd2b5d | -15.5038 | -56.0128 | 2026-08-31 19:30:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 367b7f01-b07e-3f9a-b6c6-b0eba1bd29a8 | -10.3199 | -49.9996 | 2026-08-31 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| f6c6c0c8-a730-343a-b552-5905820d06c9 | -10.5719 | -57.495 | 2026-08-31 19:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 47baefb9-413c-3cad-aadc-1a04d3c36b7b | -11.5009 | -60.5867 | 2026-08-31 19:30:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 3b1da46a-1f6f-3ed3-9a83-0630c49a78c2 | -11.4828 | -58.5159 | 2026-08-31 19:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| ba84573f-482c-3651-a066-84c578ed6d5a | -8.8885 | -66.9116 | 2026-08-31 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 46b30339-6181-3365-9425-a75ff7420b2c | -14.5623 | -52.0984 | 2026-08-31 19:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| f7cc3843-32d7-37f3-b1ef-059d86737363 | -7.6264 | -57.615 | 2026-08-31 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| f1f01846-a051-352d-82dd-421af94decaa | -7.6253 | -55.2787 | 2026-08-31 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 53f484ff-164a-3a63-b0f8-ea5d89e8c7a7 | -11.6786 | -54.5484 | 2026-08-31 19:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 88ae359b-b0c9-3d05-b2e9-7072b9cbe9d0 | -7.0292 | -55.6511 | 2026-08-31 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |


[Clique aqui para ver as próximas entradas](README198.md)
