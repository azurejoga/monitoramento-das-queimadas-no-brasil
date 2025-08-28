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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd7da761-3945-38bb-86bd-488ee3fa3504 | -12.18588 | -47.18511 | 2025-08-28 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8d4efcca-cb8d-39b7-b73c-d41c4ca8356d | -14.27754 | -53.06343 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 38.6 |
| caae0a05-a55f-3bfd-a5a6-4be966f70d43 | -9.16725 | -65.79858 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97167944-fe67-3c31-bdd3-ac11337458fd | -9.53545 | -62.39722 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f00cf8a-8566-323e-8ad0-305564a5723e | -11.56356 | -46.33683 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12026d55-1af8-3552-a2c0-e24fb2862a77 | -11.22798 | -55.0579 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| feef0056-06d0-3a4f-9e4c-0c54525ef355 | -11.24116 | -45.00336 | 2025-08-28 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4624ab33-c640-3a0b-a6c6-285e3ba4086f | -10.8073 | -60.76655 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 4e6a73b6-5e10-310d-a063-4f6e78d9de2b | -12.89082 | -48.09409 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 943fc07c-eaff-32ec-904a-0ecb3668b0ee | -15.62706 | -52.74844 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bf15f2c-09a7-30e2-9d15-196a93fe4fbd | -10.4697 | -57.94254 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b58bdb5-f9a4-3be6-b3e2-d8b93fbb9f1a | -9.78849 | -64.25152 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20fe7313-37a8-39b6-af3e-dca87e94ab5e | -13.42526 | -46.96669 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1956a6f-e056-366b-88a8-57a821f89bf9 | -9.10599 | -65.7446 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34ba40bf-6581-3054-b9d1-7df3e9ef7ec8 | -9.15755 | -59.53043 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0287550-b842-3f10-a84b-62bfccbe27b2 | -10.79781 | -60.77254 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 601722cd-21ca-3b7e-979f-4c6fd452c70c | -13.44693 | -46.96338 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29fda569-1c07-3ca7-8beb-0addbc113f60 | -14.14867 | -53.96738 | 2025-08-28 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9d542da0-9b0d-3557-987c-bdfc883418df | -9.1202 | -67.70888 | 2025-08-28 04:59:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e73b218-d062-3724-a4f2-a579b66711b8 | -14.31113 | -60.35493 | 2025-08-28 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ca88c03-ae67-303d-8207-fae91dd670ec | -10.47673 | -57.94369 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cc960052-43c3-3c85-89d3-b32139211156 | -12.81981 | -48.11729 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f6c6e4b0-0f03-3703-9915-b26e80ed9105 | -11.80627 | -46.79444 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5db97c45-16b1-39c9-b5eb-466c307f5085 | -13.83682 | -46.68595 | 2025-08-28 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfeb38b2-5746-332b-a7e5-7a1aa1ac2672 | -10.80191 | -60.77325 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 083f2499-b0f5-393d-ac84-69195e112992 | -15.60675 | -52.71561 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f5625d3-0071-31ea-b521-7133ed6dbf84 | -12.72039 | -48.17181 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| daa313ef-db22-3d54-be7c-800cec310591 | -13.00998 | -56.89715 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 803d1174-94db-3f5f-9081-bb5be5d02b73 | -15.62397 | -52.74335 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 632c50a9-cdd9-3b1e-b937-2d5182f9a763 | -9.50967 | -62.78829 | 2025-08-28 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07a612ef-1ed3-3a3a-a766-4832a650d61f | -15.63076 | -52.74899 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12a7d6af-37e2-3daa-8d4f-3076cebbee0f | -9.41561 | -60.51153 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 381f4d03-0f26-354a-8e22-d452e9101514 | -9.8052 | -61.1996 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6a9dc718-8139-3d9c-b004-648d6aa89404 | -8.34829 | -62.94018 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcbc2f41-ef6e-3f3f-96c2-90a062401526 | -8.34538 | -62.928 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6cd464cc-aedd-3dbb-a453-e680e485607c | -8.92843 | -65.92324 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49a626f1-7810-3392-af05-36b8e103da47 | -9.11186 | -65.7456 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ec615ee-5e26-344c-87e1-3f4a6ce02050 | -14.34216 | -53.34968 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c624f9b-a07b-364f-939c-017ac9850895 | -13.55125 | -46.89705 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12297850-3639-34db-b3b9-9067aa89f271 | -8.94131 | -65.95309 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f493bd23-74ad-37c0-956d-2af92caeb1d8 | -12.81665 | -48.14253 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8a88113-1bdb-3733-8c13-1207c480220b | -11.56819 | -46.38639 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4508d4ae-a6a8-39e1-829f-71c9d09776fa | -11.58432 | -46.38676 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bc66364-7b9d-300e-97e9-0541d7c289f0 | -13.46074 | -46.98074 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c11f88c-ffe3-3e87-9f16-4126248944e4 | -12.41194 | -47.79077 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 326694b2-3cae-371a-ba54-ed0a4c884cd0 | -15.6814 | -52.76561 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3ea5445-40e3-3fc0-a69e-3e87e06d1ac4 | -8.96267 | -65.95519 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b6c67f3-7ba6-3ed1-8cb0-794c32fafa14 | -14.5462 | -48.17902 | 2025-08-28 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ddc67dd-4519-3729-963b-643c814008a0 | -10.10704 | -62.92198 | 2025-08-28 04:59:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9540f64a-e99f-38fc-bdee-b5cfd76c5124 | -15.62336 | -52.74784 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a63a67fa-ff3d-3dab-ac56-aa2b7f280249 | -11.23405 | -55.06246 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a2a7c86-a89f-30ff-801a-ad1250df4e49 | -11.9186 | -46.70622 | 2025-08-28 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 273ba303-608c-3a40-8dd4-a84cbd73f85f | -15.63695 | -52.75901 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74cdd7e7-4783-3c45-9352-516f5cbbde71 | -12.81599 | -48.14777 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7806efc-18ef-3cdb-8311-78ccb78d6728 | -10.53829 | -46.7098 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 731a52f0-c769-3ecc-8455-1edd13553eb9 | -11.55772 | -46.34033 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a1e4928-276a-328c-93d2-389585db8b10 | -8.95155 | -65.96426 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8ab184d0-ecba-3af5-98fa-e28eef015881 | -9.08657 | -65.7187 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0505b26f-57c6-3579-b5d0-27a45fc034f8 | -12.74367 | -48.17978 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a2fb992-f8cb-3329-9d4a-bbc5fcf197e7 | -9.13688 | -65.76646 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9ec01d7-dd47-32e7-9fc0-fc1a90adc957 | -12.9605 | -44.58465 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c95962f5-fbad-3640-8338-17eb7dad47c7 | -12.95635 | -46.33948 | 2025-08-28 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35471b87-76e5-3d63-9160-95b9ae885b89 | -14.52109 | -53.00245 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 529f3b73-650d-374a-91a2-c70b31694338 | -13.10375 | -57.12005 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8ebb678-f989-344d-8404-33c621718aef | -9.08658 | -65.74413 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d96f6779-a142-35fc-b9a6-78906066e5fb | -8.94727 | -65.95416 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 844c65fa-95ff-339e-b4a4-34cf93cab063 | -10.6195 | -54.90328 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dd405ec-9308-39b5-af7f-d7278584516e | -11.90232 | -55.53265 | 2025-08-28 04:59:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2418962-c52d-3d25-93e6-b6e689d0636a | -9.41515 | -60.53853 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd8f6f83-3193-3302-81a3-ea81252e02b0 | -14.33276 | -51.90883 | 2025-08-28 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a04495c-bd9f-3521-8ded-008c9c7b8c36 | -12.89952 | -48.10559 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9b60ecb7-bc0d-3ae3-b903-e265379ba71b | -11.22743 | -55.06141 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebb8df32-b38b-3bf2-97a2-dc175345e1db | -13.81102 | -52.74055 | 2025-08-28 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffc3a008-b7bd-37a4-9bb5-2ddf13ae578c | -9.312 | -57.69661 | 2025-08-28 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22ffec1d-efa0-3a5d-8eec-6023522485bc | -14.2682 | -53.06392 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 794e5e44-19af-3aa2-9e90-b0aef07ca1a2 | -12.6816 | -48.17117 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 286d6653-96f5-3c03-a1eb-921cfc973522 | -15.62515 | -52.74612 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ce20191-7957-3e1c-845e-f49a91d824bb | -9.48771 | -62.3799 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa784a4a-3434-3142-b588-ac8ec9dc2ade | -8.34727 | -62.94585 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39ad09b2-e59d-3ae5-a7ae-fbb1347e81bd | -9.73785 | -64.90056 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c47ae1c4-6dec-335c-a999-b8e8b0d02c52 | -14.32692 | -53.28003 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5e4be2c-aa3d-30ff-8ac3-04f1933c5649 | -12.99824 | -56.90629 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 344899dc-27f4-3d18-b9d1-9b2a035138d1 | -13.3547 | -54.38871 | 2025-08-28 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a093b14-5b54-305b-9617-ed969993732b | -12.68204 | -48.16369 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3562ec10-3878-3000-acb1-79ede85822ac | -13.42866 | -46.84986 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e98691c-c0e8-3f96-a615-cdaf914f4790 | -12.81312 | -48.13174 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6a68d87f-598b-37f5-9442-e9427c419648 | -8.94809 | -65.94972 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 147644bf-4223-36a8-a77f-4c6fc597a014 | -12.8105 | -48.15271 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 739635c4-fc3b-35b1-acc2-d2ed34f49765 | -10.59634 | -54.89962 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe863043-ba0f-3564-aba5-fcb900c6e385 | -12.88303 | -48.11961 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 254fc94a-c448-314c-bb20-04167067ab10 | -13.73253 | -51.91668 | 2025-08-28 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2603e27-6d03-3d4c-ac4f-dfdbe038e915 | -10.52414 | -46.69809 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4048e5d-0b45-3bfc-80a2-6ea0ef14fc74 | -12.78258 | -48.17957 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f923cf0-62b4-33f5-addf-c36695f60b05 | -9.01436 | -65.68916 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b263d04-ed99-3739-b311-10a57d3e857b | -10.31602 | -62.62012 | 2025-08-28 04:59:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ba6d558-9ef8-3562-9709-fc0f8d7319fe | -12.73891 | -48.17897 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 053de348-23a1-3e60-9629-a118656fc4ae | -11.53614 | -54.40249 | 2025-08-28 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fdc1bbe-e21f-3555-8029-f4d9c7544052 | -11.33009 | -43.52938 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46a1a314-a18e-3d30-9bbd-acc6f9fba72d | -10.47321 | -57.94312 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 975d0dd8-b7c9-3571-8078-4164282b0c09 | -15.62396 | -52.71556 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README55.md)
