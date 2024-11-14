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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d87f51a4-7ab7-3b31-9c16-6c3d96e60dff | -3.77221 | -41.59464 | 2024-11-14 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c0d52773-9c6a-37b3-957f-b3358cb3ff0f | -3.76957 | -41.6048 | 2024-11-14 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0b19f001-dab1-35be-a974-e62b7552f25c | -5.94109 | -43.78217 | 2024-11-14 03:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20c9dfdd-3508-32bf-aa51-c31dfb3b8a8d | -3.77125 | -41.59999 | 2024-11-14 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 8af71386-f0e3-368b-b086-c3345b9bad88 | -6.04002 | -44.03701 | 2024-11-14 03:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d56957e2-1fcc-33f3-86a2-783804f36987 | -7.07329 | -38.88167 | 2024-11-14 03:21:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c50389f5-82db-31ee-9fd1-86943ac75cf8 | -3.77597 | -41.60589 | 2024-11-14 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 68c8ee6f-b15d-39a0-bae6-0dcbe37a90fc | -3.77029 | -41.60538 | 2024-11-14 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a4201f55-d65d-3e7b-8790-c8a0fbac4983 | -6.95899 | -39.82945 | 2024-11-14 03:21:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f6fd518f-b6ce-3a2e-8aa2-2ac5740014dc | -5.35219 | -43.54833 | 2024-11-14 03:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0ef8b3d-49bd-3127-b2eb-dd87236005ab | -8.81621 | -35.6782 | 2024-11-14 03:21:00 | NPP-375D | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 0564814e-a58b-3f72-ae83-ccad1404b114 | -6.04587 | -44.04508 | 2024-11-14 03:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| d80d4d2c-d183-3cea-9930-330baf5b3296 | -9.28934 | -35.94926 | 2024-11-14 03:21:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8ea48fb2-6a6d-30a6-b762-a684feb2b1ad | -6.53064 | -35.26517 | 2024-11-14 03:21:00 | NPP-375D | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a4c5b89d-5ae6-330e-b94c-3b3af9dced5d | -6.96441 | -39.83041 | 2024-11-14 03:21:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8453bf58-dc2f-3dd7-940e-5e615d143421 | -6.96377 | -39.83406 | 2024-11-14 03:21:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5f7d642d-fc0a-36ed-88f5-b6d0999cfa3f | -7.78965 | -37.59782 | 2024-11-14 03:21:00 | NPP-375D | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 92a0af46-d212-3478-8932-7e1c18c3446a | -5.81562 | -35.38417 | 2024-11-14 03:21:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| be2cc062-171a-3574-9240-1f9b1b653c91 | -9.10401 | -43.1958 | 2024-11-14 03:23:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d47279be-dc29-3fbf-9077-9941f537ff38 | -10.25421 | -36.46407 | 2024-11-14 03:23:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b1caa249-cd1e-37f9-a608-f75bd5cfb38d | -9.93102 | -37.62137 | 2024-11-14 03:23:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9bfea70a-2a8d-3ea9-a754-5987b1267a0b | -9.10503 | -43.19052 | 2024-11-14 03:23:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 59f3091e-d900-3501-abba-dfb359aab998 | -10.04504 | -38.14402 | 2024-11-14 03:23:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 72056502-c055-347a-983a-6e1f94a1e323 | -12.77818 | -38.50063 | 2024-11-14 03:23:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2ac6ae27-5a10-353e-9959-70a08da20bd5 | -10.25485 | -36.46039 | 2024-11-14 03:23:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0b5c8def-d2c4-37ba-8050-3af13ce0a654 | -10.18556 | -36.1842 | 2024-11-14 03:23:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e10a524a-9311-3a46-9e08-d470a8f78319 | -10.38713 | -39.12894 | 2024-11-14 03:23:00 | NPP-375D | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 623c43d9-999d-3c38-a14d-55a0c6d63fa8 | -12.77904 | -38.496 | 2024-11-14 03:23:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2f533202-93ef-37a0-ba51-64e758fc2fc9 | -9.93181 | -37.61686 | 2024-11-14 03:23:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f69f2389-da28-3316-9bab-bcd11b9c6e37 | -13.74426 | -40.57964 | 2024-11-14 03:23:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9e1085f3-22f5-3829-866e-1d4226525358 | -20.69428 | -48.80362 | 2024-11-14 03:25:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 01c0a556-19fd-3426-bb37-bb0c36217e12 | -1.8106 | -52.1652 | 2024-11-14 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 7ffeb20d-5655-3b77-96da-eb9f1f99cf97 | -17.6076 | -57.4893 | 2024-11-14 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.7 |
| 4fc66d40-0535-37ec-9335-f82217fa6532 | -2.2729 | -45.347 | 2024-11-14 03:30:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 92.6 |
| f56af8f1-8369-328a-8038-e788769d37f2 | -1.8105 | -52.1857 | 2024-11-14 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 304835ff-5535-3a59-9960-3fbb1f3521db | -1.3894 | -51.1197 | 2024-11-14 03:30:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 347bac32-de46-30ad-a795-99a841602077 | -17.6079 | -57.4688 | 2024-11-14 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| c38c3192-608b-3ad8-bab0-cfa66e77b854 | -17.2543 | -57.4698 | 2024-11-14 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| e70d7a03-84f2-3259-b79d-3c1911744dc6 | -17.5869 | -57.5533 | 2024-11-14 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.8 |
| d537a33b-b4a5-37d7-88a0-81a250715f14 | 1.3034 | -60.4263 | 2024-11-14 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 69f05eb2-5379-30f1-b992-2a96376eab42 | -1.7921 | -52.186 | 2024-11-14 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 573730af-5893-37dc-a176-6e1bf4c08567 | -4.5616 | -47.9925 | 2024-11-14 03:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| f18db56a-a4d0-308c-a4e7-a1bd97de3dd8 | -17.5672 | -57.5557 | 2024-11-14 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.7 |
| 6a518c4f-c92e-3194-a682-b2bfddf75248 | -1.7922 | -52.1655 | 2024-11-14 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 12af6023-d05f-3617-ad0a-fb7d2cc07c61 | 1.0663 | -60.5985 | 2024-11-14 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 33cdadb0-3f3e-3bfb-80e4-46532b80ca4b | -17.6263 | -57.5486 | 2024-11-14 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.8 |
| d69feb69-bf87-3c0f-a7fd-d01da2245d9a | -17.6066 | -57.551 | 2024-11-14 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| dac3b80b-1fc1-3e37-b02d-69f6c1596e49 | -17.5675 | -57.5351 | 2024-11-14 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| f047c677-47cc-37c4-b57e-a6f400705c64 | -1.4078 | -51.1195 | 2024-11-14 03:30:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| cfd3ab1e-013a-3a06-b9da-58b737fa8930 | -17.5872 | -57.5328 | 2024-11-14 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 2e5f3b75-d80a-3d29-9918-3abfe80927d9 | -6.0472 | -44.0331 | 2024-11-14 03:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 1834740c-6d0f-335d-b4f7-5d9b36b99096 | -4.5614 | -48.0141 | 2024-11-14 03:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 50d8ab34-2e59-395a-839d-433280350691 | 1.048 | -60.5986 | 2024-11-14 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.0 |
| b0532b7d-5602-3ec3-ac4a-dcdd300f7cbb | -3.714 | -50.6046 | 2024-11-14 03:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 0ae166f2-6cfb-3678-b743-d0a40f5bcd6d | -1.7921 | -52.186 | 2024-11-14 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 2be1c6eb-4623-397a-8cd7-c6efbec318b1 | -17.2543 | -57.4698 | 2024-11-14 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 66d1a70f-9e38-37ce-a0b5-7ee27683d3bf | 1.048 | -60.5986 | 2024-11-14 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 2c0282e9-1c47-3f0a-a0a0-06a2e16e2ef3 | -17.5879 | -57.4917 | 2024-11-14 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| 5bf8ceb4-bf38-3be0-8bbd-f8ec9758237b | -1.8105 | -52.1857 | 2024-11-14 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 6b3396c3-38ae-38c6-bea3-833688bc5235 | -1.7922 | -52.1655 | 2024-11-14 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| e0facefe-ea57-3a41-9ed0-e33902906624 | -1.3894 | -51.1197 | 2024-11-14 03:40:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 01e30727-ffa7-3d54-93d8-7876da55665a | -17.5869 | -57.5533 | 2024-11-14 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.7 |
| 5fa08843-7ebc-3c27-9c43-72b1845d89d3 | -17.6066 | -57.551 | 2024-11-14 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 7922a0c5-8d4c-3bad-a309-144ad3fb2f44 | -17.5672 | -57.5557 | 2024-11-14 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.0 |
| f0809299-1165-304b-8f0a-4682aa03d442 | -4.5614 | -48.0141 | 2024-11-14 03:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 3ba4d389-1f43-3a45-90b2-a8a275675010 | -6.0472 | -44.0331 | 2024-11-14 03:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| e90ba418-a359-3ddc-880b-4cd3f19c82dc | -1.4078 | -51.1195 | 2024-11-14 03:40:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 441388d1-3fca-3b10-bbfb-69ab99075d99 | -17.5675 | -57.5351 | 2024-11-14 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.1 |
| 9a941d1f-0c54-3883-b90d-2daf6261bec5 | -1.8106 | -52.1652 | 2024-11-14 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 79eb7018-23bc-3718-beed-0b6d19755d0f | -17.5882 | -57.4711 | 2024-11-14 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.9 |
| b97622a1-39db-3ca7-be6e-ca52afaa8c39 | -17.5872 | -57.5328 | 2024-11-14 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 73633392-1266-3933-873d-f09aa652f92c | -2.2729 | -45.347 | 2024-11-14 03:40:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 10e19200-3b12-34e1-b7a3-0b428c4caaa6 | -17.7052 | -57.5392 | 2024-11-14 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.7 |
| ec962a47-c417-338c-82a6-64854f8c15a3 | -5.92382 | -42.9702 | 2024-11-14 03:46:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 5dc5a437-1949-3ebb-b0ed-3ce537423c33 | -2.37162 | -46.50435 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ad35768-da07-3ea8-adce-fabf55a4b7ff | -3.86653 | -43.9427 | 2024-11-14 03:46:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 115ba340-5481-3abf-a876-9c7d7e503ae8 | -6.80891 | -34.91853 | 2024-11-14 03:46:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c8afc1bb-93ff-3eb9-aae1-9190be22055d | -3.86746 | -43.93722 | 2024-11-14 03:46:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c76b4cc2-2810-3d42-ac02-fc43a44a294c | -4.29337 | -48.10534 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9a4d2fc-f54d-324b-b36b-13496adb6de3 | -2.02023 | -46.50423 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 586f9ae5-055c-3011-aa60-cd2974d16fc3 | -4.00467 | -45.57021 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d5fa8ecb-7c0a-3643-b5b3-2397d18434e3 | -2.64534 | -46.18013 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fb8c012-acf9-3bf0-91e8-1c3296fa3035 | -5.56285 | -45.36699 | 2024-11-14 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6e47d000-ba69-3002-a152-35c5e78694cd | -2.47677 | -45.85398 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 935817cd-3a4d-3dd6-b41d-0661f5be8390 | -4.52147 | -46.48306 | 2024-11-14 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc4acff8-5a16-3a7d-85cd-73e5f7555a3d | -8.07401 | -34.97911 | 2024-11-14 03:46:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| dc2caaf9-02bd-3974-a08e-6a66f474fec3 | -5.08441 | -45.98642 | 2024-11-14 03:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ddd7d6d-a507-316d-ae78-e05e48f31e6d | -4.44701 | -45.36943 | 2024-11-14 03:46:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87dd9fbf-9564-3ac3-a0da-25b6312b60b3 | -4.37233 | -48.079 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d241db4d-4c33-3729-9ef2-0a2a63edaa9c | -5.15147 | -46.08975 | 2024-11-14 03:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a97e4b8-d235-34cd-b953-2b9c766d3577 | -2.64095 | -46.17116 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77a96fad-a29e-31e6-b6ef-b35654451fd2 | -1.85246 | -46.28491 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15b82b1a-751b-3daa-bc91-b4ce8a517e8c | -5.19501 | -44.3607 | 2024-11-14 03:46:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f72e6a4-aa5c-36a6-8617-de946cbe5f8c | -6.04754 | -44.04058 | 2024-11-14 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| d7de61c7-cb8b-3a58-b91a-113d17dbdb30 | -3.99984 | -45.5658 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 06d810b4-4a3c-3507-a5b2-6bc52df7d531 | -4.45871 | -45.36465 | 2024-11-14 03:46:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 764573b8-5fa1-3915-9678-2c807f09c88e | -4.64821 | -44.14663 | 2024-11-14 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5862f343-ab24-3315-9770-a84160c9d475 | -5.47967 | -47.0092 | 2024-11-14 03:46:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a5461cc-16c7-3854-afda-d7054a720a19 | -4.51872 | -46.48687 | 2024-11-14 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6951bd3d-cc8c-3dd1-888b-1ff95e148866 | -2.192 | -46.35862 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README19.md)
