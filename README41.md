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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88e9ae65-edf1-31bb-87b8-4166f84487e5 | -16.01375 | -59.46582 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e8f0277-76de-36ae-a042-f470f1abccf5 | -15.95506 | -59.37759 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc7dab21-1b56-3ed5-b1a1-1f85924aad9c | -16.00604 | -59.47375 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d262c7b4-cc1f-3a8a-b40a-da634cc7ba0e | -16.00657 | -59.46893 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41338fa4-b2fc-3d86-9de5-5fce81eca8e1 | -11.79206 | -64.92918 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ac7ce861-1098-3a5a-ba7d-4a3270bd6fad | -16.00769 | -59.46527 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0795721-ae5d-37bf-bce0-07d0975da767 | -16.0072 | -59.47004 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 486d94d9-20ba-39dd-9741-b62890766dc7 | -11.78808 | -64.92863 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9c8ca8b-7445-3a65-a298-adc5f9439e5c | -15.95454 | -59.3825 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5d5d1ff6-f202-32db-b6df-a30a7418208d | -15.83444 | -59.51787 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fb8ab93-1705-3101-b59f-8c3a8c73e6b5 | -11.88231 | -64.93861 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37d3bc45-d0eb-3e96-a0ed-78a3c98c58b7 | -15.96116 | -59.37806 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01047cea-b22c-30b9-ac0e-ca6098110da4 | -16.01326 | -59.47058 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 747e2623-3a0a-32a8-90a1-ed695e495846 | -11.87361 | -64.94263 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7a19ada-5af1-3363-9d7e-644582b11abd | -12.40173 | -63.8879 | 2025-09-22 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f97b7430-3374-3c6f-8e67-d186080e2e61 | -11.8711 | -64.93168 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2212048e-80ec-3325-8b3b-2a7e8ada8a0d | -15.95352 | -59.39215 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16e88134-f0cf-39a9-adc4-12907c7be795 | -11.88305 | -64.93342 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8508cd38-bef8-35a0-8745-f855ca8fbac0 | -15.8414 | -59.50976 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f04ebcbd-dceb-367f-a036-3eba792de7b8 | -15.9521 | -59.40555 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da6237e6-8318-34fa-a3f0-0ac10b7ee4d1 | -16.00072 | -59.47346 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e7a4e3d-3c29-3543-81e6-faf536a7ed65 | -15.94654 | -59.40009 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39918440-1879-309c-a7a0-cfc04d79e364 | -15.94743 | -59.39156 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31bd303c-8d1e-3d27-8e59-49b9eb8a982d | -11.87833 | -64.93803 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| deb1fc84-c0c8-3a03-95f2-66a1d30a3b45 | -15.94695 | -59.39619 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcc4fb3b-400b-3b77-b6c9-3c13e6295598 | -11.86565 | -64.94146 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d605caf7-8108-3d65-b114-9b0fce3ad3d1 | -11.87759 | -64.94321 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e90858a-af3d-3ebe-b103-31f72f7e0f03 | -11.88157 | -64.94379 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 457669f1-be4a-39d6-96ef-2ea9032249ac | -11.79402 | -64.93093 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f28c680e-9871-3cf7-8a10-9430277830e9 | -16.02026 | -59.4621 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4965301-d61f-3729-9300-b3f903b2681d | -15.77152 | -59.41269 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7728c52-7886-30e5-947a-11bc30318200 | -15.95405 | -59.38715 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 175dcb5c-88d5-36cc-8cd5-c9683f50eac0 | -15.94796 | -59.38655 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4796750f-96fd-3344-9797-d2b01106b652 | -15.83485 | -59.51407 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62a68342-ba72-3f6b-9b3d-ec2ae03f3244 | -15.84051 | -59.51812 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8529fcc-0d2e-3d78-ba37-8bf519abc046 | -15.83527 | -59.51015 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a039ab67-d5d8-30ca-895a-3da20e41edc5 | -16.00207 | -59.45414 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6f8a129-851a-346e-9370-c8034612342d | -15.96728 | -59.37835 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50e49589-66e9-31b3-aa02-2bee2782ce8e | -11.87906 | -64.93284 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b36fa13-0e5f-32d6-b4aa-401ff2a6cf78 | -16.00306 | -59.45076 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9596206d-1b02-36d2-bb8f-027ef5d4c7cf | -16.00007 | -59.47234 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac511d8f-2347-3164-b115-2003c5cfa74b | -16.01316 | -59.46473 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ec672b1-b019-3e32-9991-db9c3a9f5784 | -20.2537 | -55.4959 | 2025-09-22 06:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 59fd1052-e48a-31ff-83d3-badf443360bb | -8.00169 | -45.71919 | 2025-09-22 06:01:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 28a90a9c-f2dc-35e3-8310-ab1c7aa6fee3 | -12.97464 | -46.38056 | 2025-09-22 06:01:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d67ed960-269a-3e39-aa01-d0dfba8eff28 | -8.58784 | -45.31734 | 2025-09-22 06:01:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8a63e642-57ef-3048-a169-176a63c28dde | -5.647 | -51.4662 | 2025-09-22 06:01:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fc7771cf-3ad6-31e1-8a1e-e1146177683b | -8.59758 | -45.31862 | 2025-09-22 06:01:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 5437b151-a92c-3401-abdb-6033cdc6ccc2 | -12.97614 | -46.36955 | 2025-09-22 06:01:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d64a60b3-e890-3cf5-9dd3-a15fe1764a3a | -12.9858 | -46.37099 | 2025-09-22 06:01:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 4e23d11b-5918-373d-a849-e56f3db1c607 | -11.76905 | -44.88026 | 2025-09-22 06:01:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 78a8c206-a6d2-3a76-aecd-bb54f67d9ea8 | -11.7673 | -44.89302 | 2025-09-22 06:01:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7550ff50-32dc-37b5-b6a9-5776afa54656 | -12.98429 | -46.38197 | 2025-09-22 06:01:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 0c11077c-31e0-3b72-b0c5-90ccc2966ce7 | -8.59915 | -45.30779 | 2025-09-22 06:01:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.6 |
| c5fd8d3e-8c31-3d02-9d8e-609ab2080370 | -11.62629 | -52.84962 | 2025-09-22 06:01:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| d6476813-30d7-3223-9c8a-ed5739a438c0 | -8.58941 | -45.30645 | 2025-09-22 06:01:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ab776941-62af-3836-90fa-67b53a6b3c70 | -12.70731 | -47.70283 | 2025-09-22 06:01:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 82904baa-4cad-3cdf-8ca2-fcb5ea229515 | -5.65083 | -51.46111 | 2025-09-22 06:01:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9f499cfc-5b74-30aa-a3f2-8e0976fca8bb | -11.63673 | -52.85135 | 2025-09-22 06:01:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| d410fb53-9642-3892-9f1c-07a39c938a66 | -12.70867 | -47.69338 | 2025-09-22 06:01:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8f102c82-a3fa-3f87-a646-413e08eade0d | -12.07896 | -44.79256 | 2025-09-22 06:01:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f8c132c5-ba4c-3d79-a543-c378a74b3ed6 | -12.0648 | -44.81693 | 2025-09-22 06:01:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 93b0d41b-7009-3db1-a778-9d99681ce8f4 | -11.63884 | -52.83862 | 2025-09-22 06:01:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| d754b0fd-77b1-3f89-bc0a-3ad2c3400445 | -19.8467 | -57.29174 | 2025-09-22 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cdc79f8b-0756-38b2-a39d-422e59bd3373 | -19.85386 | -57.29237 | 2025-09-22 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d525e0f6-b17e-3b20-a220-606f364f9689 | -20.37209 | -58.0617 | 2025-09-22 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d3168d40-d299-3d41-afa3-853c792c5a5b | -19.84996 | -57.29153 | 2025-09-22 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 5c1e9b29-c1ea-3e2e-a7a0-c5abc3160fe7 | -19.64338 | -57.73894 | 2025-09-22 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 1a47d7fb-dc5f-31ce-8322-59738bd53e4d | -20.37156 | -58.06825 | 2025-09-22 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e634401d-f619-300a-b7b1-f7ac7abd369e | -19.65035 | -57.73962 | 2025-09-22 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 08a3bf1e-702c-3b9c-b9cb-bedfea283e84 | -20.38587 | -58.06295 | 2025-09-22 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0f2c8feb-5d00-37ff-850c-fc59ef49aaa0 | -20.3864 | -58.05637 | 2025-09-22 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 736a1341-0140-3852-b224-8997650d8195 | -20.37898 | -58.06232 | 2025-09-22 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 64f5d154-8682-3a60-8295-4c6d4af41264 | -19.63642 | -57.73825 | 2025-09-22 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a64b82ae-7964-38dd-b328-f04f9f567208 | -20.38657 | -58.05878 | 2025-09-22 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 0033176b-b22d-3c8f-b4c9-fe2b697ddd04 | -15.24864 | -43.07986 | 2025-09-22 06:03:00 | AQUA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 3d15bc54-736a-3d9e-a00f-6da732c99d90 | -19.86844 | -46.09852 | 2025-09-22 06:03:00 | AQUA_M-M | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 98036531-9ec4-3545-a1e7-ef0934623f4e | -14.43774 | -46.51806 | 2025-09-22 06:03:00 | AQUA_M-M | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a12539ef-a58b-3450-b57f-2ca7831f0be1 | -15.25 | -43.07291 | 2025-09-22 06:03:00 | AQUA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 692ccef4-9168-362f-ac0d-2ac3e036ef4c | -15.03762 | -55.28437 | 2025-09-22 06:03:00 | AQUA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 571ce2da-3ac6-32dc-b75a-c26ecd47e9bf | -15.0119 | -49.54842 | 2025-09-22 06:03:00 | AQUA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9bcc05e4-60a6-3408-8eae-7bad8224150a | -14.40047 | -48.55135 | 2025-09-22 06:03:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ee9c7f78-be42-3597-9266-36d75059d4ea | -20.66158 | -54.48772 | 2025-09-22 06:05:00 | AQUA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 295f5969-a2f5-377b-8d9a-a8a74fbb7f13 | -20.26718 | -55.5015 | 2025-09-22 06:05:00 | AQUA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 0682b5cd-143a-3fec-bbca-57bb763a9da7 | -20.25896 | -55.48505 | 2025-09-22 06:05:00 | AQUA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e62a3fed-a64c-305c-8554-bbf0bc19b277 | -19.84532 | -57.29457 | 2025-09-22 06:05:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 85df6708-6616-39b7-9e00-0aac3adc3aad | -20.40203 | -54.85895 | 2025-09-22 06:05:00 | AQUA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 181ac4ce-9b30-3e48-912b-04ff7602b5bf | -19.6398 | -57.7392 | 2025-09-22 06:05:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 319f12fe-606b-34c7-b448-db2952f42b03 | -22.30049 | -46.69667 | 2025-09-22 06:05:00 | AQUA_M-M | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 7240c9b7-817d-318c-b2af-2dd9c5f6b1e4 | -21.1924 | -48.82786 | 2025-09-22 06:05:00 | AQUA_M-M | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| c91e5bfb-097e-3e41-b6df-a46f7c6d07a2 | -20.25639 | -55.49932 | 2025-09-22 06:05:00 | AQUA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 6c2116ac-9b24-36de-988c-1a4def816650 | -21.83528 | -53.94399 | 2025-09-22 06:05:00 | AQUA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5569c5ca-614c-30a4-b0be-5ae05111bf8c | -21.8334 | -53.95515 | 2025-09-22 06:05:00 | AQUA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 946e0357-72e9-37e1-b195-febe1460555b | -19.64349 | -57.73259 | 2025-09-22 06:05:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.8 |
| 0ef5d8be-f032-31be-bd99-84e81460e6db | -22.30425 | -46.68944 | 2025-09-22 06:05:00 | AQUA_M-M | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| e7bd87c7-c126-311f-a305-09e9101d7349 | -20.26974 | -55.48719 | 2025-09-22 06:05:00 | AQUA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c9882531-61bb-3eff-985f-bc6ce3afb90a | -20.274 | -55.4927 | 2025-09-22 06:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 9cb7147a-25f5-3577-bc80-c2dd9fe72ccc | -20.274 | -55.4927 | 2025-09-22 06:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 98.6 |
| afcfe908-17b9-30e2-a6ea-e1d0a8dbd9db | -9.24694 | -67.39027 | 2025-09-22 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e93c35ac-f81b-366f-9803-46635f1b7919 | -10.19861 | -69.09146 | 2025-09-22 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README42.md)
