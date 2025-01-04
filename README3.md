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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9060daa-63e0-3199-8911-b41fbb6cef30 | -10.6124 | -44.3517 | 2025-01-04 02:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 257c12a1-126c-390e-a18b-b162d27cac7b | 1.34 | -60.3122 | 2025-01-04 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| b33a30a9-dbc5-3871-b517-67806b99e735 | -10.0082 | -36.2463 | 2025-01-04 02:50:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 99.7 |
| 95f350ef-bff5-3c90-a567-1cd2e7cf5cb6 | -10.6319 | -44.3257 | 2025-01-04 02:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 26de1625-2cf5-3cdc-adbe-946a931f927f | -10.6319 | -44.3257 | 2025-01-04 03:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 47e04c67-8a6b-3bdd-8108-f18981cb42f1 | 1.34 | -60.3122 | 2025-01-04 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 116.5 |
| ab10b46c-4afc-3008-8810-9c0700f98d20 | -10.6128 | -44.3284 | 2025-01-04 03:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 188.8 |
| a790238e-dd79-3760-b53f-2ba70d416f3e | -5.7393 | -35.3915 | 2025-01-04 03:00:00 | GOES-16 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 55.2 |
| ca4839bc-569c-3415-ae0c-a7e3b81cd4da | -10.6124 | -44.3517 | 2025-01-04 03:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 8ec3bd7e-eb2f-38a5-934a-2dd37404fe74 | 1.3401 | -60.2932 | 2025-01-04 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 7c6d9fe9-02d8-3ec2-b9b0-039cf7ba445b | -10.03 | -36.24 | 2025-01-04 03:00:00 | MSG-03 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2c1784ae-72f1-34fb-87f3-c9e00bbac705 | -10.0 | -36.24 | 2025-01-04 03:00:00 | MSG-03 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 489195ee-119e-3b79-b67b-f76ef97e12d0 | -10.6128 | -44.3284 | 2025-01-04 03:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 164.5 |
| dfc48fe6-7993-3a22-ba20-747be8c96c4f | -10.6124 | -44.3517 | 2025-01-04 03:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 5cd1310a-5898-3424-ac93-575fc886a86f | -10.6319 | -44.3257 | 2025-01-04 03:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 3e807ff2-3839-3bf1-bb72-58d691fe09c1 | -10.6128 | -44.3284 | 2025-01-04 03:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 50da4484-bb94-356b-b348-810b0d42c50f | -10.6124 | -44.3517 | 2025-01-04 03:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| c75b506f-1f9e-3c23-bde4-d355b7c6698e | 1.3401 | -60.2932 | 2025-01-04 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 48bf0db8-a21a-393d-b6ab-095eb4130b6a | 1.34 | -60.3122 | 2025-01-04 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a2cab756-36a6-34e8-a0d2-e7af4bd87bbd | -10.6124 | -44.3517 | 2025-01-04 03:30:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| eccaaf80-18ff-33cb-a670-124bc7f0bd4c | 1.3401 | -60.2932 | 2025-01-04 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 80ee551a-48b4-3091-bc6c-a6ca041cc49a | 1.34 | -60.3122 | 2025-01-04 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 305e0ac7-a06e-3c6c-b158-5fad328db368 | -10.6128 | -44.3284 | 2025-01-04 03:30:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 160.8 |
| be34396c-c9dd-3962-85fa-ac401a8686fe | -10.5937 | -44.331 | 2025-01-04 03:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 2ad979ca-5a59-316b-b9ee-87423f497036 | 1.34 | -60.3122 | 2025-01-04 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| fcb518b2-cd01-32a5-9888-4223e31303d6 | -10.6128 | -44.3284 | 2025-01-04 03:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 6b7593c8-c981-3309-83f7-b939c4295668 | 1.3401 | -60.2932 | 2025-01-04 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 42b409bd-b35f-3d66-bfac-23b5e05ab269 | -10.6319 | -44.3257 | 2025-01-04 03:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 92f8ff55-d83b-3436-9b90-5eb7beab15fc | -10.6124 | -44.3517 | 2025-01-04 03:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 127b4c43-66fc-3d08-b295-cf5e00141d37 | -5.50276 | -44.29846 | 2025-01-04 03:42:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d17549a2-9f43-3777-85ff-2ecb282d43d5 | -6.79757 | -35.18585 | 2025-01-04 03:42:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5e6638bd-2d15-3411-9e6f-97c20ce14f7a | -3.13582 | -40.04295 | 2025-01-04 03:42:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 119028d4-dfa3-327f-bf01-98133ed050ec | -4.00665 | -40.93462 | 2025-01-04 03:42:00 | NOAA-21 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 09cf7f46-6d5c-30fc-899c-df3197b562b0 | -4.41142 | -43.38747 | 2025-01-04 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8af5d164-9dc2-35bb-8820-b698ab109969 | -5.72347 | -39.50505 | 2025-01-04 03:42:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4350c9a7-7573-3fdf-80ea-34b2707319b7 | -5.72269 | -39.5098 | 2025-01-04 03:42:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 69f0079f-9f8e-30e1-983e-82117b59f7d7 | -4.82197 | -37.75667 | 2025-01-04 03:42:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fdd1ae67-d3ab-31bb-8019-441c5a42ef2d | -4.82262 | -37.75267 | 2025-01-04 03:42:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0013a5b7-5c6a-3b4d-a234-09e0eedb48b9 | -5.16712 | -40.76378 | 2025-01-04 03:42:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fccc2a96-a7ba-325a-8bc6-57197b7c4a84 | -4.41091 | -43.39046 | 2025-01-04 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff863e7f-9659-3076-bb28-d6fc4b8ece13 | -3.44542 | -39.175 | 2025-01-04 03:42:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1406b2fa-10c5-377a-ab65-40e91e678dea | -6.18686 | -36.55949 | 2025-01-04 03:42:00 | NOAA-21 | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d81406e4-d8b5-3b4f-956d-5ff80f7cf24e | -5.99976 | -41.13512 | 2025-01-04 03:42:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7d7af71a-4d13-3dc1-a708-2bb6e17580a7 | -4.39867 | -37.84163 | 2025-01-04 03:42:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b48c1eb7-f599-3072-9800-705ce80f0e43 | -5.69809 | -40.19042 | 2025-01-04 03:42:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f20af19e-a5b9-353d-b377-bc6bf084d03b | -5.71428 | -41.4081 | 2025-01-04 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e0a4f78e-68d2-349a-8567-d555bc07ce03 | -6.34613 | -39.56791 | 2025-01-04 03:42:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c7e50c9-0e76-35e5-885d-845e9b406998 | -5.09277 | -40.5854 | 2025-01-04 03:42:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5bb1feba-8325-391a-8d08-f9305040187a | -4.16311 | -42.02625 | 2025-01-04 03:42:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 09e5e1a6-9b99-3d6f-923d-e1dc23fa02bc | -3.44641 | -39.17242 | 2025-01-04 03:42:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a763d6b7-1244-3cf8-9b1b-0a2485ae684f | -5.33414 | -41.21975 | 2025-01-04 03:42:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 627f173f-444a-3837-be90-40b27fe0b28a | -4.52249 | -38.6795 | 2025-01-04 03:42:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1691ef5f-42de-3101-9edc-574cae7c8e9f | -6.18351 | -36.55895 | 2025-01-04 03:42:00 | NOAA-21 | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5ef6015f-f8bc-3a7b-b524-d38474983ce5 | -5.99907 | -41.13924 | 2025-01-04 03:42:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1eb22df2-6cbb-35be-8cbd-4d66585d0dba | -4.39509 | -37.84106 | 2025-01-04 03:42:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1cfc1ed3-d3b9-3029-a99e-1b1f18e1a010 | -5.21282 | -36.0937 | 2025-01-04 03:42:00 | NOAA-21 | CAIÇARA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2401859 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 624edd70-7d1b-3503-9eeb-4261fae997b9 | -4.39444 | -37.84513 | 2025-01-04 03:42:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f628abd0-97a7-3bdb-91f9-81e96fa132ea | -4.39802 | -37.8457 | 2025-01-04 03:42:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 88cc84d2-c5b1-373a-920f-459950adcf52 | -7.98167 | -35.22741 | 2025-01-04 03:44:00 | NOAA-21 | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| bdc3dc59-7c36-3979-bc0b-5d162c8d55dd | -10.61036 | -44.34402 | 2025-01-04 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 264.5 |
| 68186191-edaf-3852-ab7d-a3e1579c6f19 | -8.30923 | -38.76196 | 2025-01-04 03:44:00 | NOAA-21 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 00721828-acf6-31e5-9763-16bf0a48f221 | -8.27451 | -41.08113 | 2025-01-04 03:44:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| f8170bce-5eb4-30e7-a5f0-d702665b502f | -10.61179 | -44.34761 | 2025-01-04 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| cbdc12b9-4700-324c-8665-8ed75ec30889 | -13.98802 | -40.00036 | 2025-01-04 03:44:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1e13f3ca-815e-3478-b4d8-a9abc7c0f510 | -10.21832 | -44.76627 | 2025-01-04 03:44:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5c015b1-71e3-359c-8ed7-ac0b3895b7a3 | -7.85253 | -37.71646 | 2025-01-04 03:44:00 | NOAA-21 | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b1fca58c-d608-3c33-9d51-4132b354dad5 | -10.60901 | -44.33538 | 2025-01-04 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c1d704b6-6993-35d1-a1e1-f319096be715 | -8.20065 | -37.67188 | 2025-01-04 03:44:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 05ea836a-b48f-3463-a2ed-47b01de2b298 | -8.60056 | -39.54164 | 2025-01-04 03:44:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a800aef9-b9ac-30d0-869d-835ce8ca652a | -6.97787 | -40.00573 | 2025-01-04 03:44:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dce262c2-76f6-36af-8871-a7d10bae4b4c | -12.46714 | -46.93382 | 2025-01-04 03:44:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aaa099a5-9b40-3227-84f1-9174ed716996 | -11.80695 | -49.32304 | 2025-01-04 03:44:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bd0a7a1-87aa-37f3-86da-831916bf8cb2 | -10.61006 | -44.32978 | 2025-01-04 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65818387-8b4e-3383-b716-e1e69abd895e | -10.5444 | -44.68297 | 2025-01-04 03:44:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 763587fa-a964-3e87-ba4f-8bfd50b33d18 | -7.82304 | -35.52504 | 2025-01-04 03:44:00 | NOAA-21 | JOÃO ALFREDO | PERNAMBUCO | Brasil | 2608107 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 59a34f34-52bc-386e-b5f4-e311efb1c949 | -11.10535 | -38.43824 | 2025-01-04 03:44:00 | NOAA-21 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 224bc9b6-ee57-39f7-b9fa-22f7d10fa253 | -9.98737 | -36.39045 | 2025-01-04 03:44:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7b5b895c-dc7e-3790-962a-a962e7fd08dd | -11.76837 | -38.68322 | 2025-01-04 03:44:00 | NOAA-21 | ÁGUA FRIA | BAHIA | Brasil | 2900405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d2f89444-9cd6-3f86-a7c6-3e7b754a53e3 | -12.2712 | -44.98493 | 2025-01-04 03:44:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e838fc3-5323-35da-96ae-608505bacbf5 | -10.61339 | -44.32713 | 2025-01-04 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c5f4697f-34bb-3995-ab84-e09a930aa8ea | -6.73536 | -38.15504 | 2025-01-04 03:44:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8331bcca-5677-3f9c-a349-a986ac41dfd8 | -11.13475 | -41.55945 | 2025-01-04 03:44:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2083e9c6-0d2f-3902-b8b1-51d46bf7c2e3 | -10.21888 | -44.76328 | 2025-01-04 03:44:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00005004-1a9a-36bd-a1e7-4930c43f48d2 | -9.48545 | -35.98932 | 2025-01-04 03:44:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 17c80bce-2d53-3372-aa74-9f9dc62ada45 | -10.54441 | -44.67983 | 2025-01-04 03:44:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6fe4d702-3c82-3c52-9fc3-80ba0ac0934f | -10.41986 | -39.86317 | 2025-01-04 03:44:00 | NOAA-21 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dce42a3f-da55-34d2-afaf-94b1ad902e61 | -6.91639 | -38.20252 | 2025-01-04 03:44:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a6a69bba-6459-3c48-b728-06ecf929010d | -6.98098 | -40.01123 | 2025-01-04 03:44:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 94877e5e-ac96-3e74-bad5-8f37f417db1d | -11.80577 | -49.3287 | 2025-01-04 03:44:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 151ffe47-2a36-3b8d-8c87-78c5215f8112 | -9.48875 | -35.98984 | 2025-01-04 03:44:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| af8d234b-c4c5-3d11-87cf-a330ba08df46 | -9.85161 | -37.12173 | 2025-01-04 03:44:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3e287825-0179-3fdf-ba52-b4cb6edc6e67 | -9.84771 | -37.12474 | 2025-01-04 03:44:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d92f3638-31ca-392a-a9f5-a177ad27d1ff | -9.98792 | -36.38696 | 2025-01-04 03:44:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a4d4f706-d0c3-3386-8ad1-60b477e451ea | -12.17005 | -44.62442 | 2025-01-04 03:44:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3688d40-b5ee-3bfd-9e8a-b64a9e49032e | -10.61285 | -44.34194 | 2025-01-04 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 6367cb68-fe91-3f6c-9afb-b82ee78606e8 | -9.9081 | -38.10779 | 2025-01-04 03:44:00 | NOAA-21 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7db3a53e-be80-3edb-bc27-013526253e86 | -13.9903 | -40.00402 | 2025-01-04 03:44:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5152fc3e-a844-3583-a358-d58004aa3d97 | -13.98947 | -39.99158 | 2025-01-04 03:44:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 02bf02b8-bbad-3eba-b511-14c7d0136b39 | -8.77337 | -36.10653 | 2025-01-04 03:44:00 | NOAA-21 | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2cdb012c-cead-39a4-a476-8160c687e375 | -10.53939 | -44.67891 | 2025-01-04 03:44:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README4.md)
