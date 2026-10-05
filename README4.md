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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf2d81fb-686b-3e02-af44-c54e8bcbec4f | -4.8462 | -40.3946 | 2026-10-05 00:12:00 | METOP-C | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 496e4e39-72af-3350-9c8c-6cbdd442dcbb | -2.6844 | -49.034199 | 2026-10-05 00:12:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85313b0b-41e3-35cf-9014-7769b5501822 | -7.0865 | -41.7491 | 2026-10-05 00:12:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0ecd5326-d9a3-39a3-ae81-158f7bda09b8 | -2.8783 | -54.070301 | 2026-10-05 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8519d0a9-9ef7-36c0-a6f6-94104c266037 | -6.9129 | -43.670898 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6a7cde79-7c93-351e-98bc-c226b98b92df | -3.9489 | -40.931 | 2026-10-05 00:12:00 | METOP-C | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6bc83976-fcad-368f-a041-369cd274fc8c | -3.08 | -54.18 | 2026-10-05 00:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74307506-156f-3ed4-a424-0a434a927586 | -3.11 | -53.69 | 2026-10-05 00:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3fd25d7-a274-33b5-b6f5-7acf352d478f | -17.89 | -40.06 | 2026-10-05 00:15:00 | MSG-03 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac995aa0-be74-315b-9760-636e36d3f84a | -3.11 | -53.75 | 2026-10-05 00:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f85b25dc-497d-35a3-a55e-483edd918e25 | -3.05 | -54.17 | 2026-10-05 00:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f59a9f74-b624-3556-b943-6a52a97cb8d7 | -3.14 | -53.75 | 2026-10-05 00:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e878e64-0f03-3afa-839a-73be689a27ff | -8.6734 | -54.5683 | 2026-10-05 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 749cb400-7f0e-3e95-b545-9c3424ccf1af | -2.9082 | -54.0907 | 2026-10-05 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 122f9033-9446-391f-b749-156f8066c82b | -6.2529 | -52.847 | 2026-10-05 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| df0a271e-aa92-3520-acb6-8ac49cfec5e4 | 1.7487 | -55.6256 | 2026-10-05 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| df3a3789-7f0e-3025-a73a-1d4c847af664 | 1.7304 | -55.6259 | 2026-10-05 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| ff3f8602-d05e-3ced-a6ff-9bbaa76f0447 | -8.655 | -54.5494 | 2026-10-05 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 03e0dfab-6143-35bd-a346-1ba546d866f0 | 1.8767 | -55.7621 | 2026-10-05 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| ba5a8aae-a182-3c06-b9b5-7502528e0896 | -6.8952 | -43.6833 | 2026-10-05 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| bd136bd2-7c4a-39b2-8c53-ff6fbcb8ea8d | -3.9032 | -49.7137 | 2026-10-05 00:20:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 6ccb23e0-74dc-3c9e-a47a-ffcaa2af6a0c | -5.5893 | -49.7388 | 2026-10-05 00:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| dba862dc-b13e-32a8-a08d-e04f991f5993 | 1.895 | -55.7421 | 2026-10-05 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 098be3d7-8fc4-391a-bde0-28b090625a56 | -3.8448 | -50.3063 | 2026-10-05 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 9e042ca3-afc9-3c32-8aec-089b8d9ecb28 | -6.0075 | -53.5122 | 2026-10-05 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| ba4f426c-ff30-3201-af85-4a837b79a301 | 1.7303 | -55.6456 | 2026-10-05 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 1e3fafad-3db6-3f33-91ba-5b20c2af345e | -5.5891 | -49.76 | 2026-10-05 00:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| e7b59cfa-33c6-3df8-bfda-f682f475e22a | -3.8447 | -50.3273 | 2026-10-05 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 145.7 |
| b977fecf-1031-37e9-b108-6aeccc0c95d0 | -7.4626 | -63.5583 | 2026-10-05 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 53d17c0f-932b-3e82-9b78-389c26e9c3b2 | -5.5707 | -49.7399 | 2026-10-05 00:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| cd7eb99c-0157-3e48-a5fa-0a7b715633c1 | -3.2755 | -54.1819 | 2026-10-05 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 921b9650-6554-3382-b242-76ff1995cdb0 | -7.4441 | -63.5777 | 2026-10-05 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 48ccd624-17e5-37de-84f4-3c9dc130aa17 | 1.8766 | -55.8016 | 2026-10-05 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| cb88ce19-10bb-3c6a-a4dc-a67170c64494 | -2.9449 | -54.13 | 2026-10-05 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 2f8f42ba-c0fd-3200-b5a6-28d91904efbe | -3.5128 | -54.6162 | 2026-10-05 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 965afc74-e457-3def-95bd-9012b43fb17f | -6.2161 | -52.808 | 2026-10-05 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 581b2099-87b9-314a-a2cd-07427a905391 | -6.8955 | -43.6601 | 2026-10-05 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7dcbfd68-886a-38d2-8624-82549365f0e9 | -3.9217 | -49.713 | 2026-10-05 00:20:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 7807461b-5977-3096-ab51-fd1daccda44e | -2.7796 | -54.0937 | 2026-10-05 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 91276925-175b-35d2-9560-c20c02b25b93 | 1.895 | -55.7619 | 2026-10-05 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 7eb90e4c-2b54-3370-bd16-72913ea1a03a | -2.9265 | -54.1305 | 2026-10-05 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| deadc625-73fa-3307-af16-c6a2c1e7b7ae | -8.6548 | -54.5696 | 2026-10-05 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4d757046-0c8e-3353-860d-da92846bd824 | -2.9817 | -54.089 | 2026-10-05 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 0cd1161a-a21a-314a-9f85-e6e32283219b | -6.914 | -43.6816 | 2026-10-05 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 68342847-cc90-321a-9e2e-ee2c520480d7 | -10.2197 | -61.4513 | 2026-10-05 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 43986a1f-b285-337d-9e53-eb135a54c561 | 3.1098 | -60.5943 | 2026-10-05 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| bc46a200-556f-37bd-aca1-e5e47b4462af | -2.9817 | -54.1091 | 2026-10-05 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 9efec997-00d5-3f5c-bdba-e6e5c5109582 | -2.6675 | -49.0331 | 2026-10-05 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 432cd2ff-336f-3163-94d8-1517c0799a43 | -3.2755 | -54.1619 | 2026-10-05 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a10ad101-6d92-3be4-98a2-019fe4f9c3df | -2.6859 | -49.0325 | 2026-10-05 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 9578ec67-95ef-313f-8a67-baf6857ae968 | -3.0364 | -54.2282 | 2026-10-05 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 7e3305bd-64ca-370f-b23b-613b3452dd9b | -7.4442 | -63.5589 | 2026-10-05 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 184.0 |
| 1ab3ef85-d514-362c-8e55-03fcb8e2b171 | -2.9448 | -54.1501 | 2026-10-05 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 71124c53-1d96-39af-a5bb-84c30002f283 | -6.1974 | -52.8295 | 2026-10-05 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| e4d8749c-060d-3440-b3ef-96e571a8bcd3 | -8.3526 | -62.8302 | 2026-10-05 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 19b1c530-f666-3956-a6ac-7f00cca462a1 | -3.9033 | -49.6925 | 2026-10-05 00:20:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 5f3d46ec-f145-3082-b432-b58922a8ec16 | -2.7044 | -49.032 | 2026-10-05 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 3969ef8d-1f2e-3379-9127-e65a3a99d756 | -7.4257 | -63.5595 | 2026-10-05 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 2abeec41-8871-32f2-8be7-93b377832c32 | -6.1781 | -52.9328 | 2026-10-05 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 8bcf4b66-1ac3-36c6-8a68-3601a6a1deec | -6.2159 | -52.8285 | 2026-10-05 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| a2bba28e-41f2-3427-8b00-db856a9fd709 | -2.9082 | -54.1108 | 2026-10-05 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| bbc220b1-9b85-367e-adf7-fc17ad7e01b2 | -8.6736 | -54.5481 | 2026-10-05 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 5a25bdca-7508-392d-bad8-2fe7207d46af | -2.9632 | -54.1497 | 2026-10-05 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 7b4a8cc0-8288-32d7-952d-79a63af2bd4c | -3.0548 | -54.2277 | 2026-10-05 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| ac95346c-15dc-3c88-8cf9-6109b8032f9f | 1.8766 | -55.7819 | 2026-10-05 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 1e585d65-f744-3f71-af9b-789a86b13dd7 | -6.2159 | -52.8285 | 2026-10-05 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 4007c1e7-5444-3c7e-a7e0-bd80ececbbcc | -2.7044 | -49.032 | 2026-10-05 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 25283862-bc27-339b-8281-2f37281f9782 | -6.0075 | -53.5122 | 2026-10-05 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| cb2e6929-1592-383a-8473-5195f258b7d4 | 1.8766 | -55.8016 | 2026-10-05 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| cb07e135-f879-3da0-92a5-de0a674c7e61 | 3.1098 | -60.5753 | 2026-10-05 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 485098fd-1cb3-3025-a1bb-d0ee57cb56be | -3.2938 | -54.1814 | 2026-10-05 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 24b8937f-b6e0-31de-8afc-e83f78990034 | -3.9032 | -49.7137 | 2026-10-05 00:30:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 24be810c-0299-35cf-8fe2-4abd297cbe82 | 1.8767 | -55.7621 | 2026-10-05 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6e798175-fe14-3b7c-b341-196e9eb05254 | -8.655 | -54.5494 | 2026-10-05 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| c34b36ae-0d40-3b00-ade4-463a5d97016a | 1.8766 | -55.7819 | 2026-10-05 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| c401bb77-f679-344c-a063-0f5490b2c979 | -6.914 | -43.6816 | 2026-10-05 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| e937f104-b1f2-372d-9e86-456654bfd2b4 | 1.7487 | -55.6256 | 2026-10-05 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 0c4d181c-2681-3e88-8192-b30f011a147d | -7.4442 | -63.5589 | 2026-10-05 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 820a5bcc-fab3-30f4-8368-eed432f26ac4 | -6.253 | -52.8265 | 2026-10-05 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 133aaee6-1340-34e2-a377-1bf3ed858675 | -3.2755 | -54.1819 | 2026-10-05 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 9217f46f-b081-3c47-9c1a-66f581ead684 | -6.8952 | -43.6833 | 2026-10-05 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| fce6bd9d-bd3f-360f-aa58-92a56182dd16 | -8.6734 | -54.5683 | 2026-10-05 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 94e7f59d-2e57-3f60-8939-44a4c1df4595 | -6.2529 | -52.847 | 2026-10-05 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 8270c802-7c9e-3dc6-add2-ca6237dc9feb | -3.8447 | -50.3273 | 2026-10-05 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 7998d4c5-8701-3939-b2c8-e379361c857b | -2.6859 | -49.0539 | 2026-10-05 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| dd454895-d7c5-3ccd-8aee-f260b447572c | 1.895 | -55.7619 | 2026-10-05 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 47b5b5c3-ae33-376c-a322-a0a5a0d629f2 | -2.6675 | -49.0331 | 2026-10-05 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 93ec34cf-4a73-3547-a191-edfce11b861e | -7.4441 | -63.5777 | 2026-10-05 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 6e5dc0e2-cadf-321a-ae8b-a3d1dc8bfba7 | -2.6859 | -49.0325 | 2026-10-05 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| cbe58aa6-c8fa-3dca-b12a-954a89908583 | 3.1098 | -60.5943 | 2026-10-05 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 09a023a2-2320-3082-9a9a-a76e6f167760 | -0.3952 | -52.0357 | 2026-10-05 00:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 46.6 |
| ae919b2c-b0ce-3a7c-9340-c9fcca7febb6 | -7.4257 | -63.5595 | 2026-10-05 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| b025c486-c17f-38b1-ae3e-ac2a0b87a76c | -5.5893 | -49.7388 | 2026-10-05 00:30:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| a7c5d1cb-e222-3ffa-a837-d346018eb3a9 | 1.7304 | -55.6259 | 2026-10-05 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| d7b96697-4283-3053-841e-4e0d3728136f | -3.5128 | -54.6162 | 2026-10-05 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 0c0202bb-fc30-3836-92ab-045d8d497d19 | -2.7796 | -54.0937 | 2026-10-05 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| f351c3cc-4903-3ad9-af21-032018373427 | -6.2343 | -52.848 | 2026-10-05 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 46c51f9e-1cc3-3356-b639-8d580e557559 | -8.6736 | -54.5481 | 2026-10-05 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| f38765f9-0377-30c8-ae28-5331037b3587 | -3.8448 | -50.3063 | 2026-10-05 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 097a9a17-8868-379f-ae99-df31977a89b6 | -8.3526 | -62.8302 | 2026-10-05 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |


[Clique aqui para ver as próximas entradas](README5.md)
