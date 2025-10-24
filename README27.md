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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d111aa5-cd75-3919-a75d-e72bb40e7b47 | -16.67458 | -46.48671 | 2025-10-24 04:19:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9027249-95bb-3aae-afa3-a947d9f04045 | -7.55506 | -47.37151 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d05aae7a-eee0-33c2-bfce-acdff030d807 | -12.82161 | -50.97049 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27d6b2f3-e9dc-334e-b0a8-0b93d0178ddb | -7.67128 | -46.58485 | 2025-10-24 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c450dd4f-624d-3140-80be-55b940aec277 | -8.63089 | -44.80311 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 192f4280-9423-327b-8041-5aceacb62983 | -19.98923 | -44.22596 | 2025-10-24 04:19:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cff0a8ca-087b-3952-a16b-f129a937e57b | -15.19083 | -47.08852 | 2025-10-24 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89d398b6-ffc6-35c4-9200-f50cfd302d6a | -15.02077 | -46.20861 | 2025-10-24 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 4547b063-33de-30f4-a05a-c3ca41c454e6 | -18.35914 | -51.71451 | 2025-10-24 04:19:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c9130ab-fbef-3f3b-af04-41357f010813 | -7.5596 | -47.36759 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c03564eb-0f70-33db-9cde-0e9d1558091b | -12.82463 | -48.63373 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3fa7b30-8548-3e1e-8ca5-3785d55a635e | -12.82315 | -50.9619 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6af8f85-b3d7-3aa7-b3ab-3cadf17a21fd | -7.62989 | -42.18656 | 2025-10-24 04:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| df72fd25-d36a-30eb-b0f4-15781d2b0c85 | -17.59696 | -46.63093 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9cd56603-e286-3433-a0c6-9c22c1e16649 | -12.8466 | -48.55293 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d4e223a-a5aa-3d30-bdc9-bfa176fa1b57 | -12.8309 | -47.24316 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c27c0e4-7da8-34d7-bb82-335c6b5e8c51 | -7.27349 | -50.00868 | 2025-10-24 04:19:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 301d2b48-ae25-34dc-baf6-6d37a9c04997 | -13.02365 | -47.23466 | 2025-10-24 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d05bba4-2615-3e5f-9254-9e749d449eb1 | -13.35075 | -47.97832 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc9e335e-8e68-376c-9bbd-3a530a7f26ff | -8.64329 | -44.79042 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1747438e-bb8e-32c2-913e-853f5eb0148f | -17.5948 | -46.62299 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e959aa5-4ca2-3691-8bb9-895ce2a71307 | -6.7665 | -45.48192 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24208bf3-e77f-3d84-ad84-ccbbf7f24265 | -6.07999 | -49.3808 | 2025-10-24 04:19:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13000a46-6096-33a1-ba2e-70f4b924cf65 | -6.11247 | -48.10736 | 2025-10-24 04:19:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a62193b-b74b-3005-811b-9dfe87ef6dd5 | -20.44042 | -44.13966 | 2025-10-24 04:19:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5e98a89f-f715-382f-9af1-591236ab19cb | -6.93305 | -44.01499 | 2025-10-24 04:19:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f10d335f-f9dd-358d-842f-5a628db2c929 | -12.82619 | -48.66912 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78106cf1-206e-33b3-9c25-c183242d3430 | -14.43877 | -50.95598 | 2025-10-24 04:19:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac235738-2b44-35e2-8e68-5df8e107f6e0 | -7.65663 | -47.41044 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a58153da-0616-3ebd-8a28-3eca13207f9a | -13.89981 | -46.65136 | 2025-10-24 04:19:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e562c0b-e69d-37f4-95fa-ae938f8c5b97 | -8.32246 | -46.25185 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 58a5e9ff-e2bb-3333-a496-640a1030d034 | -12.80477 | -48.66352 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4269002-d52e-3822-a1e4-8c4d79c687e4 | -7.66041 | -47.41109 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c60ae48-2f3e-3678-a688-1f9188a9b20c | -11.5584 | -54.51868 | 2025-10-24 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2464289e-bd7c-3f16-a4f5-e53966f7faad | -7.07589 | -41.59349 | 2025-10-24 04:19:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 645acf1c-c94d-3638-b7a2-4e170fd01d7a | -13.36188 | -50.46598 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20ffe99c-e91d-34a9-b93b-6c5584f53c1c | -12.36926 | -51.46818 | 2025-10-24 04:19:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fb30b37-1ec8-3103-aa96-13debc503bbe | -18.52679 | -44.62102 | 2025-10-24 04:19:00 | NPP-375D | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 77bae03f-b5b4-37b4-bf1b-e5791b37081c | -8.32311 | -46.24784 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9217c005-3d2f-3fda-a1ac-be5a61e97cac | -6.76935 | -45.48634 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0deac2f3-434c-38c3-b0ff-4497e63c474c | -14.54131 | -48.02847 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51305a57-c875-34a5-8f99-41246c59860f | -17.42848 | -46.20438 | 2025-10-24 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b798238-d6b4-31fc-b241-1d7b0fa274ad | -7.66118 | -46.87163 | 2025-10-24 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe9c1018-28eb-36a4-a70c-67cca85fe803 | -6.98342 | -48.68179 | 2025-10-24 04:19:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a63e2091-df86-3a7d-a0f6-662984a0c16a | -13.92351 | -48.38973 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fa78366-3306-3a21-8887-a1d4b1a215ce | -14.43029 | -50.95433 | 2025-10-24 04:19:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7149e161-d51c-3c4d-b635-43b8191d78ac | -13.50465 | -47.42393 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 905f3155-69e4-35bc-9166-bede42d0803a | -6.9464 | -44.01713 | 2025-10-24 04:19:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a150d2e-f6b1-31f1-8c14-6cee75cfe81e | -12.82264 | -50.93966 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 152e0ceb-e41e-34c4-9ea8-de7538e9d46a | -14.4785 | -47.92188 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dc52383a-4ee0-3b0c-a49c-598501af4e9f | -7.02561 | -43.92194 | 2025-10-24 04:19:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f51840a8-8cce-3a04-b3e1-a948d5092a01 | -13.29832 | -47.44905 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 514ad724-bcb3-398b-810f-56184981b313 | -8.46512 | -45.56434 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 558993eb-3cc1-31c7-a33c-91c8ca464e34 | -8.08784 | -46.9098 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b55cc98-16db-3d9b-9a87-4de26dbb83c3 | -13.64237 | -49.45712 | 2025-10-24 04:19:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c7e7544-88d6-334d-b1a4-444a84bc53d2 | -6.74571 | -48.05636 | 2025-10-24 04:19:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdf31508-d768-3443-8b78-30edd2030f78 | -7.30474 | -46.94697 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1ec7dc2-4266-3803-889f-37d4ae9b56f1 | -12.4171 | -54.36633 | 2025-10-24 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 212ac804-8735-33d7-96fb-d348d1622a54 | -14.75699 | -46.60315 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f17b4cbf-ed20-3bab-8b06-d75a88fe4f31 | -6.02483 | -48.90611 | 2025-10-24 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5121621f-a867-3dd1-b7b6-bfc39729a41d | -8.07427 | -49.71555 | 2025-10-24 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4929a0f9-8289-3053-a911-3b2482532157 | -13.33038 | -47.96655 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97dd6b12-5f69-35dd-aedd-1b637fb4626d | -7.64016 | -42.29812 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1c48fa83-56ee-3f0c-bade-e1ed7f99fe4c | -8.15238 | -43.39027 | 2025-10-24 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9f65b077-6c09-3b59-8934-f5a740c32db5 | -8.31827 | -46.25523 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2082c69d-93b9-368d-bbdc-b3ad6331a359 | -14.43103 | -50.95029 | 2025-10-24 04:19:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3068e63a-d9d4-3f21-8e34-00eeda35a252 | -8.64607 | -44.79455 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4381527a-ea31-3752-a823-076272c4ea8f | -13.19167 | -47.75208 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3765cf94-3f02-3c95-9b70-1263f6135ccb | -17.65728 | -46.65257 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5595912-4d25-3642-b423-5e1fd490a031 | -7.33598 | -49.04546 | 2025-10-24 04:19:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2086adf6-0e0d-3d43-8e45-556039bce9b1 | -19.98981 | -44.22197 | 2025-10-24 04:19:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 472c3912-08fb-38f4-a7dc-63c66254338a | -16.95412 | -53.22154 | 2025-10-24 04:19:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b63473b4-a88d-3b8a-b695-b6af1ae654dc | -6.94696 | -44.01362 | 2025-10-24 04:19:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40316d73-46f8-3879-8aad-af772736befe | -17.65549 | -46.6636 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 821c5621-830f-3602-8b69-278b33cfe868 | -6.77755 | -45.4798 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| a6dcd1be-d898-3f0d-b513-ff839861a316 | -13.40334 | -47.36232 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfb2b8e2-a975-31e0-913e-1e7444f9e24c | -8.64886 | -44.79869 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac67370e-674c-3b84-9e66-31d602ebc3c9 | -13.9216 | -50.26572 | 2025-10-24 04:19:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 427d4545-7edb-30ae-a5b1-6fcca2684309 | -8.10825 | -47.04994 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e235e74-20ec-34be-a555-65478b3876c5 | -15.94458 | -45.21688 | 2025-10-24 04:19:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54b018e7-a507-3503-8848-f6ca020358bf | -16.5449 | -46.43855 | 2025-10-24 04:19:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb90decf-5d82-3569-b417-66e5274e1b40 | -8.05704 | -46.48344 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dedb9354-845c-37e2-92ca-bc8c8b101fb6 | -8.66065 | -44.78971 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26ce774a-518f-3b7d-91c3-40e3edbf979d | -17.40459 | -52.01591 | 2025-10-24 04:19:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9aa05022-4da9-3e14-857e-5b3e36d4e7d3 | -8.32511 | -46.7846 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e266591a-f1bb-3f9c-9371-5a65b95b89b6 | -5.74425 | -51.07715 | 2025-10-24 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59775d22-e35e-34d0-bddf-a061ac491dcf | -19.23661 | -46.88997 | 2025-10-24 04:19:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8e0399ad-b5f7-34f6-9ddf-1651f57fa818 | -17.31616 | -43.60194 | 2025-10-24 04:19:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 502ecdeb-af1b-3774-a9bb-85cf78276f73 | -8.09081 | -46.91457 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ced820db-16cd-338b-b570-adaa27436b49 | -15.57258 | -47.71886 | 2025-10-24 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8da7cbe-29f1-34c8-a524-0b8e7274d7d6 | -7.05734 | -43.16687 | 2025-10-24 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f89c7fe7-2cfa-3670-996b-4cff580175e8 | -15.83532 | -49.09139 | 2025-10-24 04:19:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8410fda-4ceb-3474-bac4-1c2b6330ad1b | -6.76997 | -45.48253 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28e3c122-e205-32d0-b6f1-74a718de7f02 | -15.82749 | -45.65407 | 2025-10-24 04:19:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1b224d1b-0f1c-3770-81ff-99567cd98730 | -19.15533 | -51.86765 | 2025-10-24 04:19:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 970c0cd6-7764-3ce5-bed2-74e25f01ef5c | -7.00104 | -42.79446 | 2025-10-24 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9dd8f9c8-8f29-394c-9996-06bcf7e1b9a6 | -13.28159 | -47.48344 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d50aec8c-ce01-3334-a89d-da2f9504f675 | -7.68331 | -42.24258 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 23d2c452-6873-35ab-a1ff-dbe851e87a4c | -7.69204 | -42.23988 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 19f7d44d-2be9-36b8-87ff-073ee19aaf6e | -17.04048 | -51.50003 | 2025-10-24 04:19:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README28.md)
