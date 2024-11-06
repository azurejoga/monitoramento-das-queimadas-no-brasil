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
| 7be29e7b-d285-390c-9b50-5f8e647793f5 | -3.02991 | -53.26035 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a635db9a-6992-36fe-83d6-cad3c54b0d65 | -3.03496 | -53.26156 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba3ba9e6-b5c3-32da-9aee-aa649ed3f109 | -3.03785 | -53.2769 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f288a501-69b3-3f76-a64d-83383239450a | -3.09213 | -53.71393 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1894a03b-9415-3b07-a621-65f2f1925baa | -3.13917 | -51.2006 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a22d5ba2-b25c-3352-93fd-c50d3a02dd7e | -2.82629 | -52.94247 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c43c0564-7bc8-3004-8b46-47c146284b2f | -2.81705 | -52.93452 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8724bc1a-0c91-380f-b9c6-a32c0efba0ed | -2.42458 | -53.66098 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edf63b0b-fa1d-3931-8ff2-2f2bc177e2ab | -3.166 | -53.07216 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14311bc8-b7ee-3dff-9940-287913b4b552 | -3.05094 | -51.07139 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6207945d-d1d2-3f5a-992d-f6d3922e6dff | -3.97344 | -48.16 | 2024-11-06 05:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9c259352-5fdc-3ca4-b523-bb4a89512be8 | -2.58529 | -51.86737 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6640d35f-2f05-321c-9ae0-056c1d9da76b | -2.81477 | -52.9498 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fff22cc-cafc-3c18-ae2d-07f4ae71a26a | -3.03411 | -53.26744 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 061a4493-c27a-3429-884e-994f143c8929 | -2.87527 | -51.30464 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0750d4de-46fc-3eff-a54b-02e9a4e8731a | -3.12023 | -54.25917 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73a7011c-55ce-39ed-8435-d068a7c6d830 | -2.82524 | -52.91455 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b7199d3b-53b6-39eb-a3f3-64bbd760c2e6 | -2.83728 | -52.90387 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9bd3e686-2f3b-3720-93a3-532c7f7ab813 | -3.01058 | -53.43033 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e7633997-f5e1-30cd-b0b9-977bea3383f6 | -3.24959 | -53.40558 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| af73407e-5650-39c5-af5e-89e28d813775 | -3.68521 | -51.36812 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d9f2834-38df-35e1-ba0f-b5e6585b8c1a | -2.94061 | -51.05313 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e75aeb22-1c9a-3652-990d-ddcdb48959c5 | -2.48009 | -53.98249 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e18f7ed-b234-3985-9b4c-207265757391 | -2.82945 | -52.92128 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3fbfc41f-b550-31cc-a679-65b8db986eff | -2.60691 | -51.30304 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84f984ac-457f-3046-83c8-3efbec2703eb | -2.93456 | -52.54131 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9476827-d0ae-3133-ab27-24150429b7cb | -2.91224 | -51.04447 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 37088905-c60d-3d54-8510-757ceaf7de14 | -2.67634 | -51.82598 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5ab8c1d4-f5e6-374f-a95d-f2e740ba2cf1 | -3.00925 | -53.42952 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4573466a-a1fa-3903-a83d-f823f74362d9 | -1.06705 | -62.65578 | 2024-11-06 05:31:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aec20582-858e-3f2a-b6b0-313a3792300f | -2.95414 | -53.71774 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28068b6c-985e-3521-92ef-bfa83878f225 | -3.3392 | -51.61742 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3329ab1-c720-3936-ae9d-8e62bddb21ae | -3.07098 | -47.77085 | 2024-11-06 05:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8039ba9-12f5-3dd2-b398-df41a22110c7 | -9.44531 | -68.53274 | 2024-11-06 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff961e16-08d8-37d9-9ef9-e37ea79528b1 | -3.06414 | -52.50044 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 83c9adc9-48c7-3bb7-b852-0ef35edcd307 | -3.19047 | -50.58662 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee34c8c6-5007-3d12-a6c9-41c9f7c2a172 | -2.8496 | -51.80053 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e7e3bbe-c75a-37fc-b689-fc4e3949ce7f | -3.15582 | -50.2079 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| d1c15bfc-3b41-3734-8304-b2fb359ae4de | -3.04326 | -53.27483 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95f5178a-4ebb-3ec7-9352-c3b04018996e | -2.47871 | -53.981 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f7ccb08-0791-30df-8520-9e0307762bad | -3.01008 | -53.42407 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86d9701f-0212-39dc-92b4-b09cbe011ce6 | -2.81106 | -52.93975 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8a86c5b3-b429-3029-a554-2145bb46ca1e | -3.16971 | -54.46829 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e9a406e-25b4-3ff3-9a36-9e5094125a09 | -2.83032 | -52.91547 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 396d604c-8273-3abf-9267-bab52ecbaa79 | -3.24531 | -57.56204 | 2024-11-06 05:31:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a350ede-f4ee-3c5d-9a9a-27f9a939dd6f | -2.82902 | -52.92421 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d4ba5763-97af-3aa2-bd82-6b45d1fb08f8 | -3.51705 | -51.66964 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3eef4096-2fda-3c2f-a0c4-e3a448a532de | -3.02995 | -53.26081 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4df1c66f-de14-38c4-af44-48bab8947b92 | -3.14165 | -49.13682 | 2024-11-06 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4d3d83ab-c705-3ea4-9e3a-875ddbdd869a | -3.53213 | -50.33834 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 852cd2bf-c50c-3dd9-9b2f-0f2969629a48 | -11.77651 | -64.9892 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a51923e7-6ca8-3c0e-aac7-45c64dac8736 | -2.91688 | -51.05179 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 26498e47-195b-35ab-b77f-316694f6ec94 | -2.81419 | -52.91861 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 401d42ba-e224-3c7e-9eb2-c86be3fc242b | -3.08826 | -54.50962 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ff73721-1b0d-3e58-aa1f-3079c38280ac | -3.14497 | -51.20117 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d6d50cc7-df98-3be8-9e68-9564f6ddc6fa | -3.1386 | -51.2046 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 22cbdba7-4588-3b5c-9a2a-d7e1ae66ed9c | -2.88097 | -51.30552 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df9409a5-c0ea-3e94-8b70-9be443bc5496 | -3.0414 | -51.25941 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce8d8392-508d-3712-8ac9-10231e42b479 | -3.0373 | -58.0099 | 2024-11-06 05:31:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b04c9a5d-6e5e-3058-b039-0cf973cdb165 | -3.33706 | -50.08304 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c4ea53e-9846-3b6e-834e-fb1e7b100760 | -9.66661 | -66.82859 | 2024-11-06 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7944faa9-97dd-39c8-b06f-a7f170f5a2de | -2.81242 | -52.93055 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 17eb8b6e-60d3-3cd8-ad7c-a205db2bf3fa | -2.42379 | -53.66612 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9e9348b-961d-38a5-aa2c-386120306fce | -2.8861 | -51.31034 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 327a9e15-5054-3781-a2fe-1e762ade0b96 | -9.44599 | -68.52893 | 2024-11-06 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f38017f-4572-39e9-8fac-1f4eda05d65c | -2.82074 | -52.94471 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 78a7f114-c739-3108-adc9-a5135fd69e26 | -2.81972 | -52.91656 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| aa433d8b-49dc-36a0-9490-b3275c818245 | -0.74355 | -62.90219 | 2024-11-06 05:31:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 873db7c3-9f18-3bdb-a852-385e83013f4f | -3.16992 | -53.07122 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6638f969-41e9-3140-9a37-64df9b3e54cb | -3.29646 | -53.1184 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27f94f60-7d42-397b-83e9-581ca6594e1e | -3.85341 | -52.2719 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19b11562-f200-3883-9ddb-455f67065f2a | -2.81331 | -52.92457 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bcfbb355-fb68-3b76-9c2a-9e285f0e9cec | -2.72452 | -54.14679 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| b0db8b2b-b7a4-3c01-ad04-1114d2313e22 | -3.15196 | -51.1527 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| efa9b25f-ba62-3c82-8ad1-3e754a08ee94 | -2.935 | -52.5383 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75e7aea0-8ece-3bec-97d9-1b6dc36c53c1 | -3.23119 | -50.38509 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa04e410-ddeb-3bf8-8321-c4ed20de115e | -2.8483 | -51.77078 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ae49b78a-695b-3ac4-a2b3-49357bfe81f4 | -3.1168 | -51.10685 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9dfe2694-6c03-3461-a889-b30db36dbe3e | -2.92452 | -51.04036 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6a2284fb-9230-37aa-a610-169498907b20 | -3.22755 | -50.91916 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69f94b1a-68db-39d3-b7a3-15ae0cf80932 | -2.91294 | -51.03855 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 042f3fd9-4038-352c-a023-428923ee6452 | -3.02829 | -53.2724 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7ae07082-3bbc-3818-8017-033a674d893f | -2.83775 | -52.90073 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 1f5fef73-fc61-3c1f-b506-4a71f767ae60 | -2.60687 | -51.76371 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dab55b9a-7365-3fe7-a3a7-8eadcec73509 | -2.82409 | -52.95714 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 65168977-ccbe-3092-ad51-68c9f3bc04a1 | -3.18113 | -50.59115 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c77845cf-c31d-33b4-9eaf-c779f2caeb93 | -3.32637 | -51.62667 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e64f86b-c5f7-3dfb-a4c1-b502817ca92d | -2.39335 | -50.32015 | 2024-11-06 05:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ef98afa-2dcb-3c80-8609-93b7b9321c4d | -2.8317 | -52.9063 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0060c2b5-82f6-3ca4-a99f-e11d453ad0ac | -2.80146 | -51.47589 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b76d868-c01b-38f9-bf4c-5040f6013916 | -3.03446 | -53.26402 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6a71b0bf-d26a-3263-9b21-89411b6a566c | -2.77888 | -54.72464 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 27b50825-d448-37a0-8d6a-e06d2bb5cf26 | -2.91803 | -51.04542 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 30884a2e-df1e-3a68-be95-d89b8385415a | -2.67087 | -51.82509 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 726f2585-9e9e-364e-8f1c-14fe4fe2e315 | -3.00307 | -54.09255 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7fbd7a6-558d-3c77-bcb1-9218f7abb7dc | -2.45322 | -49.03044 | 2024-11-06 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| e451f9f9-243d-3089-9386-99a5d2b4d6a5 | -3.11701 | -54.2485 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e4df309-a571-3391-99dd-ff4110d82579 | -3.23965 | -53.39805 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 25c102e4-99d7-38f1-9b71-73fa5534416e | -2.83123 | -52.90944 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 77e50ce7-9b33-32a5-bab8-ea2a503edfc6 | -2.84379 | -51.34554 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README66.md)
