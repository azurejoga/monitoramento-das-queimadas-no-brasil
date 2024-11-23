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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b232396-c6df-3f29-bdbf-bbbdb2327ac6 | -3.31599 | -53.28518 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71835fac-94ce-326d-b60f-a429b37eefc8 | -1.67406 | -52.66398 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 974e51b4-7d8f-34af-8a5a-4cc1cc252d83 | -0.95536 | -51.71834 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b349dc8-97c2-3c8f-a52c-268906829bd9 | -1.44632 | -53.39112 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2df83a4-71b1-3d29-bddc-4325bd700c0d | -1.7848 | -53.63483 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50e2ea3a-17f9-3737-85b1-fa7d2489e193 | -1.63974 | -52.70104 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9605ef88-838b-331b-a3de-6934264cba1b | -3.24644 | -54.22257 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d54c0737-79df-30ff-a15d-b8b9d91905d5 | -1.12939 | -54.17524 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 377fc630-5cee-3efd-8099-d1f947b16f1a | -2.20644 | -53.67456 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac6f6f40-bed5-3bbb-9f7f-a11117689308 | -2.20347 | -48.91441 | 2024-11-23 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80b1a628-18b1-3bbd-9cfa-47c6d2e6a90a | -3.31651 | -53.2816 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50eedc72-29ae-3edc-ae9a-a485138d596e | -1.04621 | -51.74337 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ef872b7e-4a68-312c-84a0-a5b392ced0de | -3.30434 | -54.48929 | 2024-11-23 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 668786f9-74de-309a-bf4a-d19b7f4dd23f | -3.24599 | -54.22568 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12b18bd0-7ce9-3a80-86c1-53e7f57937f0 | -3.29473 | -53.85333 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b29d439-27ca-3315-a7a0-6be9cb75b77f | -3.24553 | -54.22879 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5cdfa3fb-db73-3933-ac50-3f38f20c22f3 | -2.68094 | -52.06956 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 405c7e24-6e98-346f-a2e3-b5f29f108930 | -2.16391 | -53.77678 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca6c73d8-010b-388d-8107-165a29e95477 | -3.24935 | -54.23902 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e349c66c-7fe9-3076-957f-fc9d440fbd5a | -2.74191 | -54.12992 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe7fba12-d943-3e81-9f48-84cb623d589b | -1.43612 | -53.38616 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e48a847-d4ac-3a64-819e-4d072213f415 | -1.43355 | -53.38652 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5d38a66-3542-3602-9c40-07baf0f67b4b | -1.25902 | -53.3609 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94294f3d-82ed-3b3f-b8c3-0ed8110d6212 | -3.25072 | -54.2296 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e689a15-121d-3e99-bcc7-0ced98e2d39c | -1.45117 | -53.3952 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 2b135858-4566-3983-b03b-f8843a38e7c5 | -1.03901 | -53.17388 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2eb1c25-afaa-3f84-9270-f50fb341c7ef | -2.19883 | -53.65313 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed192ecb-3736-39fc-a79e-1338b1a3a72f | -2.89823 | -54.01092 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a4e27c9-2b2f-3e54-82d4-b45c6e5cdae0 | -3.58207 | -54.5167 | 2024-11-23 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 19267099-6a61-3a60-ba9f-18c9025acc40 | -3.27008 | -53.81699 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf09341d-ca95-32db-a4bd-eded395674d5 | -3.24417 | -54.23816 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a06fe95-c4b6-3443-a7e7-a88e7d67a8f1 | -3.00794 | -51.55125 | 2024-11-23 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16a94ddf-8e98-340b-bd99-db36a06031d3 | -3.50491 | -53.79953 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95141568-466a-3632-9826-cbbfa6494c74 | -1.9848 | -53.13474 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad22799d-0f9a-3643-985d-bc433aa1ceaf | -2.76631 | -54.0732 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36a5aaba-53e6-38fd-adca-75f536a570e5 | -3.00726 | -51.55591 | 2024-11-23 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 103235d6-ba46-3fea-9162-3284a5b3650a | -3.2906 | -53.86161 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2c82bbf-8b1c-32e7-82d8-d5c3c5c9c5ef | -1.11533 | -53.40003 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9124def-006b-34a5-98c1-e5887ee4da9f | -1.74581 | -52.38218 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ef2ef5e-a975-3f92-9809-070aae2522bd | -3.26371 | -53.82305 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9f439ab6-ffa8-32f4-9217-58b436dc3da1 | -1.67093 | -52.66299 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c091c18a-df4b-34a8-b012-4097b6931d9c | -3.25045 | -53.27274 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d92a89a-48b1-303b-bc40-6a2dadc06718 | -1.1149 | -53.39292 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d7fccd4-f7c4-3849-bc1b-4a29f474bdcc | -3.31904 | -54.09224 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b5091bf-fed9-302f-a997-87bed94b7d90 | -1.61653 | -52.60424 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3003411-c90b-3cf8-a21a-1980204495dc | -1.04045 | -53.17529 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27ef7cda-4338-3a80-8631-0819c4a28dfb | -1.20834 | -54.03404 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad39c316-99ba-3748-bf94-8ec29d2245d5 | -1.66221 | -52.70453 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b902954-dbd8-3c34-93db-7d040cdaa868 | -1.67598 | -53.20483 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8557cf1b-8d9d-392b-91b7-651cec2663d8 | -3.06655 | -53.2272 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c200766d-3198-3397-8e99-f39faff3eda8 | -3.24186 | -50.66933 | 2024-11-23 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| baf6ede6-1d3d-352f-a2c9-8fb1b88b5403 | -1.11108 | -53.3925 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b538d42-374b-3c72-a0c5-b365a91df282 | -2.62354 | -51.79501 | 2024-11-23 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47233106-076c-3504-88d7-36e34a079a1c | -0.92161 | -53.09734 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 006c632c-ef9f-352b-8deb-d89f59e3beb0 | -3.50222 | -53.8032 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e27c8593-f9ce-3cff-824a-59338d119e45 | -1.14043 | -53.40403 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c91ee4a-08a9-3c4c-b2f4-a96982dd519c | -3.25118 | -54.22647 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3f13b59-5e19-3f03-832c-085d6fcd0e0a | -1.66956 | -52.65554 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbd30ba4-9495-37e2-88cc-c753362e7fec | -3.50348 | -53.80949 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e6e2578-74f2-3649-80a6-181651b0a8a1 | -3.22497 | -53.93676 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59bf95b1-971c-32a6-a905-da6ed7ffa5a2 | -2.89775 | -54.0141 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fd0cf39-7dc7-3f74-ae71-c125566c0689 | -1.12013 | -53.40408 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81894940-d452-35ce-b2cd-c4c1ee71b731 | -1.20283 | -54.03593 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dabfeb62-6886-35eb-a885-9b7c2e415470 | -3.05818 | -53.28197 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02ac330e-f350-330d-add0-29cddfa9eacc | -1.73292 | -52.73077 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a5c0dddc-ffb5-30bb-a392-a8077f74d55f | -3.50564 | -53.81681 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dde3320-2ab4-338d-8a08-dba91a3c3398 | -1.6146 | -53.31483 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bef853da-af8a-31d4-b41f-e4e718a3cb55 | -1.64535 | -52.70194 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31831a0a-96d1-3711-be69-2667904b3d33 | -3.0642 | -53.27812 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad5d6231-8aa9-3bec-8b78-341f60a2116a | -1.28265 | -54.54256 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3c85fb39-ae46-35d3-b8e7-f13c552f367a | -1.13514 | -53.40303 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 683aeaf6-5a4c-39c2-a10a-b236ba797db8 | -1.12453 | -53.40125 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 215e3759-11e4-3f7e-b5c4-def1c720e405 | -2.20694 | -53.6713 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e384369-2718-312c-b2bc-aae52988429d | -2.20773 | -48.91322 | 2024-11-23 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdff4616-1bb3-3688-80c2-a4ce95459392 | -1.19243 | -51.93868 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53232f17-395a-3b32-9fc1-6ea6054fed6c | -3.25026 | -54.23276 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94c53aea-0f2f-3449-8aa9-2db6977b4928 | -1.60306 | -52.57875 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c234f668-047b-3226-a5b9-24bc32d80d85 | -1.13033 | -53.39887 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51ef5da2-b291-3717-b44d-68d8974f87d5 | -3.09622 | -54.29301 | 2024-11-23 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cdc050c-2b29-3b1f-94dc-2f1fe4f311c6 | -1.4098 | -54.28131 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6348eec-c807-3134-9581-0bb5e7768781 | -1.18269 | -51.9628 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aae46f4a-e959-3688-bd7c-11ca3e6e9cfe | -1.64039 | -52.0973 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d236d4f2-f1f6-3e93-93e9-e56da1a8aa09 | -3.84474 | -52.38919 | 2024-11-23 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e826509c-8245-328e-9430-b495f90f1d2b | -2.82709 | -54.02437 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9cbef7f-8ef8-31bf-bbb8-24b2e5a0bb79 | -2.85733 | -53.96726 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd7c362e-f270-3c3b-98d7-d4de19ece97f | -2.73673 | -54.12913 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd66e1d0-ae6b-3225-8440-e8f0b9d36972 | -1.54869 | -54.33702 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 741da076-03cb-3c9e-b6d1-14f06d8bb218 | -1.03846 | -53.1773 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8c74a1e-dcf0-3608-b293-b156596eb6c2 | -3.24462 | -54.23506 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b73e997f-85c4-3304-8241-9d539aeb1dad | -1.7217 | -52.72906 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c6fa645-a1da-35b6-a0a1-ec4b38567f9a | -1.61146 | -52.59956 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5f7e9acb-4273-335e-b1cf-b8f9caeb6956 | -2.82661 | -54.02753 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a83e3727-3348-3ded-8916-5b7403e46c60 | -1.04688 | -51.73913 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f975b23-40f0-3ef3-8d45-6ca81fb64ef5 | -2.82564 | -54.03384 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 45d70cf1-e7b6-3324-a4d2-ba73207975fc | -1.61998 | -53.31567 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 016233c0-b68f-37b7-909d-3b580f92faaf | -1.72847 | -52.72244 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0db6d4d8-587f-3ea2-9858-3cca38a21f94 | -2.82041 | -54.03307 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 77090df9-0232-3be3-a9e5-23dc500f1def | -1.29391 | -51.73255 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3152105e-0445-3d74-b3dc-67955a9ad4f1 | -1.60464 | -52.60632 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d9b10a73-1047-38d5-8da2-4b49b79289c2 | -1.73466 | -52.71956 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README64.md)
