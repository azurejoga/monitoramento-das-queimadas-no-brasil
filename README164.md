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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab69b6d2-6ede-35a5-a49b-e0f36a75ee9b | -8.5587 | -44.7414 | 2025-10-01 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 122.0 |
| d0ac12ed-2fca-3bb2-afa6-625a21525e1d | -8.6908 | -47.7126 | 2025-10-01 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 8dc8e9cb-732e-3c2d-b957-5a9a47630e56 | -13.2973 | -50.6605 | 2025-10-01 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| a6e66943-cf26-3fec-bcad-2559084420e4 | -9.9387 | -43.6248 | 2025-10-01 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 0373c3aa-0343-32d9-aa28-dc19c7d65f9c | -7.4656 | -46.476 | 2025-10-01 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 55e97681-7a8d-34cc-bd8a-d1d7898209a1 | -6.5546 | -43.9221 | 2025-10-01 14:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 37354dc4-7625-3552-a2ba-970e1e4a40e3 | -10.1084 | -50.299 | 2025-10-01 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| ba826212-a35d-32b9-9e1e-89bcbb081ed3 | -11.6126 | -45.0443 | 2025-10-01 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| e9306818-5635-3d34-a6ba-692e93cd269b | -11.9272 | -47.8941 | 2025-10-01 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 0d071382-d05e-3f0f-957a-64fc0d90133e | -5.3276 | -42.7832 | 2025-10-01 14:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 131.0 |
| cbf62fb8-a1ce-3563-82d4-c1d9cf1cca71 | -13.1747 | -47.7869 | 2025-10-01 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 15c73e05-23d6-3ccc-abd2-839c10209eab | -8.6722 | -47.6924 | 2025-10-01 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 5d3e097a-8a27-3930-a864-3b1616e376ae | -9.9581 | -43.5987 | 2025-10-01 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 0ad89688-ac46-32b6-95b9-953458bc7cc8 | -8.5773 | -44.7623 | 2025-10-01 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| e029a7c9-cde4-36cb-98c2-50d89e14ae88 | -6.2998 | -45.0433 | 2025-10-01 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 24ffb827-f927-34e3-bc77-822e6f1fcb7c | -15.1444 | -48.0143 | 2025-10-01 14:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| ba401358-4ebf-3aa2-9b89-091f3f83e909 | -12.3672 | -50.1971 | 2025-10-01 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 3d67512d-913f-35d8-b856-876815a69150 | -6.5417 | -45.2055 | 2025-10-01 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a0ac2efc-0367-302d-a784-e50f5a834ed8 | -6.7165 | -44.5987 | 2025-10-01 14:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 8c0603f9-8421-3b47-9c7c-c0db7152bad8 | -9.9585 | -43.5752 | 2025-10-01 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 8ae42c83-6aac-37d2-885e-3c9321893a4a | -15.5379 | -45.2375 | 2025-10-01 14:30:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 123.7 |
| b6ca8e62-261e-319f-9d69-7f3d878321c0 | -9.8845 | -45.9576 | 2025-10-01 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 6c1e0eae-95d2-3c63-a828-0410a13eeec2 | -3.7973 | -42.1712 | 2025-10-01 14:30:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 1f9d30f8-8d0d-375e-ac5d-fe3c870fb32f | -12.2816 | -44.1275 | 2025-10-01 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 213.4 |
| bf5b777c-7d36-3a1d-abf6-346a8da7eb71 | -15.164 | -48.011 | 2025-10-01 14:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e44fc9b9-9476-3af4-8166-a0b4ea0b52b1 | -10.6432 | -48.5145 | 2025-10-01 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| b3593912-9859-3088-9507-8858d4736001 | -8.5081 | -47.2676 | 2025-10-01 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| d50fee7b-c41d-387c-8cd2-e2fbaca6b1a9 | -10.09 | -50.2581 | 2025-10-01 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 98f68799-bc4d-31e1-b908-eea97c856929 | -6.7624 | -45.617 | 2025-10-01 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| db317c47-6d42-3430-99dc-226b492fb953 | -9.1434 | -47.6457 | 2025-10-01 14:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 491653b4-1303-364b-b446-994b94abfe66 | -11.9081 | -47.8967 | 2025-10-01 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 540bb6bf-4eb9-30cd-8d2a-3a49cb31c252 | -9.9035 | -45.9553 | 2025-10-01 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 3298776c-e2bc-3113-9399-126b29ef2a19 | -8.5599 | -44.6494 | 2025-10-01 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| f3f3b744-2cae-312b-bba8-7c9240bfc18f | -5.7581 | -42.8682 | 2025-10-01 14:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 76adf1ae-7484-34f2-9496-5dc7cc52c394 | -7.8163 | -47.0003 | 2025-10-01 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 89f9d052-be92-345a-91fa-f67306e703cb | -9.4194 | -54.697 | 2025-10-01 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 3dc80dfb-4f33-302d-8bd7-ef63d10d6f81 | -8.4279 | -51.0638 | 2025-10-01 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| c6bd5727-28ce-30d4-8fb6-ff0b75573960 | -14.3524 | -45.8974 | 2025-10-01 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 6c16ec0f-51f0-364b-8f6d-621d97483aaa | -14.9738 | -46.8668 | 2025-10-01 14:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 8af7b542-72ed-3070-bb20-a05c9153e9ee | -6.525 | -45.0025 | 2025-10-01 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| d085a937-ef30-3cb1-b8ed-f7ba33691419 | -8.9182 | -47.5803 | 2025-10-01 14:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| f1c8bfea-05e4-3995-a313-a1acb8aef62a | -5.3061 | -43.1131 | 2025-10-01 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0dfff09b-2e18-3329-bcce-18e12df90aa5 | -9.8845 | -45.9576 | 2025-10-01 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 3f3f4af6-777a-3359-9be9-1ea13a63490d | -13.7684 | -51.2 | 2025-10-01 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 48110102-5254-3ba4-a8cc-92ea0978b04b | -14.9738 | -46.8668 | 2025-10-01 14:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 80ab7893-c641-33ac-ba4f-87dea3c05fa5 | -10.2521 | -48.0547 | 2025-10-01 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 9d37c0bc-2884-36f2-be77-e65f3317f415 | -5.1514 | -43.7057 | 2025-10-01 14:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 56774c3d-b684-38e8-9312-8cc0d3da2ab6 | -12.801 | -50.5519 | 2025-10-01 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 456.5 |
| d0be08b1-9036-37c1-843d-92d891fe3f40 | -6.5546 | -43.9221 | 2025-10-01 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 6ee39b8b-4605-312d-a81f-c0e9d38dbc6b | -10.6155 | -49.1274 | 2025-10-01 14:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| fa32e922-6afd-3d79-96ea-86fa50cc0dc1 | -7.8163 | -47.0003 | 2025-10-01 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 4353ee81-8dba-30d3-8863-732102a9407e | -12.2623 | -44.1306 | 2025-10-01 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 251.0 |
| d11f4400-693f-3984-9df8-5d6734f02b01 | -13.768 | -51.2214 | 2025-10-01 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| e029de5a-46d2-3f10-b8e4-672656cecbe7 | -9.4192 | -54.7172 | 2025-10-01 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| a3273a96-4259-3100-a5f0-b562837c9d40 | -12.2344 | -47.8086 | 2025-10-01 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 126b2a5d-4233-3745-b97d-03d2b6a9ea26 | -11.0225 | -49.8167 | 2025-10-01 14:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 6019461c-d760-3977-aeb3-9eaee9acaa97 | -12.3669 | -50.2187 | 2025-10-01 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 799.9 |
| c35aeaad-12fd-3557-90de-f4fac9b45b23 | -7.4656 | -46.476 | 2025-10-01 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 686ba54c-84f7-307b-9206-8ad51ba27e90 | -12.3863 | -50.1947 | 2025-10-01 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 251.7 |
| a8504a31-e280-333b-b65b-8749a46c6e40 | -5.7581 | -42.8682 | 2025-10-01 14:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 1b0c35e7-c08d-3f64-8c22-da7378506ac1 | -7.2996 | -42.8722 | 2025-10-01 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 9a45fc70-2c40-3de1-853e-e8b55dd88462 | -8.5599 | -44.6494 | 2025-10-01 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 76e1d6c6-ff32-3e37-a95e-4caf258c2c68 | -10.8421 | -46.6514 | 2025-10-01 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 307.7 |
| 42ca55db-d91a-3eb5-80f0-3195402c0b5e | -9.8201 | -47.8386 | 2025-10-01 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 06d653a3-faab-36cc-a223-c5e7c345316e | -6.7356 | -44.5742 | 2025-10-01 14:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| c0e2b983-0d62-3c60-9718-301ecaf2e55d | -5.3278 | -42.7596 | 2025-10-01 14:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 74bb1bb6-881b-3e80-a93c-81164fd2f43f | -8.1439 | -46.2797 | 2025-10-01 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 234090e9-a6df-3c2e-8cd4-43b08751655a | -13.7678 | -48.0106 | 2025-10-01 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| c6166a10-d5f7-32d3-9e5e-473869d0c8be | -13.7873 | -51.2189 | 2025-10-01 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 7cf1146d-40ff-3f6d-ac0f-275f1c871123 | -6.5437 | -45.001 | 2025-10-01 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 3e6c81e0-ce82-318f-8cde-40d503e651e4 | -11.383 | -45.0543 | 2025-10-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 76b9fa52-67a8-346b-bd35-c643a97b5109 | -8.163 | -46.2554 | 2025-10-01 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 44fb35a3-da25-37f3-9ab4-f4a79d349f30 | -3.95 | -41.6864 | 2025-10-01 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 121.0 |
| 13ffa5c6-6418-331f-b9ba-cb34eb4107f4 | -8.5584 | -44.7644 | 2025-10-01 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 99546fe9-6360-33e1-917e-6128dd8368b4 | -14.8026 | -45.7713 | 2025-10-01 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 366ef350-276f-3e0f-ae4b-b1acc17da744 | -5.7939 | -43.0532 | 2025-10-01 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| afab6e87-e3b4-36d4-a9d5-bef9c6602c48 | -8.9182 | -47.5803 | 2025-10-01 14:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 3906675e-47da-31cb-af17-4782441df802 | -8.3869 | -47.9824 | 2025-10-01 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 10da59ee-7aa3-3748-aaf1-4b0b9a4f2acf | -7.4758 | -47.2728 | 2025-10-01 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 41bd4bf6-a377-3e44-8656-c55840aceb50 | -5.3091 | -42.761 | 2025-10-01 14:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 55a759cc-f75c-33c7-92b3-3005a1bae52b | -15.5384 | -45.214 | 2025-10-01 14:40:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 8018aa85-7b57-386a-93e9-c967a597d5c6 | -8.6722 | -47.6924 | 2025-10-01 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| c5b775fa-487d-360d-8212-025955a590db | -5.4964 | -42.7707 | 2025-10-01 14:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| c57ff948-5b10-34c2-91b4-39438d1a86d1 | -12.3672 | -50.1971 | 2025-10-01 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 313.9 |
| 5dd29208-4876-3afe-bb1d-41e9dc7c63a1 | -9.1248 | -47.6256 | 2025-10-01 14:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| b0f0b8c7-54e1-315f-845a-74f6b72d87ac | -8.7769 | -49.9763 | 2025-10-01 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| fc99fdf3-37da-367f-a89a-8d758fcea88d | -7.646 | -45.4489 | 2025-10-01 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 75e8517c-ae68-3fe2-8da1-8639e488044e | -11.4608 | -44.9739 | 2025-10-01 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 13e9020a-3bdd-3b96-9311-2efadd816e44 | -11.8434 | -44.9872 | 2025-10-01 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 353408e4-0ad1-3e0b-a770-d327f1f5794d | -10.271 | -48.0526 | 2025-10-01 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 160.2 |
| bd4e8354-d8fd-3e3d-bc66-4bb1b649de11 | -11.7797 | -47.5806 | 2025-10-01 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| f35beaf3-c202-3267-8d74-f7d8a93e3cdd | -4.1574 | -44.2726 | 2025-10-01 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| a5efae3c-b575-3ebe-97b6-2d3b08fbffd8 | -12.8774 | -45.1742 | 2025-10-01 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| dd8284e0-6ad7-370f-8f88-2fde3d6bbd8e | -8.9188 | -46.0664 | 2025-10-01 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 593a7700-56e7-3fdd-80ea-0cedffcd8e73 | -14.3524 | -45.8974 | 2025-10-01 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 5b7803ed-126e-3a2a-85b9-49872adf9f29 | -6.523 | -45.207 | 2025-10-01 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 26dc5570-2e1a-36f5-86a8-35215bf7edbb | -7.6272 | -45.4507 | 2025-10-01 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| c2ff33aa-978c-35b0-a912-7846a41c5262 | -12.7876 | -46.8792 | 2025-10-01 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 13013919-515d-3948-afa1-07fadd1d36b3 | -14.764 | -45.7552 | 2025-10-01 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 35945de5-c451-3301-b584-471647f8f969 | -13.8065 | -51.2164 | 2025-10-01 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |


[Clique aqui para ver as próximas entradas](README165.md)
