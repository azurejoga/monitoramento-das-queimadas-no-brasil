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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a750eff-a9c0-3d71-8c9c-b2b8375e0810 | -7.64942 | -43.89151 | 2025-10-07 04:36:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a04a39bd-1a7c-3042-a795-e8cc6f337d16 | -6.36622 | -41.61908 | 2025-10-07 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c03fbfa0-9adc-3da3-ad5e-75d587206baf | -5.49619 | -43.0801 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 4444af51-5c2c-318d-8451-86d05824ec76 | -6.33175 | -44.02605 | 2025-10-07 04:36:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dbe2af6-6759-39ef-a065-cb5e7582b61a | -5.22627 | -43.79634 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40a8340c-7520-3863-89c2-e556f4b41bd9 | -4.87109 | -50.89763 | 2025-10-07 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3dba9e10-6be1-3a71-bc3f-804b96c0b219 | -8.43788 | -48.69884 | 2025-10-07 04:36:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2548d51-5718-31e4-9de0-da28bd638d57 | -10.34418 | -48.14795 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c52183de-e059-3cab-9628-204c74386c45 | -8.17152 | -50.16299 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea26f77c-216a-3dc7-9ed9-e4a26898d3ce | -8.86893 | -50.88539 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f011225-9332-39bb-a17d-2b9a5362a725 | -8.4142 | -46.8023 | 2025-10-07 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69b968fd-b8a3-3376-ae47-8a1a9ae36211 | -8.88436 | -47.66466 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 098c617b-6392-35ef-914a-9c1ff1e3df6e | -10.38607 | -45.40929 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3106b396-011b-39e1-9b8a-4a02bbef2a50 | -8.19817 | -44.20697 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45eb819d-98e8-3658-b386-9b6c34a19054 | -8.84628 | -46.09939 | 2025-10-07 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69a31f7f-5092-388d-acc8-9aee8fbac54e | -8.17417 | -50.29863 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f608c08b-edbe-30cb-b2f8-a099c79498d7 | -3.94721 | -55.78667 | 2025-10-07 04:36:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 766ed98b-b6c3-3065-8ef1-f09c4e78f290 | -8.22129 | -49.14356 | 2025-10-07 04:36:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11e5c1ae-831c-3072-853e-5706ae52eefe | -7.06534 | -42.77498 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e36355a-b30a-3923-b63f-1fb948966dc6 | -8.56636 | -44.63845 | 2025-10-07 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60e817da-b1b0-3c53-b2f1-ba31a23cd121 | -8.22222 | -49.87246 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c143130-264a-36d4-b2ca-bdd7d76df962 | -7.69728 | -42.39535 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0fedd2c7-b09f-3eec-bf15-74d1c523ff6b | -8.27307 | -43.82658 | 2025-10-07 04:36:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c142dd45-ce54-38fc-9f06-1c8cf2340ea1 | -7.16458 | -48.25686 | 2025-10-07 04:36:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c3b47f5-6c81-3140-b58e-ae48ae16a082 | -5.61339 | -43.93676 | 2025-10-07 04:36:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 525f13a0-a3a1-3e99-9bef-7b4962f6fe8c | -9.9234 | -49.96073 | 2025-10-07 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b3d65a2d-19bb-3027-9477-0b54874de4e9 | -5.70958 | -44.83526 | 2025-10-07 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c78304ab-1940-367e-a607-ed788176d507 | -8.5906 | -44.33719 | 2025-10-07 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6f72197-f9a4-3813-857a-be924a4167ca | -6.38227 | -43.29494 | 2025-10-07 04:36:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae22048f-ade5-3c69-b1d8-7193b67f1716 | -10.23008 | -48.1842 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adb62a6d-9875-3e4a-b41f-be13d004ed87 | -6.72052 | -42.83666 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ca723506-b274-30fa-9472-0c4db4747108 | -5.84841 | -42.85437 | 2025-10-07 04:36:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 7d3a0896-044a-30b1-9367-c87c8b9120e1 | -8.8784 | -46.77402 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54b0f9dc-aec5-3004-8ec4-0aaf9209056c | -6.45829 | -42.79483 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 30804bd1-39ab-37f1-962a-2adb8fd341f8 | -6.12864 | -42.66984 | 2025-10-07 04:36:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a710d0d4-dd5c-3c58-8701-984a6e516a17 | -5.25737 | -46.4853 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a59709f1-7bda-35ed-a6d5-7ed00318c504 | -10.32138 | -46.93768 | 2025-10-07 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61ed56c4-9f3e-3f49-a218-10c78480d0dd | -7.69071 | -42.41036 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 37df7bad-a150-3e94-8cc0-9eca9f630e3d | -4.70867 | -46.46257 | 2025-10-07 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4370c8eb-3e15-377f-857c-1e802ab53553 | -6.64802 | -41.98456 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 535bf9cb-73be-30f0-972e-765b339169ad | -7.67245 | -50.20788 | 2025-10-07 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4e0199d-5160-325e-bb9e-542b0763915a | -7.04356 | -43.93364 | 2025-10-07 04:36:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d81cc4b9-6877-3e55-b694-8a4deb2e1318 | -8.552 | -50.08038 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8851f32-f43d-3077-8005-9e2bde1ce747 | -4.69201 | -45.83825 | 2025-10-07 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fb4f136f-7e0d-3a0a-b389-aabe2323bd20 | -6.13988 | -44.60706 | 2025-10-07 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76033a12-7b69-3066-9ddb-42d58fc419b5 | -10.02664 | -48.29674 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08056bae-fc4f-3841-8345-7319d46ea582 | -9.33339 | -54.51934 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c54bc7b-7a8e-35a9-b7bb-a731a35351a6 | -10.16126 | -45.42149 | 2025-10-07 04:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e352229-b28d-3cdd-8a83-356d322ab7fb | -8.18175 | -43.34065 | 2025-10-07 04:36:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bd0df724-b153-3729-bb93-546cc8848707 | -7.67309 | -42.58752 | 2025-10-07 04:36:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 56802217-6033-371c-8b65-962fef4a5348 | -7.58086 | -45.91935 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63bb19a7-aef8-36a1-8cad-14dc4889391a | -6.74958 | -49.03933 | 2025-10-07 04:36:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a1063c57-dad9-3597-a7f2-7d5b454551e6 | -6.67881 | -42.77882 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 546a7ea2-b9a0-3cb5-9053-03aedd68c434 | -6.164 | -42.59301 | 2025-10-07 04:36:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7439e623-2114-3532-aa2c-5b2088a05404 | -5.79633 | -50.20789 | 2025-10-07 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24308721-6041-3cf7-9b0f-0510954b71d0 | -3.87205 | -54.35121 | 2025-10-07 04:36:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d7c6e31-b87e-3fa4-b33b-568261f400fb | -5.41893 | -41.07607 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2b9dca9c-f33a-31fd-bc10-2cae6a01d6dc | -3.9528 | -55.78471 | 2025-10-07 04:36:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6234a463-480b-3447-ae9f-5afc93310f66 | -4.87012 | -50.90027 | 2025-10-07 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43e6635c-4d5d-3c65-b2e6-44b43baa52aa | -6.71892 | -42.84749 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d7314181-8e02-3ea2-bbc0-00441c27a375 | -6.65711 | -39.29803 | 2025-10-07 04:36:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c81d6b02-b99b-3aa0-ae38-c40663f9c0e5 | -7.52042 | -49.91143 | 2025-10-07 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ffcb50e-a181-3620-b5e9-104302a0e9d8 | -5.25533 | -46.56499 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13df10a7-2626-3d49-8def-f683a1fc2d15 | -8.38484 | -41.85193 | 2025-10-07 04:36:00 | NPP-375D | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f0424ba0-a423-3e8a-bfe6-d6df55c11fdf | -7.69415 | -42.40948 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3a74fe26-3608-321c-bfb6-183b302326ec | -8.85445 | -46.09275 | 2025-10-07 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2359bb5-5c1c-3974-93ab-19c52c3e2234 | -5.25026 | -46.5533 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 687ad489-b5bf-3ce2-9457-c7edcca58fea | -8.54355 | -46.2481 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76b260a0-63a2-3db8-b98a-513243f20183 | -6.09445 | -43.12883 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a0a9359c-f413-302c-afa5-7bcb0c3d75d4 | -10.39477 | -45.37505 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a39a93c-0de1-35cb-aa32-ca3f6ecd4652 | -7.01528 | -42.29302 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c1206970-ed1b-3a44-8c3b-fda5f84fdd98 | -8.84687 | -46.09555 | 2025-10-07 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a1d164c-d8d3-3380-8167-65fe004faab6 | -8.44506 | -47.21003 | 2025-10-07 04:36:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f34465a0-375a-3c01-9891-ed28439f069c | -6.10436 | -43.08884 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58fb0f48-dc52-37e9-95dd-8195a75c7480 | -8.87369 | -46.7852 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9865bc4d-9bc1-3a29-855f-c0d8af3379ef | -9.67832 | -45.67039 | 2025-10-07 04:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fffbb1fa-a2e4-3329-89d7-2cbea8cfb5c8 | -7.26977 | -49.40814 | 2025-10-07 04:36:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81ee1faf-b087-391c-a4ed-58b8535e933e | -7.72024 | -42.40954 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 681f9a56-38bb-371f-9277-ee85ce6f6885 | -8.19994 | -44.22167 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3b1e339c-3db0-3c0f-93b2-5e8174d977d6 | -5.64792 | -43.60811 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8dc8bf5-dbdb-357d-a263-6ba1352c3875 | -6.70406 | -42.86362 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c9049665-ca70-3acf-ae4d-de4b7f4a7e0b | -5.03556 | -44.45377 | 2025-10-07 04:36:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 234964e5-aba7-3c6c-9f2a-e9455b2cda88 | -7.67356 | -42.58641 | 2025-10-07 04:36:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| de20aca1-dde4-3314-b04b-58111fd6dd50 | -8.62088 | -44.93579 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8695f656-9858-3e05-93e4-a5134702bcd1 | -8.61807 | -54.96514 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b3f9ca8-bd68-3e8b-a786-378bba7c6697 | -6.25256 | -43.27816 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f714e4a7-ebbe-377d-b3fd-7a3d19932a31 | -7.83816 | -50.23811 | 2025-10-07 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d936011-667a-367d-957c-b56cb12f9001 | -8.48889 | -46.27176 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0321daf3-77dc-30b0-9bfd-ca29c94507bb | -8.92603 | -46.59864 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cc5669e-2a76-310f-bed6-39f20b27b797 | -8.47033 | -43.72674 | 2025-10-07 04:36:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a4cb4a99-d26f-312b-8d6c-3f2259a8da2a | -5.46017 | -42.79189 | 2025-10-07 04:36:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a83f8f1f-5ccc-338a-b77c-b3351b844baa | -9.037 | -51.48313 | 2025-10-07 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4546f7e-bb1e-3726-b22b-e36f6acb542c | -6.65191 | -39.29726 | 2025-10-07 04:36:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 45a336e9-3b16-3b41-9a05-ed5388a67650 | -5.6127 | -43.94124 | 2025-10-07 04:36:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be39a46d-af8a-3a05-b1cb-96b756ff8dfb | -6.16014 | -44.09462 | 2025-10-07 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49fe979f-2744-38eb-9e61-198cd2d73ee7 | -8.61878 | -54.97193 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af1425a8-d1cb-3661-8fe5-aa85d2b75d41 | -7.69013 | -42.41431 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 28e65b98-6bd1-3540-b91f-bde45f900405 | -7.27035 | -49.40453 | 2025-10-07 04:36:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 317e6888-e2db-3497-af7d-18d09f4aa7ce | -10.33278 | -51.22713 | 2025-10-07 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d1a2e62-c908-3245-bdec-192e9f555951 | -14.86831 | -51.45247 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README60.md)
