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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df703004-ab62-3676-80e5-35a8a18921a5 | -2.91863 | -48.24014 | 2025-07-18 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4be2d85-317e-395a-9bca-35398fbb2062 | -2.9249 | -48.23715 | 2025-07-18 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b18321c0-426a-346c-a9b2-abdf9344c986 | -3.11543 | -47.01417 | 2025-07-18 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 08426c77-b159-37fe-98bf-2c4d98e01feb | -3.11514 | -47.01228 | 2025-07-18 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b5c62931-8883-3692-8eb8-3b9b7bade1d4 | -3.12202 | -47.00832 | 2025-07-18 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d071312d-a9fa-3b0c-8a7b-14e0054c7942 | -2.63834 | -47.30659 | 2025-07-18 05:14:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5439ca6d-96ca-335d-8319-6a697dda75ab | -3.12161 | -47.01506 | 2025-07-18 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 32c23f1c-ba1f-3a97-8244-c9fdf04ed7a9 | -7.70444 | -47.29052 | 2025-07-18 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e70fff4-70f3-3eb0-97ec-d6f4e402768b | -3.93694 | -50.44544 | 2025-07-18 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ba5211b-3297-3bf0-a988-370ee5d3c3ca | -3.85588 | -50.08537 | 2025-07-18 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60a47e7a-2c95-3625-a5d5-f4972a154f9c | -7.82321 | -63.2958 | 2025-07-18 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca8e8202-83da-385d-b07a-d479d5a14bf1 | -8.88116 | -50.15067 | 2025-07-18 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 03a9fe97-037a-3d94-80fc-1facaa2daea7 | -3.40116 | -47.50259 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 138b44eb-82d0-3cd5-b82c-83e048fbfea4 | -9.50697 | -47.56578 | 2025-07-18 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2419fdb2-67d5-367c-8747-fc48650e3e82 | -3.3951 | -47.48799 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 91751b99-d54c-3d88-8902-fc2c58e98cd7 | -8.0393 | -46.6179 | 2025-07-18 05:16:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd519d80-2767-3cd2-89a6-66dd769ad767 | -7.49007 | -63.82024 | 2025-07-18 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 52ecd3cc-fab6-3344-b4a1-875df381b59d | -8.04559 | -50.07993 | 2025-07-18 05:16:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 139bde29-1ae2-3408-8331-095d7fddd567 | -8.8852 | -50.15244 | 2025-07-18 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af690d7b-d249-38ca-bffd-02be543946de | -9.0194 | -59.76516 | 2025-07-18 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a2f6fb7-c01e-3e27-8709-5424f729c675 | -3.07412 | -52.42604 | 2025-07-18 05:16:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 669281b1-eece-342c-9f83-cb3ca6bf7e93 | -8.87925 | -50.1553 | 2025-07-18 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cfcb81d2-64fc-3537-93cd-7b77c7672836 | -9.50788 | -47.55915 | 2025-07-18 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 831b8f9f-7ba7-35f6-a1db-db243abeb0cf | -10.84018 | -48.3452 | 2025-07-18 05:16:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0cc6576-ab5c-340b-ace6-3f882b322137 | -8.64573 | -47.75066 | 2025-07-18 05:16:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5266f336-6e91-3a9e-acab-3172e2306b42 | -7.53366 | -61.34676 | 2025-07-18 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 358b043e-44d7-3ecc-b663-cfbd66e4f132 | -6.61734 | -47.19527 | 2025-07-18 05:16:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 803cce98-6b3b-358a-8d8d-14a1b2f46f57 | -3.39042 | -47.47834 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b54d68bb-7fb1-39e1-a945-6485543cd9a4 | -8.88472 | -50.15597 | 2025-07-18 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c43d63c7-0ca1-3ef8-a3ed-6b0a8a4893f5 | -3.20302 | -54.58873 | 2025-07-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23b90945-e82d-3f41-82ba-4bb9df0961cb | -10.84074 | -48.34043 | 2025-07-18 05:16:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e081c8e0-f011-37ed-84cc-9dac4bcfe7e8 | -3.73089 | -53.98907 | 2025-07-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0279aea0-fbc8-39e1-854b-fa818e733d48 | -8.64892 | -47.75759 | 2025-07-18 05:16:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 899a27a8-7a9a-3ece-8b2c-5a69839cd782 | -3.73014 | -53.99408 | 2025-07-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c31f891-862d-3952-9153-f9e97283b46e | -8.88025 | -50.15775 | 2025-07-18 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 322b267f-080e-37b4-b2fe-de1ad0c8538b | -9.02079 | -61.22148 | 2025-07-18 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ac55f53-3ab1-3462-ab02-137403d627bd | -3.82924 | -47.74345 | 2025-07-18 05:16:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d148331-d128-3f14-8089-3421472638a2 | -5.9981 | -52.19793 | 2025-07-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4712ca46-4fc2-3ff5-a2fd-3819f0aa15b6 | -3.39645 | -47.47913 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| cd182c90-1a80-3273-99b7-f657f75d4c8f | -9.80318 | -47.74088 | 2025-07-18 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7296c48d-4fa9-3f65-9b92-587ab8fa8b05 | -3.38841 | -47.49164 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 47308d0e-96e6-3463-925b-38be6682a057 | -8.96958 | -61.51471 | 2025-07-18 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c745632-45ca-38bc-bf88-c662bab27a83 | -3.85803 | -50.08483 | 2025-07-18 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65fed58d-63b2-3e10-b6ae-596b76a71d04 | -3.38306 | -47.48638 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 870a1eef-b4ee-31b0-8589-8c6da4b17337 | -8.87524 | -50.15351 | 2025-07-18 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1e2fc2ba-42a5-31a7-a514-6a1ffea9f513 | -3.39909 | -47.50216 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4ee020ea-72db-3e86-904d-8ff6199cb99d | -4.11056 | -48.21402 | 2025-07-18 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bad78fff-902f-394e-b33d-e5bf5638bdcd | -3.39041 | -47.49203 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c4ef3855-2f73-3e59-a338-3d980693fe8b | -3.59102 | -48.94178 | 2025-07-18 05:16:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6beff3c3-dcb9-336d-91f8-d187f7f03212 | -3.82862 | -47.74773 | 2025-07-18 05:16:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f1811f3-f0c9-3d49-b9dc-539484e60106 | -3.58553 | -48.94099 | 2025-07-18 05:16:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03fe12ae-c13b-3b4b-aec9-00882b1c16d3 | -7.63475 | -56.736 | 2025-07-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a9213451-43af-3d9d-9d45-73c44cd9512c | -10.72037 | -49.48554 | 2025-07-18 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 38af6bdb-8fe7-3733-b048-5aad34b16181 | -9.02416 | -61.22203 | 2025-07-18 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d65b0e5-1ef8-32ff-812b-b263faaa7809 | -9.0202 | -61.22511 | 2025-07-18 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a27e6397-390b-3d4d-ba2c-9028b2a54a32 | -3.3863 | -47.47789 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0d496dde-c502-3f8f-96fc-db350ad207ba | -8.96617 | -61.51414 | 2025-07-18 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40343780-28d0-3ec6-bcc8-1f5adc2e1855 | -9.50071 | -47.5637 | 2025-07-18 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 268c768b-44b7-32ac-a891-13124668864e | -8.6451 | -47.75579 | 2025-07-18 05:16:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6580863f-8e90-3933-a413-572e31a68269 | -7.63593 | -56.72809 | 2025-07-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6756bba-2f76-3d68-8550-b5276d0700cd | -4.48107 | -46.07891 | 2025-07-18 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f7820e6-fbb5-3c37-a199-75d7f25d7ec3 | -4.30413 | -48.10642 | 2025-07-18 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca5fac9c-a8f7-35e3-9094-940057861820 | -4.87325 | -48.90884 | 2025-07-18 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7144f12c-8d19-3208-a60b-5c7c86eeb53f | -9.50762 | -47.56026 | 2025-07-18 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b4b54ea1-ec3d-39b5-88c5-b3e752b7cb6e | -8.88617 | -50.1549 | 2025-07-18 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d0459dd-14c7-3338-8ab7-432369a9a662 | -8.64959 | -47.75244 | 2025-07-18 05:16:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9476e08e-176c-3eac-89d4-a6357b25a7b9 | -7.63123 | -56.73545 | 2025-07-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 693aa8f6-ecaf-3265-846d-a054663081ae | -3.38566 | -47.48235 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fa9a9ecc-5447-3404-ae3e-84da112a5bfe | -9.24276 | -48.5654 | 2025-07-18 05:16:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43d97f6e-8904-360d-a23f-00b6f8c67875 | -9.80243 | -47.73837 | 2025-07-18 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 550397b0-dc99-302c-91fe-8f5f254b4d09 | -10.71505 | -49.48046 | 2025-07-18 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3c76670a-08b3-3809-a154-233130dc1f36 | -4.10589 | -48.20552 | 2025-07-18 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c34ec9fe-9b4f-32e0-89a3-1f3470c881a6 | -7.59152 | -46.30608 | 2025-07-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f0a1605-1d84-3f76-aef6-e19898fb5879 | -10.72088 | -49.48138 | 2025-07-18 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e5a16985-47cc-399b-9f50-84f184a76992 | -4.15126 | -48.21944 | 2025-07-18 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa189c77-44e4-3999-aa8a-1ece38c69089 | -9.76169 | -48.75637 | 2025-07-18 05:16:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e97f73bf-3417-394e-8e7a-c7cc8514893c | -4.30999 | -48.10723 | 2025-07-18 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| e6c22921-d591-38ce-b14c-98e8db382487 | -10.71454 | -49.48463 | 2025-07-18 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b33bc85c-af60-30ee-83e3-cf1cf63f062a | -8.8807 | -50.15423 | 2025-07-18 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 335f2c3a-cf0b-373c-b0ec-01676e7c31c9 | -9.80381 | -47.73555 | 2025-07-18 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06faf19b-ef5c-33fc-9975-275b272c45b5 | -3.19108 | -60.60788 | 2025-07-18 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a06cbacc-91d3-334e-8933-6837e8262d71 | -3.39169 | -47.48315 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 5b41cd7d-7d14-3a23-9cdd-8fa54d738835 | -5.19721 | -45.49223 | 2025-07-18 05:16:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 1acff34b-c780-308d-963f-19919d4469f4 | -8.65144 | -47.75669 | 2025-07-18 05:16:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d237659e-7f88-30e2-9c14-c3dcd6c0cb0e | -3.39578 | -47.49735 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de53ea90-c9c4-36e3-9646-9c6b6a6da2e1 | -3.86098 | -50.08614 | 2025-07-18 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61477b3c-fee3-3b19-9b92-d3fba7ea0812 | -5.99875 | -52.1935 | 2025-07-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| de57c35c-20ae-3938-b2f0-a45ab0bee613 | -4.15068 | -48.22351 | 2025-07-18 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05808a5d-d972-30f4-87db-6bf718bb8705 | -3.39772 | -47.48395 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 730b6577-c613-32ac-9d1b-a8d46285badb | -7.53306 | -61.35051 | 2025-07-18 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3960813-bc95-37cf-a467-bf2b2cb7c2be | -9.01766 | -59.53715 | 2025-07-18 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9624d9a6-fb71-3e05-af80-b29eda4081af | -6.61895 | -47.19425 | 2025-07-18 05:16:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32ea9197-30b0-3dd5-81a5-c322996e7d35 | -9.27565 | -49.63401 | 2025-07-18 05:16:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 101f0c9a-1760-37da-9a62-57613a5b51d1 | -3.94387 | -48.09394 | 2025-07-18 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cee33aea-b02a-3d37-bae2-92f7c0e9e263 | -4.95619 | -47.70502 | 2025-07-18 05:16:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d45f1259-aea9-3e62-b3d0-da6cd7981fad | -8.87973 | -50.15177 | 2025-07-18 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fe3934a3-e479-3489-bc40-cf9b1da65675 | -3.39233 | -47.47869 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 7987a614-5b0d-38e1-9bfd-b27dae472764 | -3.07541 | -52.42738 | 2025-07-18 05:16:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ac055df-3c0e-315e-9cca-cad9573e198b | -3.72385 | -53.98286 | 2025-07-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 129dc152-1d6a-3713-a6e9-21ea27ee8a4e | -3.38907 | -47.48725 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |


[Clique aqui para ver as próximas entradas](README27.md)
