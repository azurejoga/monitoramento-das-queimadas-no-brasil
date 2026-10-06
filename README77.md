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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c9e62f9-5b1c-3449-a5df-8d0328890e4a | -8.59633 | -67.20034 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e668c629-8fcb-30e9-a5a9-4c0527bf3e83 | -9.82398 | -65.04786 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1f41ffe8-005e-3863-a501-155a8f7e5ae1 | -10.43943 | -67.8392 | 2026-10-06 06:22:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f0aac38-6914-3d39-84c1-4ad1bb97df99 | -10.24494 | -68.30517 | 2026-10-06 06:22:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30bd226e-40cc-3095-9abf-427d6cc4040e | -9.16207 | -68.25113 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d2fecf8-fd8e-3ba4-810e-39ffaa2963f8 | -8.63101 | -69.50234 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27ad1fcc-0852-3e41-a810-1a07138cae25 | -9.11173 | -67.7117 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c185c2ab-81d4-3b07-b87e-f4288f654d4a | -9.50278 | -68.49413 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1ec8eaf-c62d-3788-bb19-4902d4968a22 | -8.77547 | -69.5332 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40cc9ed7-ddaf-39b7-9b09-01f3a776c488 | -8.82376 | -64.23324 | 2026-10-06 06:22:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 126a8ad0-3706-3722-bf68-ff376400b85c | -9.19276 | -65.33134 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58afdedd-8190-3308-9cfe-f355aba017c9 | -9.722 | -65.09467 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b008058-e1c5-3f76-b1d6-1a4a92b585cf | -9.12931 | -68.21089 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e601b4bc-ed60-3897-b60f-c4cd2db7704c | -9.13271 | -67.75397 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f36e73bc-0dca-3ece-b190-71e4a5cbca6f | -7.89891 | -71.66095 | 2026-10-06 06:22:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5faf25be-7ce6-3c1a-b957-8c1fd9c72c7d | -8.36768 | -70.57658 | 2026-10-06 06:22:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cc91fb4-631e-35f0-8bc0-5bae023cd20f | -9.22998 | -67.89131 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 348bec22-6a9a-3d35-89ca-9df047f90652 | -9.35698 | -67.43984 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c284d2f4-2aad-3ec1-9080-a436fb09d2b6 | -8.85912 | -66.7939 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb736047-ce47-3f25-9555-7b926a880f93 | -9.3922 | -68.27065 | 2026-10-06 06:22:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a206d4d0-4ee3-3596-a198-9dc5aab3dbd3 | -9.13261 | -68.24772 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38befba3-317b-3bbb-a013-d7dc4a928460 | -9.16151 | -68.25508 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ec203da-d86c-3870-bed6-5ee42de0aa58 | -7.6781 | -72.50362 | 2026-10-06 06:22:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ddffdc4-c47f-350e-85c3-933465797263 | -9.10821 | -65.36017 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d391af77-7d8e-31c3-a5e0-5e68618d5838 | -8.93753 | -67.34601 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 117973d8-606a-30c9-be9d-4e151d7b683a | -10.4448 | -67.89807 | 2026-10-06 06:22:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dceab6f-5e11-303b-99b9-244de0682d23 | -9.09973 | -67.69917 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81ada39d-7abc-3c8e-8a81-8b0c789c2ea3 | -9.14489 | -65.41332 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a497e5d-5a29-349f-9564-e230f698c9ff | -9.45717 | -64.33113 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9abbbc9-d46c-336c-8b3f-4aee433d48db | -9.11337 | -65.36089 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cf11b0b-b640-3042-82b2-2c5b3f07ddf1 | -8.97413 | -65.44045 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b452c9ca-6892-3ff6-8371-d45b0b723269 | -9.29202 | -65.64278 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a62e031-c3a9-3d32-a102-0e10efa86e68 | -9.26085 | -68.37748 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7126ea83-2b4b-3301-b990-5afbf2e4ccbf | -7.89211 | -72.30101 | 2026-10-06 06:22:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdd77a0d-28c0-377d-8a68-ab046a5b6c55 | -8.42792 | -70.11636 | 2026-10-06 06:22:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e80610ca-90e5-3f73-9d92-5ff3e58117c0 | -9.13212 | -67.75821 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b4bf4ed-4d86-3999-8766-ea4c7b260f89 | -9.02318 | -65.71339 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ff7f555-41bc-3fe9-97b8-38b87f29ceb5 | -10.2506 | -68.26436 | 2026-10-06 06:22:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcf3699d-762d-382f-b055-031657eb6d11 | -9.49006 | -63.95616 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20df1834-674e-3d3a-a09f-e2c2a1decc74 | -9.82355 | -65.05121 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4594357d-5def-3944-b49b-1e1ccd07a4ff | -9.12833 | -67.75336 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d026303b-1576-38bb-88c5-b682389d6c5a | -9.72772 | -65.09216 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd9a1026-2570-31f0-ad86-0630912e2de3 | -10.69785 | -69.63237 | 2026-10-06 06:22:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 335aff61-b8dc-3850-896e-328636473cdd | -8.62424 | -69.50385 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a943479-4d72-3176-aff1-7e0b8d4dd734 | -8.93878 | -72.84504 | 2026-10-06 06:22:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ee1a044-c693-3ba5-99c1-9f4a5b93a502 | -9.16382 | -67.8491 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8abc8ec-ce36-354e-be76-81e20485be47 | -9.10148 | -67.75381 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84a9ffdb-935e-333d-a6ad-50c7db3baf4c | -8.04888 | -72.43624 | 2026-10-06 06:22:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0a08c5d-f14b-3ef7-930c-7230081c6a45 | -10.81775 | -69.40234 | 2026-10-06 06:22:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5444800-7912-3b56-bee8-8e93aec86478 | -7.85182 | -72.46136 | 2026-10-06 06:22:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a6c69b4-7f12-3338-8b9f-03c6589f75bb | -9.10547 | -67.7523 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c3be999-09e3-3e0f-a13c-a2a9f20ac070 | -8.64517 | -66.85416 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9ab1551-b879-3b81-9b9c-a9928a87fd0b | -8.64449 | -66.85899 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 471636f0-ae41-3472-8b4f-d5dbf9372d92 | -8.62811 | -69.50443 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fff87e3f-fdd9-3ad3-8653-db0581cd3d7c | -10.24551 | -68.30111 | 2026-10-06 06:22:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff23f4b2-d9d9-3f05-bc25-2276ea065538 | -9.7273 | -65.09538 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37d303fd-896e-3817-91ec-af08c616a75b | -9.11292 | -67.7031 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a49be23a-1388-3e6b-8a04-174c5eb1446f | -9.46222 | -64.33562 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb5875ca-5a3c-319c-8a4a-74f441eed3fd | -7.81671 | -72.83335 | 2026-10-06 06:22:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ecdd5e6-f91f-32c3-9bc8-1a0fc21797b7 | -9.68064 | -67.07045 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 667ffc18-2724-3c05-9365-fff8f9fd6166 | -8.05165 | -72.35182 | 2026-10-06 06:22:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83a4ce09-d8dd-322e-bb17-4c4ca694eaf8 | -9.10109 | -67.75169 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe13d038-27f1-3b9e-92ce-f376940bea13 | -9.2288 | -67.89969 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 944d7e71-eeae-3782-b7e6-01cda4a103b7 | -8.60323 | -72.73106 | 2026-10-06 06:22:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92b3052d-d388-35bb-ac38-9199228dfcf5 | -9.12573 | -68.29492 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 637b183e-27c0-3d86-b55f-a82b935f086c | -8.54343 | -66.97776 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83ed2d8f-96ab-3029-8295-4ccd2b622954 | -8.62326 | -69.50119 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04dfd64a-3827-3958-aa37-cb3623cf0ca3 | -8.97371 | -65.44348 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b98cd88a-5384-37b5-ae02-86d26b3aeb1c | -8.39703 | -70.10923 | 2026-10-06 06:22:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d54810c-a27c-3e38-8587-1b88f6cc75f0 | -9.0933 | -65.48714 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 984ddb1c-3684-3330-a0fc-0b3774bd403a | -9.10262 | -65.36255 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22dfec8a-da44-3331-8a07-33ee1cb1cc62 | -9.36735 | -68.85704 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| caf59a54-8691-3b64-8ba9-e9997a99633f | -8.63028 | -69.50723 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83d08c9f-18e8-3377-9a9a-d8ba6b57b2f8 | -9.10645 | -67.75019 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b9344e8-f3b8-3962-8020-6df43047215f | -8.59429 | -66.81255 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a85919a7-a61c-3d87-8996-2b74b024da5d | -8.62568 | -69.51154 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 982a34dd-cfb1-31bd-b212-ba025c922f6a | -9.67545 | -66.82892 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e41f206-7379-3bd7-a9ed-8324601dfa67 | -8.62253 | -69.50607 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c27e1f4a-6d2e-30ba-b195-196f81ad6710 | -8.62354 | -69.50874 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c4656d2-6d50-31af-bcb8-0a2d04c98f97 | -9.15947 | -67.84847 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37010c14-854c-3327-be14-6e7515e6d471 | -12.13185 | -63.1567 | 2026-10-06 06:22:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 99eb92ba-d8c8-37fd-af19-4e2874eff746 | -10.14227 | -68.39471 | 2026-10-06 06:22:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02655338-5f4f-369a-a00c-62c0e9ef73f1 | -9.48058 | -67.671 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbe48ade-cc91-3617-86b6-24b711622286 | -7.84846 | -72.46085 | 2026-10-06 06:22:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38b686a1-4a6e-337f-8494-5e6e10054419 | -12.13348 | -63.15509 | 2026-10-06 06:22:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 169843c9-ce6f-335a-9e45-44b61e5419cf | -9.16387 | -61.41261 | 2026-10-06 06:22:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 274124f4-b173-37f3-bd54-2e38e4f97258 | -8.43164 | -70.11692 | 2026-10-06 06:22:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b849482-d937-33c0-a2f2-f2bbbf107981 | -9.12507 | -68.21026 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0730043e-83f4-3927-b28b-338c8029dfe2 | -8.86077 | -71.46423 | 2026-10-06 06:22:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf8897b4-e88f-3ff9-b9d9-538b2934ff8c | -8.92084 | -66.84943 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4a52b7e-0aff-360d-85a3-6ec4c0b358e4 | -9.67142 | -66.82327 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8148c914-2107-37b9-93fe-a95d4794313f | -9.11332 | -68.32108 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 554680c8-b083-3e6d-9e6a-2b2175a1537b | -10.82864 | -69.26128 | 2026-10-06 06:22:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2155d6eb-95dc-393b-a956-11ca1df36e1c | -9.10586 | -67.75446 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27e14391-f804-3564-834f-fdbad87e6ed9 | -12.13129 | -63.16161 | 2026-10-06 06:22:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a64dcbd7-5b91-3bd1-bbf4-f99a63590ba9 | -9.10985 | -65.36105 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9480de73-9db2-383c-b786-3dd3aaa31404 | -9.04025 | -65.43564 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62a342ed-c4db-330f-b9ae-13d6d0021078 | -9.46187 | -64.33114 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 075e42ad-3849-3a15-b52c-6b2f87188020 | -9.10469 | -65.36031 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31e6fe41-8397-3320-8f10-3421de3ed40c | -8.75269 | -68.97299 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README78.md)
