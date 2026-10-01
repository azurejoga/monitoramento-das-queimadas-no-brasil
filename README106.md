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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf08c126-b550-366c-8657-5fcda95acfa1 | -8.98248 | -36.95732 | 2026-10-01 15:29:00 | NOAA-20 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 438a8870-5283-34a3-90ab-78e9839f36dc | -9.63 | -37.84501 | 2026-10-01 15:29:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7cbf2ba1-cc4d-31ff-ad2b-ce22912e43ca | -12.75454 | -40.40257 | 2026-10-01 15:29:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 0cb7a13e-f3b6-3284-a09b-758a40aa47e4 | -8.28483 | -37.64144 | 2026-10-01 15:29:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 6a1abdc3-c50a-37db-850f-64966b8565a0 | -10.52085 | -36.54342 | 2026-10-01 15:29:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 80fd05b2-6b5c-3d72-abe8-a9f33e840ef3 | -9.8328 | -37.23911 | 2026-10-01 15:29:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e72629b4-3a0a-3a8a-9696-5295017c4996 | -14.31256 | -40.25988 | 2026-10-01 15:29:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| cee568dc-e16e-342f-a64b-4b8185264c57 | -9.66967 | -38.2071 | 2026-10-01 15:29:00 | NOAA-20 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 43aebcf4-42a0-32f6-914f-ac2647a46bc6 | -11.18395 | -40.56719 | 2026-10-01 15:29:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| a739a669-5429-3473-b197-d50562cafba6 | -8.92859 | -36.95006 | 2026-10-01 15:29:00 | NOAA-20 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 7d9534d8-60f7-3427-b63a-8809d8c54192 | -8.71761 | -36.85193 | 2026-10-01 15:29:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ef619078-506a-3eed-a6b6-8f3056804e49 | -9.71195 | -37.88127 | 2026-10-01 15:29:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ec938896-51b0-3383-9ee1-c054eca8d75d | -8.68592 | -36.7383 | 2026-10-01 15:29:00 | NOAA-20 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 75ad7888-57a1-34de-914d-e4f8ae8ffc3c | -10.69018 | -40.85203 | 2026-10-01 15:29:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 5c19bdbe-550c-31e8-954b-c70c5ea99b61 | -13.02894 | -41.03495 | 2026-10-01 15:29:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 5621c6ae-c920-36be-8a2f-c005eac81853 | -14.99982 | -39.74002 | 2026-10-01 15:29:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| d953dbf2-7d46-3523-9862-d696dfdedf5f | -4.47304 | -38.50407 | 2026-10-01 15:29:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 91520178-76d3-3a2a-9c29-ec7500f35f91 | -9.83405 | -37.2405 | 2026-10-01 15:29:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 95f7f37f-0e59-32aa-af26-200904992ca3 | -8.94997 | -36.51077 | 2026-10-01 15:29:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 59883392-90c9-347e-982a-18c439325266 | -8.10879 | -39.59057 | 2026-10-01 15:29:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 936c7c36-93a5-36c2-93d8-5fb93d2b1b64 | -13.02611 | -41.03537 | 2026-10-01 15:29:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3fda82f9-4098-371d-9d02-34031e9c3e26 | -8.92765 | -36.94929 | 2026-10-01 15:29:00 | NOAA-20 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 13.8 |
| d45e91d9-25bf-3086-8409-e36382f5e567 | -8.49703 | -36.8842 | 2026-10-01 15:29:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5e9a453d-85fe-3fd3-891c-ea0175b3d680 | -10.51614 | -37.93893 | 2026-10-01 15:29:00 | NOAA-20 | ADUSTINA | BAHIA | Brasil | 2900355 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1543d173-9c23-357f-b540-85138f73377b | -8.62674 | -36.6505 | 2026-10-01 15:29:00 | NOAA-20 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d64c20cf-26c9-30ed-af0c-db23e8745cdd | -5.23115 | -40.56563 | 2026-10-01 15:29:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| c96f3d42-34ed-3b1d-aa0d-5e87f52e1542 | -13.79828 | -39.88515 | 2026-10-01 15:29:00 | NOAA-20 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| f9b5e94e-796a-35cc-affa-ca78063ca292 | -13.45194 | -40.38834 | 2026-10-01 15:29:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 204642aa-7fc0-3ab2-b637-a6ab30c6a929 | -8.92331 | -36.95081 | 2026-10-01 15:29:00 | NOAA-20 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e9e86385-77e1-3a8f-b0ae-4224631b848d | -9.83327 | -37.24267 | 2026-10-01 15:29:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 448238c9-82ed-3732-acb6-bf292f0d1894 | -11.32598 | -40.34484 | 2026-10-01 15:29:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b9b613fe-5189-3914-bf00-3611966dd384 | -10.91515 | -40.16364 | 2026-10-01 15:29:00 | NOAA-20 | PONTO NOVO | BAHIA | Brasil | 2925253 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 9f0cf059-7328-388e-b226-a86dcdc588db | -7.79598 | -37.11894 | 2026-10-01 15:29:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 1196f3b9-5200-38e0-a5e6-ad255ed77f6d | -8.10259 | -39.59143 | 2026-10-01 15:29:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| cf525060-b7b4-3872-b7b3-deac75588297 | -15.24564 | -40.64645 | 2026-10-01 15:29:00 | NOAA-20 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| fde93326-c428-34f7-92b5-a384c7f77361 | -15.00133 | -39.73903 | 2026-10-01 15:29:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 33c1bab7-17cf-3dee-9c3e-70af9102fbdf | -8.54498 | -36.38464 | 2026-10-01 15:29:00 | NOAA-20 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5c100680-ea71-35c8-85b9-7a9778f35124 | -12.85876 | -40.66869 | 2026-10-01 15:29:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 0cfe0173-710c-3418-ba93-118732f392ca | -11.82194 | -41.08763 | 2026-10-01 15:29:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 7b12a9ec-fe52-309c-b591-ae6c9b602a9e | -8.30582 | -39.37968 | 2026-10-01 15:29:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a28c130c-f546-3c44-a109-50c86a47d582 | -14.38319 | -40.35361 | 2026-10-01 15:29:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| d8246b9c-ea0f-377b-83c0-1e61069b7890 | -11.18325 | -40.56084 | 2026-10-01 15:29:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| e0524216-1d77-3e10-bd32-5f3a110b8f45 | -15.243 | -40.64714 | 2026-10-01 15:29:00 | NOAA-20 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 514e7a4e-e430-3263-96f8-9766d6575737 | -8.54803 | -36.62837 | 2026-10-01 15:29:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f283f026-103a-3469-96a6-658262698da6 | -7.87549 | -37.51506 | 2026-10-01 15:29:00 | NOAA-20 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1f765fbd-f1ab-3f27-8475-feac443569cb | -10.68979 | -40.84642 | 2026-10-01 15:29:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 062abadf-0fd4-3e25-be16-eb6e3e8d2080 | -9.10451 | -41.36948 | 2026-10-01 15:29:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 436b135c-853f-3454-8286-2adacfa15b23 | -12.17992 | -40.98769 | 2026-10-01 15:29:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9074e971-31d0-3b6e-adaf-94540ca4a30c | -10.18373 | -38.06825 | 2026-10-01 15:29:00 | NOAA-20 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 11fcc4eb-b928-37d6-ab66-87c27c51517a | -14.53847 | -40.84739 | 2026-10-01 15:29:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 0bd3b17a-45e0-3d1b-99aa-2a45feb54af1 | -9.38251 | -38.82101 | 2026-10-01 15:29:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 1f315803-77cd-3d21-853f-bbc8f382ea7d | -9.87032 | -37.52444 | 2026-10-01 15:29:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 802725a4-fef4-3634-8956-a82d1a52edf5 | -3.71205 | -40.43684 | 2026-10-01 15:29:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 760b0de9-5b45-3e17-9ddf-00cc5a68d750 | -3.16576 | -41.33996 | 2026-10-01 15:29:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 36533332-c644-31e0-b6d9-92f34799d533 | -6.3666 | -55.1261 | 2026-10-01 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| dee36046-0889-3bc5-909c-a52248735fe1 | -11.2087 | -45.1939 | 2026-10-01 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 2b93e3e8-b000-34a0-9830-464224c33c51 | -1.4303 | -48.9316 | 2026-10-01 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e145685f-4f62-3dd1-a703-f6258dd1cb02 | 1.62 | -55.9035 | 2026-10-01 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| a477b713-114f-3f83-8e7a-5784f447eed5 | -11.2091 | -45.1709 | 2026-10-01 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| ddf70ea3-bfaa-39ca-a555-97b2da21f200 | 1.7115 | -55.9221 | 2026-10-01 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 0959fbd5-b32c-3e7e-b3bd-6de297f67eca | -2.4969 | -56.9108 | 2026-10-01 15:30:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 192.8 |
| 0242f876-8c5e-3d03-bf44-95af778ce312 | -6.7554 | -55.0864 | 2026-10-01 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d827f433-ca3e-354d-bcd3-03f57144f706 | 1.6749 | -55.9225 | 2026-10-01 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6adf2cc3-cf18-331f-a628-677d5f2a1349 | 1.6566 | -55.903 | 2026-10-01 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 0b0bbd3b-7156-3bf0-afae-d9c9c25665c6 | 1.8769 | -55.6239 | 2026-10-01 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| e5dec1eb-0bfa-34df-9fea-549bc681cd5e | 3.6036 | -60.4334 | 2026-10-01 15:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 94e9b80b-1978-3586-a510-26841ed49dee | 1.8037 | -55.6249 | 2026-10-01 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| d55c051a-2873-35ba-bf6f-2bd30c95cdea | 1.8586 | -55.6241 | 2026-10-01 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 84640f44-cd59-37dd-8adb-96327d7271d0 | 1.6749 | -55.9619 | 2026-10-01 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| bd691611-cbd1-3686-8089-97a24de526b6 | -7.14675 | -39.77554 | 2026-10-01 15:31:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 58a23b3d-87e8-3c08-8d29-3eb75fb08f50 | -7.3845 | -38.0513 | 2026-10-01 15:31:00 | NOAA-20 | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 45.6 |
| 0714c90e-a7e2-34c0-b95d-ede7dd648880 | -7.1935 | -41.74308 | 2026-10-01 15:31:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b0f88794-8d6b-3759-98c5-578ccb9c8275 | -7.08639 | -37.49382 | 2026-10-01 15:31:00 | NOAA-20 | SANTA TERESINHA | PARAÍBA | Brasil | 2513802 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c2887df7-7116-39a5-847f-aa157776c40e | -6.18197 | -39.38099 | 2026-10-01 15:31:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 3857c587-224f-314d-a02e-1bde57948f8c | -7.36597 | -39.35521 | 2026-10-01 15:31:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a8c5489e-9088-3489-b1fe-309d1ef77519 | -7.39045 | -38.05346 | 2026-10-01 15:31:00 | NOAA-20 | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 67e312b8-dfc4-36f4-b8ff-87c209fa93fb | -6.96031 | -39.54897 | 2026-10-01 15:31:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a40d309b-cbf5-34d1-af9e-e9c2540cc742 | -7.39094 | -38.0572 | 2026-10-01 15:31:00 | NOAA-20 | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1735557f-60b5-3bf5-9bb5-22acfaad7758 | -7.58069 | -41.29918 | 2026-10-01 15:31:00 | NOAA-20 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 11e82d0d-df13-3cd0-93b6-e1a2b6a70de2 | -7.1528 | -35.48753 | 2026-10-01 15:31:00 | NOAA-20 | GURINHÉM | PARAÍBA | Brasil | 2506400 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 89593728-27c9-3e1e-8724-0c9ad2571060 | -7.08844 | -37.4943 | 2026-10-01 15:31:00 | NOAA-20 | SANTA TERESINHA | PARAÍBA | Brasil | 2513802 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8fd2fb74-1b72-3ecd-9ed7-e143da8eca6e | -5.0689 | -36.97972 | 2026-10-01 15:31:00 | NOAA-20 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 2520beb2-6b59-31c6-b736-33eb878dce01 | -5.0639 | -36.98045 | 2026-10-01 15:31:00 | NOAA-20 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 9db26fa4-faf7-37e5-9b4e-a6575b42aa9e | -6.84437 | -41.41882 | 2026-10-01 15:31:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 39e18be6-3681-3a6d-8ef0-137d95175de1 | -6.95361 | -39.54521 | 2026-10-01 15:31:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| fe7171d6-3a79-33a1-a3ab-a2ef2a78fe44 | -7.38496 | -38.05479 | 2026-10-01 15:31:00 | NOAA-20 | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 39.2 |
| a4a8c506-dfbb-317b-83b9-c72cd9ae8bfe | -6.9542 | -39.54975 | 2026-10-01 15:31:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 8c072d65-3a30-3e67-a673-18df95349c8e | -7.19461 | -41.74036 | 2026-10-01 15:31:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 976cdae7-3be5-349c-8d2f-c72a4de6b81d | -6.17905 | -39.38344 | 2026-10-01 15:31:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 3cf6c7a9-7b1b-3225-b667-81e2123dacb8 | 1.8221 | -55.5851 | 2026-10-01 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 5b4f2ae3-1f49-3970-b5e4-686ed28f0277 | 1.62 | -55.9035 | 2026-10-01 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 2844d41c-9787-37b3-89f5-664325ba5deb | 1.675 | -55.9028 | 2026-10-01 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 543dfb3e-48e2-35d7-bfad-cbfd23b318b6 | 1.8037 | -55.6249 | 2026-10-01 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 1488bcad-7e9e-33e9-83c4-7f4842ff6142 | -1.4672 | -48.931 | 2026-10-01 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| a523e881-0f77-3a28-8592-a22452e46511 | -2.9886 | -57.9132 | 2026-10-01 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| a569d05a-bab6-3bd9-a180-d4758c5817ec | 1.7115 | -55.9221 | 2026-10-01 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 05e7f487-7d1c-3e8f-ab39-58e40d0f5502 | 1.6749 | -55.9225 | 2026-10-01 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 30151fcb-5d53-3f86-ae3d-2e39c6b6a2b8 | -11.2091 | -45.1709 | 2026-10-01 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.8 |
| c6c98015-6ada-35fe-93f1-767c839cac7c | 1.8769 | -55.6239 | 2026-10-01 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 356a8c56-53e7-30a4-8260-a3c5ce8d1521 | -11.2091 | -45.1709 | 2026-10-01 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 193.8 |


[Clique aqui para ver as próximas entradas](README107.md)
