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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37e5440e-c0fe-3ada-ade4-78c9967fb70f | -20.95201 | -46.10236 | 2025-08-20 04:12:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8de79447-2265-3eab-aa7a-9025eda31763 | -17.66739 | -54.06247 | 2025-08-20 04:12:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8bce26c-6deb-3fe8-aaca-f634faca81de | -20.22092 | -44.13358 | 2025-08-20 04:12:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4694dba6-18ce-3a2b-8efd-f69ffab2cb6f | -20.11127 | -44.33843 | 2025-08-20 04:12:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 90c335b8-0a72-3b8f-ab88-c5acf6df1d0f | -20.47185 | -45.08191 | 2025-08-20 04:12:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6a624747-6537-3306-8dd2-788da805266d | -19.88313 | -49.83773 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 869eac78-9ace-3e63-b9c9-75a240718002 | -22.27003 | -48.50201 | 2025-08-20 04:12:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f94e0c6b-ed25-3a1d-b2ae-890fcd350fba | -19.73706 | -47.87849 | 2025-08-20 04:12:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4e9bc2d-e3df-3251-a8a8-0ee0c28ed404 | -21.89828 | -47.22782 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b80b7c14-5089-3880-90f9-917e843fa2bf | -21.90541 | -47.22835 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 5bff50ab-4804-345a-ad06-23530087e05b | -23.02318 | -47.40125 | 2025-08-20 04:12:00 | NOAA-21 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0bdc7379-fca7-31f3-aa1b-ddd66a3e742a | -21.91228 | -47.24993 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 973e20e5-3d6f-38f8-99dc-f3051bd9bc03 | -23.9785 | -49.65143 | 2025-08-20 04:12:00 | NOAA-21 | SÃO JOSÉ DA BOA VISTA | PARANÁ | Brasil | 4125407 | 41 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e02e8389-a396-3366-8425-e01d6af0b01d | -21.36383 | -45.05239 | 2025-08-20 04:12:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7ea43c14-a031-37f1-8c1a-c49e4615b3ce | -20.43985 | -41.58509 | 2025-08-20 04:12:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6bb161f9-d47e-3a31-a4b4-7d33a3dfd225 | -19.73137 | -48.97535 | 2025-08-20 04:12:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e4b393a-3a7c-34e1-9552-1653a29bcaa0 | -18.67974 | -48.17348 | 2025-08-20 04:12:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 82093884-04fb-361b-98c1-6552546fb997 | -21.90607 | -47.22443 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 56f93c77-aaec-3952-84bc-c67447707846 | -21.69362 | -41.30162 | 2025-08-20 04:12:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fb58c544-58af-3fdf-9028-8c1b1589a2fb | -19.74976 | -46.04075 | 2025-08-20 04:12:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55e452df-cd50-3201-93f5-881d62d5314f | -23.65121 | -47.28873 | 2025-08-20 04:12:00 | NOAA-21 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6eab86d3-d11d-3e6b-9aab-0a919daf270c | -13.1364 | -54.9376 | 2025-08-20 04:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| a853b73c-2845-306a-baf3-dac6387f5d13 | -8.034 | -47.6639 | 2025-08-20 04:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 01d25a65-02fd-3648-85eb-cb52f6557b1f | -13.1558 | -54.9151 | 2025-08-20 04:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 8d095ced-250c-340d-9f6b-d70b6d27e822 | -13.1367 | -54.9171 | 2025-08-20 04:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 7cb243b5-987a-3200-be1e-3f904d8fa7ff | -13.1555 | -54.9357 | 2025-08-20 04:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 3f5e883d-4e6b-3352-94ac-13d0a65766d3 | -13.1364 | -54.9376 | 2025-08-20 04:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 7b57838f-cdfc-3dca-9e96-e4ada261fdf5 | -13.1367 | -54.9171 | 2025-08-20 04:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 29f4aca9-b6cc-37d8-b8b9-50da66565a75 | -13.1555 | -54.9357 | 2025-08-20 04:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| aca04d1b-e02e-3f8b-a3d6-235f49aeb549 | -13.1558 | -54.9151 | 2025-08-20 04:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 90207e33-5608-3ff9-9432-5c31e3a843b8 | -6.4532 | -45.49262 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dd9caf6-f924-3481-8125-558c5a501d42 | -5.6438 | -43.3748 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6c24658-292b-3d04-a65c-6c07ab0e87a6 | -3.38441 | -47.60937 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7fdfddd-6c6c-31a9-a8a4-56824d574d72 | -4.7785 | -45.31889 | 2025-08-20 04:34:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bee5ea80-38b6-39b8-9bbe-503a4ebba200 | -6.23398 | -46.24067 | 2025-08-20 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c223b437-0bee-3024-ba5f-45e0b144bb06 | -6.71164 | -44.32827 | 2025-08-20 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 194e0b9c-c71d-3a8b-a068-efefecd1092f | -9.29847 | -40.23656 | 2025-08-20 04:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7e1eb6fc-c576-37cb-b30c-066b6c8d5ce8 | -4.01664 | -48.0598 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c23b3545-3d4d-39e5-9723-f4b369714c52 | -8.30221 | -46.35506 | 2025-08-20 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efad1a8e-dc80-328b-9468-17c807c8e2be | -6.46315 | -53.37773 | 2025-08-20 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a583c048-2895-3ecb-b77f-58b65d006707 | -8.0273 | -47.67085 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e1c68db-0b03-3ed0-821e-5f762e64259d | -7.25286 | -50.18237 | 2025-08-20 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e310b5bf-7e73-3e05-9837-bc37cb0ba93c | -5.64165 | -43.38894 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb4213a9-5681-3997-bdfc-49f7c6fcd07f | -3.48225 | -51.19049 | 2025-08-20 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76adc121-653c-35c6-92f1-85557337f0e0 | -2.58827 | -51.92358 | 2025-08-20 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29cb76da-4aeb-3ded-adbf-82f146375f03 | -5.63258 | -43.39703 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebdf9be2-c45c-34be-8ba6-22105f8bbab9 | -8.02452 | -47.66683 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3767402c-cea1-361b-8b37-4f225711c47d | -8.30799 | -55.10381 | 2025-08-20 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7664ac5c-d5b4-3805-8a0b-d734687237d9 | -5.7586 | -43.98602 | 2025-08-20 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 779c7330-4490-376e-b8eb-50632b4cee23 | -4.42751 | -47.75278 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d4d86730-6613-3cde-ad63-9d422463daa8 | -6.08031 | -44.58557 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 447b3047-25de-35ee-92c3-fb0cee779b26 | -5.78503 | -43.60944 | 2025-08-20 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae9e604e-deb7-3eb6-b8ac-faba5b326c9f | -6.13128 | -42.95132 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| fa4d2aac-4f34-311f-8685-984a87b90d18 | -6.1894 | -53.51997 | 2025-08-20 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cd8b0f7-800d-3cbc-ba13-2e9cbe590617 | -7.63265 | -45.26876 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7c6e2e9-1f8b-3932-b310-ceedcb24b7ac | -5.63926 | -43.37891 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57e6e4f7-24e5-369a-9628-b92670f10ff4 | -7.65526 | -45.25886 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e83628d-1025-334c-8bf3-d4b1611cf602 | -7.06933 | -46.87751 | 2025-08-20 04:34:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 532b6fa2-2556-36a9-9f49-1ed9c38ea495 | -5.78016 | -43.89475 | 2025-08-20 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4702abb3-b43b-3216-b672-8116d4e98a90 | -4.20607 | -46.43309 | 2025-08-20 04:34:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 744efe97-f200-382d-9ae6-c010bee3146c | -8.22267 | -44.41486 | 2025-08-20 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ca62b7b-2abc-387f-bf11-78ade44ec900 | -8.17332 | -47.34165 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b621b6c-f9e8-304c-963c-6161354c5844 | -6.55875 | -43.00235 | 2025-08-20 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b280884-5ba4-30f6-8727-5a5ea700727b | -3.65286 | -48.32467 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8eb0c83e-68ff-3e13-81e1-86f35b813181 | -5.42125 | -47.15768 | 2025-08-20 04:34:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6284b02-2857-3987-8b21-4e23becc46c6 | -8.30106 | -47.62454 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 01313d9b-7672-3990-a213-678cf33743ca | -7.58775 | -45.42033 | 2025-08-20 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1a16fa3-c2c5-3087-9364-02c46b0fcd47 | -5.64691 | -43.38014 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bd8e609-f131-3b57-88af-4160a53abff7 | -8.79942 | -45.4738 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36c918c4-e7a9-3e3b-913c-7a6e8cbbf21e | -8.61721 | -49.84896 | 2025-08-20 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2fca456d-7ae5-3c6e-bc5d-f9f12f47c739 | -7.63744 | -45.26123 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac60afef-85cd-3175-9366-38e33ef5bc17 | -6.26734 | -52.82311 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c8d849d-d573-3df5-bb24-6d299bf3c37f | -7.64992 | -45.27034 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c071af3-0832-3672-ac6b-0954790a60dd | -8.27227 | -47.29272 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baa905b8-0e6c-3679-95be-8d4474d35e77 | -8.89824 | -47.33183 | 2025-08-20 04:34:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58219c55-0173-384e-bb5d-792500d146bb | -7.63554 | -46.22104 | 2025-08-20 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17e9607a-b894-3039-a867-b94812e31f57 | -6.57812 | -44.47121 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f73a8dfb-d812-3aa4-be44-b548dfbb80ec | -5.64308 | -43.37953 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2353ed0-b5a1-338d-822f-bd28584b9cd7 | -9.24931 | -44.49758 | 2025-08-20 04:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3d6b83b0-5283-3256-84a8-1ca293090681 | -8.30874 | -55.10603 | 2025-08-20 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0fe9e702-79b6-3b2d-aa6e-83b3b2116a33 | -8.03118 | -47.66789 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3dccd3d7-07c6-39c1-82c9-ec987951971e | -3.05086 | -47.0189 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7834a564-0dc8-3a3d-a996-afd6a9a6ec5e | -6.85112 | -43.61147 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e39a533-7f23-345b-852b-e48d17942a48 | -5.78896 | -43.88708 | 2025-08-20 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 894f2dde-23a7-31f0-bd9e-a014c1ea2001 | -6.3974 | -44.25739 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04148ab6-98ff-3727-9f71-4b3fa1fadeaa | -8.8097 | -45.4394 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94a2f0e3-9416-33bd-a4c0-f6afe7f661db | -4.39373 | -47.77234 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f486e73-67f6-3057-85af-a2d5f2c4b700 | -6.86264 | -43.61327 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a54c20d1-c536-3af5-811c-0154a0091628 | -7.58199 | -44.39802 | 2025-08-20 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 813bcfcd-e996-30d7-b09c-2c76762fcbc6 | -5.66958 | -43.37121 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 969a6473-5baf-3a8d-98b4-e29b0598b0fb | -7.65821 | -45.26344 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5b1b3c2-20a3-3bcd-a394-e3e44f19c21d | -4.8733 | -47.75913 | 2025-08-20 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a65597b5-1cc2-3744-9cf2-10b8adaf15ee | -6.20428 | -43.55948 | 2025-08-20 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd508dd3-bbb6-3c5a-9587-825e98b2b460 | -6.51101 | -43.45035 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 386b3998-2388-3492-86ae-76193a116c0d | -4.8745 | -42.70925 | 2025-08-20 04:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4dbc3e76-5552-33d2-b47a-39fb9a37cda7 | -6.6187 | -43.88077 | 2025-08-20 04:34:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 46147cfa-dfdf-394e-8272-19d990f3055f | -7.5857 | -44.39856 | 2025-08-20 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5fb85756-3836-3898-8529-6998915e8027 | -3.82094 | -41.56255 | 2025-08-20 04:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 11693b99-3bc5-3f0f-a2cb-b5f5d4c32d43 | -8.81971 | -52.02996 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7971b7b-2959-325b-9173-b1e045d28ddf | -6.57733 | -44.47354 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README25.md)
