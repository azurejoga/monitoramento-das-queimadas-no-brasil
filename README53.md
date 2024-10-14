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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 760fcae4-aa50-3b6e-91d3-f69dc20f5692 | -9.42091 | -44.15086 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 540b4571-7f3c-32ec-bfa1-7a610a0dbda2 | -9.42042 | -44.17641 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8627a34c-cbd0-3e40-8b92-0cfca0f8b71f | -9.41817 | -44.16877 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 656b52e0-1244-3f63-a168-62e1f541f3f8 | -9.41763 | -44.17234 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d98011b-81ca-33e7-bd9e-225fd1d99eeb | -9.41428 | -44.17182 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c4eca800-6a56-305c-93e9-e66fafb92f82 | -10.06994 | -44.17382 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 876b48b9-8021-3f0f-9cef-b20636d79a3a | -10.06939 | -44.17743 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0bb17960-2fba-3e36-aca2-b2c51c328a5c | -10.06659 | -44.1733 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f11531d-8dce-374d-9f4e-93a3ab805b9c | -10.06604 | -44.17691 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b1f222a-cad4-34ae-b2a2-e4f436840e8c | -10.05988 | -44.17225 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00d4f41a-dd8c-3930-9fea-f068f891cb79 | -10.05933 | -44.17585 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e90a303b-cd3c-3b1f-915a-38010f379315 | -10.05598 | -44.17531 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52e96c98-d30a-3043-aaea-e98510bd699e | -10.05543 | -44.17891 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 343abe69-d41a-3b6d-b21e-c5ef871db98b | -10.05207 | -44.17838 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 861f5d9e-389f-38e4-8eaa-a793abea36e3 | -10.05153 | -44.18199 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b0e48c2-99ee-35bd-a610-05c46aa7e5e5 | -10.05098 | -44.18561 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b81c1953-95ab-3b58-ac91-4ee7dcadca11 | -10.04762 | -44.18507 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8b7117d5-3ce1-3f60-9a09-72aa17beef4c | -10.08073 | -44.23811 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f992bd7e-f44a-3ccd-8d55-d26efd064838 | -10.08067 | -44.21605 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29003a38-4aa4-37bd-a9a2-1240c772c611 | -10.08018 | -44.2417 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d57d8206-5283-3454-8cc1-769148dcae2e | -10.08012 | -44.21964 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2e7c6da-0a62-37ca-afe9-efd07dd66a65 | -10.07957 | -44.22323 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33d51fa1-0237-3b75-ba7b-cc619b8f4f2e | -10.07951 | -44.20115 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3bb38e37-7ae9-3549-82a6-e82adbc9214b | -10.07902 | -44.22682 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf562b51-27fe-3518-92c0-3c6694905377 | -10.07896 | -44.20475 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| da08b973-6f31-3f14-ad9f-92aa62578421 | -10.07847 | -44.23041 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec453c24-9f41-37a0-8c2e-c36a2c70ffa1 | -10.07841 | -44.20834 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a9fd904-5a3d-3e1c-bed3-adabeb6001e8 | -10.07792 | -44.234 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6454e9d2-f3b3-322e-a4b5-4f8b35e33cb4 | -10.07787 | -44.21194 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e621a205-51e8-38e9-b774-89ee077b438e | -10.07738 | -44.23759 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| eacd6d6a-564e-3eca-8f5f-3d18447bc57c | -10.07732 | -44.21553 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4f3cbe7-ab42-3fac-9d1b-99d5162e5991 | -10.07683 | -44.24118 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c851949b-a975-38b1-a8de-4a8387d5c07c | -10.07677 | -44.21912 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75b329dd-c60d-381b-99f4-87901af9cb66 | -10.07671 | -44.19701 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5c07f1d-9a5c-3f1d-9d29-7e1ffc96aa5c | -10.07622 | -44.22271 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42a9950b-4ba7-33bd-9a57-4d7073ab2cc8 | -10.07616 | -44.20061 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7cc7223-6fdb-369e-aea8-a925674e1413 | -10.07567 | -44.2263 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e22f1d43-d446-37ad-a217-2fed85a36327 | -10.07561 | -44.20422 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65823508-67ff-3d68-9a06-f61aa8f02b71 | -10.07512 | -44.22989 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d9b4e28-ec8b-31b1-b3c6-1e9e6d860a01 | -10.07506 | -44.20782 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3eb9a02d-80c8-3798-9ea5-70f134824db2 | -10.07457 | -44.23348 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6524c9a8-0e8c-3ef4-8de2-aa2e237ea6cf | -10.07451 | -44.21141 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49d736b5-3dfa-3c96-91ab-a12e32b50e73 | -10.07402 | -44.23707 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bb76c561-40d9-3baa-97ac-d2952ad9c9ee | -10.07396 | -44.21501 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c69b6ac-e41f-3d06-86f8-60fd8650ca14 | -10.07391 | -44.19288 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eccee1a8-35c8-3c18-8eae-52070a242f25 | -10.07353 | -44.26272 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 78d3b2a2-a8c7-37b1-92ef-894dc14e3c88 | -10.07347 | -44.24067 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0495d64f-7b2d-3d3a-bd78-d801b9b74ef5 | -10.07342 | -44.21861 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2f71506-2e6b-362e-983d-6755b8e0520f | -10.07336 | -44.19648 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ea8e27f-ded8-3060-8d5c-473c7efbba5f | -10.07298 | -44.26631 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 621e9214-3e30-37cd-82d4-ddc345fdb2b3 | -10.07293 | -44.24426 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b6ca86b3-904f-3f34-b9a9-6e22436236b0 | -10.07287 | -44.22219 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc96224b-2d56-3e2e-95b0-cf22ac082739 | -10.07281 | -44.20009 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ae60144-f7c5-362a-a49b-960e4102f240 | -10.07226 | -44.20369 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20f9ec13-7271-3926-89b1-9bd53e1bf6d3 | -10.07171 | -44.20729 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ae00dc4-6b25-3ea2-a50b-717fe5762868 | -10.07128 | -44.25502 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| fc3518ce-cd7c-3508-af6a-3f4df12a2190 | -10.07122 | -44.23297 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f000bf1-4d7d-3241-b267-ec5e82d0c319 | -10.07116 | -44.2109 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7aab576-a1ae-304a-9f7b-1872fea17248 | -10.07073 | -44.25862 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 880d489d-a257-398a-9b60-a3411112f138 | -10.07067 | -44.23656 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51dee197-1d86-3202-b7ae-8a4439c3f014 | -10.07061 | -44.21449 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33c6dad5-af06-3ebb-bcbd-5a8ff386c3ce | -10.07006 | -44.21809 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63120b4a-c2b7-3133-8747-b02b2c7eec31 | -10.06963 | -44.26579 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 151.0 |
| fef34aac-8bb1-31d0-b03f-bb36a652e50a | -10.06903 | -44.24734 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0bdf42fb-dd59-3ff7-ad3b-352cae5c32e3 | -10.06848 | -44.25093 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9c6c6c46-a266-32b3-b186-e21d17a23752 | -10.06793 | -44.25452 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| bf1949c6-249e-3edc-9e81-f4e16b395e7a | -10.06781 | -44.21037 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d0d0b38-ab8c-3a0b-b361-1f2470f5d1d7 | -10.06738 | -44.25811 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| f625f069-d1cd-37da-b7a4-136665d2e999 | -10.06732 | -44.23605 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed7a739a-ff00-3a2e-865d-bd2b6b358970 | -10.06683 | -44.2617 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| a4a7b600-fb5a-37c1-b76f-27d2f8bd6e86 | -10.06671 | -44.21757 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 456d64d4-7cc6-3870-bdd9-eed9c2fb52b9 | -10.06628 | -44.26528 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 5c8f823c-8e64-318d-998c-f81f17a53b28 | -10.06622 | -44.24324 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2288a431-9950-303a-a52d-e1d65193388b | -10.06616 | -44.22116 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0630675b-af8b-3168-b641-81352fbb25c8 | -10.06567 | -44.24683 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 01d2a342-9169-3710-8de5-62dc9c358388 | -10.06561 | -44.22476 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76af55d6-1b5b-3f90-ac73-f04640ea5ec6 | -10.06513 | -44.25042 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 277b4149-d69c-3cf6-9929-d5531b1fc44d | -10.06458 | -44.25401 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| ccbb05f6-b43f-34b5-b77c-67a425ef7618 | -10.06403 | -44.2576 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| c2018e82-2385-3ac5-bbcb-fcf0eb0d0f1b | -10.06348 | -44.26118 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| a8fb9c21-9739-3d3c-ade8-9ffd889ca80e | -10.06336 | -44.21705 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c331e757-fa3e-36bc-9d6f-c86b47533a3e | -10.06281 | -44.22065 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa0547d0-adf9-32f9-a3ee-ff5b78d489c2 | -10.06226 | -44.22424 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70e8a977-7abe-386a-9718-e72384699d51 | -10.0611 | -44.20933 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63c910f9-abfe-3320-9e90-ede5b561c8c3 | -10.06055 | -44.21293 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f63c6ea-3d5a-3022-b42e-583b2421c220 | -10.06013 | -44.26068 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db4930c1-d378-3a8c-8571-45e58d4b0401 | -10.06001 | -44.21653 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56bc3941-1bad-369e-b963-d3a0a78a06c8 | -10.05946 | -44.22013 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd7ea134-4121-3d8e-ae82-7a2ee10000f2 | -10.05043 | -44.18921 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8bd39c0a-e77d-3e31-80f3-e8c7c2986350 | -10.04988 | -44.19281 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2869204-9255-3cad-a4be-cb957164fafe | -10.04653 | -44.19228 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ade5630-83c1-3e17-84ad-4f016babc0e4 | -10.04598 | -44.19588 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65a2f571-5f59-3ac3-b123-f45b03a9c504 | -10.04543 | -44.19949 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9edc8df7-6bbe-35f0-8718-6b899178f292 | -10.04489 | -44.20309 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 80e661c3-633d-31f4-af6e-0160d3460f37 | -10.04434 | -44.20668 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fd692ef-d65c-319c-a3e8-86d89ed09a6f | -10.0438 | -44.21028 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f95e0b4a-c2df-3be4-afc3-e466034ddfeb | -10.04325 | -44.21388 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbb00416-1e71-31c3-b676-2cae58e11b96 | -10.0427 | -44.21749 | 2024-10-14 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa63c941-0e2c-3a3b-8243-677dfa45e663 | -11.49267 | -43.23402 | 2024-10-14 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8cd525c4-a595-3cbd-a934-12c4923a4070 | -11.11185 | -43.33208 | 2024-10-14 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |


[Clique aqui para ver as próximas entradas](README54.md)
