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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c4a7d5b-db8f-3579-8b85-8010d2155787 | -7.7705 | -42.52499 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9295782d-2a5a-35fc-af1c-d5ea5c0541b2 | -8.75874 | -49.92763 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaf6ff51-3272-387d-b6ef-0045efdb72f6 | -11.56944 | -47.65417 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 835ab0eb-bf7a-3f12-9def-123b19b50e3d | -5.61775 | -51.9382 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46200a9e-980e-38d1-a103-4ded36fa7f59 | -7.75668 | -42.59266 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f1fbf6f6-045e-3599-a70d-814d02539a81 | -4.45567 | -50.0985 | 2025-10-03 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca37e017-9191-3ed6-af57-7b3479699e72 | -7.77435 | -47.37816 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 78757dd7-c165-38a7-b3e4-71096f7fb917 | -11.79525 | -47.93296 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ac4ab18-b7c3-3aad-b1c7-f4530327569f | -11.1476 | -43.40814 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bec6e218-8f55-30a4-afd0-57a5f9af3466 | -12.41399 | -45.16652 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b8a9a1a-d5cf-3637-ac7d-1fb11d9d5479 | -10.2978 | -47.93764 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03fd372b-0570-31a0-bdcc-dfccbab0aa08 | -11.77176 | -46.827 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceed2703-5d0f-34b8-aa41-89c99a10f321 | -8.91024 | -45.03909 | 2025-10-03 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d32f7afe-8051-32e3-8a0a-438398d15df4 | -11.80583 | -47.93099 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5afb9d20-14b8-3186-89a7-1f07b360ca27 | -8.72069 | -47.13954 | 2025-10-03 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90780198-1867-3737-8084-bbf0be3dfcb4 | -7.7456 | -42.59494 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 374efa6e-4b76-34c2-b1ea-5ca3c28ba817 | -6.03995 | -44.63481 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e31f975f-9c75-3da2-a718-f8acd1aeb7cd | -9.072 | -46.64926 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3be9ce03-75cb-31b0-8c4d-feeeccaf23b1 | -5.40289 | -41.32701 | 2025-10-03 04:32:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 18e3c773-51a7-3e4f-b526-94dbf5b45bbc | -8.45112 | -41.89428 | 2025-10-03 04:32:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 98ab0037-3518-37d5-84c3-1dd9a934c44b | -11.13921 | -47.1884 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 232a1170-085d-3268-bcec-ffedfb97ec71 | -11.90645 | -46.26956 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e75456c9-69c9-3e7e-929d-8d65f0882637 | -6.44115 | -44.46125 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e487c519-b848-37ac-b06d-cbac2f6a0366 | -10.94186 | -46.71157 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 27ade199-5096-3886-8924-7f4810f52819 | -6.04666 | -44.22808 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd4f0bfc-a201-3291-a564-2f2ebf6f8034 | -10.98484 | -46.68318 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ccceecca-7e1f-3a8e-bd82-60308f2ee55d | -7.70881 | -46.20224 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ccd0367d-42af-3dd7-b267-4db53efc8096 | -11.45446 | -44.96496 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f670335-7fcc-3472-bc22-dbfa376b54b6 | -11.61809 | -45.06493 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 309371a4-b298-3830-96ad-b8a81c548b56 | -5.47032 | -44.69162 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1c48d8e-0ccb-388d-9daa-d1ff9826bb42 | -5.75417 | -46.61425 | 2025-10-03 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc9d4018-0c49-35cc-9bb5-54e53e168909 | -11.45955 | -44.95628 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1e0641c-c157-3580-bea8-7ad8801b1f08 | -8.51617 | -50.03971 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ec0d5f1-b935-31ab-aa12-bc142292d191 | -4.6615 | -45.79073 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25394209-1fdb-3810-801a-ab6d8370628e | -9.44635 | -50.89452 | 2025-10-03 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71e53d3b-9261-3f8a-926a-eb78f61bd044 | -6.26153 | -43.8844 | 2025-10-03 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6b57c94a-dd7c-31f0-9c27-caa71a29f856 | -6.05041 | -44.62683 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37520d5b-c3f6-3ff6-bbe1-9ca786f72965 | -8.3047 | -44.8656 | 2025-10-03 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03bfb5ff-3a55-3790-aed0-129f8cf3e771 | -5.91149 | -42.77392 | 2025-10-03 04:32:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8a1f8fa0-0152-3bed-9506-12dfcc874577 | -10.82012 | -41.26526 | 2025-10-03 04:32:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 31e939f8-4585-3e53-b79e-ecc0ba204237 | -11.294 | -47.83967 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad056acf-fe17-3afc-87a3-56ee07bf88a3 | -5.63476 | -44.70178 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86d9746b-c3bf-3d12-b065-acf6c55f2ef4 | -8.79655 | -46.66745 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6ac6e84a-60a0-38d1-ab20-5a334a04cead | -10.58762 | -48.70929 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 33dc4c53-4d8d-31c3-96eb-ad75845de0db | -11.80864 | -45.02531 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cabebe90-c5d6-3a13-94dd-6438022943b5 | -9.94909 | -43.57628 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ccb9bee-2677-389d-bef8-20a0cfcef9f5 | -7.2111 | -46.87695 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b0ec7cb-92f7-36cb-9ef1-793389bbe67b | -6.79814 | -44.74885 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56c20a97-4c21-3a70-b082-8d07c4875c31 | -8.62533 | -54.99196 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c1c1188-9f62-36cd-b17e-1fb0a1792fb0 | -6.22637 | -45.34709 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce2af0e0-0cd4-3fcd-941c-96e0844035b6 | -11.82875 | -45.01917 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 304d7bfc-677a-3004-aea4-0f90085f27f6 | -7.43045 | -47.01162 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ed5c84d-640a-35e3-b192-956915c346d8 | -6.05102 | -44.62277 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 722b690c-5576-3030-b899-6d868cb6563c | -11.83401 | -45.01181 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fa0d643-e56a-32be-a3f5-291161d7d26d | -10.06163 | -48.18789 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5d2ba68-5fd6-3897-9efa-b2923d6dcdbd | -9.92392 | -43.72264 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 21fbdab6-7161-3a61-b593-4c71332a33eb | -11.8062 | -45.01569 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aeb89e3b-df96-3da2-821a-1d4653abcbff | -6.55292 | -43.89657 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a1a6271-9527-3e7d-a6da-235aec996dc7 | -6.68011 | -42.83128 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 797e0b14-896b-315f-8c67-f63df942645f | -8.87651 | -50.89985 | 2025-10-03 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76d654bd-316d-37b2-89f3-4aa7584771f7 | -5.23646 | -42.97832 | 2025-10-03 04:32:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 700d0cc8-1930-3864-a1e0-4d1bc2d5e60c | -10.28359 | -44.33237 | 2025-10-03 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78c23fdd-1a83-3b7e-a609-c7db6156f352 | -10.88034 | -47.81137 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a9861e4-c03c-3406-8369-8ea86ad45ed0 | -10.10399 | -48.09052 | 2025-10-03 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b4f3af9-2966-3c92-9727-f1ce5eba075a | -10.22679 | -48.23946 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6069ab6-66eb-307c-8f2c-b9af5aba02f8 | -7.77214 | -42.51343 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fe4e4aad-29eb-3801-af37-49e8506891b6 | -11.87612 | -45.01315 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 754baede-fb1d-34c7-abba-f10cea55ddaf | -10.92472 | -46.7322 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8fe88f6-faf9-3da1-9676-b658d8aa6578 | -9.39876 | -50.4152 | 2025-10-03 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7675ffbc-14de-37b2-a366-a88117c131f7 | -8.59381 | -44.77978 | 2025-10-03 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9c86a83-1992-3abe-ba8a-46ec007106e9 | -7.75114 | -46.24662 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 23da5aea-9d1f-360b-94e2-e8696b12e8bc | -8.1887 | -47.00264 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67434662-7f73-3729-8026-f623684c8624 | -7.42253 | -40.07803 | 2025-10-03 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d36815be-b278-3a8f-8704-0280f6e5678d | -9.07824 | -48.02764 | 2025-10-03 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7dffcf62-2944-3957-9f9b-1cd0c1035b26 | -11.8424 | -44.95214 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afbf510f-3e69-37b0-930f-c09d3af78459 | -6.27185 | -44.04601 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89259dca-4914-359d-88fe-1cf64c5e1e98 | -9.29665 | -45.6768 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17f6269c-551c-3484-92f6-ad2709141ba1 | -11.64111 | -45.06438 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c4b7878-eb71-3930-9d55-a07f923e43c8 | -6.70549 | -42.79856 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 881a5c58-5361-3455-b280-08e1c5cb58f0 | -5.62703 | -44.70474 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 956a3f5e-41ee-30f9-9f63-70980431495c | -6.23879 | -44.24172 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e725238-9da2-356a-9fd2-71405996cb07 | -6.83696 | -48.79506 | 2025-10-03 04:32:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb0022b3-d567-3287-8b42-9425c2e2115f | -7.05872 | -43.30564 | 2025-10-03 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9e83d1a0-bda3-3f35-b9b1-4aded98d1205 | -12.02785 | -47.89942 | 2025-10-03 04:32:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61accd92-6e54-3e08-ad6e-4129915e6186 | -5.71386 | -49.25563 | 2025-10-03 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 405c76e8-3d80-3753-a4a1-263c57a4f4b0 | -11.46262 | -44.96158 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d307476-8ec7-3f16-b64b-53c92414aa73 | -11.60133 | -47.64813 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba64705e-9cf8-3dd6-ac4e-bf9d49fdca35 | -8.71174 | -47.98355 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b2f88bc9-85cf-3072-9b3d-70830fdc4428 | -5.36106 | -45.95955 | 2025-10-03 04:32:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86364fb7-32ab-3e91-b78f-5b66b2598110 | -7.29335 | -44.1901 | 2025-10-03 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0169da93-1c6c-3eb0-b778-b4eefcd0b893 | -11.47336 | -45.0197 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 963993a0-ae73-33d3-88e4-6ad416413d9f | -8.79994 | -46.66798 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 522c25be-e6a5-3d0f-aee5-96a2c1301034 | -7.75403 | -46.27349 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 7d68e339-b4e2-3477-a112-24dc99e7b1b4 | -9.91017 | -47.72058 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f07523e-fc39-3a9c-919b-fdb6f7630948 | -7.29589 | -44.18439 | 2025-10-03 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6a42010-d50b-387d-8149-f3533cbf447f | -6.6761 | -42.83064 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d80fc82e-895b-3619-9421-6025992e0365 | -11.86181 | -44.97848 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 981b5974-da4c-35a6-bff8-a6cb5c911c43 | -9.91769 | -50.50241 | 2025-10-03 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93c05c82-aa60-3fde-bdab-3386a30214ce | -5.54326 | -51.12912 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba3bdd93-489b-3eab-a1c9-5e1ab5c58867 | -6.05163 | -44.61867 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README94.md)
