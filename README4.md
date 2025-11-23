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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fa07394-9f01-3aa3-a219-84eaf91a95a2 | -18.7569 | -45.28742 | 2025-11-23 03:40:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f7e4bd4-6829-3f62-80ae-dc91d5f8e690 | -18.73062 | -42.81591 | 2025-11-23 03:40:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 56cbfdcd-64c9-30c3-816e-fe343f48611b | -20.34624 | -41.7464 | 2025-11-23 03:40:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8139564a-58ef-3596-b252-67265bfb592c | -18.73334 | -42.81538 | 2025-11-23 03:40:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 977bc656-fbed-3b3e-b82c-908a7c01d6a1 | -18.76189 | -45.28859 | 2025-11-23 03:40:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4793964d-d386-3c0c-a53c-117511b05a66 | -20.53197 | -41.57431 | 2025-11-23 03:40:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cf804bf3-22c5-36bf-9d1c-2a5fe3ed86a1 | -20.59493 | -42.46614 | 2025-11-23 03:40:00 | NOAA-20 | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dec26530-679f-3959-84f7-e92eca32755b | -22.06188 | -41.20066 | 2025-11-23 03:40:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4d2e0d74-fa20-30b5-90e7-0e6ccbf6a66e | -20.38961 | -42.17878 | 2025-11-23 03:40:00 | NOAA-20 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c6cfdc7f-4c52-3180-b43d-c05a4872762e | -19.31835 | -43.28585 | 2025-11-23 03:40:00 | NOAA-20 | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 10111a2d-300a-3b06-a888-6c94347ecbfd | -19.62358 | -41.8512 | 2025-11-23 03:40:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 273014cb-c902-3dca-a725-4e42a0ae61d1 | -19.61967 | -41.8501 | 2025-11-23 03:40:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 974a0b69-922f-3f57-80bc-32975c9d452b | -20.34351 | -41.73923 | 2025-11-23 03:40:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 477eb70d-91f8-3ea0-b535-5a090a22f25d | -20.38903 | -42.18182 | 2025-11-23 03:40:00 | NOAA-20 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c1b4669b-4069-3b6a-89d8-1af26fe84cb1 | -20.34652 | -41.7448 | 2025-11-23 03:40:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 87174a06-d36c-36cd-8a14-b08597de2a88 | -20.33958 | -41.73866 | 2025-11-23 03:40:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 50322fba-212d-3256-b562-da0ca7c5a27d | -18.75751 | -45.28444 | 2025-11-23 03:40:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65b520d9-9197-3a0b-aa7a-4b7f1162ad78 | -20.35348 | -44.25727 | 2025-11-23 03:40:00 | NOAA-20 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8b47fe13-7518-3929-b4ed-26fee6af46b0 | -2.8675 | -45.2832 | 2025-11-23 04:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 163.5 |
| 3b12e6de-86a9-31c3-839f-37110754ffbd | -2.8674 | -45.3057 | 2025-11-23 04:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| a459e2bd-3d8b-3d4c-825b-8ec2f77333e7 | -2.886 | -45.3051 | 2025-11-23 04:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 160.0 |
| b171da51-b5e8-3e90-b568-9b6ab74b4288 | -2.8861 | -45.2826 | 2025-11-23 04:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 654.7 |
| 263585c3-fffc-37be-ac7d-0fa7fcc5e880 | -2.8862 | -45.26 | 2025-11-23 04:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 866cfea0-9af9-3444-9fc5-3ede23b5a32b | -2.9047 | -45.2819 | 2025-11-23 04:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 2a2f0cbf-18fa-332d-aea0-2756f1ea88d7 | -1.67465 | -46.45919 | 2025-11-23 04:23:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e14d5009-cc2b-3cbe-969e-40e893fe1f0d | -1.82711 | -45.57258 | 2025-11-23 04:23:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e82eb003-8fa7-37fe-b039-41a60df7cdc5 | -2.11781 | -45.93357 | 2025-11-23 04:23:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edf002bd-30b7-35c3-a12b-643b62e8856d | -0.94862 | -47.28234 | 2025-11-23 04:23:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc80e22a-29ae-321f-953e-ab092520a06b | -0.9459 | -47.16566 | 2025-11-23 04:23:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c447cd7-87a3-33c9-8a55-70e9fee61309 | -2.10616 | -45.40202 | 2025-11-23 04:23:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfd1bc64-a8d6-37a0-b33b-0a722bbaa109 | -1.6713 | -46.45867 | 2025-11-23 04:23:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25f3e052-30cd-3538-8b95-a7f3545ac3b0 | 0.94315 | -50.08712 | 2025-11-23 04:23:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 83075e28-9f15-3d59-b0f1-9b88ec203276 | -1.82657 | -45.57602 | 2025-11-23 04:23:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e92b9dae-7ffb-376f-9c59-273571d6f700 | -1.67521 | -46.45564 | 2025-11-23 04:23:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98b9962c-5a2a-37af-9488-2d97af0d3b04 | -2.12113 | -45.93408 | 2025-11-23 04:23:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52d58e6c-2bf9-3b6e-ae20-20b6df12ed84 | -2.92271 | -40.2799 | 2025-11-23 04:23:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd3365e2-3949-3291-a6b1-d25ed8a601a6 | -0.93167 | -47.38939 | 2025-11-23 04:23:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb77e364-f174-3ec8-bb75-b430d55e8aa8 | 0.94372 | -50.09089 | 2025-11-23 04:23:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26f8afd3-59fe-3d85-8a42-3f557ce27874 | -1.82381 | -45.57207 | 2025-11-23 04:23:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc23e93c-6060-3364-9fc0-70004571f28d | -1.44735 | -46.12798 | 2025-11-23 04:23:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4c30a35-ff46-3673-901a-3fbf91e5790d | 1.0569 | -50.06662 | 2025-11-23 04:23:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4206bd13-14a8-3384-9f2c-c78fa15ea22e | -0.86039 | -52.70579 | 2025-11-23 04:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e2dfb1a-b236-371c-8ca5-746025672556 | -0.85952 | -52.71117 | 2025-11-23 04:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7ebd9a70-9b36-34c6-8b1e-330d4d3d563f | -5.67841 | -48.78559 | 2025-11-23 04:25:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61f96e89-9557-3397-85d0-4c6d0263e926 | -1.85918 | -54.06894 | 2025-11-23 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcb14777-7f58-3b0a-a74e-73adaefa4d65 | -2.89741 | -45.28036 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 788581db-061e-398f-9860-126fbd79533f | -3.45507 | -40.53227 | 2025-11-23 04:25:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bb7ae33a-7b21-3222-bc31-d097fd368fe0 | -3.46021 | -47.63084 | 2025-11-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9f967ab-c006-35bb-890f-4b99f54e2c54 | -4.56148 | -45.49264 | 2025-11-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6666d04-bf12-30ff-96c7-6efc1010829b | -6.70838 | -39.6833 | 2025-11-23 04:25:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 88c2f982-bc27-3a45-b16a-d5d906a73005 | -3.42014 | -43.1474 | 2025-11-23 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16eb3dd8-af3b-3740-b92c-295a46f3cbc9 | -3.86515 | -51.14025 | 2025-11-23 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cf3a2be-ddf6-36c9-980f-be0ef393cf08 | -5.54935 | -41.03986 | 2025-11-23 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9addf2df-4175-39e6-ba0d-c1a4bed4f6eb | -3.38953 | -47.18992 | 2025-11-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f0ccf0f4-73f6-388b-8866-f4c6885561a8 | -3.45677 | -47.6303 | 2025-11-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19e18218-f60c-30a0-b914-36e72c5f693a | -2.24972 | -46.49813 | 2025-11-23 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b011d69-552e-30b2-b350-97ef03cbc4d1 | -2.47318 | -45.42452 | 2025-11-23 04:25:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18706ec3-82de-3241-9c73-ca18c647a4b9 | -1.98038 | -50.24649 | 2025-11-23 04:25:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 618bbb2c-07a0-30cc-aeab-bb8450bd8db8 | -3.57294 | -43.36894 | 2025-11-23 04:25:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75f99244-d511-3d41-a477-f1db696a80b8 | -2.89303 | -45.28672 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a02d729-30bb-3e59-a52f-ddf672bb4cf7 | -4.83377 | -44.06406 | 2025-11-23 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c98bfe71-f60b-32fa-948c-9d551efe85cc | -4.56094 | -45.49609 | 2025-11-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1361695-95a3-3e0b-a3f0-ffc354fc2dc4 | -2.95853 | -45.43456 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e503b40-1a99-389a-9519-f78fb06471f6 | -7.40408 | -40.06678 | 2025-11-23 04:25:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 48fb0e3b-fe0c-326c-ab38-1f36777d0922 | -4.04564 | -42.5166 | 2025-11-23 04:25:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d2ae6abc-ff58-3dc4-b4b5-83b2d420f5fe | -4.99069 | -43.88701 | 2025-11-23 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9333625a-43a1-3549-9f6e-f3dade5f4867 | -5.70114 | -37.94842 | 2025-11-23 04:25:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e358ae77-d552-3282-8eff-8686f33074b8 | -4.71815 | -46.46745 | 2025-11-23 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72be116f-3290-31b2-bfc0-d34dd94551c6 | -4.1716 | -44.21646 | 2025-11-23 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 354280f0-c13d-30a3-9c8c-ac8a5d06702f | -3.69879 | -47.67514 | 2025-11-23 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acbe880e-e2a4-3eb4-b7cb-8b53596e5fa5 | -7.73806 | -47.25263 | 2025-11-23 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb28e47b-2360-3ce7-83d8-1a492153a23b | -1.19455 | -53.71927 | 2025-11-23 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8af50b12-4a8c-3bb3-974b-5b83776a03cd | -1.74154 | -52.02142 | 2025-11-23 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b5c8fbc-b2a1-373b-bc26-392b274aae74 | -2.87928 | -45.28811 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 854feaf3-2e02-3562-b16d-47c6769cfa73 | -4.7533 | -47.51448 | 2025-11-23 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97be9b30-681c-3f4a-a1ca-a25146396bf9 | -2.63505 | -47.29742 | 2025-11-23 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 990415b1-cfad-3239-9903-08f04d4cfd5f | -5.6765 | -48.79762 | 2025-11-23 04:25:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5de1ae3e-8e17-3c7f-a249-ece4d806841a | -4.3665 | -50.69835 | 2025-11-23 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ac4f6ea-755c-3d48-a736-3405fc875803 | -3.97947 | -42.51495 | 2025-11-23 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cc3ff57e-58cd-3af8-a749-b7ef1651c4e6 | -7.40848 | -40.06743 | 2025-11-23 04:25:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 651c56da-d870-3b77-9379-95f9926e9d08 | -3.1465 | -40.17652 | 2025-11-23 04:25:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2eee01da-82c0-30d7-ada5-c8fb47c3ec74 | -6.04242 | -45.83217 | 2025-11-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e321cdd3-a8bb-3580-998a-93c333c8d7f9 | -4.24745 | -46.4537 | 2025-11-23 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0be18379-1f87-3204-8105-fe8d7c8752d9 | -3.42091 | -46.96956 | 2025-11-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16575a30-9145-37f4-ac13-23dd6faeda59 | -3.97462 | -42.52267 | 2025-11-23 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 369b9373-0bbc-3351-8001-a6edb386811d | -2.47972 | -47.63922 | 2025-11-23 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf6e5001-2985-32bd-bf4b-bd5f1ec1f80c | -2.49933 | -47.09215 | 2025-11-23 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c6fc84a-ab40-3614-9168-69b1b913c1af | -3.7943 | -45.93909 | 2025-11-23 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61d4465b-0ba9-301c-8697-be8f9a541994 | -2.95139 | -45.43696 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1440282c-440c-3b23-8297-7589070c1d8c | -2.83679 | -45.25327 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4635d673-0d02-3c05-bc4e-827462821d9a | -2.50157 | -47.09996 | 2025-11-23 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b83ec528-df13-3c73-90c2-a49c61f61d3a | -1.32403 | -53.14931 | 2025-11-23 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00c05859-4b34-35ec-b9f6-ad72809f57ce | -2.87322 | -45.28365 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ec626bc-8a23-35e7-829f-bf00fd51d8ce | -3.00899 | -44.43301 | 2025-11-23 04:25:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dd26f4a-88c6-3c7d-a1e6-6f8ed0838696 | -2.22951 | -53.64941 | 2025-11-23 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cedf62f-5fc5-3226-bcf8-f99e0cae1ae3 | -2.64007 | -45.48986 | 2025-11-23 04:25:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5394e135-5e15-3904-9ee8-ba9ef6c7c5e3 | -5.97544 | -40.38691 | 2025-11-23 04:25:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a8f5963-ad43-380b-bc1f-9df2d00ec4e6 | -4.39767 | -45.73502 | 2025-11-23 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cdb5e10-726c-3698-987c-2bd3cb36c296 | -3.29342 | -45.72651 | 2025-11-23 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17238cf1-16e2-324f-a01c-e455138ed138 | -2.63447 | -47.30113 | 2025-11-23 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README5.md)
