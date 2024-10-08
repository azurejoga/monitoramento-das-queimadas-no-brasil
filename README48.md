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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e918c14b-3912-38e2-b016-e1bde73fa9dc | -6.4825 | -43.35816 | 2024-10-08 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 277f4c4d-1d1c-38a8-a8ac-d0390b8152cc | -6.48167 | -43.35655 | 2024-10-08 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bf2320dd-950a-3ed2-9fe8-a2049d75c9b2 | -6.47143 | -43.34521 | 2024-10-08 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44827162-b79d-300b-9bcf-d2fa913fdb8f | -6.42826 | -43.36821 | 2024-10-08 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e31ae65b-c069-3325-8075-9a1c0b781d94 | -5.88905 | -43.8737 | 2024-10-08 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0017c404-195f-3212-8d5f-d2ba3f40d4e0 | -5.88838 | -43.87823 | 2024-10-08 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc8bdd2a-a6f3-33b5-b74f-cbabe71edac2 | -5.77407 | -43.99553 | 2024-10-08 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa7f88ba-6beb-3a31-9192-92ddab16b585 | -5.77102 | -43.99049 | 2024-10-08 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e26af33d-8c52-3eab-b1ed-45205c9c667a | -6.25505 | -35.20536 | 2024-10-08 04:32:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 06442a22-e559-3502-b909-4326e11b1c2e | -6.25292 | -35.20135 | 2024-10-08 04:32:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 825898f4-753c-3690-9530-4966c3219bae | -6.25215 | -35.20721 | 2024-10-08 04:32:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 0463acbb-3340-3949-8d6c-ba143bbfad40 | -6.43361 | -38.83121 | 2024-10-08 04:32:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 63e59278-c61a-35d2-89c3-1f99b5556b79 | -6.43316 | -38.8344 | 2024-10-08 04:32:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1a1c3310-4b15-3e70-9cc1-2d7858c57fff | -6.43273 | -38.83752 | 2024-10-08 04:32:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1cbe154a-9e0f-354f-8ed8-b64fa8fc8662 | -6.42881 | -38.82687 | 2024-10-08 04:32:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8ff9a8c2-9e90-3af7-ac6e-ecfa76c96b7f | -6.42836 | -38.83016 | 2024-10-08 04:32:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b820cf9b-284b-360d-93be-9b566d9e3f3e | -6.42793 | -38.83322 | 2024-10-08 04:32:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 39b4a6df-053f-39c4-8386-5b588483a783 | -6.42751 | -38.83627 | 2024-10-08 04:32:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eb3a2edf-50d1-39c9-9494-35a0ce96c9e6 | -6.26519 | -41.87766 | 2024-10-08 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 01348b18-5dc5-3b76-b0b4-41aa6d7859ee | -6.2646 | -41.88164 | 2024-10-08 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 3b7945b5-3861-3361-b667-38e2278e607a | -6.26093 | -41.8769 | 2024-10-08 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b682b9fc-daa9-39cf-bed1-c598e2b7940f | -6.26034 | -41.8809 | 2024-10-08 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 71e5f570-ac2c-3db9-ad84-7541c39cd4bf | -5.18458 | -41.30214 | 2024-10-08 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 758b3222-c5e8-3fc3-932c-a0f85a58fa17 | -4.80536 | -42.75547 | 2024-10-08 04:32:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d066cf41-c6db-398d-afca-110637c6318e | -4.45041 | -42.8997 | 2024-10-08 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 986b9d96-61c4-3155-b1f6-eccb0b4a3963 | -4.44578 | -42.90402 | 2024-10-08 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb429556-2c2f-31ef-bcf8-1a295a573571 | -3.61685 | -42.75267 | 2024-10-08 04:32:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e5ba1c1-59f1-3e4d-9a1b-fb99110114ce | -3.6161 | -42.75756 | 2024-10-08 04:32:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef765c91-79d7-3bb1-8180-ad965ae8cea3 | -4.25131 | -41.91918 | 2024-10-08 04:32:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| da7a3e4a-58f3-367c-bc29-f152c558d008 | -4.25076 | -41.92289 | 2024-10-08 04:32:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51c383e2-99ec-323b-9def-c3ab29928ce3 | -6.26154 | -42.51773 | 2024-10-08 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 02551592-3b9a-3525-865a-87467cc931cb | -5.96737 | -43.28508 | 2024-10-08 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d7194591-3444-3134-a77b-b7561777a144 | -5.96571 | -43.28806 | 2024-10-08 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e6344af0-36d3-30b1-aabe-7a1c95862d31 | -5.65491 | -43.00697 | 2024-10-08 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 839ab314-5ced-30db-b338-144077aed3ba | -5.53233 | -42.80445 | 2024-10-08 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| df2386c5-7ab6-3f90-9b69-6adee2938788 | -5.51098 | -42.7837 | 2024-10-08 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e272f9d8-27e0-36e9-aa1a-49b9a109b684 | -5.51048 | -42.78712 | 2024-10-08 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f954130f-e474-30b9-a102-39f6710f9433 | -6.31136 | -43.23682 | 2024-10-08 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1242ce46-af87-30c5-884f-9f3f0898d54c | -5.81696 | -43.23911 | 2024-10-08 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc2f74c5-f591-33bc-820c-531e11c35400 | -5.79566 | -43.2756 | 2024-10-08 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a9ea0a4-7dc9-386d-a514-201f639a04dc | -6.54193 | -42.70506 | 2024-10-08 04:32:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 37fda969-0544-37ea-9489-25a039ef7825 | -6.5414 | -42.70872 | 2024-10-08 04:32:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| df5b73d4-b363-398a-b4be-b58dfb276afc | -6.65771 | -42.1195 | 2024-10-08 04:32:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9251f5fc-b359-3564-937e-45154f514c97 | -6.65224 | -42.12726 | 2024-10-08 04:32:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 52d6b5c9-4884-348c-8f14-ab69edda8810 | -6.65166 | -42.13124 | 2024-10-08 04:32:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9f882097-43bb-32fa-b126-46370e1aaf63 | -6.64317 | -42.13028 | 2024-10-08 04:32:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 86ca911e-72e5-33cd-ab6a-c35801b7c2fd | -6.64261 | -42.13406 | 2024-10-08 04:32:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d527744c-9e64-30f8-80f4-a686f43e5156 | -6.61307 | -42.12944 | 2024-10-08 04:32:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 734b6d26-f7cd-349d-9ddd-dc644b52410f | -6.60888 | -42.12857 | 2024-10-08 04:32:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4ae8015e-d340-3185-8a33-c2bfc6c8b7a7 | -4.04597 | -43.24192 | 2024-10-08 04:32:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08ab577d-59c1-311a-8975-2705e86ff2e9 | -4.04218 | -43.24135 | 2024-10-08 04:32:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b33a06f-1bd0-37c7-b9c6-815352da8949 | -4.01985 | -43.23584 | 2024-10-08 04:32:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0be6ea6-4439-3013-b1af-6c2afd934d66 | -4.13335 | -43.80738 | 2024-10-08 04:32:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab1a5c39-139a-3ee0-bf44-761066d8dd9e | -4.65388 | -44.37401 | 2024-10-08 04:32:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f444aa67-8e75-3044-b6f2-4bd694ee94d7 | -3.96057 | -44.47808 | 2024-10-08 04:32:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4361da61-eb8a-3def-ad45-e8c9c0e8b829 | -5.01463 | -44.09385 | 2024-10-08 04:32:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54fffad9-ab40-38e3-a38a-f8f7575d2df7 | -4.82042 | -44.35576 | 2024-10-08 04:32:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 721c93f2-2b6c-3b6f-85b3-d916c9e60f1a | -4.81897 | -44.35381 | 2024-10-08 04:32:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4c4feb5-11f7-33dd-9c6c-a815d2ec1735 | -6.25995 | -44.79348 | 2024-10-08 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e84f046c-a05d-38ef-8c64-07cf9df78aec | -6.25932 | -44.79757 | 2024-10-08 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 478cc0a8-912c-37f7-8678-a6717b9c7007 | -6.22114 | -44.18718 | 2024-10-08 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 149a201a-3cfd-368b-ab17-3ad796661785 | -6.21442 | -44.18168 | 2024-10-08 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0f141d5-0885-34c5-b90f-3854b3e7012a | -6.21376 | -44.18612 | 2024-10-08 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97806cd9-66d8-31e3-9f87-559e2a7ec48e | -6.10414 | -44.54564 | 2024-10-08 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 011ea4cf-ece8-3f1c-965a-0cfc23b164b6 | -5.99157 | -44.44139 | 2024-10-08 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b7d01167-5c73-3c90-b6c0-1b61d79864ce | -5.98793 | -44.44086 | 2024-10-08 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e2b8c51b-47c7-3317-88d0-c85054b2dd11 | -5.85246 | -44.87561 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 35e27ad5-1788-3cd8-9074-6e730b4c1714 | -5.84951 | -44.8711 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4e95d5d8-bf52-3df2-9e72-1fed686ff47a | -5.84891 | -44.87509 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99c29b37-8bf6-39d0-9b53-26cfb8135868 | -5.81904 | -44.12397 | 2024-10-08 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11ef8633-2f89-3aed-a945-92ba6e582963 | -5.81837 | -44.12837 | 2024-10-08 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c483343d-6280-3767-9dd7-b82f975255ea | -5.8177 | -44.13274 | 2024-10-08 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39cb3d1a-978e-31e5-8a90-83e569cff503 | -5.81536 | -44.1234 | 2024-10-08 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 948dc915-b74b-39f1-bfcf-75ce0336df68 | -5.81469 | -44.1278 | 2024-10-08 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7f4cf951-a1ee-3b35-a1cb-d67e1b2d67d2 | -5.79714 | -44.04405 | 2024-10-08 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ff47599-703c-371b-b63e-b5e92b6b3de1 | -5.7139 | -44.81135 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c25c66f2-5d7d-377f-bc01-402778483153 | -5.58037 | -44.87842 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f015494e-7fd5-3ae3-8e09-a9a5fef69a32 | -5.57745 | -44.87389 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ff6059fc-dda8-371f-bba5-2a9432b3ca20 | -5.57684 | -44.87787 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e3d810f4-75e0-378b-9544-390be98ee9f8 | -5.57392 | -44.87333 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 616faffe-eea6-3ad4-8ae6-c7f141f2e17b | -5.57331 | -44.87732 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 71530c5d-c224-3f12-aa78-a88c6b065bf8 | -5.5727 | -44.8813 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| c59ace7c-72a7-3436-8fde-faba9f876807 | -5.57038 | -44.87276 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b87d73cf-6d5f-30cd-8104-4dfc81b245b4 | -5.56978 | -44.87675 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a52a111d-3f06-3342-8176-1f078ef2ef7f | -5.56917 | -44.88073 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e4b63c1d-aa2f-3105-817e-6b822d655c3d | -5.56856 | -44.88471 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7fea7f08-4d64-359a-9f89-7a642df70372 | -5.56564 | -44.88013 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3da8a91a-851d-3263-beb2-6a2c273e8aee | -5.56503 | -44.88412 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5821d09c-8bb3-3436-8bc7-34cb3105de0e | -5.48455 | -44.25713 | 2024-10-08 04:32:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fda56297-0ca3-3467-ab5f-f339e33b6b29 | -5.48434 | -44.25483 | 2024-10-08 04:32:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6c7856d9-4a67-3311-b6c8-91a440052d4e | -5.48069 | -44.2543 | 2024-10-08 04:32:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d4e966eb-3075-3ecb-8b82-560d0c43c842 | -5.48004 | -44.25854 | 2024-10-08 04:32:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ade582eb-28e5-32a6-a224-e69591b2b1ee | -5.47704 | -44.25375 | 2024-10-08 04:32:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 27d50adb-f242-371a-9bcf-81e997ff6c77 | -5.47639 | -44.25799 | 2024-10-08 04:32:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e082a3b3-c79b-3503-a695-27d0aca73ad5 | -5.47275 | -44.25743 | 2024-10-08 04:32:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c0c75c28-a7f0-390b-9d3b-111ecf05a365 | -5.17128 | -44.66329 | 2024-10-08 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 866ae87c-be4d-3cea-9ec6-8af27daac487 | -6.16458 | -43.52681 | 2024-10-08 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b5dd659-99c8-32c5-ab7b-c77681682f91 | -6.16074 | -43.52626 | 2024-10-08 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1004759c-fe24-3797-9ad0-c4eef02a8dd5 | -3.61202 | -44.78867 | 2024-10-08 04:32:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54821f77-f091-3b35-a301-0a816df333e3 | -3.61143 | -44.79253 | 2024-10-08 04:32:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README49.md)
