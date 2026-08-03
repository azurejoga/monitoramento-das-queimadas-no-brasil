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
| 1a7c7b4f-7d0d-3776-aadb-6596c06297ed | -7.5749 | -45.0923 | 2026-08-03 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| af736385-add5-3cce-972a-f1cdd07df12e | -7.5747 | -45.1151 | 2026-08-03 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 5ff23fde-ff7d-3476-8094-a9a9a00f334b | -6.5699 | -55.156 | 2026-08-03 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d0b83617-09ca-3ded-a224-013be6f538a5 | -6.5512 | -55.1769 | 2026-08-03 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| e42f2019-8fae-3298-a7e5-d80adb93915b | -1.6591 | -54.4543 | 2026-08-03 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 138.6 |
| f6e495f7-146d-3939-91a0-beb717ad84bb | -6.5514 | -55.1569 | 2026-08-03 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 68ceaaf9-ffdf-3927-8739-15572f9804df | -1.6408 | -54.4545 | 2026-08-03 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| aa8eb665-00b0-3440-b506-37734e6f0606 | -1.6408 | -54.4745 | 2026-08-03 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c48d703e-37cc-3e8c-83f3-1521168e0ca2 | -6.5699 | -55.156 | 2026-08-03 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 549825df-22f0-32c4-8257-c1e355fbf5ea | -1.6408 | -54.4545 | 2026-08-03 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 151.3 |
| eaf958f8-c1b8-37a7-87d5-a577a0b0758d | -1.6408 | -54.4745 | 2026-08-03 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3235e6d1-1d24-3553-b886-1775637a0d34 | -1.6591 | -54.4543 | 2026-08-03 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| abc3fcc7-c94a-3f15-8996-6b93ea061faa | -6.5512 | -55.1769 | 2026-08-03 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f4e15aca-19a8-3738-b11a-95042494460a | -6.5514 | -55.1569 | 2026-08-03 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| ad4e54be-362d-3b7d-ad87-78eda3aa888c | -7.5747 | -45.1151 | 2026-08-03 00:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| fb3702ce-9161-37c5-9011-a611013698ba | -1.6591 | -54.4543 | 2026-08-03 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 28d20a0e-4ef5-3781-b05b-37ed2cdcaed4 | -6.5699 | -55.156 | 2026-08-03 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 4ef4a511-5d4d-3aa0-b845-f7e31929b40d | -7.5749 | -45.0923 | 2026-08-03 00:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d1119bdf-57d2-3d0b-89e7-4297ee24f57b | -6.5514 | -55.1569 | 2026-08-03 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 97d7ee85-e3ce-3c7c-869a-dab9648f8022 | -1.6408 | -54.4545 | 2026-08-03 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 3eee0bdc-1e8b-3165-9dd2-1d47a468b453 | -6.5512 | -55.1769 | 2026-08-03 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 0888aabd-65aa-353f-8385-d7d5a53e8920 | -6.5512 | -55.1769 | 2026-08-03 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| a006c01f-4bb4-3fc8-9cb6-062544f3907b | -1.6408 | -54.4545 | 2026-08-03 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 8ab66e84-079c-3013-9397-eec336d83acb | -6.5514 | -55.1569 | 2026-08-03 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 9fc5fffa-6375-3905-aef6-724fc4764c5e | -1.6591 | -54.4543 | 2026-08-03 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 79d13994-899a-3f59-8181-e2a282b9febd | -10.5738 | -46.797 | 2026-08-03 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| e2f3abe9-070c-3227-8d96-d1418174ba81 | -6.5512 | -55.1769 | 2026-08-03 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f51d9838-3c1e-3ee3-b2ca-8c70c1ae0f72 | -1.6408 | -54.4545 | 2026-08-03 00:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 6c84e9bc-0a03-3a1f-a25a-23f2751020f3 | -6.5514 | -55.1569 | 2026-08-03 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 67e63049-c794-3b6d-bbc0-579945b3b891 | -1.6591 | -54.4543 | 2026-08-03 00:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 361baa40-36be-32e0-a667-612fc99651d4 | -1.6408 | -54.4745 | 2026-08-03 00:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 14fb5c76-1d2a-32b9-bd8a-3af8b23da209 | -1.6591 | -54.4543 | 2026-08-03 00:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| b7359c10-f9ea-30c6-9fc1-76dd19e0c898 | -1.6408 | -54.4545 | 2026-08-03 00:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 981324bd-8744-3409-b7c7-06c9f9895e22 | -6.5514 | -55.1569 | 2026-08-03 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 116085ba-a7b5-3fb0-884c-174b84f05e5f | -10.5738 | -46.797 | 2026-08-03 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 4518512c-4060-3586-89f8-1eadbe209832 | -6.5514 | -55.1569 | 2026-08-03 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1105608b-0cce-3ea3-a250-bce3bb0aafd5 | -1.6591 | -54.4543 | 2026-08-03 01:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| c2c32984-b459-3145-86ab-e592e9967a25 | -1.6408 | -54.4545 | 2026-08-03 01:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 89034923-1886-36ad-ba71-9a562ae63941 | -6.5514 | -55.1569 | 2026-08-03 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 923d1783-dfc3-37df-bd69-43c29b60cab6 | -1.6408 | -54.4545 | 2026-08-03 01:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| c60e3ce9-54f8-30ad-b37d-53bd46245fc6 | -1.6591 | -54.4543 | 2026-08-03 01:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| c039be69-a39e-3225-9936-2cb1e7e33020 | -7.25309 | -59.45541 | 2026-08-03 01:13:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| e42a05ac-99b8-39a8-b2d8-0f1f7885c123 | 2.53564 | -60.35801 | 2026-08-03 01:17:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 28.7 |
| f6cdf280-6192-3e33-ace8-a03496ab14e4 | 4.36097 | -60.8172 | 2026-08-03 01:17:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 9122ab15-7474-33a6-954e-f5ee44528fb5 | 2.53627 | -60.36354 | 2026-08-03 01:17:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 35.3 |
| c2668b36-5a83-339d-b039-b10ec27c70e9 | -1.6591 | -54.4543 | 2026-08-03 01:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 4bf996f0-76ae-3194-9514-8a43092d7e9f | -1.6408 | -54.4545 | 2026-08-03 01:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 872823e1-81ba-3718-8bb0-5bf60277c703 | -10.5738 | -46.797 | 2026-08-03 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 2b7a4881-a248-3ac1-84e6-bfc522b7a2ec | -6.5514 | -55.1569 | 2026-08-03 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a9003449-f85e-380a-9408-1b34e8cec0d9 | -6.5514 | -55.1569 | 2026-08-03 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| fbea3d2a-b512-3ef6-a67f-62991d762621 | -1.6408 | -54.4545 | 2026-08-03 01:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 7780fc85-028d-3d06-acc9-919608739268 | -1.6591 | -54.4543 | 2026-08-03 01:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 61f77144-aabe-3d0a-933a-969384648824 | -1.6591 | -54.4543 | 2026-08-03 01:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| d055a433-01c1-306d-9379-a891a00c4422 | -6.5514 | -55.1569 | 2026-08-03 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 91ec8d48-a12c-3ff6-a6d3-4e53c28d2dc9 | -1.6408 | -54.4545 | 2026-08-03 01:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 1a67d5c0-c687-3b01-8a5b-4a4d76b0dfd4 | -1.6591 | -54.4543 | 2026-08-03 01:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 477538a4-a2ae-3920-a8e5-118864e1a466 | -1.6408 | -54.4545 | 2026-08-03 01:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 83b9a26a-38b2-3215-b945-236aef8135f4 | -10.5738 | -46.797 | 2026-08-03 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| b8b4dd6e-c3c8-34e9-9c60-c4d9bf5f2ab4 | -6.5514 | -55.1569 | 2026-08-03 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a0392d14-f8db-3dc2-9c64-002023d4f2a2 | -6.2333 | -55.637299 | 2026-08-03 01:54:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46b3e7d5-7039-3312-b2ef-cccce39952f2 | -7.2459 | -59.438702 | 2026-08-03 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f737ba4-bece-3494-a2a8-dbeae63bdc66 | -7.2556 | -59.436298 | 2026-08-03 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cbf5c901-a93f-32e3-b244-84ce98828e67 | -6.2346 | -55.6031 | 2026-08-03 01:54:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d996cab3-0b88-32a6-831a-8a7f7302ad80 | -6.2428 | -55.6348 | 2026-08-03 01:54:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6c5705c-7de7-33bf-92d9-e9e3b9d5aa49 | -1.6408 | -54.4545 | 2026-08-03 02:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 69633f8e-3cc5-3c52-8b99-605bb81975ce | -6.5514 | -55.1569 | 2026-08-03 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| fa93e41a-ab48-3b58-8d50-d0fdd4a881e3 | -1.6591 | -54.4543 | 2026-08-03 02:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| a95cdfea-fda5-3934-af06-d906817849ad | -1.6408 | -54.4545 | 2026-08-03 02:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 79e87ebd-7d4a-3694-b29a-277ade8372bc | -6.5514 | -55.1569 | 2026-08-03 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 9c0dfebd-fa20-3933-b458-d07db8fe5739 | -1.6591 | -54.4543 | 2026-08-03 02:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| cdc92e22-4782-3b24-aa43-8ee1249892f9 | -1.6591 | -54.4543 | 2026-08-03 02:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 32d6dcd0-7d72-352d-b09b-3240888552d1 | -10.5738 | -46.797 | 2026-08-03 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| d5362dc7-dfb8-397e-a310-7463644395bb | -6.5514 | -55.1569 | 2026-08-03 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c140d58f-2a1c-3cc6-80c9-98a54fc0206a | -1.6408 | -54.4545 | 2026-08-03 02:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| e80f4b5c-6670-3cde-956e-10ad4bb20bcb | -6.5514 | -55.1569 | 2026-08-03 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 29e8c190-19d0-3c7d-8af8-954ec23a943b | -1.6591 | -54.4543 | 2026-08-03 02:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| eff2b53c-6b3a-3062-bb6c-e544c743fde7 | -1.6408 | -54.4545 | 2026-08-03 02:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| d60b23b8-419e-312b-8a3d-73b5a456cc22 | -1.6408 | -54.4545 | 2026-08-03 02:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| b7c639b4-41b8-391a-9ce2-4034e4739103 | -1.6591 | -54.4543 | 2026-08-03 02:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 00c3cd43-fdb9-351f-a2ed-d93d85a4b412 | -6.5514 | -55.1569 | 2026-08-03 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 60e63152-9489-3443-9301-d948db05ed6e | -1.6591 | -54.4543 | 2026-08-03 02:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| e21b8659-4dcb-3363-9774-0739e48160c5 | -1.6408 | -54.4545 | 2026-08-03 02:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 3bb40645-5e37-370d-b3dc-96c2d2f49efa | -1.6408 | -54.4545 | 2026-08-03 03:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| eb56e330-47ca-3832-af8a-21428649e918 | -1.6591 | -54.4543 | 2026-08-03 03:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ba270078-b452-3e86-8a86-287e8ef51781 | -1.6408 | -54.4545 | 2026-08-03 03:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 338fe9e4-365f-3c63-a5c6-f368500128df | -1.6408 | -54.4545 | 2026-08-03 03:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 51c68322-1334-3d4c-82ef-ff15328f73ee | -3.98014 | -48.43391 | 2026-08-03 03:42:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9050bcb-5709-37d3-8542-427d5e01eb4b | -7.19313 | -36.60355 | 2026-08-03 03:42:00 | NOAA-21 | SANTO ANDRÉ | PARAÍBA | Brasil | 2513851 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c1992e14-f2ca-328f-a8d1-7f9a8bd65258 | -4.39547 | -40.84443 | 2026-08-03 03:42:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 26b17c9f-6021-3855-8a93-fda174a2f9e8 | -3.89987 | -38.53975 | 2026-08-03 03:42:00 | NOAA-21 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57b30e38-aa53-3274-9f72-82b2502ceee4 | -6.30102 | -44.88302 | 2026-08-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70127933-c7d2-39f3-ace3-246d9bfceea1 | -5.73721 | -43.27687 | 2026-08-03 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dd4027b4-c7ed-36bb-9b7a-744e0c7fbfd7 | -5.97292 | -45.01129 | 2026-08-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ecc8e20-53df-3cd4-aab0-1e5084cce996 | -3.89743 | -38.53735 | 2026-08-03 03:42:00 | NOAA-21 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e08e83cb-a45a-3272-a45a-57a793bb88e8 | -6.30164 | -44.88084 | 2026-08-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faadaec7-9f08-3c34-9208-829fcfca781f | -3.97716 | -48.43332 | 2026-08-03 03:42:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bdf7f3a6-029e-33b1-a898-679ef775767d | -5.73772 | -43.27396 | 2026-08-03 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| df3c0463-a3dc-3009-87d0-9fa8f1437a6c | -4.52345 | -38.55014 | 2026-08-03 03:42:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d57d1aa8-91a4-3061-95d8-5f858dd5c1a0 | -7.03146 | -42.88571 | 2026-08-03 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3c4c895b-c1eb-3ea7-9567-e19687d5f0ae | -5.71919 | -44.50444 | 2026-08-03 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README2.md)
