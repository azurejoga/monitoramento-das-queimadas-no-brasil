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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a369ee7c-df07-3066-9fcf-c7170448476e | -9.33355 | -40.28902 | 2025-06-01 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 08f06b14-9ca0-3cb3-acb8-b16e6ff98b5d | -7.22588 | -43.13043 | 2025-06-01 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 10bd0450-e565-33a1-a929-5a5d7e8d3f51 | -7.22723 | -43.12318 | 2025-06-01 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2e1ab1bc-16d3-3428-a102-c403ec99d7cb | -7.21929 | -43.13779 | 2025-06-01 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 401ebe40-a986-3bd0-af4f-a240ead9de5d | -11.79768 | -41.20332 | 2025-06-01 03:15:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f9f1baa3-120a-3605-b28c-262a1bdbfa2a | -11.79859 | -41.19877 | 2025-06-01 03:15:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 346af0aa-5557-388b-9d89-5f4139262a54 | -7.22789 | -43.13186 | 2025-06-01 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| caa0cffa-1d29-37a9-bc0d-045165f3f82a | -7.2293 | -43.12461 | 2025-06-01 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c39f2593-8452-331e-95e5-41a96f687cd1 | -11.79258 | -41.19788 | 2025-06-01 03:15:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc927e87-b3e2-3574-9154-af817be48d57 | -7.2221 | -43.12331 | 2025-06-01 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 691dd94c-9518-3eab-9f1f-837b5f958abe | -7.21733 | -43.13634 | 2025-06-01 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6e271e04-c78f-37ef-9b68-d241f593aee3 | -7.2187 | -43.12901 | 2025-06-01 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 24a9f435-febf-335b-94a1-7fafe7ecad13 | -14.69091 | -45.11254 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ef7f653-e2b8-3661-98c3-66c452d96e29 | -14.68923 | -45.1201 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| defed34f-5ffa-338e-9d44-b1c8387f2914 | -14.68853 | -45.10579 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ca5fe36-d077-3a7c-9beb-4836d719ddb1 | -14.66496 | -45.12882 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f67fe7d1-7250-3392-8c01-2b51dea69316 | -14.69216 | -45.12249 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16c41079-f6e9-32c6-ab43-45da4678d733 | -14.67357 | -45.12362 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70c181b4-d2d2-3389-88a8-89ba1fc46b48 | -14.68854 | -45.08975 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38f7f07a-34f1-3748-aebd-8972732c7a3d | -14.67816 | -45.11856 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f4042bb-4e26-3eee-af84-97e7e2825c93 | -14.69554 | -45.09167 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 808fe6d0-9f7e-34e3-8ca3-6a4b3a7e9dd7 | -14.69392 | -45.11478 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| db7ca305-2a8c-3a06-98ec-cfcb3d97175e | -14.66949 | -45.12389 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a11e091-0fc9-36f2-a760-34745b781316 | -14.69014 | -45.09873 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e7f0489-c311-3a51-ac38-821c5faccc15 | -14.68548 | -45.10351 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03dc576c-40d6-3f1f-90ca-38257c52efc2 | -14.69622 | -45.12214 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da28159c-b97f-34f6-bece-3159cb1bff17 | -14.69789 | -45.11459 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad37fa71-cb5d-35f6-bd30-045cea9e2852 | -15.0634 | -43.87307 | 2025-06-01 03:17:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f50c375-7247-34e2-a575-7cb5bdbf1b1d | -14.69402 | -45.09852 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af810668-19b1-34e1-bd81-a9a1e38bd430 | -14.68706 | -45.0964 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23a00126-1a4d-30e3-af5c-a72c73648894 | -14.6917 | -45.09193 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70a7e81d-c791-34e0-92e9-c6812504d7f5 | -15.05685 | -43.87147 | 2025-06-01 03:17:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52e8022b-dce0-335a-a87a-071b14911db2 | -14.68046 | -45.12612 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7300e137-2a3d-31de-8666-82b33b559f45 | -14.68516 | -45.12051 | 2025-06-01 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0addc6a8-07ad-3130-8654-cc675d5ab41e | -4.80888 | -43.22231 | 2025-06-01 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce425903-1e79-3119-8f27-ad5817ea95f3 | -3.51525 | -40.35828 | 2025-06-01 04:06:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8fb6008f-ecc6-32ef-bc41-af0cf9052b31 | -4.51527 | -43.69107 | 2025-06-01 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b46a581c-8730-34d9-a101-e5d0b1f1c247 | -4.80828 | -43.22603 | 2025-06-01 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61518741-8fab-3592-b06f-fb8c2a4cdca3 | -3.76311 | -49.92644 | 2025-06-01 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf4a602e-328e-37fe-9f27-f747e3a07b3d | -4.25052 | -47.58649 | 2025-06-01 04:06:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ff1d024-4084-3437-ad7b-77fba7298f48 | -4.5856 | -42.94565 | 2025-06-01 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cabc349-cb48-37f7-a99d-630a376ec64a | -4.8117 | -43.22657 | 2025-06-01 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a9d0586-e362-3645-95c9-ed93be2428eb | -3.37055 | -49.16337 | 2025-06-01 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cecd1ad-4f65-382d-9e21-55b1978fc118 | -2.89661 | -41.6348 | 2025-06-01 04:06:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d93c5e50-f336-3c30-b409-32056cc21542 | -4.41865 | -42.10675 | 2025-06-01 04:06:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 054b6460-ad8c-38a7-ad99-2e47fe2112b5 | -4.80948 | -43.21858 | 2025-06-01 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01dbf4a3-8bb5-34c4-bc40-8dc02d0cd58a | -7.24759 | -43.2429 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9a6f6cbd-c3a8-37d2-8ecc-ef1af7ea2f3f | -10.6173 | -48.07434 | 2025-06-01 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09f2086e-9bcd-39dd-89c5-4bff23ce3710 | -11.5755 | -47.62977 | 2025-06-01 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0718a505-f93f-35b2-aca4-dd966e0b3e96 | -11.79796 | -41.19811 | 2025-06-01 04:08:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ef58b218-f81d-3899-b9f1-db438b36027a | -6.49533 | -47.48237 | 2025-06-01 04:08:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7a923bd-d3a0-3065-998c-a918064bff83 | -7.22176 | -43.1246 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cf5af88f-1c91-3a79-8735-e34fa212f1eb | -10.07528 | -52.75232 | 2025-06-01 04:08:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 324a7bc9-6c1a-3879-86ac-6983e2de73fd | -6.64014 | -47.34793 | 2025-06-01 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab3f8506-382a-3906-a65c-edc2ab696cc9 | -8.67559 | -46.64033 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ab25797-843c-3ac6-b3ab-cc1c6d8f8a68 | -9.1266 | -47.9916 | 2025-06-01 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3523018-a0e1-33cb-9d69-a071359f137f | -8.07312 | -34.97726 | 2025-06-01 04:08:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| af807b31-2283-36c6-b30f-e7ae54528661 | -7.22789 | -43.12924 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7f7ea6e0-9c04-3f9f-b6c4-6a1eaa4f0649 | -10.68134 | -47.20483 | 2025-06-01 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 51604e95-8809-3648-b8d3-b86c9a8dc9ab | -10.72678 | -47.899 | 2025-06-01 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75c56b87-f467-3fe4-9746-aea8419272cd | -11.57447 | -47.45296 | 2025-06-01 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6cd89784-1bea-33b7-933c-7917ea077910 | -6.44768 | -45.72918 | 2025-06-01 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f94856af-a22b-3a4e-8ff6-227828c99515 | -9.40285 | -48.94575 | 2025-06-01 04:08:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce346c20-f037-3cbd-8cfd-46fe3ad656b8 | -6.27214 | -44.2091 | 2025-06-01 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 417c359f-0c97-31cc-80fa-7a7714031d0b | -7.22454 | -43.12871 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4cb05556-cb6b-3026-8ab6-23eb2e52990b | -9.40114 | -48.94481 | 2025-06-01 04:08:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1ee580e-5f41-315f-8c21-0821f231bcfe | -9.40375 | -48.42086 | 2025-06-01 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c76cdf6-d804-393a-9fd1-e99a02e08e3f | -10.22714 | -47.17064 | 2025-06-01 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fbb9761-3a0c-3141-a79b-4ec2689a585f | -11.80189 | -41.19498 | 2025-06-01 04:08:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 150ccfbf-fc38-3fd8-b3d3-bc12927271e7 | -9.04661 | -47.02381 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a55c75ca-a95c-35fe-b472-b02e57c66b29 | -10.23192 | -47.16619 | 2025-06-01 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d8b733a-865d-3635-9d02-334310824789 | -6.2719 | -44.20576 | 2025-06-01 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 48477f7e-c916-3907-b1f3-35c97133dcd5 | -7.58725 | -45.8661 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 531ab0b7-6eb7-30ef-8e2c-66c7816f6396 | -7.21754 | -43.51773 | 2025-06-01 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 729fd69a-5683-307d-8a8f-a2498d63a605 | -10.12587 | -47.19812 | 2025-06-01 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5e9d5d3-ccdc-3494-bf00-3c2b9d52aee8 | -7.79556 | -46.22291 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cbd9a21-2e4d-3142-afec-94ed5444a693 | -7.08105 | -46.55689 | 2025-06-01 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e172187b-f94f-3303-9630-4f84fd21db38 | -6.29058 | -51.11867 | 2025-06-01 04:08:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 436bc675-8598-329e-a253-358156f8ecef | -10.118 | -47.19677 | 2025-06-01 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27966c0e-6994-310e-82cf-72cb3e41a310 | -9.13709 | -47.57705 | 2025-06-01 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dc0293d-00d8-3623-a851-0dbff7313068 | -8.12963 | -49.58711 | 2025-06-01 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 51e34f53-5b78-3bb4-b666-03ff0588a110 | -7.22904 | -43.12207 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 666bc0e6-a141-345b-a384-861cfcf443cc | -6.45147 | -45.72984 | 2025-06-01 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1604aea6-0341-36c7-a278-2560dfb65987 | -7.49469 | -43.12426 | 2025-06-01 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 84bfaae4-ca3e-3b04-8f2d-2cd58ea55cd1 | -10.65558 | -49.43344 | 2025-06-01 04:08:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0938520-2334-3c0e-a6e5-15c4fea00f54 | -9.6719 | -49.73351 | 2025-06-01 04:08:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1dcd5fa-1a19-307b-a1d7-32f41e9bab97 | -10.14494 | -52.14014 | 2025-06-01 04:08:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7075e726-7952-3f82-bbec-926f25376520 | -10.86262 | -47.46079 | 2025-06-01 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15d91f35-fbbc-3c0d-8fd9-8004063a2f29 | -10.67593 | -44.41134 | 2025-06-01 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6558c229-ecfa-32c7-975d-8f2e25dbad4d | -9.39944 | -48.42014 | 2025-06-01 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e5c9615-3ce8-353c-b1d6-370f0258633a | -7.23125 | -43.12977 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 863974ae-48b3-35be-a74b-b34b978e10f9 | -9.33612 | -40.29124 | 2025-06-01 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a2365d96-97ed-3ab3-877f-7f232e3c490a | -7.58348 | -45.86549 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b03d632-435f-3591-bd92-5b13dde67513 | -10.68137 | -47.20178 | 2025-06-01 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a0e23989-1429-3fed-ac6f-d348be4a87fb | -7.22118 | -43.12818 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a0f41ac6-f8d6-3a82-80ab-28ea30fd2b49 | -5.68388 | -46.57357 | 2025-06-01 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e636fb28-13d8-3a7b-83c7-94a1ee865fb8 | -7.51817 | -46.86045 | 2025-06-01 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e5c3b03-f5c1-3204-aa3d-d89250f1cf50 | -11.57363 | -47.45784 | 2025-06-01 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8b1a2071-364a-3343-9532-6fe472f1e01a | -9.54235 | -36.95359 | 2025-06-01 04:08:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5226263a-2e5f-3cae-b98a-927ddf6d3aca | -5.05741 | -43.24978 | 2025-06-01 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
