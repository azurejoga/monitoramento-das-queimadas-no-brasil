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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ea4b08d-e97a-37ed-b489-273e763bef2d | -6.7059 | -45.6441 | 2026-09-28 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| d42e3548-cc76-38d7-a6e1-2d035cb70d18 | -2.9081 | -54.1309 | 2026-09-28 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| e572ed76-25e9-33e2-8234-2dc374b76fe1 | -3.1953 | -51.039 | 2026-09-28 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 50bfe5f1-d2bc-3d36-92d9-9d79d088f7db | -6.6872 | -45.6456 | 2026-09-28 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| b1fa0237-4f7f-3fb5-9b47-74242d91d1d9 | -12.2116 | -50.3881 | 2026-09-28 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 114b0633-4423-3ea1-ba5e-cc54c52cd8f9 | -3.1472 | -54.0648 | 2026-09-28 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 78446b51-5288-367d-b81c-0981362b0fd9 | -2.7766 | -49.4977 | 2026-09-28 00:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e674c13f-ffa8-315f-91f0-3e34623f909b | -2.7582 | -49.4771 | 2026-09-28 00:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 50e66a02-aaf3-3884-b2f2-d41421115cc2 | -11.4425 | -44.9303 | 2026-09-28 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 3d80e28a-56bc-38f6-84f7-b4848862ac42 | -12.155 | -50.352 | 2026-09-28 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 97ed5bad-e757-3dc8-bf7a-3e8ed75e61af | -3.1655 | -54.0844 | 2026-09-28 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 8bbb3841-650e-3b7c-818a-932b26489c2e | -6.7062 | -45.6216 | 2026-09-28 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 6b30519e-25bb-363d-94e1-beca84d87767 | -3.1471 | -54.1049 | 2026-09-28 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c9e239af-2cf1-3952-be98-04e27db750ab | -3.2137 | -51.0384 | 2026-09-28 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 935ee63a-9796-3a8d-8b2d-b0b497c49607 | -2.7767 | -49.4765 | 2026-09-28 00:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 92aaaa8a-7d3b-36c8-b985-75d8dafaa7b5 | -6.7066 | -45.5765 | 2026-09-28 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| d9ccd9c4-3438-3d60-ba6f-f61cdb21e951 | -12.1925 | -50.3904 | 2026-09-28 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a4f07284-2ef5-3f6e-8fbb-c84e248578b5 | -2.7582 | -49.4983 | 2026-09-28 00:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 37f25a04-9208-3408-8c75-110f86eb4ad3 | -12.7417 | -47.2909 | 2026-09-28 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 684f2689-e363-3fe9-acc7-d04d8a980200 | -9.9266 | -60.7171 | 2026-09-28 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 855212db-01f6-3243-b6bb-fa8039048fb3 | -11.3735 | -43.4209 | 2026-09-28 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 376f396c-7913-3f4f-b4f2-e69ee923825f | -12.7413 | -47.3133 | 2026-09-28 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| c6c27266-9a11-3eaf-a907-cd827a9d2ba1 | -2.9082 | -54.1108 | 2026-09-28 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 8c4e0f1a-c176-3fbb-8814-4411e866ef59 | -6.7064 | -45.599 | 2026-09-28 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 5171de26-698a-3393-9519-b1e1d50342fc | -3.1471 | -54.0849 | 2026-09-28 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 259203b3-cda9-3f96-99b0-8d52bb8c3e67 | -2.7791 | -49.4846 | 2026-09-28 00:55:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6814e335-68d9-3e7e-a446-fab252da6eda | -11.107 | -51.346199 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4935f88-27f6-3694-9f50-3ea45f111457 | -13.7206 | -48.8139 | 2026-09-28 00:55:00 | METOP-C | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae399c8f-7964-3985-a9b4-4631bcd6d1b9 | -2.8548 | -54.1306 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d54828ec-d386-3d97-aab7-d4ead879cdf5 | 1.6755 | -55.9589 | 2026-09-28 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00d2fe33-1645-3296-b791-36f2ef91f2e9 | -15.1925 | -48.435902 | 2026-09-28 00:55:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9ce8aefa-7106-3d3c-83e5-8121b42bffd0 | -7.6755 | -54.856701 | 2026-09-28 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6afe833d-2152-3f73-8847-e626ba21b7e6 | -6.7145 | -45.612499 | 2026-09-28 00:55:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63216b4f-ea2d-3584-9769-40e13987796c | -11.6988 | -44.537399 | 2026-09-28 00:55:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a6e838be-ce2a-3ced-b2fa-f4a9eb2f1ed9 | -9.4892 | -46.3643 | 2026-09-28 00:55:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7378627-1316-3d9c-b66f-0fbeaa3b0ea8 | -14.7264 | -45.5807 | 2026-09-28 00:55:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6bd191b9-6c89-36c1-b95d-ea36772242d4 | -23.7528 | -51.922199 | 2026-09-28 00:55:00 | METOP-C | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2e96eda7-0810-3bc1-a584-c7e544a42a2e | -12.7365 | -47.2957 | 2026-09-28 00:55:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5956315-eef8-336c-8c1e-db8667ddfc24 | -2.896 | -54.0853 | 2026-09-28 00:55:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8b35b7d-a39a-3cf7-8b0f-0d8146fbe1d5 | -10.8018 | -60.7337 | 2026-09-28 00:55:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 791abb29-1f1a-339e-92b3-a2bf0011d800 | -11.1022 | -51.325298 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 44bce8d5-d85d-3dfc-979c-84b56b0a2e91 | -7.8197 | -55.134399 | 2026-09-28 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b663527-25b8-3ce3-aa2f-3c140d5786f4 | -12.663 | -47.333599 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e57c03d-a018-3efd-b573-994ad6d3e349 | -6.711 | -45.598099 | 2026-09-28 00:55:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffe0a8fe-196d-34ea-bfdb-9df5e0715018 | -7.8589 | -61.1894 | 2026-09-28 00:55:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 553536f3-18fc-36b8-a083-9facf5b4215f | 4.35 | -60.711899 | 2026-09-28 00:55:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9cbbb2ff-19df-39c2-9e2b-be8497565e45 | -8.8971 | -46.182598 | 2026-09-28 00:55:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 16c452ae-e304-33e2-9618-3d1bbdb530dd | -8.0345 | -54.8988 | 2026-09-28 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9905f45b-d415-39ba-9e4c-205fcf52f323 | -15.1138 | -53.892399 | 2026-09-28 00:55:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 52b93f24-2b69-3cff-b088-de0a64ca9ede | -10.8061 | -48.728699 | 2026-09-28 00:55:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21376ad6-a81d-393b-91ff-248c2d2f26ec | -17.8929 | -45.057499 | 2026-09-28 00:55:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 53024527-0a89-3f39-a093-a1759463767e | -12.1582 | -50.352402 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f9a5aa2-860c-3ca8-a74a-cee85dda02b8 | -15.1005 | -53.8778 | 2026-09-28 00:55:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c931f0aa-cd91-3342-a5ff-4c70b1534994 | -13.3769 | -44.018299 | 2026-09-28 00:55:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 898447a9-aa3b-3fdf-a2b8-78a368852c59 | -1.7718 | -53.770901 | 2026-09-28 00:55:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 174809b2-efb7-3298-b564-8b2dd300d76d | -6.6934 | -45.987701 | 2026-09-28 00:55:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a049609b-7e8e-318e-b942-ef92a6fd4c06 | -11.3697 | -43.415699 | 2026-09-28 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50e5e5b0-e9ad-3fcb-af8d-fc9aa799900c | -2.9007 | -54.1059 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f945429-79bd-327e-ba30-2bfdd00f273a | -10.408 | -53.824902 | 2026-09-28 00:55:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee7417f6-0c8d-3426-9351-05e968d4b6ba | -2.7819 | -57.697601 | 2026-09-28 00:55:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6f8c03c-94c5-36bc-85af-318376d86d42 | 1.7331 | -50.854801 | 2026-09-28 00:55:00 | METOP-C | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7bcd9fea-d1e6-304b-9c6e-35dabf46a39b | -11.4138 | -44.963501 | 2026-09-28 00:55:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d01c8759-90dd-3c92-9ccb-c41e00cc5674 | -6.689 | -45.634102 | 2026-09-28 00:55:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50f73abc-8df0-34ff-ae28-54e4acfade85 | -6.7057 | -45.660301 | 2026-09-28 00:55:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 753993f4-6f7a-3911-a242-84ce175fd34d | -1.7702 | -53.764099 | 2026-09-28 00:55:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4b80e59-8eac-3847-b24f-5f6f583b794d | -1.7686 | -53.757301 | 2026-09-28 00:55:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6349bd0-d508-382e-affa-34b732202766 | -20.631701 | -45.597301 | 2026-09-28 00:55:00 | METOP-C | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6235e95b-c26d-3fe0-ba6f-b5a263b3cab1 | -13.7108 | -48.816299 | 2026-09-28 00:55:00 | METOP-C | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dc7c8c5e-c8f3-3284-9c29-eccba67482d1 | -3.8733 | -51.7901 | 2026-09-28 00:55:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eac001e-fca1-3975-a6c2-bdafe0f18c63 | -13.1072 | -47.4165 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7518d6e-7710-3953-b632-eccf1b372b27 | -2.8667 | -49.638302 | 2026-09-28 00:55:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d12bee8-fc4a-37ef-bd06-be5a10ccefe7 | 4.3527 | -60.700699 | 2026-09-28 00:55:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1e8e161b-e2f9-3826-9ec8-a44b02c64ea6 | -12.1598 | -50.3596 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3073fe63-c57a-3b05-9b98-df04a89ac26e | -11.1901 | -44.773899 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f232377a-099f-3584-b095-3fdc97e90c98 | -3.2269 | -54.314701 | 2026-09-28 00:55:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 649e4209-8ea6-3447-9116-deae36d9445c | 1.6477 | -55.900799 | 2026-09-28 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37ab3bec-dcc0-3aa2-af40-66fafb02db64 | -15.4091 | -47.91 | 2026-09-28 00:55:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be7a67a7-e382-3731-b29f-3c4ccc5761dc | -6.5987 | -47.166199 | 2026-09-28 00:55:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8622412a-c073-378c-be01-d93e60c85192 | -11.191 | -44.818001 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4aec0fe4-3843-3da0-9b2a-5957f4a2b423 | -11.4589 | -44.9375 | 2026-09-28 00:55:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ec73f27-d0f9-3893-a9db-48b62938a812 | -8.6721 | -48.966202 | 2026-09-28 00:55:00 | METOP-C | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01fe09ad-5537-33d6-ad9d-4acce7de8962 | -7.7075 | -54.7696 | 2026-09-28 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5db9b3c4-fd44-34d1-b066-956e7c636697 | -2.9038 | -54.119598 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 799d6ce9-6e0b-3cc2-b176-f2261235b3c2 | -15.1385 | -43.618198 | 2026-09-28 00:55:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 46612fc0-f994-3866-8ce2-44e6970c6338 | 2.3831 | -51.027199 | 2026-09-28 00:55:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 90baacdc-5d5a-31d8-ad0b-fad54cbc7753 | -11.0972 | -51.3484 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e9928c65-d13a-3af3-9710-3ad9b21f4457 | -15.4129 | -47.926201 | 2026-09-28 00:55:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3da2b0f5-ceae-3067-8634-26bed94c349a | -3.2666 | -54.262402 | 2026-09-28 00:55:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 354e37d0-c0df-3704-9606-e94cd717a261 | -21.5264 | -45.098701 | 2026-09-28 00:55:00 | METOP-C | SÃO BENTO ABADE | MINAS GERAIS | Brasil | 3160801 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fe916328-0c73-31d2-b95c-57cdbb107b79 | -18.676201 | -41.4534 | 2026-09-28 00:55:00 | METOP-C | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ce52eb3f-5d83-3537-a0a1-be732ea567a2 | -11.1006 | -51.318298 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 884cd248-3215-3d36-9c05-5e3aacbb79f2 | -10.8822 | -43.688 | 2026-09-28 00:55:00 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e79961d3-7ac6-38ea-b9e7-994384ec6d99 | -13.6912 | -48.821098 | 2026-09-28 00:55:00 | METOP-C | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db56fa56-a0bc-3fbd-8281-913ccb02717c | -13.1029 | -47.398399 | 2026-09-28 00:55:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae86200b-034f-3d3b-a883-34387298c730 | -11.1866 | -44.759998 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee71edae-ee6a-3904-959f-bc58d429e201 | 1.6706 | -55.935501 | 2026-09-28 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d4516ba-6397-3b5d-bfd3-2e8ec50784f6 | -3.4274 | -48.342899 | 2026-09-28 00:55:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 229a134e-a9d4-3473-aeb9-6b123afe8130 | -9.9912 | -50.1362 | 2026-09-28 00:55:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 116427cb-a3de-3b1c-beba-7c79d5a1b460 | -14.7335 | -45.5672 | 2026-09-28 00:55:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 007d10a4-9d9c-39e1-9beb-24ec8e6736ba | -3.2018 | -51.030602 | 2026-09-28 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
