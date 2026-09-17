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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d9ef440-381f-3ea6-9e37-3b42d89989c1 | -8.88256 | -62.39003 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbe46c39-0f4d-30d8-a774-abcddcf4913c | -6.11805 | -51.70925 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea032417-dbb1-32cd-97ae-3113ddf76e80 | -8.64185 | -66.58534 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 894249b2-fff1-3196-bd91-124b68f48cf8 | -6.14368 | -59.94091 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7f64f7c-3fe8-3a3d-b83b-e993d7a77079 | -6.79621 | -59.19 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3dcc371-3c10-31fd-a453-c33796a70ddc | -5.14288 | -55.94136 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa4dc70e-1c48-3a0f-839a-eda36b4417af | -8.64632 | -66.58153 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 65b8c1c5-9828-3c98-85ed-c0605ac1a570 | -5.86294 | -52.06071 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48f4a0c1-7dde-3b59-a9ee-5d772321507a | -8.75765 | -66.56694 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea9f660b-bb3c-374a-9283-409e29cd28e7 | -5.1565 | -55.93916 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00a81146-65d0-3190-b36c-6e7103f9d8f2 | -9.2811 | -60.63667 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6de6089-46ba-378a-9efd-c1382d7b2b7a | -4.4539 | -55.43821 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1816cec-9338-301d-93e4-012679f68b42 | -6.68305 | -58.85235 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db40a54e-d8d1-3515-b3d1-98a9838e62a6 | -3.79943 | -60.72561 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e10c389-be33-3bd9-a784-cb7346557e87 | -8.15297 | -64.05247 | 2026-09-17 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2aa695e7-36d9-3217-8375-3daa1c15042c | -6.93451 | -63.02364 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 158f4fbc-7501-3691-a38a-505e83c1a1fd | -4.50882 | -54.97484 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 365d9e75-6167-3c86-9bd2-6f7d4644c9e5 | -9.29631 | -60.53556 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fa3446a-8dc1-3858-ad80-b04e28ac235d | -6.36606 | -58.29269 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d7fe454-12e1-3b53-9ade-6b5ba8985a4f | -9.25443 | -60.78992 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7da5becd-e545-3ee1-bb5c-bf79251a5eea | -5.14659 | -55.94616 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f0bbb54-3746-33f4-a9a2-e120ceb3695c | -6.80835 | -59.18325 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d2892ddb-6496-30d8-a294-7faa3d9962e6 | -6.79748 | -59.18157 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac0d1ee7-7d13-3509-8ddf-731378d7294f | -6.81152 | -59.16225 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee443487-c31c-3eb3-ad7a-c38e1b1139ca | -6.36986 | -58.29325 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75ed166e-869b-3793-a074-3e41a9c8d799 | -6.43319 | -55.61034 | 2026-09-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 862acc02-e039-32d3-a202-9c800fad9aa9 | -5.14721 | -55.94202 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20f12c57-3e9d-3678-96cd-d6a27d8a6884 | -6.37433 | -58.2892 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e93694a0-0152-3681-82f3-9f62f961c919 | -6.42366 | -60.00491 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aa9a64d-663b-3d65-9731-92d6faed3c06 | -3.69952 | -60.60558 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 965ae982-a215-3074-83c2-5d99f85bf6e2 | -8.65225 | -66.59167 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8b7e5b5-2423-31c5-8e81-d8be3eec0894 | -4.49412 | -55.50195 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62ad29f4-61cb-325b-a934-2e80f5ddeb37 | -9.28168 | -60.6328 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 681d8237-e5a8-3fef-a4b9-b02143b7c090 | -8.15517 | -64.06022 | 2026-09-17 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4864bcbd-9a8e-324c-8292-7c8a4b062961 | -4.73287 | -55.73676 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f550bde-8fdf-3190-9595-206d8e54e2e4 | -9.76954 | -60.46294 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab664e47-149c-3c75-8dc0-f4ea9dce0a08 | -5.86344 | -52.05703 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0201e61-f23f-3a1e-94b4-4b9e5eefe703 | -7.55312 | -62.33634 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e16e72e-75da-3b76-9272-6f7e493af5da | -4.85713 | -56.02729 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1785a9e4-bb78-3b91-8a12-23e318e16173 | -5.92725 | -51.64558 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a5b7463-ac5b-3227-86fe-87b71802b62f | -6.45759 | -52.8414 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d916e891-6ae3-3280-a974-e2b81507d326 | -5.66404 | -60.23655 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 362391fa-813a-37e9-8825-999900b2df15 | -6.79762 | -58.7877 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3373488e-9b1d-3073-b255-4ec7fbd02d9a | -7.97288 | -62.04223 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a75b072-0d49-3fad-a7e9-9823987f425d | -6.93063 | -63.0266 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0b54398-7e8a-3e23-b09a-ecd099aa0844 | -6.92787 | -63.02259 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 880af19a-8ae3-30b2-91ab-e84284ab3d56 | -4.42153 | -55.50368 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe4b9fea-7b22-3d7d-bc63-046e84c9b092 | -9.2752 | -61.3892 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 122e5db5-c887-3834-ac08-3fe85301fcac | -4.4466 | -55.20866 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45018274-c310-3deb-88ea-c9bf5b8202b1 | -9.09562 | -60.98277 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a51e3f5-4925-3995-95f9-e8b02dd4873d | -9.3813 | -60.3059 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a457b3a9-8154-3e86-a8ee-72472cd1aa66 | -6.32972 | -60.00359 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d2a2a66-c85f-365d-85cb-82aa49a79625 | -5.14226 | -55.94553 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a1eb615-0489-314a-9ca4-13cc7b103231 | -6.14427 | -59.93708 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93feac74-105a-34d4-97d5-d1068cd019ad | -4.51547 | -54.96163 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 238a1715-7165-35e3-b6ba-61e9af712941 | -5.75233 | -57.59131 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bf9f66a-3482-3958-b037-f7c6c5453b84 | -8.09607 | -61.81686 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd0e878c-ca01-30e9-834c-fc1a571845f4 | -6.71257 | -58.80764 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bdd379d3-6276-3ef1-b109-f92992313072 | -8.91796 | -62.40282 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a99147e6-3565-3d37-8a07-854e52f33e35 | -6.81388 | -59.17123 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a540bb55-1449-3b62-a949-2bb48763bf39 | -9.09902 | -60.96024 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b3fae24-42f1-3f6d-89fb-34a6b34af199 | -6.924 | -63.02554 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcd5213b-35fb-3e21-ae49-123ff46b6b41 | -6.31759 | -59.96635 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce01f71c-e514-3068-907d-3b6a02f08ac4 | -6.13775 | -57.69326 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1634d7f1-fd0d-38d1-8dd9-d3a13ff281df | -5.90885 | -59.94125 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c350cc2a-a459-3a10-8d41-21d364e7d9f1 | -6.11651 | -59.88554 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fa79656-9a32-3fb7-9ada-3073141c083c | -9.10702 | -60.95376 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e63fadb0-ae57-35e2-a325-9b29f2fb41ac | -5.86069 | -52.06499 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28e3a80d-119e-3700-bb8e-f39e882c9a2b | -9.39252 | -60.30349 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9d158cd-8841-3289-9740-3c52a707d341 | -9.09959 | -60.95648 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bd3d27e-7096-3896-8ac0-126143974142 | -8.22719 | -61.50259 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 191358e5-c996-3be1-9145-bed19b1e48f2 | -6.93672 | -63.03114 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adaa2e97-c8fa-3eee-8434-b4f900617cef | -7.80311 | -66.91164 | 2026-09-17 05:36:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0601d5f4-c4f0-3655-950d-580d200ba97f | -6.10265 | -57.63461 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2ec1ee4b-1e62-32f9-ac2e-0724c198047d | -8.49688 | -57.64077 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8dac4c5-2790-3697-82e8-38ac8e012324 | -9.09904 | -60.9833 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df419a49-476c-36bb-ada8-6c524239ddd9 | -3.7302 | -60.59941 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6b22bbd-f747-3e64-b425-26536b0f4965 | -6.36849 | -55.82968 | 2026-09-17 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4ffe209-02d5-3efd-8467-64e0c9a6efd8 | -9.28691 | -60.6217 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a2600a76-5f61-377b-a4fa-c2104e9b5e16 | -10.72292 | -54.00831 | 2026-09-17 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1cad4b1f-e77d-36e1-b23c-0b179eaa348d | -6.94059 | -63.02819 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 757cbc2e-971c-3810-9d40-54dc5080034f | -6.71227 | -58.80163 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f618f9f5-2bc4-3a75-ad0a-b5bfcf374a33 | -6.3152 | -59.97032 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 44aa392a-a290-3ac5-83a7-1353437fd55a | -4.41716 | -55.50271 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fae5bd29-464b-3325-9417-3f3d6261e04f | -9.18065 | -59.63189 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fab4121-2e5e-31b8-a26f-dab676c0b7fc | -8.09273 | -61.81633 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6696b907-621e-36b1-90b5-8ae90ed83df4 | -6.36743 | -58.28343 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac52c7d1-72e1-3c84-bf44-8b42bf63cc3f | -6.3158 | -59.96646 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5388b3c9-b640-3852-b374-1eed0d3105e0 | -3.69952 | -60.62725 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 022165bb-6589-3030-8ccc-0d73814566d2 | -5.75084 | -57.60123 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0ba4263-f416-3538-8a20-7c428c513254 | -6.14168 | -57.6938 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| def59aba-9458-3343-a148-c59c8edce274 | -9.10245 | -60.96077 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c599fa4e-85f8-350b-989e-431ec259d159 | -6.81815 | -59.16753 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92b3f30a-9db7-3a11-aaae-de2482a1eb5a | -3.70119 | -60.61668 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af8d5e57-1060-30b6-9803-ad49272ba990 | -9.59393 | -60.52269 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19278946-813e-3fa7-a89d-6bb1e0ff8a9a | -6.43415 | -55.61288 | 2026-09-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 425519b7-b594-355e-b92a-862bea5774da | -6.90729 | -59.02285 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 020b18ac-7e5b-379d-8600-e2b44b2cb520 | -6.70858 | -58.80107 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cbb91d3-26b2-3412-bdbe-10deca4f57cd | -6.69042 | -58.85345 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13c6dc7a-4ffc-39a1-a936-07558d78162a | -8.09552 | -61.82038 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README75.md)
