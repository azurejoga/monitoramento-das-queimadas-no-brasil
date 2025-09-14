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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 035530f7-8eda-3c0b-8215-b75d889cd8b1 | -11.33663 | -50.83381 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7ac565c4-9839-3a38-bcd2-fc65e8d76862 | -17.06962 | -47.15574 | 2025-09-14 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bb44a81-2ae2-3e39-b7d3-bb5df7586047 | -13.9258 | -48.29537 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31835200-767b-3857-94b2-752fc05a4c0a | -10.76344 | -46.47386 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a14d6d9-0355-312b-a31c-459943a7fc44 | -10.93523 | -47.35446 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9202c91-8e53-39ce-955f-01e0f42f2c1e | -15.76502 | -52.22688 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01fef913-ec90-32a9-b945-9997d9bdc815 | -15.92059 | -49.97762 | 2025-09-14 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 536adb67-d04d-3c0a-a151-2f774ce1bd13 | -17.28298 | -46.10019 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66d85a04-3e76-341d-ab4c-b7df9626c875 | -10.90052 | -47.21346 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8b26f46-3c8d-337d-a47f-de9647c5d5fa | -6.69479 | -45.54606 | 2025-09-14 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1b42e24-5fbd-33ff-ab95-c151f9288ea2 | -11.77679 | -46.61979 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f8c03d19-e10f-35ac-8ade-e9382b90e90a | -15.04373 | -50.15023 | 2025-09-14 03:49:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 29446888-3bb4-3ac8-92b1-245b1de45ce8 | -5.398 | -42.83117 | 2025-09-14 03:49:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d36a77df-f4b9-3b44-a096-6a0ac57361f1 | -11.23108 | -47.62498 | 2025-09-14 03:49:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 773c6ea8-0565-3b96-889f-cda9ca426087 | -15.18293 | -52.4724 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa05f629-bb5e-32a0-a8bc-e526be4222c0 | -12.13706 | -47.59375 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64afb202-d725-3694-8600-145c410f8d5d | -13.93622 | -44.85366 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bad036f0-1a8c-3f44-bf86-1e08f7705983 | -13.28667 | -43.78886 | 2025-09-14 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd0a8b7e-f866-351c-b653-f0fd0227fd94 | -11.37801 | -47.72001 | 2025-09-14 03:49:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99bcda29-e282-36c7-a467-3e808fec2716 | -13.94027 | -44.83186 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 362e4ac7-ed47-39af-9eb4-efa5c0a99f87 | -12.75171 | -48.00482 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca8da64f-a4e6-312e-bb83-6c8e9236580c | -15.68641 | -49.91608 | 2025-09-14 03:49:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8d6c500a-d677-3b6b-b1ba-cb8b3b7793e1 | -5.12958 | -45.11633 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f620e531-dd34-304c-9e9c-8b36ced7c559 | -11.47208 | -43.59922 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39898417-b736-382f-95f4-1eae5fc14aba | -14.26469 | -45.06076 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 938f9eba-bcd6-31d2-9afd-bdfa4ffb684c | -14.20145 | -46.16968 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6217fa9d-43af-3710-b190-176aaa22df5c | -11.89077 | -50.54779 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc8d6e7d-b7c4-3b9d-9ad3-d90a6a4b69b2 | -10.92049 | -47.19603 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04a991d1-cf07-329e-a7ca-b2676fa0805e | -11.35659 | -47.32399 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4db9f444-c6b2-3cc2-9940-308c15d00f4c | -17.32101 | -46.0942 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac651ffc-5730-39f2-bf26-3f5014051c0b | -6.10989 | -45.93205 | 2025-09-14 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a39c1261-7bfc-3a34-8621-72f2a445b61d | -15.68723 | -49.91218 | 2025-09-14 03:49:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 54e81d32-3b52-3a41-b2ce-f065b3691978 | -11.46649 | -43.58221 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2a269df-d13a-3c72-aa42-b9c09615a636 | -10.92852 | -47.36035 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ea04d80-5063-3ba9-a0f2-2c7e8528d2a6 | -11.47918 | -50.78233 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b1f66448-5e52-3371-ab78-82bf25343b47 | -18.0049 | -46.95772 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 156b9f2b-c4f9-3d78-b771-ea8cf28c81d9 | -14.18272 | -46.16021 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11568cba-01b1-3120-bb68-b8d94d96562b | -12.75243 | -48.00113 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a1584171-05d7-35d1-817d-cf9c2987f407 | -13.93911 | -44.81401 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cea0ae33-fb3b-3e29-9fd1-03abe4023e01 | -13.90139 | -48.30392 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35616819-f498-34b8-baaa-d3b161357075 | -12.77803 | -48.04566 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9cb639fb-6b0a-3cbd-8d16-6ac731f6e472 | -5.59161 | -39.58415 | 2025-09-14 03:49:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fd49dbdc-f844-3f60-b25c-7d7617562160 | -16.50027 | -42.1262 | 2025-09-14 03:49:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2d02af96-9a80-318a-a623-e9a8880ae87a | -14.43587 | -43.19574 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03fdf829-7624-3b6c-828b-bde88bc41d02 | -12.97008 | -48.02709 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec9234a9-b964-3535-b085-47a245178134 | -13.93754 | -44.82245 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08382b21-58f3-34ef-8e75-4be9d2bd7e8a | -11.29034 | -50.82347 | 2025-09-14 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67b63958-fccf-350e-98a8-f947672525fd | -14.28478 | -46.11685 | 2025-09-14 03:49:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cdcd735-674b-33ae-881d-8fdd7c6eb102 | -11.13282 | -45.31895 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dacdedc9-011f-3254-81ae-dd0f3921d7c6 | -15.40861 | -52.97842 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3caa178d-2909-3846-be2b-fdf8b7a1437a | -12.14242 | -47.59489 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc8f4fff-cc19-36f3-b974-543e07a49a45 | -11.83039 | -46.36395 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fb4d38dc-a9bb-3203-af12-c673080296b3 | -11.45033 | -50.76742 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2b8f600-1dee-3704-8581-27376229bca1 | -11.24714 | -47.63195 | 2025-09-14 03:49:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f9ea790-4815-3bbd-aa0d-614193e7802a | -11.44748 | -50.76935 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 416d559b-6759-3587-9e90-3727bf3442f2 | -6.20017 | -42.70541 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4e0872c0-d0a2-3c50-8585-837d9fa9925c | -10.40337 | -48.60612 | 2025-09-14 03:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 27e63a5e-4f26-30cc-904c-b0e99db62fcb | -13.93833 | -44.81822 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4ce6a71-4745-3452-9b44-a64a915e1012 | -15.64851 | -47.04241 | 2025-09-14 03:49:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02093eba-2473-3836-9e03-9b9311eed311 | -12.95173 | -48.03064 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7eba5227-61ce-30a2-b745-dfd96f661588 | -6.68828 | -45.52253 | 2025-09-14 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e1bdf2a-005e-35f4-89c1-1735b0395f60 | -11.13465 | -45.30909 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffd899cd-ef39-3220-a6fe-9e02c7e28bf9 | -6.17479 | -41.15199 | 2025-09-14 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e689a0b-19fd-35d2-8bd4-a679163fef4f | -11.40195 | -43.52757 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82af6a1d-deda-351e-88bf-e818bdf13661 | -14.19585 | -46.16839 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f02bab9e-1caa-3c7e-a505-85a23203951d | -11.13657 | -45.32503 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a629ed91-dc44-375e-901f-fb3ffbdbe815 | -13.96589 | -44.8147 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76e4a29d-f1d2-3b7b-ab60-1d550167a8c7 | -14.3158 | -46.1415 | 2025-09-14 03:49:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 021e5551-7a9f-3b5b-99aa-305b8521cd9a | -13.92837 | -44.84749 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7c5bd0b-da11-3559-a579-61a118e2c020 | -8.17215 | -34.98027 | 2025-09-14 03:49:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f4fc6648-0356-39df-a821-1ae2f97d435a | -11.30239 | -50.8322 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b47ff90-d151-3bb9-90ae-912597fd773a | -12.08804 | -44.72688 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 790849c0-a674-3f7c-b192-79b276fca2e6 | -15.15381 | -52.47492 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce3eeb8b-1ae2-35f7-bfae-7b183c2e9948 | -16.32866 | -51.52192 | 2025-09-14 03:49:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd93698a-021d-3100-9eb9-29f10815845a | -12.08359 | -44.72604 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a803379-e778-3173-98db-fbbb15a8315b | -15.1939 | -39.86341 | 2025-09-14 03:49:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f99b9262-8bc7-3f21-9556-70670e75519d | -10.89966 | -45.5668 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c378da98-f2ea-3550-abf9-4fe5888ed64a | -12.08275 | -44.73055 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc448319-f165-349e-a84f-aad1db6d5049 | -12.72818 | -48.03832 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4794ef0-45d7-33bc-b2e2-4f7130d577a5 | -15.63158 | -44.37984 | 2025-09-14 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae17f31b-035b-3f71-9146-14a39e76dce2 | -16.65432 | -49.78588 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91ceabd9-5bc7-3718-9fd0-602d5b80319e | -15.02881 | -50.16195 | 2025-09-14 03:49:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5370fc64-9f5f-3cb5-af46-93466d463355 | -14.63729 | -52.11826 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed837b79-a641-302f-a6d2-242de86a9261 | -15.43665 | -47.36134 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2beedd09-f5a3-3a00-ac8b-4ac7a2c09308 | -5.64407 | -43.89693 | 2025-09-14 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d988d17-27c1-38b7-9197-f0c58238424e | -14.60963 | -46.333 | 2025-09-14 03:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05288e32-97c3-3746-a6aa-a21916b89923 | -17.99766 | -46.94568 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f278f62e-caa8-38eb-9ae2-e4106a0fd652 | -10.73357 | -46.43518 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfdb3f1f-c30f-30e9-840e-77df15531149 | -15.18734 | -50.11111 | 2025-09-14 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2648c3d7-6275-3fa8-8550-e4c706c90ef7 | -12.96401 | -48.02568 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 931268a7-0ad5-3712-ab71-4ed8cd30037f | -11.48205 | -50.78056 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1094540c-b4da-39d7-bb22-53b948aad5e4 | -15.4338 | -47.34956 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 950cfaaa-9628-3b85-a6f6-ae13bd6f0dd0 | -16.40912 | -41.74854 | 2025-09-14 03:49:00 | NOAA-20 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 84172f2e-c284-34cc-9764-e5a56ffb2137 | -13.93864 | -44.84063 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5e3653c-ba6d-3bc6-af13-e7e4273cc64a | -5.79619 | -43.89358 | 2025-09-14 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a702b183-7f57-3aa2-b473-8017e2340c3d | -13.87467 | -48.29195 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9ce55d9-0ee4-35fd-817f-f9ac72420f28 | -6.17934 | -41.173 | 2025-09-14 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d7a69a80-6ab7-37e7-8fed-1846b4f1001a | -17.28387 | -46.09563 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d261778f-d8c1-3826-a321-c25443bfefc4 | -12.96703 | -48.01004 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e18ae2a6-5dca-34fb-b2fb-d31ae91b555b | -12.74339 | -48.01852 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README22.md)
