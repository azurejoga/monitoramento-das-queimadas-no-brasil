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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5694353-b666-3790-bf67-b9c99026820a | -4.28813 | -44.19418 | 2024-11-13 04:57:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3f056df9-bdd2-33e5-a853-623d2d1faaed | -3.00162 | -51.45605 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e40dd2dd-ebeb-3353-8890-adef23ad4b82 | -1.22064 | -51.74793 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37210f88-0a18-32ea-98f5-d72a02739c19 | -3.06536 | -50.3356 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8ab1c01d-31a3-3386-847c-2381365725dd | -0.99023 | -52.31557 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dfad2fd-93d1-393b-bd02-65756a4302cf | -2.93488 | -48.32322 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aea7ed8a-a42f-304c-8d5a-5c1cf51ea9d9 | -2.90489 | -48.2998 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78b9db97-b1e0-3d5b-aa40-646cfb72c526 | -2.93434 | -49.42454 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61dcec3c-ee58-3c0c-ba02-8b3b4bc73931 | -2.72819 | -45.28939 | 2024-11-13 04:57:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cb8cadac-2654-3177-9ced-7bb7036af98f | -2.81784 | -54.01077 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a8f5f89-6f00-37fd-b2e8-1dfde266754a | -3.14912 | -53.2396 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 74978e7a-dbea-31fb-9aec-acdd3c0767da | -3.24141 | -50.30859 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bb4b7b0-51b1-3e57-970f-4abfc2daa215 | -4.20105 | -42.3298 | 2024-11-13 04:57:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f6fd6900-3318-3854-bb5d-84055c47f612 | -3.31381 | -51.75492 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7beeab03-7aa6-3f6f-9343-172fefad0b0c | -2.24392 | -53.74528 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 29edc7a7-4e32-34f0-bc13-af9c9794fcf8 | -2.7887 | -52.86867 | 2024-11-13 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4cbbff3-c5e3-3240-bb8e-35325faaa325 | -2.99157 | -51.34284 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b284e7ab-d632-3449-8529-9737fadcd07b | -4.02968 | -55.87395 | 2024-11-13 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d3e0653-8a21-3882-bc07-36a3e19993dd | -2.57136 | -54.04312 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a133c5c-440f-3614-a71f-5c6712e92f1d | -2.87576 | -54.20753 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68d77ec7-0274-3053-a44f-f24a4d006c63 | -3.10631 | -54.30067 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07e62e02-099f-3d3c-b469-0c1f74d143d1 | -2.66299 | -57.38239 | 2024-11-13 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 377a6839-37eb-39f8-957f-02821b742602 | -3.62476 | -51.49068 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8351134e-d8f8-3e78-b334-ce08fb565b85 | -4.65632 | -45.12528 | 2024-11-13 04:57:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5392fb2a-ed42-3d5b-869b-0604fd555c54 | -3.53321 | -54.48473 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b23758a7-2957-3ece-8c23-92b6d1dfba2f | -3.92959 | -47.05776 | 2024-11-13 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5dd5a30-f788-30d2-ac85-74cb132e0f63 | -3.57336 | -54.61916 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92403fcd-0bcf-37fb-9e9a-b34f8b8b0c38 | -3.86188 | -51.90911 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe7c276d-529e-34f0-8b4f-237013af83d6 | -2.78309 | -49.22643 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d2b2b1f-80ef-3806-8c66-9e8d03633354 | -3.05429 | -50.3306 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0fd9305b-c30a-3c6d-be3a-2ed8c182cbb8 | -2.96794 | -51.03121 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c353e939-095d-358d-ae98-a8b7d1e58dca | -0.19572 | -51.49599 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 799d5959-9060-3f13-9b89-6582893da8d3 | -2.97793 | -45.16553 | 2024-11-13 04:57:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 10cdcf1e-87dd-3767-beaf-51bc4e9a4bef | -2.73802 | -49.18494 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 55367644-24f6-3054-bae8-ff7fabc962d4 | -4.32808 | -48.60973 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 52e7a53d-c7af-3e91-83d5-b0e53d4176c0 | -2.31821 | -50.58863 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3b4e58c-8209-3e64-b53b-73c33e623f33 | -1.64659 | -52.53475 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52f9c388-0195-3703-91f8-73107d72ddd3 | -4.65759 | -47.43242 | 2024-11-13 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b63f8037-f5bf-30cd-b329-00712c442791 | -0.94625 | -52.40137 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0d949a6-ed8a-3e7d-b1c7-177919989131 | -2.80728 | -54.18998 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd12e4d6-b202-3a6d-8ce9-e2d7f7abadf5 | -3.06387 | -50.34077 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b37d19d9-baf6-33bb-aa8d-405f1e4108b2 | -3.8579 | -51.91227 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7f1c5da-0a23-3a1e-a71d-16a8e2b56d1b | -3.5238 | -54.47974 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2855a5e-5cbf-3c03-bde4-5fb13f96952f | -2.13564 | -50.64522 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcc60fe2-6992-37f8-9122-048e8bd5530f | -2.87245 | -54.20702 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95510670-93d6-3680-8494-49acd3da3170 | -3.02392 | -47.97393 | 2024-11-13 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d02c8f61-fcfc-35e6-bb84-2c99bb5e6547 | -2.18454 | -53.25433 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76de294f-4aa0-36cb-aabb-6ec5e23bb341 | -4.42879 | -45.95417 | 2024-11-13 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ae19511-94a0-3363-a414-e4965603bdd1 | -3.65871 | -54.6609 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33f0a889-0f08-3cc6-ba17-6093275c0007 | -2.45552 | -53.93639 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7eb9c22c-9997-35b5-98ba-caa7d7e4de88 | -1.62168 | -52.52023 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ff0ab34-f7c1-3355-bc7b-f80325c774a8 | -3.06663 | -50.32712 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d067f32-ac80-3286-8804-d1b67318f342 | -1.64347 | -50.4997 | 2024-11-13 04:57:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa066de3-fa00-3a90-8442-7cc79d9ef441 | -3.91127 | -52.24928 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05430e4e-9591-3f01-b786-f104f72f97f5 | -0.14108 | -51.45805 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 966ed40e-4012-3d57-975d-9fa4e6e49754 | -1.01063 | -47.17734 | 2024-11-13 04:57:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e6fa306-6800-371b-a64a-b33ce7b67958 | -4.07318 | -46.44826 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04284f13-b900-376b-9bf1-f6a44892555e | -2.60957 | -46.17257 | 2024-11-13 04:57:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6aaf2327-8d87-3aa9-bfd2-c95225cf733b | -2.28025 | -48.81282 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6f1d0ea-f5ff-332e-916b-9b0cdec7c079 | -3.25424 | -43.26115 | 2024-11-13 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 15571b90-8eb5-35d4-8015-cadf7a5013d5 | -2.45445 | -53.94329 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1872f14c-4cfa-3e8b-be4e-466ffda51dd7 | -1.37388 | -52.86769 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd519db7-6368-3e66-9f49-aa82d720b05c | -0.87336 | -51.9496 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a483245-26fc-3fab-b965-84cd7d16ffe6 | -2.12819 | -50.69292 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e7023ef-517b-3f91-b64b-8c7eb65f6496 | -2.87803 | -49.43512 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d5e8ab8-8b77-3abd-80a3-55d48e0e50d7 | -2.17285 | -50.51809 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 462f6f27-a54c-322b-8459-ba3cd9e614db | -3.8846 | -52.39998 | 2024-11-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2269118a-96a0-3493-98c3-1d3687472be8 | -3.16239 | -51.13472 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e9bb826-b712-3a31-a729-0f93bedac544 | -2.14545 | -53.37103 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28690600-1d05-3580-9e87-62507994f4f3 | -3.10245 | -54.30362 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dbf04bf4-db5b-3483-a8ef-53c6151e4d7a | -2.95109 | -51.97024 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e3a930d-2589-3c80-8b8b-ffd5c124904b | -2.60035 | -51.71621 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0eb623ee-0234-3edb-a25b-7d3dc1351a6e | -2.66786 | -54.07932 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 779a5eef-80c5-3d7e-a2b8-ddd2c47f162a | -2.78538 | -52.86816 | 2024-11-13 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e176f33-a36c-34de-a716-669d6f329669 | -2.80287 | -51.49559 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb1c9195-5850-3d07-bd9a-32fc84ef1525 | -1.35307 | -51.43061 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f23a1c73-e66f-388f-b83f-4f56762122bf | -1.3906 | -52.07943 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84b431ef-5b37-3469-9a50-18ab1e1bd728 | -4.41777 | -48.84818 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e1791035-ce8a-3731-a081-d086c01ad370 | -1.6981 | -52.70584 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 443a7582-9883-3a60-8117-30eaa6147191 | -1.72146 | -52.68867 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38021b7b-41e2-368c-8078-ff149fadf152 | -3.43246 | -50.3086 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab7c3ed8-3475-3d79-937e-43c375c63895 | -2.73738 | -45.29676 | 2024-11-13 04:57:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5519c7c1-ccee-3b91-93c1-57140d1a7a30 | -2.1432 | -53.23373 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 098b4d0b-c35a-3226-9777-8da78e47c556 | -1.62832 | -52.52125 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3df217d9-ab31-31a4-8b06-b7257993ca14 | -3.05595 | -50.34386 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95fca732-23f4-3f3c-b714-8e260f592ed4 | -0.95543 | -52.34234 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4683aa87-3f3b-39b3-b3d4-9c17fc8ba1f4 | -3.96252 | -52.23128 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 239adb34-75e6-3359-bd55-88fee6775b77 | -3.25323 | -43.26677 | 2024-11-13 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| abe93157-914f-3763-92f6-c909fd481c82 | -1.61782 | -52.52319 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16618d39-5253-31a2-aae4-0b46e615e664 | -3.8605 | -49.11724 | 2024-11-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 31b3a114-7609-3b7a-9e02-5bbd751d592f | -3.85392 | -51.91545 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc3ae65d-5062-34eb-abfb-d74d978d4286 | 1.59864 | -55.77602 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e925b8e-b870-3060-afaa-cdd2bb22454b | -4.52344 | -47.89013 | 2024-11-13 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b32719f6-b066-38f4-9a74-139737266b11 | -4.33614 | -50.42308 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1e89b63d-9e53-3213-96a4-c7fa2f07c987 | -1.53058 | -54.52273 | 2024-11-13 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef9c356f-1221-3dc8-8d98-cb6b33f51b04 | -3.48696 | -54.02126 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aed3e484-6c9f-3693-ab8f-6c6b57cc523a | -3.66924 | -54.65896 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 698e5480-4328-311d-8824-ef800f64b386 | -3.27407 | -48.7492 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1dc8073-5530-339e-bcc8-9f8a42a226ff | -3.09854 | -54.30573 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c7941f21-76fd-35fc-8792-9934144f2afb | -2.06933 | -48.23124 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README37.md)
