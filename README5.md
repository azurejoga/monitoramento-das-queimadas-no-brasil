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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 888b92f0-32c3-39d6-a051-43c831836407 | -11.84426 | -43.79078 | 2025-12-27 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c47aaa5-b9ac-37aa-8560-2f4bca758d3e | -10.02132 | -42.32944 | 2025-12-27 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c53e5ff9-1490-3ed8-96e9-930f1502cacf | -8.53671 | -35.8611 | 2025-12-27 03:49:00 | NOAA-21 | SÃO JOAQUIM DO MONTE | PERNAMBUCO | Brasil | 2613305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8e5cc670-e6e4-3491-a8cd-9af0adebf9ba | -7.52225 | -35.1354 | 2025-12-27 03:49:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 892ef51d-fbce-35e6-b82a-112a95c1f8a5 | -7.2223 | -43.07837 | 2025-12-27 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 405b8316-6ee4-337d-9182-623fe2095b80 | -11.16831 | -43.30815 | 2025-12-27 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f821959c-0ef2-3493-a05f-6ce0357336e0 | -11.39408 | -47.99303 | 2025-12-27 03:49:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 83054645-6200-3012-9982-89c58bb56d6b | -12.47126 | -43.52076 | 2025-12-27 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ba5e25e-5155-3ee3-9c19-c94106793c9e | -5.45508 | -46.18014 | 2025-12-27 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c812af86-6dd6-346a-87fc-795ce39b9f41 | -11.15807 | -43.3219 | 2025-12-27 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 13620471-cf86-3a89-b75e-9b4fa77c6ac0 | -8.53615 | -35.86474 | 2025-12-27 03:49:00 | NOAA-21 | SÃO JOAQUIM DO MONTE | PERNAMBUCO | Brasil | 2613305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5ba74861-625a-3bb7-be31-ec812c590df1 | -11.01929 | -45.25569 | 2025-12-27 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f76fb72f-46b1-3df8-b852-a45b11d1125b | -10.54407 | -48.71176 | 2025-12-27 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e2861ef-3c62-3728-9cea-ccb9a03fb4e7 | -6.97019 | -39.83159 | 2025-12-27 03:49:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9121460-5ada-3066-9ec7-75bb80e28801 | -7.2259 | -43.08314 | 2025-12-27 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 511b72b7-4fcc-3e7e-a2dc-e3d30ade0349 | -11.84918 | -43.73979 | 2025-12-27 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec1fd4d5-5eee-34d0-973f-fd08d8368c70 | -8.35615 | -36.43649 | 2025-12-27 03:49:00 | NOAA-21 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 678a54b5-1708-34a0-b4f3-ea31a45fcfa5 | -12.17712 | -38.81295 | 2025-12-27 03:49:00 | NOAA-21 | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d85d80f8-3637-30f2-95c3-7de1fe68c625 | -7.72763 | -37.93015 | 2025-12-27 03:49:00 | NOAA-21 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8ac99bc4-df0b-38b9-a20a-ff1325183002 | -6.17878 | -43.41461 | 2025-12-27 03:49:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de36acaf-ec5a-30ba-b919-2fe0201e2423 | -6.76569 | -35.44641 | 2025-12-27 03:49:00 | NOAA-21 | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f64568cf-6a5f-35dd-aa71-beee65f7ce4d | -10.02528 | -42.32803 | 2025-12-27 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b6ffb505-cabc-3e3e-92f9-c0f309262e9e | -6.778 | -35.34441 | 2025-12-27 03:49:00 | NOAA-21 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bd4530ac-67b6-36eb-b439-c708950b2b07 | -11.98109 | -44.28579 | 2025-12-27 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d59a63a-0bee-3491-99f6-4450abe7611e | -5.45442 | -46.17625 | 2025-12-27 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5476edd2-0fb8-304c-99ab-ba2872cd3ebd | -11.63799 | -49.42146 | 2025-12-27 03:49:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c23b1aa-8330-3618-8746-d60712497d5f | -8.03588 | -34.98733 | 2025-12-27 03:49:00 | NOAA-21 | CAMARAGIBE | PERNAMBUCO | Brasil | 2603454 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 16ddc2bb-fe7b-3471-8500-5e4bad254a19 | -5.9359 | -44.45692 | 2025-12-27 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cbfe1cb5-1eaa-3b20-9ffb-b48bde75ccf5 | -11.9331 | -40.53489 | 2025-12-27 03:49:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e20c6ee5-40b7-3863-936f-f6fd2367fef5 | -10.02523 | -42.33011 | 2025-12-27 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| dc63ffbd-2fdf-3a6b-8bf8-b9f83b201c54 | -13.0179 | -40.62732 | 2025-12-27 03:49:00 | NOAA-21 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8b55f7d1-4d38-3b85-8f09-4f393ae262f1 | -6.9864 | -35.59467 | 2025-12-27 03:49:00 | NOAA-21 | ALAGOA GRANDE | PARAÍBA | Brasil | 2500304 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c02ec660-51b3-35b1-81fe-c18cee7530ea | -6.04452 | -41.93525 | 2025-12-27 03:49:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98545754-6b56-3aa2-9e9c-ee5d3dbf6aa4 | -7.03259 | -37.31294 | 2025-12-27 03:49:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2052584c-2b59-377a-b030-a367071f3705 | -11.39333 | -47.99685 | 2025-12-27 03:49:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3276231-eae5-3cd9-b507-cef37745293f | -7.6361 | -34.81838 | 2025-12-27 03:49:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6cda4bfc-1dde-39f4-a44d-f448d8e317ff | -11.167 | -43.31552 | 2025-12-27 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e9c36a35-8569-3d9a-952f-f0fc4f9ae627 | -11.84843 | -43.7915 | 2025-12-27 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfc22860-01e2-3328-8e46-69baadcd6d94 | -10.77397 | -45.01429 | 2025-12-27 03:49:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6af6d9b-1e55-3bc1-9afc-de43d7b57449 | -10.94518 | -49.42076 | 2025-12-27 03:49:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35d6e0fc-4329-3a10-83d0-cb5d163e44c6 | -12.16158 | -46.67485 | 2025-12-27 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ba6e048-789f-314a-a5bf-fd87dd1b2fda | -5.85694 | -40.34607 | 2025-12-27 03:49:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6e98ed34-97a7-340f-ad0f-41b64b67f848 | -7.72645 | -38.34623 | 2025-12-27 03:49:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4e0372a5-3cb1-311c-8d03-a17badfece23 | -6.5483 | -43.105 | 2025-12-27 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80f2b9ef-a24f-3f88-a065-0bd01039905c | -5.9407 | -44.45782 | 2025-12-27 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6be869ad-d244-394a-be46-9e691e26ba65 | -11.01678 | -45.25889 | 2025-12-27 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 024de687-1dda-30d1-994b-07ee488fe823 | -7.08704 | -35.16182 | 2025-12-27 03:49:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cb6bc527-300c-3b20-a729-5a5e101b7bb0 | -11.39401 | -47.99738 | 2025-12-27 03:49:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0906dbcc-13a5-3dda-9d59-686bd5b14762 | -6.18326 | -43.41525 | 2025-12-27 03:49:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79fbdad1-ceae-311a-b5b2-da52af3e52c4 | -11.2808 | -38.20034 | 2025-12-27 03:49:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8bcb3fa3-5f3c-3bad-be3c-fe0d801cd07c | -6.10364 | -42.18438 | 2025-12-27 03:49:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2692ddf9-17e2-3ca4-9607-e4dbf87b7d6f | -7.86041 | -36.3879 | 2025-12-27 03:49:00 | NOAA-21 | SANTA CRUZ DO CAPIBARIBE | PERNAMBUCO | Brasil | 2612505 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1abf94bf-3a43-3bb1-867c-a0d6f1d9fbe3 | -9.94444 | -36.45023 | 2025-12-27 03:49:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f2206cb2-d7bc-3f34-afe2-1fdc0a4714b0 | -11.13261 | -44.28583 | 2025-12-27 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d2e5021-c826-3f45-806f-af016bce737f | -10.02444 | -42.33305 | 2025-12-27 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f473fa44-2afe-3b0e-9a7d-5d77d1088acb | -6.75688 | -35.16527 | 2025-12-27 03:49:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1cfb52e4-24bf-3601-940b-933816552949 | -6.6205 | -38.72289 | 2025-12-27 03:49:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6ee67c8a-a260-3844-8e19-561f79a15d4f | -5.45572 | -46.17654 | 2025-12-27 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d950fde-fc84-3b45-8811-f2e79f614553 | -6.71117 | -38.30899 | 2025-12-27 03:49:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c75f6c9d-5c58-374a-8d39-4c2d4b621d12 | -7.13824 | -35.14695 | 2025-12-27 03:49:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c3174b90-90de-3436-85eb-3bb268c87bff | -12.51172 | -43.69166 | 2025-12-27 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8020e46-8da3-3c66-b8d1-fb6634024a60 | -5.7516 | -45.11314 | 2025-12-27 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9df2e068-9cb9-30c9-a370-b4a68933cc08 | -7.15497 | -38.87209 | 2025-12-27 03:49:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b63fdeac-da5e-3d48-aeb2-68485708f801 | -11.1616 | -43.3222 | 2025-12-27 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 19678840-2de2-3a07-bfe9-88ba2a612cdd | -11.84744 | -43.73992 | 2025-12-27 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4f22606-0981-3980-80cf-f787826d2023 | -10.87094 | -44.608 | 2025-12-27 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a30fe37f-8ba3-3f77-a17c-abda6b3fc440 | -10.54095 | -37.58224 | 2025-12-27 03:49:00 | NOAA-21 | FREI PAULO | SERGIPE | Brasil | 2802304 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 451bf106-fc87-3aee-8f04-2db4514d1f62 | -12.15657 | -46.67385 | 2025-12-27 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea47fd2d-5705-3201-9d06-b2d809ece597 | -6.55335 | -43.10161 | 2025-12-27 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7e5a6596-e8ef-3c6c-b155-4a787b838a2e | -12.51582 | -43.6924 | 2025-12-27 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| edb89eea-987b-3792-b6d0-2c385f42de75 | -6.3205 | -39.9884 | 2025-12-27 03:49:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7c49dc4d-5fe9-3ae6-89eb-a891b1e46977 | -5.84685 | -40.01779 | 2025-12-27 03:49:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a5c91d12-e5d1-3de9-8575-eaee4d33e4db | -9.73283 | -40.36111 | 2025-12-27 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d9c702bf-a81e-36be-9f4a-ef993d6d3bbd | -7.6787 | -39.93843 | 2025-12-27 03:49:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 390fafa8-0d05-3d35-9d62-e0ce584b41d8 | -5.93064 | -43.51544 | 2025-12-27 03:49:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba8677fc-d261-3d31-a9ed-1e7fe884ac3c | -7.22659 | -43.07909 | 2025-12-27 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 24f297ef-4ce4-35f2-9261-6d9b516b6ff1 | -6.53818 | -43.11188 | 2025-12-27 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 323f085d-aebd-3d2f-a54a-4697e8cdb67b | -6.51911 | -39.19552 | 2025-12-27 03:49:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ffb7284d-3353-3ca0-8b98-708fe3a9f5d6 | -12.50853 | -43.6914 | 2025-12-27 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d35699b5-b4a4-362e-af94-7378138789a5 | -11.16765 | -43.31184 | 2025-12-27 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 17b01635-d088-3f2a-875b-6be141130c1e | -6.65959 | -35.47415 | 2025-12-27 03:49:00 | NOAA-21 | BELÉM | PARAÍBA | Brasil | 2501906 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d2c74a0a-f2d5-33dd-99f1-2f53e4387a84 | -11.1039 | -49.09963 | 2025-12-27 03:49:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2bc890c-483f-3317-b344-431653666f3d | -11.84988 | -43.73594 | 2025-12-27 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 515d37a5-029e-3194-9c3c-17ddece0ca20 | -5.98632 | -39.50002 | 2025-12-27 03:49:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c320160b-9eeb-3d9e-8dfa-d3d27c7c77e0 | -8.91307 | -38.43608 | 2025-12-27 03:49:00 | NOAA-21 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 168c2ee7-a8f7-3b65-8971-cd7029a15325 | -10.53817 | -48.71075 | 2025-12-27 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba97ea6b-9182-356b-8b3f-9d11832f496d | -11.39473 | -47.99355 | 2025-12-27 03:49:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1eeb7144-c948-393e-bc84-58aa4566b7a7 | -11.01465 | -45.25474 | 2025-12-27 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 556bce0e-ea03-3c97-8922-f3368696f3c4 | -6.75632 | -35.16891 | 2025-12-27 03:49:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bfa4c14b-5c67-3457-9534-4773382875ce | -12.75755 | -41.94397 | 2025-12-27 03:49:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 81df948c-8541-382a-b21b-fe7c126d4cf9 | -12.90335 | -43.77835 | 2025-12-27 03:49:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cc1eb34-6f14-336e-903d-64792b88a571 | -10.02053 | -42.33237 | 2025-12-27 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f3ca1fe7-cb2c-36e8-abc2-a909eb6beb53 | -5.93142 | -43.5109 | 2025-12-27 03:49:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fc243a0-ec06-3dee-a463-c60b8ae9bef9 | -10.95125 | -49.42208 | 2025-12-27 03:49:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| df89e52b-cc1f-39b9-bfc6-bc2a6c110152 | -5.44968 | -46.17892 | 2025-12-27 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98d9735e-159d-39de-b44e-0b68d7e80d3f | -0.0828 | -51.2738 | 2025-12-27 03:50:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 30dd75ac-1d58-3de7-9f61-877c203fa5b8 | -13.80332 | -41.80217 | 2025-12-27 03:51:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e8a0c497-278e-393c-9157-0e410fc52aab | -20.1882 | -43.63902 | 2025-12-27 03:51:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 46c88ce9-e10e-341a-b579-940301994d60 | -20.21893 | -40.29402 | 2025-12-27 03:51:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 85069f3c-45f6-38ee-bf4e-5da9614d6de6 | -15.15441 | -39.87632 | 2025-12-27 03:51:00 | NOAA-21 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README6.md)
