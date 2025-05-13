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
| 3fa45dad-4782-3ba4-b993-e080299782c1 | -20.21268 | -46.74446 | 2025-05-13 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdfe37db-4a52-3e4a-b6f0-ecb822eb5b8e | -20.18233 | -46.55339 | 2025-05-13 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c74d1fc-8605-3cbe-8aa7-b8f75dbf5ed2 | -20.21798 | -46.75074 | 2025-05-13 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8466ba5c-6907-3d41-8227-e78d1b84c759 | -20.22169 | -46.73494 | 2025-05-13 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b96f1b5a-adb9-3b5e-b4a9-8e31c859b277 | -20.21917 | -46.74567 | 2025-05-13 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee7955cc-e3f9-39e4-a5ac-d39a3b0c4d55 | -20.21138 | -46.74999 | 2025-05-13 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 844fde92-3b55-379b-acea-c8c0b6d207da | -20.21679 | -46.75578 | 2025-05-13 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 945ea8d9-e32a-385c-aaab-7064a20343c6 | -8.07 | -43.1216 | 2025-05-13 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| cdecad85-de22-38b3-9ba2-e24399cb3ea2 | -8.0889 | -43.1196 | 2025-05-13 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 6619dd7b-b8a2-390f-955a-407ed8797d98 | -13.9902 | -56.8058 | 2025-05-13 03:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 18dc5dbc-0e82-357e-bd8c-90cc755dd743 | -13.971 | -56.8077 | 2025-05-13 03:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 937eee3e-1f30-3044-8fa8-4652c98c54e5 | -8.0696 | -43.1452 | 2025-05-13 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| a29071e0-eb9a-3752-a402-69d028074f19 | -13.5683 | -52.8783 | 2025-05-13 03:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| b064995f-4565-3708-bcc4-e4e9bb5f6edf | -8.0889 | -43.1196 | 2025-05-13 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| e9933787-92cc-3dac-80b2-c9147f5100a6 | -8.07 | -43.1216 | 2025-05-13 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 124.2 |
| bfea40f4-0615-3766-84aa-a892d9e374a7 | -8.0696 | -43.1452 | 2025-05-13 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 8260ad64-eb3a-3358-adad-01ff04d01bf0 | -13.9902 | -56.8058 | 2025-05-13 03:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 261b4c82-fa33-3025-a823-1db603f00f08 | -13.5683 | -52.8783 | 2025-05-13 03:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 955451a3-0aeb-3380-bcba-91c6402ef133 | -13.971 | -56.8077 | 2025-05-13 03:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| beeb133b-570f-3387-be86-c567f20001de | -3.77505 | -41.66178 | 2025-05-13 03:47:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cc8d2fe9-20eb-3e32-95df-500a4c1eec97 | -3.77922 | -41.66246 | 2025-05-13 03:47:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d7b9276a-7511-3f67-9501-3cef42aa2e04 | -3.77089 | -41.6611 | 2025-05-13 03:47:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc0c1d77-8045-353e-9eb8-bcaf08cf1fe5 | -10.54025 | -42.45129 | 2025-05-13 03:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8a6e89df-b811-35b0-9ffb-8bb7dd1c74cd | -10.54112 | -42.44628 | 2025-05-13 03:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9f8bac50-db0a-3a8a-aba6-921eca154942 | -10.4967 | -46.18212 | 2025-05-13 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 341ef891-513d-35b9-a6a7-439b554560d4 | -8.07002 | -43.13016 | 2025-05-13 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| 34306f1e-713e-3c6b-8035-b08905cc574d | -10.66075 | -44.41122 | 2025-05-13 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 02d0a1ff-26e1-3f73-aa50-e1e6ba416e8f | -6.64194 | -41.99519 | 2025-05-13 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e0d67dfc-7753-3513-a40e-4d5c4c88c403 | -8.49063 | -36.58922 | 2025-05-13 03:49:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45e65531-8c3b-304c-956a-4fc1de21dc8a | -7.31646 | -35.29742 | 2025-05-13 03:49:00 | NPP-375D | PILAR | PARAÍBA | Brasil | 2511509 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 97323748-29f6-35bb-9b6a-43f3584e2f9e | -8.07929 | -43.12761 | 2025-05-13 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.9 |
| 24ef5f5c-33ae-31d6-b08a-42a352241ce4 | -10.90279 | -44.34333 | 2025-05-13 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8539cefe-e5e2-3220-b88c-e01667e0628d | -8.07072 | -43.12609 | 2025-05-13 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| 02424e45-963e-31d0-8f63-ed855e9e379d | -10.53411 | -42.43987 | 2025-05-13 03:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 40b0ab93-eb39-3413-a971-c6a443ef87bb | -10.00427 | -47.84137 | 2025-05-13 03:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d254876-d6ba-3300-9e08-8e0c488f5b0d | -6.21781 | -37.53879 | 2025-05-13 03:49:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a359bf11-7c37-3100-9afb-1e2c2edf936b | -6.21836 | -37.53528 | 2025-05-13 03:49:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8ae14215-9b82-3df5-99d6-0802e74e0ebc | -6.65068 | -41.99301 | 2025-05-13 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4db8c475-f183-33c3-8307-163e7b5249b9 | -10.48822 | -46.18328 | 2025-05-13 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de019851-9303-3468-a276-6add0c3b1acd | -10.53499 | -42.43486 | 2025-05-13 03:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4ff0e034-59e8-3f7a-a262-5dce68a057ea | -10.49166 | -46.18116 | 2025-05-13 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d942de5-09d1-37cd-a882-53f17592c4a2 | -10.5477 | -42.43188 | 2025-05-13 03:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3660f992-54d4-30a3-8beb-ddd60f24174c | -8.92602 | -36.19552 | 2025-05-13 03:49:00 | NPP-375D | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fbc23951-3839-37a9-9931-648811e8a3e0 | -10.00351 | -47.84532 | 2025-05-13 03:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21a0f932-d156-3f98-9ca7-d7372b830ad0 | -11.1182 | -43.34096 | 2025-05-13 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fd386af9-5e8e-3345-8578-bb04ec88f568 | -10.49382 | -46.18117 | 2025-05-13 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc1b61ab-4e78-3a14-b1b2-f355847b3552 | -8.07501 | -43.12684 | 2025-05-13 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| 2a88c9e0-781d-318b-836e-9db1a6c9c2e6 | -8.07431 | -43.13092 | 2025-05-13 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| 4a1255b5-42be-36f9-88d6-eaea4a987a4a | -7.88593 | -37.36726 | 2025-05-13 03:49:00 | NPP-375D | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2ad5a977-0ea3-33ea-afc2-2571f4ad8394 | -10.53806 | -42.44057 | 2025-05-13 03:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6cd5708d-2f7b-3ea2-ae1b-2e084d0ca869 | -6.65128 | -41.98943 | 2025-05-13 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6d79d47b-153d-3aca-85cd-2d577608816a | -8.07859 | -43.13168 | 2025-05-13 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.9 |
| 896e760a-4f5b-3461-bae1-f0630d2398d4 | -10.65629 | -44.41035 | 2025-05-13 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 946f307f-3d6d-334c-a550-17071c160694 | -6.64255 | -41.99159 | 2025-05-13 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 02ff1370-48ed-3255-b547-53d3e84f5c20 | -10.53718 | -42.44557 | 2025-05-13 03:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a0f607ae-96ab-3844-b0ef-b998fb3e9132 | -7.21447 | -35.77656 | 2025-05-13 03:49:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e80c96af-bf81-32f5-b602-d5c69b56bea3 | -7.10994 | -36.49068 | 2025-05-13 03:49:00 | NPP-375D | JUAZEIRINHO | PARAÍBA | Brasil | 2507705 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2cd4dd92-81e8-3fea-a791-8f1a4aedd411 | -13.5683 | -52.8783 | 2025-05-13 03:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 24207214-1912-3b3c-8b1b-f017815c3fc9 | -8.0889 | -43.1196 | 2025-05-13 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| fc9f19cf-69d4-3eac-a706-5925d645e227 | -13.9902 | -56.8058 | 2025-05-13 03:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 698f9102-7928-39cc-85f0-4a0c8793cb8f | -8.07 | -43.1216 | 2025-05-13 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| e0e21b86-b91a-34dd-9652-26c23b34bb3b | -13.5686 | -52.8573 | 2025-05-13 03:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| dfc8eee6-36cd-356e-b049-d765fbe01d19 | -13.56447 | -52.8911 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8b459a29-ec67-305a-9c6f-82b7754d3b62 | -14.1894 | -45.4822 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c871bf7c-32d9-302d-993d-2106bdd54850 | -13.56605 | -52.88379 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b7f0f163-9fe7-392f-bd33-c5b7e5a72cda | -14.18551 | -45.48381 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06143939-8ebc-33a0-ae10-7346e56a386c | -11.80164 | -44.28051 | 2025-05-13 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d11187c-44a0-32f5-a2fe-f921fefbbd52 | -14.18209 | -45.47113 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de82622f-ba24-30a3-8a55-da5b0602bbb3 | -14.18659 | -45.47205 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9a15806-1843-3bdb-bf9f-5672f2315b8a | -15.4119 | -41.4228 | 2025-05-13 03:51:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 831e4ce4-19f0-36ff-9fdf-aaf23a916b50 | -13.54813 | -52.87152 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f6a6e9ee-f90b-3b0d-9800-4e26ab3ea5b0 | -14.19025 | -45.47758 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b742c31b-9f80-3a4b-ab01-83d7f05534f8 | -11.77496 | -48.205 | 2025-05-13 03:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31c34ae6-e533-30c0-a03f-68236496be3c | -17.11278 | -49.14046 | 2025-05-13 03:51:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63422ad8-563b-3500-8538-ad3bf3793e6d | -12.18594 | -46.71538 | 2025-05-13 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 476ca5f4-8613-3c64-93db-6806f42d9807 | -12.15333 | -48.00948 | 2025-05-13 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 71a0fd92-a336-3b89-8f1e-691130a7704d | -15.0766 | -48.94548 | 2025-05-13 03:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 118c52e5-f6a0-3b24-b298-c3c31b9f9baa | -13.56089 | -52.8817 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a0d33160-c6c0-34db-b654-a321fb38584f | -11.78766 | -47.35517 | 2025-05-13 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00648564-c240-3667-93ed-53fdb675f759 | -12.17417 | -44.34142 | 2025-05-13 03:51:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9b38466-93ba-3635-82db-93f7cc843e0c | -13.57466 | -52.8787 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f734f3a-da4f-3c4c-a974-129733e0cd65 | -11.61823 | -48.11405 | 2025-05-13 03:51:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 568a4d14-9fbd-3ec0-b9c9-f04e0d6cb158 | -11.80239 | -44.27628 | 2025-05-13 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfb8bd7c-76d6-3410-8eff-2bb1cefc146e | -12.1471 | -48.01205 | 2025-05-13 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 61870f45-0370-36f0-8736-ab75ff65a801 | -14.63837 | -45.09885 | 2025-05-13 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6813004-160f-370e-a33e-5511ec7d6e31 | -13.56636 | -52.89085 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a2aabd47-7e4c-3c42-867b-40a2fbd777de | -12.191 | -46.71643 | 2025-05-13 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8902df7d-e6df-305b-8ba7-5aac259e9e81 | -11.58341 | -47.61429 | 2025-05-13 03:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5c01dcb2-dab1-3fe1-9e1d-74f42d44bfeb | -13.5676 | -52.87664 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 931e37de-e8ea-39e1-a020-98ad782c6d46 | -13.56958 | -52.87641 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d0e7fb5a-1222-3f43-aaeb-f1e6ca76b980 | -14.19391 | -45.48313 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6f16413-603c-329c-87f0-2b258c2f2286 | -14.66492 | -45.12655 | 2025-05-13 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e0eb76f-0d8c-33a2-8459-86308af9d229 | -11.99783 | -43.78318 | 2025-05-13 03:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99c2341e-344b-32f3-a98c-dcbd10a03b40 | -13.57626 | -52.87128 | 2025-05-13 03:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9eca74a-5f94-3e91-8008-ef1543f15eb1 | -14.18294 | -45.46652 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8cb14eb-47ea-3642-8bf7-c983a93b8891 | -14.18728 | -45.47458 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 331c79b7-08a2-3f47-81e1-b6b866cabe98 | -11.61014 | -48.00551 | 2025-05-13 03:51:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07849f93-ac6e-3fae-88df-16c2f21fa2e2 | -15.78084 | -43.34438 | 2025-05-13 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54bd5cac-e2f1-3799-a522-ba1749a5e414 | -11.58271 | -47.6179 | 2025-05-13 03:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d20d8a8-a8bf-3b5b-98ab-9b30e2a553f7 | -14.18575 | -45.47667 | 2025-05-13 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README5.md)
