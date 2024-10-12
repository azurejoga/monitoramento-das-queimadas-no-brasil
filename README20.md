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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eee04783-1a9d-3bcd-9399-0a6bc3307a72 | -1.8952 | -54.424801 | 2024-10-12 01:20:50 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70a1a75f-b342-3354-932e-b8184703b700 | -1.6109 | -53.333 | 2024-10-12 01:20:51 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de93852c-55a0-370f-b64d-a0ad75cf7fb1 | -1.613 | -53.342201 | 2024-10-12 01:20:51 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2572dff-4594-3932-a942-ac029e6f040b | -1.6012 | -53.3353 | 2024-10-12 01:20:51 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b3d0d05-6b5a-3f88-97ec-487062b75662 | -1.6033 | -53.344501 | 2024-10-12 01:20:51 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c9f8cec-fd51-3f0d-baad-2558bf97504d | -1.6055 | -53.353699 | 2024-10-12 01:20:51 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00c62aa9-5953-3694-87b5-d5e76dd7b214 | -1.6784 | -55.136299 | 2024-10-12 01:20:56 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4339bff-c76b-3646-a471-c39c0ac6921f | -2.6188 | -59.7313 | 2024-10-12 01:20:58 | METOP-C | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db0807c6-89de-34a1-9e2f-a54f751a8c96 | -3.0477 | -61.670101 | 2024-10-12 01:20:58 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b9b53d8-ae4e-3d0f-a193-529eca08e7c4 | -3.0499 | -61.68 | 2024-10-12 01:20:58 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8a8d959-4439-3eee-bd8e-c54aa4b1a5d6 | -1.2728 | -54.674599 | 2024-10-12 01:21:01 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60210bb5-9172-396f-bd28-6322d048afa9 | -1.2746 | -54.682499 | 2024-10-12 01:21:01 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 979d2c22-745a-3430-974a-c8f2e22ddd05 | -1.5276 | -61.5826 | 2024-10-12 01:21:23 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f34eca6-0433-3f73-b5be-6e306e73ae50 | -1.5178 | -61.584702 | 2024-10-12 01:21:23 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 763acd17-b626-3705-98e0-eb80c39666a0 | -1.4961 | -61.5798 | 2024-10-12 01:21:23 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0634a3ec-d66f-354b-9e6a-3a74c4786f36 | -1.4982 | -61.5891 | 2024-10-12 01:21:23 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1769167-3c02-340d-9fbb-3c67c838ba8c | 0.8253 | -60.570099 | 2024-10-12 01:21:57 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 80f381d4-f9c8-322f-9f85-bf2a622433fb | 2.5715 | -60.687698 | 2024-10-12 01:22:26 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 410a8cac-0457-36b2-954d-ed8d99664a8d | -1.6061 | -53.3492 | 2024-10-12 01:25:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a11d6373-09f0-35ac-9473-37e6ecf9ce79 | -2.8319 | -49.5385 | 2024-10-12 01:25:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 5618f583-0ab3-38e7-9590-57e476409738 | -2.77 | -51.3829 | 2024-10-12 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 73165952-748e-314e-9398-7a3f1767b873 | -2.7701 | -51.3622 | 2024-10-12 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| f4ddd597-a7db-3a46-8c1d-b24b2a4c5309 | -2.7884 | -51.3825 | 2024-10-12 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 9e3ec516-ce8e-35eb-9704-1780abf374ce | -2.7885 | -51.3618 | 2024-10-12 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 2ae79145-d6d1-381c-9596-18c79028054e | -2.7983 | -54.0129 | 2024-10-12 01:25:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 313c42ca-ee84-3a59-abc4-a345b5cfc120 | -2.8611 | -51.6699 | 2024-10-12 01:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| cf1b0718-71ee-317e-95f1-2d1ea140a50b | -3.0311 | -50.5642 | 2024-10-12 01:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 97384fab-5153-3370-88d0-fd0420adcfde | -3.1426 | -50.3724 | 2024-10-12 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d1772274-683d-3a1e-b832-354f6ca14563 | -3.1427 | -50.3514 | 2024-10-12 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| d87bf19a-780e-304b-81e8-ca73d024fe39 | -3.161 | -50.3718 | 2024-10-12 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 5c20d1af-99e7-3697-96a4-25f60b8efc64 | -3.1611 | -50.3508 | 2024-10-12 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 0a9c1771-25b0-3229-9619-9aa2fbbc0831 | -3.2136 | -46.7843 | 2024-10-12 01:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 910ac682-5a10-303d-9cec-89d193fba2f0 | -3.69 | -47.9451 | 2024-10-12 01:25:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 69b1354d-f215-3264-8acf-3cd9184b3cb4 | -3.6901 | -47.9234 | 2024-10-12 01:25:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 0793f7c5-0ecf-3c1b-933c-b338d9d146f4 | -3.6978 | -50.1225 | 2024-10-12 01:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 2104b251-b332-3a40-a238-b0cfa6236e2d | -3.7086 | -47.9444 | 2024-10-12 01:25:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 49a9b330-8add-3ed8-8864-eba571b88355 | -3.7087 | -47.9227 | 2024-10-12 01:25:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| c67a7cee-fa45-363c-b725-b47d84cb0621 | -3.9394 | -46.445 | 2024-10-12 01:25:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| e0498f7f-df2d-3bec-a2a8-53f7e33a6a5c | -3.9396 | -46.4229 | 2024-10-12 01:25:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f5e8e423-e2ba-3a1b-bc31-df4c80180584 | -4.3782 | -50.8087 | 2024-10-12 01:25:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 18c7d0af-badb-3c4f-8112-09faf401c0b1 | -4.7188 | -60.7882 | 2024-10-12 01:25:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 9a0a84cb-2753-3818-999b-d0fa01ac4371 | -4.7371 | -60.7877 | 2024-10-12 01:25:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 929845fa-b9b5-39c0-8f32-9717bc5a4c3a | -4.8116 | -56.1639 | 2024-10-12 01:25:34 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 26f7b970-072a-3b33-96bc-a90180b64b21 | -6.0791 | -44.6276 | 2024-10-12 01:25:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 1218f34c-2108-3f45-b04e-80bd22f0aaa3 | -6.7285 | -59.3267 | 2024-10-12 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f2451441-4890-3f8e-868c-d3bb96b16721 | -6.7469 | -59.3452 | 2024-10-12 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.4 |
| d7e5f768-914e-393e-aa5d-1d71cb455da4 | -6.747 | -59.3259 | 2024-10-12 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 241.9 |
| 95d3f140-1ae7-32ff-a547-26c7f94ca43c | -10.3708 | -61.232 | 2024-10-12 01:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 3a221a22-6822-38c5-a5a5-fa5f7639dc35 | -10.3891 | -61.2887 | 2024-10-12 01:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 5741bc58-44e0-3c7c-9c9d-cb96f15670ad | -10.3892 | -61.2695 | 2024-10-12 01:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| bdc05e25-f9d4-3425-bc48-64914d43c2bd | -10.3895 | -61.231 | 2024-10-12 01:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 5ac6f314-7397-3b1a-8fac-bd8efe432616 | -10.3897 | -61.2118 | 2024-10-12 01:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 29265f8e-6f43-33c2-85eb-be43d90bbc2e | -10.4078 | -61.2877 | 2024-10-12 01:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| ea365b90-63c7-34c7-8db9-a0dc5f3f44cc | -10.4079 | -61.2685 | 2024-10-12 01:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d764131b-dd09-3dca-8807-07d54deb55b0 | -10.9506 | -44.653 | 2024-10-12 01:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 1f9d2402-4d44-37ba-981b-8543cb4e9012 | -10.8568 | -63.8988 | 2024-10-12 01:26:09 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 1c19e7e1-aac3-3a12-870b-85f4b8f1c149 | -11.2761 | -60.5038 | 2024-10-12 01:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 33ba2e32-3cf6-355a-8686-d7e833121d83 | -11.8377 | -58.8445 | 2024-10-12 01:26:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| aed99f08-253b-3759-b922-d0de7a22f0d6 | -12.7871 | -44.8639 | 2024-10-12 01:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 82b4e47c-e4b1-32ba-99bd-80046125b61c | -12.7875 | -44.8406 | 2024-10-12 01:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 083617a9-6b53-3475-85bd-6594384b9c3d | -12.8064 | -44.8608 | 2024-10-12 01:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| b048aa95-387d-3e5e-a6f2-1e10aebfa710 | -16.9805 | -57.4404 | 2024-10-12 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.5 |
| 10cb3733-e063-38b5-a4bf-0500dd1b3051 | -16.9998 | -57.4586 | 2024-10-12 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| e4597de1-d4ec-37e4-b31a-21c136f34681 | -17.1761 | -57.4585 | 2024-10-12 01:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| a270e99c-c9f1-3209-8a6d-19bd9d307ed7 | -17.627 | -56.3318 | 2024-10-12 01:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.2 |
| d99c97c0-7436-309d-b0e7-1eb81a389042 | -17.6467 | -56.3292 | 2024-10-12 01:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 261.7 |
| ab035827-c94a-39fa-808b-0d4e171b0073 | -17.6471 | -56.3084 | 2024-10-12 01:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.5 |
| 0ab829e7-f5ff-3a23-beb1-877931bcb08e | -17.9837 | -57.3819 | 2024-10-12 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 9b418b4f-0180-344a-82be-e912ae8f3313 | -17.9841 | -57.3612 | 2024-10-12 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| c4721d54-b342-3ae5-a1f5-e9d9015a162b | -18.196 | -56.5275 | 2024-10-12 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.8 |
| 7fad5399-0e74-3fd0-830c-59f51b3318a8 | -18.1964 | -56.5066 | 2024-10-12 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.8 |
| 45de97d3-0779-3c4f-9497-61cf1af08334 | -18.2158 | -56.5249 | 2024-10-12 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.3 |
| 1ec3de16-ff82-32f2-8af7-7eef53342768 | -18.2162 | -56.504 | 2024-10-12 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 2dca4062-05f4-3bf1-89cd-88d5b11529ba | -12.59099 | -48.60901 | 2024-10-12 01:34:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| b63d0173-b155-33b6-b03b-b220bd52ec2c | -10.53598 | -49.12381 | 2024-10-12 01:34:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| d059ba44-005b-3178-96a8-ca40cd615b16 | -10.53269 | -49.10221 | 2024-10-12 01:34:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 98eb440d-773e-36d5-926a-17a8e0b69c22 | -10.53117 | -49.09594 | 2024-10-12 01:34:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 8bb49031-7db3-3710-bfda-dd8dc7e59592 | -10.86983 | -49.74255 | 2024-10-12 01:34:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 1696f851-a124-33f5-8338-d4ac16c54b71 | -12.56215 | -53.0769 | 2024-10-12 01:34:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4108323c-6dc7-3ac6-be0d-71aad2d78558 | -17.74063 | -56.24828 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 7431bc4f-3643-368e-80d5-bec7693d7204 | -17.73935 | -56.23903 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| ff485b7c-77cf-37ee-95f1-dbee8c0681e4 | -17.73305 | -56.2589 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| ed7d4627-7ea0-3e58-93e7-d1be1afc5a10 | -17.72342 | -56.26669 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| b4ffc43b-2505-34e8-abe9-df159c823caa | -17.71199 | -56.24955 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| e9305382-4980-36f9-9f7e-fd0cf47e7ac2 | -17.71071 | -56.2403 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.2 |
| da80de8e-ce43-3f46-bfd1-4ca270adaa29 | -17.70943 | -56.23105 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.8 |
| d1308460-f7c8-313d-9570-2cea2d43f517 | -17.70442 | -56.26017 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 5ee5b39c-7d2e-3246-bb6f-e9edc8904866 | -17.70314 | -56.25092 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| c5daf720-6cf8-395c-abb2-c22b7289f37c | -17.70197 | -56.30781 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7e56c1fd-a0ab-300e-b952-deea6de5a251 | -17.70185 | -56.24167 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 924ad8cd-b5b6-3dbe-bbcd-7498ce6bfe6e | -17.6994 | -56.2893 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 9d846d56-cd22-3549-9b48-617e63c934d4 | -17.69556 | -56.26154 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 71b84246-7f0c-332b-aed7-59a8e41dde5b | -17.69428 | -56.25229 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| b77fcadf-2b50-3eaf-8343-2f27df9e8d1d | -17.6867 | -56.26291 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 39a9ae4e-f551-3b4e-b8c8-927d8e4fd3f8 | -17.68542 | -56.25365 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.4 |
| a2804c36-97db-35da-bb0c-d2985a5c87f6 | -17.67794 | -56.33042 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1167016b-2b1b-3fb7-9e05-39d9c12835e0 | -17.67785 | -56.26427 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 53931d03-6ffe-342f-b149-b57df864db00 | -17.67666 | -56.32116 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| a0009802-633e-339e-831d-3f7066412b84 | -17.67657 | -56.25502 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| fec65fd7-a669-3d5c-b357-b93bc74b2ab8 | -17.67528 | -56.24577 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |


[Clique aqui para ver as próximas entradas](README21.md)
