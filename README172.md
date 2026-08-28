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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c6c6e2f-fb1a-31f7-b2d0-d5a493c0f88c | -7.65949 | -72.48829 | 2026-08-28 19:10:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 88c21d93-028a-3ee1-b54d-d4af4a394bc9 | -7.58886 | -73.26421 | 2026-08-28 19:10:00 | NPP-375 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ed855de2-d228-37fe-8a62-3773ab15652f | -6.92771 | -69.98894 | 2026-08-28 19:10:00 | NPP-375 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| a9da41fb-b19c-39cd-8945-783030dfc8b3 | -9.47 | -45.68 | 2026-08-28 19:15:00 | MSG-03 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 05a6acb2-3e3f-3ee8-af6f-93b389063dc0 | -9.5 | -45.64 | 2026-08-28 19:15:00 | MSG-03 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 49a543c0-53d1-3cdb-b8c0-079e8c90e149 | -12.77 | -44.29 | 2026-08-28 19:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8183cf07-355c-36df-a577-8e54bf0bef7b | -11.04 | -57.19 | 2026-08-28 19:15:00 | MSG-03 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 035502a2-2b60-3f87-804e-629724ff2fc4 | -9.5 | -45.69 | 2026-08-28 19:15:00 | MSG-03 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d297f0aa-b7cd-3268-b267-5b33fedcf6b0 | -12.36 | -50.59 | 2026-08-28 19:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a020b80c-d2cc-3d86-bfdc-d6de7694e928 | -14.88 | -52.63 | 2026-08-28 19:15:00 | MSG-03 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 714ca8a2-ae35-3d3b-9e0f-6ff15eabc466 | -6.9335 | -58.9707 | 2026-08-28 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e111f23e-7d4d-3c85-9969-8fc1b695dd22 | -9.2477 | -57.0697 | 2026-08-28 19:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d8811c9f-aa1d-3608-9123-a1ebdd39dd96 | -8.5971 | -54.7553 | 2026-08-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 140.6 |
| abc0d062-1bfd-37ff-9701-1447620a3132 | -7.5289 | -61.3825 | 2026-08-28 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 772bb03c-8a69-3ddd-a2b4-27f4ee69812f | -9.191 | -59.4425 | 2026-08-28 19:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 1ad1aa90-d30b-38ce-ac36-c68bdbffae98 | -6.5865 | -55.4346 | 2026-08-28 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 039f74e7-24f3-3535-9add-ee7359bc3504 | -9.2285 | -59.4017 | 2026-08-28 19:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 7a2c0388-a4fa-3c42-88e3-d4050253d9c0 | -11.0247 | -49.6656 | 2026-08-28 19:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c24991c3-176e-3f52-8903-106ec39a6c9d | -6.4908 | -53.2629 | 2026-08-28 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 63f384e1-19a7-34e6-bfe7-a3e3a7a90599 | -10.3013 | -49.9801 | 2026-08-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 5242e01d-64bd-37c8-a648-b443e7d80c9d | -9.9708 | -53.9419 | 2026-08-28 19:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 171.1 |
| f3d3593f-d86f-330f-a1c1-6c91ff883fd1 | -10.3391 | -49.9762 | 2026-08-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 6e0b8df0-5a71-3f72-8cc5-3948818f3564 | -6.5323 | -55.2378 | 2026-08-28 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| a64df32f-e597-38f6-b8c7-27b3560dfdf1 | -7.0289 | -55.6909 | 2026-08-28 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 844af303-8e6c-313b-a0b9-00d15d2fa2d3 | -14.9193 | -56.3237 | 2026-08-28 19:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 6a755fc8-1eca-3503-9b4c-a6888c04a4d7 | -6.8941 | -59.3971 | 2026-08-28 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 3cff595b-80f7-3e51-879f-d1dbde93b757 | -4.3022 | -59.4634 | 2026-08-28 19:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 588d2d1a-4b90-3add-a799-54277d3fe37a | -9.1525 | -49.9639 | 2026-08-28 19:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 04eab88b-a782-3f4c-a683-1927b0479cdd | -8.0548 | -45.8616 | 2026-08-28 19:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| d7866f7a-dca3-3d6b-92cf-735be3b6c432 | -6.9336 | -58.9514 | 2026-08-28 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 10bbc5e4-edac-3da1-8298-c2abae591200 | -6.894 | -59.4164 | 2026-08-28 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| a42063e1-51db-3a5d-bc2b-b8442d1afbec | -6.1473 | -57.78 | 2026-08-28 19:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4c712101-614f-319c-9b8d-13719dea8ff8 | -9.1909 | -59.4619 | 2026-08-28 19:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| a8bbb1d7-a0e2-38a8-9db4-87b9f370b3ce | -10.3205 | -49.9567 | 2026-08-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 248a26a3-cecc-334e-856c-f6f988a9bc90 | -6.8384 | -59.4571 | 2026-08-28 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9d904472-1994-3a80-81fe-b4fdeec11ead | -6.8569 | -59.4564 | 2026-08-28 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 18c67c55-ddc7-3ef9-aca4-d94aa3a38984 | -13.4707 | -57.0574 | 2026-08-28 19:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 73729e0a-6f35-3722-b097-102190059630 | -4.1696 | -42.4346 | 2026-08-28 19:20:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 389fede5-e097-3a37-a001-2d283716100f | -7.4734 | -61.4037 | 2026-08-28 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 2945e239-06cd-30b6-ab21-4fc81edba70d | -6.8756 | -59.4171 | 2026-08-28 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a33ab9e8-7c47-3d73-a4b1-0a0ab92bbbeb | -12.9244 | -59.8843 | 2026-08-28 19:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 04206959-67bd-35a7-a789-9b3be8ab53df | -13.5991 | -45.772 | 2026-08-28 19:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 96c1fc83-4356-3a9d-90ec-c7f78878d861 | -12.3811 | -48.1877 | 2026-08-28 19:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| cf19ab06-561b-3699-b3ee-5bf27c760241 | -7.4735 | -61.3846 | 2026-08-28 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| fa8d0869-f57c-305d-9e0a-f8a34f3c10cb | -6.7514 | -55.6654 | 2026-08-28 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 276.5 |
| a1650d60-2ce8-3bb5-9f61-d808e3cab8dc | -8.8576 | -71.3159 | 2026-08-28 19:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 54.4 |
| acd880aa-21cc-3b29-97db-e9da6a19e9c4 | -9.1895 | -59.6364 | 2026-08-28 19:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 6f6ec5b7-603e-3183-ab8c-7fbfd8d3cb23 | -4.924 | -55.7645 | 2026-08-28 19:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| edbd7136-5d59-347e-b6df-dd9b312f84c2 | -11.2128 | -53.9976 | 2026-08-28 19:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 0994d2f7-a4cd-3726-aa46-f2b80152d75f | -7.5104 | -61.3832 | 2026-08-28 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 0f2641b0-5c8f-3f85-9ac9-8a731769f0cb | -13.8752 | -54.1153 | 2026-08-28 19:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 8b894fca-981f-3a66-b92f-c01190e013cc | -14.1784 | -48.7703 | 2026-08-28 19:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| fb581420-3f21-3483-9a12-f5e35a067f62 | -9.1711 | -49.9835 | 2026-08-28 19:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d2d4ec3d-1f7b-3622-ac0c-28764ef83e04 | -7.5105 | -61.3642 | 2026-08-28 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 3d1a610e-935a-3da4-9242-a696e211dac2 | -6.7698 | -55.6844 | 2026-08-28 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| abed7550-bf3d-3402-b377-6f71cf942016 | -9.0012 | -57.5585 | 2026-08-28 19:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a66a9f86-f728-3935-994c-a4f826884f73 | -9.4825 | -66.6347 | 2026-08-28 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 24a7bdb9-6f07-3188-b3e7-28846ac5c5ce | -4.3021 | -59.4826 | 2026-08-28 19:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 7169c3bd-1850-3a8a-8af0-3236a39cc184 | -11.6212 | -54.5947 | 2026-08-28 19:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 7d6d3785-1037-3203-bf49-7edf75e0fdcf | -6.857 | -59.4371 | 2026-08-28 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 0010ad29-1651-3eed-861b-ccfe0007913c | -6.9521 | -58.9506 | 2026-08-28 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.4 |
| eceb3e68-0d18-382c-9f5c-34750a266ce1 | -7.5845 | -61.3423 | 2026-08-28 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 263.7 |
| 074fa64e-0a41-3db1-848c-6c6471699b94 | -14.9 | -56.3257 | 2026-08-28 19:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 3e5e45e7-32ee-3c93-a99d-3850464bb654 | -11.4968 | -45.1071 | 2026-08-28 19:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 35228633-eb61-30bd-86f3-4bc37ae929f2 | -9.7874 | -43.5742 | 2026-08-28 19:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 052aa288-83fc-3e7e-9552-0e4dbe045458 | -6.1657 | -57.7793 | 2026-08-28 19:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 162.9 |
| bea3847e-01ae-3cda-b99a-af04edb0473b | -14.1645 | -52.8269 | 2026-08-28 19:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 0001e4c0-579f-3b33-a450-ef21e71b95e9 | -7.3478 | -55.1744 | 2026-08-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| a03f5801-0148-3e90-906a-054f391a91ea | -11.7598 | -47.6277 | 2026-08-28 19:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f94508fc-020e-33e5-a380-dfeeaf6cfae5 | -8.0739 | -45.8372 | 2026-08-28 19:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 590c5615-2181-3322-8fa9-2a4b92a7f7df | -9.02 | -57.5377 | 2026-08-28 19:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 9a3473fb-b85d-3917-889e-b912b436af64 | -7.4953 | -55.2862 | 2026-08-28 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 159.9 |
| d67cab66-e146-3931-baaf-309f1e34912c | -8.8184 | -49.6308 | 2026-08-28 19:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 5b5d9cff-be80-35be-b2d9-bde033bd868a | -10.7407 | -54.0401 | 2026-08-28 19:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| fb646568-3f4d-3d28-ad34-aa46ba918c9a | -14.1835 | -52.8456 | 2026-08-28 19:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 38f07928-09c8-380d-b5df-27345310f561 | -13.471 | -57.0373 | 2026-08-28 19:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| daeb1a6a-9753-36ed-9269-79e10db4b5a1 | -9.8065 | -43.5717 | 2026-08-28 19:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| ab87c0b5-ad12-35e8-a3ba-f4905091b1f9 | -6.0005 | -57.6689 | 2026-08-28 19:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 2845008c-7eab-3feb-ae0c-8df4df98829c | -10.3202 | -49.9782 | 2026-08-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| cb001e56-8c2e-31b3-8ff9-c5fcac977424 | -8.1432 | -64.0053 | 2026-08-28 19:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 8015c56d-6d46-3fe7-94a7-dd698037ee62 | -8.5781 | -54.797 | 2026-08-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 23cf3de8-daf6-3d68-b7d9-09a256fc00c3 | -3.2361 | -61.2359 | 2026-08-28 19:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| bf028ba4-82cf-3588-b7c5-da281bd7ad83 | -3.8947 | -60.9399 | 2026-08-28 19:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 37e28362-893f-3999-86ea-2474efb9e3bf | -8.5365 | -55.2826 | 2026-08-28 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 7ec9fff7-270e-3fd2-9bde-6d729be2b3ac | -8.5783 | -54.7768 | 2026-08-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 8c1e7fa4-6f13-3f61-accf-a7cc2ffd060f | -13.4901 | -57.0355 | 2026-08-28 19:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 17304128-7526-362c-bfc0-15dc03bd4bda | -4.3205 | -59.4821 | 2026-08-28 19:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 360ae811-1419-318d-a9da-ae2e16317244 | -6.7513 | -55.6853 | 2026-08-28 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 6d7264cb-b878-3db0-88c4-3021553f1189 | -7.3663 | -55.1734 | 2026-08-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 1025149f-4864-3b90-97fb-55fd0ab81a0c | -7.5478 | -61.3056 | 2026-08-28 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 155.9 |
| c4d889f3-6573-3142-87e2-c3bae9b28cdd | -7.5475 | -61.3627 | 2026-08-28 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 123.5 |
| e41c356e-e014-3dd1-88eb-9652a5ac696c | -8.5969 | -54.7755 | 2026-08-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 206.8 |
| 00eebb83-bc17-3607-9ef4-5c25395318c4 | -11.2314 | -54.0164 | 2026-08-28 19:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 4159e650-8409-3778-9760-2e6569913418 | -8.0551 | -45.839 | 2026-08-28 19:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 40d70360-7c85-3fdb-82c9-3d73535c7b05 | -8.5785 | -54.7566 | 2026-08-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 7405bf55-2d7b-3a74-8163-c092e2e2fee6 | -10.9377 | -46.6168 | 2026-08-28 19:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 5c2af930-d146-395c-ac05-4b6ae3ffe7b7 | -7.529 | -61.3635 | 2026-08-28 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 251.8 |
| 4ca2683f-7f2a-3426-8700-a04ddb2aace1 | -8.5975 | -54.715 | 2026-08-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 71dec1e5-5243-37fe-a037-c925341e7fcd | -9.6865 | -46.5658 | 2026-08-28 19:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| ecb71ce7-47d3-34d0-b1a7-e2c2ae18522d | -16.177 | -45.6265 | 2026-08-28 19:30:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |


[Clique aqui para ver as próximas entradas](README173.md)
