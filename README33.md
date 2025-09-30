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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b2af0ad-1dab-3696-b2d2-3d47e151da5d | -6.54768 | -43.5494 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b791d2a-feba-37b6-925c-254e556016c7 | -13.79213 | -47.86884 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d379e37-8a88-3bb6-aec2-e946d7ab6847 | -13.4981 | -43.81434 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aaca3f67-a751-3e3d-a16a-19fa86411838 | -11.75338 | -44.74756 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a0c3647c-fb02-3d51-a1e4-9a8f5d342c4d | -5.71797 | -42.83387 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 80243b16-6dc0-3621-9f72-3b7d9720dbb4 | -13.73081 | -48.68662 | 2025-09-30 03:49:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc7b86aa-e5d5-3936-a2af-24b0c991a927 | -7.01322 | -45.20857 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26579a82-2b6b-3f47-816a-25f34c5e9d55 | -15.22983 | -48.02917 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67c47628-7089-302e-81a5-438634adf382 | -14.50458 | -46.19111 | 2025-09-30 03:49:00 | NOAA-20 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 339999d1-16a7-3ddb-a675-71562d1e59c9 | -15.10864 | -46.49045 | 2025-09-30 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae4e1bce-ecb2-3dfa-9b46-858949581cd0 | -6.06041 | -42.45275 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fb097d6e-dfca-3d97-9a66-8826560bb376 | -15.78219 | -43.6609 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cd501e7-7efa-3f61-af03-2b4903efe91b | -14.72513 | -45.21301 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e052515-637a-3d7e-87fe-68d0c946e3c1 | -13.38659 | -48.07375 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b012c125-47e5-34bc-a973-b969a9b9677e | -14.70224 | -48.14292 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f77c550b-56e4-3744-86b9-21b236e66f7f | -11.0662 | -47.82167 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e51737dc-c577-3e72-9613-98d21fe97c37 | -5.96849 | -44.13456 | 2025-09-30 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba55f6de-a0d8-39d9-8766-003a86ab4caa | -13.3827 | -48.06157 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 728439a5-9ea5-34b6-93c0-cc627ebd1eba | -6.09889 | -42.66201 | 2025-09-30 03:49:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 38a54ead-ae26-367e-a317-666d96d9794c | -6.57518 | -43.41755 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2cc4600a-bdab-3c0a-b6b4-f1d4086f43cc | -13.61761 | -48.03136 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6702e47-427b-3513-9cc8-61b603914feb | -15.40069 | -40.86844 | 2025-09-30 03:49:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a525c674-4f5a-3990-a677-a552dab68a10 | -13.62305 | -48.03227 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ea005b5-de5c-3da7-a8b7-3f045cca903c | -5.71142 | -42.87259 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5c4a7087-dc01-3872-80a4-0ddc475a6349 | -5.72306 | -42.83044 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d0160447-c665-3a90-a1c9-33673c43f057 | -13.2315 | -48.44939 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7255b4c8-e7be-3a46-aa3d-8cacb1f12fd2 | -11.21875 | -47.2074 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0de9f29-96b9-3fa5-9bfb-4ee59b59d35e | -14.5152 | -48.38768 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59188179-69c1-3f11-9cf9-d2515c923bb7 | -12.17409 | -48.35532 | 2025-09-30 03:49:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1fd2cd5e-3e2b-375f-8233-c507752db967 | -14.55269 | -48.48708 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 15948100-6c2a-3f25-a0da-a518bea98497 | -6.27519 | -44.06671 | 2025-09-30 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6bf8c11e-a90e-395b-8d37-30d048413da1 | -15.83203 | -42.02094 | 2025-09-30 03:49:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e27b7753-0ff7-3400-a3cf-fe3675b52bd4 | -6.37107 | -45.63046 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d760bb3e-425c-3451-aada-72e92ce455f4 | -12.8419 | -47.02054 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1cf66df-a0a3-3384-ba11-eb0833d5efc3 | -14.72541 | -45.23583 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d693799b-0a0e-3335-a5ab-0fd9a1f44144 | -13.8444 | -47.49466 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b49cf65-780d-365c-bb2f-179d9ea26fdc | -14.694 | -48.23907 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6add4dbd-44ee-3e64-aadf-09e6e8ff0d60 | -5.75803 | -42.54429 | 2025-09-30 03:49:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8651d5c2-6fca-3689-ac0c-6d49c99154b5 | -7.28691 | -42.87006 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 38942fb7-e8ea-3825-9ba2-318eb92c0007 | -15.60228 | -47.82836 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a83a261-078e-3cb8-ab47-c6a7fbe31bef | -5.77747 | -42.85625 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 543a36dd-6f4c-33f6-9c0e-010b664403f7 | -16.41168 | -43.12349 | 2025-09-30 03:49:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db4c17a8-dae4-3ca4-972a-67108a9b652b | -13.59875 | -48.04109 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c81bc20-2515-373a-a6da-b621fb1ffea1 | -14.70143 | -48.14692 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa5cc66b-c663-33af-bbbb-d87c1d28f31a | -14.51179 | -48.46397 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 771dcf35-1372-302c-ac79-d3bce8c6f42d | -11.75207 | -46.85004 | 2025-09-30 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7648114e-2312-300a-bcea-6f6e70d7e704 | -6.76325 | -37.89449 | 2025-09-30 03:49:00 | NOAA-20 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8826f579-f7b5-355e-9a04-8334c508751f | -14.70546 | -48.23775 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4c56e32-8928-37d0-9503-a356e556df47 | -7.56911 | -42.40211 | 2025-09-30 03:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4c08ab31-aaa2-3dba-967e-b6b7e160537b | -11.07113 | -47.82611 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe747f37-d120-34e2-8d24-5d3a5b9af347 | -13.39824 | -48.07217 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b677149c-9180-3515-9e53-8c1ef95d4b29 | -14.3862 | -47.13633 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c86e1a94-9b89-3c4d-a917-c7ab16cb0f16 | -4.95644 | -47.60311 | 2025-09-30 03:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf6dcdfc-f092-3802-b3d8-102cd955b3b0 | -15.73052 | -48.89724 | 2025-09-30 03:49:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b13a0cdf-1139-30b9-a5a1-9318a19a0761 | -13.73326 | -48.6745 | 2025-09-30 03:49:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cbca3ec-cbaa-36ee-86be-dbc920c9b3dc | -7.04357 | -45.18412 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cfae613-f626-383a-8e6d-20e6eb08d628 | -6.5057 | -45.23117 | 2025-09-30 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83cb1338-c856-3a88-96bc-d7f10e3165ad | -5.31265 | -44.78955 | 2025-09-30 03:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8efa19e3-7bf6-356b-82fe-6825cfa7aedf | -17.03643 | -43.41702 | 2025-09-30 03:49:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ba1e8dd-6bbb-31a3-b77e-9bcb1db63278 | -6.40758 | -43.75902 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4fa8048-8b63-37a6-9987-b1fb02fb9bb7 | -12.84892 | -47.01191 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f655dbac-b95e-3f39-b135-c2b9d816c67c | -5.81265 | -42.78254 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0b6d1cd5-f7f4-32c9-9e14-0eb362af2d4c | -7.11668 | -45.53205 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d5ab567-a586-321a-8382-1706cd1fcd25 | -7.10826 | -45.54967 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41a5a0c9-f29c-364d-9b5d-181713b30677 | -6.07879 | -44.06442 | 2025-09-30 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a160e20e-7414-33af-8a9d-80a28f83044d | -6.07568 | -42.61577 | 2025-09-30 03:49:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| edbe84e4-7e88-33bd-b6b2-309eab4de9e0 | -12.8605 | -46.89808 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af5e00fc-76f4-3be7-9539-a09f4dc89141 | -5.86518 | -45.77761 | 2025-09-30 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dd28bb7-27a2-3db1-ba0e-4eb360e51516 | -12.96065 | -46.40884 | 2025-09-30 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36d5c036-62b1-3ebb-8138-459ebb825f2f | -6.0265 | -43.9348 | 2025-09-30 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b8bddb1-de30-33d2-b037-4f981e555c43 | -17.39133 | -47.13249 | 2025-09-30 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 093bbff8-f032-3108-9b2b-9b6cd23c4d56 | -7.36054 | -42.1262 | 2025-09-30 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 69b10160-cbc0-3ad6-92c7-d845811c9866 | -12.75029 | -46.85206 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 346953f1-6bde-34b5-a480-b027d80110bd | -12.82732 | -47.00342 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b5bb427-143c-3ffd-8ace-d38528265d75 | -6.10819 | -42.65945 | 2025-09-30 03:49:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a23012d4-e5ff-31be-81ca-ff497ae58c00 | -6.88439 | -44.52748 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c43c78d6-b1ca-3cee-9a35-bc78bf864ba5 | -13.39281 | -48.07095 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d58c7737-a542-31e0-af21-a58eb1ca420c | -18.02333 | -40.59595 | 2025-09-30 03:49:00 | NOAA-20 | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 941ce9d6-61aa-3ff2-a057-e44d2d3535f1 | -15.92052 | -46.24361 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25c7c49a-1770-3afd-add3-3b04e28de426 | -15.24751 | -48.74643 | 2025-09-30 03:49:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fec918c-0a6e-3fea-be3c-1924516adce9 | -14.76411 | -45.75608 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09a9008c-fac6-308d-87cf-da7fb84a801a | -11.91279 | -48.06409 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 46f98523-3f3e-3003-87fc-201d1ada590a | -11.74802 | -44.75132 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07c50cc7-f028-33eb-be8e-27da39c69091 | -13.09369 | -47.03313 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f8ef2bb-b4c0-3979-8a05-db9be3a8a310 | -13.00317 | -49.44056 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6cf2932a-1942-3992-aa00-1b63b27d1c53 | -12.17977 | -48.35643 | 2025-09-30 03:49:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b78fb121-6a56-3b71-8ea4-876e2ba0db4f | -15.29111 | -46.41483 | 2025-09-30 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f12a0b84-1cb3-323b-86e1-bce10565a224 | -17.50058 | -43.47747 | 2025-09-30 03:49:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50700bcf-1295-3acb-9bc7-f52e4ecdd502 | -19.3089 | -43.81015 | 2025-09-30 03:49:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a1fecfb-93a4-3e81-a042-4d9ab3c05e2d | -7.17434 | -41.70074 | 2025-09-30 03:49:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 82f508d2-0df7-3260-99ad-a2a5515f200e | -13.79665 | -47.87407 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0a94d58-9b5c-35e9-9be4-6faca1db830b | -6.37293 | -45.64869 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5da5eecb-3f9d-31c4-a1b7-24b104a6a201 | -13.78255 | -47.94521 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87d2ebe5-2980-337a-a68b-522e0bd1aa19 | -6.57595 | -43.41308 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1a080ced-8f09-3956-834a-46fb758e3c1c | -13.62253 | -48.03489 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9091f688-9a10-338e-96be-8f9701e95aac | -13.81456 | -47.47926 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaa5c48e-4451-3287-adba-080c6a083f85 | -13.7215 | -48.64594 | 2025-09-30 03:49:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4510a672-de95-39e7-b7d3-a394c46c8d8e | -15.28091 | -47.85847 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f08f3802-00f3-3040-bb77-cf4a3e0251fd | -11.88718 | -48.02805 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a111eaea-b0fa-334a-a10d-3c232641feed | -14.58772 | -48.28472 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README34.md)
