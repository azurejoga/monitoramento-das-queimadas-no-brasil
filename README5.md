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
| 9c39f4c4-5891-3c47-a27e-7db9047cfb67 | -8.0324 | -43.1022 | 2025-12-14 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| 3a6b2ba0-8cea-3fc9-9395-b5827838a314 | -8.0327 | -43.0786 | 2025-12-14 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.1 |
| c865e468-3da6-3d6e-865e-79624837c24f | -8.0696 | -43.1452 | 2025-12-14 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.6 |
| 4c31d40d-98b0-36a0-abf2-434b94a3b2f5 | -8.0327 | -43.0786 | 2025-12-14 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.0 |
| b874ad05-2249-309e-b8d3-c30462ff6da6 | -8.0324 | -43.1022 | 2025-12-14 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.3 |
| 6ccc846e-f3fb-3384-be30-5e3d093a8a32 | -8.0324 | -43.1022 | 2025-12-14 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| e34f1196-af5a-3f29-9bfe-82f96c73af54 | -8.26975 | -35.4868 | 2025-12-14 02:51:00 | NOAA-21 | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8a64e88e-8662-3554-a11c-5d6f0f86d2cd | -8.0324 | -43.1022 | 2025-12-14 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 81108e93-c375-3d83-96d5-a4b181a50460 | -8.0324 | -43.1022 | 2025-12-14 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.1 |
| ddf1162b-a0f0-3fc4-971b-8f717645203c | -8.0324 | -43.1022 | 2025-12-14 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.5 |
| 5782666c-7122-3a93-b946-016dc1ab156f | -5.67522 | -39.27408 | 2025-12-14 03:21:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| a169e324-e5dd-3705-8d52-c5a87cc53ed6 | -11.71491 | -37.64729 | 2025-12-14 03:21:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d9ca42cd-02b8-3cbd-9201-6b0d78d6335e | -6.80687 | -34.97858 | 2025-12-14 03:21:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 700bb73b-859d-368e-bd58-2eaead10d4ac | -5.34543 | -40.68697 | 2025-12-14 03:21:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 02d3f238-523d-3ba5-bcb4-44cb74c30b66 | -8.26822 | -35.48378 | 2025-12-14 03:21:00 | NPP-375D | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 53a213c2-0e79-365f-9b2e-a4851a55cea2 | -5.66938 | -39.273 | 2025-12-14 03:21:00 | NPP-375D | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 4f8bf09b-bbb3-3dcc-9f0b-a06c4c5cde53 | -8.03396 | -43.10319 | 2025-12-14 03:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 964b8e11-10c8-3ede-b2b0-b77f358bbede | -10.14661 | -36.2779 | 2025-12-14 03:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c7491484-a163-369c-9f4a-b5e638bd3b99 | -8.07134 | -43.15298 | 2025-12-14 03:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 096ede87-7862-385e-80f1-9eba8a233b8e | -8.06818 | -43.15395 | 2025-12-14 03:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 907ef308-5182-3377-9922-03556635cc93 | -5.35186 | -40.68802 | 2025-12-14 03:21:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 784d0a98-2dc5-38cb-bdac-f5971d836f00 | -7.91466 | -35.28479 | 2025-12-14 03:21:00 | NPP-375D | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 99ea0236-e275-3f80-b9dd-4095e13f9569 | -6.80257 | -34.97784 | 2025-12-14 03:21:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d81b818e-ef69-3ddb-a9a1-7bb8772c3ed8 | -6.07852 | -37.94364 | 2025-12-14 03:21:00 | NPP-375D | MARTINS | RIO GRANDE DO NORTE | Brasil | 2407401 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 13050e1c-b4a0-3deb-82e2-02e6f60380b2 | -10.14218 | -36.2771 | 2025-12-14 03:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 86bdd46e-9861-3e63-b0a9-8b750189c50e | -5.67451 | -39.27812 | 2025-12-14 03:21:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| f8a134eb-cd96-3315-a79d-81e6ace91b4f | -11.715 | -37.64589 | 2025-12-14 03:21:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8d918b7b-f8d1-32c8-bb9a-82a049d3a692 | -8.0753 | -43.15514 | 2025-12-14 03:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5b9a5274-8ab7-3699-931d-979c111ddd5d | -5.66867 | -39.27702 | 2025-12-14 03:21:00 | NPP-375D | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 88ec925a-01c2-3fd7-94db-f99ba0d00405 | -8.03531 | -43.0963 | 2025-12-14 03:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e9dd8042-6842-310b-b152-aabb5087381f | -5.34584 | -40.68744 | 2025-12-14 03:21:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2b8e9a82-2483-3e24-8d12-5df5d08dbc35 | -5.35227 | -40.68847 | 2025-12-14 03:21:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05f85372-7fde-3e49-ad78-14b7066f7246 | -6.07783 | -37.94753 | 2025-12-14 03:21:00 | NPP-375D | MARTINS | RIO GRANDE DO NORTE | Brasil | 2407401 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 106776c9-58f1-3761-b3e5-08eb3d9cbbc0 | -10.15027 | -36.28303 | 2025-12-14 03:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c69f89da-f3ce-3a6a-8a97-72360e83b3dc | -8.0269 | -43.10176 | 2025-12-14 03:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e225768-9170-3031-89ef-0b1162d29384 | -5.72802 | -35.52092 | 2025-12-14 03:21:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc819c43-87c0-3bea-9df8-418513724c25 | -7.91655 | -35.28492 | 2025-12-14 03:21:00 | NPP-375D | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| af56e2fc-8da2-3f68-aaaa-79c86319dd67 | -8.67871 | -35.61057 | 2025-12-14 03:21:00 | NPP-375D | PALMARES | PERNAMBUCO | Brasil | 2610004 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 88097a29-7753-32eb-bd60-78ce4ea36fdf | -10.14582 | -36.2823 | 2025-12-14 03:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 288572cb-9a21-32ed-8c90-30b287e2c00b | -17.84185 | -40.1272 | 2025-12-14 03:23:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fe77cf3c-5e7c-3f54-b677-b47644adb90a | -8.0324 | -43.1022 | 2025-12-14 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 2ee3c950-088c-350f-8689-607939b2a41e | -8.0324 | -43.1022 | 2025-12-14 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 9942a333-8ac0-3d96-89ea-438960dab145 | -6.40481 | -41.08545 | 2025-12-14 03:42:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 99e29f84-1a77-342b-ab8b-9180ed68cb12 | -3.88256 | -42.52373 | 2025-12-14 03:42:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 5cebdca1-4380-3d98-968f-e54dd87ba438 | -5.93775 | -44.4593 | 2025-12-14 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6305bc4f-0baf-3ee7-91ac-abf93778e2ea | -6.91128 | -38.59046 | 2025-12-14 03:42:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c669ba8a-0f75-377b-b085-92d8cc82d7e4 | -1.52172 | -45.68559 | 2025-12-14 03:42:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e0aad443-3c96-3023-881c-1fec0fb1478d | -5.34867 | -40.68446 | 2025-12-14 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 85630de4-d71f-3aae-b20a-bc67cebc6560 | -2.48173 | -45.442 | 2025-12-14 03:42:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c073ec7-0a7b-317f-a204-4301fc72d702 | -4.34043 | -40.27693 | 2025-12-14 03:42:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c81a43f3-5754-3b0b-b11b-d009d34f5009 | -3.72604 | -43.76289 | 2025-12-14 03:42:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 454705c8-b8b9-3064-a65d-bb7a26226c7a | -3.36525 | -39.81478 | 2025-12-14 03:42:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6b716345-d7c9-3dd1-9b4d-eefc4b8525b7 | -3.73192 | -43.7604 | 2025-12-14 03:42:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58aa4b7f-9774-3643-8201-f3ab6cffb099 | -2.83731 | -46.73378 | 2025-12-14 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07765fa0-902d-3d1f-8606-69eae3ab30aa | -6.4817 | -39.50597 | 2025-12-14 03:42:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 93e2d4d8-7b97-3420-9f2b-d92487a00f80 | -5.34384 | -40.68762 | 2025-12-14 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5518ffb9-94dc-34fa-b103-8379c731ed72 | -2.83082 | -46.7326 | 2025-12-14 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bd5da1e-bd4c-3318-9d0e-6c43041105e0 | -5.34448 | -40.68377 | 2025-12-14 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8896f4c2-bea4-370a-b53a-ef13b0cdccaf | -6.45051 | -39.78642 | 2025-12-14 03:42:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4dccd14b-64b8-3909-9141-c95886616a8b | -3.77101 | -42.09995 | 2025-12-14 03:42:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6bbd7dfd-a613-39cc-8c11-f242c4eae223 | -5.66998 | -39.27883 | 2025-12-14 03:42:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 18.3 |
| b036dad2-e7c3-3c29-bbdc-c8a1d8cd4924 | -6.59133 | -39.56999 | 2025-12-14 03:42:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 54aee9ff-6cac-3a95-99a9-b559b926732c | -2.58668 | -44.95998 | 2025-12-14 03:42:00 | NOAA-20 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d04d50d4-9cf9-3c10-b497-8c2bb7239d09 | -3.87769 | -42.52291 | 2025-12-14 03:42:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 833f1b47-65eb-38e1-afbc-571779ed72b9 | -5.98588 | -44.59504 | 2025-12-14 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf4c1ca5-5363-3292-998b-6b76453cf3b3 | -3.14336 | -45.36607 | 2025-12-14 03:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3e0ad1b-c8a7-3538-836a-b6e3e986c26d | -6.40425 | -41.08988 | 2025-12-14 03:42:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5efaff9a-c8d4-3f5d-9c7a-9b90f7066e4f | -3.73135 | -43.76375 | 2025-12-14 03:42:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a5070611-c7f5-3431-b9ac-c4a1e859fbed | -3.43829 | -41.64702 | 2025-12-14 03:42:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 94486887-c11b-367d-9d5f-d43e4a8288b1 | -6.71216 | -40.00029 | 2025-12-14 03:42:00 | NOAA-20 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 83150a8b-b7a3-3350-ba37-bdc5b0f7e60d | -5.67455 | -39.27484 | 2025-12-14 03:42:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 15056197-297c-399d-a798-4a1af9780d06 | -5.94042 | -44.45996 | 2025-12-14 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a9ee41c9-37bf-3de3-914c-836d9cf39b06 | -5.34604 | -39.48344 | 2025-12-14 03:42:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 22749c86-4343-3876-86a1-6fecd988aeaf | -3.43368 | -41.64627 | 2025-12-14 03:42:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2a1e0d52-af5c-3e98-96dc-af8bfe444de5 | -2.21227 | -45.69717 | 2025-12-14 03:42:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8e663647-9865-3dcf-af1a-0a713e09fbe7 | -2.88357 | -44.96404 | 2025-12-14 03:42:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ac92eb7-d1fd-35a6-b09c-f42d864b7228 | -3.87859 | -42.51748 | 2025-12-14 03:42:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f880c55-4edf-3307-a22e-84b71617302c | -2.47644 | -45.4365 | 2025-12-14 03:42:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4425fc7a-6e55-3cee-8dce-58b069af1b62 | -3.14262 | -45.37047 | 2025-12-14 03:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce917e73-50f6-3163-97a0-61ee7c6c64fe | -2.88869 | -44.96915 | 2025-12-14 03:42:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1de7bcb-5080-3972-8261-82eeeb940c86 | -2.83755 | -46.73089 | 2025-12-14 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a7e0126-205f-3cd4-8ba2-fce490263e0d | -6.5875 | -39.56939 | 2025-12-14 03:42:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 40a5330f-af12-3291-8cec-fa00a47a79f1 | -3.14187 | -45.37488 | 2025-12-14 03:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bb2a006-8449-301c-81f9-6823192eec7b | -2.58738 | -44.95576 | 2025-12-14 03:42:00 | NOAA-20 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c9f9499b-5f58-36d2-8bec-0a1db2e5869c | -5.72599 | -35.51741 | 2025-12-14 03:42:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b9af707-bb4a-37ca-ae4e-57bd9e73465e | -3.8805 | -42.52345 | 2025-12-14 03:42:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 318efc37-4bc4-38b6-a58f-04db6b6f30d0 | -5.98528 | -44.59848 | 2025-12-14 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33e7f063-976b-37b9-976a-3359bc8d30e8 | -7.17672 | -38.86907 | 2025-12-14 03:42:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 41dfc3aa-a5b3-38d7-8cd1-67252e33ddaa | -3.30579 | -42.53567 | 2025-12-14 03:42:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7026aa9-72d4-3041-ba0f-142722fcccba | -3.20706 | -41.85429 | 2025-12-14 03:42:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a998613-713d-389f-b586-f572f4f37348 | -5.67074 | -39.2742 | 2025-12-14 03:42:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 18.3 |
| c475101a-7589-3af2-8c57-97f976b67956 | -6.07805 | -37.94279 | 2025-12-14 03:42:00 | NOAA-20 | MARTINS | RIO GRANDE DO NORTE | Brasil | 2407401 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e3460fb6-01fa-38c9-9ad1-dd0d5eb35c01 | -6.40491 | -41.08591 | 2025-12-14 03:42:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 1b425d3e-678d-3d8f-9609-078163921acb | -1.52462 | -45.67794 | 2025-12-14 03:42:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2e260ee7-3eb3-316b-855c-356ed0a778d1 | -6.59171 | -39.52081 | 2025-12-14 03:42:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a4575f14-6011-3db5-a0ca-027ce740b230 | -5.94309 | -44.46036 | 2025-12-14 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 070a33a2-240e-3d22-a0ab-059d42983177 | -3.73079 | -43.76708 | 2025-12-14 03:42:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 105471c5-1197-3863-be51-d7cf4bbe0ac4 | -1.97303 | -46.48299 | 2025-12-14 03:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0aca14d9-88db-37ce-b968-8edd6105b34b | -3.88345 | -42.5183 | 2025-12-14 03:42:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2a216945-5a7a-3b9b-ac40-16822ebc2ef2 | -3.88143 | -42.51804 | 2025-12-14 03:42:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |


[Clique aqui para ver as próximas entradas](README6.md)
