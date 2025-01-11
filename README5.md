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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48a694bd-224e-36fb-9a24-abd16838a133 | -21.30935 | -52.07388 | 2025-01-11 04:55:00 | NOAA-21 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fca3825-4bb8-3053-bd5a-0c55ae0cdede | -19.71101 | -58.02017 | 2025-01-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6bc4176a-3c2f-3774-8866-4e9afadec785 | -10.71739 | -59.22953 | 2025-01-11 04:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 66b2e831-0bb8-3804-b624-32aa4d529d13 | -19.34816 | -54.16381 | 2025-01-11 04:55:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 180b2c96-4015-3e29-bff6-ec6dd10bbc6a | -21.56604 | -54.19891 | 2025-01-11 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 141b7e4b-928c-3db5-a02b-390f3861d374 | -22.83607 | -48.85275 | 2025-01-11 04:55:00 | NOAA-21 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6db704b9-3173-3df2-82df-209d574a4f4c | -19.48728 | -55.33811 | 2025-01-11 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 672d3bd7-6941-34a4-b75a-f6e96d864544 | -18.60567 | -55.49802 | 2025-01-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 44653487-36bf-3e26-aa1f-fd1da17aec76 | -16.11008 | -58.19339 | 2025-01-11 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| e8a338d5-1fda-3a4b-a0d3-048c61bb227d | -21.5632 | -54.19437 | 2025-01-11 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 39bf59fb-c12b-3f7d-9e34-eac3a4ef10e3 | -19.66481 | -54.41247 | 2025-01-11 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae3496b2-3a6f-345e-a1ad-461d9d030071 | -19.66538 | -54.40869 | 2025-01-11 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f9e7f13-56e0-36ac-947b-08f173088811 | -19.66818 | -54.41299 | 2025-01-11 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0311f608-e74a-38dd-84be-abc36129a7e6 | -19.67807 | -52.25416 | 2025-01-11 04:55:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91161ca5-f5b5-3557-925c-942511d7fe85 | -16.11082 | -58.18908 | 2025-01-11 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| a27b0e8a-de66-3d74-baa5-3fc323439041 | -21.17146 | -48.55592 | 2025-01-11 04:55:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6fc50541-6747-3deb-903e-9c5c6083db22 | -18.60898 | -55.49858 | 2025-01-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6034ff02-5594-31fb-a5de-871bf321a01f | -19.34479 | -54.16325 | 2025-01-11 04:55:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81826c23-da48-39f1-9066-2e6008a92eb0 | -21.41912 | -55.77312 | 2025-01-11 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17d99de8-3682-3285-aec8-491cc38e4458 | -19.24654 | -50.66687 | 2025-01-11 04:55:00 | NOAA-21 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b4c9cd59-8ac8-3cb3-9948-71eef80b28e6 | -30.83045 | -55.39511 | 2025-01-11 04:57:00 | NOAA-21 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 093355d5-a2c0-3aa5-889b-d96c49c5d4b6 | -30.83107 | -55.39042 | 2025-01-11 04:57:00 | NOAA-21 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| dcdaf0fb-636d-3ea9-be1f-090177552ac6 | -30.83251 | -55.39741 | 2025-01-11 04:57:00 | NOAA-21 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 3f5de496-a333-3158-a257-fdbb3d84b135 | -30.82751 | -55.3898 | 2025-01-11 04:57:00 | NOAA-21 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 5.5 |
| afbb6c16-1b75-384e-8496-5ee1a9ce80d5 | -30.3849 | -56.1546 | 2025-01-11 04:57:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| a326e751-5b07-3f13-acad-3a4146495cff | -30.83401 | -55.39571 | 2025-01-11 04:57:00 | NOAA-21 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| dc8a024e-fead-3301-b258-627ccedcbbfc | -30.83312 | -55.39272 | 2025-01-11 04:57:00 | NOAA-21 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 3.2 |
| f78b5ad7-9c65-3e56-8246-1ed7a409c150 | -30.37454 | -56.15277 | 2025-01-11 04:57:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| ed543bd0-077d-3974-894d-a0734a7601c4 | -30.82955 | -55.39211 | 2025-01-11 04:57:00 | NOAA-21 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 3.2 |
| 9b2da839-ea8a-3a68-8ba9-6c75e6b474e2 | -30.38429 | -56.15898 | 2025-01-11 04:57:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 7370af80-2512-3f14-b958-f3ec45b49e6a | -29.88618 | -51.13124 | 2025-01-11 04:57:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 302b9cf4-4133-356e-ab4b-042728887d53 | -30.38774 | -56.15959 | 2025-01-11 04:57:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 292e3241-06e6-3bd9-b6a3-ab75ff3a2c3d | -29.54558 | -54.33282 | 2025-01-11 04:57:00 | NOAA-21 | TOROPI | RIO GRANDE DO SUL | Brasil | 4321493 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 94248b68-0cfa-399b-a1fb-a4afb37a00bd | -30.38714 | -56.16395 | 2025-01-11 04:57:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| 568964f8-a477-3f85-8988-d2cfe908821a | 3.31978 | -59.97937 | 2025-01-11 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1bfcc6e-cc12-3489-835a-cbed9ae6a6be | 4.0109 | -60.1622 | 2025-01-11 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cacf4f98-3e79-306e-bc24-f119350e37ed | 4.41333 | -60.0383 | 2025-01-11 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b848a1af-4a0a-376d-9b8c-1de35ed31163 | 3.37794 | -60.25911 | 2025-01-11 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb7bf3ec-15c1-384a-a838-bf205b09c6a4 | 3.3773 | -60.25486 | 2025-01-11 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54b609af-a9e6-34e3-89d8-c0d08b5822c6 | 4.01455 | -60.16149 | 2025-01-11 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09c13109-7640-34c5-b5a8-b9e144814072 | 3.37815 | -60.25747 | 2025-01-11 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06b81f8c-4b97-34b3-be4e-e88491895ea9 | 3.37515 | -60.26228 | 2025-01-11 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 692ec200-94c3-3726-96d1-c4359434f40c | 4.34442 | -60.90084 | 2025-01-11 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95db1044-602e-3285-be82-a640b6d4a7ba | 3.92659 | -59.75901 | 2025-01-11 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95d9c3b2-806b-34f4-9093-0b919314fe7b | 3.37748 | -60.25323 | 2025-01-11 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d37195d4-d302-3a11-9f7b-c5895bbffe02 | 1.11679 | -59.46473 | 2025-01-11 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c31daa6-9a27-388c-b7da-a15ef40d97a3 | 1.11907 | -59.45671 | 2025-01-11 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4257090-2ad4-320c-9df0-e69032c2c11d | -3.46533 | -53.95828 | 2025-01-11 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bee2bd88-834c-3aab-bf9f-d7b2341edbdf | -2.60408 | -54.18212 | 2025-01-11 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4be82c23-df35-3ab8-be9c-bd4c57253235 | -2.60026 | -54.18151 | 2025-01-11 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43864be1-7197-3c0e-b2b8-07f1bea88ea7 | -2.53471 | -53.9565 | 2025-01-11 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89818d10-dc77-38fc-adf5-26f7385ac294 | -3.87109 | -54.23196 | 2025-01-11 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ecd61837-391a-334e-9a04-3c242c9c2198 | -3.77361 | -47.50308 | 2025-01-11 05:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfac068d-fd59-3537-bceb-a41eec49d3d5 | 1.11966 | -59.46046 | 2025-01-11 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 174127d9-4286-385e-a4f9-a4a801cff6bc | -2.79832 | -54.16878 | 2025-01-11 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efa487f0-341b-3b17-a4fe-7cdec49d9bf5 | -3.31927 | -52.44239 | 2025-01-11 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81879395-f1b2-3c2c-864c-40fd8f2938e3 | -2.84044 | -54.07393 | 2025-01-11 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 360316a9-e0e0-3a1f-82b6-cf375265824c | -3.4614 | -53.95774 | 2025-01-11 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7488843b-bf92-3afe-a217-07ff08cfe4f6 | -3.35177 | -53.25224 | 2025-01-11 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f73cf3fb-5cd9-37a2-9013-f817d25a2179 | 1.11275 | -59.46152 | 2025-01-11 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cdba9e8-5a03-3e37-b7e0-8659d258966a | -3.35231 | -53.24862 | 2025-01-11 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 116a6fdf-fb09-3b53-b651-ea3bef4da90b | -3.32358 | -52.44312 | 2025-01-11 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2522b383-1386-3869-a383-90e7982eeba8 | -1.71009 | -54.50024 | 2025-01-11 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95f770ea-22e3-37ca-ab78-ea0d0c7c0324 | 1.1162 | -59.46099 | 2025-01-11 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 812453c9-f088-3801-afba-dbbe1c531c73 | 1.11562 | -59.45725 | 2025-01-11 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdd1138a-c87b-32ba-bca5-e8e2c8ca6975 | 1.11217 | -59.45778 | 2025-01-11 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a5a5891-5076-3cc3-b725-ab6b00fa6ca3 | -3.77292 | -47.50767 | 2025-01-11 05:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3e3471b-17ff-3c5b-bb68-d5e73df04c8d | -9.26004 | -60.31703 | 2025-01-11 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb51eb97-6b18-3ab2-9a11-eeb0a0b04733 | -9.2567 | -60.31649 | 2025-01-11 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa2a4a9e-1314-3164-ae92-76ae07dd1700 | -19.16033 | -54.8431 | 2025-01-11 05:20:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27b6e8a3-e1df-3a2e-9646-75c9719da8d6 | -19.34173 | -54.16505 | 2025-01-11 05:20:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d8ce6b18-8316-3661-b9d4-fe9e4343f956 | -16.10999 | -58.1894 | 2025-01-11 05:20:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7bbc61d8-b086-3ff2-9433-1898fc56150f | -16.21198 | -59.07897 | 2025-01-11 05:20:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b9c2653e-1d9a-379a-9d45-548eefb7d282 | -16.2114 | -59.08295 | 2025-01-11 05:20:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b6e3466c-e3fc-3ffa-a979-a707bfa529c5 | -19.49111 | -55.33645 | 2025-01-11 05:20:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4edf8bc1-8f2e-3846-adea-1ea44998015f | -19.48662 | -55.33583 | 2025-01-11 05:20:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8b4cd65c-7baa-38fb-b6bf-db3800ed0757 | -19.34657 | -54.16577 | 2025-01-11 05:20:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 76adb327-9dd6-352e-8b80-1ce977f113fe | -16.10938 | -58.1937 | 2025-01-11 05:20:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 96b1be29-66d4-3fb3-9696-7cc0c10384c8 | -19.49166 | -55.33179 | 2025-01-11 05:20:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4da05f67-c4b3-35cf-84dd-f2ab85f46303 | -19.16093 | -54.83809 | 2025-01-11 05:20:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18a4951b-afc3-3409-a631-4bd7be995005 | -21.41577 | -55.77192 | 2025-01-11 05:22:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71060807-8022-3233-9b88-f9903e37ce1f | -21.41771 | -55.77522 | 2025-01-11 05:22:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17810013-3e37-329e-94a0-31664dd9b2c9 | -21.56261 | -54.19864 | 2025-01-11 05:22:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d60c2b0a-eaa3-3397-8f35-c082fdf64124 | -21.42025 | -55.77258 | 2025-01-11 05:22:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99cfaad8-3670-3290-a66c-1277535e11fa | -21.41829 | -55.77039 | 2025-01-11 05:22:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5327e57d-ff0f-3c6f-a989-38eb700a2fd1 | -21.56758 | -54.19926 | 2025-01-11 05:22:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6754c87a-d697-367a-8acc-e979daa8db0f | -19.7125 | -58.0202 | 2025-01-11 05:22:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 32768929-fc8b-321d-816a-ee11d6bb1e4e | -30.38403 | -56.15372 | 2025-01-11 05:25:00 | NPP-375D | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 549352f4-2b10-383c-999c-4869289a77b5 | -30.83099 | -55.39247 | 2025-01-11 05:25:00 | NPP-375D | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 6d9a6cd4-1e26-3e2c-b8d9-42cbadee6aba | -30.82583 | -55.39189 | 2025-01-11 05:25:00 | NPP-375D | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 805f3ec3-245c-3240-a77e-68a8232934e3 | -29.6186 | -53.75909 | 2025-01-11 05:25:00 | NPP-375D | ITAARA | RIO GRANDE DO SUL | Brasil | 4310538 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 13823aa8-831c-370b-b3ad-d3e6772631c0 | -30.38836 | -56.16056 | 2025-01-11 05:25:00 | NPP-375D | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| b6e8f868-090c-3428-8497-489d308527ff | -30.8307 | -55.39599 | 2025-01-11 05:25:00 | NPP-375D | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| dffcac8a-35f3-3b45-b7b7-b2f007a45c65 | -30.38345 | -56.16009 | 2025-01-11 05:25:00 | NPP-375D | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| ecf75364-dc43-3d91-8a20-24b35f948e20 | -30.82611 | -55.38842 | 2025-01-11 05:25:00 | NPP-375D | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| d537dc8e-2d30-3fa9-962d-55ec745eced3 | 3.37834 | -60.25441 | 2025-01-11 05:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab6f048f-6d13-33a8-b6aa-98f07b2d7a1a | 3.37878 | -60.25364 | 2025-01-11 05:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ade926f8-bdde-333f-ad39-e13781255d9f | 3.37586 | -60.25823 | 2025-01-11 05:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38f18831-4048-3e38-a93c-53c520364841 | 3.379 | -60.25842 | 2025-01-11 05:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd6d10a9-5f46-3103-a481-76047d19692a | 4.34828 | -60.56176 | 2025-01-11 05:37:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README6.md)
