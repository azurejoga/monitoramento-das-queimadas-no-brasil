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
| c5ada4bb-5262-3c9f-861d-1437071f6c75 | -17.565001 | -57.4631 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4b982c00-852a-3537-9aae-b9be314d1fa9 | -10.1303 | -65.0159 | 2024-11-16 01:30:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1de2b216-c278-3868-87c8-162afde5cf4b | -17.629 | -57.554901 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f22cfff3-9e9d-3125-91e2-47de023dac99 | -17.5704 | -57.527199 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5c5b88dc-6e92-3a2b-8467-5d8595cc8b17 | -17.590099 | -57.5653 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 43508b5e-3347-3e0c-8578-5cb759c2d811 | -17.680099 | -57.552101 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| babfcc07-63c9-3579-97ae-9e209d735301 | -17.5779 | -57.557701 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4728e9b7-9cf9-3b22-8536-18c046ce0924 | -9.0793 | -65.849297 | 2024-11-16 01:30:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0021c90-9ffc-3661-b2b8-b3f5caf164ee | -17.574699 | -57.460499 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 347e798a-bdc8-3489-9348-ff73539e8a7b | -17.6096 | -57.560101 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bdabe26c-fe2d-373b-a78c-65e245b6549c | -16.0319 | -59.395 | 2024-11-16 01:30:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d05388e-0543-3f81-be30-14a50b6f30d2 | -17.287701 | -57.514999 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2fcb297-ae37-37f4-a0d9-53c5d325142e | -17.567101 | -57.429501 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db31fc4b-27ed-3d2a-820a-712f88de0fbc | -17.658199 | -57.5471 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7cf3359c-5b56-33ba-b546-37c7df6bec3a | -17.560699 | -57.5298 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d05def18-e3eb-326c-8935-218e31cfafd0 | -16.932699 | -57.631001 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6f21e6ee-bda9-32ee-b07a-4274cae32a62 | -17.5534 | -57.5425 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 46600c80-aff1-30a1-a4d4-effe3d93548b | -19.755501 | -55.394798 | 2024-11-16 01:30:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 55e67820-8122-3f87-ae3c-eaacc8e81ce5 | -17.645399 | -57.452599 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e12a9607-1895-31e4-a00c-a984f363f84a | -17.5823 | -57.491299 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f2f66ecc-5b7c-3e7e-b6f7-7e5be9769e17 | -17.548401 | -57.522099 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e5f11f6e-6410-3124-9aca-1efc08925bce | -17.646 | -57.5396 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 76dd1962-11a2-3cd1-8604-19f3f32da84e | -17.570601 | -57.570499 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b65f381a-a180-33d2-bde1-59bc5044d54b | -17.565701 | -57.550098 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ef9b7f0-b9e5-38d0-86ae-c168c6774c29 | -19.758801 | -55.4076 | 2024-11-16 01:30:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a0a1b585-91e6-3ceb-90ef-9514c15f818e | -17.641199 | -57.5625 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a0c93615-a6f6-3abf-b181-d12d479b11da | -17.584499 | -57.457901 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 82e52c67-3506-3602-a6a1-8735445d2da8 | -17.584801 | -57.501499 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8482deea-28cf-33c9-b8ca-8f3617cf9363 | -17.633699 | -57.532001 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e439b271-dbbe-31b8-805e-eb4f730371bc | -16.935301 | -57.6413 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9ffcbae-363b-3bd4-9088-c4190263b12f | -17.592501 | -57.575401 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 109b67d6-d1fd-34c1-bdd1-a537a946a3b1 | -17.626499 | -57.544701 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| affc106b-c72d-3cb1-b6e4-483a77f8adda | -10.1205 | -65.018097 | 2024-11-16 01:30:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 680416f9-3923-38a1-be45-f1c633c1510d | -17.555901 | -57.5527 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 313f1ab5-2392-3470-bfd3-66a90fd80f92 | -17.575399 | -57.5476 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 66f6a020-4a0c-3e6f-b8d6-ceefa93c6531 | -17.573099 | -57.580601 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 87bf6d63-7e92-3c12-ac08-cfa54a0f688a | -17.5625 | -57.452801 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3d7bbf91-e5db-301d-ac04-25eeec0f0342 | -2.1294 | -53.7099 | 2024-11-16 01:30:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82e1d75f-e94e-33d9-92c0-496ff216a557 | -16.100201 | -60.083199 | 2024-11-16 01:30:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 219b28dc-4940-3829-9148-de3367efebb6 | -17.6217 | -57.567699 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9e4c1f55-b47e-36ea-bdf2-002af72106d5 | -17.5828 | -57.577999 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2dbcde33-16e4-356b-9a0a-d49aa574b436 | -16.949699 | -57.615501 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d3a14f6d-350d-3029-91ec-507ea60ed9db | -17.5459 | -57.511799 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cd611a4b-6b03-3a2f-a600-41a62a27d014 | -22.050501 | -56.007099 | 2024-11-16 01:30:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9a7fc0af-97d6-3710-a335-1adaff501829 | -17.655701 | -57.536999 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 311e9f1f-55fe-3871-bf33-cf7a1ae1e8d4 | -17.5853 | -57.5882 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 087b7bc0-099e-3f0b-90f2-257106933b1d | -2.139 | -53.7076 | 2024-11-16 01:30:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12a1ce41-1106-3fff-a92e-a099cc790a9a | -17.642799 | -57.442299 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 273174df-1292-318e-9345-01258820d6e9 | -17.631399 | -57.565102 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f58eeda-0c0c-3c71-88fb-7671bbbcfb7b | -17.250401 | -57.447601 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 041fe1dc-c8ed-3237-8e35-5fee6a47411d | -3.7393 | -45.6747 | 2024-11-16 01:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 125.2 |
| dfeddab6-3b47-356a-a9cb-5628290a5c47 | -16.958 | -57.6269 | 2024-11-16 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.8 |
| b1fe3cc4-5a42-37a4-a9f4-7ac8d07e963e | -2.1576 | -46.5527 | 2024-11-16 01:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| e83e643e-ffcc-3bde-80e0-28ff52d1c45e | -2.5456 | -46.8944 | 2024-11-16 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 62babbef-9d6d-3e5d-bdf0-0cb6c0e7d968 | -4.9971 | -44.3149 | 2024-11-16 01:40:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 24c78fdf-51f1-32cf-9074-5faa1b8b49ce | -3.7394 | -45.6523 | 2024-11-16 01:40:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 176.5 |
| 025a65d2-7b9c-340e-923e-1f12a7afcb3d | -16.9381 | -57.6495 | 2024-11-16 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 19e474c9-2b3f-3f72-b6b1-7881233a68bc | -2.1562 | -53.7241 | 2024-11-16 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| cb50febf-d0c3-34a2-bd6f-221b318e3e35 | -16.9577 | -57.6473 | 2024-11-16 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.3 |
| fbf3e6d2-a94b-35f8-a155-5998bc218260 | -2.5642 | -46.8938 | 2024-11-16 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c40c6058-7488-373e-b9ee-79e265011111 | -2.1562 | -53.7039 | 2024-11-16 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 11bda306-c1e5-37e7-b341-b96060399257 | -2.1379 | -53.7043 | 2024-11-16 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 1a9669cf-ffc0-3b2a-aa66-7bf765e06529 | -16.9384 | -57.6291 | 2024-11-16 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.6 |
| a299ccea-4cf9-3f06-9efe-b5c4a2c32a31 | -2.1378 | -53.7244 | 2024-11-16 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 972a3778-c4b6-393c-a01d-a3d4042aaa6d | -3.7685 | -50.7908 | 2024-11-16 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8637ad6c-8da4-3cdb-8869-35323d88a5b9 | -3.7208 | -45.6531 | 2024-11-16 01:40:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 194.8 |
| 1b0052ed-18e9-32a9-ab18-2657a15c1ee7 | -17.5882 | -57.4711 | 2024-11-16 01:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| ab78803a-b461-3712-8090-4ae36f17a8e9 | -3.7207 | -45.6755 | 2024-11-16 01:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 700944b1-4bb2-306f-ae25-b2a1d31f6fb6 | -3.7393 | -45.6747 | 2024-11-16 01:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 120.0 |
| c0877780-dae2-3e11-8dfc-54d8f2492338 | -3.2009 | -45.5405 | 2024-11-16 01:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 4babdde1-6960-3fd3-92e1-ec26cd76a8dd | -2.5456 | -46.8944 | 2024-11-16 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 4338d2c5-6ca4-33b8-b132-7ad6f49357c3 | -5.6796 | -35.6418 | 2024-11-16 01:50:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 69.0 |
| a8475c0c-9c74-3b4f-8281-78d7fbdc8412 | -2.5642 | -46.8938 | 2024-11-16 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 0acad7f1-adb3-3558-beef-d42c79f76da4 | -2.1378 | -53.7244 | 2024-11-16 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 966b6720-ac17-3c73-add8-89293166bc7f | -2.1562 | -53.7241 | 2024-11-16 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 0783336c-6261-3199-a36c-10d290505cf2 | -3.7207 | -45.6755 | 2024-11-16 01:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 014802e4-d059-3e6b-89f2-92a83bf71f6e | -3.7208 | -45.6531 | 2024-11-16 01:50:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 4a804aa5-3e1a-3f9a-89de-e31def13fb64 | -3.6255 | -53.9912 | 2024-11-16 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 754d08e5-3ef9-3b0f-ad54-ddc54c62481b | -17.5882 | -57.4711 | 2024-11-16 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 11edc15f-bcc3-3b22-b67c-a8f22e8ecf8b | -17.5685 | -57.4735 | 2024-11-16 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| bad1ccb1-0fa2-3c64-b46a-582daa66ad54 | -3.7685 | -50.7908 | 2024-11-16 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| ea8e0d02-b0cd-3189-b1aa-8ea8f60af5d3 | -2.1379 | -53.7043 | 2024-11-16 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| d01e372a-981b-3d1f-8da5-e064a3bbcd69 | -3.203 | -45.0902 | 2024-11-16 01:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d372c588-e7cc-340f-9bf2-038ae3627730 | -4.9971 | -44.3149 | 2024-11-16 01:50:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| cfe522bf-34cc-37fa-9435-757788414430 | -16.9577 | -57.6473 | 2024-11-16 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.8 |
| 83226972-7259-38e4-a6aa-6049813fff3e | -2.1562 | -53.7039 | 2024-11-16 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| eda4731d-8db1-34e9-a4dc-ffa9a1137911 | -16.9384 | -57.6291 | 2024-11-16 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.3 |
| fff9b8a3-761c-3021-8c6b-0d62392ea93b | -16.958 | -57.6269 | 2024-11-16 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 140.4 |
| 3dbdee63-84ad-3d3c-99c6-d4582dad06cd | -3.7394 | -45.6523 | 2024-11-16 01:50:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 227.6 |
| 65b11837-6cc2-3335-8c56-01e1c7b52643 | -22.05888 | -56.01213 | 2024-11-16 01:58:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ea01a81b-4e15-349d-bc67-c0d60a40d1c2 | -19.77593 | -55.41913 | 2024-11-16 01:58:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 28.4 |
| aed57a29-8550-3d0f-812e-7fad95af685d | -17.5882 | -57.4711 | 2024-11-16 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 479b190f-0d86-3958-b20b-383a97e745c3 | -6.1363 | -42.578 | 2024-11-16 02:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 48.6 |
| f2e80851-fa9c-37ff-83da-894c88715474 | -2.7986 | -48.5586 | 2024-11-16 02:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 7262f929-4d61-3c5a-8bef-980888de2089 | -2.5456 | -46.8944 | 2024-11-16 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 4ef20960-e56f-32e8-91aa-ae791a8634f4 | -2.78 | -48.5806 | 2024-11-16 02:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 7183ab63-ec31-3dcb-a9d7-4cb40f28bd22 | -2.1378 | -53.7244 | 2024-11-16 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| bdec1c24-9f77-39ad-a5de-3dc4755fbeeb | -3.7685 | -50.7908 | 2024-11-16 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| a1d59645-98e2-3fea-8e7f-999039e0ac3a | -16.9384 | -57.6291 | 2024-11-16 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 1d7b8cd5-ff9c-3145-a5eb-81465746acce | -3.7208 | -45.6531 | 2024-11-16 02:00:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |


[Clique aqui para ver as próximas entradas](README12.md)
