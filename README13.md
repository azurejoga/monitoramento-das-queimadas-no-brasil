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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff0ac467-27fa-3757-a2ef-44a74f7a0e71 | -4.4632 | -43.2386 | 2025-10-28 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 84a95e48-a87c-32fb-ac25-e4f758d5f05e | -10.5878 | -49.7567 | 2025-10-28 04:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 3831b23e-2bc6-3d32-b5ee-195c9c9c89e5 | -10.5686 | -49.7803 | 2025-10-28 04:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 63eb8c46-6a8f-37db-928a-d0211a025387 | -7.9693 | -46.7423 | 2025-10-28 04:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 262.7 |
| b08b17d7-59c1-3cd0-aed1-75077caaaf5a | -7.9691 | -46.7646 | 2025-10-28 04:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 813c7f01-cb65-3032-92c3-f34eae6efca4 | -3.0343 | -45.3896 | 2025-10-28 04:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 40.4 |
| b75b0d32-2a13-3336-89ce-850b09017f04 | -10.5683 | -49.8018 | 2025-10-28 04:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 1a8487ad-e1b1-3ada-8019-fa118b1fcf9e | -10.5872 | -49.7998 | 2025-10-28 04:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 85155a5d-0cea-3b6d-94a3-9c4aaeb7dc91 | -11.2798 | -45.5052 | 2025-10-28 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 9b4beb25-74e9-3e49-b455-f08d0ff2e968 | -3.0343 | -45.3896 | 2025-10-28 04:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 40.0 |
| b669343e-f811-36f8-b961-1819c626ce11 | -7.9693 | -46.7423 | 2025-10-28 04:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| a567fd2e-e183-31c9-989c-591af9707323 | -13.6324 | -47.0211 | 2025-10-28 04:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a2b6294d-266a-3dd4-baa8-7da967d14d58 | -10.5683 | -49.8018 | 2025-10-28 04:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 8a9583c1-c982-3f6f-aec1-973a4d297797 | -10.5878 | -49.7567 | 2025-10-28 04:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 6125e8f7-fff4-3fdc-8892-7b1c1ba7d0b5 | -7.8223 | -46.4664 | 2025-10-28 04:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 544a4114-dfe4-341f-bce5-b37b15f12b23 | -10.5875 | -49.7782 | 2025-10-28 04:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 22f22258-51af-358a-89ad-ae8b10a393b3 | -3.0344 | -45.3672 | 2025-10-28 04:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 539b34b3-da93-3d91-8e72-9175dbe480d8 | -3.0157 | -45.3903 | 2025-10-28 04:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 8eca0ac6-2a32-3b5f-8e5a-a3b81f90ade8 | -4.4632 | -43.2386 | 2025-10-28 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 5263c296-ae2a-389e-a2d4-356ca803ddef | -3.0158 | -45.3679 | 2025-10-28 04:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 116.6 |
| d1942a1f-90cf-332e-b231-773f97d4e790 | -7.9691 | -46.7646 | 2025-10-28 04:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 70fb64e4-ba9c-380c-aeb6-4a8d98416dc1 | 1.82672 | -50.51279 | 2025-10-28 04:10:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45f0dd7d-aeb6-3b40-b114-d1380ea80ce3 | 1.8262 | -50.50931 | 2025-10-28 04:10:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da0f8bb2-abf1-3393-86c1-1a82195e6092 | -2.64272 | -48.50388 | 2025-10-28 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fda3849e-234d-3bdb-a56b-9a451435c372 | -2.42259 | -48.44156 | 2025-10-28 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 11c1df67-8e6e-3aed-b3d8-c2912fec9c74 | -5.48504 | -44.37853 | 2025-10-28 04:12:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c521d72-9532-3838-af5d-fa9dd684056f | -6.11055 | -41.73954 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e4fb2391-a92d-3cd2-9f8a-24a2846ad8e4 | -5.66072 | -41.12442 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 066504b1-98ab-39de-b8cb-0cb901277982 | -3.91027 | -43.32308 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38bd6a06-dd21-39fb-a29f-575f0768b5cf | -3.04892 | -53.01632 | 2025-10-28 04:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 450df5b0-70a6-31c3-978c-2abb9528337b | -6.13649 | -41.83736 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aabb9e92-6538-3930-91fb-85fc75e43462 | -2.53501 | -45.13534 | 2025-10-28 04:12:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a58a3a9-18ab-31d7-98f3-9ddc92a0fa24 | -4.90774 | -48.56502 | 2025-10-28 04:12:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d7b30d3-03fb-3641-b0ed-fb18a52feba6 | -3.01709 | -43.22488 | 2025-10-28 04:12:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 841892b4-1b86-3bca-9285-bfdce3469e72 | -4.40898 | -43.1176 | 2025-10-28 04:12:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8776619-3d32-3afd-ba26-f9ca61e89d6d | -3.60831 | -43.55566 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69565c2b-98ae-395f-9bfb-3d4327045b93 | -6.14091 | -41.83081 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d9f0e644-95f4-303d-87fe-c0b3675f0048 | -1.83721 | -45.29332 | 2025-10-28 04:12:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a068648-7154-3e1d-b15b-27b7f0f5554f | -1.5058 | -53.12439 | 2025-10-28 04:12:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb95fdd1-71fc-38dd-bb44-c80dceadb8aa | -2.95113 | -49.34618 | 2025-10-28 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1135ad3f-122e-3f8e-a630-47fdd19ed2bf | -6.09792 | -41.77734 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| de685718-18b5-34da-a516-23e56649fe11 | -3.58004 | -41.06343 | 2025-10-28 04:12:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 51ca6aec-cb88-3be5-8cdc-65a781af8374 | -3.5888 | -43.63602 | 2025-10-28 04:12:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c3bcfe38-eddd-35f2-afd5-0af852c40015 | -3.58322 | -43.62787 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3895340-59d7-3d5e-861a-27f52ac52189 | -4.35903 | -50.51414 | 2025-10-28 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6fdb2563-ea64-3dcd-9151-1317ce26aa51 | -6.15962 | -41.57596 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 52b79043-d6cd-3018-940a-29cf1f51f28a | -4.17907 | -47.65009 | 2025-10-28 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95c1d975-ad89-3d9b-87ea-6f8e4499fbe6 | -5.592 | -41.31322 | 2025-10-28 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d96a3901-cac6-36b6-a515-002c310bfa34 | -3.88055 | -47.99743 | 2025-10-28 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80821270-bd29-3ebf-983e-7051f792221f | -3.08448 | -44.44803 | 2025-10-28 04:12:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64d2f9c9-b7e8-3967-933b-f0825392ddcf | -5.27034 | -44.31552 | 2025-10-28 04:12:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0aec9f15-d4d0-3618-b994-e4ce26a24a15 | -4.50069 | -42.83533 | 2025-10-28 04:12:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d798241-1141-3f88-bfd8-1608226487ca | -3.77055 | -48.92562 | 2025-10-28 04:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cc271d2-98ee-3e1e-8967-521675b7feaa | -4.45558 | -43.64247 | 2025-10-28 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| db8d3686-8295-34c2-9cfc-6d65757f7cb9 | -6.13215 | -41.71024 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1a44fe08-6e58-30a1-bed9-d4376422d3c5 | -4.33036 | -48.09564 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b6ba812-c8ef-33b8-8800-917914e406a0 | -0.90571 | -47.55387 | 2025-10-28 04:12:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2015a69-a0ff-302a-bfd0-b67b15da7df7 | -3.54332 | -54.69306 | 2025-10-28 04:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 149c85cc-7c7c-375f-a8d2-c731d82d81b7 | -6.1383 | -41.71472 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 17ff9a6a-db97-315e-ab26-adb863361d35 | -3.60497 | -43.55514 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 366c22a8-4a01-3bdc-9dd9-006ce8a9a068 | -5.43201 | -40.87246 | 2025-10-28 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2a61680c-d95e-3869-b612-add0108cb91f | -6.17503 | -41.69852 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5539c256-d0f3-39d4-a3ed-4fb92561a8c6 | -3.02973 | -41.68882 | 2025-10-28 04:12:00 | NOAA-21 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3645c556-4883-3141-93b1-1379bd598214 | -2.91992 | -48.72007 | 2025-10-28 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ee305f6-5820-36c8-bad5-175d389daf71 | -2.4221 | -48.44454 | 2025-10-28 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 02205062-c208-3180-852a-e99cf27f94ec | -4.15955 | -46.79047 | 2025-10-28 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d58775d-9a2e-381c-b8bc-e605cc55fb46 | -3.08201 | -51.28353 | 2025-10-28 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d627c47-c575-30c3-9a54-f6cb55c61f7b | -5.84424 | -43.27404 | 2025-10-28 04:12:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6413fedd-66b3-3b25-91f6-371616ff7d60 | -3.02466 | -45.3722 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 2755f262-1308-3fb8-b05e-f74bad922245 | -4.72649 | -46.8158 | 2025-10-28 04:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04d151d2-10a3-3a55-8ede-d966c7fdba1a | -4.59117 | -48.53545 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86da5eb4-fa88-3e99-a8be-4454be10147e | -3.99329 | -43.31455 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e6db8d5-e963-38b4-b13c-3fde9eabf236 | -5.81498 | -40.82348 | 2025-10-28 04:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2f459954-ebb0-3e67-bff8-f5c8ae3dcada | -3.5934 | -48.99061 | 2025-10-28 04:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c10ce4fd-25cc-3a32-8933-77e1760815d9 | -2.75391 | -45.40474 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 03686a4a-846b-3dee-b134-be659de3983c | -4.55752 | -46.63489 | 2025-10-28 04:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20e43cf3-515a-3ee3-81d0-ce4e7d121c96 | -5.26976 | -44.31914 | 2025-10-28 04:12:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45edf88f-a14f-3515-b3f9-1a5d7f3b4ff1 | -4.30664 | -47.53683 | 2025-10-28 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 791108eb-945f-36a0-ae2e-6b52cbd745a0 | -3.44474 | -50.22165 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b707190-5176-3420-8224-de02a2135842 | -3.46778 | -49.97006 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41fad123-96e8-3964-8e28-c64cddd1153e | -3.5771 | -43.60151 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04366a8a-0ccb-3f89-9a49-e38bdc7297cc | -3.58043 | -43.62382 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2efbdde6-790a-37a8-b7fe-031404649c30 | -1.67227 | -51.99518 | 2025-10-28 04:12:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0723a7ac-029d-362a-a66e-667265e3beff | -3.46861 | -49.96488 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8b79b5d-f6ff-3ea3-a94b-a6330a2b3459 | -4.35724 | -50.51233 | 2025-10-28 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ecbc7ac5-fe21-32f5-b759-2b07a4c54d33 | -5.42297 | -45.37033 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68daabdd-bf49-31d9-84bb-263b4d33f1bc | -6.09156 | -42.14959 | 2025-10-28 04:12:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a28263d6-7fb2-365b-91d1-95a8dfff6a34 | -5.52315 | -41.7135 | 2025-10-28 04:12:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8f2e919c-fee8-3b10-83c6-4ac91ee97b8a | -5.43541 | -40.87304 | 2025-10-28 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a0a50cc5-db24-3998-86b9-43866a84f682 | -3.1282 | -49.10059 | 2025-10-28 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5104503a-5434-32a6-a698-216a69ebe63d | -3.26229 | -44.63104 | 2025-10-28 04:12:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f961061a-e336-3728-a2b1-460e41400a15 | -4.33098 | -48.09192 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d79228d-9fc5-3fa2-9fe1-e63a6554fdd4 | -4.26964 | -48.69662 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a84d851-646a-30e7-a3e1-72ca5aab506f | -3.57485 | -43.6157 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d43a08d2-c944-3150-a810-c1efd44a99b6 | -4.46201 | -43.23574 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| bfb63182-1416-306e-b66d-a2cae7d3749f | -6.15893 | -41.53566 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 80212605-8b1a-3780-a179-3f24a9950cb2 | -3.70713 | -41.57856 | 2025-10-28 04:12:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a85e811-9e2a-3705-ae76-4637a955e08d | -4.86523 | -47.3544 | 2025-10-28 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6da54cc-7d78-3b8e-8a11-900d1de72c4a | -5.26697 | -44.31499 | 2025-10-28 04:12:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6a7eff2-37f9-384e-b8bf-d8d7d92b8a25 | -2.52724 | -47.29954 | 2025-10-28 04:12:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README14.md)
