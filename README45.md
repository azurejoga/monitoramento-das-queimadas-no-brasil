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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2005c19-e402-3483-a7ac-33c434fc11f4 | -6.80654 | -43.43284 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aa168729-1cc0-375f-a69f-0ebf1e4396a3 | -7.26648 | -44.61764 | 2025-09-11 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ba332ad-b3dc-3c7d-a665-1cd182cf48b4 | -2.55553 | -47.71753 | 2025-09-11 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2b4691e-bcfa-3ee5-8107-b1066bc85c5f | -5.87839 | -45.66861 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89eb8ad6-2dd3-3cee-95bb-2fed66d95bba | -8.10815 | -49.24703 | 2025-09-11 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ee47d4e9-4774-31fc-b404-38b16265918a | -6.29779 | -42.21548 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5033e1bd-6e14-36cf-bc32-de1e44a3845a | -6.31322 | -43.41603 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1690690d-f417-3dec-8554-f9b72f2440c3 | -6.82372 | -45.59835 | 2025-09-11 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82872828-1602-3e7a-af10-0582d0409f43 | -7.33307 | -49.61159 | 2025-09-11 04:21:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a18c52fb-56b3-368a-a00c-bba86c36b65f | -5.85399 | -45.12364 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec6418a8-5f33-32c0-9336-c1088ecbbbba | -6.39284 | -43.51224 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6063eb29-982b-3a38-b4d8-5f7b09c31edb | -5.52716 | -44.34644 | 2025-09-11 04:21:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 032346e4-7c8d-392f-8840-aaa735108adc | -5.65925 | -43.89349 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ead17e8e-3ac6-32d9-9988-af36635ca874 | -5.47309 | -43.43631 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e4066bb-27dd-332f-8f1c-27ab440d25a5 | -7.3899 | -47.35181 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d78544f-d9d6-38bd-b11e-83fbff418645 | -8.66002 | -45.73364 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3067680f-884d-3406-9e05-9a70ae85bcb7 | -5.738 | -45.59986 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2079d307-f66d-399d-8663-851e62df81b1 | -9.06361 | -45.70474 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37ae28c7-443e-301d-9397-8fdea6d44bf4 | -8.02925 | -48.66089 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82eeea5e-d86e-31ab-b36d-29e9188af292 | -6.39842 | -42.59661 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e43872ed-6b1d-335c-94c6-c3b72fc6f26b | -6.62189 | -43.98928 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51831f83-09bf-3958-8024-4d82e4863bc3 | -6.33239 | -43.54657 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e50ed57-8213-3234-896b-e8db4de790bb | -5.35679 | -43.41151 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 675a0bee-1b65-3912-a59e-69d4608ae67d | -3.86611 | -52.39377 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 276acc6f-51c3-37ef-9bcf-343b4764481c | -5.69301 | -43.3365 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ba02ad94-a653-339f-a36b-906419aac66c | -4.90007 | -49.92228 | 2025-09-11 04:21:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 751d19e7-f42e-34e9-8727-368b7a4b0ea2 | -7.83975 | -45.40115 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec13f874-1397-346e-8cc3-61c7f3d37e41 | -8.07174 | -42.95365 | 2025-09-11 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e6771f1f-0188-39a4-ac36-7ce7283f5d78 | -5.23908 | -45.46246 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 355792dd-f785-366e-b619-6e44afa631c7 | -6.34747 | -43.04037 | 2025-09-11 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d971ce16-0dc1-3908-bdc7-b47d30dbacb8 | -5.89367 | -45.81015 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba44cf87-0f0b-337e-9327-ced6e44c84e9 | -8.23718 | -47.86305 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 918f129c-81cd-3077-97eb-2fbbbae32335 | -6.63931 | -44.07456 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddd2aa13-ed95-37da-9eec-a6bac079ae73 | -6.18294 | -43.49142 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c6a7338-e407-3e13-b783-6c6453d64591 | -5.87204 | -45.61345 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7485e9e4-224c-3bb0-9d65-921510ac04f9 | -5.3963 | -43.43187 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bae4ca9-b879-3746-87bb-f4e6ff691c54 | -8.51822 | -45.68499 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be1370c4-5c5b-3ddc-b646-b43354706e4d | -5.65372 | -43.9069 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b53b385b-5527-31e6-ae4e-ce3702af3df0 | -6.07875 | -44.81987 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60639844-b036-38b3-a954-88b6061c977b | -5.46918 | -43.43933 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11a98d13-98c8-3c09-a580-70ace8912833 | -7.85576 | -45.50751 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40a850bb-1821-341b-9f9c-bc8ee1e0a02a | -6.42224 | -51.70621 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea8e6620-96eb-36fe-ad2c-5e7dc6dbe4d4 | -5.56818 | -42.93406 | 2025-09-11 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| aef10db0-2df8-3093-814a-0845985c334d | -6.20594 | -43.52047 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c03f87d-dac3-3297-b0a7-2159dac48e19 | -6.68484 | -44.53876 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6806e4f5-75a5-3ddd-b1bd-e8101dc6ab00 | -8.1931 | -50.10888 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17cebf81-1a33-3b07-9402-8ae50566871c | -8.06473 | -50.17869 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 212f0015-3fe9-306c-86b7-fa99927d16b4 | -5.93668 | -45.69244 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf302c22-1117-39b7-bfbe-614c2182dff4 | -7.49282 | -48.25148 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23891785-537a-3089-bead-12363e18ae69 | -4.89943 | -49.92611 | 2025-09-11 04:21:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63c0ac74-05a2-3388-bf99-bab74dea180a | -4.93926 | -42.78295 | 2025-09-11 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fed90259-4478-38f0-b8b1-e31021f6a6d2 | -8.75981 | -47.11584 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad08b568-269d-3087-ba76-a595eeaf40b2 | -5.55028 | -43.04977 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90fdcf8f-719d-3b16-8a4e-69e12bc34f3d | -6.7486 | -45.93927 | 2025-09-11 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f46b44f9-1f3f-3a61-b155-2b59a105dc8a | -7.46553 | -45.28043 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76d9e291-54bd-3948-8584-a25e92c7b8fd | -5.56534 | -42.9299 | 2025-09-11 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 21c77be2-ad5b-3ef5-8862-1e9c23d07819 | -6.19005 | -45.65585 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ffeb6ef-5649-3b2e-9230-9125b6b364f1 | -5.9788 | -45.80513 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd33a102-7549-3c4b-9aaf-e82b137bb43e | -5.4036 | -45.922 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb1cbc0e-8eeb-3450-9256-82854ba220ed | -6.07265 | -44.81534 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e26e847-d40c-3cb2-9fb6-b05427f04733 | -7.85986 | -44.88625 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd03fe38-d3d9-384f-9f35-e1f6a26248d7 | -5.66313 | -43.89052 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21eda134-aa57-308b-a872-544aa9766af8 | -6.66453 | -44.1251 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10d0870c-2d5f-3b44-9eaa-34bde322962c | -9.03963 | -45.79094 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bc80f3df-12f3-3cac-b400-31544ce61757 | -4.92891 | -55.78979 | 2025-09-11 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dab7f696-973c-3f92-8b81-bc4e50a91f44 | -5.60511 | -48.11496 | 2025-09-11 04:21:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65352ddb-44ea-3510-8d3a-0af206a6c100 | -5.12423 | -44.66981 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6820dead-fb1a-37e0-b0b6-8bc7fad8fc72 | -7.49599 | -54.94913 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 184daf3d-93ea-3229-8d18-e3df3eec3a03 | -8.97681 | -45.52517 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 599816b0-ea5d-3954-ab4c-7f75f56afe64 | -7.35687 | -44.30299 | 2025-09-11 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af10d47b-103f-3835-ba57-5c19144dcb7f | -6.10068 | -45.93451 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a43f8f6e-c06b-3ec6-bb5e-f7e880fed7e8 | -6.49197 | -49.18163 | 2025-09-11 04:21:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5788f072-4422-3674-89be-165b410b7dc7 | -6.21796 | -43.49643 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42137c4a-2fa5-33d5-a1b1-d1cda491cdd3 | -5.57776 | -47.60084 | 2025-09-11 04:21:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 455b9bfc-1a88-330f-ade1-b6471f4c8811 | -6.82187 | -52.80068 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a580f089-a557-3c7b-b060-31a12aaae569 | -3.38706 | -47.49273 | 2025-09-11 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8349ded-c0a5-3de2-95e8-8e162bd41ca9 | -6.96165 | -44.81493 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23343230-5596-396f-8dcc-67add46174a2 | -8.62624 | -47.16426 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee49b01b-8eae-31d5-97d4-f7504703ff54 | -8.03883 | -48.67226 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 285b5271-43f2-322f-ad99-eef5deaab61f | -7.64001 | -49.81269 | 2025-09-11 04:21:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8f911264-7308-3e7c-98ba-267af0d1f10e | -3.40458 | -43.00134 | 2025-09-11 04:21:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de0292ba-17c3-3b48-bac8-402d8543f3b4 | -7.86813 | -46.72921 | 2025-09-11 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b7cac9f-c33e-3a22-b1cc-e0043b477407 | -7.88513 | -46.04389 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a59af89f-687b-32cc-a124-da06369a3855 | -6.31978 | -42.21779 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41964a96-27d2-38b8-8c51-1539bb7cec31 | -3.31902 | -48.70714 | 2025-09-11 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdfbb70e-b5fb-3c7a-8b7a-1269a1e94d65 | -5.8437 | -47.36756 | 2025-09-11 04:21:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b473ac83-6161-3f99-815d-22ad08e57d9c | -6.56681 | -44.21008 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3a56fe28-dc50-3318-94fb-486cc778e156 | -5.97907 | -44.72269 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6a1e69c-159c-3fcd-95f4-4c902ee01627 | -8.97169 | -46.06573 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2e40cdf-6b6b-3718-9f07-a639e26f63b2 | -9.09858 | -45.69961 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7eb67dc-50ff-3f65-94b1-f719636ee20a | -8.42283 | -49.08334 | 2025-09-11 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1954d85a-4388-3573-b2f9-c498299c4a82 | -6.30986 | -42.21222 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eb4f861e-0d28-3632-8189-088e3cb45c17 | -6.20538 | -43.52402 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bc35f76-e7d1-3d1e-83b2-62b2616b589f | -6.67993 | -44.56999 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2c45b66-3be7-3898-86fd-b89e58a53d36 | -7.66257 | -50.27127 | 2025-09-11 04:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66ca4255-5bae-3b8f-bce9-a276d89a4915 | -8.07231 | -42.94987 | 2025-09-11 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 529480bf-ad4d-3093-a37b-b891a667cbd6 | -4.93066 | -55.78009 | 2025-09-11 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87ea7474-805e-33a3-b16a-f421c1fb0367 | -7.89539 | -46.28075 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6774a5d8-016a-3e61-a8cf-5346e4fd5ef7 | -5.44996 | -43.99963 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec7ad95d-3908-3153-b35b-1188b81d9a15 | -5.08528 | -44.25182 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README46.md)
