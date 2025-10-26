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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a2c703e-dc53-33d6-bd7e-a7ba4fc85bb9 | -13.84796 | -44.35977 | 2025-10-26 03:42:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 103b4357-3306-339f-b07f-00b6bb02101e | -13.00655 | -43.85296 | 2025-10-26 03:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1fca5720-2ca8-339d-8fec-b2ec86c9c8a1 | -12.30534 | -47.45717 | 2025-10-26 03:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 618d1454-9f28-3c9f-9fc1-0eaba89f1062 | -13.40464 | -43.02473 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4c014e29-9f11-3ea6-a6cc-511cdcb50766 | -14.96105 | -42.28123 | 2025-10-26 03:42:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9b4c207f-813c-3063-982a-3d4f2925f680 | -14.50987 | -43.00144 | 2025-10-26 03:42:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| ff168999-1953-3571-b49b-5e4e8acd26b5 | -13.54791 | -44.00974 | 2025-10-26 03:42:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bfc3b574-7210-3e73-a9d8-7d48c7c99adb | -12.30401 | -47.46367 | 2025-10-26 03:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d041cee5-1e05-3aec-a99c-87a5a78d5a40 | -15.21975 | -47.93877 | 2025-10-26 03:42:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2a2f6cf-0777-3319-8b4c-46881da535db | -17.43216 | -46.88252 | 2025-10-26 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ce6010b-797a-3f95-98d6-bdd6b7fadab5 | -13.5414 | -42.99994 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 4286fd1c-045c-3c2f-b0de-e4a2b93404fc | -14.5142 | -43.90654 | 2025-10-26 03:42:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e05f8c3-05d1-375e-9392-7e8282a51644 | -18.47674 | -44.43504 | 2025-10-26 03:42:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a1aaf0b-c869-39f5-a387-11cbeb1c4b26 | -15.04527 | -46.2112 | 2025-10-26 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f60385c-bc32-38a6-ac39-1496b6bdad01 | -14.50589 | -43.00201 | 2025-10-26 03:42:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1260efcd-5005-39bd-8b06-6ae3bd63f754 | -13.0076 | -44.01849 | 2025-10-26 03:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b9a9718-fd10-31e8-ba6d-f2d49f82a1b3 | -13.00783 | -44.01376 | 2025-10-26 03:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c41263fe-22a3-31d3-b642-5e9f25cd3c4b | -17.32542 | -43.65541 | 2025-10-26 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f476c09b-8b96-3604-bf90-98d372ca76d1 | -15.21459 | -47.93221 | 2025-10-26 03:42:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d97306e1-e062-3321-ae36-0f056256ea7a | -17.37975 | -45.51966 | 2025-10-26 03:42:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cd8094b-f087-32db-b9b1-5671ce7ca56f | -13.53456 | -43.0097 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 80356aa1-45cd-3185-88f0-d53666bda7fa | -15.269 | -43.17987 | 2025-10-26 03:42:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 1e1d6c55-5a82-3b01-88ec-2bc7f9bda8b0 | -13.40254 | -43.55582 | 2025-10-26 03:42:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 477fa938-f409-3a1d-9e20-4d4ad0cbe678 | -12.176 | -47.01612 | 2025-10-26 03:42:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e6c9b498-bfa7-3a18-9686-23957b8ba13c | -12.56702 | -43.97721 | 2025-10-26 03:42:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c133fba-12d9-35b1-a84b-b7d661724ae3 | -17.32639 | -43.65055 | 2025-10-26 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b735fb73-31d3-323e-85e9-de4f32d9ef6f | -14.16299 | -44.68521 | 2025-10-26 03:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff79480b-940d-3a5e-9ee6-6ce0db17e69e | -14.54271 | -48.04627 | 2025-10-26 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 473bd45c-aef1-32c2-b24a-5f0f915e4a7a | -13.39985 | -43.02382 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 68a2eb15-1ffd-3209-a033-e298076cabe7 | -15.21927 | -47.93268 | 2025-10-26 03:42:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 427ff03f-86da-3b59-867d-c50b8b7014c0 | -16.2191 | -48.65571 | 2025-10-26 03:42:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54cab27a-d464-35c5-bf0c-94e3e08ad899 | -12.99893 | -43.80996 | 2025-10-26 03:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44a8304d-d56a-346d-b69d-25544f16e15a | -18.48153 | -44.43597 | 2025-10-26 03:42:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4928ea4d-a7eb-3069-a650-830c66b4f892 | -14.76988 | -44.97781 | 2025-10-26 03:42:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2047d1f-6ff2-3dc9-8052-95d0c6170136 | -15.60811 | -46.79081 | 2025-10-26 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b83100b8-ccc5-3318-be8c-8d6d3ca02942 | -12.30386 | -47.46013 | 2025-10-26 03:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 757a78b2-4d76-3adc-a23c-d9709cac933f | -15.26802 | -43.18493 | 2025-10-26 03:42:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 15.8 |
| b1a06bba-9b2c-3a71-8bd5-6cbeb779e9e5 | -17.37526 | -45.51498 | 2025-10-26 03:42:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa95ea57-85a3-342a-90bc-b4051cd9fd70 | -14.93258 | -41.66149 | 2025-10-26 03:42:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 91970caa-9029-3df7-b1cf-c67f94dd9798 | -13.53664 | -42.99894 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 71b9dac0-ed7a-3e78-961f-2133018336b1 | -15.27368 | -43.18081 | 2025-10-26 03:42:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a8c4f5f4-cbe6-3e53-b65a-b7c5037d72ac | -17.85118 | -44.111 | 2025-10-26 03:42:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fa8617a-8b79-37d4-8cfc-ef27b5b67eea | -16.2256 | -48.65694 | 2025-10-26 03:42:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d155cec-969a-31cc-bd2e-b1a65ba1448a | -14.58158 | -44.14267 | 2025-10-26 03:42:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 92ac51e3-e8c8-3eec-bcd6-f89935bb6883 | -13.5356 | -43.00436 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 25.0 |
| cf7c48e1-6a98-330d-bca2-fd083fb4032a | -15.29671 | -42.93662 | 2025-10-26 03:42:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 20a08135-628a-38ce-b570-acefb02e307d | -17.42648 | -46.88128 | 2025-10-26 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd789c3a-66a3-3bcf-921e-8aa5af9e1447 | -17.38499 | -45.52073 | 2025-10-26 03:42:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e87e69f2-39e2-3ec4-9f05-616af433bbaa | -14.48047 | -45.26666 | 2025-10-26 03:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54ab1d6e-ce47-376a-8faa-1d107ab51949 | -15.33478 | -42.81301 | 2025-10-26 03:42:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef653909-fb47-3169-80ef-154649c814b5 | -14.96234 | -42.2836 | 2025-10-26 03:42:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6454a3ee-13b0-32ea-b7fc-f5d8b9ec097b | -12.30251 | -47.47104 | 2025-10-26 03:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a458bba-5b5d-3771-8427-4a250eed7ed4 | -14.15856 | -44.76431 | 2025-10-26 03:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 01c5c854-e1f2-3225-835b-07c43264f4b7 | -18.20116 | -42.16658 | 2025-10-26 03:42:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| de40b1b4-7b1d-3f48-8c52-345e1f2c0a61 | -13.53324 | -49.54286 | 2025-10-26 03:42:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e14757de-33e5-302a-a060-4e75d53045ef | -12.91114 | -43.7035 | 2025-10-26 03:42:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e084ecae-3402-39c9-8a48-0d4b22ab0bf8 | -15.47561 | -43.13192 | 2025-10-26 03:42:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5b123392-392f-3c77-b53c-73351b94055c | -15.29766 | -42.93174 | 2025-10-26 03:42:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42fcbe79-3924-37ea-aee1-daa12725c23c | -17.33008 | -43.6563 | 2025-10-26 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88d223a9-948e-3101-b741-1479dbfa8cc4 | -15.21294 | -47.93143 | 2025-10-26 03:42:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 86c50ce8-2fca-3bc1-887d-0a14d9cda451 | -13.54117 | -43.00381 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 35.7 |
| a8da62ce-9e85-3571-8ba6-2ae3872c516c | -14.50955 | -43.00822 | 2025-10-26 03:42:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 47147153-5cc0-3662-97d7-48993b024a65 | -13.53741 | -42.99736 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 77a404f6-2656-3c4a-99ff-15cdd84860d0 | -14.54433 | -48.03892 | 2025-10-26 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| daf5e190-95d0-366e-8d60-3b159b65a1b5 | -17.42566 | -46.88502 | 2025-10-26 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4f2430f-b546-3626-b408-24bd6761297c | -12.84993 | -48.6473 | 2025-10-26 03:42:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79284b51-ccc9-342a-abaf-02a1f9982c9d | -17.32173 | -43.64963 | 2025-10-26 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cc6a28fb-54ef-391a-a71f-37aa471a3ee6 | -13.40309 | -43.02558 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bc68edf2-8885-315e-87f9-427811478cce | -13.53541 | -43.00819 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 070df4b4-6257-3b9b-99bb-f55e74c6b0ed | -16.17569 | -46.46019 | 2025-10-26 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f4636b6-1467-3ab1-ae11-19c20139e643 | -12.30235 | -47.46729 | 2025-10-26 03:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e5f0ea7-1107-3394-874a-8170f5ec15bf | -17.31518 | -43.64664 | 2025-10-26 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4397e4b4-c884-3049-be73-087726e16e20 | -14.43971 | -49.96466 | 2025-10-26 03:42:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3ae53f1-5ab7-3055-b254-ca669d606bad | -22.77088 | -43.39054 | 2025-10-26 03:45:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 46ace44a-af38-3b7f-b559-42f80842c590 | -22.48101 | -44.10949 | 2025-10-26 03:45:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 573011e4-3705-32fd-8e92-4f56c56936be | -21.43271 | -49.59808 | 2025-10-26 03:45:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 2a6a755e-2ea8-349b-b1d8-e3f95f7c2e4f | -20.98204 | -44.31682 | 2025-10-26 03:45:00 | NPP-375D | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 211869a0-114e-3e31-b87e-d272c3034de2 | -19.92277 | -44.65445 | 2025-10-26 03:45:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fda36566-58f5-3f26-9f55-495a9fffc2ec | -21.75873 | -50.04655 | 2025-10-26 03:45:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| dba99fd1-6bfd-3d3b-a522-24b1d33d797c | -22.4177 | -43.41873 | 2025-10-26 03:45:00 | NPP-375D | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 55fd9637-bc40-3e3b-8a56-1d355e785bca | -19.34845 | -45.59793 | 2025-10-26 03:45:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7f1810a-9776-384f-8ecc-2816df2fc752 | -19.3998 | -45.86892 | 2025-10-26 03:45:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6980be5f-d2d5-3fb0-a7bb-bc4664380fdf | -21.41566 | -44.08653 | 2025-10-26 03:45:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| de3f6391-90b7-3eee-8091-3e530a594cb3 | -19.65721 | -44.62539 | 2025-10-26 03:45:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0af037e9-e4d5-36c4-9eda-a8a7026858f9 | -20.34013 | -41.74075 | 2025-10-26 03:45:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 19bc9124-8497-3460-9dfb-613c43ff7ec1 | -18.46398 | -47.17342 | 2025-10-26 03:45:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 77e509f2-5b31-3f49-af67-52506e86e985 | -21.76222 | -50.04916 | 2025-10-26 03:45:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 632b6f8a-ef8b-3ed8-9d40-4d7bbbd97360 | -20.45113 | -44.18391 | 2025-10-26 03:45:00 | NPP-375D | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a586d67a-fd9f-3327-b5ef-775b3e8aa93e | -21.42952 | -49.59235 | 2025-10-26 03:45:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 39d44a7b-a56b-347c-9ebe-c889c906b2d7 | -21.92895 | -46.51625 | 2025-10-26 03:45:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 67c36443-0851-3dfa-a241-18a81e0ce944 | -19.88582 | -44.3687 | 2025-10-26 03:45:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cd7b63d-f3b9-38d1-b9dd-04259fa3494f | -21.29803 | -47.14502 | 2025-10-26 03:45:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| af41a81e-afdf-3dcb-8b3d-75d9f94e5d40 | -20.58199 | -42.96737 | 2025-10-26 03:45:00 | NPP-375D | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c47433d5-a2fa-37b9-9cfe-2f98897dd011 | -19.40493 | -45.87011 | 2025-10-26 03:45:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e23782d7-1c3f-327b-84a8-b63e569560d8 | -22.41851 | -43.41452 | 2025-10-26 03:45:00 | NPP-375D | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 53c6870a-5539-3edf-8131-1f5e3d51e088 | -19.40423 | -45.87344 | 2025-10-26 03:45:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f91dc4c6-4f3f-3232-996c-906e7a6cde30 | -21.42786 | -49.59117 | 2025-10-26 03:45:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 20f6e84b-05b8-3afb-8418-a5408a9d82bf | -21.29888 | -47.14117 | 2025-10-26 03:45:00 | NPP-375D | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 837d5331-1d26-3406-ba77-062a09d3fddb | -21.7635 | -50.04377 | 2025-10-26 03:45:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 75552cbe-4f73-3803-a471-1c0ef0e9e68c | -20.58187 | -42.96936 | 2025-10-26 03:45:00 | NPP-375D | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README13.md)
