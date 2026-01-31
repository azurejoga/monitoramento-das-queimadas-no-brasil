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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db7584c9-2089-3663-8171-ddd72dab131d | -8.15203 | -43.19493 | 2026-01-31 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3e608da1-f865-3e70-9269-adce9882ca2f | -8.15297 | -43.18975 | 2026-01-31 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 70d247cb-3915-3e7c-86b7-200b023ef42c | -7.65799 | -35.19753 | 2026-01-31 03:44:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bc6a84dd-4f2e-385d-919f-30de2156a5f6 | -4.5867 | -47.54435 | 2026-01-31 03:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7949af15-7095-3239-a6d0-c4a5b802dbcf | -7.38662 | -35.69064 | 2026-01-31 03:44:00 | NOAA-20 | ITATUBA | PARAÍBA | Brasil | 2507200 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8d281303-ce65-3af1-8ecb-6b674cf49706 | -9.46861 | -40.24282 | 2026-01-31 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c7aeb135-736f-33aa-93bf-de0087544b79 | -7.18591 | -35.23983 | 2026-01-31 03:44:00 | NOAA-20 | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 729b28e0-add5-3669-9180-02ba5e6a07db | -12.08952 | -43.7778 | 2026-01-31 03:46:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bba47f8-8b99-3992-85a3-560d26d235b1 | -12.09031 | -43.7736 | 2026-01-31 03:46:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27e7fe3b-9e21-34f0-8c16-0daaf891b8f3 | -22.022 | -49.50625 | 2026-01-31 03:49:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 16ce1cc5-95ce-39c5-8dd5-231942edeb46 | -23.45483 | -46.39059 | 2026-01-31 03:49:00 | NOAA-20 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6b9f7554-321c-3fa3-a5fe-31cc43a54074 | -1.8058 | -54.4923 | 2026-01-31 03:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 4b13e812-46a5-3806-a6a1-55318b6ed211 | -20.3178 | -57.3644 | 2026-01-31 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 8214fc31-a344-3d79-8f83-255b7a6a1597 | -20.3174 | -57.3854 | 2026-01-31 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.8 |
| 71f43252-536b-3ae3-a629-e6e604b0f37a | -20.3178 | -57.3644 | 2026-01-31 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 1387a2e7-6c81-3866-b517-c8a9c2ea9acb | -20.3178 | -57.3644 | 2026-01-31 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.9 |
| 78770f36-88b3-3799-97ba-6d9b1efc50a9 | -1.8058 | -54.4923 | 2026-01-31 04:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 5c645dd4-12ad-3689-b479-d0bb6dd0992f | -1.41244 | -45.65634 | 2026-01-31 04:31:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e06873bc-3754-3052-ae3b-22c447396a4e | -3.2656 | -42.54779 | 2026-01-31 04:31:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85ccc10f-e016-3778-a057-56cbe8966973 | -1.10268 | -46.61222 | 2026-01-31 04:31:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 604aafdd-ec1c-38a7-a58b-f7ded79f33e9 | -1.41913 | -45.65737 | 2026-01-31 04:31:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6714acb3-8fca-37b7-bedb-e755e49deb81 | -3.26482 | -42.55284 | 2026-01-31 04:31:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11de9564-a464-31b0-b3c4-a2d0713847ee | -1.39912 | -45.67595 | 2026-01-31 04:31:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 24910678-fc88-33a3-bd76-283b09f7e11b | -1.80617 | -54.49358 | 2026-01-31 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f4d02601-9456-3579-8656-8989181f0211 | -3.42505 | -43.16671 | 2026-01-31 04:31:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 509ec56c-79a9-38c2-9be8-115b2acc9e65 | -2.4081 | -44.87239 | 2026-01-31 04:31:00 | NOAA-21 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b1ceb6e-4be2-3e61-b49f-49124489428d | -2.40869 | -44.86861 | 2026-01-31 04:31:00 | NOAA-21 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55e700e3-7a6c-3f10-9793-d2a34beea670 | -1.81252 | -54.48749 | 2026-01-31 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| efdbae58-680b-367e-950f-b58aa241395b | -3.16305 | -49.5512 | 2026-01-31 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 19bb172e-bfa1-3d5a-aff1-b6f4a21a7a59 | -1.67721 | -46.83609 | 2026-01-31 04:31:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ef18527-4cb6-3779-85f7-5f18cb303535 | -1.81654 | -54.48987 | 2026-01-31 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f00b79b-860a-3a07-9681-73babd2b67b2 | -1.4091 | -45.65582 | 2026-01-31 04:31:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15b19947-7858-3ae9-ab1c-84bd830d60f3 | -1.80535 | -54.49876 | 2026-01-31 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3440a892-d1a5-35d1-9e2c-6e2338b964b3 | -3.00311 | -49.56627 | 2026-01-31 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cd58c8e-72c7-3ba5-93bb-20e4b4114af5 | -3.31094 | -43.50744 | 2026-01-31 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33294e59-4275-3e4a-ab69-b45518f101c8 | -2.23689 | -47.75766 | 2026-01-31 04:31:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 296ca65f-8150-368b-846e-d56e92e1ac43 | -1.18962 | -46.6013 | 2026-01-31 04:31:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 040605ed-862c-34d8-aca0-f92627f60a48 | -3.05131 | -48.46483 | 2026-01-31 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebd105b4-8a22-32fb-a929-3c674a07a9a9 | -1.81177 | -54.4891 | 2026-01-31 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa7d8036-02be-38d9-8a0e-2b1f01e632f4 | -2.30223 | -47.9918 | 2026-01-31 04:31:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e35abd6f-308b-306a-a58e-d380bf702f43 | -2.90319 | -49.37601 | 2026-01-31 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59822a04-f820-31cf-9ea3-4375cbc84ea8 | -3.26165 | -42.54716 | 2026-01-31 04:31:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5c4fa5d-720d-3cbe-ad3f-83f578bf7204 | -3.16366 | -49.54741 | 2026-01-31 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 28ef4b86-764b-3550-b6d1-e0859754483a | -1.807 | -54.48836 | 2026-01-31 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 8729ab05-851a-3071-8bc1-94f38d522bb0 | -1.39633 | -45.67191 | 2026-01-31 04:31:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d4016df-038a-3ff4-afbd-dfeacdaa9028 | -1.81642 | -54.49343 | 2026-01-31 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42c9c26d-07bd-3c7c-a8a5-21ff9bf9a935 | -2.41392 | -47.45728 | 2026-01-31 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07ec822b-b981-325a-b833-eb35bba2f47c | -1.51703 | -53.9716 | 2026-01-31 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b7fc9b2-cc0d-309d-b8ac-1bb5393bb2e2 | -1.81166 | -54.49266 | 2026-01-31 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8beea963-da52-39cf-bec3-4d17eae0e047 | -1.8014 | -54.49279 | 2026-01-31 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6d6cd11e-4d6a-3dff-8f34-70e076ab2a99 | -1.10598 | -46.61273 | 2026-01-31 04:31:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 836e9f69-ab4c-3e6b-9402-11a7e763d3f7 | -3.26444 | -42.55 | 2026-01-31 04:31:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fbfd7c09-fd16-3a26-89a2-1f95182ecc51 | -1.80223 | -54.48758 | 2026-01-31 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 0978ee3e-9f35-3d17-8a0f-58b8f626fe9f | -1.96444 | -54.0583 | 2026-01-31 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 986ca70e-6b8e-34eb-8396-f50f7163342f | -3.25771 | -42.54652 | 2026-01-31 04:31:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b16762d-366c-3218-a75e-a5b3641aaab2 | -1.80782 | -54.48318 | 2026-01-31 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 95b40eef-1f52-360e-9d5d-ff8439c8ca94 | -1.76529 | -47.14077 | 2026-01-31 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a053852-e9b6-3d17-b3a1-5b0054cbc148 | -3.05466 | -48.46535 | 2026-01-31 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cb13219-ac97-3c47-ab4e-fe6d571c0150 | -7.83364 | -42.05694 | 2026-01-31 04:33:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e6ddfdeb-e079-3644-9693-c860a49def4e | -7.83424 | -42.0527 | 2026-01-31 04:33:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8cb58c6d-e789-375b-8751-e3f2750b4634 | -9.81511 | -38.10251 | 2026-01-31 04:33:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c75ea9f3-076e-372f-b0f5-0c7a40650d84 | -9.81588 | -38.10416 | 2026-01-31 04:33:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| aaca60cf-4512-329a-ae2c-84e6ff34152d | -3.85956 | -54.08139 | 2026-01-31 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 547c9426-83cb-3f1e-b69d-dabb15e13175 | -7.95496 | -40.15148 | 2026-01-31 04:33:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3e2e3f4-6bd7-31b3-8975-c2f89a16e202 | -8.09003 | -48.19871 | 2026-01-31 04:33:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 082c179b-4b17-3d63-b1aa-28d6272d50ce | -5.24937 | -37.50238 | 2026-01-31 04:33:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1d1583d1-5a55-3a04-927f-6e820d85ee91 | -4.96909 | -50.91124 | 2026-01-31 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 957294b7-13f1-3db5-94df-6a02d17718cb | -2.57988 | -54.72538 | 2026-01-31 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fce37a96-ee57-36d1-b602-bb8aef9ad42c | -7.06719 | -48.03547 | 2026-01-31 04:33:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b304511f-89a3-39fc-b86e-2cad22dcc098 | -5.09467 | -37.5517 | 2026-01-31 04:33:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| afb33dda-83fa-3587-b364-ed630b20b6bc | -10.88133 | -44.53672 | 2026-01-31 04:33:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b645f3b-59fc-3270-a0b6-244eeb041eaf | -5.93724 | -44.45875 | 2026-01-31 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7bb6e7b-ad56-3f1c-9a81-bc5c8aec8864 | -11.17274 | -43.56836 | 2026-01-31 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38c70c77-3977-38b9-8476-afd50b8f9271 | -4.58936 | -47.54096 | 2026-01-31 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d6516b17-2785-3952-9b12-7d261a3ef7d8 | -10.88324 | -44.5334 | 2026-01-31 04:33:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f792c242-53c6-37dc-a6b8-a6ed1f530222 | -11.02685 | -44.83942 | 2026-01-31 04:33:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5cf66f7-a256-3854-a211-efc6fca2d326 | -5.97803 | -40.38762 | 2026-01-31 04:33:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 10b94bee-780e-3d82-99b0-9393a2bc46a9 | -7.04517 | -45.06236 | 2026-01-31 04:33:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e86bd12c-918e-3198-928a-00e2ffe72668 | -11.1666 | -44.50819 | 2026-01-31 04:33:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d4e9731-cdf2-30d3-a0ed-0295eb0c0ce4 | -5.98345 | -45.73938 | 2026-01-31 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81c89d7c-7b54-30e8-b449-b85ed5bd2e54 | -3.63026 | -51.94294 | 2026-01-31 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed3b4e6a-3470-3822-9391-a36b9b479473 | -8.15413 | -43.19252 | 2026-01-31 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c36b6335-03ce-3a93-a42e-1f495b341e75 | -7.04122 | -47.61356 | 2026-01-31 04:33:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 76580260-2fcd-3bee-9821-94e0264429a2 | -8.87739 | -47.97108 | 2026-01-31 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 163559f8-081f-3733-bcd2-fe3f078a4d8b | -5.97715 | -40.39043 | 2026-01-31 04:33:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fe874282-c0bd-333d-9101-29f919f74c14 | -8.154 | -43.19241 | 2026-01-31 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d7c27709-eb31-3c9c-bec7-61dcb385db08 | -10.88205 | -44.53177 | 2026-01-31 04:33:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e748807-40f1-3fd2-9827-d25e0b12e044 | -2.9255 | -52.69324 | 2026-01-31 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64b88c36-5fff-3828-a6d4-d419a558b075 | -7.82927 | -42.05633 | 2026-01-31 04:33:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8eae85d5-83fe-3d11-8090-53173151df84 | -5.73029 | -47.92561 | 2026-01-31 04:33:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fbe1e85-eefd-31a6-9516-7dc323f548c4 | -9.81457 | -38.10694 | 2026-01-31 04:33:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 56f3937a-fe84-33ff-9dea-a978ef8d2ca6 | -10.87936 | -44.53284 | 2026-01-31 04:33:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 482c67f8-3248-3d0c-b331-cf7ed12931f7 | -8.87354 | -47.97403 | 2026-01-31 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7e95a44-4624-3bba-a170-2d3f58dc3f67 | -8.14994 | -43.19177 | 2026-01-31 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a7b68c27-f6d7-334a-a6c4-25f7eeee3617 | -7.3828 | -35.68561 | 2026-01-31 04:33:00 | NOAA-21 | ITATUBA | PARAÍBA | Brasil | 2507200 | 25 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 663115f5-51db-3847-b177-5f94f93fc3fc | -7.38207 | -35.69133 | 2026-01-31 04:33:00 | NOAA-21 | ITATUBA | PARAÍBA | Brasil | 2507200 | 25 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3b7f6559-3389-321d-9887-bdb114bb143b | -5.93358 | -44.45822 | 2026-01-31 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45911892-f512-38a0-8080-a2949aaeec11 | -3.63416 | -51.9436 | 2026-01-31 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cb31ff51-7aec-3a1b-930f-894f7cdfeb66 | -2.81708 | -52.9594 | 2026-01-31 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5bd1480-b455-3e72-8f6b-b58e6eb4e912 | -7.10042 | -49.93368 | 2026-01-31 04:33:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
