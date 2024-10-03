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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02ec36f3-e93f-3ee2-98a5-b17dcacbfce7 | -8.8695 | -45.5066 | 2024-10-03 01:15:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| f73f691e-3b2e-3601-8b12-be34e9397154 | -8.9244 | -45.6367 | 2024-10-03 01:15:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 78def93b-ca33-3f56-aa6f-6e19b783d257 | -8.6488 | -66.7139 | 2024-10-03 01:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 2780ad4d-9d4f-32db-bb27-3978b9d745ce | -8.6675 | -66.6762 | 2024-10-03 01:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 75b4a468-6029-3577-bdfc-c78b2c075ab1 | -8.8926 | -62.3348 | 2024-10-03 01:15:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| c2b9e279-7e0b-3c0a-a655-62097940605c | -8.9976 | -67.4094 | 2024-10-03 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0ff3dafc-6f3f-33ad-9dff-62e852eb2142 | -9.0149 | -67.7423 | 2024-10-03 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 7469f1a8-28c3-3b7f-99d2-d9c014544c03 | -9.0334 | -67.7419 | 2024-10-03 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f190085a-e264-3621-a945-f4ee5d3aff5d | -9.0515 | -67.871 | 2024-10-03 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 667b4d1a-88ea-3cdc-ad95-f8b7e3830672 | -9.1566 | -61.6758 | 2024-10-03 01:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 78a1eb8a-e824-3df8-90a7-a6c4615da2e6 | -9.4574 | -40.3641 | 2024-10-03 01:15:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 2be73a7c-1abb-37f9-b8f0-88b9f8d09b4a | -9.1752 | -61.6749 | 2024-10-03 01:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 105.0 |
| ebaeb3f4-cd9d-3ef2-8dae-4830e4623ba1 | -9.1754 | -61.6558 | 2024-10-03 01:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ad3a876f-59a4-3106-8891-3d581deda6cd | -9.3839 | -61.0526 | 2024-10-03 01:16:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a694cb5d-42de-34f8-83d0-74e6fb2c4c09 | -9.4025 | -61.0517 | 2024-10-03 01:16:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| eeb5d2e6-9804-3c7a-8b06-22306c0de41f | -9.4368 | -64.5419 | 2024-10-03 01:16:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 0f4519ec-fe7c-3acf-b4ba-eb994044e8a6 | -9.468 | -62.3857 | 2024-10-03 01:16:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 8e4f6a94-02a5-3923-b102-915d643346eb | -9.4865 | -62.4039 | 2024-10-03 01:16:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 035b64f2-2573-3343-9230-7805843f794d | -9.4866 | -62.3849 | 2024-10-03 01:16:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 13ca2c9d-e671-30c8-a328-ceb5eaf1c898 | -9.4939 | -68.508 | 2024-10-03 01:16:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 6d5eaf62-e06a-324d-b51a-dcbe2b50dcb5 | -9.494 | -68.4895 | 2024-10-03 01:16:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 8deacb7e-3f5a-3808-a478-57128773bd13 | -9.5125 | -68.4891 | 2024-10-03 01:16:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 935c48e5-7232-3831-a8a6-afd0145cbdfc | -9.7173 | -64.2302 | 2024-10-03 01:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 78f09567-2064-3ba4-94b1-d3d1e4cf0302 | -9.9129 | -60.0807 | 2024-10-03 01:16:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 20470a7c-d0f4-3095-9204-f6ba71c3c87f | -10.1802 | -57.2848 | 2024-10-03 01:16:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| be588622-fea3-35ba-9511-4c6ab3c142df | -10.1804 | -57.265 | 2024-10-03 01:16:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 1439faed-a943-3c96-bda9-169d18b278b6 | -10.3319 | -67.9868 | 2024-10-03 01:16:05 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 41.8 |
| c89cceb1-385e-3ffb-9013-4b59017de176 | -10.3319 | -67.9682 | 2024-10-03 01:16:05 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 88f86844-1e28-3e39-bf11-9a75de8f239a | -10.3506 | -67.9677 | 2024-10-03 01:16:05 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b9f7b1e8-6ec2-3092-bef2-b92650ae90a2 | -10.8942 | -63.8971 | 2024-10-03 01:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a66ec0a4-63f1-3401-9d02-a18ecebcd916 | -11.2567 | -46.9123 | 2024-10-03 01:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 65f6fd00-ab91-3e5f-8a62-93f4936895fe | -11.2758 | -46.9098 | 2024-10-03 01:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 6b51aad6-e9e9-3fb2-a7a2-bcd7e13f96b8 | -11.6742 | -65.0172 | 2024-10-03 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 7743ee56-9aa0-35a3-b0f6-18e32d462a52 | -11.9876 | -57.1877 | 2024-10-03 01:16:14 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| e32a51bc-1fab-3f65-8f42-2f466f387b05 | -12.4038 | -63.0009 | 2024-10-03 01:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 1cf0f994-2527-3ce1-ab91-1c3cb0aa72e9 | -12.404 | -62.9817 | 2024-10-03 01:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 3431f13b-35a2-3026-a636-1dbc693f2b0e | -12.6484 | -63.1214 | 2024-10-03 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.0 |
| c7f054e3-7fa9-376d-aaf0-ec088e851b7c | -12.6486 | -63.1022 | 2024-10-03 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 4ad2733a-217e-3521-99de-c7ea954e7635 | -12.8049 | -62.497 | 2024-10-03 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| c04c2627-6aef-35ae-a39d-e30742729b5b | -12.8802 | -62.5503 | 2024-10-03 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 97.4 |
| ae74c8eb-dda8-377a-995a-01e9349481b7 | -12.8803 | -62.531 | 2024-10-03 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 38c9ad00-0ba1-357e-8ac9-15c775f54493 | -12.8991 | -62.5491 | 2024-10-03 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 111.0 |
| d46c9163-4633-3b9c-8663-a7c2d9db66fd | -12.8993 | -62.5298 | 2024-10-03 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 104.5 |
| c38a034d-a54a-3eab-8a6a-f6d40d332dbc | -12.9167 | -62.7022 | 2024-10-03 01:16:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 1ff918c4-287c-35cf-a63f-ac624a43b0fe | -13.5195 | -51.1467 | 2024-10-03 01:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 858460a7-a481-309b-9092-49892115240e | -13.5198 | -51.1252 | 2024-10-03 01:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| cff09538-ba8e-3eb4-9797-a9f2b25f9ba0 | -13.5562 | -51.2489 | 2024-10-03 01:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 85697e1e-1098-3d1d-b3be-e025e5b75c80 | -16.5585 | -58.2204 | 2024-10-03 01:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 929f2256-2df8-33be-b25a-c93d4c34fc2e | -16.578 | -58.2183 | 2024-10-03 01:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| 6ca29074-0224-3c96-a6a4-cb102c8d1ffb | -18.8935 | -41.199 | 2024-10-03 01:16:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.1 |
| 449c9a3e-86bb-34c8-b3d1-558750291bd1 | -19.0344 | -43.1944 | 2024-10-03 01:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| 3a2956fb-bab0-3eba-996d-7d87460309ec | -21.3328 | -48.8277 | 2024-10-03 01:17:03 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.9 |
| 3aaab5ac-1072-34c6-8f76-6c6f74f69b46 | -21.3528 | -48.8462 | 2024-10-03 01:17:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 99f938d4-7ea5-3044-940e-dfae86ba2efc | -21.3534 | -48.8229 | 2024-10-03 01:17:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 196.7 |
| b088d11e-4d6c-3182-a17d-595709f7d399 | -21.3868 | -47.6734 | 2024-10-03 01:17:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 7b27a146-7868-350f-a4dd-80762dcdc1be | -21.3875 | -47.6497 | 2024-10-03 01:17:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c07150d4-7053-3e29-a99e-4ca6cc115c2a | -21.3734 | -48.8414 | 2024-10-03 01:17:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 3b64cd88-a06a-3ae1-b909-7f5ce69fb781 | -21.3741 | -48.8181 | 2024-10-03 01:17:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 1ef73d82-c459-34de-9370-1b3009e75ad5 | -21.346 | -55.6626 | 2024-10-03 01:17:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 110.1 |
| cf17dff7-cad6-38c2-a75a-db3a3e6414b1 | -22.2515 | -48.4456 | 2024-10-03 01:17:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 94b802e5-3f8f-32f2-be24-89ddd90746cb | -22.3495 | -47.9515 | 2024-10-03 01:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 1b9521af-8744-34ff-bc44-1ccc2c9e399b | -22.3502 | -47.9278 | 2024-10-03 01:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 7a6b6f60-97e3-332f-9349-00ce68be0e16 | -22.3704 | -47.9462 | 2024-10-03 01:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 43d561e8-dd07-3dc1-a31e-778f5a36d477 | -22.3711 | -47.9225 | 2024-10-03 01:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 142.1 |
| e0f8789c-16b7-36b4-99c5-bcf35b131572 | -22.3719 | -47.8987 | 2024-10-03 01:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 71.8 |
| f451ccca-921d-382c-b780-aebaf3c6233c | -22.446 | -46.8576 | 2024-10-03 01:17:09 | GOES-16 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 6f6520d5-d031-3b67-9bac-5bba731f7e5f | -22.6062 | -42.1712 | 2024-10-03 01:17:09 | GOES-16 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 128.0 |
| 3a5659ce-1be6-336a-9b6d-967831a6a383 | -22.6275 | -42.1643 | 2024-10-03 01:17:09 | GOES-16 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 120.1 |
| 4f70f002-b68d-3715-9dd3-9738d1146ba2 | -2.9616 | -54.6503 | 2024-10-03 01:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 14c3d601-5f6c-3d1b-a976-c053e00b33a8 | -3.404 | -42.2858 | 2024-10-03 01:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 2a4d818a-7337-3d52-9534-9db72f13fd34 | -3.4042 | -42.2621 | 2024-10-03 01:25:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| d8504d90-00a0-3f61-846c-ffe2490f803d | -3.4227 | -42.2849 | 2024-10-03 01:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| e6b285c5-ad40-32d3-afff-ad14f03504af | -4.0949 | -48.4894 | 2024-10-03 01:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| c06d3bf5-a144-32dd-8d23-8bbc9513f6ca | -4.095 | -48.4679 | 2024-10-03 01:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| bdf0a764-1642-3a37-9cde-9efff938ae74 | -4.1134 | -48.4886 | 2024-10-03 01:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 6ee328eb-6835-3791-8962-a18e47b77063 | -4.5375 | -43.304 | 2024-10-03 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 150.4 |
| ac125284-b0a3-381a-b696-559a01ee84fd | -4.9264 | -43.79 | 2024-10-03 01:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 8d2bc58a-8e6e-3b9f-bc7a-1cbbb194e256 | -4.9265 | -43.7669 | 2024-10-03 01:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 57c6c661-0ba1-36e8-8ebf-f228ec7b4461 | -4.9451 | -43.7888 | 2024-10-03 01:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 62f2aa5a-5b20-3347-9a1e-c8ae55b14d97 | -4.9452 | -43.7657 | 2024-10-03 01:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 2401a9e8-2098-39ec-aa39-1a46abb730d4 | -5.2441 | -43.8151 | 2024-10-03 01:25:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| de0281a9-c751-3dae-89d3-40bb507267b6 | -5.2443 | -43.792 | 2024-10-03 01:25:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 39fd8c1f-9289-3a06-bed9-6adf833d77cc | -6.7112 | -59.1345 | 2024-10-03 01:25:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| d907d2c4-5cde-3d6a-afc2-2d53b089c1a6 | -6.8777 | -59.0504 | 2024-10-03 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| f73b12a6-58d5-3f65-81dc-8b547541444f | -6.8778 | -59.031 | 2024-10-03 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 07c625b6-40d2-389b-9705-e656bc435e9c | -8.8506 | -45.5086 | 2024-10-03 01:25:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ebf7c7bd-ebe6-37e8-9fd7-17434e3bdf31 | -8.8695 | -45.5066 | 2024-10-03 01:25:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 38057229-473c-3549-b530-fcc203fdd308 | -8.6675 | -66.6762 | 2024-10-03 01:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| af68d5c5-535e-3db1-ae22-e267ca7172dc | -8.8926 | -62.3348 | 2024-10-03 01:25:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e908b32b-d3c1-31f5-a872-d97000738f40 | -8.9976 | -67.4094 | 2024-10-03 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d297a64a-e5c2-3f38-9ef6-b157104e32bc | -9.0149 | -67.7423 | 2024-10-03 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 210d0af0-e43c-3d13-b1c1-fd12b1167f71 | -9.0334 | -67.7419 | 2024-10-03 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| b1a8e569-24d1-3a85-980f-317c63e1a471 | -9.0515 | -67.871 | 2024-10-03 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| def81efb-54ad-3670-9841-7477cd7edbc6 | -9.0516 | -67.8525 | 2024-10-03 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| c705047f-ee6a-39b3-af5b-1ab46a84f43f | -9.1566 | -61.6758 | 2024-10-03 01:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 12291671-0409-3558-be86-a409b6b6fdfe | -9.4574 | -40.3641 | 2024-10-03 01:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 113.4 |
| 2d163c1e-bb8a-3c69-8b1a-f14bb77303e2 | -9.4765 | -40.3613 | 2024-10-03 01:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.9 |
| ed0b412f-b96a-333b-b3fb-bd855fa04383 | -9.1752 | -61.6749 | 2024-10-03 01:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 88.7 |
| a4336ba0-3043-3397-aa33-bf157e56f47c | -9.3839 | -61.0526 | 2024-10-03 01:26:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 900d86ad-0d06-3977-a0ee-fca45712cdd4 | -9.4025 | -61.0517 | 2024-10-03 01:26:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |


[Clique aqui para ver as próximas entradas](README35.md)
