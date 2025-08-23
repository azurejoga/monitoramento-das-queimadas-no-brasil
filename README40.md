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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 469cb310-27fa-3e6b-bbec-99a9bb306daf | -6.10198 | -45.90479 | 2025-08-23 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5db1cfb8-aa34-35b8-8e23-650d86e537f1 | -6.74495 | -50.95501 | 2025-08-23 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b678fa6-b8a0-3e17-b37e-03c95a5ae657 | -4.89945 | -49.92569 | 2025-08-23 04:51:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f309e51-76d0-3260-b72b-cb0d8b9d0380 | -7.61185 | -46.26598 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b9bdc3f-88ec-3aa7-9a10-52527450e579 | -6.3702 | -45.56121 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 73cd2c19-a692-3ee1-9292-7f7db33116cf | -6.87376 | -59.81825 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b506bbdb-73f7-3e1f-b936-3c75008a2260 | -8.59195 | -62.61964 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 93542f0a-aefa-3725-9efe-18f5fd4929d7 | -6.63454 | -58.54004 | 2025-08-23 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb228c0d-9453-3538-81c6-fd77d213853e | -9.06041 | -49.53219 | 2025-08-23 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bdd3a32-ebeb-375a-9d79-00607d4269d1 | -6.57219 | -59.87323 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 11ae1a87-541e-30b4-be8e-b509f72fd605 | -6.38704 | -45.52589 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b250d507-768b-3227-b179-c6ee92004767 | -10.64498 | -50.12978 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6c36668-5929-30b3-8488-e70b343c67a7 | -5.74616 | -57.59947 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1041d4c1-6e09-3845-8432-f20d47c42143 | -9.18225 | -59.64391 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b507257-af07-39b6-95a5-6a0164b61a54 | -8.89619 | -47.33197 | 2025-08-23 04:51:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba32b022-dbc0-3537-a692-0995a1d15a1a | -5.80248 | -59.21965 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dadb6bce-f338-3cf3-8020-a6125b2b50a9 | -8.39455 | -48.17444 | 2025-08-23 04:51:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f34db39b-245e-3978-aead-dc83c9036abf | -8.52241 | -48.85826 | 2025-08-23 04:51:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c5b21c8-a769-3797-9e13-5074d05b5c69 | -9.2054 | -59.47339 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 84d5283f-f313-33e7-aadd-c295bc28878f | -4.07734 | -48.0386 | 2025-08-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05266f93-6ebb-37e1-88af-c1f5ee7c1a35 | -5.61445 | -60.22915 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 187585a2-92c0-3e77-8eb6-4895e9d8156e | -9.19744 | -59.44252 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a4122eb-f9e4-3f65-a072-d770527f6fa7 | -9.17352 | -59.60833 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d7686c7-8954-35d6-9130-c9b0826b2bfb | -8.6222 | -62.63566 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a99c68f-a9de-3650-b4e9-d3b39070f6ce | -10.75442 | -48.25504 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d3480da6-6147-3594-9870-5024d38001b7 | -9.18807 | -59.6363 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43cf60b1-9478-3dd7-b6c0-e7f3ce2699cb | -3.65435 | -48.32848 | 2025-08-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bcc69d2-b9c0-3b9f-b7e9-ac69ad8bedce | -7.55149 | -63.85377 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f795dbe6-dd18-3599-a805-69c1c5079ef6 | -10.74861 | -48.25118 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a30a573c-11f5-3903-a820-be4da158b50b | -6.18224 | -45.43298 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2baeb231-1d26-3c89-b4a8-d4014b3fc564 | -6.45239 | -53.38791 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c2c8981-e15f-3e61-a073-b7d2a02c5062 | -6.00709 | -53.32091 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30530090-64f6-3e9e-a08b-4b27ed9bf693 | -10.75542 | -48.24763 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ebacda75-140e-3f8a-8cc9-fc873de6cdd4 | -7.81334 | -51.00647 | 2025-08-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c6b22dd-d8d7-3b1d-829c-762d701101f0 | -5.73814 | -57.59825 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ab07b89-b90a-3dbe-9a3e-63461cb4687a | -7.78489 | -61.57863 | 2025-08-23 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0386baac-c3a0-3bc3-a232-fb62b96abe4c | -6.32021 | -43.74919 | 2025-08-23 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 75070f89-0fac-359f-9018-5f07bbcc73cc | -6.54199 | -55.30743 | 2025-08-23 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f466c333-e163-376d-93ca-a38a3cbc571e | -10.22613 | -47.56717 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3222871-d1ca-38e2-8523-c6474bb5dfaf | -11.12607 | -44.7585 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 602f23db-30bc-3308-9927-24bfb1e469bd | -9.20251 | -59.46443 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 082b9862-1d32-34a0-bd71-fc6e989b6a97 | -9.25446 | -59.61362 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cccdb9bf-27bb-3f4c-8b4b-426289209723 | -9.47472 | -57.82405 | 2025-08-23 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d09409d-b7c5-3033-a902-a84163a6653e | -8.30841 | -47.27025 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92b90934-234c-362d-8a74-3d288ec5d74b | -5.74791 | -57.58904 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 7db1aa5e-7738-313c-81d8-6cc866631887 | -9.19029 | -59.62378 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8de46d04-081d-31a4-b344-2355df657b5b | -4.2272 | -47.21373 | 2025-08-23 04:51:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4eb664d8-3bd7-3409-8217-f722676bdcca | -5.88245 | -57.75615 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 572e0b4a-df4a-3999-9359-341430794f77 | -6.65346 | -58.81583 | 2025-08-23 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d85f2d2-6785-3615-8cfd-8556aff1ae53 | -11.14112 | -44.76724 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04c988e2-0867-35e2-bfba-ab0f25f4a8d3 | -9.25014 | -59.61289 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5611d83c-1059-3141-95dc-8d5de001129a | -4.82377 | -47.31635 | 2025-08-23 04:51:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9767b358-d729-379e-aacd-350d1d0309a8 | -7.30189 | -59.63056 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d059a9c3-f1db-3279-a85d-e0f52c80c2d5 | -9.21159 | -59.47871 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0bb03dc-7a26-3efd-bff0-b145d7a04747 | -7.02714 | -44.63882 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 42ac5ff4-c638-34c5-a942-368cb77b256f | -9.21414 | -59.61499 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9afa994f-ab8c-3acb-b3e4-25c051fb9437 | -9.8785 | -47.80877 | 2025-08-23 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa473144-cbae-396c-b128-e75a0af1a40c | -6.31062 | -59.89036 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1355a3f4-a6af-37c5-a742-b7ca64d39ce1 | -6.30908 | -59.89267 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7adc8780-907f-3402-8db0-fde657c3ec87 | -7.81679 | -51.00694 | 2025-08-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 761a46ca-9f72-33ec-9b05-514d181176fe | -11.12525 | -44.76513 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5056ae8-7ac2-37e5-8d87-c789c2b575c7 | -6.12327 | -44.40728 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2455801f-5660-3d81-92c3-2fbcf644cdda | -7.02508 | -44.65347 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d2437271-8a4e-3eec-8372-37eeac2b309b | -7.43543 | -45.41868 | 2025-08-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07dceca9-8146-38b5-901f-4904c5be33da | -10.75325 | -48.24831 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 466d1240-2c63-373d-b283-1376fc77f5ee | -6.97863 | -44.18202 | 2025-08-23 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa22de01-7da6-37f2-bf9c-7f40fc20171c | -3.41392 | -48.87793 | 2025-08-23 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04bb175c-1546-3629-9ce0-edd3ba440e32 | -9.07798 | -49.51635 | 2025-08-23 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aaa452b-7abe-30e2-95ba-fd2ef94d3123 | -9.18596 | -59.62306 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 188847dc-3512-340b-b62a-0b4791ac04ac | -9.23116 | -59.74813 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 874eb4af-39da-39a4-89ee-84b99273ee30 | -7.62493 | -63.48334 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4e51d7b-403b-38d6-ab58-755a568b5a68 | -9.19103 | -59.61959 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 04b906ac-1b42-386a-aca9-5d0101ee3ed5 | -6.37896 | -45.53214 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 196875f5-33f4-3fd1-ac00-9a0cdbfb84f3 | -9.44713 | -47.65041 | 2025-08-23 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fc455682-f7d4-3799-bafe-b14e31969490 | -5.74768 | -52.32794 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2447a21-5c03-3f8d-800d-17f183549976 | -6.87392 | -59.82075 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 95ed4de1-d3d8-321a-bbeb-385f664975b5 | -9.81182 | -46.40309 | 2025-08-23 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 01e26e0d-4ca9-3688-8db2-7fca91a0cee0 | -5.74465 | -47.42428 | 2025-08-23 04:51:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04de590b-315f-3321-8e8f-3a22e62aa44d | -5.88159 | -53.61965 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 738e61bc-d935-3808-b412-6ab4163b69b3 | -9.20737 | -59.45277 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4aacf20-d9cd-3859-a2f7-47793e222ce3 | -10.70834 | -48.2059 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3b689c2-8117-3905-a188-06df52954f48 | -6.78223 | -44.33299 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccea1768-b5fe-37ae-bdf1-3d1f1ae26861 | -9.18151 | -59.64808 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d8d5357-1a8f-3d58-a013-a67f09b5eaa7 | -5.85666 | -43.88898 | 2025-08-23 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7d1e3496-48f9-3c00-9bf9-002ed1df7b8e | -9.15405 | -59.59206 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a4b9004-4f65-356f-8374-01c29c91ff00 | -6.3776 | -45.54203 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 5589f226-acbb-3af2-b8ab-e94673dbf50d | -3.98756 | -47.88639 | 2025-08-23 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3655b3ec-2f18-3db5-9d10-1cff439b5fba | -9.94261 | -48.90059 | 2025-08-23 04:51:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc680591-8c81-300b-a90a-66e5007ec764 | -3.43625 | -49.04682 | 2025-08-23 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bde6fad0-21f4-3ba2-bc34-9125c6f03b80 | -5.8017 | -59.22418 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21c1ed24-10d2-3482-9eb7-56bcbd54b38e | -8.01683 | -45.49201 | 2025-08-23 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4853f6a8-67ca-362a-b919-f0c9fd822dfa | -6.7818 | -44.33617 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87d75ca3-3da2-36d4-a0b2-3090256e8c81 | -11.12893 | -44.7788 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 345647c4-ceea-3494-8285-f9bc5ee1d4cf | -9.20955 | -59.44896 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1616c3c5-14b4-364e-a66f-9433e253eaa4 | -10.74516 | -48.26103 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 048b14f2-e87b-3d69-a47f-55b373ca5f34 | -2.93058 | -53.69311 | 2025-08-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93b63a6f-f123-3e9b-b421-91798995e3f4 | -6.72688 | -51.97865 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f18e953-8c15-3846-b174-b7cc1228ebec | -9.17137 | -59.62088 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33023870-f364-3033-bcf4-61eb1f2e4c6b | -6.37088 | -45.55623 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1b9f7fcf-c7fc-3c39-b9ed-af5471e2a6fd | -6.27145 | -53.71397 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README41.md)
