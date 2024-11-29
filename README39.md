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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1ce7090-d4c2-398d-bd6d-55140fd45d26 | -1.68416 | -53.81727 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b85e664c-33a4-3293-97a7-e61613e89b7e | -0.96281 | -51.65209 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3a1569b-dc47-3fc2-8dfc-527fcfb361f8 | -3.42188 | -53.88552 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11af21e8-5a86-32f5-841f-536742cd4fdb | -2.77098 | -54.06926 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b341f0cb-6b60-3558-b8ea-5242e0768ebe | -2.8373 | -54.12185 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86d4e134-1b51-3063-acb0-03c096736b8b | -3.03007 | -54.02127 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2788324-4471-3c30-808d-9c6f2c196d47 | -1.75297 | -52.76525 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54532506-9ed7-3133-9b6c-3cf175275aa8 | -2.8276 | -54.03215 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 919e7c52-98b1-3069-adbe-0aa2f6cf5399 | -2.96181 | -53.71864 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cb19700b-b315-39aa-9096-8a99b553ed39 | -5.37165 | -44.84501 | 2024-11-29 04:57:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f05a1df-0c24-3f61-ae67-cf9ced17f333 | -1.37911 | -53.63561 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46e6c8bc-b4e0-32b8-9165-4f1d515afee3 | -2.97861 | -53.28147 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 47caeaea-bc57-3a20-b728-31c1c0018026 | -3.97152 | -48.9172 | 2024-11-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b303626e-b2f0-3409-a4c4-2f20bbdc7a73 | -2.8591 | -46.83118 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1f2643f-1646-324f-a097-3695f421df0b | -3.11839 | -53.10519 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79f5cbbc-9450-3e4a-87c3-e5db3ebdc79e | -1.2886 | -51.74599 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63fbbf9b-f2be-3129-a62e-ca03eecc041a | -3.65105 | -51.41181 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbc2adb3-f3b2-3af7-9aa3-26b215941de4 | -2.77746 | -54.02795 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9427036e-0e33-32eb-969d-66a9c440bd31 | -2.60986 | -54.35886 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a0f0ff8-fbba-35ae-b0b6-8c1f84f9875a | -1.20666 | -53.71804 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4d9e8c08-b136-339a-ab6e-8f8e1bdf3b79 | -3.38661 | -51.40478 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b86ffeae-db25-3fcb-bddd-878487ff16bf | -3.15567 | -49.4316 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82e039dd-35c2-3891-a48b-5a281c1a94f8 | -3.05329 | -48.51581 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a96073b-5fa7-3a4a-9cb5-2460bebe3351 | -1.47337 | -52.66143 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37c77058-b55c-3421-b7ca-81119f28b57a | -1.1215 | -53.73945 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c6d2146-b858-3e82-a7ef-3e64a7ad4faf | -3.34462 | -50.52082 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8eb3fb79-c374-31c7-8437-1f6daa6bbedd | -3.02545 | -53.419 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 856f5597-4f34-3f84-92ce-167a36d0f446 | -3.13192 | -51.04109 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91d70616-a11d-3520-8fa4-149269ff31a7 | -2.56897 | -54.03377 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d3fe53d-bd47-31ee-9399-c94fe25fd4a9 | -2.0068 | -51.16277 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a2c8e6d-3c47-3ae9-aa58-8eb59104a4e4 | -1.9447 | -52.97501 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88a7baaa-a74a-3b79-babe-1abc2ee518d6 | -1.71212 | -52.76605 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 61752ac3-2496-3648-8952-9abd45d74947 | -1.43086 | -53.39068 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ba5fd4c-942f-3e88-aac6-d19feafb791c | -3.23605 | -54.09617 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33e570f5-e433-35a9-a960-2f5afc83ba09 | -3.77193 | -44.12216 | 2024-11-29 04:57:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 659d6707-efdf-382b-8b82-b3fb60c2187c | -1.06659 | -51.75231 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9964b8c2-9964-385b-85a6-6dc0edf6996a | -1.16788 | -53.37749 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc0f140c-eb7f-3391-867c-1bf8077b419c | -1.25757 | -54.54617 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b5e78eb-087d-346c-a799-8b15ca5ac391 | -1.24349 | -51.62485 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c95bc347-4bb0-31a0-bc0a-0742434b7809 | -1.71655 | -52.49665 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7564c1a2-0b62-37dc-a595-068294dc8355 | -3.69993 | -50.22406 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48db46d3-af80-3feb-bbcf-6c4250234a64 | -1.36995 | -52.12304 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be8c78a4-b54b-3798-8c5f-53b7b5659e23 | -2.25545 | -53.62205 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 615a20ad-ff12-3a90-9f5c-b24c1d182883 | -2.98232 | -53.89061 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afd926b1-0fb6-3ab7-bcf3-fdc9771865a7 | -2.83422 | -54.03317 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41bee0e0-5fd7-3ae3-bdac-04229e58f691 | -3.65613 | -54.17259 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6638f71c-3699-3c84-b465-b42db605dbab | -2.58757 | -51.92126 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6566767-c78e-3573-8963-1a3d280ce40a | -3.5473 | -52.02153 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2013dcf6-2140-370e-9052-746514537306 | -2.97753 | -53.28836 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| f99d358a-92e6-32d4-b839-ab987e62e113 | -2.4793 | -54.01985 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f0e2f8d-7e8c-3389-bb4d-6f99d102ea8b | -2.96766 | -53.94114 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fefcbdc3-7c58-390a-930b-97a2137b35f5 | -2.64444 | -54.02781 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61187fdd-0e8d-307e-b6d8-130d150298f0 | -1.37518 | -53.61742 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc650c65-478e-35b8-99e8-e37e51776cbd | -3.11015 | -53.81195 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3deab9f6-1b22-3652-aa60-70f9b291576a | -3.03784 | -54.03656 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a60f2b0-1bd0-3c42-adbd-fcfc1acc149e | -3.32985 | -54.14951 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05ed790a-9109-3176-a599-49970c18ee49 | 0.88795 | -50.95719 | 2024-11-29 04:57:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74b3fc30-4e68-3d84-a789-d7ecaa620bba | -1.08542 | -53.38222 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3833512c-ec9b-366a-a232-445128b0018d | -1.24131 | -51.79429 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ca444b80-8a50-360b-994f-e57f9c84cc14 | -3.22589 | -54.18276 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 16be1008-bf1c-31fe-a1db-3dbb5e9dd8c0 | -2.29302 | -51.98394 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b126a38b-f39e-3c79-83ab-d1d84120f1ce | -1.46433 | -54.50616 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6235dfe-51f6-32f6-ab51-d4a8382d8e68 | -2.8572 | -53.99443 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d56237be-eb8d-3e6d-ab71-0acbe7ec97d9 | -1.19398 | -53.71255 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df47de1b-b4e5-3783-8283-62114e1074e3 | -2.66672 | -48.78337 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 368113d1-80e4-31cd-9fd8-357e26b2873c | -2.72903 | -54.11852 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 942724ba-cba8-3901-bdb3-8f9113eb33d7 | -4.065 | -54.38555 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92164278-4dee-3e30-b756-b1f66410d666 | -2.86704 | -53.9748 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a21b4a0-3cb0-3350-ab00-facfc31b6096 | -1.10523 | -53.38526 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8b98ca9-f312-3a04-80f8-822816811083 | -2.8343 | -54.05433 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 027e20ef-0009-31af-8ff9-9e7391715ac1 | -3.04722 | -54.04153 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbf170a5-e92a-3986-b423-a5be36f27591 | -3.15374 | -49.42881 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cecd4c1d-ffc6-3bc1-b37a-076ccbf21e3e | -3.25355 | -53.63423 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 97c51772-dcde-3419-8406-5cc987e48ee1 | -1.66395 | -55.22948 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54466d35-88fc-3bed-902e-580b621cabda | -3.11357 | -53.98896 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4239315-7e55-39c5-bc6b-96135cfb69fe | -3.13689 | -51.63445 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca465681-65d6-3c85-b0b3-01b396fcb05a | -2.79838 | -53.0412 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1cea657-f945-3166-96b8-34fe257161e8 | -5.04289 | -43.62144 | 2024-11-29 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c07de915-2935-3187-abf3-9432b5dd7da6 | -3.22025 | -45.38516 | 2024-11-29 04:57:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ba6cdfd-25dc-3d50-ad69-45d8f836be5d | -1.7709 | -55.5303 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8603bf0a-ab0e-3444-93ff-ba10c9a70494 | -3.04812 | -48.52237 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69246b34-82a2-3b5a-91e7-9685f13c926b | -1.66616 | -52.73419 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f629be3-5d01-3ff1-8dbe-02bd941fd9b3 | -3.94497 | -46.69176 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b273632-bace-3d1d-b234-91ead58c86d7 | -2.58895 | -54.07928 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0dd60754-ea1e-3614-845f-abc72294fd56 | -4.84319 | -41.25526 | 2024-11-29 04:57:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8224d65e-0d66-3561-b6c0-0448b030f5ea | -2.80036 | -54.11969 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5ba3100-05d3-3fa3-9863-00c4fbd0c0f0 | -2.26472 | -53.47593 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a5ee5f7-fc47-3f13-96b8-0290ff83dfc9 | -1.60284 | -52.28892 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 849a800e-59a9-32ad-ad59-216b342b0574 | 0.93873 | -50.74137 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7208e919-5347-3204-abce-1e59eb75bd27 | -3.78603 | -46.69413 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b63ce33-2f0e-3d02-b29c-1d3c2426505a | -2.06177 | -51.18977 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9204f527-128c-3839-9380-002f13f7608f | -1.5336 | -52.66715 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f3d8fff5-05b2-33d0-857a-90f2c7877ba6 | -0.9979 | -51.78247 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41bbcaea-8596-3583-bcd7-35ce1d5a3758 | -2.24118 | -54.47629 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e07a3e1e-7b8c-3618-9c6f-d9302d5cc66b | -3.19196 | -54.48592 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7660d484-4cf4-317f-95a8-a04504c46909 | -1.62117 | -52.28098 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c20b1e0-7f6c-3e46-b750-5497e4b7f547 | -1.21202 | -51.7383 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d9ada69-b35e-3c1a-ad0b-27133d35654e | -3.88961 | -46.67847 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e2115bd-8b7b-323f-933b-8bc8db07519a | -0.77699 | -52.39363 | 2024-11-29 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f21e4801-1a7c-3705-b60a-4e9263abfa65 | -2.79961 | -54.05956 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README40.md)
