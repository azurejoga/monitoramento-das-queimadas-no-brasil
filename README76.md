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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e103b33-4ea0-3442-b782-418d7eb1827a | -1.59058 | -52.27985 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e9419cab-8b7b-3e0d-b982-e658b4f1c54e | -2.83337 | -54.10359 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 911b9c84-6e0d-3810-8df0-618c4da1bc37 | -1.60618 | -52.28944 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08c94478-769e-3176-9c21-fa9cad6e2853 | -2.4439 | -48.60797 | 2024-11-29 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70c03e39-1b38-3807-af3b-91e57541e189 | -1.49299 | -52.60068 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d6d7bca-af4d-3cdd-b4ee-313d75638a68 | -1.25469 | -53.9976 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbcbbc41-eb93-3dca-805c-8587678476d0 | -3.09747 | -53.80648 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a5850a1-6deb-3d65-89f5-6d85a8822b79 | -2.72626 | -54.11456 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9958eb1c-e22e-3290-ba65-d4b72d11399c | -3.01362 | -54.03987 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65d52f8e-e5b9-3288-9292-69e6d129cb13 | -3.68132 | -51.85658 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e79c41b-2ff4-383e-a8a0-f8b64404529e | -1.06891 | -53.37967 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13efb481-62aa-3853-82bf-288e261637be | -2.43378 | -53.89594 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 932faafe-9cdd-3626-966d-1bc9c25f60ae | -3.93015 | -50.98105 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ec592ec-8473-3690-a5f5-f371e7bad600 | -2.39726 | -55.6568 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c9bf38b-f01a-33ad-b427-b1c95058022a | -3.25247 | -53.64109 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f3fe4dfe-e63b-32d8-9e7f-1d4c8ef27534 | -0.87475 | -51.71978 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28ad187e-74e0-3f25-90b7-848e476c2494 | 1.45917 | -55.92289 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32558e13-8a98-3c62-b861-21fbad6d9322 | -3.1794 | -54.32775 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0393d11-a7c1-3f0f-83a8-2968e6abc514 | -3.27189 | -54.1052 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f94345b6-7cc1-3e66-a3bd-0e1e5feeda8f | -5.98111 | -45.35654 | 2024-11-29 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1cb866f4-e8df-3613-89fe-05ab72d426fc | -1.22896 | -51.80706 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a56d284-60e7-3e86-96cd-9109000cd393 | -1.52022 | -52.49097 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c931b2a-1e3c-3e1e-be7a-cc4df9865df0 | -2.91247 | -53.90448 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34211852-f3d9-3556-86ff-c283b709a086 | -1.06413 | -52.42757 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 670a96e5-7aa3-3948-89d6-b7b9e4d9f2e5 | -1.18342 | -53.40793 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cb22fb1-e0d7-39fb-8fa3-5a712f9f0757 | -2.60453 | -46.84063 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da7d79be-1c3e-3d1f-b353-ab245179f7bd | -1.10655 | -53.57527 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 223a7f94-a4f4-3358-9e65-c280fbbeeb5a | -1.19125 | -51.76086 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cc18ab3-fce4-3b9a-973b-8ca1cac07e25 | -3.04337 | -54.04446 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f121915-4c71-3833-b8c6-db716ac15427 | -2.84516 | -46.86195 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4b50e94-2b24-3a09-aa7c-68d872080bd2 | -3.28289 | -53.68816 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27b947bc-c9ed-3f38-b09c-cd0666c5a12b | -3.91875 | -53.66822 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fd08569-2b4d-35aa-a3ed-1177a71ae285 | -1.14694 | -51.68001 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7336435-fd0c-324f-bb86-75da2a118080 | -0.99924 | -53.69577 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 492bc001-9e06-3951-b35c-0dfe5b177c9e | -1.72321 | -52.49767 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8678f2dc-4194-3cce-ab1d-f5df9a89257d | -2.8323 | -54.11049 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 910afe69-d08d-3277-afed-4ccebe099fc6 | -1.88009 | -53.32389 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92567551-6a4c-3218-80c0-ebb3a765b09d | -2.16456 | -54.48599 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 476592a2-3ffc-3044-ac31-b889ff81b886 | -2.89674 | -51.57618 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 960161fa-fa9b-313d-95be-f27581c00893 | -3.59283 | -50.3644 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e52667f2-5fc0-3731-8b45-634c3d0c9e99 | -2.53053 | -47.33668 | 2024-11-29 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1587864f-2ab7-3bfd-aa40-d6f05621c764 | -0.88149 | -51.72082 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf3df2b1-6abf-307b-a78b-cb1ee1821138 | -3.61599 | -50.18592 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8c44e7ff-fd2a-3f5b-abd8-f70ef5aa3724 | -3.10604 | -50.36387 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f930bb1-7fdf-3197-a0e3-da680ae1cb81 | -3.34931 | -49.50834 | 2024-11-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ee93817-358b-3b7a-8a15-d6df8194169b | -0.99444 | -51.7159 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01542302-4772-3872-b926-e6054fdbd565 | -2.86808 | -45.54198 | 2024-11-29 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f729c836-3c29-37f9-b1d4-82dd7e7711e0 | -3.52969 | -53.78328 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2d85b1e-d44d-3edc-aef9-4da828056387 | -2.44396 | -53.96091 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 848c1256-254a-34d5-be14-0a8bd362d025 | -2.75563 | -54.01323 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07124b80-e848-3969-84e4-08a743812bca | -1.1243 | -53.21974 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f86585a-0b0c-30e9-b1ed-2140425df4f3 | -1.24112 | -53.38941 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a47296e-6bc2-346a-ad78-cade9635b683 | -2.79353 | -54.0551 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e699fa8-7db9-3320-8bb7-240701e26ed4 | -1.3084 | -55.74492 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65bb4b1f-6c18-3116-8110-9c7e28193913 | -2.84591 | -54.0667 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83b6fc48-c84a-3e5e-937e-14f5aa0b75cd | -2.74616 | -48.6217 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ae6ac7a-4740-3885-9763-69ed7f43c70a | -1.2145 | -53.75454 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 34b4ef71-91f7-33d9-926e-dd14a72bce4f | -1.70936 | -52.63087 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80bb8b1a-74a2-336e-998e-7301513fc768 | -3.5558 | -51.67034 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d026aa3-49e6-3ff8-8798-768a95308043 | -3.8213 | -46.60458 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bfede67-f955-36fd-8275-4bade475d008 | -3.08711 | -49.21609 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bbf1b9b3-e106-3425-9664-a20ce01b6291 | -3.85721 | -50.15125 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16af66a7-4913-3d13-b7a6-b74861122546 | -2.31439 | -51.95773 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbf3f6f7-ae03-33ad-908b-626c4ca7a0ee | -1.65536 | -52.49738 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b360c487-94df-31e3-9c29-81a9715fc064 | -1.27678 | -54.5491 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4da63aac-4a0b-373c-8d03-e5065abe6f95 | -1.59828 | -53.82161 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ae88642-704b-32f6-97b3-9f8dc5719f06 | -2.97699 | -53.29181 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| d8e39ff4-b8d1-3da8-b74d-781c95949991 | -2.58618 | -54.07532 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a12d52ca-0aba-3435-ae1f-081ec1c6ff6a | -1.98051 | -52.07176 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6b86130-18b9-304a-a279-5caf396e7476 | -2.5826 | -48.08092 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1b6bf89-1f8a-3bb9-aa2f-defd6cc37a61 | -1.14745 | -53.61667 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e7b1759-9702-3677-9294-3ff3c8700976 | -3.58193 | -53.64357 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 804f6c2a-bd78-3c0c-9e4d-c73455351c31 | -1.88884 | -53.31119 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b61555d-d6bc-342a-9c5e-b9b4b3c87035 | -2.82102 | -51.95297 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18ab9a12-6c67-3382-9b42-ed3052c973a3 | -2.58834 | -54.06152 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 30ecd98a-39a4-3693-b08b-014471f6694e | -2.06412 | -50.29893 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74061383-61ca-3491-914d-91b062eb93a7 | -1.16973 | -51.92222 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b954b6b-ae09-3276-a57a-12bfe6e2a07f | -2.34536 | -53.91738 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e67aea5-39ac-3ae9-baf4-5e214d6f0888 | -4.19929 | -50.68598 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e99b18ec-e520-3c06-8e58-f73fae83a441 | -2.69764 | -51.6833 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a63e2692-8a1e-3795-85d7-148a8eaae250 | -1.3934 | -53.6308 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4797c714-f15c-3cc0-8141-d0649731c68d | -3.9779 | -46.72702 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b166b99e-fa97-399b-b105-cb23064c835c | -2.76027 | -54.07035 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a534cbf-d877-325e-9f36-2df37fe41ac9 | -3.17434 | -46.29958 | 2024-11-29 04:57:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4426cb7c-5d45-3ffc-a4d9-ba9befaad7f8 | -1.14376 | -48.3492 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81db60c9-0d02-3576-a3b0-cc8e342986e9 | -3.43369 | -51.82366 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b765fea-c710-3b8e-9fa9-3aafac503964 | -3.70623 | -47.12757 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d57d73ac-adf8-368e-b4cd-06702d59b83d | -1.45599 | -54.49381 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1e65d6c-4162-3754-958c-0b9d733de34a | -3.15684 | -49.43416 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d10f5e52-e5e0-3d56-a3d1-79764d8460d1 | -0.95399 | -51.65476 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba39c2ba-7e3c-3a19-8adf-d01e6a79e896 | -2.87238 | -46.86619 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4481f8fd-46a9-3ffe-b825-ce177af1e53f | -4.09825 | -53.97826 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4854179a-8168-35e0-ac18-3a46a1f49bcc | -0.94667 | -51.65732 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 109a0a31-b28a-3bc5-9d8d-948a19540a00 | -2.39609 | -55.66434 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3115c4ea-d709-347c-8906-0a1c70c36209 | -2.94814 | -45.72467 | 2024-11-29 04:57:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d03adb8-d2f0-3fca-8ad7-30b34e5728cb | -2.8173 | -54.0764 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77f9bcad-7e7b-30b4-91cd-8c2145fe6837 | -1.89373 | -54.54431 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3fb0dc1-3038-3238-8b4b-ed3c11818cd7 | -4.14029 | -54.34069 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c16c147c-5ed4-3c0f-8ce7-2d1701f2c2d6 | -1.60593 | -55.37557 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0010299e-c5bb-33fb-8e02-28823fe47ed0 | -2.59007 | -47.48443 | 2024-11-29 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README77.md)
