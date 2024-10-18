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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d275f8d-0798-34ea-bb19-19240f754e78 | -17.8045 | -57.4861 | 2024-10-18 03:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| d96bfa7c-0ea7-363c-b9ad-13176263f348 | -17.8049 | -57.4655 | 2024-10-18 03:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 9773b724-60f8-322e-b727-f47882bf2c34 | -17.9234 | -57.451 | 2024-10-18 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| f1162799-fff4-3cea-bc67-85a28a348dca | -18.0434 | -57.3539 | 2024-10-18 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.1 |
| a465fed8-aac4-3f93-a083-0a3d8b7f8841 | -18.0629 | -57.3721 | 2024-10-18 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 602e5ee8-c0d3-32d8-8502-7d529f543f21 | -18.0632 | -57.3514 | 2024-10-18 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.7 |
| 51bcb183-945f-3fc6-9427-d1d642d4c433 | -18.083 | -57.3489 | 2024-10-18 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 172.3 |
| ffc64c8b-95dc-3ff7-b160-5613212b550a | -18.2533 | -56.6446 | 2024-10-18 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 7a097cc2-9946-301a-ab53-0655a4496ce7 | -18.2537 | -56.6237 | 2024-10-18 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.1 |
| 9d267387-0f73-3786-9ec1-7c67c34b2b53 | -18.2735 | -56.6211 | 2024-10-18 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.0 |
| eb6b1cc2-c7dd-3204-bd80-ff114420763e | -22.968 | -49.5286 | 2024-10-18 03:07:12 | GOES-16 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.7 |
| 433ef845-01f1-3dff-ab92-ce6b83efa92c | -19.64577 | -40.77872 | 2024-10-18 03:08:00 | NOAA-21 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| e40a3ed8-f75a-3519-a563-15e738bb7138 | -19.64467 | -40.78352 | 2024-10-18 03:08:00 | NOAA-21 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 13f80097-34b0-3713-9757-cc94e3971107 | -19.37056 | -41.61427 | 2024-10-18 03:08:00 | NOAA-21 | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f939f0cc-4820-30c9-a1a4-0e1ae76ee9d9 | -19.36463 | -41.61083 | 2024-10-18 03:08:00 | NOAA-21 | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| db447bae-271d-3417-8354-fe0860cf0d80 | -19.286 | -41.4515 | 2024-10-18 03:08:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f8fe4c48-483f-3061-b991-1bf57847ead2 | -18.60225 | -40.99969 | 2024-10-18 03:08:00 | NOAA-21 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 72df373b-3c2b-3e99-ae24-fc49a7226be4 | -18.60096 | -41.00531 | 2024-10-18 03:08:00 | NOAA-21 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3fa51f44-7eed-3f90-b255-d79f2f7e372d | -18.55459 | -40.94969 | 2024-10-18 03:08:00 | NOAA-21 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 3a82e8e4-ddcc-3ea9-80a9-99a1ca7c12e5 | -18.39375 | -42.20747 | 2024-10-18 03:08:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8a3461d9-ac43-3c4c-b327-4f2431b00434 | -18.387 | -42.20607 | 2024-10-18 03:08:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 4465a352-0b52-3f80-a362-419dc54d481b | -18.38038 | -42.20414 | 2024-10-18 03:08:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 76c7f887-f323-30d7-9d90-16c7a491d0f4 | -18.10344 | -42.72532 | 2024-10-18 03:08:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 62874451-e3d3-3197-84a2-753c1c8ae926 | -18.09833 | -42.66009 | 2024-10-18 03:08:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 1957bc1a-40bf-3abc-8380-b76e75e48e0c | -18.09697 | -42.66063 | 2024-10-18 03:08:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| f990973a-f6ec-3d43-9b3f-3ee40852121b | -18.09687 | -42.72214 | 2024-10-18 03:08:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 8b2d82e1-5e1d-377d-9ea7-6900b0dd2f9e | -17.96514 | -42.51622 | 2024-10-18 03:08:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| dd8bdef5-c279-3dd7-b9e8-2e362ee3faab | -17.96478 | -42.51886 | 2024-10-18 03:08:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 54d83e68-c89e-38c7-a9bf-0cbc115864da | -17.95918 | -42.51187 | 2024-10-18 03:08:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 6896d715-19d4-38c7-9c98-a0e0ff3bc8ae | -17.83103 | -42.32135 | 2024-10-18 03:08:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ff5cc165-5dad-39cb-822b-823de35cd445 | -17.83068 | -42.32071 | 2024-10-18 03:08:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4a3fd311-2ea3-388f-bbf6-f49ac99b2616 | -17.82487 | -42.31702 | 2024-10-18 03:08:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5b5d9fd0-93fa-3012-bcf2-dc0d220672b1 | -17.82452 | -42.31629 | 2024-10-18 03:08:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 213f84d5-74d2-3d50-ba67-32d1b8512177 | -17.82353 | -42.32261 | 2024-10-18 03:08:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 2d8fe974-f75f-38db-af14-31dc45fc48bf | -17.82324 | -42.32178 | 2024-10-18 03:08:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 5f2b5ef9-b82c-3cbe-9a9e-ca630ac5e663 | -2.4644 | -48.9745 | 2024-10-18 03:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 037a4624-c9e5-34c7-9e54-d455c6481061 | -2.7045 | -54.656 | 2024-10-18 03:15:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ccfe91c1-190d-32f5-b322-d5f266fed4a7 | -3.7009 | -45.9 | 2024-10-18 03:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c416acfb-6d69-311d-88f4-508adb832bc5 | -3.9078 | -42.4256 | 2024-10-18 03:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 4dc4fe2b-8c1f-3b8e-a77e-c4ffd9c65317 | -3.908 | -42.402 | 2024-10-18 03:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 167.2 |
| eb84650a-a0a8-396c-a3ab-266326593f01 | -3.9265 | -42.4246 | 2024-10-18 03:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| b14438d0-c2a3-373f-9f5b-39077da76b2e | -3.9267 | -42.401 | 2024-10-18 03:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 206.0 |
| 368e8fcd-9c11-3862-b053-20316f6462c6 | -4.4258 | -45.9763 | 2024-10-18 03:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 7693ee93-f7f9-3c44-8633-abead39726e4 | -7.7279 | -34.9243 | 2024-10-18 03:15:49 | GOES-16 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 77.1 |
| cd81bc5f-1c90-3d8e-a000-51b7d6ca0b27 | -9.962 | -67.4394 | 2024-10-18 03:16:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8e8a4e9b-897b-30f2-b3c4-d0f416c74ce5 | -12.5048 | -55.1846 | 2024-10-18 03:16:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 7518920a-2475-345b-b866-31e15e4884ff | -12.4966 | -63.2066 | 2024-10-18 03:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 5597b304-dda8-374d-9908-9d60a3619087 | -12.5155 | -63.2055 | 2024-10-18 03:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 77a3f108-2e05-351c-b3eb-8caa3f88243e | -17.3873 | -40.4343 | 2024-10-18 03:16:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 81.7 |
| 775cf2c9-b6e7-3b91-be33-93d94210a2da | -17.2177 | -57.3102 | 2024-10-18 03:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 2708564b-3ac0-3868-8ae6-bea2e70ec205 | -17.2373 | -57.3079 | 2024-10-18 03:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.7 |
| 2cadb7e2-cbde-3177-9046-7393e9e3ba25 | -17.9234 | -57.451 | 2024-10-18 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.1 |
| 27be3cd9-ee9a-3639-9dfa-4f127d82f875 | -18.0632 | -57.3514 | 2024-10-18 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.2 |
| c184665b-99af-3e4c-a232-6d71ab115e5a | -18.083 | -57.3489 | 2024-10-18 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 8db77611-c0e6-369a-b30d-f2e35684e87a | -18.2533 | -56.6446 | 2024-10-18 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.3 |
| 1424cf2b-1d40-3a32-8417-a32994525072 | -18.2537 | -56.6237 | 2024-10-18 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 181.1 |
| b4f38eeb-7030-390f-b1eb-9616def69c83 | -18.2731 | -56.642 | 2024-10-18 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.9 |
| db2f33f1-4a09-348d-8375-09cb6349e375 | -18.2735 | -56.6211 | 2024-10-18 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 50503088-73a4-3d70-b613-90cf9ea2b1bd | -19.5804 | -57.0281 | 2024-10-18 03:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.7 |
| 2607f6ed-94f8-3fca-a264-79f8323f3976 | -19.5808 | -57.0071 | 2024-10-18 03:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.2 |
| 9b732814-2bf9-33ca-9d14-4bc304937cf2 | -19.6005 | -57.0253 | 2024-10-18 03:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 180.4 |
| 67592b56-ad34-392a-a785-eb0120408888 | -19.6009 | -57.0044 | 2024-10-18 03:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.7 |
| c6df06a0-5555-32a1-8a78-540a00b63961 | -19.6206 | -57.0225 | 2024-10-18 03:16:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 4ed11edf-f45d-33e9-839f-7e830a6a4145 | -19.621 | -57.0016 | 2024-10-18 03:16:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 975da445-45be-30e7-afb8-16ba3eaa44d0 | -22.968 | -49.5286 | 2024-10-18 03:17:12 | GOES-16 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.7 |
| a9bf1fc2-0134-3f33-ac1c-061d4aa1810c | -2.4644 | -48.9745 | 2024-10-18 03:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 9a18f4c1-59e4-3754-8fcb-482bbe45d0af | -2.4645 | -48.9532 | 2024-10-18 03:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 4bbd241c-0901-353a-9271-0377d02f6397 | -3.7009 | -45.9 | 2024-10-18 03:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| c7e8167b-ddf0-3a2d-88a9-04f97592ddd7 | -3.9078 | -42.4256 | 2024-10-18 03:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 120df046-4a0c-3a74-8a1e-65e231753dbd | -3.908 | -42.402 | 2024-10-18 03:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 205.6 |
| d5b2ccd2-c08d-38a9-8cd4-f4cad939b7ed | -3.9265 | -42.4246 | 2024-10-18 03:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| b2589ff4-a90a-38db-aa25-d1eded4e92cd | -3.9267 | -42.401 | 2024-10-18 03:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 183.7 |
| 24e49759-10c5-377a-89cf-42e081efbd70 | -5.5716 | -44.8927 | 2024-10-18 03:25:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c8c59568-49ab-314b-ad22-720940de33f0 | -9.9619 | -67.458 | 2024-10-18 03:26:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 453855e0-ebab-3c5c-a936-749867adeaba | -9.962 | -67.4394 | 2024-10-18 03:26:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 73.4 |
| c8fd8ae9-9c9b-34fc-85bf-2054bb4f575b | -12.5048 | -55.1846 | 2024-10-18 03:26:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e59fe79d-429b-3f86-9cb6-3e2be4bfcd30 | -12.4966 | -63.2066 | 2024-10-18 03:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| dd9664ac-5362-3b22-877d-d8403bee6363 | -12.5155 | -63.2055 | 2024-10-18 03:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 23c46360-58ce-3594-a65b-a623ec17d27f | -17.3671 | -40.4397 | 2024-10-18 03:26:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 97.8 |
| e7a6659c-1146-346b-97f5-6d9f3fa742a2 | -17.3873 | -40.4343 | 2024-10-18 03:26:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 102.6 |
| d25a7c4a-a50f-3dd0-8169-eac7b255bb1c | -17.2373 | -57.3079 | 2024-10-18 03:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| d967cb8c-fa61-303a-ad03-a0c9295196a1 | -18.0629 | -57.3721 | 2024-10-18 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 93042b22-775e-320f-9019-906d25af2e0f | -18.0632 | -57.3514 | 2024-10-18 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 8e8ccaf4-cca0-32e0-912e-8e27bcb58ae2 | -18.083 | -57.3489 | 2024-10-18 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 467c7544-8447-3810-b1ae-32798f1105df | -18.21 | -56.8576 | 2024-10-18 03:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| b8c7a76e-33a0-39ef-8837-bfecdaec40ce | -18.2533 | -56.6446 | 2024-10-18 03:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.4 |
| bfdc5ab3-f9cc-3b28-8eef-65e11e3b8402 | -18.2537 | -56.6237 | 2024-10-18 03:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.7 |
| 40e730da-6230-3980-9f69-7ec5d15104e8 | -19.5804 | -57.0281 | 2024-10-18 03:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.1 |
| 5675afe6-95e1-3217-9ebc-4323f2da08a9 | -19.5808 | -57.0071 | 2024-10-18 03:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 6d12ba5d-ab30-3e0a-8c63-b3ec5c9ef2d2 | -19.6005 | -57.0253 | 2024-10-18 03:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.7 |
| 62f9aa92-fbb7-3b8e-8965-50bb148863c2 | -19.6009 | -57.0044 | 2024-10-18 03:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.6 |
| b6fe5195-52cc-3dc7-8405-d39ad6fb0c29 | -19.6206 | -57.0225 | 2024-10-18 03:26:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.8 |
| f9468b6f-57b1-3eb4-a4e2-db83040de954 | -19.621 | -57.0016 | 2024-10-18 03:26:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 508d87d1-f770-3cda-bbd5-4444d2161aa3 | -22.3413 | -51.861 | 2024-10-18 03:27:09 | GOES-16 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.0 |
| 1183e567-76bc-36f2-9af7-66cfbe0bbf38 | -5.16513 | -44.00101 | 2024-10-18 03:28:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97fe9a49-38a4-391f-be3c-3daa3eaa1a3e | -5.08585 | -44.25203 | 2024-10-18 03:28:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6308c677-044f-34f4-85fa-c6decab69f3f | -5.08478 | -44.2579 | 2024-10-18 03:28:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2508285-9c54-36c6-9609-8c1e167ff469 | -3.78388 | -44.77381 | 2024-10-18 03:28:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c9f2fc8-7ea5-3df5-aaa9-b40ab2b47f63 | -6.57165 | -35.12625 | 2024-10-18 03:28:00 | NPP-375D | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 696c2543-17fd-3403-9693-05f7bd92a41b | -6.54 | -35.15985 | 2024-10-18 03:28:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |


[Clique aqui para ver as próximas entradas](README22.md)
