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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee5afeee-cbd8-394e-83d9-fcb236afff75 | -11.78212 | -47.09853 | 2026-03-15 03:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfab9c08-06a4-3561-8483-b4f71d75282c | -12.6564 | -47.10014 | 2026-03-15 03:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a49ebac4-bdf4-3162-b2e6-ee420abe0a63 | -11.31734 | -37.62901 | 2026-03-15 03:40:00 | NOAA-20 | ARAUÁ | SERGIPE | Brasil | 2800407 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3d7dedd0-835e-3824-a026-0ff445f5e4fd | -12.75811 | -41.3981 | 2026-03-15 03:40:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f1ecd2d5-951c-3a41-9bb5-92b3c217c369 | -11.9472 | -41.3285 | 2026-03-15 03:40:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8f6f0817-0050-37a6-9677-8297149695d5 | -10.66546 | -40.30441 | 2026-03-15 03:40:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad58a29d-9553-3ca9-b4d7-a29a61df44fe | -11.94363 | -41.32342 | 2026-03-15 03:40:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f6cf0c02-2d15-3184-bce5-f415c68aa44e | -11.94285 | -41.32767 | 2026-03-15 03:40:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| abb768b0-f3b9-3fae-94a3-b597f8f3bc86 | -29.77611 | -51.1811 | 2026-03-15 03:45:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 5d3526ee-a144-3ce7-bd92-a8438349b5cd | 3.1092 | -60.8218 | 2026-03-15 03:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 3a2bf3eb-20e6-30d7-9402-690da14a6abb | 3.1093 | -60.8029 | 2026-03-15 03:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 7c02920e-dda9-3e75-96ac-e3f669b69a47 | 3.1093 | -60.8029 | 2026-03-15 04:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 65900711-5dcb-37d7-bdad-3e5ca2101b12 | 3.091 | -60.8222 | 2026-03-15 04:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d649e924-66c7-3c66-8672-79dc25c7cb5b | 3.1092 | -60.8218 | 2026-03-15 04:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 05f9e676-c092-34fa-8494-031b67b77826 | -10.0855 | -36.2324 | 2026-03-15 04:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.4 |
| b5fcc445-b36e-3b8e-9d46-1b715beab909 | -12.07426 | -45.33223 | 2026-03-15 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10353a6a-e284-37a6-8e7e-b69aeeed004e | -12.07997 | -45.29342 | 2026-03-15 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a80e7e48-7c8a-3f1a-9f2c-069768f8ee69 | -11.94489 | -41.329 | 2026-03-15 04:27:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2d8a6291-bded-3002-a311-5ed6c21a3a79 | -11.16709 | -49.23763 | 2026-03-15 04:27:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24c91cd3-96d2-38a5-8fc4-d922c0d8b512 | -11.16464 | -49.25261 | 2026-03-15 04:27:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4feeeb3-cc07-3162-ad7c-a0fe4c75193b | -10.03639 | -36.25042 | 2026-03-15 04:27:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3e1bbfc3-24b3-3dad-a403-89990dc0aff7 | -5.95568 | -38.63285 | 2026-03-15 04:27:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b49050d5-47c0-332c-a81a-017fd5c94f28 | -11.05367 | -45.38798 | 2026-03-15 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 431c92a8-a54f-35e3-ab64-6843487f5128 | -8.80299 | -44.80985 | 2026-03-15 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 073e1a30-e01d-38ab-bffd-d08a4cfa6d95 | -10.03306 | -36.25135 | 2026-03-15 04:27:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 2c6de17c-338e-36d0-9ddf-124e19703df9 | -11.94113 | -41.32411 | 2026-03-15 04:27:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3fa26b3b-66ce-31ba-9aad-ee55abe7caf8 | -11.95878 | -41.29224 | 2026-03-15 04:27:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ac5c9d36-c95b-376c-8593-349eea5e5858 | -8.79613 | -44.8088 | 2026-03-15 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6111241c-c9d5-30ab-a115-c496f3920185 | -11.94547 | -41.32475 | 2026-03-15 04:27:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4fa6e14b-1760-3208-b92a-3291e7120249 | -11.94605 | -41.32049 | 2026-03-15 04:27:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 29910b38-e027-363f-ba20-2b03e162d290 | -8.80699 | -44.80662 | 2026-03-15 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47b43c89-70a5-36fe-ae67-1dcfe74c52c5 | -12.52763 | -43.35337 | 2026-03-15 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6663debe-1f74-3117-95e5-918323f1ba6c | -8.80356 | -44.8061 | 2026-03-15 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7632edd-6ce9-3f68-9662-0f0f3cd49574 | -11.7841 | -47.0956 | 2026-03-15 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72e7c4a7-062a-3e75-8bfb-7f9667c93b0a | -11.78741 | -47.09612 | 2026-03-15 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72516b15-7c5a-3a28-b370-44a3f1e74c06 | -8.7967 | -44.80505 | 2026-03-15 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 476b6c4b-27ab-3b3a-84e9-0ff41e7689f9 | -10.03043 | -36.24964 | 2026-03-15 04:27:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 200e3193-fe0f-3dc7-813e-4b025d54ddb3 | -12.08054 | -45.28953 | 2026-03-15 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05e0d31d-164f-35bf-bca6-5b167455139e | -6.85103 | -48.74076 | 2026-03-15 04:27:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b30eeee6-7c2a-3fad-9f75-7810b5300aa8 | -11.028 | -44.67057 | 2026-03-15 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| db38c4a1-399b-3b91-a3ee-9ad984979aa2 | -10.03362 | -36.24694 | 2026-03-15 04:27:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d8e0a25c-0618-36ef-833d-a468e19708d7 | -5.95643 | -38.62768 | 2026-03-15 04:27:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a8c7ff6e-3b25-315d-bae7-357ecf8977bb | -8.79956 | -44.80932 | 2026-03-15 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ced7ef8-c1db-30db-9fb6-c14489b43623 | -8.80013 | -44.80557 | 2026-03-15 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b63db0d7-bd5e-3ae3-b35c-6c176d819326 | -12.65732 | -47.09843 | 2026-03-15 04:29:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a96920ea-47ae-3eac-bb47-c4eab0cb47f8 | -12.66172 | -47.09188 | 2026-03-15 04:29:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07935c82-23f9-3021-aec7-3062363b8094 | -12.65841 | -47.09134 | 2026-03-15 04:29:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27d55705-ca8a-37d7-9a91-8c6948a9b175 | -12.65509 | -47.09081 | 2026-03-15 04:29:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f1d712b-250e-351f-b500-d1a0f9272d48 | -12.66118 | -47.09542 | 2026-03-15 04:29:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 829bf279-f7f1-3478-9970-32bb25c8d9b5 | -12.65786 | -47.09489 | 2026-03-15 04:29:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20814215-38ec-3adb-82f0-1a1ee3775e15 | -23.45213 | -46.7005 | 2026-03-15 04:32:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c4eec45c-8721-3650-8f27-a96cd2e1506e | -23.45175 | -46.70225 | 2026-03-15 04:32:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 29fa2fe3-b64b-3344-92d9-0316c9534524 | -25.22987 | -53.51165 | 2026-03-15 04:32:00 | NOAA-21 | LINDOESTE | PARANÁ | Brasil | 4113452 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e0ba4d38-24ce-3dba-83e0-a11c09cd85a3 | -25.22931 | -53.50872 | 2026-03-15 04:32:00 | NOAA-21 | LINDOESTE | PARANÁ | Brasil | 4113452 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 99dfebb7-46bd-3853-93af-cf63f98b5958 | -19.87885 | -55.54993 | 2026-03-15 04:32:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 81df696d-8c9d-3e8b-9e4e-d2c5b6148892 | -23.47911 | -55.25883 | 2026-03-15 04:32:00 | NOAA-21 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d6fce68d-9e95-30f9-a45b-bd55301c2ae8 | -27.49496 | -54.48339 | 2026-03-15 04:34:00 | NOAA-21 | NOVO MACHADO | RIO GRANDE DO SUL | Brasil | 4313425 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 74474727-ae07-33f1-9340-de2e6d8d574a | -30.053 | -50.85038 | 2026-03-15 04:34:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| a0bb46ff-b988-3139-a201-acc3907ac465 | -27.56596 | -51.08441 | 2026-03-15 04:34:00 | NOAA-21 | ABDON BATISTA | SANTA CATARINA | Brasil | 4200051 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 525b6289-eef7-3ede-bf66-d86c434170ac | -30.04965 | -50.84972 | 2026-03-15 04:34:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 5956eaad-3ef9-3f56-82e9-d212a0c01502 | -27.75187 | -50.55625 | 2026-03-15 04:34:00 | NOAA-21 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ded33f12-a4fb-3d58-b7b2-2be4a2d33288 | -25.63761 | -53.38432 | 2026-03-15 04:34:00 | NOAA-21 | NOVA PRATA DO IGUAÇU | PARANÁ | Brasil | 4117255 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 97497ea7-2b99-37d4-96e9-0afb43be0e85 | -30.25397 | -50.98411 | 2026-03-15 04:34:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 8519cbfe-211a-31e3-a0c4-4389fe45079b | 0.8374 | -60.13435 | 2026-03-15 04:55:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8ab2f51-be2a-3a35-89a2-066957ee9c3f | 2.3144 | -60.24158 | 2026-03-15 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 732a5f16-a46f-3514-b84a-180730f321a1 | 0.83793 | -60.13781 | 2026-03-15 04:55:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9811192b-fd35-3ca6-b096-c23a123da401 | 1.87818 | -60.42974 | 2026-03-15 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aec763a0-9076-3f06-94de-5d5782a98acf | 2.31984 | -60.23993 | 2026-03-15 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6969f0a3-f76b-3295-ab99-e83f28f93d86 | 2.10533 | -60.19238 | 2026-03-15 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3697bd75-e015-3d01-bf80-47475a4b7029 | 1.472 | -60.05534 | 2026-03-15 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c283186f-ce5e-3bd4-8d25-e43d293d77c5 | -0.08933 | -51.28097 | 2026-03-15 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dda1fdb-0e90-3584-b9bf-8f9c607860cd | 2.10585 | -60.19587 | 2026-03-15 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 060b0c03-20a5-302b-a7ca-9cf7b36bb262 | 1.47796 | -60.05805 | 2026-03-15 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9c734b1e-5e51-346a-9897-67f6872a61c4 | 0.90701 | -60.2962 | 2026-03-15 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eff99c2b-1bc4-38b8-b882-6c4a65452ef6 | 2.32116 | -60.23805 | 2026-03-15 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76c8375b-5bfe-3f14-9e26-3447c3e8deeb | 2.31575 | -60.23979 | 2026-03-15 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c732577f-6756-3d4c-8e0a-93a66360ed5d | 1.55156 | -60.28154 | 2026-03-15 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6264a20-44d5-375a-b0ac-146e39431260 | 1.17662 | -60.00327 | 2026-03-15 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a1bc4a7-dfb7-3784-a8c8-a17df7865be0 | 1.87875 | -60.43348 | 2026-03-15 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fbde07e-0ed7-3f83-9983-be49a0802773 | 1.55211 | -60.28509 | 2026-03-15 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 709f8460-7929-3eb6-9edb-c341a549c21a | 1.1761 | -59.9999 | 2026-03-15 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a408291-753f-393f-8602-0fde8adeae37 | 1.17074 | -60.00083 | 2026-03-15 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47ea0acb-1301-3803-b5c5-400b060ea208 | 1.47253 | -60.05879 | 2026-03-15 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e358d62-cad7-3c7e-b2e9-0e85557270a0 | 0.90756 | -60.2997 | 2026-03-15 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f43d479-11f4-3cba-9852-8f138594d6ea | 2.31028 | -60.24118 | 2026-03-15 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7db750e4-79c2-3ec8-b1c3-ad4f3ca4bfc1 | -11.16604 | -49.23986 | 2026-03-15 04:57:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e15b3ed-92f0-3c3a-a426-7aec26ae7ef1 | -8.25211 | -48.29042 | 2026-03-15 04:57:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af24e64c-7bdb-3133-a1af-07b20d336db8 | -8.80076 | -44.8091 | 2026-03-15 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1236c8c-8d36-36bc-9afd-a3df453b3e77 | -6.85109 | -48.73823 | 2026-03-15 04:57:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15710d38-01ad-3eb6-b052-153d4784cef7 | -11.05105 | -45.39097 | 2026-03-15 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64fc8e03-00e1-35aa-b8dc-975594c63fca | -11.94407 | -41.33044 | 2026-03-15 04:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 731b3130-d9c3-39d4-8311-ecc4e2462255 | -11.94664 | -41.32427 | 2026-03-15 04:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0b1d65c6-fc14-319f-b081-13236f767c92 | -11.94597 | -41.33004 | 2026-03-15 04:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| dba9353c-4093-3c38-8b03-a120ee4cf180 | -11.16569 | -49.2378 | 2026-03-15 04:57:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a57e9f3-38e8-36cb-8479-644c4785c2f3 | -11.94004 | -41.32345 | 2026-03-15 04:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 795ef9aa-802c-3cda-a39d-ebfe40a8e9f5 | -11.9447 | -41.32467 | 2026-03-15 04:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7d68a60d-4c31-3ba3-8442-f80cc88f8422 | -11.05144 | -45.39066 | 2026-03-15 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a37f0d33-208e-3f07-86a0-b06c5f7fcc71 | -8.79609 | -44.8055 | 2026-03-15 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24733533-5e44-3bf3-91d6-9d0997ad5107 | -8.80115 | -44.8062 | 2026-03-15 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6239cef-98dd-390c-9cc3-a700832d3b46 | -11.93938 | -41.32919 | 2026-03-15 04:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
