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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38f0c9ca-8e10-348a-875a-33a7f837e435 | -11.87715 | -47.5333 | 2025-09-12 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aeae337c-a9a1-3fef-8b4f-733cf466f3dd | -9.99477 | -51.73186 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5678b981-9151-38ca-90ce-2dc86a8863c0 | -11.08573 | -48.40825 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76df5b43-8e71-38d5-8c3c-dc07a55ee188 | -6.82783 | -45.65208 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d02b3a8c-38bd-38e7-bae0-f70e9689d1dc | -11.1804 | -48.43112 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c4f8234-4366-3e18-8e39-6ed1182f86fb | -9.71151 | -48.30507 | 2025-09-12 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c47b01f7-3f79-39ec-a298-1978bc4cd070 | -12.50046 | -44.6883 | 2025-09-12 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10631a05-26de-31a3-a774-c8dee55a1c73 | -9.71949 | -46.89514 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d1b5abb-b568-38c9-9815-9e3d09284271 | -10.71101 | -48.62363 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64d21af6-1836-3f3d-8c20-d45f29ebc905 | -6.10794 | -45.934 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31f553ff-7b4a-331b-ad5f-ba349abf26c5 | -5.82785 | -45.27377 | 2025-09-12 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e6840cb-a07e-3041-b83f-4bc03c7a2291 | -8.37533 | -47.59625 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a81c7087-f24f-32be-ad78-8d187ac2d200 | -10.1263 | -47.90483 | 2025-09-12 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 990bae2d-1320-39ab-a2a5-03e2df96acc3 | -10.44285 | -50.59993 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f312d82-ef0e-305d-bf69-3a451262900d | -10.66413 | -48.6569 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7deed1b-dcf5-3d6d-a7eb-4b2517878450 | -10.70706 | -48.6267 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c2073dd2-8144-3091-8173-a71d2f46cd8a | -6.18621 | -42.74862 | 2025-09-12 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05105209-893d-3cbd-b047-68e68fe05afb | -10.55502 | -51.53752 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc49f5d4-8233-349b-9d0a-9bada4ae9a84 | -9.8574 | -43.12867 | 2025-09-12 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3dffd09f-06c9-31c2-bd7b-9d53605486c8 | -8.08363 | -52.35716 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1342c13a-8607-352e-bfe5-e26e866614e1 | -5.82833 | -39.65135 | 2025-09-12 04:25:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 154440cf-aff5-3325-ba41-6dc4c679e840 | -6.18281 | -41.0812 | 2025-09-12 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9ddfd32b-bec1-3768-b16e-2bf855614c49 | -11.20622 | -48.39853 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7af137b7-afce-33c1-bab6-c064e26b89f2 | -10.40955 | -50.00483 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 647ae6bb-1132-3bd0-9f4c-6a21aaa826e2 | -8.94611 | -46.0656 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94a9ae79-2794-3419-93f8-2914e474cdcb | -7.51834 | -44.67954 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4e08435-a40f-346b-a786-f90231854bfd | -10.11795 | -47.91432 | 2025-09-12 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5feeb96-4327-3dfe-994d-77094eb8d8f9 | -11.68322 | -46.60139 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b514e1e-c85b-3258-962e-4fc7a1c77f31 | -9.25575 | -57.06964 | 2025-09-12 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3745980-50ee-3df6-9901-5a70022c3ae7 | -6.7489 | -45.93929 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d97a2211-11dc-3458-9f54-3c04b6e3e0d3 | -8.88888 | -49.93206 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cda5f384-81c8-3be5-b8fe-cf4379bc0391 | -6.71284 | -42.04964 | 2025-09-12 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d64118e4-52a4-32e1-a6f6-f68296ab7ede | -10.4135 | -50.59589 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6303b47-0f98-3d3d-a48d-fa6cb603f675 | -8.47071 | -47.27324 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7711b91a-e9cb-33cf-b508-cb1b93497ef8 | -9.66914 | -47.55647 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 511a9632-35f9-3289-a44c-f7643c98986a | -5.73716 | -45.59171 | 2025-09-12 04:25:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecafe905-4c0c-394e-9903-b9b344f8bc8f | -9.6758 | -47.536 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f0857df-2f30-3d0b-be92-d82aea1990f9 | -11.676 | -46.60387 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 800008a4-26b0-3069-989c-611891e8a849 | -8.36923 | -47.59164 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06cb9f36-f9e2-38b4-ab7f-8f6600d6397c | -11.44145 | -48.5587 | 2025-09-12 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3547c348-47dd-3c5b-bf95-4ed0fb54b5c4 | -6.83174 | -52.80135 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16eeb940-d09d-3e66-a208-c17f9a9f9216 | -5.64189 | -51.86716 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3424c89-acb5-3892-8d54-b760d6264d7f | -9.78529 | -47.3808 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6027a0f1-7cb2-36a0-a449-7c3e07f15e97 | -9.07316 | -50.49455 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42bba983-4619-3aab-9ecc-8d24180cb13f | -6.91268 | -45.54292 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 039d86e7-cfb2-32e7-a0a7-7bb58e485b3d | -6.28074 | -42.40246 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 66393b23-47fb-311b-bcba-c60532717adb | -12.02423 | -43.78767 | 2025-09-12 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d84d1476-10fd-3827-bdfc-fc7769433002 | -6.566 | -43.15127 | 2025-09-12 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 763d66ff-5135-3a2a-acf3-b50473519bb5 | -9.07241 | -50.49901 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c44683b-cf4b-33e6-8d35-bd21466ae932 | -6.63552 | -49.78084 | 2025-09-12 04:25:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac127357-54d6-330f-9a56-d0201ce2c970 | -6.19868 | -42.66639 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2344a1e9-97be-3d31-8d86-c16221bacc15 | -5.85421 | -47.36055 | 2025-09-12 04:25:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04bfe049-30e7-3612-b381-2d8cf454f66b | -7.35225 | -44.30159 | 2025-09-12 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05f33336-890c-3762-b9a7-e7583e9e8753 | -9.96781 | -51.70084 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a742ddf5-c288-3ea3-bede-1f212c6a97c6 | -11.44638 | -49.3014 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abbcddb8-8e14-3877-92eb-76b774915222 | -8.46463 | -47.26869 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 489a9a3e-fd4b-3ed0-81c0-6374c840cffa | -10.55583 | -51.53273 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 754eacd1-5971-32b0-8411-c900383c2fba | -7.79184 | -50.77293 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b7a7d8d-5aa7-312d-b5d6-cb5f603a4c4e | -11.70592 | -46.49891 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d994e59b-43eb-30da-897e-45a1b329c212 | -8.1803 | -46.10045 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b705d486-901f-3bf7-b134-a77cf7fdc529 | -9.79656 | -47.77863 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e96542dc-05ae-3edb-bb0c-6537a8ad5c43 | -11.6721 | -46.58497 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a73de14b-5ebc-38c1-8750-a485e256ad72 | -10.21834 | -46.24387 | 2025-09-12 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b126ca13-3874-3c37-8191-229d87f839e0 | -7.46098 | -44.41461 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9a99a71-8d26-3f10-a74b-e3d2b8c8404f | -10.88655 | -45.58824 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4140e28c-543b-367e-bb05-20eb07aa089d | -10.55546 | -51.48845 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bb1f4a28-b778-346a-88c7-77c3ae5a5d1a | -9.51464 | -54.63084 | 2025-09-12 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 82f383f4-c9e4-34ae-9f71-f265ba194290 | -11.14341 | -45.23521 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c4d83bc-1cf0-32a4-bc5d-c82a2931e011 | -6.44409 | -44.03989 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a767566-4c01-3538-8893-36e7a0d97ea4 | -9.0401 | -47.06828 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c88b083f-2694-318c-b301-3db4aaa8b860 | -11.68102 | -46.61558 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6cfb842-1487-30af-b44c-622813f945b6 | -10.87355 | -45.55949 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 294d9aaf-0da1-32f7-90ca-9477698db873 | -11.1251 | -45.12238 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e287a24a-bb89-394a-85b3-fdeed4355632 | -7.45117 | -45.00303 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 02191c96-6e66-3176-b299-b1663707e386 | -6.67591 | -44.57899 | 2025-09-12 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97630e81-9d8a-3eeb-bc56-dbf2b687a5f5 | -10.32492 | -48.80084 | 2025-09-12 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83bdc310-9766-34a0-bd7a-4eca2d2b9022 | -8.1764 | -46.08192 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95b17ee5-f2b2-3eae-8eda-00abec035d81 | -10.88596 | -45.59205 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 920a38d7-920b-34ea-9b97-af232098880f | -11.97793 | -46.64806 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3897da5f-cac9-33d1-a2e1-a15a73418ef2 | -11.70981 | -46.49586 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4e01576-74ee-3b69-b97c-71df7b5fcc09 | -8.06782 | -52.32386 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 344f0a00-a9c8-3f3b-a019-59d1640f593b | -8.13756 | -49.51567 | 2025-09-12 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69c5f30e-9fba-3ab5-b744-af31a004f1c6 | -7.32739 | -44.41804 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c50a043-909c-3584-b2b5-3d8fafd94235 | -6.29694 | -44.58569 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2a9c0fb-649f-37ff-9970-0b1be4174f17 | -11.69207 | -46.56626 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f53a5cc-e5f0-3966-931d-828abe22458b | -7.46041 | -44.41835 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ec0e3fe-390d-3e88-924c-85fa77835da4 | -6.19433 | -42.67017 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 60eb9639-bf75-3d11-b37c-4acf617cabf0 | -10.08965 | -48.17527 | 2025-09-12 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7980f5a-2ed5-32c4-a75f-e2d0f0175a01 | -8.95198 | -46.72226 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8dbbd68-1926-373e-a7c2-774b500fe499 | -11.67427 | -46.5488 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82fa28f9-9d90-38d4-82f4-09fcd1579e9e | -6.29789 | -44.23846 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0ac9504a-ab28-37da-9d90-7710af55c158 | -11.12222 | -45.11798 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6381ec0-6103-31e4-92f8-3c25b468970a | -9.68798 | -47.5236 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc723240-0c1b-3252-8782-f4f918c11913 | -7.88701 | -44.83293 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 050062e3-98a0-3d15-a8be-880eaf8a9717 | -11.23972 | -49.40697 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67d2e1fb-d6f1-3c96-bffb-c1272b7bad83 | -12.11954 | -44.87181 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d990f092-9b61-31be-89bd-8af0de5cf015 | -10.09069 | -50.39628 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 513c638a-602f-3be6-9336-9012c8c11801 | -11.56685 | -43.23632 | 2025-09-12 04:25:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1c1df44b-4a1a-3501-951f-758bb99a308f | -7.85564 | -45.39619 | 2025-09-12 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d0d43a4-e2fd-359a-9d1c-262b160a3c15 | -6.81259 | -52.80691 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README67.md)
