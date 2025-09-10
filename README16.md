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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43e30d60-d256-3e4c-a580-c045b9f04f61 | -13.8252 | -43.86242 | 2025-09-10 03:23:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5954e310-1112-3e6f-84e0-79be68931ca6 | -13.76098 | -43.61847 | 2025-09-10 03:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d2fcfe8-4b9d-3485-b467-dd7d43af0638 | -12.41363 | -44.7249 | 2025-09-10 03:23:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd016ad0-f961-3a3e-88d6-8a5fb8ade0c5 | -11.42575 | -43.58381 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 789748fa-4a20-3157-bbb9-faa110e32250 | -11.57316 | -44.6643 | 2025-09-10 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbd39a8d-2be9-3258-9710-22b546a62222 | -11.39165 | -43.54222 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d88fb7a-6693-3332-9151-d4925b084b21 | -11.12211 | -45.1166 | 2025-09-10 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 86ee2d8d-ec73-3e4e-b5e0-bead7c007bc3 | -11.44431 | -43.60585 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c86b1b6f-6f8e-3c5d-b610-84174917fb53 | -11.44144 | -43.60305 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11c0ca6e-715b-3d9d-a6c6-c6d01314f638 | -11.43726 | -43.59149 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab20c7eb-ccf8-3883-8642-31a09d6ce040 | -11.43394 | -43.62536 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d8dd484-123f-3c6a-8600-5478d7a6fcd5 | -12.41236 | -44.73094 | 2025-09-10 03:23:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c00ed524-cd38-3ae1-b6e7-5fa6b811575e | -13.75495 | -43.61715 | 2025-09-10 03:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d46625d3-623b-339e-953a-e3be91c6a679 | -12.02063 | -45.86374 | 2025-09-10 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e16f801-639f-3cfc-9773-e5af2f643974 | -11.43288 | -43.63071 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54f50189-3097-3891-8f71-23c15a904906 | -11.87767 | -39.56793 | 2025-09-10 03:23:00 | NOAA-20 | PÉ DE SERRA | BAHIA | Brasil | 2924058 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 105e3736-3611-3bc6-b5d8-e66c5820d799 | -11.45189 | -43.61601 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| de94d251-4bb9-3da5-a69a-3dbcd5e442f1 | -11.43926 | -43.64594 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3a5acd9-43bd-3ea5-aa6f-8b3c0e7a473a | -11.38016 | -43.53449 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9eaea2e1-7290-378b-a0ab-32c7c98d0f50 | -12.02436 | -45.86295 | 2025-09-10 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f3f2f2b-ea41-35ed-b87f-933cf5ee0cd9 | -11.44354 | -43.62489 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a3a9895a-75ee-3fa4-9089-13e44bed8535 | -14.0925 | -42.09319 | 2025-09-10 03:23:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cae33421-715f-3f17-b7b1-4370d01f5ee4 | -18.02167 | -47.14837 | 2025-09-10 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 0f205813-5216-3cf1-b78c-a201c319322c | -19.29857 | -47.98817 | 2025-09-10 03:25:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb741cb4-ff47-372e-816b-0e9c331fbeee | -17.74429 | -44.48221 | 2025-09-10 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9d8e775-805b-3325-bdda-954b2a64b109 | -16.28894 | -45.68909 | 2025-09-10 03:25:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 594b31b5-e168-3da4-8dcf-591a04dc46ec | -20.37369 | -46.64058 | 2025-09-10 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a1c12aa-ade8-3be9-9e49-0a8d8c93dd07 | -19.64457 | -45.04049 | 2025-09-10 03:25:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d72661df-ff82-3ed5-87f2-3407078d610e | -18.52033 | -43.28299 | 2025-09-10 03:25:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8d0c0588-1fb5-3e93-92c2-a66c02070c18 | -14.74717 | -45.335 | 2025-09-10 03:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e72b0d6-3e02-31b9-a73e-99f59db73439 | -21.39751 | -43.8771 | 2025-09-10 03:25:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b0729e69-68c0-32be-ae9d-244bbb0ec247 | -20.01015 | -47.62753 | 2025-09-10 03:25:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 79219651-562d-33c2-b46c-63050cfd00de | -20.11104 | -47.83263 | 2025-09-10 03:25:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5624d4e1-9e34-3f8f-9119-2e4f28ceff41 | -22.02458 | -42.90054 | 2025-09-10 03:25:00 | NOAA-20 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f2b55ee4-dcac-3b8c-a88b-2d8eb56a91be | -16.56639 | -41.64889 | 2025-09-10 03:25:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8f6091c5-b9b5-3c4b-995b-e006b0371d36 | -19.6367 | -45.04799 | 2025-09-10 03:25:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 24de232b-eac7-3c8b-bf59-5bc40d87beaf | -20.10433 | -47.83054 | 2025-09-10 03:25:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d429ead2-6f07-33da-bca1-7a5ec851b186 | -17.71564 | -44.44382 | 2025-09-10 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2562cf0d-c5c9-31ef-8d00-83d1a0f9bf8d | -20.28208 | -46.25081 | 2025-09-10 03:25:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fd6c48a0-5e17-3e0a-98a1-a949f3be9c5c | -19.16918 | -43.06329 | 2025-09-10 03:25:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 51d38966-0387-3978-9e5b-067ef4dc5f67 | -18.45853 | -46.47476 | 2025-09-10 03:25:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1693c0c3-6918-31c4-a6ae-2e2eb9a121dc | -17.73979 | -44.48802 | 2025-09-10 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb419e7f-b33a-38c8-aec8-f8707faaa51f | -21.11985 | -47.7396 | 2025-09-10 03:25:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 261f2754-450b-356e-9624-cfb56ce406a0 | -14.59985 | -43.92728 | 2025-09-10 03:25:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e881e1f0-946e-3d79-a410-3aa4b455de7e | -20.3749 | -46.63058 | 2025-09-10 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e8fecf7-c69d-3387-b36d-c3f77b5bb140 | -20.00795 | -47.63069 | 2025-09-10 03:25:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| bb97d790-8345-3db8-96a7-23b3340bd8fa | -20.01573 | -47.62812 | 2025-09-10 03:25:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccf08cc4-0459-3ebc-90d4-1189690e93b0 | -18.02723 | -47.15533 | 2025-09-10 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 26.0 |
| dd6174a0-0deb-3982-a0a9-dd4a4e88a17a | -21.58339 | -43.97384 | 2025-09-10 03:25:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 20cacea9-a7e2-325c-a873-f315dc5455e7 | -17.74302 | -44.48797 | 2025-09-10 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5387f86e-e8dc-3be2-9445-e4d285ed4b19 | -19.77536 | -45.79186 | 2025-09-10 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4beb7e18-fc83-3084-ab54-fbe566ef6642 | -17.29787 | -46.72703 | 2025-09-10 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cf2e582-9e4b-32de-8bce-4bf4f97493ea | -20.51231 | -47.64308 | 2025-09-10 03:25:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd11fdcb-f2d7-3c50-b7be-ef3c95dac233 | -20.00311 | -47.62114 | 2025-09-10 03:25:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1dae20cb-c534-3437-bff3-ce4902a39673 | -18.46404 | -46.48077 | 2025-09-10 03:25:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 69e916f9-d574-398f-b7f7-99b61143c94a | -18.52217 | -43.27873 | 2025-09-10 03:25:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d8692218-9974-38c3-a844-1c2cf1b192fe | -19.74723 | -45.72195 | 2025-09-10 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e07ad1e-ce05-3b3e-b31e-2e862f3126ca | -21.12411 | -47.73852 | 2025-09-10 03:25:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf8e0c63-fe90-3c2b-8a2c-cbf5a46a2452 | -20.01435 | -47.63384 | 2025-09-10 03:25:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4ea1a15-b0b7-306a-8889-6b1680be80ec | -18.03006 | -47.14337 | 2025-09-10 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| e51f3a94-cfa8-3f06-b422-8cc29d1d24e1 | -19.34851 | -47.45541 | 2025-09-10 03:25:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d5ad71fb-de68-3be5-bdb2-d8b9fa533032 | -20.10943 | -47.8103 | 2025-09-10 03:25:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b8806db7-43e2-391d-a67b-cd28e5f76210 | -20.11107 | -47.80366 | 2025-09-10 03:25:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d0da462f-9802-35bf-b6f9-a0d3f3f98aa8 | -17.30155 | -46.74633 | 2025-09-10 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72f8c853-d4e6-3e68-a42d-41c7baac4126 | -19.30081 | -43.25814 | 2025-09-10 03:25:00 | NOAA-20 | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 141e5f78-df41-3125-ab91-0750af0eefba | -17.32508 | -46.70152 | 2025-09-10 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 679c1183-519a-3ff5-9b53-f802986686c4 | -19.63768 | -45.04358 | 2025-09-10 03:25:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 46a260ff-9224-3c4f-aa1e-80e3fff96c52 | -17.7384 | -44.49456 | 2025-09-10 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79d5b73f-b25b-3758-acb8-deb9986270ce | -20.11754 | -47.69019 | 2025-09-10 03:25:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c0bb162-80c0-32af-9353-96602016c34f | -18.02871 | -47.14907 | 2025-09-10 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 41d63471-3832-340b-bcc3-37ed491d2d99 | -20.15258 | -43.66214 | 2025-09-10 03:25:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e0f2a48d-62b9-34fb-8665-8a773bd419ae | -20.37272 | -46.63986 | 2025-09-10 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9380c90e-0d22-3cc4-b601-5e1b13fee65b | -20.10616 | -47.82354 | 2025-09-10 03:25:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8fe4a24e-4744-3427-86c5-7a3861e6bf93 | -20.00646 | -47.63688 | 2025-09-10 03:25:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b47123d5-82ad-3116-a03a-a7d54d9ad291 | -21.30757 | -43.89118 | 2025-09-10 03:25:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7c67191d-d1bf-3f93-8856-e2a6dc2ecb29 | -21.31289 | -43.89244 | 2025-09-10 03:25:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 311c17f5-0ec3-30ee-9943-37075ce8b91d | -17.99999 | -47.11683 | 2025-09-10 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5647576c-3e9d-384e-9f09-1f6db05e4eca | -19.34854 | -47.45855 | 2025-09-10 03:25:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5183e9e-4434-3c63-873d-b278d37fc72e | -21.02301 | -48.4218 | 2025-09-10 03:25:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 80f43609-5056-3cbe-b2b1-cb488f23e271 | -20.38152 | -46.63596 | 2025-09-10 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fafd665-d370-3cf9-a43e-6cfd3607a23c | -20.16427 | -43.66021 | 2025-09-10 03:25:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ac35cc35-e867-38ac-95ca-4fa4ccea2035 | -20.06407 | -47.54532 | 2025-09-10 03:25:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c29a2810-976c-3649-b2b6-0d95bd2bdf63 | -18.95673 | -42.3931 | 2025-09-10 03:25:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 13430dda-325d-35d8-948a-528b45e6cdf1 | -19.6426 | -45.04935 | 2025-09-10 03:25:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7b3d0e8f-06c5-3f1f-9cf2-8c7e5c5eeb5c | -17.23638 | -46.07813 | 2025-09-10 03:25:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b728b4f5-b700-372e-91c0-a4598ed73919 | -17.7768 | -46.14035 | 2025-09-10 03:25:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de4fb828-07f1-3f4e-a22b-a8c643649e69 | -20.15334 | -43.65862 | 2025-09-10 03:25:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 93600d51-8bda-376d-8d49-f8bfc9126581 | -18.02035 | -47.15394 | 2025-09-10 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6693fa85-04e0-307d-93f9-d074aead8a76 | -19.6865 | -46.17702 | 2025-09-10 03:25:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da8685e8-ca37-32dc-a124-db2b5ea816ba | -20.38056 | -46.63503 | 2025-09-10 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 875b50b6-e3ec-3b12-aefe-784c9fe54d5e | -20.51888 | -47.64522 | 2025-09-10 03:25:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d805ac73-e75a-321f-862e-8cd750826033 | -20.06709 | -47.54122 | 2025-09-10 03:25:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2435e31d-57a0-3134-8b0c-e4d04710f7dc | -22.02951 | -42.90169 | 2025-09-10 03:25:00 | NOAA-20 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1e3e0d1f-0879-3e8b-a18d-8b9bcf61a014 | -20.99059 | -47.99519 | 2025-09-10 03:25:00 | NOAA-20 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2a60a5c-b3e0-3b6b-adfc-2620c9bd2e1f | -21.50433 | -44.78956 | 2025-09-10 03:25:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 0065fc6c-f0d0-3dec-8c52-0c8722d530b4 | -19.48922 | -45.30517 | 2025-09-10 03:25:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f969976-63e7-34bf-af86-60aa0d287b11 | -20.53914 | -47.67865 | 2025-09-10 03:25:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec477618-6bfb-34f2-b17d-d6cd3a0d0392 | -21.12142 | -47.73327 | 2025-09-10 03:25:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27e57b09-fc67-3516-92a7-311691c60612 | -18.9522 | -42.38939 | 2025-09-10 03:25:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e77cdda7-ea6a-300f-b40e-afd88500c8a7 | -17.23446 | -46.07816 | 2025-09-10 03:25:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README17.md)
