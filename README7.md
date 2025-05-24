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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 952859bc-976e-36fb-bbfc-fb0182bc31f7 | -17.5957 | -43.19786 | 2025-05-24 03:47:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ea2e9be-cb3f-3461-bb8a-825e13041edf | -12.37869 | -49.9929 | 2025-05-24 03:47:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f7412a61-e7da-313c-a67c-775b5049c24c | -11.39255 | -47.96121 | 2025-05-24 03:47:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb55946b-ac2e-3ca3-af18-4e734832c7e1 | -19.43786 | -44.33985 | 2025-05-24 03:47:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8580584-5199-3e57-a9b4-88b7db52459f | -12.37829 | -49.99215 | 2025-05-24 03:47:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9d0ba0cf-bbfd-3027-bd15-e5f5c8a0fb47 | -12.07533 | -48.4581 | 2025-05-24 03:47:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bc918fd-34e0-3399-903e-8ebb4500b177 | -18.34602 | -45.59158 | 2025-05-24 03:47:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc425834-a5f4-3348-88c4-a4094b4c80f7 | -12.35491 | -49.93366 | 2025-05-24 03:47:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb56e424-3ebc-3190-9aa5-c7e6df64e4d2 | -13.45736 | -47.47859 | 2025-05-24 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cf23c0e-6d6c-3a7a-bff7-008cf50314c1 | -17.59626 | -43.19864 | 2025-05-24 03:47:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 040764fc-82fd-3aa9-8bb5-18f82a53af82 | -12.07141 | -47.34948 | 2025-05-24 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 596e0df2-0dea-338c-80d1-aea34e2e21cf | -23.18452 | -52.11093 | 2025-05-24 03:47:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6db67477-8d6f-3d6c-b6ff-82ab80daecad | -10.95033 | -48.15475 | 2025-05-24 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7871e3dc-22e1-3673-b641-bb38a6cadcbd | -11.79634 | -44.28561 | 2025-05-24 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94736c90-11de-358e-8c11-40a06050b739 | -14.65491 | -41.02792 | 2025-05-24 03:47:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| feaca91c-ad98-3054-b223-858f780bcf01 | -13.45646 | -47.48304 | 2025-05-24 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3023872-9747-393b-aab9-576a2a6b8747 | -23.33951 | -46.77133 | 2025-05-24 03:47:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5e0aebd3-ebc9-30e6-892c-5c61118ce04b | -11.57563 | -47.61751 | 2025-05-24 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6155ede-9492-377e-83bc-d3cc91598cb3 | -12.39507 | -49.98271 | 2025-05-24 03:47:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 540c6666-1434-31ac-92c8-6eaeb7333835 | -12.07054 | -47.35384 | 2025-05-24 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 922f1b04-eed9-3498-9797-814b586d7967 | -15.69948 | -42.25733 | 2025-05-24 03:47:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35ffb4b3-ffc8-371e-8bd0-b56c047f94e0 | -12.83343 | -47.39691 | 2025-05-24 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8eb5d1f-2361-3cad-86cb-3bf7e82a0f89 | -12.35618 | -49.92757 | 2025-05-24 03:47:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36b1ceb0-93ef-307d-b4f2-be2c4b5e0357 | -19.1573 | -41.56857 | 2025-05-24 03:47:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2f109238-a6ab-35c3-bbb8-b27fbea1c591 | -12.35692 | -49.9286 | 2025-05-24 03:47:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| deff496f-5d3c-35d0-8db2-8b91b72e1c00 | -14.22821 | -44.6286 | 2025-05-24 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c57fcd4-1f68-36d7-86ff-65153364d6a4 | -21.2188 | -48.61356 | 2025-05-24 03:47:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b4bb16f9-23c2-3763-be77-647bf930aa64 | -12.83426 | -47.39278 | 2025-05-24 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7267f327-7820-3c11-b858-6ea4f12f786a | -12.07228 | -47.34513 | 2025-05-24 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b33075ea-a878-3151-9018-94eacc506b98 | -22.53958 | -48.81139 | 2025-05-24 03:47:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e1e3056-b420-3e1a-bdcd-89804537d5d6 | -12.40185 | -49.98426 | 2025-05-24 03:47:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7f58705f-2151-37ea-a80e-f57e9128aed0 | -18.03959 | -39.92684 | 2025-05-24 03:47:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8057046f-3ee9-3966-96c1-0f7296028b14 | -19.8333 | -40.11368 | 2025-05-24 03:47:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2b739310-5ab1-3a56-bdc8-b182edca6780 | -12.07431 | -48.46313 | 2025-05-24 03:47:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70ded854-b6fe-37c7-8548-c3a30f3242df | -16.30464 | -42.77621 | 2025-05-24 03:47:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5dc5a13-5dbf-3109-9540-b073f6f35d46 | -12.07727 | -47.35064 | 2025-05-24 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20ad6a4e-c208-3dfb-b634-fc6957c05e3f | -14.23198 | -44.63459 | 2025-05-24 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 677b7ff3-912b-34d0-92f9-08d033e02003 | -12.4005 | -49.99065 | 2025-05-24 03:47:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dfbcb257-46f9-3f58-8510-557090b084e2 | -13.46217 | -47.48447 | 2025-05-24 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c21e50d0-5537-3664-9274-f1b178fc59d8 | -14.22724 | -44.63368 | 2025-05-24 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 804d9fba-afcb-33e1-90b9-c1a73ede3abe | -12.06554 | -47.34834 | 2025-05-24 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ef07eb4-d3cf-3f3e-86c2-aa87d0b00b41 | -12.40879 | -42.52951 | 2025-05-24 03:47:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b99c0c28-0e2d-3d1f-acdf-76878e6588b4 | -11.56435 | -47.45765 | 2025-05-24 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04e45d5b-4896-35b6-a13e-8a25ba419af4 | -11.39159 | -47.96598 | 2025-05-24 03:47:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f863f63-d0dc-3a7a-8672-0da84fcfb606 | -12.27717 | -44.59867 | 2025-05-24 03:47:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd596648-27b8-3df3-8e55-92efef5ca9a1 | -12.40315 | -49.97811 | 2025-05-24 03:47:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 684611af-4600-3d9b-8baf-6809564e1113 | -12.40454 | -42.52871 | 2025-05-24 03:47:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| de680e5f-a8af-3c1a-a444-7cb1e7dd5838 | -12.06467 | -47.35268 | 2025-05-24 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5ea0de51-506a-399f-a2f5-74be48702c0a | -19.76242 | -40.875 | 2025-05-24 03:47:00 | NPP-375D | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0bbfcb52-1b14-31f6-b0a9-b27d16d40b0e | -12.07814 | -47.34629 | 2025-05-24 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6809fedc-8e87-3ddf-8e35-9d0a829b64b5 | -12.38007 | -49.98642 | 2025-05-24 03:47:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 33fda222-c81b-30be-b9d0-4c3477d2ab89 | -17.595 | -43.20157 | 2025-05-24 03:47:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7acc32b-f909-3be3-9864-62c55e7e94c7 | -20.4441 | -46.37376 | 2025-05-24 03:49:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b25a0696-5233-35de-9822-7c28d55d093c | -29.61262 | -49.94497 | 2025-05-24 03:49:00 | NPP-375D | TERRA DE AREIA | RIO GRANDE DO SUL | Brasil | 4321436 | 43 | 33 | nan | nan | nan | Pampa | 4.0 |
| 47ba3c4d-659a-36a1-b5af-392afbed02dd | -20.44439 | -46.37004 | 2025-05-24 03:49:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 167aa7ac-e931-31cb-b67b-ec121537e590 | -20.44878 | -46.37492 | 2025-05-24 03:49:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fa7da68-d151-32eb-9482-3a678b85de7f | -19.51425 | -44.27697 | 2025-05-24 03:49:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 806b1e1b-7375-392b-9fb6-b46656e08007 | -20.34848 | -40.35961 | 2025-05-24 03:49:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d1e79e67-3bad-3319-880d-e08eb0b6888e | -19.60155 | -45.02081 | 2025-05-24 03:49:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d79abaef-ab59-3b70-b6d4-630fbd6dbfcd | -20.40285 | -46.33245 | 2025-05-24 03:49:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a9b6e46-4412-3443-9ddb-abb30a7ab12e | -30.85231 | -51.45405 | 2025-05-24 03:49:00 | NPP-375D | TAPES | RIO GRANDE DO SUL | Brasil | 4321105 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| f2515521-9e03-32d2-b513-38368ba358cb | -29.60782 | -49.94351 | 2025-05-24 03:49:00 | NPP-375D | TERRA DE AREIA | RIO GRANDE DO SUL | Brasil | 4321436 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| bc8403e7-8943-3ff3-a820-2b1d685594e9 | -20.44799 | -46.37659 | 2025-05-24 03:49:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 394355f3-0253-37f2-a665-ec5068bbf285 | -29.60639 | -49.94316 | 2025-05-24 03:49:00 | NPP-375D | TERRA DE AREIA | RIO GRANDE DO SUL | Brasil | 4321436 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 3cab49d4-dce3-3b11-9f2e-473598018a74 | -20.44332 | -46.37535 | 2025-05-24 03:49:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fdfe6108-7196-32e9-a653-385d40975082 | -20.40176 | -46.3378 | 2025-05-24 03:49:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37246f29-f84b-333c-a616-133adb002c6b | -29.61119 | -49.94463 | 2025-05-24 03:49:00 | NPP-375D | TERRA DE AREIA | RIO GRANDE DO SUL | Brasil | 4321436 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 04353f58-ce07-3dfd-978c-1cd4cf840edb | -20.76256 | -46.77074 | 2025-05-24 03:49:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9d356e45-99d8-3333-a465-cd939621cf84 | -19.60241 | -45.01641 | 2025-05-24 03:49:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dfa489d9-bb79-3070-b51a-7ccc2cc3edb4 | -8.0889 | -43.1196 | 2025-05-24 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.8 |
| ccdb8991-10ed-3101-98be-9fae504c95b0 | -8.07 | -43.1216 | 2025-05-24 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| eea43ed0-fbd2-3858-aa1d-07f102f628bd | -8.07 | -43.1216 | 2025-05-24 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| ff508100-0402-351a-8b22-c145c15b40e9 | -3.42221 | -43.16421 | 2025-05-24 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 942615ed-7415-3eba-8f1f-351a4d00d7bc | -3.2753 | -43.54163 | 2025-05-24 04:04:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8b1a9fe-e838-34b5-b21d-c828aa9de2af | -4.17451 | -42.03267 | 2025-05-24 04:04:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c7d99d83-a37b-3f1b-9686-bd5db8b3373a | -6.68441 | -43.97029 | 2025-05-24 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b203b78-f05f-3e4f-a916-051c01874b35 | -7.22201 | -43.12205 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fd0bc74e-521f-3087-86bb-b9455d7f28d9 | -7.07155 | -44.93736 | 2025-05-24 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbcf6cbc-2ba9-3bb6-a9f6-03790fba3db7 | -7.20341 | -43.13018 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f37d083-5c2d-3cca-b081-1467100dc199 | -7.07083 | -44.94167 | 2025-05-24 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6bc158c-c267-3092-ad44-c1f0bc8e2d00 | -6.2172 | -43.35318 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9a0b32bb-4fc8-3921-8f3a-00316e843eda | -7.95116 | -46.82129 | 2025-05-24 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abf97810-ec4a-33ca-9928-daca9961fb98 | -7.11543 | -46.54437 | 2025-05-24 04:06:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1942f29-ed8d-38a2-82d9-1a6c31740af2 | -7.9949 | -46.97782 | 2025-05-24 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5141cc50-d06c-3f20-ba1c-bc3f5262fba0 | -8.07108 | -43.1213 | 2025-05-24 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0827f495-f1a8-3b21-a40f-1d8772500408 | -6.21839 | -43.34577 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44218c51-8fac-33ee-a2d3-f7ba778bf8fd | -4.82105 | -44.35497 | 2025-05-24 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b3cfd53-5864-37f1-a0c3-6ea66b7c843c | -10.55205 | -42.43119 | 2025-05-24 04:06:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 9ee07e50-4b82-3801-bd79-5c066abd5a75 | -5.57261 | -45.19285 | 2025-05-24 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22d7ec2b-57ec-3297-8b2c-63b9bb93cd78 | -8.07439 | -47.12576 | 2025-05-24 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b8a30ee-487e-368f-bc2d-dce3cb162217 | -6.22181 | -43.3463 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f784bc0-7134-3fd9-8df8-1d21d8e15d6e | -8.047 | -45.69357 | 2025-05-24 04:06:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 532032e3-63a9-3f89-b1fe-603227ae1e54 | -6.61407 | -48.01351 | 2025-05-24 04:06:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b2f8efa0-bd1f-351b-ac2a-d5d95d656fea | -8.07223 | -43.11414 | 2025-05-24 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 0e80013c-7c95-300a-b84e-4159df24e411 | -7.0672 | -44.93797 | 2025-05-24 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5872f3cd-19b8-3553-9bb9-09d40b19417d | -7.27214 | -43.24882 | 2025-05-24 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85644e6d-339b-3a3a-9259-7b173413bb1f | -4.81742 | -44.3544 | 2025-05-24 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ae090a5-8b4b-3cb2-81ae-cf6b815d4e4c | -6.22122 | -43.35001 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b134a376-3137-3cb8-a3d5-b302007adcae | -9.37467 | -48.40223 | 2025-05-24 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2511919c-b508-3c79-ac24-5c116e2a7691 | -4.28399 | -48.27108 | 2025-05-24 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README8.md)
