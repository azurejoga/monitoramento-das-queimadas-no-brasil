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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22f471f7-13a4-38ee-9e27-f71790b88cd3 | -9.41111 | -48.41008 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 409d67c3-f581-3d0e-9fe5-88834adee7b8 | -9.04546 | -49.69204 | 2025-06-17 04:34:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45932e7a-1eaa-3388-9493-006f12f4ab25 | -9.41779 | -48.43263 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa0dd3e1-ad41-38f6-b633-2d7f955c1098 | -7.67922 | -44.5727 | 2025-06-17 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 292ddd57-6f83-3679-9a6b-50d3cf380d83 | -5.41674 | -47.56792 | 2025-06-17 04:34:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc0881e1-d1f1-32f7-b9b9-68a7031edf0b | -7.27612 | -50.0092 | 2025-06-17 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bae5e941-d7bf-3df5-8738-d95d36916a61 | -7.72009 | -55.14109 | 2025-06-17 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 18a2b42a-6855-3da3-88c0-5590c0fa2feb | -7.24715 | -43.09145 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2ce0702d-9a8e-34c2-8e6a-ccca35393d6a | -7.27956 | -50.00977 | 2025-06-17 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 800d8e0c-b0ea-315a-90ab-6cb30f460976 | -7.26689 | -44.6371 | 2025-06-17 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09e7de16-41d2-3369-8da0-a9f9497c9704 | -8.60886 | -45.01547 | 2025-06-17 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a67ef90-3806-38b1-8790-69f757758367 | -7.23204 | -43.08195 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5a7fa105-255a-3dee-8f75-3795e6b55793 | -7.27121 | -44.63336 | 2025-06-17 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf9aebff-f5de-37a7-a1d4-afd33e557af9 | -4.37989 | -48.07218 | 2025-06-17 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11d25b3e-eb90-3255-a63b-13c3e79dbc96 | -4.00205 | -43.24139 | 2025-06-17 04:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2ca2ff3-4b7c-353e-bb46-b5fb72f833d5 | -6.85782 | -47.83092 | 2025-06-17 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f06a8ffc-0563-332f-974d-bce7ceed9f1e | -7.18188 | -43.60936 | 2025-06-17 04:34:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6c08441c-002a-37a7-98fe-b73b719ee2e1 | -6.29049 | -44.23075 | 2025-06-17 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e1eb2335-337f-3f79-8035-df039f702f53 | -6.73438 | -49.64267 | 2025-06-17 04:34:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e94ce6d2-a009-33d0-82e0-6301140e1af6 | -6.48831 | -42.8493 | 2025-06-17 04:34:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 03bef2f8-9f11-33cb-bb4b-84f877d176e4 | -7.28284 | -50.00662 | 2025-06-17 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99f011a1-5075-342c-b666-40c6e17be6e4 | -7.27953 | -43.89474 | 2025-06-17 04:34:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c98cd8c7-9b46-384f-b9aa-3fd903255cd8 | -5.29243 | -44.71729 | 2025-06-17 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4aaa24e9-08c7-3972-89ff-7ed73e995baa | -7.54801 | -45.64702 | 2025-06-17 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 689cfe91-5d05-3a64-ac5a-01f8ea1a8032 | -8.13326 | -49.5893 | 2025-06-17 04:34:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb91c3a2-69a9-3ca6-a168-d97f8996fc92 | -7.07606 | -44.39154 | 2025-06-17 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d588c8be-cd56-3f74-ab6f-1511f26f0c93 | -8.07189 | -43.11048 | 2025-06-17 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| a696fc9d-b51b-3806-b027-f80b19dd3c2b | -9.39119 | -48.42838 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98383be4-bc5c-3f1d-ba89-473b63bd89da | -5.5697 | -45.20469 | 2025-06-17 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c288593b-86b7-336e-a613-a9299eb76869 | -8.51685 | -54.76814 | 2025-06-17 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 393b65a1-f049-3f22-8f56-a025d10703ce | -7.54919 | -45.63921 | 2025-06-17 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d77a30e-0b41-3689-b0dc-4c8a00e34476 | -8.07545 | -43.1147 | 2025-06-17 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 889311a0-31bf-33c9-9cb6-f1fdc39eb243 | -5.92319 | -46.8033 | 2025-06-17 04:34:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc379d2b-9f15-3ab8-a100-92f9513548cb | -5.5703 | -45.20078 | 2025-06-17 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 85512acd-5cf6-3dca-ad05-e9a34e4ba835 | -7.26257 | -44.64083 | 2025-06-17 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9fed176f-1cde-3227-9e45-d0627d6bc955 | -6.15821 | -48.06119 | 2025-06-17 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45ac4619-01ad-33af-8bdd-52d380882572 | -7.66798 | -46.08265 | 2025-06-17 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f034906-c64c-3c49-8143-de3716b2bc7a | -4.25059 | -47.58595 | 2025-06-17 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 918801c4-4286-3fb5-8c3e-335c75aa4028 | -8.54788 | -48.26253 | 2025-06-17 04:34:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef6c26cc-b595-3195-9433-266a83bd1148 | -7.86217 | -47.89302 | 2025-06-17 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dae7fca0-0ea2-3403-b729-51e29fc89866 | -8.70241 | -46.97351 | 2025-06-17 04:34:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc2c99c1-696f-37c1-9ae0-bea81e5d4e02 | -6.66586 | -43.1881 | 2025-06-17 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9144aba2-fe1b-303e-a478-3c8aa7ae016c | -6.29691 | -47.0056 | 2025-06-17 04:34:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ca7f36b-accd-366c-94a1-9d2a779a6c3c | -7.24012 | -43.08317 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c12c0e93-1ed8-3500-ad5d-efcb6e1f4eec | -6.16153 | -44.41852 | 2025-06-17 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9e06ec9-ea57-37d3-b220-fe04ffcc03c3 | -5.53505 | -45.29104 | 2025-06-17 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9611874-5aad-3ea8-9e3d-e87b6c355639 | -8.06728 | -43.11351 | 2025-06-17 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9631203c-6616-364a-8be2-30deb49b888d | -8.33926 | -48.45044 | 2025-06-17 04:34:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0f6ea9e4-4c93-34fb-8d6a-0c0e2fe9bb50 | -2.44698 | -47.50092 | 2025-06-17 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9caa6e7a-5d99-3e02-ab00-a2d7141ef353 | -7.64634 | -49.42344 | 2025-06-17 04:34:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cc26792-0859-3554-9685-3c0a8135bc61 | -9.39784 | -48.42944 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4462d436-0470-3ec4-99bf-674955877b4f | -7.23908 | -43.09021 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d87b5928-656a-3699-b90e-0bf739a7ad8e | -7.77186 | -47.646 | 2025-06-17 04:34:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7db902c0-b869-3640-8c11-8753bca84054 | -9.40337 | -48.41598 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67a76276-9499-305d-a022-bee4bb2e0b0c | -9.95388 | -46.30623 | 2025-06-17 04:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58d7868c-5175-3e48-b328-a8fd3db9b3b7 | -7.68294 | -44.57326 | 2025-06-17 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b849888-9c6c-38cf-9e0a-6ef0fbc8ed17 | -7.15008 | -44.09746 | 2025-06-17 04:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2bcbe618-dd4f-3fbf-9255-2ac76dddf4fb | -9.19896 | -49.69799 | 2025-06-17 04:34:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2dfb1ebc-4412-3f54-81db-c9603ec5caa9 | -7.2396 | -43.08668 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f68ebc31-24b9-375e-8256-a00f7b3f2445 | -7.04647 | -43.4183 | 2025-06-17 04:34:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2e92a40e-de94-30ca-ae69-82e19c471012 | -9.41724 | -48.43613 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8986fe0-3ead-3d22-984a-438bfe964e8e | -6.32964 | -47.33411 | 2025-06-17 04:34:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83dc2913-4fb7-36b2-bdc2-139e04db7374 | -8.55121 | -48.26306 | 2025-06-17 04:34:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb72e47e-eff3-3db4-8332-60d67d4b40d0 | -7.97105 | -45.94335 | 2025-06-17 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c8f1877-0c02-3ed5-b66b-816749ee50b9 | -7.19521 | -43.59944 | 2025-06-17 04:34:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adf3c167-5ba7-3fd6-937c-8566ebb04d30 | -4.64374 | -47.96749 | 2025-06-17 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b07fb7c7-a1ce-3a10-bb12-056a762967da | -6.66984 | -43.18872 | 2025-06-17 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c0d786a1-bc9a-32f1-b249-a0eae7df1a06 | -7.11127 | -47.84927 | 2025-06-17 04:34:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5e83e1b-4856-3d9a-8bc1-7b13683e8f5a | -7.28016 | -50.00603 | 2025-06-17 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27747e61-2e00-3bd6-9d3c-b8399cc9cde4 | -7.23392 | -44.76111 | 2025-06-17 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b722887-cb87-3678-be28-1fa94b228f0a | -9.41444 | -48.41061 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67be2c3b-62a0-3299-8694-2d06797fe88a | -7.10849 | -47.84526 | 2025-06-17 04:34:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30b3f693-860e-314c-ab7c-2322c825e53b | -9.38841 | -48.42435 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63eed3c5-43cc-3b3c-918c-4c2e4e2d23dc | -7.19572 | -43.59646 | 2025-06-17 04:34:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| beb7b22b-1d69-3e1b-8b1d-38911ceb5912 | -9.39451 | -48.42891 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| adade51b-bad1-3a4c-934d-d98f21366c90 | -6.22184 | -43.33077 | 2025-06-17 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 239eae08-a843-38cf-92d6-3b5340cd959a | -9.66898 | -48.77071 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a02c2411-7a95-32a5-858e-70a6c497648b | -4.55136 | -48.01683 | 2025-06-17 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3710d84-76f2-3512-a7f8-c6d9e79c155f | -5.61986 | -43.99764 | 2025-06-17 04:34:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71e4562e-864d-36a6-b6ca-b6da7bd9d47d | -7.24768 | -43.08793 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d5c7e45f-ebd4-31d7-96b7-2b193961df08 | -9.72343 | -48.31659 | 2025-06-17 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07f4b11d-ddf8-3814-9bf7-7fe640e73d82 | -5.53468 | -45.29202 | 2025-06-17 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48ee77cd-5187-3793-9a35-f98148474862 | -6.49237 | -42.84991 | 2025-06-17 04:34:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 79ee269d-4c67-3c0b-bc5b-c66bce337d99 | -9.6723 | -48.77124 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 360f89a9-7153-3049-9ba0-cb424719ee1c | -7.20073 | -45.35018 | 2025-06-17 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 264f1207-a775-309e-84dc-a7e7e6a4422f | -7.26992 | -44.64204 | 2025-06-17 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 159b2c7c-f6b6-3152-826c-d71cd1e65e06 | -7.1913 | -43.59882 | 2025-06-17 04:34:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9f182d2-6672-3e46-a823-3852551dec6c | -7.24311 | -43.09083 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9a8607d6-7231-3387-b850-3c16a5e39d6f | -7.25105 | -44.61667 | 2025-06-17 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65fcac57-8218-3710-8f2c-f41f8d94d318 | -8.72915 | -47.99406 | 2025-06-17 04:34:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3832553-e1a6-39e1-ae8d-668ff02226b8 | -9.32892 | -47.83607 | 2025-06-17 04:34:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6cf0a6c-0d41-33ad-ae44-af9c8825bda9 | -8.33594 | -48.44991 | 2025-06-17 04:34:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 013c76d0-4e29-3176-bc7d-6979954ef153 | -4.54747 | -48.01978 | 2025-06-17 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35e10f5a-803f-3fbd-bd0e-8fb451c6a0eb | -9.41667 | -48.4181 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73941a4f-e7ba-31c8-82ad-417a55459b8b | -7.41504 | -49.36454 | 2025-06-17 04:34:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 226bfa77-a705-3e56-afad-114a4d6ef1e1 | -9.20232 | -49.69855 | 2025-06-17 04:34:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e680fdca-9457-3dd8-aa05-e1c0fd31aa81 | -6.12256 | -42.52399 | 2025-06-17 04:34:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6eb7f5f8-01de-301c-85ed-f490687500aa | -7.45875 | -45.49656 | 2025-06-17 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a49ebb18-3c63-3352-b6db-ff06da84be05 | -6.50258 | -43.6393 | 2025-06-17 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e181251-5ba9-3771-ba34-2b271d9dc8c4 | -8.39205 | -47.46895 | 2025-06-17 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README12.md)
