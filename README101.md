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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 927b9c38-b30b-31e3-b920-1a78f7a6c412 | -9.228 | -51.5638 | 2026-08-31 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| af7041fe-d0fd-3f2a-8c55-f5eae865d2c5 | -13.471 | -57.0373 | 2026-08-31 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 035fa3cb-be59-3977-b9cb-6347d6d5962a | -11.1634 | -50.5727 | 2026-08-31 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 56c98eb5-3cb8-37b9-87b2-b27b12391c03 | -3.6398 | -60.5656 | 2026-08-31 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 606ae2ad-0b2d-3819-b796-c3fdab421be6 | -14.4831 | -52.2151 | 2026-08-31 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 35.5 |
| d8148aa7-2d1a-3cde-852e-f33740b0ab6b | -11.3615 | -45.1955 | 2026-08-31 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| c39422f5-8d1d-313a-802a-3aa8c43a751f | -11.0563 | -51.4751 | 2026-08-31 15:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 6d8709f3-ccd1-33c9-8816-8abcffc2c86b | -6.7123 | -58.9412 | 2026-08-31 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| bd3f25f7-7ad5-334e-a8ae-7668d9208a73 | -19.4907 | -57.5609 | 2026-08-31 15:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.6 |
| b007012f-f977-3d82-93d8-e7351e3ea743 | -11.1824 | -50.5706 | 2026-08-31 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| c397e750-2f7d-3941-b79c-aca80af4aad1 | -13.9667 | -54.4157 | 2026-08-31 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 377.9 |
| a8cc1d5b-fe56-3f44-ae69-0de226acfecb | -6.8017 | -59.4394 | 2026-08-31 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6077e8fd-c24e-3f83-bcf0-ee742576cb14 | -11.0566 | -51.4539 | 2026-08-31 15:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 33553c35-9867-3f8c-96e8-0b84f5c996f0 | -9.196 | -64.4568 | 2026-08-31 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 3d42ec08-f5c7-3202-a650-ff52963b0ba2 | -5.8537 | -57.5576 | 2026-08-31 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 4d35ee66-27af-3a32-aecd-a13e6274dac5 | -15.2669 | -53.8851 | 2026-08-31 15:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 91c4c188-6773-31ee-8587-f8a4eac08fad | -6.7514 | -55.6654 | 2026-08-31 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 816531e8-cd59-3914-b8b2-48afcd6a5b84 | -11.6786 | -54.5484 | 2026-08-31 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| d0a016b8-f5ba-3c32-9f02-f1a3fafb8197 | -11.3611 | -45.2185 | 2026-08-31 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| b1be64f4-805f-3341-b523-f4778b425359 | -10.7407 | -54.0401 | 2026-08-31 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 288.2 |
| 1c5cb69b-06b3-37bf-9108-b2df22078f52 | -7.5661 | -61.3239 | 2026-08-31 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| cab67a61-4d0b-3970-b065-eb886b0c7673 | -14.5871 | -54.0944 | 2026-08-31 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 60f0bc72-795a-3742-83ba-6dbdf14f863c | -10.8043 | -50.5259 | 2026-08-31 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 4d12b459-3431-37e7-a93f-8b511ebdaafa | -12.1905 | -50.5194 | 2026-08-31 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 827872ee-d65a-3874-bfff-4123ff36c17c | -10.1087 | -50.2776 | 2026-08-31 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 64bdc15a-9274-3458-9693-cd48a3b71629 | -11.8021 | -51.0343 | 2026-08-31 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8bbeb14c-3af3-35b7-9f2e-247a7c2dfc1a | -5.2363 | -55.8914 | 2026-08-31 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| c13a54f3-afff-33cb-bc49-c89c28357c01 | -19.4706 | -57.5636 | 2026-08-31 15:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.2 |
| c430a096-20ae-3671-93b7-03d0da1bb157 | -6.2471 | -53.6623 | 2026-08-31 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d05c46c2-1ec3-3fd0-abe2-b40e75eb3743 | -8.7631 | -46.4418 | 2026-08-31 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| e1c3a598-fa2d-32ec-9e87-b4d5c1ddb04c | 0.1914 | -60.4878 | 2026-08-31 15:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 07f26bd2-ffe7-36de-9669-3ca622afb79a | -7.5136 | -55.3251 | 2026-08-31 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 18869948-4a75-3e39-95c8-43db6114548a | -10.5607 | -50.3595 | 2026-08-31 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| f8a1ef1f-dc56-336b-a40c-119268732268 | -12.1902 | -50.5409 | 2026-08-31 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 834d168e-43e0-393d-8d03-98417d242d81 | -5.5831 | -60.2307 | 2026-08-31 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 128.0 |
| ec939b23-f546-37d5-9f17-64a4b1c30b1d | -10.7598 | -54.0179 | 2026-08-31 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| d382f889-a6fe-34f8-a1cb-78d6548a30ec | -6.3032 | -53.5782 | 2026-08-31 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 031721d6-cb3b-3742-ae1e-bb53f8b2e28f | -8.948 | -62.3894 | 2026-08-31 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| e6c258b7-f41d-3ce0-94f2-09c6e279a7cb | -5.9636 | -57.6704 | 2026-08-31 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0de77b89-ca58-385a-a817-075213866a04 | -7.0982 | -45.7689 | 2026-08-31 15:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 231.3 |
| 5fb80791-66b1-3804-8b71-f48fd6ce5ded | -9.694 | -65.0958 | 2026-08-31 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 08958382-6a7e-384c-ad72-808c0250413c | -9.406 | -60.5711 | 2026-08-31 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 092c43e2-fc4b-3437-987c-f047185f5f78 | -8.6673 | -62.8369 | 2026-08-31 15:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d587b951-8a9c-36a9-944e-4cd43392edf7 | -3.6216 | -60.547 | 2026-08-31 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 4a3d04c8-3c70-3996-9858-ee044b3ed20b | -6.2847 | -53.5792 | 2026-08-31 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 5ff43e4c-a541-355c-8c3e-df56cbcb37a4 | -6.1109 | -57.684 | 2026-08-31 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 284.9 |
| afd10bfe-9829-37d9-b147-e4039f063a1a | -10.8046 | -50.5046 | 2026-08-31 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 149.8 |
| b742b978-b387-3108-90d0-92dea442e6f7 | -11.3427 | -45.1751 | 2026-08-31 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 6174c704-e047-3261-808b-0e4f2af9d8ea | -11.1349 | -49.9117 | 2026-08-31 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| f274d9dd-88f6-32e0-9b55-30699ca95890 | -13.8371 | -54.0989 | 2026-08-31 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 3fd8f9d1-8386-33ad-9c40-657440922961 | -11.8408 | -50.9874 | 2026-08-31 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 14fbefd0-85e7-337a-8aa1-d261da2a2171 | -5.4876 | -57.1416 | 2026-08-31 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 23c1246a-bd68-3fdb-b2e7-b300365f8f58 | -10.8617 | -50.4772 | 2026-08-31 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 6eccadc0-bd33-3e37-bb28-1eb07a75c16d | -9.4342 | -45.6704 | 2026-08-31 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| a2a398bb-1fd4-3623-b813-388ea2c8ba96 | -13.4194 | -51.3945 | 2026-08-31 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6684d2b3-04bd-3509-b0ad-9507fa3f7a0c | -10.7431 | -50.8514 | 2026-08-31 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 8478a91f-39d7-3d2d-99c8-5b6675b8604e | -10.844 | -45.3356 | 2026-08-31 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 535819f0-fd90-3b53-accb-3e313b1f5cfd | -9.971 | -53.9214 | 2026-08-31 15:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 26ae0c8a-7925-3596-bb9b-5b70faab9e59 | -12.1711 | -50.5432 | 2026-08-31 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d0df618c-a56d-3e64-a3e4-10eb82c22364 | -11.1821 | -50.592 | 2026-08-31 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| e4aa11a5-6afd-38e6-9361-03367cad5911 | -6.9177 | -55.6967 | 2026-08-31 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 8d7c99fb-b612-34e8-9b24-41037fc2451a | -10.9177 | -50.5352 | 2026-08-31 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| b65d27f6-9921-3b5d-ac92-40bbea1f9509 | -14.5678 | -54.0968 | 2026-08-31 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| dfe0567c-193c-30bd-8d51-8e32ee73a234 | -12.1714 | -50.5217 | 2026-08-31 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 8b54b0a4-a939-31b9-ba85-8ce62b271c79 | -9.6676 | -47.9429 | 2026-08-31 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| cb46a86c-c6f9-3e66-ac8a-7f5f0fa93d5d | -7.9907 | -46.5177 | 2026-08-31 15:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| ac74833f-7f63-3b69-ac15-5170a01d47f4 | -7.7938 | -44.084 | 2026-08-31 15:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 325.1 |
| 4dfecde4-e1fc-3126-adea-9233e0f37df0 | -11.0569 | -51.4328 | 2026-08-31 15:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 97bc9615-8416-3079-99bb-57fdcf515d2f | -14.5868 | -54.1153 | 2026-08-31 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 196.1 |
| 0804ab64-c79a-3c54-a6ca-e4a752da682d | -11.3423 | -45.1982 | 2026-08-31 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 5527b065-614d-3b8d-829d-278e8fe00f13 | -11.0744 | -51.5365 | 2026-08-31 15:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 1192dda8-058a-3eba-81ba-cf4e9d2bacd9 | -8.7439 | -46.4661 | 2026-08-31 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 215.1 |
| f5b0b76f-1e6e-36a8-b5db-bf874c92c0b5 | -10.7593 | -54.0589 | 2026-08-31 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 0db20c8a-b4d0-359e-b4a8-13554e25aca3 | -11.381 | -45.1697 | 2026-08-31 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| cec4f16a-3485-3c2a-a9d1-7ec1251091f8 | -10.7405 | -54.0606 | 2026-08-31 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 0d02ceed-dea2-3df0-8bff-e9d8a5c2a844 | -13.9474 | -54.4179 | 2026-08-31 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 203.5 |
| c72106c4-a34c-3f53-9a3f-13bd0e816d9c | -8.7989 | -62.5095 | 2026-08-31 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 202d59b3-129a-3bcf-a8a7-fefbc850773a | -3.6215 | -60.566 | 2026-08-31 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 176.6 |
| 3fa8720b-ac19-3939-a839-43d67ad22f7e | -5.2362 | -55.9112 | 2026-08-31 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| c3df00e2-395f-3e9b-9c5c-0e554b461700 | -9.6942 | -65.0582 | 2026-08-31 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1fb2dcb9-0f0d-3006-ad38-fa9437fa3cae | -7.1123 | -42.7727 | 2026-08-31 15:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| d19bf266-b8cc-3021-a739-21427ce9cff1 | -3.4002 | -61.3276 | 2026-08-31 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 1a376322-ada2-31d1-ade5-2b2dd4bf01e7 | -4.9788 | -55.8417 | 2026-08-31 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 67e8a0ed-03d8-3423-a492-0586955c9dbd | -14.5674 | -54.1176 | 2026-08-31 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| bd277a89-5f2b-3634-b513-37f19426cd48 | -8.7442 | -46.4437 | 2026-08-31 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 2957c641-36e1-370e-b96c-0d1a3fbe8d3c | -11.063 | -47.1161 | 2026-08-31 15:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 156.2 |
| f6e589cd-bdbd-3aa4-b418-b6e074cb0d9b | -10.7409 | -54.0196 | 2026-08-31 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 73c4428e-9c7f-329e-9ed7-f75553368303 | -12.0925 | -47.1587 | 2026-08-31 15:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 0eeea9c5-0e23-3fb1-bf81-6b05d1c07bed | -3.6076 | -59.0769 | 2026-08-31 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| d9eca424-366f-3e48-b26d-5894f5d72cef | -5.2548 | -55.8907 | 2026-08-31 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 1fc6a41f-da96-34e1-9ebd-95ba88555f52 | -9.5964 | -47.6204 | 2026-08-31 15:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 5773080c-477d-3a54-ad16-144f1203c2fc | -3.6399 | -60.5466 | 2026-08-31 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| ff47d682-cc2e-3afa-b118-b9ead2c55eb3 | -7.917 | -61.3481 | 2026-08-31 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| b545a68e-ace4-370a-956b-68bc091c2f9a | -7.5659 | -61.362 | 2026-08-31 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 570a50d2-2796-367a-8b33-3b2e55723126 | -10.7405 | -54.0606 | 2026-08-31 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 0fb44d86-1830-3ad4-ad70-1f7c7d43d9d4 | -12.1905 | -50.5194 | 2026-08-31 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 12efe2f2-bea7-3615-b8f6-250c99e28bb3 | -3.4002 | -61.3276 | 2026-08-31 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6b832f5e-cd2e-3c55-bafa-f6ee9427bf18 | -7.0982 | -45.7689 | 2026-08-31 15:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 7c6ae670-14ef-3b43-8a7f-4ba538f6ec51 | -6.1109 | -57.684 | 2026-08-31 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 257.7 |
| b81ade8a-7f5b-3603-98fa-93407bc6ccca | -10.5601 | -50.4022 | 2026-08-31 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |


[Clique aqui para ver as próximas entradas](README102.md)
