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
| e45610a9-fec5-3767-82f5-81b2041643fe | -22.243299 | -52.862099 | 2026-07-17 01:06:00 | METOP-C | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b0fd4938-5b0e-31cb-a14f-8bd92a8d0ae3 | -19.842199 | -57.9716 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8a0ff973-0f42-3ac2-82d2-cb93d7a2f450 | -28.8937 | -52.625999 | 2026-07-17 01:06:00 | METOP-C | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8183e096-42ce-3ce5-88cb-9b3168c320d7 | -20.6534 | -50.106998 | 2026-07-17 01:06:00 | METOP-C | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b265532e-c5f5-365c-aa64-a5eb710b0e6c | -19.856501 | -57.993198 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f50ccb43-cca8-361b-b7a2-b0d7a90d501a | -10.8147 | -45.112701 | 2026-07-17 01:06:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9f60255b-93e4-3cf8-b8f9-3a5e24ee2700 | -8.1042 | -58.286201 | 2026-07-17 01:06:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf6df815-3ed7-3ddc-b7fa-77bcdbe52d21 | -22.2449 | -52.869701 | 2026-07-17 01:06:00 | METOP-C | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 62467cad-ebb5-3122-923a-50af5f08e52b | -10.8243 | -45.1101 | 2026-07-17 01:06:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 35228550-7bb2-3489-9f16-754f3912646a | -19.8542 | -57.9814 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8893e253-ae16-3700-bd53-40cf6b63e9b7 | -21.7724 | -56.313202 | 2026-07-17 01:06:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c30f5580-d27c-33a0-9a76-6af1892922e5 | -19.8444 | -57.983398 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fc234eca-c1be-334b-85a6-6cf32f1aae06 | -8.5101 | -48.059601 | 2026-07-17 01:06:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e96288aa-8727-378c-a45b-1a17c2ae8648 | -9.5179 | -47.138199 | 2026-07-17 01:06:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1bff71c-41b3-3cdb-8e3f-7a9b597ae055 | -19.816099 | -57.940399 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d45cd1d8-6b92-3f30-9f47-78828db32dd2 | -21.662901 | -56.326199 | 2026-07-17 01:06:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a9397f77-6d23-3924-b54c-e485221d7ab6 | -19.866301 | -57.991199 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 31e130f9-5aa6-3167-aafb-3a160cf36121 | -19.8325 | -57.973598 | 2026-07-17 01:06:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 42570f9d-0753-363c-adb2-d9de1bed9a30 | -10.8092 | -45.1338 | 2026-07-17 01:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| e75b5da7-64ea-3a13-bb21-e300e2dc10d1 | -19.8637 | -57.989 | 2026-07-17 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.8 |
| d73a75e2-0c52-3777-a2b7-fe73c706e402 | -10.8096 | -45.1108 | 2026-07-17 01:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 03fa45b1-618f-3df2-bee3-9be5a29ec293 | -13.4448 | -43.8604 | 2026-07-17 01:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 8e78ef5d-188a-3c78-9d70-d525c0942bae | -9.4582 | -64.033 | 2026-07-17 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 281c9652-abb4-3322-8b7d-e62aae320252 | -10.8283 | -45.1312 | 2026-07-17 01:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 8aed5abb-263e-3dea-bdf3-d6dc60981582 | -10.8287 | -45.1082 | 2026-07-17 01:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| e43d5b86-9785-3a66-8991-d657f69e21fd | -19.8436 | -57.9917 | 2026-07-17 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 0249bdee-f022-305e-bb80-48306136ce18 | -10.8283 | -45.1312 | 2026-07-17 01:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 3f4e2a17-27c6-3338-9c98-634bc0d2af0d | -13.4448 | -43.8604 | 2026-07-17 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| b172450a-9108-385c-a33c-317cabd0cdcf | -10.8092 | -45.1338 | 2026-07-17 01:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| de2a5761-de6c-30d2-910b-cd4afb555747 | -9.4582 | -64.033 | 2026-07-17 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 3707b429-48e4-39ff-8cd3-e701d733814b | -10.8283 | -45.1312 | 2026-07-17 01:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| d84ef99b-6b36-32f9-9740-5242f526aaf6 | -9.4582 | -64.033 | 2026-07-17 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 969921b8-c7d0-3237-8d11-6965f468f922 | -10.8092 | -45.1338 | 2026-07-17 01:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 2128edba-c4ca-3736-82b7-97d6da11b8e7 | -13.4448 | -43.8604 | 2026-07-17 01:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| c657e7b0-89e0-32b7-8c1f-af088867d023 | -19.8245 | -57.96229 | 2026-07-17 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 5c52a139-452e-35c7-acf2-9881d8bf7569 | -19.82515 | -57.96702 | 2026-07-17 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 882603ae-2667-3564-8b1e-703cb57e0c59 | -9.44926 | -64.02947 | 2026-07-17 01:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 328af368-3b9b-3a65-b21e-b7707af93bb5 | -9.45466 | -64.02151 | 2026-07-17 01:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 26a2e4d6-783d-3102-b078-a1b3b92e9d9c | -9.45864 | -64.04556 | 2026-07-17 01:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 2b2a53bc-e0d7-3cbd-a480-e8bc8bc48b1c | -9.4582 | -64.033 | 2026-07-17 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 54ad0e55-ae51-36e6-b392-12dd9c372565 | -10.8092 | -45.1338 | 2026-07-17 01:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| cff13454-257c-391c-a547-9937bc54d32d | -10.8287 | -45.1082 | 2026-07-17 01:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 20c6b86f-4e7a-373e-8977-75b055eadf89 | -10.8283 | -45.1312 | 2026-07-17 01:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 2083f28d-d545-3650-be2a-33ad9ebbca22 | -9.4582 | -64.033 | 2026-07-17 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| b8b75a3c-1bd0-3700-97fd-d4a9c43b96cd | -10.8092 | -45.1338 | 2026-07-17 01:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| c332cda7-cffd-3d09-9402-2d1f99fdf1de | -13.4448 | -43.8604 | 2026-07-17 01:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| fcb055ac-3e59-342b-ace8-9fbe760cf3bc | -10.8283 | -45.1312 | 2026-07-17 01:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 93af961d-0961-376f-95ee-0b719b6cf819 | -10.8092 | -45.1338 | 2026-07-17 02:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 127a71ef-8fa3-3dc5-8034-c717e3dbdb75 | -9.4773 | -40.3116 | 2026-07-17 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.2 |
| e9ce5145-4fc0-3b78-956c-7f790b758438 | -10.8283 | -45.1312 | 2026-07-17 02:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 443e0c7b-12a7-3f17-afbd-d184a7fa42ba | -9.4582 | -64.033 | 2026-07-17 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| fb8d52b6-40d0-3c85-b0f5-64ed6798aa18 | -20.9879 | -40.9068 | 2026-07-17 02:10:00 | GOES-19 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 70.4 |
| 110e67ac-7614-344a-9ad7-f3a340480192 | -9.4583 | -64.0142 | 2026-07-17 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 0531b5d1-5f02-3cef-b5a5-5e09576d83b2 | -9.4582 | -64.033 | 2026-07-17 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 799a5056-a2bf-3722-84e6-e95f2375ca94 | -10.8092 | -45.1338 | 2026-07-17 02:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 261232af-b9d2-3968-9ad2-0c9c4e56d267 | -10.8283 | -45.1312 | 2026-07-17 02:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| dffe04a2-29cd-359d-952a-6ceea253fa14 | -10.8283 | -45.1312 | 2026-07-17 02:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| c7b7a64e-08d8-39a4-b634-0f6ba0b1e083 | -10.8092 | -45.1338 | 2026-07-17 02:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 656a0dd1-78b6-37cb-9f39-76b3f8aad1b8 | -9.4773 | -40.3116 | 2026-07-17 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 242.2 |
| 0c1c62e9-a98d-3463-875c-cfb7cf3503e8 | -9.4777 | -40.2867 | 2026-07-17 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 180.9 |
| 6e82d67b-cba0-35ef-bbec-f35264ff0bc0 | -9.4582 | -64.033 | 2026-07-17 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 0e2e6f07-cdd7-3a83-8ada-91ffafd36727 | -9.4582 | -40.3143 | 2026-07-17 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 215.8 |
| c0a27f33-f754-3110-b5e7-c255f1ae9e8f | -9.4586 | -40.2894 | 2026-07-17 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 160.9 |
| e75c6c87-0789-3264-9c5a-5478de4582a4 | -9.4581 | -64.0519 | 2026-07-17 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 9b2ff492-7614-3f93-a1dc-e42e334560d9 | -10.8283 | -45.1312 | 2026-07-17 02:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| ee924507-fb5c-3378-aeb8-ce3f90d6dee7 | -10.812 | -47.3702 | 2026-07-17 02:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 4fe2ec71-3748-37ef-aa61-e2386ccf2467 | -10.8307 | -47.3901 | 2026-07-17 02:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 2b654b92-3223-36fa-8bc2-d47c31795065 | -9.4773 | -40.3116 | 2026-07-17 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 226.6 |
| 1d3847dd-05cb-33a4-bef3-aa3bf9b37bf6 | -9.4582 | -40.3143 | 2026-07-17 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 9ea045b5-aa72-3a01-8ff5-1bfa8f2c5a5e | -9.4777 | -40.2867 | 2026-07-17 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 98.7 |
| aeb23e06-8ed9-3ea1-87b9-0b4c037acc66 | -10.8283 | -45.1312 | 2026-07-17 02:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 239969ec-abd3-3001-8cb2-ce36219cf395 | -10.831 | -47.3679 | 2026-07-17 02:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 3b85a5d8-53b8-31f7-95c0-af35f5315fe1 | -9.4581 | -64.0519 | 2026-07-17 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| ce8b8d32-66f8-37b1-8e96-689a1d8881a3 | -9.4396 | -64.0338 | 2026-07-17 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| f3f8f112-0469-3df8-91d2-aeb938e618a8 | -9.4582 | -64.033 | 2026-07-17 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.3 |
| c46ab54a-914a-31a6-9647-b68533823060 | -9.4583 | -64.0142 | 2026-07-17 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 31.9 |
| e4a1c06c-2188-3472-a74c-063ac985d229 | -10.8092 | -45.1338 | 2026-07-17 02:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| fdc6c46d-7af1-336c-9156-ad7c01e4a13e | -10.8116 | -47.3925 | 2026-07-17 02:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 55bebbb7-ed61-36d8-a2af-9c3b6a560d3b | -9.4767 | -64.0323 | 2026-07-17 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 66aa55a5-559c-394a-8bf5-538a714f361d | -10.8283 | -45.1312 | 2026-07-17 02:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| bddc9af6-de49-3cf0-b709-a3d6e8107fe0 | -10.8307 | -47.3901 | 2026-07-17 02:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| b6f37174-484a-32ec-93ae-b82d3858775b | -9.4581 | -64.0519 | 2026-07-17 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 723f6113-69ef-3100-ba7e-0e6d90132113 | -9.4773 | -40.3116 | 2026-07-17 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.9 |
| b6082fc9-1d43-3aed-a806-9ef095f627ad | -9.4582 | -64.033 | 2026-07-17 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 73f292eb-6b53-3baa-9b13-58415273ba5c | -10.831 | -47.3679 | 2026-07-17 02:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| af3c9aa7-2ccf-39c0-a90b-a23e73f975b5 | -9.4582 | -64.033 | 2026-07-17 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ae540b2c-da65-367e-98ec-e9dd37a32e5d | -9.4777 | -40.2867 | 2026-07-17 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 91.5 |
| bae02e6e-9d28-3dd5-9cd6-f3da6e9fb4c1 | -9.4582 | -40.3143 | 2026-07-17 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.7 |
| ef6ea57b-0ac5-3d8d-837d-10996205d96d | -9.4773 | -40.3116 | 2026-07-17 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 179.3 |
| 69bb2e07-edfe-310f-80d5-4fc21cd966df | -10.8283 | -45.1312 | 2026-07-17 03:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 184645f0-63cf-3ce7-b540-d6475f037ff9 | -9.4773 | -40.3116 | 2026-07-17 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 188.9 |
| 34fb7587-1bdd-3632-b92e-1f2f43110390 | -10.8283 | -45.1312 | 2026-07-17 03:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 31a6f624-0d68-30d4-9f3a-57f1a018ffe7 | -9.4777 | -40.2867 | 2026-07-17 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 105.2 |
| c442acd5-8a71-3cf5-b32a-db0cc16dafa1 | -5.0327 | -38.13708 | 2026-07-17 03:15:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bddaf984-53c0-3eb6-9042-aa985098932e | -5.12209 | -38.06544 | 2026-07-17 03:15:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 865d832e-dca2-3fde-8c4f-73062ec823cd | -5.12555 | -38.06701 | 2026-07-17 03:15:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fa5a979e-5abc-3c54-954e-c17f1622999d | -5.60369 | -36.86973 | 2026-07-17 03:17:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a53f8c2e-cb99-3758-9ac7-c40c0b3ebb5f | -9.47209 | -40.30096 | 2026-07-17 03:17:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 155.2 |
| 9e3a7fbc-5f18-3a22-ae5f-ad7f3baf92f0 | -9.47744 | -40.30754 | 2026-07-17 03:17:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 624fdc1f-1c25-3bc6-8f86-c72746946c48 | -9.46999 | -40.31164 | 2026-07-17 03:17:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.7 |


[Clique aqui para ver as próximas entradas](README4.md)
