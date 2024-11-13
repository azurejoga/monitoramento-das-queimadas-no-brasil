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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86aa5881-f03e-3363-858c-553fc3c96fb3 | -1.63496 | -52.52227 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 317441dd-35ae-3ede-ba83-1f20f45f9d55 | -3.62066 | -54.79475 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3eaffa34-e466-308b-8d23-145f324f2c93 | -3.02334 | -47.97782 | 2024-11-13 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a2ceae0-d3d6-3fc9-bd33-9b376267bde2 | -2.72933 | -51.74307 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8aa64c4f-a347-3194-a9de-f2391f938cb2 | -3.07605 | -53.27416 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c411307c-2b41-3f53-a244-07c664169bbf | -2.73436 | -51.82934 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 159b27a4-3b76-39d4-bab0-a8d5d784dcc4 | -2.95861 | -53.72004 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf574a6d-324e-36ab-8908-67ef896edd0a | -2.68809 | -48.66122 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0877f4a6-7b32-3aca-ad78-40a72ae445ea | -3.62919 | -54.11034 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee854073-c90e-33a8-a052-507b3bbdb627 | -4.33238 | -48.72234 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27846487-0347-3478-89fe-d01a2444413c | -3.26394 | -48.76191 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed389f7a-fde2-3476-b5dd-5748e6d43cf7 | -2.94343 | -48.31621 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c9cdda6-5aae-3dc8-9820-5f71de11ebee | -2.38884 | -53.66578 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b612d22-b16e-3d7b-b660-55c1762622c5 | -3.53898 | -51.27327 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce199fd7-27ea-3e5c-978f-3d49198c7a8b | -2.65354 | -49.43724 | 2024-11-13 04:57:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39613c78-9587-36bc-bba2-f36fc671cf6a | -2.12298 | -50.67992 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4a90060-cc8b-323f-a845-1a2524be8945 | -1.96698 | -52.13569 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4b51add-85a1-3a1b-8164-64df15a431aa | -2.6644 | -46.82119 | 2024-11-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b21a7604-871e-33c4-bb34-41199c49ed37 | -2.3027 | -53.87059 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0856c5e-5117-3c6d-b40e-d511ededbf6c | -2.76957 | -54.73396 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23470813-8064-3fff-aef2-1d62ee322db0 | -2.59978 | -51.71987 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c7624c2-4ece-3f70-9fd3-b9ac288b802a | -3.10191 | -54.30709 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 36fcd2f8-c3a3-320b-8c00-74a010cac3bd | -3.20297 | -51.03276 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6daf49ba-e756-37d5-8e15-ba95d4b689d2 | -1.88955 | -51.29858 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a99635d8-c488-31e4-bc8a-fa3a82a89cfc | -3.798 | -52.09842 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 402d05b0-c188-383f-ae86-cfaac134d1a4 | -1.98989 | -51.10122 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c9c49b8-4e2d-329b-9e8a-5b69ca737138 | -3.41974 | -51.06026 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b91d4d74-3ce3-3ca7-a25d-1cacdc548b32 | -3.81028 | -52.35582 | 2024-11-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 114398cb-e09d-3321-a27a-fd5f5d40af76 | -1.64884 | -52.54221 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddbd14e9-4f43-3a52-bc1f-6bd4b70db1e6 | -4.33246 | -50.42253 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 80c0a67a-ebb0-3b93-907a-911757016a04 | -2.17962 | -52.73849 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ebbf7c3-dc89-30f8-aad2-88459165b7b1 | -3.7681 | -54.65705 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8f10eaa-507b-3d62-bd61-0bba94b6be4e | -1.61523 | -52.23324 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5e3fa99-851a-30ca-986c-1044366aeec8 | -4.12837 | -46.85555 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1918be6b-641d-3174-b94d-a1a6127295f4 | -1.6588 | -52.54374 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 728f7f3c-fd13-3902-95d1-0fc1de7bde79 | -2.78955 | -51.40207 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d2dcc20-6dba-3201-a898-fa89a3e93874 | -2.59768 | -48.29187 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41d4b392-cf17-3883-9035-60a065754a6f | 3.376 | -61.19874 | 2024-11-13 04:57:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65a98cec-136d-3638-9968-49b4c68a857e | -3.28938 | -50.75193 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01446f39-35d4-3948-b840-afd866357dcb | -3.0233 | -51.09162 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c32ecc8-e688-3fdf-b0c2-181f4f3e4ef8 | -2.88647 | -46.81158 | 2024-11-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 984039a1-0f33-3c70-a8ca-8b179166235e | -2.7321 | -49.37917 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64675afe-2206-35f9-9596-84a569f8733e | -2.9299 | -54.34015 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05c650a9-640c-3143-98c2-a326b79639c3 | -1.65601 | -52.53976 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1b06edab-3c13-3fb9-9546-20f2704a8a85 | -2.95757 | -53.86063 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58a18b80-c333-3982-925a-8f8ac1d31de6 | -2.90727 | -53.94066 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97a89cc0-5d0d-3775-89e6-f9a39493f252 | -3.16553 | -50.58805 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed0ba207-d7a9-3f28-b744-263fd970f1c2 | -4.21885 | -46.45507 | 2024-11-13 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b658d2e-eeea-3cc2-9b2c-6c755d880625 | -3.05066 | -50.33004 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7894f181-bc8c-3428-bd61-7b1b7a26c220 | -3.05858 | -50.32695 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d316e280-0ad4-3351-8548-df91d8eb45ce | -2.97634 | -45.16225 | 2024-11-13 04:57:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c9e3690-df65-3b52-88e6-bb0bbfe55a17 | -3.81946 | -51.26636 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 046500fc-3a47-3709-8b39-d52ff725510a | -0.97358 | -51.72493 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f9dc298-d99c-3c12-a267-854484643037 | -3.15189 | -53.24355 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e319ca79-85af-3f5f-b5c0-820d9ab98b60 | -2.3182 | -50.68302 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcfe25bb-aba1-3086-900f-b5739137afe2 | -4.45711 | -49.65667 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f69b763-f4f4-3943-8512-178af923a64c | -1.21568 | -51.78017 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ed9466b-db50-3e19-ace0-78cceb104a1a | -5.35124 | -43.52971 | 2024-11-13 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fcc66d4a-5cf7-3560-a54e-c075707a1141 | -2.34499 | -50.58039 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1830a1e2-8ebe-3979-8b18-e41f29f8f622 | -3.97808 | -50.93622 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d0dcc5f8-97e9-303f-afbd-2012deaa9fbd | 1.5826 | -55.80256 | 2024-11-13 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e89d9f2-d6d7-3150-bedb-6b7e74c75ace | -2.81838 | -54.00732 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14e955b4-1d49-3bf5-af4c-dc39685254b9 | -1.19439 | -52.1397 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56fb5be7-b93d-3a0b-81a3-66acb20b0060 | -2.54797 | -53.97602 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 309b898f-4ea9-3c6b-aa0f-88b918e7f1a6 | -1.78321 | -47.84166 | 2024-11-13 04:57:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3cf1e47f-6d3f-3187-9c2b-5fd1cfd97fec | -3.08864 | -53.25849 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9915cc3f-c665-3030-b59c-69682b49e4c9 | -3.08054 | -50.3336 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61b88538-93bf-3c85-991e-c358d24f9dc7 | -4.47231 | -49.6345 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9f89419-22b5-387e-8691-1f74711e5e0f | -2.838 | -51.97549 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f5b82c0-f273-3184-a768-ede0e1076a10 | -1.61577 | -52.22972 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48dd56a5-a7f7-32b7-9efb-b1a9f5b95d8c | -2.27155 | -50.67992 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afc489f1-9a52-3b10-a83e-5effd7d1346d | -3.24375 | -50.31767 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| adc20a55-54c3-3ce1-8316-ade7d533747c | -3.22924 | -54.86333 | 2024-11-13 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7f1bdb9-77df-3654-94f7-e6ed912b78d5 | -3.05363 | -50.33484 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69f750c5-94b1-3e60-9091-c6fad1348bcc | -2.98994 | -53.97818 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95b13c23-5717-34f2-a581-95ea10f9ae80 | -1.40661 | -51.58413 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 369a2928-758b-3aba-a039-8ebb8fd9aa43 | -3.43677 | -50.30487 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4430b9fd-8859-3a1c-9acb-5f26e6048b30 | -4.52183 | -48.93262 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7d87860-6960-3df9-9661-1172b502a2ad | -3.10577 | -54.30413 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1a9350d-4534-3e85-aa84-2c0a2f3de097 | -2.40959 | -48.83485 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c63eb7ee-ef8c-3f21-b2b3-bef0ac7ad2e7 | -1.04275 | -49.31839 | 2024-11-13 04:57:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e3d8790-5d16-3797-8d95-bd0bc6d280d9 | -2.70197 | -49.34562 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e4ebdcf-e93a-3f45-b4cc-cb6524caa4ed | -2.89911 | -48.31016 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b539f5b0-ccab-3901-a619-1a2e5e7aacfe | -2.78668 | -51.39778 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59a80bfc-e3e9-3e55-ba54-873c4e11c395 | -3.22313 | -50.37948 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ee401be-8e81-346e-b024-9cd12ad6b7a8 | 1.27052 | -50.67559 | 2024-11-13 04:57:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 292e7ce0-544b-383f-849f-835545b37aba | -1.52093 | -51.30033 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdfe93db-3545-386b-ac31-376fa7daf86c | -2.55946 | -51.23202 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1abe1b16-4a2d-39fd-a330-c8ab7b6c0461 | -1.62448 | -52.65557 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1db955bf-1b80-3c6f-b937-99b114f1daa5 | -2.11883 | -50.68335 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6cce4d2-db0e-30f0-b919-6473c91c6374 | -1.38946 | -52.39502 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58e0180c-b107-3caa-967b-aa01a1015834 | -2.84465 | -53.97327 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75310ccb-6001-38a1-a521-fcc838266fb1 | -2.56805 | -54.04261 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ef5da94-b17b-3118-8af0-ac42a432e5fd | -1.62688 | -52.22424 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3c032c6-97ba-3c76-81e9-676da2075e78 | 1.00765 | -60.57345 | 2024-11-13 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ce73ebc-a2b1-3549-b19e-77bdd9d879f0 | -3.83551 | -54.59631 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d49b2497-4b79-304e-a7a7-4196ea61422a | -2.31466 | -50.68247 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70fe3e56-ae4c-3da8-88da-36e057ed6bb5 | -2.65894 | -51.7247 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a2ebd5c0-687c-3ed4-b8e4-26821c676246 | -2.87447 | -51.82857 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d763447-ad7b-3359-8036-093cba1613f9 | -2.45016 | -53.68931 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README30.md)
