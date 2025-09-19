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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72980f22-0352-3cd0-9724-4aa0265aba87 | -21.35377 | -45.78788 | 2025-09-19 03:36:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c2f91c55-e1dc-3bf9-a714-f4da305d5537 | -20.52097 | -42.39311 | 2025-09-19 03:36:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c0adf10a-5257-3095-ad9f-fce4fbc343ef | -20.55697 | -43.98411 | 2025-09-19 03:36:00 | NPP-375D | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b6cf93a9-6bf1-38c2-8340-08caa9a7ffe6 | -20.51432 | -42.40315 | 2025-09-19 03:36:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 989eb1ce-d7a3-345e-a82b-47ea9dc56815 | -22.03667 | -45.59293 | 2025-09-19 03:36:00 | NPP-375D | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 63885a19-0ce3-3b61-8bb9-06237bc28716 | -17.22227 | -45.94494 | 2025-09-19 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6993b934-bc65-35f3-be15-a25bb0c25942 | -18.0473 | -45.52492 | 2025-09-19 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3667706-9a6c-34ff-ad4e-a88c5cffc371 | -17.22249 | -40.9267 | 2025-09-19 03:36:00 | NPP-375D | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4c519d0c-0112-36f6-8c98-8c7745802703 | -22.01975 | -42.21183 | 2025-09-19 03:36:00 | NPP-375D | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b60b6cd0-6de3-3c63-bf64-f8d8d7d1f059 | -19.59464 | -42.10625 | 2025-09-19 03:36:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| da854473-1325-3231-aa2d-d467fd3589a1 | -17.08574 | -43.33825 | 2025-09-19 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dbbb700a-22e6-3b6a-8228-49f048e6ffdb | -18.1199 | -44.66688 | 2025-09-19 03:36:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00196607-8d8b-3b06-a07d-4d35915f99fc | -17.08703 | -43.33181 | 2025-09-19 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10310ce5-e9ea-35e7-b878-605a718be1cf | -18.57639 | -43.46768 | 2025-09-19 03:36:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 04175b9d-77b2-3f90-b6fd-246d180ec619 | -20.78344 | -46.11545 | 2025-09-19 03:36:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79f94d06-9597-3645-91df-cc0cfd874192 | -20.5164 | -42.39259 | 2025-09-19 03:36:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5c190def-a988-3868-ad4c-e8dd8edb104a | -17.2213 | -45.94938 | 2025-09-19 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2d2492cf-d133-3839-94e3-de87545524c8 | -20.78987 | -47.23813 | 2025-09-19 03:36:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f438fffe-90f6-320b-94a2-13a0c54c6b5b | -17.45303 | -44.79716 | 2025-09-19 03:36:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28462681-30b1-3187-ab8a-61d2d6ee32ad | -18.0499 | -45.51266 | 2025-09-19 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43142ac7-df94-3b28-b684-ed6b8ecee6b4 | -20.78251 | -46.11962 | 2025-09-19 03:36:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b858b2ec-de6f-3927-90ba-ee736d99ae47 | -17.22686 | -40.92745 | 2025-09-19 03:36:00 | NPP-375D | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f93ef5f3-ae77-3677-9384-ed78c51fee42 | -17.23214 | -45.95697 | 2025-09-19 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6756d047-47ba-34b9-a225-8ca9ab20a747 | -16.51259 | -43.55245 | 2025-09-19 03:36:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bba00240-8322-3302-886c-6164e06641e9 | -18.1192 | -44.66848 | 2025-09-19 03:36:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d79e2dbd-ebb2-3779-942f-9bcf45c0da06 | -22.03825 | -45.58563 | 2025-09-19 03:36:00 | NPP-375D | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4011a1aa-d967-315a-9f64-b7335085c664 | -21.40561 | -44.2788 | 2025-09-19 03:36:00 | NPP-375D | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b20cf432-a3fe-39b4-9a5b-06fe5599a132 | -18.58291 | -43.46146 | 2025-09-19 03:36:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e60d6673-4c7e-3ace-b406-383dd5212c1d | -20.03734 | -44.04223 | 2025-09-19 03:36:00 | NPP-375D | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 52b9f5f5-9ba5-3713-8f98-a88e716dc379 | -17.17391 | -45.90155 | 2025-09-19 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0859c262-81c4-3a51-bae3-0a20895b7647 | -20.54293 | -44.02714 | 2025-09-19 03:36:00 | NPP-375D | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 965b9060-8434-3fef-8ef7-accc784da06d | -18.64305 | -43.89514 | 2025-09-19 03:36:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c36ace8-40e6-3870-8703-7cf50c53379c | -16.51299 | -43.54944 | 2025-09-19 03:36:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6bd25e5d-bdaf-3cfe-b61d-9e8a85278e4c | -21.29241 | -48.79898 | 2025-09-19 03:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 630a435a-c397-39c3-8c2b-80f156ae9424 | -20.03665 | -44.04554 | 2025-09-19 03:36:00 | NPP-375D | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5ff9d205-b904-38f0-8627-c9cbe2581cd8 | -18.11905 | -44.67083 | 2025-09-19 03:36:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| baec84e7-650c-382f-b7a8-8c926cebc786 | -17.23315 | -45.95235 | 2025-09-19 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8a62a50b-7a62-371a-a309-475a92553d3e | -22.04198 | -45.59416 | 2025-09-19 03:36:00 | NPP-375D | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1ed44901-0c36-37f9-9221-0ae21028cdae | -21.28933 | -48.80266 | 2025-09-19 03:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b898366b-20c5-3c89-b7c6-4d2864a79e53 | -17.09083 | -43.33932 | 2025-09-19 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 634ef812-0d69-34b7-91a8-1dd13910e5e9 | -21.29066 | -48.79725 | 2025-09-19 03:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 86361e01-2168-31bd-afb2-01255b5fb29c | -21.28611 | -48.79665 | 2025-09-19 03:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 08ed0fa1-827b-36d3-bb52-bd0d6b897ab5 | -18.58134 | -43.46894 | 2025-09-19 03:36:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| e134ab41-3136-3536-82d2-efaebd2096e9 | -17.45773 | -44.80227 | 2025-09-19 03:36:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8dea2bd-37ac-3ad9-8e93-0b48b25360ac | -17.23113 | -45.96158 | 2025-09-19 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7b2e6394-72a8-36de-af5c-b4fbb1906c8d | -20.34785 | -48.79034 | 2025-09-19 03:36:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bef92e1-e0ee-3b46-84ca-23fca980db25 | -17.21937 | -45.95819 | 2025-09-19 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1a83bc38-6db8-37af-9d2b-f653cc9328ac | -17.22724 | -45.95081 | 2025-09-19 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4ccdf854-e848-386e-951c-7a81b1f0cebe | -20.34414 | -48.79298 | 2025-09-19 03:36:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20a3dc45-0a2d-349b-be3e-01a72339505d | -18.64868 | -43.89377 | 2025-09-19 03:36:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8bfcdb9-fb92-33bf-87dd-37742fc7f8b4 | -16.51819 | -43.55062 | 2025-09-19 03:36:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3b11d88-f096-3e07-a8f4-6b15f0eafa44 | -20.21083 | -44.61069 | 2025-09-19 03:36:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a333308c-9f74-3604-8e95-d30eb165824b | -17.45848 | -44.79873 | 2025-09-19 03:36:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d490ee82-48e9-3f61-b514-f916ba12bf2e | -21.04567 | -48.44077 | 2025-09-19 03:36:00 | NPP-375D | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3f4042a-fe09-37f8-94d4-1001e2cebcb4 | -20.54844 | -44.02433 | 2025-09-19 03:36:00 | NPP-375D | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 39fdd990-efae-3514-905e-7e1051962f1f | -20.796 | -47.23896 | 2025-09-19 03:36:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4daf0d82-9708-3e67-970c-fd65c3980104 | -17.08764 | -43.33897 | 2025-09-19 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0098e189-6997-3bd1-887c-85cc7c82e44f | -17.08832 | -43.33571 | 2025-09-19 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa66226d-92e2-3732-8e6d-fc1cf3c595a1 | -17.163 | -44.79828 | 2025-09-19 03:36:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 632fa2c6-2e92-39aa-b0f7-8c469fd57bb6 | -22.04503 | -45.58944 | 2025-09-19 03:36:00 | NPP-375D | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 26d7c228-2762-3b3c-9183-d1ae3cdb7c94 | -21.3546 | -45.7842 | 2025-09-19 03:36:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5af5fbe2-aac2-3dfa-95a9-1471783373a6 | -17.20621 | -47.34885 | 2025-09-19 03:36:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b333518-8c8a-3360-8463-db9be693828f | -17.22524 | -45.9599 | 2025-09-19 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 074261b6-2bea-3c18-a878-a05318541f88 | -18.64227 | -43.89886 | 2025-09-19 03:36:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb011b80-ed22-3a13-828b-7bad48fcf9ec | -20.51537 | -42.39783 | 2025-09-19 03:36:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5bf0656c-7a3a-3715-ac64-d0b8a49c89bd | -19.82036 | -44.21944 | 2025-09-19 03:36:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a0033cf-0fee-3ddc-9451-cf07852be65f | -19.91267 | -44.58099 | 2025-09-19 03:36:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 83be2904-7ebe-3762-844c-98b1351278bd | -18.6528 | -43.89964 | 2025-09-19 03:36:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9564df94-bad0-3428-9a3e-6129b8a860ec | -18.1184 | -44.67237 | 2025-09-19 03:36:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7721aa93-fddb-3e57-a0b8-cc3dfc559eec | -20.79049 | -47.23885 | 2025-09-19 03:36:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4f25a3c3-67db-34ac-94de-c63af3fecf23 | -20.79481 | -47.24419 | 2025-09-19 03:36:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c927a8c9-2d08-31ba-a189-3a657672aadd | -17.08639 | -43.33503 | 2025-09-19 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31719f12-d33a-33d4-8369-b42a7626e194 | -19.95449 | -42.41565 | 2025-09-19 03:36:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 34846daf-a45c-3766-b131-8b778419920e | -18.58174 | -43.46705 | 2025-09-19 03:36:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 64ec87e8-e53c-3a9e-b9d5-e5736de11594 | -17.16467 | -44.79041 | 2025-09-19 03:36:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb7df654-cbb3-327a-88cf-275387018613 | -21.05205 | -48.44232 | 2025-09-19 03:36:00 | NPP-375D | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2074152-f9ec-3652-a60d-4f2b30229bd2 | -17.15829 | -44.79303 | 2025-09-19 03:36:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6baecd8f-63e5-31be-8389-255caebfbe60 | -17.08509 | -43.34153 | 2025-09-19 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f1d51009-0920-3d48-83f0-6fd9b50a6d5b | -19.9186 | -44.57878 | 2025-09-19 03:36:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 306ee78a-6369-3f73-92a6-4831bd139f31 | -17.06355 | -45.91087 | 2025-09-19 03:36:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9da6bf3-2a1d-3d15-909b-6b0a058de467 | -18.64713 | -43.90118 | 2025-09-19 03:36:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 631ff82b-0e42-3b84-bbb1-011eae9de50c | -20.33989 | -48.79454 | 2025-09-19 03:36:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca9990d5-927e-3c4b-9fe9-c629bb590613 | -20.79658 | -47.23985 | 2025-09-19 03:36:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 35ea170f-9f7c-30ae-8588-dddbf0ca8053 | -17.08326 | -43.3345 | 2025-09-19 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfe1bd8b-ae04-344f-96ba-b38cc7523550 | -21.28435 | -48.79499 | 2025-09-19 03:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d8d27e27-dbf8-3913-a4b3-1de191c6d3d0 | -22.03745 | -45.58932 | 2025-09-19 03:36:00 | NPP-375D | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 97527a66-3a0a-3d06-b4fb-589c00b40c8c | -20.51996 | -42.39826 | 2025-09-19 03:36:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 157dbed0-f396-3ecc-814d-cef13cc57780 | -20.54351 | -44.02302 | 2025-09-19 03:36:00 | NPP-375D | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 5056f1cf-2509-34be-9dcc-35cec9b5973f | -19.78959 | -43.74389 | 2025-09-19 03:36:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7882bbf0-d846-33d2-b6ce-d626fee02b13 | -20.34561 | -48.78693 | 2025-09-19 03:36:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f8df08c-9957-3261-bede-ca7ec358db5f | -16.51325 | -43.54913 | 2025-09-19 03:36:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c705868a-f66f-3eae-94c4-d695327231ae | -20.34134 | -48.78839 | 2025-09-19 03:36:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3119324f-8f5c-3d7f-8250-152003ff46af | -20.54218 | -44.02931 | 2025-09-19 03:36:00 | NPP-375D | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 139a3b95-30d2-3179-80a7-b4a18320723a | -21.16081 | -47.13161 | 2025-09-19 03:36:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b9aa68b-1590-3f31-afff-f46af3ceff90 | -18.39864 | -44.10098 | 2025-09-19 03:36:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b201dd3a-a35f-3015-90ce-5719945f1fac | -19.9214 | -44.15403 | 2025-09-19 03:36:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 457fa959-0f69-3b93-8637-cc47e87de1ed | -21.12177 | -45.72524 | 2025-09-19 03:36:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 523a546f-3650-3aa2-bed5-89967137b1e6 | -21.28295 | -48.80067 | 2025-09-19 03:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 06af41da-fa03-36f9-881a-befbaaa0e0b7 | -16.51751 | -43.5539 | 2025-09-19 03:36:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 793339c8-50e5-3ff1-a4af-3cd8d49e8a32 | -18.05384 | -45.52231 | 2025-09-19 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README9.md)
