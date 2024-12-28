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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a784022-6bd3-319e-9794-57ce885a2b4e | -4.50318 | -44.2348 | 2024-12-28 04:14:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8241e030-4f07-3a82-a6a2-f3374d9f0358 | -3.99771 | -46.73682 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdb065db-8550-3b0d-8ace-12eb99000079 | -4.07702 | -47.08955 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| c4dbf3e9-4445-32e7-87c1-721b747875c2 | -3.90821 | -46.9832 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f3636674-f291-3e75-88ee-a204f44e9ec2 | -6.28794 | -43.77151 | 2024-12-28 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d42a0e8c-7559-3673-8f8e-09a8645e7db6 | -4.49617 | -47.08834 | 2024-12-28 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9f3f249-072c-36f0-b2b0-040891796444 | -2.3318 | -45.80727 | 2024-12-28 04:14:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 11aefce4-8e65-3880-b4b2-ddf8c719980c | -3.91102 | -46.9158 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fee06e5-464f-3a8f-a153-cf62f5d4f45e | -5.98679 | -44.60065 | 2024-12-28 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 970cdce2-6194-3b05-968d-5a54d9a541a2 | -3.90719 | -46.91524 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9da8343b-09f2-34b9-9fd0-5ae50bdcaa1b | -6.11991 | -43.95175 | 2024-12-28 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f855b8d-67b5-331d-a899-89877c30e1c2 | -4.03545 | -47.05352 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8386ebc-160c-3ed6-90f7-6a5235f4ea58 | -5.90717 | -43.48795 | 2024-12-28 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7942f23-685f-3c38-9f6e-780dc58a527e | -3.41783 | -50.01965 | 2024-12-28 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42059d5b-bd57-3a52-8e71-ae408f798e80 | -4.04008 | -47.04929 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d76774d0-57fc-3851-89c7-ec15bd518260 | -5.21469 | -41.24274 | 2024-12-28 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0b0e6633-dd05-3e51-83b9-85263c4274f2 | -6.50026 | -41.78601 | 2024-12-28 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8187b71f-1e9d-33fc-a553-03917c761313 | -3.88747 | -47.01466 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d95ecf5-0db4-3457-aff7-62f7b269aed3 | -3.56283 | -53.10152 | 2024-12-28 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f74c050-e58e-310f-8db6-3d20cea2d111 | -3.96143 | -46.7691 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0122a6ea-fc13-3b04-856c-b2d7ee4c188e | -5.31454 | -46.06097 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5632b2f6-5610-34c3-bd83-9d437bc40f5c | -3.90877 | -46.93 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1efc341c-27ee-3ecd-b709-f2baf77c7414 | -4.85448 | -39.75544 | 2024-12-28 04:14:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9e9eab74-14ca-384f-9a46-f7a02a755f19 | -1.71471 | -46.22874 | 2024-12-28 04:14:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d56b6ca8-1fb0-3ecb-a724-122558ab9dd1 | -4.50374 | -44.23124 | 2024-12-28 04:14:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3e1f5568-1851-3bed-b914-3eca30ecad9f | -3.90868 | -46.90582 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd59e4dc-b0ee-346e-9ad6-e0c7b6536138 | -3.90561 | -46.90052 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 359e7f75-2c92-3c11-abcb-091b7f97cec9 | -4.00446 | -46.71898 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e860f31-4cfe-3c76-b4e0-332f567b09c9 | -6.44024 | -40.62337 | 2024-12-28 04:14:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0eaa247a-6185-36e3-8e33-c393f80bdbe5 | -4.05393 | -47.03689 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6a35027-372c-369a-8529-9418158083a0 | -4.02843 | -46.54641 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4084b671-9118-3a6e-a509-ef33dd427570 | -4.55697 | -44.06826 | 2024-12-28 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92b63455-b174-3387-92a6-dcdd975048e5 | -5.45059 | -38.16972 | 2024-12-28 04:14:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6e9598bb-6862-3d6a-981d-1fabfd9bcf1c | -3.96137 | -46.67492 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da5a459b-954f-301f-8e19-f54a8f17fbf9 | -3.97564 | -46.33978 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec0f7af2-122d-3223-8d17-f6f6bd2a1767 | -5.22261 | -41.23648 | 2024-12-28 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 11bf7aa3-8986-34e5-839e-70e1d7677107 | -5.81019 | -38.10206 | 2024-12-28 04:14:00 | NOAA-21 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d77f4b62-e5e4-3067-b179-4d0eebf4d59e | -5.21526 | -41.23907 | 2024-12-28 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4ed6a1b1-dcd3-3ab7-8a39-88807f7d91aa | -4.02025 | -46.54965 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 164d776b-9c9d-33bc-9e94-19bb0bcbfb2a | -3.96431 | -46.67667 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9bce5aa1-f228-3e0b-bb57-a0bbf87a0fe2 | -5.64288 | -43.71906 | 2024-12-28 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b034773-be78-3432-8c3f-b4dc8294c951 | -3.91929 | -46.97858 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0598c35f-546c-3c89-82af-bad6f0a9e60b | -6.21687 | -46.22192 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9db50ed0-bdd7-3c3f-8c27-0d7cb6acbcae | -3.97754 | -46.88588 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18604845-8d18-3f1f-806e-35cf7812a4c0 | -5.97837 | -41.68792 | 2024-12-28 04:14:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 69be44b7-702d-30a5-aabc-cb5a4ff1b78b | -3.99778 | -46.34346 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da4a0f78-db76-3cef-9efc-a70336d8d689 | -3.8 | -46.85722 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06171e4b-81f9-337d-9781-d0d5ca452a01 | -5.48856 | -41.62843 | 2024-12-28 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c51fd9b1-b046-3051-97bf-3514761445ac | -3.9859 | -46.90681 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0be8e582-4e34-32cc-9187-c20148797c97 | -4.03624 | -47.04868 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83102c7e-948d-38ef-a7c4-2f486aad6f13 | -4.56054 | -45.9903 | 2024-12-28 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dbc0ae6e-e429-331a-a4ac-d88d1f12aae8 | -5.64343 | -43.71558 | 2024-12-28 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8284f39e-c9b4-3c37-ba21-905d36000c0d | -6.01091 | -39.27274 | 2024-12-28 04:14:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ba35457e-111e-3555-8878-3688e4fa9755 | -6.37125 | -43.56469 | 2024-12-28 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78e21e76-8806-30f7-8168-71b97105d6ef | -3.82098 | -46.62807 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d568ee89-cf0b-3ddf-8ea8-d951072d03dd | -5.45009 | -38.17313 | 2024-12-28 04:14:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 348f5529-1b5f-308a-9872-1177c4342aaa | -6.58821 | -39.26836 | 2024-12-28 04:14:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| ff4816f9-1006-3683-9836-b1fb8079395c | -4.56414 | -45.99085 | 2024-12-28 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6c1c7ff-33bd-3e5f-9348-5d4c79a8e1fe | -3.99076 | -46.68414 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cbef7f0b-01aa-3564-8f84-bb9ec49ed897 | -4.00437 | -46.69553 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9cabf676-b951-3eba-bf67-2b9b8400d58f | -4.04087 | -47.04448 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c85258aa-d940-35ca-8794-c3e319ea9463 | -3.817 | -46.72583 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf4f361a-47b0-3da0-85dc-24e46694a236 | -10.67148 | -45.01336 | 2024-12-28 04:16:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e92f1d16-8e1d-3d75-9191-9690a4630f63 | -13.17452 | -39.78438 | 2024-12-28 04:16:00 | NOAA-21 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 41149a49-3259-30f1-8b77-bcaf891184d8 | -10.2054 | -42.22762 | 2024-12-28 04:16:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 97e2bce8-7a9b-3151-b67c-6bea9f0a9602 | -8.98736 | -40.62201 | 2024-12-28 04:16:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 479c0803-a4a1-3001-b7d2-fde19bb4c2d3 | -8.6978 | -44.32754 | 2024-12-28 04:16:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a56abc3-38bc-3d64-81ba-1089490e64f9 | -13.73382 | -39.45145 | 2024-12-28 04:16:00 | NOAA-21 | GANDU | BAHIA | Brasil | 2911204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73d162bc-5f92-3804-ba31-fb5954300787 | -10.68865 | -45.01248 | 2024-12-28 04:16:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cd8a6b2-0a05-33d2-9b10-f9521bb7be20 | -10.42955 | -44.88714 | 2024-12-28 04:16:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fa61131-6b11-3bfc-a48b-d60b8878e087 | -13.17094 | -39.78058 | 2024-12-28 04:16:00 | NOAA-21 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b57d08d3-41f0-326c-843d-40cb4228ae2d | -10.68809 | -45.01601 | 2024-12-28 04:16:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecfd54f4-b4cd-34f2-8817-c3860544ab59 | -10.91391 | -46.74282 | 2024-12-28 04:16:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d197b43b-92fc-3826-b718-acaacda1afe1 | -9.39104 | -40.67614 | 2024-12-28 04:16:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cadedaf1-ce2e-39c1-9bbd-b0d92b01c53c | -10.43231 | -44.8912 | 2024-12-28 04:16:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6fcff29-5856-31f5-96fd-49f40db4dcde | -8.62862 | -46.02728 | 2024-12-28 04:16:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbfc1e76-8bdc-3cc4-a2fc-f21a5a1f99d0 | -13.17543 | -39.77753 | 2024-12-28 04:16:00 | NOAA-21 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| acbafd6a-4ba5-302b-bd6e-5fb226ee8a5a | -10.63796 | -40.21219 | 2024-12-28 04:16:00 | NOAA-21 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| abf11aea-0291-3590-a974-842074a69c92 | -8.12126 | -43.14032 | 2024-12-28 04:16:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2a59ba07-c108-3cd3-b120-f77437097427 | -15.54075 | -43.14121 | 2024-12-28 04:16:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 662e7df7-4743-33fc-b342-35f318355d0b | -12.18747 | -46.69761 | 2024-12-28 04:16:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 157be01d-273e-3411-9137-7e45ce64532f | -9.11379 | -40.96457 | 2024-12-28 04:16:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f9d278ce-a24c-3cb8-93a2-c776e7779ff2 | -9.26361 | -40.95632 | 2024-12-28 04:16:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e5341f86-91ed-355c-8c7c-14837c41aa76 | -11.13759 | -43.30618 | 2024-12-28 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4b72389f-ceb4-364c-b8a4-4cef416f8d63 | -10.60413 | -44.98795 | 2024-12-28 04:16:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 536236d2-e06b-38e6-b4bf-af26fbd38317 | -10.63731 | -40.21682 | 2024-12-28 04:16:00 | NOAA-21 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 95011dbc-1b10-3b33-8a2f-9addc1e8bdf1 | -8.69449 | -44.32701 | 2024-12-28 04:16:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e19472c1-feed-3bb8-b6fe-7b5a86480de8 | -10.87835 | -41.24002 | 2024-12-28 04:16:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fcaf7e97-e74f-3ec8-948d-8801cae4ee23 | -11.39664 | -43.14394 | 2024-12-28 04:16:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 24aab1ab-5d28-33d8-af30-1243dd5980ad | -9.55518 | -40.91245 | 2024-12-28 04:16:00 | NOAA-21 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 20e7a935-b91f-327c-b1ba-873c254d5f06 | -10.60468 | -44.98442 | 2024-12-28 04:16:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cefa990c-6c07-30a9-a183-910bb638fb1a | -10.03755 | -44.78391 | 2024-12-28 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80968d61-b40e-392a-b77c-c0ad7965a330 | -10.91216 | -46.74264 | 2024-12-28 04:16:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c85267b2-33cc-3944-8e8a-dc0a498abb23 | -11.13479 | -43.30209 | 2024-12-28 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 741dab44-2a26-3888-afe0-a921efab01b1 | -10.21788 | -44.76243 | 2024-12-28 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 803053af-2bc2-3730-bc2b-cff59e837a8a | -11.24862 | -44.48076 | 2024-12-28 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 761513ca-2ae9-36d9-ac9d-b1c368f5fabb | -12.18279 | -46.70464 | 2024-12-28 04:16:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcf93641-d38a-33e5-8386-c9a17a2d3a72 | -11.13813 | -43.30261 | 2024-12-28 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 64240fc8-a420-3060-b166-3b856db192ef | -8.62517 | -46.02671 | 2024-12-28 04:16:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 494e192c-d957-3073-97f6-939e4f6ecb3b | -11.39999 | -43.14446 | 2024-12-28 04:16:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
