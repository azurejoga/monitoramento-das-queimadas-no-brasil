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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98c2cda3-3dfb-3dd0-a388-bd910b3736ef | -4.41162 | -55.39922 | 2024-11-02 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 093bdda8-1f57-364c-8cd1-a56ba742134e | -4.27355 | -55.1474 | 2024-11-02 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed3bb2a4-d9b0-3dec-9332-b14ddcbcfce0 | -4.27271 | -55.1533 | 2024-11-02 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c91350dd-e6d3-3420-a8f9-9059a2a220d5 | -3.88085 | -54.14475 | 2024-11-02 05:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ead17e04-abfa-310f-b50f-3604da775b11 | -3.87371 | -54.14371 | 2024-11-02 05:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08a537e8-af60-3155-8fbe-2ed403f08f08 | -0.75975 | -62.90299 | 2024-11-02 05:53:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d712bb5f-8530-35ac-add4-41696fea9522 | -0.7559 | -62.90239 | 2024-11-02 05:53:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1004435d-1b15-3a94-9f26-3bb42ce9a8e5 | -0.7528 | -62.89701 | 2024-11-02 05:53:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d4ca0e1-b6b3-3d47-bcda-bec73a64fa33 | 0.39127 | -62.6849 | 2024-11-02 05:53:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94482ab2-9734-3a51-8a0c-dbdfdc1d756e | -1.07189 | -62.65132 | 2024-11-02 05:53:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9abefb4d-fc2f-334e-8512-65b5e2fd3ea8 | -1.00842 | -62.80151 | 2024-11-02 05:53:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29b6e13e-a080-3aa1-a32d-01ce92f6afad | -10.90021 | -69.4644 | 2024-11-02 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e0c908f-b21d-3f64-8980-a99ffe46b334 | -10.8969 | -69.46387 | 2024-11-02 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ba28402-18f1-36ad-b3d3-d4e9730ceaf0 | -10.88264 | -69.68367 | 2024-11-02 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7cb568c-e906-33a3-9c46-b7e909334893 | -10.81815 | -69.77005 | 2024-11-02 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d35bb4d-5d17-38bb-b510-270b213234c5 | -10.77407 | -69.33642 | 2024-11-02 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8e5af5a-e40a-3822-88b0-48fc1ffe2eb6 | -9.26016 | -71.87264 | 2024-11-02 05:53:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb2850ad-c4da-3def-a6f8-d26c25b500bc | -8.11103 | -71.31981 | 2024-11-02 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4726536-1d6f-32f3-ae41-0d01f5f6caa8 | -8.10755 | -71.31925 | 2024-11-02 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27810745-bc3c-3f37-9d0b-446da8b8263f | -8.07794 | -70.87622 | 2024-11-02 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 835dee0e-3f56-3e6b-86a4-73e30a6d4fc3 | -8.03381 | -71.32332 | 2024-11-02 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 606fa311-82c4-30d6-9e60-d0e5dbda32e6 | -8.03318 | -71.32721 | 2024-11-02 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89eb8ddf-b179-3a2e-ac04-663ab991d4ba | -8.03032 | -71.32275 | 2024-11-02 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a3b4122-1e84-3654-a97b-64fe22a0fdc3 | -8.02969 | -71.32664 | 2024-11-02 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2037f7b-0dd5-3f0a-9d5c-feb257bc4b9a | -8.01978 | -70.73725 | 2024-11-02 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a4c85c9-df5c-3aff-8ca4-6d0e3e3de9bc | -7.84828 | -72.7467 | 2024-11-02 05:53:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ce7a2b2-b378-3a4a-9340-34f8f2a458f5 | -7.34309 | -72.74818 | 2024-11-02 05:53:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b2c5189-4e7b-3a9d-965b-ca08a3c45d48 | -7.34232 | -72.75281 | 2024-11-02 05:53:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d475082-689b-3ae2-a9aa-62665bf34bf9 | -7.19127 | -72.60895 | 2024-11-02 05:53:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f770cdc-c15c-3bd2-be83-a856409861ec | -1.6187 | -47.2231 | 2024-11-02 05:55:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| f7bac7be-6322-3b6e-a7d0-c3dfc5924862 | -1.6002 | -47.2234 | 2024-11-02 05:55:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 5a7c27a5-f6c8-33ea-801f-b88a7b1cbd59 | -2.2663 | -53.7422 | 2024-11-02 05:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 65d6210c-f4e3-334f-8643-bcafc5adef5f | -3.0727 | -45.1179 | 2024-11-02 05:55:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 3dd352f2-53f3-37d5-a7f8-9ae07b6b5f03 | -3.0726 | -45.1405 | 2024-11-02 05:55:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 820c1209-51eb-3f94-9aca-f56a8128ed9b | -3.3878 | -45.3307 | 2024-11-02 05:55:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 6a0080f6-4a9c-311f-a176-88ff83bc0ee2 | -3.9474 | -48.3451 | 2024-11-02 05:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 48cda776-1bb3-3b9d-aaa7-d8f87a37f1a8 | -3.9473 | -48.3666 | 2024-11-02 05:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| aec63148-59e1-385d-a1ad-96be79751547 | -4.7185 | -49.5933 | 2024-11-02 05:55:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| f448cc4d-53b5-36cf-9240-3ce2f363637c | -4.7184 | -49.6145 | 2024-11-02 05:55:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 3ef41250-4cf2-3944-bb77-d03d4e7f7afa | -1.6002 | -47.2234 | 2024-11-02 06:05:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| d7579322-9ef1-37ab-83a4-5c0af92ab519 | -3.0726 | -45.1405 | 2024-11-02 06:05:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 07850652-162b-3260-99a1-789a2410b8c6 | -3.2047 | -53.4179 | 2024-11-02 06:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 570e7bbd-3666-3721-bcd5-fbbf84ff1ada | -3.3878 | -45.3307 | 2024-11-02 06:05:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 32b09964-6966-3105-871c-1c841f4b8918 | -3.2599 | -53.3962 | 2024-11-02 06:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 7c303b30-2946-3713-98a8-bfbf1f9b985e | -3.2599 | -53.4164 | 2024-11-02 06:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 0a6487be-8829-3f03-a355-ef92dc98ff81 | -3.2415 | -53.4169 | 2024-11-02 06:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e4416ddc-546e-38aa-b115-a491339d3fb4 | -3.2231 | -53.3972 | 2024-11-02 06:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 9f2cef36-b9a8-3ecb-a92d-46e83d0a8fd5 | -3.7701 | -43.5554 | 2024-11-02 06:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 8cab50a6-1418-3a7f-9ef3-9bdfe70e7e59 | -3.9473 | -48.3666 | 2024-11-02 06:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 38c06147-8c83-3fdf-aaf0-6508e8248475 | -3.9474 | -48.3451 | 2024-11-02 06:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| c71b3d95-94ef-3e38-944d-73ac610df608 | -4.7184 | -49.6145 | 2024-11-02 06:05:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d831f504-94a9-3492-af75-b5ff3bd5598a | -1.6002 | -47.2234 | 2024-11-02 06:15:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| ffc56d20-4c5a-3a70-a8a7-c5cd27e96f6a | -2.2663 | -53.7422 | 2024-11-02 06:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 8738eb0a-46eb-3bac-abfc-8cfd7f7fe5bb | -3.0734 | -54.167 | 2024-11-02 06:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 7fde5065-ee62-379a-8697-153dd015fecc | -3.1098 | -54.2665 | 2024-11-02 06:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| da6f8453-cfe7-37e8-a360-a2053f8ea1fd | -3.2047 | -53.4179 | 2024-11-02 06:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 8c5a5319-f797-3ecc-8d41-c59c4522225b | -3.2231 | -53.4174 | 2024-11-02 06:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2c335b11-f9d5-3717-a528-640b61028ddf | -3.2415 | -53.4169 | 2024-11-02 06:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 1358a28f-cff6-32d9-8fd8-b3326639e8bf | -3.2599 | -53.4164 | 2024-11-02 06:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 7f65b7e6-2df2-3801-b08e-fb1d5a692457 | -3.3877 | -45.3532 | 2024-11-02 06:15:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 8a38a5ae-b31b-3cfa-a9ee-a27919eb7260 | -3.3878 | -45.3307 | 2024-11-02 06:15:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 103.3 |
| f78ba1e4-a6dc-3ede-b824-4747f166f59e | -3.4064 | -45.33 | 2024-11-02 06:15:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 0966ba24-6089-38d4-801f-269e80d183d0 | -3.2231 | -53.3972 | 2024-11-02 06:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 78c36fc0-80ac-32b1-9b03-1218242e1a9b | -3.7701 | -43.5554 | 2024-11-02 06:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 9a6d069c-f631-3493-ad6f-267e71b38661 | -3.9473 | -48.3666 | 2024-11-02 06:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| ffd4e12a-a1cc-3e7a-8ff4-9315963e6aa5 | -3.9474 | -48.3451 | 2024-11-02 06:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| a6b0c24c-6158-300e-9e78-1e76baf33dcb | -3.0734 | -54.167 | 2024-11-02 06:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 04e317f5-8412-30c7-8989-735f9ec6fc2b | -3.1281 | -54.266 | 2024-11-02 06:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 27324154-c1da-396a-b7fa-3183ad38daa9 | -3.2047 | -53.4179 | 2024-11-02 06:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 2f348912-ab37-366a-978f-02886fafd621 | -3.3878 | -45.3307 | 2024-11-02 06:25:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| fd54457c-bc8d-30c5-afdd-9eab334f11a7 | -3.2231 | -53.3972 | 2024-11-02 06:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 36c623e4-de06-3f83-9eee-2b1163664c71 | -3.2415 | -53.4169 | 2024-11-02 06:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 9e5a2e44-013c-3ff9-9594-0c9d84b70ed4 | -3.2599 | -53.4164 | 2024-11-02 06:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 14479959-a667-3009-b51b-4c37d69807c1 | -3.2047 | -53.4179 | 2024-11-02 06:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 55380495-3ad1-337c-b618-16c095eefea8 | -3.1281 | -54.266 | 2024-11-02 06:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 5adb3230-d861-3fd5-8920-7c1a109ed3f7 | -3.0734 | -54.167 | 2024-11-02 06:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| c3b97805-bf32-3626-879f-54c59bde00d3 | -3.2231 | -53.3972 | 2024-11-02 06:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 7382a458-8a99-3168-8b1b-21496c687f04 | -3.2415 | -53.4169 | 2024-11-02 06:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 8673ffe8-93d7-33f1-aad8-95311344310b | -3.2599 | -53.4164 | 2024-11-02 06:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 3702cec6-fd56-337c-9bbc-9bc677344f31 | -8.0335 | -71.32369 | 2024-11-02 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 99d4495a-32b8-35b6-9ad2-a70a769d99d1 | -8.03297 | -71.32767 | 2024-11-02 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 282bf1c1-55c7-3ea1-81d6-606f822dc13b | -7.34477 | -72.74792 | 2024-11-02 06:46:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10d25c1d-a2cf-36d3-9afe-21dce731df73 | -7.34436 | -72.751 | 2024-11-02 06:46:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7de88fa-28f2-3ed9-b01d-d317140f0d3b | -7.3425 | -72.74767 | 2024-11-02 06:46:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 666cfc88-0d8a-36f7-a10f-494b4f99b083 | -7.34207 | -72.75073 | 2024-11-02 06:46:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b440af5f-b9ae-382d-99ff-19c0d4bc9795 | -1.2014 | -53.9184 | 2024-11-02 07:05:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 87832e51-4f1b-3794-8fd9-efbfe67a6e06 | -1.2014 | -53.9184 | 2024-11-02 07:15:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| dc142e7f-3335-303e-a24e-5a0f1886260b | -1.2014 | -53.8983 | 2024-11-02 07:15:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 3fd92526-46e4-3478-9bd0-d869749e4ae9 | -1.2014 | -53.9184 | 2024-11-02 07:25:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4e98413d-747f-3ea0-85bf-8492e2cc0fd6 | -1.2014 | -53.8983 | 2024-11-02 07:25:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 30388444-e400-3ad3-a9fe-c7c9515e193a | -1.2014 | -53.8983 | 2024-11-02 07:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 95188ee5-0a9d-304f-9668-920b8d8caa2b | -1.2014 | -53.9184 | 2024-11-02 07:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| dd4e4d7f-9305-31bb-acbf-b6bceb08340f | -9.71 | -40.68 | 2024-11-02 10:04:28 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 54d82bde-352c-3213-8ca7-28d17092c545 | -9.68 | -40.67 | 2024-11-02 10:04:30 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e9a4946e-06d7-3520-b5ef-e0589f8419b4 | -4.26 | -45.82 | 2024-11-02 10:05:02 | MSG-03 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c103edd6-0417-3433-9ed9-7ee72370c519 | -4.29 | -45.82 | 2024-11-02 10:05:02 | MSG-03 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45dad441-eb8a-3d60-b231-05dbd14b4c21 | -4.26 | -45.77 | 2024-11-02 10:05:02 | MSG-03 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bce4a9d4-e395-35cf-962b-45a2ae5ad386 | -7.75273 | -38.75948 | 2024-11-02 11:38:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 126.9 |
| 2ac7e769-c0e4-37ca-8889-f83841ba2a05 | -5.3997 | -36.41351 | 2024-11-02 11:38:00 | TERRA_M-M | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 1965ced4-f227-363e-96de-a65843897488 | -5.4118 | -36.41531 | 2024-11-02 11:38:00 | TERRA_M-M | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 66.6 |


[Clique aqui para ver as próximas entradas](README102.md)
