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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e01e48d-a68a-33af-8a4c-6e3339fc25d2 | -1.78697 | -52.75319 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5029cea9-aace-3cfe-ad92-371ce073143e | -3.07543 | -53.9222 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 345afa45-2b6d-36a1-b219-4a10752d35b7 | -3.24069 | -53.87621 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79d3e94a-3a7e-39de-a3e5-7f0f85998bfa | -3.34081 | -51.20741 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bc85d78-e223-39de-ba1c-eb566ac6d05e | -3.27145 | -50.20911 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0522e14-c9ba-3484-a7d3-93d9b73a477e | -3.10074 | -53.22789 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0e6a61d-4a85-3359-9c0c-fcfeb0f4a9ac | -2.75667 | -55.33542 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adfb6a96-df68-3bfd-9961-5af36472d1b0 | -2.78811 | -55.36707 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5b204ab-8004-3c02-97d9-3566428d9285 | -2.82102 | -53.05392 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58196056-d3b0-3fc8-9d82-837408e2529b | -9.03066 | -63.52523 | 2024-12-03 05:25:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77e395e8-4f15-3241-931f-5851fdd840b8 | -3.09695 | -54.29546 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d73acff0-b058-3575-af28-0b9ca14225e5 | -1.7321 | -52.61709 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72e0ae8f-88b0-3a93-92da-b874fa126d56 | -3.1095 | -53.75574 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b9c078e-4129-39e5-9489-090e614bccb8 | -2.81691 | -53.05008 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4169874c-c241-3b18-94e6-b306d2ec826a | -2.79811 | -53.05035 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9c45bcd-a33e-3cf3-a34c-4a625c565678 | -2.44396 | -54.00774 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47bfc6bd-319a-309b-af27-9af025ec308d | -2.88766 | -54.16042 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0749f9d-1b04-3b52-8a7a-a67f75b88405 | -1.42833 | -55.30252 | 2024-12-03 05:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10a63c52-e783-3162-bed7-bd7c8cbbfb4a | -3.06856 | -54.0551 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b64cd54e-40e2-3bee-8dc1-30ccfa06d723 | -1.38697 | -53.55636 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ce42663-791f-3164-b40d-da0e93fef440 | -9.0232 | -63.53228 | 2024-12-03 05:25:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 439f4de0-88c1-38e6-a8b2-059af1e9b3f3 | -3.2548 | -53.65565 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a04195c4-9158-367e-9cc2-888f48d4c1ad | -2.82174 | -53.04922 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 620654da-c894-3ce1-a200-27cf962c9307 | -2.98894 | -53.34993 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d63c248c-59b3-3403-9603-daf4e8dc7ab6 | -2.98611 | -53.88512 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a0eb2da-f717-3cc8-aa2e-4dbb18f05d1c | -3.08796 | -53.38002 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 86a504ba-6c72-3ed5-a320-8e934ca9083f | -2.813 | -53.04465 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32236077-4338-3d90-bd0c-9befbc74163a | -2.82149 | -53.05079 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 13e6b128-f4f8-3be1-9b73-988ecc79b066 | -1.6558 | -52.74961 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d42a8abb-d798-3334-9c47-9e3d06dd22ac | -3.10005 | -53.23263 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eaf3f6c3-4426-32fd-abbf-f2a7d0fa7696 | -13.10929 | -58.04319 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04c2a3da-b6d9-3e01-9d24-08661fca0a2f | -2.3596 | -53.92883 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2dce294a-f5fa-3dac-9ec0-9216dc22a0d6 | -2.87958 | -54.12676 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f14c9c2-03e8-3e8f-b735-de7fd58900a8 | -2.62756 | -57.70294 | 2024-12-03 05:25:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 873e36e5-6ac7-3f6c-9ce4-897e13eb79ff | -2.68541 | -46.60965 | 2024-12-03 05:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 305c0169-247d-30ff-9623-d5bfe51b8ab2 | -2.87987 | -54.01743 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5c78668-e110-387a-9cf0-b86a5d0ee499 | -1.52138 | -60.32662 | 2024-12-03 05:25:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 180db1de-ec92-366d-93a8-75ff2eac1d46 | -2.74447 | -54.13659 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af8a0bb7-c478-3784-a490-8326d2fdb863 | -1.5349 | -52.6806 | 2024-12-03 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 530555c4-a707-3e63-85ef-ba0a5053b951 | -2.80179 | -53.0573 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa61154b-4864-3392-add8-17d6992c536d | -2.441 | -53.61972 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b62f4a8-9125-3691-bec0-db0d7d254ed4 | -2.34125 | -53.79921 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2afd35e-7706-3cbc-a828-8fefcfcff454 | -1.64916 | -53.82166 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14fbb43f-49c2-3153-918f-4f5d4511af92 | -2.81622 | -53.05479 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 092cd25a-de3c-3f6e-b446-349a0fb5a4f3 | -3.09986 | -54.05161 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 979407df-a556-31c4-886e-be27dc441266 | -1.93099 | -53.4462 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b98b29f7-f369-3dfd-9edb-9f6a319b594a | -3.26002 | -53.83574 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ad35152-92c3-3d71-a896-9eeb90a6ef8c | -3.34467 | -51.21773 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0978752-68ee-3ee0-b5b0-a057aa148591 | -3.37581 | -50.6988 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d6999989-677d-3d21-a12c-1ff21fb94a43 | -3.08861 | -53.37555 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2f33cca1-cb38-30b8-8251-6e138c5daf5e | -1.95041 | -53.34758 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 598a83ba-08f3-3a7c-a4d4-9fa29b22936c | -3.41923 | -53.99915 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5834bdc7-b21e-3832-b8c5-436a0a8b7c2e | -1.9026 | -52.85631 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d02360d5-90b7-3f19-b352-ae70a507f2d7 | -9.14782 | -63.91156 | 2024-12-03 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90356ea4-0e94-3187-a33d-6e845efdf14e | -2.66493 | -54.08656 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f59d073-5188-3042-bdc6-cff3fc81176a | -12.71142 | -58.20528 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 811659bf-242b-31a7-95aa-54bf06f151e6 | -3.25734 | -53.66933 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9be24753-ee6b-3c6d-a816-b3dd68cc9722 | -2.56879 | -53.39528 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a83d06f0-ed80-34b8-995f-58a5830ca50b | -2.46661 | -53.62831 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1f26f8a-47bb-33e6-ab15-406bafc1e799 | -3.10137 | -53.75012 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14815bbd-b9f1-36eb-9469-c16df8c92d22 | -1.75091 | -52.64971 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5768480e-4511-3ce7-8f79-08902829cd92 | -3.0841 | -53.37491 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0a05bf56-f198-396c-afa1-9dc84d81d0af | -2.78424 | -55.36504 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63211424-0493-39b5-95ab-8928591db96b | -3.1207 | -53.98727 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a444cb89-cb7b-3e8c-b93a-f8b08314f7f8 | -3.47562 | -47.68145 | 2024-12-03 05:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75494cb7-0972-3c48-b24d-a5f1892a8de0 | -3.02312 | -54.03573 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c04c4b6-6df4-3faa-91c2-8dc7f22c57ea | -3.47196 | -49.92791 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 790dd4f6-cf19-3b6c-b903-80815f6942e8 | -4.16621 | -48.18976 | 2024-12-03 05:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0d3d2515-795c-3a27-b620-ac1fb3d020e0 | -2.84434 | -54.10655 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e20d44a6-2f3d-32fd-ad4b-6b983ebfae09 | -3.09115 | -53.2536 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a78f93c5-8aee-3167-9f63-cb8e8baeb7d0 | -12.70634 | -58.2141 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 766aa2e2-24d5-3b2b-8f3d-37294f2dbe0a | -4.16468 | -48.20081 | 2024-12-03 05:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 83f66f4a-acf2-3999-b3d4-9bd7c4636226 | -1.7559 | -52.8016 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0f032b7-9b20-302b-902d-cddf55256d3e | -3.12009 | -53.99137 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5cd198a-b514-39d6-b557-02036ced5c7d | -2.86152 | -53.99374 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2db4df2-d9f9-310a-9809-801506bd9e9f | -3.26774 | -53.6336 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66a208b8-c4d5-35cf-bdb9-0215d59eadc2 | -1.94926 | -53.3251 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60f181be-455c-3e80-9a13-c2f81dc320bc | -2.19717 | -53.77413 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5502bddb-a8da-3bba-8d7c-2c4507e9fafb | -1.30579 | -52.85609 | 2024-12-03 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10ee9b6f-a4fb-3cd0-b6b4-454b3f0ae97f | -1.70102 | -52.6023 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46a17996-27d9-326d-b38f-16006fe68a87 | -3.21073 | -53.11604 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89ec8822-d4fe-3540-a07f-b44191bab1c0 | -13.11213 | -58.04141 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dc3d7543-6ccf-35ca-a8b1-6ecba799f6f4 | -3.24935 | -53.63523 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c224de6b-ae76-39f3-a157-b4a63b83159f | -1.10571 | -54.14421 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac0f7029-138e-3c17-b239-fdf098c351a6 | -2.82609 | -52.58006 | 2024-12-03 05:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9bbe8976-e449-376f-b0d4-86f67d90a37d | -3.11578 | -53.99071 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3462c23f-0b42-381a-a15d-a8172710d759 | -2.88909 | -54.01467 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b19d4d01-76f9-3b97-bd24-2c91bb5b0381 | -3.26841 | -53.62925 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 490fb115-3da3-36d4-8810-472aec9f4f13 | -1.27951 | -54.55357 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e16ec307-ce57-36fa-a983-064e2689ddb5 | -3.2293 | -51.7312 | 2024-12-03 05:25:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 843b0fc3-0ff9-34c4-b8f0-867faad43d0c | -3.36551 | -54.06207 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acdbc1fc-531b-3fc3-b1ed-3de3ca0ef234 | -12.70322 | -58.20892 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0512b96c-3d8a-3b5d-bb84-d90173232db0 | -3.28854 | -50.79232 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2afe66a6-c00b-3353-ae1c-e81429fc0a1e | -12.57116 | -57.80072 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1643b838-db11-3ba8-a2a7-3be723bed465 | -3.34514 | -51.21454 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f581d100-9967-3aed-8b05-4e90a643acff | -2.64203 | -54.21262 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90d0f0e2-ac9f-3efd-8bef-6a885f2084c7 | -2.37252 | -53.85426 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 913580ef-f7e7-304f-8acb-e1febe1ddca9 | -2.77324 | -55.35828 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42218759-53a7-36cf-9e73-4ae383b9e74e | -1.65791 | -53.22847 | 2024-12-03 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c65e3c3-0153-3ef2-ad17-59e890c8ed4c | -2.20887 | -53.78447 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README63.md)
