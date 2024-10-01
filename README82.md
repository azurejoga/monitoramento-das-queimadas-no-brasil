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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4e4d070-b77e-37cd-a3cc-5a926edfb1dc | -12.96807 | -51.42621 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 99a66918-df0c-3728-b2bc-4f41113a2875 | -12.96804 | -51.22643 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24852e67-e738-3701-955e-9ef788f444c1 | -12.96778 | -51.23864 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0d4292d2-9065-3b69-9ea5-d9115cea3499 | -12.96697 | -51.24319 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2f917c9b-1fe6-3581-b13a-2c4ca8d63b59 | -12.96659 | -51.35864 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34395f1a-681c-3e74-8048-4f3c0d0c8cff | -12.96657 | -51.25903 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11d6c089-f90c-38e7-9618-9503e8ee937a | -12.96615 | -51.24774 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 34583b48-77dd-3f69-9df4-4c5cedc9abeb | -12.96576 | -51.22416 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a89f69c-49e5-308f-98bc-68341bda5809 | -12.96573 | -51.36326 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 23bfd0a7-0994-3b29-8517-dad3088c8e1d | -12.96531 | -51.31552 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7269fb70-e258-3f01-a604-192246742334 | -12.96495 | -51.22869 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e925a154-f5f4-3251-b4b8-a94357dc996c | -12.96488 | -51.36788 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 715b3d05-98b9-3b51-bf50-76c50ffbdc42 | -12.96465 | -51.24455 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d8cf706f-754c-38f9-a729-66b05cbd0651 | -12.96452 | -51.25685 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ec236a0-11c4-3cea-8fff-1ec000fbd38c | -12.96414 | -51.23323 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 260d13fd-f674-3bf8-acf9-1d51624000a3 | -12.96269 | -51.43 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3747935a-3920-3d75-b5de-0fd50a103710 | -12.96251 | -51.24232 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 724cc227-4e6f-361d-b25a-accb7cb38de0 | -12.96183 | -51.43466 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fe60e4d5-128d-36c3-868c-142ce68e4b3a | -12.96131 | -51.22331 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8704fd0f-3e97-3d6e-8b66-e262c961e381 | -12.96124 | -51.36239 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ac52278f-995b-35d6-82c2-20dfa91c5036 | -12.9601 | -51.444 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cb1293a9-df34-34e6-8c5f-79f70e7cb3f4 | -12.95913 | -51.22473 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 117512f8-8688-31a1-a118-977e687b0c8e | -12.95847 | -51.35229 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 875b54fe-296d-327f-b62d-8475e75c0d4d | -12.95604 | -51.22697 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e12dd019-1a94-302b-9710-b1348d4be8a5 | -12.95467 | -51.22387 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2f63ed99-2019-3c7b-92f6-3cd42f53e615 | -12.95382 | -51.22839 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 047deaba-138b-323c-893e-075935c46dc6 | -12.9528 | -51.4329 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 27.4 |
| c788bbcf-21d6-3996-8918-f2b244c9c75e | -12.95193 | -51.43756 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 28ee87e4-00d6-3f3e-acdc-276c460eb7c2 | -12.95158 | -51.2261 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77efa377-f0a8-3490-8c61-4a6932a58309 | -12.94932 | -51.45159 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 160067e9-86b4-32bf-acb0-5bbc26c765d9 | -12.94828 | -51.43203 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e856b1f-283e-3842-856b-b0efc55dcc00 | -12.94567 | -51.44604 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 863ee029-9796-33f0-882f-8bd603c6c31a | -12.94289 | -51.43581 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 38d29b53-da0a-3d5d-85d5-5181304d8843 | -12.94115 | -51.44515 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |
| d4ca57fa-f1a4-3d44-b0dd-7aab16b1b0bc | -12.93751 | -51.4396 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2f93573d-9feb-38cf-a002-072a9f8a7078 | -12.93663 | -51.44427 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 42158655-f236-32df-9fc1-694f2ef2a3a2 | -12.93401 | -51.45827 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 83216e7e-89de-3384-be5e-0d3d0e448cd4 | -12.93225 | -51.43695 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd1856f7-eb46-38de-869b-f92ae5050993 | -12.93211 | -51.44338 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| a83faffa-e913-30f0-8420-59d8b2f1ae3b | -12.93124 | -51.44805 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 6503d41a-db17-3144-a15a-2e6697a8c681 | -12.93057 | -51.4463 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 256248ad-8e0b-3959-825d-14599f04f348 | -12.92973 | -51.45098 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a0e49aa1-8a87-3f76-8255-2ea25b0a48da | -12.92521 | -51.45009 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 805d8346-ab27-3bbb-8d56-fd9a801e7283 | -12.91815 | -51.46327 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4039d43e-4cc1-3c60-acf6-7a107ceb9594 | -12.91605 | -51.29467 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 234a5d88-a16f-30f4-b5e1-fe3d1c14c23e | -12.91415 | -51.46413 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1e6fe0d0-5497-3eff-9ef3-967b6d9dab20 | -12.91362 | -51.46239 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cdb520c-0420-33af-a829-7dcd4767a20e | -12.91074 | -51.29839 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2203cfe5-5ebf-38f9-83bf-9f83d82651e3 | -12.88132 | -51.30694 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7725700-1f9f-3be7-8a90-44b44852a9a9 | -12.88048 | -51.31153 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 566f95b4-e2f7-38d4-9eea-2d5825bbe2d4 | -12.96721 | -51.43088 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ee70705f-7b17-361a-a089-fbb35da2129d | -12.96634 | -51.43554 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 98c4b089-0a54-3334-9485-f6c6e259406b | -12.96548 | -51.44021 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 20b396ad-5503-39ed-8460-60e18215be9d | -12.96096 | -51.43933 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ed76f5e-65d5-3398-a26f-78b14ea53fa1 | -12.95818 | -51.42911 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 75e1a9d5-e81e-33a1-850a-16ccbeb385f3 | -12.95731 | -51.43378 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 375922e7-241a-3eff-b366-4fa9927b11a6 | -12.95645 | -51.43845 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 1cea7a7c-397b-3138-9ebf-32591f9a24fd | -12.95558 | -51.44312 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 22facda7-8592-3a7b-afd3-e09cb9e8d04d | -12.95471 | -51.4478 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a8f57cb6-6a9d-301b-a32d-049050103d18 | -12.95106 | -51.44224 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 2114c706-6266-3438-a731-15e40b594e9e | -12.95019 | -51.44692 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 54136537-15e1-3611-90f9-6af8e4274dc0 | -12.94741 | -51.43669 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 04b4bf6c-8e97-350c-a838-038c28395d5c | -12.94654 | -51.44136 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 6db4479b-7c4c-38af-92cf-5b14fb8cd8ac | -12.9448 | -51.45071 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 28c5dedb-3bff-3423-9ce0-924a1cccc5c4 | -12.94393 | -51.45537 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 47cf0e48-e231-3cf1-9b44-b17664dc2e3c | -12.94377 | -51.43114 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80a02a3b-172f-32e8-9b69-d32972b90565 | -12.94202 | -51.44048 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| ba45ce68-df9d-3361-abc5-99f4c2f11213 | -12.94028 | -51.44982 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 9d6bc31f-c074-3c2f-8b7f-98a8726aa4d0 | -12.93941 | -51.45449 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8f4b6949-37bc-3c62-b8dd-6246dfc56643 | -12.93854 | -51.45916 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 33805bd2-fb85-3a1f-97f6-b1b365fe4a0c | -12.93838 | -51.43493 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a2629549-3f57-3da0-9117-b8b940d42135 | -12.93576 | -51.44894 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 5ef91c62-298f-302b-aced-fa394d653727 | -12.93489 | -51.4536 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7d4ab7c3-1a41-322b-9dfe-17f3b7defa4a | -12.93141 | -51.44162 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe1317c5-843f-3bd2-b467-17c0e3dcf886 | -12.93037 | -51.45272 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2ce9749b-6c75-3f32-b9cb-b2a018cce072 | -12.92949 | -51.45739 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 811032fd-9f15-370a-be7b-5ca609ad07f8 | -12.92889 | -51.45567 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d51053e9-53c5-3410-9b45-2ba235dd53c4 | -12.92584 | -51.45184 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae0bedb5-00d9-3341-83e9-1ed8f54ba590 | -12.92496 | -51.45652 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b7cf427-45a0-34c8-9ecd-4e34ee2885d9 | -12.92436 | -51.45478 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0ad4e0c-02cd-381c-9e8e-e353c943564f | -12.92044 | -51.45564 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74f6ad8b-74bf-39f0-bd48-eb9002883840 | -12.91984 | -51.45389 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e9460a5-5d0e-3ee4-bf08-578755b69ce1 | -12.9173 | -51.46797 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecca0d4c-828e-3c53-8d87-506631547b89 | -12.91591 | -51.45477 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf54f60f-b125-312e-8e33-4055f88c71b2 | -12.91446 | -51.4577 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df5d69a4-d9d8-3c91-9752-46240ee2bc00 | -12.91277 | -51.4671 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 859d95ca-5177-3ae6-a779-3de7f56016e5 | -12.71924 | -51.91895 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8f90f176-0176-3c11-9aa3-fc443861bf7d | -12.7179 | -51.917 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 8afa3e5b-ecf4-3e9a-b573-79d80479202c | -12.71548 | -51.91316 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| b9cf2b94-b290-3fd9-9c93-9334b88ced61 | -12.71455 | -51.91808 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a93d221f-55fc-3453-8f77-d3b6aa1878d3 | -12.71321 | -51.91611 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 2460ddfa-3f81-3103-893b-90bf625eefbb | -13.22418 | -51.21643 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 385489d8-4cf1-3eeb-a679-bad2f7cbeced | -13.22336 | -51.22092 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6959c64e-0d19-317e-979e-476a3239e5ad | -13.21975 | -51.21557 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| b9d7f658-6e5e-3bd3-a5e1-3bde8796fc81 | -13.21892 | -51.22005 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4be9cf3c-89d6-3a1b-bf47-78e79a82ff92 | -13.21532 | -51.21471 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 8ae9e85d-d6a8-32f5-a0ff-88d0161e8ccd | -13.21449 | -51.21919 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f2721053-7047-333e-bece-de8417a8c5ce | -13.21089 | -51.21385 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 178751e3-2306-3be3-8aca-7c8a70261257 | -13.21006 | -51.21834 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a9e7ea15-5c99-392f-9f4b-86007e215081 | -13.20563 | -51.2175 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README83.md)
