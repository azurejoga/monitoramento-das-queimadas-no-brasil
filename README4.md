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
| ff07c94d-ff56-3af7-b1d8-400dc1cca26b | -5.58915 | -39.53502 | 2024-12-28 00:26:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ee1b08e3-1317-30b4-ba2c-ac550157d954 | -4.74458 | -44.65635 | 2024-12-28 00:26:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 87aeeeed-f1bf-3d74-ba26-7fe057e8247e | -5.4313 | -44.83351 | 2024-12-28 00:26:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 74629e31-497f-3b37-b5de-5948ae5b6b87 | -9.40112 | -35.70164 | 2024-12-28 00:26:00 | TERRA_M-M | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 52.1 |
| 6d574d5e-a735-330c-89eb-64870b957383 | -8.04907 | -41.17785 | 2024-12-28 00:26:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6c784c34-1d9f-3c9a-8766-3c0d4f210aaf | -10.75646 | -37.15432 | 2024-12-28 00:26:00 | TERRA_M-M | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 41.6 |
| a24c9f6e-70c6-33b9-9d93-e23f374d6edb | -5.58859 | -39.54101 | 2024-12-28 00:26:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ee8a8cd4-e5d0-346b-873a-cf1ab6a663a0 | -4.7387 | -44.66352 | 2024-12-28 00:26:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 005e7866-b2f2-31f9-abf3-7dc7181db7a5 | -11.24403 | -44.4831 | 2024-12-28 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4cce706b-47de-3ae8-9998-32a8e7ad7728 | -5.21929 | -41.2357 | 2024-12-28 00:26:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 348e4699-1529-3961-afe0-5d1fe4e6dea2 | -5.32087 | -46.07059 | 2024-12-28 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9ac62be1-7c2c-3bdb-8579-8e25b6314045 | -5.24159 | -41.39288 | 2024-12-28 00:26:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| f5fbe78a-1d84-35a7-b12d-45c15d17c63c | -5.71404 | -43.26116 | 2024-12-28 00:26:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0ad746bf-339b-33eb-b88f-fbb51109af9c | -4.28696 | -41.81113 | 2024-12-28 00:26:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ae6e87b9-1237-3817-bf14-4334fb8179d9 | -7.73017 | -40.17601 | 2024-12-28 00:26:00 | TERRA_M-M | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 8d567f8a-7844-3331-a9c8-3c409a1b1e7b | -10.05451 | -36.19724 | 2024-12-28 00:26:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.2 |
| ef3413d7-5420-3afd-927c-cbd7483c645d | -10.20244 | -42.22826 | 2024-12-28 00:26:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a336e489-f7e6-3fe7-8abb-1f123dfefca2 | -6.70627 | -44.31661 | 2024-12-28 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bda2b182-d9e1-357a-8b7a-fcb1ef39f6c4 | -10.05199 | -36.18081 | 2024-12-28 00:26:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 178.0 |
| 26ea5dfa-72c1-34a5-8c8a-2ae07392c515 | -11.92236 | -41.35145 | 2024-12-28 00:26:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 80e7cc59-61ca-3e8d-8c09-cd55d0cb2423 | -4.70904 | -43.45162 | 2024-12-28 00:26:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 6f445c42-e195-302b-8b17-fbe1a6de00d3 | -6.44862 | -44.38081 | 2024-12-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6440b820-f685-3784-8c86-69715915093f | -4.54278 | -44.04865 | 2024-12-28 00:26:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 19b66423-055a-3c5a-8262-9946ff49e456 | -4.71974 | -44.47213 | 2024-12-28 00:26:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 2d754203-bf07-3202-b6c4-122490daaa26 | -6.75524 | -39.40135 | 2024-12-28 00:26:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 29e72b42-2abb-3fbe-ac40-84f3d4dcd8f5 | -6.76794 | -39.4042 | 2024-12-28 00:26:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 19211fe5-9293-3c8a-a3e6-76b3040147c6 | -10.63896 | -40.21385 | 2024-12-28 00:26:00 | TERRA_M-M | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| d932ff60-884f-3555-bdb3-9364c88b22f1 | -5.93739 | -45.56581 | 2024-12-28 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6f7337f1-b5b5-377a-90e8-8ca3bd690c63 | -4.74327 | -44.6466 | 2024-12-28 00:26:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1383.7 |
| 559ff6a3-69c0-3776-a0da-205b772a1d91 | -4.57338 | -41.29564 | 2024-12-28 00:26:00 | TERRA_M-M | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 66a0ae4b-13e8-34bf-9208-9cfd3d7b3199 | -5.09957 | -45.10201 | 2024-12-28 00:26:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9f9c217d-bcdd-3866-8636-696b514885d5 | -11.3125 | -42.1293 | 2024-12-28 00:26:00 | TERRA_M-M | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f74d4ca1-941f-354a-ab6d-2374a6ae79e0 | -5.31064 | -46.07177 | 2024-12-28 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| a9b357a2-e4ff-3fee-bd53-0e9e4a280c1f | -4.82357 | -42.35139 | 2024-12-28 00:26:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5e6bbeb5-cb53-3ddd-b200-476c2b04236c | -6.14479 | -41.85353 | 2024-12-28 00:26:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e3b4f3b8-fd9b-3129-96f8-1d93560ff6ee | -10.60531 | -44.98882 | 2024-12-28 00:26:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| da13f9f9-3a73-31da-aee4-4a3b33810b65 | -9.11581 | -40.96701 | 2024-12-28 00:26:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 8f2007b0-abc1-3e18-8ba8-fcef91978fa5 | -4.74196 | -44.63688 | 2024-12-28 00:26:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 218.8 |
| f26f9f5d-a67d-36ee-b85b-de7dc3bbf131 | -4.82481 | -42.36025 | 2024-12-28 00:26:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 6750c753-89ed-3367-a8b6-e520aa4cf4f3 | -5.57579 | -46.13405 | 2024-12-28 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3886d8de-643b-34e8-882d-a40a36de228e | -4.71671 | -43.44141 | 2024-12-28 00:26:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d21b5bf8-67a0-3242-857e-572daa8761e5 | -6.72014 | -44.15901 | 2024-12-28 00:26:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7a4d6276-a6bf-3aec-9e16-64c47b47a5bd | -5.65971 | -39.53595 | 2024-12-28 00:26:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 036183f0-b20c-3404-8456-f0a6693bc77d | -11.92111 | -41.34245 | 2024-12-28 00:26:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9b5110cd-ecec-3ba2-9dd1-d771b9f4e7b4 | -10.87612 | -41.24211 | 2024-12-28 00:26:00 | TERRA_M-M | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1f723495-cf57-36a0-8199-64accb5d3e4d | -6.76658 | -39.41077 | 2024-12-28 00:26:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 94145231-711b-3867-baeb-5954c8a72bfc | -5.91129 | -43.48843 | 2024-12-28 00:26:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a05ec473-cd9c-3034-826a-cf4954aa0413 | -4.7078 | -43.44265 | 2024-12-28 00:26:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1983212a-3f15-3875-a72d-77bb2db7cc9c | -10.04945 | -36.19247 | 2024-12-28 00:26:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 83.4 |
| 81151247-52fe-3def-8f6e-55c2b07ac72c | -10.75148 | -37.14695 | 2024-12-28 00:26:00 | TERRA_M-M | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| a4a4e2e6-fb4c-3078-b088-9710bd447a78 | -5.3091 | -46.06011 | 2024-12-28 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7d17b183-1a25-3a53-ae51-70ba0bfa639d | -11.14011 | -43.30791 | 2024-12-28 00:26:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8b5ce310-c5a9-3929-b094-5628f2bc7a37 | -11.25399 | -44.4818 | 2024-12-28 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 14f4cd7f-8aa7-3ddc-8ba2-ea13bd7bc483 | -4.53373 | -44.04989 | 2024-12-28 00:26:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9a478989-eac8-3191-918a-8bf655a3cd26 | -4.71314 | -44.47945 | 2024-12-28 00:26:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8b9c2e74-7dcd-3b9c-8b57-78b917dbdb21 | -9.55889 | -40.91451 | 2024-12-28 00:26:00 | TERRA_M-M | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 436d2cf8-e4ca-3a96-8b32-87351b37d012 | -6.7568 | -39.41217 | 2024-12-28 00:26:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| e162eecf-3aae-3faa-9626-2bfaeae2e225 | -4.17035 | -42.03316 | 2024-12-28 00:28:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 79158f23-2f18-34b0-94bc-5e8e5b6f0560 | -3.19435 | -46.13023 | 2024-12-28 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 3e968bef-9740-38e2-8bed-2cede3bfd66f | -2.55285 | -46.87823 | 2024-12-28 00:28:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 6960b2d2-7ccb-3ed1-b72d-76c5fdd90d2b | -2.71759 | -46.01213 | 2024-12-28 00:28:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 64487f2c-5c97-378b-acba-596e34f386d0 | -2.4431 | -46.0241 | 2024-12-28 00:28:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| deff22eb-6a9a-3d09-b81c-1ab3f0a957be | -2.72617 | -45.62577 | 2024-12-28 00:28:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 26e86bda-52e1-361b-ac7d-059c2d83f6f4 | -3.94436 | -46.76831 | 2024-12-28 00:28:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 74b1aff8-724e-3b50-801f-94c9c4931973 | -3.86483 | -47.02374 | 2024-12-28 00:28:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f640baa8-75c0-37ab-94ee-c978fd841fae | -3.84146 | -46.68566 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fcead347-6b65-3a8d-bb92-0eb75c542e31 | -2.28722 | -45.57066 | 2024-12-28 00:28:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3286af20-610e-37ad-8b38-929585b304cf | -3.84312 | -46.69806 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4e7498a7-fb03-3c56-96ac-a2bc034ecf63 | -3.19471 | -45.97697 | 2024-12-28 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1a1da21a-1307-3da8-b81e-5ae972cc3550 | -2.23987 | -47.66508 | 2024-12-28 00:28:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1da755f1-4ea0-3482-b8a3-a97d91b4b4f1 | -3.07492 | -41.90529 | 2024-12-28 00:28:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 11c33252-647a-3937-a486-d4a78416c458 | -3.19768 | -45.99895 | 2024-12-28 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 38.4 |
| bef804e0-eea4-3442-adc4-3afa983304c1 | -3.73616 | -47.18928 | 2024-12-28 00:28:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 609db1e3-eed3-369b-87e3-37674cb2bb39 | -3.92045 | -46.66876 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 816978cc-7648-342e-9b6a-2f60e687cb3c | -3.72535 | -47.19078 | 2024-12-28 00:28:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 0fa42485-ba72-3dc4-90e2-9c2fb99bf3e7 | -3.86994 | -47.01511 | 2024-12-28 00:28:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2481b9d6-c391-3add-b435-2d43bda68800 | -3.20603 | -45.98658 | 2024-12-28 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 954e76ad-4e25-3f19-b726-c99cbaf39d44 | -4.12856 | -46.69243 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 5d100c9b-5e1a-311b-a711-7eac035780f5 | -3.99336 | -46.73547 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 99406bae-af82-3f29-9e21-a2ad662e58eb | -3.19444 | -46.12444 | 2024-12-28 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 52404a6c-f642-32f9-93f1-a37994f75529 | -4.00771 | -46.71473 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 592c7e2f-be08-329f-ad83-44e0b641599a | -4.07914 | -47.09073 | 2024-12-28 00:28:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 6debe340-3ab6-36d3-9207-8403745326b7 | -3.56316 | -40.85011 | 2024-12-28 00:28:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 67dd4e2a-c69e-39ee-8bb7-721f3bf3cde7 | -2.28059 | -45.59236 | 2024-12-28 00:28:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 02c5eaaf-f572-3e35-88fe-51ad53e576b2 | -4.03819 | -47.06126 | 2024-12-28 00:28:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 9eb32986-3a9e-365d-96ef-ab9983879a5e | -3.96383 | -46.67545 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 28.3 |
| c97a80ad-6ca7-3f89-bfec-6f49a7451c09 | -3.21107 | -45.49047 | 2024-12-28 00:28:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| a3d6f08b-09a6-3217-973f-56cfd1316c47 | -3.53554 | -40.92493 | 2024-12-28 00:28:00 | TERRA_M-M | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0d2921f4-6eae-3ccf-94b7-6158f5539ed0 | -3.70891 | -41.69768 | 2024-12-28 00:28:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 336a345e-90ee-3cb6-a929-1dba825ad112 | -2.44965 | -49.30568 | 2024-12-28 00:28:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 408bc898-06fa-3a58-bcbd-e9a5534ed7cc | -2.26369 | -47.67593 | 2024-12-28 00:28:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e26d4c78-2414-326d-8ee3-42a90156774a | -3.95486 | -46.7668 | 2024-12-28 00:28:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 56e0f597-4b45-318f-9bd8-5264aef5a72b | -3.76331 | -47.22689 | 2024-12-28 00:28:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0f4eb5cd-1f21-3d0e-a846-4a2016ceb06b | -3.74696 | -47.18768 | 2024-12-28 00:28:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| fac4f80f-f17c-34dd-baf2-62e29bc23e24 | -2.57353 | -45.53777 | 2024-12-28 00:28:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f98e5b2f-7aeb-39d6-b1e6-cc898cf47816 | -2.52081 | -51.86775 | 2024-12-28 00:28:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| f8e3e0b2-b773-3689-bf4a-03c2256cadb2 | -1.6458 | -45.86999 | 2024-12-28 00:28:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 330d8941-dbaf-3b50-98dc-e492418fdb70 | -1.34114 | -46.98869 | 2024-12-28 00:28:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b9082f85-d8d4-369a-a092-eba0bb90105d | -3.71793 | -41.69641 | 2024-12-28 00:28:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| e952030b-fcba-3026-8652-1284838d89d3 | -3.91459 | -46.90947 | 2024-12-28 00:28:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |


[Clique aqui para ver as próximas entradas](README5.md)
