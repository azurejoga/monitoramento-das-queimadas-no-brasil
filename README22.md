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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49490324-682d-3e06-8786-40d7ce680690 | -7.1947 | -35.1641 | 2024-11-17 03:44:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 22e863d9-387f-3a34-b645-f0c6c9783dfa | -4.30231 | -48.07143 | 2024-11-17 03:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 09b8ffb2-12cb-37fb-9353-b1a789211822 | -4.74266 | -48.12091 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da621a9d-bdd3-3251-ab0d-93d721e3ef74 | -6.8816 | -44.76978 | 2024-11-17 03:44:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0b77154-8143-3d7b-8243-6ede32a176f6 | -3.01269 | -45.39806 | 2024-11-17 03:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5e07a66-d942-3692-a7a2-51957c046253 | -7.97599 | -35.34369 | 2024-11-17 03:44:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 05bee750-d6bb-30eb-9263-2b48ea6d50de | -7.65805 | -38.84188 | 2024-11-17 03:44:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9093845e-7bb3-336b-8273-5c3fe0cb4a93 | -3.93358 | -46.17462 | 2024-11-17 03:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 246120e3-1da9-3e0b-967a-4b3ac52a865e | -7.65689 | -38.83628 | 2024-11-17 03:44:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a2131da-daf9-393a-ae89-28fb5ebccdbe | -3.35314 | -46.06579 | 2024-11-17 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a11deaec-8a4d-3705-8379-446b5c6f887f | -9.38656 | -40.57701 | 2024-11-17 03:44:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3353ae3f-a786-3264-831d-6f17736c7150 | -3.42352 | -41.0275 | 2024-11-17 03:44:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 82c479b8-a2b2-3aa0-949a-24ccd807be64 | -2.60395 | -47.54562 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 96ea6e67-7f24-3a74-802e-84928059886b | -7.44486 | -39.09445 | 2024-11-17 03:44:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 096b9039-b269-3c2e-9e0e-35e41be30f24 | -5.58716 | -45.20769 | 2024-11-17 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ab73d1b-924e-3db9-b227-7d1ee2cb1c43 | -2.67323 | -46.21005 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b67dee7c-5bf5-3fbe-b487-f9f3f43490f8 | -4.37821 | -48.08552 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 94773011-bc67-3f62-8020-755a72e2fe3f | -5.27747 | -44.90946 | 2024-11-17 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 08ae7f89-5764-31d4-ba55-c9854906dd75 | -7.31178 | -39.17331 | 2024-11-17 03:44:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b4d1239a-a2cb-3f6e-a9f1-4c1228167f64 | -2.60866 | -47.54851 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1532c718-66fd-35ec-ba55-a0ad33e7fa12 | -3.07448 | -45.46632 | 2024-11-17 03:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bf952a94-9320-3472-a2e0-831583757aa0 | -4.03897 | -45.47335 | 2024-11-17 03:44:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d5ba65e-093b-3a4f-9c2a-c768c64ab521 | -4.20524 | -48.70392 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bc49d066-c2ed-3ef2-a449-e9879ad51af4 | -4.74388 | -48.11426 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 945605fc-7dfa-3068-9e36-3001bd7cdadd | -3.91619 | -46.53143 | 2024-11-17 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c446424b-a6f7-3e2e-bda1-7292e35068cc | -3.6265 | -43.16244 | 2024-11-17 03:44:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8794298d-02e1-3807-929e-fcd5da9908b2 | -5.40424 | -46.35199 | 2024-11-17 03:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ba7e379-2b88-3d40-b92b-9f6f9c977082 | -4.21828 | -47.21704 | 2024-11-17 03:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe389f27-7b06-313b-a43a-77a2514b3b06 | -7.09012 | -42.17466 | 2024-11-17 03:44:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7ae7bee2-a996-3e69-9f05-6c9f3cf9873e | -3.89618 | -45.91631 | 2024-11-17 03:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea39a986-f93c-3fef-878f-0902f5c0b9cc | -3.57742 | -45.68331 | 2024-11-17 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dde0d8b3-6fa6-3920-b1d1-a040dcebafd6 | -7.30073 | -39.1716 | 2024-11-17 03:44:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e9bab1c0-92fd-35cc-9622-f08380815150 | -4.7318 | -46.84361 | 2024-11-17 03:44:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9054f1a8-30b3-30fc-8e61-05b079d0d03a | -4.30073 | -42.1861 | 2024-11-17 03:44:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 30e3edd4-71d4-3de3-96a5-08f97469e5c2 | -6.50079 | -38.29895 | 2024-11-17 03:44:00 | NOAA-21 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bb5d4c4a-31d0-3926-8148-25148f2ab14d | -3.91705 | -46.52647 | 2024-11-17 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 29edb0d7-25ba-3973-a932-e700fa54b563 | -8.43732 | -44.204 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 33211abf-b2bd-354d-91d6-64b112b8175e | -8.44386 | -44.19624 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6f44e259-3031-3198-a5ad-03490976dac4 | -2.58512 | -47.5638 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 67b53b82-ff5a-33ce-9b68-6a79b00728ce | -2.8664 | -46.72808 | 2024-11-17 03:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 85e28978-e3d9-38f3-ba14-c5c6ab523a87 | -2.5841 | -47.56986 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 2001b077-a0f4-31bc-ba83-34113a20d2e4 | -6.97131 | -38.48309 | 2024-11-17 03:44:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fb899257-0c5b-38a4-ad78-5f08936fb07d | -3.04558 | -45.76216 | 2024-11-17 03:44:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7a00e7c-402a-3d0c-b081-15900628ab48 | -7.9793 | -35.34421 | 2024-11-17 03:44:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7b2d3027-6a4e-3b04-9a5e-366409dc5267 | -7.22318 | -38.00171 | 2024-11-17 03:44:00 | NOAA-21 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 18246307-cff7-3343-bfe7-d752c500970a | -3.93438 | -46.16989 | 2024-11-17 03:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00cdb86d-8338-31f8-90fa-a6cdd149146b | -4.40891 | -44.3169 | 2024-11-17 03:44:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7df1ce3f-0323-3247-ab5a-a86f6b9b382d | -3.78269 | -43.91148 | 2024-11-17 03:44:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4985c17-7e01-369c-8323-2472956d73d3 | -3.8932 | -43.13752 | 2024-11-17 03:44:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7f5ab4b-a29e-3450-9563-9c8dc4d72e7e | -8.45092 | -44.18549 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bc171a8-77bf-31a7-bf2a-fa493639f116 | -3.4998 | -43.79174 | 2024-11-17 03:44:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7bacac7f-f3eb-391e-ab82-d7970ea7502a | -6.82059 | -46.77838 | 2024-11-17 03:44:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e91e87d-18a4-33aa-9e46-57b96ce8eed7 | -6.16953 | -41.16925 | 2024-11-17 03:44:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8cf3ff42-1560-3b53-a32c-038d586fb3f9 | -8.43574 | -44.21287 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 18087372-8579-39da-bb58-665b38b99d8d | -3.78498 | -46.04848 | 2024-11-17 03:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a2f0d52-8a75-3037-bcf7-6611d23f118a | -2.60183 | -47.55777 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 570cfda2-47e2-3784-8899-00e3f4374a58 | -6.38553 | -45.68481 | 2024-11-17 03:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0b69c9e6-f844-35dd-bb59-fac1d4e2020b | -7.44593 | -37.48893 | 2024-11-17 03:44:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7c0f5702-ee33-3d46-9913-610352594db1 | -4.21732 | -47.2225 | 2024-11-17 03:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a178e350-22d0-31cb-a8dd-9ed8b4c2f0b2 | -2.57725 | -47.56892 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6bd48b7-5e4b-33f6-b43f-247c44f77798 | -2.68033 | -46.20611 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a18dedd-3322-36cb-80b9-24e36de0d543 | -3.00232 | -45.42316 | 2024-11-17 03:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 203d630f-29e8-3618-9a14-70d820fbca8c | -4.82131 | -47.32408 | 2024-11-17 03:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef1eacef-7280-3597-8aba-f5de504dccb7 | -4.55828 | -47.99881 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 4f21d82e-7b77-3bd1-8340-491a812c4e5a | -8.45432 | -44.19551 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf4d8ecf-0c08-34e0-bfb8-f1018f1dceb1 | -2.66696 | -46.209 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba4eb146-1168-3fea-962d-365c01de9bd8 | -4.59624 | -44.58126 | 2024-11-17 03:44:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba8fabbc-ac54-35e4-8385-0a2a888bb54c | -3.35393 | -46.06111 | 2024-11-17 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 289f0ae3-69a3-3702-9b4a-b0ddbfe8b2cd | -6.81931 | -46.78048 | 2024-11-17 03:44:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 389f69e1-9bf1-318c-9e9e-ca026e593f73 | -8.44626 | -44.21186 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e650ed9f-6c86-36b7-9b97-5740924ea718 | -4.82154 | -47.32255 | 2024-11-17 03:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a224fa33-46ad-3b3c-8a79-01f08c9caddd | -8.44179 | -44.20792 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a0b5377c-937b-343a-8542-5ee0d76274d6 | -6.40161 | -44.74342 | 2024-11-17 03:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9cea4d5c-6ff1-33c4-8265-87165b504798 | -3.74325 | -44.53214 | 2024-11-17 03:44:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcccb3b4-e5e1-394d-91fd-d66275aaba96 | -5.88077 | -40.15323 | 2024-11-17 03:44:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8ae573b0-dcc4-34e5-b47e-930736785b99 | -5.12095 | -45.1572 | 2024-11-17 03:44:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 169d1fae-fdd1-397d-b24f-d4d1cfd92f16 | -8.4082 | -44.13614 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daf49915-0978-320d-8723-ae35e40d698a | -8.44127 | -44.21088 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3a860e93-c44d-3734-b595-b37de19b2f90 | -3.4857 | -40.64812 | 2024-11-17 03:44:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 49ca90fa-5d2f-3a77-91c0-df74c6bcc81b | -5.62894 | -46.36566 | 2024-11-17 03:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c948922a-bc4c-3af3-8ee8-50f33c4600d8 | -3.3462 | -46.06937 | 2024-11-17 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a31a434-e767-3287-8847-6f28f5c12266 | -3.41218 | -45.86534 | 2024-11-17 03:44:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0ab3514-5cae-32ac-9c6d-fe41f4ab3587 | -6.98986 | -39.66158 | 2024-11-17 03:44:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 9d1cad28-0266-3b0c-af61-6df3e798c55d | -2.60958 | -46.25903 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 89bb6d3a-12bb-3cda-a6d3-c9e2fc916a10 | -6.98209 | -38.48436 | 2024-11-17 03:44:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1888dff0-0894-3c62-99ef-148f27625fc2 | -5.1775 | -46.171 | 2024-11-17 03:44:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e21729f-6672-32af-a158-ac2cd56801c8 | -5.00013 | -44.33519 | 2024-11-17 03:44:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2db5fb25-61e1-30f4-9e02-63a6b29e308d | -4.24043 | -41.92906 | 2024-11-17 03:44:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 0a42add3-ae45-3ba8-8e51-9536267bf32d | -6.3113 | -39.48965 | 2024-11-17 03:44:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 12743b5f-3f00-3728-bd0e-f3a5181c5ae5 | -2.65904 | -46.21771 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6ba1ddb-9e00-381e-8303-83e2697b8ffb | -3.77968 | -46.04281 | 2024-11-17 03:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d772b2aa-d4eb-38c7-b877-410047933268 | -4.57959 | -48.02657 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| c5f66c7f-80e9-3a0e-93d9-684f76cde264 | -5.46568 | -42.15174 | 2024-11-17 03:44:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e29f1a44-8db0-3a96-9b6d-b46f8a391077 | -3.78713 | -43.90942 | 2024-11-17 03:44:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2399b18d-3ad6-3a12-b6ae-48b11fba157f | -4.56248 | -48.00432 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 004ba30b-9c68-305d-92ef-eb649f248410 | -2.86088 | -46.72163 | 2024-11-17 03:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 9d8aae0b-b4d4-33e7-9b16-3cb2df6098c4 | -2.60653 | -46.2603 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad595414-7888-35d7-827a-aa33b1476b60 | -5.14755 | -39.71378 | 2024-11-17 03:44:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c152e16-57eb-36ed-9c7d-c75558953edf | -3.16826 | -46.59899 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e3093f9-e15a-3cde-8a1e-55c189feba7d | -3.21497 | -42.0874 | 2024-11-17 03:44:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README23.md)
