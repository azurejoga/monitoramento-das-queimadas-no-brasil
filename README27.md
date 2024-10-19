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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07da638c-cc02-3074-a114-22c094136739 | -5.21214 | -47.1906 | 2024-10-19 04:49:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5936e5bc-f34c-35e8-803b-6f9b798e89fc | -5.01933 | -47.52154 | 2024-10-19 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 880931b3-58de-3124-88ec-936223cd8a6e | -5.44639 | -47.6582 | 2024-10-19 04:49:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baa9de21-e0e4-38dd-9a66-8cd36eeeb5cd | -5.35767 | -47.74496 | 2024-10-19 04:49:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35725229-2294-3624-b947-b03907006b2c | -5.2386 | -46.77236 | 2024-10-19 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46e45095-86e4-3def-a68c-bdfc6bbb33fe | -5.23804 | -46.77604 | 2024-10-19 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84b9e89e-d227-3a82-b9a3-b35194dee67c | -5.01688 | -47.51855 | 2024-10-19 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a393300a-4537-3a43-bb61-a8558e09fdca | -7.68494 | -47.31494 | 2024-10-19 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c719e00c-e9fb-3d42-bcc7-da16648611d0 | -7.6844 | -47.31871 | 2024-10-19 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1237ca08-dc28-3194-ba98-b8d05d1a4fbe | -7.68131 | -47.31059 | 2024-10-19 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8572ac39-5c4e-3285-8717-7318a36a4c71 | -7.67552 | -47.3213 | 2024-10-19 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c69a8e63-1041-35fc-a66d-caf60aad17bc | -7.67135 | -47.32069 | 2024-10-19 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4cdcf32-b701-38a1-9c53-d609ecf63643 | -6.61733 | -47.37646 | 2024-10-19 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7209302-4116-3380-afce-86c8efff0c7d | -7.71629 | -47.58042 | 2024-10-19 04:49:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23ae2fbe-df13-3a70-905e-f4a626ccc57e | -7.68548 | -47.31117 | 2024-10-19 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 293f9682-e3e0-3275-afdd-c1d12f1c7a22 | -7.68077 | -47.31438 | 2024-10-19 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a0821af-e3ab-3812-a021-1a370c9d7052 | -7.68023 | -47.31814 | 2024-10-19 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b78e7acf-6d7e-3a97-ac6f-b5bd388bf8dd | -7.67498 | -47.32506 | 2024-10-19 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8fabc91-ab28-3a71-be05-d1ff223d0359 | -7.67444 | -47.32882 | 2024-10-19 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3440db3c-c41f-3b71-8c78-fc6855f88462 | -7.67081 | -47.32446 | 2024-10-19 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4cd2ac3b-9c20-35bb-8957-47fd55d19eaf | -6.6168 | -47.38008 | 2024-10-19 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88e53bc6-056c-38a1-8c24-463a4ae60821 | -6.61325 | -47.37582 | 2024-10-19 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72b789c2-1c7c-3d8a-b171-96d42e8dc10f | -6.61271 | -47.37945 | 2024-10-19 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04dcb74a-1dc4-3bae-b3c9-f654f97d9521 | -1.97273 | -48.68447 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cb91369-6964-34a5-b4dd-5ffa8c4d364d | -1.97211 | -48.6885 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af55efdc-fe52-3f0b-8e48-36f2b4280b59 | -2.02424 | -47.55123 | 2024-10-19 04:49:00 | NPP-375D | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b1b58996-3f4d-330e-9053-5e4886e5202f | -1.95789 | -47.88563 | 2024-10-19 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0d6aab9-a74c-3acd-913b-16ab5063c232 | -1.95661 | -47.88288 | 2024-10-19 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f996570a-a12c-345d-a71e-a8d3ebd751a3 | -1.95592 | -47.88725 | 2024-10-19 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d646400-59c7-3590-80c8-657131f90d22 | -1.87659 | -47.83446 | 2024-10-19 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b7d8451-8515-34b5-b0e4-8958fc05d77c | -1.87591 | -47.83886 | 2024-10-19 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d8a816c0-41e0-3f75-bc30-92ee048a98ae | -1.8722 | -47.83825 | 2024-10-19 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4ad08ef-270d-3dc5-accc-b4443d13370f | -1.86848 | -47.83767 | 2024-10-19 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 814a6cfb-2c33-3969-99fe-272abe2c4dbb | -1.69182 | -47.75582 | 2024-10-19 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cfe375e-562d-3283-a49a-002e6d160047 | -1.69114 | -47.76023 | 2024-10-19 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee81cce5-57f1-320f-b869-63355188fc09 | -1.37484 | -47.38837 | 2024-10-19 04:49:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d16557ae-54bb-3dd4-b49a-6af80b7c741b | -1.37482 | -47.38577 | 2024-10-19 04:49:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adc314b6-3cb8-39ea-b19b-57f51bd32419 | -1.14385 | -47.30996 | 2024-10-19 04:49:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 724fcf89-4a0c-33ba-81c0-77d68d893bbc | -1.14313 | -47.31459 | 2024-10-19 04:49:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2a5e72ec-2fbf-3d86-98ab-708f186ba669 | -1.14241 | -47.31916 | 2024-10-19 04:49:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cbac24d1-8f1e-3c36-96e2-2192af4a6e0a | -1.14006 | -47.30934 | 2024-10-19 04:49:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cfa5fa1-a824-3c13-a3f9-24a4ea907d36 | -1.13933 | -47.31397 | 2024-10-19 04:49:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e09d3354-7574-3499-b847-188855faa58d | -1.9763 | -48.68502 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b861aa5c-b75f-32c0-8dcc-bf130d8c5a08 | -1.97567 | -48.68904 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 260c2649-4a5a-345e-aa46-23b41248ceab | -1.65836 | -48.52831 | 2024-10-19 04:49:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97e630e1-a9c3-33b1-be79-1540fe8a1192 | -1.43793 | -48.14351 | 2024-10-19 04:49:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28889a21-3051-360c-92ea-e53f57636c97 | -1.43429 | -48.14294 | 2024-10-19 04:49:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bf3ac5b-3404-3d3b-9461-a209980c6454 | -3.48725 | -48.24118 | 2024-10-19 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 352c05e0-5d50-350e-b8b8-552c8c0436b0 | -3.48354 | -48.24055 | 2024-10-19 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3838185-ba01-327f-b120-313bbfd645b4 | -2.65434 | -48.49325 | 2024-10-19 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f92317f1-4a87-32cc-9a81-9669ac51b39f | -2.44692 | -48.48513 | 2024-10-19 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ae747af-1e01-3d0b-acca-a8a2f08bad6f | -2.4433 | -48.48458 | 2024-10-19 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 037213f5-007b-3be1-9909-5c262936a680 | -2.41352 | -48.50968 | 2024-10-19 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c09ed860-44f5-3ce4-860a-ea2a5c1c46fe | -2.32924 | -48.83055 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f776d2f3-e726-3a52-b5fd-2a3fcce12173 | -2.32245 | -48.56888 | 2024-10-19 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a81828d-1638-34d8-a532-c536bcefc11d | -2.31885 | -48.56832 | 2024-10-19 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a660db4-cc26-3a93-9081-8a823c46c6f0 | -2.31459 | -48.80786 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98992505-0e1d-3e79-ab90-a0cf55f38fd7 | -2.26821 | -48.82523 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 981c8aed-3329-3562-ae63-6f2127d0bab6 | -2.16979 | -48.83158 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbc29ca4-8db6-3d58-8960-3fefc6c2c9a6 | -2.16038 | -48.82199 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 355c8127-80dc-3f9e-838d-4716e1d9e4e1 | -2.35438 | -47.6094 | 2024-10-19 04:49:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0080a37-5a07-35d7-9f3e-efd303107125 | -2.35367 | -47.61398 | 2024-10-19 04:49:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1d46d73-9635-3657-9a1d-ac82806699bd | -2.28633 | -47.85342 | 2024-10-19 04:49:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3987717f-e18b-39c7-b229-2a558ac8e639 | -2.28605 | -47.85113 | 2024-10-19 04:49:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 39f23fce-d569-3f24-8fbf-606f1f729288 | -2.25407 | -47.66201 | 2024-10-19 04:49:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 754b79b1-9a98-3889-a242-43137f3a5967 | -2.72126 | -48.83319 | 2024-10-19 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5db39cc1-faf4-32ef-a259-e69e73aec1f8 | -2.72064 | -48.83722 | 2024-10-19 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56e24a1a-c36f-3779-b3db-3d6294642bc4 | -2.71707 | -48.83665 | 2024-10-19 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ba0a4b9-732e-37d8-9b2a-e7827845f4ad | -2.65306 | -48.5016 | 2024-10-19 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e378aaa-5800-3c3e-b3b7-58bf6a19af65 | -2.57625 | -48.39724 | 2024-10-19 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a20136e2-e7a0-3501-9171-51739e7ad400 | -2.57261 | -48.39668 | 2024-10-19 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c51b54b-2128-35f6-9ac4-8a2383c66e3c | -2.41789 | -48.88372 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a8c9bca-382e-321d-8c24-308faa17f2dc | -2.41714 | -48.51023 | 2024-10-19 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3071439-86dd-3288-a9c3-7100b7ba492a | -2.41434 | -48.88317 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb7b9fe0-6ba8-35f6-9e93-00c15d64b5d8 | -2.32861 | -48.83455 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ade1d8d5-1a2b-3c39-b506-d824b987e512 | -2.26466 | -48.82469 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38366477-7128-34ca-a4ba-a85fed0368a4 | -2.26111 | -48.82415 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2584404b-1fab-3265-9112-c38bab673816 | -2.25816 | -48.81963 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac595d2b-a5ad-3470-8ba8-9268d0d572f2 | -2.25755 | -48.8236 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2045db0b-03ba-313f-b3ce-7f49603be612 | -2.254 | -48.82306 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9aff82d7-1ab9-3026-987f-bb7233add0d5 | -2.18107 | -48.73517 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fbe7bfa-3c86-3563-b94f-94c6038b7453 | -2.17334 | -48.83212 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96af90ca-b2f1-3829-8d86-27e70e9cf9e0 | -2.15976 | -48.82597 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58b436b1-5d3e-32ad-bd45-022bca667158 | -2.87893 | -48.24196 | 2024-10-19 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5202556c-da23-3163-98bc-8403285bf7dc | -2.87524 | -48.24139 | 2024-10-19 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d2e044e0-9bd4-3417-ac92-eeec3f13fa49 | -2.87393 | -48.25002 | 2024-10-19 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfba22f4-fd21-3d5f-8007-9880c47ef5c3 | -2.87211 | -48.24736 | 2024-10-19 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7f14bb7-87a7-3da4-b84d-2f754182d06d | -2.87143 | -48.25168 | 2024-10-19 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 872d054b-82fc-35a1-ae65-042498391f15 | -2.87025 | -48.24946 | 2024-10-19 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f835413a-6f49-34c6-8826-d70544dd5513 | -2.7177 | -48.83262 | 2024-10-19 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 07fa3c4f-925d-30d8-828b-074c1e36f320 | -2.6537 | -48.49743 | 2024-10-19 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0137e001-9382-3167-8f56-3b021758449c | -2.46031 | -48.3502 | 2024-10-19 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2f8e8b4-4b5d-3eca-8403-e1446beadea3 | -2.44674 | -48.43826 | 2024-10-19 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a20a9c1-c51f-36d6-83ae-840241e5d543 | -4.95346 | -49.14421 | 2024-10-19 04:49:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe22b0cd-8be9-30bf-aee7-f7c07b938881 | -4.82924 | -48.54257 | 2024-10-19 04:49:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 747dc53e-33a2-34c0-8b81-14504f897e19 | -3.90887 | -48.33391 | 2024-10-19 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64c80601-02cd-3070-ab0e-9cbb8febb44f | -3.90516 | -48.33332 | 2024-10-19 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c04521c1-b9b7-3d8a-b042-b242dc3800b9 | -3.90447 | -48.33778 | 2024-10-19 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9573d917-7c68-3bee-9017-be931e9cfcd5 | -3.90145 | -48.33275 | 2024-10-19 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6a4b5ce-7f8b-3a1b-9e8e-53c0ff8913ec | -3.587 | -48.94407 | 2024-10-19 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README28.md)
