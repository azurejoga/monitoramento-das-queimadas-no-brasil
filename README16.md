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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34997243-67b0-3e29-a27c-e64db6fa5655 | -3.1949 | -48.6651 | 2024-11-11 00:51:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d066ca23-c1d9-3baf-80a5-49fe296772d5 | -1.4011 | -54.498901 | 2024-11-11 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8aeb5274-116d-3b2b-b7e8-a167bb4d3b5a | -3.1639 | -53.641998 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 662dd068-b80d-3f15-a0e9-df88822cea91 | -3.5573 | -52.293201 | 2024-11-11 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e9fd53d-1c39-329f-b3c3-c0a93eaf11dc | -2.9165 | -49.509399 | 2024-11-11 00:51:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09143ec3-5385-3233-ac0e-088f600de438 | -17.6957 | -54.0872 | 2024-11-11 00:51:00 | METOP-C | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 440c4d57-24b0-32ae-98d0-c3a89275e788 | -2.9084 | -49.252102 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6f21a77-aea3-3d19-b89d-1501818ecf88 | -1.3864 | -52.361801 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1c82680-1909-3f8e-85a9-497425f17b74 | -3.0821 | -53.282902 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a307656-2902-30b8-88c8-faeeb6b1b332 | -1.4426 | -51.662899 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e48b6c99-fc93-32f3-a29a-651795893035 | -3.0339 | -45.8284 | 2024-11-11 00:51:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e4b5e71-893b-34e6-b774-72228b40ad3a | -3.3404 | -51.660999 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d0d3d34-3596-3c79-80e4-5929f300f55d | -0.8778 | -52.933399 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6143cd6e-184c-327b-ace0-d247bb525b85 | -3.621 | -54.704102 | 2024-11-11 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1e8b40f-9237-3ced-b936-54d98b775ae1 | -2.2664 | -50.669701 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7d54d2c-dece-33a5-8eca-2374c94628d8 | -2.5597 | -53.9758 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09fafe47-06a1-3e48-a338-6067fdccb40a | -3.6913 | -50.629299 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89a8c738-78c3-371a-8edf-ca12fc9fcb95 | -3.2864 | -45.331299 | 2024-11-11 00:51:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b3c6e9a-c5d6-3fcf-bb0e-3eb12a84f4ae | -2.5898 | -54.2435 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91842439-0e81-3867-bc65-0475b2f2159f | -3.2961 | -45.328999 | 2024-11-11 00:51:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5965d1de-65c3-3923-a43e-de7bb3c74677 | -3.2637 | -50.4305 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8e3c1e-e59b-39a9-af15-d7edbed023b2 | -2.4285 | -51.957901 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b256d59-3730-3e9b-91be-447c91936489 | -2.8675 | -49.5205 | 2024-11-11 00:51:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1695e3d5-3383-340a-8f01-d8decfed3309 | -1.2016 | -53.626301 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d39c9cc-5b12-3a04-bfbb-1ea2418c2069 | -3.031 | -45.8162 | 2024-11-11 00:51:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| caec8843-7d94-3b2b-9713-f3e72b39c9e9 | -4.0526 | -49.2034 | 2024-11-11 00:51:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58dfe7b6-f03f-35ec-b284-7a41559e5d4d | -2.8508 | -49.432 | 2024-11-11 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| cdfd245c-0b79-37c1-9855-94e9491ce70f | -3.0323 | -45.8377 | 2024-11-11 01:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 4d80e4f7-e767-3d3f-88d7-853b46cee24c | -3.2603 | -48.7582 | 2024-11-11 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| a2386d85-4883-30b8-a73d-e7a625d19bb6 | -3.0137 | -45.8384 | 2024-11-11 01:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| bc2f657e-a9a8-340a-9b4d-05c0e7fb90af | -3.6218 | -50.5661 | 2024-11-11 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| d109ade3-1336-3d05-b9d6-ed9c8a20f2a1 | -6.1323 | -44.9426 | 2024-11-11 01:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 73a493d5-4302-3569-95c9-a4aa63cba645 | -3.1984 | -50.2657 | 2024-11-11 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 83d20dc7-db40-385d-81db-1cf68c68fd71 | -3.0111 | -50.982 | 2024-11-11 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| cdc8b653-c0bf-3e96-8634-9bd201660764 | -3.0296 | -50.9607 | 2024-11-11 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 9855b41a-4ab0-3eb2-8c27-4b3cb1b0adae | -3.6604 | -50.2081 | 2024-11-11 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 44518b01-ae78-3f17-85d1-1a4497fd494f | -3.0324 | -45.8154 | 2024-11-11 01:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 180.5 |
| 27e9dd58-2611-3ff6-a195-97b244367eb9 | -3.2352 | -50.3065 | 2024-11-11 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 3e5c9235-0c44-391d-9785-93a7841c64d1 | -3.0214 | -53.2404 | 2024-11-11 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 32ef0f2a-2faf-3309-a5c9-5312575e55b8 | -6.1512 | -44.9184 | 2024-11-11 01:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 0a5854d6-eec3-3f04-8a30-331787b7a40d | -3.1983 | -50.2867 | 2024-11-11 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b6345fb4-ef7c-33d2-b623-7fb8158ee37b | -17.5889 | -57.43 | 2024-11-11 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 98379978-23e6-3080-8c8b-a9ff5d111a8b | -3.2348 | -46.2087 | 2024-11-11 01:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| cf8b730b-109d-3bc6-886b-4e701fdbd93c | -4.1286 | -49.088 | 2024-11-11 01:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| fb599232-1efc-3436-94b9-3683b8de0296 | -3.2168 | -50.2861 | 2024-11-11 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 73f659d8-4496-3b9c-8ce9-223d9ea1c036 | -3.5346 | -45.7061 | 2024-11-11 01:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| f4544ba3-9567-3956-97cd-497f31acd09c | -3.2428 | -53.0519 | 2024-11-11 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 6639008b-1229-3219-aa49-0f8b0c92b6ad | -3.5322 | -49.9599 | 2024-11-11 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| db9781f2-d4c5-3d3c-ab54-0ab685c068de | -3.6217 | -50.587 | 2024-11-11 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| e95fdde1-30e1-3b31-8d4d-84130e4a3e79 | -1.2201 | -53.6364 | 2024-11-11 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f9708328-96d2-3097-8d20-dd2b34deffc2 | -2.1891 | -48.36 | 2024-11-11 01:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a7e753bc-cebe-3817-8f72-51770b5ba328 | -4.11 | -49.1102 | 2024-11-11 01:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 2b524179-2e19-3f19-9dd6-056c01723f24 | -3.2427 | -53.0722 | 2024-11-11 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c1220669-c13d-3d12-8fcb-dfeeb332bd1b | -17.2933 | -57.4857 | 2024-11-11 01:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 156.8 |
| 35d9ff4c-9f82-364e-a731-57fbad6c6838 | -2.2504 | -46.5061 | 2024-11-11 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| bde078a5-7aca-3821-880c-305431473a5f | -3.5772 | -52.3072 | 2024-11-11 01:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| cf0628ba-b7bb-3b97-b131-962c1220075a | -2.8508 | -49.4108 | 2024-11-11 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 15d7bdc3-596f-3bc6-b66e-c7bd154e3446 | -3.1423 | -50.4352 | 2024-11-11 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| ec85bcdc-1e06-3b58-ad8f-465a58685194 | -4.0293 | -46.9703 | 2024-11-11 01:00:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| aea799ec-1a54-3050-afb2-1b8d2a9f4b0e | -3.1458 | -54.4659 | 2024-11-11 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 480f0a06-8d84-33a0-8057-7b8328279802 | -2.9978 | -45.256 | 2024-11-11 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| ba51a5fd-a267-36c5-86ca-a6ea69a5efc1 | -2.8323 | -49.4325 | 2024-11-11 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| c351a734-27fd-363f-ac87-afdf981f47a4 | -2.2997 | -48.4648 | 2024-11-11 01:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f3bf1413-5017-30cb-ac8a-d59ce82a0154 | -3.2588 | -53.6994 | 2024-11-11 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 135cb3f3-f364-3f1a-8196-014099a8d67b | -5.9788 | -45.3621 | 2024-11-11 01:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| e6b25954-a47d-3509-b51a-419f6ec07ba5 | -3.7149 | -54.6504 | 2024-11-11 01:00:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b73c4932-209e-3d3c-96da-82d62c88fc6c | -3.0138 | -45.8161 | 2024-11-11 01:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 80ac1d28-2e5e-3d50-8e19-48fe94fbb669 | -6.1325 | -44.9199 | 2024-11-11 01:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 3fd8b24e-f9ad-3cc9-bcf0-d382372b6752 | -4.1101 | -49.0888 | 2024-11-11 01:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ed9879b1-9a4b-38a3-b6f1-a6c99e041efc | -3.5137 | -49.9606 | 2024-11-11 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| c1773c56-cf44-3145-9b54-bcb944cd4994 | -17.2936 | -57.4652 | 2024-11-11 01:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 875d9e82-a08c-31fc-9ee8-eeaa13fc533f | -3.048 | -50.981 | 2024-11-11 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f6143800-08db-31b4-9855-0eacb9244b31 | -15.9985 | -59.3449 | 2024-11-11 01:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 8fac15bc-1847-3a50-a073-bc0b53247ff0 | -3.2244 | -53.0524 | 2024-11-11 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 6e0ebbcc-f9b0-3dab-addc-26a3501b1623 | -1.4057 | -52.3758 | 2024-11-11 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 97c90155-c5e7-3e40-9c64-e06c90bc9e9b | -3.2536 | -50.3059 | 2024-11-11 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c91bb8cd-86ac-3738-8fc1-28cc43d62661 | -3.2243 | -53.0727 | 2024-11-11 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 31aac7b0-121a-3e72-85f5-5b3fd99c0f06 | -15.9982 | -59.3649 | 2024-11-11 01:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 0c4628ac-d6b3-3f27-8b72-9c77c6c5bf40 | -3.6789 | -50.2074 | 2024-11-11 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 4f9acea4-537a-3cc0-9ca3-68633f04551c | -3.2352 | -50.2855 | 2024-11-11 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2305c0e9-7f36-361d-93c6-36f970f0badc | -3.1458 | -54.4859 | 2024-11-11 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| e1b9a4b0-4792-3198-92c0-74b57795fae6 | -2.2075 | -48.3811 | 2024-11-11 01:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 393a1934-d840-3611-b06d-3a37bb472b3a | -3.0295 | -50.9815 | 2024-11-11 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 900f1637-0761-3108-81b4-de85a4fcdeb8 | -3.2603 | -48.7368 | 2024-11-11 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| f417aeee-d289-3372-b9ed-59996cc7fbe9 | -3.0213 | -53.2607 | 2024-11-11 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| a13adff2-39bd-3eb4-81e6-1d1ad030fcff | -2.189 | -48.3815 | 2024-11-11 01:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| c1c737a3-2806-354f-be59-e39baed653f4 | -4.1285 | -49.1094 | 2024-11-11 01:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c0094d73-8cc8-36cd-a94a-630e27b47b41 | -1.5164 | -52.1491 | 2024-11-11 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3ff72183-2e52-382e-8181-b2f9206d5c8e | -2.4598 | -50.412 | 2024-11-11 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| d5071a12-4f2c-3586-b4ae-439a460d2266 | -4.1246 | -43.5833 | 2024-11-11 01:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 162a8bbc-21aa-38df-add2-887cbbe8076a | -2.2504 | -46.5282 | 2024-11-11 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| b34d6890-ff61-34b6-85c8-343e3e8d3d9d | -17.6086 | -57.4276 | 2024-11-11 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.7 |
| c44cf94e-3c24-3808-baab-ba181ad8f825 | -17.313 | -57.4834 | 2024-11-11 01:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 6b832d87-4a31-38bb-9ebe-ffc4d13bebf5 | -3.2772 | -53.6989 | 2024-11-11 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 4693139d-b6dd-38f7-91c4-2f5ec9bdd9d7 | -1.4057 | -52.3553 | 2024-11-11 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| fe2cde2b-cccc-352a-9407-18a5dd96a2c0 | -4.0294 | -46.9484 | 2024-11-11 01:00:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 11cd3f28-23c0-318a-93e5-0d7700ce5078 | -2.76 | -49.37 | 2024-11-11 01:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 218ee8b1-6272-3e6b-899b-c1046275dbb7 | -2.73 | -49.32 | 2024-11-11 01:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e11e149d-cbd5-35b7-bc7f-c9cd558b99d4 | -2.76 | -49.32 | 2024-11-11 01:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7844ebf3-f374-3034-805a-a5c04527bc26 | -3.5346 | -45.7061 | 2024-11-11 01:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |


[Clique aqui para ver as próximas entradas](README17.md)
