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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56230a02-fb56-3211-95a0-aa746ef329ed | -11.77525 | -47.35076 | 2025-05-15 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dd3c9df-65eb-37cf-b7e0-1f4f9ed29707 | -12.14813 | -48.00999 | 2025-05-15 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3fcfd06-63df-3e47-9d6c-9b27e59d601c | -11.78698 | -47.35943 | 2025-05-15 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dfd592ef-7c8e-391b-b661-081ed40e60ed | -11.62786 | -48.47126 | 2025-05-15 03:36:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9a09643-8ab2-32d2-9a1a-1b244e6ce2dc | -13.28919 | -45.44549 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18ec0e7f-5b97-3a2d-971d-320b9ad36a9f | -10.32958 | -47.978 | 2025-05-15 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4ffd27e-c692-3e4f-ac84-462570adfa1f | -13.26828 | -45.43285 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1846f4c7-528e-316a-9ce9-250b4acda11d | -12.10538 | -44.74557 | 2025-05-15 03:36:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fe45a1d-04ae-3d8b-b760-5a81ad7ac93d | -9.65658 | -47.56033 | 2025-05-15 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a435b25e-21db-3019-bb3c-0ded090b9334 | -13.28358 | -45.44421 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b56a2fd7-6b81-394c-b39b-544f4e1ba869 | -13.28107 | -45.42739 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10bc2e37-f8f4-37d3-ad52-d05b76f7504b | -11.65197 | -48.11595 | 2025-05-15 03:36:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ed816ec0-1e22-3e14-81a9-9261d39fa915 | -11.64522 | -48.11441 | 2025-05-15 03:36:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 00c92853-4a7e-3719-ad87-f3cd39880926 | -11.55002 | -47.62134 | 2025-05-15 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b35902d2-ebe0-3f88-b1be-98ca35ffa220 | -13.2658 | -45.41592 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d2264dd-3b04-3654-bd51-bcc417ef449a | -13.27625 | -45.42216 | 2025-05-15 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a6f11a8c-842f-3df5-818d-a594b3eea043 | -20.7649 | -46.77081 | 2025-05-15 03:38:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bf7f5fa9-2ca6-3c70-bbff-9afcae76141b | -17.80068 | -44.35561 | 2025-05-15 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| caeea168-ffae-3072-95b6-a224329d4e20 | -19.15812 | -47.81789 | 2025-05-15 03:38:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c8bab3eb-1d56-3fe2-b423-539052251ab2 | -22.24802 | -50.36327 | 2025-05-15 03:38:00 | NOAA-20 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.9 |
| b32bee48-dcaa-36c2-a359-1fdd013611bc | -17.80436 | -44.36236 | 2025-05-15 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 307fa662-c1a3-3f25-849d-fef9489b631e | -17.80547 | -44.35684 | 2025-05-15 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f48b821-bdc0-389f-b7d2-941bd159923b | -19.15703 | -47.82278 | 2025-05-15 03:38:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4b226b5-e738-335b-9856-1aa81aaac8bc | -22.2494 | -50.3576 | 2025-05-15 03:38:00 | NOAA-20 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 11ce8c20-1477-3669-bc12-dc503d0bda3d | -22.25078 | -50.35199 | 2025-05-15 03:38:00 | NOAA-20 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 61fa7311-fa3f-3ff8-837d-eda0ac8b07c1 | -20.22886 | -46.75352 | 2025-05-15 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d935a20-926b-3c23-aeb4-758d3c4e4926 | -23.33677 | -46.77253 | 2025-05-15 03:38:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| af1616c2-91b8-35b4-b429-9d4aade7b351 | -17.84317 | -40.42392 | 2025-05-15 03:38:00 | NOAA-20 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b2233324-2f10-36bc-82c2-c354a297c9dc | -15.76792 | -47.15263 | 2025-05-15 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a56d751b-2fb0-3831-b669-95b9dbca39e9 | -15.76686 | -47.15749 | 2025-05-15 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8863af89-b4c4-3584-8c97-d4224d65aef3 | -23.6077 | -48.295 | 2025-05-15 03:40:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9b0a4a3e-7b0a-3000-ba71-876f3304403d | -23.40495 | -46.55381 | 2025-05-15 03:40:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7dec0d26-8744-3200-af63-47dd991209ed | -23.60229 | -48.29334 | 2025-05-15 03:40:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d21beec1-2f7b-388d-a1f4-6ec2b765dfcc | -6.5631 | -51.1126 | 2025-05-15 04:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| d47447ee-da33-311c-9cf9-31161bba790c | -6.65027 | -41.989 | 2025-05-15 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 477277a1-ccbc-39cd-aef6-1a4704853fb7 | -8.38859 | -44.03774 | 2025-05-15 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d95b4420-78f5-3020-a7fa-a6b8d9a9cfc8 | -5.73923 | -47.98843 | 2025-05-15 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c0f3879-0408-37e7-84a5-914468198ea5 | -8.58269 | -45.89331 | 2025-05-15 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42a17a5b-16da-3817-bba6-56af60704607 | -6.55219 | -44.49974 | 2025-05-15 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee6eb7c9-b985-35b1-92a9-677424b370e4 | -5.57839 | -42.929 | 2025-05-15 04:25:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 534de7f5-911f-3cc3-807f-881fb7a32159 | -9.66294 | -47.56072 | 2025-05-15 04:25:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e45dbb72-8323-304f-a476-8741e9eea27f | -9.65963 | -47.56019 | 2025-05-15 04:25:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a1248fc-f346-3003-95fc-b12f32fcc8e1 | -8.7212 | -47.98028 | 2025-05-15 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 836a8453-73f3-3fca-8c5a-8a46d564ca78 | -5.76494 | -43.4961 | 2025-05-15 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac8b2070-df2d-3011-93ec-789215642985 | -9.31721 | -44.83262 | 2025-05-15 04:25:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e4db860a-4682-3e02-95b6-aa25f48db3e2 | -7.33133 | -43.29108 | 2025-05-15 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee8bac7e-74bf-3570-a0b5-ede97918f86e | -9.36637 | -48.39798 | 2025-05-15 04:25:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 040e076a-82b8-3d87-afb9-ff94298f2025 | -6.18013 | -48.06487 | 2025-05-15 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef071548-c991-3966-94b4-0ed5ba969448 | -7.07389 | -44.38853 | 2025-05-15 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12ef2335-489b-3b9e-b647-01866ce52c4b | -7.95133 | -49.76479 | 2025-05-15 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d062c29a-de65-3569-9610-ed583b4439c9 | -8.89322 | -44.7852 | 2025-05-15 04:25:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f26f344-d431-30c9-91b8-929c1adeff9b | -6.75399 | -44.53398 | 2025-05-15 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cb4c8f0-f749-308e-b881-c27f020ca19d | -7.80099 | -45.34094 | 2025-05-15 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48f5cecc-bfcc-39e0-ab2b-1b8b82532f9c | -9.61918 | -40.34642 | 2025-05-15 04:25:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d6d16740-66e0-37c2-ba17-b3614cf6a749 | -6.17214 | -48.07121 | 2025-05-15 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2adbc2f5-15f8-3c71-85eb-0a9872387ace | -8.58323 | -45.88979 | 2025-05-15 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88cd876e-eda5-34a8-b1b3-1e8d4af8d5b1 | -8.80227 | -49.82099 | 2025-05-15 04:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5cc061d7-1ee2-34db-a54d-2f9a1e1d3c39 | -6.17555 | -48.07173 | 2025-05-15 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4e963e3-f76e-39f8-9d96-004f0dc7f139 | -7.36725 | -39.1813 | 2025-05-15 04:25:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9e383aea-a9fd-3232-acb0-0f40690d0464 | -8.59043 | -45.88728 | 2025-05-15 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f21dcaed-00de-3c0e-9722-8ff4ee3e67fb | -9.66018 | -47.55669 | 2025-05-15 04:25:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30dbeb1c-9aa2-3913-ad51-99437dc5e9df | -6.55671 | -44.49285 | 2025-05-15 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb8c389c-ea7b-30f7-89ae-f09bdd10de04 | -6.75344 | -44.53767 | 2025-05-15 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81468ea2-4408-31b7-809e-5dbd962ff9d5 | -5.78721 | -43.61831 | 2025-05-15 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65910852-9a05-36e8-83da-473196a568f6 | -8.59097 | -45.88375 | 2025-05-15 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 62774661-c658-3506-8374-3f7a580f324d | -7.36793 | -39.17645 | 2025-05-15 04:25:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 075d00b5-b31f-3aa0-9a9b-f64bc81b93b9 | -8.43275 | -46.64006 | 2025-05-15 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1578dfb-885f-36e9-be26-0928cdd97fa1 | -8.59261 | -45.87321 | 2025-05-15 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aa796d6-c9ec-3e57-a2d5-cd4b59bbb0a8 | -6.55559 | -44.50023 | 2025-05-15 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c4a878e-f464-3c0c-b8ed-f2ae8c428753 | -8.58711 | -45.88677 | 2025-05-15 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b9fc744-0614-3db7-9570-4decf78b0c22 | -8.33903 | -55.09589 | 2025-05-15 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 216c8e34-1fd2-3732-b0af-c08223264dcd | -8.79803 | -49.8245 | 2025-05-15 04:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c1920f7-fdd3-3c98-8cba-353d02b8c9d5 | -6.94033 | -42.80267 | 2025-05-15 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e9688c12-c221-3e2a-b6a3-4af1d12900d4 | -5.78551 | -43.61914 | 2025-05-15 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85a5e157-5b75-3fe1-8d1f-6989e0699801 | -7.30697 | -43.35531 | 2025-05-15 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edb6937e-9538-30e9-a505-ab431c2198c9 | -6.66073 | -43.19799 | 2025-05-15 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 150509e6-ffc1-30c3-a261-289e979578ba | -6.17954 | -48.06855 | 2025-05-15 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5ef67f54-129c-3bb7-9c84-975a840af4a7 | -9.61681 | -40.34428 | 2025-05-15 04:25:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7588d02b-6c56-3464-9454-1a59d8c68251 | -7.24571 | -39.17721 | 2025-05-15 04:25:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f09b2fae-8dd2-35f7-8e05-e2eeea7ed84c | -9.32064 | -44.83315 | 2025-05-15 04:25:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b7287b73-e78f-37fb-bcaf-11fbf67f39ca | -5.39794 | -46.96036 | 2025-05-15 04:25:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b89df625-1d41-396d-bef9-3082401b7171 | -8.58656 | -45.89029 | 2025-05-15 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56286cf5-72b3-3caf-9939-a58c628394cf | -8.72234 | -47.97316 | 2025-05-15 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15790f6a-1fd0-3965-9bdb-16e5be7cd14c | -9.48009 | -40.32167 | 2025-05-15 04:25:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 58fc6e55-f6d2-330b-a819-601ce003198e | -8.59152 | -45.88024 | 2025-05-15 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a25975e6-a1eb-32b1-bc84-c110e313a12f | -7.07617 | -44.39651 | 2025-05-15 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f6ecda8e-93ff-3791-87ed-18b550ac9560 | -6.6534 | -41.99438 | 2025-05-15 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| f270180d-2f83-39e9-b32a-dc16ffccac22 | -7.95201 | -49.76063 | 2025-05-15 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 69fc5e91-17e1-394c-abc4-70ca775582f4 | -6.17332 | -48.06379 | 2025-05-15 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| ec7620ef-457f-3418-a069-5f7d28d1358a | -7.94773 | -49.76423 | 2025-05-15 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 193201b4-56f8-360a-bc26-c782e6b88a41 | -6.80897 | -40.58577 | 2025-05-15 04:25:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5f815da0-24d0-3cd9-9799-7b9fef330662 | -6.55274 | -44.49605 | 2025-05-15 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35b82fe1-9576-320f-bcd9-47734332c893 | -8.59206 | -45.87672 | 2025-05-15 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1e37768-1fba-39e7-b0a0-1888bdbc6e84 | -6.18435 | -48.06517 | 2025-05-15 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d88a869-6a42-3940-9746-35db9927080e | -5.67287 | -45.22475 | 2025-05-15 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2c6c3fb-307a-319a-a165-78b75bd5c7b3 | -9.65907 | -47.56369 | 2025-05-15 04:25:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e506cae1-021a-31c0-bb1a-880a56c92786 | -10.82607 | -37.16689 | 2025-05-15 04:25:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b7cb8dc7-f54f-33e4-abc7-71f1fda5c424 | -8.334 | -55.09502 | 2025-05-15 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2d69e7d6-4e10-3148-8aca-b63ca4aa0186 | -7.80154 | -45.33738 | 2025-05-15 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11833c5b-1625-31bc-a356-ccc37efd8829 | -6.17273 | -48.06749 | 2025-05-15 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README5.md)
