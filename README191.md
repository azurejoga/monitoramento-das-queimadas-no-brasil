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

## Dados Diários - Página 191

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab36cd68-1206-3adb-973a-a48bacdc5c0f | -13.1163 | -51.1765 | 2024-10-04 13:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 4e4e5cef-5d3b-3780-937d-913ac4e368ba | -13.0786 | -51.1385 | 2024-10-04 13:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 605b6c45-71c5-3431-9bf9-7af25ca22079 | -13.1595 | -48.6322 | 2024-10-04 13:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 92da592d-b88f-3aa2-9a8b-e13f71f41efe | -13.1443 | -46.3261 | 2024-10-04 13:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 56b92cf8-a5ea-38a1-b49b-c337fa8865bc | -13.1447 | -46.3033 | 2024-10-04 13:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 577a5f7f-a34f-34a2-bbb1-205024fc305d | -13.1787 | -48.6295 | 2024-10-04 13:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 7dc058eb-73f3-3e02-a0b7-dec0eb22d5a9 | -13.1791 | -48.6073 | 2024-10-04 13:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 53d76029-7019-3659-a487-eb593fd5be71 | -13.199 | -45.492 | 2024-10-04 13:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 4f0801c4-ba0a-3864-87da-d00ca2159e8a | -13.5255 | -48.6018 | 2024-10-04 13:06:22 | GOES-16 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a32820f0-dce0-38dc-a8b6-f36f33b0e3ec | -14.5362 | -49.2898 | 2024-10-04 13:06:28 | GOES-16 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 4a1336ed-cf16-38b0-a144-3cb0fb702098 | -15.6304 | -47.2063 | 2024-10-04 13:06:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| af8c6933-b910-374e-8cbf-c02d39745b7f | -16.613 | -57.1965 | 2024-10-04 13:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 220.4 |
| c0bd065b-fd83-3eb0-9d9f-3d62fc31be3f | -16.6127 | -57.217 | 2024-10-04 13:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 2e240312-7f37-3727-88d1-849834304972 | -16.5925 | -57.2602 | 2024-10-04 13:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| d9721a60-ff54-3f29-8c40-19084a14db69 | -16.6133 | -57.176 | 2024-10-04 13:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.9 |
| 70f8da9d-8f1e-376c-a1c3-dd538b99a0e8 | -19.1134 | -48.2833 | 2024-10-04 13:06:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 59c33d52-2c5b-3b0e-b07a-905abb26f8ae | -19.6122 | -46.2632 | 2024-10-04 13:06:54 | GOES-16 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 2fd25009-6876-3f8e-abb5-4eecf466db20 | -6.9479 | -47.6668 | 2024-10-04 13:15:46 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 0e3a96c9-b2e5-3365-bdc9-c39ae1bbf166 | -6.9477 | -47.6887 | 2024-10-04 13:15:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 7251e852-bb07-3bf4-b4c3-70c015d214ef | -7.2565 | -45.0079 | 2024-10-04 13:15:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 764a0eb7-11d9-3bbd-bcc1-a58597a46ef6 | -7.6484 | -45.2446 | 2024-10-04 13:15:49 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 55f33833-7489-327f-8ae2-203f33812482 | -7.7567 | -44.0415 | 2024-10-04 13:15:50 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 7df8f542-bdea-35d1-83d2-d4be1bab9aa4 | -8.1951 | -43.6703 | 2024-10-04 13:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 71771647-6322-3ab5-8368-171de81595a7 | -8.1948 | -43.6936 | 2024-10-04 13:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 198.7 |
| e32cdc95-c0b3-3fb0-876f-5c05a5848c42 | -8.1759 | -43.6957 | 2024-10-04 13:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 74af23dd-b908-3524-a7fe-bfa49c3006e8 | -8.3194 | -42.8343 | 2024-10-04 13:15:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| d1651cab-b745-3758-a7cd-f09c79c77340 | -8.435 | -47.0977 | 2024-10-04 13:15:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 397e951d-e4b2-3017-9b7e-cd540756f12e | -8.4535 | -47.1181 | 2024-10-04 13:15:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b4d1aaf0-4f5b-3288-853d-86d13e1f14e8 | -8.4347 | -47.1199 | 2024-10-04 13:15:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| a3452cb0-233f-31ab-94ba-c9d00ac750e6 | -8.8362 | -45.1688 | 2024-10-04 13:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 527ab375-6285-326b-bf0f-a703cc65c7eb | -9.1041 | -50.902 | 2024-10-04 13:15:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 482.5 |
| 182013d5-2076-36e2-ac2b-1950c7a980bc | -9.1039 | -50.9231 | 2024-10-04 13:15:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 209.6 |
| e5f203e8-7e7b-375d-aff1-674d5cff3374 | -9.0853 | -50.9036 | 2024-10-04 13:15:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f9f7a8c6-4944-302c-ba96-3ef957fcf1b1 | -9.8855 | -47.2124 | 2024-10-04 13:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 83990d2c-fdfa-3b99-a764-7465055cf69f | -9.9822 | -42.0976 | 2024-10-04 13:16:02 | GOES-16 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 90ad03c7-134d-39f0-9eda-dd969450ef26 | -10.2381 | -47.7038 | 2024-10-04 13:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 09f945f8-a672-3c25-8654-847bf7ed00ee | -10.2378 | -47.726 | 2024-10-04 13:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 9c9676c3-353a-3cc0-838c-aafe0ececd2f | -10.2764 | -47.6774 | 2024-10-04 13:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| b6deda27-6a75-37de-a643-97e93aaa5b36 | -10.2571 | -47.7017 | 2024-10-04 13:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 417.1 |
| e27a6588-24da-3146-aed0-a479f69eb502 | -10.2574 | -47.6796 | 2024-10-04 13:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| ea1f6ab5-5295-33c9-a243-f6de53089333 | -10.6367 | -45.2027 | 2024-10-04 13:16:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| a8bba2b9-a522-33ba-9edc-c136d8af6a72 | -10.8216 | -45.5444 | 2024-10-04 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| cb683750-ea1e-366b-a19b-158b024a5c80 | -10.7118 | -47.7149 | 2024-10-04 13:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 75f92035-4d6b-3062-a29e-4a84f9948b87 | -10.7359 | -46.1465 | 2024-10-04 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 651.9 |
| f010d1ee-9b78-38dd-b9d9-d40448d546f9 | -10.7355 | -46.1692 | 2024-10-04 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 522.2 |
| 749efca1-aaf3-34da-9241-da039a3acd67 | -10.8021 | -45.5698 | 2024-10-04 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| db9e040d-3b42-30f7-b61f-fa8ec2496609 | -10.7309 | -47.7126 | 2024-10-04 13:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 0d5bd3e7-f9ed-3c06-8cab-1e8f4d828aed | -10.8018 | -45.5927 | 2024-10-04 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 7f41d9d4-6b59-3610-8d32-0c61d4ad8c8c | -10.8661 | -46.3331 | 2024-10-04 13:16:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 3eb0eb5e-a52d-3183-99c9-a465cac18841 | -10.7352 | -46.1918 | 2024-10-04 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 43df6a7e-d099-3f37-b824-d9998549ef60 | -11.0345 | -46.5143 | 2024-10-04 13:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 92155436-90ab-3888-81ff-93a49d419a6a | -11.0349 | -46.4917 | 2024-10-04 13:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 5fd893c3-fd8e-3366-9bb2-83eedb69088d | -11.0536 | -46.5118 | 2024-10-04 13:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 266.1 |
| 52fc8e65-814e-3ef6-990b-5fc7f8bc5fb2 | -11.1388 | -45.9577 | 2024-10-04 13:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 5f1be928-14e7-3036-b0dd-494fb1f09d9c | -11.2369 | -46.9597 | 2024-10-04 13:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 348.8 |
| 29473472-f1a0-3b1a-98be-376513d249a2 | -11.2372 | -46.9373 | 2024-10-04 13:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 72bf5561-aee9-38f2-8ae2-3e2ddb5c5c31 | -11.1384 | -45.9804 | 2024-10-04 13:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 437.3 |
| c202ecf1-43ca-30e5-af42-078f93fc9244 | -11.2971 | -43.4088 | 2024-10-04 13:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.3 |
| b6c72f95-b02d-3bb5-92fb-b6147908dab5 | -11.275 | -46.9548 | 2024-10-04 13:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 653.7 |
| 0dc78d85-7861-30ae-aaff-9d9232d32c3f | -11.2754 | -46.9323 | 2024-10-04 13:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 155.5 |
| b01c9d25-7a53-31a4-b8ca-d0dad4c30237 | -11.2563 | -46.9348 | 2024-10-04 13:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 437.4 |
| 322827a3-6b8f-3e7f-a448-1cacd00779d0 | -11.3853 | -47.2088 | 2024-10-04 13:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 6c50c81a-fa48-384a-9d17-a17d25a4df03 | -11.6804 | -47.8156 | 2024-10-04 13:16:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 89482fbc-e7e2-3766-8e0a-a8e1f5497810 | -11.7415 | -49.9925 | 2024-10-04 13:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| e1347ad2-a4c4-3826-a766-70becf9609bc | -11.7412 | -50.0141 | 2024-10-04 13:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 4532115f-d9a0-34b6-8167-87ec947e9bc8 | -11.9105 | -50.1447 | 2024-10-04 13:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ff615186-7491-3ee2-ba20-530f88c715c2 | -11.9487 | -50.1402 | 2024-10-04 13:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 2d4c3158-79b6-3907-9bb7-e6af9e20eaf1 | -11.9296 | -50.1425 | 2024-10-04 13:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 282c4515-5eef-3617-8a13-763b7100b565 | -12.7815 | -50.5758 | 2024-10-04 13:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 161.4 |
| c3120404-9acc-37e0-92ab-d42251ff3ec0 | -13.1779 | -48.6737 | 2024-10-04 13:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 35104542-0d13-3e65-8828-7d9fb66dd759 | -13.1443 | -46.3261 | 2024-10-04 13:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 946bf408-ac09-3b43-85bc-40ae7abcb307 | -13.1447 | -46.3033 | 2024-10-04 13:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| b53e9648-789d-35a6-bc3e-b6616aca3718 | -13.1787 | -48.6295 | 2024-10-04 13:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 60f0341d-692c-3001-9997-c762565c892b | -13.1791 | -48.6073 | 2024-10-04 13:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 9265d0d0-c3db-3a8d-83b0-a7b74c34a081 | -13.2685 | -51.2428 | 2024-10-04 13:16:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| b4928632-1c22-3634-b094-45f74befeec4 | -13.5255 | -48.6018 | 2024-10-04 13:16:22 | GOES-16 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| de737a84-fd8d-3bbd-b1ce-2b604885b204 | -14.0378 | -45.1648 | 2024-10-04 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| b8b11300-5b38-38ef-8433-a0d5e5c3fc02 | -14.0382 | -45.1414 | 2024-10-04 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 1bb2e62b-107d-3c42-9d8e-483860b66f0c | -15.4247 | -47.6736 | 2024-10-04 13:16:32 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| af9a30ff-ce33-3625-a294-b47efce4b40c | -15.6304 | -47.2063 | 2024-10-04 13:16:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5f1da7b2-dd95-379f-9d63-146ed800ed74 | -16.6313 | -57.2762 | 2024-10-04 13:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 53436222-20e4-379d-b3a7-f1ac46c01de9 | -16.6127 | -57.217 | 2024-10-04 13:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 2ca19364-aaf4-3f23-9ad5-7c206e7e0827 | -16.5925 | -57.2602 | 2024-10-04 13:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| d2b4855f-7fd0-3984-8adb-05c964e9dfcf | -16.6117 | -57.2784 | 2024-10-04 13:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 26e99ee0-7f93-39e8-8b40-3437680630aa | -19.1134 | -48.2833 | 2024-10-04 13:16:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 48246c82-5174-3f6c-9d53-40f7e4364190 | -19.6122 | -46.2632 | 2024-10-04 13:16:54 | GOES-16 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 103.7 |
| afdcb9cb-2517-3e86-8aaa-15d0c9b72a31 | -19.6115 | -46.287 | 2024-10-04 13:16:54 | GOES-16 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 97.3 |
| f42489f0-cdca-3124-a66c-94fd370e25f2 | -6.9477 | -47.6887 | 2024-10-04 13:25:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 8b145495-1be4-36c1-966d-c3812d93a2ed | -7.2565 | -45.0079 | 2024-10-04 13:25:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 43428e96-f198-3c35-9496-d73f642b2978 | -7.3136 | -44.9343 | 2024-10-04 13:25:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| b4fcfb75-3fad-3838-9368-f435e6421fec | -7.8539 | -45.3611 | 2024-10-04 13:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| b3b12430-5377-3eb6-baa8-5f4a6b249523 | -8.1948 | -43.6936 | 2024-10-04 13:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 318.6 |
| 402cf176-400c-3e73-a8b1-546995331f0b | -8.1762 | -43.6723 | 2024-10-04 13:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| aa22d965-3613-38d9-80ea-6672a86e73ad | -8.1945 | -43.717 | 2024-10-04 13:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| ac6f2c90-e240-31bc-a3ce-b767dedf0c42 | -8.1759 | -43.6957 | 2024-10-04 13:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 26bc5236-20f5-372a-a7f8-e30a5a0517c9 | -8.1951 | -43.6703 | 2024-10-04 13:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 791cf993-29f1-34a6-bfea-5b0c2917cde6 | -8.2859 | -45.4317 | 2024-10-04 13:25:53 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 24c5a3a7-2ca5-3cd0-a66b-5f7294d14979 | -8.4347 | -47.1199 | 2024-10-04 13:25:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| ce88d2db-cd77-37f0-a181-a0bfeaf97400 | -8.435 | -47.0977 | 2024-10-04 13:25:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 4a2f0c3e-b31f-32d6-9be6-911a5a4cbdcd | -8.8362 | -45.1688 | 2024-10-04 13:25:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |


[Clique aqui para ver as próximas entradas](README192.md)
