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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b334de02-e422-3a06-8a76-5a3a52376e4e | -16.38063 | -47.05858 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d8fa33b-224f-328a-bf0c-5cc8aed83830 | -15.7583 | -43.6953 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c5fb9a2-e496-34c6-9871-b116793ee688 | -15.80476 | -43.31881 | 2025-10-01 04:21:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f663faf3-c950-3ce5-bcd8-3466ead5d093 | -11.47006 | -45.10138 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b3d3284-a67d-30bb-98fc-e90019aa64fc | -14.68128 | -48.12541 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ae5e1767-09a8-3a43-a82b-2fe0607690e9 | -14.35592 | -45.92566 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f734cbf5-982c-3f0b-bb74-557d2cf250ed | -17.40028 | -47.17096 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7114540e-c6a0-3d8c-9362-204bc2d470b9 | -14.0939 | -49.74622 | 2025-10-01 04:21:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 568488c7-eead-3096-a8f4-7c952538e770 | -13.76507 | -51.22056 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 021be720-18e1-3a94-ab32-29c72f9043d1 | -12.77229 | -46.89094 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9efc380e-678a-389f-8b22-8f8198c898c1 | -13.79771 | -48.02613 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b2420e7-8d4c-3b2c-93db-04ca4b49c20d | -12.88225 | -45.26984 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98eb57bb-aad3-3e33-9953-a3ff766944c0 | -12.97532 | -48.42524 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc8e1861-fe40-379f-bc47-cb233f34571b | -10.06756 | -50.26982 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a36e4ab9-5302-32a2-a30b-0a72b682d994 | -14.6855 | -45.27511 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78abd1ba-9c4a-32db-93e9-9a95b613bb57 | -15.39449 | -40.32155 | 2025-10-01 04:21:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c06c41f5-816a-3d00-9f9d-0fe6ef696a55 | -14.38165 | -47.13298 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24238439-867d-34b8-8772-9caa09216d26 | -10.90602 | -46.51126 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cf6edcaf-21ff-3f8c-8ebe-821b5a916043 | -15.93416 | -48.13138 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5d82e89-3700-3589-b29b-7e77fe32c169 | -9.23849 | -50.63216 | 2025-10-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0eb1092-a722-3f25-83f5-be543dd05dfa | -13.27717 | -47.22654 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d850fafd-c600-3d3f-bfd4-65bdb8caa8ba | -11.82313 | -44.99329 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7eb9312a-030d-31ad-bfff-8d470db8698f | -11.84533 | -45.00411 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3963040-72e7-3bf8-931d-6de3b645c730 | -11.63428 | -47.48857 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d26e2a65-f826-32f4-b510-57cfc94919c8 | -17.49661 | -43.47319 | 2025-10-01 04:21:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d34c1e3-cb56-3f88-adff-198fc7c1507a | -16.40324 | -47.04403 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b373453e-5181-3883-b3cf-8d195ab131b7 | -11.6835 | -45.32689 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2aa2b88a-d47b-37c9-9ad7-538b287a9330 | -9.32365 | -50.62452 | 2025-10-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93b347ad-029d-3b48-b4b9-706d478b5bfb | -11.94908 | -47.05769 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db4fa2ad-ebb2-3226-ba9e-f7b163aa1e41 | -15.83925 | -46.25032 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55512dc9-0cd0-3f22-a577-06ae3af0fc6e | -14.61111 | -48.31197 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1a6517e-efdc-3ce5-a5ec-6c5de5904b55 | -13.31108 | -47.20638 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71ee2974-ed16-3069-b5ef-5fa9f8d9496f | -11.11957 | -49.78842 | 2025-10-01 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf4823bd-637d-3fd2-850e-bbef8f547254 | -9.30595 | -51.56775 | 2025-10-01 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55a37414-b564-37e5-a1e2-ffa85ad985f0 | -14.68854 | -48.22918 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb497227-5007-3919-b14a-06bbaf4b7dce | -11.04913 | -47.82224 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00cf610a-a1e9-361a-a394-6a8e393d474f | -14.52231 | -48.36601 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8ea4477-f81f-375a-bce5-363cabab7fcf | -13.32346 | -48.14557 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adc31f14-5fcc-3694-813e-e74d9f379b3d | -14.36575 | -47.14525 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51fca253-46f1-3943-ac31-a37833f53f71 | -15.51014 | -45.868 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fec8e742-57ba-32bf-917d-7c1959f02cc0 | -15.80413 | -43.32328 | 2025-10-01 04:21:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dc2c6de-1dc8-3770-9bac-84ba02106034 | -13.33322 | -47.87163 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9d6fa091-24da-3f33-8573-6dd741270451 | -16.11828 | -48.40443 | 2025-10-01 04:21:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9527a7c4-d041-3684-8cfe-96b16899b576 | -11.84087 | -44.98878 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2e515dd-7c30-35b5-be5b-75f37008f52a | -11.56711 | -50.1764 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4828514a-28b3-360a-81e6-14ec306ba0c8 | -13.6551 | -47.31154 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67d71378-1216-304a-99e0-eae1a221c325 | -11.367 | -45.06356 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2cf4b19d-a929-3668-9457-fba8b0c6fc83 | -14.78134 | -45.78864 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 533916ed-e885-3391-97a8-593c9381f7d8 | -12.77692 | -46.88432 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebcd5f93-721e-3f02-9a51-a372e1e7a3aa | -13.33951 | -47.81164 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06e63ddb-dda6-3bb4-a3e6-79514d227e20 | -11.85367 | -45.01636 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2bda482e-e4a6-3bad-b9c9-1ef48a4bcc02 | -17.40414 | -47.16794 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13e48f77-298e-3ce8-9bb7-555e7abed377 | -10.90922 | -46.55521 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ad1703eb-18a0-37a4-9cb3-782c694fc0cb | -17.40526 | -47.16076 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d30c466f-0769-30a1-9ff8-2ba235190a7f | -11.19485 | -47.19891 | 2025-10-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ad6f5a11-3b97-3cf2-98b0-b75df4e9e288 | -14.49882 | -48.42373 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b911ea9-302e-3160-989c-8c53c884fb00 | -10.10874 | -50.2407 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 723d3f28-e7f7-342d-bbca-9db3d244a0e2 | -13.91893 | -48.09937 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fcc88d5-dcbb-3a32-943b-703067f028ae | -14.88366 | -48.32668 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a27ff3aa-83b3-3276-b79b-a31b5af251f4 | -17.2809 | -44.91814 | 2025-10-01 04:21:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 889108dc-b94d-3b45-8991-9a8c83909a55 | -13.63742 | -47.65221 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 727c5b2c-9e72-3240-8af2-b248f2423bde | -12.88267 | -46.90498 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0c513d0-411e-3da0-b75d-9658fb591957 | -14.35538 | -45.92922 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 04b3dd44-124d-3a26-be9f-07a37184d9e9 | -15.27419 | -49.2809 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20fa46a8-094d-338b-9e19-d2780bf9627f | -10.93032 | -46.508 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f729428e-0909-3f6d-b927-fecd957e671e | -10.82158 | -46.6354 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5efee30f-ec9a-3264-96a4-c4fbabec20e3 | -13.58112 | -47.60191 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a42b4ba-31ed-31c1-a2f6-686422fe13a4 | -10.64826 | -48.53735 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c90cceae-245d-3da0-b53e-ac804a4268bb | -11.10086 | -47.71926 | 2025-10-01 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef5b8caa-9a14-3982-9685-10be87b817f6 | -14.53246 | -48.36777 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a52f3931-06af-3a2c-8ddd-66a4279ee372 | -10.83398 | -47.78354 | 2025-10-01 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 298a3b65-cad9-3a5b-8d5a-f80700a5c90c | -15.76576 | -43.68133 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74b103c7-b954-3488-aca7-81e8ad419052 | -15.77775 | -43.6744 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83517c2f-2bee-378a-ad83-fc9d4cf299d0 | -13.23743 | -47.32657 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8f40284-c53c-39df-a754-3267b9a2b482 | -10.83594 | -46.65223 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96a658c8-c2cd-3960-83f1-76e4280cd4af | -13.34406 | -47.80485 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69aacea6-7965-3222-9cab-ced363db3532 | -14.69598 | -48.12002 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf24352d-704f-3c06-b450-f0d01ba5cb1e | -12.03409 | -47.90375 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a56e05eb-991a-3c6b-aa55-a7f8d625df76 | -15.27153 | -47.84638 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98f8f990-79bb-32b0-b886-5dbd001c8c2a | -14.51709 | -48.37658 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5144ac38-33d9-37e0-a987-e59e375952a3 | -13.10497 | -47.02621 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab1163cd-d7b1-3f41-8828-c8ee6f126cd9 | -11.95961 | -46.5864 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3535a43-dc53-388c-9732-e49c6f56ab1c | -13.73687 | -48.6914 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88626138-e32e-3c58-bc2f-3fc8782fcdc7 | -16.08911 | -51.0466 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0289f5c3-6a5b-38a7-8e05-b20dd4783c26 | -13.80974 | -47.87664 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc8c74d5-f9a9-395a-a7de-595f61793250 | -10.90641 | -46.57285 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c0f0a787-9e8d-3642-a164-392437911690 | -13.37651 | -47.32801 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a162182-7264-3fd9-ab4a-e9a4ac46e368 | -9.40117 | -54.71055 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57beec5d-798e-3f7b-a643-c44c4cce1cd6 | -10.92757 | -46.50393 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5cf7254-e1d8-3dd2-bc30-354bbee54e9e | -12.05683 | -44.86485 | 2025-10-01 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f41e7465-2f80-3fbb-8361-44dbf51fb725 | -14.79148 | -46.97192 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 013ceace-7e2a-3d5a-a281-1ad2a73b3357 | -10.70906 | -47.98913 | 2025-10-01 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da88c413-e0f5-3d23-9594-f8a7431dd085 | -15.27351 | -49.28495 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50f57599-ec88-3c07-8e0e-695cab7c32f0 | -11.87453 | -48.02071 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f36d6e9-4954-32a3-9d5b-1f1551bf0491 | -9.43165 | -54.57505 | 2025-10-01 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 460f2c31-6b8d-3b42-a4f1-27516912f25f | -15.25724 | -47.89239 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04232b53-8096-3928-83f7-4fb2b30579fe | -12.88763 | -45.18996 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83b6d272-d5ca-3b0e-b14f-5faaaadab00a | -11.76345 | -46.85563 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7da47d0f-af0d-3a3f-b077-9e98b6c613f6 | -17.18945 | -43.80434 | 2025-10-01 04:21:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11436c77-5ac9-3a24-a833-6fdafefd12bc | -14.35971 | -47.14053 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README58.md)
