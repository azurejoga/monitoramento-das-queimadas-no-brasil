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
| 909ed1f0-e009-348e-99c4-4179f96a43c8 | -16.75707 | -50.69239 | 2025-11-19 04:53:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2453cb65-1990-393c-accd-05340b2e2579 | -10.30237 | -57.13699 | 2025-11-19 04:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d6978ee-f6ac-31c7-ad16-8be2c607b62c | -6.34604 | -44.22424 | 2025-11-19 04:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 194ae920-9dbe-3a14-805a-768a17e12f77 | -10.10175 | -47.88948 | 2025-11-19 04:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d10bd83-a870-33f4-968c-33b4751906f6 | -10.06871 | -47.91243 | 2025-11-19 04:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f457431-cab7-37c6-8974-d9866f48fbb4 | -10.0542 | -54.34759 | 2025-11-19 04:53:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3ea241f-56d1-3188-95f8-ca6cc03c67aa | -11.04525 | -47.6107 | 2025-11-19 04:53:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2981b68e-f734-3974-86fb-099050a75de9 | -9.38374 | -48.43196 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a874d66d-1d0e-3ec6-bace-47cc2072ab9a | -10.41015 | -48.83239 | 2025-11-19 04:53:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1ea52ff-1246-3042-ba69-25e64bdbc0f9 | -16.65579 | -54.5801 | 2025-11-19 04:53:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfe0c053-e346-3c9a-aaa9-cdc96f0bd42b | -10.06508 | -47.90798 | 2025-11-19 04:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f880fb6e-8dcc-3047-87d4-b15dcab3b761 | -9.39315 | -48.45103 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b41e1e7-758c-3de0-bb02-4ddbea2dad3d | -11.61503 | -43.90364 | 2025-11-19 04:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c57f3bc-7e18-3b5c-8243-49ab63791c6b | -10.92067 | -48.66867 | 2025-11-19 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9136af97-e9c8-3cb5-8756-4a0cc903d845 | -11.66809 | -47.97342 | 2025-11-19 04:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0429ad5-324d-3929-bf2c-aa9312f122a9 | -9.35661 | -50.74234 | 2025-11-19 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5347f826-4b6c-326d-bd4c-e013c4c4386a | -12.30928 | -47.91117 | 2025-11-19 04:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4d9161a-6cdd-3d3f-9dde-fccf45c5cebd | -8.39085 | -44.06347 | 2025-11-19 04:53:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89f44c30-d48e-3be6-ba22-e9eb97dfc4b2 | -10.35124 | -48.90674 | 2025-11-19 04:53:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 817e56f5-a74a-3be6-a597-d22321010d1a | -5.45798 | -50.74694 | 2025-11-19 04:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67d7bc3a-1341-35ba-beba-9f17d1b9ecd2 | -8.87848 | -47.33241 | 2025-11-19 04:53:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9989d35-737a-3461-acd0-b22839ff3973 | -16.15801 | -54.59348 | 2025-11-19 04:53:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15bfa28a-d3ec-3300-9363-705674e1d9ba | -7.78836 | -49.61685 | 2025-11-19 04:53:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8de47e6-d6db-3cd3-b2f9-d451406eed7c | -5.01069 | -50.91576 | 2025-11-19 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2da67faf-86db-35ff-a207-e156732cd100 | -10.09909 | -49.58639 | 2025-11-19 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b616a857-f7f9-389d-9e01-d3803116cbeb | -11.66864 | -47.9694 | 2025-11-19 04:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b465c988-c443-3afd-a430-73377e312961 | -6.32164 | -55.35851 | 2025-11-19 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e87ae318-7787-3c51-b8ae-a4f7c28a34cc | -10.8768 | -49.54781 | 2025-11-19 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5465c179-5420-32a1-8c41-0ad11400b0aa | -11.67235 | -47.97396 | 2025-11-19 04:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2291cc9d-94c0-3212-8325-0fea3b25225b | -10.09805 | -49.58847 | 2025-11-19 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 682f31e0-ed22-3065-8285-adfcd12f3af3 | -10.35052 | -48.9118 | 2025-11-19 04:53:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 58ed578b-9009-34ba-ab47-cf747a8afbc5 | -8.87905 | -47.32843 | 2025-11-19 04:53:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 607185fc-b42b-337f-b2ca-4cffdec7751d | -9.39649 | -48.45596 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35215a1b-3d25-39b8-87bd-34f0debc49f2 | -8.83381 | -62.30008 | 2025-11-19 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3dfbf74-c772-3936-b80a-9077c571b836 | -10.06817 | -47.91621 | 2025-11-19 04:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a3dffb7-4399-364b-b70d-26e47ef893e3 | -11.20589 | -49.41502 | 2025-11-19 04:53:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aee2c31e-b1bd-3dda-9c09-43957df13283 | -10.01278 | -48.21966 | 2025-11-19 04:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4458eebc-008a-36bf-9b8f-de2923297e70 | -12.31359 | -47.91174 | 2025-11-19 04:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ff0693c-d8eb-3544-99e3-eed1d35208cf | -5.03192 | -56.96517 | 2025-11-19 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89e841ae-fe42-308f-9288-8d4bad74191d | -8.1267 | -47.58509 | 2025-11-19 04:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58292e3e-5fb2-3250-a056-0cf5c714e078 | -9.37925 | -48.43481 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aaaeaf2b-21ac-34ec-8169-6d17736e134e | -10.88617 | -54.14045 | 2025-11-19 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8be71f2e-6923-39f2-a6f0-e88a5d5fc99d | -18.25888 | -52.15158 | 2025-11-19 04:53:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d5611874-3b7f-33b7-985c-3d476fe852d3 | -7.26065 | -48.02741 | 2025-11-19 04:53:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 931489a1-15da-318a-b1ca-b142369c052b | -11.27504 | -48.50939 | 2025-11-19 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93e24add-22df-3e44-86b9-b45f10edcccb | -12.60113 | -48.87704 | 2025-11-19 04:53:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fefa66d1-6b9c-3bec-bdbc-77ba262a3ca0 | -5.00395 | -50.91476 | 2025-11-19 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ecf00ed-3346-3d7d-a896-b3cd7f1a9171 | -10.82844 | -48.02819 | 2025-11-19 04:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 70d99885-17cc-3a0d-8ecf-027d619ebcf8 | -6.31811 | -55.35792 | 2025-11-19 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 575c3c4c-a428-3b63-86cb-fa2844d59497 | -17.53778 | -53.71169 | 2025-11-19 04:53:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb973be0-e262-3e69-8885-1bf9e845bcfc | -11.61635 | -43.90388 | 2025-11-19 04:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 15efbe23-128f-30d4-a001-9f147669c28c | -10.73891 | -48.18452 | 2025-11-19 04:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0618989e-545d-31f4-bdf6-a31fb37a06c6 | -10.34835 | -48.92698 | 2025-11-19 04:53:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8406fdb8-d84f-3025-9d8e-7301cb79af75 | -11.28159 | -48.86795 | 2025-11-19 04:53:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0ac6438-5a43-3beb-8d51-feaa615c1ea4 | -16.26999 | -56.562 | 2025-11-19 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 0a3b9499-a232-3ee1-8d03-f44d8a98c76c | -6.34562 | -44.22725 | 2025-11-19 04:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85e44214-af90-3a70-ab0e-26bddd764ab3 | -17.53441 | -53.71113 | 2025-11-19 04:53:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73d64e2f-a987-3af5-9ea7-0514ad8b689c | -12.53083 | -48.75534 | 2025-11-19 04:53:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cc2ec62f-7c27-3431-b915-5911a9eedca7 | -10.65938 | -49.37276 | 2025-11-19 04:53:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fec404be-7cde-3f28-9239-10a28bb106e1 | -6.71033 | -47.78836 | 2025-11-19 04:53:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01772810-4926-3385-a2ae-cc890753d3d3 | -8.38592 | -44.0651 | 2025-11-19 04:53:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c77b4df-629d-3897-a0fe-3837afa2cb48 | -10.55145 | -44.11919 | 2025-11-19 04:53:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaa2015d-e6af-3778-b876-f3915c2fdc1f | -10.87747 | -49.54311 | 2025-11-19 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b54f6648-204c-35af-91d6-3f36406e3dc5 | -15.87756 | -51.14326 | 2025-11-19 04:53:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a82afdf-c192-3bc4-b6c3-5ae8c8d97e01 | -14.92905 | -47.77044 | 2025-11-19 04:55:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc8d1f3b-bdb8-39b9-9c42-7ce8bafd5c85 | -12.88759 | -54.75869 | 2025-11-19 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93c8344b-4271-3903-a3d2-6f0b4def732d | -13.69413 | -55.02753 | 2025-11-19 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 045d3ddd-4e28-3f36-8630-77a1768a7331 | -12.19426 | -61.07454 | 2025-11-19 04:55:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d34cb66-04ec-372d-8ae0-0620a94b1c28 | -18.50449 | -55.52425 | 2025-11-19 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9e98a0df-85df-3c28-847f-4da5e0a1556e | -18.50061 | -55.5273 | 2025-11-19 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e64645fb-23a7-36bb-aed2-c055d048bfdb | -13.88241 | -47.41973 | 2025-11-19 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84b92810-9347-3fbb-b4b6-123d3ef2f5f5 | -12.38736 | -54.16587 | 2025-11-19 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7acb110f-a8af-3c6b-8ab2-27bbc3547f29 | -12.45736 | -54.45176 | 2025-11-19 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 43397ea4-91e3-3685-a52b-afe801ef74a5 | -18.92305 | -52.1483 | 2025-11-19 04:55:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d0231d6c-21ea-37d6-9303-d883a85696c1 | -12.45405 | -54.45121 | 2025-11-19 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c87936a5-0d7f-314a-b007-294a929c5810 | -19.79523 | -56.10252 | 2025-11-19 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 75cc4937-948a-3e4c-b5b3-6e7c2bbfad7a | -14.09036 | -54.69581 | 2025-11-19 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67f67974-b59d-34e7-8f48-cbe1d97dc171 | -13.69081 | -55.02696 | 2025-11-19 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f15a16fb-cf1b-39d3-bd41-426426f313bd | -13.51727 | -47.9243 | 2025-11-19 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 758bda4a-bb03-3729-b7a3-fe9b78fd4b23 | -20.75431 | -48.03681 | 2025-11-19 04:55:00 | NOAA-20 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd48fa4d-e80d-3e80-9204-e54ac31fd9e1 | -13.88568 | -47.43029 | 2025-11-19 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c34d3ac6-89d6-3f2c-8cb2-68cefe50d987 | -12.45461 | -54.44769 | 2025-11-19 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e188d3e-3cd3-3014-961c-f3e333d81065 | -20.75372 | -48.04223 | 2025-11-19 04:55:00 | NOAA-20 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6ad44be-3690-39bf-ba50-46a19a46c077 | -13.90508 | -47.4234 | 2025-11-19 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2c9f5194-42a5-3d4a-b391-2fe3e2a4e584 | -12.88268 | -50.15496 | 2025-11-19 04:55:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa51cfb2-ceb3-3db0-ad41-fd0759780fe7 | -12.88202 | -50.15959 | 2025-11-19 04:55:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20359d4f-05eb-352b-954a-d2f705a5d9af | -13.91867 | -47.42565 | 2025-11-19 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3543d8b3-5e1f-375a-aa09-766a82150e47 | -14.05346 | -47.58075 | 2025-11-19 04:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3efbb063-47c9-30d0-94ce-df4741b81396 | -14.05402 | -47.57628 | 2025-11-19 04:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29332354-1d59-3c86-91a2-78b48e892dcd | -19.2491 | -55.345 | 2025-11-19 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| bff7f5da-8804-3a89-ac9b-d971dd58c284 | -14.09423 | -54.69282 | 2025-11-19 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d303057-3e11-34fc-8e23-08b5606c8b17 | -13.8896 | -47.43575 | 2025-11-19 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0016fac7-9f0c-39d5-bbf7-dc03d71943d8 | -18.50392 | -55.52788 | 2025-11-19 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e92add91-0aee-3529-9ba8-43c3f52c5748 | -13.48856 | -44.39185 | 2025-11-19 04:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43185f81-bdf0-3df2-9e14-d75a19cb422f | -13.9057 | -47.41861 | 2025-11-19 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82b08dcc-d756-3530-bfad-9fc325e3310a | -12.45792 | -54.44823 | 2025-11-19 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1f5c0fbc-eb43-3d69-9774-35d6e4589792 | -18.92377 | -52.14679 | 2025-11-19 04:55:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f12609b-d063-3a6b-9b94-4d3904ca4d58 | -22.18965 | -53.97572 | 2025-11-19 04:55:00 | NOAA-20 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f6fe018f-7365-3acf-b5e7-23118edd5bfd | -21.18618 | -47.82428 | 2025-11-19 04:55:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| deef2ad1-81cb-39ec-b203-db87dbd443a3 | -11.83706 | -57.85242 | 2025-11-19 04:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README21.md)
