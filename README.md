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
| b8572a6d-07f6-37ad-a799-e87c0a86df45 | -6.7555 | -46.3125 | 2026-06-25 00:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| f7358429-bacb-3408-96f4-6d33955e90f5 | -12.7562 | -44.4724 | 2026-06-25 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 7ef1fa94-becc-3bb1-8de7-9fa7cbab9c11 | -12.2163 | -55.4764 | 2026-06-25 00:00:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 8ee45fe8-cb93-3afa-b7d2-98b2104c6f31 | -6.9793 | -42.8798 | 2026-06-25 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 5bcab658-e9ef-3993-9cff-89819088fee1 | -12.7373 | -44.4521 | 2026-06-25 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 194.4 |
| b559f062-703c-346b-9b3a-cf595bd77a85 | -17.365 | -42.6035 | 2026-06-25 00:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 18e3b44c-ceb9-3ab7-9f4a-626558230e1c | -6.9791 | -42.9034 | 2026-06-25 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 9c1e8bbd-65e1-3f0e-8fea-198d185371aa | -8.6701 | -47.8682 | 2026-06-25 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| a4098930-15bd-35ea-97ee-9e85d1807d4b | -12.7566 | -44.449 | 2026-06-25 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| a453de19-2352-3401-96bf-2de60d8ceecb | -12.216 | -55.4968 | 2026-06-25 00:00:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 312.0 |
| 26a4facb-2c20-3091-adb2-2f4e90427a14 | -12.2348 | -55.5153 | 2026-06-25 00:00:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| b3f6adfc-337c-327e-bd56-501dc37b96c5 | -12.235 | -55.495 | 2026-06-25 00:00:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 0ff7d1da-f937-3de1-bda7-574ead3235dc | -17.3442 | -42.6333 | 2026-06-25 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 0f25604b-ae93-344c-a9ef-eab9c1a7915a | -7.7498 | -44.6184 | 2026-06-25 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9b46dcac-a4a6-3b0a-9d57-4e70ce9f2518 | -10.1678 | -56.6301 | 2026-06-25 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 17358a6b-d83d-368e-999f-704483d73158 | -8.6889 | -47.8664 | 2026-06-25 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3e4609e6-8dbc-3d81-a35a-f6b12c7a9d3d | -12.2158 | -55.5171 | 2026-06-25 00:00:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 175.2 |
| 91f7e0a5-f083-3771-b95b-6ebbca927fcd | -17.3449 | -42.6084 | 2026-06-25 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 123.9 |
| b6f8aae7-d85c-3768-a22c-8d5f1a0d12eb | -17.3643 | -42.6284 | 2026-06-25 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c794de03-e3fc-3e90-bc78-d75ffc0e9f74 | -12.7369 | -44.4756 | 2026-06-25 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| c6fdb1ae-b67a-301c-96ff-7d5ceca31c55 | -12.235 | -55.495 | 2026-06-25 00:10:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 169.2 |
| 27850b34-c62b-3c2a-9df3-f135460f0502 | -12.216 | -55.4968 | 2026-06-25 00:10:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 198.0 |
| 087d7930-bf87-3693-af4f-9b9baa3609fc | -12.2158 | -55.5171 | 2026-06-25 00:10:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 4a2ea533-1b9f-38cf-aaa7-32247210abe7 | -17.3449 | -42.6084 | 2026-06-25 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 131.6 |
| f55ca9d3-3fa1-318f-a639-96991165d2ee | -6.9793 | -42.8798 | 2026-06-25 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 4447e4a1-5ca2-39ea-9f75-59123d0e3027 | -17.3643 | -42.6284 | 2026-06-25 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 1db0ef06-7cb8-3a69-8824-0b4a22fd2668 | -12.7566 | -44.449 | 2026-06-25 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 8ca2d00b-8adb-3315-b4e9-570e3139d091 | -8.6889 | -47.8664 | 2026-06-25 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 9491e070-50d0-356a-b7fd-af5da9a8f7b1 | -6.9982 | -42.878 | 2026-06-25 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 5d7cf266-61de-381f-93e4-892009db09d0 | -6.9791 | -42.9034 | 2026-06-25 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| c607b576-f926-32d1-9844-cffc74bc4929 | -13.0635 | -53.3546 | 2026-06-25 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 30d50872-a444-3b81-8dd3-4858a6cb9c1c | -12.7373 | -44.4521 | 2026-06-25 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| b46d0b7d-9ba3-38a4-bf05-a79ff1859a2c | -12.2348 | -55.5153 | 2026-06-25 00:10:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 3c2815e2-8218-3f50-b831-f73fb7ca46b2 | -17.3442 | -42.6333 | 2026-06-25 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 4d76ba7e-1a28-35ef-9aec-4f3221f47b87 | -7.7498 | -44.6184 | 2026-06-25 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 6483814c-0bbd-36da-b241-d9714be0b7a2 | -12.7562 | -44.4724 | 2026-06-25 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 5ff8af5d-41c9-3bab-b142-1bb4ac9b040d | -17.365 | -42.6035 | 2026-06-25 00:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 966ecc09-100a-3b1e-b39e-3d4a849767a0 | -11.2412 | -43.3226 | 2026-06-25 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 0f5f3059-1c70-3403-b95a-b294eadc83ec | -12.7369 | -44.4756 | 2026-06-25 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| f0a9de85-4b1a-3bb9-b691-62df4f522c12 | -12.235 | -55.495 | 2026-06-25 00:20:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 16942be0-ee85-3758-8bbc-a7b901c9b5a8 | -7.7498 | -44.6184 | 2026-06-25 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 9facc377-9c5d-32ac-801e-7e822c6c5f8f | -12.7562 | -44.4724 | 2026-06-25 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 2a8ebad8-a353-3e98-bf74-c55d3b43b9bc | -12.7369 | -44.4756 | 2026-06-25 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 22d23e5a-a80c-379a-8e12-76fe3cd1220d | -12.7373 | -44.4521 | 2026-06-25 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 73fabe61-291c-321f-911c-6eff5a9ad90a | -17.3442 | -42.6333 | 2026-06-25 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 8617492f-0a6e-345c-ba4b-184b1f85bc90 | -12.7566 | -44.449 | 2026-06-25 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| d7386a86-043f-3411-9c23-6171160d5438 | -6.9791 | -42.9034 | 2026-06-25 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| a70c8962-8e1a-3f9f-8d25-7f23327bb5c5 | -17.365 | -42.6035 | 2026-06-25 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 1d1d2fd7-dc6d-3dd4-947e-896e80b9a7ea | -12.2158 | -55.5171 | 2026-06-25 00:20:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 6315033d-2319-3543-944b-c86863b1f75d | -12.216 | -55.4968 | 2026-06-25 00:20:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 204.4 |
| 79577bc6-372c-3847-aa87-0d540813e1d1 | -8.6889 | -47.8664 | 2026-06-25 00:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 0ac86077-67ff-372e-b7e1-f2cfdbf42d83 | -6.9793 | -42.8798 | 2026-06-25 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 0a38f0f1-d0b6-34bb-ba0e-d1e1a8edbf1b | -17.3449 | -42.6084 | 2026-06-25 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 1dc0a745-ca45-3cad-848c-d539e20df611 | -17.3643 | -42.6284 | 2026-06-25 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 08000691-ff48-30c3-8d60-c22e1121a786 | -12.2348 | -55.5153 | 2026-06-25 00:20:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 808ae962-3d0d-3e34-a326-3a6f6482f17b | -12.14089 | -48.25928 | 2026-06-25 00:22:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 2e6045ff-715d-3901-809e-a9e6fd6e4957 | -13.06553 | -53.34977 | 2026-06-25 00:22:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 7a30447c-27b2-3943-9125-645da85f8840 | -12.52006 | -54.38966 | 2026-06-25 00:22:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e41e68a9-fb92-3ee7-a6b7-51b1a013d44e | -12.2247 | -55.51826 | 2026-06-25 00:22:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 96edd43d-e003-3aeb-8e3a-806784820a71 | -12.23335 | -55.50461 | 2026-06-25 00:22:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0ca527da-05a3-3eb0-aaa3-6d8133d681a2 | -12.31099 | -46.74771 | 2026-06-25 00:22:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 72beeb91-0b43-3a42-8665-35f99bcb9d31 | -12.07937 | -54.60954 | 2026-06-25 00:22:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1a88d142-5e02-3e43-ab77-834ff2e3bc8d | -13.20528 | -48.3194 | 2026-06-25 00:22:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 261a4336-0888-3806-92ae-b2eadcc25dcb | -12.14276 | -48.2716 | 2026-06-25 00:22:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| bbe01dbb-7d07-3263-92af-964e27ce8a61 | -17.34263 | -42.64146 | 2026-06-25 00:22:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 114.9 |
| be59660d-7c53-348c-b014-82e78b156bc4 | -12.21296 | -55.50741 | 2026-06-25 00:22:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b2417ad5-8c2f-36d5-9bf8-2c70223feca3 | -17.35007 | -42.61789 | 2026-06-25 00:22:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 133.2 |
| e0bf310d-1655-322a-9b18-f38147b05c8c | -13.20571 | -48.32511 | 2026-06-25 00:22:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5250f816-c814-3b2d-a860-eb5ca2eaf4c0 | -12.55571 | -54.59179 | 2026-06-25 00:22:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5aab151e-e2a0-3a71-b94a-711c1c384530 | -17.34053 | -42.64751 | 2026-06-25 00:22:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 41.9 |
| ee7ee4c3-8c2e-3523-ae5c-0aad339265d4 | -17.33769 | -42.61478 | 2026-06-25 00:22:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 1f3f2c9e-b585-31d4-8561-9f0b8b98a9f5 | -12.83743 | -44.371 | 2026-06-25 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 0fec35c0-34db-3a99-b9f4-0250daa50437 | -12.31951 | -46.74082 | 2026-06-25 00:22:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 34de1d82-5007-31f6-b8c1-4375d32a0672 | -12.74706 | -44.46652 | 2026-06-25 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 244.9 |
| d30824f5-96dd-3704-ad95-223220b0183b | -11.88385 | -51.75746 | 2026-06-25 00:22:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1033c40a-97de-3de7-afe2-6bda34503493 | -12.74316 | -44.44312 | 2026-06-25 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| a99bfb16-ddf1-3d7a-9787-42acc795dfda | -12.84339 | -44.36473 | 2026-06-25 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 9a9fbb99-ae7b-3307-9795-7ace838c3cee | -12.67557 | -54.58026 | 2026-06-25 00:22:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ae57feab-f578-326a-a235-713f30b110df | -13.07594 | -53.35815 | 2026-06-25 00:22:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 270c2c65-cd13-3430-a093-1956623d427d | -12.22315 | -55.50599 | 2026-06-25 00:22:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 277.7 |
| 40d4da19-29da-3092-ab1e-6128495c80f7 | -17.33575 | -42.62064 | 2026-06-25 00:22:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 308c7547-e400-398e-b3a5-eed52e05bd2d | -11.62304 | -48.49213 | 2026-06-25 00:22:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b22ccb94-386e-33df-9987-65573c6d405d | -11.89269 | -51.75616 | 2026-06-25 00:22:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 0a16d1dd-15d5-3ed2-87a8-6c48dcde2011 | -13.06681 | -53.35943 | 2026-06-25 00:22:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b8600537-6fe6-33c8-9674-f519b2a90b2c | -12.72952 | -44.44557 | 2026-06-25 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 5d748d61-f9be-3388-ad75-ee043dacba7c | -11.2569 | -43.34325 | 2026-06-25 00:22:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 156f8565-1551-3e59-8974-e5de06cf0896 | -12.75378 | -44.45859 | 2026-06-25 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 5498c7c3-28da-3b10-9aa8-1dd1020f44d1 | -17.352 | -42.61193 | 2026-06-25 00:22:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 45.6 |
| f20fca04-194c-36a4-9817-ef696ebb1583 | -12.22161 | -55.49377 | 2026-06-25 00:22:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 29d7923c-bfc0-3f06-af8c-6808d961107e | -17.3548 | -42.64464 | 2026-06-25 00:22:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 5c568c2d-ecc9-3fd7-843a-d0923ce9273a | -12.55432 | -54.58094 | 2026-06-25 00:22:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| de4ab665-298d-33ae-a10e-44a37da304d5 | -17.35691 | -42.63863 | 2026-06-25 00:22:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 80d654a5-4bf9-303a-9097-b4cbb01dd90d | -11.89144 | -51.74718 | 2026-06-25 00:22:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7c1c78eb-e1b9-38ac-89ed-4fa120189895 | -11.24158 | -43.34576 | 2026-06-25 00:22:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 38.2 |
| b5ff3009-3ff9-3b0f-98ac-8440e233e65b | -12.66591 | -54.5816 | 2026-06-25 00:22:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b94c9599-d1cd-32ab-bbad-a8c61a307a2a | -12.73344 | -44.46896 | 2026-06-25 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 033596be-9676-33c0-8255-de18b89c807f | -12.7523 | -44.469101 | 2026-06-25 00:23:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f975ccc3-6ec7-38b6-8981-d88903b9b89f | -6.9896 | -42.886799 | 2026-06-25 00:23:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fe19c679-b12f-3daf-8bd3-3c9aaee0b404 | -12.8308 | -44.358002 | 2026-06-25 00:23:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76a4e1c7-da3a-3be6-a88e-fbd34f88ed4e | -7.6259 | -50.2024 | 2026-06-25 00:23:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
