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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b91a6186-fcde-36b9-9bc0-a081245e318a | -12.19526 | -50.54832 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abfe8b2a-cb3f-3993-a23b-266e9402eb38 | -8.58454 | -54.82061 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7e58df2-2350-3d81-bbd5-8f2c57bdf4b0 | -8.52563 | -54.8195 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 059dcab8-25b4-3cf7-9e0c-b3c334fd2f3b | -9.20718 | -51.54698 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f362176-76f6-38c2-a49c-0eebe2470f62 | -8.60343 | -54.77299 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c81c1839-760c-3f21-a2c9-f7356ae29ef2 | -7.5236 | -61.37277 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fa5d9d1-3a10-3ea0-853c-f9ea90435f4b | -7.48273 | -61.40734 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e71ee861-f231-3a32-ba1e-47929d3bd4fe | -6.84475 | -59.94768 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cc5eda4-7b61-3dd2-add1-642616e37c4b | -10.75675 | -54.04403 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb9ee239-9de4-36a3-8553-c3c703b3ef7d | -11.36128 | -45.14996 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 149ab34a-6938-35fd-9554-656cf914a606 | -17.82588 | -50.95679 | 2026-08-29 04:53:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eb8bf17d-be26-3235-b4ff-7a421fb36d2f | -9.97457 | -53.93587 | 2026-08-29 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36ebd1d9-4654-33bd-8c57-dff8dfe1dcbf | -16.61339 | -49.40842 | 2026-08-29 04:53:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72310bb7-32f7-3096-89d1-10734d130b0a | -11.29203 | -54.03311 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3b0b0e7-72e2-37fc-bad2-ee4ee9298d9c | -7.29088 | -49.95079 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4ae844c-989d-3585-8d8f-6d6de1a101b0 | -8.66334 | -49.5454 | 2026-08-29 04:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dea1ce7b-6d74-3eb8-8b9e-3aa3c4473b05 | -9.93237 | -60.43702 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6de040e-967e-3d76-b84f-70d5c7e8dd10 | -6.15651 | -57.79677 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f2492919-7ef0-3772-8297-1bcd1c7c18a2 | -7.00124 | -59.63796 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 653e1384-3980-374a-8309-f52d372937c2 | -11.48464 | -45.10187 | 2026-08-29 04:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4bd199b8-4e81-3e52-a4e0-769c5c0c9b0c | -6.74599 | -52.45221 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f64c31f-a7aa-3318-9ee9-71be9eba203c | -11.03289 | -57.22312 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d2971b99-ec97-31aa-b460-7f73aedad72d | -7.25024 | -51.7426 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45fe3311-4e13-3106-9f68-6cb52bdb1fd7 | -11.22145 | -53.99088 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 850a8987-a753-3e3b-a778-c32f6867cbe9 | -8.04741 | -54.00784 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b578f522-e14a-3a1e-9407-58c080030868 | -11.4874 | -45.06362 | 2026-08-29 04:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 289ae859-a808-3bb0-8ac8-c166bae12906 | -11.03203 | -57.2168 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b9ddc109-5e5a-3ca7-a415-4ff7bc9d647e | -12.18779 | -50.57434 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8dc57aa-e1d1-3ce6-b2e7-2b42c5b03fc8 | -11.02224 | -57.2501 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 952297d8-4bd8-36fd-aa2c-3bd1c086ffde | -19.28028 | -49.52049 | 2026-08-29 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 566d1e05-44e4-3c0b-a0d3-bc73f0eaece2 | -19.2881 | -49.52161 | 2026-08-29 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca781d26-754c-31ca-a459-8efdb9ba4b58 | -10.82927 | -50.51139 | 2026-08-29 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b446b797-f5bc-3e49-bf1b-66a83065fd9d | -11.36932 | -45.16047 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9c439b58-c14c-3ba3-8825-39b263aae432 | -7.36707 | -55.17448 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55d0cd92-ee05-3513-9180-e27ca7d4f15d | -7.28693 | -49.95396 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5c7b2ab8-c6fd-3f64-8e57-728314678cd6 | -11.03208 | -57.25084 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82a3adff-a6f1-3096-8cc6-a3bd0bdaa611 | -9.16285 | -58.30923 | 2026-08-29 04:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e247b6c1-03f9-3e13-a48e-7ac62cffa947 | -7.20238 | -42.73696 | 2026-08-29 04:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 544cf79c-e3e0-3306-816b-cfd239891d7f | -6.95135 | -45.22677 | 2026-08-29 04:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6090b56b-0d29-3384-9799-25e0b27c9c3d | -8.94844 | -62.409 | 2026-08-29 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6651bc3-b444-3125-9e99-09d467325c6e | -10.80913 | -50.64439 | 2026-08-29 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1126a516-bf85-3c20-b3ba-d20e25b9f922 | -6.7511 | -58.72272 | 2026-08-29 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fc12c5b-0acf-3fe2-ae47-203c7a43c15c | -8.11641 | -51.65763 | 2026-08-29 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb19d688-1563-3cf8-9760-8f981c838c79 | -11.77892 | -47.65543 | 2026-08-29 04:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a3ce15c-9760-3eac-92ea-65ebbf0fd999 | -6.75871 | -46.13947 | 2026-08-29 04:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 793c14bb-5368-3b6d-9a9a-df61abae7105 | -9.43256 | -51.68978 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6898cc9-5f94-30f4-a645-f66fc237d848 | -7.30105 | -49.97433 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d087f8e-d51b-3ee4-98b9-5e66ea468a60 | -11.90745 | -55.89509 | 2026-08-29 04:53:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 395d7812-2013-3069-b024-399727684a5f | -9.22296 | -59.77443 | 2026-08-29 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8e002be-0279-345e-ab3a-5894580e099f | -8.01888 | -51.82336 | 2026-08-29 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab79941c-a5d4-3308-bbce-1415bbe9640a | -8.95423 | -62.41014 | 2026-08-29 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa4799f6-5ae6-363c-8fc6-fbd363b73752 | -11.36001 | -45.15928 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d02ee322-46ff-38cd-a76b-652bd23a4d5a | -11.22883 | -53.98835 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3084e621-4aa7-3930-aeab-23701286ad58 | -6.84068 | -59.94073 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7433547e-2321-3299-8c35-5caab84e36ca | -7.29767 | -49.9738 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ebed8159-fcee-3a1d-b6f8-660ae4ba2a39 | -7.58061 | -61.33767 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a3f630e-eef2-3c84-b929-701ffdd9db6b | -11.18246 | -51.28847 | 2026-08-29 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7c7ffe2-d3d2-3684-93a1-0a572d8b9b40 | -7.50417 | -55.27849 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ab1f53d-3fd6-3691-bd92-3385b63c2df5 | -6.17669 | -57.78661 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19718cdf-32ae-359e-be4c-249958f661e9 | -9.01876 | -57.54308 | 2026-08-29 04:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e5325be-ae18-3c71-9ed5-0086e1d26ed4 | -11.02799 | -57.22762 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1eae40aa-2856-3615-95c2-8d6582abfe28 | -7.35081 | -55.15777 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bd94b6b-558c-3076-a5a7-955d75518934 | -11.26271 | -54.02059 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a16e8243-2288-30b2-a1e6-3ffdc5e5c253 | -6.40766 | -51.67943 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b80e601-8147-32fb-8160-f0d86fc4bae0 | -17.58176 | -51.63919 | 2026-08-29 04:53:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d953283e-c4c1-3445-a9ab-03914eee4263 | -17.2841 | -46.03045 | 2026-08-29 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e35688f2-b3b2-3d72-ae45-fbef3ef90723 | -10.75614 | -54.04775 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81667fa1-169c-3d45-a1b8-800a755b36e6 | -7.27005 | -45.3515 | 2026-08-29 04:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16933dba-9526-327e-8716-8ade03edd356 | -16.47565 | -49.23562 | 2026-08-29 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10d72ba6-4c56-3c61-9107-187e9aa94160 | -9.40163 | -51.62766 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8b1fc17-f952-3324-98a9-738a92c7d435 | -6.81708 | -59.45406 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de44dd2b-09ab-3e78-b44d-a16d9f2ea717 | -11.02932 | -57.24321 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0112a41-9d83-3237-9cd7-1a1643cacab7 | -8.94904 | -63.27336 | 2026-08-29 04:53:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b4a607f-e1f8-318d-b004-31b24fc01daa | -8.76985 | -50.08221 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2eef7636-4e92-3c20-8a11-64158008c6c2 | -11.02343 | -57.24317 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d85018f-6dfe-3ffa-815a-3058f038cac1 | -12.43139 | -43.41556 | 2026-08-29 04:53:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0671ef4-636e-38ff-a546-6761f533daf1 | -9.20609 | -51.55392 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8f652b5-9fed-3cda-b176-851ab72b365e | -18.99947 | -47.43896 | 2026-08-29 04:53:00 | NOAA-20 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9508edf2-8818-3916-84f8-498df25d2a83 | -10.50575 | -59.62965 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd6584dd-32bb-3ac6-9b0a-2d46c5b03faf | -11.4875 | -45.09981 | 2026-08-29 04:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f894dd2-800b-32df-9413-955e18621ecb | -13.31753 | -48.2029 | 2026-08-29 04:53:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 553618f3-c0c3-3982-927a-4dbc0dc57f07 | -6.78048 | -55.66219 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| cccb9e31-ea07-3b6b-aa63-447fd4d36960 | -7.11964 | -43.16823 | 2026-08-29 04:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 26602ea5-22a0-3372-9003-d2f6abc84af9 | -11.27385 | -54.03765 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d09c0b3e-3ed4-37b9-b57a-f320aea29f12 | -11.0369 | -57.21228 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ad72fde1-0223-319f-8589-058ff0679101 | -7.51011 | -55.31204 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 8a58a863-dbb5-31eb-a908-64b41ef198ad | -8.68069 | -62.85173 | 2026-08-29 04:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9f911bb-f073-39dd-b87d-c9d5e01ac0df | -11.37524 | -45.13759 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4748112a-8d86-326f-b8c3-b672298b8b61 | -8.9581 | -50.79471 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41f22211-b3e7-3ff4-9dd5-d06c9dcb4a6e | -8.59512 | -54.80113 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73df9adb-6af6-3773-aab1-84be89e86f5e | -5.88458 | -57.75641 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f2009eee-4297-30d9-b142-1b5e514a48eb | -6.11183 | -57.82963 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7f3b95f8-1436-32e9-924f-74b1c282f42a | -8.94732 | -62.38305 | 2026-08-29 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26b44c22-c07e-3ad8-89af-4a14f3f91658 | -8.59181 | -54.7541 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b677116-9bd2-3541-b91c-c561efa47c1b | -9.40273 | -51.62068 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3f8b965-1d3f-325b-88a5-98927bdedc16 | -14.0793 | -44.06398 | 2026-08-29 04:53:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4747457f-d028-3f23-893e-4e74ed3c4e8a | -7.34347 | -55.16749 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a0ed2948-750e-369a-afe9-8db6d52c3f7e | -17.29302 | -46.03689 | 2026-08-29 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb0a257d-8d04-3b07-93f3-9154ce3f78fa | -9.20772 | -51.5435 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| edeeeb61-5a5a-336e-810f-fda2281ac9fc | -6.58755 | -51.63705 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README52.md)
