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
| 747adc22-6e2e-3556-a5ff-48930915b18c | -1.1831 | -53.8985 | 2024-10-27 00:15:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 6a29dc9e-b55e-3709-b453-f00de28a4079 | -1.1831 | -53.8784 | 2024-10-27 00:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| cdaebbe7-eaef-34fb-80ff-96448307a9c4 | -1.5159 | -48.576302 | 2024-10-27 00:15:12 | METOP-B | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3820c451-f9d7-3b9b-8cb2-71152fe4e736 | -1.518 | -48.5858 | 2024-10-27 00:15:12 | METOP-B | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1204b630-9e70-3415-9c89-f002553676a2 | -1.5201 | -48.595299 | 2024-10-27 00:15:12 | METOP-B | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db05b59a-bd42-3981-9b02-b985908f3d88 | -2.8235 | -54.510899 | 2024-10-27 00:15:12 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1285bfa2-903f-3e0e-861d-31480df08205 | -2.8139 | -54.513 | 2024-10-27 00:15:12 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 832f6dff-8184-33e6-9f0f-136c56860b01 | -2.6332 | -54.243698 | 2024-10-27 00:15:13 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a917bd6-047f-3a51-bbbb-26b16ea3f6d9 | -2.6235 | -54.2458 | 2024-10-27 00:15:14 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4629cdc6-277e-3eaa-a1c5-3d04eb2c49f2 | -2.6288 | -54.269798 | 2024-10-27 00:15:14 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bdbde48-4d23-36d6-9544-947efcaf1373 | -2.6138 | -54.247898 | 2024-10-27 00:15:14 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 072ea627-cf20-3931-bbe0-2bffcf15f0c9 | -1.7874 | -46.4065 | 2024-10-27 00:15:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 7f8b0bcc-64c5-30fc-b61b-e5209485314f | -1.7875 | -46.3844 | 2024-10-27 00:15:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 6ce8593f-bdde-3b1b-b321-c3f8204fee58 | -1.8059 | -46.4062 | 2024-10-27 00:15:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 667a2bc0-d847-3db9-a3b0-6aa03b0c49cf | -1.806 | -46.384 | 2024-10-27 00:15:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 5920608d-66d3-305e-8db5-adc26872b620 | -1.1205 | -48.005001 | 2024-10-27 00:15:15 | METOP-B | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3a2e79c-e9d3-3945-99ce-cd7b2e707148 | -1.906 | -59.9839 | 2024-10-27 00:15:16 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e935b26a-3cb7-32e4-9125-44a813fd0bbd | -1.9243 | -59.9837 | 2024-10-27 00:15:16 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 554b1100-55f9-3b3c-9a59-fa8b9aef4d43 | -1.9232 | -52.049599 | 2024-10-27 00:15:17 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb758231-d3fb-3ab5-940f-a2b386edf80f | -1.9269 | -52.066002 | 2024-10-27 00:15:17 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a30f876-0a11-39fd-862f-d050b037dfed | -1.9135 | -52.051701 | 2024-10-27 00:15:17 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a331557-2408-3490-b10d-b08ed3be1048 | -1.9172 | -52.0681 | 2024-10-27 00:15:17 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51aa9549-bdd8-3c41-a1f0-2c755cbbff0b | -2.3578 | -47.6641 | 2024-10-27 00:15:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| ff780f4c-1137-3b1c-bdaf-f244b6657f3c | -2.4786 | -50.2858 | 2024-10-27 00:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 156d143b-bced-36cc-bb1f-28f4ce6a3110 | -2.486 | -48.0507 | 2024-10-27 00:15:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8aa1f874-a069-3b97-a220-92579c31dc43 | -2.6321 | -54.2975 | 2024-10-27 00:15:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 62c5beea-7427-3cf3-ba23-72578e82a84e | -2.6482 | -49.2465 | 2024-10-27 00:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 0a8fe0cb-3004-3071-ae80-ca07aa4b78d7 | -2.6483 | -49.2253 | 2024-10-27 00:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 3245870b-f901-3720-b203-6a2fbefb7be0 | -2.6505 | -54.2971 | 2024-10-27 00:15:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 21525186-482f-3ade-a295-a46ce355af0b | -2.8329 | -49.2626 | 2024-10-27 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e734d761-731b-3769-a361-c440aa46e452 | -2.7033 | -49.33 | 2024-10-27 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| a9a019ab-1cc7-393f-91c9-6c4245948238 | -2.7034 | -49.3088 | 2024-10-27 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 6d24052b-b2c8-364a-a9f6-06faa04b2feb | -2.7611 | -48.7098 | 2024-10-27 00:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ee18dc0e-4c40-3a23-94cf-434ffcd58b03 | -2.8145 | -49.2418 | 2024-10-27 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 9c3fd390-cf2c-3b86-ac20-8f543c39c01b | -2.833 | -49.2413 | 2024-10-27 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| f36358d7-f2f5-31b3-9475-84d1075e66f0 | -2.8501 | -45.0131 | 2024-10-27 00:15:21 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 409.8 |
| 79cb2384-2045-3e35-9faa-62a2b212d27a | -2.8502 | -44.9905 | 2024-10-27 00:15:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 508.9 |
| be86cb5f-705d-3846-a0b2-9ea972c6f40a | -2.8422 | -51.8148 | 2024-10-27 00:15:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ceedb065-4ebf-3d8a-9d18-68f6ef6f4b93 | -2.8423 | -51.7942 | 2024-10-27 00:15:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 7776bbd7-8d6a-326c-aa63-ccbe073edd70 | -2.8687 | -45.0125 | 2024-10-27 00:15:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 454.8 |
| 6386fb41-686b-3808-9b9c-c2dbd4d4c83f | -2.8688 | -44.9899 | 2024-10-27 00:15:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 536.0 |
| 04fb3545-3321-3714-a223-fd18c2d351b6 | -0.9164 | -48.560001 | 2024-10-27 00:15:21 | METOP-B | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e9c275e-178a-33d2-9749-69037f5f4e74 | -0.9185 | -48.569401 | 2024-10-27 00:15:21 | METOP-B | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60ba8afe-22ca-39ab-ade5-62cfd951205f | -0.9066 | -48.562199 | 2024-10-27 00:15:21 | METOP-B | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03742ba6-de0d-3329-b7bb-cf859374e096 | -0.9087 | -48.571499 | 2024-10-27 00:15:21 | METOP-B | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa842905-aedb-36e6-9b0c-8b95dda9d721 | -2.2094 | -54.436001 | 2024-10-27 00:15:21 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0cf66e3-8ded-31ac-884d-184d077484d8 | -2.2148 | -54.4604 | 2024-10-27 00:15:21 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 376e4a4a-39e9-36a3-bd1e-69357a372c9b | -1.6582 | -52.005299 | 2024-10-27 00:15:21 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a35321a-c87d-3348-9d21-37ee1dd27cc1 | -1.6618 | -52.0214 | 2024-10-27 00:15:21 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f57f7e9b-9e32-3b07-acfb-a0a620cd398c | -2.8939 | -47.8439 | 2024-10-27 00:15:22 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| cc58576d-3510-35fa-bf36-edf80df820e4 | -2.916 | -51.7716 | 2024-10-27 00:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 858302b4-ea63-37bb-9a2c-f51cbf88262a | -2.9161 | -51.751 | 2024-10-27 00:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 98364092-1fb8-32e7-831a-ab93f552f670 | -2.9214 | -50.295 | 2024-10-27 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 54ee89c7-d602-320d-bcf7-825bc38c2d94 | -2.9215 | -50.274 | 2024-10-27 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| e9dc41cd-66de-3fcd-947d-ce81adaaf76b | -2.9345 | -51.7711 | 2024-10-27 00:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| e2835098-98b9-3524-8a90-9e73a90711cb | -2.9345 | -51.7505 | 2024-10-27 00:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| cecbc00f-bc34-38aa-8138-f1587eb79fb5 | -2.9398 | -50.2945 | 2024-10-27 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 04d2465a-d0e0-3d58-9d78-97bff8553be5 | -2.9399 | -50.2735 | 2024-10-27 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1ed43334-8fbe-34b8-ac4a-1f314ac3a810 | -2.9669 | -53.0389 | 2024-10-27 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 83615ab9-4feb-33a5-8b1e-c74666850bb4 | -2.9853 | -53.0384 | 2024-10-27 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 50397581-0c06-33bd-b920-f727b8ffc58e | -3.0703 | -45.6575 | 2024-10-27 00:15:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 103.0 |
| e64d9d65-9b32-3f44-93e0-cde050e6d51c | -3.0888 | -45.6568 | 2024-10-27 00:15:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 4b50fed9-3c36-3b85-8e79-7e8a38515151 | -3.1106 | -44.9809 | 2024-10-27 00:15:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 4fcfed3f-ecb5-3a59-8d29-abbf8cc74b7e | -3.1057 | -50.3525 | 2024-10-27 00:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 99a123e2-a8b3-3e3d-ba89-e46a17500bc0 | -3.1292 | -44.9801 | 2024-10-27 00:15:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 49864a05-d0d4-3f16-abb7-78257681cef1 | -3.1242 | -50.3519 | 2024-10-27 00:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 6aa5eec0-486b-3de4-84da-9a709abca89b | -3.1811 | -45.7875 | 2024-10-27 00:15:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 39300961-9dc2-3726-b246-83cdb17cc9d6 | -3.2486 | -51.5558 | 2024-10-27 00:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 3406e169-4d6e-3062-88e1-23a54e3bad20 | -3.3256 | -50.7641 | 2024-10-27 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 3d36406a-9f4d-3a78-8f04-3c48482777bc | -3.3256 | -50.7432 | 2024-10-27 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 80202618-953c-3853-9536-e0120a602242 | -3.344 | -50.7635 | 2024-10-27 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 3721de55-8cd6-332a-9adc-d9e62301c51a | -3.3441 | -50.7426 | 2024-10-27 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 79dbd581-217a-3164-ab88-e67ecd12f482 | -3.3925 | -52.4358 | 2024-10-27 00:15:25 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1a6273e0-ab6b-3100-8441-28c5e84d8439 | -3.4392 | -50.0896 | 2024-10-27 00:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| f605b3d6-f34a-3b2a-9b65-79dab365773f | -3.4577 | -50.089 | 2024-10-27 00:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 3f8ff7a9-978d-385f-9b30-6f849c117d09 | -3.4762 | -54.5772 | 2024-10-27 00:15:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 386909ff-ff16-3a14-8698-45833347b4a9 | -3.4763 | -54.5572 | 2024-10-27 00:15:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 35a552bf-a0f3-3f71-83f3-f07ab47e5e81 | -1.9355 | -54.344398 | 2024-10-27 00:15:25 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a795081a-0ed9-3d1c-8a41-e1c90b2b3260 | -1.9408 | -54.368198 | 2024-10-27 00:15:25 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bdb1fd7-fa0b-3e30-811e-bd263699a2a3 | -3.5626 | -51.4217 | 2024-10-27 00:15:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 38da7cf1-7c18-3ba9-94d9-e6189ef325bb | -3.682 | -45.9455 | 2024-10-27 00:15:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 7179c2fc-c7df-31db-ad67-b5ef76870f8e | -3.8149 | -48.8874 | 2024-10-27 00:15:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 878b6041-31dd-34e8-a53c-5150396aee1b | -1.5978 | -53.286201 | 2024-10-27 00:15:27 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9691d40-a67f-3fc0-a881-82ea4f06933c | -1.5656 | -53.460899 | 2024-10-27 00:15:28 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a989fe7b-f422-3f90-92bd-b36555bac3a3 | -1.5702 | -53.481201 | 2024-10-27 00:15:28 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57efbddf-8c3b-3a00-8ffa-7ca1edd43c05 | -4.3841 | -49.7571 | 2024-10-27 00:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 7fffb2ea-d185-3a77-932c-dbe3b9d894ea | -4.4026 | -49.7563 | 2024-10-27 00:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 4d3dfc06-7ff4-3e1d-9154-36c628e8666f | -1.4222 | -53.366001 | 2024-10-27 00:15:30 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f5e33ae-20de-3949-86bf-a2889235a4fd | -1.4267 | -53.385899 | 2024-10-27 00:15:30 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16aef7be-ef1c-3e18-9e55-a89f94117efa | -1.417 | -53.388 | 2024-10-27 00:15:30 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c61c916e-ea4f-3866-a1f7-80aeb265f7b2 | -4.4696 | -50.9926 | 2024-10-27 00:15:31 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 37b34b9a-9ed6-3152-83ad-d4c1d72807fc | -1.2583 | -52.998699 | 2024-10-27 00:15:31 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0638d4f5-ce74-3c21-8809-33fa3bb695ad | -1.2486 | -53.0009 | 2024-10-27 00:15:32 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3c04c4d-9e6e-36f1-9e45-6b4334607e96 | -1.4272 | -54.023499 | 2024-10-27 00:15:32 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8639253-0ed0-3d71-bb49-d283a4376311 | -1.4175 | -54.0256 | 2024-10-27 00:15:33 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57a0f2e6-5f30-3cfb-8932-d90f7358ff09 | -1.4224 | -54.047699 | 2024-10-27 00:15:33 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4d070d8-1e5d-335b-8cc1-cc6e5052d979 | -5.0072 | -45.4275 | 2024-10-27 00:15:34 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 25a035a6-2a0b-33c9-a855-3d13927d43eb | -5.2896 | -60.1632 | 2024-10-27 00:15:36 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| df6d8c86-14df-39a5-9635-57f38c0372d4 | -1.1749 | -53.851299 | 2024-10-27 00:15:36 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a83dc5f-b7c3-3e95-9460-e0541c576ffd | -1.1604 | -53.832199 | 2024-10-27 00:15:36 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
