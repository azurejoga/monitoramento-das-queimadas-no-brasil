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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3007efa-cee4-3ba4-bdb8-4130af258956 | -22.56624 | -42.15302 | 2025-12-26 00:07:00 | TERRA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 1f522811-fee3-3485-8910-499b6dc44b39 | -22.93439 | -47.17631 | 2025-12-26 00:07:00 | TERRA_M-M | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 04cb0d67-e9b5-3b3f-a2cd-29e146c6ed3c | -18.15586 | -46.94138 | 2025-12-26 00:09:00 | TERRA_M-M | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| aa42688a-18d8-32c4-beb2-3e1390337ff5 | -16.10567 | -43.45977 | 2025-12-26 00:09:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e6584553-9abe-322e-a835-d00f4f94bb9d | -20.19934 | -43.6298 | 2025-12-26 00:09:00 | TERRA_M-M | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| b76ec85b-43df-3e2c-8b92-c5520b5123d9 | -11.84904 | -43.78808 | 2025-12-26 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b7c1fe01-c64a-3d14-9056-d8ac01ea9237 | -15.43004 | -43.24128 | 2025-12-26 00:09:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 663b015a-5b3c-374f-8cdd-6953d3260373 | -11.84015 | -43.7894 | 2025-12-26 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f39c1ff1-27ef-3c76-a294-a4460a8234a1 | -16.10694 | -43.46891 | 2025-12-26 00:09:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a43ba5b0-904b-3ae2-a82e-969d3955a720 | -15.43133 | -43.25046 | 2025-12-26 00:09:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 86ec867d-d2eb-3f0a-a438-652d00e5d558 | -21.00497 | -41.54264 | 2025-12-26 00:09:00 | TERRA_M-M | APIACÁ | ESPÍRITO SANTO | Brasil | 3200508 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| ffd88ba6-2d95-3a5d-b90e-66549d8c589a | -18.56797 | -41.22144 | 2025-12-26 00:09:00 | TERRA_M-M | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 58cea6d7-f350-3123-882a-144f8003bbd4 | -21.0064 | -41.55243 | 2025-12-26 00:09:00 | TERRA_M-M | APIACÁ | ESPÍRITO SANTO | Brasil | 3200508 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 78708cac-c74f-39a3-b687-843b7278d758 | -11.84144 | -43.79852 | 2025-12-26 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8aa93cb2-8e8e-3cbc-8cb8-a296eba2c480 | -11.85033 | -43.7972 | 2025-12-26 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| a765e849-8293-3317-8fe9-506c16d499cd | -12.07968 | -43.52945 | 2025-12-26 00:09:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6334b0c0-dc30-33d5-9706-eafdde430c60 | -5.93681 | -43.51518 | 2025-12-26 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fe394510-586e-350b-901b-666f9048a973 | -6.57506 | -43.79673 | 2025-12-26 00:11:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aecdc6fc-9f21-3e3b-8e8f-77a492f3addb | -5.92738 | -43.51665 | 2025-12-26 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7257fdf3-3fe6-38c3-b351-211fc9b98fb7 | -10.04752 | -36.42009 | 2025-12-26 00:11:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.6 |
| 44b746a0-2fec-3194-a1ee-3fc18bb9c512 | -11.16278 | -43.30934 | 2025-12-26 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 00e6b784-1c42-3eeb-8e3a-95a32713407e | -10.04954 | -36.42512 | 2025-12-26 00:11:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.1 |
| eba13428-7d73-302e-bf6b-8e7e9c12fcf8 | -2.3675 | -51.911701 | 2025-12-26 00:28:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20e0f6b3-3bfe-319b-95c0-d80f262f84c5 | -21.253 | -49.280102 | 2025-12-26 00:28:00 | METOP-B | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 50a4985f-7536-36d4-adfd-a3af0859ef18 | -11.8502 | -43.821899 | 2025-12-26 00:28:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 64d21b61-c33a-37bb-a6ec-14987daa31e4 | -2.9103 | -51.852402 | 2025-12-26 00:28:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60e49058-37bf-39e7-b056-108f9d884711 | -11.8459 | -43.805099 | 2025-12-26 00:28:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 094c15b6-7938-3ab2-9cb5-523d0808ff2e | -19.8999 | -50.9613 | 2025-12-26 00:28:00 | METOP-B | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3da6778-5130-3091-a975-103b4bdccf68 | -20.239901 | -40.275299 | 2025-12-26 00:28:00 | METOP-B | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bed23f17-ae54-3749-93e6-2a21329a8f81 | -19.901501 | -50.9687 | 2025-12-26 00:28:00 | METOP-B | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 95cb783f-ea3a-3eb6-ab6b-00a50c322bfb | -2.3692 | -51.919201 | 2025-12-26 00:28:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98c747af-95dc-3d5c-a868-cd643cb87928 | -16.143 | -43.5807 | 2025-12-26 00:28:00 | METOP-B | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3687597f-77fa-370a-8ffb-f48ff304bc26 | -19.903099 | -50.976101 | 2025-12-26 00:28:00 | METOP-B | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8824d0ca-f773-3a0a-86e9-835ca5b773cb | -11.8362 | -43.807701 | 2025-12-26 00:28:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb353c28-b47f-3244-a37b-abdb1913a4fd | -6.7507 | -35.1659 | 2025-12-26 00:50:00 | GOES-19 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 132.2 |
| d80ee853-6723-3e3d-98dd-dc0d84a78dc5 | -16.1432 | -43.593399 | 2025-12-26 01:08:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e0b3c174-6e07-3261-93e2-dce9f2d1a96e | -22.928499 | -47.1833 | 2025-12-26 01:08:00 | METOP-C | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1101ac5e-f434-319a-8bdd-f0a5c1fd5729 | 3.8129 | -60.524601 | 2025-12-26 01:08:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2491285a-d5a2-304e-9c63-5897dff95012 | 3.8147 | -60.516701 | 2025-12-26 01:08:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 30373ff3-ebc5-31ce-9eec-d9a7169c25e9 | -2.3724 | -51.9221 | 2025-12-26 01:08:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec9cf3c7-5ecb-31b3-9cca-bce4d26aeb9d | -21.247999 | -49.285801 | 2025-12-26 01:08:00 | METOP-C | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 91c33528-7ac5-3eb9-916e-22c2aec45e6d | -19.9021 | -50.9706 | 2025-12-26 01:08:00 | METOP-C | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f741a07a-2225-3353-a75b-65e16dc743c6 | -21.25 | -49.294102 | 2025-12-26 01:08:00 | METOP-C | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 80dfdd01-185a-3005-8ad4-a2568573cab7 | -2.9041 | -51.8615 | 2025-12-26 01:08:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d469f17f-b338-3bc0-84f0-55f08c78d17b | -22.930901 | -47.193199 | 2025-12-26 01:08:00 | METOP-C | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03905627-640c-3884-98c2-6607df1e6709 | -6.7507 | -35.1659 | 2025-12-26 01:10:00 | GOES-19 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| 6a2673a4-5b97-3659-8d25-a4de5433a185 | -10.0682 | -36.1275 | 2025-12-26 02:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| 36d0c2cb-ecc0-34a0-bb2c-c2d88c1908f5 | -9.9414 | -36.41535 | 2025-12-26 02:57:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 3cb5680d-0333-3d60-963b-2099f180cd1e | -9.94024 | -36.42117 | 2025-12-26 02:57:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| d0665006-28ed-3222-9a38-89463d616acf | -6.71056 | -39.16032 | 2025-12-26 03:17:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fac4b20f-1f37-3f58-a94c-db54a949ba49 | -9.9402 | -36.41626 | 2025-12-26 03:17:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| ce007430-80b5-3778-a025-a7cfaeff1eb2 | -9.94466 | -36.41704 | 2025-12-26 03:17:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| d8e0b0ad-7e20-3258-b260-7ae82ff973db | -6.30743 | -35.22282 | 2025-12-26 03:19:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 981e9dbb-2a08-35ac-b018-7fe917f040bb | -5.66474 | -39.48803 | 2025-12-26 03:19:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e560d629-062c-3a98-9cf7-a7fbaff2c942 | -6.31182 | -35.22348 | 2025-12-26 03:19:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| acce94ca-d287-3d0d-b3a8-5d4fca3832ac | -16.13849 | -43.55906 | 2025-12-26 03:19:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3134fff1-1c06-3edc-b9cb-2d6442bc1818 | -6.31107 | -35.22784 | 2025-12-26 03:19:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 5ea871ba-9003-3348-9001-144da0bd94ca | -5.12835 | -38.91577 | 2025-12-26 03:19:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7b133c3d-c289-3317-bc45-94b87757092b | -5.66065 | -39.48724 | 2025-12-26 03:19:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 81f006d3-e618-3fed-b927-e4233d94c6d7 | -12.07107 | -38.98344 | 2025-12-26 03:19:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c2e40134-26ef-3328-b5cc-90711022f52b | -16.13733 | -43.56435 | 2025-12-26 03:19:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| caf5bb1e-6853-3fbf-a143-788ab79871a5 | -5.66655 | -39.48817 | 2025-12-26 03:19:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 63b2a450-e13e-3f6b-aae7-64b4ff7dd9cc | -12.07616 | -38.98446 | 2025-12-26 03:19:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1a748500-78ae-332e-bf7a-062139d9b86f | -5.13254 | -38.91787 | 2025-12-26 03:19:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e5a3323-cc6c-3455-a3e8-6d36ecc636ef | -6.30668 | -35.22717 | 2025-12-26 03:19:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 8a8188ed-b393-3458-9dfc-cbf541bc3d70 | -22.92662 | -47.17981 | 2025-12-26 03:21:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 68239277-8779-340c-b330-e1916033a803 | -19.51406 | -45.86091 | 2025-12-26 03:21:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8335325-3fec-3a7a-8b56-17f0dc1c8b75 | -20.19006 | -43.63264 | 2025-12-26 03:21:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d4dfaef3-f94f-370e-8940-e155f867c8b2 | -22.92827 | -47.17325 | 2025-12-26 03:21:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a5778c05-a3e3-3638-a6eb-8f94ff92c10b | -20.2027 | -43.63119 | 2025-12-26 03:21:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4d5144a4-39f1-3e1e-a844-2b53f9f13d02 | -22.92276 | -47.17356 | 2025-12-26 03:21:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ca7a18af-67ac-32ef-a74b-e71a4abf1b54 | -20.20383 | -43.62623 | 2025-12-26 03:21:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a419f8b4-28e4-36f0-8098-204dbbe447b5 | -20.19757 | -43.62667 | 2025-12-26 03:21:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8a46915a-79c4-30ee-a9b8-c827acddcdf8 | -20.19118 | -43.62772 | 2025-12-26 03:21:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6d7717c9-614f-3dab-b63d-e17c7a810b30 | -22.92941 | -47.17558 | 2025-12-26 03:21:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7a477d2e-ab19-3cbe-981d-8ed99f62f183 | -5.93222 | -43.51481 | 2025-12-26 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a757d988-f9e7-3000-8be4-4aaa493066a4 | -4.57153 | -38.37472 | 2025-12-26 04:08:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c0b92cf4-9214-3ae2-af94-eddb97bdd5d3 | -6.00356 | -39.5203 | 2025-12-26 04:08:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d844eea8-27b5-3976-82b5-3e85bfe9b2ca | -4.44615 | -38.93045 | 2025-12-26 04:08:00 | NOAA-21 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fd4b9344-f1eb-3c94-87ae-d232a516acbe | -5.51012 | -39.56008 | 2025-12-26 04:08:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 83b7968f-78cd-3960-afca-7a8fbf0e54f2 | -5.04397 | -40.8614 | 2025-12-26 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e8d4ec40-3171-3066-8bc8-2aacc71cbe87 | -2.91779 | -40.90721 | 2025-12-26 04:08:00 | NOAA-21 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a821975c-1336-351f-83cf-f465ac9c17b1 | -9.95026 | -36.41224 | 2025-12-26 04:08:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ebad518f-8332-3b25-b5bd-cca5fd453c03 | -6.27322 | -38.61403 | 2025-12-26 04:08:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8945ee1e-324c-35dc-8aba-3635f5acc680 | -5.93281 | -43.51108 | 2025-12-26 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f774fac-b376-3d42-a5d9-448d89e02980 | -5.39257 | -36.80554 | 2025-12-26 04:08:00 | NOAA-21 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 60c0dc8c-89c6-38fc-b02f-7818e76ba1a0 | -4.2603 | -40.80539 | 2025-12-26 04:08:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8d1e9140-4ee8-336c-a87f-8af404f357b3 | -6.57442 | -43.80002 | 2025-12-26 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c0e3c09-a443-3c0a-814b-6a97399b98c1 | -5.32835 | -36.80426 | 2025-12-26 04:08:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 98cfdbd9-3f2c-3d8f-9646-451888a6440b | -6.27223 | -38.61317 | 2025-12-26 04:08:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| db1c6949-c456-3402-a2d0-3c162662cfaf | -5.48893 | -36.91265 | 2025-12-26 04:08:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 60fad5d6-753d-348e-8d66-eae39beb1b31 | -4.56159 | -40.5976 | 2025-12-26 04:08:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4edd3f91-ef79-3e72-8fb6-7accf52bab39 | -5.84644 | -39.12858 | 2025-12-26 04:08:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b6259e9e-959d-35b5-a95d-197747f75438 | -6.30794 | -35.22161 | 2025-12-26 04:08:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0ccf7b13-973e-3174-8725-7ce6bf7789cf | -5.34618 | -37.0387 | 2025-12-26 04:08:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d9de1f0-ad58-37fe-aaef-3d79014ed43c | -2.368 | -51.9052 | 2025-12-26 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 402a9d8f-8bed-3448-9aa0-fa58097854e1 | -5.666 | -39.4809 | 2025-12-26 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 71c612e1-174f-363d-9eb3-00994399a031 | -6.17607 | -39.46909 | 2025-12-26 04:08:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 689350df-52e0-3867-a270-cd34d265dafd | -4.90972 | -38.60176 | 2025-12-26 04:08:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6a96a158-c536-3d61-b878-5416e0787aff | -2.91725 | -40.91064 | 2025-12-26 04:08:00 | NOAA-21 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |


[Clique aqui para ver as próximas entradas](README2.md)
