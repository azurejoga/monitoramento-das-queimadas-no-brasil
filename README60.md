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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 794ec053-56da-3f5c-989b-c5a1c80f769c | -2.54091 | -51.17458 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0ec4694-b7fa-37b2-a230-e89b6de39988 | -2.54033 | -51.17833 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e24fbab-46a7-39a5-b8bd-f30cfd4a48aa | -2.53975 | -51.18208 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17a0b567-49a8-351f-8900-5b872b63b6f1 | -2.53916 | -51.18583 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4a42390-7eed-3516-a540-872da67e415d | -2.53806 | -51.1703 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00994e22-801d-3992-b33e-1f90802ab84d | -2.53747 | -51.17405 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eab565cc-9b5a-3e08-a9c7-3c3d053e86b6 | -2.53689 | -51.1778 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b18b5a1-7f27-339c-b1c4-d75687af223d | -2.53631 | -51.18155 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5678d8f-cee7-3b76-84fd-47126dd1decd | -2.53573 | -51.1853 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1468b98-d2e8-3dd9-9ceb-108bd9ec4e38 | -2.53515 | -51.18904 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82b181df-c32b-3961-8105-aabf8df2a30c | -2.53404 | -51.17352 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 117a8f3a-2c81-3171-9bbe-c65c1aff95e9 | -2.53346 | -51.17727 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 648c26c6-83b2-33a0-a31b-f580e1dfeb15 | -2.53287 | -51.18101 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69f1ebf2-7c92-34dd-93a6-bac8a482b1ae | -2.53229 | -51.18476 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 504d6f61-f002-3746-9d6d-61c707b06a9c | -2.53171 | -51.18851 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e4050f6-2ba7-3530-a7e2-bb38f198d111 | -2.53113 | -51.19224 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a303ca5-eaab-3c9d-b7f0-46538751672d | -2.53002 | -51.17673 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ef69e994-9a9a-3dd6-8a01-5daac13ec958 | -2.52944 | -51.18048 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c0eb9f1b-3819-3621-910e-cead8813a15f | -2.52886 | -51.18423 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a7b75b94-b544-34f1-a725-0fe8f7da9359 | -2.52828 | -51.18797 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6c8f7d8-5d54-303d-bc54-814dba1e8cb0 | -2.52775 | -51.16869 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40d63c92-8e22-336c-81bd-a0dbec09fdd5 | -2.5277 | -51.19171 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6360b8ce-20ff-3aac-8382-3c291642b6d2 | -2.52717 | -51.17245 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cace4921-5348-3cf4-bc12-d51e2b7cb860 | -2.52712 | -51.19544 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5ac5d1b-0159-3160-b6e0-7789064ae9c9 | -2.52658 | -51.1762 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1120c960-8c4b-3634-8729-45a58883bdab | -2.526 | -51.17995 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6ab333b5-c7e8-3311-a2a3-2adb5dc0b077 | -2.52542 | -51.18369 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e7f7d1f-1534-370f-8a88-43aca03e8e01 | -2.52484 | -51.18744 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0acf0ef1-bcc1-308a-993f-7d2667ae8901 | -2.52315 | -51.17566 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b1f3644-3b67-3212-a3b6-987a6cae5621 | -2.52257 | -51.17941 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cfd86c7-108b-3e39-9c69-9eea376b596f | -2.52199 | -51.18316 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fe096e1-f01f-33cb-8ca3-f5a66c0e3cf0 | -2.51971 | -51.17512 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ec0b98d-a734-3159-b934-8ff17f3293ef | -2.51913 | -51.17887 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc0ca3d5-fa25-3601-bd89-46001ec8b414 | -2.51855 | -51.18262 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49498371-d887-37b8-b2d8-a192e60cb9c6 | -2.51797 | -51.18637 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39f45e7c-3a9e-3529-951b-947cc63610ae | -2.51628 | -51.17458 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0c5968d-5cf7-3e8f-a6c1-be88fc794bd7 | -2.5157 | -51.17833 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 359a5b62-83c6-36aa-bff4-bbfb79bdd471 | -2.51512 | -51.18208 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e78962f-5376-3657-82bd-2825ffe622c1 | -2.51454 | -51.18583 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85ea6bff-8382-39ac-81a8-6f2ffd3ceff9 | -2.51227 | -51.17778 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aafe072b-e04c-3647-a987-632d8eb2b598 | -2.51169 | -51.18154 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 69bd11b5-9dd9-32c1-8460-877aba4b82fa | -2.51111 | -51.18529 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 91ffc94d-c69f-3792-9317-3e3165a5cc25 | -3.34229 | -50.75356 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79258739-373e-3b3d-a1c1-1d39dc20e948 | -3.34168 | -50.7575 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d462c53a-afde-3d68-b060-9f64d04e0d04 | -3.34108 | -50.76143 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 536a983b-d70f-39c1-8469-da627b40426f | -3.33876 | -50.75301 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bee2345-fa27-34f3-9ff6-6a5e3d502150 | -3.33816 | -50.75695 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95284ffd-512f-39fa-8926-c86e377741b7 | -3.33554 | -50.82106 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ce053ab-1a1c-3d1d-8623-193536c28965 | -3.33463 | -50.75641 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4390fd1f-bc04-33e2-9ff0-b4ceb6527238 | -3.33403 | -50.76036 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 237b69e3-962b-3b4e-b618-55d21313c0a0 | -3.32286 | -50.76269 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5447be1-f312-31c5-9869-c1a49e3a998c | -3.26614 | -50.77551 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd76031c-f64d-3862-abc5-f63ab6ab3999 | -3.25625 | -50.65223 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84512b14-4c90-38fa-9002-ca4bc6c2d560 | -3.25564 | -50.65622 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd39c72a-0578-3947-b5ca-b192cde0d8e6 | -3.25394 | -50.64369 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9d2668a-23cd-35f2-976d-4df4112ae406 | -3.25333 | -50.6477 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba106912-a0a3-3ce2-8074-8bba6fcaca74 | -3.25098 | -50.75704 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c92f7f11-09e8-3edc-9a54-7e193fcc0a47 | -3.24408 | -50.84837 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69f637b8-066f-3b4b-906d-36eab198b7cc | -3.24347 | -50.85228 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4b0ee4e5-c80b-3b39-8d61-01a0a0cddb99 | -3.24057 | -50.84784 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 96f9d4c5-2f22-37a1-9b73-06af5a021535 | -2.65222 | -51.74676 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22dff3a7-4bee-3fc6-9986-f658aae30ff5 | -2.65166 | -51.75036 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 086ef8c9-159a-3c1a-b2d6-18654575160b | -2.64941 | -51.74264 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 498be8e2-1b30-37f2-9c60-42dc98349e0c | -2.64885 | -51.74624 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fece04b-3564-35b4-8130-1e49d0218e5f | -2.64829 | -51.74984 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 019b6949-20db-3f11-b1a7-4e1e31bab499 | -2.64715 | -51.73491 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0d99d37-67d5-3bdd-8c10-aa51120fcbfa | -2.64659 | -51.73851 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5069699-d41c-381c-b3c9-b9a212187b77 | -2.64603 | -51.74212 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2d515a8-0373-3f45-b094-4a125277d922 | -2.64547 | -51.74572 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78675bd7-3466-3b3b-bb5f-c15c71ba5cc2 | -2.64492 | -51.74931 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6781609-17e6-34d1-849f-bb73b8850c11 | -2.64433 | -51.73079 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35e57a8d-9be2-3af5-9084-eea4e3d5cdbf | -2.64377 | -51.73439 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 342e8c70-4496-34d5-b323-17a3cf81ff69 | -2.64321 | -51.73799 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d17c8aef-8155-345c-862f-24efd178796b | -2.64266 | -51.74159 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2cb3cb9-8174-3169-bec4-4ea4806380df | -2.6421 | -51.7452 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 588e19f1-d950-386e-9cad-dbe90668b684 | -2.64096 | -51.73026 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 413e9d50-04e6-39b2-8cfd-7683032db617 | -2.6404 | -51.73386 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0e2c952-475b-3493-9aa2-5f43c1d292e3 | -2.63984 | -51.73747 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55f7a2cf-e71c-3288-98bc-04fe7a0a2458 | -2.63928 | -51.74107 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79e4daba-c330-3dfd-bd21-1b79cbb1d86b | -2.63814 | -51.72613 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef67b615-a3f6-3410-89be-2fe93aa90093 | -2.63758 | -51.72974 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78ab8d7e-9f09-32af-b02b-6d17564f0e0a | -2.60336 | -51.77236 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17ad62fb-ed62-3d44-90b4-f6a0e2045e34 | -2.60281 | -51.77595 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 953b46ed-e597-3f97-856d-de768b8738bf | -2.60226 | -51.77954 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3c6e22d-143d-3625-a3db-228279090e88 | -2.60161 | -51.77242 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 352a18ce-0154-3241-ad28-c44685773687 | -2.60104 | -51.776 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 597c9a67-e2a1-3ad9-bd73-de9c875186ab | -2.60048 | -51.77959 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 070e095d-dd57-39ff-bffc-7f8743b3ee9b | -2.57576 | -51.84916 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc35ff27-5756-3e3a-8ddb-08f56383818f | -2.5752 | -51.85273 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3adb894f-750f-34a1-88a9-2d19ef3c2f3b | -2.5724 | -51.84864 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a9907f9-6de1-3983-84ef-4364ce7604f6 | -3.17172 | -51.0865 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f27ce061-e8aa-34ac-bb9d-173871ebbe87 | -3.17114 | -51.09033 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e57c606-a9c9-352d-92a5-56f56db87488 | -3.16825 | -51.08597 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b13e4e31-9d68-3e4d-96aa-255609cb254d | -3.16767 | -51.0898 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa648539-5804-37d0-a71b-bd536b65314a | -3.15562 | -51.02902 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c07f7fa7-f176-349c-94d4-3d7b75215503 | -3.15377 | -51.02892 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54423119-6c98-3755-bf40-87c6f35205b7 | -3.15214 | -51.02848 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3be10fd5-b888-37be-b9fc-ce588df9b403 | -3.14112 | -51.64723 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60bb695b-7c82-3d67-8355-2cf8dc4ac197 | -3.12607 | -50.60401 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31d33ab1-477a-3101-9532-028a2f62828e | -3.12547 | -50.60797 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README61.md)
