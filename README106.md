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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2bd0b70-f5cb-3c66-9e2e-e0713e17750a | -2.55961 | -54.33817 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ad1b76a-0ce4-3fe6-87dd-3577a7b758f6 | -1.08624 | -53.3582 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57615552-4b8d-3dca-905a-68a0606b15ed | -3.08579 | -49.20925 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f76b35d-5e54-332b-bfd7-09ad8c7b924f | -2.46881 | -46.56512 | 2024-11-30 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b923c924-962e-3b35-8608-4fcb11038eb5 | -1.2378 | -51.62312 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4fe28e7e-96a0-3dcb-a08c-0f6957daae3b | -3.24904 | -54.21428 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a0cbd51-8472-3865-91d7-02bb8491dd94 | -3.67348 | -54.04973 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab28a2d1-72c6-392c-beb9-a0bf9579ac0d | -1.26108 | -54.54935 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71d91c51-a248-3f44-8f79-c61d2d6e5427 | -3.07953 | -53.29109 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 075cb19d-f38d-38c3-ae50-17a4d7f30dee | -2.64052 | -54.06215 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37db1a97-d20c-32ea-aefc-497e2c1b0005 | -2.80589 | -53.05416 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fc56f42a-3cac-38f5-9a45-79d42ed61a30 | -3.64839 | -50.21411 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c0b2a65-2d0c-3859-84e8-9e527f6fdaa1 | -1.36282 | -54.65694 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 95007700-cb04-318c-b83d-8f6f001e2e0b | -1.61541 | -53.88574 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a2d2001-1f9a-334d-b6c9-208c85504117 | -2.83559 | -54.11079 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87d8b360-8b2e-3fea-86e6-8d13dd649507 | -3.26332 | -48.76699 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 767376df-28eb-3273-9cb6-b3b7c588b307 | -2.44853 | -53.66548 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e0f8c8d-0b65-37c9-91cf-c0a841d0dec4 | -2.80476 | -54.0236 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2c8e045-d798-30c3-9dc8-fe656ec6051b | -1.58006 | -53.83377 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c5324e5-ad16-32dd-ba30-3bae89107878 | -2.42338 | -53.93556 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0582937c-dbf4-3e4e-b72c-145a69c1a5f3 | -2.76894 | -52.90765 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5984a8ff-ac7d-34cc-a686-7eee39f53191 | -2.6316 | -51.74494 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 48a05c3e-d30b-3f7a-b141-98c69bab91e6 | -3.14376 | -53.84514 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bf7921f-f8c6-3407-9efa-77f2eb771684 | -1.15472 | -51.69869 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 45c1ac3a-bca2-38d5-a247-378c5cc52a8e | -1.34478 | -54.98233 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fe60039-f404-3145-b473-834cb3ab96e5 | -3.10298 | -54.04122 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80407358-1639-3287-8def-b458a3721e41 | -3.23182 | -45.19246 | 2024-11-30 05:01:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70474bad-4a64-3f4d-b38c-c172ff3d0fdd | 1.05218 | -54.64705 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f66ca2df-cb20-30af-bb39-d4b2104185ec | -1.23102 | -51.80758 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 270fe4d5-d822-301e-a0ed-7d1ac2bfb3fa | -2.59747 | -53.98752 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 19394e23-e4ec-337f-a10e-73bb9458beaf | -3.2995 | -50.35653 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 580be7c1-6381-38cb-8b49-b34f6eb70611 | -3.80901 | -46.54171 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb377f11-6463-3779-b8f5-21bb0436a710 | -1.20072 | -53.87832 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52cd8375-f910-3e65-9c07-f0660299e27a | -1.20017 | -52.56277 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02608f53-b2e2-326d-944e-47e3771815be | -1.31078 | -51.75728 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c077c94d-c28e-36d5-94d2-b34986ddd38b | -1.58399 | -53.85225 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4753428-e4ca-3696-b8a5-363f28addf6a | -2.53044 | -53.98801 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09d0e304-f2c3-3bf1-9bbc-de4815dac352 | -2.96023 | -53.72238 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 673f0e0f-23e9-3c9e-bdfb-5c18157e119e | -3.03284 | -54.03707 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8134a552-43ef-3df6-b23c-b1b49380e233 | -1.00438 | -51.73347 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56920d81-fb10-360c-a826-1fe6b07eaa49 | -1.83246 | -54.53291 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8a3ecaa9-c0d9-3fdc-880e-6064064fda37 | -3.04779 | -54.85039 | 2024-11-30 05:01:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc9b4691-d977-3752-b066-fe12ffbf4975 | -1.07788 | -53.38957 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b543e4f-e1fd-3012-acad-e27e405b1301 | -2.80226 | -54.12708 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad15e1d2-dc46-3eaf-9d6c-3043503a63d9 | -3.27563 | -50.61645 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6d77a54-816f-38d5-9d6f-aa879e2c9987 | -1.70949 | -52.76426 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba94d297-aea5-301b-92bb-98d1107e3c5a | -1.64632 | -52.7476 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22f04aff-5874-3fe1-a58f-4d98f8af038b | -1.19269 | -51.77304 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e497131f-b298-3d5e-9488-9ea87372423c | -2.53443 | -54.02798 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a64a94c-0bd1-39e1-8a80-9c2d37c124bd | -4.08154 | -50.03602 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e234e42-bb6e-34e6-ab2f-302321c53d17 | -3.38819 | -50.31985 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15fe6333-25c4-399f-8545-f0c7faa5c1de | -1.14256 | -53.666 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 323104d1-5f48-3b73-951b-aa7c45b78057 | -3.08918 | -53.29634 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be0de8b7-b3df-309c-8df8-8bce5faeb898 | -2.60536 | -54.24227 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f58e28ed-bf2d-3197-90db-e039579d895b | -1.5887 | -52.28775 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9d061b9-919a-3471-8c3b-1969cdbd2d4d | -2.87266 | -53.98384 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a91ada47-76ab-3010-b6fc-cb47d8e8dd29 | -1.10028 | -53.4003 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71732ab3-c0e7-3f38-aed8-6c85626ae20d | -3.30509 | -50.37286 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1666d208-0aa9-3111-b122-396b8d321fcb | -1.36775 | -53.63277 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ca12db3-a188-318f-8d97-74bad7c42d80 | -1.59688 | -52.28115 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f151250-a625-39d1-82c1-2850bcd9d2a5 | -3.17955 | -53.00342 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acd22d39-1aed-3331-a9e6-fc12d9910b2d | -3.0904 | -53.24401 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91054376-d0e7-3ad0-a178-cea0420432f2 | -3.67479 | -47.12539 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7517ae72-1dd3-35b6-8c7b-e71f78fbbec5 | -1.61596 | -53.88226 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 585935fa-75e1-3856-b929-079bdc75ed75 | -2.45923 | -53.70703 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29d9a998-a797-339c-9718-3bd9a1c6a18e | -3.09195 | -50.35659 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 617fdac2-d2e8-32dc-91b1-598dd5249f1d | -4.69011 | -42.37076 | 2024-11-30 05:01:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d5d4d79f-c82b-3a63-bb7a-886acc8a906b | -2.43468 | -54.01611 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bfec2e3-0809-3614-8772-b570ef089414 | -1.16245 | -53.5829 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dadb1346-f1ba-3299-8705-84953bfa47fc | -1.36775 | -51.97355 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 215362a1-5c6c-3a72-ae61-6163f48ce172 | -3.3215 | -54.18235 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| da7d252a-f0a1-35ff-9e9d-27678de73188 | -4.18791 | -50.68243 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e36d5b8-012a-304e-a1cc-73be7f6f0cb0 | -2.83041 | -54.03475 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e4856ff-9c1c-3938-9410-3589901f7ba1 | -1.11023 | -53.22723 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77f05e5a-3221-315a-8868-6436f5f6e31b | -2.91229 | -53.06685 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f38997e3-8993-31b3-af51-8824a5e1a4fa | -3.58271 | -50.51244 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06e434fc-0cda-3ce6-8574-739059632d4c | -3.4574 | -54.56694 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d5743045-be63-3b98-a32e-07863dfd25f4 | -3.24026 | -50.9465 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65b9a796-8e87-324b-8473-7a23f472b781 | -2.02492 | -50.77211 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e92eb5be-4d1f-3d0d-9c71-efc62dfcf76d | -1.55617 | -53.51755 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 872e0c4e-6119-3778-8a4d-7e6139cc22c5 | -3.60513 | -49.9844 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 610adbda-41d1-3cdb-99cb-2c3fd740a28b | -1.10067 | -53.22208 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bed72c8-8523-3806-ade5-e2bd2b8e3bba | -1.60146 | -52.29759 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de4a073e-4c5b-3941-bcd2-086018b2bfb9 | -4.45171 | -46.35319 | 2024-11-30 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7b8e5b4-09fc-3809-a799-750a9f546899 | -3.67396 | -47.13097 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eda59a37-c962-35f3-aa41-c4789ac9b34e | -2.74626 | -54.07919 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d02bd06-d24f-3267-bce3-4bbc97adb21b | -3.20031 | -46.58054 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8225a0a-4202-3ad7-8f08-c93d91201408 | -2.26335 | -53.4654 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4108e805-31c5-33a1-9dfb-f7ab6615121d | -2.18088 | -47.14764 | 2024-11-30 05:01:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 905c90ab-2992-3297-b6c3-e0bfff2c7b0b | -2.90556 | -54.18232 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15168575-5cd4-3b32-98df-1da6dcb5a3e4 | -3.91721 | -53.67048 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72420570-1bc3-34f7-8175-ae8991295fca | -3.8243 | -46.55521 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5896a936-268b-3d90-a896-442987e9d91f | 0.97945 | -50.1247 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 686f16aa-eacb-32ce-87a9-6ad29ed97c56 | -1.90811 | -51.07853 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8251781-7091-3e4c-886c-587b04d0ae61 | -1.35237 | -51.38764 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1284c29-d1fe-314d-be0c-2e31d0b6a497 | -2.86549 | -54.02943 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70808efb-787a-3656-9145-b0dfb9035e01 | -3.24143 | -51.55777 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55f470a8-575e-3882-b043-255052f3af15 | -3.50542 | -53.82767 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8afa0bb-daab-34e4-a07b-274e5e260ede | -1.37027 | -52.11685 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36bcba33-b985-3398-a2d5-721ca4518876 | -2.80093 | -54.04812 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README107.md)
