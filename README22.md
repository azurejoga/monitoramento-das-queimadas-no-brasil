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
| 8296561a-36bf-300f-95ff-010226fc6fa6 | -4.117 | -51.10706 | 2024-11-13 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fe79f3d-09f8-3b64-8502-6fb907b32a19 | -3.96072 | -52.23511 | 2024-11-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13ac0429-8273-3cba-a44a-4f9f6a2e1a7c | -3.80135 | -52.097 | 2024-11-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9907d79-a8c0-3155-aa86-83c0708d98d3 | -4.77116 | -45.57711 | 2024-11-13 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0de27d13-d93f-3a8e-ba95-1fcfea7d244a | -3.85287 | -51.91306 | 2024-11-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11f4df6d-113e-3bb0-9114-2b1ef0dabc11 | -7.54333 | -48.30798 | 2024-11-13 04:06:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 472d07af-dfd9-3fb3-8a98-fd49908a72a6 | -4.31347 | -50.82206 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a84e454c-aef7-3fb7-81fb-dbfcfa11b12d | -9.85701 | -48.36986 | 2024-11-13 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e9bb157-ba4b-39d0-812b-5946cb02b459 | -5.3568 | -43.529 | 2024-11-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac4ba14c-9572-3ca8-a38a-485d6d8e2a30 | -7.50846 | -35.10421 | 2024-11-13 04:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4f65d517-c97d-3e10-8aaf-c216656abfe7 | -7.40004 | -37.56033 | 2024-11-13 04:06:00 | NOAA-20 | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3bae630d-c50f-332b-a5de-17017fd68012 | -3.81479 | -51.26796 | 2024-11-13 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0920d917-284d-3858-a369-46d6cc2cc201 | -4.50963 | -47.5865 | 2024-11-13 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47b44a52-5b1b-3a9b-a27f-b9957178558c | -4.99748 | -44.28804 | 2024-11-13 04:06:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a053354a-97d0-3558-86f9-4c6dd1302eae | -4.66226 | -47.42798 | 2024-11-13 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 37a1f805-852f-3600-820e-376e98a4a8ca | -4.39865 | -49.96252 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d26e8b64-538b-3c37-a997-42959782c563 | -4.39252 | -47.28271 | 2024-11-13 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eedf588e-2856-3f04-a426-0eaec9f68d6d | -5.35273 | -43.53226 | 2024-11-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 4d6d6185-b0e2-31f5-a2c2-da07f076d19d | -3.7955 | -52.09959 | 2024-11-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 42c211de-27f6-3064-8aaa-e0fc08242320 | -4.66156 | -47.43228 | 2024-11-13 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f5e9c089-1cbe-3221-8541-1096257b98e2 | -5.05506 | -44.48134 | 2024-11-13 04:06:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5c86d0ee-edd4-356b-806a-7ffe2c293f05 | -5.95161 | -38.32932 | 2024-11-13 04:06:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5bbbc2e9-b864-36df-8a86-142ac53ad366 | -4.25104 | -50.25793 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dd5ee2e-0e41-3ec7-b389-6584f15bae48 | -6.95157 | -47.85759 | 2024-11-13 04:06:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fffb0a57-481f-3f57-b45b-f1edc87a1fd2 | -8.12004 | -38.62002 | 2024-11-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b951a571-d1d6-35de-bf1a-1d8a31400e9a | -5.54817 | -42.93138 | 2024-11-13 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 526aef6d-bf4d-30ac-b8c5-8e55666a27ce | -3.97736 | -50.93756 | 2024-11-13 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b337f6f8-7dca-32e6-ad61-4dde37a93269 | -5.45433 | -43.25131 | 2024-11-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05d55fca-c140-3ccd-af5b-54b3ad030209 | -3.25493 | -54.53735 | 2024-11-13 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 443dedd7-4e9c-3bf6-a925-84d7472939d6 | -3.8521 | -51.91751 | 2024-11-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f42da2f-219a-30ee-b74e-d518c3135a70 | -4.58258 | -47.06506 | 2024-11-13 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bad6cf8-00ff-3d9c-9bf7-332f93a407fe | -5.41436 | -43.32543 | 2024-11-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ce36245-d18e-3706-a6c5-4079ef10f37a | -6.92465 | -47.83196 | 2024-11-13 04:06:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b44dfe3-de27-31c1-b18b-ecdf496057c9 | -5.97668 | -45.36038 | 2024-11-13 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06a31c83-ac64-3ebd-aff5-54bc34c6d51b | -5.35876 | -46.07109 | 2024-11-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e48d8d1-6a33-3f68-bc58-def0e628fe66 | -4.11527 | -54.23095 | 2024-11-13 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b246388-9d3c-3297-9f15-6dc91d3b3114 | -4.65716 | -47.43162 | 2024-11-13 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6b2b91cd-7049-3695-9ffb-ce30e679713e | -4.10563 | -51.10521 | 2024-11-13 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a4726a0-3bec-3ae5-a084-b21d2f033eb8 | -5.37452 | -43.72874 | 2024-11-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e70e6e12-a4d8-3158-aab9-ec5aa5f20b46 | -5.94801 | -38.32878 | 2024-11-13 04:06:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c1d41366-b1df-3b3c-979a-3547d3d63788 | -3.66112 | -54.66531 | 2024-11-13 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 12d07d91-f85a-308c-bc3a-eb5ac7cf4201 | -4.75656 | -45.44676 | 2024-11-13 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4dd7ddea-878a-338b-a48d-973104564bca | -4.49914 | -48.79977 | 2024-11-13 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e34b6e8-b985-3770-b753-199b6e4f8d5a | -5.35619 | -43.5328 | 2024-11-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f1ae381-0e4f-33cf-bcfd-e76bc47a4f31 | -6.13682 | -42.80235 | 2024-11-13 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b1f424aa-7ad8-3d4e-8c92-65c9168dbdc2 | -4.61185 | -46.96759 | 2024-11-13 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc847db6-93c8-3341-bc15-50db80386500 | -4.7704 | -45.58181 | 2024-11-13 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6c872d9-0cd8-3f03-b8f3-b9630f046c5e | -5.97646 | -39.32509 | 2024-11-13 04:06:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 16d9cfcb-86a1-3c46-9f90-da07c22a118e | -4.89108 | -48.06557 | 2024-11-13 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d15434ce-063b-3658-843d-e25e9256cf30 | -6.55523 | -35.27562 | 2024-11-13 04:06:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2ec06975-e4b6-3967-8fda-d61427457f9b | -4.41754 | -48.85061 | 2024-11-13 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 681c5d5c-3777-3e19-aff4-81bbe204db39 | -4.77782 | -50.55418 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65379475-0e1a-3974-a3be-b8ae8521a680 | -6.3046 | -39.87654 | 2024-11-13 04:06:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66c9b860-f8b9-3983-9262-bb72c69a90a5 | -7.25483 | -48.72836 | 2024-11-13 04:06:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c45082af-277e-3fea-b58c-178d1361d647 | -3.14667 | -54.48885 | 2024-11-13 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f2cc4d9-f783-37ca-8d49-08ddf8d31379 | -5.94643 | -39.68031 | 2024-11-13 04:06:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9fdcb0e3-e51e-37dd-9a22-20093c55582f | -5.92057 | -42.9674 | 2024-11-13 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 174f707e-9cfc-3252-b457-c1f237615581 | -5.35703 | -46.07255 | 2024-11-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 275e0e85-6efd-3b6b-8352-eb070757366d | -15.86468 | -43.78957 | 2024-11-13 04:08:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3207dfbd-f946-351c-8d44-b4b9ad0c1456 | -17.67484 | -42.7427 | 2024-11-13 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c152ba0-6440-302b-853a-c405d3a58a42 | -10.73362 | -49.52986 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fe5a16bd-7473-32e5-ad8a-970c9f456d77 | -18.06653 | -42.62376 | 2024-11-13 04:08:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 63851f25-2493-3020-ac51-76808615a63e | -10.73321 | -49.53262 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 09faccde-bc3c-3ab2-b0c7-52d01e8e30d5 | -15.46785 | -45.90197 | 2024-11-13 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29ca0fa2-2c19-33db-8f0a-42e95fb43bcd | -18.37182 | -47.51684 | 2024-11-13 04:08:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a7115fd-8c34-39dc-acd2-5c8e1410331d | -15.86411 | -43.79314 | 2024-11-13 04:08:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b2fb132a-8127-3e94-8c8f-9a82d68bce85 | -10.37295 | -49.17701 | 2024-11-13 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f07b5ee-73c0-3745-8c78-2e7b1cbcb286 | -15.78177 | -46.43252 | 2024-11-13 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6e021c6-8c48-3cbe-b2ec-66ba5feff827 | -17.84968 | -45.99924 | 2024-11-13 04:08:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98471bc8-8fc0-39ef-ace3-91f5dc600c9b | -10.7395 | -49.52401 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 73b9fba4-bab9-38d7-94ae-a20f3a27353f | -10.73528 | -49.5204 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 79a51b24-256a-3a6e-9fb2-89ae20af34da | -18.04859 | -42.37015 | 2024-11-13 04:08:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7e720b66-d587-3dac-84fe-3db145dd952c | -15.6451 | -39.18647 | 2024-11-13 04:08:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e7d0fd23-d663-3d51-90f8-06e76f178f7c | -10.73038 | -49.52228 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d3326f68-b063-3682-bee6-2137511e4d75 | -16.13837 | -43.56033 | 2024-11-13 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c17ee01b-2fed-3580-b159-8e425fabe9dd | -15.64895 | -39.18707 | 2024-11-13 04:08:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c2b19c31-9bc3-3773-85b3-dfcfc7055257 | -10.72989 | -49.52426 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 007e883d-c6a3-3ac3-8154-1e0dc42840c5 | -10.36684 | -49.18517 | 2024-11-13 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d8842b5-1e61-314f-a5cc-344e41cad979 | -17.69453 | -44.65313 | 2024-11-13 04:08:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41c0094c-b62f-3b1a-b22b-775162e84acd | -10.73445 | -49.52511 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5b5d7b6a-f926-3dfe-be8a-43cfbbd7da00 | -10.72905 | -49.52902 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d939b066-13fe-319d-acd4-4f1da5e585b8 | -15.77121 | -46.43065 | 2024-11-13 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 377560b9-c1d3-3268-aadd-13fc48916fdd | -10.73864 | -49.52872 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 96beef3b-5667-39b2-babf-1c8ac45e80ab | -10.73408 | -49.52785 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2ac0883b-d461-3bc6-89d4-13c124fa3a88 | -15.86798 | -43.79012 | 2024-11-13 04:08:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 150c055d-fff1-3c4f-baf2-e5645e64906b | -14.61765 | -43.66298 | 2024-11-13 04:08:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c99ab1e-9e18-3e64-9ad9-26f0ea0ec113 | -15.36523 | -43.18415 | 2024-11-13 04:08:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0513c45f-a1e9-33f3-a1b2-3f58c5ccc6ae | -10.73072 | -49.51952 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 89ce5fd7-8444-32c7-aa62-71f1ec84e942 | -10.72951 | -49.52702 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 42da3da2-ae99-3b80-8995-c744a5576bdc | -15.77825 | -46.4319 | 2024-11-13 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8334ca2e-f364-3747-a674-65117b3bcffa | -10.36847 | -49.17618 | 2024-11-13 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d6c96cf4-d1a8-3a73-ac5a-8922ba24a825 | -17.09508 | -43.80377 | 2024-11-13 04:08:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8819ca1f-bbeb-38c6-bb02-e924b5a9b662 | -16.82141 | -46.72229 | 2024-11-13 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4afe4f69-1ca9-377f-a0c0-842b17777428 | -10.73495 | -49.52314 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c335653c-d391-3185-9068-6bf6a837855e | -17.59558 | -43.19913 | 2024-11-13 04:08:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f497516-4bd9-3f78-931d-51498a4f6973 | -15.78529 | -46.43315 | 2024-11-13 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4858f2a-03ae-3842-b119-48e52d84417e | -17.75007 | -42.89586 | 2024-11-13 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 281bb3bb-11cc-354f-94e2-1f1d736d7979 | -14.95461 | -42.30254 | 2024-11-13 04:08:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6982ec19-b512-3a17-86e1-7996e29be37f | -15.77473 | -46.43127 | 2024-11-13 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f92460cc-2e8b-36e0-af13-f4cf621d7cd0 | -15.76285 | -46.17743 | 2024-11-13 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README23.md)
