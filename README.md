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
| 7982e767-5637-3034-a5d7-14c9208e9b2b | -21.455601 | -56.1469 | 2026-04-20 00:55:00 | METOP-B | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 64994e83-4e7d-38ad-9d7d-a427f7eb6812 | -23.706699 | -51.623199 | 2026-04-20 01:28:00 | METOP-C | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 152efe1f-21fa-34ee-b0ad-f48ec70bf22c | -23.7023 | -51.6314 | 2026-04-20 02:00:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 65.1 |
| f6f87812-efd9-3d4e-aa11-cbb18f1ba685 | -9.94394 | -38.44487 | 2026-04-20 03:13:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aa4c22d2-ef8b-3e5c-8992-8cb7cbcfa914 | -9.79795 | -37.4725 | 2026-04-20 03:13:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9824e382-cbf3-30ef-b44a-d557e8769d2a | -9.80338 | -37.47351 | 2026-04-20 03:13:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8c6c5efa-916e-37ad-9d89-bedc3b4e55d2 | -9.80272 | -37.47701 | 2026-04-20 03:13:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 82f706e2-e923-3756-a491-bb72751025be | -9.94318 | -38.44884 | 2026-04-20 03:13:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 216f23b5-d139-321c-8743-2fce5779204c | -9.79729 | -37.47605 | 2026-04-20 03:13:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 73caa93d-a9b6-3897-a6df-816a62d121a7 | -9.7986 | -37.46906 | 2026-04-20 03:13:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 30fe434e-7805-3bc9-a8ec-a788a014d13e | -17.24959 | -42.66765 | 2026-04-20 03:15:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| dd6be851-7833-37f3-accb-e6ff82b8e8a5 | -17.24427 | -42.66441 | 2026-04-20 03:15:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2bee6f24-1498-326a-9128-f13c641d9494 | -17.24921 | -42.67288 | 2026-04-20 03:15:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cce6c72a-7c99-341f-ba01-49b4f13cd666 | -17.25104 | -42.66135 | 2026-04-20 03:15:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| fbc8831b-3f38-3a2b-81d0-8e40cc5eea80 | -17.25071 | -42.66614 | 2026-04-20 03:15:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| aede9d2b-baab-381e-ad02-093c68f4c369 | -22.48422 | -43.08075 | 2026-04-20 03:17:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| de0896d6-ec94-37f1-a5e2-ffc3e5594461 | -22.49334 | -43.07393 | 2026-04-20 03:17:00 | NOAA-21 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0e2211ec-d763-3b70-bdab-42cadbdb4326 | -19.84167 | -45.01762 | 2026-04-20 03:17:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e658e4b0-02d0-3e06-990e-4a1d2ebfb515 | -22.49175 | -43.07571 | 2026-04-20 03:17:00 | NOAA-21 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0a5339ea-66ae-37e7-b375-623e21987b9b | -22.49291 | -43.07075 | 2026-04-20 03:17:00 | NOAA-21 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eca5cef0-a81c-39cd-8499-8faf709e5502 | -19.84467 | -45.01832 | 2026-04-20 03:17:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 65bfadba-20a4-35ea-842b-2c5051595562 | -22.48619 | -43.07724 | 2026-04-20 03:17:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4954fd2e-c479-315d-8e78-4492c8efb58d | -22.49212 | -43.07902 | 2026-04-20 03:17:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d0663a57-f7ec-3a7e-afbd-b152a8b6177e | -9.80232 | -37.47277 | 2026-04-20 03:45:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 514b5c16-7234-3e6f-9704-5117fbd18d23 | -9.80301 | -37.46866 | 2026-04-20 03:45:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5bc11ca3-40e9-3d68-b86c-92eae9cae922 | -9.94718 | -38.44468 | 2026-04-20 03:45:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0960cfc0-db83-34ea-9430-f3f13b30a394 | -9.80522 | -37.47751 | 2026-04-20 03:45:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b30dcdd5-eced-3df6-9ad9-7b99382febe8 | -9.80163 | -37.4769 | 2026-04-20 03:45:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4dd5c1c8-8670-3dfd-8b18-3ed4741c498e | -9.80591 | -37.47339 | 2026-04-20 03:45:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ea6463e3-0455-372d-abbe-0de47bf6b0af | -9.79874 | -37.47216 | 2026-04-20 03:45:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.0 |
| beb16cf0-eec8-31ea-8b3c-1841f6e4708f | -9.9464 | -38.44922 | 2026-04-20 03:45:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d85482d6-62b6-3c2b-9e21-1ba5e8677c25 | -11.61164 | -37.84391 | 2026-04-20 03:45:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4fa67fe9-a92d-316d-9d2d-7fc3b9b347d8 | -9.66803 | -37.04403 | 2026-04-20 03:45:00 | NPP-375D | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 087068cf-e2f6-3d12-a8fd-6b3843b28eca | -9.79804 | -37.4763 | 2026-04-20 03:45:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d7d4bc5f-9243-3134-b8c4-8d25a1461aaf | -9.79942 | -37.46806 | 2026-04-20 03:45:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 12d0a939-3adc-35dc-b1eb-445abc941e2b | -22.49347 | -43.07747 | 2026-04-20 03:47:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e976ada1-3979-38e2-98fb-3e33280e1907 | -22.48538 | -43.07563 | 2026-04-20 03:47:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d0646f48-373d-32d4-b94a-e81b029c08d0 | -11.95638 | -37.83723 | 2026-04-20 03:47:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 54f9a7af-a0c8-304b-a551-bab25ddddff4 | -17.16658 | -46.83584 | 2026-04-20 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d7d4da33-35ff-36fc-afa7-696a02c499fc | -13.47049 | -44.03339 | 2026-04-20 03:47:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2dbd12a-34ac-346b-8e91-db9f322373d7 | -22.49422 | -43.07359 | 2026-04-20 03:47:00 | NPP-375D | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a85d5886-a16e-38cc-bd97-e6b0e3e8a7f2 | -13.47559 | -44.03436 | 2026-04-20 03:47:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bbf76d9-0792-369c-ae5f-2dd8bb6df4aa | -13.47109 | -44.03035 | 2026-04-20 03:47:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 458c392b-89e0-3616-94f2-591801929b83 | -22.49495 | -43.06978 | 2026-04-20 03:47:00 | NPP-375D | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 168e88c5-4c46-3446-af14-a26d1e2ecf81 | -22.48948 | -43.07626 | 2026-04-20 03:47:00 | NPP-375D | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d3ccb9f0-f458-3ac0-98a9-fa14e0eb9735 | -17.24717 | -42.66725 | 2026-04-20 03:47:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3a672b39-9e7a-393f-83a4-67604d808fdb | -11.96486 | -37.83029 | 2026-04-20 03:47:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cb83cacb-a16b-324a-bf53-6b8ce3fd2de8 | -17.24804 | -42.66267 | 2026-04-20 03:47:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3b043067-d781-34d6-ac4e-765b461d4ab8 | -21.96087 | -46.11139 | 2026-04-20 03:47:00 | NPP-375D | IPUIÚNA | MINAS GERAIS | Brasil | 3131505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5c49b6ee-d8e1-3ec4-bbc1-d7a9631078e3 | -17.2515 | -42.66822 | 2026-04-20 03:47:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 31a34e32-827f-3db6-ab14-572f467072a6 | -13.63289 | -44.44349 | 2026-04-20 03:47:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05d92c7b-263b-39c8-af01-26a120fe3cd9 | -17.1674 | -46.83199 | 2026-04-20 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 73183ed1-f205-3fd3-8a2d-19f6e22f4480 | -13.47619 | -44.03129 | 2026-04-20 03:47:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fb715fb-763f-399f-88e4-75cfde3c9483 | -17.25238 | -42.66359 | 2026-04-20 03:47:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d9819b0e-c7dc-3786-937c-1f628d59be32 | -22.49025 | -43.07225 | 2026-04-20 03:47:00 | NPP-375D | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a9bf761e-812e-33c7-bc18-e0f01c5a3e68 | -25.1775 | -49.40011 | 2026-04-20 03:49:00 | NPP-375D | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| edb74e14-8198-319d-9c1d-8454767d0059 | -19.84283 | -45.02027 | 2026-04-20 03:49:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a925ac0b-d263-3773-a2e6-e81f8cdcabbd | -24.17378 | -51.22679 | 2026-04-20 03:49:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7837714d-5160-3da4-83bd-a63c1db01cb3 | -27.75662 | -49.97492 | 2026-04-20 03:49:00 | NPP-375D | BOCAINA DO SUL | SANTA CATARINA | Brasil | 4202438 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fc7399a0-7486-322d-a769-5f290eeb4bd1 | -24.17241 | -51.23223 | 2026-04-20 03:49:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| fd306e4d-0006-3490-9165-72aef80c9756 | -19.84397 | -45.01467 | 2026-04-20 03:49:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6037f52a-73dd-3684-b4bc-69363996ec4a | -9.94674 | -38.44186 | 2026-04-20 04:04:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8861d268-1ae8-3a6e-8348-a8c71f76237c | -9.79972 | -37.4775 | 2026-04-20 04:04:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b6524403-9359-37af-b676-cfb14bddf18a | -9.80334 | -37.47805 | 2026-04-20 04:04:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9757a5bf-d39a-3df1-8e44-af3916c8d031 | -9.80398 | -37.47382 | 2026-04-20 04:04:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b252147e-892e-3fc8-9a23-e309de236315 | -9.79673 | -37.47272 | 2026-04-20 04:04:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 16fec99e-1633-3e91-abe4-5af2388c6040 | -9.66583 | -37.04371 | 2026-04-20 04:04:00 | NOAA-20 | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1aee4d56-ce9b-3559-8c98-118596a691b4 | -9.80036 | -37.47327 | 2026-04-20 04:04:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1bff8c8f-6779-3c20-be01-ae830cb2a160 | -9.94615 | -38.44574 | 2026-04-20 04:04:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 727481e6-32c8-33d9-b223-ebe95e6e8ff1 | -9.79738 | -37.46847 | 2026-04-20 04:04:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b277fae4-4536-3d6b-82e8-58837386af28 | -9.801 | -37.46901 | 2026-04-20 04:04:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9f2d3de6-a6d0-3cbf-92ec-f04c69874f62 | -17.16718 | -46.83308 | 2026-04-20 04:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 33ededc6-817e-3df3-9433-a8b84818f2f2 | -13.63369 | -44.44403 | 2026-04-20 04:06:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8627418-96bd-30dc-8335-7c24a70cf233 | -17.25028 | -42.66474 | 2026-04-20 04:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7faf4be9-9e65-35e9-a987-c3d663441aba | -17.24697 | -42.66417 | 2026-04-20 04:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e8496cb8-0c67-3d95-97a0-b708f53f46f0 | -13.47213 | -44.0285 | 2026-04-20 04:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d6e6ba2c-5761-3a4b-8551-542d2bd7562a | -17.16631 | -46.83789 | 2026-04-20 04:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 867f030b-6144-3b6e-b5f1-33656a28be39 | -13.46864 | -44.02792 | 2026-04-20 04:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ee83315-764f-3926-9fee-58f063e5e1e3 | -17.24754 | -42.66057 | 2026-04-20 04:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9f1b8747-1e1c-3683-b1ff-d986a251a971 | -13.47146 | -44.03245 | 2026-04-20 04:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1d45652f-3624-33c0-8ef7-ab5d89398aae | -14.552 | -46.93334 | 2026-04-20 04:06:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29581002-90fb-3b27-86c2-2b5b2b90dba0 | -22.80125 | -43.33664 | 2026-04-20 04:08:00 | NOAA-20 | SÃO JOÃO DE MERITI | RIO DE JANEIRO | Brasil | 3305109 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e95d2c49-30c5-3c64-b415-9a6972279b59 | -22.48587 | -43.07103 | 2026-04-20 04:08:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9663e640-6712-346e-97b8-f023ba832adc | -19.40031 | -53.35753 | 2026-04-20 04:08:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9174a4e7-f404-3ea3-aaa0-8edcbf48fe29 | -19.39475 | -53.35999 | 2026-04-20 04:08:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c54de858-218f-317c-90c1-2c76ae3d1c97 | -19.39397 | -53.36005 | 2026-04-20 04:08:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9413d96b-1583-37e5-ba52-cb42e4cfe441 | -23.64803 | -48.00294 | 2026-04-20 04:08:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e331bd23-1d31-3ad6-a53b-dfa6fc0a8f39 | -21.96055 | -46.10846 | 2026-04-20 04:08:00 | NOAA-20 | IPUIÚNA | MINAS GERAIS | Brasil | 3131505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a1f54d83-e73e-3e86-9e5a-b953db44c223 | -22.48919 | -43.07163 | 2026-04-20 04:08:00 | NOAA-20 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3e9f0401-25a5-3ba0-b836-9f07c9d7f8d9 | -19.39947 | -53.36132 | 2026-04-20 04:08:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c71db73-e8c3-3c17-8305-3f4f2e3cfd9f | -23.86838 | -46.85807 | 2026-04-20 04:08:00 | NOAA-20 | SÃO LOURENÇO DA SERRA | SÃO PAULO | Brasil | 3549953 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 52aa1a90-0e6c-3a02-80ac-a305f9d4efe7 | -19.40026 | -53.36124 | 2026-04-20 04:08:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b96c4f7-24e9-345c-b1ab-ac07a29d2e3d | -22.83027 | -47.14795 | 2026-04-20 04:08:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a91d2eee-f9db-35f0-914c-5599c2275abf | -23.64892 | -47.99817 | 2026-04-20 04:08:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f47c94e2-b6fe-37c2-b529-5069464e8238 | -18.81562 | -49.08915 | 2026-04-20 04:08:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8270f6ad-9e8c-3bb1-90f9-0f21169b0950 | -22.4853 | -43.07473 | 2026-04-20 04:08:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 08ebc8a8-5f86-32fd-8041-b3dee0eabd35 | -24.17467 | -51.23056 | 2026-04-20 04:08:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 80119bb0-36ad-3f1b-8dd3-bb17eee7ee3c | -20.03544 | -49.59635 | 2026-04-20 04:08:00 | NOAA-20 | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c51b4804-2227-371f-bf66-94edb28bb41a | -23.65032 | -48.00208 | 2026-04-20 04:08:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32f1193d-2260-326f-be52-cb4a037014b3 | -22.82866 | -47.14925 | 2026-04-20 04:08:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
