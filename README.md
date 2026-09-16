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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e32b118e-9235-3090-9db3-df771cbd4c27 | -7.5608 | -62.33 | 2026-09-16 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| bdf0f6e2-db6d-32b6-9baa-3f8387af960d | -1.0182 | -53.739 | 2026-09-16 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a162594a-7ce4-38f3-9d56-92ffe0c852b6 | -3.1816 | -61.1235 | 2026-09-16 00:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f5dcd8c8-ef29-35bf-8bcf-76ca1761536a | -3.3231 | -47.1535 | 2026-09-16 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| ee81ac60-a941-34cf-84b9-70dfef3a19ad | -2.6966 | -57.6084 | 2026-09-16 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 128a2603-69e4-3b1f-8e92-050fce6e6f9a | -12.6621 | -50.8693 | 2026-09-16 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| f15ef3c2-48c5-3347-87a9-a990108f9064 | -9.0931 | -45.7314 | 2026-09-16 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 70caf923-4b1c-3ba2-9861-d1c5a0b11861 | -9.8012 | -46.4854 | 2026-09-16 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d53136a1-0f3b-32eb-8be2-23cbea99ed25 | -9.1123 | -45.7067 | 2026-09-16 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 1a9c0fd1-d26f-30e2-938f-71d7473bbc95 | -3.1174 | -57.6779 | 2026-09-16 00:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 1d03a108-3201-3b55-902b-28d6bea88570 | -8.6566 | -44.4777 | 2026-09-16 00:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 13599c3d-c19b-3a25-9579-466fea2800d7 | -6.2731 | -55.2904 | 2026-09-16 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 9bc539f6-062a-3b5b-941e-b33dd32b8df7 | -4.1824 | -49.4053 | 2026-09-16 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 8817c008-54c2-33d6-96e8-5160aa27f7f2 | -14.6122 | -42.1419 | 2026-09-16 00:00:00 | GOES-19 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 70.4 |
| da1adfe6-a5e3-30de-bf61-32f86bedcb03 | -3.1634 | -61.1048 | 2026-09-16 00:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6a32df6e-9a3b-399e-b20b-382c97ec854f | -12.7521 | -51.2213 | 2026-09-16 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 931a40d3-7edb-3720-916e-2a29cf7f1a0c | -5.144 | -55.9345 | 2026-09-16 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 2371c343-da51-30e9-9a98-7a4626657a6b | -11.9906 | -52.4695 | 2026-09-16 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 02a6d89e-d010-3b73-bfc3-6ccca09a2ef2 | -4.2951 | -49.1234 | 2026-09-16 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 0753e8b1-8d71-3230-85b4-9f04847ca914 | -18.2265 | -41.2303 | 2026-09-16 00:00:00 | GOES-19 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 158.8 |
| 90cae024-6ba2-3672-bc4e-7bf177b567c8 | -3.3232 | -47.1316 | 2026-09-16 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 21fbf174-e504-3561-9b68-1c78b5e943cb | -11.1401 | -40.4748 | 2026-09-16 00:00:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 0a19c6e8-d60d-3bd8-9a6f-a402d3c4e4ff | -4.8784 | -42.744 | 2026-09-16 00:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 3bbf0a7e-eb5b-3bbf-be2d-5de6ba84c8e4 | -5.1215 | -47.6146 | 2026-09-16 00:00:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 100.9 |
| d2a3c2a7-4900-332a-ab47-531ddd3703bb | -5.7756 | -45.0826 | 2026-09-16 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| e140664d-97c8-3670-89a7-326faa5c17ae | -10.4695 | -44.9491 | 2026-09-16 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 557089ba-c136-3911-888c-253825459bba | -9.112 | -45.7294 | 2026-09-16 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0775732a-0882-3f1c-af81-909d25b0ead2 | -18.2257 | -41.2559 | 2026-09-16 00:00:00 | GOES-19 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 161.8 |
| 7dff9b5e-2e6c-360a-8979-3d95b36a52f3 | -9.3893 | -60.3022 | 2026-09-16 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| cb8dd36c-1571-37ea-b8b9-0148cc260c4e | -3.3806 | -50.8458 | 2026-09-16 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 5296f0af-b46d-3e27-a541-750dacb46d7c | -7.6511 | -67.164 | 2026-09-16 00:00:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 140.6 |
| d51cfd62-ed40-3e5d-8a33-05e71f600fa8 | -12.7518 | -51.2426 | 2026-09-16 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| d33ccc62-670f-3b09-9728-befbb152d255 | -7.6327 | -67.1644 | 2026-09-16 00:00:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 8603b108-4e1b-32be-a570-b007bc2406ac | -7.651 | -67.1824 | 2026-09-16 00:00:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 56c9641a-07ec-3871-b998-a6c3fd019844 | -11.5033 | -45.8396 | 2026-09-16 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 3fb197b6-3f6e-3b18-8afa-228f473ec526 | -13.2986 | -51.7501 | 2026-09-16 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 4ec73dde-6d81-3f7e-ac99-980acaa05485 | -12.6625 | -50.8478 | 2026-09-16 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| a0352d40-2c6d-3d0e-a76e-c2f576953d38 | -3.1816 | -61.1045 | 2026-09-16 00:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 13968a13-604b-38f5-9ca2-a9cf9a75634b | -4.8782 | -42.7675 | 2026-09-16 00:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 79ed2bb0-a42d-3660-a757-1ea64514cf70 | -2.1051 | -52.0575 | 2026-09-16 00:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 91bc9229-096a-3066-817c-c7b0fa007aa1 | -10.7015 | -54.1663 | 2026-09-16 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f3cafcee-f650-3e5c-ba3b-8eba5761a99b | -2.1052 | -52.037 | 2026-09-16 00:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 99f490b9-f2b9-378c-bd21-15f146195695 | -5.1256 | -55.9352 | 2026-09-16 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a7a5f413-bad9-3a75-9cb3-2ecfd78d2801 | -9.7822 | -46.4876 | 2026-09-16 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 91d6a741-2b27-3d38-b363-a29f3a92efc9 | -5.7754 | -45.1053 | 2026-09-16 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 9ef74aeb-00fd-309d-af62-58d3afeb5f25 | -2.1051 | -52.0575 | 2026-09-16 00:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c6a2fc66-faef-31e4-b019-0ed63819fbb6 | -7.5608 | -62.33 | 2026-09-16 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4370d13a-2127-39b3-bc5d-56dc1cbc6cbf | -9.112 | -45.7294 | 2026-09-16 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 1deed043-0090-3f11-96c8-12f473315714 | -3.3232 | -47.1316 | 2026-09-16 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 30f68443-3665-343a-a801-128b2680e72f | -7.6327 | -67.1644 | 2026-09-16 00:10:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 9e3622e0-512a-3310-9007-4330095bbcde | -5.7754 | -45.1053 | 2026-09-16 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| c99f6eb4-2a4a-3e9d-a495-a67f65604b22 | -7.651 | -67.1824 | 2026-09-16 00:10:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 1fd2f811-b46c-3e19-b36a-6d6f9f3fb95d | -18.2257 | -41.2559 | 2026-09-16 00:10:00 | GOES-19 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 165.3 |
| 9d9aeceb-38ec-3ba2-afa7-194d800ae8cd | -5.1029 | -47.6157 | 2026-09-16 00:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 03a9c109-2a12-3f70-9bb5-0b918b79b227 | -11.5033 | -45.8396 | 2026-09-16 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d1f1e277-ade0-387e-8c06-5065ebfe90f2 | -5.7756 | -45.0826 | 2026-09-16 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 62b9aa79-59a9-3c77-8e27-6c0bc83cd193 | -4.2951 | -49.1234 | 2026-09-16 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| a0cc1cbe-27fc-316b-a2bb-5fe6e497e6ea | -9.1123 | -45.7067 | 2026-09-16 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 648f2ae5-ae82-38e4-ae81-71834e66d594 | -7.6511 | -67.164 | 2026-09-16 00:10:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 141.3 |
| d8cbd80e-c81f-339a-b7db-cf1e5871fad4 | -5.1215 | -47.6146 | 2026-09-16 00:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 53214f99-bd88-319d-a401-82d3cb03fc2b | -3.1634 | -61.1048 | 2026-09-16 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 827b4b52-fd0e-38e8-a75c-2ab0e79ddaba | -9.7322 | -64.9067 | 2026-09-16 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.4 |
| b9a19f9f-8d19-3107-85ff-3a3fbddbd75f | -9.3893 | -60.3022 | 2026-09-16 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 146.4 |
| fe2c2767-d10c-35e7-b41e-8f7afff80148 | -11.1401 | -40.4748 | 2026-09-16 00:10:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 65.7 |
| a8c2a707-e1b3-32ea-8b7c-33871c551141 | -3.1174 | -57.6779 | 2026-09-16 00:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 34bdcc4d-a6af-3ab1-9c39-52b344679b32 | -9.3892 | -60.3215 | 2026-09-16 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| e87fb172-7078-3fd9-acef-f79421408a5c | -9.0934 | -45.7088 | 2026-09-16 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| d49118d2-bc64-3d80-8088-05908e1c0ffe | -1.2907 | -55.7098 | 2026-09-16 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d2f1a1ba-94b4-3531-8153-deda7dc8d04d | -3.3806 | -50.8458 | 2026-09-16 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 0f683a24-31ef-31e6-a10a-d92bb13518ad | -18.6453 | -50.1845 | 2026-09-16 00:10:00 | GOES-19 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 120.4 |
| 30481124-d522-385d-bcec-93eb19eb8813 | -10.4695 | -44.9491 | 2026-09-16 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d8292555-62d9-3c25-b16b-f52837e473cd | -11.9906 | -52.4695 | 2026-09-16 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 2ae4aca5-0263-308e-a8f0-b98d70b6883d | -1.0365 | -53.7389 | 2026-09-16 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| ac080185-36d8-355c-b21a-fa8ade1decc5 | -12.6245 | -50.8311 | 2026-09-16 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| f267cf2b-a4a5-37e1-bdec-58f1e662b773 | -3.1816 | -61.1045 | 2026-09-16 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| b05a7475-ade9-35c4-acc4-b25e7d40ecfb | -2.6966 | -57.6084 | 2026-09-16 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 21ab420c-25ad-3d3e-a201-70ed2d0a2cc1 | -18.2265 | -41.2303 | 2026-09-16 00:10:00 | GOES-19 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 129.7 |
| 1e9527c1-0c96-361e-828f-68c4c2904930 | -5.144 | -55.9345 | 2026-09-16 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 9f7e75c7-445f-306c-88f6-b3721df4289e | -3.1816 | -61.1235 | 2026-09-16 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f6042993-8a5e-321c-b57e-083e0a79bb81 | -3.3231 | -47.1535 | 2026-09-16 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| af2e6ea9-bb30-3294-baca-f6c4bca2b82d | -3.1633 | -61.1238 | 2026-09-16 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| e1913011-fdbb-3722-89c3-81d49ba579c9 | -2.1052 | -52.037 | 2026-09-16 00:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 38df7918-c6a6-35e8-a213-ca54b127c477 | -12.6054 | -50.8334 | 2026-09-16 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 2edec199-2b52-33a4-a66c-7259b7baf52a | -1.0182 | -53.739 | 2026-09-16 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 9c699412-7d5e-3f35-89a5-49214d0ac4bb | -9.0931 | -45.7314 | 2026-09-16 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 3a77bece-ad1b-3fc6-9211-3d3e04b89a6a | -10.7015 | -54.1663 | 2026-09-16 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 198a0d86-7f0a-377a-b5e7-72632d6ee602 | -9.3893 | -60.3022 | 2026-09-16 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 98db86ad-4cf6-3409-8fca-56bf7fc61a29 | -3.1633 | -61.1238 | 2026-09-16 00:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 557817d3-317d-3725-9d81-20764e09afc0 | -1.2907 | -55.7098 | 2026-09-16 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 72cfc550-1d68-3784-a8c7-18830017e16f | -12.6433 | -50.8502 | 2026-09-16 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| a1579087-0ff2-30c5-a10a-02d81b1432a6 | -18.2257 | -41.2559 | 2026-09-16 00:20:00 | GOES-19 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 150.1 |
| e9baf44e-e7f5-3bfb-9f44-33ffc26d5ae6 | -11.9906 | -52.4695 | 2026-09-16 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| e90e585e-35a0-34b3-9ada-7a08690065e2 | -12.7521 | -51.2213 | 2026-09-16 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ee982bd8-5ed7-3890-a37f-8e51ac881418 | -7.6511 | -67.164 | 2026-09-16 00:20:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 71e31c21-6914-3d47-a35e-27882ff2a34a | -18.2265 | -41.2303 | 2026-09-16 00:20:00 | GOES-19 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 136.8 |
| d606b21a-e029-3fed-8d69-cdf96ce01d95 | -3.3806 | -50.8458 | 2026-09-16 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 033dd042-a799-39a4-b370-f7624e40f81c | -4.2951 | -49.1234 | 2026-09-16 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 816557dd-dae3-3406-9ae1-c83d76c67305 | -5.7756 | -45.0826 | 2026-09-16 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 1b6260b5-6a58-3d50-b64c-1142174e27b1 | -10.7015 | -54.1663 | 2026-09-16 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 98b53882-ab84-3b9d-bc4c-462cc3e03be3 | -12.6245 | -50.8311 | 2026-09-16 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |


[Clique aqui para ver as próximas entradas](README2.md)
