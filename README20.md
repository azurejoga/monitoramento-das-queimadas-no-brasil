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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3483dbf7-a5a0-385e-b732-6b1ed1400fc7 | -12.64405 | -43.44479 | 2025-11-18 03:32:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9e75396-6621-37cc-bac1-75852df8685a | -11.42492 | -43.33178 | 2025-11-18 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46498924-2ee2-3378-a803-85a9436dc8a6 | -22.86528 | -42.39567 | 2025-11-18 03:34:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3968f60f-62f5-3b39-b8eb-b14437d801c5 | -22.86377 | -42.39406 | 2025-11-18 03:34:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 37b5498c-a2cd-3fac-9fde-ae5416dfdf7a | -20.99583 | -41.51833 | 2025-11-18 03:34:00 | NOAA-20 | APIACÁ | ESPÍRITO SANTO | Brasil | 3200508 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 42e8784c-194c-3abe-b2e5-22bb4b242339 | -4.1764 | -44.2257 | 2025-11-18 03:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 21f024da-151b-3428-84fa-cbc907aec984 | -6.1138 | -42.9569 | 2025-11-18 03:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 9fb63cb8-1d3b-3e3e-b4c2-0afaf939154c | -4.195 | -44.2247 | 2025-11-18 03:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| c0c719b8-8432-3370-9752-62a5ae6be4f1 | -9.3969 | -48.4523 | 2025-11-18 03:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 3b62d11a-240a-39b7-84e0-6760155f70fe | -9.3969 | -48.4523 | 2025-11-18 03:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| af044ebd-bf2e-33d3-84c4-2f470d7c9a78 | -4.1762 | -44.2486 | 2025-11-18 03:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 844a5ba4-0c7d-35fc-a9ca-a7c8dbe2e502 | -4.1764 | -44.2257 | 2025-11-18 03:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| f11b2689-9c42-3b91-a709-0cfdcb26d148 | -4.195 | -44.2247 | 2025-11-18 04:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| b23dbe65-f53f-3be3-97f1-5f97dc374a8b | -9.3969 | -48.4523 | 2025-11-18 04:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| e8db645c-7a09-3161-b9da-248c3f3f329c | -4.1764 | -44.2257 | 2025-11-18 04:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 3e4ab60f-2593-3b3e-9b14-585137ce024f | -9.3969 | -48.4523 | 2025-11-18 04:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 8a400e5c-0fdd-3170-8d63-82d21477dec8 | -4.1764 | -44.2257 | 2025-11-18 04:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 0958f0cf-002d-3fae-8756-4ce360b21a61 | -2.52634 | -51.18553 | 2025-11-18 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b962f423-53a2-32df-aa4f-794c6a3f30cb | -3.24996 | -43.04164 | 2025-11-18 04:18:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86c3465e-6ae6-3970-a485-0c470fc5a214 | -3.4007 | -45.83121 | 2025-11-18 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5140e672-b748-3ebe-9399-b5e4e9982275 | -2.98124 | -51.07751 | 2025-11-18 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 745279ae-b217-35ea-9a79-8af904b64732 | -2.81082 | -45.14507 | 2025-11-18 04:18:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 718d7028-e2a8-312c-896c-48c4e101b6e0 | 0.05411 | -51.11399 | 2025-11-18 04:18:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c26d2d3-be34-3db4-91cd-8cf4c961e9c8 | -2.51624 | -47.81822 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cce03a52-7d88-3361-8622-10c79f9ecae1 | -2.51772 | -47.80893 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b4fe2a8-0fca-39a0-8255-12e0e68bd4e7 | -1.42357 | -48.90522 | 2025-11-18 04:18:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fe4cc66-a045-3eff-8a17-bbf33278af19 | -3.35121 | -44.39503 | 2025-11-18 04:18:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 10a40d41-aec9-33c9-be6e-7ac6034aa915 | -3.59741 | -43.60595 | 2025-11-18 04:18:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35fa36a2-a41a-3d70-8f5d-0e1830050639 | -2.98673 | -51.07325 | 2025-11-18 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ec2baf7-a348-3289-b8e1-c61e31be96c4 | -2.50482 | -47.81656 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0855960b-1172-350f-99ca-083690a2b632 | -2.12962 | -46.27977 | 2025-11-18 04:18:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 000b6247-129d-36ea-9ed6-3317a69aae1e | -3.93756 | -41.7271 | 2025-11-18 04:18:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c8f7e4f7-565d-3058-a771-e01835fe75ab | -3.35506 | -44.39209 | 2025-11-18 04:18:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bb7a22f-ea6f-38b6-9a3d-fa61ed8157de | -2.29471 | -47.23194 | 2025-11-18 04:18:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 79c42d68-0ab4-3977-bc9e-bbee358b5f54 | -2.28173 | -51.93438 | 2025-11-18 04:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2521220-304a-3990-b797-c490bafb16aa | -4.23075 | -43.22988 | 2025-11-18 04:18:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba1db3f5-7c38-38f3-aa2b-6e7ff9a92b0d | -2.80958 | -45.24007 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e258c88-60cf-37fa-952c-b3b0df5fd098 | -3.02566 | -44.47461 | 2025-11-18 04:18:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43a82cb2-3315-3d80-b758-236123d4683a | -2.52532 | -47.81014 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7a52348c-e7af-30c6-99f1-4382419d070a | -3.47925 | -46.06818 | 2025-11-18 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4e9c10b-7072-3ab1-bd88-23c606fb476d | -3.60402 | -43.60697 | 2025-11-18 04:18:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26f30d46-bcc6-393e-929a-aa4f54c820a2 | -3.98276 | -44.31475 | 2025-11-18 04:18:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07051da0-754d-3011-93ea-f1af5211d205 | -2.99705 | -51.00949 | 2025-11-18 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e47d94a-74fe-3adb-bb40-a721f4e5fb69 | -2.82626 | -45.41975 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 292dd144-0589-399d-902b-9317c702fa72 | -3.35561 | -44.38865 | 2025-11-18 04:18:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 795b4534-0861-3f39-bd80-cd1ab633c1e9 | -2.86843 | -49.46894 | 2025-11-18 04:18:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed5284a8-c1c9-3722-851c-4183b0e8a072 | -2.45214 | -53.80461 | 2025-11-18 04:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95ac76f8-5349-36fa-acae-0ff6b61ce9bb | -3.08099 | -50.34879 | 2025-11-18 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80458bfc-e628-337c-b1ed-f44f1194ab52 | -2.45782 | -53.80552 | 2025-11-18 04:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdfe0ae2-b5b7-33b1-8fcd-8a0915485510 | -0.99169 | -47.07841 | 2025-11-18 04:18:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8fe9884d-588d-32b9-91ed-10172fb39b3d | -3.25714 | -43.03918 | 2025-11-18 04:18:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| fb66f0ae-88ed-32ea-88d0-d6d623b2ce38 | -3.38106 | -41.17844 | 2025-11-18 04:18:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0e80e566-d624-31a7-86ce-d6cfc1045250 | -3.177 | -48.02743 | 2025-11-18 04:18:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 01798dcc-b672-39ff-9ada-70d65c6805f2 | -1.32188 | -49.32073 | 2025-11-18 04:18:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 99283beb-71f2-3c54-878e-9a7c13ffa1f9 | -3.39728 | -45.83068 | 2025-11-18 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46f405a5-a9d7-3d3d-b79d-4423cc3a3886 | -0.83163 | -48.64269 | 2025-11-18 04:18:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 82485fd8-a150-3309-8811-f84c2f35d94f | -4.13916 | -38.34762 | 2025-11-18 04:18:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6b65a356-ec6e-3a89-96a9-89eb96622c55 | -3.03174 | -44.4791 | 2025-11-18 04:18:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3bda8e20-cb18-3a40-b4cc-30de6332664b | -2.75682 | -48.42733 | 2025-11-18 04:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00f32c02-6da3-36c7-a75e-f35a336a7c42 | -3.25104 | -43.03468 | 2025-11-18 04:18:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d9bd0f08-751f-3a72-8003-c7a98658d543 | -3.59464 | -43.60199 | 2025-11-18 04:18:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c939db36-ab96-323b-8bf7-9154a304bbe7 | -2.99881 | -45.44246 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9ddde8d-9b1b-3f09-a72c-b8a2590a9a54 | -2.56684 | -48.53016 | 2025-11-18 04:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c61ef872-77c1-3778-9625-5477c9a13a36 | -1.43184 | -48.9065 | 2025-11-18 04:18:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eddcd3dd-ad45-3860-a356-186cee8b7057 | -3.07582 | -50.3525 | 2025-11-18 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49721600-91e5-3ba5-999f-9babc6a3d44f | -1.86996 | -50.96225 | 2025-11-18 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b10f3af-de1e-3619-aac7-ad9166bff304 | -1.4277 | -48.90586 | 2025-11-18 04:18:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2e2f47db-b3f4-3308-b574-62c856134ea7 | -4.29709 | -42.1236 | 2025-11-18 04:18:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 725b7c1f-e965-3db9-9e77-3ce65dbad045 | -3.3479 | -44.39452 | 2025-11-18 04:18:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1d327d19-d2d7-31c0-a180-9285b3dbf77b | -2.82288 | -45.41922 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00faf6fb-495e-330c-93b3-229a778063d8 | -3.17405 | -49.80389 | 2025-11-18 04:18:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18dc8b4b-51b7-3f8d-9aa7-511f09eab712 | -3.25382 | -43.03867 | 2025-11-18 04:18:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 088dd8ac-2d86-383f-9f07-5c72806c7f94 | -2.82908 | -45.4239 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9d0b9475-6aaa-31c5-ba86-17c7fa89725f | -2.49471 | -49.33622 | 2025-11-18 04:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38011656-52cb-3f64-96ca-260a72ad243a | -2.49767 | -49.34457 | 2025-11-18 04:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdfc82d2-1ef7-320d-9b0b-b652003b2649 | -3.4306 | -42.42189 | 2025-11-18 04:18:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 286ed3e7-b554-366c-9d58-d81998404937 | -3.02941 | -47.83768 | 2025-11-18 04:18:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4995df27-bde7-3aa1-90e8-ba85f5de891e | -3.17397 | -48.61108 | 2025-11-18 04:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2154a62-a858-34ed-ab2d-0e0934fe345d | -3.58472 | -43.60046 | 2025-11-18 04:18:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| add825f3-faaa-336b-9acf-d6a5497b8d56 | -3.06151 | -49.36953 | 2025-11-18 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c9333ca-66d5-341a-bedd-9edcbcce8621 | -2.77557 | -48.65754 | 2025-11-18 04:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85075846-f5ce-31c3-b0ac-84930bd5329e | -3.35176 | -44.39158 | 2025-11-18 04:18:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a4da14d7-f85d-33a7-a819-7aa3e6ad311d | -1.42175 | -48.91642 | 2025-11-18 04:18:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2075cbf5-b94f-327e-bc8b-7f9540891d82 | -2.50863 | -47.81709 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a72b32a9-c294-3911-9aa8-62c8fa53204c | -2.98593 | -51.07823 | 2025-11-18 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4abe160a-aca4-3c4b-a92d-b391f254c86e | -1.91653 | -48.80238 | 2025-11-18 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7a83077-68c3-3c3c-a7b9-bfd535d6f26d | -2.47121 | -50.24179 | 2025-11-18 04:18:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83453d48-d55b-3c9b-a566-622a27fe0b50 | -2.92653 | -45.34265 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71832f2b-47db-3946-9600-fae8ad5046a7 | -3.25328 | -43.04216 | 2025-11-18 04:18:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2e1728e-7a2a-31e7-99f2-1e20f64a59b6 | -3.02897 | -44.47512 | 2025-11-18 04:18:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05535e19-d047-3e8d-9d6d-d6fc0c102626 | -1.43244 | -48.90277 | 2025-11-18 04:18:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7769e346-6b0a-34be-8aeb-692c78d9a403 | -3.34845 | -44.39107 | 2025-11-18 04:18:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 66b38a6b-fa33-37f2-bde2-531e5eda6f74 | -1.43658 | -48.9034 | 2025-11-18 04:18:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f4885dd-6ea8-36b7-9991-aeaaa18fb4c1 | -2.99848 | -51.05998 | 2025-11-18 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 464f6963-8ee5-3182-aa23-78818e8110c5 | -2.99222 | -51.06904 | 2025-11-18 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05034739-4d55-3234-be8c-cee40f4f1733 | -3.06857 | -44.41751 | 2025-11-18 04:18:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7949fe7-f003-308c-8b72-c7890e3cec31 | -2.51699 | -47.81356 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eaad575a-60aa-3b2b-94f4-b55436fd6779 | -1.41761 | -48.91576 | 2025-11-18 04:18:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c08fa31f-859a-3337-bd9d-9e22b6ed3c12 | -4.14635 | -43.44476 | 2025-11-18 04:18:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0682b6c-33d0-38e0-b2ea-64ec822e1c3b | -2.996 | -45.43831 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README21.md)
