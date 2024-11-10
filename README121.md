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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2d8fe3b-f037-3eab-9672-7a9cd31e9585 | -17.60921 | -57.51686 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.5 |
| 05bc836c-6c99-3afb-8a82-f40a3d71fcad | -17.62514 | -57.48972 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 62acde6c-39ee-3da7-8fec-c90d2d959ad4 | -17.60746 | -57.53681 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 4d516e8b-3ba0-3077-871a-a34f0a59ffc8 | -17.63042 | -57.51058 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| fe67f8af-9eeb-3875-9b91-ab88014474dd | -17.62996 | -57.5191 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 8a8baedc-7d61-3942-9b92-ae6a8cf70fea | -17.63152 | -57.49718 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 3ba30cdb-f511-3911-a4be-84ea5a2c2e4b | -17.60229 | -57.51611 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 1808ca67-44a7-31d7-8562-0c80075014b9 | -17.60113 | -57.52942 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.4 |
| cefe6937-8162-38a4-ae48-aaa13c28eb04 | -17.62241 | -57.52316 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 7c555f9b-9fe9-3ab5-a3dc-0b284d4ea20a | -17.62296 | -57.51648 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 1dab8ffc-a58e-3910-aa8a-f4c4f22482c4 | -17.60979 | -57.5102 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.5 |
| d7f7ee0d-32dd-38fe-b80d-d8a9ab0bb71c | -17.62937 | -57.52576 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.9 |
| d4df4e16-89c4-367b-8040-1fb15833fd57 | -17.62187 | -57.52983 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.3 |
| 124e5c28-1bd0-3887-a042-c9413af623d1 | -17.62187 | -57.53166 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.9 |
| 771a94fc-316d-3800-955b-41171ed6df88 | -17.63173 | -57.49906 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 30a406f7-142c-344d-b98f-3206de17a835 | -17.62245 | -57.52501 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.9 |
| ad671097-9277-3dda-8d3c-197b8f8f1c1d | -17.61729 | -57.50427 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 04d7d022-9272-379f-b8ed-651588acd213 | -17.6248 | -57.49833 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 3e0e533d-1ac3-3751-9021-5d2948740517 | -17.60171 | -57.52277 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 13b05239-d16b-352d-859c-7e56e23b6af9 | -17.61612 | -57.51761 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.5 |
| dc0d18af-386c-31f1-bf9f-c1ac3a86bc85 | -17.62304 | -57.51836 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 4c70b467-6e44-3708-9c2e-8e7759e81058 | -17.61604 | -57.51571 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 7d5dd080-5dac-37cc-817f-a9e35540c259 | -17.62405 | -57.50312 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| d512aec4-16f6-31a5-838f-1f0fafa72c98 | -17.62539 | -57.49164 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 0abfcba2-5f1f-3b51-a377-91695f247fb0 | -17.62363 | -57.51169 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| b3f86fc5-b78c-3c90-85c8-56945412e5a1 | -17.6167 | -57.51094 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.5 |
| 248b31d0-2311-352a-a11a-39ad826f4f59 | -17.60804 | -57.53016 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 7bd74f78-0737-35ec-b232-f893ed0406d1 | -17.62933 | -57.52393 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.6 |
| 9494adab-9867-3064-9bfd-9a8e295c4b49 | -3.2243 | -53.0727 | 2024-11-10 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| af9c1bf8-eae0-3d46-89be-8cd4ee1eb8a0 | -2.7587 | -49.3497 | 2024-11-10 06:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 0d042f60-20fd-3fc1-ae04-931e2fcde310 | -3.9669 | -48.1716 | 2024-11-10 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 8f616d37-8b5e-3bb5-a08d-978915de52c4 | -3.2168 | -50.2861 | 2024-11-10 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 57a0c2a9-81d8-31da-9afa-c4bf7a45a92b | -3.9483 | -48.1724 | 2024-11-10 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2296de47-c399-35e7-8f66-756d3d10927d | -1.5347 | -52.2104 | 2024-11-10 06:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 1237602d-2a2c-319d-8091-48a1483e154a | -2.9355 | -51.482 | 2024-11-10 06:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| cf169b67-feeb-3ae4-9ea4-e130dd504e06 | -3.1422 | -50.4562 | 2024-11-10 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 132a2aff-3d9d-3217-a23b-85b4769c565c | -3.2352 | -50.2855 | 2024-11-10 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| edc0b0e0-22e8-3262-a3ad-19d8075e1d4b | -3.1239 | -50.4358 | 2024-11-10 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 8437999d-6369-38d1-8512-e3be85eeb144 | -3.1238 | -50.4568 | 2024-11-10 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 81136a0d-4d9f-3ed6-94c1-8f60a8a49373 | -2.931 | -52.7753 | 2024-11-10 06:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 0eea6253-22dc-37d4-8527-2915a8be6fb1 | -2.9494 | -52.7748 | 2024-11-10 06:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 6fd732de-a8b0-3f97-a539-8c756bd9dc77 | -3.2244 | -53.0524 | 2024-11-10 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 7ae2cd88-87ac-3407-802a-efcca20d6bdc | -3.9485 | -48.1508 | 2024-11-10 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 017873c4-49a9-38f4-af66-b7754b01484b | -3.2353 | -50.2645 | 2024-11-10 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ab5a3b6b-496b-3d2e-a856-2c72bc226edb | -2.7772 | -49.3492 | 2024-11-10 06:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 5398162b-39ab-3d17-b821-818ab48f5b4d | -3.1423 | -50.4352 | 2024-11-10 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| e9f09a74-d529-37de-a4a0-b5c9c938104f | -3.2536 | -50.3059 | 2024-11-10 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ef372792-aca2-3601-b1d6-ebfa85592257 | -3.2352 | -50.3065 | 2024-11-10 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 4bc6aaa8-e2cf-3ba3-85ca-99e00b862c11 | -3.525 | -44.0286 | 2024-11-10 06:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 60d15c85-1acd-3929-9867-2a8b1a70d47f | -2.8701 | -51.45961 | 2024-11-10 06:12:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| ba021258-c36f-392b-84f5-e9077ffbbf89 | -1.27998 | -53.704 | 2024-11-10 06:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 75ab15ff-9137-398a-8e44-c8bad730bf51 | -1.28634 | -53.71182 | 2024-11-10 06:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4d86fd53-11f7-3d12-a680-dfb1d19fc39b | -2.08019 | -48.82417 | 2024-11-10 06:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 0987063f-10e0-3ac9-9203-ba0d79b1f8cf | -1.32112 | -54.63276 | 2024-11-10 06:12:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bd9b5e39-77b0-31a8-9efd-369165214c11 | -3.22696 | -50.25275 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 48b50961-951f-3979-808e-287de545cbc3 | -1.49163 | -55.43163 | 2024-11-10 06:12:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| cd47240b-19be-349c-9916-f891ef036538 | -2.56073 | -50.66827 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 6e0944a3-4ee4-3b23-9f5e-df02a4f71f2e | -3.12595 | -50.41708 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5f8d4382-de52-3e11-90cc-9dbd8519d17d | -1.13161 | -54.10008 | 2024-11-10 06:12:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9510157a-c040-3818-a19b-84954171c695 | -2.86701 | -51.48095 | 2024-11-10 06:12:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 95d8641d-575d-380b-a49e-93cb82220e45 | -1.51602 | -52.19282 | 2024-11-10 06:12:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 911484c1-aa2d-3813-922e-ad420e27d14a | -3.22729 | -50.67904 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| e4473d3f-1ef5-3d64-aeab-6795642bdd5b | -3.13665 | -50.44551 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 44adb2df-6ba6-307c-876b-006de4686138 | -1.47419 | -54.29448 | 2024-11-10 06:12:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9dd08aab-c4bc-3597-8756-246254351f03 | -1.3059 | -54.66578 | 2024-11-10 06:12:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 73f2703d-6a30-3c62-a641-f616b20b0fd6 | -2.61465 | -54.39647 | 2024-11-10 06:12:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2fdcef1f-9003-34a1-875e-25422585a95d | -2.76696 | -49.33472 | 2024-11-10 06:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| d7498957-ebdd-319a-b7c7-aad4204d6739 | -1.52325 | -54.99107 | 2024-11-10 06:12:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 13eaf63f-0331-3174-ac6f-591dcf6a061c | -1.27551 | -53.71066 | 2024-11-10 06:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 5780fb08-65bd-3b95-bf8a-83c26b6a45dc | -1.13374 | -54.10759 | 2024-11-10 06:12:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 668edc78-1ad6-3d17-b324-122ee248e048 | -2.8069 | -52.52365 | 2024-11-10 06:12:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c4a2a6ed-1e94-3637-844f-154124b4709f | -1.51884 | -52.20024 | 2024-11-10 06:12:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 38dec905-9915-36c8-8861-ee3d260ebc29 | -2.41914 | -51.95013 | 2024-11-10 06:12:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 5d482a22-68a8-380b-a56f-e5a21a9c3077 | -3.25273 | -50.28415 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| af5f1503-6536-3183-b67d-cb05da31d89f | -2.76234 | -49.36603 | 2024-11-10 06:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| fd8b0918-6673-3105-a2f1-e945e46711d8 | -3.14052 | -50.41893 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| ce9668fa-14da-3511-b740-b20915e393a0 | -1.4864 | -55.43577 | 2024-11-10 06:12:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 8b567d39-ff0d-3d9c-a0d4-554ddcf12df7 | -1.3974 | -52.36578 | 2024-11-10 06:12:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9bed4073-3358-3c3a-8168-ba61d7dc8753 | -2.80434 | -52.54126 | 2024-11-10 06:12:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 8edd02d9-c8b5-34d6-b9ef-0477cf3f32dd | -2.23362 | -53.77567 | 2024-11-10 06:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5e399064-26fb-3739-a869-ae75765a6bc8 | -2.57011 | -50.66442 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 1c1cff8b-b3d7-30c2-b9ec-e9de99265884 | -3.2384 | -50.27498 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 7cf299ec-326f-3eb4-88c5-2ac96307798b | -3.13901 | -50.45096 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c4574b55-8f09-3bb2-9397-81008fe81323 | -1.95239 | -51.09153 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| ac3a4fd2-1188-38cf-bb83-725ef8aefed0 | -1.50911 | -52.15559 | 2024-11-10 06:12:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a48a86a3-baaf-3274-af8a-adb2ada998e7 | -1.4696 | -55.64941 | 2024-11-10 06:12:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 23396ae7-0cfe-33bd-9cae-2734e129a41f | -2.08848 | -48.83027 | 2024-11-10 06:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 99b75817-dab7-361d-8476-523dff9195fa | -3.23799 | -50.28217 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 4ee7faa7-753a-3030-9b41-176229da7246 | -1.41446 | -54.76284 | 2024-11-10 06:12:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 09615fcc-83ac-3cd4-9466-2b56a1bb7430 | -2.93112 | -52.76428 | 2024-11-10 06:12:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 162f7c71-02d7-3c03-86e5-9ad4413dec83 | -1.15023 | -53.78226 | 2024-11-10 06:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 4a1eaed4-917e-30fe-9076-627150c89353 | -3.12213 | -50.44353 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f05c1bf5-1ece-35fa-9311-fabc965d2027 | -3.10018 | -49.41047 | 2024-11-10 06:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 08ceed64-8ae7-3046-a656-ee6ef43ec511 | -3.12016 | -50.14224 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 7eba182d-f4d2-3309-99db-a34b431ee3f8 | -1.34273 | -54.61909 | 2024-11-10 06:12:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 809de764-eb87-3dcb-87c3-0550e4e72892 | -3.22758 | -50.24557 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 0d829a16-0ba7-3721-a08f-d54d07b28190 | -2.92868 | -52.78133 | 2024-11-10 06:12:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 6be9c576-3c03-3653-bfe7-54f6238c6e65 | -1.17989 | -52.09105 | 2024-11-10 06:12:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 6ce77205-13e2-3caf-9c9e-9aef47078019 | -1.53107 | -52.202 | 2024-11-10 06:12:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 9941463c-e810-3157-bf68-9934a4240260 | -2.87847 | -51.46804 | 2024-11-10 06:12:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |


[Clique aqui para ver as próximas entradas](README122.md)
