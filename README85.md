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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3c62cad-7b48-39c4-8ad2-c1dc7fddee5d | -8.55109 | -44.88891 | 2026-09-17 11:47:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| caa62483-a2da-36b2-8f10-bf9926fef58b | -10.15794 | -45.39742 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| be65084c-2059-3930-b67f-00d6255c588b | -11.4918 | -45.73611 | 2026-09-17 11:47:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| c116fe1b-8c82-31e8-b4f1-91e5606f4972 | -6.92895 | -41.6962 | 2026-09-17 11:47:00 | TERRA_M-M | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| ea909ad4-4ff0-30be-9b78-e3a241e119fd | -10.9174 | -46.29837 | 2026-09-17 11:47:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 78803cdf-2e0b-3f46-9a2a-55ad0779eb4a | -7.36138 | -44.46892 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 44b20e91-8742-3712-9120-cf110024d69b | -7.08145 | -41.83691 | 2026-09-17 11:47:00 | TERRA_M-M | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 802ce06a-76cc-3e9a-a324-fa3d216f337a | -10.85995 | -48.11563 | 2026-09-17 11:47:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0d565d94-8bff-3dd9-bb2a-5241874d85a9 | -9.12045 | -45.72599 | 2026-09-17 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 43db91ae-2124-329e-9378-b7591d1e3ab7 | -7.00988 | -43.64381 | 2026-09-17 11:47:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 644.3 |
| 9e6cfe9a-2976-3476-950d-657a065d27ec | -12.49346 | -50.70952 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 36.6 |
| fba2071c-3673-3246-ab97-03de1ff65b56 | -7.99064 | -44.19248 | 2026-09-17 11:47:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4220417d-cf5d-30d3-a8e1-4faf4bd0898b | -5.08423 | -48.50718 | 2026-09-17 11:47:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0e3f5f96-0c7d-378d-8e9c-54f30711ca1e | -9.94885 | -45.43612 | 2026-09-17 11:47:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e16c430c-1d72-354e-bbbe-e149ea525c27 | -12.30969 | -47.96138 | 2026-09-17 11:47:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| de4a98c1-7286-3b90-ba66-f0ae38678108 | -7.00818 | -43.65691 | 2026-09-17 11:47:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 413.4 |
| d38d6b8c-767a-3137-a4d2-cf46efb77247 | -12.70862 | -48.27227 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 78bf65cd-f466-360f-bd2e-55408ce0da25 | -10.12422 | -45.57363 | 2026-09-17 11:47:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6409f40b-67f3-3b37-8064-3c5d53999842 | -8.56592 | -44.54697 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| b20c67bd-2a54-39de-a229-56e803ee7b39 | -11.56802 | -46.86238 | 2026-09-17 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 57e95427-a529-3cc1-8103-44534b95ae08 | -12.43198 | -48.47876 | 2026-09-17 11:47:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f8750373-d8d1-3043-a571-f0a314de073d | -9.87486 | -48.36829 | 2026-09-17 11:47:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| be20cfaf-ac9f-38bf-88a6-6dcdff45712b | -10.86929 | -50.84165 | 2026-09-17 11:47:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b7523d21-e48b-3612-97af-72a8e265e09e | -8.48205 | -44.56579 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| d9bd5db7-15c8-3af9-94ea-c40c2ab79809 | -10.14662 | -45.40737 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3894e9b4-a6dd-3cac-9f2b-6e1d5f35aa1d | -7.04014 | -42.06544 | 2026-09-17 11:47:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 4ec3ef83-eae4-363e-a93b-a6dad717b052 | -12.41079 | -50.77085 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3aa8751a-a186-33b5-8c49-f392acd05997 | -12.42776 | -50.78352 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 308bb941-80bd-341c-812e-6bc13e5f5b86 | -7.3754 | -38.96774 | 2026-09-17 11:47:00 | TERRA_M-M | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 7f6070fb-1dd7-337d-94d5-36c9eb117b9d | -11.33241 | -46.77176 | 2026-09-17 11:47:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6e4c33dc-91a5-37de-a424-fecc675f96b2 | -8.85938 | -45.86632 | 2026-09-17 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 6e11fe38-0d2d-3717-8a84-c6c917c67931 | -8.51893 | -44.52182 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 7fae9ac6-0be3-32b6-b6af-fc9df73df646 | -10.82569 | -46.15364 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 254bab6c-0fca-311c-b2bd-97d22be83a31 | -8.87819 | -45.86866 | 2026-09-17 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f54bb492-b32e-317a-89d6-b7a817a63d60 | -10.82379 | -50.82433 | 2026-09-17 11:47:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 85340011-b220-3023-a98e-38dea9724dd3 | -11.54571 | -46.88895 | 2026-09-17 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 09ba36be-5c28-3a55-bf79-5ebfde6352a9 | -10.50565 | -46.29355 | 2026-09-17 11:47:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9a0a561b-bded-3250-8cd4-666a6152cfeb | -7.01692 | -44.67216 | 2026-09-17 11:47:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 8be86e00-ec28-3304-80f4-b7d5028bc35d | -9.59126 | -46.6419 | 2026-09-17 11:47:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| e83a720c-ba86-3e68-b61b-4551b776ff95 | -9.82951 | -48.35546 | 2026-09-17 11:47:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 220.0 |
| c23251d8-f9ee-3f02-b325-c58d84a1fda0 | -11.53108 | -46.8707 | 2026-09-17 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ab591cc1-82f9-31f6-a179-2b4d020012ec | -9.83832 | -48.3567 | 2026-09-17 11:47:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| dd9578e1-8ac0-352a-ab3f-ed6904c0c479 | -10.40376 | -44.9356 | 2026-09-17 11:47:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 775ede59-bbba-3ed2-8d6e-ab13fd66b8a7 | -6.97202 | -40.41126 | 2026-09-17 11:47:00 | TERRA_M-M | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 33.8 |
| 227722fa-00b0-37b4-91c8-36afdfd57db1 | -12.43955 | -48.48903 | 2026-09-17 11:47:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 4818937d-2845-36a6-b4ed-f4a0e2fa5b33 | -12.50962 | -50.85313 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 348f51e6-c7c0-377a-acb0-1d9192d8cd4b | -11.56407 | -46.89156 | 2026-09-17 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 65e9c822-3453-39b4-bb91-518d71fa9987 | -11.33156 | -47.24639 | 2026-09-17 11:47:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e7903b02-bfec-338e-9676-347f72ecef30 | -7.07373 | -47.50414 | 2026-09-17 11:47:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 1f9b9918-8b38-3dfd-ab0b-880a586af2c9 | -6.91978 | -47.41622 | 2026-09-17 11:47:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 38623141-2a1c-3059-8b42-5f456e012006 | -9.18138 | -46.54477 | 2026-09-17 11:47:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| c780a449-9588-3210-b872-35fe3bedf19b | -11.60072 | -50.63227 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f87da879-2183-3b09-90d1-5af93249597f | -6.92663 | -41.71432 | 2026-09-17 11:47:00 | TERRA_M-M | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| d26b3b51-c2eb-30c2-969f-e821d9b8ed4d | -11.89066 | -43.82341 | 2026-09-17 11:47:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| ccc5c214-7b2e-362e-9d77-cde176b251e4 | -12.43071 | -48.48778 | 2026-09-17 11:47:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b0b0fd9d-b828-3217-b92c-3552643a3333 | -12.52035 | -50.84462 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 51786967-2e5d-34a1-b4d9-52c0be5730e0 | -7.39596 | -44.51534 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 849c3f36-e2fd-3366-a193-8aca7a370fc1 | -10.82224 | -50.83456 | 2026-09-17 11:47:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 908e96b5-c6dc-35c9-bd5b-9669c57568b0 | -11.54701 | -46.87934 | 2026-09-17 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 94b1f6a5-bf59-3926-93e4-469c9b14e041 | -7.5754 | -42.64285 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 44.6 |
| f80ecda8-6ec1-332b-9672-ce8108075f03 | -10.82295 | -46.17423 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 3d8e53a9-5030-3ee5-b241-efe63da7157b | -7.74861 | -47.29771 | 2026-09-17 11:47:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1ad956ca-14f3-3df3-994b-1418f1462f8e | -9.58217 | -46.5726 | 2026-09-17 11:47:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 211c2fee-6ff9-3389-bdfb-9bfe4076b00c | -7.01844 | -44.66101 | 2026-09-17 11:47:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 218.5 |
| a9d54c2d-d9ad-3a37-af3a-a2ac6e49ed1a | -12.51037 | -50.72211 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 222.7 |
| 3d3e12e5-091b-31b0-97ff-7cf85445c6bc | -6.9931 | -43.64841 | 2026-09-17 11:47:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 06bc06ed-5871-31a8-bc35-4a6f1e58fc38 | -18.70564 | -47.16639 | 2026-09-17 11:49:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 168a1697-c62b-330f-a406-abed2e3ea51e | -19.23442 | -46.67877 | 2026-09-17 11:49:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7faa4e71-00ab-31f9-aa8e-237a3bee175e | -15.47741 | -47.34922 | 2026-09-17 11:49:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9fdb183a-ebbd-3c77-bb27-a0f0d3fdcb1f | -19.26923 | -49.05132 | 2026-09-17 11:49:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 321acb73-b5aa-3bbd-aa8e-0a319d2ddab8 | -13.75032 | -48.79248 | 2026-09-17 11:49:00 | TERRA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d38befca-0621-3d79-b014-554074ac1406 | -17.05282 | -48.56528 | 2026-09-17 11:49:00 | TERRA_M-M | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 658960a6-87a4-35f2-9cb2-972905704627 | -13.74779 | -48.81047 | 2026-09-17 11:49:00 | TERRA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ed1ff594-b87c-35eb-8cfc-439a3b87e7b3 | -12.66616 | -50.78856 | 2026-09-17 11:49:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b573c8a5-2fb2-34be-92ba-e6e72e9f9a9d | -14.18704 | -45.16135 | 2026-09-17 11:49:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| dc45f6c1-5b43-38f2-a1d0-be6e9a64fd1a | -13.74906 | -48.80147 | 2026-09-17 11:49:00 | TERRA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d1c42afa-92d6-3536-b98d-9ea25c28e5b1 | -17.74951 | -47.69091 | 2026-09-17 11:49:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c2e2680f-5c39-300f-ab7a-d74cb29f7084 | -14.15214 | -45.13684 | 2026-09-17 11:49:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8d37b01f-6006-35e5-980e-0385057d3bbb | -15.63452 | -45.97095 | 2026-09-17 11:49:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c5064b24-e6c1-3fd8-b3a7-78502dc5e803 | -19.26792 | -49.06105 | 2026-09-17 11:49:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a72c8d48-0587-3601-bcf3-9b762f5aa322 | -12.78536 | -51.28301 | 2026-09-17 11:49:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e1bb59d6-3466-384e-ae81-a4cd38185e96 | -15.63953 | -52.72642 | 2026-09-17 11:49:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 41c949ec-2ec8-3320-9487-f16f11ae9905 | -17.308 | -47.48042 | 2026-09-17 11:49:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b000574a-96ab-3d5d-83c1-9e9c735047e3 | -17.00082 | -45.45941 | 2026-09-17 11:49:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 72072ac0-e1b0-311b-bfab-e9599feb2f59 | -16.99914 | -45.47341 | 2026-09-17 11:49:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 532589dd-c0e4-39cd-b9a6-7a7a158cea12 | -17.39567 | -49.22338 | 2026-09-17 11:49:00 | TERRA_M-M | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8696a9d5-3596-3052-9526-fee6ea8330db | -12.78693 | -51.27269 | 2026-09-17 11:49:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 16a6161c-aaa8-3484-9d79-b9d537cd9972 | -12.67717 | -50.84065 | 2026-09-17 11:49:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 33.1 |
| fa5a2fee-a768-3d38-8f4e-60d9ab7347bb | -13.60985 | -46.94209 | 2026-09-17 11:49:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8e1805b9-d63a-314b-bcc2-05faf677f86a | -18.70708 | -47.15484 | 2026-09-17 11:49:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6cc982f9-0f95-3feb-970e-1a49a8b9e365 | -18.88775 | -46.8487 | 2026-09-17 11:49:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| fa16566a-abac-3f88-9dda-42a4f30521be | -12.95526 | -48.61218 | 2026-09-17 11:49:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e20028f8-def2-3d30-b33e-e81df4a0f105 | -14.44044 | -44.85965 | 2026-09-17 11:49:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 343b6b06-d632-3a67-82f6-5ff9d53b62f6 | -13.27575 | -46.90263 | 2026-09-17 11:49:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 76928b20-768c-3514-adf6-8eef1c80d7b4 | -18.8893 | -46.83643 | 2026-09-17 11:49:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 871bad34-6587-3be7-b012-d3bd75a0e760 | -14.18869 | -45.14799 | 2026-09-17 11:49:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 9dd18a4f-4333-3210-a856-25ed4f278bbb | -12.67568 | -50.85054 | 2026-09-17 11:49:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f39604c2-581e-3dbe-a5dd-47bce269061c | -7.0804 | -47.5031 | 2026-09-17 11:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 4d14f88a-712f-390c-85f3-99d1b06f2b67 | -9.8694 | -48.3814 | 2026-09-17 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 24e9be0f-8c0e-3a85-8432-e0baa1a4e50a | -10.8118 | -46.1594 | 2026-09-17 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |


[Clique aqui para ver as próximas entradas](README86.md)
