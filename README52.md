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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d88a2125-c19c-3337-8f1e-749f553fa507 | -1.62226 | -52.60881 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cdcfbfae-f2be-39bf-9ee1-7c73a6407511 | -2.76257 | -54.05352 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b070cfb3-c13a-3b36-9d94-56470c5dfece | -2.4177 | -46.03302 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b73b6bf0-a23c-3921-b76e-a69ae8cd2cf7 | -1.25714 | -51.7564 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c7c7b60-82e0-34a0-9908-770dd3cb1f2a | -2.70273 | -46.26959 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acc8d6ad-6342-3ec9-bc90-085e74061086 | -2.77439 | -54.0472 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c28d00e-128e-3370-bf07-981abafd5bbb | -2.13063 | -46.40166 | 2024-11-23 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b8c3985-dc2b-32cf-ace4-8831aff6b8da | -1.52864 | -51.55973 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6377877a-b912-38e4-a24e-14046d424a62 | -1.3147 | -51.74989 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11ba6b07-0678-3b0b-9d4c-c2ca7d454bb8 | -2.74216 | -47.54451 | 2024-11-23 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41526ff1-0331-313d-98c1-6ae9d4ebc136 | -1.12796 | -53.40044 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81511221-4b3f-354a-a8b2-632d79b36332 | -1.78856 | -53.64669 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 128ff68a-17a5-3930-90cc-bcd8fdcf77f3 | -2.81982 | -45.15891 | 2024-11-23 05:10:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66a84c51-cb65-34c5-a23e-3dc25441acc7 | -1.28453 | -54.53898 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbfcba8e-3c02-33ee-91f5-f4655977e466 | 0.38305 | -51.08647 | 2024-11-23 05:10:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d65e70f5-af58-3dd6-a7e4-89b0f2e1fde0 | -2.19785 | -53.65211 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20a06136-337d-3727-8c7a-e42aae3bf638 | -1.77706 | -53.60896 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1078134-0b35-32b3-ac76-47568f0ddc75 | -3.02323 | -45.13653 | 2024-11-23 05:10:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22c307da-6cd9-3b76-b4a8-399fa2a3aaf0 | -0.32259 | -51.53869 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f77abee-b948-3416-9c44-38bdbf8f913e | -1.25396 | -51.75075 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72a51f8e-c5a7-395a-b601-36c5b1548a9c | 0.69555 | -51.44217 | 2024-11-23 05:10:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 631454c8-7ec0-3885-9f7d-ffd2f4e38267 | -2.19595 | -53.6644 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74cd7b8e-de47-311d-b944-727cb5f4cf18 | -2.54693 | -54.04214 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbf9b11e-5a8a-3802-a3c2-6993b8ab3b4f | -2.44727 | -49.0854 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 136d9378-983b-3240-8a99-01673ec10d37 | -2.13757 | -50.70091 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f440786-89fb-3045-a28e-9a97ce229fa5 | -2.72237 | -52.56135 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a4d2198-97b6-31a0-a538-b4d0e28bad86 | -1.61545 | -52.60312 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 978f5611-8d90-3030-b20c-d3661481917e | -2.7705 | -48.60738 | 2024-11-23 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef0f2fb8-828a-3f43-90e9-873496c749b3 | -0.76905 | -51.7706 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25c43950-a923-37ef-945b-2873cc64abe5 | -1.42849 | -52.40969 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd8b8dc3-b2d7-31f4-ba7b-ab9454f7f0df | -0.93554 | -47.55854 | 2024-11-23 05:10:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35d920fb-4d29-3c25-b20b-a6f604ed45e5 | -1.20414 | -51.94641 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25d41511-1299-3f79-be2c-a21f2391ad04 | -2.68224 | -52.07409 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e3a595f2-19e2-310d-b29b-5103cc8c5798 | -1.19271 | -51.93788 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 63fbd3fe-2312-395b-9fbd-1e3c45c46333 | -1.78733 | -53.65479 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72e1e3a7-e885-3cc9-bacb-fd7085600e3b | -2.16356 | -53.77931 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4223d5fd-13a1-3eb9-9e81-bff9979f3642 | -1.235 | -51.74265 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| efc11070-7b61-3a4c-bb0c-cecd06a18b80 | -1.77067 | -52.70539 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c794fae5-3da1-36ae-8305-d3a317f8c961 | -1.19339 | -51.96478 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7db6ffc-1284-34fe-9c76-3f6b7fcb990a | -1.72844 | -52.73108 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6141017b-6498-3322-9ac3-c816eb320f92 | -0.93327 | -51.7211 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e097ae2b-3199-36f7-968e-d45082fc9004 | -1.21065 | -51.74758 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94b34c2e-7127-3fee-8e70-3bec6f8d988f | -1.19003 | -51.93423 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fa3ebf2d-b841-36e8-9313-244f622405bf | -1.62583 | -52.5861 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4babbf20-8ace-32b0-9c0f-1844632073ae | -0.03664 | -51.23083 | 2024-11-23 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af1d4cb8-50be-3d84-859c-680122bc936a | -1.19728 | -51.96539 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ff76ef2-69c3-3bd1-aa96-2198067b6475 | -1.25637 | -51.76143 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c047546-53b3-3cee-9303-aa91fdbc9b75 | -2.77195 | -54.06306 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ecf141c-c521-3400-b3f9-cec751add9d0 | -0.98203 | -51.71845 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 436831c2-bfd0-3dac-8e4c-1521c9f096cd | -0.42166 | -51.80463 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ede19285-da52-3aef-aade-62a2a55a87d4 | -1.20671 | -51.74696 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ae6c914-6743-3a51-8cf8-dd5327bca9bd | -1.77747 | -53.62976 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 66e29399-ea6d-305e-9139-feab01cd9f78 | -0.82109 | -52.4769 | 2024-11-23 05:10:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2005124e-b1ac-371d-afcb-53f26f2aedf2 | -1.6785 | -55.02629 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69e35b97-627a-32e2-9b4b-00ec2c684e11 | -2.28944 | -51.09822 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e53ff78-d38c-31b2-b5fe-1f9ed4104d37 | -1.78563 | -53.64757 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 572b477a-809a-34ed-b764-fe91646e9449 | -1.61901 | -52.61032 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1efe27f-3fbc-3610-87f3-522b978579b9 | -1.77303 | -52.71497 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91fc426b-a329-3f95-94a5-381fdfc45e59 | -1.18876 | -51.96908 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5164ee9c-ffb1-3010-a535-4713eb315991 | -1.11291 | -52.34462 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f578355e-a6ed-3ea1-9f14-f23020222b8f | -2.63816 | -53.9665 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 898060fa-8499-3653-9b0d-c1a2526e0980 | -1.77349 | -53.60841 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24de9401-f933-3c7c-a5d2-f8d33855bd46 | -2.61831 | -54.26122 | 2024-11-23 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dee5ed2f-1540-3f96-8650-01986d59da50 | -3.47225 | -47.68816 | 2024-11-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bfe933b-ba53-341e-90a1-9520f862fc72 | -2.44245 | -49.08464 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5b01f300-06eb-3e84-a861-10b3543aea29 | -0.26181 | -51.56816 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6007a116-ecdb-39b4-9aa7-0eb89b4e79bd | -1.70305 | -55.60939 | 2024-11-23 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 075244d0-3dc9-3d36-8b5a-12300272df85 | -2.78728 | -53.96345 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44b53e3f-aa25-3f93-92e6-b948895a32ad | -2.66504 | -46.60507 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38f7d61d-3a28-36c8-a3d0-31b523a8b91c | -1.60417 | -52.60138 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9eae0f89-4ecb-3f11-b125-5c341ee0396f | -2.76075 | -54.0654 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f5c91f4-5e98-39f7-9ab2-853155c6a450 | -3.21395 | -51.01954 | 2024-11-23 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86dee5ba-1405-34e0-8d78-ff0efe4c0c3e | -1.74659 | -52.38433 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32d97d40-1df5-367b-9b79-fe00d4329ac8 | 1.36637 | -55.94305 | 2024-11-23 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55d173db-10d4-3ab2-8568-42728abae24e | -2.38085 | -49.10184 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3af878e0-da2e-3832-8353-4a9e316cd58f | -1.79741 | -53.66047 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b35af8c-ae4a-37f6-9542-6b2333486505 | -1.45845 | -55.4538 | 2024-11-23 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b58413cf-ec7d-3167-ae17-215b9bc7e9b3 | -2.01283 | -51.17451 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6add2f3a-b5f0-30c8-9c9c-84cdab5de2bc | -3.15348 | -45.21843 | 2024-11-23 05:10:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 785d82c1-b69b-35cb-b9ea-2a6330dbff20 | -2.61421 | -54.26456 | 2024-11-23 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88d3be72-a558-3b1f-9080-05412fb5bb0e | -2.70906 | -46.09494 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 329066c0-09cb-3d17-a6e1-8ec293c8e6d7 | -0.27017 | -51.61776 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bd582b3-1e2d-3451-8867-a6c0550a129e | -2.82611 | -45.15983 | 2024-11-23 05:10:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96bd3320-9f33-30b5-8a47-032dc102dbec | -2.73989 | -54.13086 | 2024-11-23 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0baacb37-6b71-3683-88e4-2498fc1301c3 | -2.53898 | -53.97607 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7f91a7f6-aebc-398c-9221-b58dcd2571a9 | -1.07168 | -53.18121 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4176f6eb-7c97-3c42-92e0-633dc31abeb6 | -1.67292 | -52.66042 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 86218089-4aa4-3afd-8da4-4dd0708fa1d0 | -1.21118 | -51.95252 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1893fc9d-b4af-3db3-826a-1754ef141f5e | -1.2039 | -54.0376 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70919521-e622-389d-9758-ca5fdeba9c80 | -2.95534 | -51.44241 | 2024-11-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2110360b-411b-37fe-8962-b69bbb1e1004 | -2.70297 | -46.26249 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7f7c7ee-4cc2-3c30-8f64-a5d666238a98 | -0.91959 | -51.65197 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c188037f-0cf7-3f59-9f15-8eeaee5b2fd7 | -3.15419 | -45.21337 | 2024-11-23 05:10:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a3597a83-ca8a-3840-a30a-937f55d3281b | -1.28943 | -51.73041 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3e74113-734f-3c0b-871a-6603dff7a75c | -2.57098 | -54.05001 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f07ba59a-d3cf-34f8-a02c-899fd5f570e6 | -2.13636 | -46.40263 | 2024-11-23 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58e609fd-25e4-3c40-b1bf-af8e79a11e4d | -1.70017 | -52.75658 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58203e2c-428c-36a3-9213-fc1692c0514f | -2.54299 | -53.99719 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 03fb320d-883e-3bfb-b93e-09a3ec86a39f | -0.81289 | -51.61339 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19e43ea7-dd32-3459-b9c3-92eda761b749 | -0.96158 | -51.72038 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README53.md)
