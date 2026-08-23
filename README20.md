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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 404a2630-7db1-3166-8078-437babb91f82 | -19.81445 | -45.64204 | 2026-08-23 04:12:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39a700ec-1864-3a09-ae34-abed38d0b3f2 | -19.6481 | -45.72709 | 2026-08-23 04:12:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e9cab47-df22-335d-b3dd-4189f1813ef3 | -21.44884 | -46.14122 | 2026-08-23 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 092c043e-2bb3-3796-894f-106815f1620e | -20.65742 | -46.58866 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e566913-0d66-3e8b-8e25-1049fef58901 | -20.6566 | -46.57259 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ece28e63-d607-35a3-af1f-6e8b0a927331 | -20.25637 | -44.05305 | 2026-08-23 04:12:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 97f3191f-1395-3287-98e6-96a46c61f8a8 | -18.611 | -43.64169 | 2026-08-23 04:12:00 | NOAA-21 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 39f6ccab-34db-312c-840b-9108c9d3b9c9 | -18.53602 | -47.16296 | 2026-08-23 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc15f938-453a-3768-9423-d1a509401472 | -18.77692 | -43.77847 | 2026-08-23 04:12:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c8db55ef-7956-3674-94cd-2373025a0578 | -18.63943 | -43.9235 | 2026-08-23 04:12:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75b32c9e-a15d-3a2c-9e48-6198840a27c4 | -19.80779 | -45.64085 | 2026-08-23 04:12:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfdb0174-a003-35ff-8552-c3066c8e6067 | -23.52114 | -47.31952 | 2026-08-23 04:12:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dafb0169-d455-3b75-ba52-0ba462c7a5f7 | -23.19075 | -49.15799 | 2026-08-23 04:12:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dd9cf83-8f4a-370e-960e-6bf2aa17fcec | -20.65385 | -46.5682 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c4b72f1-b9b2-3aa6-9a6c-48651a8a1691 | -19.6487 | -45.72338 | 2026-08-23 04:12:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0dc257f-7d1a-3964-8c84-452948c67cf5 | -20.66188 | -46.56176 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 311d1908-a46b-3dbc-8997-c2ff3bf9f1d2 | -18.52971 | -47.15752 | 2026-08-23 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88154630-bfe3-3d05-82cf-e2d1633f7ad3 | -20.96379 | -48.92704 | 2026-08-23 04:12:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 43a371f7-e40f-31c5-b227-a020110eb745 | -18.5262 | -47.15687 | 2026-08-23 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 35cccc59-bff1-3940-93f2-058995f8d89b | -25.46542 | -49.65038 | 2026-08-23 04:14:00 | NOAA-21 | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 43c6d61e-8b55-3761-a2d0-bd487d3f6d85 | -23.73984 | -54.58584 | 2026-08-23 04:14:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 10b9aebe-f3f4-332a-9e22-7630e941abd0 | -25.2244 | -49.47771 | 2026-08-23 04:14:00 | NOAA-21 | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 13348e64-32f9-35b1-86f9-104fa7548edc | -28.06222 | -48.67281 | 2026-08-23 04:14:00 | NOAA-21 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7d18f7c2-e665-3e83-a293-b2607f58bd6e | -25.51393 | -50.04668 | 2026-08-23 04:14:00 | NOAA-21 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 06bceff9-ff88-3f65-a1b0-22c8ac49b102 | -25.17982 | -49.3744 | 2026-08-23 04:14:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8c665ff9-2ebe-302d-be21-175158360fd2 | -27.45523 | -48.45234 | 2026-08-23 04:14:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b3375aac-89da-31f0-9e66-b97cc3afaf52 | -6.782 | -59.6519 | 2026-08-23 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| b38904f0-46f1-3158-bdec-dc78fecd1eec | -6.8062 | -58.6469 | 2026-08-23 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| c5433528-4a7b-3ba1-ac34-0a1d96009bf6 | -6.8188 | -59.6696 | 2026-08-23 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3fff79a3-111d-3cc0-8b3a-1ef5145862d8 | -6.6766 | -58.7299 | 2026-08-23 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 142.6 |
| aa25625c-6a36-30e8-b2dc-bbf5ee638465 | -6.6949 | -58.7485 | 2026-08-23 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e8dc14e4-5bc3-3da4-8c4d-4a96388ca5c4 | -13.1697 | -51.4258 | 2026-08-23 04:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 02a1c5e2-63e4-38d5-b8ec-c79de7ddb947 | -6.9514 | -59.0666 | 2026-08-23 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 65051c9e-0ba3-33ad-ab61-505363fcecd8 | -6.9699 | -59.0658 | 2026-08-23 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 6856c386-87ba-34e9-8be1-f3e5ddf5eeff | -5.7799 | -57.58 | 2026-08-23 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 18f6bc31-8d3b-3d60-b3c7-50198729a1e5 | -6.6765 | -58.7492 | 2026-08-23 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 0e5740da-0cf4-319e-b36f-38a117fc857f | -6.695 | -58.7291 | 2026-08-23 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 8a7e6d2b-ee67-339f-956b-7afcdc2fa7bf | -13.1505 | -51.4281 | 2026-08-23 04:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 03f75a36-2c6c-33db-ab07-3074ca314cb4 | -6.6581 | -58.7306 | 2026-08-23 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 4e75ad2d-f9ce-3cdf-830f-69f9be912ffc | -6.9514 | -59.0666 | 2026-08-23 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| a2582bb7-8a4f-32df-9f29-04f25e54ef40 | -6.9699 | -59.0658 | 2026-08-23 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| ca18f695-b005-3921-a789-08730fc5ae91 | -6.8188 | -59.6696 | 2026-08-23 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e535b32b-3c1e-3431-826b-6fc65043208b | -6.6766 | -58.7299 | 2026-08-23 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 36c94635-eeb3-33b2-b999-fde48b7f0616 | -6.695 | -58.7291 | 2026-08-23 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 017c40ff-2cee-3921-823c-147542814d34 | -6.1286 | -57.8198 | 2026-08-23 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e0b700a9-f696-3c91-a45e-b5eace714718 | -10.8364 | -50.9479 | 2026-08-23 04:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| a0fe1e79-ae1a-3742-8525-4b07cf085cf8 | -13.1697 | -51.4258 | 2026-08-23 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 650fd8c2-b9ae-369b-a941-ea11125057d4 | -6.1285 | -57.8393 | 2026-08-23 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 44c38e27-e6de-3e70-8332-90b61d034214 | -6.8062 | -58.6469 | 2026-08-23 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 62014bd1-c660-3ac5-af5f-b19c238cb290 | -6.8357 | -59.9571 | 2026-08-23 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 3b80f5d5-13ca-381d-bccb-95fdde38d197 | -6.8172 | -59.9578 | 2026-08-23 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d6dfd747-c429-3d2f-b0ae-0f710c615a14 | -6.6765 | -58.7492 | 2026-08-23 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| e71744c9-e311-330c-b922-5c862ea38199 | -10.8361 | -50.9691 | 2026-08-23 04:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 577fc477-73d5-3789-b0a9-df756ad3d570 | -6.9514 | -59.0666 | 2026-08-23 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ed75d229-1ba6-31c8-b24e-2c9fb913364f | -6.6766 | -58.7299 | 2026-08-23 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 300bc522-d168-3db1-846d-c69a4b960e83 | -6.8188 | -59.6696 | 2026-08-23 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| f2ee7db0-1c6a-39d5-b4ab-9ce8bc1997af | -13.1697 | -51.4258 | 2026-08-23 04:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| f4dfd9b0-f828-37b6-951f-5945f12eef5d | -13.1505 | -51.4281 | 2026-08-23 04:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 5548c6ca-5f26-3eec-b55e-464e67b17845 | -9.4582 | -40.3143 | 2026-08-23 04:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.0 |
| becdc0ab-ab53-32eb-ac5e-fbd90ef15e77 | -6.695 | -58.7291 | 2026-08-23 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| d471801d-48c2-33f0-80aa-41e39cd686e9 | -10.7982 | -50.973 | 2026-08-23 04:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 65f47211-5ee1-3b72-8352-22d1104e6b59 | -13.1889 | -51.4234 | 2026-08-23 04:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| b95599e8-b025-36e1-b300-6274e81d90ea | -10.7985 | -50.9518 | 2026-08-23 04:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 07b9cae5-ca4b-33be-a702-4eb8f9eb4388 | -6.1285 | -57.8393 | 2026-08-23 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 03770bc6-a22e-3474-9c40-0d2f264bf14b | -6.1101 | -57.84 | 2026-08-23 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 61832be0-e79b-32fe-90b7-215612e45613 | -6.8062 | -58.6469 | 2026-08-23 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| f92819f2-295f-36a7-a6f8-fd1a0a55cf58 | -6.9699 | -59.0658 | 2026-08-23 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 113ef195-1a95-3b3c-b771-a61b0cdc65be | -6.6765 | -58.7492 | 2026-08-23 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 15f808b9-d83f-3375-96bb-7f92ddef6a2b | -1.57779 | -47.74013 | 2026-08-23 04:42:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 696dcaf9-414d-3956-9de6-52ca482abe03 | 2.7868 | -50.93245 | 2026-08-23 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cb1d30b-2ad6-3c9f-b928-24c694805cee | 2.78945 | -50.95015 | 2026-08-23 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f08219c-cc5f-3c9b-a12d-bc3e79e6e2fc | 2.79339 | -50.94926 | 2026-08-23 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5079180-d419-34be-b8cd-2e38c1b4917e | 2.79228 | -50.94221 | 2026-08-23 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0a679ce-263b-3794-a67b-a664303c4c13 | 2.78733 | -50.93599 | 2026-08-23 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92bdf0b4-73a3-3060-b78d-e39c010049bd | 2.7965 | -50.94183 | 2026-08-23 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7af1e4c3-0f31-3357-bf7b-ac7ee2eab3e6 | 2.78839 | -50.94309 | 2026-08-23 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 894053fb-484d-3310-91eb-58e328df2195 | 2.78822 | -50.94284 | 2026-08-23 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20063a32-61ef-33a9-af99-594d2fdcd534 | -1.33355 | -47.95775 | 2026-08-23 04:42:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6ce0ce8-69cc-369e-ba37-2a16addff48d | -1.33019 | -47.95722 | 2026-08-23 04:42:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 455ef722-726e-37cc-98b6-37984737d13e | 2.78711 | -50.93575 | 2026-08-23 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d87c5678-2b11-38a6-942f-2b92a3cbba54 | 2.78655 | -50.93222 | 2026-08-23 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b48470f0-d8bc-39eb-921b-d4e69169cb27 | 2.79245 | -50.94246 | 2026-08-23 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbf7c20b-dd97-3153-823d-62eb00d7324f | 2.78933 | -50.94988 | 2026-08-23 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2824b957-da58-312e-81e2-5db5ccbb62f1 | 2.79351 | -50.94953 | 2026-08-23 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 512abe54-d49b-328a-bbbf-66f7daa2e959 | -6.66486 | -58.74946 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c8b7ba12-0035-327f-829d-69f39b004372 | -6.54576 | -56.26163 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f382d903-af0b-3bea-ba48-59378f794f20 | -6.80008 | -42.6726 | 2026-08-23 04:44:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 737132d2-20ff-36ab-af22-77a1385fa274 | -6.79914 | -59.80194 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d7242af-2398-3761-9613-cbfe2a0a9df4 | -4.17448 | -42.44532 | 2026-08-23 04:44:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b860451b-5515-322e-880d-3f93fddb94fb | -1.96389 | -48.37308 | 2026-08-23 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce08e538-4706-3fd5-9642-f403c36f4fd9 | -8.10079 | -50.05948 | 2026-08-23 04:44:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8b01647-338d-3042-936d-00e271257c6e | -6.81222 | -59.67725 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0ae7b57-3798-3b2b-8759-c251df54eb16 | -6.96538 | -59.06005 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9783d1a-59e5-3361-ae62-bc401108f40d | -2.9913 | -48.96004 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5c097626-4787-3306-bccf-04f1994ef711 | -1.61056 | -54.40134 | 2026-08-23 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fa98621e-8345-345e-b373-15548ba6e120 | -8.09005 | -51.66342 | 2026-08-23 04:44:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea69f8ad-8a6e-3c21-9fcb-04ed996df8a8 | -7.39727 | -45.98637 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4422a587-a937-3b55-bfc2-a4dd4772bd5f | -6.18484 | -53.52089 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61d50985-bce2-34ad-a00b-01585587c8fd | -7.1079 | -59.7774 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bde5acea-2be0-3706-ae19-f7fb55089689 | -6.75323 | -58.66507 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README21.md)
