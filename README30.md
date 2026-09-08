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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcbffeb5-39af-3d87-8f20-5af18a14c275 | -5.15789 | -35.63603 | 2026-09-08 15:03:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 5f468262-ec0c-3c2c-827e-6bb2a19a082b | -8.78139 | -36.89526 | 2026-09-08 15:03:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| cf1440cb-cfdb-36ab-a42f-d96955d0ffdf | -8.6438 | -36.8244 | 2026-09-08 15:03:00 | NOAA-21 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| fac88d70-2262-37f8-a987-7983f2a5eb84 | -8.77879 | -36.8953 | 2026-09-08 15:03:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 5c933796-a7e5-3cf6-ade5-ba686563a154 | -9.7332 | -43.3932 | 2026-09-08 15:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 116.3 |
| e222f3c0-4741-342c-a832-98a2788fb99b | -2.7398 | -49.4776 | 2026-09-08 15:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c69d2dc7-10ac-37ec-a4cc-cebd168ba045 | -7.6968 | -44.3247 | 2026-09-08 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 7a5194ad-94f5-34d3-86f7-4d8772e2d018 | -8.5506 | -63.8786 | 2026-09-08 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| c7100b58-e9cc-3ead-a095-78442ad571ed | -3.9439 | -49.0104 | 2026-09-08 15:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| de2eb8b0-4bb9-34b5-8c57-a0c77f9f728d | -8.5322 | -63.8604 | 2026-09-08 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b1873a8d-bf47-36b1-aafe-81a6b11fde9c | -7.2158 | -43.6069 | 2026-09-08 15:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 2c790216-e077-3f88-ae67-99645ce245eb | -1.2174 | -55.7302 | 2026-09-08 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 6d7670e0-3865-3692-b01a-4cc70382b71e | -5.2899 | -60.1059 | 2026-09-08 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 79cf46e6-35a8-3579-b990-c2697e918fbd | -8.5321 | -63.8792 | 2026-09-08 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| fc8a7593-e578-340b-a815-aaf6663f1ba8 | -8.8175 | -62.4898 | 2026-09-08 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| d29fa6ee-b551-3427-919a-7162232e22c6 | -10.0964 | -45.728 | 2026-09-08 15:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 476a35b7-26e3-31b8-8783-e04c94cfcdaa | -9.72 | -43.46 | 2026-09-08 15:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be7f85bb-5fdd-3a3a-9c7f-5b630ef013a1 | -8.5506 | -63.8786 | 2026-09-08 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 1b744063-fc89-3aa6-b92c-bfbe686f5d7e | -7.6968 | -44.3247 | 2026-09-08 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 7b5c9bb7-9575-31f1-a1f8-27390f93a1dd | -8.5321 | -63.8792 | 2026-09-08 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| decc2831-adb7-3755-88dc-fbd3f01690a7 | -10.1151 | -45.7484 | 2026-09-08 15:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 27dca89a-d8aa-39d3-860f-38d57e09647e | -3.4058 | -59.2538 | 2026-09-08 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 3bde213a-731a-3b34-8592-76171396b6b3 | -8.5322 | -63.8604 | 2026-09-08 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 9cae0f09-df36-36ff-9a87-7b22226ae150 | -7.2158 | -43.6069 | 2026-09-08 15:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| f8ae2752-35e9-3920-9249-2577e053cc3c | -9.7138 | -43.4192 | 2026-09-08 15:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 367.7 |
| cf365e2e-c32a-3f4a-9567-5ed8c2faf350 | -10.1155 | -45.7257 | 2026-09-08 15:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 176.5 |
| ce2c5eb6-5c17-3f4d-b2b5-8c5d6170cbb5 | -8.8175 | -62.4898 | 2026-09-08 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e2971358-2d3d-3dd7-be0d-8dc94fd277cd | -9.7328 | -43.4168 | 2026-09-08 15:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 6f2b933a-1d00-3e85-b1b2-83675aeb9f05 | -10.0964 | -45.728 | 2026-09-08 15:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 239.4 |
| 85d495bd-36b0-300c-ab10-073543949a28 | -10.1155 | -45.7257 | 2026-09-08 15:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 4428dc5d-a99b-3a7c-83f5-5cb5327f4e77 | -7.7156 | -44.3228 | 2026-09-08 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 5a9d160f-6dce-3cb0-aa84-0463b092deaa | -7.6779 | -44.3266 | 2026-09-08 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 0804da9d-571e-32d2-b9c6-7bec716cb5b5 | -7.6968 | -44.3247 | 2026-09-08 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 8c4ca729-ebba-3078-bc94-8ddb15bf8009 | -1.4211 | -54.2171 | 2026-09-08 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0eeff665-e15e-3ea0-bb5a-5e48738b78a8 | -8.7066 | -62.4374 | 2026-09-08 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ac291885-a606-3a20-970a-374656c25c28 | -8.7437 | -62.4359 | 2026-09-08 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| af8932ab-fdbe-35b5-8cab-b04613b0f9b4 | -8.7622 | -62.4351 | 2026-09-08 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| aeb7dca3-4da8-3a47-a394-c594e2a86901 | -10.0964 | -45.728 | 2026-09-08 15:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 238c2e03-d97d-3b4f-a359-1ea4ae872876 | -3.8289 | -53.7634 | 2026-09-08 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| ace49b6b-b750-3ff3-8cde-e0b4b8589c64 | -9.7325 | -43.4403 | 2026-09-08 15:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 0a79291a-f962-36f4-8cc6-8b35003bed25 | -8.5322 | -63.8604 | 2026-09-08 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 88508f1d-53bf-3598-a658-8fd8955b475e | -8.7252 | -62.4367 | 2026-09-08 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 568fa43d-1562-3c2b-afb9-4a13264f2b7f | -10.1151 | -45.7484 | 2026-09-08 15:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 6ded5a92-a12f-3511-a8d5-705ba8fb07b5 | -9.0058 | -65.4373 | 2026-09-08 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| c71e6e5c-432a-317c-8fa2-ccf45a979d44 | -9.7328 | -43.4168 | 2026-09-08 15:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 68b3cf24-fc33-3c8d-952d-70091f718f3b | -8.5506 | -63.8786 | 2026-09-08 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 60f4c09b-b695-31d5-b6a0-8ee2d232f09e | -1.1991 | -55.7304 | 2026-09-08 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 1e3fa787-a2d2-3ad4-9a5f-7d91e501e32e | -6.3847 | -55.1851 | 2026-09-08 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| d84ce078-3323-35c3-9d7f-c75cd34ac721 | -3.4058 | -59.2538 | 2026-09-08 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| e0ba4727-f481-3f10-af6e-05185cfe8d59 | -8.5321 | -63.8792 | 2026-09-08 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 86f738a3-cba7-3e30-8854-ad89508b598a | -7.1372 | -42.2484 | 2026-09-08 15:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| a9b26e35-d98d-3b25-8cc4-9579b7722a40 | -8.688 | -62.4572 | 2026-09-08 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 5e3b267f-7e06-3487-acee-cd0c66e4c161 | -3.4241 | -59.2535 | 2026-09-08 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 150.3 |
| a3374333-eb0d-3e46-bead-2e9a10cee5eb | -9.0982 | -65.4904 | 2026-09-08 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 0d7c85a3-2a70-3537-8833-c4491b959010 | -8.5321 | -63.8792 | 2026-09-08 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| bbcdf12f-f682-384c-9177-da8bb87b804b | -7.1372 | -42.2484 | 2026-09-08 15:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 14edfab5-7334-3e5a-9eb0-855e766d0694 | -2.8839 | -50.4428 | 2026-09-08 15:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 28c2376b-7895-3602-be31-1531b21868ee | -10.1151 | -45.7484 | 2026-09-08 15:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 147b796d-327c-3d1c-82b7-035c500b150a | -8.5506 | -63.8786 | 2026-09-08 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 2431ab17-efad-3089-9c0f-79aef509a5fb | -8.5137 | -63.8611 | 2026-09-08 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 4d748e83-47af-34f0-a881-faa9218b0264 | -2.8654 | -50.4643 | 2026-09-08 15:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b258bb3a-a155-3ee5-b947-9992b45cd2b3 | -10.2563 | -45.2062 | 2026-09-08 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 160.7 |
| d6b8f45f-010f-3c32-92ed-1c1011b50b57 | -4.0613 | -55.3573 | 2026-09-08 15:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| ff0fe509-0b74-3fcb-9178-79282633a6c2 | -1.4751 | -54.8555 | 2026-09-08 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| c9829422-7fdb-3874-8e86-a065b79986c3 | -7.7156 | -44.3228 | 2026-09-08 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| c0faed3c-af3d-3953-be5b-952fd076142c | -9.0058 | -65.4373 | 2026-09-08 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 4fe7bdc9-88ea-31cb-a778-9b1f62fa144e | -8.5322 | -63.8604 | 2026-09-08 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 19180dcf-bcd3-34f0-b3c1-1a929570fcac | -9.0982 | -65.4904 | 2026-09-08 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| d632801e-bfed-3b18-9a92-be66867e1f5d | -7.6968 | -44.3247 | 2026-09-08 15:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 7e66da4b-6630-3391-a329-b5ef07e63938 | -9.0058 | -65.4373 | 2026-09-08 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| f73a0ce7-3926-34df-a413-2f86fcd0d900 | -9.0244 | -65.4181 | 2026-09-08 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| d201d9cc-81a5-37cf-a306-e061174232b8 | -1.4752 | -54.8157 | 2026-09-08 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| e402dab8-aca6-3f00-96e8-7a9c97cf9c8f | -1.3747 | -49.0177 | 2026-09-08 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| e2ccc359-99dd-33ea-84d7-10dbd2131028 | -9.0059 | -65.4186 | 2026-09-08 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 8995fd4b-7745-3c1d-8175-dd247a16757b | -8.5322 | -63.8604 | 2026-09-08 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9367d722-b5a1-3ff5-abf1-58bcd7b8412f | -8.5506 | -63.8786 | 2026-09-08 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| ed195a45-e135-321a-87b8-72deaafdc43a | -10.2563 | -45.2062 | 2026-09-08 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 1483385e-677b-3dc8-a66c-70b5e222f816 | -1.4751 | -54.8555 | 2026-09-08 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 369d825f-7cea-333b-9974-f1d1937b957e | -8.5321 | -63.8792 | 2026-09-08 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 219dd37a-0447-3c26-9f44-7b0db776f170 | -8.5137 | -63.8611 | 2026-09-08 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f4a664d8-2d0e-37f0-bfd2-55d4472f5cff | -9.0244 | -65.4181 | 2026-09-08 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| bd40edbe-5a02-3093-bc6c-c6eb1a8c96a5 | -6.6526 | -45.355 | 2026-09-08 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 4115a6c7-1cec-33a0-a2b6-e7e01b25f3b2 | -8.5137 | -63.8611 | 2026-09-08 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 7733c6a4-8a50-399f-b532-fce999acdd05 | -8.5322 | -63.8604 | 2026-09-08 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| b30f4d08-fdad-35e8-b2a4-a8380b947016 | -9.0982 | -65.4904 | 2026-09-08 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| d8a611bd-2e28-3b8e-b7c9-25982f9c2472 | -8.5506 | -63.8786 | 2026-09-08 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 55e614c7-a988-327b-a46e-5350cf6c90ae | -2.1118 | -49.5355 | 2026-09-08 16:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| fc431917-e7bc-3e15-8a60-096f85696e8c | -10.2563 | -45.2062 | 2026-09-08 16:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| edea49dc-83ba-32e3-8d85-4106009f5cfa | -1.1991 | -55.7106 | 2026-09-08 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| f3920817-32ba-33e9-ab7e-db4b541baa5a | -8.5321 | -63.8792 | 2026-09-08 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 3d09f948-c7c2-3630-923c-bed95ed92500 | -7.6968 | -44.3247 | 2026-09-08 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 193.6 |
| 6e860912-b1a4-31b8-bbb6-50f478664aab | -7.6779 | -44.3266 | 2026-09-08 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 48569797-dbb4-39d1-a130-69cd3fce5860 | -3.4058 | -59.2538 | 2026-09-08 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| dddb453a-1542-3d5c-96c7-c76a66453dfc | -9.0058 | -65.4373 | 2026-09-08 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| cc300b5a-2d11-3032-a4fb-3e7dfbae58c2 | -7.7156 | -44.3228 | 2026-09-08 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| bcbd5978-16ab-3acc-9e99-6c8edd28b743 | -8.6881 | -62.4382 | 2026-09-08 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a7c2455d-c233-3259-a84f-823346429c61 | -8.5506 | -63.8786 | 2026-09-08 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 948ea77d-ed9c-3757-a14e-acae0d7adc44 | -8.5322 | -63.8604 | 2026-09-08 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 391fe9f1-2436-33a8-88b7-4f8b31d0d0cf | -8.688 | -62.4572 | 2026-09-08 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 9fd2788f-9c87-3a6c-a382-afad99a32d71 | -8.5137 | -63.8611 | 2026-09-08 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |


[Clique aqui para ver as próximas entradas](README31.md)
