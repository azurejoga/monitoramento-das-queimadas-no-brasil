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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8028b436-414e-37dd-a28c-f0867a68e79b | -12.44592 | -63.92516 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51273e57-f356-3025-8d25-3be7349330fa | -8.384 | -70.75174 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac1674f2-9536-3265-8531-31e714d68ea7 | -8.69666 | -71.03014 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1e948fe-2011-3857-9835-dc273a9819db | -7.60584 | -70.19986 | 2025-09-01 05:53:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a375388-1987-3eae-bbe7-5bce7b53e9cc | -7.7999 | -71.93479 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1869b121-5cbb-3b5b-ba20-848d5ee8a206 | -9.07179 | -65.45322 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5a0c04b-bb4f-3bd8-a655-5e2bbd1b96ad | -12.43437 | -63.92347 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d315fddb-7a5f-362f-80e2-a2733016972e | -7.46363 | -70.13148 | 2025-09-01 05:53:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 198434d5-84c9-340b-8184-8654c57c2d76 | -9.34467 | -65.42023 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2c02de9-8190-345f-8430-b1b8db563193 | -9.27719 | -67.64865 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13589df8-8ce7-399d-b0d8-2b73c38a79f2 | -9.13787 | -65.83942 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19f56285-e4c8-3d75-af06-3a88f018e09e | -7.89973 | -63.01125 | 2025-09-01 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23fe9e12-fdd5-391d-a079-df7ab1fe8425 | -8.36115 | -70.7524 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfd50fe7-8460-34ec-bc84-2eed3e1b8cf8 | -8.67987 | -62.4051 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3002782f-f7d8-3d58-a46c-6ab9f5331cf6 | -8.76655 | -61.42907 | 2025-09-01 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bc1ce89-0c5e-369c-a969-16ded33c05b7 | -8.65519 | -62.92256 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd4d2bf3-f6e8-3651-89c7-6088539ff955 | -14.31723 | -60.34844 | 2025-09-01 05:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d59d242-a29e-3c32-88ed-ebf1793ccbe2 | -9.13731 | -65.8431 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0eab3eb9-224f-367d-b0de-86e71c3bed60 | -11.51776 | -54.46984 | 2025-09-01 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc959554-dd33-3833-8a7f-7bf2e8c75fb7 | -9.66704 | -68.97243 | 2025-09-01 05:53:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8797715-12d3-3947-9e12-8c3d5dc0e9f7 | -11.65621 | -57.35817 | 2025-09-01 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 021b9b0e-7bf1-3daf-a3bf-9fba8d7b7811 | -12.4337 | -63.9283 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a97e3fcd-ba7b-3350-9896-b2dfce53a5ba | -8.65635 | -62.83236 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04baac99-e988-34bf-8f68-c1df9242dd92 | -8.73724 | -69.60168 | 2025-09-01 05:53:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd8dc1e8-5c33-3a2d-a651-d8ba6a21b4df | -9.27387 | -67.64812 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c460601f-cc28-34a2-b73f-3bace5f20ca1 | -9.06722 | -65.43708 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b70505e-96c7-3728-a6db-70b77d32edf1 | -9.86361 | -65.03255 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93096d2f-bb76-3c25-b152-1dc87bcd3653 | -8.72311 | -62.42655 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1a25189-28c9-3ccd-83c5-97614eb07771 | -9.69046 | -65.01177 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af4ea88e-ff4d-3797-b3a9-b8e2dfa0a617 | -9.13972 | -65.82834 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76056a41-53bb-3891-ab80-443abb46a701 | -9.11134 | -65.76359 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fb1567d-8488-3434-a5a7-9c34f1f07c54 | -10.5001 | -68.10822 | 2025-09-01 05:53:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8075b5fc-0516-34c1-8ca5-3f7933a7b4bc | -8.6639 | -70.99714 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 368d780f-6ae7-3a24-8bae-1baa9f45a1d8 | -7.4616 | -70.14394 | 2025-09-01 05:53:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db871f28-c4c5-377f-b848-2e46224a88d8 | -8.88528 | -62.38889 | 2025-09-01 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75ef8f7b-0365-3909-8879-e15d06702dad | -8.86764 | -71.27888 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 715eae4a-211e-3511-bcfa-c3b738bea65f | -12.4491 | -63.93056 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c7ab2da-be3a-365b-ae47-1227dde1d895 | -9.02422 | -65.69402 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b8bfa47-9630-3656-b5c5-c16670ab789b | -10.08352 | -68.46811 | 2025-09-01 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a1f7df7-15b1-3a52-8a3e-7d73decfa78b | -8.97053 | -65.97454 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53b360bb-83f1-32bc-b859-fef3b010aca7 | -10.88063 | -55.76043 | 2025-09-01 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d20a13c6-2ae6-3b7d-8490-e5bad3aa5fd4 | -8.51948 | -72.69498 | 2025-09-01 05:53:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66137f59-0a6b-3f77-b852-acfecfe6fe5f | -9.1753 | -67.56419 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 454b46f5-e12e-3a79-beba-f5c5691949dc | -12.44112 | -63.9227 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e127d2a8-578c-3e59-82c7-63ebbb7158e4 | -10.84768 | -55.75421 | 2025-09-01 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f630dbb-4413-3cbc-971b-d15d61b705e3 | -8.75854 | -61.42378 | 2025-09-01 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da405ea8-b82d-3c5f-bcab-f997988818da | -9.95228 | -66.87509 | 2025-09-01 05:53:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e56be6e6-cebc-3b8b-af0f-b88b13899691 | -8.55353 | -63.01422 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bb5f4f6-3e69-3fd4-9d7d-755c2d3427d5 | -8.64688 | -67.2473 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8079ca41-1508-34b5-9d5b-27620f413c1f | -8.97165 | -65.96727 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1f121a0-d3c1-3d1e-9088-2d2d5f468ec5 | -8.24317 | -72.82005 | 2025-09-01 05:53:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5452386-a781-30d3-932c-e9857497725e | -9.27054 | -67.64759 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 867fa4f4-cf61-325d-9c48-3edb2f89905a | -8.50985 | -67.12545 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46899ba5-6f8b-3c47-a6b4-5a1feb2a8dfc | -9.13122 | -65.54234 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf6a04b4-2485-3b93-9998-75743b21d316 | -10.12022 | -68.28152 | 2025-09-01 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35736fba-453d-37dd-b54d-9fff650dc6cb | -9.07237 | -65.44946 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3e2f45f-85af-390b-86ac-4fd9f1b75386 | -10.09356 | -68.46974 | 2025-09-01 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1a9fbdc-ed9a-316b-b5fc-3e418ea8549b | -9.28107 | -67.64569 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c368ab4-d3af-3429-9685-87bfb4a5378b | -14.3122 | -60.34759 | 2025-09-01 05:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dfd8ed23-8b7b-3c51-91f2-93e3729507d0 | -9.66365 | -68.97187 | 2025-09-01 05:53:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a4cc200-ea82-3b77-b991-c6f0816f5430 | -9.06971 | -66.07866 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00227679-e1f3-314c-a807-437d7bbc5392 | -9.13405 | -65.8425 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2aaa9ee7-c31f-3439-9d5d-ce1774a3cec1 | -8.76112 | -61.43651 | 2025-09-01 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bab4de42-b991-3830-ba15-0b1d851904b2 | -8.65447 | -62.92744 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0b16e25-f1ba-3458-9374-cf4c2ce0828b | -8.72474 | -62.41521 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 445382a4-2c00-315f-bc06-3c4e4288f00f | -9.11167 | -61.20459 | 2025-09-01 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 581b1082-d93d-37c6-b4d4-d3966c6d1ba6 | -8.84667 | -64.14355 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90bd1e86-8a93-31f0-be50-73d3ff24b15e | -8.67585 | -62.40454 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da08b90d-0476-3a45-8412-c1eef362cbb7 | -9.87891 | -65.02679 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c537ca5f-3ac4-39a5-9831-49b510cd595c | -8.64534 | -62.82567 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c354216-db42-3d29-ba18-1caafc8b77ba | -8.65707 | -62.82742 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7981591-44f9-3692-8601-e5c0d8ae1fba | -8.66685 | -62.92427 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b66b5ea3-145e-336d-a934-027ce307ff97 | -8.6559 | -62.91768 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9b9c72a-eecb-319f-a154-ef70b5fa37c3 | -9.69459 | -65.00836 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61fa234c-79a0-3afb-bdee-cee53eb8e01d | -8.76283 | -61.4244 | 2025-09-01 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ff3347d-21eb-3d43-a8b6-b352fd9ab3c0 | -8.45909 | -70.19203 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6220d449-4470-3f03-b484-682d41d6179e | -8.96826 | -65.96674 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 952004e5-de49-33b9-969b-000d3a577967 | -9.12435 | -65.54128 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a745147e-b48b-32b2-97d6-64a76fbf6c42 | -8.84686 | -70.84485 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71da8065-dc98-31ff-9f88-9f0f769847b3 | -8.96432 | -65.96985 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33de5ee3-3c8d-33b4-addb-e8e984fa3dbb | -9.83127 | -65.05593 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e33ad79-dce3-373d-8ad5-65558b173050 | -16.20408 | -55.95151 | 2025-09-01 05:53:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9e56a915-423d-3bf0-a692-bdcf3d195f84 | -9.13564 | -65.8541 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edc471e3-441c-3356-935c-726d16e814c2 | -8.8424 | -64.14722 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae76774d-a61f-3142-8b84-9fa442630541 | -9.35044 | -65.42888 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b5871e7-e1eb-3602-be19-41e3b70022ba | -12.44977 | -63.92573 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7138e240-d724-36d5-92c7-a8f4454bc6f2 | -8.67027 | -63.85767 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54328e3e-d4c1-3e50-98c7-01ce5e7a24c3 | -10.09021 | -68.4692 | 2025-09-01 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a5fac9e-13a8-37fc-81cd-400011c3441d | -10.17768 | -68.15699 | 2025-09-01 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 62e9c683-9d29-3c64-829b-e25778080e19 | -11.51998 | -54.47223 | 2025-09-01 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3ec21b5-92cb-36ad-8310-52a687d8b35a | -9.66306 | -68.97551 | 2025-09-01 05:53:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d4b417f-a437-3243-b4f1-a50d9d1b6d12 | -8.90603 | -64.46543 | 2025-09-01 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdba7721-8a9f-3ec1-b091-833d687b9698 | -9.64824 | -63.11505 | 2025-09-01 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b523c6bf-0a00-3ea0-bc93-2e94da9eaea5 | -9.13408 | -65.54661 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43ec8b38-23a3-3c18-9fba-13023a8ba8a5 | -9.72212 | -64.53646 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07275898-8710-3226-a37b-808c933c5c2b | -6.97456 | -71.74667 | 2025-09-01 05:53:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c04ae460-b05c-386b-abdc-fd8c296b9918 | -8.65907 | -62.92313 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e39e02a-46c9-3144-8730-71d61a383f2d | -10.09078 | -68.46565 | 2025-09-01 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fc7cce5-9d73-3a88-98a6-2c5224c8f187 | -7.81012 | -71.94722 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92e2cadc-49ca-33c6-874a-fd4aeb09ae96 | -8.50875 | -67.13243 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README90.md)
