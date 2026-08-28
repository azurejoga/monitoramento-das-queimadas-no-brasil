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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0c08fd3-06f3-39cf-b27b-ff59981ae7f0 | -6.17461 | -57.7839 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 87a0840c-9257-36b6-826d-1a63a3564358 | -6.79195 | -59.396 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| b9540a49-8e88-302b-9ca3-699c83648a80 | -8.02262 | -48.01381 | 2026-08-28 17:28:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9af0f5b6-ed31-3d29-8500-32b8b799019c | -9.26253 | -56.89225 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| aa73e45b-fd03-3737-9b7f-c1886d2728f8 | -8.61745 | -54.69822 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b9d906fe-493e-3fab-9dd0-1bc5dd51e980 | -6.91294 | -58.9253 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| c93a617c-0146-3da7-b620-26215d8a279f | -9.17794 | -59.55988 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4daab1d4-6bee-3ef0-ab78-f3a821583254 | -6.21317 | -57.76733 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5dec68c7-8586-3f0b-9d7c-2895f4fc9be9 | -3.9331 | -59.33705 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0579f4ff-ea49-3a49-a118-634622df0d64 | -4.58158 | -54.90237 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c646b550-31a2-32ad-ab83-b9bc6cac0919 | -7.36138 | -55.16453 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fda4a2ce-8861-3656-a56e-b3208fe36bd7 | -7.92477 | -70.66143 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 27605441-b00e-3a83-bf5a-a882fdedbdcc | -8.8235 | -68.97548 | 2026-08-28 17:28:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 02d2cdd0-e834-355e-a4dc-ae9e18ab51f6 | -7.59814 | -61.21534 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e81f9fc0-aa1c-3e48-9172-4d9284fedcc5 | -5.91459 | -61.40104 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7750b3ed-5cc9-323b-811f-ed291878653a | -6.37145 | -54.95303 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5198f7d4-a5ad-389d-b649-cbda8ce3c9ca | -6.90161 | -60.06079 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66e6cfba-167b-3b13-b62d-a3bae0a1fb1d | -4.30811 | -59.46383 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b1b86ffb-6cf8-3017-a3c5-5e74cf24cec3 | -6.5937 | -55.43264 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bdbf9b72-1f68-3596-8799-a5092c018a76 | -4.50012 | -55.5183 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 013631c9-99a5-3486-b67a-e760c96122e1 | -9.23011 | -51.52682 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1dd03502-1198-368d-8ae3-6cf10ae3add6 | -6.75544 | -59.44163 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d95d037b-3651-3120-9589-779e83e6d63d | -6.62129 | -53.18247 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2ebbe31e-07fc-3135-ace4-383c83bb4592 | -4.06083 | -60.64328 | 2026-08-28 17:28:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 45f4a69f-b957-3b73-9e17-e9b662c9dded | -6.6561 | -59.1115 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a2ea0fd9-3d7b-3d20-b50b-76f1ed06dbd9 | -4.00078 | -55.33752 | 2026-08-28 17:28:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0299e582-614d-3780-9473-bfb0397e6f46 | -6.20655 | -57.6786 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5236853a-23c1-3271-9177-451e544e0714 | -8.59346 | -54.78614 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| fec6a150-f081-3ddc-b4d7-c9e777d157a8 | -8.5912 | -54.79408 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 34f88ae0-3a25-33cf-b158-77b8b82c5d8e | -6.84373 | -58.99402 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ee141a3b-4688-3d75-a6c2-ab0ff650b877 | -6.8408 | -59.94987 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| cc813d50-1926-3728-a7df-47a64fa09137 | -7.70598 | -57.74833 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| d88c3f44-8fd7-38bd-b838-ee97609c4753 | -7.89604 | -65.62845 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 246a55e7-e90d-34c6-ae13-e4cd1c292424 | -8.87343 | -66.90263 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c6f4a47a-acca-3344-97db-f502893d0695 | -7.60206 | -61.21477 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f4ecdfaf-e0fe-3e4a-ab09-afd95bb1c29b | -7.59573 | -61.33837 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 1483ef05-6556-3cfb-b9ff-a74253ca3ddc | -6.00563 | -57.84674 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 75674140-e131-3b26-a0b1-560dc39be69e | -4.30382 | -55.24478 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c84926c7-7a5b-39d9-9edc-b53c6bc5009b | -6.5513 | -56.55394 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 751f8d6a-1ffe-3c81-9beb-14f25a86cfd7 | -9.31207 | -56.79763 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4e0db0a5-3456-3a13-a369-21c2df56565f | -10.05236 | -68.83123 | 2026-08-28 17:28:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 14.9 |
| c3316ea6-68dc-3f01-aa86-a5521287ac12 | -8.63813 | -66.53852 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a9f22757-8374-3b0a-9a18-e368bd558eae | -8.53175 | -55.26279 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| bd9ae2b7-e1a2-3c32-bb85-b98999a6bd18 | -6.62878 | -53.18128 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 79dc34ff-cf16-37c2-a53a-ad5e2061194b | -6.47088 | -55.94447 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8973d244-2c72-3639-b95d-ce70e14df8fd | -10.20405 | -69.35831 | 2026-08-28 17:28:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 24.3 |
| ddb4bf65-f48b-360c-b92c-d246ae93c9f8 | -7.35174 | -55.16977 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| e33bd14d-41fd-38e8-b069-e40a25c389b4 | -10.51737 | -59.6227 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| fb37c7f1-f652-3f07-adc5-7535fd5bca7c | -9.00008 | -65.4513 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.9 |
| a87333d8-ebe6-34cc-ad71-12c973004751 | -9.22369 | -59.77235 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| fe35acea-ec37-32e1-83c6-9c825d0b0b74 | -4.15031 | -59.39201 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 74e596aa-fd3b-344e-8716-a425b5dffc9b | -8.64902 | -62.85082 | 2026-08-28 17:28:00 | NPP-375 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| d23238b4-212b-3507-a747-10f304544b69 | -4.17773 | -46.45669 | 2026-08-28 17:28:00 | NPP-375 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c15db39-2c93-3e3e-b2e9-baf6c969274c | -8.59404 | -54.78986 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 1b856db4-ca98-3a3a-82a6-b1be3f7c2e6f | -7.25269 | -45.85891 | 2026-08-28 17:28:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f5974f61-a43f-3046-88e0-74977ab0c5b2 | -7.92562 | -70.66846 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 1aec9213-408f-3243-9271-596b0bcd4d36 | -6.01922 | -57.73344 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7e11c40-ee1e-36d3-ab05-1d8036374689 | -5.77992 | -59.17136 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4dce7499-94a7-3d28-94a2-20374b3bf852 | -10.76427 | -53.9771 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 30c2d96f-9b8f-308e-8f0c-6c03629a5c4c | -9.25867 | -57.06987 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| ccc1879f-94aa-33ba-b704-a1610149576e | -9.54524 | -50.85574 | 2026-08-28 17:28:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9b5cde9f-45f2-326e-a081-782ecd247f9c | -8.11475 | -51.66491 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e0ac1303-96bf-3189-bce2-1273d30982df | -5.14067 | -56.27668 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 962507d6-26aa-32a4-9336-c34c5d5a822a | -7.45775 | -50.93071 | 2026-08-28 17:28:00 | NPP-375 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0398f2aa-5090-34e2-8362-8f9b1c6746a3 | -11.42675 | -61.42654 | 2026-08-28 17:28:00 | NPP-375 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5f9feccd-b939-3458-8d21-9691eddf4e64 | -6.11429 | -57.82961 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f3605ef0-64ce-376b-95b3-3f967c05c461 | -8.01585 | -48.01601 | 2026-08-28 17:28:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57c1cf73-07b0-36a5-bc55-62039a15012c | -9.04635 | -65.4317 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 219777b2-27b8-3cd7-b8d4-ce610565a6b2 | -6.16196 | -53.51382 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 36459764-66ca-38b5-8e62-ff71f5949f7a | -4.79326 | -55.69891 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 84415431-bf03-3cbe-9e7a-a2df1ef44726 | -5.97578 | -55.6979 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0588e33b-7110-3409-873e-e8e279c31f2d | -6.88595 | -59.44682 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| d4fab6ce-e63d-3e10-aa2b-4c5476b5d303 | -9.75752 | -64.97308 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| ea5ce9ea-c59d-3206-86f4-3478d6b0a406 | -9.46627 | -51.69466 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 95e82db2-d10e-38e5-b15b-2126b9c5425a | -6.01578 | -57.66594 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 9b91308c-380c-34ad-bb86-78ec2e033e03 | -3.57668 | -54.53209 | 2026-08-28 17:28:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5dfcbb59-8c62-3268-b699-4c1da42d5ba4 | -6.01384 | -57.78803 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 11cbe2ba-db0a-300f-89be-68237c7d9c83 | -9.92958 | -60.43645 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 136456a1-e6ca-3ad1-95c9-cdda8df8553c | -6.24674 | -45.96492 | 2026-08-28 17:28:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25dca2d3-ebe7-349c-968b-1cae3724b256 | -9.228 | -59.77616 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| fbe77b52-aafa-32c4-becf-3b3b3254fac4 | -9.25585 | -57.07393 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a48ec9a2-3b90-35b0-b883-3a10e6a171b4 | -6.01665 | -57.78402 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dcf7d547-82dc-3607-b7e9-c50a5eb147dd | -8.59004 | -54.78667 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 3cbefa8f-920b-35d5-b44c-3572e1d8a9fe | -6.90099 | -43.65333 | 2026-08-28 17:28:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 7c82b295-6fe5-3243-8859-350f07c35934 | -9.06131 | -45.91782 | 2026-08-28 17:28:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f9c770e3-6df7-3d87-b359-ae85aa2fd5cb | -9.91731 | -60.43322 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b7c5bd74-9574-3a43-990c-051fb29b1c3f | -8.21812 | -70.50912 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 30.2 |
| a9ce7202-c506-3344-8010-54c83def7a7f | -8.6038 | -54.82994 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| fa6bd50e-8941-3d53-8f59-8a0b7777a9b3 | -9.26307 | -56.89578 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4ca3594c-53c3-3c5c-bb38-0b8e9a19b5ad | -6.60333 | -55.44976 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f8d0abf4-6b05-349e-a788-41d7948de537 | -6.82556 | -59.57337 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b9e05ed4-0c2f-361e-aad5-6c278a94e9a7 | -8.11875 | -51.66425 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4728f3eb-e4b3-30c0-bae1-2c2eb7e8be77 | -5.80217 | -57.63828 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8fc7ce55-014c-3a3d-a5dc-0d356af1dac3 | -8.82358 | -49.63266 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1bc4ade0-fa5a-36d2-8f1d-baa408f1f24f | -8.18519 | -54.94243 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 90e3eb17-2eb4-3730-a15b-eab7d4b0dc78 | -3.60794 | -56.86086 | 2026-08-28 17:28:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| aee9b7a8-fc7a-3ceb-8fd6-947cbc7adcc6 | -6.16229 | -57.79293 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 9c766db9-b19c-3441-b733-c8f6b6febd26 | -6.58193 | -56.53139 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7837fde4-0df0-339d-80bb-cdf0956d9847 | -6.82057 | -55.61071 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 012ae83e-befd-38f2-9979-7670943b548f | -9.45483 | -51.57793 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README130.md)
