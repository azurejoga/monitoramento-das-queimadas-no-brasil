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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da887ba1-1178-36e1-ab4a-a194a6ab9ccc | -26.17471 | -51.73515 | 2025-09-21 05:01:00 | NOAA-20 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 5fa8d456-997a-3948-b1c0-69e8e55465a6 | -20.50166 | -56.87706 | 2025-09-21 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35298f9f-675c-3975-ac84-f97fb21c4231 | -20.54218 | -56.14341 | 2025-09-21 05:01:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aece0873-2617-387c-aa03-75e313fde314 | -23.14204 | -47.63085 | 2025-09-21 05:01:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2c8a1e66-b778-38b4-a6fc-43893be44274 | -22.95268 | -45.41265 | 2025-09-21 05:01:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7d9f64e3-7607-30a4-852b-0b2908d220a3 | -20.60715 | -56.72403 | 2025-09-21 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07414166-e4de-3094-bb00-d2a29c5597bd | -20.59935 | -56.73032 | 2025-09-21 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 742dd6b9-153a-3687-a5cd-67510804187d | -20.60325 | -56.72719 | 2025-09-21 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0a9e3d9-8c86-342f-966e-31cb64e7a8cd | -20.79748 | -56.92017 | 2025-09-21 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b93ddbe-166c-3ba4-8776-228519ab35a8 | -20.60773 | -56.72031 | 2025-09-21 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5ee5586-6cf2-3cb4-bded-2ed68c9f6004 | -22.46536 | -48.2131 | 2025-09-21 05:01:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 73c099d7-87fa-3ced-87ff-5f5c10cc33e6 | -23.14798 | -47.62752 | 2025-09-21 05:01:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 837005f7-15d2-3f2f-a033-b8e35cbc5b7b | -20.99384 | -54.77075 | 2025-09-21 05:01:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e26e54a8-4446-3cf8-8bcc-7b072c7ca846 | -28.28144 | -50.35314 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 51d414e6-99a5-3681-b1af-4f1006daf79a | -26.17024 | -51.73451 | 2025-09-21 05:01:00 | NOAA-20 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| fe372299-7176-36ef-8b89-77cdcc9c0bb9 | -23.01753 | -45.43296 | 2025-09-21 05:01:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 472478d2-32ef-392b-b049-4e10c7b69110 | -23.15564 | -46.65036 | 2025-09-21 05:01:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0ab08d42-41ca-34c3-8e0a-76d828492dad | -23.1424 | -47.62674 | 2025-09-21 05:01:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1b3edf4e-6b48-3293-abd5-f1a1a5d12764 | -22.47573 | -48.21775 | 2025-09-21 05:01:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f16f09e-2bd8-3423-8471-04c75e9f19a4 | -28.28467 | -50.37264 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1455c811-359d-3a7a-b344-2cedc7fabba7 | -22.70519 | -51.55706 | 2025-09-21 05:01:00 | NOAA-20 | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6149e06c-0a52-3f8b-a421-c0fdca33e732 | -28.28642 | -50.35389 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 97fac53f-09d4-3040-9ffd-37ce73f5f095 | -21.31918 | -51.66568 | 2025-09-21 05:01:00 | NOAA-20 | NOVA GUATAPORANGA | SÃO PAULO | Brasil | 3533106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 49244eda-2bf6-305f-952d-fd3d69cbcbab | -28.28583 | -50.36023 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 2e24e0e3-2923-3d27-9924-e38384943106 | -22.4647 | -48.22009 | 2025-09-21 05:01:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a87487d-1535-3cf5-b2bb-9d639ee89e46 | -22.25239 | -55.99452 | 2025-09-21 05:01:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3797099f-a3b0-30c6-82f0-c865ebb99ac3 | -21.98902 | -46.86778 | 2025-09-21 05:01:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a820a32-26bc-32d2-9935-dc6f985df26c | -25.15221 | -51.97023 | 2025-09-21 05:01:00 | NOAA-20 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e6cf6d79-ec56-3d21-91ec-f7e2e1a80fec | -28.28475 | -50.37364 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 291ade68-bb90-34c8-91cb-fb7e43417769 | -26.17522 | -51.73037 | 2025-09-21 05:01:00 | NOAA-20 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 0557d41e-53a3-32d8-a703-a83d6067f150 | -23.15016 | -47.62301 | 2025-09-21 05:01:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 51c8878c-beec-387a-a1b2-9e04da2206cf | -22.47606 | -48.21424 | 2025-09-21 05:01:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d05dd9a2-c1a9-3abf-83bd-ce015fd861e3 | -24.75587 | -48.81686 | 2025-09-21 05:01:00 | NOAA-20 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6ddf27d3-b061-376b-90f4-9e1f6449bad4 | -22.46973 | -48.22394 | 2025-09-21 05:01:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1236af7d-acfa-3263-90b8-f62d837644f2 | -28.29029 | -50.36801 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 676bbf66-86bb-3631-84f7-2cb8a2a4807b | -28.28139 | -50.3541 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 09a91aee-2d5c-3594-b265-abe2c5244791 | -22.78064 | -55.36699 | 2025-09-21 05:01:00 | NOAA-20 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9750e05f-ef9e-3934-b164-6f85d2150999 | -28.28966 | -50.37329 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 21cd6b96-9a31-3607-a2c0-e7cae3d1f0b7 | -22.47104 | -48.21017 | 2025-09-21 05:01:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93250caf-d398-35a3-8e7c-bc147c9e9677 | -24.75534 | -48.82269 | 2025-09-21 05:01:00 | NOAA-20 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3c5f3fe3-5e71-37dc-aed3-aa6708c3c642 | -22.62704 | -48.2534 | 2025-09-21 05:01:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37398029-3ac7-3877-b4e1-b108fa48fcd4 | -20.55944 | -54.65614 | 2025-09-21 05:01:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df85f8d9-e103-35f9-b754-51047084386a | -22.22556 | -56.01038 | 2025-09-21 05:01:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b64cdbf-5a35-3868-bc28-8622b63f0dbd | -20.6044 | -56.71973 | 2025-09-21 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a952a4a9-3fca-3da8-bc41-90452d07efc8 | -20.54105 | -56.15101 | 2025-09-21 05:01:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26312373-7d43-3fa1-9fa3-05b46125e204 | -22.46503 | -48.21658 | 2025-09-21 05:01:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46e3ccb2-3001-3905-aaa0-a4626f383a2c | -22.27348 | -56.01751 | 2025-09-21 05:01:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 17378540-9122-3067-b14b-51fb4a9ab6f1 | -21.98864 | -46.87191 | 2025-09-21 05:01:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91b9a183-9639-3348-956d-7714b638dced | -23.24656 | -50.85734 | 2025-09-21 05:01:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 68078b3d-12a0-3191-83c5-b7b4aaaf1043 | -23.72867 | -54.93719 | 2025-09-21 05:01:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b9116864-69fb-3279-9a5e-d99bb6b2d2d8 | -23.14275 | -47.62272 | 2025-09-21 05:01:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2fd8a6e5-3604-3f80-acd8-3625f770edef | -23.14834 | -47.62344 | 2025-09-21 05:01:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7faaebb1-d6a1-33ec-a1e9-0b625a7200ac | -24.7501 | -48.82165 | 2025-09-21 05:01:00 | NOAA-20 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b353eff9-994f-379f-91f1-e3d2778bf97b | -20.60658 | -56.72776 | 2025-09-21 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86337aa4-ddb8-37d8-9fc4-462c64ce03f9 | -23.73289 | -54.93323 | 2025-09-21 05:01:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 32323685-e5d4-38fe-80a7-bfe848df7a5c | -28.28638 | -50.35485 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 58cb76a7-e348-3dfd-8022-211ab690b694 | -20.53825 | -56.14664 | 2025-09-21 05:01:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c331b5c8-471d-3420-af75-090cb0b207d6 | -20.54835 | -56.14836 | 2025-09-21 05:01:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80ae079e-7a79-3d66-986e-a9991a1f201a | -22.29984 | -48.50136 | 2025-09-21 05:01:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0a44e578-0715-3233-8079-d391cf9ab3a3 | -23.21729 | -46.4196 | 2025-09-21 05:01:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 167f27b0-9861-3e36-acba-f57e894005be | -23.54816 | -50.861 | 2025-09-21 05:01:00 | NOAA-20 | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cef7424a-0ec5-3ab5-bc47-d9740da2c217 | -20.54498 | -56.14779 | 2025-09-21 05:01:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4ad79e4-ab24-3db4-ac57-99cc8b5007dd | -22.47006 | -48.22047 | 2025-09-21 05:01:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a83c4c10-705f-3944-b2aa-916446ffcf43 | -22.47039 | -48.217 | 2025-09-21 05:01:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9716d0bf-3ee1-3305-a03b-38bfe6e3db87 | -28.28583 | -50.36119 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c1f06dc4-1db0-3cab-8305-f030a2759876 | -22.28118 | -54.16481 | 2025-09-21 05:01:00 | NOAA-20 | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1ded8147-e9b5-3ffc-a61f-6665f102634a | -24.75615 | -48.81379 | 2025-09-21 05:01:00 | NOAA-20 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f4b0a3d8-9ff3-307c-aff5-9552d06a1752 | -22.26267 | -55.99545 | 2025-09-21 05:01:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 143b1704-0354-3edb-aad5-0148a01da3e0 | -23.2423 | -50.85854 | 2025-09-21 05:01:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a5f6a2b1-c4c0-3bf5-9188-5ec010dad9fe | -23.21688 | -46.4244 | 2025-09-21 05:01:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 919b826c-5205-3c35-9bfe-fe3c4d417cb4 | -22.46568 | -48.20969 | 2025-09-21 05:01:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 818cc57b-333a-3a6d-a372-f54294b92338 | -20.53432 | -56.14988 | 2025-09-21 05:01:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7816542-9d3d-3614-b878-cd6169164be4 | -22.70037 | -51.56076 | 2025-09-21 05:01:00 | NOAA-20 | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 62e12c99-9f2c-3bd1-8502-1d17030d6fda | -28.29025 | -50.36705 | 2025-09-21 05:01:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 634da747-dd6f-3f97-8597-b7e4075448e9 | -22.63236 | -48.25423 | 2025-09-21 05:01:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbe0222e-8a87-3e9c-a8e5-347f2a38e7e5 | -23.24202 | -50.85666 | 2025-09-21 05:01:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f4289bde-de71-35f3-915e-ccbc08c03cb6 | -23.50861 | -46.97867 | 2025-09-21 05:01:00 | NOAA-20 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 31bdeade-fc3b-3e86-9259-e9840ee2688d | -25.05544 | -52.19266 | 2025-09-21 05:01:00 | NOAA-20 | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 931716ff-717e-36fb-b27e-a61d9ff55e95 | -20.85368 | -55.16727 | 2025-09-21 05:01:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57e85b33-5aea-38a8-ba65-6cafecaed4da | -23.01791 | -45.42789 | 2025-09-21 05:01:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1d22cd84-a2d9-33c4-baf6-ad8a40b54aa9 | -23.72928 | -54.93264 | 2025-09-21 05:01:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 62471dbb-5d08-38f5-9f90-95e671b6a8ef | -20.53711 | -56.15424 | 2025-09-21 05:01:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aec70570-c07a-38e8-9bb2-d8b6ffc64b4f | -20.53095 | -56.14932 | 2025-09-21 05:01:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea621984-6524-3dae-a54d-baaa1b62bdaa | -28.91103 | -56.29894 | 2025-09-21 05:04:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| d1bd6a80-4365-3ce9-a153-f42c36ce6557 | -7.71501 | -44.45471 | 2025-09-21 05:21:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5c6dd0f3-6c60-3a34-a770-de008a3f69f3 | -7.94431 | -44.09857 | 2025-09-21 05:21:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6b141f6b-d4c9-3611-bf4b-a52fe6f42f3c | -7.71798 | -44.46063 | 2025-09-21 05:21:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 50c4b8f0-e249-3d9a-96f2-8b2dae290125 | -5.568 | -42.14922 | 2025-09-21 05:21:00 | AQUA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 1886ce62-a67f-3c6b-9303-1dec50482f8d | -5.57872 | -42.15097 | 2025-09-21 05:21:00 | AQUA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 3f58d806-3ce7-3cfd-88e7-d956ec4e649c | -5.58081 | -42.13752 | 2025-09-21 05:21:00 | AQUA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| a4a607cb-6aa8-358b-8d19-6689d7037676 | -7.9203 | -44.09466 | 2025-09-21 05:21:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 9aff0313-2c38-3754-84ee-0e9d1e6d70a2 | -5.67451 | -41.39925 | 2025-09-21 05:21:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e8733d5c-de2c-328e-bc2f-bdb756c96f36 | -6.24544 | -45.31844 | 2025-09-21 05:21:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| de3cc6ae-a0f4-3bae-94c1-6a6246c8f693 | -7.91748 | -44.11184 | 2025-09-21 05:21:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b71f5904-24c2-3442-8318-e74faf631061 | -5.51954 | -43.86729 | 2025-09-21 05:21:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| b130aa38-aece-34b5-a6f5-cf3877672962 | -5.55725 | -42.14759 | 2025-09-21 05:21:00 | AQUA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 1ac37a5c-ea49-386c-aa93-efa6735c8985 | -6.29841 | -42.36138 | 2025-09-21 05:21:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 8357a952-fdc4-3f84-868c-0b646a033a83 | -5.67638 | -41.3873 | 2025-09-21 05:21:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 7b1d5ce8-4512-3d97-94e4-a9b4c0679e57 | -7.9323 | -44.09663 | 2025-09-21 05:21:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| d2d70300-ca24-3bd2-ad2d-abc7610ce22c | -5.52089 | -43.87478 | 2025-09-21 05:21:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |


[Clique aqui para ver as próximas entradas](README43.md)
