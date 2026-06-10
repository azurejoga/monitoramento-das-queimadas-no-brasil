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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27605d8f-b029-3de5-a90f-1eae7b25ea49 | -14.69672 | -48.3122 | 2026-06-10 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9b40709-1ae9-3f98-b5ac-cd84468d54d5 | -9.32302 | -45.49032 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 14a69868-1744-3cd6-a678-629d836216b6 | -14.69598 | -48.31745 | 2026-06-10 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b749bf45-9d8c-39c8-9a7a-fe5231a7c379 | -11.80043 | -58.17125 | 2026-06-10 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 700f03c7-378e-3136-8176-535a2ed61c61 | -11.55382 | -52.80354 | 2026-06-10 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b20ce39-4f11-30b1-a4e3-d4462a917abd | -8.97884 | -47.98275 | 2026-06-10 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| faece1e9-436a-31f1-b16f-4841d59f99dd | -9.31111 | -45.48004 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| af0fe2c2-bfb9-3f86-b012-10d955485199 | -9.31096 | -48.9718 | 2026-06-10 04:51:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ecbfed88-dd8f-33d6-a3d1-ae1888b1f8b9 | -9.31548 | -45.48063 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| d9bed5b1-f1aa-36f0-bb00-0609e29ac8e0 | -14.37325 | -45.55764 | 2026-06-10 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bd29e78-a0cd-3c72-bc72-7a4aa31a3baf | -14.69654 | -48.31401 | 2026-06-10 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8de90d65-6a78-3d0a-8189-3d7c8b94b2b3 | -12.85663 | -44.36919 | 2026-06-10 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f0f722c3-4365-3566-888f-90fee419f89f | -12.40841 | -47.49984 | 2026-06-10 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb2676b4-d809-38eb-9c1f-fdffbf8bf707 | -7.67145 | -55.00607 | 2026-06-10 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb7d8c27-6abf-3331-a0fb-b27a1817b520 | -10.67521 | -51.74728 | 2026-06-10 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b674e41-a8bd-3e40-817c-5900f8777c39 | -11.55714 | -52.80408 | 2026-06-10 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42e4bf69-b52e-3a6f-b4f6-90b38130e3f2 | -14.69989 | -48.31803 | 2026-06-10 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2aa40ec-55ba-3ffb-a79f-e0a46cae5245 | -9.21051 | -48.58305 | 2026-06-10 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf6458ce-870e-3aa8-bf42-fa27ebcd96a3 | -10.83832 | -53.74598 | 2026-06-10 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2d713f7-1394-3ab5-859c-8382ce464f12 | -11.33738 | -51.39837 | 2026-06-10 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ca17d13-577c-3277-b48d-ed56c228887b | -9.14199 | -47.98462 | 2026-06-10 04:51:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cec149a0-faef-3265-a7bf-eeddea5fb9e4 | -14.4133 | -45.57837 | 2026-06-10 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6258b8b-77da-3624-b964-fb50af6d1ee9 | -12.85184 | -44.37542 | 2026-06-10 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| aa540bb1-dc70-346d-8fe1-b170327d426f | -8.32156 | -45.39038 | 2026-06-10 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0cae353-e4e4-3b67-810f-da12a67f87dc | -14.62042 | -47.99933 | 2026-06-10 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69ab19d1-7c46-3ae4-b052-6a3c9ab3d6d5 | -10.5818 | -49.65076 | 2026-06-10 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92181171-0cea-30fe-a83d-fdfe77483d04 | -9.32362 | -45.48608 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| d62bc3d1-d89a-37e0-a6fa-62377f5df9b4 | -9.29919 | -45.46979 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e2984e5a-b63a-3792-bef5-42f63ce25185 | -9.2986 | -45.47405 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3eaee0e0-0723-334c-a9af-e596b90e7759 | -9.31171 | -45.47579 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 5659c6f5-861b-39b6-a908-89f147925532 | -14.36646 | -45.53632 | 2026-06-10 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4771cce-4618-3dba-b001-9157183f19d2 | -9.30238 | -45.47888 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 37157df1-4134-31db-8643-5a4b01d976e5 | -9.11349 | -47.95937 | 2026-06-10 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5955b56-17be-35a2-b5f4-c510fd38879f | -14.40126 | -45.56144 | 2026-06-10 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a9d2433-ee87-3881-aa2d-14f96aa4c02f | -15.18023 | -43.85351 | 2026-06-10 04:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b58b01be-7a84-3583-82b2-5b0a32af5332 | -8.97144 | -47.98159 | 2026-06-10 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c0f8cf7-8a05-3daa-af8f-4fce615bc243 | -10.85732 | -53.74052 | 2026-06-10 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 814f3986-94a5-3313-bae5-a98fa834770e | -14.61722 | -47.99318 | 2026-06-10 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5815a77b-d10c-3630-9302-f4aaf5b64438 | -7.67515 | -55.0067 | 2026-06-10 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10da31fc-254a-347f-965c-b69fec796456 | -9.70053 | -48.60677 | 2026-06-10 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ab06488-10c4-3491-b44c-d1dc2c302e15 | -9.31866 | -45.48972 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8ed55b5d-7804-37f0-aca2-cae457c25939 | -8.44137 | -49.7083 | 2026-06-10 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45ed38ad-7975-3705-935a-834f88849cc1 | -11.54994 | -52.80653 | 2026-06-10 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4aad2f4-ce50-3efd-a199-001e58987f01 | -12.40903 | -47.49549 | 2026-06-10 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f2c75c9-c57b-3325-8253-5cb64cbca0cc | -12.05406 | -49.76349 | 2026-06-10 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13c12c1f-fdbe-3319-ad7b-dec18e822037 | -9.00343 | -47.99553 | 2026-06-10 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 932a4bee-c6bf-3cb3-ab1c-2402cc01967d | -8.97514 | -47.98217 | 2026-06-10 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3ad819f-2b47-333d-8ff2-967394c4a3d1 | -9.7518 | -47.88038 | 2026-06-10 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a149b25e-0fed-30da-978b-6692734145e3 | -9.29482 | -45.4692 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0e3aaac9-5be5-3203-8c2e-efea686ffb0d | -9.69992 | -48.61094 | 2026-06-10 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6e3bb75-46d7-3f0a-8162-144f046bfd0d | -14.64772 | -47.99478 | 2026-06-10 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba85d971-e40a-37df-b2fe-1fc4cc1861a6 | -9.41558 | -50.68132 | 2026-06-10 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09fbac9b-4440-359e-82c1-5a02b36a7c73 | -10.1904 | -49.59314 | 2026-06-10 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ed96bf1-abdd-3855-97e6-62e652f440ee | -14.36795 | -45.56199 | 2026-06-10 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c13543d3-f6bf-36e7-a311-4a91171774bd | -10.61761 | -52.28297 | 2026-06-10 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52801721-84db-3d94-b691-5a83c50d2d9b | -11.38288 | -47.81818 | 2026-06-10 04:51:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 022dca90-6b1c-3ff5-a238-b11e0ddbdb44 | -11.6022 | -55.33797 | 2026-06-10 04:51:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f391a5e1-783d-39d2-bb72-072e6c3d000c | -9.2638 | -50.12253 | 2026-06-10 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc9bdd63-de93-3bb1-9f1f-4f912ae7e976 | -11.59861 | -55.33734 | 2026-06-10 04:51:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be4d716a-5de8-30a9-b1ed-b854b2a7a7a0 | -12.85168 | -44.36855 | 2026-06-10 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 43a132fe-a534-34a4-9f7e-426a1841d8f6 | -9.08181 | -50.60058 | 2026-06-10 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96a360f2-b851-3d85-a36e-ebde1c4bda9a | -9.14269 | -49.837 | 2026-06-10 04:51:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cb7147a-9546-3196-970e-8d1ce388a1ef | -9.30297 | -45.47463 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 823141cc-2900-356f-bbb5-d3fb1b8d33dc | -14.64576 | -47.99249 | 2026-06-10 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 580bd25b-c6c1-329e-b835-912b0618de0c | -14.13176 | -49.85079 | 2026-06-10 04:51:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75288177-6fea-3518-8f4c-fc9b2089230d | -9.31489 | -45.48488 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 17dc2a37-c150-3c6d-adaf-14ef43dad976 | -10.01194 | -48.21478 | 2026-06-10 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24f6f406-0a45-39b7-8689-39042132b136 | -13.96038 | -46.19036 | 2026-06-10 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 15508f64-9a39-3b67-9af0-84e3f7e0c4e5 | -11.33793 | -51.39482 | 2026-06-10 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d165db2e-ca6b-3ee9-87dc-67c7746a07a1 | -9.31985 | -45.48122 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2d3e2e66-7866-3bf7-9b84-c445be112032 | -9.29541 | -45.46492 | 2026-06-10 04:51:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ac063c72-55f2-378d-9bdc-9525d8f02aa2 | -14.39658 | -45.56085 | 2026-06-10 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ca6b89d-a98b-343d-ae86-a75d9822889a | -9.30356 | -45.47037 | 2026-06-10 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 95a38b56-fd95-3b6b-a013-b4e29897e37b | -11.95933 | -53.49605 | 2026-06-10 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da5d27ea-e474-398e-acf9-76f7ae9773b3 | -9.2202 | -48.56751 | 2026-06-10 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d74ced3-4750-358e-8fbb-97b0dddd5ca1 | -9.21957 | -48.57172 | 2026-06-10 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36017143-c3fd-3359-b36d-7eeb7eb6402f | -8.38423 | -49.624 | 2026-06-10 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ec36bfe4-9286-3918-b590-b36e0cf57038 | -9.14263 | -47.98019 | 2026-06-10 04:51:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c5078f4-b621-38ca-8e35-dcf48500f4cd | -9.20989 | -48.58718 | 2026-06-10 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6487f9c-8974-3cd8-8b82-b3add1ca564b | -14.36329 | -45.56135 | 2026-06-10 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5254d420-d7fa-3cd5-a2eb-8441d5f0a2a4 | -9.29978 | -45.46553 | 2026-06-10 04:51:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4ae5167a-cd2a-3dd5-869c-98bbb18771ef | -10.84715 | -53.73882 | 2026-06-10 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a682205-8e8b-3466-89ea-7c54ebc4906e | -9.07513 | -50.59953 | 2026-06-10 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92a296a8-8082-3127-b599-9dc48384d663 | -10.84994 | -53.74306 | 2026-06-10 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea9ee2ed-4d70-30eb-857f-01d25982c0a0 | -10.83493 | -53.7454 | 2026-06-10 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 160cff5d-7e95-3a7b-9826-4f75cbc53cdf | -9.22381 | -48.56802 | 2026-06-10 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c53008c-172f-30ed-824c-b7ac27eaf2ae | -9.31449 | -48.97234 | 2026-06-10 04:51:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b47d108-78f2-3638-8ed7-7844f912e0c9 | -12.85749 | -44.37041 | 2026-06-10 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 976c1402-8353-33a4-bd62-1e7b36540fd6 | -13.96097 | -46.18586 | 2026-06-10 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14caa0f1-565c-35ab-9aa2-c38ec36c5748 | -9.21113 | -48.57892 | 2026-06-10 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76bc94c8-eba5-3eec-b270-16b7124c6a7f | -12.85254 | -44.36975 | 2026-06-10 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| f9edac64-b799-3efe-b473-6ed0434738f8 | -9.26324 | -50.12619 | 2026-06-10 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3c18f17-1e95-3d5c-8c9f-55f2cb378240 | -13.95592 | -46.18985 | 2026-06-10 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a25a9b3d-2b96-3e64-b164-f38c020ab501 | -12.85589 | -44.37486 | 2026-06-10 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| eafd925b-95a8-3f81-b875-c90206fb9bae | -17.43283 | -43.82043 | 2026-06-10 04:53:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd7db115-8215-3834-98cd-f87b73e1f9fb | -20.23143 | -41.89655 | 2026-06-10 04:53:00 | NOAA-20 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 217e17d7-0a94-3824-bd94-48f88554440b | -22.74598 | -45.63361 | 2026-06-10 04:53:00 | NOAA-20 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9cb499b4-5775-3645-934a-e78f6115fe2f | -18.95941 | -52.46459 | 2026-06-10 04:53:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97437570-7c5c-3d71-8568-41fceaad9764 | -18.95998 | -52.46077 | 2026-06-10 04:53:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 151a05ce-fcef-3cb6-b51e-53829e1c766c | -17.45182 | -47.18922 | 2026-06-10 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README11.md)
