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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 187230a3-ff4b-3f11-83d8-302a69d3fa28 | -6.86677 | -43.73692 | 2026-08-21 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c81398f-3d25-3efe-a37e-06b326470007 | -6.38995 | -54.94305 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcc1dc07-bcbc-3184-a0d8-125584ac9552 | -4.10873 | -56.36129 | 2026-08-21 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66853aba-c41c-3f51-a395-dbd507a43688 | -13.7436 | -51.86199 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d942c4d8-a46d-3bd6-822a-819c53d54b29 | -6.87393 | -59.44094 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf4a6127-8613-3013-a184-de1c25269ec7 | -13.73956 | -51.85635 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1c89edd9-1ddc-3af5-b2f5-84b7e8d654fe | -9.17657 | -57.00399 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bf225b3-3c52-30f3-94f8-60e7114aba26 | -6.92299 | -59.35409 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7dc1f747-8587-39bb-9146-ff6162f66597 | -6.109 | -59.92852 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ec8c51f-4ed3-3464-89b8-c9f393ca26bc | -8.49366 | -54.88143 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3067bd14-b762-3e2f-81c4-cffd864e0e39 | -9.21048 | -59.77342 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64670a56-2e4e-3a9a-9929-7c856749913f | -9.50983 | -51.68383 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98043c1e-e5f6-33b9-b463-7a0267fb5cee | -6.85802 | -59.43073 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a46f3577-a387-3e3b-bc6f-973f6b2479ec | -9.07158 | -60.42765 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 280546e1-5f09-317e-9372-65c6d500d0b2 | -6.9408 | -52.78679 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99592bed-dbfb-3d57-8c24-f8e936a162c2 | -9.99407 | -48.56028 | 2026-08-21 05:23:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2e08b68-facd-3c2f-8704-556b5510613c | -9.21788 | -59.77086 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc05d499-287c-3ef0-819f-f48e5d4a8df1 | -6.58122 | -58.96287 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fb60636-1ce4-32a2-8c66-2cf3c460ba86 | -6.89428 | -56.43855 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c456776-d519-3586-bd6d-654d2782af82 | -5.66866 | -51.64426 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5139b736-520f-3637-afe3-44ed5bc11329 | -4.65405 | -50.8718 | 2026-08-21 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a84ed5bb-6fcc-3a08-81b3-9549e83c4b23 | -15.01286 | -52.67187 | 2026-08-21 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf1bc239-b97f-3c54-bb41-8e2758e332b6 | -8.49794 | -54.87019 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ec8b73d-6929-39c8-a80f-5efbfddaf8ac | -6.13139 | -57.73787 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf37db54-f327-3389-a515-109e2a45833f | -6.79477 | -59.43579 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab4d9cad-0386-33b6-9902-a272db5a8875 | -7.60222 | -60.95259 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40e46532-f773-364f-8ce4-eaac452af45d | -6.82683 | -59.40667 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f87492a-729a-3ee1-ab81-4390e8576599 | -6.86056 | -59.02594 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bc38ab8-c531-3ff5-9b59-53a30492e969 | -6.87578 | -56.42469 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b48fa1e2-61b7-3897-abf3-0d5e14abc2cb | -9.16762 | -58.37421 | 2026-08-21 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6aca138-15c7-3500-af83-824ac5827a04 | -8.61167 | -54.68805 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0768381-604f-3647-b8f2-bc8840bf1faa | -6.2477 | -55.41372 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90ffc481-5021-3b48-af8e-6cae96a1c9eb | -6.09263 | -57.91684 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75d8779a-56ec-3e61-83a0-c0324057fdb2 | -6.87675 | -59.44521 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8dc147ad-1b4d-3abf-aa10-1dcc825e4e85 | -6.13865 | -59.90126 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60cba787-d786-3f1f-b523-495e50962e81 | -6.01227 | -57.82573 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ba91a45-a848-3b99-94ec-fd5e69bdb3c0 | -6.81436 | -59.39707 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e48a27f8-4f4e-35f3-b811-e6df00f80f86 | -6.24593 | -55.42501 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d032e18-6daa-3ef2-9947-0092af0865d9 | -6.58329 | -58.99291 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 681880d1-cb33-3067-affe-1a82f7aba2fb | -9.21508 | -59.76662 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 67c0f130-7996-3db5-9179-db59c0323818 | -9.80377 | -46.65377 | 2026-08-21 05:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| e2c86795-cee3-36c2-b2b6-0725bf1b7b34 | -6.00396 | -57.83511 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c95adc7-c0fe-3391-9547-62e8c570cb49 | -8.38132 | -62.69708 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 0c674e3f-8577-3775-858b-bc0036dd7dab | -9.22188 | -59.76775 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 289cf8a3-d263-3df6-8a0c-6b178e5038af | -6.08653 | -57.91231 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9027042c-80dd-389e-be05-ef808b48604d | -6.23044 | -55.41119 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a390c024-9fec-35d8-8ba6-bf10ccd714c0 | -16.74509 | -49.37246 | 2026-08-21 05:23:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5feffc9e-7c99-30ac-9f9e-649974fe7a2d | -6.11443 | -59.91735 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3389910d-436b-31cf-8648-660fa69b4be4 | -6.12559 | -59.91514 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae814e4c-d43d-3041-9e15-1325ec8e3069 | -9.22128 | -59.77143 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b028f1d5-37c0-3318-b679-6c2c5cd66246 | -4.44624 | -55.39217 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1f82a5c-1de9-3229-8ed4-c4680fb5e15a | -7.35094 | -55.67714 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e094a6e-8ff3-3d2f-92fc-bf8d35dfe8a5 | -8.37959 | -62.70727 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 9c3c2bb8-3833-3cde-9d2f-de1bbc2786ec | -5.80589 | -55.71779 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5281b6e7-cbe0-3ba4-a777-ab6455dc5862 | -6.79568 | -59.59688 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b468e39a-dbea-39e7-ab18-f966dbdd0066 | -6.87462 | -59.02829 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 210235fe-5551-3f6e-8035-1720cbfcfa46 | -7.03775 | -55.51096 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a669731a-3983-3f2f-ac52-2bd1c8f2e582 | -8.05757 | -50.1072 | 2026-08-21 05:23:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bc320c4-3117-3a42-b36d-ecc06191cc11 | -8.59235 | -54.74183 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 295faa67-2233-37aa-af66-a4b8a0b8b8f6 | -6.13324 | -59.91239 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad325df3-c2fa-3350-bd17-3bb3952ff1e3 | -7.45913 | -46.1565 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38514380-e68f-3eb2-bda4-d521e26920cf | -7.88654 | -61.66426 | 2026-08-21 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dc242db-b22f-37b6-8a09-896fe4f3d769 | -6.87188 | -59.41019 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 549b2d89-4b4c-36ee-bf1d-b6d9e2da1aae | -10.52216 | -50.77231 | 2026-08-21 05:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac04fde8-87d8-3992-92b3-fa55b541db03 | -7.01441 | -48.03509 | 2026-08-21 05:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09e3f223-e64d-3d6f-8d89-2bac3142a86d | -8.28472 | -62.89465 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5968921-f8a4-30e9-8d30-db3408657091 | -4.01229 | -48.06209 | 2026-08-21 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3ab009a-52c2-311c-b8f0-8a7647082f08 | -10.29749 | -48.232 | 2026-08-21 05:23:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fa5ac19-6e46-34da-a8e9-dea5e8d753d4 | -9.05509 | -60.44078 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da042afd-4fc2-34ab-b745-27eb28ed2022 | -6.88696 | -59.03774 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a60dd13-5029-32b9-b683-3e5b2fd52a7b | -13.39808 | -54.38647 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 9c773618-0c6c-38a4-b7c4-67688b912850 | -11.33113 | -45.01897 | 2026-08-21 05:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ff59989e-ace3-3b68-a236-acc22a0db220 | -6.70234 | -59.09719 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d76f62e-53e2-3612-a6fb-c05d1e7e2952 | -6.36328 | -58.34016 | 2026-08-21 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae86056e-33db-3caa-b050-f942ac6ec91c | -6.42709 | -52.7267 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8dd9e22a-6f28-3e23-b5be-d0a29db8b0c9 | -14.57781 | -52.99609 | 2026-08-21 05:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eee702dd-f319-36e7-a62e-eaff27e594e2 | -6.12861 | -57.69121 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54c442f5-cc22-3a65-b777-ca16e33aa9e9 | -6.86385 | -59.41646 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34b93616-d95c-3a4c-9b23-21a703bdc621 | -6.43056 | -56.18723 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02f46949-98bc-3d01-816e-fa3deb202c38 | -7.34174 | -55.69107 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e36f5185-d4c6-352d-991e-e59d65ce5465 | -6.1436 | -57.85367 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f64e1f7f-e89e-3d18-92fc-b9320acddbc1 | -5.81157 | -55.72612 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fa9a9fc-9f49-345d-903e-bcf9e5c34fce | -6.7097 | -59.09467 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b907f753-fd6d-3803-b03e-8620dee0a1c7 | -13.39485 | -54.38079 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| d0cd1fc4-37d7-3f78-a2ac-6f39105e05fa | -6.86487 | -59.43183 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ddeb0fc8-0857-3b3d-bc91-4ee0dc3f8c85 | -8.27422 | -57.34807 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f231b2d5-a9cf-33f6-801e-bbc3e6f80755 | -6.89164 | -59.44002 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a0a9e84-f811-3d9f-b4cc-28567aec5fa3 | -15.16614 | -48.78486 | 2026-08-21 05:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0a6512ab-a725-36f9-b0e7-d4f9d3884d16 | -9.0703 | -60.43539 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78f6315a-99b2-38cf-bfdd-d187a46d6d5e | -8.1822 | -54.99434 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f1e11c8-e06c-3958-b282-8279841496ae | -7.05446 | -59.83955 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88e85ab4-05e4-32da-8248-c736c4a12a5e | -4.11418 | -48.93575 | 2026-08-21 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 362bdec4-3663-334e-bcbe-5139670a1a53 | -6.2322 | -55.39988 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f440a439-793c-3522-8568-b5492f918f05 | -8.17033 | -55.0003 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15de72d7-54e1-3f8f-827d-c121ea131717 | -8.59534 | -54.74664 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2d976be7-b34c-3f02-9d9d-8e408e4c658f | -14.72587 | -47.14017 | 2026-08-21 05:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e54f1d1e-24a5-304a-93a8-877065c43c95 | -12.50187 | -54.75478 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbfd0ea7-b471-325c-a8c0-791a6949dc40 | -6.66045 | -56.351 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe1612d9-e994-3799-802a-31bbdc9a5c03 | -7.00964 | -59.54958 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df654bf6-ec13-3f41-937c-98150372f498 | -9.45387 | -51.64559 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README66.md)
