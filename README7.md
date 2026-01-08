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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4633a9e0-58b7-3379-ae43-a32a8d05516b | -4.2726 | -43.7832 | 2026-01-08 04:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 79a8a552-59ca-3023-927f-cc9257af7e4d | -4.2728 | -43.7601 | 2026-01-08 04:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 7c22d224-19ca-35e2-a6f8-c3d5def16829 | -4.2913 | -43.7822 | 2026-01-08 04:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 34679fe2-c999-3bc2-aec8-ee0fe65e48d3 | -4.2726 | -43.7832 | 2026-01-08 05:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| a6142b28-51ce-353d-a5db-857f586a5ba7 | -4.2728 | -43.7601 | 2026-01-08 05:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| b9d800c5-ae0c-357f-8756-72cf142a8be0 | -4.2913 | -43.7822 | 2026-01-08 05:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 1dfc0e2a-d884-3560-8f74-e6b533a62db0 | -4.2914 | -43.7591 | 2026-01-08 05:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4a09ed94-1f63-3455-b3f8-03cdc10bba1e | -4.2914 | -43.7591 | 2026-01-08 05:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 7486c3a3-a882-3b8d-9e71-c9eedaaeae25 | -4.2913 | -43.7822 | 2026-01-08 05:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| cb9a6996-2519-3724-90e7-d6d69f7f209a | -4.2726 | -43.7832 | 2026-01-08 05:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 6f658f2a-7e03-3795-b671-e30e19ecc4d4 | -4.2728 | -43.7601 | 2026-01-08 05:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 5e434904-43d5-33c8-9cb0-70345e19ea8f | -4.2914 | -43.7591 | 2026-01-08 05:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 710655a2-46bf-3cd0-a0a8-2e157170d52e | -4.2726 | -43.7832 | 2026-01-08 05:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 142.0 |
| cb037924-18e4-3b6f-af58-66f8798bc5d2 | -4.2728 | -43.7601 | 2026-01-08 05:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 96e63b1e-e68c-3f6f-abde-42cfc2d9f747 | -4.2913 | -43.7822 | 2026-01-08 05:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 1a8a1473-29d6-3320-bdc8-c10b952c0757 | -4.2726 | -43.7832 | 2026-01-08 05:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 639e9be0-9b95-32df-aa37-11a4c5d4229b | -4.2728 | -43.7601 | 2026-01-08 05:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 3d66ef2a-701d-3afc-85f4-218b1a35b40e | -4.2913 | -43.7822 | 2026-01-08 05:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| c9070e39-6e6a-3467-9d07-d8f3abd9acfb | -4.2914 | -43.7591 | 2026-01-08 05:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 715ef012-72a6-3f6e-a38d-8d8ab890f9f5 | 3.16322 | -60.95893 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0c1d8c4-3387-35c7-b476-3d5cd3855e4e | 3.94221 | -61.32446 | 2026-01-08 05:31:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab2eb912-612e-3be8-9d1e-9333da900ecf | 3.16436 | -60.46749 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d65e8037-6018-39d6-b2e6-96114e5d47a0 | 3.15603 | -60.47942 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 668a5e01-afa5-3cc1-9850-267c3f776a45 | 3.16714 | -60.46352 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76f471e9-c011-35d8-99ee-1974ef8ffb17 | 2.78403 | -60.65128 | 2026-01-08 05:31:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fee8b0d2-ab6c-3c18-9b26-7684cfd5ceac | 3.15935 | -60.4789 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad6df198-0a32-3b63-b688-6869399da441 | 3.69061 | -60.50214 | 2026-01-08 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76beab80-bd4c-35b8-9b6e-ddac554794bc | 4.06931 | -60.30769 | 2026-01-08 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bec19604-bc09-3699-af4b-c0469ebec9de | 3.16104 | -60.46801 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd3a5271-0509-3dcd-a178-ccfe589d5b86 | 3.54648 | -60.72372 | 2026-01-08 05:31:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dfb8f92-4b26-3ceb-be2c-7de541cd031d | 3.16381 | -60.46405 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7889b0d4-a783-3ade-91b0-5116ef454bd7 | 3.15826 | -60.47199 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff0fd4eb-a078-3d67-996d-c7d2f9f6b806 | 3.15712 | -60.48633 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23e64053-ce08-3e5d-aa5c-20dc19502309 | 3.15658 | -60.48288 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 37de0d0b-1de2-33d1-ae11-4bbf0596f98a | 3.15881 | -60.47544 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e83445bf-c717-3a88-8ca3-22f07e3a7ff0 | 2.96553 | -61.31078 | 2026-01-08 05:31:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 366e2d5b-67c2-3077-94f0-e9996a63b98b | 3.16491 | -60.47095 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36a7693a-b0cd-3882-8629-59350a8b709f | 4.26159 | -60.90706 | 2026-01-08 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4a98851-bdc9-3228-917c-bc6973e47727 | 3.16158 | -60.47147 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 960367e7-4a78-3f90-ad4b-b5e929f76d5f | 3.16768 | -60.46698 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da5af47f-df3d-3f73-937d-b447cc32c6aa | 3.16091 | -60.95929 | 2026-01-08 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69518b1d-752d-3f49-a716-bf3c7248617a | -2.89833 | -52.63439 | 2026-01-08 05:33:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c6363b4-7abb-3004-babe-0d7b19a86651 | -2.89879 | -52.63129 | 2026-01-08 05:33:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 482264dd-0056-3314-9879-c05f28fda874 | -16.32031 | -57.56487 | 2026-01-08 05:37:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 402957fc-3d70-3eef-abaa-a7e1172aff54 | -20.89008 | -52.35086 | 2026-01-08 05:37:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 891b4f37-6662-3386-aaed-030dd2e40bc4 | -20.88705 | -52.3414 | 2026-01-08 05:37:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d384f27a-8d86-3811-bc52-603413736edb | -20.72878 | -55.16501 | 2026-01-08 05:37:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ab37826-4246-391c-83bb-279f88d9ef78 | -20.73447 | -55.16551 | 2026-01-08 05:37:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d69fc6a-926e-32ec-afa6-1a2d799b8b84 | -20.8938 | -52.34175 | 2026-01-08 05:37:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b9b6f531-4ace-3bdf-a223-6873cbe48956 | -20.56274 | -57.95844 | 2026-01-08 05:37:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 6759b762-6e9c-395e-a208-95260ad86b4f | -20.89058 | -52.34498 | 2026-01-08 05:37:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2e3655a8-31d4-3d8a-865f-17ed3d6e0d69 | -20.89334 | -52.34763 | 2026-01-08 05:37:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f653e960-18e8-3b7f-a1cd-39b77ba4a359 | -20.72915 | -55.16111 | 2026-01-08 05:37:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34727615-e1c0-3458-a613-72daad9318b1 | -20.56746 | -57.95905 | 2026-01-08 05:37:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b18f8616-5d62-3aa1-8535-0eeb04738b59 | -20.73243 | -55.16771 | 2026-01-08 05:37:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb1d4321-44cb-35d9-91f3-b4d73944d980 | -16.32074 | -57.56179 | 2026-01-08 05:37:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5cd99d3e-d3d5-3247-ab21-eebb8d296dea | -20.73282 | -55.16386 | 2026-01-08 05:37:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1c02bb5c-c558-3864-b013-799d81d2fec5 | -16.32488 | -57.56549 | 2026-01-08 05:37:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1fff307d-d40d-3b89-bac9-70ce38c06912 | -16.32018 | -57.56641 | 2026-01-08 05:37:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 017eb505-2715-3def-a7c5-2c2fe9ffe8b3 | -16.32089 | -57.56032 | 2026-01-08 05:37:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e3320ec3-8070-301c-be88-494bc741cc26 | -20.89109 | -52.33904 | 2026-01-08 05:37:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4cd1047e-35cb-326b-8c6d-6c95f4d8a8c5 | -20.88658 | -52.34737 | 2026-01-08 05:37:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 91472cac-7eba-3f28-b9e8-5afd38e7659b | -19.17423 | -57.54049 | 2026-01-08 05:37:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f20b2070-b327-37b9-8eba-5712ab0041e9 | -4.2728 | -43.7601 | 2026-01-08 05:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| f9571fcb-9b83-3d90-8ed1-09b5ac8dcfcd | -4.2913 | -43.7822 | 2026-01-08 05:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 9dc711af-e1ab-38d6-8141-b91a71737b4f | -4.2726 | -43.7832 | 2026-01-08 05:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| e693b351-5812-3707-ab7a-7908ad4ae498 | -4.2914 | -43.7591 | 2026-01-08 05:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| f792ace4-929f-3282-9544-715b72579552 | -21.53913 | -57.54039 | 2026-01-08 05:40:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3de9c5b1-37c3-3c35-a00d-bd7363b09f8c | -21.53806 | -57.53971 | 2026-01-08 05:40:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 973f4e19-01a9-3360-a418-5494c4230251 | -21.54294 | -57.54058 | 2026-01-08 05:40:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4dce8b3e-f739-34ba-8729-ea9406eb7a7d | -21.53981 | -57.53384 | 2026-01-08 05:40:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d521056f-01e8-3d67-bbd7-9ec40af20bc7 | -4.2913 | -43.7822 | 2026-01-08 05:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 94dc6ec6-94c5-3757-92ce-441bde8fc5a9 | -4.2726 | -43.7832 | 2026-01-08 05:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 217.3 |
| fda9b861-8bdb-3a3b-8904-0f19e2b01856 | -4.2728 | -43.7601 | 2026-01-08 05:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| a5bdde5e-a474-39ab-b909-e90402119ef9 | -4.2914 | -43.7591 | 2026-01-08 05:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| e2b34bb4-3240-30fc-a747-44fb23ff6cbc | 3.54885 | -60.7275 | 2026-01-08 05:52:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58dc6b55-2e48-3deb-94dd-4f3f33d367f0 | 4.27185 | -60.66687 | 2026-01-08 05:52:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 253c8387-8113-3bee-b25a-f2fe1b446ffd | 3.97886 | -60.94246 | 2026-01-08 05:52:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66c42782-2a4d-39d4-b792-43da3c8869d2 | 3.9411 | -61.32373 | 2026-01-08 05:52:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7eb71ada-2590-300b-b38d-f7c22218726c | 3.97947 | -60.94615 | 2026-01-08 05:52:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33574c6e-1554-3fa2-9f2a-83ebee8f7cdb | 3.98297 | -60.94179 | 2026-01-08 05:52:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2d175d0-c25a-35a6-8426-8328fe870836 | 3.15487 | -60.48781 | 2026-01-08 05:54:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a36bb746-d6a9-34f6-964c-9ab21c492370 | 3.15355 | -60.4797 | 2026-01-08 05:54:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7322bfb-83bf-399c-a6f2-80308e2be453 | 3.16143 | -60.96021 | 2026-01-08 05:54:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2f58717-0504-3520-b288-0608d6ea603b | 3.15785 | -60.479 | 2026-01-08 05:54:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3398dc6d-b700-3fe0-a1dc-010585a2678f | 3.16326 | -60.96001 | 2026-01-08 05:54:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1d6d817-149b-3032-82f7-8512e0995cfd | 3.16512 | -60.46947 | 2026-01-08 05:54:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa8230d5-04ba-32ad-b403-d7f84fa3abfc | 3.16876 | -60.4647 | 2026-01-08 05:54:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34f1dfa8-014f-3b62-8a83-34016f7dcaf2 | 3.16082 | -60.47017 | 2026-01-08 05:54:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 994b4af6-52ed-3f49-a269-cb953402e299 | 3.02268 | -60.25833 | 2026-01-08 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b47a6938-48e0-3631-8521-984d0532e07e | 3.15421 | -60.48376 | 2026-01-08 05:54:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| da535856-d6b2-3166-b6cb-72db7a62fc25 | 3.1585 | -60.48305 | 2026-01-08 05:54:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c2e3b02e-c247-3772-834e-0164c5b424c4 | -16.3154 | -57.56711 | 2026-01-08 05:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ec6ba7dc-9759-38a6-8eac-1a4f04f137bf | -16.32221 | -57.56798 | 2026-01-08 05:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 19f54d99-66f4-36d4-a9e2-d6296f72afb4 | -4.2914 | -43.7591 | 2026-01-08 06:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 5941c7f9-fe4d-307a-b4a6-7e0b6c47f0a9 | -4.2726 | -43.7832 | 2026-01-08 06:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 678db5d4-190d-3e25-80f2-9ea80cd45a83 | -4.2913 | -43.7822 | 2026-01-08 06:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 02297ad8-5263-3ae5-a4d2-8b3044b0f01a | -4.2728 | -43.7601 | 2026-01-08 06:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 175.8 |
| c79bec42-fffb-357e-95f4-9e0dad8766ff | -4.2726 | -43.7832 | 2026-01-08 06:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 71b1f71d-69f5-323e-b0a8-87c8da1279a5 | -4.2728 | -43.7601 | 2026-01-08 06:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |


[Clique aqui para ver as próximas entradas](README8.md)
