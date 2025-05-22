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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ad14925-81a0-382d-8a37-48d6b0f2157b | -7.46948 | -47.06103 | 2025-05-22 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1e3cc1a-987d-3999-a677-e18325dbd032 | -12.35201 | -49.98115 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 277e04a4-f0ce-3910-84bf-acaf24f2e6ce | -10.37011 | -47.97181 | 2025-05-22 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e509d81e-07d7-39fd-8331-bf9e28f8f602 | -12.29714 | -52.49112 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f7b725f3-c82e-3562-b1d4-d60d7fd2801b | -7.46444 | -47.06009 | 2025-05-22 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fb688c2-6f9c-39e7-8f3e-3f3b678d49cd | -11.58274 | -47.61721 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9f1c89ba-b55c-3fac-ab95-429b36991cda | -12.28994 | -52.49969 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 83da57a6-552a-31c6-b5a7-d4a29e4ee301 | -10.46209 | -49.14689 | 2025-05-22 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06c99a14-fecf-3eb3-8c40-c983488e03e9 | -12.08144 | -47.34948 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f76bd37-0a8e-3147-8045-900e0b1ef958 | -14.05107 | -45.52951 | 2025-05-22 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aef91566-f831-3ae4-99aa-7ab3e3386368 | -13.52122 | -43.69037 | 2025-05-22 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a4bd75b-68b5-3b89-8aa0-085e627ebf54 | -7.9709 | -49.6922 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 261e7a89-a44c-3dbd-9e0f-d621e82e0527 | -8.91267 | -50.02541 | 2025-05-22 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 772a1cb0-94be-3cdb-9340-e51f386a8713 | -9.04674 | -47.01694 | 2025-05-22 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 58d7552c-4a21-3d88-b322-691396eb52a0 | -9.01843 | -47.74434 | 2025-05-22 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96250a5c-a073-3539-a31a-e2ddbf80ecd5 | -11.57788 | -47.87233 | 2025-05-22 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8a9fb34-fb6d-3954-af36-edc7176b0fa0 | -12.35682 | -49.98623 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9d7caa33-187f-3691-9313-1a6f80f795ce | -11.59734 | -47.62016 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 568e2690-70ba-3fbc-a9f1-b7380a7c2898 | -14.05075 | -45.52928 | 2025-05-22 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33e20d0b-ed10-374b-b248-6783bff3ce81 | -10.12093 | -47.10572 | 2025-05-22 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73e8faac-34ea-37ac-a80a-c526ef67bc13 | -13.38675 | -48.45626 | 2025-05-22 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cde37eaf-80c8-3be6-b7a7-50ba0036ace7 | -17.61257 | -54.17505 | 2025-05-22 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b04e2434-0cfa-33c8-920e-0e0de82c68b3 | -19.88378 | -44.76172 | 2025-05-22 03:57:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f07cc684-2f88-387f-9cd0-c1be7784b3bd | -17.85723 | -49.61287 | 2025-05-22 03:57:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 210fca4e-64e0-3416-8033-a81acdf74807 | -20.57931 | -44.57507 | 2025-05-22 03:57:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d836bcb1-09fe-37ac-b3dc-f8f22de5a5bf | -17.77804 | -42.80799 | 2025-05-22 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db8122b8-33b6-341d-8e37-429a22405f6a | -17.84094 | -50.81319 | 2025-05-22 03:57:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2ab3710-af3c-3b38-884c-8ba57a3aa1ef | -16.02897 | -43.67976 | 2025-05-22 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 830dc0ed-9f06-3110-a0fb-1098d0bce8d7 | -20.83785 | -43.21811 | 2025-05-22 03:57:00 | NOAA-21 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 06842ff5-1461-3380-a985-c964be916d4a | -19.06048 | -53.45516 | 2025-05-22 03:57:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5a03b515-3f01-3e49-a250-5af9921c053f | -15.74532 | -43.48933 | 2025-05-22 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d00bad5c-e862-32ce-9f3e-4efc75401c88 | -13.78599 | -54.31096 | 2025-05-22 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 99cdd248-8be0-38ad-9af5-8e12148fc109 | -17.34642 | -51.90427 | 2025-05-22 03:57:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d787ef7-9a8a-3d92-be4e-ad46e3b4688d | -21.36594 | -48.76563 | 2025-05-22 03:57:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af302b94-4018-34db-a833-95afe4360f02 | -19.51354 | -44.27742 | 2025-05-22 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0377ec98-4ade-3714-8585-611f2174fd66 | -16.81589 | -47.65962 | 2025-05-22 03:57:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d95271dd-0797-328d-b5ef-d28c603a6454 | -19.8394 | -40.08197 | 2025-05-22 03:57:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3c80e34f-1fe3-3cae-9209-e1a21034b99c | -17.62074 | -54.17537 | 2025-05-22 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cd54fc2b-1e91-36ef-96a6-f7e5ab48b1e2 | -13.66917 | -53.93513 | 2025-05-22 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2db4ea11-32f3-346c-a7d7-08d16ae5f0d1 | -17.47394 | -45.4728 | 2025-05-22 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3a93c62-e9a6-3daa-a74a-fdef5a4aa921 | -13.66772 | -53.94167 | 2025-05-22 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a924b340-16f5-3763-bbf2-cf03d4985d2a | -14.0333 | -53.37714 | 2025-05-22 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3ec3c971-ebb8-3997-8deb-f6ebddbe1cf3 | -19.15873 | -47.82043 | 2025-05-22 03:57:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d02410e-32d7-328c-94b2-fbd9a38c72a8 | -19.84937 | -43.8459 | 2025-05-22 03:57:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 780b1f1e-025b-3ddf-92e1-87e2d6f12028 | -17.27232 | -42.65306 | 2025-05-22 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e00163d-e0f8-3cb9-9b3a-01f04c998b0a | -15.69526 | -43.42162 | 2025-05-22 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fedb4fb8-b88b-3619-b83c-df1e7ff866c2 | -20.60932 | -48.86264 | 2025-05-22 03:57:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 78d8061f-5f16-31f4-a64c-709e726f06b3 | -19.05929 | -53.46043 | 2025-05-22 03:57:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e89c20a4-a79e-3258-b6f1-6e546bc113d4 | -18.35167 | -46.4822 | 2025-05-22 03:57:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61ae3075-905f-3e25-b3f2-ecf5a22802e3 | -20.99805 | -51.79367 | 2025-05-22 03:57:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d3c1878b-c87c-3f80-bffd-0704df63b728 | -13.66231 | -53.9334 | 2025-05-22 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6542fa4b-fc82-3630-ab36-092601c2024e | -13.78755 | -54.30405 | 2025-05-22 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2fbe4994-4b2d-30d1-919d-7bb7a02eef21 | -19.05436 | -53.45383 | 2025-05-22 03:57:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0d4a67e-86f8-356e-ac74-158df97a4ea4 | -13.66342 | -53.93281 | 2025-05-22 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3a11e9b2-4830-33ae-a055-9b89d4059d81 | -20.05301 | -45.42276 | 2025-05-22 03:57:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 133a84bb-7b89-3f3e-bca8-7a29644458f2 | -16.8708 | -42.87117 | 2025-05-22 03:57:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aeaa2716-26ae-3952-a7af-af748abce95e | -22.16434 | -42.939 | 2025-05-22 03:57:00 | NOAA-21 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 92f3e5e6-ae44-354e-8d73-33ac44ab3418 | -14.03995 | -53.37862 | 2025-05-22 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c3910a6a-372d-3a48-9ac6-00c6f001df13 | -18.35013 | -46.48524 | 2025-05-22 03:57:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4177c3a-b59a-3ed0-a756-3e391f65733d | -13.78126 | -54.31334 | 2025-05-22 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2cf5c1a9-3032-3919-a1c1-108293733858 | -15.57157 | -47.85505 | 2025-05-22 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30682c6a-f158-3842-82cf-4978f7c5bc4f | -13.80319 | -52.89677 | 2025-05-22 03:57:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 247fa5a0-b5c1-3618-bcea-35c659c78dbb | -17.28085 | -42.64995 | 2025-05-22 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1898acc-77b1-31f2-8f25-aae9b21b7513 | -19.36336 | -45.35736 | 2025-05-22 03:57:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cbb3fe47-a746-376b-87c5-d24d032c2738 | -21.66994 | -43.44159 | 2025-05-22 03:57:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 850ad49c-fec5-345c-8dfb-cb8ebb038ae1 | -22.78633 | -43.75673 | 2025-05-22 03:57:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3fe61805-2a82-3356-b928-d218cef8db44 | -17.59727 | -43.19827 | 2025-05-22 03:57:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d9b74f7-6742-380f-8924-60850153049c | -15.57007 | -47.85715 | 2025-05-22 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07857ae2-eb10-376a-83fd-94fdaec17651 | -17.21487 | -44.80227 | 2025-05-22 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa77cc2b-b237-3241-94ff-59cdb37c0b6b | -13.80482 | -52.89296 | 2025-05-22 03:57:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7812f7bb-f464-3c59-9202-37da87a8160c | -20.34797 | -40.3609 | 2025-05-22 03:57:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0fa93571-42e7-39fb-abed-4ce6e8ffccfa | -17.15036 | -54.01101 | 2025-05-22 03:57:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b2f46d4-f795-3d65-bd4a-a72d78f0865d | -16.03181 | -43.68464 | 2025-05-22 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f8cb943-7de0-39d9-a222-541f47656f10 | -21.21849 | -48.61403 | 2025-05-22 03:57:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0f4628d7-e2ea-3d0a-9be7-6a64ed2085ac | -17.78143 | -42.80861 | 2025-05-22 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7104036-45a9-3417-807f-45f8a0c0b48a | -16.74148 | -46.64846 | 2025-05-22 03:57:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1d80a76-68e2-3303-9c27-32430e960a3c | -17.70521 | -47.4971 | 2025-05-22 03:57:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16516a61-2e28-3c96-a497-a016093ba3af | -15.20942 | -43.82411 | 2025-05-22 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a775002-5e2d-3425-a02d-4d328cd6138c | -19.73625 | -54.51222 | 2025-05-22 03:57:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d8d95ffe-5df4-338f-829a-e0824b896f8e | -13.67456 | -53.9435 | 2025-05-22 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 838ca15b-bd92-315d-9802-6f1d29d765cf | -13.78282 | -54.30622 | 2025-05-22 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| df587b03-fe3d-3eb5-906c-a8a0b431b9f3 | -17.71035 | -47.49368 | 2025-05-22 03:57:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93e2125d-89f1-38a9-837b-f0ab98ec7369 | -17.66652 | -46.68224 | 2025-05-22 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5355612-576e-3ce4-bd56-e8e22884be60 | -13.78435 | -54.31823 | 2025-05-22 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eefab824-4db4-3acb-90bf-26079d6ba177 | -13.66888 | -53.94105 | 2025-05-22 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| faec1d19-3468-3f03-8b07-0aaa77cd7565 | -14.03538 | -53.38213 | 2025-05-22 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0b125b86-ddff-3d71-bf20-c147317f75be | -17.62061 | -54.17008 | 2025-05-22 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21dbd6d8-2f23-3315-99a4-82d6407e40ea | -19.50858 | -48.6651 | 2025-05-22 03:57:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 714d64c9-0a51-3f60-8daa-b677736c8f0c | -17.91675 | -45.52765 | 2025-05-22 03:57:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07ecc408-aa81-389d-9025-b3167fdbbaad | -17.15551 | -54.01124 | 2025-05-22 03:57:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3addcced-b5e4-3aeb-be83-e16a66a5d228 | -22.90255 | -43.75528 | 2025-05-22 03:57:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e6a4eab8-d64b-3666-b3bd-22c2ebfb96ea | -22.88346 | -42.05274 | 2025-05-22 03:57:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 64440a63-61cf-3a19-8ddd-d50511ebe40b | -19.06537 | -53.46198 | 2025-05-22 03:57:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 42817e6b-7c79-32f5-9df5-5982ce9f2d16 | -14.032 | -53.38327 | 2025-05-22 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0524a75b-ac02-3be1-b243-d37eec0ad4fc | -19.36673 | -47.62143 | 2025-05-22 03:57:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fed72686-4fa1-3b6a-82a4-e86a741cc7dc | -18.91105 | -47.0132 | 2025-05-22 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 337d4dd7-4520-3d3b-912c-eba4b12a9d2f | -19.97531 | -47.18933 | 2025-05-22 03:57:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0c61e47-e4a6-3c8e-9505-c79c143df582 | -17.61925 | -54.17591 | 2025-05-22 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cc9e5d64-aa6c-3405-83f0-8088a1f4edad | -22.67851 | -42.85593 | 2025-05-22 03:57:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b8298d9c-72e6-37cf-83c5-c05e036f7a3e | -21.21942 | -48.60942 | 2025-05-22 03:57:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README9.md)
