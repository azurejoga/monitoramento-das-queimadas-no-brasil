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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fb0d8fd-dabf-300e-b0c1-29185b4ff522 | -2.5423 | -47.811 | 2025-10-12 04:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a1668a47-91cb-3331-a1fe-9f9e42c49bb4 | 1.17358 | -50.8983 | 2025-10-12 04:59:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 011d40ad-466b-3313-aa1a-67f993d0d0d5 | 1.82328 | -55.82784 | 2025-10-12 04:59:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e5abd3b-1c46-3416-9b41-db3fbe45be01 | 1.82387 | -55.83157 | 2025-10-12 04:59:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a573ddf-e912-3196-83ec-52168a8037a1 | 1.8503 | -55.84718 | 2025-10-12 04:59:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82f3a0f5-bc76-3220-90f4-bbd622613bd2 | 1.17249 | -50.89929 | 2025-10-12 04:59:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4283a7dd-b35d-35f1-b487-608f2bff9f0b | 1.17715 | -50.89773 | 2025-10-12 04:59:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dd0379d-f431-3937-98d0-6ee2f2556aa9 | 1.9073 | -55.73886 | 2025-10-12 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31939fbe-4f40-3980-80be-ffe8b238f91a | 2.92695 | -60.2909 | 2025-10-12 04:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b77d065-7d11-3f64-b9c4-16f394ada2c1 | -3.97249 | -42.85371 | 2025-10-12 05:01:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d962800c-ac89-3bf7-a490-34de1d8bc771 | -3.14779 | -52.40138 | 2025-10-12 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 666aa43f-d241-36b4-8929-2f6962ad3603 | -3.146 | -44.42965 | 2025-10-12 05:01:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95d6340d-bd8f-36f7-a223-0c3140e3236d | -7.49402 | -42.77062 | 2025-10-12 05:01:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3310fa3b-0e5e-34c9-9704-3a9a3edc636b | -5.90909 | -45.43095 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05434ba8-260c-3dd8-b033-9ca1f4b79bbc | -3.51006 | -45.84583 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 51628b54-3626-372f-bfb7-bfefc68ce2a4 | -3.27677 | -52.96179 | 2025-10-12 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ece4e1b1-bf2c-3556-966a-0d14ff0cd26e | -0.43109 | -52.0685 | 2025-10-12 05:01:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dca77c91-dcf9-3a5c-93a4-86adbc8dcf1b | -3.52841 | -48.91686 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68da0b7c-bb44-319e-9222-3b72c81a8eaf | -3.5154 | -45.8466 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d47bd21b-c1dc-3ef4-8217-936d606f096c | -3.68092 | -49.19297 | 2025-10-12 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2622675f-d770-30df-b34a-0aa3a48f875f | -2.53818 | -47.80662 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 849bb6a1-cb69-3fea-9908-f0cf43954816 | -2.44383 | -49.37119 | 2025-10-12 05:01:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c24bc51c-680d-3cac-a533-46a2a95c0de0 | -7.88177 | -44.51531 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02eb76f2-5703-3771-a047-a7d5fd5efd72 | -4.4219 | -43.46707 | 2025-10-12 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35c39ea9-3983-366d-b32d-abaf47235b09 | -1.13476 | -47.80528 | 2025-10-12 05:01:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c9a082a-b8dc-36c5-a4db-da0a910a5042 | -2.53286 | -47.81067 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bea9d273-d180-366a-912e-7398c944e603 | -6.50388 | -42.44106 | 2025-10-12 05:01:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e34596b6-a002-3edd-a44a-0914b8a843e0 | -5.80383 | -51.49943 | 2025-10-12 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb7d54c7-41a9-3f7a-9390-d1f23cecf913 | -3.50958 | -45.84914 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 86eac4dc-b943-3ae5-b92b-a58646b3bffc | -3.93691 | -47.98401 | 2025-10-12 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f69e3e8-642a-3646-a926-f71153bd406b | -2.43972 | -49.37055 | 2025-10-12 05:01:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80ace4e7-e104-3eea-9d34-50596fc7917c | -3.50521 | -45.84174 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7b8f0d9-6698-3005-9a78-15b0d5f245c9 | -7.80456 | -42.42752 | 2025-10-12 05:01:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8d1c396f-feed-3cbb-85b8-35fa024e4f84 | -2.53892 | -47.80185 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 879f15ed-2d3c-3844-a0e2-340eeb9e80db | -3.53211 | -48.92159 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f775737-afe1-330a-9314-3bb0a5f63104 | -2.26863 | -47.85218 | 2025-10-12 05:01:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2cf284c2-2139-3faf-94e0-09edf81fabf1 | -5.86109 | -42.8544 | 2025-10-12 05:01:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 31ef5f01-6f14-36f5-9548-c4d1b94bf5f7 | -5.9215 | -45.42492 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e44d91b7-a900-3cce-b3ce-2bdd41e212db | -3.50696 | -49.05833 | 2025-10-12 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 570b5a49-8074-36f7-b7a6-d616b67e6922 | -3.53149 | -48.92566 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f693189-c4c7-3d22-af10-ad64cd4425c3 | -7.85584 | -44.52901 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2bd00b13-749f-3a3a-9216-74c172c0dabe | -1.56927 | -60.34565 | 2025-10-12 05:01:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 566a70e8-3ca0-3b38-9109-acce9c322df7 | -6.27739 | -43.9117 | 2025-10-12 05:01:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bd1c7a8-c211-3b81-8b26-c046b8e87366 | -3.53643 | -48.92222 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b13b19e0-e48f-3834-97ba-82e5cc07befc | -4.27371 | -46.92075 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c445eed9-3f0b-3a10-8fe1-9f2537aeb295 | -6.28453 | -44.41027 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c96433a-051e-3e7e-981b-d63fc82dd43f | -3.51492 | -45.84988 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 61f54f6c-63e7-3681-94ea-72f06675bd25 | -3.19705 | -49.47935 | 2025-10-12 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ffb6cae-222e-3e0c-9216-42d70bfe1e97 | -3.512 | -45.83253 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d932797-2750-3f11-bddc-dd3bc035126c | -8.21763 | -43.36111 | 2025-10-12 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ae8af728-84f4-3f46-aa68-0661b5662575 | -5.8619 | -42.84865 | 2025-10-12 05:01:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cf6424c0-ab93-322f-8b1c-96017bbf3dc1 | -7.26064 | -44.15585 | 2025-10-12 05:01:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eecab9ea-43e3-343c-932e-f1841dfaf4b3 | -2.63145 | -47.30331 | 2025-10-12 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb384d2c-a7c5-3abc-8b80-8ccc5bcc8310 | -6.84385 | -47.34748 | 2025-10-12 05:01:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15c01d1b-1f87-32e5-9565-1a8c4380cfd4 | -1.89923 | -51.01192 | 2025-10-12 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 82ad64df-c4bb-332a-9835-c823d2e99692 | -3.51734 | -45.83331 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f221def7-aa83-354c-a042-37669bc266e7 | -7.8707 | -44.88211 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07b6ef69-04ff-3f4b-b1e7-84568be21fad | -7.85403 | -44.5352 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1016059a-a010-34af-a11e-4dbe80c4a67f | -5.91476 | -45.43184 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0632ee37-8e0a-3c4d-a10f-2ce8c0ed98d7 | -7.62345 | -47.50942 | 2025-10-12 05:01:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04cb3285-64f3-3340-b91d-41ba20fd1355 | -2.92397 | -48.30087 | 2025-10-12 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71c605ba-e453-3136-86fc-0f90d48f0ed4 | -5.59406 | -45.84142 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 511fd0d0-e8b7-359b-8f41-3cf7c8ebb0f3 | 0.25687 | -51.0826 | 2025-10-12 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b919af90-1469-3726-b980-3017cec0dd29 | -6.58611 | -44.62865 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 38d43013-ba5b-3536-986d-bff11681ba85 | -2.99768 | -48.73796 | 2025-10-12 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 671fb378-ff0c-332d-b31f-b92dc6b235e4 | -4.27871 | -46.92154 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2fed440-5764-3d68-a3a3-58c943982c51 | -2.44082 | -49.3632 | 2025-10-12 05:01:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a428bb74-8a6a-3de2-8b40-adaf5c89f55c | -3.42483 | -52.72702 | 2025-10-12 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 676fa35d-22ec-39dc-8a87-67ad9715f9b3 | -6.49699 | -42.44015 | 2025-10-12 05:01:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6161b3f9-c9fb-389a-9d9f-1c38e94df89d | -7.42475 | -42.96887 | 2025-10-12 05:01:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d036145b-28a7-3568-a9a1-d77a2dc98626 | -3.60939 | -42.74798 | 2025-10-12 05:01:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1d21427-14f2-3b73-85f5-102c3e0bea9c | -5.75725 | -46.4992 | 2025-10-12 05:01:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e81b268-036d-363f-abf5-bf234f06bec7 | -6.58676 | -44.6239 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 503bdf73-b92d-33ed-85e2-0a06172476c5 | -1.57049 | -60.34398 | 2025-10-12 05:01:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99015e1f-ee92-3ddf-9f51-63c93aa25136 | -2.79256 | -49.62422 | 2025-10-12 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6c84114d-b933-3af2-b663-eac9cdaea85b | -3.51054 | -45.84251 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0609ef0-e63a-3d97-b850-fe817e6400cb | -4.45924 | -50.09951 | 2025-10-12 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94e1341c-0d17-3e49-8363-feef9c739a30 | -3.58008 | -51.23913 | 2025-10-12 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a108683f-0358-3ae1-a70f-0f5c1f2e4725 | -6.76681 | -42.84162 | 2025-10-12 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ba43e551-4caa-3a52-be67-ccdd312e1e70 | -3.53581 | -48.9263 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b5de834-9340-3401-a52d-ab10575a68f6 | -8.19147 | -43.32796 | 2025-10-12 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bae05b3e-97e9-3f5d-a58a-e32cdfbeef7e | -4.27327 | -46.92365 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0107634e-16c1-31f1-ad0b-e16dda5e903d | -7.80535 | -42.43264 | 2025-10-12 05:01:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ea96940f-be51-3777-a95c-cace5eeb6f6d | -5.91423 | -45.43571 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7aea8d5-0f13-3b77-a84b-38b961e3e4d8 | -4.67649 | -43.26207 | 2025-10-12 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e03a9ff-bca1-3726-806b-344027dc466f | -3.50648 | -45.8443 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63bb0ada-3bae-335c-be14-94399a9f9e04 | -3.51103 | -45.8392 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b04ed0f6-36b6-3805-a4e7-3a81c8f6a115 | -6.59422 | -44.5686 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7678976f-8a1e-3c8c-935f-08789ad55c3a | -3.87737 | -42.51144 | 2025-10-12 05:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e08af64a-914d-3476-b7de-b79b0641e087 | -3.51685 | -45.83665 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b67595b8-a26c-3c6b-92ab-35dfda35638a | -3.34483 | -42.1573 | 2025-10-12 05:01:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| aee0878c-c6da-3892-876a-190df7633e24 | -3.50547 | -45.85092 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b456c734-1e77-3eb7-81e4-ef1bbce5f6fd | -5.75772 | -46.49597 | 2025-10-12 05:01:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11f727aa-e75a-33b6-8ee1-71a4d0f6d4a0 | -4.41486 | -43.47128 | 2025-10-12 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 152245f2-a578-322f-8fdd-b27ffc8d4f57 | -2.29285 | -47.99624 | 2025-10-12 05:01:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60ffae43-0948-3332-a642-aa0150b4be5d | -3.54012 | -48.92692 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4d0cb6a-965e-31d8-af13-3fdeaa9f45bc | -6.5807 | -44.62315 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9518d184-dd07-3ee9-b7bf-b597eb237afe | -2.99273 | -48.74141 | 2025-10-12 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9abd8245-ae6c-38ec-85ff-bf8b508d6df3 | -6.6003 | -44.56935 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f68648dc-7558-3b69-bb7e-109f258a56f7 | -3.5838 | -51.2397 | 2025-10-12 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README38.md)
