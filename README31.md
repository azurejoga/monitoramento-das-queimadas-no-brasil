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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdfa08f3-b4ce-3621-959e-5d8b238030b6 | -7.89995 | -63.531 | 2025-07-26 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a243914-cfa3-3990-aef7-88b3f747b616 | -7.56133 | -61.40794 | 2025-07-26 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 756ba6f2-6351-3f0f-bc46-13db3541dcaa | -8.06971 | -63.85892 | 2025-07-26 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8957323-f88a-3881-bc17-c5d4b7e0b85c | -10.22444 | -59.4127 | 2025-07-26 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4a292f4-74fc-3042-996b-dce1257b3120 | -8.21087 | -70.50007 | 2025-07-26 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 062dcc3a-c249-3ae8-bff2-b55a2432506d | -8.49922 | -64.04084 | 2025-07-26 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5ae0456-d03a-3070-89fe-b3d72081f25d | -10.22517 | -59.4067 | 2025-07-26 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f6fe2a9-c00e-3a2f-81fd-d28a345f6743 | -7.89954 | -63.53405 | 2025-07-26 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9089284b-59af-37e7-a7ed-c23bf54cb846 | -7.6648 | -69.92734 | 2025-07-26 06:08:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0110bfa7-eb56-3c04-8375-0ad0cb791cd3 | -7.49789 | -63.82248 | 2025-07-26 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68d2b223-1e88-3949-af93-acd8756562d2 | -7.65733 | -69.93007 | 2025-07-26 06:08:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35873afa-b746-302b-aee8-453c8a36c36c | -10.64552 | -68.73712 | 2025-07-26 06:08:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ada2686-d37b-3def-b562-faab185c4551 | -8.93345 | -71.24933 | 2025-07-26 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e568709a-ded2-354c-9816-0d5cd6f1d8ef | -9.52436 | -68.29244 | 2025-07-26 06:08:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a84b0a4-d891-3b2a-95ed-3a23c4c8ce45 | -7.49329 | -63.81889 | 2025-07-26 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b359dd9-5c24-3e4f-ab31-7845717c019d | -8.9329 | -71.25288 | 2025-07-26 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb1c6156-ee08-3a85-9bf3-91911b489d30 | -7.50052 | -63.50974 | 2025-07-26 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12665b08-6bfc-38f0-b0d1-c9e1457a27ad | -8.45243 | -70.08553 | 2025-07-26 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2adcb235-b183-3b88-ac1e-52a0398543c8 | -9.96924 | -64.95633 | 2025-07-26 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 21029a89-2340-3794-9d2f-48bd963ea764 | -7.72996 | -72.30061 | 2025-07-26 06:08:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68619fe9-b5fd-3032-936a-e71d1c251b37 | -7.66423 | -69.93111 | 2025-07-26 06:08:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2329a9b4-a47e-33b7-beaf-304811233f92 | -8.10013 | -61.40265 | 2025-07-26 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16a9155f-1b55-308d-948b-85f5695f14fa | -11.00842 | -68.49772 | 2025-07-26 06:08:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8e99075-e7f0-3313-a483-ccd2dacbec81 | -8.50383 | -64.0444 | 2025-07-26 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55dc8142-e027-3859-a4cc-625575c55bb9 | -7.56779 | -61.40449 | 2025-07-26 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78796c73-5738-3fec-8c48-f07c8407196b | -8.06931 | -63.86185 | 2025-07-26 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7bcbf370-7ad5-3033-a64a-dae653ed0cb7 | -8.03317 | -72.29639 | 2025-07-26 06:08:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42405c63-eafb-30c7-b78c-d7061e295bb5 | -7.56722 | -61.40872 | 2025-07-26 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eec0e69f-9a6a-3915-80e8-18311d54324b | -18.2442 | -44.7767 | 2025-07-26 06:10:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| dc2f947a-e573-3a00-b797-88c44357193c | -3.75152 | -49.04531 | 2025-07-26 06:12:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b871c961-98b8-3d0d-9a22-20a31f1a83e6 | -4.29934 | -48.1083 | 2025-07-26 06:12:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8b4abb90-6524-31bf-ba88-126bc8e71fcf | -3.38514 | -47.49712 | 2025-07-26 06:12:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 19f369cc-b1b3-3d43-9ffe-b7f7e1a15a98 | -4.03659 | -42.51129 | 2025-07-26 06:12:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 36.6 |
| 21c00dca-9ef3-3724-93c7-1d50790e6b2d | -3.38709 | -47.48368 | 2025-07-26 06:12:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| bb5a4040-a0c8-3dc7-883b-2ec85096b119 | -2.90592 | -48.25321 | 2025-07-26 06:12:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8f7de778-b340-3b96-82cc-8a0194fc677e | -3.39592 | -47.4987 | 2025-07-26 06:12:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3eda8621-4f00-3b78-ae3a-39cd0491fbad | -2.90765 | -48.24144 | 2025-07-26 06:12:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 30580b91-780a-37e3-a1c1-5a21318c366f | -4.30116 | -48.09565 | 2025-07-26 06:12:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 98fef40c-59c0-3924-8b3c-93bff6f62d73 | -3.3979 | -47.48513 | 2025-07-26 06:12:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 86ba4da0-a7fe-3028-82c9-75799a101a6a | -6.63828 | -58.85189 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 227.1 |
| 2655ae1d-88d8-35c7-95fd-51097f6cfedb | -6.62881 | -58.83032 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 695.1 |
| 97fb953b-9d34-345e-8bc0-55709672f772 | -6.68078 | -58.84412 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 106.9 |
| fa4aca95-5623-3a63-b6bd-4010760ea244 | -13.24274 | -51.15081 | 2025-07-26 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7372acf1-729e-30c5-8cdb-51c4c1568e3b | -6.67137 | -58.82278 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 70069558-a72b-3c9c-ae3c-2db653b3150e | -6.64457 | -58.81327 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 1d1651ca-7790-3712-a03e-619f61534c2f | -6.66362 | -58.85604 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 541.1 |
| 7858dd0a-84c8-356e-a067-c4c1388c8096 | -6.64144 | -58.8325 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 377.6 |
| 0bc8f851-2a5c-3416-ad3a-446dd711788a | -7.24406 | -43.0526 | 2025-07-26 06:14:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 46.8 |
| 992022df-9bbc-376e-84e2-68d639709d70 | -6.66675 | -58.83655 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 667.0 |
| 85b55d44-010a-3664-a94a-28c602faf951 | -6.67628 | -58.85818 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 5ac39826-1c58-32da-82b0-b131c12573a2 | -6.62563 | -58.84975 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 320.3 |
| f4e31d40-ad5f-3450-93f9-e7deaef79b00 | -6.68246 | -58.8194 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| c4553a7e-e6b3-33ec-bf76-0d9d053b05a8 | -6.61616 | -58.82826 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 229.8 |
| af278c1e-7957-393e-930d-84d119653b98 | -6.66813 | -58.84206 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 586.5 |
| ec40115e-5fb2-3803-9da0-16b3ac9a8013 | -6.684 | -58.82481 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| e1f8bc69-e388-39fb-b5e7-cc5fe8def880 | -6.66984 | -58.81728 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 461eabf8-968d-31e1-8850-eacac8915b58 | -6.63197 | -58.81106 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| d994104b-9ba6-3831-a58c-92a6a2d56425 | -6.66485 | -58.86154 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 174.5 |
| 118a1401-4256-3f67-af7d-dc3ad1115160 | -6.61294 | -58.84777 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| de21b6ee-14ec-3a70-b9a8-61e9b464b446 | -6.65095 | -58.854 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 266.1 |
| ad637e39-4e3a-33ed-9f26-f81bc977e008 | -14.93847 | -46.95777 | 2025-07-26 06:14:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 8b917a69-6dd0-3043-b209-82d69234b287 | -6.65721 | -58.81523 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 164.2 |
| f936ba4e-24e2-3fb5-9f81-852554883e29 | -6.65409 | -58.83455 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 414.9 |
| 418f2970-7c39-3b7d-9c89-95cb81a52921 | -6.6794 | -58.83857 | 2025-07-26 06:14:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 138.7 |
| f726143f-10cb-3c79-8c3a-75a946933f5e | -21.99821 | -57.60476 | 2025-07-26 06:16:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2fce9d18-a101-3e15-8395-d19d2e132a3d | -18.24483 | -44.79788 | 2025-07-26 06:16:00 | AQUA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 5d49c25e-2213-33b9-a7f9-dad2e107c70c | -18.24129 | -44.78988 | 2025-07-26 06:16:00 | AQUA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ec842936-e9b8-354e-81b6-a648147744da | -21.99663 | -57.61463 | 2025-07-26 06:16:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| aed538b9-2045-36a9-bb52-a462e17ef6a3 | -20.61909 | -54.83382 | 2025-07-26 06:16:00 | AQUA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e5fd785b-2635-319c-846c-02ed8847c471 | -18.2442 | -44.7767 | 2025-07-26 07:00:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 46.5 |
| bc00b71c-e190-3e77-b0e1-1a1d83044d2a | -18.2435 | -44.8008 | 2025-07-26 07:00:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 47.5 |
| b024b285-cae5-386f-a312-3016f3ac9da9 | -18.2435 | -44.8008 | 2025-07-26 07:10:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 4f4d4fd7-4022-32a6-aae0-4832a8644221 | -18.2442 | -44.7767 | 2025-07-26 07:10:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 47238dbf-d284-3152-80c0-2ce10e736775 | -18.2442 | -44.7767 | 2025-07-26 07:20:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 083bb555-21b9-3aa7-a0a6-e5d73fab16df | -18.2435 | -44.8008 | 2025-07-26 07:20:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| bb0e41a3-7c4e-3216-a166-f7ae5ce32148 | -6.639 | -58.8475 | 2025-07-26 10:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| ff4ee5f4-d7df-3f3f-9cda-e26d08640ff8 | -6.6575 | -58.8468 | 2025-07-26 10:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 124.5 |
| ac82ea77-01a7-3134-b7d5-c54cb22f03b0 | -6.6759 | -58.846 | 2025-07-26 10:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 104.0 |
| d14507a4-ac52-326f-a527-7bfbb6732e08 | -6.6206 | -58.8483 | 2025-07-26 11:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 5996d6bc-3b2d-341a-9909-3b7db959568f | -6.639 | -58.8475 | 2025-07-26 11:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| e167b0ba-7018-326b-a1ea-3183cc2e77a4 | -6.5377 | -45.6126 | 2025-07-26 11:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 47e12278-cedc-3328-bf30-00305470db39 | -13.5081 | -45.4873 | 2025-07-26 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 7ccc435b-46d9-36c7-9ab7-c8ab2b02b677 | -6.5377 | -45.6126 | 2025-07-26 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 8fbe45ac-25ac-3842-8406-4f497c3d20af | -13.5081 | -45.4873 | 2025-07-26 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 71c45419-eade-3a7b-9e09-59f9ec75de37 | -4.37274 | -38.71903 | 2025-07-26 12:10:00 | TERRA_M-T | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 9f6f3c83-9a51-32c1-9824-5db6af78b5c9 | -4.71256 | -43.49547 | 2025-07-26 12:10:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4269bcb5-c0f4-3c1d-93eb-fb892f9aac5a | -4.04086 | -42.51448 | 2025-07-26 12:10:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 07285f44-6b07-3eea-acb6-536b31409276 | -5.48658 | -42.1475 | 2025-07-26 12:10:00 | TERRA_M-T | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 452fffde-2943-375c-9902-bff1176471fe | -4.08891 | -44.49268 | 2025-07-26 12:10:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6f41b68b-d375-309a-bf89-902f0b6d189b | -4.06797 | -42.52459 | 2025-07-26 12:10:00 | TERRA_M-T | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 4d09c850-4b54-37c8-8e15-8e314ecd926e | -4.06669 | -42.53362 | 2025-07-26 12:10:00 | TERRA_M-T | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 9a9501fa-b312-320c-abc7-adeafbfcb04b | -3.65988 | -43.05046 | 2025-07-26 12:10:00 | TERRA_M-T | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3a35fe1b-ab3c-3108-96bb-8fae11fef79f | -4.36141 | -38.71758 | 2025-07-26 12:10:00 | TERRA_M-T | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| bc344be9-b1e7-3c32-a206-bcdadf35edde | -5.42214 | -40.73757 | 2025-07-26 12:10:00 | TERRA_M-T | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 30ebeaf0-079d-3b2a-b3ab-629876eae77a | -5.48375 | -43.32963 | 2025-07-26 12:10:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 34050ab9-48a9-3030-847a-4f805d8cfffa | -3.99443 | -43.22929 | 2025-07-26 12:10:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 650bf3bb-ebc3-3af1-8fb7-f1d617f1e1f4 | -3.94682 | -41.48672 | 2025-07-26 12:10:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 427fad47-f381-3b2c-bed8-698e0d064d8e | -5.48248 | -43.33847 | 2025-07-26 12:10:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a8fbdc4a-f037-3fec-b112-610b796fe9f1 | -4.96373 | -43.21995 | 2025-07-26 12:10:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 37fa2575-41e0-344f-8e31-027253ca448d | -8.00566 | -45.043 | 2025-07-26 12:12:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README32.md)
