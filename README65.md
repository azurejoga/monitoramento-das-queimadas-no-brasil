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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20ba43ec-2fed-3c9e-93c1-949ba7d5a69c | -1.71627 | -53.26539 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e6090d4-5c5d-3fd4-875c-94cf7f862347 | -5.0579 | -49.86141 | 2024-11-20 05:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07b2f82e-2a13-33d6-a374-484e41170a88 | -2.34761 | -54.75065 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a66a1cef-6364-3816-b33c-d74114299e1c | -1.9844 | -53.13662 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ecbff82-c700-3934-afeb-c5f3414da395 | -1.69908 | -52.35915 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c75572e8-f2e9-3f76-a06f-7526243992a3 | -2.44904 | -49.15201 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d844537-2462-3d94-8874-c160b6dd1c47 | -0.8306 | -52.83965 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b7ed07c-d020-3adc-9ec9-fc00da4f208c | -1.62951 | -52.67693 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb1a7682-98de-31ff-8099-8da9fc2e47f6 | -2.80963 | -54.02076 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fc0ac692-ca12-327a-9d0a-e97ee44e9b61 | -1.38103 | -51.55503 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c19d9a93-7bb8-3c6a-8caa-a75107c19e98 | -3.05529 | -54.41146 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 412bba7b-d7dd-331e-9748-342b6ff1f131 | -2.72532 | -49.3471 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c176e0e9-f1f9-330f-a51b-621e09ad13d1 | -3.48534 | -54.69755 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de7a339d-db99-3203-a0dc-5b7905e3ac66 | -4.57447 | -48.02273 | 2024-11-20 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e908817-1fb7-314c-b163-46a625b9ebd8 | -1.85491 | -47.83073 | 2024-11-20 05:14:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b629776-584f-37ef-bba0-981228237515 | -1.24213 | -51.78462 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 371aae3b-ee1f-3e97-a334-b953abc1b808 | -2.21574 | -48.77136 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ec87fb7-3d51-3b96-8ed0-72ea8c5cc32e | -1.25454 | -53.36834 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6288627b-9856-3625-bac2-66dfa32a9210 | -1.23291 | -51.78736 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f34a0b28-0b9f-3548-8778-1e83ba32cf9b | -1.73209 | -52.79482 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d179d18-f682-3a56-98f1-2b0c9a761379 | -2.90289 | -53.05958 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 532f9130-f181-303a-868d-dae20e2bc1da | -1.4106 | -53.47904 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc831402-d0e8-39eb-b381-59bab6b05ff2 | -3.11781 | -53.70073 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d5ac7a3-a871-333a-b572-48b488bce4cf | -0.18862 | -51.6337 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bed62e2-30b7-3cca-98b5-7991ecdb1c06 | -1.98837 | -53.13723 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bc5ac04-327d-3ffb-a6a8-e4b91b3a88b7 | -2.83386 | -54.01487 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a8b49a8-d649-3ea3-a00e-f29b8b118b69 | -1.19874 | -51.98244 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ad4a652-6719-30ae-838b-33be7560c41d | -1.44711 | -52.67213 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 916761b7-1d52-30df-936a-ed61656b85df | -2.79099 | -51.72106 | 2024-11-20 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a52030e7-199c-3edb-8f97-12bda29f2f0f | -0.83381 | -52.87199 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b0dbc6b-4094-3b42-9f47-0c29572aec3f | -0.14805 | -60.86987 | 2024-11-20 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13d6a171-0fe7-37fa-93f7-90e1485126c0 | -2.92501 | -53.07723 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 20db1c60-ae5a-3eb1-a4d8-d52c6a96a126 | -3.80636 | -47.8031 | 2024-11-20 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dcad68f9-469a-3b8d-8096-097f4f256424 | -2.72011 | -49.34636 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d48c39ca-a2ba-3348-8bad-3d2bb74c1337 | -1.13774 | -53.6667 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fc85453-2bab-3501-9e5b-bdfe63565a63 | -1.52036 | -55.48525 | 2024-11-20 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b9ec113-b632-3b4c-b6c1-54eea0fa5602 | -1.20518 | -51.78027 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06eb86c3-15af-3249-aae5-cdc06fbdf9eb | -3.08664 | -54.66594 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86befecf-dab0-3ad0-aedd-205fc349961b | -1.38545 | -52.5596 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e97b24a3-d3fd-344d-8d6f-df4b57207b5f | -2.45478 | -49.14965 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f896a95-22b2-36a5-8f26-5b8739377da6 | -2.05976 | -53.43233 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8ba6c73d-2931-367d-b684-ca4d6b6bfe69 | -3.47071 | -53.48871 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d675323c-156e-3d87-b60e-3cce65705dab | -0.93059 | -51.64517 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3e914e9-07f9-33f1-8cd0-7cac52d259cb | -3.60832 | -54.74982 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7f4e959-6764-3236-a978-a623c734fb8e | -2.18472 | -53.42874 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40d94f13-8d54-321e-b1c2-19f8d9c9ab3b | -0.24744 | -48.59054 | 2024-11-20 05:14:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bad7ee9e-1f54-3b4d-9cb1-ea204d15d52f | -5.37598 | -50.47465 | 2024-11-20 05:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c782d42-5042-3922-abaa-c9bcefae1b76 | -3.06466 | -53.28426 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccd36992-b864-3a15-bf2a-42f7d750a6b1 | -2.59592 | -54.00454 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4829df42-b426-3542-a5ec-f88ff3102ec8 | -1.73263 | -52.79127 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1abb2be-a585-3d11-82c0-f710afeb8fe8 | -3.31841 | -54.08834 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c982398-d475-34a0-b2bd-423d55f9c421 | -1.4436 | -52.66797 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 059f7b48-53ca-3f33-abde-7a1aeacc45f3 | -4.0737 | -50.03833 | 2024-11-20 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02e7387e-6fc7-3a69-8eea-a290dd8a2ce4 | -1.62849 | -52.62869 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b76e08a-4a73-34ea-93c5-effd9a25686d | -3.70714 | -53.75447 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 597f81e4-c2f5-3e6b-9a6a-d23a1e959cb0 | -1.59669 | -47.13972 | 2024-11-20 05:14:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dd316174-d4d1-3249-a47f-489f65df2256 | -3.04081 | -52.43691 | 2024-11-20 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc7e3d00-b964-3694-a7fa-5fb76e67966d | -1.19542 | -53.67073 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a6304242-5afc-3f70-8851-10533c8f74c7 | -2.22014 | -46.48378 | 2024-11-20 05:14:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49d2b280-1038-3c17-867f-473dc1d23014 | -2.87069 | -53.35037 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb8e251a-9907-38e3-aeb7-5896874780c3 | -1.63257 | -52.62931 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f31b053b-4dbd-395d-815b-b53fd1d20378 | -2.27647 | -53.6394 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb1e3230-3895-3f20-836b-e92ee1dbf4b1 | -3.61265 | -54.7461 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3c6602e-02fe-34be-baa7-77a326195ea3 | -1.79586 | -54.04237 | 2024-11-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2e953bc-1568-3ab9-8909-920947b0a0f1 | -1.96924 | -53.13807 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aadfc7fe-0141-3c93-853c-674c816a26f2 | -2.74106 | -51.72234 | 2024-11-20 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68dd5233-437c-3b6f-8f0c-1030eb16c4ea | -3.03905 | -49.47429 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25917bd8-bc54-3f1f-b9b2-f6e999b54403 | -4.07876 | -50.03911 | 2024-11-20 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4946ab7f-5103-3e6c-8f28-513a780e600e | -1.47416 | -52.5244 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f17b38c-089c-340b-b7e7-e3f93a054c6b | -0.96167 | -51.72919 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cfc4bbd6-6753-3409-9afa-e62eb495c54a | -2.95891 | -52.46451 | 2024-11-20 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94dc4386-61f0-38f9-b8e8-96640d2cf137 | -3.72541 | -47.37662 | 2024-11-20 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ad69bf7-59d3-3983-8a52-dfc6e3aa17bf | -1.30674 | -52.26321 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 538193d7-7ae6-3b4a-a207-99bf0d5cbc9f | -2.75076 | -45.70845 | 2024-11-20 05:14:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b2a849a-faea-3c53-a9ed-cd70a89ba5c4 | -3.20119 | -54.32419 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c9b4edb3-a88a-3a48-8607-b793f765e68c | -1.23721 | -51.78801 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0b64b25-bfa3-3577-8344-710309386a77 | -2.76619 | -54.05449 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d96aa9e-39f3-3f64-8d73-e47c620b6f16 | -1.19851 | -53.67581 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 543dbd46-8bbc-38af-b65f-4dc1418c8fb9 | -1.3276 | -52.40058 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 17717e6d-03eb-30e3-95bc-aa4a63659ebe | -3.81163 | -47.80801 | 2024-11-20 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a9ff89d0-a8b0-3370-9e52-c2254f6964d8 | -1.66356 | -52.80625 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b861ed5-cbc8-3b46-ba47-c87fc8f98c97 | -1.45173 | -52.66915 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fbb6c004-f4e2-3684-bf3b-ecfc1a007171 | -2.83457 | -54.01023 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a0eba83-3892-338b-995a-efb84ecb88a4 | -3.28216 | -53.82766 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f698c8d1-ccf2-37b8-bc25-a0b21206ca0e | -4.57505 | -48.01862 | 2024-11-20 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c27c534-c2e3-3eeb-a059-ac129e8a5364 | -4.45025 | -46.58281 | 2024-11-20 05:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 374d918f-847f-3377-92c2-8f28adec4a38 | -2.16463 | -51.96877 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3da20d9-e426-3162-9190-681c3ac73b53 | -1.51157 | -52.22734 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1050d07-2c39-3c58-9f07-ff85f8235ff2 | -2.80494 | -51.80664 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67f320a8-92fd-3c50-93f8-6c9913cd41f7 | -4.44795 | -46.58505 | 2024-11-20 05:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 31f79a80-1ec4-3d70-beb8-0fae5a049664 | -1.2385 | -51.75077 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a3eaa9e9-aade-3eb0-a594-7df7e30644a6 | -1.19934 | -51.9785 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f32f4079-e1f7-3d19-8553-fb44cd9ff80a | -2.74396 | -51.82351 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 71e599dd-2b49-36b3-b479-259715018a3d | -3.42581 | -53.28606 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09127339-3f45-3305-8875-5f61d10c8826 | -1.19923 | -53.67123 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 57567ba0-1400-39f0-bcc4-430a22f6f8b3 | -3.57632 | -54.54907 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7feeca9-8a09-32fd-a358-a6a6f0cca717 | -4.38608 | -47.77724 | 2024-11-20 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4925e2d9-8ea8-3fbc-afa6-27b0700d1f34 | -3.02253 | -51.52709 | 2024-11-20 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0f574c94-b668-33a2-8950-2db873b7ba2f | -2.59754 | -54.0166 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d03fe527-49e6-3886-9fcc-ff5216c2ccc6 | -1.36638 | -55.37647 | 2024-11-20 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README66.md)
