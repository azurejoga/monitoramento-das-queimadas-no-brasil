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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b47bb735-5ed6-3614-85f6-53cc7cf7bbce | -9.2566 | -43.5241 | 2024-10-06 14:35:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 139.9 |
| 0f42cff2-cd2d-3975-bd8e-c95e5475f35e | -9.9395 | -46.0866 | 2024-10-06 14:36:02 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.2 |
| fe9e3481-7c78-3948-9bbb-abb5e2e6499d | -9.8366 | -60.2976 | 2024-10-06 14:36:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 90dc5c1c-f8ea-34e1-acda-5228065cdecf | -10.2711 | -45.4787 | 2024-10-06 14:36:04 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 2b5c6def-f907-3422-a936-76d204cc54a2 | -10.6981 | -46.1287 | 2024-10-06 14:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 59f59e5e-8496-3157-b177-e07d3f2d77d2 | -10.8032 | -53.5417 | 2024-10-06 14:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| a244f2b3-e01c-3188-af2e-befbec8cf4fa | -11.0802 | -54.0302 | 2024-10-06 14:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 899af4ad-4275-3a2e-9b61-938f7e9cc58c | -11.2335 | -53.8519 | 2024-10-06 14:36:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 710e35ad-e6dd-38c6-be94-5fc593b09b8c | -11.3853 | -47.2088 | 2024-10-06 14:36:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 583f9f0e-9164-3d16-9152-1ee08bc99434 | -11.4238 | -47.1815 | 2024-10-06 14:36:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 140.2 |
| e631705c-2157-34d7-91b0-b4d6ad766ac9 | -11.6857 | -45.2411 | 2024-10-06 14:36:12 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 7bdb39bb-426d-382d-a8fa-809a05df41d0 | -11.6665 | -45.2439 | 2024-10-06 14:36:12 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| f903ee42-918b-3c99-9ac3-bf948ed245af | -11.9932 | -47.3736 | 2024-10-06 14:36:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| d2046461-ac9a-3f23-bb4b-4ad2993f893b | -12.0124 | -47.371 | 2024-10-06 14:36:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 24909295-a43a-3c26-90f6-ef909e00f22b | -12.2538 | -45.6167 | 2024-10-06 14:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 7b9d338b-d811-3f77-bfc3-3eb5f6a11e18 | -12.6633 | -54.6988 | 2024-10-06 14:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 325f0e7b-70d6-3d5e-9946-cec6b32a5ca2 | -13.8943 | -44.6058 | 2024-10-06 14:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| bb40d483-e065-34eb-9588-a1750189d8ad | -14.0767 | -45.1579 | 2024-10-06 14:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 5a037cd0-dffb-31fa-a261-a12b337b796d | -14.0762 | -45.1813 | 2024-10-06 14:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 8fcda488-9ca9-3cac-9b08-bc24bcb68b01 | -14.0772 | -45.1346 | 2024-10-06 14:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d3f12edb-9ead-3854-ad4c-a7e080ed4376 | -14.0198 | -45.0981 | 2024-10-06 14:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| d625bd46-1bcb-3ccd-8809-e0bf9686e2b1 | -14.774 | -48.0532 | 2024-10-06 14:36:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 109.4 |
| fd2004f9-574a-38f2-a75c-d9b6ad8d6bf9 | -15.1435 | -48.0594 | 2024-10-06 14:36:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| c217aef7-d1cf-3378-8891-7321332f65ab | -15.1635 | -48.0336 | 2024-10-06 14:36:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 176e27c0-5e8a-35d7-8bc9-0e6153d49629 | -15.163 | -48.0561 | 2024-10-06 14:36:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 1c379b51-a896-3d7c-a7f7-8f352703c69f | -15.6702 | -47.1763 | 2024-10-06 14:36:34 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 80efd540-6de5-3556-a2c5-d531685df7f8 | -16.6731 | -55.8934 | 2024-10-06 14:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| d1315c5c-dd01-31b3-97b8-9e9a6530303d | -16.9098 | -47.1493 | 2024-10-06 14:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8f3d85c4-279f-3fc3-a9b3-496e357ce4e3 | -16.6535 | -55.8958 | 2024-10-06 14:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 63f8eae3-0e5c-3486-8ffa-8044df7b1998 | -17.8125 | -53.7645 | 2024-10-06 14:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 175.7 |
| e6a29bd1-2669-3bec-9eb6-d271b9d69c0d | -18.6383 | -57.2993 | 2024-10-06 14:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.4 |
| 92606a1a-b19c-3fb3-b7ae-944ff5e28db5 | -18.889 | -54.5373 | 2024-10-06 14:36:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 10b27410-05cc-39f2-baf3-943c9deaf784 | -18.869 | -54.5404 | 2024-10-06 14:36:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 5897a653-d915-3bb8-afc7-1d46d577e580 | -20.5813 | -49.3865 | 2024-10-06 14:37:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 255.4 |
| 62160fba-a3ed-3f9e-bb36-4cc9509e5dc1 | -0.8584 | -48.682 | 2024-10-06 14:45:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d0a7827a-0bcf-384d-9331-9e06e2077909 | -1.475 | -54.955 | 2024-10-06 14:45:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| a33af6ef-22d6-3a38-b1a6-51d9ed161cc6 | -1.5486 | -54.775 | 2024-10-06 14:45:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| f94b7e6c-50f0-3f2f-a174-0eefa85d8362 | -3.113 | -48.5916 | 2024-10-06 14:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 1d8ce285-c5ac-3aed-b775-165391a5a29d | -6.5781 | -45.3158 | 2024-10-06 14:45:43 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| b92258d7-87ed-3cf4-8665-a9df409de0f9 | -6.7979 | -60.112 | 2024-10-06 14:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 72cef107-3e30-3f0d-9daf-50bd9292a5af | -6.7795 | -60.1127 | 2024-10-06 14:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 6cd43000-903f-3853-8df4-ac87ebb90e66 | -7.6444 | -42.4342 | 2024-10-06 14:45:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 9b12f990-6dd7-380a-8961-c50b3cfe8cee | -8.1567 | -43.7211 | 2024-10-06 14:45:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 116.3 |
| 2f0f174c-e655-3358-aeea-cd656c69514b | -8.157 | -43.6977 | 2024-10-06 14:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 622d2e04-4d66-31f3-b1c0-554ccf6e0a72 | -8.1948 | -43.6936 | 2024-10-06 14:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| ba2b0637-d244-3e6d-a851-5d971401649e | -8.1759 | -43.6957 | 2024-10-06 14:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 4fa9a421-e7f4-32ec-85b6-8735dbbb98b3 | -8.1667 | -44.4152 | 2024-10-06 14:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 221f11c5-fb70-3b8f-b008-dec173ef12e9 | -8.5364 | -67.1246 | 2024-10-06 14:45:55 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 493.0 |
| 38ff55c6-4229-390d-b682-78bf10bac470 | -9.257 | -43.5006 | 2024-10-06 14:45:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| e002ab4d-fe31-38b5-87da-fef32a6803e0 | -9.238 | -43.5029 | 2024-10-06 14:45:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| 41d7152b-6a2e-3ff8-8b7e-9c1400dd4a64 | -9.2566 | -43.5241 | 2024-10-06 14:45:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| 8d804fb3-3a34-3867-a5c1-e608e46b79bc | -9.8552 | -60.2966 | 2024-10-06 14:46:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 6f693441-4f7f-379e-9225-67e5c7daaae3 | -9.9925 | -46.3508 | 2024-10-06 14:46:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 1eb9f97e-2ca0-392f-b4d3-cb6a5e757ea3 | -9.8366 | -60.2976 | 2024-10-06 14:46:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| b828de8c-45f6-3f76-827e-e85478b54718 | -10.2711 | -45.4787 | 2024-10-06 14:46:04 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 5af48bea-d249-3a48-9e74-84a67424d040 | -10.7445 | -45.6002 | 2024-10-06 14:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| fddf2cd6-bb82-32b1-a6ae-57d4c167de37 | -10.7831 | -45.5724 | 2024-10-06 14:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.0 |
| f3c5ecd3-2afb-3289-be2e-4da2267e8142 | -10.7449 | -45.5774 | 2024-10-06 14:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 29789f9a-dca7-322a-adc4-b4686f59ef9b | -10.8032 | -53.5417 | 2024-10-06 14:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 63906634-a907-32b2-949e-b04d2b251807 | -10.9187 | -46.6192 | 2024-10-06 14:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| e6e3d55d-348a-3b1d-b548-c8a10048c356 | -10.8338 | -51.1388 | 2024-10-06 14:46:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 7a4e1c1c-9f53-3e3f-b252-a2470c139446 | -10.918 | -46.6642 | 2024-10-06 14:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 4786c052-441e-374e-89d4-dff746b12b38 | -11.1545 | -51.2112 | 2024-10-06 14:46:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 317e5935-1d44-3a6b-8312-c4261570473d | -11.0966 | -54.2336 | 2024-10-06 14:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 0fd024da-3f5f-3c3f-8602-ccd51a74d235 | -11.2488 | -51.2435 | 2024-10-06 14:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 3fc01832-6d46-382e-88c5-8d26edf385c3 | -11.2117 | -51.1839 | 2024-10-06 14:46:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 452cf208-54ed-3134-8ae0-199b414def3e | -11.2335 | -53.8519 | 2024-10-06 14:46:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 995928c6-ef7d-37f6-ac80-8e0ee2c6a398 | -11.4238 | -47.1815 | 2024-10-06 14:46:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 9bd3426b-62ad-3e05-bca2-3a20ce13815f | -11.6853 | -45.2641 | 2024-10-06 14:46:12 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| b41afdc9-cac6-30ca-b639-aaeb2ea5ee48 | -11.6857 | -45.2411 | 2024-10-06 14:46:12 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 245.6 |
| dd707ad7-efe4-303a-800f-e595f24514cc | -11.6665 | -45.2439 | 2024-10-06 14:46:12 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| d7a0fc1d-0af1-386b-b80e-e27f49bd11fc | -11.9932 | -47.3736 | 2024-10-06 14:46:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 165.7 |
| a3b5e729-8b77-3f5a-9aa3-71f098d92ec8 | -12.2538 | -45.6167 | 2024-10-06 14:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| f3771033-ec6d-37f6-9829-ae45ce75784f | -12.325 | -59.2218 | 2024-10-06 14:46:17 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| aee542f8-ce00-36e4-a643-e52f5c879150 | -12.6633 | -54.6988 | 2024-10-06 14:46:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 70ae5f01-1dce-3e59-84ec-bc79187247cc | -13.8943 | -44.6058 | 2024-10-06 14:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 535bb233-d228-3458-9b1f-c4f024feaba3 | -14.0874 | -45.5739 | 2024-10-06 14:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1a5686da-6a43-3582-8711-1a0b253c50b4 | -14.0767 | -45.1579 | 2024-10-06 14:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 7319a30e-7653-33d9-9254-6be4d9a75bb8 | -14.0193 | -45.1215 | 2024-10-06 14:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| ee2d3d11-ba31-33a7-9f2d-a7a5eb71ecd3 | -14.0198 | -45.0981 | 2024-10-06 14:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| aea25f71-b428-360d-838e-fb14bd1f6172 | -14.774 | -48.0532 | 2024-10-06 14:46:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 03648be8-7806-3b4e-8df5-096f61a9cae9 | -14.7735 | -48.0757 | 2024-10-06 14:46:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 44.6 |
| aed60c17-8fe0-3bb2-b434-8578ee7f9307 | -15.163 | -48.0561 | 2024-10-06 14:46:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 83330b30-24f0-30ed-a62f-0203e5f3c2ae | -15.1435 | -48.0594 | 2024-10-06 14:46:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 2fbbaa6c-fa22-321f-b53a-8c604d5249ee | -16.6535 | -55.8958 | 2024-10-06 14:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 425412ef-525f-39ff-aafe-17d704aa1d9a | -16.9098 | -47.1493 | 2024-10-06 14:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 89e5fe8c-59bd-32bd-a8bb-9a95acc4d00d | -17.8125 | -53.7645 | 2024-10-06 14:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 239eae40-7849-3ee5-9305-a13b780c8dd4 | -20.5813 | -49.3865 | 2024-10-06 14:47:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 221.3 |


