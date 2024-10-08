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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 844b6c4f-ef6a-3488-bcd0-cc0568a04b6e | -16.5902 | -46.4746 | 2024-10-08 11:56:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 7499f1ff-34a7-3459-81c6-3acf2d373fc4 | -16.571 | -46.4553 | 2024-10-08 11:56:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 243.9 |
| 503bc2d7-2598-3306-90fa-43c7c605ce46 | -16.7852 | -57.422 | 2024-10-08 11:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 02b95f79-5cb7-398a-96db-80e1c806ebf3 | -16.8048 | -57.4197 | 2024-10-08 11:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 161.1 |
| 9d4073de-e951-35d2-a107-a0cdd94b4be6 | -16.8244 | -57.4175 | 2024-10-08 11:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 37066c5b-a7b8-3ea1-9ce7-e161fe2df97d | -16.8051 | -57.3993 | 2024-10-08 11:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 2e425517-e659-3502-8800-f1dc87a7c894 | -17.1471 | -56.8256 | 2024-10-08 11:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| b7a2e94f-c125-310b-80a8-cbc41c92d27d | -17.0992 | -57.3651 | 2024-10-08 11:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 217.1 |
| 9b874d24-14c6-3d27-983f-275b980962df | -17.0989 | -57.3857 | 2024-10-08 11:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| e7dd7a56-5fbd-36b5-a656-a2edecfdbeab | -17.1178 | -57.4244 | 2024-10-08 11:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 714b453d-a48a-36ac-a0bf-fccb3eebc87d | -17.6692 | -53.0174 | 2024-10-08 11:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 4a00b797-6320-3099-94e8-8b765f1d328c | -18.5993 | -57.2629 | 2024-10-08 11:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| f1adb148-633d-3c7f-98a2-c64058b6197d | -20.3513 | -48.8648 | 2024-10-08 11:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 246.8 |
| e3cbeed9-0052-31ef-af96-04eeb6691738 | -13.88 | -44.61 | 2024-10-08 12:04:05 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f95c1f63-2dd7-3bec-b098-69da00c9fa6f | -13.88 | -44.56 | 2024-10-08 12:04:05 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 24fa63b5-350a-307c-8e11-e8f453c6984c | -13.8744 | -44.6329 | 2024-10-08 12:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| dae12612-8b6e-380f-9344-556718d98111 | -15.7068 | -59.4326 | 2024-10-08 12:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| feb3056f-b4fe-35cf-8fb9-819fbde5f71e | -16.4184 | -55.9455 | 2024-10-08 12:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 182.3 |
| 9e786ff2-c77b-30e1-b998-bdc6304b08e7 | -16.418 | -55.9662 | 2024-10-08 12:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| d065985f-8219-3f9e-b625-c892d252fba4 | -16.8244 | -57.4175 | 2024-10-08 12:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.9 |
| 8d00f707-5b46-38fc-b088-eb9346225361 | -16.8048 | -57.4197 | 2024-10-08 12:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 187.8 |
| 4c27dc2f-299d-3388-b9e4-aa5621ce290e | -16.8045 | -57.4402 | 2024-10-08 12:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 1f87f65b-17a1-345c-8234-844185b3db6b | -16.7852 | -57.422 | 2024-10-08 12:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 96f84b55-227d-3085-b802-aee2296f8cbe | -16.8051 | -57.3993 | 2024-10-08 12:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| d4a53e82-5a68-36f6-9cd8-18b45cad7a9e | -16.9407 | -57.4859 | 2024-10-08 12:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 708f250e-42ec-3dd0-9e6e-5ed8c57d6366 | -17.1471 | -56.8256 | 2024-10-08 12:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 4e536ef2-b122-357a-a900-a4dea0e64f4a | -17.1178 | -57.4244 | 2024-10-08 12:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 0075a389-f9cd-3b03-aefa-98f92cf98509 | -17.1474 | -56.805 | 2024-10-08 12:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 7110f2fd-9da7-3f28-9a59-eb6b548423fc | -17.1074 | -56.851 | 2024-10-08 12:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |
| f039a03d-1ed8-3632-968e-b9067c3bb586 | -17.1375 | -57.4221 | 2024-10-08 12:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 935d4acd-d7f5-3e2a-a24e-66dfbf554e07 | -17.1078 | -56.8304 | 2024-10-08 12:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 104cbd1f-2e0f-336c-b3b4-0651f6bba262 | -17.1274 | -56.828 | 2024-10-08 12:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| ddbceb8a-58d0-3ed0-a659-574ddad6c785 | -17.0992 | -57.3651 | 2024-10-08 12:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 179.4 |
| fcd0ea9f-cdab-309b-ab51-393e2b3c4348 | -17.6692 | -53.0174 | 2024-10-08 12:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 139.2 |
| de2ab796-56f2-398e-84d0-8d5e1aebb7f3 | -18.6192 | -57.2603 | 2024-10-08 12:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 0d59f875-0842-3654-88f5-312960dc2560 | -18.6195 | -57.2396 | 2024-10-08 12:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 0cc11ddc-6ddf-31cb-a9ca-2b7202be22d7 | -20.3736 | -48.791 | 2024-10-08 12:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 38b01b8b-20ff-3b79-8942-1066139f4039 | -20.4463 | -47.6405 | 2024-10-08 12:06:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 366e3ef3-8ae8-39ec-b078-1dad2514374a | -20.373 | -48.8141 | 2024-10-08 12:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 115.5 |
| e9283a2b-7294-356b-bf73-a113911e21ad | -20.3513 | -48.8648 | 2024-10-08 12:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 184.7 |
| a94c1e77-c9bb-3461-972d-5198ad08b9a4 | -20.3532 | -48.7955 | 2024-10-08 12:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 3fdf1d3c-5688-3c69-b248-57b0877e9b7e | -14.7186 | -45.1588 | 2024-10-08 12:16:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 247.1 |
| ae40692a-0846-3830-a275-df4d3d51a6d5 | -15.7068 | -59.4326 | 2024-10-08 12:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 825f8bd3-2d64-3b15-ac3d-42724e393305 | -16.5078 | -57.6979 | 2024-10-08 12:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |
| ec3163bc-a934-32a0-b43a-5e934bb473b5 | -16.418 | -55.9662 | 2024-10-08 12:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 744c6e07-9ff6-3d51-930e-04951a7ec728 | -16.4184 | -55.9455 | 2024-10-08 12:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 150.3 |
| ce5dd144-09b2-3f46-89b8-f43d50b1fe7f | -16.3956 | -57.3845 | 2024-10-08 12:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 3304fe23-598b-33ce-b8b3-076a2a09c759 | -16.8045 | -57.4402 | 2024-10-08 12:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 8bbf0f48-f4b4-326f-adfc-52ca51a85856 | -16.8048 | -57.4197 | 2024-10-08 12:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 182.8 |
| 26871e84-3a40-3828-9540-8b82a295b835 | -16.8244 | -57.4175 | 2024-10-08 12:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| c4f527bd-96f4-3874-b1df-f0dc54b6a8a2 | -16.7852 | -57.422 | 2024-10-08 12:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 7b9f113c-368a-3fb4-b595-eff41afe1937 | -16.8051 | -57.3993 | 2024-10-08 12:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| ac512eab-12cf-3211-ac58-0170e6726fe7 | -16.9407 | -57.4859 | 2024-10-08 12:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.0 |
| 1cd70fe2-af1f-3b2e-a469-c822d681f436 | -16.941 | -57.4654 | 2024-10-08 12:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 7967b7f2-0e8b-3c0d-928e-c018fd9af354 | -16.9937 | -56.6178 | 2024-10-08 12:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| f0f4fe2b-d7ee-37e4-bdda-b9cf5389f881 | -17.1078 | -56.8304 | 2024-10-08 12:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 932f67fb-e6f3-3184-8898-7fde59635342 | -17.1474 | -56.805 | 2024-10-08 12:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 84d950c5-aef9-351e-80c0-ee5821afe077 | -17.0989 | -57.3857 | 2024-10-08 12:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| fe83c2a0-5e86-3e19-a809-6997c914a04d | -17.1471 | -56.8256 | 2024-10-08 12:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 3fc4bd26-d83b-3f1a-b54e-5124ffb613e3 | -17.1175 | -57.4449 | 2024-10-08 12:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| a6d62471-ceaf-3a11-9e66-016753fca941 | -17.1375 | -57.4221 | 2024-10-08 12:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| b41acdc5-5c08-3953-8217-c795ef08b7d6 | -17.0881 | -56.8328 | 2024-10-08 12:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 126d8f96-6503-39f0-b1f2-24f643a4493e | -17.1274 | -56.828 | 2024-10-08 12:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| 919cc3bd-547a-3950-8144-e2cabcb6d736 | -17.1178 | -57.4244 | 2024-10-08 12:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.9 |
| dbdad3e9-1e4e-3c03-a82c-c3c7bce5649a | -17.1074 | -56.851 | 2024-10-08 12:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 0e9589d3-0d42-3bd9-9ec2-1604f2e63895 | -17.0992 | -57.3651 | 2024-10-08 12:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 210.8 |
| 2b74e0cd-95fd-3623-9bfb-f821f458e3fe | -17.1584 | -56.1429 | 2024-10-08 12:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 5b438e91-761e-3ec1-9bb1-3b4b411ac126 | -17.6692 | -53.0174 | 2024-10-08 12:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 2d4f2c6f-539a-3b89-bbf5-2680a9f70829 | -18.4931 | -53.4457 | 2024-10-08 12:16:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 6cc73f1e-76e0-3443-8e24-b93a421297ef | -18.6195 | -57.2396 | 2024-10-08 12:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 41247f54-8d20-37e2-9cb2-e7819d5f9994 | -18.7183 | -57.2682 | 2024-10-08 12:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 44ed14db-7940-3d2d-8598-3d884a95971e | -20.3513 | -48.8648 | 2024-10-08 12:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 219.7 |
| f9cc7374-3d10-3ce9-8f93-0769577bef1c | -20.3532 | -48.7955 | 2024-10-08 12:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 132.0 |
| f1b53229-d894-3920-a9e9-72087149553d | -21.9782 | -46.5507 | 2024-10-08 12:17:07 | GOES-16 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 162.6 |
| 25bdd8ca-ac99-3be4-8a07-166a3a48298f | -10.4032 | -49.4318 | 2024-10-08 12:26:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 44b973ec-3817-3a59-8833-e96da2693e4e | -13.8744 | -44.6329 | 2024-10-08 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| b42908f6-617c-3c3e-be57-c0275544fc10 | -13.8359 | -44.6162 | 2024-10-08 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 84ca391f-bb30-3cc0-9856-d6141b30982f | -14.7186 | -45.1588 | 2024-10-08 12:26:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| cfe93b1c-c385-35c7-8221-e9a27dcf2b11 | -15.7068 | -59.4326 | 2024-10-08 12:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| fc8819fb-59ea-33a5-9143-38104e4d78d6 | -16.3956 | -57.3845 | 2024-10-08 12:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 5750ec90-a931-3029-9080-8fcc48769a0f | -16.4184 | -55.9455 | 2024-10-08 12:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 201.4 |
| 7e89b747-8d5c-3d9f-a5c3-b4dc59723751 | -16.4729 | -53.9147 | 2024-10-08 12:26:39 | GOES-16 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 9311638d-2a77-3e3f-84c4-385a0a1dfaed | -16.488 | -57.7205 | 2024-10-08 12:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| b77212a6-46bc-3de9-9d96-f60129259b8e | -16.571 | -46.4553 | 2024-10-08 12:26:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 173.1 |
| cfd6df75-cf52-357b-994a-15bab889722d | -16.5512 | -46.4592 | 2024-10-08 12:26:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a7c61967-8794-3286-b838-b4da133d0f47 | -16.5902 | -46.4746 | 2024-10-08 12:26:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 29257f70-6388-3cb8-a918-35d6ba5abd1c | -16.418 | -55.9662 | 2024-10-08 12:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| e25b7429-47e8-307f-8565-96618d5470a7 | -16.5752 | -55.9055 | 2024-10-08 12:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 13bda382-d562-31be-9e5d-5b1fbf5af986 | -16.941 | -57.4654 | 2024-10-08 12:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| b49949a0-e4c7-339b-8cca-4f25a09b90bb | -16.9211 | -57.4881 | 2024-10-08 12:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 9fa6d247-b215-3126-98b3-5a9cde245121 | -17.0123 | -56.6773 | 2024-10-08 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| e01507cb-a6d3-3d81-93cf-00859fa6cdec | -16.9937 | -56.6178 | 2024-10-08 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 46a898da-2356-370e-a332-e41dfe3baf68 | -16.9407 | -57.4859 | 2024-10-08 12:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 3eb13550-3285-366d-966f-97f5467df9d2 | -17.1074 | -56.851 | 2024-10-08 12:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 1f25147d-5d46-39da-9c22-69c32c9ffef5 | -17.1274 | -56.828 | 2024-10-08 12:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| bcd99986-6bd7-318f-9288-739cbb65e21f | -17.0982 | -57.4267 | 2024-10-08 12:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 97e630ca-a8f8-37c9-a341-4255cb560a02 | -17.1584 | -56.1429 | 2024-10-08 12:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |
| e4f17c86-8f2d-3e16-a929-5d7701990825 | -17.0992 | -57.3651 | 2024-10-08 12:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 286.2 |
| 11876da0-7433-3f7e-967d-96beee751a5b | -17.0881 | -56.8328 | 2024-10-08 12:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 5e8f0317-dbba-3428-88cf-8600bb993416 | -17.1375 | -57.4221 | 2024-10-08 12:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |


[Clique aqui para ver as próximas entradas](README137.md)
