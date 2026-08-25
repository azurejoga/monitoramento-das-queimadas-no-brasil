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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 123ab50c-1048-3638-b12f-09ce6e2e609d | -7.3807 | -55.1703 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e169d4dc-8a77-3bca-88ec-d93a29962d5b | -6.4359 | -54.957401 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb41d17f-7731-329a-9f74-7535dc3b56bd | -12.4154 | -43.356899 | 2026-08-25 00:32:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90f26e2c-4d28-3940-8d3d-4f3db9e5f227 | -6.3464 | -54.7463 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e21ad22-104c-339d-8cd9-3a8c5dbf996a | -7.2286 | -45.830601 | 2026-08-25 00:32:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01442590-5b43-3cec-a77a-36bf4d201a26 | -10.3081 | -50.382301 | 2026-08-25 00:32:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27d2b168-ef9c-321f-9b84-4ed66d868964 | -6.7962 | -59.618599 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ffb5e475-3217-3254-8816-13c76a538e14 | -6.7089 | -55.569801 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb73369-0507-37c5-857b-72ac98b98f82 | -10.786 | -50.912601 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2db46ca4-a0ca-311c-85d3-0644ba0eac12 | -6.7608 | -59.644501 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58740117-acc8-3ea6-8ded-cb89bc80b855 | -6.8326 | -52.4758 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 337b3dfe-e375-3a72-8654-4db4c6f119d0 | -6.0126 | -57.649101 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ea039a5-3c60-31b3-9b69-4e86e7b04c41 | -9.9994 | -46.3866 | 2026-08-25 00:32:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f3cce6a-3dad-346f-8587-4dbb0f1a5a40 | -7.3248 | -64.641296 | 2026-08-25 00:32:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3df2e1fb-ff52-3c5d-b9d2-99090213a141 | -14.8745 | -52.634399 | 2026-08-25 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c9108da6-e875-3e91-ba4a-ff7973950ecb | -6.3595 | -54.7584 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 740d242f-eee4-3730-a29d-34630d783f81 | -10.0676 | -60.466301 | 2026-08-25 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8ef078d-dadd-3d3f-ad78-e680afd25ed9 | -6.9978 | -59.226101 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07620fde-c612-3c52-b3de-b7c726f04e6b | -3.5175 | -48.1558 | 2026-08-25 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11e9b789-6b52-3e28-8b80-58bc889945e9 | -6.2556 | -55.3881 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cfd82c7-f159-3516-9620-3bce99046c18 | -8.044 | -44.608002 | 2026-08-25 00:32:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ff24eb8e-05bb-3c87-9689-ccd9fd8b8a97 | -6.1212 | -57.813801 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6628a816-cd7b-3f6f-bd13-4d918a2e2350 | -3.5132 | -48.137501 | 2026-08-25 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78ad3b27-6679-3bd9-ac67-4ab13ab68ddc | -14.3868 | -52.9375 | 2026-08-25 00:32:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7954fb46-99eb-31a1-b33e-247242883160 | -6.2086 | -53.473 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebe796ef-6b5b-3a48-b401-3dc2b558776c | -6.8155 | -59.660198 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21adc74f-9ffc-3461-b63a-da62fd147031 | -6.7068 | -56.336399 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6348bcc7-8e7d-39ee-99ce-1e59175b43bd | -6.3399 | -54.762798 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cb46562-8b51-30d1-bfdb-29dae7f9af93 | -11.8499 | -43.778801 | 2026-08-25 00:32:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 54902037-3d02-31a8-8731-efb7f8fed918 | -7.482 | -55.344299 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52cab052-3a66-302f-830b-4af8fbaa8992 | -7.3151 | -64.643204 | 2026-08-25 00:32:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3609008-723d-323e-b0ba-8063b5399899 | -9.678 | -55.0793 | 2026-08-25 00:32:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d99abbe4-a219-3222-9f74-fbfcf928d2a8 | -5.7913 | -57.5336 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08395881-d16b-3015-909f-528f8de04653 | -6.1775 | -53.471901 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12da05b7-6a24-30f8-b2e1-5f8ae85c11fe | -8.6818 | -54.683201 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2769b39a-e9bd-3906-bebb-7609bade5241 | -6.164 | -53.458302 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf346adb-1f64-3297-bb25-2eaad8513e06 | -8.5403 | -55.286701 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0817144-15ce-3207-8540-e3b4bd249159 | -5.7828 | -57.587601 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b697c57-66cd-3643-aa10-a6d4b6f7aee5 | -10.3105 | -50.392601 | 2026-08-25 00:32:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0135fe48-e315-3b47-a809-6b251f46f5ec | -6.254 | -55.381199 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53214359-0e1f-3a53-980a-e0f9772fbed8 | -7.2457 | -44.050098 | 2026-08-25 00:32:00 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e366735a-1bc1-3642-9bba-19af193768e8 | -14.3538 | -52.883701 | 2026-08-25 00:32:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c767447-ca0e-32cb-9065-4b2bef70d72c | -9.168 | -58.308498 | 2026-08-25 00:32:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a4deb55-3cb2-304a-a29d-fc9a1cd1816a | -6.8044 | -59.562199 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c852a563-ef56-377e-bb52-645488b4f854 | -7.2514 | -45.313099 | 2026-08-25 00:32:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44091348-0bf7-39ca-957a-2e716eec7c68 | -6.6293 | -58.483398 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c54d076c-9c9b-3c1e-b993-a90b9fb8666f | -11.1599 | -53.9786 | 2026-08-25 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7080813-01b7-376f-96bf-ef6d55a077c1 | -6.0816 | -55.529499 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46e8ca9f-4a8d-34a4-9385-568a61e13b76 | -6.9544 | -56.476601 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22f5bffd-ca18-3d6a-95da-a0620d6b7073 | -6.8101 | -59.5882 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 348a48a5-a4aa-3096-9399-b000485bb311 | -7.4918 | -55.342098 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d1a0d83-85e0-33f5-91c2-d7e80320df80 | -6.7412 | -59.648701 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3fcf59d1-32a6-37e6-a3b9-1afe8c685f3f | -8.5968 | -54.7174 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c7c7cf3-bfff-3b74-a58c-78cc600b7af5 | -6.5492 | -58.492901 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71f717c1-0df3-3e37-b6b8-60ad0efc28cf | -12.7236 | -46.433201 | 2026-08-25 00:32:00 | METOP-B | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| acb926f1-59b1-3b8e-9ec7-a4df14566a92 | -15.3161 | -52.807201 | 2026-08-25 00:32:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d183ecb0-1bab-3b3d-9aa1-236cd7db968b | -7.2382 | -45.828201 | 2026-08-25 00:32:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f966e3ec-43ad-3612-993f-673fd4d9b9d0 | -8.037 | -44.580799 | 2026-08-25 00:32:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 36d02e2e-65b5-3c50-bf73-a0042b7ff835 | -10.7785 | -50.9244 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ce23df7-9cb2-316d-99cd-64739db396c0 | -8.0344 | -44.6106 | 2026-08-25 00:32:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 400595d9-64f6-31e3-8d99-be24eae57a25 | -14.2896 | -53.144798 | 2026-08-25 00:32:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4cdc5324-d8af-322a-b2e5-4429bca03619 | -14.3522 | -52.8764 | 2026-08-25 00:32:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d16af4e8-4c76-34e4-8212-755813a42074 | -7.0076 | -59.223999 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da7e0ae6-213f-3668-beb0-5a78e1d7d308 | -8.5748 | -55.257 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c32f522f-5ae3-317a-ad1e-db3840e62bff | -6.1638 | -53.680901 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bfb6ec2-e4fc-3368-8420-1926b52808a4 | -7.4965 | -55.3629 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85d467b2-d6cc-3d89-bf42-0ebfdb75be1c | -2.7948 | -48.647099 | 2026-08-25 00:32:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a40e0a00-d4f8-3d04-acf8-8d1724cc4c4c | -8.5475 | -54.7729 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61446cdf-a040-33e0-843d-1a1ad841587e | -7.6608 | -49.369301 | 2026-08-25 00:32:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70cd42cd-d683-33d9-b77a-9ed0c2026e89 | -7.5469 | -61.3433 | 2026-08-25 00:32:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23c7a6f2-db72-3d5a-9826-04ca77e128a5 | -8.6082 | -54.722099 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecc326c1-8837-33d5-9a36-bd57dee35cc7 | -6.2442 | -55.3834 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65c2b26d-aeb1-3eb4-ac38-5f2c0593fd38 | -12.8371 | -48.474701 | 2026-08-25 00:32:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bd8d72d-10df-3729-b5e7-490690ca1ce0 | -11.1517 | -53.9879 | 2026-08-25 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 729b298f-0b6e-301f-8d57-1113718c9286 | -5.7799 | -57.528702 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c979c3a1-06b1-310b-b865-d6b12e95e64f | -6.1721 | -55.428902 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22cb79d5-d6da-3d04-82d3-e429c844d740 | -12.8534 | -48.457298 | 2026-08-25 00:32:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9cdc0b8f-94a0-3434-a4a2-98b28bd861b7 | -6.6155 | -58.3741 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c9711b2-b8ce-36fd-a736-7117aee92d58 | -6.7472 | -59.6292 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 62486745-8375-30b5-b40a-80e721dac348 | -6.3562 | -54.744099 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7f5ae0d-8c1f-3c01-94c5-7c8002ddf7d9 | -8.5952 | -54.7104 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc9bca07-1366-3e89-95e6-2965518aa19c | -3.5219 | -48.174198 | 2026-08-25 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1a94884-d448-3c31-8738-eeb082a3e15e | -10.3363 | -45.0186 | 2026-08-25 00:32:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 830dedd4-ca5a-3216-8b72-f3ed3507ac3b | -7.3536 | -55.641899 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e718161f-0c10-33b2-8d42-6261d9baa36b | -6.1527 | -57.678299 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c644b76-04d0-3606-8483-8ff39c6bb871 | -6.2407 | -55.413399 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72e1ec65-ea38-39a9-a266-67874a3f6418 | -13.343 | -48.1819 | 2026-08-25 00:32:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 162b6bc5-8f3e-3756-ac80-2822b7afd779 | -7.3112 | -64.624496 | 2026-08-25 00:32:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a845d1ca-79b3-3630-998b-aad66188f594 | -7.2674 | -45.335602 | 2026-08-25 00:32:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7de72b53-95bc-3876-845e-9bb8344d50d2 | -14.9153 | -52.632301 | 2026-08-25 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| db5ccfcc-a924-3bc4-824c-82b3cb9137c6 | -11.4072 | -44.473499 | 2026-08-25 00:32:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 55f9c7f3-b872-3b17-af46-ada665c504cc | -8.0664 | -47.497299 | 2026-08-25 00:32:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e3d56d8-7ebf-353f-b1c6-e9f94db42dc2 | -6.5333 | -55.068501 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc67a3e9-b84d-313c-8f6a-c57a91d1a142 | -7.6577 | -49.3563 | 2026-08-25 00:32:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8725e11b-a6fb-36ac-b3a7-680ef0c02e35 | -8.565 | -55.2593 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f30c6857-284c-325e-ae50-5a9090e70910 | -7.3438 | -55.6441 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b98f432-f3ac-3cea-9d61-1963a18955ae | -7.0094 | -59.232399 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 77ebe688-5124-310e-91ce-0c2d4921e142 | -12.728 | -46.450199 | 2026-08-25 00:32:00 | METOP-B | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8994e6cf-9e1c-31b9-a361-7e00e017f4fb | -12.7376 | -44.207802 | 2026-08-25 00:32:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae2cf597-b4d6-3e10-a764-1ceb575f8166 | -6.8062 | -59.382401 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
