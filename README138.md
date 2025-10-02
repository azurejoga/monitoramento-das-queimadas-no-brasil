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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b48218f5-7796-3bf6-b675-c3f1d30d258f | -7.77884 | -42.50924 | 2025-10-02 05:55:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 63041270-c893-3c8c-8237-24202a7c9440 | -10.22363 | -48.21927 | 2025-10-02 05:55:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 479d98ea-d336-363f-8920-72c29d879ed6 | -7.7193 | -46.21671 | 2025-10-02 05:55:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 79f8364c-9bf4-34e7-adfe-e541c6dbccaf | -3.09778 | -47.00568 | 2025-10-02 05:55:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 557122db-9988-368f-a561-b29899b460ed | -8.57225 | -49.59707 | 2025-10-02 05:55:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2db55974-1e34-3964-8568-5b6e830bb203 | -6.66417 | -42.78992 | 2025-10-02 05:55:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 772ea60c-d9bd-3df9-befe-fdf7b5433617 | -11.18267 | -47.26331 | 2025-10-02 05:55:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 58449fe2-715c-364d-8dbc-5923a1b7938f | -8.8955 | -46.61832 | 2025-10-02 05:55:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0990b1c5-3a83-319f-a917-24e874062697 | -11.03522 | -47.8125 | 2025-10-02 05:55:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 519857c8-dd6c-3f36-a60a-0cce530830c9 | -6.22427 | -45.33545 | 2025-10-02 05:55:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9c4543d3-b4b7-381b-8f01-08ceede99f84 | -2.9248 | -48.29714 | 2025-10-02 05:55:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 72de502e-6d5f-3477-aab6-47b6ead75a72 | -9.32899 | -45.71009 | 2025-10-02 05:55:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e9203c6d-a092-33da-bc4a-2bd3f58a21be | -11.19484 | -47.18303 | 2025-10-02 05:55:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dc515ad0-7df4-3165-b44b-f96734c3cbbe | -10.99622 | -46.60584 | 2025-10-02 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| ff64967f-8841-3408-bd2f-bd74a2c8c3e6 | -6.72438 | -44.14896 | 2025-10-02 05:55:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 86680494-fb35-3ea8-bc46-df4b04b0d32f | -3.33862 | -43.18953 | 2025-10-02 05:55:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ed261c21-d2ba-33c8-8511-d0d6efda2967 | -11.06328 | -47.80766 | 2025-10-02 05:55:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6447e0a2-bff1-3a68-ba2b-f58ffb0ab9d4 | -7.78905 | -42.51079 | 2025-10-02 05:55:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 6d5fefa2-3d29-32d6-b07e-fc2b5d5d6491 | -11.46747 | -45.02531 | 2025-10-02 05:55:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 9ab19144-d3c7-3b7d-bb87-3e6bb44a1588 | -10.99489 | -46.61474 | 2025-10-02 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1a928bfe-dfd5-3f66-a3b6-62b2b88f365b | -10.82079 | -46.60339 | 2025-10-02 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 7b17fedf-185d-3649-beee-0e628a1ab640 | -9.94277 | -43.70805 | 2025-10-02 05:55:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| f241cd01-9725-3a5b-8ee8-5171fd03dc77 | -8.56796 | -48.63831 | 2025-10-02 05:55:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d18395c0-4961-3dd9-a53f-57a1590fc33f | -3.69289 | -49.56832 | 2025-10-02 05:55:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1add6d9e-fabe-3988-bbe5-c9a756516b8d | -6.33248 | -43.03701 | 2025-10-02 05:55:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 956833d4-c759-3326-9761-636bedf255ef | -4.59125 | -38.44621 | 2025-10-02 05:55:00 | AQUA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| dd9af742-11d4-3418-8a56-6d75967d2df8 | -9.04801 | -46.65372 | 2025-10-02 05:55:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 210a1f84-5cc1-37cf-9600-c717cd6efe9c | -10.22507 | -48.20991 | 2025-10-02 05:55:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 605e9d7a-1c80-3c00-91a0-19aed3229140 | -5.61759 | -43.24543 | 2025-10-02 05:55:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7e5e5c5b-cc02-3944-9945-c31e331ef931 | -4.24853 | -48.56046 | 2025-10-02 05:55:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7ddd64e5-4696-3a37-b528-e2b9b4190656 | -5.70604 | -42.69501 | 2025-10-02 05:55:00 | AQUA_M-M | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| bbb34759-ec1e-3923-800f-748cb2a84524 | -9.33784 | -45.71142 | 2025-10-02 05:55:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0c439b0c-8ff3-3ab1-a841-bdb90e3bd088 | -11.17115 | -47.27987 | 2025-10-02 05:55:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 70eb0d48-1f4c-3637-a2d4-baef50a8978d | -11.08994 | -47.81193 | 2025-10-02 05:55:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f3251096-d41a-3202-9e3c-023879da1e57 | -4.42499 | -47.74882 | 2025-10-02 05:55:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 115e433d-299a-394a-81e0-84c786633ae2 | -9.39825 | -47.57266 | 2025-10-02 05:55:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f9169760-4815-37cb-baf6-3e4cd0eed268 | -6.23659 | -45.32582 | 2025-10-02 05:55:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 775355bd-bf43-3874-972c-d5f4a13a5769 | -11.47451 | -44.97584 | 2025-10-02 05:55:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 21901f3e-182b-33ac-bc52-1a57e497ccf5 | -4.44932 | -43.23314 | 2025-10-02 05:55:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3c52b220-6c85-3c0a-a414-544dfc7dfc27 | -9.43747 | -45.46764 | 2025-10-02 05:55:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b9cb7aa2-6ba9-3a2c-acae-22c242c6eda7 | -10.27255 | -50.32608 | 2025-10-02 05:55:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f38e1738-ae14-3a75-89fb-7b89d37204d0 | -6.95809 | -45.31198 | 2025-10-02 05:55:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 71cba6f7-9b2f-3c06-ab64-baa64005e524 | -6.95675 | -45.3209 | 2025-10-02 05:55:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 126207cd-c917-3b21-a540-ec345dde8095 | -7.79079 | -42.49845 | 2025-10-02 05:55:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| bea8cff6-e364-3cc6-b7ac-c458560d5215 | -10.27456 | -50.31386 | 2025-10-02 05:55:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| e3e5ae3d-7961-3077-9c73-694a5b349d6a | -9.93348 | -43.77327 | 2025-10-02 05:55:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| caef7bea-4e11-354f-82e6-ff96c7e46cb9 | -0.90409 | -47.53977 | 2025-10-02 05:55:00 | AQUA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cec4206b-fd66-351a-a14d-43b67ee2bac5 | -5.82938 | -43.95782 | 2025-10-02 05:55:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c10c4dde-decf-3e65-9e5d-7c4ede3e72a3 | -10.66908 | -48.56251 | 2025-10-02 05:55:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 95fe29c2-3356-3e0c-bd66-8f298f993a38 | -9.40762 | -47.33228 | 2025-10-02 05:55:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fe861bf9-52ee-3759-acd2-d9bbaa428911 | -11.08854 | -47.82103 | 2025-10-02 05:55:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1a060562-c630-3261-b671-42c9c1157de5 | -11.03379 | -47.82169 | 2025-10-02 05:55:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d4eb3cbe-ca36-3066-a615-5b7dc9c201c2 | -4.42344 | -47.7589 | 2025-10-02 05:55:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 264b439d-f9ca-3b6b-a2b3-1ee7c1bcb66f | -5.99302 | -44.59866 | 2025-10-02 05:55:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 27a23f2f-d2e4-321c-9cfc-62fde893de06 | -6.53952 | -45.21685 | 2025-10-02 05:55:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1ba965d5-5fa6-326f-9045-794a2d9d288e | -3.08711 | -47.014 | 2025-10-02 05:55:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b44f836c-6850-3491-a138-c2e521c95b1d | -6.77147 | -45.57685 | 2025-10-02 05:55:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e3ee0c53-34e1-378f-88aa-940333a05860 | -9.39737 | -47.33996 | 2025-10-02 05:55:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2fecd60b-99dc-3c38-98f0-4c895be7b0d0 | -5.91731 | -44.85739 | 2025-10-02 05:55:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b7ea546b-2698-3a31-93bf-d91c593189a4 | -7.77714 | -42.52139 | 2025-10-02 05:55:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 2dab332a-bec6-3d6c-a042-c8d0fd6e329e | -9.91871 | -43.73804 | 2025-10-02 05:55:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 2a0eaef1-fb88-37c7-bf43-7a809f2400f7 | -10.20845 | -48.19729 | 2025-10-02 05:55:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| de64e9ca-7dbe-3e19-8d18-ae6edf28ca84 | -9.8499 | -44.59883 | 2025-10-02 05:55:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fc5f1aa0-c05a-3c80-aabe-e868ab51b57f | -8.89683 | -46.60947 | 2025-10-02 05:55:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 509bcccd-68b2-368a-9a08-26f474b68c79 | -11.08432 | -47.84855 | 2025-10-02 05:55:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e2e7d401-f006-39f9-9090-99e5f77dacaa | -7.36505 | -47.03316 | 2025-10-02 05:55:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3ed16492-6c1e-3d6b-a9d1-9dd1662ee295 | -9.94432 | -43.69713 | 2025-10-02 05:55:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 4e524040-f44a-34d1-925a-f8ed0c97a823 | -9.39874 | -47.33097 | 2025-10-02 05:55:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6c984c6c-0c4d-3e78-9963-9e675cff9b76 | -6.69188 | -42.82262 | 2025-10-02 05:55:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 413dc0b9-b1f2-3232-b434-a9d09803fc7d | -10.82825 | -46.6136 | 2025-10-02 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ed491d05-0574-3f6c-8743-5f36041b94f3 | -9.43286 | -47.34537 | 2025-10-02 05:55:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fdb48a2c-a8c4-3817-af11-8b320b7e2931 | -4.36979 | -43.0107 | 2025-10-02 05:55:00 | AQUA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e4bfedd7-b9ae-3459-a913-051f4eced452 | -6.22559 | -45.32664 | 2025-10-02 05:55:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 79c603c7-57c6-3e8d-8ef2-24534dfdfe60 | -10.26602 | -50.31815 | 2025-10-02 05:55:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 09d626b7-6422-3d49-9963-cca9d42a6934 | -7.72941 | -46.20924 | 2025-10-02 05:55:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7ca2562f-94cc-3fbf-af2d-dffb343c3b0d | -9.92928 | -50.48759 | 2025-10-02 05:55:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5a172811-c8fe-3c0b-a67b-1da7af6efe31 | -3.62274 | -42.77441 | 2025-10-02 05:55:00 | AQUA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d434dfaa-8400-320e-aafc-df1eb83d0536 | -11.46669 | -44.96459 | 2025-10-02 05:55:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a612bb01-d84c-3839-b698-2927f1cceb8b | -9.76925 | -47.74572 | 2025-10-02 05:55:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eca352dd-8121-329e-8079-dcafbe141ed5 | -11.17387 | -47.26196 | 2025-10-02 05:55:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 7390a96b-8bae-38fb-98ad-b3748b1b74a4 | -5.72809 | -42.8862 | 2025-10-02 05:55:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 2f90b751-45ba-3b37-9053-6836b138d8a4 | -9.92842 | -43.73934 | 2025-10-02 05:55:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 708.6 |
| a7eefd5e-79f7-3fcc-9b34-7999884565d1 | -9.95175 | -48.78309 | 2025-10-02 05:55:00 | AQUA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b47cfaf3-1d03-3930-8c20-53a5092c4043 | -11.00156 | -46.57022 | 2025-10-02 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b4e7d34a-a0c2-33c3-8267-db90ba78917b | -6.04991 | -42.43869 | 2025-10-02 05:55:00 | AQUA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| b1eb6043-cb91-3cc9-84f7-51ec92004b0a | -11.01035 | -46.57155 | 2025-10-02 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 59aeb337-09eb-3424-9c87-256a2b03089e | -11.45825 | -45.02404 | 2025-10-02 05:55:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ef3f9d3f-9b79-39bf-8506-1c51995a2567 | -6.77279 | -45.56805 | 2025-10-02 05:55:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 5eacaabf-dbf7-379f-b51d-24f563d4575e | -10.84381 | -45.38661 | 2025-10-02 05:55:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| c737e0e4-1c8b-37ab-b387-68bb372b5916 | -6.69043 | -42.81668 | 2025-10-02 05:55:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 00f34ea2-8dbb-35a9-96f9-333b4d65b992 | -10.66602 | -48.52234 | 2025-10-02 05:55:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0442f7ee-5b6d-3fd4-bbd0-24e55daf7ecd | -2.92302 | -48.30856 | 2025-10-02 05:55:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| e0ef4e16-3cda-35ba-86b7-fbce6815c1cd | -7.76355 | -42.5442 | 2025-10-02 05:55:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| fbe74e1d-56b8-3f76-8f6b-62ec311e1baa | -7.78735 | -42.52289 | 2025-10-02 05:55:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| f70ef822-61bd-3ea4-9d59-39dab24538a1 | -10.81679 | -46.63005 | 2025-10-02 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| f2a78d09-5955-340a-bb04-0bb169e81ebd | -11.14814 | -47.19409 | 2025-10-02 05:55:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a687d456-28af-34ca-bf4a-a03771810fa4 | -9.33296 | -45.68328 | 2025-10-02 05:55:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 009c1118-b11a-3dfe-b090-19e616f059ca | -9.92996 | -43.7285 | 2025-10-02 05:55:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 202.6 |
| 3894b681-da8f-384a-91d5-342791734bcb | -2.26631 | -47.84129 | 2025-10-02 05:55:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 222fe259-aec2-3ac8-a37a-dcbdd02d36b0 | -7.76522 | -42.53218 | 2025-10-02 05:55:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |


[Clique aqui para ver as próximas entradas](README139.md)
