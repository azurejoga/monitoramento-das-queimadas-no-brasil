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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e07f4d5-6b4a-3d03-ba89-211874595d99 | -18.7176 | -57.3097 | 2024-10-07 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.7 |
| 54d5cdbd-32b6-39fc-8245-77bb352d6d13 | -18.718 | -57.289 | 2024-10-07 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 0a3c8387-c4d4-3489-b572-00f1d4c32c72 | -19.8838 | -42.641 | 2024-10-07 03:56:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.5 |
| acffaaf2-7e1f-33f2-a0df-0ab78a0ca0ee | -20.4443 | -47.7109 | 2024-10-07 03:56:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 166.1 |
| fc7e2c89-ad48-3e3c-9e16-d2bd6e525162 | -20.4449 | -47.6875 | 2024-10-07 03:56:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 65dcb937-3c0f-3004-8215-8c23cf2b13e7 | -20.4648 | -47.7062 | 2024-10-07 03:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 24791bd2-873c-3403-b25e-9a22cb99f462 | -20.4655 | -47.6827 | 2024-10-07 03:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 287.2 |
| 0a7cbe01-485f-343e-807b-2041863d7de0 | -20.4661 | -47.6592 | 2024-10-07 03:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 45280879-06c5-3a99-89ad-3ddfbb94c755 | -20.486 | -47.6779 | 2024-10-07 03:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a472cc92-86e3-3b70-9731-200009f5a1ad | -20.5138 | -48.1366 | 2024-10-07 03:56:59 | GOES-16 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 41f04414-d34d-35e5-916a-8af80ea090dc | -20.5145 | -48.1132 | 2024-10-07 03:56:59 | GOES-16 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 40a9cb0c-4ba2-3349-bd1b-fb89348aa9fd | -20.5848 | -48.5137 | 2024-10-07 03:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 242.7 |
| e1ce6444-f683-33bc-82ff-ece2727d37da | -20.5855 | -48.4904 | 2024-10-07 03:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 3f3fc771-5ae1-347f-a0de-ee6dce70cb34 | -20.6053 | -48.509 | 2024-10-07 03:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 282.0 |
| 02ddf058-4bf6-33d2-bc7d-d88db37688eb | -20.606 | -48.4858 | 2024-10-07 03:57:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 283.7 |
| 29bac46f-7a4b-3ab7-b1e1-194e8d895602 | -1.20206 | -46.58966 | 2024-10-07 03:57:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76c8688d-9682-3cce-ab31-77babc1fc450 | -4.83592 | -46.86725 | 2024-10-07 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 913be508-c914-3f09-a904-609cf6f26bb5 | -3.9534 | -46.45403 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85ff13d8-9f1d-31f3-804d-593e593a12b3 | -3.95078 | -46.45068 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 646d874e-9928-3674-8261-0f4091f6d029 | -3.94999 | -46.45558 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcf13a1a-4409-3c73-94f9-71dd1798c56f | -3.94882 | -46.4529 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51c1d352-6e41-337b-96a6-dc9dc4e71254 | -3.94157 | -46.44862 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 264a144b-19d7-31cf-886b-f4e271684071 | -3.94042 | -46.44609 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 707fa1ac-6d37-3903-8814-4b12403c11d7 | -3.93959 | -46.45098 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9e706eb-8801-321d-8b48-b307230019a7 | -3.93693 | -46.4478 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3fee6b0e-e3f3-3a1c-bcda-987df59f3fe1 | -3.93307 | -46.4422 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e052fe93-07a0-309c-89c8-ce73add2eb38 | -3.93229 | -46.44701 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c9dd24d-d4ea-3669-8471-5882c6ef16c1 | -3.8522 | -46.46872 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9795c7f9-8e46-3bf2-ad55-847159394029 | -3.8499 | -46.46637 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e686dc71-515c-3c99-84dd-e7646771b60c | -3.8491 | -46.47134 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5ceeca3-65ce-3ca0-9303-907f20af189a | -3.84757 | -46.46777 | 2024-10-07 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e64ef328-7767-3875-90fe-4267d5b61010 | -3.49581 | -48.90017 | 2024-10-07 03:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a4ee16e-85d8-391c-b57f-bc56d23162d3 | -3.49029 | -48.89919 | 2024-10-07 03:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c483cac8-dc07-3632-917b-366f9e4c573c | -3.46029 | -47.66394 | 2024-10-07 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0557841-d864-3d4f-9bee-4e67f777f25e | -3.45979 | -47.66695 | 2024-10-07 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f3dcb34-8c68-3d1f-9786-3cae1f75e5a4 | -3.22595 | -48.92884 | 2024-10-07 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eda740f7-1fdb-3f93-8657-e93b22b96eee | -3.22535 | -48.93254 | 2024-10-07 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fac328ed-7232-39e4-92f6-d7ce848b907e | -3.22448 | -48.92964 | 2024-10-07 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4b48e62-79e1-3457-bbe2-da07fe25ed36 | -3.2204 | -48.92783 | 2024-10-07 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcf048f3-19b1-38c4-9b5d-849b98ff3a75 | -3.21979 | -48.93156 | 2024-10-07 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58bd6e68-bce4-31fc-8d54-01eb54362893 | -3.21892 | -48.92868 | 2024-10-07 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85bfdb8e-d739-3b6e-b326-524897995d41 | -3.12481 | -48.61359 | 2024-10-07 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2ebaeb5-4268-341e-9b77-f6df1f38bdf4 | -3.12131 | -48.63481 | 2024-10-07 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e22acdc0-8690-3633-92c1-7da4cbf315d8 | -3.12054 | -48.60549 | 2024-10-07 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74226ebd-30b2-37eb-a5ed-9ffe4d9563f6 | -3.11996 | -48.60905 | 2024-10-07 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 718028a2-2888-3387-a3d6-a65f70ac3293 | -3.11937 | -48.6126 | 2024-10-07 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09380d1c-f875-30b3-a9e4-23c933fc1582 | -2.93408 | -47.8442 | 2024-10-07 03:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7a7a0c2-3534-303d-bf13-2a5b0d8e6f88 | -2.74348 | -48.6965 | 2024-10-07 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00611849-85c2-3e61-ae27-be0678322a14 | -4.0931 | -48.25884 | 2024-10-07 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acf52b6a-0a0e-358b-b2ef-0d4ad4873f02 | -4.09254 | -48.26209 | 2024-10-07 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e329756-403f-3ccb-a65c-b5c5bf0ef92a | -4.09198 | -48.26532 | 2024-10-07 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f7bc2f2-20be-3f5d-aba6-a91755d0a713 | -4.09143 | -48.26857 | 2024-10-07 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e26c0ac0-bdcf-355b-a5d4-c61049ff9f80 | -3.90597 | -48.34687 | 2024-10-07 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 516f3fa8-fbf0-3e27-bdf9-bc461da6a160 | -3.9054 | -48.35028 | 2024-10-07 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0f1d0bf-e2e0-3890-becb-21711cf45538 | -3.90483 | -48.35371 | 2024-10-07 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 478bcac8-7780-3213-8a93-800225430e1d | -0.26787 | -48.73954 | 2024-10-07 03:57:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1b71719-a45e-3511-b82f-fe6b73efaef5 | -0.26723 | -48.74355 | 2024-10-07 03:57:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68ce65e8-51c4-357a-be12-cdd8666d63ac | -3.35518 | -49.91896 | 2024-10-07 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14c62bcd-7a2a-33fb-97c2-098334a32595 | -3.35309 | -49.91781 | 2024-10-07 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5a2759b-d52f-3c7c-86ad-b69d45d6e152 | -2.78895 | -49.52761 | 2024-10-07 03:57:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3d09e06d-ae15-3447-a747-8545f642903a | -2.78862 | -49.52709 | 2024-10-07 03:57:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 764c7f16-fb0a-3cf7-8102-2d1870919e51 | -2.78827 | -49.53173 | 2024-10-07 03:57:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 94f374fe-5397-357e-99d4-da7a70ed8a70 | -2.78792 | -49.5312 | 2024-10-07 03:57:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 38d3eb5f-d56c-37b9-974c-5a0439b8380f | -3.32756 | -49.16011 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68248c39-a85c-38b9-b2ed-f145d0fc0d34 | -3.32322 | -49.1515 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09c06206-0938-3ee1-8844-32891da1163f | -3.32257 | -49.15535 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c7e67b6-73ee-3995-b30b-72c1c119282c | -3.32192 | -49.15918 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45cc2f76-956e-30dd-9e95-33d5c313cf37 | -3.31823 | -49.14669 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba9b6970-edd4-3a62-b2ea-4f6367d6657b | -3.29199 | -49.14599 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4075e4e3-dcb4-35dd-ba51-98bbadd2c8ee | -3.29135 | -49.14989 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5ca2009-6e07-3f40-bfbc-da8a4f24521a | -3.28942 | -49.14574 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 864512b6-bc6b-38a9-89c4-bebc63a63608 | -3.28875 | -49.14964 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30dd9182-74fa-35b3-9022-e8690cb68e9c | -3.26946 | -49.14204 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d5ce3bc-59b7-393d-ab96-80178f087aed | -3.26882 | -49.14592 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dee8159d-5a69-34d0-b91f-fa43c60f0845 | -3.26634 | -49.12586 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| feb88b0d-03d9-3d24-8460-a673a079dfa5 | -3.26573 | -49.12959 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7821c4e7-6b11-32b4-9ff6-f21e59dfd7b3 | -3.2651 | -49.13339 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2639c838-1fa7-38e2-846f-901ba1f4e02b | -3.26009 | -49.12868 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 937d41ed-8eb3-31e9-b227-3b5c88860bae | -2.53243 | -49.02113 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb44b9d2-f34e-3487-902c-1f1db4f19a10 | -2.5318 | -49.02502 | 2024-10-07 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3647185-e5a0-3d39-bb06-b3f43515489b | -3.69432 | -49.85003 | 2024-10-07 03:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8655f2b-7ccc-3e0e-93e5-b5bc45774a68 | -3.69326 | -49.84805 | 2024-10-07 03:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efa01f52-8501-3391-ac9c-87b24df8a3de | -3.69254 | -49.85221 | 2024-10-07 03:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8df967cd-9766-31bf-ac66-3bee838cc88e | -2.88042 | -52.90297 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 947d11a0-b0aa-3f37-a610-53e720f13092 | -2.87921 | -52.90989 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b4fa26a2-37df-3cf4-b7f8-df40321d5ad7 | -2.87799 | -52.91692 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b265ee04-e6b4-3e56-af93-ecd40413e8c3 | -2.87728 | -52.90128 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| acefc834-c520-3d2e-833f-428c6a91f4b3 | -2.87612 | -52.90821 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 08357e7c-ade2-3e88-806c-7acb6ae273f9 | -2.87495 | -52.91521 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 69399420-b40a-3a69-beec-b6f68537b21b | -2.87377 | -52.92222 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 924a4787-e5da-3de5-a726-4b7c14b4543f | -2.87323 | -52.90208 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 79634d17-4f65-3f24-95cd-d2aeb9f51463 | -2.87201 | -52.90904 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0c18fc66-d35c-3940-b345-e3dbda1ca9f8 | -2.87081 | -52.91597 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b4225f4d-e8a1-3090-9530-50c34a822d15 | -2.8701 | -52.90036 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5ca61b14-588a-34fb-82af-5376574d5267 | -2.86961 | -52.92282 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9caaa909-666d-3ac3-895a-07e92b0b50b9 | -2.86892 | -52.90736 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a503e26a-b62e-38cd-8816-e7eed593ae8c | -2.86776 | -52.91428 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0905687-0c1b-3e6e-b428-9309370c9fb0 | -2.86664 | -52.92096 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ff5e5cc-ff2f-3f01-8423-92b698b3c4e2 | -2.86604 | -52.90122 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 08a03912-a782-3bc1-9716-aff251a56db8 | -2.86481 | -52.90823 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README54.md)
