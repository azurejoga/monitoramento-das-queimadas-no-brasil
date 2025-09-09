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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af1a30ec-be3d-3e32-b490-4b400bf07d5e | -5.67749 | -45.4017 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6529eb8-3b86-3294-84c3-26c24dddde59 | -5.19438 | -43.03852 | 2025-09-09 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6abca742-344d-3d59-8282-56f0c5aa27a0 | -7.18961 | -44.91261 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1efee4e-d626-3ac7-a490-ed027e48c1e8 | -7.02513 | -44.93974 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3d6984f-b74a-3b5d-b326-c4f26ccf0898 | -5.81856 | -43.98119 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be761ee9-86ac-3816-9e98-d05466a02d49 | -5.36341 | -44.80191 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c1e65b0-a971-39fd-b9a6-8f78a8a64658 | -6.09618 | -44.14576 | 2025-09-09 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26c9f09d-6f26-3a4d-a3d4-8644896107aa | -6.30672 | -44.78653 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db7af7c6-897c-399d-a9b9-df2d0df6001a | -6.17695 | -43.39406 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 598d4155-dba2-33cc-9f90-653e2632d0ab | -5.87078 | -46.08825 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37fdeb4f-ed08-3e4e-9e02-a9d2586c9f10 | -5.9896 | -46.20351 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c8e5cd7-9c49-3d57-8052-dacdb56b3ace | -6.20966 | -43.38888 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82ba2efb-50a7-380f-a413-19c2f8cf3896 | -5.93894 | -45.77921 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3a4a8ec-026b-35d6-817a-cbbb6e037491 | -5.35976 | -42.63457 | 2025-09-09 04:32:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d01dd166-68fb-35eb-9203-d97654c472b5 | -5.83526 | -44.21071 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02dd4985-8993-3aee-9349-6b06308186bc | -5.45644 | -42.80491 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e5ab642b-c6dd-3d11-bee8-140c14afc910 | -6.40564 | -44.45303 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca74f3b8-05a5-33dc-91ee-4610c525eee5 | -5.7258 | -45.40033 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa470573-5d0a-34c1-aa06-c44ea9cd1d68 | -7.07671 | -45.20034 | 2025-09-09 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c357a95-a3c2-3da7-ad77-fbe448cb3827 | -5.5575 | -43.78769 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc21d4b6-dba3-3134-9f66-25929872dc08 | -5.57677 | -45.04137 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 543e704b-67bd-3293-a873-e6d42a2d9b36 | -5.93837 | -45.78299 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26ab817c-957b-34d7-9ade-4eafcc8146d7 | -5.64193 | -42.61368 | 2025-09-09 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5d4cfc96-9f03-3fc4-bf11-c53028b7907c | -6.40121 | -42.97663 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 053ff3d6-c53e-3496-b32c-834e4e26c1e0 | -5.19393 | -43.03972 | 2025-09-09 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87f6af8a-21cd-356f-a6cf-9abc267b5267 | -5.71552 | -43.89392 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf0c9a75-5605-3023-b972-c6b9a7ed19f0 | -5.78967 | -45.4259 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba77d464-c31e-3f92-bdca-56776532da0c | -5.87004 | -45.65688 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5190ee33-898d-3c9e-ab42-0781f3a37b99 | -6.18118 | -42.65489 | 2025-09-09 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 97cf297f-7b23-3f69-90e4-852cd506c9a0 | -4.42446 | -47.95665 | 2025-09-09 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 917c1f28-9e54-332d-8152-6f7a84c671ff | -5.65828 | -45.43428 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9f76166-84a0-3e2e-b6c5-63e2978cf39c | -5.46038 | -43.44333 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 845d8b86-11a5-3761-a8e1-c9fd0130af23 | -5.87418 | -46.08877 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bb882b0-30de-3a27-9d70-4cb73a3fbbdf | -6.26784 | -43.40454 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa57dea5-aadd-38ca-ba41-b3aa833d3d82 | -5.06608 | -42.90262 | 2025-09-09 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dfd14f98-7d09-35cf-8e6f-4ff292e94532 | -4.89776 | -49.92426 | 2025-09-09 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d728b209-9efc-308a-bd2e-264681291bb6 | -5.76855 | -45.5407 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd2c060c-5e5c-36af-8a37-9bf128bf6171 | -6.49278 | -42.41972 | 2025-09-09 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fb3502bb-a77b-375c-9b35-2cd856976177 | -5.81604 | -43.97909 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 641ab811-f0c2-388e-86a3-2fa28e416797 | -5.86156 | -42.5344 | 2025-09-09 04:32:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c1160844-6fad-3961-9824-6699acb6af60 | -5.76972 | -45.53309 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbb43740-eec3-36a5-b88b-5aa4f1b2b2ae | -7.07747 | -44.86206 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d350cce1-4a42-309f-9871-75d0ff924554 | -4.52751 | -54.84453 | 2025-09-09 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 342e2a02-012d-365c-bde5-046cf164906e | -6.46645 | -44.66808 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c278bd2-d0c1-3069-9040-c37f71b6de60 | -6.4009 | -44.43471 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ceabd526-e4a9-3222-b427-dbc23cacbeee | -5.2577 | -44.44439 | 2025-09-09 04:32:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e6d90a09-1b20-32cf-bfbd-9feaf07cff4b | -5.30811 | -44.51037 | 2025-09-09 04:32:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 97020840-2a8c-3560-9478-8a7484ccb484 | -5.65655 | -45.4222 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39e66bff-7b82-3c57-acf2-0034de90163f | -6.26856 | -43.39961 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7579ef44-2911-30df-951d-12b71eb3f51b | -6.87822 | -45.53204 | 2025-09-09 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 998badfe-1134-3b2f-a92f-33221c96b2a5 | -5.67807 | -45.39787 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fbc2d1f-dada-3526-b130-b1f30520f8ca | -5.98456 | -43.69911 | 2025-09-09 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6895c293-c3db-39f7-8f3f-690b15ac05f8 | -6.70083 | -43.5425 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed934c53-f19a-3e7b-aec8-cdaf14c81fbf | -7.0761 | -45.20444 | 2025-09-09 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 0ef435f6-3914-3af5-8cfa-64fa7fe04876 | -6.43876 | -43.60957 | 2025-09-09 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2491feda-7a8a-3680-b734-6cfa4ddbd69f | -7.29543 | -43.70341 | 2025-09-09 04:32:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8b9f038-8bc4-3f3c-85f2-157bc5a0962e | -6.55347 | -43.91228 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f99e7c5b-4890-34fd-bd28-a78fd418e7e6 | -5.77573 | -44.85214 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7453306f-a2fd-3316-bc94-29aac1bae2bf | -5.80389 | -44.83556 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33948ba8-a79e-350f-952c-dfb82f98f2db | -6.06449 | -43.12644 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 73c3419a-17c5-3764-8824-ab4da073339e | -5.69158 | -43.89959 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ead0abd-ed48-3948-aea0-9b56985f1ae4 | -6.23176 | -43.51599 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fa01b1ee-2323-32a2-b920-fded440d7cf7 | -4.95628 | -48.40619 | 2025-09-09 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e3d27c8-8470-3d3d-942d-90d0604e049b | -5.36467 | -44.7937 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf5cfaf0-b24d-36d7-98f0-4c7627166049 | -5.93723 | -45.76738 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e55c874d-3f8e-32d8-815a-71aa5f9620dd | -5.79287 | -49.39732 | 2025-09-09 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03563f81-6dc5-396e-a649-0db699903c6b | -6.81705 | -44.90414 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bad88fa4-515c-39ff-a5c2-4535b526b04b | -5.58271 | -42.90545 | 2025-09-09 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| af2a49a0-00dd-32db-9af3-0c3a6ab67a3d | -6.10193 | -44.13293 | 2025-09-09 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8dbc2d97-98d6-3626-a329-b0b68d5c2835 | -6.09504 | -45.9285 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b68d9d76-dce7-38b6-b999-ee7cf6702950 | -3.31148 | -48.71675 | 2025-09-09 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 449632b6-1143-3980-bf8b-ad666b0a1e43 | -6.39972 | -44.43758 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7343ca27-e3ab-30ac-bc47-71890a8682d5 | -7.17212 | -44.90572 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f0901bd-36b7-3a1a-9666-4f5db5e46f5c | -5.55681 | -43.7923 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0981d0f2-0019-360d-8618-88e34e2a807b | -6.20834 | -43.31695 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9bb1fc43-ac6a-349d-a641-ae28ce8bc1da | -4.61361 | -46.59267 | 2025-09-09 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33b3005f-3da5-3a42-a634-d8f08592b8c1 | -6.62112 | -44.00483 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 90d0a103-a428-3be9-bfbe-b336ee164069 | -5.49252 | -42.66922 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 836859dd-d9bb-3094-bdf0-f511592937fd | -4.30114 | -47.57453 | 2025-09-09 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebbd99aa-e013-3df8-974c-ebb0c12a80cb | -5.81686 | -43.96712 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 04b17808-3161-354a-9658-53382642571b | -5.48847 | -42.66859 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e31722ec-d663-3cb9-8bbe-1349df8aae77 | -6.34904 | -44.06727 | 2025-09-09 04:32:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23edee53-aa6d-34a5-b7ef-22c49dabbec0 | -5.42094 | -51.53568 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19b95303-e7a4-377e-9e5d-99b3b70c2e00 | -5.68576 | -43.9127 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6bb46ed8-2f10-3e2f-b7c1-028471f20f2b | -6.39861 | -43.88556 | 2025-09-09 04:32:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ee5a6c5-3cc4-3fd2-8235-95d36cbe81b6 | -3.24603 | -50.81222 | 2025-09-09 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6a96deb-7b4b-3712-a99d-115bed7f51c0 | -5.78907 | -45.42978 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1da9d546-0332-371a-b63c-1df3f18f41c2 | -6.40174 | -43.89076 | 2025-09-09 04:32:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e52d0c1d-b2d6-36f1-9681-99d1251c4cb6 | -6.1095 | -44.77639 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09effb86-4f2c-3993-a636-962058fc12fb | -5.95328 | -45.77756 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0085711f-06fa-3049-a5e9-58de8262a605 | -6.19118 | -45.80511 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c3aba6e-e0be-311e-8798-a2d702c189a5 | -5.69602 | -43.89562 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 619d821c-8830-347d-bb61-22342ac7ec5e | -6.20669 | -45.56558 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6900547-cc3b-3c26-aaa5-bcc6bda960c9 | -5.70704 | -45.41811 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43fe99fa-cf6b-3bc0-b0eb-d6a6c5997ec4 | -6.8412 | -44.8908 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57bd8c7e-51b4-3c0f-89de-39b31117aa7e | -5.63799 | -45.42726 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 490295b7-d158-3eb4-aa55-94707964296d | -6.40101 | -44.42868 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab202872-cbdd-3bc6-b1a7-db75d1c66e07 | -6.2083 | -45.02869 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63f07ed9-c11b-315c-9f9d-15a8c8145daf | -4.27262 | -48.18761 | 2025-09-09 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 243ec7dc-273a-3116-87f4-2975a727a647 | -6.21977 | -43.507 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README30.md)
