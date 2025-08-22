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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33784bc9-6b1f-3a66-83b7-27242df177c9 | -9.09498 | -70.08836 | 2025-08-22 06:01:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25d6595b-23fd-3533-9938-e903be112d6a | -8.87707 | -62.42322 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e38102bf-25e5-36dc-a1a3-679b69036457 | -9.17093 | -59.71121 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aa64556-191f-308f-a95b-4892c082194f | -8.87244 | -62.41964 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b23e4bbf-5c3b-321b-8dd2-009696411380 | -8.88671 | -62.42754 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a672df2d-0eba-3466-acdc-d961e5a3d9d4 | -8.86476 | -62.40083 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eff71ec6-7278-37e4-b6bd-570a93a3d5bb | -9.51387 | -60.55042 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b51facb-5111-3651-bece-266c32c7b4ce | -8.65845 | -70.03779 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ceaaf79-d7c8-3b5c-b191-13b6227944e0 | -8.6729 | -69.72676 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dce4f994-e0ef-3ee3-a8d3-5ae549f6f53b | -8.61091 | -62.61623 | 2025-08-22 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 762514f0-3bab-33e4-93dc-e9be130ebe0b | -8.42422 | -70.70657 | 2025-08-22 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a63f9ff-6131-3948-aa1b-b06e1a1450a3 | -9.21661 | -59.78576 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5c061b4-5805-3bfa-bebd-14d86160e4aa | -9.1019 | -61.43121 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e3fd697-827a-378c-a17e-08af0464ee0a | -8.87827 | -62.41446 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d984fdca-f319-33e0-b0d1-1f8cd877bf34 | -8.55251 | -66.95289 | 2025-08-22 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8939820a-015e-3d6f-b8b0-9df52e324334 | -7.7176 | -66.91843 | 2025-08-22 06:01:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5439c245-7eb5-3a26-a23c-db26063bd1ec | -9.94976 | -60.17916 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54d3a5cf-b1eb-3ea4-a10b-bd3632c47f35 | -9.30874 | -57.01728 | 2025-08-22 06:01:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b2ae798-cd67-3ccb-94fa-e103316e6bb9 | -7.757 | -70.15578 | 2025-08-22 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56d138b3-0e67-3448-9470-9776e36fac5c | -9.15911 | -59.59868 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4253ce07-5e42-3be7-981a-6c009bbb6cc2 | -14.78743 | -59.67033 | 2025-08-22 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e01f1131-5a16-3741-9eca-0c532d474495 | -8.87204 | -62.42256 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d89222b3-774f-31d7-aef3-d9867e880ba6 | -8.42753 | -70.70711 | 2025-08-22 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a2e3b39-dab1-3f9b-bc16-858272d7d64e | -9.1946 | -65.6653 | 2025-08-22 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bff5ea9-64d6-3568-a6ca-d16773d9d585 | -9.15377 | -59.60104 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4074b48-a733-390f-a9a4-05bdcba39819 | -9.5122 | -60.51758 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a2a382c-91b5-39d6-a26b-1554bf213dae | -9.18733 | -59.62925 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 78101604-c13d-347c-80c5-f859e22dc997 | -9.21468 | -60.79339 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6aa364bb-8856-3f3f-b8ff-e94666e5900a | -9.21519 | -60.78954 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fb6f542-effd-326a-b7cc-a342015b0a9c | -9.20953 | -59.45155 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09de7bdd-159a-34b2-9ccb-2c0aec8119ac | -9.17979 | -59.59068 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5004e34c-1864-32e5-a9cb-b309408d90e5 | -8.87667 | -62.42616 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fa2da07-dcea-3e0e-b153-6ae7b0843878 | -9.52432 | -60.56014 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d948a3ea-86fb-33b2-a541-47a0e402a6b0 | -7.63342 | -69.94733 | 2025-08-22 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96b53165-291a-3632-b68d-688b88a6939d | -8.71368 | -69.46382 | 2025-08-22 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd406e3e-9676-37ff-9bce-37cfde2b135c | -9.19279 | -59.63498 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98aba38e-1fe3-3e60-a49a-08447ca4e6d5 | -9.1852 | -59.63519 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 24a180ff-a784-382b-9e87-4d6884a9b842 | -8.71088 | -69.45972 | 2025-08-22 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 83e2064c-4ed0-3f3f-9fd4-e6d4905ec3c6 | -9.18128 | -59.6283 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d462c416-b4b0-3e5d-b651-88ee5e6a6822 | -9.20894 | -59.45633 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6cd19ca7-b288-3d6a-b14a-d9280185f4dd | -9.50592 | -60.52095 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4f2a57c-f6eb-3bb3-94e1-5c96f82ae835 | -8.86397 | -62.40663 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 092db34d-12b1-3a3a-8b3c-8df0dbeecdc4 | -8.90784 | -69.43463 | 2025-08-22 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02d6d20b-7c63-3660-9c35-e5924fe39e85 | -9.15985 | -59.60184 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7965eef-15bf-386d-bee4-cd3e05921552 | -9.20121 | -59.46684 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 379a7f8a-08ce-3ae1-a91a-d5e17dbde47a | -15.8955 | -43.4523 | 2025-08-22 06:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 79.8 |
| bad13bd1-0de1-3bac-824d-86889ea310ec | -15.8955 | -43.4523 | 2025-08-22 06:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |
| dec184e8-a523-3ed4-b7b4-8c49e2d70340 | -14.8924 | -47.9665 | 2025-08-22 06:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| d254c749-5aa8-3ac3-9ed4-46682e48ee3b | -15.8955 | -43.4523 | 2025-08-22 06:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 99884f6b-2e12-3049-8062-81c8095441b2 | -15.8955 | -43.4523 | 2025-08-22 06:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 5c6a87f2-77f1-321d-be77-8a4844586752 | -6.3123 | -43.7572 | 2025-08-22 06:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 5fe6e667-0c01-3937-b475-84ef3a76498d | -14.8924 | -47.9665 | 2025-08-22 06:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 2bcba80e-4137-37b8-b20c-15a74b4dc3e6 | -14.8928 | -47.9439 | 2025-08-22 06:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 48e2d53e-1e25-39ca-988f-adb27bdd50a5 | -8.66438 | -70.03626 | 2025-08-22 06:52:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bb79d63f-0bde-3f56-9df4-c888112aa9f2 | -8.46865 | -70.09005 | 2025-08-22 06:52:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 648d0f5e-e815-3ddb-abbf-5aecb2fe6f87 | -8.66502 | -70.03806 | 2025-08-22 06:52:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 497f06ae-cc05-3df0-9f93-ab4784b3882f | -8.67133 | -70.0373 | 2025-08-22 06:52:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cee1180-8e65-376d-95d3-1cc13f6bfd05 | -8.65809 | -70.03696 | 2025-08-22 06:52:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad660421-9ff4-3657-a784-d34bf7c0075b | -8.89303 | -72.70748 | 2025-08-22 06:52:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d2fffcc-c9d5-3306-ac08-8a1fc5b7ae5f | -14.8924 | -47.9665 | 2025-08-22 07:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 3f07ba63-90f5-3a94-b77a-0d9a144d097f | -10.742 | -48.2401 | 2025-08-22 07:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| b6c548a5-2c8d-37c9-a105-e1e6633b5314 | -14.8924 | -47.9665 | 2025-08-22 07:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 5bbeea64-9725-344f-94ca-d51797464dec | -8.6607 | -70.03776 | 2025-08-22 07:18:00 | AQUA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 71b71589-ce1a-3abd-80ee-cb3f48b7e007 | -9.5217 | -60.53489 | 2025-08-22 07:18:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 7e563181-7a55-33bd-bce4-6a7ab3a1ee54 | -7.5809 | -63.43192 | 2025-08-22 07:18:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 74dd3a83-ad51-36bf-b4f6-ccc859911017 | -14.8928 | -47.9439 | 2025-08-22 07:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 717d08d4-5667-30d4-b715-a99206e53152 | -14.8924 | -47.9665 | 2025-08-22 07:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d4735c37-e8bf-3c24-b668-f263d344c040 | -14.8928 | -47.9439 | 2025-08-22 07:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 125555bf-971e-3fb0-8853-49059da64705 | -14.8924 | -47.9665 | 2025-08-22 07:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| c4a0e608-739f-3834-82f3-18513bc786c5 | -12.9921 | -45.2252 | 2025-08-22 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 0982889f-634d-33bf-93e3-7ee8b774dd50 | -14.8928 | -47.9439 | 2025-08-22 07:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 836458e0-8156-3095-a019-fb36fc343c3b | -14.8924 | -47.9665 | 2025-08-22 07:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 100.8 |
| df8c2ff6-1d4a-3a2f-b27b-6e61dfda7bbc | -14.9119 | -47.9632 | 2025-08-22 07:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 7f874f60-57c8-3fcc-9117-f58bad4e4797 | -14.8924 | -47.9665 | 2025-08-22 07:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 115.0 |
| c3de47c0-fba9-3db1-89c5-b347f5b0e7c1 | -14.8928 | -47.9439 | 2025-08-22 07:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| f4671799-1952-3814-88a7-3e641e777463 | -14.9119 | -47.9632 | 2025-08-22 08:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| e6010bb8-5fad-30bf-8a3d-f5656c11a705 | -14.8924 | -47.9665 | 2025-08-22 08:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| bb4c441f-0de6-3691-a0ce-3824a9d26321 | -14.8928 | -47.9439 | 2025-08-22 08:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 517cae3d-495f-3c3b-8b8b-626aaf080c30 | -14.8924 | -47.9665 | 2025-08-22 08:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 5af12c96-8653-3969-a646-894917c934b7 | -14.9119 | -47.9632 | 2025-08-22 08:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| bce2e83c-2edd-34fc-b9a7-237dd85f4ba2 | -14.8928 | -47.9439 | 2025-08-22 08:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 0972f793-4a1b-361e-b543-7b9b6527b2f9 | -14.8928 | -47.9439 | 2025-08-22 08:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 7303e622-0c0b-37c6-a5cc-17c48408b026 | -14.9119 | -47.9632 | 2025-08-22 08:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| df456a20-a511-3257-967c-2a3b50eb28fc | -14.8924 | -47.9665 | 2025-08-22 08:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 115.6 |
| b4bd6988-256e-3b73-8539-7a7eb53c30c0 | -14.9119 | -47.9632 | 2025-08-22 08:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| bcf5b980-efaa-3def-a449-656a8b744a1c | -14.8924 | -47.9665 | 2025-08-22 08:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 1a874a8d-0805-3b84-b0a9-838993007135 | -14.8928 | -47.9439 | 2025-08-22 08:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 1c7d1dba-ae76-3557-9912-59bef4e11464 | -14.8924 | -47.9665 | 2025-08-22 08:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 95f3e3dd-e7f9-3e2a-8524-8508f55fb1e3 | -6.5573 | -45.5209 | 2025-08-22 09:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| f23482cb-99b9-321b-b3b1-6b644cc55e2a | -12.9925 | -45.202 | 2025-08-22 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 2f60f2b8-f37a-3530-91c9-0bc96d7a8c45 | -12.9921 | -45.2252 | 2025-08-22 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| d6dfde52-cf33-30c6-8730-555f85389175 | -12.9921 | -45.2252 | 2025-08-22 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 35c47307-2ead-3892-9659-bc40a1417581 | -12.9925 | -45.202 | 2025-08-22 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 3f3a12c3-b346-343b-ad56-02f2544cc2bc | -10.876 | -50.8163 | 2025-08-22 11:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| a1eeb21e-b07c-3fef-ac12-83032536964c | -10.8571 | -50.8183 | 2025-08-22 11:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| dd8581a2-bda4-3317-8db3-13ed2703954e | -6.4266 | -45.4861 | 2025-08-22 11:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 0cf940e9-7aff-36c1-8075-8423b43c0a9a | -12.3129 | -50.0097 | 2025-08-22 11:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ac761795-10d7-33a7-bb93-955bc30058d8 | -12.9925 | -45.202 | 2025-08-22 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 57197969-29b3-35a6-b554-2eeb1fed5ee7 | -7.102 | -43.6875 | 2025-08-22 11:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| c5c0d3ed-4d2b-3487-a21e-360387da7ac4 | -12.9921 | -45.2252 | 2025-08-22 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 190.1 |


[Clique aqui para ver as próximas entradas](README64.md)
