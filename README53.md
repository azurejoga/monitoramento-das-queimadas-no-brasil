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
| cec65c7c-9dd7-318b-bcf0-4929723c40d1 | -7.35914 | -44.06075 | 2025-10-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23c9e869-e5c4-3a2a-9e68-f623f52f604d | -5.87513 | -44.82858 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2cbd377-86be-330f-980a-dcbc166b686c | -5.72231 | -44.5219 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f7cbfc9-ae90-3b65-9094-6c015ad4b650 | -7.1834 | -41.68353 | 2025-10-17 04:19:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 55b278c3-a935-3f2a-89e9-060978390c05 | -10.11685 | -44.61461 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a361f57-dbf4-3079-aa04-155f9a678874 | -6.46281 | -41.8249 | 2025-10-17 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 96d51e02-d25b-3b91-bcd3-43e5bacfeaf5 | -7.1776 | -42.36624 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 19d47b67-1927-390c-902a-30d09c1ec48c | -4.92248 | -41.52014 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cf5bb993-bba7-3a46-b4ca-46235356b3ae | -8.23997 | -43.43389 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ab4971e-5a4e-3953-a212-c14adceabc10 | -10.59926 | -47.39676 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67d8a3f6-377a-3b0d-83ce-c7094a3f3674 | -9.25938 | -44.35357 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6ab88ba-0d91-38b2-a876-8078dfdda84d | -10.4208 | -48.88312 | 2025-10-17 04:19:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2f3493c-b9ca-3af1-b68a-4d641729e555 | -8.37452 | -46.30617 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73d1911b-797d-3b21-96fe-0b20b2496688 | -9.13842 | -46.64189 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 4f114bdd-d5b1-33f9-a15c-653e12931e66 | -10.09723 | -47.65048 | 2025-10-17 04:19:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b3b7328a-3227-3521-9edf-6f7015114d47 | -7.22369 | -47.86993 | 2025-10-17 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2183eefb-a28e-34be-8e18-7305fecefca3 | -10.18044 | -49.5178 | 2025-10-17 04:19:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e84fec2-df1f-30ba-8bf6-cd117653b500 | -5.86815 | -43.91269 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9677d6e9-9cc9-3d41-b793-d5ccc8feea43 | -8.37787 | -46.30668 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63d04d06-b9de-353c-a0ba-1a5275e4c971 | -3.50984 | -52.48883 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 36e8c963-4697-3204-b07b-bf26ec4607f8 | -10.50846 | -43.43147 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 78a59b89-e041-31b0-addf-4df9cdb0da81 | -4.42166 | -40.18282 | 2025-10-17 04:19:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 62beeacc-0505-32eb-9619-8820168cc459 | -5.33384 | -43.08271 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb71986c-e3f1-3df4-9260-0aa7a742cbf2 | -5.84217 | -43.88376 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f0107fc-3366-3fbe-bb59-1281a080fd65 | -10.43449 | -45.02471 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cefa8722-0610-3821-bd9b-19a57ee08e06 | -8.36912 | -46.25429 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad30da5b-4743-3226-96b1-f508755b6dea | -5.7289 | -44.52292 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ee4604c-ee83-3aa0-bb2a-2e36069b18c5 | -6.16599 | -40.90589 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7bf9a4a8-2780-39c4-87ff-72771180d817 | -7.17145 | -42.52281 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 52492545-1513-3bc9-a16b-da539dd1d178 | -3.65776 | -50.27 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e5ec4824-9972-3011-898f-87aeb4f412f3 | -4.47602 | -42.93253 | 2025-10-17 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 555d52df-2fea-3f2f-a36f-7ad6a91757e4 | -5.28293 | -47.93093 | 2025-10-17 04:19:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ee232fc-b004-3093-acbf-bcc3850cd9c9 | -2.86927 | -50.72836 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e5cbe96d-ae6e-320e-bbfe-156339b741e7 | -4.64154 | -42.18035 | 2025-10-17 04:19:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3147ad64-04a7-3620-b610-453d1652126d | -10.2864 | -44.04028 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| bbf59ed5-ea91-3e72-b934-d946e36fb7e3 | -9.21113 | -47.84475 | 2025-10-17 04:19:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93c87235-ccc5-3584-a01b-4103153eb7da | -10.29313 | -44.04132 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| a4d6e9e8-898a-3c9a-a284-7a14dd204eec | -5.27078 | -43.26882 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b0a4a84-3411-3997-aaaa-396a7f7b6ef3 | -8.26211 | -44.09345 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45326668-74ed-340c-b2e8-0ae6b84e8c5e | -6.12912 | -41.75692 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f440e995-6888-3a4f-b830-2bce7dfb34e3 | -7.30068 | -41.95932 | 2025-10-17 04:19:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 34c9db50-77b2-3da9-a9ca-33a890eca0ae | -11.39846 | -44.13804 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0abf77a3-8f2d-3f45-8061-1d711778d663 | -9.27648 | -45.29668 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d395020d-9601-35d4-b46e-759cff2f3f13 | -10.61981 | -42.31593 | 2025-10-17 04:19:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 75299f90-4816-3f46-984a-cc7d32a5ea09 | -7.83161 | -45.45965 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 944b66c3-0600-3bbc-980d-236b2d9d386f | -7.17701 | -42.37012 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 70488b29-ffb8-3fb7-b04a-8d14c94c33a7 | -5.27563 | -43.21535 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 180ea34f-cf16-3c01-ba6b-6420fabe4642 | -7.10971 | -44.74539 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db8c170c-134d-3e56-86a5-fcd72cd93453 | -5.62826 | -42.67691 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9cbfa9db-6e79-33c8-b6a3-81e55f790898 | -5.90293 | -44.73766 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 730c87d0-eb23-3059-90c1-ad499efe4280 | -4.71061 | -46.09771 | 2025-10-17 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1384505b-f058-3a28-bfbd-c1eeee78a4ef | -4.64962 | -47.94937 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d186c0a2-2f1d-3fdf-93f9-9611276035e7 | -8.16168 | -43.99469 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4c85848-9cd4-393b-8303-9890369bc5a4 | -10.18198 | -49.50859 | 2025-10-17 04:19:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c389bd24-1337-38ec-b364-79dbbd6c022b | -5.29464 | -47.92837 | 2025-10-17 04:19:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7886229d-bb69-3096-bc3f-800095c92868 | -7.48485 | -42.13262 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 38de0be4-b8d7-3700-a31e-88780afdf3fc | -6.3218 | -44.32076 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 599e7797-a02f-38e0-a505-735c3ef322d3 | -7.6645 | -45.63197 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a4f5946-70b7-376f-81a3-7590bb0043a6 | -8.49896 | -48.4912 | 2025-10-17 04:19:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 771298b4-5114-386a-b596-c3fad970915f | -7.13032 | -43.7805 | 2025-10-17 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80354266-1c31-343a-b9c6-ac698eaa56cf | -10.27238 | -44.04184 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19ca942b-7005-308f-8567-83d978cc746f | -10.8463 | -43.95677 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20752c9d-850d-395a-be70-64caa5c5dc38 | -5.60379 | -46.38137 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a268cff7-75cd-3298-be28-004556b13987 | -4.64757 | -50.4944 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47ceacb6-0380-3dbd-8b8f-35fe279e1cb4 | -8.56319 | -44.58896 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b75e7f7-9be7-31f0-94b9-48810f756b36 | -11.48701 | -44.19328 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| caa34b46-5edc-31bb-8a79-187a72b04990 | -5.72507 | -44.52585 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49858ea7-cbf1-3c7d-9a98-a5095f625722 | -10.50438 | -43.36507 | 2025-10-17 04:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17d0809a-128f-3413-b4b1-c5df249b0123 | -6.44203 | -43.39163 | 2025-10-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b2d4b8c-e3b9-3404-bd21-8c231c202803 | -5.97858 | -45.50952 | 2025-10-17 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39ef4ec1-e2ae-34d6-aa64-10d51611987b | -11.39924 | -44.2022 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c35058f7-d446-3f29-abbe-06d7d8cfb04b | -5.30122 | -41.07959 | 2025-10-17 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 681205d9-9350-3234-959b-3676f315a75f | -10.62083 | -47.32822 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d930d100-029a-35d0-b684-2034cf5bf4ff | -7.46013 | -42.15333 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 04bf785e-a97d-3001-8af1-7daf32ebe250 | -5.42942 | -43.29718 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80578602-d84d-3aef-aca7-bf807a54c05e | -10.2673 | -44.02989 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b64f9e3-4e1f-3c8d-a69d-bed9b590799e | -5.23208 | -42.01176 | 2025-10-17 04:19:00 | NOAA-21 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 87498f85-d8e9-379c-85b7-93992973fafa | -8.39651 | -46.23286 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c678b1dc-5090-3635-a738-4d9992c995c4 | -9.24886 | -44.35553 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae434894-05e2-3229-96a1-6961871a7d0a | -9.05224 | -46.98593 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34af753a-dc70-349c-9ba7-09a49a2b5818 | -6.42765 | -44.03612 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 495bf519-4507-343b-8c50-f8a5d3ebcc9f | -8.20492 | -43.31275 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 420b5dd8-5918-347e-a8a2-0d2bb70feda6 | -4.43875 | -50.55376 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a1a2726-8b0e-34ab-ac14-75a4e557f13b | -9.13287 | -46.63361 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db25cc6b-f4b6-3d72-ad8e-b4b1f5e8ea98 | -10.91568 | -47.4408 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f96341fb-c222-3436-b56a-b16b95f825fd | -6.20717 | -41.74222 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 61be4e31-6cdd-3d29-afc7-2f3fee3c8d00 | -8.49395 | -48.49907 | 2025-10-17 04:19:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef0d3547-1b6d-3899-92b3-27a1a905e1ed | -10.66398 | -44.8598 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 743f1620-bfb9-3a55-8b3d-5fa0e45f57c5 | -10.51762 | -45.12453 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b922e6af-62ee-32db-ae53-4ed65b0ecbb3 | -6.76398 | -42.3807 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 106ade56-5f09-3f7f-ac2e-f1cc32a6dbb1 | -6.32175 | -40.94492 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d1c5cf50-128d-30ba-9abc-4ea80baa0bb7 | -4.3748 | -46.53284 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47d786d0-4dd3-312c-af6d-3e4aca3801e4 | -5.74979 | -47.47332 | 2025-10-17 04:19:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db152fa2-949c-3bdb-8a40-59738ef52af9 | -9.23005 | -48.59067 | 2025-10-17 04:19:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0c6f9bac-5961-3f10-ab46-0000d39a6ffa | -5.59049 | -43.64154 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34a9b96c-cb56-3267-b280-c2109c583a87 | -8.19419 | -43.31481 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 721387fd-c167-39bf-b041-7b6306185a75 | -3.72998 | -49.68405 | 2025-10-17 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c97468c-7461-317c-bf6b-824c12f91192 | -10.15522 | -44.54098 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48827aba-ed0b-3977-a07b-bd7c3c938851 | -8.30584 | -43.41026 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fc11dee6-ebc9-361f-9e94-37908dec20b6 | -11.38016 | -44.21424 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README54.md)
