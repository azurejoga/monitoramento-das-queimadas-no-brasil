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
| 0b250639-e8ee-33a0-a862-229342320681 | -14.4144 | -43.9433 | 2025-10-09 00:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 90c66f35-3f5d-3f26-8e49-05224bf1bf14 | -4.9894 | -45.3159 | 2025-10-09 00:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 267a9d3e-8fa0-3a19-b996-9c77f6043840 | -14.4523 | -52.8961 | 2025-10-09 00:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 3c4ee4a4-eba1-33da-a5aa-68e0cb60b4da | -4.4446 | -43.2164 | 2025-10-09 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 739ed4bc-8024-32cf-ac6a-d08e071eda7d | -8.6103 | -45.1249 | 2025-10-09 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 769c78a1-89da-36af-a85e-fd5e3823fbe1 | -13.7913 | -45.8321 | 2025-10-09 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| d8cf498b-3424-3a3d-be59-76dea2d280a9 | -7.7758 | -44.0164 | 2025-10-09 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 59e81ca0-64e4-306a-bf96-f4ddfeee34f3 | -13.8108 | -45.8288 | 2025-10-09 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 4c817269-3005-3a7d-a09b-10643bd6359c | -13.7909 | -45.8552 | 2025-10-09 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 339.1 |
| b0dd25d7-6c17-3951-9159-90f8d99ef020 | -21.3856 | -49.1385 | 2025-10-09 00:40:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.8 |
| 95c26db2-a694-3a18-b1b9-36bed24f0318 | -14.4329 | -43.9874 | 2025-10-09 00:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 416ee4c0-8de8-3de0-a7da-e92653d07a6a | -14.4133 | -43.9911 | 2025-10-09 00:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 259.3 |
| a9859527-0c8c-312f-b22f-809c5f951b90 | -5.46 | -44.8322 | 2025-10-09 00:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 15a1c0c9-a766-3bdf-9b82-f19c39ce017a | -7.7755 | -44.0396 | 2025-10-09 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 0941d7b8-4136-3165-8629-e24c486bd5ee | -5.4415 | -44.8107 | 2025-10-09 00:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| b4230186-d5c9-38d4-9bf0-7140929f880d | -9.1018 | -47.9575 | 2025-10-09 00:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 78087cd8-5d96-354e-8a67-e8f91ecfd3f1 | -4.4445 | -43.2397 | 2025-10-09 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 96fc45ef-cae4-323d-b9cb-46b051d180d1 | -4.9708 | -45.317 | 2025-10-09 00:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| cb57ba71-5e63-32cc-99a8-94f1d0e7da7a | -10.7262 | -49.3317 | 2025-10-09 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d0c417f0-53b0-3433-9ac1-d32a7a181938 | -13.7904 | -45.8782 | 2025-10-09 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 6bc7d90c-3c09-3dcc-892c-0c357a288076 | -14.4334 | -43.9635 | 2025-10-09 00:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 356.9 |
| 1290a987-28a4-3a0b-b363-411d807bb850 | -16.3955 | -46.3741 | 2025-10-09 00:40:00 | GOES-19 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 0a213bf9-2729-3a4a-9270-4d06958cfdd6 | -4.4633 | -43.2152 | 2025-10-09 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 09491842-4967-39e5-be06-1d7d1c701fb8 | -6.6993 | -46.3169 | 2025-10-09 00:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 9037f7f1-e0ba-3614-b830-819729cafe7e | -14.452 | -52.9172 | 2025-10-09 00:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 76f48de7-4422-39b0-9014-eca403d2f9b2 | -21.3862 | -49.1154 | 2025-10-09 00:40:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.3 |
| 09347bc5-ecfa-3ad4-a113-377d42d2e9f7 | -21.4069 | -49.1106 | 2025-10-09 00:40:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| 76dcb735-c4a3-3005-9c31-c39187b98a65 | -8.1993 | -43.3424 | 2025-10-09 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.9 |
| 4dcc68e9-c99a-390e-911a-ce61744d106a | -6.6808 | -46.2961 | 2025-10-09 00:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 222.3 |
| 9bb8da93-f86b-3b1e-b50d-a13ebaf9e6ca | -16.3757 | -46.3779 | 2025-10-09 00:40:00 | GOES-19 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 216c9ee4-4587-3ed6-91b8-4861e4920bde | -14.4717 | -52.8937 | 2025-10-09 00:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 626ace8c-6022-31bb-85a4-3c43fb400207 | -9.0829 | -47.9594 | 2025-10-09 00:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 0e4c5852-6441-3290-81c3-2f0c1d381206 | -14.4138 | -43.9672 | 2025-10-09 00:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 489.9 |
| 760a3f23-b300-3a75-8d09-0f68ccbe5f44 | -6.6806 | -46.3184 | 2025-10-09 00:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 03334c22-b60c-380f-9cbd-21f639de963f | -18.0453 | -51.1556 | 2025-10-09 00:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 03ca7897-1408-395b-863e-a9fcfe940963 | -18.9974 | -43.0805 | 2025-10-09 00:40:00 | GOES-19 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.3 |
| b1a54b6a-462a-374a-8eac-e72d76a9e3e4 | -4.4446 | -43.2164 | 2025-10-09 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 74d6aa17-3cf0-3e22-bef7-9f600d15097e | -4.9894 | -45.3159 | 2025-10-09 00:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| b6113064-d738-304f-89ab-074ac006cf73 | -6.6995 | -46.2946 | 2025-10-09 00:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 272.6 |
| be2d66cf-13e6-3836-b087-d402e2742ff6 | -9.0832 | -47.9374 | 2025-10-09 00:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c41c91db-338c-36ae-bf42-275fdf4b2f5e | -7.7567 | -44.0415 | 2025-10-09 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 177.5 |
| b68249a4-97bb-32fe-b4f1-2c601552d6f9 | -7.7569 | -44.0183 | 2025-10-09 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 840409a2-8109-32cb-b489-a136f8d97733 | -13.8103 | -45.8519 | 2025-10-09 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| d3997c19-be73-38ca-8580-809cf7030e75 | -21.4062 | -49.1338 | 2025-10-09 00:40:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| d9a26f71-4d26-37da-91b8-47efc7dcd107 | -14.4523 | -52.8961 | 2025-10-09 00:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 48f95f4c-25b1-3350-8ff8-acb4731ddf08 | -17.8413 | -57.6459 | 2025-10-09 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 16f95605-754c-3173-a22d-a3df98a4e083 | -9.1021 | -47.9355 | 2025-10-09 00:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| e4d1ab66-b7e8-3e55-8818-b79924179bc4 | -8.1996 | -43.3189 | 2025-10-09 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 1a0a0f93-9bfa-3927-acb7-3312841b42a6 | -5.4413 | -44.8335 | 2025-10-09 00:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 99acd75a-a4a8-3f48-9181-44bbd934b850 | -3.1164 | -47.7931 | 2025-10-09 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 0b7306a8-bc76-36b1-b39a-2bb0c2451e32 | -19.7553 | -42.1994 | 2025-10-09 00:50:00 | GOES-19 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.4 |
| 40184db7-98f5-38d7-afed-4d8dce9a5028 | -6.6995 | -46.2946 | 2025-10-09 00:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 309.3 |
| cb384efa-b146-3dde-ae7d-2f1ce6ad5f6a | -14.4138 | -43.9672 | 2025-10-09 00:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 413.3 |
| e7ba15e6-7527-3979-88aa-eb6b6daa7824 | -17.8413 | -57.6459 | 2025-10-09 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 0ec43a66-2171-33af-8637-d91b5c38efcd | -9.1018 | -47.9575 | 2025-10-09 00:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 68337666-e913-35be-b9ad-6601987ba90c | -4.4446 | -43.2164 | 2025-10-09 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| f6d34abc-7e39-33a5-8a18-59b8e155f954 | -16.3757 | -46.3779 | 2025-10-09 00:50:00 | GOES-19 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 90.6 |
| f16d6ecb-b38b-3b93-97c4-c91c150129df | -6.6808 | -46.2961 | 2025-10-09 00:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 428a54b1-b9ae-3bf4-88eb-6506cb7e599a | -14.4717 | -52.8937 | 2025-10-09 00:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| c7292ff9-800a-35d3-8539-8e0bf22cb540 | -6.6993 | -46.3169 | 2025-10-09 00:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 3b338f3c-e36f-39a0-944b-00daaa4b7497 | -16.3955 | -46.3741 | 2025-10-09 00:50:00 | GOES-19 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 85.0 |
| a27845e5-2d66-31a2-8e2f-28629294b0fc | -13.7909 | -45.8552 | 2025-10-09 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 163.5 |
| fb182948-a789-3c51-ba44-2631e400a4e5 | -5.4413 | -44.8335 | 2025-10-09 00:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 7d649645-9aea-3e81-b38c-567654a743bf | -8.1993 | -43.3424 | 2025-10-09 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.4 |
| 6e95c043-3d2d-3cc0-bad9-42c042b495ab | -13.8108 | -45.8288 | 2025-10-09 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 1d9d84eb-3862-3bf0-9295-b0080b1ddc72 | -7.7758 | -44.0164 | 2025-10-09 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 5ad63114-eb5a-3fe0-a495-efc2ae6c1a99 | -13.7714 | -45.8584 | 2025-10-09 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 50c52d02-edf7-31d8-bc21-060648317430 | -18.4118 | -45.2394 | 2025-10-09 00:50:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 7f980145-f1e5-35b9-9ce4-c867946a274d | -18.0453 | -51.1556 | 2025-10-09 00:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 1095e439-f439-3679-bc2e-667730426795 | -9.0832 | -47.9374 | 2025-10-09 00:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| b47b2633-aae5-3a2e-b5de-d5d11b4499c3 | -14.4133 | -43.9911 | 2025-10-09 00:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 280.1 |
| ad15e8d9-e9f7-30c6-94e1-889114017a5e | -17.6421 | -47.1871 | 2025-10-09 00:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 61.6 |
| a504e1f3-cfdc-3787-ab09-c3de47a5bd8e | -10.8505 | -49.9217 | 2025-10-09 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 447940b5-c882-391c-a664-ee2b706cfee6 | -13.7913 | -45.8321 | 2025-10-09 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 7c6097fc-5194-3156-b725-52678e1ef0da | -14.4334 | -43.9635 | 2025-10-09 00:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 247.8 |
| 83ca57d0-078c-3ab9-8cfa-58dc0ebd2022 | -4.9894 | -45.3159 | 2025-10-09 00:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 47ff9199-ac57-3eed-b881-70f853e7a415 | -18.9974 | -43.0805 | 2025-10-09 00:50:00 | GOES-19 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.7 |
| a12cbd60-558b-3cd1-b0a6-82abc139df18 | -19.7347 | -42.2052 | 2025-10-09 00:50:00 | GOES-19 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 151.9 |
| 3bd4c829-7142-3dd1-9882-66ac895348e6 | -14.4329 | -43.9874 | 2025-10-09 00:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 41f1c047-7474-3263-aef4-bffe30f4c987 | -17.6221 | -47.1912 | 2025-10-09 00:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 1ce48eaf-be56-3c88-adad-2fab812c4a2b | -10.7262 | -49.3317 | 2025-10-09 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 3952b973-0ed3-3c13-9d21-f523bbf82fce | -7.7567 | -44.0415 | 2025-10-09 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 5b583731-2f4f-3586-8e4a-c53569ea4aa2 | -18.0648 | -51.1742 | 2025-10-09 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| f5c55aed-0727-38bb-8ced-bb91581bd507 | -14.4523 | -52.8961 | 2025-10-09 00:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1eda1c96-f81b-38c4-99c8-7520a34bcac2 | -7.7569 | -44.0183 | 2025-10-09 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 142.6 |
| dcf7d16a-9b23-377d-b580-35eb69d48dcd | -9.0829 | -47.9594 | 2025-10-09 00:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| c6e96f30-ea8b-39ff-b62f-101fff5a56d5 | -4.4445 | -43.2397 | 2025-10-09 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| bf644830-80ee-3750-81aa-2fbcbc80b9b6 | -5.4415 | -44.8107 | 2025-10-09 00:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0538ae2a-eaa9-3f63-aeb9-5e772b30dc19 | -6.6806 | -46.3184 | 2025-10-09 00:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 9355ca65-fe18-36f6-bed0-2eed8cd4c7f1 | -4.4633 | -43.2152 | 2025-10-09 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 3ee58fbf-7462-33db-85c2-c338bd8185a0 | -4.9708 | -45.317 | 2025-10-09 00:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 44dea374-5343-3ffa-8be4-8ffe289d4346 | -7.7755 | -44.0396 | 2025-10-09 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 659b3e2d-f5ee-3416-96f0-d4d63b0b0434 | -11.0416 | -51.1596 | 2025-10-09 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4225bc7e-246e-39ed-b9d1-8dbf2c06b756 | -18.0448 | -51.1777 | 2025-10-09 00:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 91.6 |
| f1c88452-fa44-375f-a7af-5a68ab3dea23 | -10.8502 | -49.9432 | 2025-10-09 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 33ae1e13-b59a-3888-a778-edc9c9d2a61a | -7.7758 | -44.0164 | 2025-10-09 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 0c33dcb8-5cda-3a3f-954a-b185b88bee2b | -11.1292 | -47.7526 | 2025-10-09 01:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 39f767c1-1d73-3060-aa14-1780ec65f3ec | -4.991 | -45.1124 | 2025-10-09 01:00:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 3379b501-a2f6-3b63-abbe-80490bd4ec3c | -19.7347 | -42.2052 | 2025-10-09 01:00:00 | GOES-19 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 154.4 |
| 47772433-37a8-391c-8fbb-b94baf2617bf | -4.2781 | -48.8677 | 2025-10-09 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |


[Clique aqui para ver as próximas entradas](README4.md)
