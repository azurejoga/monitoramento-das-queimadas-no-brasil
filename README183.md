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

## Dados Diários - Página 183

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ec667e0-0cbd-340c-b9b8-08d1d5632111 | -3.5893 | -59.0773 | 2026-09-21 18:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 3f243d97-6865-3298-a6df-b98aaf6e5d89 | -3.4215 | -60.1896 | 2026-09-21 18:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 5ba1963f-2568-35d6-899f-147bccca806b | -5.5848 | -45.5478 | 2026-09-21 18:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 45a3a14e-9e2e-3dd3-b55c-fba67bc0e5c4 | -1.4302 | -48.9529 | 2026-09-21 18:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 472e4186-4505-3591-a6c3-28e7db0e89fa | -11.3359 | -43.3793 | 2026-09-21 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 95d93f57-53fa-3291-8043-470e774e0a50 | -10.4728 | -51.302 | 2026-09-21 18:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| ec3e7209-664d-3030-86de-f033e50dd0e4 | 1.0844 | -60.6741 | 2026-09-21 18:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 102.3 |
| e4202d3e-cfbd-3d99-bcdf-4ab33e96f5eb | -3.8957 | -60.5984 | 2026-09-21 18:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 122.6 |
| b61043fc-0979-3401-b398-60984741a327 | -10.8853 | -51.5347 | 2026-09-21 18:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 6cb953d6-95b1-3c65-bc6e-9796e6efdec9 | -9.7504 | -46.0637 | 2026-09-21 18:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| ae79d0f7-6a99-3073-834b-15651685f8fa | -9.8692 | -48.4033 | 2026-09-21 18:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e86f7cfb-5a2c-368c-99e0-aa81512d7fd1 | -5.9333 | -53.5362 | 2026-09-21 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| fa3a7769-f410-3813-8fb9-bbf2b5a962c0 | -6.2946 | -47.6493 | 2026-09-21 18:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 4b94bc33-fc42-31ac-819e-97591cd5a0a9 | -2.8791 | -57.799 | 2026-09-21 18:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 231.9 |
| 02b204bc-5fec-3fb4-a8c9-16a5116b1d30 | -2.9906 | -57.2137 | 2026-09-21 18:00:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 144a2d92-dbab-3e78-b10f-0d07e83433ef | -6.0743 | -57.6465 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 1ee1b126-9a2d-3e8d-8017-9170c2fa9efa | -6.9223 | -42.9323 | 2026-09-21 18:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.7 |
| 10ab0e72-caf6-353b-9541-47cea700bcfb | -5.9151 | -59.9522 | 2026-09-21 18:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2b2e2ddc-f952-3b40-8aa8-b7ca29bc5b10 | -6.2585 | -41.6617 | 2026-09-21 18:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 6fff694c-31b4-33de-891b-8cffb8638caf | -11.6802 | -43.4209 | 2026-09-21 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.2 |
| e71a4f95-fba8-3127-8fb3-bd109a6cd35c | -8.8758 | -71.4806 | 2026-09-21 18:00:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ac2cf150-6b80-3c2e-9586-cd4f8550b7b4 | -3.753 | -59.419 | 2026-09-21 18:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| a77fbb38-c9a0-3bdf-b5d3-c2372b072519 | -1.6583 | -54.913 | 2026-09-21 18:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| b6b0ff02-d708-3e32-bd26-3ef5bb85979f | -10.8472 | -50.1581 | 2026-09-21 18:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 349.4 |
| eeecf429-e302-38d2-a4e7-b441bf1a6202 | -7.822 | -61.8084 | 2026-09-21 18:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 128.1 |
| ee71f9a9-6f03-38f3-be93-19810720cbf9 | -7.9152 | -72.9324 | 2026-09-21 18:00:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d96690b5-1296-3779-9838-28780586b866 | -11.8559 | -49.979 | 2026-09-21 18:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 4fcbd41d-5068-3c89-98d5-1855cb6a6347 | -7.3289 | -55.2155 | 2026-09-21 18:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e7671684-f981-3f23-9da4-d47fe05b118b | -11.4541 | -45.3662 | 2026-09-21 18:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 327c9eab-ea64-3b8a-ba9a-6894a8553452 | -3.1514 | -58.644 | 2026-09-21 18:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 51d225a0-c4de-3b93-b168-0e0181d354d9 | -10.6883 | -50.7084 | 2026-09-21 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 2a013683-3b4d-3799-80f7-89a9d80f64d1 | -2.9391 | -50.4832 | 2026-09-21 18:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 86142c49-808b-33e4-a780-5f94938e217c | -9.3797 | -48.3232 | 2026-09-21 18:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| f4d68de6-5672-37fa-ab9d-b78a80937810 | -6.5571 | -45.5434 | 2026-09-21 18:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 274.7 |
| 01b110a8-f847-3fe7-b6c9-8a16f5b4e293 | -3.6449 | -58.8647 | 2026-09-21 18:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 67873942-57a7-3234-b83c-ad944e0b1459 | -7.8825 | -70.1381 | 2026-09-21 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 12055215-749e-3ba6-8dde-ca88d36d23d6 | -3.3142 | -59.3132 | 2026-09-21 18:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 095f7791-fc8b-33d8-9ec7-d6b9a516b28c | -9.419 | -68.7499 | 2026-09-21 18:00:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c646262e-2a3f-3e12-a946-a96af20be11e | -10.2732 | -68.7489 | 2026-09-21 18:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1b4c5864-4893-36f0-98b6-8ac812a93462 | -2.9525 | -57.7394 | 2026-09-21 18:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d22a2f41-f10e-3ced-8347-4e329d834415 | -10.4288 | -50.3305 | 2026-09-21 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 21d1d512-a7d4-3eb9-955b-e04432678920 | -5.9335 | -59.9515 | 2026-09-21 18:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 288f2ada-5769-314c-a377-43c08f96cbd7 | -10.279 | -50.2391 | 2026-09-21 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 948d9906-a78e-329f-a8d5-5cca17bbe7c9 | -9.294 | -60.6153 | 2026-09-21 18:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| ab45210d-fe17-3cb0-996b-c78df8d9eb60 | -9.0287 | -69.2191 | 2026-09-21 18:00:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 60.2 |
| b1f794a1-32ef-304b-b43d-5d002f0225cd | -1.4487 | -48.9526 | 2026-09-21 18:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 5c278e4d-8673-3c02-ac0c-493c4cbefbba | -11.4353 | -45.3459 | 2026-09-21 18:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ba4608cc-5585-37e8-a4be-358683f5b8a5 | -0.7471 | -49.2161 | 2026-09-21 18:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| db1c5a90-59ff-3942-9bf8-cd1c7aba0a54 | -6.8796 | -41.6995 | 2026-09-21 18:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| dec3b428-1aab-35fd-a51c-33f9752b6fec | -3.3138 | -59.4281 | 2026-09-21 18:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 09c2fe01-b4f9-339e-85ac-58b5365b39de | -11.8499 | -46.8105 | 2026-09-21 18:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 708306c9-9a8d-371a-8098-500959f12c4e | -5.9151 | -59.9522 | 2026-09-21 18:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 26eaff0c-7133-34b7-a59a-dcf246911641 | -10.2748 | -50.5592 | 2026-09-21 18:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| edc172be-5189-3032-bd8d-795ecd3e96c6 | -5.9335 | -59.9515 | 2026-09-21 18:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 5b76b4eb-8b02-311d-8521-0a1652a1ea64 | -12.3018 | -50.7203 | 2026-09-21 18:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d436a4ff-e98b-3817-9175-b5cfb1ab69db | -9.5885 | -45.4707 | 2026-09-21 18:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8fcf7bc4-c02f-31c3-8f56-0915ba761141 | -3.6449 | -58.8647 | 2026-09-21 18:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| bfc38ae6-9d3d-32ce-bdf4-8da4bf4dfa4e | -5.8159 | -57.7346 | 2026-09-21 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 294.9 |
| 784464ca-2f7c-3e79-8cb2-539c1a274a81 | -3.753 | -59.419 | 2026-09-21 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 6d76adf6-7e4c-3413-89ba-27c61adcc90a | -8.6755 | -70.0345 | 2026-09-21 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 07400064-c394-345a-b189-8124d2cbafd1 | -3.7707 | -59.5909 | 2026-09-21 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 90ec77c9-c0a2-39f7-bb93-f723b8086861 | -6.2766 | -57.7358 | 2026-09-21 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 99f5e8a6-6c34-3c25-83dc-7c92035cc606 | -12.8387 | -44.2008 | 2026-09-21 18:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d7351e4c-3634-33f8-9077-34e73b30cfdd | 1.0397 | -51.1445 | 2026-09-21 18:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 8655e865-5f87-3310-b866-4cb49e7cb5c6 | -11.6802 | -43.4209 | 2026-09-21 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 009c92ce-acbe-34ee-83d5-2dd831851ea8 | -6.5569 | -45.566 | 2026-09-21 18:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 12d70771-ac48-3cfc-9237-1e0f13bfb31a | -5.6223 | -43.3701 | 2026-09-21 18:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 3a58f004-ddad-3115-bfc5-072fa3e80e43 | -5.6221 | -43.3934 | 2026-09-21 18:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d1d16e6c-a9c6-36fe-afd3-5d5eb065222a | -10.6883 | -50.7084 | 2026-09-21 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| b7429999-3cf5-3d7a-a3b5-16b49dfa0c30 | -3.3139 | -59.3898 | 2026-09-21 18:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| f23576fb-81cc-34db-be32-445c8d032e51 | -10.1814 | -68.4175 | 2026-09-21 18:10:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 14ede89d-1bfc-3b34-b14d-2310eb029d89 | -9.2939 | -60.6345 | 2026-09-21 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 237.5 |
| 865850b1-5a98-3c39-8765-bed68e6f0ef9 | -8.7916 | -44.2778 | 2026-09-21 18:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 469.5 |
| 4caf4d9a-c132-380a-969c-192f7349b72d | -10.473 | -51.2808 | 2026-09-21 18:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7c0a6cdd-60d3-3218-8ed4-2d8cc90ed66d | -9.859 | -46.4114 | 2026-09-21 18:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| bbddb8fd-874f-3dda-b875-a8c826d8d1c3 | -1.3742 | -49.3154 | 2026-09-21 18:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4404a22f-1cf7-36a1-b25f-b0c9a064b414 | -11.4001 | -44.076 | 2026-09-21 18:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 17cc89ea-e397-3737-b606-6670b313e7bc | -8.3167 | -45.9934 | 2026-09-21 18:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 5ebe416c-00c2-3a8a-abfe-c0ac78324299 | -2.8608 | -57.8188 | 2026-09-21 18:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 204.9 |
| c68d0422-c44e-34a6-ba70-595994921fef | -10.6875 | -50.7722 | 2026-09-21 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 36cc1259-5c92-36fd-bc2c-13c2f4247892 | -10.2152 | -53.9216 | 2026-09-21 18:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 146.7 |
| ba91631f-31d8-3951-a0d5-46d9c04bea61 | -3.5318 | -59.9588 | 2026-09-21 18:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 3060ab75-1ce6-3014-a43e-6523370d46b3 | -8.7911 | -48.7502 | 2026-09-21 18:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 324b381f-95ca-3f54-837c-e396c6831d48 | -4.3542 | -55.6455 | 2026-09-21 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 13b5afd4-913f-36a9-99da-3d9f897c4b99 | -9.4202 | -68.3802 | 2026-09-21 18:10:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 31755163-0cc2-380f-b9a3-263615a47591 | -6.9223 | -42.9323 | 2026-09-21 18:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.0 |
| 374986be-4e79-39f9-8092-423486472216 | -10.8285 | -50.1386 | 2026-09-21 18:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| d5e12785-d099-3bb8-8e32-3b972c8a4a96 | -9.0415 | -49.8245 | 2026-09-21 18:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 950d461a-481b-36cb-a65c-49bda03e3803 | -10.8475 | -50.1366 | 2026-09-21 18:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 195.8 |
| fa8f3dd2-5749-3c81-b189-c7b13c137103 | -11.801 | -49.8345 | 2026-09-21 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f1a0d9db-ca58-3f1d-a99f-23dda5c224e0 | 0.7755 | -59.21 | 2026-09-21 18:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 38c7f1c5-899e-30c2-b15d-696840f3a337 | -6.922 | -42.9559 | 2026-09-21 18:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.3 |
| a4c0fadd-f720-306a-a73f-d13607816ef8 | -7.5477 | -61.3247 | 2026-09-21 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 9e225d9a-cc1f-3d3e-bebe-dda9692783aa | -8.7447 | -72.7992 | 2026-09-21 18:10:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 19b460c9-0687-355d-a567-156c77de9d5a | -2.9525 | -57.72 | 2026-09-21 18:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 840e648d-3181-342f-bd7f-beb21307d89e | -7.5891 | -57.6561 | 2026-09-21 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 244.0 |
| a62c2fb8-3df0-3739-ab53-4995b0d87cf4 | -6.3436 | -55.8243 | 2026-09-21 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 25c5b05c-088d-33bd-a5b6-4918321a2a10 | -7.6264 | -57.615 | 2026-09-21 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 48230dba-e1f9-38c4-87b9-fc616a0f73be | -3.4578 | -60.265 | 2026-09-21 18:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 7ffa3104-53d2-31a6-bae9-d2a3ce4793da | -2.9157 | -57.8177 | 2026-09-21 18:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |


[Clique aqui para ver as próximas entradas](README184.md)
