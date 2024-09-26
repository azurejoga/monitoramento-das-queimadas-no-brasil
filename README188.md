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

## Dados Diários - Página 188

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 113760f4-2c82-3454-b519-724151664ef9 | -12.8106 | -51.1502 | 2024-09-26 13:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 303.1 |
| 02326d1f-da9d-30cb-866d-ff63be7d1fdd | -12.8294 | -51.1692 | 2024-09-26 13:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| ab714d63-b1e5-35b3-8968-3336aa44d7c0 | -12.8297 | -51.1479 | 2024-09-26 13:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 510.9 |
| ce67f200-b536-3433-9bbd-c9ddb16a7d96 | -12.8465 | -51.295 | 2024-09-26 13:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| b2a48e76-340b-386c-ac7a-9d1594aab330 | -14.57 | -45.7205 | 2024-09-26 13:36:28 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| dfe4271e-6f60-3438-9603-a2a2bd817ea4 | -14.5705 | -45.6973 | 2024-09-26 13:36:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 332ae699-dcc7-3989-b0a1-a9f2d6671346 | -17.8068 | -43.2338 | 2024-09-26 13:36:45 | GOES-16 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 9a2958b2-1d10-3122-808f-fd5c77c85027 | -17.9922 | -44.4756 | 2024-09-26 13:36:46 | GOES-16 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 851498a4-fdc8-38fd-bf59-cd8d27704678 | -17.9929 | -44.4514 | 2024-09-26 13:36:46 | GOES-16 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 10d3f066-cc1f-3fb0-b9f0-e12d7b7d4005 | -18.9102 | -49.1674 | 2024-09-26 13:36:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 124.8 |
| caa9c962-32c1-30e1-b3f3-f15f7b3ee799 | -21.9374 | -48.5688 | 2024-09-26 13:37:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 0e9059f4-eaee-3038-bad9-3e01a66afca0 | -21.9381 | -48.5453 | 2024-09-26 13:37:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 153.2 |
| f863844f-7aec-3d80-861f-83c8bf49c32e | -21.9583 | -48.5638 | 2024-09-26 13:37:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 59e16ba9-9b82-3d12-b456-1e900cc5678e | -22.679 | -47.3927 | 2024-09-26 13:37:11 | GOES-16 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 178.0 |
| eb06f721-a4da-361f-b530-709be9d2c2b0 | -4.3882 | -43.2663 | 2024-09-26 13:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 57c88265-8637-3825-84ae-a11f3bbcb374 | -5.212 | -47.9577 | 2024-09-26 13:45:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| ceaeabb9-3f5b-3baa-ae82-c1dbffaed6a3 | -6.7908 | -41.2254 | 2024-09-26 13:45:45 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 1d960b5d-432c-3a8c-a630-d546a4f5619d | -6.943 | -42.7654 | 2024-09-26 13:45:45 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| c48ed2b8-01f9-32c3-b0c6-dc752242189f | -6.784 | -59.3052 | 2024-09-26 13:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 261a428f-1349-3d24-ab05-8c4f6bc18309 | -6.8023 | -59.3237 | 2024-09-26 13:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 6df763a9-61e0-39d2-ad75-4ba3ac5b6107 | -6.8024 | -59.3044 | 2024-09-26 13:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| b9f8b36f-c023-3ab9-a87e-ebd58144d5d0 | -7.0595 | -44.1316 | 2024-09-26 13:45:46 | GOES-16 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 44f239af-eb7d-3f3f-960e-abd986f60233 | -6.9305 | -63.1241 | 2024-09-26 13:45:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 74f75e7b-d5a6-31c7-a962-7fdfdb505ccc | -6.9306 | -63.1053 | 2024-09-26 13:45:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 0dd35e4e-60f1-3844-ba5d-8a238fd28a14 | -6.9681 | -62.9349 | 2024-09-26 13:45:47 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 1e0472c8-5701-3d68-93bf-9f81b47f1b6f | -7.0981 | -59.2343 | 2024-09-26 13:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f8148013-7a67-326f-a753-e5c6cca748a5 | -7.3606 | -44.1035 | 2024-09-26 13:45:48 | GOES-16 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 2555daca-c246-33de-8dd1-90297ba74c57 | -7.3695 | -43.3352 | 2024-09-26 13:45:48 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 07ccefa8-68f9-34c9-9728-80af9258fd88 | -7.2006 | -60.6706 | 2024-09-26 13:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| d0870361-d408-303a-a67d-7b190eb98e39 | -7.2627 | -59.4974 | 2024-09-26 13:45:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 3747a30f-7ea5-364c-a51a-1b439b155554 | -7.2906 | -61.0869 | 2024-09-26 13:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.5 |
| b29fe6be-0086-35dc-9e4d-a28cd7c8d938 | -7.4761 | -43.8839 | 2024-09-26 13:45:49 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e5329ded-4fe7-31a2-b1d1-83b4b842270a | -7.4774 | -43.7677 | 2024-09-26 13:45:49 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 108ea4b2-4a03-3ba5-ab1d-a8b3467dd4f8 | -7.4777 | -43.7444 | 2024-09-26 13:45:49 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 05313976-c222-377c-b3cb-9f8ffecc29de | -7.3637 | -55.5134 | 2024-09-26 13:45:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 1492f669-e55b-3731-b70b-a7e41177147a | -7.3639 | -55.4935 | 2024-09-26 13:45:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| df5bb959-8b40-3db5-809a-e1a03d07cf94 | -7.3824 | -55.4924 | 2024-09-26 13:45:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 35e5ca2c-db76-3dbb-bb7c-48e475e56d2e | -8.1075 | -55.39 | 2024-09-26 13:45:53 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 42561714-61c2-36e4-b727-898f86ab914a | -8.3805 | -45.3994 | 2024-09-26 13:45:54 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| ebfab812-517d-3782-b1e7-454e5182d3b6 | -8.3155 | -54.9956 | 2024-09-26 13:45:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 1198e52c-f3c3-39ee-952f-f9b3df3c0ff2 | -8.4646 | -62.6556 | 2024-09-26 13:45:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 0b815915-08f1-3e85-beee-079ec6b6c8a6 | -8.5187 | -55.1834 | 2024-09-26 13:45:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| acbc438f-6278-34b5-9ca3-5ae9292f3570 | -8.839 | -44.9628 | 2024-09-26 13:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 238.7 |
| 7ad8b454-377d-3597-86c9-94975056229f | -9.787 | -53.5885 | 2024-09-26 13:46:02 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 310a9669-98b8-373f-920e-ce7764bb290c | -10.0136 | -53.467 | 2024-09-26 13:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| cce50c00-704d-3f9d-a134-b38a940c3f34 | -10.0139 | -53.4464 | 2024-09-26 13:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 2ad93a55-db45-3647-98d2-984234a4682d | -10.4371 | -45.7992 | 2024-09-26 13:46:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| e8fc3feb-6376-3c78-ba2f-3ac0e44dde38 | -10.3589 | -49.9098 | 2024-09-26 13:46:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| d588dfb3-e781-30bc-b252-6a9f1fc0b950 | -10.797 | -45.8893 | 2024-09-26 13:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 4ec4906b-cc93-3482-a486-09af434d9a52 | -10.8352 | -45.8843 | 2024-09-26 13:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 5d9c57db-4f6f-3e4a-94cd-db8a942691d0 | -10.5878 | -54.2375 | 2024-09-26 13:46:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| c3299271-f9bc-3a47-aaa5-8ecdb8e97f83 | -10.6657 | -50.9866 | 2024-09-26 13:46:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| c86648f2-0f5f-358d-8741-f161da0d1a2c | -10.8525 | -51.1581 | 2024-09-26 13:46:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| c31010a5-c5df-30a5-b8c4-027bbb3268cf | -10.8714 | -51.1561 | 2024-09-26 13:46:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 16fa2449-3a28-35fe-94dc-c30977176735 | -11.1542 | -46.1824 | 2024-09-26 13:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5a1e232f-1b3c-32d8-b2f9-a75175a46eef | -11.0569 | -51.4328 | 2024-09-26 13:46:09 | GOES-16 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 31453e14-2cc5-3203-a59f-8c7fa698608f | -11.2317 | -46.1041 | 2024-09-26 13:46:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| d5e3039f-ca01-3fd1-aba7-d85ddf9a52bf | -11.1931 | -51.1648 | 2024-09-26 13:46:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| ba3eed85-d9fe-35a1-bd17-2330f60dd9d2 | -11.212 | -51.1627 | 2024-09-26 13:46:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 211d1e24-11e0-3834-847c-faee7f65f250 | -11.2123 | -51.1415 | 2024-09-26 13:46:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 42035816-221e-3e68-bc2f-9e9f00e5a75f | -11.1847 | -54.7565 | 2024-09-26 13:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 5965c19c-73fb-36ed-b5e0-50a81e2ce07a | -11.222 | -54.7939 | 2024-09-26 13:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| d9a1a37d-9594-3e92-936d-6b4d83ad2d72 | -11.6988 | -47.8576 | 2024-09-26 13:46:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e3eda2d3-6d1e-383a-85e8-7cbadc117bc2 | -11.8536 | -47.7264 | 2024-09-26 13:46:13 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 179cb3ea-e1ff-3f16-996c-b5e038df97ee | -11.8422 | -49.635 | 2024-09-26 13:46:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 5cef07c4-a78c-3c44-8bf8-b1683f3ad21e | -11.8609 | -49.6544 | 2024-09-26 13:46:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 2d7ef926-4156-30ad-94fd-42c43c86486c | -11.8613 | -49.6327 | 2024-09-26 13:46:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| d9cf2c76-c100-3e75-ac3c-a32cc6e676f2 | -11.9365 | -47.3367 | 2024-09-26 13:46:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 55d32395-ffd2-3b5f-a70c-5eece92b610c | -11.9369 | -47.3143 | 2024-09-26 13:46:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| f5f6d314-7b96-3865-85c9-2dc3d79e2a51 | -11.9373 | -47.2919 | 2024-09-26 13:46:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 83446552-0eda-3467-9353-083472c139f4 | -11.9564 | -47.2893 | 2024-09-26 13:46:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 4f0af0c5-865e-3258-b705-1fda3b6b12c8 | -12.2053 | -50.7959 | 2024-09-26 13:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 552b6bc6-4b8f-3c8e-ac91-d7acba4b1ec7 | -12.2857 | -50.5294 | 2024-09-26 13:46:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 349a43af-49d9-31c8-a621-bcc74e9dd932 | -12.286 | -50.5079 | 2024-09-26 13:46:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 07102144-4eab-3d3e-ae52-d8644c51abb8 | -12.3048 | -50.5271 | 2024-09-26 13:46:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 99709812-24c9-30f6-8d5f-2fb76252a807 | -12.4835 | -48.9224 | 2024-09-26 13:46:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 0e6ad1ca-fe2e-3898-a2a0-82d4ef827db0 | -12.4974 | -50.4177 | 2024-09-26 13:46:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 669d1839-b345-3a5b-bc1f-5d764edf8830 | -12.5464 | -53.5147 | 2024-09-26 13:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 76e426ab-bc25-37c9-a23f-764f8a1afbe6 | -12.9516 | -45.3242 | 2024-09-26 13:46:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 34d71a50-85ec-37ba-8920-f3d6bfef43e3 | -12.8297 | -51.1479 | 2024-09-26 13:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 4642f3f8-4036-31d4-ad63-7001a85fdf96 | -12.8462 | -51.3164 | 2024-09-26 13:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 1f8b2b69-d012-3042-b30c-6c16d6f7735d | -12.8465 | -51.295 | 2024-09-26 13:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| cd7ca8b1-6874-37ca-ab7f-d339d81eb6d3 | -12.8486 | -51.1669 | 2024-09-26 13:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 99798a20-98d2-369f-8912-30788e8a2e60 | -12.8653 | -51.314 | 2024-09-26 13:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| cfd55ccd-585a-31f3-a037-66a6c560e40c | -12.8674 | -51.1859 | 2024-09-26 13:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 48f5dcfd-2eb0-3dd0-88a6-245886517937 | -13.1603 | -45.4983 | 2024-09-26 13:46:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| b9cd97e9-8f7e-33e1-b2d2-c86ee9c9c9d2 | -13.1796 | -45.4952 | 2024-09-26 13:46:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 306.1 |
| e1a945e9-d6a1-3138-acfb-a4e6c4d16bbd | -13.1963 | -45.6308 | 2024-09-26 13:46:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 342.7 |
| e5a21c77-4e55-33d2-aa8e-5c3efc357935 | -13.1418 | -48.5464 | 2024-09-26 13:46:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 1e387a81-bb0f-3124-9a1e-a8588ed0343e | -13.7335 | -50.9902 | 2024-09-26 13:46:24 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6243fe85-b9fd-362c-8fb4-0056e76356d4 | -14.0006 | -51.1263 | 2024-09-26 13:46:25 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 5db7245f-d576-3e83-a3cf-1f7c8b632716 | -14.57 | -45.7205 | 2024-09-26 13:46:28 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 4fa9dc7e-6b40-395d-9aa0-04f9cc87fb00 | -14.5705 | -45.6973 | 2024-09-26 13:46:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 82aa01f0-dbbe-3750-b22b-9f12d88b707f | -14.6924 | -45.4665 | 2024-09-26 13:46:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0ca539cb-08d4-3ce7-8e92-cf180d135280 | -17.8068 | -43.2338 | 2024-09-26 13:46:45 | GOES-16 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 237b681e-66cd-33e7-919e-f9cce542bbd9 | -17.9929 | -44.4514 | 2024-09-26 13:46:46 | GOES-16 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 158.2 |
| c4437f71-72d0-3c4f-99b9-03208e3bdc90 | -18.9102 | -49.1674 | 2024-09-26 13:46:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 123.8 |
| 2e7bff24-fd1d-3d12-a6ea-8ca96d2912db | -21.9374 | -48.5688 | 2024-09-26 13:47:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 4c38bc36-f256-3b59-b932-0f01a33e0b7b | -21.9381 | -48.5453 | 2024-09-26 13:47:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 6948d82d-4d75-3f4d-8da7-b15ffb60257e | -21.9583 | -48.5638 | 2024-09-26 13:47:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 142.1 |


[Clique aqui para ver as próximas entradas](README189.md)
