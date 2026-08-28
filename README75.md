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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a40cccd0-3907-3ee9-9b02-7e0e56670898 | -10.7839 | -50.6346 | 2026-08-28 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 2248e434-3642-3cde-bf23-13b9f25e7b5b | -13.4191 | -51.4159 | 2026-08-28 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 82adb2c8-f6a5-3624-8b41-37f8e8058375 | -11.2693 | -54.0129 | 2026-08-28 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 91b15542-64f2-3408-9ca0-661ffd30de21 | -11.269 | -54.0334 | 2026-08-28 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| ea1235c3-da2c-3540-ae2e-9c6bce781e8d | -11.2314 | -54.0164 | 2026-08-28 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ce1cc4d2-ca34-309e-9f0f-bd1f93de7c76 | -12.2277 | -50.5792 | 2026-08-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 6551d3b7-cd16-3328-9479-29ddd8f156f1 | -11.2879 | -54.0317 | 2026-08-28 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| ec82a4c0-a100-3174-9037-b33e10ad5e0f | -11.2493 | -45.0501 | 2026-08-28 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 7dca8e3f-d767-30b2-8f23-201a75717010 | -8.0928 | -45.8354 | 2026-08-28 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 59b812da-5d9d-3f99-8001-10894a381eed | -7.0654 | -43.5978 | 2026-08-28 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 832e4445-7738-3d70-8b76-5045c39afe87 | -7.0656 | -43.5745 | 2026-08-28 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| bed2687d-480c-3c8d-abd5-1cccd9618a0c | -13.3258 | -46.9107 | 2026-08-28 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 5555305e-cabf-379a-b8de-03367c62daa6 | -8.872 | -66.90865 | 2026-08-28 13:29:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 92dee841-f915-3565-a3a6-e28f8fcb40b2 | -8.88457 | -66.89557 | 2026-08-28 13:29:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| f3543466-2921-3236-8302-09421024540b | -8.87469 | -66.88766 | 2026-08-28 13:29:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| f07f8a2a-6664-3bfe-b9d5-32b653491821 | -12.3038 | -50.5915 | 2026-08-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 2c5d2ff0-20f6-35f0-8498-534c72e3a7dc | -10.8028 | -50.6326 | 2026-08-28 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 2092c337-fc8f-336d-92f6-fe1dd26f4542 | -14.9791 | -52.5951 | 2026-08-28 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| e2ffb1d5-6955-3c82-848e-a744597a57b6 | -7.603 | -61.3415 | 2026-08-28 13:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| c429b0a7-99b8-3f7e-bbc0-b55389d1eb8d | -7.6214 | -61.3408 | 2026-08-28 13:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 315.6 |
| 596124f1-7f1a-31a0-a038-35d67be484b7 | -13.3258 | -46.9107 | 2026-08-28 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 641a6821-d280-32b3-83a9-908bd3139b01 | -13.4194 | -51.3945 | 2026-08-28 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 053578c8-ff1d-3d42-9499-a177c13f30f1 | -9.9708 | -53.9419 | 2026-08-28 13:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 43dc3484-f2b1-382f-be01-1135930eeaa5 | -10.7839 | -50.6346 | 2026-08-28 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 295.7 |
| 4a965d67-e1eb-3431-a8b3-3e3a0f6dd8a6 | -10.7596 | -54.0384 | 2026-08-28 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| ae965dde-c71e-3e47-9a3f-d34cc95e303a | -6.2693 | -53.1322 | 2026-08-28 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 13e49e09-fee7-35f0-9b2e-2d16849e6cf8 | -6.1472 | -57.7995 | 2026-08-28 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| d16aa403-39e8-3220-aab9-f64ba5720f34 | -12.285 | -50.5724 | 2026-08-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| cebce178-eab8-33d0-920f-47b9a5bc11c7 | -6.1656 | -57.7988 | 2026-08-28 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 213.9 |
| baf0549b-ff94-3db6-8b7b-53e8743149ae | -16.6644 | -50.1605 | 2026-08-28 13:30:00 | GOES-19 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 4f0f5d8c-88e1-32b1-a836-31031079f9df | -12.2854 | -50.5509 | 2026-08-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 64849e43-2586-3902-a9c6-da2fc7594922 | -13.4191 | -51.4159 | 2026-08-28 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 354f98c9-d486-31b6-83a1-38740d40c9cc | -11.2109 | -51.2476 | 2026-08-28 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3b2e87e2-80e6-33f2-9a7f-22c36ecb0265 | -12.209 | -50.5601 | 2026-08-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 9e912a05-1ec9-32e8-9627-a0694d05c4d7 | -10.899 | -50.5159 | 2026-08-28 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| aa408d6c-4cf9-30ab-825e-a6a5501b5f6b | -11.8239 | -47.2178 | 2026-08-28 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b48bbcd6-80fd-390c-b4b4-c3edf2da272b | -12.2281 | -50.5578 | 2026-08-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 200.1 |
| 51b4dcd5-19d9-3d39-8a90-74c9f6b39b7d | -8.5969 | -54.7755 | 2026-08-28 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 9d60e4ef-8cae-3acf-851c-8938c0896931 | -11.2111 | -51.2264 | 2026-08-28 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| fd9375a9-a023-30f3-b7e7-de02a5149dfa | -10.9556 | -50.5311 | 2026-08-28 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| e272e3ba-56bf-377e-b1b9-6bc3b5858d62 | -10.937 | -50.5118 | 2026-08-28 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 1df7db5a-d534-3d76-a120-62714c78894c | -12.3041 | -50.5701 | 2026-08-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 212.5 |
| 32bc5baf-7688-303a-af16-c8b7e2db7a17 | -11.2302 | -45.0528 | 2026-08-28 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 97e4cba9-f3b4-3979-8422-64de6979736d | -21.0372 | -57.8494 | 2026-08-28 13:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 86.0 |
| b99d62cf-9d23-37d6-89c4-f1e222c6f878 | -6.1657 | -57.7793 | 2026-08-28 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| c795a2f2-494c-3ff7-8d53-432f300149dc | -6.2692 | -53.1526 | 2026-08-28 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 9b0487d6-6a77-3c63-9fc4-2bc17bf96676 | -2.7303 | -47.0644 | 2026-08-28 13:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| a1b60396-61b4-3c92-a8c2-4866687e89c5 | -10.918 | -50.5138 | 2026-08-28 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 4b3d54d5-e233-36b9-8a1f-cd9e96f30328 | -11.3285 | -48.3895 | 2026-08-28 13:30:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 324fcdd6-0e47-3512-94a9-9cda5afbd676 | -14.3182 | -51.7046 | 2026-08-28 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 128.3 |
| b5ae66a2-9bc2-309f-9f36-1f02f9fbccd9 | -6.6048 | -55.4536 | 2026-08-28 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 5b4d6cce-b8f4-30f1-a94a-ae321dd18124 | -14.9985 | -52.5925 | 2026-08-28 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 819c2fdd-3e69-32ce-9914-d134be6751ac | -11.2493 | -45.0501 | 2026-08-28 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| e152eb86-d0e2-3128-9756-1c034c71caee | -8.5968 | -54.7957 | 2026-08-28 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8d67c317-7933-3808-a92b-c1f58f95d379 | -16.6841 | -50.1572 | 2026-08-28 13:30:00 | GOES-19 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 38a59ad2-71ec-3fda-bc18-8c4ac2f0ccdb | -8.59797 | -70.21007 | 2026-08-28 13:31:00 | TERRA_M-T | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 18.5 |
| e73e9bc8-0734-303b-9b0b-2dac21588688 | -11.82775 | -64.9911 | 2026-08-28 13:31:00 | TERRA_M-T | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 28681385-e490-3f3c-9309-5a9a7a54acc8 | -9.28028 | -68.77998 | 2026-08-28 13:31:00 | TERRA_M-T | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 11.3 |
| bb187d73-bc33-3ed7-b120-4fd627949219 | -10.50628 | -64.51265 | 2026-08-28 13:31:00 | TERRA_M-T | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 101.4 |
| e5747da4-0d96-3fe7-af1b-097cd13a9d2f | -8.60806 | -70.21137 | 2026-08-28 13:31:00 | TERRA_M-T | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 317099ff-c115-3ce0-b788-ccd4df4ee128 | -10.49875 | -64.50655 | 2026-08-28 13:31:00 | TERRA_M-T | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 5e3df91c-68f1-3b2a-8905-d80c0617beff | -6.1656 | -57.7988 | 2026-08-28 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 185.1 |
| ce460e11-5f80-35db-b24d-c05a6482d026 | -10.9556 | -50.5311 | 2026-08-28 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| f16bac02-b6ec-3958-b83b-c31e713c97d6 | -11.8239 | -47.2178 | 2026-08-28 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 5a0a2b22-ec82-3d77-9bd0-9d5be07e9843 | -11.6586 | -50.4532 | 2026-08-28 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 25150ee5-29c7-3e49-86bd-ac76acedfa4e | -14.9209 | -52.6029 | 2026-08-28 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 0a79eac6-d4c2-3940-a63d-45284ddf11fc | -6.2693 | -53.1322 | 2026-08-28 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 2ee44998-b8d6-3826-b8b9-003874618a04 | -10.498 | -64.5193 | 2026-08-28 13:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5a3276cf-d449-3586-8072-7f81d3862ea4 | -9.9708 | -53.9419 | 2026-08-28 13:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 158.5 |
| edd6be98-677c-34bd-9673-bd9711c2deed | -11.7786 | -47.6474 | 2026-08-28 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 86401885-6bd6-33fb-bda6-a2882f9800d0 | -6.5863 | -55.4546 | 2026-08-28 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 4b6d8141-81cb-380d-8f4a-d9c7a78cbc19 | -12.209 | -50.5601 | 2026-08-28 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 66824d1a-75da-3cbc-8572-2d7f022390da | -11.2128 | -53.9976 | 2026-08-28 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 55d7c3e1-4f1a-3708-b78d-9b6d35d7b457 | -6.1657 | -57.7793 | 2026-08-28 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 8debf0ce-d12b-3d98-8b76-346ccd82577e | -12.2281 | -50.5578 | 2026-08-28 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 418.3 |
| 2181c3bc-a932-3d59-9cd3-11b73c4a45e2 | -11.2693 | -54.0129 | 2026-08-28 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 8500444f-ee53-37d6-ad26-023e70e4c182 | -10.9367 | -50.5332 | 2026-08-28 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 573ce378-fe9f-3b5d-9d49-dc5f132ef9f0 | -21.0372 | -57.8494 | 2026-08-28 13:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 4488c0d7-0e2f-3923-8273-5fc0725a6ce3 | -14.9791 | -52.5951 | 2026-08-28 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| f705221c-43ba-33eb-8676-d8018ac31ef2 | -12.2277 | -50.5792 | 2026-08-28 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 985cb154-88fb-3d59-abe7-466621654287 | -11.2882 | -54.0111 | 2026-08-28 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| bf48f381-0897-3880-844b-9ab63204d68f | -8.9478 | -62.4084 | 2026-08-28 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 35d7d6b7-58e6-3d67-ba3c-e39c02c57347 | -14.1784 | -48.7703 | 2026-08-28 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2ab97a39-06a3-3801-95ba-cec4df03ccbc | -6.1472 | -57.7995 | 2026-08-28 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 8639aab8-b5a0-36e5-80fe-b9b4ca7cfd01 | -10.937 | -50.5118 | 2026-08-28 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 5ed6995c-d3bb-3efe-b124-d33eee714e4f | -11.269 | -54.0334 | 2026-08-28 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| d78fe65e-9020-3fd7-8b13-637606e991df | -13.3258 | -46.9107 | 2026-08-28 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 53c09c1c-bcee-31a0-ba27-d7955c71038c | -11.2317 | -53.9958 | 2026-08-28 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 4efa0ab8-f7e8-337d-9de4-d42d89a9b2dc | -7.6214 | -61.3408 | 2026-08-28 13:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 211.8 |
| c1cd48a1-58c7-384b-a336-1247d23e2fb2 | -2.7303 | -47.0644 | 2026-08-28 13:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b4707add-1907-32b3-9f61-2d14dade117e | -8.5969 | -54.7755 | 2026-08-28 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 5f923cc3-69ca-3d76-acae-5e1ad6f25d89 | -10.899 | -50.5159 | 2026-08-28 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b6371e43-c0f7-3056-99a0-1d1db1fff87f | -6.6048 | -55.4536 | 2026-08-28 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 3f701629-84f3-36a5-b546-1c8fcec2e382 | -10.8028 | -50.6326 | 2026-08-28 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 602b89aa-bc99-34b1-93d2-d4b8f276ddb6 | -11.2879 | -54.0317 | 2026-08-28 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 138.4 |
| b1a05a60-2f3b-3074-9fdd-9581dfbab0cf | -12.0733 | -47.1614 | 2026-08-28 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 710cd78d-0c73-390b-8cef-2c50e8546e77 | -13.3985 | -51.5037 | 2026-08-28 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| c7d53408-f711-3bbe-8841-6b9df24f484d | -6.2692 | -53.1526 | 2026-08-28 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| eb89c1de-8774-3926-8292-1e63634c6356 | -14.9985 | -52.5925 | 2026-08-28 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 3eac550b-95f4-338e-af67-c38b6dd67565 | -16.6841 | -50.1572 | 2026-08-28 13:40:00 | GOES-19 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 101.4 |


[Clique aqui para ver as próximas entradas](README76.md)
