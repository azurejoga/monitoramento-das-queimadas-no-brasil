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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 754fc4fd-f029-3284-856e-1e0f42251837 | -21.80246 | -52.71382 | 2026-07-07 04:49:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2a559a5-6519-304d-b665-8712a5bb324e | -22.38122 | -49.7916 | 2026-07-07 04:49:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5de9b223-092a-3fa8-97e7-e9b902ee3b12 | -21.80577 | -52.71441 | 2026-07-07 04:49:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ecd3d127-148e-38e4-be41-2deae022e805 | -22.28023 | -46.86781 | 2026-07-07 04:49:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 380c8544-1c1d-3201-b1eb-6edf7abb6e25 | -21.50868 | -48.81798 | 2026-07-07 04:49:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 851563d4-dd12-3979-9456-fd0127b21e2c | -22.82919 | -47.14662 | 2026-07-07 04:49:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f153c64b-9786-3e09-8029-f02b0d625017 | -21.50875 | -48.82148 | 2026-07-07 04:49:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3820b519-5abf-3090-9532-752af913f61f | -21.05907 | -47.25985 | 2026-07-07 04:49:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0470275b-764d-3696-aa68-c3a5d693781e | -22.02637 | -48.22202 | 2026-07-07 04:49:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21093722-1aed-3d16-a3d9-ecea06801cb5 | -22.82867 | -47.151 | 2026-07-07 04:49:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 02e331b2-759f-3c90-a3a5-03d720da9f79 | -22.0257 | -48.22739 | 2026-07-07 04:49:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a8c2ae8-b2f0-39f6-bd5a-7e2e438d0a61 | -21.50941 | -48.81655 | 2026-07-07 04:49:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1898f17-b637-36ca-9ccf-3ba671532dbf | -21.06124 | -47.25947 | 2026-07-07 04:49:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b530420-437b-3a7a-af1c-423391355541 | -22.7874 | -49.34282 | 2026-07-07 04:49:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7ef7c3f-3805-3ee2-91a3-4d8e5ee5b4ee | -22.78804 | -49.33795 | 2026-07-07 04:49:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2be7b606-08d3-36a1-9419-d90597d49455 | -21.25366 | -49.17892 | 2026-07-07 04:49:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e6667cdb-5168-3f77-aa34-18009adccb11 | -21.25212 | -49.17609 | 2026-07-07 04:49:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 655cf50f-42c3-3231-bd6a-b43038f58734 | -22.37757 | -49.79104 | 2026-07-07 04:49:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 736e4a13-f5e5-389a-b600-ee2353e6f898 | -22.28075 | -46.86348 | 2026-07-07 04:49:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a362e104-b459-3065-b542-0c15ec1160c3 | -21.06323 | -47.26031 | 2026-07-07 04:49:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a779529-cf50-3b73-840c-8a527f1076e2 | -22.02305 | -48.22506 | 2026-07-07 04:49:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b53db1b-40c0-3d11-8011-1bc73a1cdade | -10.9393 | -43.0832 | 2026-07-07 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| a498c140-cce9-39d1-af95-250ce7001cac | -10.9397 | -43.0593 | 2026-07-07 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 89228ef7-e431-32b3-bfe2-c733faeb7dc4 | -6.9138 | -43.7049 | 2026-07-07 04:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 900666fc-874b-3246-aab2-7c44b00adb6e | -12.7944 | -44.4895 | 2026-07-07 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c242d21b-b465-3a54-bece-649bb219fa33 | -6.9326 | -43.7032 | 2026-07-07 04:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| d2251ff0-33ff-345c-b6ca-99b53ec40434 | -12.7944 | -44.4895 | 2026-07-07 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 4ae99f11-b2af-33d9-8de7-a80964ee9723 | -10.9397 | -43.0593 | 2026-07-07 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| a311234b-a71a-3b7c-9801-6ffd5214ba50 | -6.9138 | -43.7049 | 2026-07-07 05:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 8f8dbdd6-84fd-35b1-b300-6265e2edbe1e | -6.9138 | -43.7049 | 2026-07-07 05:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| e00d925e-b18e-3e1e-8f4c-5532f0099f01 | -12.7751 | -44.4927 | 2026-07-07 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 2416294f-8d41-3884-a8ed-677b954da9dc | -6.9326 | -43.7032 | 2026-07-07 05:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| db725bb5-c8af-3eb1-a053-bf20cd1911ce | -12.7944 | -44.4895 | 2026-07-07 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 48a79b3a-ac6d-3049-bc04-b534daff4dc6 | -10.9393 | -43.0832 | 2026-07-07 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 0cca5862-02eb-39d0-bf2d-55c1a469427e | -11.6597 | -44.5508 | 2026-07-07 05:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| bb92820f-b939-32c6-bc39-96eea0d9081d | -11.6592 | -44.5741 | 2026-07-07 05:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 26e4717d-06a4-34a4-b320-69892eb78aad | -12.7949 | -44.4661 | 2026-07-07 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 6d35cf55-f632-306c-a926-e0aa665b25dd | -11.6789 | -44.5479 | 2026-07-07 05:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 159.2 |
| b7d2666c-b20b-3027-865e-2ba260fbcc7d | -10.9397 | -43.0593 | 2026-07-07 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| af8b9437-bd06-3d39-8874-4672e928551a | -11.6785 | -44.5712 | 2026-07-07 05:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| b8a2cfdb-deb3-3d7b-8428-a979391e2d6b | -10.9397 | -43.0593 | 2026-07-07 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 195.9 |
| c3a86eb2-220d-39b8-94a1-9e072e9dc1d4 | -11.6597 | -44.5508 | 2026-07-07 05:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| d82a329e-6076-3008-b3ca-3edb09b3e831 | -11.6592 | -44.5741 | 2026-07-07 05:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 8a2cde3b-0a77-3dad-af6e-18cce03b0d7b | -12.7751 | -44.4927 | 2026-07-07 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 6bc19412-d92f-371c-9447-1f7927243b0b | -11.6789 | -44.5479 | 2026-07-07 05:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 7a203827-c985-3414-857f-e1942f44c113 | -6.9138 | -43.7049 | 2026-07-07 05:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 335cea5f-aecf-3ece-8c43-305a4159d7ea | -12.7944 | -44.4895 | 2026-07-07 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| aad7c8c1-319a-3ec7-88d8-29c57977af38 | -11.6785 | -44.5712 | 2026-07-07 05:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| ad730c99-9ecb-3790-b268-cdab4d245503 | -10.9393 | -43.0832 | 2026-07-07 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 0b24c0cd-28c6-3a1b-b15d-d4f73c514ef6 | -12.7949 | -44.4661 | 2026-07-07 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 7554e3c6-8cab-3636-a387-591eef072592 | -7.64527 | -50.02649 | 2026-07-07 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 428ff42d-980d-304e-8ee9-6ce50d1a4414 | -8.55558 | -63.36823 | 2026-07-07 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b41416d3-3ed9-3648-b0cd-4ecc6ab2fc15 | -8.5517 | -63.37121 | 2026-07-07 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d1dbdf2-cda7-3db5-8a2a-a017ac71ec4b | -8.55226 | -63.3677 | 2026-07-07 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 862fbc1e-7e2f-3ac3-adb7-1e3ca11659ce | -7.63831 | -50.02947 | 2026-07-07 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe7a4b77-482f-3272-bb54-be053fd3e97a | -8.55391 | -63.37877 | 2026-07-07 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12483b78-56ee-368a-8a6c-84df0a111335 | -9.01566 | -63.53648 | 2026-07-07 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c86f1343-7a05-3351-a109-065dd8678dc2 | -8.54894 | -63.36718 | 2026-07-07 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 275da2c7-10ee-3ef5-9730-18e33bed61b8 | -8.55502 | -63.37174 | 2026-07-07 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e846f8b-abec-3fa1-8a78-8f3605bdd41a | -7.63873 | -50.02565 | 2026-07-07 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10382c6b-198e-3e4e-a7fa-1b653f5eb11c | -8.55115 | -63.37472 | 2026-07-07 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70fe4898-0a38-3baa-95c3-0651c2061ec9 | -8.55447 | -63.37526 | 2026-07-07 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ad377b7-1364-3846-bb84-e143f890cef2 | -6.9138 | -43.7049 | 2026-07-07 05:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 7b1dcd54-a872-3b66-bd5b-f68062564c0b | -10.9397 | -43.0593 | 2026-07-07 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 199.2 |
| e52bfdab-81b1-3a6e-a665-86f103ee837f | -11.6592 | -44.5741 | 2026-07-07 05:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 23acf0dd-a599-3e76-98dd-f214b79b622a | -11.6785 | -44.5712 | 2026-07-07 05:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| c7c9fdab-3779-30e2-9e9f-e952b41b999e | -10.9205 | -43.0622 | 2026-07-07 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 3767e0db-15df-3d56-a46d-b6da6da4de3f | -11.6597 | -44.5508 | 2026-07-07 05:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 7e81ed83-41b7-3360-9fd5-9402ad9bab92 | -11.6789 | -44.5479 | 2026-07-07 05:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 90b6672f-fc67-33c0-8515-4c52734446f1 | -13.26264 | -54.33637 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5612d4a-124a-3c61-89a8-673ef8809c12 | -13.3176 | -54.37476 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02cd4d3b-cfe0-3703-a340-bb496cbad49a | -13.2717 | -54.35154 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5b103b5-3070-3e52-bacc-2db111a136af | -13.25828 | -54.33902 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76bbae3f-3b05-3b79-b3ea-9dffa4891a4d | -13.29869 | -54.35197 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9fc46ee-3381-3565-bc96-d3a1f42c2d91 | -13.26233 | -54.3501 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a2e50b2-5933-37b2-b273-e173ac9b56af | -13.27825 | -54.34176 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3401d711-ce81-369e-97eb-1b4d18b686fc | -13.25607 | -54.22364 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9501c646-ece5-3754-a2a8-f4eb1d11daf6 | -13.26595 | -54.23202 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb172dc2-351d-3570-91db-11e90c04e9c3 | -10.20506 | -61.48385 | 2026-07-07 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42dc1747-6145-35ea-bbc6-8e1825ba7979 | -18.0896 | -54.02927 | 2026-07-07 05:31:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13d80aec-b0bc-3829-a812-6a102ae0caf0 | -13.318 | -54.37141 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0897edcd-7df8-31a2-bd77-b9f6a3e9a906 | -13.30911 | -53.34434 | 2026-07-07 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ddb6c5c-2cd4-3798-90fc-f3f8a096a48d | -13.27663 | -54.35566 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc57297a-b25e-36bd-815b-c5c49393e4d6 | -13.2721 | -54.34805 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f29e7b8f-ad37-33dc-8f10-b72ac5be9a3a | -13.28727 | -54.35711 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d6663cb-56c9-3515-9c5a-388e92804e8e | -13.28436 | -54.33578 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b74705c4-4d5c-3bac-83c1-c7f4f9d0d734 | -13.28887 | -54.34348 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fb6aecf-faf3-3b52-afd5-d30c533ae19e | -10.10698 | -67.48546 | 2026-07-07 05:31:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b7111e0-c7ce-3d01-b6f3-11ae11061b3b | -13.28154 | -54.35985 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49b510c0-9aeb-3bbb-8052-c65120337178 | -13.29338 | -54.35112 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0955311-bfe1-3db1-8e4a-5f89ba9f4c8c | -12.84363 | -58.30564 | 2026-07-07 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27eac411-c9d7-3eda-8538-74e26768d4bd | -13.26717 | -54.34394 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2223e763-110c-3fd1-853c-5726e535658d | -13.26637 | -54.22858 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92b0818a-2353-32ee-8637-7d43acff84a7 | -13.26758 | -54.34046 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4731525b-78f5-3f0d-ab54-c63d0cdc95d3 | -13.25564 | -54.22714 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98212d26-d516-36d6-a304-d597d3519d6c | -13.28316 | -54.34602 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f4114a1-199a-3dc9-a577-32152d4ea330 | -13.54656 | -52.91296 | 2026-07-07 05:31:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd7889b4-7ab4-3aec-a803-6ae1fea704da | -13.25786 | -54.34246 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 108b1928-3e5d-3628-86b3-d59378873fa2 | -13.26418 | -54.22844 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a179d9c-0e38-3e17-99eb-d1550cb7111e | -13.5407 | -52.91214 | 2026-07-07 05:31:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README21.md)
