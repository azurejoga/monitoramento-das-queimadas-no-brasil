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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 151fc0bf-91f5-3ba3-9f6b-e8a8f2424f41 | -2.2033 | -45.662998 | 2024-12-01 00:38:00 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88d928e2-07a0-3ea5-a923-d9e6bcf19c59 | -4.5012 | -43.933998 | 2024-12-01 00:38:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b664bf3-b3cb-32ac-bb0f-821f80e15568 | -4.1641 | -48.621498 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35b3fc70-e46f-360c-a5f2-42f5dead5865 | -3.321 | -45.634998 | 2024-12-01 00:38:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 75c185e0-8813-3da0-b901-78b5a602061d | 0.9968 | -50.2701 | 2024-12-01 00:38:00 | METOP-C | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 131518e9-2886-3bbe-8281-e4f5a5adf00e | -3.0945 | -53.262199 | 2024-12-01 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f31f35d6-c837-3b89-9c9f-1907de803532 | -4.0491 | -46.818001 | 2024-12-01 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad4a6352-94e0-324e-a596-5d575921cc25 | -1.3846 | -52.5667 | 2024-12-01 00:38:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 030c7d50-0109-34b3-aa5d-2b23f3a79e88 | -4.0326 | -46.925499 | 2024-12-01 00:38:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f17f5cf1-3216-379d-a8f2-e7ccf7c55965 | -2.1467 | -54.881401 | 2024-12-01 00:38:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a7b22ee-7ffb-3013-9a8e-8e3b11fc8d14 | -5.3285 | -45.438099 | 2024-12-01 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b4a0ea7-1f44-324d-bc1d-5be4aced1266 | -4.5598 | -43.309101 | 2024-12-01 00:38:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81eb3d9c-31ae-3415-86eb-c152dd85aabd | -3.7652 | -50.174801 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad5deec-afb8-34ce-9e93-c016fb61ac7f | -4.4422 | -45.354599 | 2024-12-01 00:38:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 389213f9-d2ef-3fd4-9da1-470905db08a9 | -3.669 | -50.250099 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9f67793-7be6-39c9-ba7c-f5e6ce6b1b20 | -1.3144 | -51.672199 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81ae4164-2807-30a3-a43f-69e16df63ee0 | -1.1917 | -51.7668 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2ca68d1-7954-3ce1-8a1b-a2e598e7629e | 0.9413 | -50.736 | 2024-12-01 00:38:00 | METOP-C | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2ef1feb1-89f8-3668-876f-c3c4609fb68f | -4.5453 | -43.291199 | 2024-12-01 00:38:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be131d8a-57ed-386b-a346-2291aab30e67 | -3.8666 | -50.167801 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adc4ea06-51eb-3602-93e2-9d43110a04b2 | -3.9711 | -47.240398 | 2024-12-01 00:38:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3335fcf-f22a-3306-b1db-7739456ecc4f | -2.8256 | -54.073601 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e5c750a-095e-3845-9cb2-45e7acfcdb32 | -1.204 | -51.7304 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea26392f-af8d-3ca9-bdd7-7f507bf9d94d | -4.1013 | -49.069401 | 2024-12-01 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9572151-6a50-33ad-afad-f127b9f42694 | -4.4141 | -48.587299 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8db7c89-a104-3321-83bd-3730db1aeb48 | -2.0246 | -52.078098 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2bac612-fccf-3375-b9b4-498cabdea60c | -3.6869 | -50.2384 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 979f723a-696a-35bd-81d2-475ecb96ea98 | -2.9492 | -49.442299 | 2024-12-01 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35914c6a-39bd-3788-84a6-e767c2d488f3 | -4.2554 | -50.839699 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dd9174d-6d63-31ca-bcd5-10a5d357655f | -3.4549 | -45.678501 | 2024-12-01 00:38:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c6e55229-5e99-3c56-a9de-8fb900553b95 | -2.8282 | -54.085098 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89c6a160-2654-3636-bf60-c6c4f62ba26b | -1.1899 | -51.758801 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 411cbea3-7d45-3c69-a45b-5e3bc0090e0e | -3.8289 | -50.137501 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19a5b917-4023-32a6-aba6-9f468862d123 | -1.6687 | -52.503899 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fde90ed6-a026-3873-acea-30798a873de7 | -3.1344 | -45.986301 | 2024-12-01 00:38:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d94a869-db6d-3cf4-986c-b7ddd1a06430 | -4.4317 | -48.3032 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3934303f-4982-3a76-ac36-9df092241eff | -3.0122 | -49.538101 | 2024-12-01 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86f54f67-e972-323d-a911-c150188de939 | -3.8559 | -47.054001 | 2024-12-01 00:38:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 533326f4-f1f5-3671-8110-9e427a7f839b | -3.0917 | -53.2953 | 2024-12-01 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dfeb969-5ef6-365b-ad37-84922588e68f | -4.6956 | -42.405701 | 2024-12-01 00:38:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 626be25c-61c6-3e78-891b-b0f729772132 | -4.0821 | -50.027699 | 2024-12-01 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67cb9f63-4043-31a8-80ef-42edf36f2c2e | -3.6771 | -50.240601 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0f7c43c-719b-359c-a4e9-87dc7d17fdb7 | -4.4125 | -48.580399 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbe38f6c-b18b-3adc-9a24-40090e357987 | -2.333 | -54.617599 | 2024-12-01 00:38:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff55ff5-51ad-3032-b034-0a5155686b6e | -2.6105 | -45.417599 | 2024-12-01 00:38:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2839231e-e1a0-3b00-93b9-265543063803 | -1.6998 | -52.459702 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82a559fd-2ccd-33c6-ad23-6eab77af5528 | -3.5413 | -51.5056 | 2024-12-01 00:38:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba87d391-51fd-3df3-98cc-893e5a4244e5 | -2.8713 | -54.003502 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07a34f0b-ec25-3d70-82b4-90ead944c215 | -1.3666 | -51.855801 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de04eb66-1008-3f77-bf22-86eb8ab512a0 | -5.5845 | -45.208199 | 2024-12-01 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1467ee4d-41ef-3ee9-a403-d177915aef8f | -4.5574 | -43.299 | 2024-12-01 00:38:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61ff10a6-96ba-3ff9-849e-e7d0992519ca | -3.4531 | -45.6707 | 2024-12-01 00:38:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af0e8e05-777d-3099-915b-275d34f36c69 | -4.1839 | -43.9879 | 2024-12-01 00:38:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3591092a-76c8-3b5c-99ba-0dc8cb6eb3f0 | -2.8039 | -45.9403 | 2024-12-01 00:38:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a8f781ec-a59b-3a1b-ae33-4d92afec035d | -2.9524 | -49.4562 | 2024-12-01 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 385496e9-0e18-37ce-aaa4-619a16b64f3d | -0.9494 | -51.652901 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf9fd9fd-ebda-382e-acd2-d01029032c2e | -3.6289 | -49.846901 | 2024-12-01 00:38:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60b0bdcd-2d1c-35e9-afe7-c16c9bfc4011 | -1.3058 | -51.724701 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e4e776-409f-3e0d-bafa-878aedd33c3d | -3.9058 | -42.419399 | 2024-12-01 00:38:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5d6fff89-7474-373b-a377-a708823f70fd | -2.5518 | -45.609402 | 2024-12-01 00:38:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1729d98-9b94-36a4-aec1-131112b6056d | -1.2409 | -51.621498 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce158a6c-20c8-387e-9e05-251d61358ef8 | -4.533 | -45.700401 | 2024-12-01 00:38:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aedabd09-5f3c-3c9e-8a96-375483e88fa7 | -2.8308 | -54.0966 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c870c9ff-59ee-308b-b826-f2d85622f8f2 | -2.859 | -53.994202 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fccb79d-cac6-3fc1-9b09-3e7b4bd9f3bc | -2.8662 | -53.980801 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5ab494e-e664-3624-b397-4ce13615779f | -1.6521 | -52.250301 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa765166-e79e-3776-a7c4-1336404b7263 | -2.3275 | -54.593102 | 2024-12-01 00:38:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 081f6b96-db8a-313a-ace0-b1a9c2d567f7 | -3.2403 | -53.911098 | 2024-12-01 00:38:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 686f94b7-5c8b-3bcf-8056-b710d83e4676 | -2.9508 | -49.449299 | 2024-12-01 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52b157a9-6ddc-350f-b4bc-e6109c13b712 | -1.2843 | -51.721001 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10d4848a-6ddd-3f3b-92f9-c954b19bf20d | -1.6548 | -53.753201 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58a49c82-5c5f-394e-a9c7-c5191f23775b | -2.2015 | -45.654999 | 2024-12-01 00:38:00 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3dcdc5da-217a-354a-a04f-ce03001bf158 | -4.5477 | -43.3013 | 2024-12-01 00:38:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 343537e6-38d5-37d7-a2bf-6b7ffbaabcb1 | -4.4039 | -49.7659 | 2024-12-01 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82b1e05d-7b05-37ba-82ca-7fbefbcbbcb9 | -4.532 | -45.740601 | 2024-12-01 00:38:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 39f2650f-4097-3c21-b55f-61220efd7256 | -3.8605 | -46.537899 | 2024-12-01 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a1f3926f-0b61-3cd8-abe5-471168a63e8b | -0.2476 | -51.603401 | 2024-12-01 00:38:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| fc58a2ec-7a90-3896-9502-2cc7e204b907 | 0.9495 | -50.7453 | 2024-12-01 00:38:00 | METOP-C | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 98bd00bf-7171-3284-bacc-0c9896c583d2 | -4.2141 | -47.713902 | 2024-12-01 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f0c86ce-1736-37ac-9698-ab0e8dc7ff80 | -4.044 | -46.930302 | 2024-12-01 00:38:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c9ab397-be81-3df4-825a-25d7081bea0c | -4.493 | -48.210701 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5daa6bde-5d13-33e0-9edb-3a89dfa14406 | -3.8713 | -51.007198 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edda0232-91b5-3677-9330-4af05dbb36e7 | -1.9923 | -50.398899 | 2024-12-01 00:38:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 358c68fe-f68d-3252-9fbd-b129243b3426 | 1.1584 | -55.987499 | 2024-12-01 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 899b9b94-f229-36f7-9ee0-6e5382f3853b | -1.2391 | -51.613602 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca54417-f100-3c33-8577-4eaaa166dbdc | -3.3022 | -50.494999 | 2024-12-01 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b860ca89-3c08-34f8-953a-93a8829bc43a | -3.8731 | -50.150902 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 054cb334-bfbe-38fa-a77e-d710417fc164 | -3.0893 | -53.284901 | 2024-12-01 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49a10491-06b8-3a34-b467-05253eba1b7a | -1.3242 | -51.669998 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74b873a7-22eb-3236-b330-c03a3dc61a57 | -4.1128 | -48.532398 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbd27e7a-b154-3f47-8b9b-f9bc8d20ccef | -2.6744 | -46.138302 | 2024-12-01 00:38:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a3ce403-6648-3e68-a535-ca7b39f4b246 | -1.5592 | -53.513699 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45a359f0-a912-3974-bd66-57ae3c3336a3 | -3.0189 | -49.521999 | 2024-12-01 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b2d5143-6355-301d-b956-f7ca62d54834 | -1.4934 | -52.321701 | 2024-12-01 00:38:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fc18988-62ca-3ea3-a7dc-5efd50225fc2 | -1.1997 | -51.756599 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05ab3361-44fe-3c9c-9d4c-0c9a696c69a5 | -2.7428 | -51.751301 | 2024-12-01 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc4b64e8-95ca-3529-9466-9d53272b244e | -2.0373 | -54.669601 | 2024-12-01 00:38:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96ec1b59-6cf9-30ec-b727-3cb89239aaee | -4.0723 | -50.0298 | 2024-12-01 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8f65b6e-17f8-323d-94b9-64179f63baeb | -4.2036 | -48.117901 | 2024-12-01 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1b85b0e-906d-32f3-838b-db76a0ac4af8 | -1.9906 | -50.391701 | 2024-12-01 00:38:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
