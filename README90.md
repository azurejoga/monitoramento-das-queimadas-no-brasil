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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79b0cee5-aff6-3a6a-965b-07110855de5b | -12.88703 | -44.69725 | 2025-09-30 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a09bed3-2861-3c2d-89cd-06eff79aae18 | -10.95161 | -46.48238 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f447075-2db7-309a-9312-ffa0215cb71c | -8.44282 | -46.93443 | 2025-09-30 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ad6e6d03-cc20-3927-a02b-1a5ae961da57 | -6.89031 | -44.52011 | 2025-09-30 05:08:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6419dfc1-2cd1-34da-aa12-fbf36cf95084 | -9.12919 | -47.63437 | 2025-09-30 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10a4e781-3fdc-3433-8435-a8150042965e | -7.71657 | -55.46147 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f3f52ae-e934-3a52-b529-519bf877e1a8 | -11.17179 | -47.23728 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ea7b5b6-c0f3-38a5-af9c-16b7b88b7ef7 | -12.83366 | -47.00171 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28807a05-48a9-386f-b074-32db3ae74ecc | -7.91526 | -44.6316 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7aa699ce-21ee-35f4-adc4-73f3b8b3a732 | -11.15044 | -54.11976 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1a61e881-ee5f-3569-80d8-968450b10af4 | -7.79079 | -55.03088 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e1781aa-2068-3ee7-a2ac-21a41e787d21 | -12.82748 | -47.0047 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7c39a9a4-4737-36ca-aa64-c8988162abe2 | -8.86244 | -46.68824 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad3d9e3a-ff04-3821-9028-c78545623caa | -8.86434 | -46.58839 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 127f1bf1-3e41-3d30-b9cd-283b9ed199d2 | -8.50702 | -54.59787 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9929b139-c809-3798-ad7d-427c3ac23e24 | -11.75991 | -44.74317 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| abb5fde0-929d-3cd1-b7a4-c7bf32c310eb | -9.3233 | -50.63357 | 2025-09-30 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a9a90c2-13a1-3ac6-8e78-9b0f9b12c15c | -7.79822 | -48.30782 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0c9e6c7-ca51-3143-8db5-d37f7627c964 | -9.05015 | -47.63164 | 2025-09-30 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e658c817-d68b-3ff7-bc4c-a9dd32dd8cdf | -13.07108 | -47.07806 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a70816a-cc0b-3d8f-b1b0-4f8cae97cb6e | -8.44236 | -46.93777 | 2025-09-30 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9efe10a0-17a9-38fd-affa-acb90b3b0132 | -13.34377 | -47.82005 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48dfc2cf-9185-3adf-ab31-4cef7154d187 | -12.96126 | -46.40459 | 2025-09-30 05:08:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa9b498a-9723-31b3-9e9e-41cac11d3d8f | -10.38491 | -48.16259 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 141fad99-ac7b-3eaf-b50d-02c6cb391a12 | -13.34458 | -47.81321 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca2d80bd-9a46-3304-99ec-efabd631a6b4 | -11.00221 | -57.05492 | 2025-09-30 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 781800ed-ccee-3ee5-8dbc-11ba38532988 | -6.37139 | -45.61451 | 2025-09-30 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a0f9008-f5df-3dfe-bd85-4c196ea8fb93 | -9.40504 | -54.71765 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b0a84d2-c7ac-39d6-9fa9-90bc0295cb14 | -7.78282 | -54.92704 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f61a64e-f30a-307f-8ae6-5b5983132810 | -13.35274 | -47.83819 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7ee31ce-87a6-3b64-8d23-e3202e4294f0 | -10.76211 | -45.36844 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6948787b-4e9a-334d-824c-c319ab00a28b | -13.59537 | -48.04295 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf7a5529-0221-3982-8033-9d15d06a67ae | -9.40618 | -54.71022 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ede790b-9d5c-374b-9f5f-7d9cbb262cd5 | -10.19558 | -52.55442 | 2025-09-30 05:08:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15826a64-85b8-3b13-8ae6-99bba32f21a9 | -12.80052 | -46.88777 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7e61be3-8dae-3d1d-be3a-14826dc25cf6 | -13.39195 | -48.06076 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faa41626-0b40-3ac9-a90b-36b5cfa4e9eb | -11.92855 | -47.99757 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a165493a-8067-3412-adb5-115ec17f477a | -10.03672 | -50.19592 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5a6466a1-7dff-3479-b73a-a4bd47140d06 | -13.23116 | -47.31539 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aba805d4-0902-3570-93a7-d7dc9418dc9c | -11.22082 | -47.20176 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e40a0e65-c544-36c1-af40-1ef605bb1eaa | -8.88036 | -46.63896 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 125fc4bb-0f80-3a45-b4a1-49aea009526f | -9.40045 | -54.70172 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc1fb09d-8320-3367-99ce-90fb4c4cb139 | -6.49523 | -44.26868 | 2025-09-30 05:08:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7bbecbe2-6d1e-34df-9dd9-bb030b10708f | -11.74725 | -55.83764 | 2025-09-30 05:08:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f213a42-7fc3-3924-a9a7-e71e2cb20686 | -11.94053 | -43.9169 | 2025-09-30 05:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a49081c7-71a5-3831-8d41-59ef922a6a38 | -9.41017 | -54.70702 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4a2bd7a-ffca-3b42-8193-6395af215dd9 | -7.68533 | -61.05726 | 2025-09-30 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6308c1ca-4006-3dbe-8446-4a06172a5354 | -12.96482 | -48.41746 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 760f3804-e75f-3fe3-85b8-de600a0f82cf | -12.8162 | -47.00152 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 442cb3ce-ecff-382c-a30b-78ae75f5e693 | -13.21946 | -47.31721 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8ac68bb0-26c0-3fee-9e5f-329c76fee06c | -11.36209 | -49.37732 | 2025-09-30 05:08:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a09681fe-e7fe-364e-b0f6-46faf5e644dc | -11.06323 | -47.81876 | 2025-09-30 05:08:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ebe99394-0ab7-3322-844f-c4b656e2b154 | -13.23724 | -48.44495 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56be48c3-941b-39c1-8a83-8760a075e403 | -8.87888 | -46.64997 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 37d2b2ed-0dff-3485-a4a9-12d8b3c57ede | -12.94991 | -48.40875 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3669cf94-386a-37a9-a699-96378d6314ba | -11.36277 | -49.37215 | 2025-09-30 05:08:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44c3696b-2f1c-3ca0-98fd-f8ee3984e467 | -7.91002 | -44.60464 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6758d6b0-87bb-3a54-83ba-e11160c8b8d5 | -13.41063 | -48.15267 | 2025-09-30 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7c48907-18db-3c2a-8ff0-d682ec9a9f25 | -9.40844 | -54.69532 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 748ef343-51d3-32a7-8db8-6c8180ef2936 | -7.10549 | -45.54654 | 2025-09-30 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d27935a9-ccad-3347-806b-f0072cdcd4e0 | -11.72289 | -44.43742 | 2025-09-30 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0054071-5da6-3d88-8779-87920241d137 | -9.41646 | -54.71181 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ae56f48-e7ff-3e48-ac6a-5578fb1acf02 | -11.15635 | -54.12896 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bc7642d9-707c-399f-99c2-0211cb0a6685 | -7.8308 | -46.99865 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 676e96dd-94b3-3c0b-9af7-993a20492630 | -6.9376 | -45.39988 | 2025-09-30 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fa58e83-5ade-347d-a7d0-3d0618464247 | -10.40532 | -48.16652 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06b3f6e3-5d11-3a90-9a1c-cea0b405d43e | -9.51 | -47.69883 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfc25ecd-07da-3ef9-99ce-64ba7300c15d | -10.1866 | -44.89307 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ccca43d7-fee1-3a72-8911-9461f679069f | -9.30402 | -54.51067 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11edf736-c209-3104-86ec-bb985702625f | -7.866 | -47.25473 | 2025-09-30 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a3acfe8-f1d8-31b6-9f3d-ff87b18022f2 | -10.63851 | -53.68589 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6800e95a-b82b-3afb-b73f-6fc8211d4c60 | -7.23449 | -46.7663 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3893caff-3957-3865-bcd3-4eae892ab3a4 | -11.38477 | -54.35346 | 2025-09-30 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94f4d64e-91b0-3350-ad27-9c3520ee6ead | -9.37453 | -48.95493 | 2025-09-30 05:08:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4c68fbd-9fc4-3d6d-95c5-c8a1084309a0 | -10.04445 | -50.19019 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db4fa2fa-170b-3430-9da9-fdeae1becf80 | -10.76302 | -45.37173 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 305b7144-3864-3308-a4b6-898f2d4c3ce4 | -8.046 | -49.70527 | 2025-09-30 05:08:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6406ed6e-ffdf-355c-a82e-750a89ce21c8 | -9.05581 | -47.62917 | 2025-09-30 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcc31620-afdb-32c5-832a-60d24c5bcb26 | -7.78619 | -54.92757 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 212883c5-8ea6-3045-ba73-23ec3412de05 | -10.63668 | -53.69836 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 663094eb-6f06-3c46-b2d6-dce16e8e44db | -12.85232 | -46.99199 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7365c61a-bfd5-3eae-9a0f-6e08d880bcbd | -9.42845 | -54.72509 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccb3acaa-5720-34bd-8350-a9be41c8c321 | -8.23534 | -45.5037 | 2025-09-30 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c88799ea-9ad4-34cf-84ac-0d67b2c37384 | -13.23609 | -48.45466 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72407b9d-4188-31f9-b8e7-c97191b681d9 | -9.98834 | -45.40959 | 2025-09-30 05:08:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 96087ecd-a153-3ec4-91f7-4ff27781148d | -13.3653 | -47.91852 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23042695-0219-3160-a89f-609f538cddd4 | -10.06755 | -50.22038 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1c308508-a2cf-3948-b378-52c7ec56f278 | -8.87281 | -46.65298 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 77c0b42c-91c0-3583-a9ed-caeee865fe3a | -8.61426 | -54.98812 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dc97ece-4e25-31f3-ba7b-19c47be6c638 | -7.9112 | -44.61447 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c9bc941-a0ac-330d-b58e-bc25444b04ef | -9.06105 | -47.62981 | 2025-09-30 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac506f8c-6225-3ffd-8426-b90d99f8c113 | -11.17702 | -47.23707 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7339e0f-7e1a-3090-aafc-f07ca2602d91 | -10.65424 | -48.54191 | 2025-09-30 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4977af48-1b5a-3d80-9789-a03007287dd2 | -13.40933 | -47.55103 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c1c30d29-7f8f-33a2-996e-1d23ad9339db | -13.24299 | -48.44139 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9e9d6bc-5208-3f67-ad83-f7cdd7c47d55 | -10.11525 | -47.79029 | 2025-09-30 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc9f6e2a-a93d-3989-b590-0f5f416d9e30 | -9.989 | -45.40437 | 2025-09-30 05:08:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b8844b6b-f0d6-383c-a956-6ef6e4bdfa60 | -11.24513 | -47.23241 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 459e3121-038d-3eec-9b7c-cc99c4822f23 | -10.75553 | -45.38124 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0e3758e-c84a-394d-9986-27a01da4a385 | -11.2914 | -47.82391 | 2025-09-30 05:08:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README91.md)
