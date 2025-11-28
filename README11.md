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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca3589be-9a8a-3117-8d6a-ec5b41641b17 | -2.9943 | -43.84125 | 2025-11-28 04:31:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b30608e-de74-3d2e-8435-e34123dea3fa | -3.80134 | -50.01175 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6001471c-52b4-3e3a-ae45-13731c139446 | -3.48343 | -52.15797 | 2025-11-28 04:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0957e00b-3ff8-3e01-84b9-4cc9281e94ca | -3.2631 | -51.17109 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e574722-8b2e-3202-92ab-f4d877be44c4 | -3.76599 | -46.96037 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 485013fd-69c5-3086-8479-a6e7cd13bf2c | -1.62631 | -46.19785 | 2025-11-28 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 771dbd1a-04b1-3c38-98e4-2c91391ebfca | -3.8531 | -47.05561 | 2025-11-28 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59b8fabd-30b5-3f7a-bf7c-1b05c6813425 | -3.387 | -54.1261 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e35cad2-5548-3e7c-a0be-92f32cd779a6 | -3.62063 | -40.64698 | 2025-11-28 04:31:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 461b16f5-08b3-359e-9602-170d46d95e75 | -3.23573 | -50.6982 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 696067d6-63ab-3944-b4e2-dac89849f584 | -4.57651 | -48.44889 | 2025-11-28 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20b54e64-f969-3af1-9b66-f2e6f6eb1be5 | -3.9275 | -50.99628 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f7b82ca8-723a-3961-89e7-925f6fa5b521 | -3.44833 | -50.54459 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25925735-9036-3f67-bc80-67b76aff9322 | -2.62948 | -47.35189 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5ce8741-d7ca-3925-8abb-ec98879bf1d9 | -2.02385 | -46.31004 | 2025-11-28 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3401638c-3e33-3969-acb1-0050c77e5ae3 | -2.79977 | -48.56392 | 2025-11-28 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 859995a9-312b-326e-8463-a43ab27097e0 | -5.15311 | -46.15613 | 2025-11-28 04:31:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4921eaf2-552a-345f-9f47-6b197f62a18b | -2.89423 | -45.54608 | 2025-11-28 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d43a5067-a70c-3d6d-acd8-aba275f9493d | -2.81006 | -46.76444 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f18e475-5c06-38e6-9df9-52c071047ba8 | -6.36143 | -46.15508 | 2025-11-28 04:31:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a98c7db-a167-3691-991b-8f7bb40843ee | -1.2484 | -54.06083 | 2025-11-28 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2914755a-f3bc-3888-acdd-e313ef979e2e | -3.85963 | -47.03549 | 2025-11-28 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80d30af7-9930-3a4b-a6e6-b574be6ceed9 | -5.30209 | -44.72715 | 2025-11-28 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7d04a95-3083-3f86-a16f-162ff8cd06e6 | -3.18811 | -52.0209 | 2025-11-28 04:31:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de0dd8d6-cd32-389b-95d9-61e1cd362294 | -2.61794 | -47.36068 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e52a9567-ce32-37ee-b83d-c146000546aa | -5.44913 | -44.69016 | 2025-11-28 04:31:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 969d640b-1d83-3c0d-bb1f-333b3dca506a | -1.47639 | -54.205 | 2025-11-28 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9aa8368-a6af-3288-b541-961dcc38634e | -3.25841 | -53.06019 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f323b251-22df-3989-820a-18b09e90614c | -2.64911 | -46.96797 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa14296a-73c2-3dd6-a63d-057200cde097 | -3.8498 | -47.0551 | 2025-11-28 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06c6b522-549b-3f34-a3b5-e4fe59ece907 | -3.36944 | -50.82521 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de94aa50-1677-3d33-b525-72a2dbdbe7ec | -3.06452 | -50.36346 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65050090-8e83-3be1-86e1-bdc981970f69 | -4.57317 | -48.44838 | 2025-11-28 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc4f1c48-3fef-3bfc-84bb-fc1fb6f0ca6b | -2.62894 | -47.35534 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5551ee08-45e8-31cf-8965-643f69a793f2 | -3.40476 | -53.30335 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e5cb7b6-4048-3a4f-99ab-997f7f01f53b | -7.4614 | -34.81638 | 2025-11-28 04:31:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 72c58ff1-a4d5-34b6-8ee9-69323f19a50b | -2.47367 | -50.23762 | 2025-11-28 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c75d282-2511-395c-8933-3ac9d8dd4e04 | -3.33941 | -50.26688 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cbf8a21-3c50-35cc-9a1c-190d3c365f26 | -3.1651 | -50.60337 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d67bdfe3-b998-3ec8-b640-50d5ecba490a | -2.4251 | -48.82682 | 2025-11-28 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddd028a8-c21e-39d7-bbe4-32bd40466e3e | -4.01557 | -42.45517 | 2025-11-28 04:31:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a6689bc8-1f2c-3101-b53f-a567f5c96366 | -5.06496 | -43.89447 | 2025-11-28 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 665f2181-6cc8-3631-8ba9-98b4d8817137 | -3.85579 | -47.03842 | 2025-11-28 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06093cc1-4b0b-38af-9692-4c96bc793aee | -2.74587 | -49.3289 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f66d3aa1-07ab-3f90-925d-40716d2c1985 | -2.61295 | -47.34933 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 025ff01c-de43-3fcd-a74e-1a213190b022 | -2.62179 | -47.35775 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11b30389-ebcd-31b7-bceb-5dc372d0a12c | -2.27782 | -45.28965 | 2025-11-28 04:31:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a65b800-53f7-3489-a2ba-b765c80217b1 | -3.45989 | -53.07409 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ab69bee-44c5-3eb7-8e64-72421d5045ce | -5.47826 | -44.69054 | 2025-11-28 04:31:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6171fcd3-1580-35d1-a5cf-5e87e75c1346 | -1.22679 | -46.20602 | 2025-11-28 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c3a38ce-1105-3b46-af0c-0aa3a639f9a8 | -2.39184 | -49.38917 | 2025-11-28 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5f50b9a-a830-3263-82f8-8c119e41ddbb | -3.7643 | -46.94954 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfd29782-f598-3fb4-a4e1-69de8d8a19f1 | -2.96103 | -51.02054 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 258fd480-919f-3ac2-9d52-a00291317437 | -4.18717 | -48.63041 | 2025-11-28 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10b3905f-4813-3a05-96be-bf377409f981 | -2.71947 | -53.18013 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc42741b-0d09-35a1-8969-5319eb133576 | -2.65018 | -46.9611 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01253f50-21a1-3ec5-a482-27a730674380 | -4.95416 | -42.67043 | 2025-11-28 04:31:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecdb98b8-0ff5-3f5f-b1ae-2ee771dc5d0a | -2.7487 | -47.13469 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d81e59e3-9a06-3959-96c9-2dccd3fcf1d5 | -2.8692 | -52.08079 | 2025-11-28 04:31:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c30dec7-1af3-32ab-a3d1-5cedb27286f4 | -2.99123 | -51.05143 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e175a04f-bd86-314c-98cc-94e89c51b151 | -1.24916 | -54.05608 | 2025-11-28 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff2f7061-8be1-30ed-871e-d69878147ead | -2.58894 | -53.9705 | 2025-11-28 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0379757-0004-3aed-a1f0-befb789656bd | -3.93775 | -50.44447 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25ee4f87-f503-36a6-8e8e-c7ec2c1ddbe1 | -2.38897 | -49.38477 | 2025-11-28 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c7c8ea0-d75c-3fa3-a4e9-377ec16e7ebf | -4.29857 | -55.61211 | 2025-11-28 04:31:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a02cdc7-11fa-3850-ae8a-0d5468b1286d | -5.30269 | -44.72312 | 2025-11-28 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3d8eb7b-90f3-39a1-aa58-5231c2918547 | -4.97395 | -50.87747 | 2025-11-28 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eec18ef-8a7e-3038-8e76-66d86879190d | -5.23267 | -44.92085 | 2025-11-28 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd5c2f84-21dc-3533-b266-356d52ca9525 | -6.66215 | -46.178 | 2025-11-28 04:31:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7662e79d-cfea-39f7-819e-48fc77b58ffe | -3.47347 | -52.99061 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03fb2d72-c8fd-3135-9030-22393833a3c2 | -2.56719 | -49.0389 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f7b901a-7381-35e4-9164-cadd6639501d | -5.40409 | -46.92344 | 2025-11-28 04:31:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5aab3c3d-d69f-3457-bc53-62daf7d0bb10 | -3.95247 | -44.76361 | 2025-11-28 04:31:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f39bb086-2fa1-39d8-af2b-fe193d1e8460 | -4.04757 | -40.44946 | 2025-11-28 04:31:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0e29aa17-5fbb-323b-ac78-f051d56defe2 | -3.83176 | -50.18529 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f99bd3f0-82de-3559-811e-ac46f89b0c1e | -4.01435 | -50.59664 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 105498a0-1d70-3d1f-8783-b8ce2fd3c758 | -3.0589 | -50.37552 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef7f16a7-d0d2-32c8-94c1-54a831607774 | -3.19661 | -45.11 | 2025-11-28 04:31:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41401c80-3f32-3cd0-8906-3872bce08607 | -3.35482 | -54.0928 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20e47ccc-dfdc-36ec-a0ab-0e085155f96c | -2.42788 | -50.28799 | 2025-11-28 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cae1dc12-9d6e-38d5-959f-59f977384493 | -8.37966 | -41.75601 | 2025-11-28 04:31:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b15d4ee2-030b-3984-97bb-731a1086a2cc | -2.83358 | -46.72232 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d72c4cb6-d234-34c9-b24b-ee233c6d9541 | -3.5245 | -51.63585 | 2025-11-28 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cebdca1f-848a-3567-a7c0-c7ea897e954e | -3.51501 | -43.98667 | 2025-11-28 04:31:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 420af787-8ead-3202-bf2a-bdf91b88c04c | -5.73845 | -47.93832 | 2025-11-28 04:31:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 885e4e75-11a5-30d0-be58-a3bebc65dad0 | -3.06585 | -50.35501 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e1bdbb9-bf0a-30d1-a7cf-1fe7ea560be3 | -3.10292 | -51.05752 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a57061f-7fbc-3882-98fa-b4f7fe28b4d1 | -2.42497 | -45.74394 | 2025-11-28 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 366f6e89-d6f5-3fcd-9e03-54b8dbfc465a | -3.32887 | -46.22932 | 2025-11-28 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 195db934-49ed-3e7d-9c55-589cb40127ec | -2.67675 | -46.85625 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d327f42a-b561-3398-8dd5-7f332f5bb828 | -3.06253 | -50.37609 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 857bad3f-716f-3f80-a25b-e34fa6bc9644 | -4.78053 | -48.42736 | 2025-11-28 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 148df863-3389-3337-a760-de63e8e03bf0 | -5.45578 | -50.75196 | 2025-11-28 04:31:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03bd3185-3361-39b1-8225-ebfc552a605b | -3.73245 | -43.00349 | 2025-11-28 04:31:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2659384e-b2ab-37ab-900b-8b4fc9da1c6d | -3.82975 | -50.10637 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0ff19ec-4103-31c3-9bee-addc4bf00b58 | -5.40463 | -46.91996 | 2025-11-28 04:31:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c60f13a9-9221-39e2-aa73-24393f05145a | -3.76099 | -46.94903 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acb3edb4-bbbf-35d3-bec7-d5bab7f3b5b0 | -5.15518 | -46.15608 | 2025-11-28 04:31:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f84c319-ddac-3310-8ec1-bf1d424406f7 | -3.68288 | -51.69815 | 2025-11-28 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29965048-620d-3145-b348-7348141e89b5 | -1.48114 | -54.20579 | 2025-11-28 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README12.md)
