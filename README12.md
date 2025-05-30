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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b069575-3c6e-3d8a-be2c-79b31f34f551 | -11.29558 | -53.98183 | 2025-05-30 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b83b5781-ab51-3d29-b44b-8bd1a6a63aa7 | -10.30911 | -58.44298 | 2025-05-30 05:14:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c07e6f24-a69d-3d93-85ae-2a2065325b81 | -10.29428 | -59.09505 | 2025-05-30 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be17203d-4ee5-31c8-be6a-be57ab89df23 | -13.63334 | -47.43322 | 2025-05-30 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e050b1c-227c-3c8e-a243-155e66d9b01b | -12.47699 | -57.18941 | 2025-05-30 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| cdaab870-8fdd-38c0-a58f-3f2367d4814e | -11.89639 | -47.43909 | 2025-05-30 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95cfd6c1-4609-3797-8e60-13100126a77d | -14.83947 | -48.10693 | 2025-05-30 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 82ede2c0-bf52-34be-b057-26cb2f6fd696 | -13.22695 | -49.83517 | 2025-05-30 05:14:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 063d33b8-acab-3fb3-a1f2-7e64e58ed4de | -13.65224 | -56.59358 | 2025-05-30 05:14:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f142e02-a917-3168-8fd4-5c7bc37faef4 | -10.29859 | -57.14395 | 2025-05-30 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cd98884-9552-376d-a595-c3d94e3a4965 | -10.16897 | -53.92075 | 2025-05-30 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cd9cf85-111a-3528-afd8-433ce094e3d7 | -10.19465 | -52.64926 | 2025-05-30 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09ea7c43-f107-374e-8867-5b9510148282 | -13.22163 | -49.83447 | 2025-05-30 05:14:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a12e7144-711b-32cd-8244-3991c04ac82b | -12.30196 | -50.0885 | 2025-05-30 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72ba0c4d-3b78-30b8-af42-79ad1b0eb3a1 | -12.39146 | -49.96623 | 2025-05-30 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c5182a6-0f0f-394f-8041-ea06322464de | -11.2995 | -53.98243 | 2025-05-30 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2abffc4e-4f84-30e0-ba91-20c798ddf0f4 | -14.83995 | -48.10246 | 2025-05-30 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 35b136e3-a5b3-3d97-b1cd-e1fcb778bb5b | -13.63191 | -47.42821 | 2025-05-30 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6267e298-fa50-326f-92fe-0f2f8fa6c8f3 | -10.29185 | -57.14287 | 2025-05-30 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1ea632f-ec51-3472-a62a-60aa98d29680 | -11.29537 | -53.98528 | 2025-05-30 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 346ef1b3-cd32-3ed8-8e48-b7e6fa93e988 | -11.69273 | -46.21008 | 2025-05-30 05:14:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 211c6c1d-1bf8-368d-b84a-1b78843af6b4 | -12.01081 | -49.51911 | 2025-05-30 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66dd5f62-5d69-344e-889b-93f7de1e1c10 | -10.69039 | -57.65216 | 2025-05-30 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9bf7d9c-3431-3b7f-8e1c-8b4b7b286e57 | -10.29522 | -57.14342 | 2025-05-30 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 121d30de-95d3-3381-ab60-587804f49359 | -10.29763 | -59.0956 | 2025-05-30 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ca9818b-5f0f-3d92-ae0a-c378df3c512d | -14.8593 | -48.0944 | 2025-05-30 05:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adb32261-10e1-3dc6-9f1f-3eecec3af6d2 | -12.0104 | -49.52254 | 2025-05-30 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62bfb8de-26eb-3478-8f7a-7b1d947006d8 | -11.79871 | -47.37791 | 2025-05-30 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a68508b3-e27d-383b-86ad-191b05bb6be1 | -11.91815 | -54.83035 | 2025-05-30 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb47e806-cd1b-35f4-85c7-cd3dde0c082a | -11.2993 | -53.98587 | 2025-05-30 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcea0b9a-a4f2-3b0b-adca-bee37b2756fd | -12.29679 | -50.0878 | 2025-05-30 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44a7af9b-2aa9-3965-b9eb-86cb0a5ff349 | -11.91439 | -54.82979 | 2025-05-30 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51703660-e0fb-37e5-a41d-76d097301e15 | -12.40281 | -50.003 | 2025-05-30 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff6e77c9-6885-3f61-a1ed-595d01b76e3d | -12.0234 | -57.10111 | 2025-05-30 05:14:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f74a7308-ec14-380a-94c0-d292dcc66ed5 | -12.39107 | -49.96943 | 2025-05-30 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3fad5e5d-9587-3b55-84a0-0e6ff95afeb5 | -10.29706 | -59.09916 | 2025-05-30 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5477be76-b587-3f09-9107-11f6851b380f | -11.79557 | -55.43491 | 2025-05-30 05:14:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a289993-17d8-3a4a-987b-dfd74910ca56 | -12.30157 | -50.09162 | 2025-05-30 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f81962ed-ce08-328f-9c22-c7f143baceee | -11.91882 | -54.8258 | 2025-05-30 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36b5ce10-fe34-3d35-bf60-c2285f74f63f | -12.01533 | -49.52666 | 2025-05-30 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0dad04f-25ba-365a-b087-470c68051699 | -11.97891 | -52.45837 | 2025-05-30 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1ff87f2-0bdf-3cb6-9031-bb46723558ef | -11.40189 | -52.94703 | 2025-05-30 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0f850a4-296f-3eb3-827c-fd79fd7c5255 | -10.68705 | -57.65163 | 2025-05-30 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 896f99c8-3ed5-3dd5-903d-dba5ac319078 | -12.02364 | -57.10185 | 2025-05-30 05:14:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae38d76b-bff1-3fb8-ab69-4e5a86edbf12 | -11.72655 | -56.43356 | 2025-05-30 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d99abef-875e-3b6e-9d79-48f8367fdde5 | -12.01617 | -49.51979 | 2025-05-30 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6fe3309-f2c4-39ff-8893-f0b33377d193 | -15.74562 | -52.05336 | 2025-05-30 05:14:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b6b8824-e93b-3644-ba5a-7c5a1d981275 | -11.65772 | -55.35904 | 2025-05-30 05:14:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93888b2d-3b26-3114-b8cd-1e1170c8fdb7 | -12.00998 | -49.52596 | 2025-05-30 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32ef23c4-2fc0-3ded-9a3f-5991ce7882ee | -11.20421 | -47.82503 | 2025-05-30 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6a1fc29-e4e4-3820-aaba-acf0b6bc3e8c | -12.3976 | -50.00237 | 2025-05-30 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ceedbab-aa53-3a53-b3db-9491ca12c294 | -13.62716 | -47.43186 | 2025-05-30 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 446fe2c7-6b74-3708-8448-224b84fcad84 | -11.40556 | -52.95147 | 2025-05-30 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e949cf8d-2c76-3e3e-a6c1-731904f95cd8 | -11.97453 | -52.4577 | 2025-05-30 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88d5e168-163b-383b-bc7e-4ff0cffcc137 | -12.06626 | -48.46928 | 2025-05-30 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a70566c5-26ae-3b18-9206-878d82efdd54 | -11.66137 | -55.35958 | 2025-05-30 05:14:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bf1121b-807f-332f-b779-d6796aec546f | -12.39239 | -50.00166 | 2025-05-30 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f9ea781f-8035-3b35-9de1-bf681da25fcf | -13.2247 | -49.83394 | 2025-05-30 05:14:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0900f8ad-6386-3fb0-a119-7b7fdf5a6eab | -14.84749 | -48.0896 | 2025-05-30 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 196223db-d195-3e9d-878e-c6586ed725d7 | -10.68418 | -57.60384 | 2025-05-30 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 963628bc-9d8a-3140-a64f-8ad5c87480a4 | -11.89583 | -47.44382 | 2025-05-30 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f491552-00a5-3dcb-acdf-75066821145c | -10.6876 | -57.64809 | 2025-05-30 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1aaed9e5-c6fd-3a18-ad0e-ec952718ddfb | -11.45294 | -49.10066 | 2025-05-30 05:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0571f8f-c6f3-3ddb-9d2e-fc7bb14003ed | -11.80483 | -47.37873 | 2025-05-30 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6158722-6bb7-3db4-8359-fcbd577cb50b | -13.2251 | -49.83056 | 2025-05-30 05:14:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db74b3fe-a19a-36e5-9b27-9ccb7048985a | -10.69094 | -57.64861 | 2025-05-30 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5744a5b-7b0e-3dd4-8b8a-26babeba77aa | -22.07712 | -56.84864 | 2025-05-30 05:16:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec7bb26b-3076-3b90-839d-4af64eca79a5 | -22.87614 | -48.64901 | 2025-05-30 05:16:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8c0a5b1-1d66-3cb1-8fac-2aef0d30c433 | -22.22988 | -50.85913 | 2025-05-30 05:16:00 | NPP-375D | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d41918cd-b634-3b6e-b874-71c55eb24533 | -23.9843 | -48.91922 | 2025-05-30 05:16:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b7d706a-3d05-333b-ac0c-33fd201e356a | -22.22758 | -50.8606 | 2025-05-30 05:16:00 | NPP-375D | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| e6888e6c-cde1-38e3-aa7f-c09e8082866c | -22.22949 | -50.86303 | 2025-05-30 05:16:00 | NPP-375D | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| cb1b19c4-9bbc-353e-8e4a-b913005bd1df | -5.21024 | -43.30362 | 2025-05-30 05:18:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 6d782a67-cb96-37a6-a996-bf528ac7179f | -6.23634 | -43.37392 | 2025-05-30 05:18:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f5434aa6-b2a6-3d75-91b1-b823054f6618 | -5.20854 | -43.31451 | 2025-05-30 05:18:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4e28f244-552e-3bb1-b626-ccc84fcce9dd | -5.77766 | -43.60767 | 2025-05-30 05:18:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e37848dd-ba5d-35f7-bf65-8553cc81b2d4 | -6.33607 | -43.38564 | 2025-05-30 05:18:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 493e3f52-8b5b-3abb-a1e1-2bd39745381e | -7.61758 | -45.73566 | 2025-05-30 05:18:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1f9e0636-4f20-3578-9567-4c036260eb80 | -6.33772 | -43.37499 | 2025-05-30 05:18:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 06e53fb2-ad5d-34d3-a2b7-97dcadb5c88b | -13.53884 | -43.67377 | 2025-05-30 05:21:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 8908208e-c0e5-30a8-92de-9a23afa27913 | -10.45701 | -47.94886 | 2025-05-30 05:21:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 92dfbd2b-1bde-3815-836b-b4685cec629a | -13.5286 | -43.67602 | 2025-05-30 05:21:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d28bd0e3-d782-3314-be24-242bde3961b3 | -14.83458 | -48.09636 | 2025-05-30 05:21:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d04a1fa4-2dd1-3a8b-8397-670faeeadfb7 | -13.53735 | -43.68324 | 2025-05-30 05:21:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 563d428b-dceb-3d95-a5f1-f3adbb2b7acb | -7.9041 | -55.41788 | 2025-05-30 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31bddcff-0603-328f-a89a-7a290b12bf14 | -7.8969 | -55.41539 | 2025-05-30 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 422379ee-b0ee-3fc5-9860-e7af7489ae1a | -7.90719 | -55.41692 | 2025-05-30 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19c0b26a-77e8-3b74-9700-748ee5d78e45 | -9.36732 | -57.55096 | 2025-05-30 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96694744-8a01-3f1f-a35f-b3a0028ceb13 | -9.3537 | -57.549 | 2025-05-30 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9cd2d44-4a0b-3db1-b6c9-bdbf10ed5bbf | -9.35824 | -57.54969 | 2025-05-30 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbc7fb4b-df07-332f-b415-7f1d81e8126c | -9.35434 | -57.54432 | 2025-05-30 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5ada982-8e6d-3677-ad49-b00660f072e7 | -9.36277 | -57.55037 | 2025-05-30 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 100df66d-077c-3bd8-92fe-7ce3cc6d82bb | -7.9045 | -55.41481 | 2025-05-30 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bf143ab-6896-3cf1-b8b9-46ee5260384f | -6.6363 | -55.01205 | 2025-05-30 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a9ebb58-6c18-3190-9d4e-6c9817c80958 | -7.89734 | -55.41229 | 2025-05-30 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f03d831-a6f5-337f-92e6-04b3e9ce1ead | -7.90204 | -55.41616 | 2025-05-30 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18398d1e-cb9b-3d46-b00f-7a917e0c7168 | -7.90247 | -55.41308 | 2025-05-30 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f515a8e-63d3-3a74-83ea-9b00b29fd5ee | -6.63673 | -55.00894 | 2025-05-30 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a952c48-cf76-388a-959a-054276f6f4f7 | -9.46667 | -63.35365 | 2025-05-30 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 24f272e8-bf5b-3f10-9a6f-aebcd81071fd | -9.47002 | -63.35416 | 2025-05-30 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |


[Clique aqui para ver as próximas entradas](README13.md)
