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
| 21655d26-91a7-30da-a223-be75083b1369 | -4.2726 | -43.7832 | 2026-01-09 00:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 3ce3e49d-734f-3263-94f0-4d4986147335 | -21.2315 | -56.2575 | 2026-01-09 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 2e5baa0b-a3a3-34c1-9895-b9916ab0662c | 2.5437 | -60.584 | 2026-01-09 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 8e8be166-d9b2-3792-85e1-d1d63eecb3eb | -21.232 | -56.2361 | 2026-01-09 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 17d4ae86-996a-3adf-ac29-97054287d4e0 | 2.562 | -60.5838 | 2026-01-09 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 04061874-9ff4-3a43-8e52-3b8f14a41920 | -21.0086 | -48.6943 | 2026-01-09 00:00:00 | GOES-19 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.0 |
| b21e40e2-794a-3083-abf5-5725f1341b02 | -21.0093 | -48.6711 | 2026-01-09 00:00:00 | GOES-19 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.1 |
| 1df0e830-cb5b-3a87-ac31-bc907674d6d9 | 2.5437 | -60.584 | 2026-01-09 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 965a38d2-207a-3164-9727-ec42e915db8c | -10.9086 | -37.5217 | 2026-01-09 00:10:00 | GOES-19 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 57.9 |
| c99164cb-4de3-36d5-8c61-a73acb20e5fc | -22.8293 | -49.2836 | 2026-01-09 00:10:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 0704d85c-073a-33d9-b74d-3f24e2182005 | -27.3298 | -51.6661 | 2026-01-09 00:20:00 | GOES-19 | OURO | SANTA CATARINA | Brasil | 4211801 | 42 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| c9d73f42-9ed6-3170-9725-c9a568339aa2 | -22.8293 | -49.2836 | 2026-01-09 00:20:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 6f385c25-6c73-3411-a3d0-ec435e41fbde | -4.2726 | -43.7832 | 2026-01-09 00:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| a5a2d809-ecd7-3db8-91da-3bc4bedb14ea | -10.928 | -37.5181 | 2026-01-09 00:20:00 | GOES-19 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| 0280fe18-6d28-3be8-96e6-70f0fe886ce1 | -10.9086 | -37.5217 | 2026-01-09 00:20:00 | GOES-19 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 106.2 |
| 44757eed-e184-31c2-9d68-cbcc8394aaa7 | 2.5437 | -60.584 | 2026-01-09 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.3 |
| fd66ed6b-df83-33bd-a58a-e2a227185169 | 2.5437 | -60.584 | 2026-01-09 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 7ed94c9b-49d7-33a5-855b-f1d81b8084df | -4.2726 | -43.7832 | 2026-01-09 00:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 96642e42-8865-33af-84c3-08be02d36cc3 | -21.2315 | -56.2575 | 2026-01-09 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 84.3 |
| bb23d2ff-6968-31be-9881-34a6cebbda46 | -22.8293 | -49.2836 | 2026-01-09 00:30:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 420ae879-73f6-3e92-8b9a-d2c79e012eca | 4.3421 | -60.396198 | 2026-01-09 00:39:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad98250-e4aa-3a0e-b1af-f7a119ee14dd | -19.438999 | -54.7682 | 2026-01-09 00:39:00 | METOP-B | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 15658c0c-55ec-3fc7-bb11-1ff5e4d63a0f | -17.656401 | -56.346401 | 2026-01-09 00:39:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 952ab1f8-3c88-345c-a6fc-d115ee79e0d9 | -16.1103 | -56.739799 | 2026-01-09 00:39:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e332de21-b945-3838-a462-b1fadd1e7858 | -18.958799 | -55.168301 | 2026-01-09 00:39:00 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6e989661-6034-31f8-ba7b-f3ee01a09bd2 | -21.0012 | -48.665798 | 2026-01-09 00:39:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd8468c4-7d74-3447-a537-795b9b120b1a | 2.5469 | -60.5807 | 2026-01-09 00:39:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| db038836-1bd4-345b-b704-a3b0fd50b6ab | 3.1749 | -60.404499 | 2026-01-09 00:39:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a6e19888-5f89-35e8-a74e-2051b367b5f0 | -2.624 | -51.950001 | 2026-01-09 00:39:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00d60a1c-7445-3688-beb8-cdf60bd78ed3 | -20.9083 | -48.881401 | 2026-01-09 00:39:00 | METOP-B | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 419d00c3-db6b-3aa0-b7dc-a14a8069120b | -27.32 | -51.66 | 2026-01-09 00:39:00 | METOP-B | OURO | SANTA CATARINA | Brasil | 4211801 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a610d692-c9ef-373a-bb5d-2c3887ef2aa7 | 2.5487 | -60.573101 | 2026-01-09 00:39:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 660fd8be-bf50-3465-bce9-1cd7d6bf5790 | 2.5504 | -60.565399 | 2026-01-09 00:39:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| acaa2e43-5b26-3237-bddd-ec4b01a7090b | -22.818399 | -49.286301 | 2026-01-09 00:39:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c615c3bf-053c-3e20-8b17-82577c292e49 | -21.230101 | -56.232399 | 2026-01-09 00:39:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bd901e84-4aad-3cf8-aa02-600ff6d99a11 | -21.233601 | -56.2505 | 2026-01-09 00:39:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 419cc6e5-75ef-3b3f-9d7f-7b72f26b4b95 | -17.6581 | -56.354599 | 2026-01-09 00:39:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 48221f74-5be8-3ddb-afdf-fbc3ba0e4a1f | -27.3216 | -51.667801 | 2026-01-09 00:39:00 | METOP-B | OURO | SANTA CATARINA | Brasil | 4211801 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 69ea16bc-5d2e-3acb-845e-3efb93c8b753 | -22.826099 | -49.275101 | 2026-01-09 00:39:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d2aac157-97ec-3fc6-a78a-dbb0b73d0f65 | -19.302601 | -55.244999 | 2026-01-09 00:39:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 27500d71-ba4d-3bee-9a4d-6248e6e1b5eb | -21.0035 | -48.675201 | 2026-01-09 00:39:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6211e6c6-0a6f-32c1-8d11-c86bd4da355a | -12.3974 | -58.030102 | 2026-01-09 00:39:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ed79575-2c4e-32bc-aaac-6713ce3fc90b | -20.5595 | -57.9305 | 2026-01-09 00:39:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 345302fe-b88e-3e03-8f7a-4b5796a1b052 | -19.3043 | -55.2528 | 2026-01-09 00:39:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2395c849-cd86-3411-ab62-07be288156ce | -12.4072 | -58.027901 | 2026-01-09 00:39:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f1e98c53-b17c-3b06-9a5b-ff3e5090af3b | -19.437401 | -54.760601 | 2026-01-09 00:39:00 | METOP-B | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6dcd966a-4123-396a-9593-900aae558be6 | 4.3437 | -60.388901 | 2026-01-09 00:39:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e1fdbe3b-2258-347a-b484-5809c42e8679 | -22.8281 | -49.283699 | 2026-01-09 00:39:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ea70da3f-62d9-3450-a96f-36bbc2f9f6bb | -22.830099 | -49.292198 | 2026-01-09 00:39:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8d567841-a612-3c01-9db1-473f75ca1543 | 3.1766 | -60.396999 | 2026-01-09 00:39:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2248acc5-9cf3-3a65-ad30-b86fd03f8787 | -20.5616 | -57.941399 | 2026-01-09 00:39:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9e2ee050-6244-3e75-b3f9-9b0c8bc374e0 | -21.231899 | -56.241402 | 2026-01-09 00:39:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e192bd4d-92b6-3c0f-9d4f-d2e0eca4487c | 3.6919 | -60.623199 | 2026-01-09 00:39:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4a3bdb66-bf15-3c17-8063-40e5af3fe94c | -22.8293 | -49.2836 | 2026-01-09 00:40:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 131.1 |
| d917892c-11b6-3605-a117-f4e80281dfde | -4.2726 | -43.7832 | 2026-01-09 00:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 6a99d134-1dc2-387d-83ae-cbd776feec25 | 2.5437 | -60.584 | 2026-01-09 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| c7ba190a-7aea-3cf8-82db-34130adbc6f7 | -22.8293 | -49.2836 | 2026-01-09 00:50:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 1cc2ca55-9dbc-3f0f-b0cd-a02cb3e54bd4 | -22.8293 | -49.2836 | 2026-01-09 01:00:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 3e37fc92-e570-303f-827b-b74e234dd11e | -4.2539 | -43.7843 | 2026-01-09 01:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| f04b2d51-0b1c-35f6-89c2-2dfdbac91b99 | -4.2726 | -43.7832 | 2026-01-09 01:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 4afe08b7-967e-3fed-810a-ce3dcb857d45 | 2.5437 | -60.584 | 2026-01-09 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7b1f958b-f113-36dc-b3e2-4d17ec1e96af | -27.32264 | -51.66933 | 2026-01-09 01:04:00 | TERRA_M-M | OURO | SANTA CATARINA | Brasil | 4211801 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 8f3c3b02-2eb0-3444-8658-a12ae3f4f69b | -22.82608 | -49.29373 | 2026-01-09 01:04:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 8188948e-a78b-3d12-8d47-a126fee2863d | -22.824 | -49.31409 | 2026-01-09 01:04:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 36e3ec7b-16d7-38a6-9911-b93172f9fad7 | -22.81925 | -49.28969 | 2026-01-09 01:04:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 110.5 |
| b802f8b4-152d-3eb1-a642-9692a759e85e | -21.22937 | -56.25986 | 2026-01-09 01:06:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9886a638-8675-3a27-90ca-0b7a0b7fb247 | -17.65425 | -56.35804 | 2026-01-09 01:06:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 6ffff3c4-d1d5-33af-bac0-a435b0004b78 | -20.55614 | -57.95414 | 2026-01-09 01:06:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.2 |
| cc0b7e7f-3871-399a-8475-b7c66766ab93 | -21.22794 | -56.25012 | 2026-01-09 01:06:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 0505c23b-3b8f-3f98-8ec5-3e403ee8ead3 | -23.04296 | -54.91958 | 2026-01-09 01:06:00 | TERRA_M-M | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| cef52c35-0691-3b03-80b9-f5edc03f0d87 | -21.00065 | -48.68068 | 2026-01-09 01:06:00 | TERRA_M-M | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.3 |
| 02600516-2f47-386f-bf2d-273af73e82bc | -16.10799 | -56.75203 | 2026-01-09 01:06:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3479a9ad-72cb-3c97-8e73-8971682b1b88 | -16.36322 | -57.30529 | 2026-01-09 01:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8ce95ee1-2f16-3d10-9987-d666b1552ad2 | -21.2369 | -56.24856 | 2026-01-09 01:06:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f2a0c234-0066-3af3-9627-fa5f00079ed0 | -16.09881 | -56.75353 | 2026-01-09 01:06:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a59fb46d-9d00-3586-a3a8-5e2af568b78f | -19.30089 | -55.26387 | 2026-01-09 01:06:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| f696d0c2-4f75-3c71-b3b4-37b6a651c20b | -17.66344 | -56.35653 | 2026-01-09 01:06:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 8111c050-2ce9-3b66-a857-ef23018ae3cc | -12.39332 | -58.04666 | 2026-01-09 01:09:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5e2ea2fe-d6a9-3582-b7da-d03491de9897 | -12.40098 | -58.03588 | 2026-01-09 01:09:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 16d623bb-9209-3307-b5db-c6e4ed06f8e2 | -12.41 | -58.03451 | 2026-01-09 01:09:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b832a341-78cc-3ee2-8d7d-9ceb6666159e | -12.40233 | -58.0453 | 2026-01-09 01:09:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 70081642-4d66-39dc-bedb-3eb2c6c5e340 | -4.2726 | -43.7832 | 2026-01-09 01:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| dbb42933-3e1b-36a8-b0d6-60beaf80bd27 | -4.2539 | -43.7843 | 2026-01-09 01:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 5ab3fdc7-2bed-3bf5-9799-e304f9837c5b | -22.8293 | -49.2836 | 2026-01-09 01:10:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 118.0 |
| b4f690aa-d484-36f5-aed6-5bb919a74e67 | 3.37986 | -60.23111 | 2026-01-09 01:13:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| af7cf2e7-3114-32bd-83ed-609c7a491d27 | 2.54621 | -60.58725 | 2026-01-09 01:13:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 22.8 |
| ff14dbd6-394b-3701-880c-443286f658cd | 2.55545 | -60.58854 | 2026-01-09 01:13:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e9dc5a52-cf8e-3c31-a374-9c2382a7325f | 2.54753 | -60.57754 | 2026-01-09 01:13:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 33.1 |
| e238dd40-a476-365d-821f-deb5244c0d1b | 2.55678 | -60.57883 | 2026-01-09 01:13:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a747ad3d-c5ca-312c-bb42-5067b0284162 | 4.51748 | -60.66921 | 2026-01-09 01:13:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4cd2a586-0637-350b-b56f-f46681558cca | 4.5189 | -60.65887 | 2026-01-09 01:13:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 39d9d7e7-459f-373b-8d0c-fb6741cbe15f | 3.1779 | -60.405899 | 2026-01-09 01:18:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5d87c67f-1c4a-36bb-9f7e-5a241073d772 | 3.3832 | -60.23 | 2026-01-09 01:18:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c3b46f4a-6ee3-33be-b2be-df3366a70dd6 | 2.5499 | -60.580898 | 2026-01-09 01:18:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 41ea3317-b0a4-37d9-b7e0-e7d42cf64be8 | 2.5514 | -60.5741 | 2026-01-09 01:18:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9c69e367-b92f-3547-b2d4-f20ba6b3d422 | -4.2539 | -43.7843 | 2026-01-09 01:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| a4906e67-79bc-32ad-87d8-61e91bf10f08 | -4.2726 | -43.7832 | 2026-01-09 01:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 0fd5a804-2a42-3359-a502-92b93bf50dbb | -22.8293 | -49.2836 | 2026-01-09 01:20:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 93f7780f-4053-3d7e-b146-7986b42964c5 | -4.2539 | -43.7843 | 2026-01-09 01:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| c4eeb7c1-ed92-379d-84ef-64673a4f0f6e | -22.8293 | -49.2836 | 2026-01-09 01:30:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 89.1 |


[Clique aqui para ver as próximas entradas](README2.md)
