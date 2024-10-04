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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c881e24-c301-360d-a45d-9c2a95a155d5 | -23.87081 | -55.4194 | 2024-10-04 04:36:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 80800535-cf09-355c-8d50-bc96deb2cf93 | -22.93707 | -55.62163 | 2024-10-04 04:36:00 | NPP-375D | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2b2cb57e-cf52-3a7a-907b-6aecde114fcc | -23.9378 | -55.25523 | 2024-10-04 04:36:00 | NPP-375D | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0c6f7d75-8465-3e05-a409-f887d25c5b4b | -19.65714 | -56.47095 | 2024-10-04 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b1d27607-e797-358b-853e-c37e3dc252d7 | -22.11683 | -56.70632 | 2024-10-04 04:36:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 728a3d1e-511c-3e7e-8988-152ed59eb19e | -21.40344 | -57.22628 | 2024-10-04 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e06bf2b-cd78-31a0-863f-4641f861b86c | -21.40269 | -57.23023 | 2024-10-04 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 96e9f5ec-4d23-344b-ba5a-5eda43d4fe84 | -18.89429 | -57.70317 | 2024-10-04 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2b2dd6f2-c6a0-3d05-8f76-a7be432f5217 | -18.89244 | -57.7126 | 2024-10-04 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 367d4e53-3dbf-3208-9efb-2bb91d77c22e | -18.71873 | -57.34798 | 2024-10-04 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 3a6635c0-5366-3df2-b6f0-992427069c52 | -18.71522 | -57.31907 | 2024-10-04 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9689af1e-2786-3807-9d0d-cb7d1bc512e8 | -18.69679 | -57.2964 | 2024-10-04 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ea8ef2e3-d5dd-3959-8c81-636b2378a760 | -18.69431 | -57.29253 | 2024-10-04 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8d883545-4cc1-3c7c-833c-74af4042491a | -18.69346 | -57.29702 | 2024-10-04 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d1808ae0-e7cd-3e91-af13-01b22a477701 | -18.69329 | -57.29099 | 2024-10-04 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d38ade39-4298-3c7f-b706-c23d6b4002a8 | -18.6924 | -57.29545 | 2024-10-04 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8495aab3-a662-388f-88e2-c924c906ab92 | -10.4968 | -48.1587 | 2024-10-04 04:36:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 25dab32f-6647-34ee-a9a6-50a899ec1c34 | -11.2566 | -60.5825 | 2024-10-04 04:36:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| cb37fb26-bff1-384b-95b7-345402674c99 | -11.5992 | -65.0015 | 2024-10-04 04:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c53fccd9-0356-316c-9f43-f2653f46ec7d | -11.6181 | -64.9818 | 2024-10-04 04:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| fa808f1f-abd9-3386-a9c4-84cad2a73081 | -12.5898 | -53.1359 | 2024-10-04 04:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 4403db7d-a3da-39af-934b-5f0cd5ae44b5 | -12.5901 | -53.115 | 2024-10-04 04:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| f806ff14-03f8-3d0b-9695-e1789c38dee2 | -13.0598 | -51.1195 | 2024-10-04 04:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 3293df28-716a-3958-87f1-bb6d30174497 | -13.079 | -51.1171 | 2024-10-04 04:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 2d7c4d0b-533a-35ee-9133-837695cea4c6 | -16.4151 | -57.3823 | 2024-10-04 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 56416005-0870-3d22-93aa-ff80006b191c | -16.5935 | -57.1988 | 2024-10-04 04:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.2 |
| e1b9a5ff-1854-37b2-b0d1-6c5435d265ba | -16.5938 | -57.1783 | 2024-10-04 04:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 170.0 |
| bf7d9dc1-34fc-39df-82ba-425fa4ded442 | -16.613 | -57.1965 | 2024-10-04 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.2 |
| 75f1c53d-6081-3c66-854a-9f00f8330e1a | -16.6133 | -57.176 | 2024-10-04 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.1 |
| 1738eada-b626-3dc0-ade5-6928c2add54f | -16.6871 | -57.4536 | 2024-10-04 04:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 731f163e-d6b9-3401-85c6-3843c77437b5 | -16.7455 | -57.4674 | 2024-10-04 04:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 1d69429d-fdb7-35bb-b5eb-1440a7aef351 | -16.8433 | -57.4562 | 2024-10-04 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.9 |
| fc942de2-277a-3363-a285-9d8e19f9a94b | -16.843 | -57.4767 | 2024-10-04 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.5 |
| 16937d1d-f8c4-370b-86e8-43c242a60174 | -16.9283 | -55.8405 | 2024-10-04 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| bf0f8fcb-a118-37a9-a982-7b7975249b45 | -16.9287 | -55.8197 | 2024-10-04 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 95a7e0ce-6703-3f85-a949-b9a03338dab1 | -17.1085 | -56.7892 | 2024-10-04 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 9e03c5fb-9491-3753-bde0-2f3c6414b38c | -17.1088 | -56.7685 | 2024-10-04 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 32b9a572-ca50-3fea-8115-904f393c3eca | -17.1378 | -57.4016 | 2024-10-04 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 2ce20f02-ec6e-3a9d-8e5e-d2a9d64700dc | -17.1771 | -57.3969 | 2024-10-04 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.9 |
| 6f01edac-8b8b-3873-8874-c68484beaba9 | -17.1574 | -57.3993 | 2024-10-04 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 6bb5e9b1-3428-3d60-bd6c-d2a2dd511fa8 | -17.1577 | -57.3787 | 2024-10-04 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 7b542847-b827-3189-9f59-7138132d3681 | -17.1774 | -57.3764 | 2024-10-04 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.5 |
| edc57a1f-b136-3335-855e-6b6cbe55058c | -29.87523 | -51.15654 | 2024-10-04 04:38:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 4de4863d-a03e-3018-b586-0e37f5c4824b | -29.81462 | -51.17343 | 2024-10-04 04:38:00 | NPP-375D | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| b15fb622-947e-32ab-8f1c-d30fda1c585e | -24.6513 | -52.53426 | 2024-10-04 04:38:00 | NPP-375D | NOVA CANTU | PARANÁ | Brasil | 4116802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 597df778-97f8-3546-884c-27d66edc640b | -9.845 | -68.9623 | 2024-10-04 04:46:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 49.0 |
| c03386e6-5e77-3e11-8f6b-323a0c8b387f | -3.37461 | -42.28891 | 2024-10-04 04:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 32.2 |
| b33fad98-5d7d-3e44-87a2-374c6b472582 | -3.37393 | -42.29356 | 2024-10-04 04:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 419a04b0-29d1-335c-b789-b91544b05333 | -3.37325 | -42.29821 | 2024-10-04 04:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 20.6 |
| d72e7686-de42-3dd6-bd8f-1539c2dff370 | -3.37257 | -42.30286 | 2024-10-04 04:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 89ae485b-f8ab-3403-9fa7-5954e6b1be04 | -3.36851 | -42.28799 | 2024-10-04 04:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 45.2 |
| 7e06c672-ba54-3203-8b75-7656bde16686 | -3.36783 | -42.29263 | 2024-10-04 04:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 45.2 |
| 7ba78edf-6554-364f-a23b-1789e520f473 | -3.36716 | -42.29725 | 2024-10-04 04:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 50.0 |
| 1c9231f5-589a-3f4c-b7ed-809c87fe8d0f | -3.36649 | -42.30188 | 2024-10-04 04:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 50.0 |
| 37d23e6c-7382-3956-849c-30032bd977c5 | -3.40655 | -42.28362 | 2024-10-04 04:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 16fce49f-1c2a-3f55-95ab-2fb577302ba2 | -3.40586 | -42.28827 | 2024-10-04 04:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a39f827-7406-3c19-8c25-1e0acd7c0cca | -3.40517 | -42.29292 | 2024-10-04 04:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41756c74-acd7-3438-9533-d53d9404cade | -3.36918 | -42.28338 | 2024-10-04 04:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6497b87b-c469-3b2a-95b1-9e6dfaad598a | -3.43328 | -43.3456 | 2024-10-04 04:53:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7ae8e04-586f-3a33-8e4e-1064610d1c75 | -3.43272 | -43.34946 | 2024-10-04 04:53:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa010f0d-2ce4-3eb7-a6d5-de8c6ff301d5 | -1.58829 | -48.02949 | 2024-10-04 04:53:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f18c28be-69f4-3e01-bfb8-d8f5e4d2579f | -1.58774 | -48.03297 | 2024-10-04 04:53:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25221737-2a4a-327d-8008-08a1eb475a55 | -1.49358 | -47.34047 | 2024-10-04 04:53:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6debe4b2-387f-3d92-8d5b-e87173944d96 | -1.49346 | -47.33778 | 2024-10-04 04:53:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80975e37-5692-3029-93e9-5a5aee088f32 | -1.49285 | -47.3416 | 2024-10-04 04:53:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83b545f4-f91b-32f8-95c7-9f04c1ced81b | -1.07067 | -48.01808 | 2024-10-04 04:53:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2930c2e-c4d9-30cb-9932-beb9592c90e3 | -1.03817 | -47.7939 | 2024-10-04 04:53:00 | NOAA-20 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 321c8355-bfc1-3232-8e7d-c5f34f1b30da | -1.03762 | -47.79745 | 2024-10-04 04:53:00 | NOAA-20 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02649adf-b4cc-39e3-8486-d6f46fccb93c | -2.33827 | -47.97523 | 2024-10-04 04:53:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7844fd2e-ae8f-3705-9355-8c087c2abbd4 | -2.29617 | -47.89423 | 2024-10-04 04:53:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0418a063-ea28-3413-9c76-4c6dbac850ac | -2.29261 | -47.88999 | 2024-10-04 04:53:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b32136cd-8be8-3ffb-80b3-83b4ec5a8278 | -2.209 | -48.1633 | 2024-10-04 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e6c5507-75c9-3908-9b0f-fa4d8193ef3a | -1.38516 | -48.97541 | 2024-10-04 04:53:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2fa400d9-ede0-3809-8d99-131b226e1c31 | -1.38067 | -48.97942 | 2024-10-04 04:53:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9f0e2dc0-0c7d-3e3e-beb0-47919f97bec2 | -1.1394 | -53.64361 | 2024-10-04 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a8f46bd-42f8-3187-80d9-d6035a7efd9e | -1.75681 | -54.44898 | 2024-10-04 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 77bb3ce3-d2e8-3fdf-ad0a-d7f702ff9990 | -1.75401 | -54.44489 | 2024-10-04 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4021307a-4549-31e3-8145-fb9a38954ca6 | -1.75345 | -54.44846 | 2024-10-04 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 955a8f1b-9c25-3698-a781-e978b17e0ae8 | -1.21681 | -54.05621 | 2024-10-04 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7044bdb2-85c0-30a5-91db-ec4c363f6d7d | -1.13662 | -53.63965 | 2024-10-04 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 002d392c-957d-3bdd-91c2-08ec839386c1 | -1.13608 | -53.64312 | 2024-10-04 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7f1cf89-aa28-32ef-890f-8509c92933be | -1.1333 | -53.63914 | 2024-10-04 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6706dae-b1b4-33c4-b70d-2ff11a9dabb1 | -1.12998 | -53.63862 | 2024-10-04 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b058052c-288f-3fb0-b7c4-a7b113f38854 | -1.04901 | -53.52742 | 2024-10-04 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4e166ac-119e-31a5-9e5f-032940585b84 | -1.04847 | -53.53088 | 2024-10-04 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71beec13-be05-32fc-a120-f4b31132c70a | -1.04569 | -53.52691 | 2024-10-04 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81c09044-6998-385f-8a9f-8b819d3dde24 | -1.04515 | -53.53037 | 2024-10-04 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e8f51eb-df64-3d98-839f-214ed96aada0 | -1.63084 | -55.18211 | 2024-10-04 04:53:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f1394bd-05c9-3db1-a71b-197cca106b67 | -1.4262 | -55.25927 | 2024-10-04 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0c98d6c-1a06-3e6a-b8fe-c62d72cd4bce | -1.36649 | -55.68676 | 2024-10-04 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1667e7bd-6b2f-3395-aa4d-ca01fcf78741 | -1.31349 | -55.86261 | 2024-10-04 04:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cf3a91a-a54a-3b88-9d80-0079eda46bcd | 2.69148 | -61.31984 | 2024-10-04 04:53:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ede4ab9-b0e9-3e4b-b638-9bb384bd8898 | 2.68608 | -61.32057 | 2024-10-04 04:53:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1306368-60ca-338e-8fe9-18e083304879 | -8.43207 | -41.94533 | 2024-10-04 04:55:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1495514c-2ff3-3f2d-8e16-7a4c8ff5b224 | -8.42463 | -41.95064 | 2024-10-04 04:55:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 982d75df-f971-3778-8854-d3b1e599c4b4 | -11.04363 | -42.01889 | 2024-10-04 04:55:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f378df65-3781-3635-bd46-163e78ec1be6 | -11.0429 | -42.02522 | 2024-10-04 04:55:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6f899376-817c-383c-b487-ce084eacd797 | -4.82157 | -42.76546 | 2024-10-04 04:55:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6826fc47-5856-30de-8085-7b91ad777f76 | -4.8162 | -42.75994 | 2024-10-04 04:55:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22eae40c-2c79-3070-8ae1-a6ea8fa693e3 | -4.81556 | -42.76444 | 2024-10-04 04:55:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README138.md)
