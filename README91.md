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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d34281ee-bdf8-32c4-96fc-fed6dd083750 | -4.115 | -42.2011 | 2025-10-16 13:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 108.8 |
| cc504c64-e46c-3d00-b6e0-78b5ebe1eee6 | -13.0743 | -46.9717 | 2025-10-16 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 9054f46c-992b-36e8-8222-2207b10eba7e | -3.8572 | -41.5719 | 2025-10-16 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| e2bee323-91a9-340a-b330-857836a55065 | 1.0765 | -51.1026 | 2025-10-16 13:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 5fd59d2e-41ed-3394-bc1f-b2263eb3f681 | -11.2862 | -44.0226 | 2025-10-16 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| f7e3b037-43f1-3eb6-8e17-8ee1be408d1d | -10.1333 | -44.5545 | 2025-10-16 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 214.4 |
| dd5d95b8-4369-3d3b-8999-df66e8885669 | -10.673 | -45.3125 | 2025-10-16 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 51e04121-2ced-35ff-8a53-3b27b64fd03e | -12.7063 | -50.4993 | 2025-10-16 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| c5d3a644-09c8-3250-8b12-355b694459da | -11.5724 | -44.0736 | 2025-10-16 13:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 201.4 |
| d43b1480-adb7-3e1b-b7bb-6c00ef1f083a | 1.8402 | -55.7034 | 2025-10-16 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| ac9131f8-e8a6-3eb6-a3cf-d89904fb9b96 | -9.3599 | -46.959 | 2025-10-16 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 2347503d-30ca-3280-8cf8-d13af834727f | -13.9127 | -45.5808 | 2025-10-16 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 00d31544-918e-3be3-899f-e14387f814af | -11.5729 | -44.0501 | 2025-10-16 13:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 0b137c24-a10c-3167-9ebc-d160604328f4 | -11.3411 | -45.2673 | 2025-10-16 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 16e76b58-47ef-3c0c-8a9f-5c30cc7e4590 | -13.4605 | -47.9454 | 2025-10-16 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d01f2d65-784d-3bda-a955-2d3f950159e7 | -9.2255 | -48.6 | 2025-10-16 13:40:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| b9452d5d-1294-39ea-8bf5-781604b723f2 | -12.2652 | -47.1346 | 2025-10-16 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 3d0e4371-494d-3456-bf6c-82012f795117 | -10.6024 | -47.4178 | 2025-10-16 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 159.7 |
| bc2afe7d-4d80-3ee1-b495-54bb2dbf54af | -10.6539 | -45.3151 | 2025-10-16 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 40b61213-add9-3e21-bb52-3fdcbd68ed5f | -10.133 | -44.5777 | 2025-10-16 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 251.9 |
| 1ed49a39-c27b-3aca-8739-1674c0306620 | -14.1339 | -51.2157 | 2025-10-16 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| e6151ca9-bb30-37db-af54-590e36df9ab1 | -9.3602 | -46.9368 | 2025-10-16 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 837b2ef1-a90f-3f1d-a662-3296923bead0 | 1.8218 | -55.7431 | 2025-10-16 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| f2a611b1-ae19-39ce-a005-efc19d38df95 | -10.6214 | -47.4155 | 2025-10-16 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 94c2cf13-72e0-32dc-bbb5-6bd83e403256 | 1.7479 | -56.0791 | 2025-10-16 13:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 05a5b561-1fab-3cf1-9af7-52846a5753fd | -10.6169 | -45.2512 | 2025-10-16 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 86cc3bc0-3c65-3d0b-b4c7-44d4b9c0bd22 | -10.6734 | -45.2896 | 2025-10-16 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 38c77dd1-d196-3a55-81a2-2bc1505d0ab6 | -9.7162 | -44.5149 | 2025-10-16 13:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| a6090022-5d1e-3520-b77a-7da0c8627ed5 | -11.4589 | -43.9969 | 2025-10-16 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c482ca4e-5394-3379-ab54-76f766611e0a | -9.3788 | -46.957 | 2025-10-16 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 5ff1398e-0700-360d-9050-d332060f4c6e | -3.2161 | -42.5069 | 2025-10-16 13:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 6f113f76-d6b7-3882-9071-fb1a523a3d23 | -3.7628 | -41.6967 | 2025-10-16 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| cebccf5d-5cdc-35be-937e-b13790c1252f | -10.514 | -43.3815 | 2025-10-16 13:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 84b95690-8f5e-321c-b215-ad22dbc933f9 | -9.2258 | -48.5782 | 2025-10-16 13:40:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| cc4033e4-cfba-37ea-a578-60a7b776f730 | -10.6543 | -45.2921 | 2025-10-16 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 77492f73-01a2-3a1c-8077-1bde464b2840 | -13.2535 | -43.752 | 2025-10-16 13:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 53bbab77-3e67-3930-be04-249dcb447aba | -12.9909 | -47.3217 | 2025-10-16 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 73dabfd0-b54e-3f49-8125-7aba8a30c89c | 1.7851 | -55.7436 | 2025-10-16 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 5ae8bb8f-1b66-3080-a001-e4ad985bfd22 | -11.3599 | -45.2877 | 2025-10-16 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| e3606665-4ecf-3cd4-b531-105de20e8610 | -10.1143 | -44.557 | 2025-10-16 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 276.6 |
| e11451c9-ff74-3f25-a0ac-82b2e6315744 | -12.7993 | -50.6595 | 2025-10-16 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 34ea9ab2-9a62-3ded-9c46-d0452fc46a30 | -14.1343 | -51.1942 | 2025-10-16 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 2774b545-c5a4-370d-b7e7-07c17fb53822 | 1.0582 | -51.0198 | 2025-10-16 13:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 70.5 |
| cd5fe7ce-98e6-3f4b-b218-b2f1424ec8c1 | -11.1406 | -45.8437 | 2025-10-16 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b15894f4-6489-3c48-8465-bdc62f51a8f2 | -10.1139 | -44.5801 | 2025-10-16 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 293.1 |
| d7cc6832-2795-32c3-ad6a-3f3855aec86a | -10.6024 | -47.4178 | 2025-10-16 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 9a2a12eb-3326-3e1c-ac9b-00052520aa01 | -12.2652 | -47.1346 | 2025-10-16 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| a0296a47-c2b5-397d-bb82-d762e0b350c3 | -10.5834 | -47.42 | 2025-10-16 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f4f9cd96-b871-3768-a2d9-6d2d199fac38 | -12.2919 | -45.634 | 2025-10-16 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 77176421-cbca-36e7-ac9a-d7e5dc1a9666 | -17.6215 | -46.4269 | 2025-10-16 13:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 29e01ae7-d31c-3f99-8ad0-15f1612a7706 | -9.2255 | -48.6 | 2025-10-16 13:50:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| f919af87-89aa-3860-80aa-31fbd8ff2654 | -12.2655 | -47.1121 | 2025-10-16 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 8166ccfb-eecb-3988-9ccb-69a6bc7204ed | -11.9073 | -46.8026 | 2025-10-16 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 58ef8036-0adf-3a4f-ad14-10fab08ad22d | -9.2258 | -48.5782 | 2025-10-16 13:50:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| a302cc1b-c800-304a-8e03-6780811509ad | -12.284 | -47.1544 | 2025-10-16 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 9c3c4065-ecf3-3ff1-a0c3-12cac5dd587d | 1.0582 | -51.0198 | 2025-10-16 13:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7e2a5e9e-65e8-38be-a1a0-38a335ba237f | 1.0581 | -51.1236 | 2025-10-16 13:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 570363f6-3d31-36e2-934b-49860155a285 | -10.1333 | -44.5545 | 2025-10-16 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 237.0 |
| 7055a957-20c7-3abc-9780-4ee5191c3bca | -12.3032 | -47.1517 | 2025-10-16 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 140.4 |
| d5839a1f-573e-34df-9c89-a950b98ecb9c | -12.9565 | -47.102 | 2025-10-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 95544cad-78a1-34dd-87c6-bf2ecd882575 | -10.1143 | -44.557 | 2025-10-16 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 278.8 |
| 97bba5cb-7fbb-3425-9ca4-888a654d8f4c | -12.7989 | -50.681 | 2025-10-16 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 97c2cdc0-d6fc-38b2-b7c1-eb23da6e3a26 | -9.6782 | -44.5196 | 2025-10-16 13:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ba780ac1-b8e7-344d-af48-9eb8b69d009b | -11.907 | -46.8251 | 2025-10-16 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 3a26213f-eba8-33f5-b164-1f1c62ae50d9 | -10.5144 | -43.3579 | 2025-10-16 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 23271d5f-cd6e-318b-9c56-7f91238a4d1c | -10.6021 | -47.44 | 2025-10-16 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 294.0 |
| ccd79042-7377-312e-891f-1454d28bc7da | -4.1149 | -42.2248 | 2025-10-16 13:50:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 129.5 |
| 5d70a45a-7444-3fb9-8317-377c53e8647a | -4.3687 | -43.3838 | 2025-10-16 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 147.4 |
| c7196a3d-0bac-376e-9e84-99b6f849c7cb | -12.2844 | -47.1319 | 2025-10-16 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 870666ea-2c24-3883-ba0e-70ac6e7dcd84 | -12.9716 | -47.3245 | 2025-10-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| bb132009-407e-35b6-a378-32c72b52580b | -11.4589 | -43.9969 | 2025-10-16 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 348df08f-b4c4-3fda-ac32-849dd420975c | -13.2535 | -43.752 | 2025-10-16 13:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 752f04f5-2621-3b5e-8727-a90d6c62a293 | 1.0582 | -51.0405 | 2025-10-16 13:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2c143ea3-2ba6-3959-8b13-2941d5d15b37 | -13.9127 | -45.5808 | 2025-10-16 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 322.1 |
| b699fc41-72a8-31ef-bce0-219e69453a0d | -13.4605 | -47.9454 | 2025-10-16 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| ea4cc144-c943-38b4-b8f7-54c9538ab0a2 | -12.9372 | -47.1049 | 2025-10-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| e77d008f-8713-38b2-9c78-50e45952bfaa | -9.2288 | -46.8841 | 2025-10-16 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 6ec12d3a-8361-3cad-aa6d-bc5849ddd61f | -10.673 | -45.3125 | 2025-10-16 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 6a9d7829-b060-3c93-b2b9-777eebdb046b | -11.3599 | -45.2877 | 2025-10-16 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| d9d87e46-f74b-3c75-b127-c38c70144a21 | -10.1136 | -44.6033 | 2025-10-16 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c4c415ba-77a2-31fe-88a1-3ac3bbe8c5cf | -4.3685 | -43.4071 | 2025-10-16 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 2dd94dca-edc5-3e5b-b8d7-2ecab8f9947d | 1.0765 | -51.1026 | 2025-10-16 13:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 91.4 |
| d634ac57-6533-37af-b3cd-d102f00da681 | -10.6543 | -45.2921 | 2025-10-16 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| df15e4cf-80dd-3751-bc1f-48a154f96294 | -11.3224 | -45.247 | 2025-10-16 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 67940997-1af4-3258-a3d4-b66bad3834a5 | -12.9909 | -47.3217 | 2025-10-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 235d36f2-c4c8-3968-87b1-e8e1e53d006e | -10.514 | -43.3815 | 2025-10-16 13:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| e35b6746-3554-33a1-afe4-dc2fa07462dd | -10.6214 | -47.4155 | 2025-10-16 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 670e22bf-984f-38ba-849e-8331a51ff7fb | -11.3411 | -45.2673 | 2025-10-16 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 114b9bf3-6c9b-3113-a12a-cba30dba9071 | -9.6972 | -44.5172 | 2025-10-16 13:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| c5ab0529-3439-339d-a1da-3a1ce2a9b1de | -12.9179 | -47.1078 | 2025-10-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 02050d57-d555-30be-a6fe-2ee4d5359763 | -11.5921 | -44.0472 | 2025-10-16 13:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 291e03be-e1f8-306e-9ca8-4472022f9afe | -4.115 | -42.2011 | 2025-10-16 13:50:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 171.0 |
| 697bc372-7507-3b82-be3a-d0fe4636db25 | -9.7162 | -44.5149 | 2025-10-16 13:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 9c1529bd-ce8b-3c73-865f-e67357e250bc | -11.5724 | -44.0736 | 2025-10-16 13:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 14ee135a-62e1-3df9-ab8c-450e7b341852 | -11.3603 | -45.2646 | 2025-10-16 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 4e1705f0-e407-3e25-b5c2-3cdfd077456d | -10.1326 | -44.6008 | 2025-10-16 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5dddfa0a-66dd-33ee-a96d-30f04c24132b | -10.8289 | -43.9482 | 2025-10-16 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 807be231-162d-3173-80bd-16c8ad098d17 | -10.6539 | -45.3151 | 2025-10-16 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 6eabdc69-df9b-3018-b82b-552ae708ea54 | -4.3872 | -43.406 | 2025-10-16 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 186.1 |
| fbade0e0-a465-3214-a4d2-2f071b6af7d5 | -11.1406 | -45.8437 | 2025-10-16 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |


[Clique aqui para ver as próximas entradas](README92.md)
