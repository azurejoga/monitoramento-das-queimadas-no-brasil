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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c79e951-bca2-35f4-a77d-29126c7dc0ea | -20.10578 | -44.81378 | 2024-09-27 03:49:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 93fbf677-0e57-32d6-98cd-4070eac22df5 | -22.44241 | -44.13441 | 2024-09-27 03:49:00 | NOAA-20 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a3d567b0-1328-3f12-8f39-533e337d7c28 | -22.43876 | -44.13359 | 2024-09-27 03:49:00 | NOAA-20 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 64ff06df-a1f6-33b0-8cb9-1b3edeee4ce4 | -22.43342 | -44.14205 | 2024-09-27 03:49:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b19810eb-0636-3867-a16d-08e10f6354ef | -22.43064 | -44.13646 | 2024-09-27 03:49:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 275c5366-1d94-33b2-80b8-ae1ed1d25048 | -22.11569 | -44.17204 | 2024-09-27 03:49:00 | NOAA-20 | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 94d6022b-4b4d-3a60-941c-f34aa76eaa70 | -21.65599 | -43.97109 | 2024-09-27 03:49:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1069bb93-91eb-3a46-a1b7-cca9d52334d0 | -21.65317 | -43.96558 | 2024-09-27 03:49:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0f507b98-47af-344e-8a9e-5d3bbc7c0fc5 | -21.18136 | -44.27377 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 320d3050-596c-36ba-996b-8cbc624d9c6f | -22.05331 | -44.81375 | 2024-09-27 03:49:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4a13071e-6b2f-3dd3-8650-104703b1479d | -22.01985 | -45.2805 | 2024-09-27 03:49:00 | NOAA-20 | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5f5adc56-a57b-3b2e-b1c6-b9c6aecf3cf5 | -21.1963 | -44.88555 | 2024-09-27 03:49:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a7ce8f2f-db5a-3573-8d87-8cf9bdc0fff2 | -21.19531 | -44.89081 | 2024-09-27 03:49:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6bab5cef-e74d-3a1e-a1b8-63e7be545ae7 | -21.19337 | -44.87973 | 2024-09-27 03:49:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3ccff918-14a5-348c-accd-91a57227ebfb | -22.52954 | -44.15063 | 2024-09-27 03:49:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8617d5de-fd3e-3485-872c-2acf15dc6f39 | -22.31394 | -45.47901 | 2024-09-27 03:49:00 | NOAA-20 | PEDRALVA | MINAS GERAIS | Brasil | 3149101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 23475512-80aa-3544-a7d9-3f37ed1b505a | -22.31289 | -45.48456 | 2024-09-27 03:49:00 | NOAA-20 | PEDRALVA | MINAS GERAIS | Brasil | 3149101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 88ae65fb-e990-3edc-aab0-654007cc2b96 | -22.76736 | -45.15803 | 2024-09-27 03:49:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 836c86d3-14ad-3976-85b0-6c806f6c7e53 | -22.76643 | -45.15609 | 2024-09-27 03:49:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fafec3b1-36ef-3ad6-ba26-fa385e47ed78 | -22.74539 | -44.79938 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| f5b9c8f4-1a4a-3c8e-b156-cfb538ce7cbe | -22.74454 | -44.78291 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1d3e7665-2189-34bf-b29c-ca0afb199e8b | -22.74438 | -44.80476 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| faf02ff9-c57c-35bf-b894-35e13e1f19dc | -22.74339 | -44.81009 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 63d328b0-c268-330f-8aa2-da437fb0765d | -22.74154 | -44.79903 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 52949a2b-0948-3986-8fa5-5cddbe57d118 | -22.74072 | -44.78247 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f145123a-1cba-3e96-987b-7935de5edb83 | -22.74054 | -44.80436 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| f81ea21e-69e1-3dc6-b443-9332ef823a82 | -22.73954 | -44.80973 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 332d3f6f-d62f-3cb4-98cd-7ab9aa425519 | -22.73768 | -44.79871 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| b5fb8ac6-dc6e-3035-add6-4368d73a1a97 | -22.73669 | -44.804 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 891d1712-e835-3c07-90cd-5c9c072d520d | -22.73569 | -44.80936 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 9668560f-7e1b-3c91-bd7b-80102a210e73 | -22.73483 | -44.79302 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5268978a-9982-3992-91d3-39765ef9a04b | -22.73382 | -44.79845 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 76f55efa-7895-3236-b90f-c4a3c21e6e62 | -22.73282 | -44.80376 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 146dfa96-127d-37e1-a9cf-6ce9094c21e0 | -22.72995 | -44.79816 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| aba0e0b2-72ce-3ce4-9e69-1aa2eb95aa41 | -22.68004 | -45.31877 | 2024-09-27 03:49:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 061348c6-cb5f-316a-bd31-ec3fbc8ed6cc | -22.64788 | -44.86269 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 488a412a-aa11-38f1-917b-b6e43c69a549 | -22.64695 | -44.8677 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| a932b5c3-cdaf-3daf-8936-f4b0c2aada10 | -22.64409 | -44.86192 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| ad1e8aab-6c47-3b14-bfc6-93e84b038997 | -22.64316 | -44.86694 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 5a852463-83e9-34f1-af70-8f7a816f1277 | -22.63083 | -44.86974 | 2024-09-27 03:49:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 773075f1-5e28-34bc-bce6-1a2ec9be3304 | -22.59306 | -45.2212 | 2024-09-27 03:49:00 | NOAA-20 | PIQUETE | SÃO PAULO | Brasil | 3538501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| d6772526-8acc-3250-965a-d961b7a5f076 | -22.59218 | -45.22591 | 2024-09-27 03:49:00 | NOAA-20 | PIQUETE | SÃO PAULO | Brasil | 3538501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f6c0b0a4-5eda-3288-a19a-9bf0e66df443 | -22.58837 | -45.22476 | 2024-09-27 03:49:00 | NOAA-20 | PIQUETE | SÃO PAULO | Brasil | 3538501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 65a332af-d2b8-3094-bf2f-931635f37ee8 | -22.51778 | -44.84846 | 2024-09-27 03:49:00 | NOAA-20 | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 21481fae-1ea9-38d2-9618-0582d0f22c5c | -22.90472 | -44.7387 | 2024-09-27 03:49:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| 6e649a44-15f1-36b2-b14f-39d98203bf27 | -22.90384 | -44.7435 | 2024-09-27 03:49:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| 46b7ed65-6dca-3128-b5ef-6d37e3ce337a | -9.47534 | -44.07767 | 2024-09-27 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 871e8a02-1589-313c-8c0b-a8b878a93497 | -10.59768 | -44.28446 | 2024-09-27 03:49:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 418c24ff-1160-3eee-b9b7-628abf9d5f51 | -10.59689 | -44.28896 | 2024-09-27 03:49:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98837dfc-8c07-30c5-b2d6-47e4bce498eb | -10.59321 | -44.28362 | 2024-09-27 03:49:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5cbd0691-e24c-352d-bd58-3567d1a2be01 | -10.59242 | -44.28809 | 2024-09-27 03:49:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1714938b-ed94-3c31-a156-386725ac722a | -10.29939 | -43.533 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c846feef-256e-3e84-9f46-9ea736d18f5b | -10.29798 | -43.54116 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48c15223-bfde-308c-b3e4-497ce071ba19 | -10.29727 | -43.54525 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58587fdd-507d-3fc0-87bb-7ead1196a416 | -10.29228 | -43.54855 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4fab617-f1c1-3665-b9d4-faaef3618cb1 | -10.29157 | -43.55264 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84f80bd4-d2bc-36af-9ee9-6f949d8dcad1 | -10.29155 | -43.52735 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5136ed47-88ea-3934-a922-548f21b5b05a | -10.29086 | -43.55673 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a69f9ef-1796-3b5f-a324-a04bd199ec44 | -10.29084 | -43.53143 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b50ed39-45f1-3d32-8d25-f4a5bedd867d | -10.28587 | -43.56002 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ff7d8e1-a90c-3c91-b645-34a9e7aae7d3 | -10.28516 | -43.56412 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 972f17ed-5786-3b48-a86c-5d1943ce3962 | -10.28373 | -43.54695 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cdc3adb7-ee9d-3874-9e5d-3f4bb62b115b | -10.28302 | -43.55104 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd69fcd7-69b8-319a-a9fe-f4e36f3fd87a | -10.28231 | -43.55512 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6e37c42-f569-3ecb-b815-d1514bc30813 | -10.2816 | -43.55921 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a30142ee-ca54-315b-9427-d62e037f09d2 | -10.28089 | -43.56329 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 621e9bd0-cbfd-3a65-8720-67c93d635484 | -10.27945 | -43.54618 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b18e8e81-c0aa-3b0f-b5bf-3019775a2cfa | -10.27874 | -43.55026 | 2024-09-27 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f8ad953-0cea-3699-bce3-230680303239 | -10.13604 | -43.37006 | 2024-09-27 03:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8aa593be-4388-3454-bac8-0653f923666a | -10.13537 | -43.3738 | 2024-09-27 03:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 717b9805-4a18-3a95-9e7d-32e606f2a2e0 | -10.13107 | -43.37748 | 2024-09-27 03:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a7aad24d-e007-3984-8f3d-e964c19c55cf | -10.13045 | -43.37686 | 2024-09-27 03:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1435a68f-803c-3bee-98dd-78f12431e53b | -11.48888 | -43.24321 | 2024-09-27 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4a71dff9-a40f-32d1-a854-228e4be8ea2d | -11.48822 | -43.24697 | 2024-09-27 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d2bcde9d-a159-3eed-9e48-12e1112bef37 | -11.20799 | -43.32632 | 2024-09-27 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 098b6a3a-9fe5-3b9e-9f82-7af854d84dc7 | -12.00081 | -38.16619 | 2024-09-27 03:49:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ef8f2a42-37b1-33ec-aed0-e3af560cbb3c | -11.06835 | -39.42454 | 2024-09-27 03:49:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b9701090-d9b6-3416-ae2b-c5b4f7177287 | -9.78738 | -41.77456 | 2024-09-27 03:49:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cd905d4b-a8bd-3dc5-bedd-b4a6a22c307a | -10.49421 | -42.50508 | 2024-09-27 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f580bfc5-f5b2-3b89-95ab-9e61c15367ef | -10.49359 | -42.50859 | 2024-09-27 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 57fa3a59-9108-3afc-91f3-86043e4eb0f0 | -10.49227 | -42.50526 | 2024-09-27 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2ae29bbd-f646-3c9b-85d6-435bf387dc4d | -10.49167 | -42.50878 | 2024-09-27 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a067479c-c6d9-3458-981e-bd3839715427 | -8.56056 | -49.60602 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 706a56a1-4d7a-3454-a101-ad2e34a506a1 | -8.55952 | -49.61158 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| df304e0b-f623-3b21-85f0-e4e40353f557 | -8.55922 | -49.60814 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 35a8da77-a6e4-377b-b3c5-25959b38ec7a | -8.55814 | -49.61367 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2f79f72c-9013-39ac-981e-3bbf1a857788 | -8.55298 | -49.61039 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 45cb8dad-9b36-31da-9cef-c901c25cacc7 | -8.55196 | -49.61583 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dbd0dfa6-d26a-3b68-bd41-18fd60e17dbe | -8.55161 | -49.61243 | 2024-09-27 03:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 76b42cb1-6b82-332b-b078-812280657481 | -9.60879 | -50.14396 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ed4f34e-a4f6-3487-916d-5ae149d363de | -9.60647 | -50.14125 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93839d2a-8420-3b1b-bdcf-1dc1c64d8015 | -9.6053 | -50.14703 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f91c6b2-bae7-3478-80c6-b391f2f4f72e | -9.60333 | -50.13672 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1db58d16-61e8-385c-9bec-12a6d317d11f | -9.60295 | -50.15866 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0f6a9568-1973-319c-85ce-4974a92551b2 | -9.6022 | -50.14252 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86e7ecf2-182c-3e57-832b-2eca441c0ecf | -9.59988 | -50.13984 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a79570d1-7136-3d99-bc97-b465ad3cf6f0 | -9.59674 | -50.13531 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 6877bc4b-6fc1-3fbb-bfba-7551913b645b | -9.59561 | -50.14111 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 559bd034-52d0-3f08-9d69-23da6bda8d3f | -9.59127 | -50.12817 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| e008d003-250b-3d8d-967c-daca47043876 | -9.59014 | -50.13393 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |


[Clique aqui para ver as próximas entradas](README65.md)
