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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02772a8e-9a21-3805-a2a6-86f30f4dddb7 | -12.7355 | -44.546 | 2026-07-04 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 524f06bf-cab9-393f-94b5-1fddf493e51e | -12.7359 | -44.5225 | 2026-07-04 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| f5948242-4c01-3b3c-b139-ee05661cf812 | -13.2592 | -54.3489 | 2026-07-04 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 144.3 |
| c0d851e9-c471-35c6-ac68-1f512453787b | -10.9397 | -43.0593 | 2026-07-04 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 9ae2958a-77c9-33c7-a0c6-f3d9e8e7619e | -12.7553 | -44.5194 | 2026-07-04 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 178.3 |
| ee428695-3562-324b-89af-108c95584222 | -10.9401 | -43.0355 | 2026-07-04 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 6e6af524-c6f8-32b1-80cf-3809df705bbc | -13.2401 | -54.351 | 2026-07-04 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 193.1 |
| 2fb51307-6535-3e31-9082-a469895469c0 | -12.7741 | -44.5396 | 2026-07-04 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| e01392e8-ca1c-37fc-9dcc-71a421a509b5 | -12.7548 | -44.5428 | 2026-07-04 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 258.2 |
| aa456403-e822-34fc-9cec-20ec69578bc7 | -13.2404 | -54.3303 | 2026-07-04 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 147.7 |
| e29f7387-a7f8-3f1d-be83-867326376c6f | -12.7746 | -44.5162 | 2026-07-04 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 0811a6b1-eeed-3771-9cbb-8f332368c62b | -4.3402 | -47.7645 | 2026-07-04 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 02c37b18-e4da-3f77-a8f9-e42b69729ea3 | -13.2595 | -54.3283 | 2026-07-04 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 10a3bdaa-b287-3f7d-b258-90f85c7e625f | -10.9205 | -43.0622 | 2026-07-04 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| d5a5cbe1-1608-305c-aa43-4535a60a7e5d | -10.9397 | -43.0593 | 2026-07-04 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| c3faf6ca-dd81-3fed-8fef-a463c96b006d | -13.2592 | -54.3489 | 2026-07-04 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 207.6 |
| b59af15d-0c8a-369b-a13d-c2ad7bbdae4e | -10.9205 | -43.0622 | 2026-07-04 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 63187d3e-444a-3dd4-b2e3-45112b029060 | -13.2404 | -54.3303 | 2026-07-04 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 134.4 |
| dd345748-b9a8-32aa-88a5-b724c67904ab | -4.3588 | -47.7636 | 2026-07-04 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| f1a673cb-6dbe-33d9-8c5b-e2b7e1965c4f | -12.7359 | -44.5225 | 2026-07-04 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| aac77e5b-e96d-3581-b919-d9021569396d | -12.7553 | -44.5194 | 2026-07-04 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 204.5 |
| b3591eae-52cc-386f-8ec4-32e8b9eaff05 | -13.2401 | -54.351 | 2026-07-04 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 151.9 |
| ab5dafa6-70c1-35ae-b4af-6489220e2333 | -4.3402 | -47.7645 | 2026-07-04 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 31618166-2c93-3f53-bee0-45cd55f5c5cd | -10.9209 | -43.0384 | 2026-07-04 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 199.3 |
| 384d6bb8-6098-3fd0-9928-b2cb6b3c0c50 | -12.7544 | -44.5662 | 2026-07-04 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 3ecfc132-395d-3a21-8e6e-81ad2e1a608f | -12.7746 | -44.5162 | 2026-07-04 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| ee0ae743-a2f5-31ae-bba8-4ebdf788ee8e | -12.7548 | -44.5428 | 2026-07-04 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 322.6 |
| 03c5423b-9feb-367b-90ae-f908aee37593 | -12.7741 | -44.5396 | 2026-07-04 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 43ffc3f2-d2a2-3bec-9388-ac00c7fc1965 | -10.9401 | -43.0355 | 2026-07-04 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| d84d1771-85a5-3275-b6fd-374ec1cd05ad | -13.2595 | -54.3283 | 2026-07-04 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 161.5 |
| e3b0e66f-2dfe-3642-904d-5f2cab180a00 | -10.9401 | -43.0355 | 2026-07-04 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 7ec46561-5486-3ff9-9319-213e3fb61039 | -10.9209 | -43.0384 | 2026-07-04 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 35ec8a80-f4c5-3576-a32a-05e86b6bffcf | -13.2401 | -54.351 | 2026-07-04 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 164.4 |
| f8c1cf6a-a4a3-3a4d-90da-9c1ed3b796a4 | -13.2404 | -54.3303 | 2026-07-04 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| babb0016-1898-3042-9d21-f0562c7b1049 | -10.9205 | -43.0622 | 2026-07-04 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| eaa167a2-af4a-3158-9ee8-2719ff57a64c | -10.9397 | -43.0593 | 2026-07-04 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 1a313b3b-2969-361b-8d71-4870b20afd7d | -4.3402 | -47.7645 | 2026-07-04 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| dc792e18-c6a3-354d-96ee-e1ad723f1d25 | -13.2592 | -54.3489 | 2026-07-04 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 0e4b4171-7ad5-39ce-bdd1-cc1f44a249ef | -13.2595 | -54.3283 | 2026-07-04 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 34592865-0866-354f-b957-f7c5d69be355 | -6.8624 | -38.34906 | 2026-07-04 03:04:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7e562971-202f-315d-be95-1967f36bd8b8 | -9.44209 | -40.33301 | 2026-07-04 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3c458883-1515-3d18-bebd-202682b053da | -13.2592 | -54.3489 | 2026-07-04 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 176.6 |
| 9c54ba8b-2a12-3f69-b27f-13225f48b732 | -12.7548 | -44.5428 | 2026-07-04 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 267.0 |
| ad35e382-e0d5-3a38-b1a8-826b303c8846 | -13.2398 | -54.3716 | 2026-07-04 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| cf6339fe-5a02-38ca-a088-e2a63a0f4544 | -12.7544 | -44.5662 | 2026-07-04 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| baf03bb8-867c-30c2-9059-a23076a27ae2 | -12.7359 | -44.5225 | 2026-07-04 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 5c7dfe11-89fc-300f-ba3e-366dd9f1b7f0 | -10.9397 | -43.0593 | 2026-07-04 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 477f7657-69c6-3771-8c91-e195693d17e7 | -10.9205 | -43.0622 | 2026-07-04 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 758182db-dd59-38fd-b20e-131ee3e1a822 | -13.2404 | -54.3303 | 2026-07-04 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 155.9 |
| 34dbca13-b0f6-391a-9a45-bbad96dbc38b | -12.7741 | -44.5396 | 2026-07-04 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 7bf81eb1-791f-3710-b6ae-4e80611f0277 | -12.7553 | -44.5194 | 2026-07-04 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| d752f3ee-cd58-375d-a920-b7e64d1a0520 | -12.7355 | -44.546 | 2026-07-04 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 160cc908-fc52-3a77-a6db-48a71f40396a | -10.9401 | -43.0355 | 2026-07-04 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 47d72bdd-619a-31ab-b910-ee4e16e785e4 | -10.9209 | -43.0384 | 2026-07-04 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 182.1 |
| d4381945-f385-3a81-bd9a-17067c6fd2cd | -13.2595 | -54.3283 | 2026-07-04 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 1ad2d7fd-263b-361a-b441-96c3bf77e364 | -13.2401 | -54.351 | 2026-07-04 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 237.6 |
| 5dcba86a-bc43-3b2a-9451-398272241ef4 | -12.7355 | -44.546 | 2026-07-04 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 64ff98ce-73cc-3bd7-970f-cc1fbd6faceb | -12.7741 | -44.5396 | 2026-07-04 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| cde34854-923b-3df4-aadf-3eca3c35156d | -10.9205 | -43.0622 | 2026-07-04 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 11dba77f-facf-3fd7-97e6-8d31e49a1411 | -10.9401 | -43.0355 | 2026-07-04 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 2ee8fe91-ff16-34f3-8ec6-9ae2dddd4c9f | -12.7359 | -44.5225 | 2026-07-04 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 7c56c7cd-44d4-3658-93ef-bac30a62c0a2 | -12.7548 | -44.5428 | 2026-07-04 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 270.1 |
| 9104e669-28e6-354b-909f-414569850f7f | -13.2404 | -54.3303 | 2026-07-04 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 154.2 |
| c1b25f40-29ef-3639-9bda-1386ecb19131 | -10.9397 | -43.0593 | 2026-07-04 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| cfa1c987-47f7-3db4-9117-e192561c508e | -13.2595 | -54.3283 | 2026-07-04 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| e6e4ec69-a1cd-3713-b2b3-5642d2e019f8 | -13.2401 | -54.351 | 2026-07-04 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 257.5 |
| e4c00de4-1958-376f-abea-eff94847916c | -10.9209 | -43.0384 | 2026-07-04 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 194.3 |
| d3459d61-9553-3078-88aa-052063e620d4 | -13.2592 | -54.3489 | 2026-07-04 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 215.3 |
| 74314b54-81e1-35c6-9185-61b15086b1ef | -12.7553 | -44.5194 | 2026-07-04 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| c94fb4f3-2a61-3609-9380-3576f50f1c91 | -10.9205 | -43.0622 | 2026-07-04 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| bc020e5f-b037-3557-8cd2-245272ad567a | -13.2401 | -54.351 | 2026-07-04 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 180.4 |
| c201437f-4311-3280-b81a-b67e0fbfdced | -13.2595 | -54.3283 | 2026-07-04 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 1cde46c1-713b-3735-8df2-0c84bfcc4059 | -12.7553 | -44.5194 | 2026-07-04 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 54ffa63e-29a3-346f-a9b8-cfc3f1d3b96e | -12.7741 | -44.5396 | 2026-07-04 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 3cf082f5-4d1f-3f86-882b-cc48609e516c | -12.7548 | -44.5428 | 2026-07-04 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 284.3 |
| b762b17a-1c52-3ea2-b6ec-27c73428c6f7 | -10.9209 | -43.0384 | 2026-07-04 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 354aabbb-6b02-35b3-a74d-93c6a16cbe5a | -13.2592 | -54.3489 | 2026-07-04 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 176.2 |
| b2672bcb-86b9-3740-a83f-169a84438146 | -10.9397 | -43.0593 | 2026-07-04 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| b55b4bed-a3e6-3d55-96fd-0db7799e6759 | -10.9401 | -43.0355 | 2026-07-04 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 548d0c9c-077b-3692-80ef-49a2bfaf1adc | -13.2404 | -54.3303 | 2026-07-04 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 3241d87e-200f-3ab0-8c8d-1f8cfa7a1f83 | -13.2592 | -54.3489 | 2026-07-04 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 0d663a8b-c734-3732-b688-f5fee3e0d5eb | -10.9401 | -43.0355 | 2026-07-04 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 8d11a000-0824-3129-a652-77da6f91e457 | -13.2595 | -54.3283 | 2026-07-04 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a4ea0dea-bff7-3bcf-a532-4dad16bbf3d3 | -10.9209 | -43.0384 | 2026-07-04 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 0e72a949-4464-3abe-8d17-e1e72194e234 | -12.7741 | -44.5396 | 2026-07-04 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| a9a353ad-a062-3c28-a9a9-e513dd7d56db | -10.9205 | -43.0622 | 2026-07-04 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 1b1319de-e60e-32ea-89cb-e42cda945e14 | -13.2404 | -54.3303 | 2026-07-04 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| b4e14eb1-2660-33a9-b4c7-c03d508ff699 | -12.7553 | -44.5194 | 2026-07-04 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 46750202-f592-3831-a773-53bde07ba6e2 | -13.2401 | -54.351 | 2026-07-04 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 256a6eb9-b110-334f-a499-b2ecd63cc669 | -10.9397 | -43.0593 | 2026-07-04 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 856e8b90-af15-33ef-9fb6-a8bca29e5ef1 | -12.7548 | -44.5428 | 2026-07-04 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 302.5 |
| 827a2925-2e18-3a83-843e-0126f1ef8d37 | -5.79684 | -43.64284 | 2026-07-04 03:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 197b663c-a810-3ce7-a564-692609f66a60 | -6.42329 | -43.72371 | 2026-07-04 03:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 800fbdce-9cef-3dfa-9a9e-9e2bb7d6ab3f | -6.93461 | -43.71815 | 2026-07-04 03:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 650afef5-1940-36c4-bcbe-cf4d0b61e7c6 | -7.00793 | -42.77983 | 2026-07-04 03:40:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e9dfab15-6705-38a5-b036-c39cd19ebff6 | -7.00251 | -42.77271 | 2026-07-04 03:40:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b5f86863-2fb4-3fcf-bbcc-c871c8665f42 | -5.79061 | -43.64167 | 2026-07-04 03:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 203ca7d1-4689-32e4-b948-901c287bf245 | -7.00361 | -42.77047 | 2026-07-04 03:40:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cabb8c41-8e22-3d9e-9f5f-e0e7556e9dd5 | -7.00677 | -42.78204 | 2026-07-04 03:40:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 402c7dfa-6559-3ab4-931e-c312f1b8ab96 | -7.73633 | -44.17197 | 2026-07-04 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README6.md)
