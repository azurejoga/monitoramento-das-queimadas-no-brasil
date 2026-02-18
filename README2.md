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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12be86b4-b7bd-3127-ba1e-f17597639551 | 2.68187 | -60.21404 | 2026-02-18 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 157.7 |
| ab8e45e9-14e2-3e8e-9ea2-975c65f44c5c | 3.23015 | -61.19441 | 2026-02-18 01:09:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ddae9513-c872-317e-bec3-36386996f050 | 2.56412 | -61.01168 | 2026-02-18 01:09:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9fedfdda-e4aa-3be8-86af-da342a875a17 | 2.68049 | -60.22421 | 2026-02-18 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.8 |
| fac45fd2-2e31-3373-abd6-890c37ac9a0c | 2.92272 | -60.81881 | 2026-02-18 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4a2531ce-d81a-36aa-9165-ac86863b355e | 4.27439 | -60.07856 | 2026-02-18 01:09:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 446c725a-58cc-38ff-ad87-5ad99d7c0fcb | 2.66982 | -60.16036 | 2026-02-18 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c9fee46f-2063-34a0-9e18-12daea84f86c | 4.33341 | -61.21077 | 2026-02-18 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3aa65431-7f59-3381-bf39-5d8fb655beff | 2.91089 | -60.83667 | 2026-02-18 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7e78925c-91d0-367d-8b84-b897389f2593 | 1.28956 | -60.43305 | 2026-02-18 01:09:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 34d77f13-3833-371f-a70f-9d34056ef884 | 2.26205 | -60.19796 | 2026-02-18 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3f07123a-28ad-3de2-a94e-0dac4ba28978 | 4.23198 | -59.78511 | 2026-02-18 01:09:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9451ee88-8366-3cde-886d-eb2e8ef4a14b | 1.29089 | -60.42341 | 2026-02-18 01:09:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| becb7284-bd43-3292-bc3c-7d22b4317842 | 1.81115 | -60.45355 | 2026-02-18 01:09:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c27a669-9e40-3690-9713-6efeda022eaf | 4.01995 | -60.31184 | 2026-02-18 01:09:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 00050b63-5774-3d41-9ad4-3d908bc9096b | 2.6712 | -60.1501 | 2026-02-18 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 29.5 |
| e64cd7bd-904b-39e1-8edc-0223f84df57f | 2.67931 | -60.16167 | 2026-02-18 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 7e636c73-eee5-3372-9822-4d6cb8697a19 | 1.44578 | -59.96786 | 2026-02-18 01:09:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6741c997-9db2-3060-a65f-9cfad87a4084 | 2.91353 | -60.81749 | 2026-02-18 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7b7029d0-1b86-3ce4-8fbd-8ce1719b0192 | 4.30622 | -60.38087 | 2026-02-18 01:09:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0ad1e066-e329-3364-975f-ce1108542739 | 2.91605 | -60.93453 | 2026-02-18 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 08dc8b15-b9ef-3097-97ad-ea35402a02ba | 2.6724 | -60.1453 | 2026-02-18 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 0e0f9187-ee3b-3193-9479-0fce37c3e641 | 1.267 | -60.4076 | 2026-02-18 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8e77f4bd-713d-39fd-a71f-50689a48109f | 2.6905 | -60.2211 | 2026-02-18 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 460bc22c-06c5-3d4c-a40b-362e17201c19 | 2.6906 | -60.2021 | 2026-02-18 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 651792f0-5d08-3189-8f82-cce1d3be9d5a | 2.6723 | -60.2214 | 2026-02-18 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 18b40ee3-249d-3980-8db7-c361e9187575 | 2.6724 | -60.1643 | 2026-02-18 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a54e29f1-a843-3b25-a003-251515b97678 | 2.6723 | -60.2214 | 2026-02-18 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1318ddc1-2727-3dd4-a923-c7d182a50424 | 2.6724 | -60.1453 | 2026-02-18 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4c01d3eb-5614-3993-b9db-489cb9674a7d | 2.6905 | -60.2211 | 2026-02-18 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 095d4bac-62c6-3c8e-8189-417920cb6e71 | 2.6906 | -60.2021 | 2026-02-18 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 1c1907f8-2082-3fe7-8bce-566efba3b152 | 1.267 | -60.4076 | 2026-02-18 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ce036a62-2c0e-3caf-8ee9-a5e73b93b7d9 | 2.6905 | -60.2211 | 2026-02-18 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 006eefab-0b7c-33d1-b12b-cb9a5fda0195 | 2.6723 | -60.2214 | 2026-02-18 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 995ebd38-097e-3011-a7ce-94abc539e743 | 2.6906 | -60.2021 | 2026-02-18 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 6ff5fdf8-989a-30be-93be-8892fdee68e0 | 2.6724 | -60.1453 | 2026-02-18 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 88dda2fa-a635-32e2-8a1f-7ff23cd4927e | 1.267 | -60.4076 | 2026-02-18 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 0b8b0009-907b-36f5-a4a1-a671cd0e9c6f | 2.6724 | -60.1453 | 2026-02-18 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 559513ef-112f-3751-934e-8bca61c48893 | 2.6723 | -60.2214 | 2026-02-18 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3872db40-d997-3a48-8b17-2a29f691e566 | 2.6906 | -60.2021 | 2026-02-18 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| bf6634a4-062b-362f-aff7-6feb2eb1e93f | 2.6905 | -60.2211 | 2026-02-18 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| f40f07cd-79fc-3aaf-b67c-095f02150f34 | 2.6906 | -60.2021 | 2026-02-18 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 53b250a9-6047-37c0-a13e-0f54d523ec1a | 2.6724 | -60.1453 | 2026-02-18 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c5832cb6-e73a-3351-bf8b-5f749bcf12ed | 2.6723 | -60.2214 | 2026-02-18 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| cdf39aee-1d10-33b3-a1a7-861c10679846 | 2.6905 | -60.2211 | 2026-02-18 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| b1b758a4-544d-3429-985a-765820025772 | 1.267 | -60.4076 | 2026-02-18 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.9 |
| b9e98910-ce08-3273-8008-a13709866038 | 2.6723 | -60.2214 | 2026-02-18 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 71f6c864-ae7c-3c31-8ace-e049ad43ca72 | 2.6905 | -60.2211 | 2026-02-18 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 096eb3db-9163-3f2c-a250-2d7153572c26 | 2.6724 | -60.1453 | 2026-02-18 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 88a4398a-6b1b-318f-8e65-7cae7fffc8cf | 2.6905 | -60.2211 | 2026-02-18 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 22d96abf-ea99-3775-9d31-018216ccdb83 | 2.6906 | -60.2021 | 2026-02-18 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 29a7c9df-e69c-3da8-842a-6dc78d38ab43 | 2.6724 | -60.1453 | 2026-02-18 02:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| f243a9af-07b1-34bc-8388-8a2686e2d7dc | 2.6905 | -60.2211 | 2026-02-18 02:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 84.7 |
| a75895fd-b4fe-3baa-8af2-acdb43c687ed | 2.6906 | -60.2021 | 2026-02-18 02:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 777d2279-34a9-3725-a01e-d61c2f1fbf09 | 2.6724 | -60.1453 | 2026-02-18 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 876324d5-efa2-3fe7-96cc-d39206a39174 | 2.6723 | -60.2214 | 2026-02-18 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 8e70687e-3f8a-3884-b27a-ccb891fbd0af | 2.6905 | -60.2211 | 2026-02-18 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 31e62f64-3345-3f3f-b012-4e7a31a6d30d | 2.6906 | -60.2021 | 2026-02-18 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 3224fff2-d7c5-3f83-ae31-13da081b7f9b | 2.6723 | -60.2214 | 2026-02-18 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 183c1e89-ea8e-352c-9814-b5a43bb34c25 | 2.6905 | -60.2211 | 2026-02-18 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 50569153-77a1-35d6-8e84-af2923730416 | 2.6724 | -60.1453 | 2026-02-18 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 244019c3-48c6-3436-a7c8-0bc2db9af5d1 | 2.6724 | -60.1453 | 2026-02-18 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e7d8dde0-8c57-3764-9ebf-1b01fb22b164 | 2.6906 | -60.2021 | 2026-02-18 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| db3048d0-bff8-3b05-9ba9-6ef8efd14fa8 | 2.6905 | -60.2211 | 2026-02-18 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 86.4 |
| c62d115b-bfd7-375b-8bb3-1c34014607e1 | 2.6724 | -60.1453 | 2026-02-18 03:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 1435f6e0-c8a1-369f-8a0c-8b0425e702fe | 2.6905 | -60.2211 | 2026-02-18 03:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 1ef5e137-bfc9-36e8-bbeb-9ea84a22b324 | -7.65 | -35.24413 | 2026-02-18 03:06:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf261e2e-1d10-35b1-a2b1-9adc30fa301c | -7.64473 | -35.243 | 2026-02-18 03:06:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89685a62-56a6-3e89-a150-751e1fc4f482 | -12.90146 | -41.51591 | 2026-02-18 03:08:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1fa42825-ca46-3f18-b600-f32945b341b3 | -15.31494 | -42.057 | 2026-02-18 03:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 80955738-edc6-32f9-b2c1-102773fe95a6 | -15.31657 | -42.05943 | 2026-02-18 03:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| f58f1ffc-d59f-3755-82ca-53f0d90e26d9 | -12.9085 | -41.51756 | 2026-02-18 03:08:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 29453714-abbe-3782-afa8-17e9afdd417e | -12.24866 | -38.32424 | 2026-02-18 03:08:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 908ebc97-ed71-39d7-8288-37f80263c83d | 2.6905 | -60.2211 | 2026-02-18 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 95ec3abb-f420-324d-9c55-fa571229d771 | 2.6724 | -60.1453 | 2026-02-18 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 83ae3d63-d889-34d9-a5d7-b9e8697a9fb9 | -16.67908 | -41.37105 | 2026-02-18 03:10:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b66b66b6-dd0e-3bbd-aa9b-ed7ebcd36b7f | -22.46288 | -42.04626 | 2026-02-18 03:10:00 | NOAA-20 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e12de375-25bd-3a2e-a855-1819008ca14f | 2.6905 | -60.2211 | 2026-02-18 03:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 86410d75-37c0-3fae-8ff9-59732b44d7e4 | 2.6724 | -60.1453 | 2026-02-18 03:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 24c4d49a-c4dd-3a4a-861b-b50d1ff384de | 2.6724 | -60.1453 | 2026-02-18 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3192701b-f7e0-3d27-b2f9-9824b8d24c18 | 2.6905 | -60.2211 | 2026-02-18 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 60003f7e-f803-3869-89af-7946d53037e5 | 2.6905 | -60.2211 | 2026-02-18 03:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 941179d8-e948-3595-aa9b-d05c1c198b88 | 2.6724 | -60.1453 | 2026-02-18 03:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 56df2a53-6019-3246-96bd-2e0a54968115 | 2.6723 | -60.2214 | 2026-02-18 03:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 2cda054e-a565-360c-80f1-e3ec2fcff4ab | 2.6724 | -60.1453 | 2026-02-18 03:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f3d612e5-870b-3e1b-8c06-691de1e8e6cd | 2.6905 | -60.2211 | 2026-02-18 03:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5f1c5e1d-28fd-3784-9d68-94afa4dd7fc7 | -9.23307 | -40.51162 | 2026-02-18 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c69b2546-b439-3dfb-920b-0155293a7ade | -7.74552 | -35.20633 | 2026-02-18 03:55:00 | NOAA-21 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fb6fdd0d-84f7-34bc-9a8d-e3cf9b7b3ddb | -9.1125 | -44.67864 | 2026-02-18 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| debdc147-ae83-3cb7-8046-b5884ada9781 | -8.28983 | -40.40704 | 2026-02-18 03:55:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3e2f6074-9bf2-3b52-a674-cd3aff167183 | -8.44105 | -45.1364 | 2026-02-18 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5aacf92a-055c-3690-9032-962679565e73 | -8.53963 | -35.86145 | 2026-02-18 03:55:00 | NOAA-21 | SÃO JOAQUIM DO MONTE | PERNAMBUCO | Brasil | 2613305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| afcc8ce5-474d-38ec-9316-7601d7c9d902 | -9.81293 | -38.1007 | 2026-02-18 03:55:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8de4ce80-a5d5-352f-a02f-e6f12ddc72fd | -9.33979 | -36.84078 | 2026-02-18 03:55:00 | NOAA-21 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e5b90b6a-a82d-3e79-9085-d66f6264e061 | -14.8618 | -43.84992 | 2026-02-18 03:57:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a99dbc42-176d-32d9-8583-8e03b49acaff | -11.88787 | -45.27743 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b2ff0fc-9ca6-3744-8e91-70200b520545 | -13.01782 | -45.0595 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 202ea006-47f9-33e8-9ed9-6e7ba1b92128 | -12.4723 | -43.73064 | 2026-02-18 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53d08d4d-531f-35fa-bc6d-31f982497d7d | -15.55565 | -41.78671 | 2026-02-18 03:57:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 96e1f1a9-26cc-3e8a-8895-5c7fcd554d52 | -13.01383 | -45.05877 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README3.md)
