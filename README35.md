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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f40b8f35-7fd3-371f-836a-72b04eed8f90 | -5.27098 | -44.73374 | 2025-09-28 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6d4488ff-1768-3ff2-887e-a7e1b0729c20 | -9.87796 | -45.9379 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78f6de02-9af1-3a4e-8eca-73e2d8fa2de7 | -9.67637 | -44.52258 | 2025-09-28 04:04:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46a831bd-799f-3483-830c-2c7cf7dee932 | -5.81143 | -42.79642 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0a5fe049-0251-3714-98b9-dfd7849d6c31 | -7.58304 | -43.9117 | 2025-09-28 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d194b3c4-2ddc-392e-8d65-cb6c1b0e3383 | -6.48475 | -44.24751 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d388bec-a037-3f3e-9105-a242290f447c | -6.49377 | -44.24646 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dab20f8e-5ea0-3be9-8a43-e97e58ad47c6 | -7.53565 | -46.11072 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9af0f7fa-8a31-36dc-91c0-67b4ffcf9e22 | -9.11332 | -46.6743 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2077c3f-7562-39e7-82ea-0491472af5a5 | -5.91237 | -42.9303 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4826d0df-ada9-3102-b51b-60050785acce | -4.1293 | -44.21979 | 2025-09-28 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1638d430-b5cb-365b-a007-5385a2758545 | -6.25029 | -42.4728 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a3b50213-07b2-3674-8ccc-b7bf2bc66112 | -7.38001 | -47.03967 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ba981742-cc7d-3102-aa18-fa41831929ba | -7.87206 | -44.55858 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e91cf457-e420-30a1-9ffd-14d3d6a13ac4 | -5.81299 | -42.80948 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3249854a-42aa-3de5-8a57-cbeb5c5dea73 | -5.98919 | -44.12674 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31520781-43ef-3944-b2b7-4db6855fb26d | -6.70198 | -44.60226 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26791182-c9db-3f19-9465-64a3e33abcae | -6.79354 | -46.18662 | 2025-09-28 04:04:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26dfe620-f04f-3162-8844-7e1d7e9e9a01 | -5.72912 | -42.65862 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6d8f4e2c-5cb9-3c5c-9e0d-4dcc69a97415 | -7.15339 | -45.50998 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fa32a26-77e5-3191-b2ae-a0920ed75e18 | -7.75303 | -45.74877 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f9e6fac-e7b2-3e2c-85f3-44879d5aeba2 | -4.67502 | -43.24747 | 2025-09-28 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af0a96ea-1fcc-3d60-aa49-7003cea89d3e | -3.83414 | -40.33131 | 2025-09-28 04:04:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b875bef9-6986-31a1-9244-ec235cb637a2 | -4.26186 | -48.5531 | 2025-09-28 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1db31166-9673-375b-b20c-d2627a8e4f20 | -8.49666 | -47.00951 | 2025-09-28 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e71872bb-871d-38cf-ba12-7d331efb3681 | -7.1032 | -44.23968 | 2025-09-28 04:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a7c75ed8-4c8d-31a0-a56c-e023e478f366 | -9.44044 | -43.69729 | 2025-09-28 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ae0d20bd-a7c2-34c9-b436-d3b77fae70bf | -8.83134 | -45.99322 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2168f12-9300-31e7-8c55-2d9edd127d28 | -7.76078 | -45.73357 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7dc3e7d9-b465-3f11-b224-3b2593ee513b | -5.96026 | -43.76926 | 2025-09-28 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34fd8dae-02a8-3d84-8b86-beb35ef084ef | -3.03261 | -50.4438 | 2025-09-28 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 275cdfc5-8e01-3785-8232-464b7c25df3b | -4.18317 | -38.11818 | 2025-09-28 04:04:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bffafd9b-6236-3c48-94a6-eac399fa07e6 | -4.68241 | -41.95211 | 2025-09-28 04:04:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a5168ee-2b42-3855-b562-3bae195991b7 | -8.28276 | -45.46166 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e6a44a9-915d-3bbb-b8fb-cb003529e9d4 | -7.14574 | -45.5048 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 979a2abe-2680-38ee-b2bf-8fd370af4786 | -9.31167 | -45.67246 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17bfbfd9-8c17-3544-b065-338b516ec0de | -5.45972 | -41.08588 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b60ea2f-b0ea-3079-8e92-b8d7ef933fca | -7.10398 | -44.23495 | 2025-09-28 04:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6957b948-3be6-36b8-be6c-49e405dc9b15 | -3.74937 | -39.52183 | 2025-09-28 04:04:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1a0322db-c34d-3878-9535-90ae46dc0c4c | -7.75785 | -47.00082 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e6b787f-6bf9-3583-b9d5-e8f0e4bee433 | -9.3399 | -47.55796 | 2025-09-28 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a95022cc-5ddd-3526-bbb9-5f816a92d7b5 | -8.29451 | -45.4417 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96f22343-bdb5-36bd-b2a2-324019417ab1 | -5.75879 | -41.7448 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3bef95d9-05b5-3ed7-b616-fde8f59384dd | -7.57188 | -42.4051 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1c0dd0ac-d3de-3733-a730-e6d6d9334b47 | -2.25635 | -47.88885 | 2025-09-28 04:04:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e975ea4-07ee-32f2-a264-ba795ef4784d | -8.48618 | -47.80551 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 898b426f-d750-3aa1-a54e-7e532a73a479 | -9.96113 | -43.59135 | 2025-09-28 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8079a99f-6114-3b6d-9b8b-29f15e181f19 | -6.61195 | -45.0876 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1384f9ff-8dcf-3b8d-8105-9bad11223297 | -5.74565 | -42.82919 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0ed116c9-25fa-3dc8-a54c-7c3b0084267b | -5.73512 | -42.84863 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 25f6cb2f-9be0-358f-8ad3-be29ab4a09d1 | -10.5354 | -43.6278 | 2025-09-28 04:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5e478218-d238-38a7-bf68-eae35d0290a6 | -8.20537 | -44.40071 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2326fa09-8b7b-3c49-9ae4-60fe4073af7a | -4.85765 | -49.46856 | 2025-09-28 04:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e61fdba4-a6fa-3f6b-b769-8457065dccfd | -5.69735 | -42.62878 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5f7d624e-c0cd-3d63-b812-310f95044bb1 | -6.06042 | -43.21087 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 15fba9a5-3c3a-37da-8626-7db99dba052e | -8.16803 | -46.4348 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6b7992e5-1655-3b2b-adfe-54f68993df95 | -6.87124 | -39.26764 | 2025-09-28 04:04:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2b8ad316-1fcc-3660-9345-d3f74049bab0 | -5.89739 | -43.95801 | 2025-09-28 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2fc3e725-2766-3b26-b387-d15d43c830fa | -5.94299 | -42.90154 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 570f33a0-1089-3c79-be2c-4ddb358c18c8 | -7.47079 | -44.44169 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1cffd27-c573-3c06-adbd-b288a5976adb | -3.32953 | -50.25009 | 2025-09-28 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0774db8-4f62-3866-b52a-cd8288b019c1 | -5.82029 | -44.44587 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a69ab5da-f4ef-3b11-8ed1-69469fbeb3ed | -7.85832 | -45.29284 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d5e5e35-48c5-3bf4-84fa-207a118c6374 | -6.70677 | -44.59777 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b34787c8-8cfe-3b9d-a33d-062c353251c7 | -10.04787 | -46.13475 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f2dde89-dc32-376d-9f55-f6dc4ba37675 | -6.27308 | -42.48823 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1e7201ad-af23-3c97-b8c5-61be973c9864 | -7.82117 | -45.14413 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 771d3417-ba37-334d-80af-8dbd6a598e66 | -4.8653 | -45.75913 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6bdafa7f-ad85-34f7-b7c4-49dae741770e | -9.451 | -47.61894 | 2025-09-28 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9af4203f-11c0-3cef-bb9e-6bc77e94c610 | -6.08985 | -49.39618 | 2025-09-28 04:04:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99aaa6cc-740e-3bdc-97f7-afaaa259bea6 | -5.91034 | -42.94274 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d3b51894-116e-375f-96d8-c95dc489b3ae | -5.09656 | -46.04386 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef2cc47c-0d89-3e53-9a0f-4ba9c15cf169 | -6.18291 | -46.71941 | 2025-09-28 04:04:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 114be7e1-f4ca-3e94-a663-42c0ba27a587 | -6.42682 | -43.07182 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2709f9f6-0d3c-3131-a1a9-ecca3250f877 | -6.42907 | -43.08074 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1acb2039-f895-3b34-aa0e-f3d1e14a68c8 | -8.85966 | -46.60315 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c935e31-2e71-3f72-8370-9feea82f9623 | -4.13329 | -44.22042 | 2025-09-28 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66fd346a-322d-3e6a-9b1b-7e5e54b2e544 | -5.36137 | -42.28014 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c6ce90eb-ea09-3b11-99c9-44883b09561e | -6.5817 | -44.43602 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 899546a8-506a-3522-ad2a-13bbae26ce18 | -4.15108 | -40.00074 | 2025-09-28 04:04:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3fa63fdc-d9e3-399f-9334-f6d7bd76332d | -5.96573 | -43.26721 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2077f3dd-573c-3aac-bba0-63d2dcc88879 | -5.89917 | -43.28873 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d87481d-7dc2-31f1-bf1c-877e547f4ec4 | -8.49288 | -44.7263 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a42998c2-dadc-30a6-995a-f5f9b0d91396 | -7.76144 | -45.72981 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14b8befa-5e58-3b8c-914f-ed0fa35c9835 | -7.8055 | -46.99488 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f69138ef-c5a5-35c2-89e6-765f31a05043 | -5.6074 | -43.37886 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 22dee756-ea60-3741-8d15-59d57551efeb | -7.06588 | -40.38774 | 2025-09-28 04:04:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dda9adf7-57d8-3999-935a-3439f95b972f | -5.65177 | -43.06312 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7a1c6085-5697-3518-9801-9d10d20050df | -5.81165 | -42.81768 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| e799f779-96fe-3b29-bd2b-32cd259ef2a7 | -7.80017 | -46.99871 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c88a7769-ee62-3de1-beb2-d468d9df2634 | -7.24566 | -44.75579 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9374cc8e-628b-3391-b555-8d8dcdeac831 | -2.44691 | -48.60783 | 2025-09-28 04:04:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d0c6e70-123a-3e7a-9466-8dc55c4da23e | -2.58109 | -48.40647 | 2025-09-28 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b092b967-a621-395c-bc55-6fba2867a222 | -5.69933 | -42.61675 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| df472117-cb5a-3c68-92dc-09f2fede452c | -5.59108 | -43.38529 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c92a2675-b58c-39ba-9626-5486f407ff70 | -7.76921 | -47.42083 | 2025-09-28 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2faa299-2285-3643-b3ce-ea812875ea72 | -6.11487 | -41.81248 | 2025-09-28 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5807613f-6d0f-3d3d-9d8d-38eff1388173 | -4.89651 | -37.72552 | 2025-09-28 04:04:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3a52e3bc-1a51-3a5b-aa0e-71e24d06d992 | -2.44677 | -48.60749 | 2025-09-28 04:04:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df808332-6346-354f-80d4-f08d11ae47b1 | -5.26379 | -42.88032 | 2025-09-28 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |


[Clique aqui para ver as próximas entradas](README36.md)
