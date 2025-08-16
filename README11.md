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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16b8aadf-a6a4-394e-97c0-aa3931e1efd9 | -13.1265 | -57.1494 | 2025-08-16 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 72e7d37c-8a11-30ff-90d4-b08fe886cbd0 | -9.0531 | -67.4265 | 2025-08-16 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| c514556e-4ce7-39d0-9031-2c0e9357512f | -11.2599 | -50.4553 | 2025-08-16 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 1b516e45-3519-3bee-9ce3-394e2f572d9c | -9.1894 | -59.6558 | 2025-08-16 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 6d9fc1fb-67bd-3363-80c9-71824c87ad4a | -9.5179 | -60.5461 | 2025-08-16 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 12a61a31-be65-398d-b762-022c6ef7d9f7 | -7.8247 | -61.3327 | 2025-08-16 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8465c834-a2c7-3da3-b5cb-ce0430e52eba | -14.9441 | -54.6959 | 2025-08-16 01:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 9c5035c9-9165-3651-aa23-439ab15efac5 | -14.5828 | -47.905 | 2025-08-16 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 093d2bba-d854-3d4c-a5ba-cc83d834fa9c | -12.5947 | -46.9301 | 2025-08-16 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 395bc5b4-b989-32df-a972-72750537c7bd | -9.518 | -60.5268 | 2025-08-16 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 47cb04f1-540c-33da-b9a0-07f59bc9dea2 | -12.5942 | -46.9527 | 2025-08-16 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 37470d7b-3359-3435-a458-58678ac27043 | -9.2082 | -59.6354 | 2025-08-16 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| bc7d83ba-3d67-3ef0-967b-d32c1e86d930 | -9.0346 | -67.427 | 2025-08-16 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f1b7bae6-e5da-383f-af30-dc70ae317f42 | -6.9487 | -59.5297 | 2025-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| b798be82-d5da-3ad3-b098-50e901f9959b | -4.9118 | -43.257 | 2025-08-16 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 97bba27b-992a-3e00-a2be-3c21d49a2953 | -14.9632 | -54.7143 | 2025-08-16 01:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 8b8aa278-d8a8-3ecf-bd5a-7cfd694f81af | -9.1711 | -59.618 | 2025-08-16 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 3b9651ee-7294-3e56-a9dc-eeaf2acdeca8 | -9.1709 | -59.6374 | 2025-08-16 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 74d83fce-826e-37bc-b29a-6c79978b02ed | -12.5365 | -46.9611 | 2025-08-16 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 7d2a72e3-85cf-34b2-80b0-ab03688daf2f | -11.3466 | -55.4326 | 2025-08-16 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| cac42d89-d1e6-3b9f-8e7f-bb620dbc6ecb | -14.6023 | -47.9018 | 2025-08-16 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| e6f5c30a-cc27-3437-8689-9b7285a8e8e8 | -14.9438 | -54.7166 | 2025-08-16 01:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 033dd765-3c4c-3325-8b36-b91eb5e28304 | -11.2596 | -50.4767 | 2025-08-16 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 60cdfa7c-ed32-3ee4-8aaf-e36ab7c4a119 | -8.9708 | -61.7033 | 2025-08-16 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 656d43db-3567-327e-8c22-84d809d20ba7 | -17.615 | -46.684 | 2025-08-16 01:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 40.5 |
| cdcea8d5-4380-319e-a957-635aaf4bb7a8 | -14.6018 | -47.9243 | 2025-08-16 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| fb1149aa-3d71-34f6-bd69-7afb4f0eb377 | -8.9706 | -61.7224 | 2025-08-16 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 07add8e7-b7c1-37fe-8716-ba4994efd6db | -7.9334 | -61.7281 | 2025-08-16 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 06429919-4d76-31ec-9709-efae915ff364 | -9.1708 | -59.6568 | 2025-08-16 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 4d9b196d-79a1-3540-be07-1701066e7c8b | -8.971 | -61.6651 | 2025-08-16 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 746746ea-773c-394f-b8e4-099a27c2f41b | -3.8209 | -47.7444 | 2025-08-16 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 9c6b8a86-c5cc-3b18-9b72-3e5a37fdc245 | -18.0467 | -47.7253 | 2025-08-16 01:00:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 6b7cf619-1718-3595-914b-bb2a95529a24 | -7.9149 | -61.7288 | 2025-08-16 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 105.6 |
| ecf50917-6901-3f88-a596-cb624bcece47 | -14.9628 | -54.7351 | 2025-08-16 01:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| f3660a78-4868-32ff-aed2-c6f5de1eb8e6 | -7.9148 | -61.7478 | 2025-08-16 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 36ece6ff-13bf-3406-b50a-f405799c2591 | -12.5558 | -46.9583 | 2025-08-16 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 5d1c8aad-e36a-3a1b-8c7c-56755a900f38 | -4.9305 | -43.2558 | 2025-08-16 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 559df3ac-c5f3-35bf-bcc5-4fddc1f3ddb9 | -7.9333 | -61.7471 | 2025-08-16 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 5abf3329-b974-3561-9891-b0ea116f28a6 | -13.4294 | -43.6733 | 2025-08-16 01:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 91a0048d-735a-3476-b0ee-113d45835dff | -9.1523 | -59.6384 | 2025-08-16 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| d7ad443b-0d2f-3d8c-8a41-e4e27e00ddc8 | -13.1074 | -57.1511 | 2025-08-16 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| fcb498b2-936d-3f2a-b6b2-1baf5d35e337 | -12.6135 | -46.9499 | 2025-08-16 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| a9d889cb-a2eb-3391-a7b7-35c480dfc9e3 | -9.4994 | -60.5278 | 2025-08-16 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 635eb96d-0ce7-3c47-9d7d-a2e802c07ab7 | -7.0796 | -59.2351 | 2025-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 476574ad-7a07-33f3-99c9-0bd7dec7ef84 | -6.9486 | -59.549 | 2025-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| da2a1860-1d6c-39e7-aa7e-ed4413367ae6 | -9.4992 | -60.547 | 2025-08-16 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| bd786d76-eac4-3396-8bbc-b1d9a416e6ce | -8.9709 | -61.6842 | 2025-08-16 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 131.9 |
| a1159b1a-f9ed-350f-bd15-95debf164b57 | -13.1077 | -57.131 | 2025-08-16 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 0b7e96e5-5fa5-34e0-8807-b10c76c666d6 | -14.9435 | -54.7374 | 2025-08-16 01:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| b76e2618-c735-328f-83d7-c85222877691 | -13.1267 | -57.1293 | 2025-08-16 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 6fe0138d-d095-3f52-9015-a19f0ead4755 | -8.9893 | -61.7024 | 2025-08-16 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 84b52ab5-bee8-33a7-a5d6-ab754dfcede9 | -2.3763 | -47.6636 | 2025-08-16 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 24b76b56-b2d9-32df-9533-3712132a3510 | -9.518 | -60.5268 | 2025-08-16 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 6d05c060-2c0e-3ad8-8229-a43ef2892d3c | -14.9632 | -54.7143 | 2025-08-16 01:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 590a3341-450f-3354-87bc-0432b536dded | -11.3466 | -55.4326 | 2025-08-16 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 7b266904-74a3-362a-8f1f-e2a658f1d717 | -14.9435 | -54.7374 | 2025-08-16 01:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 6c2f255a-ed1d-3cf6-aae5-908986de9d54 | -9.4994 | -60.5278 | 2025-08-16 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 5d55f848-ba0d-3eed-b871-db176edfed46 | -4.9118 | -43.257 | 2025-08-16 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| b93131cf-d4b7-3bdd-a783-1ca3abecb0d2 | -9.1709 | -59.6374 | 2025-08-16 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 7376c52f-234f-384b-9e5e-947e8a3bab0b | -7.0796 | -59.2351 | 2025-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 59179580-5a94-31fb-b1db-d70490264a9b | -7.5292 | -61.3254 | 2025-08-16 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| e336026c-2228-3e10-b081-62440f774596 | -7.9148 | -61.7478 | 2025-08-16 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 133.0 |
| b7d189ad-7e85-39ea-b579-ae3725026ff3 | -14.6023 | -47.9018 | 2025-08-16 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 911bec75-aab6-3ea1-8dbd-877db2f81357 | -7.9333 | -61.7471 | 2025-08-16 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 42a29af9-d1d9-37e4-8a3c-46417888af81 | -13.1267 | -57.1293 | 2025-08-16 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 7adf176c-346d-3a0e-883e-93b050eb04bd | -14.9635 | -54.6936 | 2025-08-16 01:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 4a2c829c-c7b2-3037-8ada-07ad9304c84b | -3.8209 | -47.7444 | 2025-08-16 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 8fdc3e89-6d80-33d7-af85-a1c979d97431 | -7.9149 | -61.7288 | 2025-08-16 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 0a0a5f9d-e73c-3a88-bb40-4483028c142d | -14.5828 | -47.905 | 2025-08-16 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| b191f955-94fa-334b-af76-4ad3ba4cea97 | -14.9441 | -54.6959 | 2025-08-16 01:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| a7694e1d-ec49-3562-b121-4e709c792abb | -6.9303 | -59.5305 | 2025-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 477938dd-65a8-3b3a-9a3c-1d7078c77be1 | -13.1077 | -57.131 | 2025-08-16 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 9c30e7e6-6e9b-36db-84a0-5c926bcc305c | -6.9487 | -59.5297 | 2025-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 2981a7fb-4a43-35d3-b3d9-aae068e27f88 | -16.2326 | -51.1269 | 2025-08-16 01:10:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 5b7c8534-7338-389a-80ec-3033050f5a78 | -9.5179 | -60.5461 | 2025-08-16 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| e78a6db5-aa0a-3797-a2d5-2744f5c61d15 | -6.9486 | -59.549 | 2025-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 4de859f2-65a0-3fde-9adc-222f02c6784e | -4.9305 | -43.2558 | 2025-08-16 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 81ea2e41-5e83-32d7-8bae-59f25e14bf9f | -4.9116 | -43.2803 | 2025-08-16 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ba6f9bdd-e813-324d-b3e8-a081ba46d514 | -9.0346 | -67.427 | 2025-08-16 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| abbc4994-09b7-394a-a533-321dd0161afc | -6.6327 | -60.0033 | 2025-08-16 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 00b00f94-d1fc-366b-9234-2e3bd54ef589 | -14.9628 | -54.7351 | 2025-08-16 01:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 81a07476-416e-3542-8da1-969d4545beab | -9.1708 | -59.6568 | 2025-08-16 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 4a66129a-3f09-3745-b4e5-007f6594841a | -7.0612 | -59.2358 | 2025-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| f475b6e8-4fda-32c6-be44-47d37c4591b6 | -9.1711 | -59.618 | 2025-08-16 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 27607d14-fed8-3ef3-b754-ce00402b1179 | -7.9334 | -61.7281 | 2025-08-16 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 1fdcb92a-3778-37ec-b5fe-f633b8538e9a | -7.8247 | -61.3327 | 2025-08-16 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 709cae9d-24a5-3192-84f6-dd6f1b946786 | -14.9438 | -54.7166 | 2025-08-16 01:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 98412590-d179-367e-9abf-5e324f81b95d | -9.4992 | -60.547 | 2025-08-16 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| ade1479f-3132-3d57-95cf-eccaf29a30d8 | -6.9302 | -59.5497 | 2025-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 5300885b-7e70-3680-8da1-0b1583fef451 | -9.1523 | -59.6384 | 2025-08-16 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 0df9e066-f9bd-352a-98a0-e517933fa8b8 | -14.6018 | -47.9243 | 2025-08-16 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 9274213f-9cf0-3af8-b0e3-ed1a2ca763ec | -13.1265 | -57.1494 | 2025-08-16 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 2590642b-e39b-367f-a8c4-c3292ea29019 | -12.5558 | -46.9583 | 2025-08-16 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 0fdea09f-ca62-3230-a6d4-13469a6fa751 | -7.9148 | -61.7478 | 2025-08-16 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 30c5a3cb-5e57-3f3d-abcd-58e346d44cf7 | -12.6139 | -46.9273 | 2025-08-16 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 55536132-d599-39fe-8e10-05e30a7266e0 | -9.1711 | -59.618 | 2025-08-16 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 48a8f49a-0ec2-3602-8f5e-fb31ec6f4159 | -9.1708 | -59.6568 | 2025-08-16 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| def1ab54-39a2-344f-85f2-293429d837f6 | -14.5828 | -47.905 | 2025-08-16 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 24319557-8fd7-38cf-b037-f3b4a69e2671 | -4.9118 | -43.257 | 2025-08-16 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| b8845089-9fb8-349f-a9f8-f8b0ddcb4c31 | -13.1267 | -57.1293 | 2025-08-16 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |


[Clique aqui para ver as próximas entradas](README12.md)
