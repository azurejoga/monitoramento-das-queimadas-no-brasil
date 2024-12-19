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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d3bedd7-3af9-3a5c-a6a0-1f713aa245b3 | -5.17719 | -37.5865 | 2024-12-19 03:44:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 55cfa66d-782e-3af9-b0af-5831e187079d | -5.20003 | -37.69003 | 2024-12-19 03:44:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7ff28da9-392c-3b91-98d5-156e3da1d787 | -4.4796 | -45.42819 | 2024-12-19 03:44:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f2dd85f-5807-3bab-ac23-51232dc8fac8 | -7.9064 | -35.24236 | 2024-12-19 03:44:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a7f70118-825c-3de7-9e65-7f74630c540c | -7.15849 | -34.8685 | 2024-12-19 03:44:00 | NOAA-21 | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 29273bc1-32aa-3a72-a711-a9fbd5e39580 | -5.93575 | -37.94371 | 2024-12-19 03:44:00 | NOAA-21 | RIACHO DA CRUZ | RIO GRANDE DO NORTE | Brasil | 2410702 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9864f418-1fa1-355b-9bb7-729e646f466c | -4.33345 | -48.29905 | 2024-12-19 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68cfeaba-1749-3186-a83d-cb0ec3e36f28 | -8.32606 | -38.53327 | 2024-12-19 03:44:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 02aaa32c-c37e-3a82-9e47-72b0246bc282 | -4.34668 | -48.46582 | 2024-12-19 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc664843-360a-3cd6-9992-7237f77a33ae | -8.84151 | -35.7041 | 2024-12-19 03:44:00 | NOAA-21 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b6ba967d-6d53-39ca-802c-dd5c8c060a4f | -8.43631 | -36.7027 | 2024-12-19 03:44:00 | NOAA-21 | ALAGOINHA | PERNAMBUCO | Brasil | 2600609 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b8965e87-4311-3dfe-8c53-d71ff3d97c8e | -6.29584 | -46.04494 | 2024-12-19 03:44:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a3fa436-1df0-3a31-b6f3-1483a958b18e | -5.38993 | -40.67267 | 2024-12-19 03:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 06d3c6d4-69a1-3779-ad39-ad7708c80688 | -9.38389 | -35.95391 | 2024-12-19 03:44:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 87ff3333-c1e9-3b8c-b553-4becde534707 | -8.84097 | -35.70757 | 2024-12-19 03:44:00 | NOAA-21 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ebfa5b18-fb2c-35e9-ae1c-30f66fea5f54 | -7.90309 | -35.24184 | 2024-12-19 03:44:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| fab76744-739e-3be0-bf49-d6bff126bf41 | -4.79698 | -44.02813 | 2024-12-19 03:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6c09a4d4-6c40-39f4-b218-100b018167af | -9.73564 | -36.16396 | 2024-12-19 03:44:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e02eadae-a2b9-3434-985f-8ba60b8ae446 | -5.90941 | -46.23132 | 2024-12-19 03:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22a7c9c5-ac9e-303c-9e53-d56e8aa2c567 | -5.31924 | -39.45367 | 2024-12-19 03:44:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 21d6b8bc-c75c-3279-8f3a-385d3236118a | -11.96344 | -41.3293 | 2024-12-19 03:44:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 646f8c94-d427-32bf-b8f2-32639a3a0225 | -4.78084 | -46.39479 | 2024-12-19 03:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 17769016-1614-34b6-8327-730d06687eb1 | -9.23643 | -35.69896 | 2024-12-19 03:44:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8947beae-0bde-3075-8cde-244dfc103c89 | -6.50169 | -39.58661 | 2024-12-19 03:44:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 84e18fcb-07a8-3454-9e15-6d71f0324228 | -8.39002 | -37.76923 | 2024-12-19 03:44:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 56e5d7ca-6c63-3f7a-a568-89614c621b55 | -5.93203 | -35.62539 | 2024-12-19 03:44:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 056203c5-183a-3b17-905f-d173e6f491d0 | -7.09512 | -39.03658 | 2024-12-19 03:44:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 2cc4caa8-40cf-335f-b09e-2df764f6008d | -5.4153 | -36.78259 | 2024-12-19 03:44:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b85b1d51-2a69-3c32-abeb-cc7ce5a40a85 | -5.02741 | -40.95366 | 2024-12-19 03:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 26c53f59-f3bc-3bda-a0c4-fb91ffb01cb7 | -20.16653 | -40.20236 | 2024-12-19 03:46:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d41a405d-0688-3bc5-b722-cff6137936c3 | -16.35034 | -43.69484 | 2024-12-19 03:46:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d018c69-34af-3273-a016-11b61987a61e | -19.43767 | -44.3406 | 2024-12-19 03:46:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eecdde36-8b4a-3a8c-b322-068499b6ac96 | -20.77939 | -49.85839 | 2024-12-19 03:49:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 86dc1a12-e0aa-3abb-8614-f08b4fab8cd3 | -20.76188 | -46.76997 | 2024-12-19 03:49:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 668f0fee-ee4d-341b-b93a-80e96842170c | -19.06509 | -52.8863 | 2024-12-19 03:49:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1f8c9d4-53a8-30ed-ae8c-d6a6acdb5e5f | -19.06153 | -52.89208 | 2024-12-19 03:49:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0d0822f1-34fc-33b9-833f-963b02bbe9cb | -23.70514 | -46.478 | 2024-12-19 03:49:00 | NOAA-21 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 51294e46-0f47-3bd2-bed0-d04acba79b5a | -19.06347 | -52.89315 | 2024-12-19 03:49:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e6d8db57-ebca-3855-8359-b70c59d43f1d | -19.35737 | -49.19778 | 2024-12-19 03:49:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8461b9f8-7a79-3fd2-b6ae-ed5f615afe8a | -20.78033 | -49.85421 | 2024-12-19 03:49:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 98c47de8-c7f6-3933-9d5b-59d3fdc7ebbf | -22.20085 | -53.16132 | 2024-12-19 03:49:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 33593ee9-4147-3e03-8a14-cfacad36bf73 | -23.40722 | -46.55601 | 2024-12-19 03:49:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ae85b82c-8d57-3064-8919-8a492ee3f961 | -21.61974 | -46.92478 | 2024-12-19 03:49:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d01d24ee-f34d-3819-990e-81654560ad19 | -22.20253 | -53.15453 | 2024-12-19 03:49:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 05df9f77-9635-3cfd-87ff-2955c73f98db | -19.0632 | -52.88525 | 2024-12-19 03:49:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0ff16d60-e6e1-3f39-8fce-e9f7b3eaacae | -19.67747 | -45.90949 | 2024-12-19 03:49:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 867128f4-840f-3ead-a52f-e0ea97dc62e6 | -23.32464 | -47.62548 | 2024-12-19 03:49:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1edbab95-b676-3827-ac3d-65c4fa8c19c3 | -22.54963 | -48.37082 | 2024-12-19 03:49:00 | NOAA-21 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4656dc5c-4c49-3b56-abf5-1a5d4ca087ab | -22.5503 | -48.36768 | 2024-12-19 03:49:00 | NOAA-21 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7eae724-3827-3aca-8853-d5af1a87893f | -21.59448 | -48.49157 | 2024-12-19 03:49:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce81fd55-747e-3465-8117-7f99a2916d01 | -28.15101 | -51.85366 | 2024-12-19 03:51:00 | NOAA-21 | SANTA CECÍLIA DO SUL | RIO GRANDE DO SUL | Brasil | 4316733 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1308e465-e8c4-383d-827a-a31114466fb0 | -30.33467 | -50.28062 | 2024-12-19 03:51:00 | NOAA-21 | PALMARES DO SUL | RIO GRANDE DO SUL | Brasil | 4313656 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| eabc0a0c-c0b9-3ff7-aa39-5e19a787cdb9 | -1.75297 | -45.82152 | 2024-12-19 04:06:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f5f00a1-5a2e-3b0f-b42f-575fb90b139e | -2.87718 | -45.24782 | 2024-12-19 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b68df2b2-a12b-3522-a754-8acc29b88e95 | -4.888 | -41.39894 | 2024-12-19 04:06:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 49c6f249-7399-34b0-af06-04d4b1594929 | -4.8825 | -41.41228 | 2024-12-19 04:06:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9b57efc1-21f0-3c59-abe3-1470e28e6adf | -4.92576 | -41.32674 | 2024-12-19 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d70c9636-4690-369b-a7d7-9860495a3a33 | -1.6046 | -47.1776 | 2024-12-19 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6ff3496-ea41-3458-983f-fd90864b2add | -4.88522 | -41.39495 | 2024-12-19 04:06:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2e0e4a02-be12-3676-b463-c37c41be0fd8 | -4.13184 | -48.1343 | 2024-12-19 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f21f5d4a-dab5-33e5-ae34-053f7a3755c3 | -4.91688 | -41.31826 | 2024-12-19 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 86e74a48-d5d2-34fb-9810-f76cea714147 | -3.02423 | -40.38419 | 2024-12-19 04:06:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c9308f4b-6027-3c0c-bdda-e888b4108a88 | -4.25753 | -43.45044 | 2024-12-19 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecde7c1b-10eb-3bcb-af56-6e5b2dd95da0 | -3.39881 | -42.2745 | 2024-12-19 04:06:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c029497e-d341-3dc4-9b31-78fe9fe3edbb | -3.84958 | -40.45179 | 2024-12-19 04:06:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fde813c6-aa49-3766-9fc0-e4b582d74d59 | -5.34127 | -37.45074 | 2024-12-19 04:06:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1e8976f2-b481-3975-b38b-5e0c2b8a6e87 | -5.17383 | -37.59371 | 2024-12-19 04:06:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e841224d-06b9-380a-b93f-5f8531499bdb | -4.11962 | -43.56532 | 2024-12-19 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4174d64f-782e-383e-bb41-75681846ca8e | -4.87744 | -41.37955 | 2024-12-19 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a71214db-a842-30fe-9380-957e49de80a1 | -4.87025 | -41.38198 | 2024-12-19 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6239ab09-07b8-3187-820b-e7e4bef6780b | -4.32865 | -45.86998 | 2024-12-19 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7bc7c85e-e4e6-37e8-b731-53eef6271436 | -3.78377 | -44.06423 | 2024-12-19 04:06:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ab7f6f8-025b-3efc-b94c-0176141dfadd | -3.2209 | -42.07524 | 2024-12-19 04:06:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1c0c808-7b77-354c-a238-8095b1b393dc | -5.02553 | -40.95229 | 2024-12-19 04:06:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b0065db7-3f90-3ab5-b2e4-fc734408fa50 | -4.39817 | -41.43505 | 2024-12-19 04:06:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 10dd7f60-6a55-346d-9b86-b748a586e859 | -5.17824 | -37.58981 | 2024-12-19 04:06:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 304f92a0-8f0b-391f-af96-aa8ad6177ee3 | -5.17757 | -37.59427 | 2024-12-19 04:06:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a207c8a4-6680-3f4e-8c6c-55835cb82b9e | -1.83159 | -47.11163 | 2024-12-19 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc161c2a-5d31-3a1c-b34e-dae2bbe51b9d | -3.68503 | -43.75342 | 2024-12-19 04:06:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aca08579-5f55-32ac-84ca-4bd5fe21161c | -4.00109 | -46.54605 | 2024-12-19 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a7830aa-d2c8-3352-aca6-ab93e462e4b1 | -4.67462 | -43.29653 | 2024-12-19 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9ecd9f7-4ac5-3b98-95c2-2500368e198f | -1.75767 | -45.81855 | 2024-12-19 04:06:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 314c3e7d-d300-3167-9f41-064b13f48cfc | -4.86197 | -41.39133 | 2024-12-19 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0c9f3413-43c4-3e43-8182-35cb7b9992a7 | -3.85291 | -40.45231 | 2024-12-19 04:06:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4ffc01e3-c4cd-3c01-9c63-5e98d023c352 | -3.5915 | -44.54031 | 2024-12-19 04:06:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dcd694d-48aa-3200-a26c-a80c0621a88e | -2.84108 | -42.18039 | 2024-12-19 04:06:00 | NPP-375D | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b4c9084e-ea78-3361-978a-2c88171f59d6 | -4.86971 | -41.38545 | 2024-12-19 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c4fc5a93-da23-3a6e-887a-c5944eb6eab0 | -3.41861 | -41.85606 | 2024-12-19 04:06:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8e25ee1b-8fa6-3180-95a2-b11d4fdb3e8c | -2.87348 | -45.24517 | 2024-12-19 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc6bc00f-aef7-3fca-a961-f2b8ada30962 | -1.78683 | -46.8112 | 2024-12-19 04:06:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2dbd17b6-e1cd-3164-a822-be5fd44d5f50 | -4.12313 | -43.56588 | 2024-12-19 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9f111bc-1be5-30aa-becc-439a4f9c7843 | -3.22033 | -42.07879 | 2024-12-19 04:06:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f26f31b-8f91-3e3e-8f52-0e5f0ba4226d | -1.61023 | -45.85233 | 2024-12-19 04:06:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e00d2be-7f90-369b-9abd-a91aa935161b | -4.38738 | -42.14142 | 2024-12-19 04:06:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc501b70-000f-3462-b18d-c08c3a12f01c | -3.67362 | -39.57665 | 2024-12-19 04:06:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 988adb99-bf9e-308a-ab2f-7b4df296137b | -5.32148 | -39.45475 | 2024-12-19 04:06:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 59e34076-cd6b-3bcb-a055-c0e71ff21c6a | -4.71199 | -38.44873 | 2024-12-19 04:06:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a65fc23c-236a-35f3-9b40-c36812cfecea | -3.42168 | -43.16598 | 2024-12-19 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83aed049-38bf-3a5c-9dfd-cc53722caa78 | -4.87412 | -41.37904 | 2024-12-19 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b40fbcf2-17be-33e3-9df0-fc5e6d8e053d | -4.10215 | -42.8569 | 2024-12-19 04:06:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README7.md)
