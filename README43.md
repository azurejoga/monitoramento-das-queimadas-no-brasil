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
| c8081ad0-6d00-3a19-a0c7-f7bfa4c1dcdc | -12.59181 | -46.95133 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd375e3f-a773-3e7a-89d3-f5af2689ed95 | -8.99124 | -60.50666 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0db829a8-5e0e-37f9-8953-a31346d6f698 | -11.30826 | -42.13387 | 2025-08-16 04:34:00 | NOAA-20 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3cf345e4-2f9d-3b3f-9e0a-ea33a4c82aee | -12.60114 | -46.96059 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 61c7611d-e71e-307c-ae10-0946e6051c03 | -12.61672 | -46.92736 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99b5008a-a472-3919-a40f-4effef43e8cb | -12.59588 | -46.94785 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 602ba096-7aee-376e-8ece-c70081f46183 | -13.12754 | -57.17249 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4b45a5a-4425-32cb-9d5b-e260ca2ecae3 | -11.41641 | -44.68871 | 2025-08-16 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d80ada8e-3d97-3dfc-b33c-c3a3bf45d9a7 | -9.38725 | -60.5461 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f8fd442-7094-35e7-bf5d-5ef8a763bde9 | -11.35695 | -55.4152 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 070c1aa0-2cc7-347f-abb7-3a91abc14d70 | -16.0821 | -48.08147 | 2025-08-16 04:34:00 | NOAA-20 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3a53c046-7b86-3710-b572-e52b800f88b3 | -11.50693 | -47.24187 | 2025-08-16 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fee60b76-2e66-3edb-99fc-365a23f0c51c | -12.58773 | -46.95485 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c63e71ab-66f7-3469-aa1c-bcdc8b0a66f5 | -12.56304 | -46.9677 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8af3310-053f-3a8a-923b-8d6d3a38465a | -12.59531 | -46.95174 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 178e8870-d543-3e18-8103-ec97608c9f3f | -9.38625 | -60.55118 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 061d0702-5b7e-31e2-8368-c1cd580108bf | -9.16651 | -59.65737 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e5b2251-9e9d-37a1-9b72-141a73b78a5b | -9.21326 | -59.63898 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3e1e102-8fc6-387b-a832-aa73e5b19cf7 | -9.20577 | -59.65961 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc999410-9849-31da-9216-1909f6582346 | -12.82524 | -46.00588 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cf8ce77-543c-35db-8818-1162c22fb355 | -8.98228 | -60.55309 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3dcf08de-0630-37a0-8b11-9c2345ca0e84 | -16.82288 | -49.27748 | 2025-08-16 04:34:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 52de5562-e6bf-36b0-92b5-af93588952bf | -11.36563 | -55.41695 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4245316-099a-3a1f-b84e-2fb8279af500 | -15.62374 | -49.26811 | 2025-08-16 04:34:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7ba303a-dea6-3749-aa70-ddc53fea3865 | -9.1664 | -59.62534 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 358182f6-4756-3044-955d-e0d2bab627d8 | -13.57316 | -46.97983 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f86bf14d-48f3-3ff3-8562-b8cde8029cf6 | -13.86798 | -45.55322 | 2025-08-16 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| baa50b3d-7887-395e-97ae-9804577f0cc7 | -12.59062 | -46.93513 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36868953-c8ef-3f68-a8c7-6d948d8b422e | -12.61909 | -46.93551 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27077301-558c-3d1e-be60-a83e3e3cd75f | -9.50134 | -60.54645 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c18fce36-a233-3c3c-bcd8-930acc956b88 | -14.2739 | -49.56882 | 2025-08-16 04:34:00 | NOAA-20 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0404de1-cb10-3d91-9cb6-b33c1680a18e | -11.55188 | -47.26808 | 2025-08-16 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88bb3fc1-bfb9-38d1-be4a-123ef67b5cd1 | -12.4522 | -47.00691 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0381ccce-c5f6-3878-94ce-74e2329041d3 | -12.92685 | -46.95617 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a15a121-bb95-3e6a-b3fe-1feef1bfa522 | -14.94584 | -54.69512 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8ee380c5-77db-33ca-a577-0aa78e0aaf83 | -9.38412 | -60.54677 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39c01e22-5050-369e-8f02-cd7f95524a70 | -13.86869 | -45.55115 | 2025-08-16 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| beb8faa4-221e-38b6-a1af-3db9400aa52b | -9.1588 | -59.63283 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 74afd007-c2b4-3ae4-a526-c1fc7430cea9 | -10.86898 | -48.48045 | 2025-08-16 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5929e82f-ee5b-3407-9d58-4f2154c28ac1 | -12.5381 | -46.96778 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8b7140a-cefc-36c5-9928-d64640465426 | -12.59701 | -46.94019 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 0c783fc7-f9b2-3531-b615-54b5c1c7a04e | -9.20314 | -59.66004 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19c1ebf2-f4c3-360a-a4f8-2bf83a895a6b | -12.77897 | -45.93775 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ded3f309-29f1-3433-8ac0-ae89152a773c | -12.62709 | -45.2419 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 069aa19f-f6cb-3d8b-9eda-47f39b20fe2e | -8.99997 | -60.52935 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d5d571bc-959b-3049-8440-0e1b4a4fce9d | -12.80014 | -45.97226 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c16ef55-09af-3e09-b6b6-5550dfec3c77 | -12.56302 | -46.94405 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f541e20-f46a-31fe-90c5-6188d60dad4e | -9.50331 | -60.53637 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3a8c4cee-b6ce-32d1-b7fd-370a1f298d36 | -12.59823 | -46.95614 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff94fdbc-6f32-34bb-be88-d2dd94a07ddf | -12.682 | -44.95965 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ba8c7e4-0685-3529-8a80-ff1ca9639b6b | -12.56535 | -46.95229 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 243bb5b7-d6ed-373b-8054-ae88834a39fd | -14.96776 | -54.73119 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ceb363a-850b-3109-b0f8-9b17182946b6 | -8.89185 | -60.74154 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5ecf911-c9c5-343b-8168-f6c7804ecbc8 | -8.99164 | -60.53858 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c0933d54-709b-306f-98b1-18d789534e68 | -8.9843 | -60.54262 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 4f767fb3-6291-3109-b7d9-0d4324fcb83f | -12.45278 | -47.003 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1324dc3-db34-3beb-92ae-e458b6d461bd | -17.72999 | -43.52243 | 2025-08-16 04:34:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db791ed4-b343-333f-8361-df5f24d9ccc8 | -11.65568 | -51.62683 | 2025-08-16 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78b9f2c5-8fa7-32d5-a295-f16fcac8e530 | -11.75096 | -48.35207 | 2025-08-16 04:34:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9cf6a42-c762-3660-a2b7-6237bd0e90cc | -14.86404 | -60.09032 | 2025-08-16 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fef581df-91c4-36bd-8c63-4baa3798be09 | -12.56185 | -46.95184 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 697dbc0c-e73b-3330-a2f6-053d36607160 | -7.95035 | -61.75188 | 2025-08-16 04:34:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45e88f13-e6d0-3fed-ac15-6473c4224c90 | -14.57882 | -47.91426 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76654712-b0dc-3d10-823b-d05e23895d51 | -17.60735 | -46.68084 | 2025-08-16 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c7b4ee3a-6bda-3681-a9c8-1358b67c9163 | -13.00082 | -56.86682 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca130543-17f3-3e7d-9be1-c7828220d71e | -13.61304 | -46.90372 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fc459fa8-9338-3841-86d7-143a8fd0ed68 | -14.97443 | -54.7165 | 2025-08-16 04:34:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5798f039-c960-3364-addb-c459de85beaa | -14.59644 | -47.9366 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7cd99f66-62df-3104-8492-3b35f0f899bd | -8.99263 | -60.53342 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0f683225-6595-3818-b196-9d9d821fa516 | -13.45264 | -47.06312 | 2025-08-16 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b866c25d-144d-314e-af6f-b8240b28c7e8 | -14.8711 | -60.08392 | 2025-08-16 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 740f4bb1-f944-34cc-a7ac-ccae1c548766 | -12.59937 | -46.94835 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 326d0d97-cace-33eb-927d-95485f6e562a | -13.42051 | -43.67781 | 2025-08-16 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f455d42-0e88-33c0-b301-d38d777314ba | -9.2065 | -59.64207 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd8ab8fb-6135-3f9c-a13b-5dac9d96a2a3 | -14.9311 | -54.70951 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 531b0490-5df7-341e-bca7-7ffb88869376 | -12.771 | -45.94122 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc2b73ed-7ff5-355c-84b4-8a5ef508b3de | -9.21244 | -59.64339 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbdba4f2-3ebe-3616-b01a-5dc99b46db55 | -11.65982 | -51.62352 | 2025-08-16 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16763c29-05f8-38cc-990c-33955472d1bf | -8.98762 | -60.55944 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1ea1a9c0-8951-3125-b976-2951c2d0253c | -15.18253 | -53.84636 | 2025-08-16 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83992710-17d4-3815-a386-95de286f25cc | -11.90328 | -43.43521 | 2025-08-16 04:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9913b083-5c25-332e-8466-f93158ae8188 | -8.99223 | -60.50156 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61a7624d-5af2-3048-8680-e8a8683e43ab | -12.48895 | -47.50472 | 2025-08-16 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5450dbe-dd4c-32a0-bbfc-b548b15c900f | -12.57176 | -46.95708 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc3bac21-0833-3ec7-83cb-a9d50b11daa4 | -12.82724 | -46.0165 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f217313-dd4a-33a0-b9e7-305313a86814 | -12.82946 | -46.02873 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8278f3ea-21d5-3c31-a69e-bf649eaeb777 | -9.21346 | -59.65187 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f6d883da-dda8-32d0-9807-3ea4658017eb | -8.98494 | -60.50539 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7a935b02-cfdd-3aa3-92e4-742261a3963a | -14.519 | -49.39049 | 2025-08-16 04:34:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 555edf1f-a6fd-30ad-9ddb-74161e42ceb7 | -8.9803 | -60.56335 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aca813f4-0f90-3a5f-8db7-8f8a3a1294e9 | -8.66273 | -62.46738 | 2025-08-16 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2444e59-6d15-36a3-a857-e34e255cb4f9 | -12.57409 | -46.94155 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3d1c624-b200-3520-94ba-db7955bf9991 | -14.94792 | -54.72873 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5e3038bc-cf31-34b5-88ac-687d0e46e916 | -11.50351 | -47.24135 | 2025-08-16 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a68dc3cd-61b4-32d0-893e-d258505bdf7d | -16.7448 | -49.30331 | 2025-08-16 04:34:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99a23216-c604-3e47-847f-69583c8b31bd | -11.36129 | -55.41608 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e07d8ed-ae14-35ba-bbd2-0174905c4828 | -15.50365 | -40.75286 | 2025-08-16 04:34:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 78dfb583-302e-38bc-8fc7-b9a504cd9151 | -16.23381 | -51.12761 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb1e33ec-7a92-37bd-90f7-5cd164a5b9f1 | -17.33539 | -45.02764 | 2025-08-16 04:34:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 463eebd8-1818-387d-bd7c-a75281f443ef | -12.82339 | -46.01896 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README44.md)
