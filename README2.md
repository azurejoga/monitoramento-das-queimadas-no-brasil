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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f1c7217-281b-36e2-8257-1d7e9e6da808 | -17.6674 | -57.4411 | 2024-10-23 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| e6abe36b-15c6-31f1-8c17-3b9bc637650c | -17.6868 | -57.4593 | 2024-10-23 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 8f0aa72e-24b5-3495-aa1a-a12dd5fdb8cc | -17.6871 | -57.4387 | 2024-10-23 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 3330a904-22c6-3981-85f2-8545a8a87fab | -17.744 | -57.5756 | 2024-10-23 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.7 |
| 0e2cde71-ccb7-33ad-8bda-580d939881b3 | -18.2439 | -56.063 | 2024-10-23 00:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.1 |
| 65a59e26-0472-3ceb-8e72-dd6ed6bc76cc | -18.2633 | -56.0812 | 2024-10-23 00:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.5 |
| bb9045f4-dc3a-31ff-b52a-86edc392f648 | -18.2637 | -56.0603 | 2024-10-23 00:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 175.5 |
| 07b48d2e-1e22-3f28-8e87-4cba2ea0d302 | -18.2641 | -56.0394 | 2024-10-23 00:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 876cc3d1-bae4-3eb8-8ace-68a7aff2e82b | -18.2832 | -56.0785 | 2024-10-23 00:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 008941a0-e392-33e1-beb9-20f7a9c2a87d | -18.2836 | -56.0576 | 2024-10-23 00:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 95fb5e0d-2b26-3e34-96f9-82488cd99250 | -2.5224 | -54.1193 | 2024-10-23 00:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ec89bb38-1a77-3ba8-815b-c7a0ead20f6c | -2.5225 | -54.0992 | 2024-10-23 00:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 95999c1a-a5c1-352c-9b4e-beaa0db52644 | -2.7589 | -49.3072 | 2024-10-23 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 344de186-8c76-3727-ae99-fdc0c4f53fc0 | -2.7614 | -54.0338 | 2024-10-23 00:25:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f2eeac7b-837f-3f65-9a53-0cf299f01596 | -3.0917 | -54.1666 | 2024-10-23 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 75aff165-849b-3476-8af2-933d48971230 | -3.0918 | -54.1465 | 2024-10-23 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 1b654ee5-4048-3eff-aadc-62fabfbc97d6 | -3.1101 | -54.1661 | 2024-10-23 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 9c02e158-e368-3337-839a-000f1ae63965 | -3.1102 | -54.146 | 2024-10-23 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| ecdb1d22-3f10-337c-9dfd-dd5efcbab789 | -3.2542 | -50.1799 | 2024-10-23 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 62c3756c-93c0-3391-9877-1daaabd6a43c | -3.5307 | -54.7356 | 2024-10-23 00:25:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| e5946a08-09b7-3dd9-9e08-52845b4d818d | -3.5491 | -54.7351 | 2024-10-23 00:25:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 8effc49e-5eee-3a7b-b983-25daeb53e0c4 | -3.685 | -45.4078 | 2024-10-23 00:25:27 | GOES-16 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 64099428-783d-315c-887d-92ea7a2ad055 | -4.1719 | -47.9894 | 2024-10-23 00:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4d73419a-0f14-3ba8-a9d3-d2e4a64824f3 | -4.1905 | -47.9885 | 2024-10-23 00:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 2efb8b1f-4cd7-306a-adcf-d2afcf998952 | -4.6016 | -47.5337 | 2024-10-23 00:25:32 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c7aa7c5d-33e0-37fd-8c99-9a04610c8964 | -4.6588 | -44.61 | 2024-10-23 00:25:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 792a3193-4af2-362c-8da1-760f2f547721 | -4.6775 | -44.6089 | 2024-10-23 00:25:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 4a5961f5-24ec-3820-9640-f8078fb13024 | -4.6776 | -44.5861 | 2024-10-23 00:25:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| d2539c34-2047-3f44-a3f3-6c5afebb0ee3 | -4.7254 | -45.7363 | 2024-10-23 00:25:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 421b024c-9283-3550-bdfd-b1239495ce71 | -4.7375 | -46.6701 | 2024-10-23 00:25:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 091c5169-b292-381f-97bd-669af6da5f17 | -4.7565 | -46.6249 | 2024-10-23 00:25:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 6d92816a-dd3e-3370-ac3f-3b15ac3bdb11 | -5.2305 | -43.1886 | 2024-10-23 00:25:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 01234050-c8e7-3330-81b0-3121f7efbb9d | -5.2307 | -43.1652 | 2024-10-23 00:25:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 3b9cab21-de72-37bc-8c9f-4abf81b70de6 | -5.5671 | -43.2576 | 2024-10-23 00:25:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 809c9bb5-7f81-3641-8a4b-e7a3f16d04b4 | -5.5858 | -43.2562 | 2024-10-23 00:25:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| e42accf9-0675-3783-930f-cdfc404d7c4c | -6.5601 | -35.162 | 2024-10-23 00:25:43 | GOES-16 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 59.4 |
| 863d041f-dc38-3de5-b4fe-3ca2e3f9cf11 | -6.5605 | -35.1346 | 2024-10-23 00:25:43 | GOES-16 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 85.7 |
| 1c48256f-b909-3a37-89ff-886e19dfa071 | -6.6765 | -43.0491 | 2024-10-23 00:25:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 2dfab13a-67ee-3dce-89ef-8131462257e3 | -7.161 | -45.153 | 2024-10-23 00:25:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 9cce46e6-1e08-3355-82ce-b3947701be42 | -7.1613 | -45.1302 | 2024-10-23 00:25:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 079d324b-484e-3782-b825-052ab21f2ee4 | -7.1801 | -45.1285 | 2024-10-23 00:25:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 2d139127-7cdb-3f67-acf7-d9c8c14ac79a | -11.3217 | -54.3564 | 2024-10-23 00:26:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 321ad85f-1056-3863-a25f-77b1cd0fb5a2 | -11.3406 | -54.3547 | 2024-10-23 00:26:11 | GOES-16 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 5e635744-f8e1-3e02-89df-cb54e549e0a9 | -11.6115 | -48.5521 | 2024-10-23 00:26:12 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 708effb3-1531-3c20-acf7-0f99ac916a83 | -11.6118 | -48.5301 | 2024-10-23 00:26:12 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 22cf8c6c-323b-369c-a1e4-5dfdc336123e | -17.7436 | -57.5961 | 2024-10-23 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| ff742611-37b3-3f72-b921-633d07f7d29c | -17.744 | -57.5756 | 2024-10-23 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.3 |
| 0280f9cd-cc32-34ae-8f1b-4696e0012c28 | -17.7634 | -57.5937 | 2024-10-23 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 9eb3a1d6-3c0d-35fa-b813-911ebb4988e5 | -17.7637 | -57.5732 | 2024-10-23 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 1034c89c-d798-3497-bdb4-6743e52a7ca8 | -17.764 | -57.5526 | 2024-10-23 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |
| 6b49062c-7dc2-387e-bbbe-b0be86d95d27 | -17.7838 | -57.5502 | 2024-10-23 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |
| 9043f039-e1ac-32bb-b98f-886f3b4ac548 | -18.2633 | -56.0812 | 2024-10-23 00:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 0b4dd7ca-882b-326b-a138-064e371ad463 | -18.2637 | -56.0603 | 2024-10-23 00:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 1397ef9a-122d-3d68-9165-8f533cb1fe4a | -2.5224 | -54.1193 | 2024-10-23 00:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 3b742fed-da25-351b-90d1-6d9614e74a5a | -2.5225 | -54.0992 | 2024-10-23 00:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| c718406d-2166-35fb-a73f-7c9197465a94 | -2.7589 | -49.3072 | 2024-10-23 00:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 5f384d36-96b6-3a1f-9de2-49c1f422d99a | -2.7614 | -54.0338 | 2024-10-23 00:35:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 142a12d6-b08e-328e-b1d3-f4e348629a5d | -3.0917 | -54.1666 | 2024-10-23 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 9a5152b3-f749-3b48-82c1-bbf137771ff0 | -3.0918 | -54.1465 | 2024-10-23 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 050b8ff2-fcf2-31ee-9fa7-2d66b4938e2a | -3.1101 | -54.1661 | 2024-10-23 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 3dda7213-947e-350f-8b6b-2916eab9d3a2 | -3.1102 | -54.146 | 2024-10-23 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 2360ccaa-32f7-3075-99af-70fa61f5645a | -3.2542 | -50.1799 | 2024-10-23 00:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| cdd29715-a5bf-3da8-9493-d621c45eebd6 | -3.549 | -54.7551 | 2024-10-23 00:35:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 080f368d-1164-35d5-8e6a-9cbdd14679a6 | -3.5491 | -54.7351 | 2024-10-23 00:35:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 02613b2b-2634-3c38-bc86-608343d28861 | -3.5307 | -54.7356 | 2024-10-23 00:35:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| af625146-e1d2-33f5-837e-d091f87e4d0e | -3.685 | -45.4078 | 2024-10-23 00:35:27 | GOES-16 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 85688d3b-76b2-338e-97bf-a80188239bf2 | -4.1719 | -47.9894 | 2024-10-23 00:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 5b25659a-81e0-37d4-8279-7ce627ce19b8 | -4.1905 | -47.9885 | 2024-10-23 00:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 828130bd-1c66-30d7-b182-ca93f6263c33 | -4.6588 | -44.61 | 2024-10-23 00:35:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| c6faa8d3-1b61-37de-993a-9d4dcece901e | -4.6775 | -44.6089 | 2024-10-23 00:35:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| e936861b-100c-3e96-a54b-07a55c1b6133 | -4.6776 | -44.5861 | 2024-10-23 00:35:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 345f2951-7523-3349-99dd-041baec2b9e3 | -4.7254 | -45.7363 | 2024-10-23 00:35:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 94.1 |
| cd68d293-7316-3948-a99e-e4c6d2c76628 | -4.7375 | -46.6701 | 2024-10-23 00:35:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1f8058f9-06f0-3591-83a1-0d5e128a9ec7 | -4.7565 | -46.6249 | 2024-10-23 00:35:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 5e8cd824-f37a-32b0-bca2-ecb0537942d2 | -5.2305 | -43.1886 | 2024-10-23 00:35:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 80b277c1-918f-3390-8dff-28f903e53993 | -5.5671 | -43.2576 | 2024-10-23 00:35:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 8aa10170-4bcd-36ea-bdcd-dc83bf7955d8 | -5.5858 | -43.2562 | 2024-10-23 00:35:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 6e9a963a-032f-3e95-a939-45d381de6732 | -6.6765 | -43.0491 | 2024-10-23 00:35:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 232cd8c6-1209-33b4-a57a-0598392a3a64 | -6.6767 | -43.0255 | 2024-10-23 00:35:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| fa4348ec-5c8c-3f1b-8727-04cda9e2928c | -7.1613 | -45.1302 | 2024-10-23 00:35:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 78d2f87b-fc95-3b04-b727-859a0a63cbb5 | -7.1801 | -45.1285 | 2024-10-23 00:35:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 5278df8d-7456-3ae9-80dd-968cf470ee98 | -11.0262 | -48.2724 | 2024-10-23 00:36:08 | GOES-16 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 15376490-ca7d-3628-ba3c-39c2af5a9cd1 | -11.3217 | -54.3564 | 2024-10-23 00:36:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| c1688892-217e-3373-a503-aac104d059f3 | -11.322 | -54.3359 | 2024-10-23 00:36:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| ac218057-2232-3d0b-83f7-284a0266d89f | -11.3406 | -54.3547 | 2024-10-23 00:36:11 | GOES-16 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| e2286e67-aa08-3835-b3e1-d97b0cc711ab | -11.6118 | -48.5301 | 2024-10-23 00:36:12 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| fd5e508c-8c7a-3e0b-9d78-592a11a93f9b | -17.744 | -57.5756 | 2024-10-23 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| ca0858af-55a1-3eb3-a6e8-64a97adf821d | -17.7637 | -57.5732 | 2024-10-23 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 70ad5794-0d88-3933-89dc-74eda7febc99 | -17.764 | -57.5526 | 2024-10-23 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 75202589-4db1-36a4-b4bd-241f9358207d | -17.7644 | -57.532 | 2024-10-23 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 682bb29b-96b7-3429-87df-490f52dc6b42 | -17.7838 | -57.5502 | 2024-10-23 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 23b703dc-a212-3b35-b3b9-2f66e63c2a16 | -17.7841 | -57.5296 | 2024-10-23 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 2443e551-d0e1-3aeb-a876-b12106119636 | -18.2633 | -56.0812 | 2024-10-23 00:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 3454fdae-e289-3d1c-964e-dbd6c1325a81 | -18.2637 | -56.0603 | 2024-10-23 00:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.8 |
| d9db7880-c6f3-3d22-9afc-f6c7bef04e2c | -18.2836 | -56.0576 | 2024-10-23 00:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.5 |
| 1d51505d-e4a4-3444-9d8a-c29511b929c7 | -19.5681 | -56.6114 | 2024-10-23 00:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 54.9 |
| d40f3ed1-f0f6-3d03-8ec3-b086fff42b6a | -22.62772 | -42.21702 | 2024-10-23 00:41:00 | TERRA_M-M | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| ab2f30f3-0d53-3515-872a-8758ba6c782a | -22.62638 | -42.20747 | 2024-10-23 00:41:00 | TERRA_M-M | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| b4c3c703-c746-3f21-8cb8-35396bc93827 | -21.22978 | -44.18553 | 2024-10-23 00:41:00 | TERRA_M-M | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 0efc2063-75d6-36d3-9e4a-d25077a3f396 | -13.09693 | -43.36503 | 2024-10-23 00:43:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README3.md)
