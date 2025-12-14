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
| 9b6da687-9e76-3166-b9e0-8f785ba86ab1 | -4.93368 | -43.95591 | 2025-12-14 00:32:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b7e6ab9a-eeb1-31f8-854e-eb4a7512cf64 | -5.39938 | -44.67846 | 2025-12-14 00:32:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 273f3794-6818-3910-a6e7-07a15b8fd2ad | -3.4478 | -41.67205 | 2025-12-14 00:32:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 6db04880-19a3-3e35-a8e0-12b90bec073b | -4.09923 | -48.95279 | 2025-12-14 00:32:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2ebbd414-a644-327f-8fd9-0a0b8dc63a84 | -3.44231 | -41.63728 | 2025-12-14 00:32:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 925a8ff2-2072-375f-bed9-cd59e81fe2e6 | -3.67482 | -44.82901 | 2025-12-14 00:32:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 181d6659-6e83-3d48-b5e8-3fc57bd85219 | -4.47524 | -48.80362 | 2025-12-14 00:32:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3db3c3e6-dd1f-3618-844a-c7b6b8483294 | -8.04087 | -43.09292 | 2025-12-14 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 77dffd9d-eee1-3b45-a8ea-6791bc771fd4 | -10.76892 | -44.93592 | 2025-12-14 00:32:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ba3cc789-3892-3183-9c84-32b75f047fa5 | -9.86337 | -50.56512 | 2025-12-14 00:32:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 77a3318f-a066-302e-a973-be92e1279b35 | -3.43592 | -41.6435 | 2025-12-14 00:32:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| ed5a3ec8-4e93-35de-a328-eb431aa2414a | -1.3581 | -52.63379 | 2025-12-14 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1deff4db-45cc-3091-9214-1cc22a98f118 | -2.19093 | -53.66601 | 2025-12-14 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eb30e39a-94fe-30e5-8339-cc9ddaa564f0 | 3.38614 | -60.51506 | 2025-12-14 00:34:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 18.2 |
| b12a6be9-7008-3d76-981a-d15d91ad6d33 | -2.08984 | -56.47993 | 2025-12-14 00:34:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 5a7aa610-c78e-3baa-b69c-f9179350e782 | -2.14292 | -45.46701 | 2025-12-14 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 83f11a77-31be-327e-a409-df83c00b4734 | -3.79857 | -49.03043 | 2025-12-14 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ed846eef-ee99-3063-a3e7-1a0f1e469cfc | -2.84387 | -45.40727 | 2025-12-14 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a8bf9399-6048-35b9-8917-9f83b81e64d7 | -3.40841 | -52.19921 | 2025-12-14 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 5d8e1f1a-9fde-34c9-97b9-df49691bcb91 | -3.5317 | -48.91873 | 2025-12-14 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 781a6ec9-bd9f-35e5-a1d9-5ca484ae4007 | -2.0787 | -56.47125 | 2025-12-14 00:34:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| b241fe26-782b-3269-9634-feedff265850 | -3.31293 | -50.97073 | 2025-12-14 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1c57cbb2-68a9-3ea8-b584-04bf56027ecb | -2.85615 | -45.40548 | 2025-12-14 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 0aab89b0-dd8b-30ec-9f31-5a7358a9809a | -1.78699 | -54.1511 | 2025-12-14 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 0ffb0c9c-234c-3b0d-a330-8e29156a144c | -2.28952 | -45.58674 | 2025-12-14 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 32.9 |
| b2793de5-a87a-3cc9-8688-a95b0d01456d | -3.43892 | -49.02571 | 2025-12-14 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 35f51d23-1116-376b-9985-4625b8a543d2 | -1.39181 | -52.54053 | 2025-12-14 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d0ca9627-d40e-3e0f-812d-d3dc0c8f43a4 | -2.47695 | -45.43708 | 2025-12-14 00:34:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 785452e2-88f0-330b-b753-c8aa40b922f8 | -1.51769 | -45.67535 | 2025-12-14 00:34:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| dac8adc5-7733-3aef-af32-65334058b78b | -2.88423 | -44.97684 | 2025-12-14 00:34:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 33.7 |
| da1a68df-cb4c-3cda-8795-673f812858f9 | -2.25015 | -53.67831 | 2025-12-14 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| fb75877a-815d-3c5c-8204-c5940d3d9230 | -3.5266 | -48.9258 | 2025-12-14 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 8b1de77a-5823-35f6-b81b-bcd44de42f1b | -0.96927 | -49.14851 | 2025-12-14 00:34:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a551c13d-2cb2-3af1-99ef-3bb2958c68ec | -1.44675 | -46.2884 | 2025-12-14 00:34:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 0c4d7224-e871-3fad-8b5f-4503cd2a3487 | -1.39057 | -52.53155 | 2025-12-14 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f29640cb-3846-3452-a1fa-eb0394966ce4 | -2.09017 | -56.46971 | 2025-12-14 00:34:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b97e28f1-5431-3b88-9615-3dca15c7a619 | -3.80789 | -49.02918 | 2025-12-14 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cfad2d48-fb0c-359f-b569-9717a6d7e7eb | -1.50898 | -53.99475 | 2025-12-14 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2c8e4c30-6bab-37ca-9aa9-77746c59f40d | -3.13132 | -52.45967 | 2025-12-14 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bf6b039a-df43-31b6-9c2c-6a733b0f920c | -1.5203 | -45.69329 | 2025-12-14 00:34:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 29.6 |
| b4a476da-b7b4-33c5-b49d-55aa0295c84f | -1.28419 | -53.1655 | 2025-12-14 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 42d8472a-28fb-398e-9dc5-e8c0dc03dba3 | -3.15621 | -54.60149 | 2025-12-14 00:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 521e4781-7af5-30da-95cb-a80522a4ce72 | -1.96968 | -46.48672 | 2025-12-14 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9b926270-f7d1-3003-a7f1-63434b2bf8f0 | -3.53313 | -48.92873 | 2025-12-14 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3a9d9339-1aca-3f77-be7d-8f6b6463b3f8 | -3.52593 | -48.87854 | 2025-12-14 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 43625c5c-ab4d-331b-b404-495d54dfa109 | -1.79327 | -54.05401 | 2025-12-14 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7885cbc0-eba6-3bdd-8766-686de86f42f7 | -2.27731 | -45.58857 | 2025-12-14 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 97782b00-e237-363d-afc7-dae8a52204a1 | -2.09234 | -56.48507 | 2025-12-14 00:34:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| b1216aee-9756-3085-895c-9c8a60f67f58 | -2.84168 | -46.72587 | 2025-12-14 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8288e6a1-b505-3150-8ccc-edb0ae433bec | -1.13798 | -52.03624 | 2025-12-14 00:34:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2808a8ff-7997-36a8-a8ea-23d554e89c11 | -2.3453 | -53.9096 | 2025-12-14 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3122f74e-ab8f-30c1-bfc1-907be6bdc85a | -2.11178 | -54.21832 | 2025-12-14 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5dca6cad-b9d0-3af8-b4ae-31345800c978 | -1.52998 | -45.67361 | 2025-12-14 00:34:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ad52b64e-eef8-32a1-93f8-a6b73e075a05 | -2.19231 | -53.67607 | 2025-12-14 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0e4bc2ed-e507-3c5e-9f0c-ccf11e25be3e | -2.07632 | -56.4661 | 2025-12-14 00:34:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9fe1209e-ab91-399a-a65c-74899b0a7a2a | -1.53257 | -45.69148 | 2025-12-14 00:34:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 81406df4-d95f-321e-84dd-1c5398108f56 | -2.88134 | -44.95736 | 2025-12-14 00:34:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 36.5 |
| df386a3b-57d9-386c-9175-f157c3c7601f | -2.85054 | -45.39444 | 2025-12-14 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 5848bf42-513b-31eb-9e73-4c8424243d53 | -2.8816 | -44.96291 | 2025-12-14 00:34:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 875faf98-9c44-3a85-8ef4-a02fd4ebc442 | -3.13007 | -52.45049 | 2025-12-14 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6a8272bd-89e1-30ba-a20f-63b5a8b6527c | -2.08779 | -56.46458 | 2025-12-14 00:34:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| d96c5536-143d-3274-8896-990d34235304 | -4.00905 | -49.28507 | 2025-12-14 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 56eacc76-e8ec-3350-b362-6849f231dfd9 | -1.36821 | -53.57253 | 2025-12-14 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7f8638c3-a0ce-3545-958d-a76921a1de4b | -1.42862 | -53.47876 | 2025-12-14 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1174558c-cb92-31ed-9ce4-e144fe118a49 | -0.96784 | -49.13811 | 2025-12-14 00:34:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c533854b-0820-3cce-a489-8d741565c38f | -3.52521 | -48.91577 | 2025-12-14 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| c32cff53-ac7c-3510-8588-1178fd1cc743 | -2.85307 | -45.41245 | 2025-12-14 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 3a8d3969-32eb-3dce-be33-93e272916474 | -2.14025 | -45.44872 | 2025-12-14 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 4d2328ea-456b-3a4b-afb6-b2d744d6cfd0 | -2.88434 | -44.98236 | 2025-12-14 00:34:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b4f0abe1-205d-3cf2-a127-5ba429eaa2ee | -8.0324 | -43.1022 | 2025-12-14 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.5 |
| 974738fb-0db0-370a-a1a6-f235267804af | -1.5296 | -45.678 | 2025-12-14 00:40:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 562b985c-6066-3715-aae5-a62633eb92e8 | -8.0327 | -43.0786 | 2025-12-14 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 0e375d4f-bb22-39c4-ba03-a4b4a3a55937 | -5.6611 | -39.2607 | 2025-12-14 00:40:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 56.1 |
| be83cf53-909d-3840-9571-440cbf829f39 | -5.6797 | -39.2841 | 2025-12-14 00:40:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 55.0 |
| bf188050-0e96-3006-aaab-f0abed30d455 | -5.6608 | -39.2858 | 2025-12-14 00:40:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 51.1 |
| fefcd790-4ac3-3f34-a96e-bf7b78f1153d | -5.68 | -39.259 | 2025-12-14 00:40:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 59.6 |
| b66c5b70-6136-3914-ac4f-ab1737aea89a | -16.2383 | -58.8395 | 2025-12-14 00:40:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 1167c872-743d-393d-8a19-70b7499074f5 | -16.2188 | -58.8414 | 2025-12-14 00:40:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| dfc2f593-4437-35db-b322-301fa38ad0f1 | -2.0768 | -56.4674 | 2025-12-14 00:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 34eac748-bf2d-3529-bb07-21b9b8bd76a1 | -3.6277 | -45.6797 | 2025-12-14 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.8 |
| b2b2de0b-ab4c-3c74-b5a4-536896110046 | -8.0513 | -43.1001 | 2025-12-14 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 82e64924-ae53-3319-aa2a-a0b0617e84e1 | -2.8875 | -44.9666 | 2025-12-14 00:40:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 0bc66ac5-1b8a-3ad5-a316-69f9435ea8cc | -8.0696 | -43.1452 | 2025-12-14 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| fb2eb471-7e26-37b5-adb8-9b6cedc49f39 | -1.5296 | -45.678 | 2025-12-14 00:50:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f65dab05-34f1-3daf-bd7e-f3a50bdb88ab | -2.0768 | -56.4674 | 2025-12-14 00:50:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 4581e466-b5af-325d-8268-21efa6f51b77 | -8.0513 | -43.1001 | 2025-12-14 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.1 |
| 8748d077-0367-346e-8d6c-4b93e7e83c92 | -3.4451 | -41.6413 | 2025-12-14 00:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 46903277-d28c-3296-9d01-f8c35211f39c | -2.4768 | -45.4309 | 2025-12-14 00:50:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| da187394-7cb2-3213-8d52-b202f93d49df | -16.2383 | -58.8395 | 2025-12-14 00:50:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 26bfc012-0569-3cfa-99a6-fb375245c72f | -2.4767 | -45.4534 | 2025-12-14 00:50:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f39b8ff9-ce90-3188-a9ea-fcb3c9440c1d | -5.6797 | -39.2841 | 2025-12-14 00:50:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 57.5 |
| b2eaa3c0-f1fb-31e4-b72b-6d152ae56018 | -8.0324 | -43.1022 | 2025-12-14 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 134.5 |
| 5f430a62-177f-34f5-b7a1-cef24f206baa | -8.0696 | -43.1452 | 2025-12-14 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 0524ab3c-f0d1-3876-b780-bc6ec1218a1c | -5.68 | -39.259 | 2025-12-14 00:50:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 966d41b5-9b14-37d1-8c35-7dbee7e5930b | -8.0327 | -43.0786 | 2025-12-14 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| db8bc9c8-5e78-30c8-ae4f-b36e57f79dc2 | -2.8875 | -44.9666 | 2025-12-14 00:50:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 148.9 |
| ca734487-d837-373b-8cb2-db06eea9b3b8 | -5.68 | -39.259 | 2025-12-14 01:00:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 82.9 |
| b5da86f0-aceb-3435-b87e-e072bb2f2491 | -2.4768 | -45.4309 | 2025-12-14 01:00:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 190.1 |
| a3d4d8e2-159a-3f88-b5a7-7cf484cd8d91 | -2.8876 | -44.9439 | 2025-12-14 01:00:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 092085ee-07d7-3e3b-b466-1a3cbf2203d1 | -16.2383 | -58.8395 | 2025-12-14 01:00:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |


[Clique aqui para ver as próximas entradas](README4.md)
