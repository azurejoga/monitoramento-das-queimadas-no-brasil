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
| bf89ad56-28b0-3b7e-a721-f84c452eb8d5 | -12.11587 | -45.63614 | 2025-04-03 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27f12811-eecd-31c4-884e-6eac90e00cd5 | -19.71403 | -44.76938 | 2025-04-03 04:17:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7d73ccf2-f305-3043-ad45-99f70f2003d2 | -19.7101 | -44.77263 | 2025-04-03 04:17:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a1dbb3a7-53f6-35f4-b53e-73844d0f77c9 | -14.10139 | -47.66143 | 2025-04-03 04:17:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e0dcfd1-c65f-325f-9c05-c825f7aad614 | -12.79033 | -45.88174 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcb868ae-9948-3d3f-896e-58ec24c328b9 | -13.03264 | -45.09142 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1006fde3-e7df-3181-a645-dff6e44c7d55 | -15.80841 | -43.56875 | 2025-04-03 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a9a64718-d45c-3559-980c-df5316e529fc | -22.96363 | -43.59964 | 2025-04-03 04:17:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e42b0613-d2e6-3a33-a65d-0464ba812100 | -12.56091 | -45.34109 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8ef7afec-58a0-3da6-ba8a-5212ff8c64d8 | -17.16108 | -44.7967 | 2025-04-03 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f8320d8-5970-30d9-b51b-75ccfe1d17aa | -21.48177 | -57.08209 | 2025-04-03 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d49b1ddf-1ece-3f0d-a70d-bb3bcd6f7441 | -12.84465 | -43.83281 | 2025-04-03 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12d3ab39-da40-3c8a-bb12-3397bce1f9e1 | -21.45646 | -48.70668 | 2025-04-03 04:19:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35f64c99-4a64-3679-9bef-a0fce46d1827 | -20.16436 | -47.32076 | 2025-04-03 04:19:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0924d5f-1878-331c-98e7-951e614c3362 | -21.17888 | -43.97979 | 2025-04-03 04:19:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7198ab83-5d60-3458-8169-39e303b27303 | -19.96731 | -45.16458 | 2025-04-03 04:19:00 | NOAA-21 | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72fe16a9-3855-3881-99d2-2f66605dd750 | -19.42784 | -54.78253 | 2025-04-03 04:19:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76c0216a-3b6a-3590-b3de-4d07b5cfde05 | -19.42292 | -54.78135 | 2025-04-03 04:19:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acc7f149-621c-3ea0-9c69-e751758638b6 | -20.21194 | -50.64591 | 2025-04-03 04:19:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2846c151-f588-3c4d-8c75-fa1e01cc6718 | -20.90231 | -43.82062 | 2025-04-03 04:19:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e00187bd-80ab-3c74-bb6f-d522734f02ee | -19.42639 | -54.78712 | 2025-04-03 04:19:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7971c1be-ee45-3703-a2f6-b8cce62856e5 | -20.41603 | -43.55456 | 2025-04-03 04:19:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| feb29c8f-08f6-3009-9a69-5de8820a0872 | -21.13108 | -48.67497 | 2025-04-03 04:19:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0424520e-cf66-3add-aa16-1d1f7ccdc73b | -20.16042 | -47.3239 | 2025-04-03 04:19:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22826690-14cf-35ee-ac3a-4bf8caa67851 | -21.13208 | -47.80095 | 2025-04-03 04:19:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8831956d-b1ce-3753-82ff-55a8ad196cb4 | -19.70978 | -49.82737 | 2025-04-03 04:19:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b8de4ed-24fe-34fa-9b9a-bcfcf4c3dd29 | -21.1304 | -48.67894 | 2025-04-03 04:19:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 02565f65-e264-3eb5-ad74-eccf1a6b5777 | -20.76359 | -46.7685 | 2025-04-03 04:19:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 240993dd-221e-3603-aad1-09b450ee97f7 | -21.12697 | -48.67829 | 2025-04-03 04:19:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b5bd25eb-459c-3501-8008-fda5a1c73b0f | -6.23402 | -48.05584 | 2025-04-03 04:38:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a163da2-9579-3974-b914-d675c878c0da | -6.23065 | -48.05535 | 2025-04-03 04:38:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b2ae9ff7-8557-3a5b-8f27-513e2ace1c82 | -6.23739 | -48.05635 | 2025-04-03 04:38:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f03cdf52-6879-3b2c-ae75-f5306cdc0f02 | -14.09881 | -47.66566 | 2025-04-03 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72bb46ea-1146-393e-8d01-60441b020be4 | -12.29386 | -43.544 | 2025-04-03 04:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a38f579-69d4-3b34-9b0f-42045b526261 | -12.11987 | -45.63518 | 2025-04-03 04:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe6903e9-f682-3b45-80be-6577fff2ca2f | -12.78825 | -44.97247 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc5e387d-c735-3094-ba15-39eddc321fad | -14.10047 | -47.66347 | 2025-04-03 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ace90f5-d492-3c7f-afe5-5587889c6c3a | -10.35174 | -44.83804 | 2025-04-03 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c8ad041-418d-3aaa-81a5-411b90757611 | -12.56191 | -45.34133 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd868656-d89d-33bc-9406-b8477778bab2 | -8.90235 | -50.04416 | 2025-04-03 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8382809b-6e10-3af0-9c4e-e5a2ec1ae3c1 | -13.03382 | -45.09356 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 258bac0e-6a95-336a-b55d-17c43f95a295 | -12.69439 | -44.94027 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 24fccd09-76a5-3b32-aa78-5f5dda096f3c | -14.10247 | -47.69287 | 2025-04-03 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c0ee7da5-fdf9-3150-8c52-f62a8e0b6685 | -13.03696 | -45.10208 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75fcb678-5368-3ee3-bba4-769853904634 | -12.29119 | -43.5465 | 2025-04-03 04:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 940dac1c-6c68-3c2f-9b8b-1d2504461692 | -14.10308 | -47.68854 | 2025-04-03 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1240e521-08f5-3861-82eb-38bd3b3c3a83 | -10.3476 | -44.83743 | 2025-04-03 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2e8b605-70d0-3612-8b53-76f15a20a54a | -12.29181 | -43.5416 | 2025-04-03 04:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c664533-62da-39c1-8b94-08b4f4dca744 | -12.12037 | -45.63165 | 2025-04-03 04:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2548e7f7-3810-314d-b4fd-81eb091b60a9 | -13.03274 | -45.10148 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb594b99-a9aa-33c8-a6df-171bcc795ad0 | -12.30143 | -43.50307 | 2025-04-03 04:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 678a02af-24b5-34f9-9741-6b28bd81fc65 | -13.03491 | -45.08563 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fcea392-ead1-3f5f-90c3-816843112c7e | -13.03437 | -45.0896 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c43723e9-c288-3f02-b0d6-faed588c758b | -8.10957 | -43.12635 | 2025-04-03 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ae8190c3-61cb-3338-a0f1-c58c0077f6bd | -13.03328 | -45.09752 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ab8134d-6613-39eb-803b-ecd4181bdb25 | -12.84536 | -43.8339 | 2025-04-03 04:40:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b80ce70a-8e0e-3b31-9e34-62cdec7fbbb3 | -14.1098 | -47.69394 | 2025-04-03 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbfd8c01-ba21-3bde-ae67-b53c5587f7bc | -14.10614 | -47.6934 | 2025-04-03 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1731f9af-07f8-322f-97e8-92df9354fc96 | -13.03859 | -45.09018 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83bd8f05-bb6d-3b79-8f11-62fcd955f0c0 | -7.29785 | -55.31836 | 2025-04-03 04:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 31093efe-da33-309a-9295-7093d651e7e5 | -10.58292 | -48.51829 | 2025-04-03 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63a5d400-d1ed-3ac9-895d-b0e953e6e3df | -11.27422 | -40.98341 | 2025-04-03 04:40:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d6d0ce11-8cdc-3896-a8a6-697636367f5d | -12.55778 | -45.34073 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2e237d13-72c2-3697-8aab-33a9b3f3c5b2 | -13.03805 | -45.09415 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f3f8a8d-23d4-396a-8b88-e36652fc7613 | -13.03751 | -45.09812 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80b50947-6e46-3f4c-8163-3f48f9fa9970 | -12.69864 | -44.94086 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73420d5d-6a2e-32e7-b0cc-503ab5bd31f7 | -13.56592 | -45.2516 | 2025-04-03 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19a6fcdc-1fba-342b-a140-bbdc19f6847d | -12.29677 | -43.50242 | 2025-04-03 04:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c293501-28f2-3f2e-afca-3362645ec149 | -12.11583 | -45.63465 | 2025-04-03 04:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96b1112c-f744-304e-80b9-f8812089d193 | -9.21882 | -47.8189 | 2025-04-03 04:40:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d286bcc2-959c-3b2a-a3f3-38593b390f47 | -13.0296 | -45.09296 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cada0bf2-f309-3247-8b25-b60825534fac | -11.27467 | -40.97985 | 2025-04-03 04:40:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d9361f2-e67d-3e4b-8544-7d144bf49df7 | -13.56538 | -45.25552 | 2025-04-03 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5866b99-97f5-3233-a853-7699851ca39f | -9.21535 | -47.81837 | 2025-04-03 04:40:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6e69dcef-96e9-3b2e-91b5-97c7e9ae813f | -13.56645 | -45.24768 | 2025-04-03 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed0f3f6d-9e53-357a-8589-1cbdf7e3ee2f | -12.78454 | -44.96782 | 2025-04-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3892d26c-1a41-375e-808d-9122fd9f940b | -12.28921 | -43.5434 | 2025-04-03 04:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f95f79e-5fc9-3034-834e-3a88af5cc107 | -17.77511 | -42.80692 | 2025-04-03 04:42:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8c7c8fe-c5a5-3f65-8eb1-417309002e6f | -19.14265 | -50.59632 | 2025-04-03 04:42:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 47843585-a842-311d-b8ad-d974a14d38f6 | -17.15869 | -44.7967 | 2025-04-03 04:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b16d77c-f21b-3ac7-b71e-f03a32a90886 | -19.49652 | -52.5157 | 2025-04-03 04:42:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d00606ef-f32b-3cfd-a86a-47022eda3a30 | -19.71261 | -44.76843 | 2025-04-03 04:42:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 61de178d-ffc9-3681-817f-a32a766af8fa | -19.3651 | -45.50183 | 2025-04-03 04:42:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d2724cc-2097-3cbb-82e7-92eb9a3a0d0d | -19.71205 | -44.7735 | 2025-04-03 04:42:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8cd5355c-bbed-3754-8fef-e9b97f2a785f | -15.80828 | -43.57053 | 2025-04-03 04:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78b3ee01-921a-33eb-a928-d90020a9316d | -15.8059 | -43.57161 | 2025-04-03 04:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d76d27cc-7107-3c9d-ae12-d5fa8f07aff3 | -20.16093 | -47.32248 | 2025-04-03 04:42:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eedbba4b-d19b-36d1-b304-a1c0ee41ae9c | -18.13848 | -52.35731 | 2025-04-03 04:42:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc3b7bce-98fa-3210-9c37-904ce9c65211 | -18.19726 | -52.17286 | 2025-04-03 04:42:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| afaf113f-d5b5-3829-bbc5-6cde39a2d7a6 | -15.80654 | -43.56607 | 2025-04-03 04:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85fc1d3d-26f5-3bab-b624-0cc3bdfdb21b | -17.78037 | -42.80765 | 2025-04-03 04:42:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43f4a3c1-94d0-3093-9f35-174cd623a85a | -14.87032 | -51.98517 | 2025-04-03 04:42:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be31f59c-80f6-302f-b030-15e55d61e9e6 | -20.17226 | -50.50336 | 2025-04-03 04:42:00 | NPP-375D | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d1b753de-0c40-3b03-895a-40ba4b0ca464 | -19.71143 | -44.77099 | 2025-04-03 04:42:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6101c64d-78e3-3781-8563-ae6f7315b6ec | -16.3482 | -43.69721 | 2025-04-03 04:42:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f21461e-a8fe-3c6f-836c-ecceb6a2b96f | -18.13515 | -52.35672 | 2025-04-03 04:42:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 824e0b3f-56bf-3a59-a8e6-caa5e0b326cc | -15.8034 | -43.56987 | 2025-04-03 04:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 372f31f9-2b02-3ad6-aee6-1ab3312d6f10 | -15.52558 | -48.50325 | 2025-04-03 04:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e433acb-80bd-329d-aed7-69059af4cb7a | -19.42425 | -54.78514 | 2025-04-03 04:42:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 496de35a-d0fb-3457-b3e1-e2aa9b8554f7 | -20.16091 | -47.32339 | 2025-04-03 04:42:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README4.md)
