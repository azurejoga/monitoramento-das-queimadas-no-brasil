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

## Dados Diários - Página 174

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 601be6c1-d66d-3683-8e6e-1fcc16d40326 | -10.7603 | -53.9769 | 2026-08-28 19:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 61da957a-a9de-3b3d-a047-c99d6005a7d4 | -14.3376 | -51.702 | 2026-08-28 19:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 141.4 |
| be22181b-03e6-3872-849e-3feb01ef3669 | -7.9169 | -61.3671 | 2026-08-28 19:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 8fe1d117-9fe2-3f32-8b1a-95088052c171 | -8.5365 | -55.2826 | 2026-08-28 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 8f7322a4-21e3-3b56-a57a-4f032239d3c9 | -12.7797 | -44.2576 | 2026-08-28 19:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 185.6 |
| f00e5b2b-e0a4-3fa4-8fc1-c84f81517ef6 | -10.7407 | -54.0401 | 2026-08-28 19:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 521101e4-d944-3915-8588-9f1bd9b92f08 | -6.857 | -59.4371 | 2026-08-28 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 0853d0bf-bd23-3ad6-a1e9-f0902508b4a1 | -8.5971 | -54.7553 | 2026-08-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| fc39e523-8dab-3f40-b724-4f40dafd2adb | -4.1696 | -42.4346 | 2026-08-28 19:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 6ee9057c-f9ad-3e07-8b14-4ca14556b764 | -6.1102 | -57.8205 | 2026-08-28 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 7f14e732-25fe-33c3-80be-db741e51c2e1 | -7.3478 | -55.1744 | 2026-08-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 11d53ecd-d877-3903-888a-edff11eb0fd6 | -6.5322 | -55.2577 | 2026-08-28 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 9fb3595c-f7d3-3a84-bebe-e111b48cffcc | -6.5865 | -55.4346 | 2026-08-28 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 7acf9482-a89a-3c38-9f9a-fc93246ab960 | -9.2475 | -57.0894 | 2026-08-28 19:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| bf356c6c-ba8f-3c8d-a35e-f232dd2023c2 | -9.1711 | -49.9835 | 2026-08-28 19:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 164fad2e-bcf3-3281-9737-0e662923a939 | -9.9708 | -53.9419 | 2026-08-28 19:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 15b72bf1-565c-3fbc-a711-4ce585c505cf | -11.4968 | -45.1071 | 2026-08-28 19:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| e6b9cfa7-6fa5-3095-85be-ae4e2fbd4ead | -2.7304 | -47.0424 | 2026-08-28 19:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| aeebe5e1-8a76-33a7-b7e5-357a86cacbc3 | -10.3202 | -49.9782 | 2026-08-28 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| d07de00e-3014-3ab5-90c3-421ba80987f5 | -9.2477 | -57.0697 | 2026-08-28 19:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| e9a5b2c0-f18f-3c67-b86a-582c16b57193 | -8.0113 | -48.0161 | 2026-08-28 19:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 74b1b134-cf1c-3d7b-91e1-028833f3ee16 | -7.4734 | -61.4037 | 2026-08-28 19:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |
| e784e4dd-3b14-3e8e-ab2f-180026520f48 | -9.1739 | -56.9754 | 2026-08-28 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 57e3af95-dfc2-394f-9bab-844024aa7c16 | -6.8571 | -59.4179 | 2026-08-28 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 3acd347b-3561-3afa-ac87-42d3fd9d4789 | -14.3565 | -51.7208 | 2026-08-28 19:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 464.0 |
| d5f66145-d034-32cf-9b59-e451f1c23751 | -14.3759 | -51.7183 | 2026-08-28 19:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 229.8 |
| f9b5516f-d064-3bd5-b4d6-03ee21e5e659 | -14.9015 | -52.6055 | 2026-08-28 19:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 0d15e700-0077-3cab-bf16-8dff7963ed3e | -14.3569 | -51.6995 | 2026-08-28 19:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 558.4 |
| 2456847c-ff73-3c7d-92f0-9cbfd4df7d7c | -7.4953 | -55.2862 | 2026-08-28 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 152.1 |
| a8cdfbee-cb0f-30af-8eab-d4e5bba1dcf8 | -11.0247 | -49.6656 | 2026-08-28 19:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 08599d62-4a0c-3b57-89bb-16148a4aa0a7 | -8.1432 | -64.0053 | 2026-08-28 19:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 009a5d6a-cd41-363d-a8a9-791268172ac8 | -9.1714 | -59.5793 | 2026-08-28 19:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 8d40a105-5153-3e96-acca-e2d2495ec68c | -9.1978 | -61.0809 | 2026-08-28 19:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| bddd5e13-fb24-3a78-84ae-07519895a0ae | -10.3391 | -49.9762 | 2026-08-28 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| ab961565-3e6d-389e-9ae3-1e7558f5d4ea | -6.8569 | -59.4564 | 2026-08-28 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 883c7240-0f86-3fcc-8aef-a29ec62204e6 | -7.529 | -61.3635 | 2026-08-28 19:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 171.5 |
| 301412a8-6e9d-3d41-872c-8d303436c9e7 | -6.9521 | -58.9506 | 2026-08-28 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.3 |
| ae1e0f93-6584-31e9-9373-070589fad572 | -6.8756 | -59.4171 | 2026-08-28 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 4c7311fa-ceeb-31a0-b72f-687d2c7531b5 | -3.8947 | -60.9399 | 2026-08-28 19:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a23663f0-5821-309f-b668-b62d64e10c5e | -8.0548 | -45.8616 | 2026-08-28 19:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| eabaf45a-ab58-3b88-bda8-99cc74f09c31 | -8.0301 | -48.0145 | 2026-08-28 19:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 7956e9f6-af46-36ba-8805-81c8ed1b934d | -6.8955 | -43.6601 | 2026-08-28 19:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 496aacc1-fba6-3c8a-a213-7e32044d3383 | -4.3022 | -59.4634 | 2026-08-28 19:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 7d30aad3-a0cd-33df-9c79-81dc45541130 | -10.3205 | -49.9567 | 2026-08-28 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 4d422bd9-f36c-3ba9-b066-9abecb2239fa | -8.6012 | -70.2192 | 2026-08-28 19:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 0c597894-0292-3619-a5b3-31809d27d0dc | -4.924 | -55.7645 | 2026-08-28 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| d015e530-7a92-339c-90b3-28deb8e02600 | -8.5783 | -54.7768 | 2026-08-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 43e07bbe-e0d4-3956-bbf1-adf6c5ed92c3 | -6.9336 | -58.9514 | 2026-08-28 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 153.4 |
| b35a6bce-e8c8-3a84-8e4d-9906a9d0264e | -6.7513 | -55.6853 | 2026-08-28 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d2967e64-fed8-3703-9bc2-c9b3c997a778 | -14.8817 | -52.6293 | 2026-08-28 19:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 3d0854c3-9e5b-3260-aaa2-0ed1981da8f3 | -9.02 | -57.5377 | 2026-08-28 19:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 21aa6885-b940-34e1-b2dd-5757dc0b5e72 | -6.0005 | -57.6689 | 2026-08-28 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ea468ec4-68b1-3077-b767-9f7aa7db6fe4 | -8.5969 | -54.7755 | 2026-08-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 357d8d4d-bcbd-3d0c-9b00-c8eae97d7860 | -9.7874 | -43.5742 | 2026-08-28 19:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| efbff0b1-0d30-3b84-beed-157b058acd7f | -7.5289 | -61.3825 | 2026-08-28 19:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 8491a791-0c6c-3b27-852d-d6ffcefe60c1 | -6.8357 | -59.9571 | 2026-08-28 19:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 45e9a8af-42ba-3469-af8d-c69a914b6f36 | -8.5968 | -54.7957 | 2026-08-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 3d403cfd-0a63-3022-af5f-dcf29811388d | -9.1976 | -61.1 | 2026-08-28 19:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 4caaa624-9f61-3f8f-8149-88e141674e0f | -3.1815 | -61.1613 | 2026-08-28 19:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 6f6fcb71-6d3c-388a-82a3-7590acf5b955 | -6.894 | -59.4164 | 2026-08-28 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 78aa72f6-ca01-3c96-9cb0-85e035c9fcd2 | -6.5323 | -55.2378 | 2026-08-28 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 8edcde2c-139b-3420-8ecc-e37b7f1255c5 | -13.471 | -57.0373 | 2026-08-28 19:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 7cde9f40-9ad3-3fa8-b04b-256dd37f2888 | -14.9193 | -56.3237 | 2026-08-28 19:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 26b3c87c-60ba-3084-84ee-e7f4016948b2 | -7.5104 | -61.3832 | 2026-08-28 19:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| dc6c0ad4-6be8-331f-b528-580748afa28b | -9.2285 | -59.4017 | 2026-08-28 19:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| a9125993-69a6-3aad-93c1-37e6bfb68cc0 | -14.8821 | -52.608 | 2026-08-28 19:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 55be51ef-5d1c-3f57-a8b5-f577ecc112f4 | -14.1835 | -52.8456 | 2026-08-28 19:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 261c37dd-d9b6-349c-b8ed-38758d1bb174 | -11.7167 | -54.5244 | 2026-08-28 19:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 125.1 |
| de180b09-8a87-3e40-b1be-7068ea40cd22 | -14.1784 | -48.7703 | 2026-08-28 19:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 140.4 |
| c4183a64-5d73-3988-97ec-0ae1f6aed47f | -13.5991 | -45.772 | 2026-08-28 19:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| b86e9628-4157-33ae-af85-c5f0b0a00ed5 | -16.177 | -45.6265 | 2026-08-28 19:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 83.2 |
| e7c09305-f754-399d-8a00-05f2d69f7640 | -9.1525 | -49.9639 | 2026-08-28 19:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 119df3a8-2746-3cd4-ac22-23edae23356e | -11.0247 | -49.6656 | 2026-08-28 19:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| fc945f48-f855-380f-9089-6484e1b92dfc | -6.1473 | -57.78 | 2026-08-28 19:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 67125240-35f6-38f4-97a6-b021d43d71f0 | -6.8569 | -59.4564 | 2026-08-28 19:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 4bf47d52-08e2-3c65-95ce-da76a3b5f4f2 | -14.3372 | -51.7234 | 2026-08-28 19:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| d65909b1-4f98-3a82-b885-838f51736fda | -3.8947 | -60.9399 | 2026-08-28 19:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9e29bcd4-ed01-3591-b9ec-ea173788c7d3 | -14.3565 | -51.7208 | 2026-08-28 19:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 570.9 |
| 86092aa7-479f-34b0-94c1-2f143cc1fe10 | -6.7647 | -59.4601 | 2026-08-28 19:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| a145f050-abb3-3bef-977f-150a4aeb285f | -14.3376 | -51.702 | 2026-08-28 19:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 97b413e0-3a4a-306b-91d4-6e68f08638a0 | -8.6012 | -70.2192 | 2026-08-28 19:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 5ef118af-e697-311a-bcbf-207f370dbfff | -4.3022 | -59.4634 | 2026-08-28 19:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b2a1f77e-7afb-3a61-bd48-39265d19d1aa | -4.1696 | -42.4346 | 2026-08-28 19:50:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 47679759-f0fd-358c-8fde-d8183794bdd8 | -2.7303 | -47.0644 | 2026-08-28 19:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 495926f5-600d-3897-986e-246736b6f527 | -14.1835 | -52.8456 | 2026-08-28 19:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 8967783c-923c-3627-a905-065b8ac2a693 | -14.1838 | -52.8245 | 2026-08-28 19:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| f334c12a-c2c5-3334-92c7-00fc107356fd | -6.8358 | -59.9379 | 2026-08-28 19:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| f4f9d7d8-8d94-371c-ad59-2e90e086677b | -12.7608 | -44.2373 | 2026-08-28 19:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 5e606b95-e060-3497-a26d-79938315de9f | -9.0198 | -57.5574 | 2026-08-28 19:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 165.4 |
| 186024fb-b4e5-3c00-a44b-a5531e35d290 | -14.9015 | -52.6055 | 2026-08-28 19:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 9cc63660-dcd8-3ddf-8967-eebe335b3bb5 | -9.2285 | -59.4017 | 2026-08-28 19:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| cce9242d-b00c-3489-9848-29d7c177b6b4 | -6.1657 | -57.7793 | 2026-08-28 19:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 192.4 |
| d30cd7e0-3f71-3503-aa09-3d355f238c18 | -9.1978 | -61.0809 | 2026-08-28 19:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 7e67c7ab-1d3c-3a47-8471-00502636bc7b | -8.0113 | -48.0161 | 2026-08-28 19:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 86045c93-9068-33b8-b51f-775f4c5c3051 | -9.1739 | -56.9754 | 2026-08-28 19:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| aec05af4-7f9e-39cc-bcb1-98be6fa246fe | -2.7304 | -47.0424 | 2026-08-28 19:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 175.5 |
| 0ac05420-0ce0-3a42-8085-af49e6dcb82d | -6.857 | -59.4371 | 2026-08-28 19:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 21a83abd-4a84-353e-aaa9-c137aa68595a | -6.9521 | -58.9506 | 2026-08-28 19:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| cd44310e-705d-3f74-8730-4287aaa339fa | -11.4968 | -45.1071 | 2026-08-28 19:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d266f063-209b-36d2-a4d6-feb231e47440 | -14.9791 | -52.5951 | 2026-08-28 19:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |


[Clique aqui para ver as próximas entradas](README175.md)
