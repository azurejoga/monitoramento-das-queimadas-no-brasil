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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59c6dd66-f3a0-3e42-8906-69e1cfed6fa4 | -15.5666 | -48.3469 | 2025-09-02 00:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 285ddcd6-e32b-332d-b8dc-6ea8127b89be | -14.2692 | -45.2403 | 2025-09-02 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| f91f85d9-d509-3f21-95dd-929e1ecc21c4 | -10.45 | -54.7785 | 2025-09-02 00:20:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| cb33381a-dd32-394f-8cb9-02352dd4f871 | -7.6783 | -61.0908 | 2025-09-02 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 68566325-2ed9-3261-ab5d-0c4be78a8b26 | -9.8804 | -65.0139 | 2025-09-02 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 9efad0f5-685c-381e-b91a-777563525138 | -6.403 | -58.1979 | 2025-09-02 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 164.1 |
| 454097b8-c75e-33cf-bfd3-17192265bc30 | -7.6598 | -61.0915 | 2025-09-02 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d0a656db-4ea0-3f68-9c86-d11fe7f4f9a0 | -9.1207 | -61.4864 | 2025-09-02 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 6295a3ed-e70d-30ef-95ca-f25fd4219600 | -9.8617 | -65.0334 | 2025-09-02 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.0 |
| e313f3ad-2c40-3984-91b2-10df609b2b09 | -9.0799 | -65.4349 | 2025-09-02 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 526c25ea-6d8e-3319-9263-6060038dc70e | -9.1206 | -61.5055 | 2025-09-02 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 8cbea72a-e64c-3d00-939c-38bd8604b26a | -12.9197 | -56.9471 | 2025-09-02 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 8ffddd53-769a-3567-b49a-3a585bca51ba | -11.6647 | -57.3533 | 2025-09-02 00:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9468a626-19e3-3715-8fc0-74b79314899b | -11.1228 | -44.6288 | 2025-09-02 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 42d25ea2-0468-32f1-b006-f001810a20a0 | -6.403 | -58.1979 | 2025-09-02 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| c6095cb6-d0d9-3438-9839-df0660293c5b | -12.9197 | -56.9471 | 2025-09-02 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| bfc50fff-9e30-32dc-9621-dab262f301a2 | -6.4029 | -58.2173 | 2025-09-02 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 7661ddd6-5ea7-31ee-b699-037a4c4a6739 | -10.0617 | -48.1417 | 2025-09-02 00:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 1a5b32db-6b49-3289-b40a-72b1658e9cd5 | -9.1267 | -46.044 | 2025-09-02 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b87fe214-6610-30ba-98b9-39716548a66c | -10.4502 | -54.7581 | 2025-09-02 00:30:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 14c87413-ed89-3ee8-ac6d-05ddc1fcc2ee | -9.0799 | -65.4349 | 2025-09-02 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 9a1baaa2-7db9-3a97-8b86-232d1065356b | -10.062 | -48.1197 | 2025-09-02 00:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| ff2061d6-dee6-3559-af1e-2b3960c9c7c1 | -9.8617 | -65.0334 | 2025-09-02 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 2331c8f1-370b-3bce-87f1-df787a7fc4d9 | -8.6673 | -62.8369 | 2025-09-02 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 116.9 |
| de32a038-c8df-3a09-a92c-86965fa8c59e | -7.5292 | -61.3254 | 2025-09-02 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 776fffe8-e27b-3b13-b90c-5432b384c102 | -7.5291 | -61.3444 | 2025-09-02 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| a3c5dda3-d873-3173-942e-5f112c859a0b | -7.5477 | -61.3247 | 2025-09-02 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 216.9 |
| e651dc3f-1e99-331e-8264-66c139e4a45b | -11.1037 | -44.6315 | 2025-09-02 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| a13644d2-6e5c-3cd5-acec-2fed2b592bac | -6.2674 | -44.5213 | 2025-09-02 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 4096dab6-8637-3be5-8d19-54eb1ed170b5 | -8.8467 | -45.8034 | 2025-09-02 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 1871ec53-dab1-37e2-98dd-36dd1ac5e572 | -8.7154 | -50.4492 | 2025-09-02 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| dacede4e-30b1-3e9b-a879-4d230c2e2184 | -12.9385 | -56.9655 | 2025-09-02 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5bfd870c-6a20-3abd-a013-a6ec521e5dcb | -8.6487 | -62.8376 | 2025-09-02 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 0d8661b0-dd59-338a-88fe-b82b57a75f5d | -9.1207 | -61.4864 | 2025-09-02 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 63fc2b21-01f5-364a-8205-3be6b18069fa | -10.45 | -54.7785 | 2025-09-02 00:30:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| c3c69ab6-8261-3224-8705-b72fd4db3c98 | -14.2687 | -45.2636 | 2025-09-02 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 5bcfee58-da34-3931-800d-cb79702ccd12 | -3.2305 | -47.135 | 2025-09-02 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| c9c048b7-2e98-31f6-bfd4-8d72ceca1124 | -15.5666 | -48.3469 | 2025-09-02 00:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| dcf81ce2-c73f-38f1-bc00-af5e30511edc | -8.6674 | -62.8179 | 2025-09-02 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5444f418-2334-3dab-b4e5-6360dd3ac958 | -6.2676 | -44.4984 | 2025-09-02 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 8a15d486-87a1-3223-8c35-0f47da1653ca | -7.6783 | -61.0908 | 2025-09-02 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 4d3ea803-9916-3515-9e81-a3fb5de7d7e7 | -7.6598 | -61.0915 | 2025-09-02 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 88a3ad91-a8e0-3f1b-b890-1b2f85700896 | -14.2692 | -45.2403 | 2025-09-02 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 016c694d-d8ae-33c9-8622-06e5f950404d | -7.5476 | -61.3437 | 2025-09-02 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 217.1 |
| 14c3eecc-09f7-37f6-af55-5382752acd05 | -7.5476 | -61.3437 | 2025-09-02 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 208.0 |
| 2f94888c-ea7d-346a-8847-3d096412b55b | -10.45 | -54.7785 | 2025-09-02 00:40:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 7df2b860-bc9e-39d3-a25b-6eedb84ee9e3 | -6.4029 | -58.2173 | 2025-09-02 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 3efaa8cd-bbcf-3d39-8ff8-6f8eb14fcead | -11.1037 | -44.6315 | 2025-09-02 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| b32776d3-b61d-36b6-833f-b997c2879a80 | -12.9197 | -56.9471 | 2025-09-02 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a6c3e7a5-75c8-30e6-8f84-829d8bff2fae | -6.8095 | -52.8154 | 2025-09-02 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 9ef2b00c-e3a7-35f5-9bcd-ac797076a04e | -7.478 | -45.3512 | 2025-09-02 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| bc0149bf-36c1-3477-a532-d8b8137a7834 | -9.0799 | -65.4349 | 2025-09-02 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 962c3174-f816-362d-aa97-fef15c4014a4 | -6.7909 | -52.8165 | 2025-09-02 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| f53bf7fe-75fc-369b-9b7a-34f52b6fe9cd | -7.4778 | -45.3739 | 2025-09-02 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 8e995081-5b94-334c-aad7-83bb39e52d80 | -3.2305 | -47.135 | 2025-09-02 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 56104f0d-2162-304e-b294-b495e1267fd3 | -7.6598 | -61.0915 | 2025-09-02 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c209f5f7-c853-309f-bdc3-5e3994ccbcc5 | -11.0526 | -45.399 | 2025-09-02 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 36bed2a3-43ed-39d6-bf84-8d7a048b6f79 | -12.938 | -57.0057 | 2025-09-02 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 792b24b2-fc4b-3191-9a8a-1132a04b5810 | -7.4969 | -45.3495 | 2025-09-02 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| a5a27d2f-8553-31fb-b57a-8e481f7e64cd | -12.9387 | -56.9454 | 2025-09-02 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| ddfaa6cf-3dbb-3701-a0e1-f665171841b2 | -6.2674 | -44.5213 | 2025-09-02 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 7a40fbaa-4715-3b24-8215-5bf997d55e87 | -3.2306 | -47.1131 | 2025-09-02 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f33f28f0-6a3e-3ec9-86fc-76cc981563f8 | -11.6458 | -57.3548 | 2025-09-02 00:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 698b914e-40a1-3f49-8cb0-aab8501d01b2 | -6.7723 | -52.8176 | 2025-09-02 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 91027914-d36a-35f3-bd43-3d9afb3f074e | -6.7911 | -52.796 | 2025-09-02 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| cc2c0a37-772c-39c1-8722-62454841fdf5 | -9.1207 | -61.4864 | 2025-09-02 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 58f89c5e-42c3-3abf-912a-f79decea4d1c | -6.403 | -58.1979 | 2025-09-02 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 9262e6ba-5104-3b42-a2b7-38c27bb690d2 | -12.9385 | -56.9655 | 2025-09-02 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 6a37ce00-f059-37f3-9d7d-c0de7c81e159 | -10.4502 | -54.7581 | 2025-09-02 00:40:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 09489179-2467-3f21-a0cb-d08215e4b433 | -7.6783 | -61.0908 | 2025-09-02 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 9934f1b4-b411-3f73-9d34-c5d0a108585b | -12.9194 | -56.9672 | 2025-09-02 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 0fc3a40d-d615-3671-b4f9-0f9fc49fdd73 | -10.062 | -48.1197 | 2025-09-02 00:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| f34c08a4-2b6b-34aa-b263-a5a2d4dc890c | -14.2687 | -45.2636 | 2025-09-02 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 3db776ee-2b0c-304e-afbd-ed253411f528 | -10.0617 | -48.1417 | 2025-09-02 00:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 359fcbd5-8fe1-321c-9e04-52304f801fb8 | -15.5666 | -48.3469 | 2025-09-02 00:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ea356be9-7b7a-35a1-8ed2-c388cf8b3ee0 | -7.5291 | -61.3444 | 2025-09-02 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a2587518-30ec-30dc-a2a3-e63e75620ad6 | -7.4966 | -45.3722 | 2025-09-02 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ace64f77-d948-3c60-8c5a-47a486c3b174 | -14.2692 | -45.2403 | 2025-09-02 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 3283c645-8969-3e5e-a839-0c7f15abbdd8 | -8.6673 | -62.8369 | 2025-09-02 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 3bffcff3-3c81-3d94-8905-fc4f4172e7ca | -8.6487 | -62.8376 | 2025-09-02 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c4646e47-ce66-314b-a8b8-6dc968f7ad97 | -11.6647 | -57.3533 | 2025-09-02 00:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c8d3b244-c4d1-37e8-8985-e3e0ff4acb64 | -12.9382 | -56.9856 | 2025-09-02 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 50439590-9b1c-3ea2-8daa-cde537f2e4e8 | -17.7091 | -46.8962 | 2025-09-02 00:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 77157f09-8473-3a6f-b734-5f3c9e949b47 | -7.5292 | -61.3254 | 2025-09-02 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| ca11e93c-8f2b-3708-a1a9-73aaa934a494 | -7.5477 | -61.3247 | 2025-09-02 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 188.3 |
| 8414190f-6e50-3166-a7cd-cac69435b8d9 | -6.4029 | -58.2173 | 2025-09-02 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 50dcddaa-8b0d-36c4-b127-1ffb323c5478 | -5.6081 | -45.0038 | 2025-09-02 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 1cd7f150-885a-3202-92ef-3ecd981c78ea | -10.4502 | -54.7581 | 2025-09-02 00:50:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| dfc6013a-1b1c-3501-9692-3f587aba6a69 | -5.6266 | -45.0252 | 2025-09-02 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 331f14c9-de01-3db4-bd94-ec0338a71e80 | -8.6673 | -62.8369 | 2025-09-02 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 9173ea30-33a0-3241-9485-a003493d181e | -6.2674 | -44.5213 | 2025-09-02 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c3097362-846a-3d10-8602-a2f6657466a7 | -9.8804 | -65.0139 | 2025-09-02 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 6e574521-d038-3301-8988-9a51833ada2c | -17.7091 | -46.8962 | 2025-09-02 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 1a4388d4-49b6-31bf-b0dd-51351c331e74 | -6.8466 | -52.8132 | 2025-09-02 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 8d7ec57c-71a9-3bea-82f5-f166afae3f31 | -6.7909 | -52.8165 | 2025-09-02 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 8c6ab496-d0ff-3b8a-9cff-9d2e9306ca4f | -11.1037 | -44.6315 | 2025-09-02 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| efa65f69-1774-32cb-a623-1407910a267c | -7.5291 | -61.3444 | 2025-09-02 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 0192020b-6dbe-3be4-894c-ed183c2e4d16 | -12.9194 | -56.9672 | 2025-09-02 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 1367e36e-4ec9-39af-95cb-e464cd91c9db | -15.5666 | -48.3469 | 2025-09-02 00:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 0879e610-31d6-320e-8358-57d481cd8f90 | -6.8279 | -52.8348 | 2025-09-02 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |


[Clique aqui para ver as próximas entradas](README7.md)
