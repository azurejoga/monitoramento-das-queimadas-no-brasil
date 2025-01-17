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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48e7c3d6-9fc0-3242-9137-e3de86633487 | -7.69704 | -35.18719 | 2025-01-17 03:46:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9e92e7e3-4013-356a-8ed3-620c0f2f6ad0 | -7.01961 | -35.17642 | 2025-01-17 03:46:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d5428a67-449e-3375-8723-b21fa02b3a3a | -5.3806 | -36.46291 | 2025-01-17 03:46:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f43314dc-5875-34e4-b1be-cba9ce2219f9 | -7.81731 | -35.17853 | 2025-01-17 03:46:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8f67c528-8f2c-3aab-99d5-88574332979b | -7.84125 | -35.2051 | 2025-01-17 03:46:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dfe63a65-0a68-323f-82b5-d9e4c6232134 | -5.38114 | -36.45946 | 2025-01-17 03:46:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 552092a0-d747-3767-8995-7206b589fe44 | -6.80297 | -35.17352 | 2025-01-17 03:46:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3289345d-1549-32ee-8dd6-001e52ff2c02 | -7.5391 | -39.19296 | 2025-01-17 03:46:00 | NOAA-20 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c472ed69-b0a8-3b90-9af6-a9e924f3c5a7 | -8.91371 | -35.42518 | 2025-01-17 03:46:00 | NOAA-20 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 83fc527f-8426-3842-b199-e13d668c0782 | -8.52683 | -40.57378 | 2025-01-17 03:49:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eaa0cb3b-8b89-3fd6-951b-73b8ad3da8fa | -17.73437 | -39.52423 | 2025-01-17 03:49:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ca709fb5-c5a6-32b8-9502-d588d7845263 | -10.48072 | -36.89391 | 2025-01-17 03:49:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a861a956-faff-3404-9b76-1df5e34f7551 | -19.83635 | -40.08255 | 2025-01-17 03:49:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4c85f4aa-2d77-3ba9-a578-3f1293a073d0 | -10.18716 | -36.35046 | 2025-01-17 03:49:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1c516612-bb89-39c9-ab07-81fb74d92163 | -22.85434 | -42.98149 | 2025-01-17 03:51:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6be2b09b-4f48-3961-b185-075b5a7da344 | -22.6758 | -42.85565 | 2025-01-17 03:51:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| accf9bd0-c229-339a-a03b-cc5f086afcff | -29.6431 | -53.35908 | 2025-01-17 03:53:00 | NOAA-20 | RESTINGA SÊCA | RIO GRANDE DO SUL | Brasil | 4315503 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5679cada-8c8f-3ac1-8f45-290e268d9d1f | -29.64174 | -53.35784 | 2025-01-17 03:53:00 | NOAA-20 | RESTINGA SÊCA | RIO GRANDE DO SUL | Brasil | 4315503 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ebf17d34-c296-33b6-b5e8-1eaa335ee7f6 | -29.64081 | -53.36169 | 2025-01-17 03:53:00 | NOAA-20 | RESTINGA SÊCA | RIO GRANDE DO SUL | Brasil | 4315503 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4fd1ec86-5717-3fa3-90d9-0f9b5de15e0f | 1.3403 | -60.0271 | 2025-01-17 04:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 46fe8f1d-8562-329d-8fe7-38167863e239 | 4.33705 | -59.70444 | 2025-01-17 04:36:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 902a3bc5-390a-3725-aae3-74118e5b4154 | 4.33781 | -59.70981 | 2025-01-17 04:36:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34b2b447-33c8-3d15-8f5a-a7300d28f06d | -0.15788 | -60.87347 | 2025-01-17 04:38:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ac2b93e2-d6a4-39ec-b8cf-3b08b4827891 | 1.34918 | -60.02715 | 2025-01-17 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| dedbaece-f59e-3bf7-bdfd-85bc137c7c72 | 3.59731 | -60.10725 | 2025-01-17 04:38:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 374363a1-199f-346b-a5a3-2a074e3113f6 | 1.34263 | -60.03239 | 2025-01-17 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b57aadfb-3bdb-3a9f-b93a-e47741bb4e1e | 0.84899 | -59.5451 | 2025-01-17 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2993fd19-b828-34df-85e1-60ff5bcdfa36 | 1.34346 | -60.03336 | 2025-01-17 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 95e0d7e1-c72e-356d-b1f3-0f94f451c5bc | 0.63139 | -60.03727 | 2025-01-17 04:38:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1171cd7f-2f99-3207-b18a-d7093eecf09d | 0.73095 | -60.12109 | 2025-01-17 04:38:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c449c88-32c3-3eb3-88e6-350bf2227166 | 0.84823 | -59.54015 | 2025-01-17 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2700c33-1169-3173-9189-05c360f4076e | 2.28577 | -60.21926 | 2025-01-17 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d21b1d5a-702a-3ee8-8b08-a1c10e8996c7 | 1.34921 | -60.03162 | 2025-01-17 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 784e7b53-d362-3512-b9c6-4bffa3779270 | 2.28945 | -60.2198 | 2025-01-17 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 85b8ce2a-eff4-3b30-8e2a-6761113e1bfa | 0.84473 | -59.53986 | 2025-01-17 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1776c4a-0e65-3668-929c-2a25e69672a2 | 1.34838 | -60.02613 | 2025-01-17 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 09619c95-fa4b-3c16-84b6-7c0ce78a0563 | 1.34262 | -60.028 | 2025-01-17 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8653456d-0a2f-31a3-b17e-e9d05f01b2b7 | 0.82092 | -59.71733 | 2025-01-17 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 425f6770-96f8-314e-a200-25c3e29f1200 | 1.35005 | -60.03264 | 2025-01-17 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f60ddaea-af84-3437-821e-d6c589d416b6 | 0.84266 | -59.54595 | 2025-01-17 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc26353e-fb8f-3f19-895a-09883234c5f1 | 1.90447 | -60.57339 | 2025-01-17 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f175d23f-dfaf-3de0-bca6-00fdf72f4539 | 1.90353 | -60.56725 | 2025-01-17 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d1fa5e5-1ae0-3839-ac73-fadf439b5f4a | 0.72444 | -60.12222 | 2025-01-17 04:38:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0ee5eb7-0ed4-35dd-8011-7b1c6cb628c1 | 3.13859 | -60.69882 | 2025-01-17 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2979df84-b205-3ad6-b31f-486406e57ac1 | 0.67076 | -59.99245 | 2025-01-17 04:38:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 701412cd-27a2-3f24-9e6f-af9e5f87e7ca | -2.53498 | -53.95761 | 2025-01-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a96fbe2f-a712-30d2-8099-2f894394a018 | 3.60322 | -60.10019 | 2025-01-17 04:38:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a0f351d-b349-3bca-9464-eb1fcc316458 | 0.73181 | -60.12663 | 2025-01-17 04:38:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce62e917-2ec8-339d-8a7c-1e9ca9d7fbf5 | 1.17503 | -60.48838 | 2025-01-17 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7309a2a-87d7-358a-9e28-d86a4825b336 | 2.29249 | -60.21834 | 2025-01-17 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2964ef13-61fe-3264-abed-8ca58de6cfbc | 0.84553 | -59.54482 | 2025-01-17 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e98d1de7-fb76-34f0-acc7-32a397b95ff1 | 0.8419 | -59.54094 | 2025-01-17 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a34b836-7990-3cdb-bbb5-bfdeadc49320 | 1.16925 | -60.49532 | 2025-01-17 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef15c4e0-adb8-34d1-bca6-a2c394eed2dd | 1.3403 | -60.0271 | 2025-01-17 04:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 68ee7f63-a1e0-3da7-867c-6138bf467c39 | -10.47991 | -36.89315 | 2025-01-17 04:40:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7075bcca-03dc-3af5-af0b-208f39ce1c84 | -18.3635 | -54.98224 | 2025-01-17 04:42:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 12baa694-c9ff-390b-931a-42e7f1a2d21c | -16.11865 | -58.17543 | 2025-01-17 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| aef67da0-3f90-33dc-a088-5017ba0f6306 | -16.11784 | -58.17976 | 2025-01-17 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4b642f62-4023-3ba8-9d95-586f34eeeb64 | -15.60908 | -57.34501 | 2025-01-17 04:42:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f6ad6d2-1395-3148-ac3e-9432be573799 | -15.60979 | -57.34113 | 2025-01-17 04:42:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21601980-6e46-363e-bc57-7a7ee935e2ce | -16.11946 | -58.17108 | 2025-01-17 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ccaf5a74-33cf-3d78-8fb5-61331a09a692 | -22.67743 | -42.85174 | 2025-01-17 04:44:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 13fb07d3-d576-332d-9d40-310a147906b8 | -20.79983 | -56.47987 | 2025-01-17 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b0cd6ae-884e-3070-90ae-c7753032745e | -20.20925 | -56.62132 | 2025-01-17 04:44:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e871df51-d98d-3ff7-bfee-28f84992cc71 | -22.67597 | -42.85524 | 2025-01-17 04:44:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7e2e679f-4ce2-3210-9832-b43c5aed6cea | -22.67706 | -42.85571 | 2025-01-17 04:44:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a26910ab-0acf-358d-992d-862d4454ffe9 | -20.41591 | -54.7454 | 2025-01-17 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc2f0445-5eca-34b4-ad28-a8d968ee6012 | -22.67631 | -42.85127 | 2025-01-17 04:44:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2f8add26-d7c2-3f9a-aaed-5cfea501087a | -23.9996 | -52.36085 | 2025-01-17 04:44:00 | NOAA-21 | CAMPO MOURÃO | PARANÁ | Brasil | 4104303 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 782df1fb-b13f-32d7-972f-da37ab98859b | -20.38458 | -55.9247 | 2025-01-17 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4270b9ab-557e-3e01-ae4b-adc25d67d908 | -29.62087 | -53.29099 | 2025-01-17 04:46:00 | NOAA-21 | AGUDO | RIO GRANDE DO SUL | Brasil | 4300109 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f54ea7af-8f07-3da8-9d22-62f05c297b08 | -29.77945 | -51.17517 | 2025-01-17 04:46:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| 5f92cac5-bbd1-32f2-b372-3773628172c2 | -29.64326 | -53.35761 | 2025-01-17 04:46:00 | NOAA-21 | RESTINGA SÊCA | RIO GRANDE DO SUL | Brasil | 4315503 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d7830cf9-7801-3322-af71-67f97a003594 | 1.3403 | -60.0271 | 2025-01-17 04:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 3719afb3-4222-33e6-8bd7-61a4f81d19b3 | 1.3403 | -60.0271 | 2025-01-17 05:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 2b06409f-83d5-3f75-a311-ff90cf8f124c | 2.16845 | -61.85421 | 2025-01-17 05:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6dae1be-0950-3d7f-a34d-29282ed24e3d | 3.79325 | -59.7289 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6aca47d7-f74f-3920-a036-9849e6c6a449 | 2.98473 | -60.25608 | 2025-01-17 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b8f8ba4-198b-3cd6-8d1a-5eb805af5377 | 1.35136 | -60.02951 | 2025-01-17 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 3e35d8dc-15ef-30fc-af3f-81c9a2e229fd | 3.74168 | -59.71843 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d75fa8f-7a8d-3927-8247-9b6c615a0acc | 4.00898 | -60.33762 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62e5c244-bdbf-3ca3-ab74-dcbd7e65c040 | 2.986 | -60.25398 | 2025-01-17 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a12e79e-0a50-33a7-8057-e783be88e24c | 4.12091 | -60.02926 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8294c3a-f6eb-322c-ad07-ba548e4592ba | 4.29299 | -60.36366 | 2025-01-17 05:01:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 326218ad-b76c-3d46-b5f5-03dc85af824f | 2.19711 | -61.81124 | 2025-01-17 05:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f75c7ac0-fb0e-37e5-bb5c-6eb43573fac9 | 3.6031 | -60.10038 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01ea446d-9596-3805-b2de-7474c17c0869 | 2.2896 | -60.21689 | 2025-01-17 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cc73426-c830-360e-bfdd-0f3c30c9dc5e | 1.90405 | -60.5667 | 2025-01-17 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30f0b974-304a-3710-a138-b05da195cb3f | 3.79264 | -59.72477 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f346a64-70c1-3039-a9e3-f05fdf7e8556 | 2.1668 | -61.8558 | 2025-01-17 05:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e1d8622-aee8-33ae-aac1-a7dc7d13cf0e | 4.26677 | -60.151 | 2025-01-17 05:01:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25acdff2-6bba-3fa0-abbc-1164a01745a2 | 2.28521 | -60.21756 | 2025-01-17 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77e6802c-31bf-3173-8a97-c529dfb47e7e | 3.60376 | -60.10474 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a51e4c66-5c15-3e66-a265-127fc184e178 | 2.17828 | -61.85274 | 2025-01-17 05:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 13e37829-6b84-3a7f-8bd5-8bc618d9c870 | 1.17135 | -60.49154 | 2025-01-17 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ef1a3b1-6d29-3d81-b8b9-190d40600d8d | 1.32401 | -60.03748 | 2025-01-17 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d423625-47df-3be4-a8d4-58685b59aeb8 | 1.05177 | -59.65234 | 2025-01-17 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 568455bf-e4c9-3b20-aec8-436c4d28464e | 1.17508 | -60.48663 | 2025-01-17 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bf8d732-3467-32b7-b6ff-bfb8344a2187 | 3.14406 | -60.69931 | 2025-01-17 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dfc6d71f-03c6-3894-a44a-d8ddea6c952a | 3.78891 | -59.72958 | 2025-01-17 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
