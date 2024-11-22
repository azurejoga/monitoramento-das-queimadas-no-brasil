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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cb9df4f-181d-350b-8822-d32e3314e3e5 | -2.55817 | -47.32726 | 2024-11-22 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a81db448-7c78-36f4-8f02-7c6186c7ab71 | -3.37794 | -52.45572 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a40baf38-fe81-3c73-bd2a-20ec3718e301 | -2.19766 | -50.68354 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e93b592e-0080-34e7-80ea-aee8ae77fcbd | -2.13583 | -50.70166 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0280f5ef-f209-3036-bfa9-aa17f66a8a42 | -1.19105 | -51.94482 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d5a1587-c4b8-35c5-8d2d-9aac16d2f1c5 | -5.94736 | -44.46629 | 2024-11-22 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6a7297f-d5f5-3114-bc2d-dd339a656b40 | -2.50695 | -48.99431 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f61632f3-5f2f-3838-8fc6-96996a9689c7 | -3.99246 | -49.95905 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89a4695b-4c29-3430-8002-fef2b7d04292 | -1.80475 | -48.7717 | 2024-11-22 04:36:00 | NOAA-20 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b592d700-20d4-3a58-9a43-8987f31f5230 | -2.01376 | -51.17604 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 763ed503-a664-36bc-8db5-9943e61b505b | -1.25688 | -51.76096 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab9cc7c3-40ae-3dfe-b309-218d464d6c8f | -0.20887 | -51.76239 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09601901-0862-3c1c-88d2-094b4e6d5aa0 | -1.91695 | -52.08675 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e0eb3a4-e6a7-3030-a16e-bfe7528e0171 | -1.51908 | -47.06599 | 2024-11-22 04:36:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17a6dad1-e6b0-3196-bdff-bc86c963117b | -2.68292 | -46.25652 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cadedea7-3122-3f51-953d-5a75546015c4 | -2.95742 | -54.05844 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e840692-4349-3b50-ace9-962b4deab5f6 | -1.84478 | -53.69882 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 879b57e1-6a71-312c-bce4-7cb401338a9b | -1.20178 | -51.9738 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5af758be-1da3-3a1d-903a-2124e5bb79b6 | -3.10787 | -53.7529 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f074e8b9-7e4f-308e-9e51-65e3e4d8cd55 | -3.96244 | -46.72845 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12c2cfea-61de-31a7-8836-1be665e09c91 | -4.28742 | -48.21488 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d66fd71-35b2-3459-981b-c357262bac8b | -0.40319 | -51.5956 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c47378ad-5b30-3ac7-9b6a-5b3a5e1f2502 | -0.9788 | -51.72158 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a0df258-08cb-3d14-a217-1d80e41c57e6 | -3.90626 | -46.48347 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aa48344-9c78-3ed6-838f-48a8f03bc2ab | -0.97581 | -51.71667 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e72b6979-64f4-3583-8be0-773b18551240 | -1.19382 | -53.6779 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93119844-18dd-3992-b284-7c0e8e8756e0 | -1.29109 | -51.73542 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eef8f54f-6c67-3e93-bee0-5505f102fdea | -4.07811 | -46.84184 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b1c5a72-f3f0-300c-9505-498433ba4a24 | -2.15831 | -53.79638 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 616636fd-8b38-364b-a0db-0e3f1b683c2d | -2.70505 | -45.23275 | 2024-11-22 04:36:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2677c8e1-1b8c-3fb3-b156-53b40433744c | -3.62041 | -51.36798 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98285ff6-2a2c-3faf-8799-11ec07b4878d | -3.03195 | -45.65925 | 2024-11-22 04:36:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb6ef2e2-62f1-38e8-b79a-34f55670bbb8 | -3.53736 | -54.08582 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07c890d5-c942-3c56-bb3d-15bd544d2c98 | -1.47533 | -51.96582 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6716f90-8e09-36e4-b7f9-842a9f9cc8b1 | -3.82747 | -52.26661 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3654db36-220b-3d6b-bd91-50327b87f8ee | -2.97989 | -45.12539 | 2024-11-22 04:36:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2e649605-3c54-3bf3-abb1-8ac048bec413 | -4.49222 | -45.80061 | 2024-11-22 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb6c036c-65e5-3dbb-8be5-7ebd6d680737 | -2.19908 | -49.26563 | 2024-11-22 04:36:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 435aee6b-2f0a-3b3b-a44e-ac69435971f1 | -1.64295 | -52.62223 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efe03720-0626-3703-a5e1-c519d9e527ac | -2.26216 | -48.45633 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8943e7ab-b97f-3b52-a262-0b45da429dc8 | -1.18432 | -51.93919 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0b1b313-87a5-3d2a-b344-93a135c435b1 | -2.10497 | -50.36361 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10fdf02c-5f3d-352e-b98c-659e28214486 | -1.3074 | -51.75121 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7059d691-5d4c-3ac7-9b11-0a78b2153879 | -3.27587 | -53.82045 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 48fb3b1a-89a1-3ff1-974f-d1582661512c | -4.4966 | -46.1073 | 2024-11-22 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9279a773-5cd3-3ca1-ad58-e0d5e517f556 | -4.25474 | -48.70523 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dbcaac1-eddc-39f2-9597-bc3ef70b1484 | -3.19611 | -48.58849 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa3ca9f8-22e4-3c14-ac10-a7f6e0e669b3 | -1.2125 | -51.75972 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ce23f35-dd70-35d3-a940-045871113870 | -3.4412 | -51.60662 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e7adabb-ce36-379d-a852-e3efd14af229 | -1.42466 | -46.79999 | 2024-11-22 04:36:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f4d9775-27e0-3e84-beca-31e5b5c2cbcd | -3.22695 | -54.23235 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8665a24f-e717-33bc-882e-04b75aea7139 | -0.27447 | -51.56152 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4cb7ce8c-c889-36ae-a862-2146b2b16c61 | -2.94794 | -48.07036 | 2024-11-22 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c37a54b0-2200-330b-a341-50fde086b985 | -2.84904 | -54.00712 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2e0822d-f94f-32cf-a1d8-e4d7efad1c0d | -1.65596 | -52.6755 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea95d151-0cc9-3a2b-af33-4fad4c8fd6e0 | -2.3696 | -50.33222 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa6ed1dd-8ca4-31dd-853c-f7ed0105a5ce | -3.10587 | -53.70952 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f65ce7f-9186-38f7-b136-6d5e84a3d017 | -1.34155 | -52.24553 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c795773-0efe-3334-996d-742101161542 | -2.78138 | -51.717 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b01b7884-2db5-33c5-acc6-b76e4bf4a0c4 | -3.51358 | -53.79306 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1794918-c414-3cc8-ab07-fa7d54e1e5ee | -3.2326 | -54.23306 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4e6070e3-0d64-382b-a75b-91c683130a75 | -2.45696 | -46.05078 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96fc57fe-340e-36a4-ba6a-9b30496ba215 | -0.93798 | -51.65057 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aecb1221-bb81-3783-925f-3351310e3317 | -1.09203 | -53.16549 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 62b82e92-06fd-3cd8-b98b-4114adfdfe13 | -1.63836 | -52.6264 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 18d18f73-7f21-3325-9485-9718ae686f78 | -4.80163 | -50.44992 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7cc1ff2-f41b-3413-878e-fa755022d9aa | -1.20558 | -53.68412 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ed584cfc-755a-3836-a0d1-a9186105b2da | -0.2195 | -51.19321 | 2024-11-22 04:36:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e48cbf8-b1d8-340b-b82f-bde146b87019 | -3.34688 | -42.79091 | 2024-11-22 04:36:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ba1dc527-8a88-34ac-9ab8-de8ddd4a1f3f | -3.46998 | -45.91566 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e99bf3dd-5f39-3c16-8d8e-5552a9baddf4 | -3.04341 | -54.40602 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d45286bb-388a-3486-b849-0c995b3a44fc | -3.27768 | -53.83516 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3df71c1-2d5b-329b-af7d-172a8c12133d | -2.37505 | -50.38588 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8e3070a-7eda-3b97-857c-d3d06bef83b0 | -4.24964 | -46.11296 | 2024-11-22 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b2b54d98-d773-30f9-8a0f-42dbc1bb2652 | -2.75259 | -48.57884 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b780ff9f-aece-3278-a4de-d7c28465f707 | -2.68588 | -46.87316 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02d8090e-7b5e-30ef-8e31-8ef6e0049985 | -0.1884 | -51.5569 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d846efc-1281-3a99-ad3c-ecfa5f4755a5 | -2.55823 | -48.17148 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 101768de-171b-34ee-804e-0bde82b0ede1 | -1.25666 | -53.3636 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18b0ac53-d26f-37a1-895a-6c36c51af800 | -3.90567 | -46.48727 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03e73079-62ca-368a-9cae-e9f243c5a97d | -0.96338 | -51.72362 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 641ffbdc-c696-3fbe-9932-73af936d9eaa | -4.3985 | -44.12542 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 083fb9ce-3ec2-30f9-b9a7-f530643ce46b | -1.26694 | -51.62758 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53a5e10e-8c47-3ca7-a4aa-997ce6b1f606 | -3.23221 | -54.25309 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| bc095994-a9bf-3226-836f-f4ef95afac38 | -4.00582 | -49.91787 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ac44637-17d2-3283-b47b-5826ab1c0c97 | -4.49954 | -50.67708 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 012521e3-a18d-33bd-9618-3042e8001136 | -2.09755 | -50.36623 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe2c9910-9372-303b-8706-181da506e666 | -1.74332 | -52.39983 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f6332f3-efce-3f2d-a041-077d2d4d36ff | -3.03542 | -54.84492 | 2024-11-22 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96233735-2488-3880-9791-6512df74ee2a | -3.03132 | -45.66331 | 2024-11-22 04:36:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28efe928-604c-3ea0-ad33-b034406728ea | 0.46965 | -51.34135 | 2024-11-22 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be8214d0-1745-3438-a726-fe624d3aa952 | -2.70322 | -46.24012 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae500f12-401f-3714-9844-937c79a72d56 | -3.24738 | -54.24722 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0eb10dac-9d4e-37b8-b080-6a9be7e72430 | -1.81222 | -52.15906 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 899bb2c8-1990-378b-b9cd-ef7894e305af | -3.31947 | -54.09286 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4c485a4-a78a-3607-ade9-ad08b32f3c87 | -1.42437 | -52.40837 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78a1e84c-8d06-382c-b999-e7ecdf1e2814 | -3.26042 | -46.53621 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5058da36-b241-3f14-9e5c-9e0b614bf2b1 | -1.65594 | -52.70013 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e3b45adf-f076-36d6-9902-d429cc064719 | -2.6117 | -46.19949 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c624144-5f18-3498-bba6-8250ed26cae4 | -1.46362 | -52.66978 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README50.md)
