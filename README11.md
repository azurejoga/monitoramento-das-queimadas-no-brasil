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
| 7f1e85af-a266-30ac-a34f-4a3c54e8eded | -6.9336 | -43.6101 | 2025-08-19 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 76145c8b-b368-3b5b-9f03-51161bb0a526 | -6.9712 | -43.6066 | 2025-08-19 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 5eb6479e-d1a1-3ad1-af21-a9e8acaa0295 | -6.9339 | -43.5868 | 2025-08-19 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 458b2654-f3d6-3d99-99cc-592731697bb8 | -19.9433 | -48.1957 | 2025-08-19 02:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 022273c0-3874-3036-9d20-5e63cfd67832 | -3.982 | -42.516 | 2025-08-19 02:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 49736299-5916-3dcb-a3f3-89d270448ac7 | -6.9527 | -43.585 | 2025-08-19 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| b3b8aee3-29ad-3640-a09c-b1eaee3dca75 | -6.9715 | -43.5833 | 2025-08-19 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| e4f12039-f053-3df2-8380-b93aeab9760c | -15.0389 | -54.8089 | 2025-08-19 02:10:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 63267355-7311-38db-8354-f34a1801d22a | -7.736 | -66.980499 | 2025-08-19 02:18:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45e9456a-411c-3cf7-afcd-b2861d50a50f | -8.3187 | -70.155602 | 2025-08-19 02:18:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| cf689c6b-4678-3a51-bbd9-b3542ff0a096 | -7.7458 | -66.978104 | 2025-08-19 02:18:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d4b865d-b4c1-367c-b5bf-0ac9b4081345 | -8.5786 | -62.646801 | 2025-08-19 02:18:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 645a1204-766c-3f2d-9f03-3f1d0056add1 | -6.9339 | -43.5868 | 2025-08-19 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 8b97d71a-f49e-39a2-b9bc-15d87e28e0e1 | -18.518 | -53.2054 | 2025-08-19 02:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 52.9 |
| e169f060-e886-3a7b-804b-8383a0cc0791 | -6.9336 | -43.6101 | 2025-08-19 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 999a0794-59f8-3004-94d9-cbc7b737df58 | -6.9524 | -43.6083 | 2025-08-19 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 06a6395d-52b1-34cd-9df7-084faf3cf62b | -16.4863 | -45.0702 | 2025-08-19 02:20:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d88b5224-8a4e-3bda-91f6-bbf612b33a89 | -3.982 | -42.516 | 2025-08-19 02:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 2f9790d3-3b0f-3cc4-8d43-679b8ebe0297 | -6.9715 | -43.5833 | 2025-08-19 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 420ad25c-6376-39c6-a338-fd83e0ff3111 | -16.4857 | -45.0939 | 2025-08-19 02:20:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 90.6 |
| f76caaed-6684-376a-b6ff-a8bde47888a2 | -6.9527 | -43.585 | 2025-08-19 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 22adce7a-7362-3f0f-bb6a-78d68a0f0e60 | -6.9712 | -43.6066 | 2025-08-19 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a162e6e2-3bdf-3915-83c2-09c1963f374f | -14.9809 | -54.8158 | 2025-08-19 02:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 9f7b45c9-976e-30ef-86c8-ebcb44d37f8a | -16.4857 | -45.0939 | 2025-08-19 02:30:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| fb3255a6-06bd-367a-886e-b4d039bc4fed | -16.4863 | -45.0702 | 2025-08-19 02:30:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 37ba1833-1aff-333e-818d-8578aea4303d | -6.9715 | -43.5833 | 2025-08-19 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7ebedd1a-bf09-3d5d-85ee-c6b848ac8649 | -6.9524 | -43.6083 | 2025-08-19 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 70e3decd-ce9f-3b65-a414-943c9913bb1a | -6.9339 | -43.5868 | 2025-08-19 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 9040ca91-0250-3167-bb29-655ed9c01227 | -6.9336 | -43.6101 | 2025-08-19 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 0f061480-7330-3bfb-aaa5-89dd7cf2af05 | -6.9712 | -43.6066 | 2025-08-19 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| eadfaf0e-94d7-3923-a794-88542113d755 | -6.9527 | -43.585 | 2025-08-19 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 7146c0de-33b8-3ef2-99d4-0d69a2a11f2f | -3.982 | -42.516 | 2025-08-19 02:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| 10d986bd-8eea-381c-b397-2737bfcf44e9 | -9.4952 | -40.3834 | 2025-08-19 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 109632d3-93fb-3e05-be27-78ac26cf28fb | -6.9339 | -43.5868 | 2025-08-19 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 60bc558f-d512-3a55-8df1-ab2e7194ff53 | -16.4857 | -45.0939 | 2025-08-19 02:40:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 1e79c948-9ce3-36e3-b8ee-ec4f6dd4f95d | -6.9527 | -43.585 | 2025-08-19 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| c8eff20c-4ad1-365f-8d21-a18bde128237 | -9.4956 | -40.3586 | 2025-08-19 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 573684eb-280c-39fa-941b-34a6db933ffd | -6.9712 | -43.6066 | 2025-08-19 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 2579d849-cf7b-379d-953e-618c4fb9a8fd | -3.982 | -42.516 | 2025-08-19 02:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 7e641a01-40ce-31f5-9e6f-ac9c5b03d300 | -14.9812 | -54.7951 | 2025-08-19 02:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| af43ebd1-d452-3f0a-81a4-03fe28d6ccb1 | -14.9809 | -54.8158 | 2025-08-19 02:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| f22875e6-73f8-3e90-a083-6bd51079fd99 | -6.9336 | -43.6101 | 2025-08-19 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1ffabe89-a094-345c-b674-55c01f2eefbb | -5.7887 | -43.6134 | 2025-08-19 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| ed0eb972-f458-341e-a97a-4d64d8a8bc8e | -15.0389 | -54.8089 | 2025-08-19 02:40:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 163e166f-82d8-3c9f-9dc2-7be71a8bb74e | -6.9524 | -43.6083 | 2025-08-19 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c2ca1c9c-6775-3f5e-b98e-c00ad59febba | -6.9715 | -43.5833 | 2025-08-19 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ae339802-06aa-3eef-a2d4-8e49c6251416 | -6.9524 | -43.6083 | 2025-08-19 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 42b5bede-1272-3b09-be20-8218c4a4bf18 | -6.9339 | -43.5868 | 2025-08-19 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 24ab7acd-f485-35d9-8906-7d3d8cd08ce1 | -6.9715 | -43.5833 | 2025-08-19 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| e91b91b9-bcac-374c-8656-bba0166557c0 | -15.0389 | -54.8089 | 2025-08-19 02:50:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| d10b1e6a-b7ce-31f4-a11b-75bb48e795f5 | -14.9809 | -54.8158 | 2025-08-19 02:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 8eaf443b-cead-3c26-a7f9-15b50119e108 | -14.9812 | -54.7951 | 2025-08-19 02:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| a53bdbec-3640-3f5c-a5bc-bb4bd62989dd | -6.9527 | -43.585 | 2025-08-19 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 5b4bb4db-eb1e-3da0-845c-ea06a4d826c5 | -6.9712 | -43.6066 | 2025-08-19 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 9cb688ce-49be-3dcd-bbdd-fa6cf39f49a7 | -13.1555 | -54.9357 | 2025-08-19 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 4297530b-f10d-38ce-be74-430ec8ffca51 | -6.9712 | -43.6066 | 2025-08-19 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 0bd795e3-83fb-3eb8-84ad-6564f26f0ff0 | -6.9524 | -43.6083 | 2025-08-19 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 832662bd-4452-3434-becb-d273d0f1078e | -15.0389 | -54.8089 | 2025-08-19 03:00:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 3f8795f6-617d-3c8d-9b9e-6f5c19f552af | -6.9715 | -43.5833 | 2025-08-19 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 3e7025d1-8062-366e-8090-39b7e4fdae90 | -6.9336 | -43.6101 | 2025-08-19 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 1b9c5812-3cc3-3160-9c9f-f2d88e9bfae9 | -6.9527 | -43.585 | 2025-08-19 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 0f167a26-70f1-3386-996e-9a4c8762cfd1 | -13.2755 | -50.8137 | 2025-08-19 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b0a0e84c-4559-3645-8f00-5f60d35e89ed | -6.9339 | -43.5868 | 2025-08-19 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 2792c075-15ac-3410-85b1-d97a7a66561f | -13.2563 | -50.8162 | 2025-08-19 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| a85c1680-9f75-365a-b862-8e9cb1e4aeb8 | -14.9809 | -54.8158 | 2025-08-19 03:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| c7463ce4-467c-3679-95f0-41529505dc7a | -6.9715 | -43.5833 | 2025-08-19 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| f1084a22-d5a5-3094-8bd2-0fb47742cf54 | -14.9812 | -54.7951 | 2025-08-19 03:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| d6f8b6f2-e123-3972-8f53-6dff652d0d17 | -6.9527 | -43.585 | 2025-08-19 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 01be17ec-2f87-3616-be0a-b7cfbff2abc0 | -15.0389 | -54.8089 | 2025-08-19 03:10:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 03cca8af-f7d3-3e80-bf36-bf39ae363f82 | -13.2563 | -50.8162 | 2025-08-19 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| c03785c7-fada-378f-a282-d4d270a0a76c | -6.9712 | -43.6066 | 2025-08-19 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 53dba2a1-7691-3887-8729-618d758135cb | -6.9524 | -43.6083 | 2025-08-19 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| a261ee51-a76a-3589-8ddf-a0a2261ee7d8 | -6.9339 | -43.5868 | 2025-08-19 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 282223ff-ed31-3c5f-b5ed-746257eb96c3 | -6.5537 | -38.8003 | 2025-08-19 03:13:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 37718160-b374-35e5-a6de-1ea8bd1b75c9 | -4.72607 | -37.84708 | 2025-08-19 03:13:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 521fbf4b-cd41-302b-98c0-8edf61299ad5 | -4.25562 | -40.28609 | 2025-08-19 03:13:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 75a547c3-7923-3d35-ba2c-9d5ded998a60 | -4.26271 | -40.28733 | 2025-08-19 03:13:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4f1304f0-b94a-3ad7-b463-9b0c2790e716 | -4.7264 | -37.84406 | 2025-08-19 03:13:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 44f1c71c-5792-3915-ba5f-711955f2d8e7 | -4.72557 | -37.84872 | 2025-08-19 03:13:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b520abe9-0f68-3990-9349-6ab5f36b070e | -6.55767 | -38.79802 | 2025-08-19 03:13:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 47705c4d-4f61-37bd-beb8-6af4c0643e6a | -6.55684 | -38.80246 | 2025-08-19 03:13:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d4e71bed-a9e1-3317-82f5-db1382188ad4 | -14.53055 | -39.73418 | 2025-08-19 03:15:00 | NPP-375D | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b1353567-2a22-3bd0-8f82-32b46a22b162 | -14.53631 | -39.73557 | 2025-08-19 03:15:00 | NPP-375D | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ca1a14e6-49ef-3842-b9b1-23b8cad19c4b | -17.57489 | -44.48247 | 2025-08-19 03:17:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc54baef-3276-3c2b-a9de-a8d4858b92c6 | -16.78919 | -40.06412 | 2025-08-19 03:17:00 | NPP-375D | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6b2f1a92-d818-31ec-92e9-da8810ed0c16 | -17.56746 | -44.4819 | 2025-08-19 03:17:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24c91e03-01ee-3917-a942-7f6060c829d2 | -21.40306 | -45.00406 | 2025-08-19 03:17:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| adba84df-a21d-3e47-9002-752f57d4ffcf | -19.95799 | -42.12931 | 2025-08-19 03:17:00 | NPP-375D | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2052b019-c6c0-3f46-a173-d3c308b093cc | -21.39638 | -45.00166 | 2025-08-19 03:17:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| c1a3e8c6-5766-3e66-a827-0501f12b252c | -17.56548 | -44.48204 | 2025-08-19 03:17:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6658e3ec-e5e8-32ce-b9cd-408907d60a10 | -19.93365 | -45.06105 | 2025-08-19 03:17:00 | NPP-375D | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eae3d646-c521-3dcc-9a9d-a0d3ef749184 | -17.57283 | -44.48291 | 2025-08-19 03:17:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61e255b5-11bd-342c-8edd-e358e08394e4 | -21.39469 | -45.0084 | 2025-08-19 03:17:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 82c22b25-6741-3ed9-93b6-8915c91f7201 | -19.94069 | -45.06289 | 2025-08-19 03:17:00 | NPP-375D | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f0f4694-5e85-374f-8055-59e983dcf4ca | -19.95813 | -42.12796 | 2025-08-19 03:17:00 | NPP-375D | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| de3983ec-2446-3388-aab7-4d24463efca0 | -21.40133 | -45.01097 | 2025-08-19 03:17:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 23446813-8274-3671-bf91-3d9abbb3f858 | -21.38116 | -45.76472 | 2025-08-19 03:17:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| acad052b-6b88-3633-b826-6e431a9ce770 | -15.39993 | -43.06567 | 2025-08-19 03:17:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f66df18-a11b-3b66-87f9-c686bbed8c16 | -19.95695 | -42.13322 | 2025-08-19 03:17:00 | NPP-375D | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| eb980db6-ebaa-3986-9fe1-c08aa1aecc88 | -23.11136 | -45.27675 | 2025-08-19 03:19:00 | NPP-375D | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |


[Clique aqui para ver as próximas entradas](README12.md)
