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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cedeb43e-b686-393f-8dff-6c562a03a5fe | -8.90234 | -60.59314 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56f77b8b-546b-32fe-8d62-43502c7598a7 | -6.86412 | -58.98021 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f1f0e363-c5a7-30cd-a3a4-ab0039ec28c9 | -8.61006 | -54.68992 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e3b9224-0560-3959-be7d-b4b18cbe0b42 | -6.62078 | -59.0714 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| affcd93e-2415-360a-8067-6b611f391db0 | -6.53808 | -55.17873 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cbfe2b1-bbbe-3bc3-8d33-7eab6c62fc86 | -6.96653 | -59.29655 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4be3f619-101c-35a7-9755-8b5f25188e41 | -9.49675 | -51.61703 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5916263b-c1d9-315b-a170-c6853bcdc98b | -6.82121 | -56.4551 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9934a9cd-9cab-3f7a-82e9-3ba282c69515 | -6.85928 | -56.42375 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33bb39ef-8964-3208-ae3c-3f4c284595eb | -7.64598 | -42.75641 | 2026-08-16 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 97b95558-22fa-34ab-b679-17b0f8b941b4 | -7.07 | -56.65006 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 857197db-127b-35b7-b9a8-2c3403beb886 | -8.6462 | -54.69062 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbfc9d66-7f1d-3195-ae8b-3b8e2a0c50aa | -6.81703 | -56.44565 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1ca6f360-c9bb-3277-8224-221184f403eb | -10.62558 | -53.90065 | 2026-08-16 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a8b90fa-64de-3f23-9f02-891f8f80698f | -6.8208 | -56.45095 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f7614fdb-9c51-3ee1-ae76-d6568a3015cb | -10.94261 | -57.13786 | 2026-08-16 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58147c54-7fd4-38dc-9107-f7e245bfc1c1 | -5.62759 | -47.106 | 2026-08-16 04:40:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc54c041-683b-3c5a-800a-4dd9aa5c4ab4 | -6.82835 | -56.46155 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a5f47493-f591-3c29-81d2-6507c7c13f0b | -9.10962 | -46.39144 | 2026-08-16 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16380200-09d5-3043-a359-859d04451c97 | -11.07045 | -47.25175 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb4e34bb-1c81-39a1-83ee-67f28e4441c7 | -6.62559 | -59.07582 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 65221e36-7d90-383b-a3ca-ccfe0cbafef4 | -6.7172 | -58.93439 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f3cee8c0-694f-3cd1-9773-963066c888db | -11.07039 | -47.27786 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af304fdf-ae97-3a38-8536-7c9cc0f0533e | -6.3099 | -43.60609 | 2026-08-16 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c749bb8-5e8f-3bcd-a6af-6814bcfc9feb | -11.21216 | -54.81603 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73823ecf-83f9-36de-9375-e999bcd3a7c2 | -7.4979 | -60.08116 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb186f89-6780-3f8a-81b7-7038292c6588 | -8.30154 | -49.40129 | 2026-08-16 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af325a07-fc12-362e-9bf3-17736ca07573 | -7.41121 | -60.00716 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d864822e-acd9-3b78-98a2-7d2ec96812d4 | -8.54861 | -55.2781 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 195387f6-2e38-336e-8e35-eda313ea0ce3 | -9.09779 | -46.39445 | 2026-08-16 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 414b0a53-4259-333c-a253-cb038a01b374 | -6.96105 | -59.29561 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffb9c46b-2877-30bd-aaa0-394afa72a213 | -7.04051 | -50.52992 | 2026-08-16 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10666002-61eb-35ef-bc7a-a93aca74f793 | -6.83406 | -56.46167 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cbd3b80e-9775-32fd-ad8a-6c5a7b6d35e4 | -11.10138 | -47.24361 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6d07d10-a71b-356b-a090-2455dce4df20 | -9.47135 | -60.50759 | 2026-08-16 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fae2bc29-0e68-3886-b9b2-d3b50e0e98f2 | -6.59694 | -59.11065 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a4a8f92-14aa-3dfe-9761-6cfdd1a51611 | -7.17213 | -43.23692 | 2026-08-16 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ed568dae-eb7c-3f32-80aa-667cc099e38c | -9.26315 | -56.90469 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78a4b7ef-f6c2-3d8e-a0ad-cb810969a69e | -11.05167 | -47.2531 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d305cc0-95d1-3266-88bd-3523a9aba58a | -10.27438 | -48.28905 | 2026-08-16 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5a646273-f957-3647-a411-13425c5730bb | -11.0771 | -47.25714 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54c41b3a-a64b-3928-939a-b9ad66b89bdc | -7.34435 | -59.60011 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ee28c2b6-ff3b-3620-8436-a2fc862d2b41 | -6.83447 | -56.42488 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 559b4086-1eaa-3cb6-95d4-4c5b745482fc | -6.69095 | -59.06429 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fe36e48-4dfe-3f0c-bbda-f089d26a9cfa | -6.60675 | -58.98191 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43122dca-da0c-3e13-a1cd-857bd3088b03 | -6.6252 | -59.04661 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f00ab085-4693-3039-b2b6-358d3103fa42 | -7.40973 | -60.01524 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c1a14b4-56d9-3a6f-8af0-afa5b8c59b12 | -6.70888 | -58.95042 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c3f8e47d-41ec-3aa4-9575-55dccb9a8a44 | -11.48519 | -46.59463 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c632e52b-a6f2-3da0-9e9c-b62ee5b18e47 | -11.3026 | -54.87839 | 2026-08-16 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8eeae434-44cc-3afa-ac68-1b1d1664e65c | -8.57414 | -45.3405 | 2026-08-16 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 533ce356-0212-3907-909d-d47a7ecf4fbb | -9.06074 | -45.78203 | 2026-08-16 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18355f09-382e-3e82-bbb8-2661cb80943c | -8.93702 | -45.46356 | 2026-08-16 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25c3d8ef-9c71-32dd-bffe-5b17e1da2200 | -6.99719 | -45.91156 | 2026-08-16 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccb4de6e-80f2-3a94-b581-0be2936eb3ef | -10.2698 | -48.29612 | 2026-08-16 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67fe9bb8-7d67-3e8d-9ead-b3c0de52e3f8 | -6.62745 | -59.06533 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 380ce8e0-b413-3075-8490-aa69e6f2bfce | -6.86458 | -56.41998 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bae3e0c2-6eb2-3cd9-9c66-4025b591e14c | -8.95032 | -60.56287 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f1f6303-c689-3581-b341-07d8b19f4e3b | -6.86006 | -56.41922 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3dec5779-1813-3752-9e3d-5446593aa3a2 | -6.25663 | -47.69654 | 2026-08-16 04:40:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d28fbf75-6493-302b-95b5-c4aef5dd31ec | -7.38443 | -46.82845 | 2026-08-16 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d735301-c729-3b6e-a19f-28859d60f54c | -6.84868 | -56.43123 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 760208ed-fa8a-35c3-8625-140222b1d01c | -11.48074 | -46.59877 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c1b0b55c-30f8-3eaf-9794-b58156236706 | -6.83065 | -56.44776 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1581fc3d-caa0-3a5c-8789-d6f0c314a598 | -10.18161 | -46.41205 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcdc24c7-f8ca-3394-b341-a49325390d6b | -7.01397 | -41.43214 | 2026-08-16 04:40:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b814dd4a-19a2-3089-a438-e1f35d461af2 | -7.55562 | -61.1745 | 2026-08-16 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0653bcce-3048-33dc-b02b-07a62d79c797 | -10.5395 | -44.84784 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce770015-7080-316b-ad95-c832d34a59ad | -11.21137 | -54.82073 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c7a60ee-031a-35cf-a39f-cecae20513f8 | -8.97156 | -60.51273 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b7aac6f1-59b5-3468-ad44-243bbc57e91d | -12.23592 | -43.14415 | 2026-08-16 04:40:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 65302a53-c450-3967-8d8e-8c216d432fdf | -6.70648 | -58.9324 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2fdfb248-873b-3aea-ba2d-41c02fb1915e | -6.58932 | -58.98621 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f89d2fd3-1cff-3e17-a6b4-059fc34b41a0 | -6.58871 | -58.9897 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3a78d15-7be1-35ac-b33d-9df94e7d2676 | -6.6772 | -43.99463 | 2026-08-16 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 63262b2f-0819-3010-9ebb-e4f6b2bc17e2 | -12.46209 | -46.65418 | 2026-08-16 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf84be2d-b24d-3383-bce5-29e524219aea | -6.63373 | -56.39256 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eab905e1-1529-390a-aa6f-1fb8818e7d99 | -9.37041 | -57.3642 | 2026-08-16 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccd3bfb4-5d47-320b-9e90-6efb32d0f6fb | -8.46173 | -45.42652 | 2026-08-16 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f19a0528-8938-30bd-986f-6395568e8b81 | -6.8691 | -56.42075 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab6881b1-f437-3432-a1f1-280a3c268579 | -6.60014 | -58.98794 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 706d78f8-4dec-3f89-b041-998ded115566 | -8.61145 | -54.70573 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1d17576-eeb3-3592-a11e-b168c26c94a3 | -6.87142 | -56.40725 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d0462f9-e04c-3cb4-af3f-45f1d1e22cda | -10.53062 | -44.85046 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2273c9ee-a060-3b0d-a55a-2bdf2ae925a1 | -6.86379 | -56.42456 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a91f7ee7-055b-36cc-9f45-4200c6195151 | -6.84322 | -58.97315 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4422a7e3-f8a1-3312-95c7-e9f7655440af | -6.71242 | -58.93005 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2acfd14c-d413-3c09-9764-eb21f6766cf6 | -6.60556 | -58.9888 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c547f88-31d8-37b3-961c-e0dd98d7782e | -6.63226 | -59.06975 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a7d877d7-5349-3c7c-9d93-b7ce95f204c0 | -9.48756 | -51.65263 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de82af17-b64d-3d29-8b28-3bb3f05a26b2 | -6.83589 | -56.42448 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 121823bb-a365-3c73-a881-ea6352fad231 | -7.38752 | -59.99633 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23f53b1e-9d86-35a9-97b1-574c3858be40 | -8.66022 | -54.72622 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cc1f41b-9623-3c39-bb6e-61de1a330a35 | -6.60274 | -58.98534 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 18a8599b-398b-34a2-92e2-c541cbc742f9 | -3.50535 | -59.58408 | 2026-08-16 04:40:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fffb2d0e-1385-383b-aa86-0e454d1bc19d | -11.105 | -47.24427 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5492dcca-a832-310a-8f5e-c1b4a07be6ef | -12.66015 | -47.09187 | 2026-08-16 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7213c4a-297b-3ace-9939-eedefbeaf535 | -5.23435 | -49.3372 | 2026-08-16 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a64cb45-8f01-35ad-84bd-c7f53a44815a | -12.23244 | -43.13556 | 2026-08-16 04:40:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a09b0b9b-7741-3857-bc29-c99ba0665abb | -10.52645 | -44.84984 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README21.md)
