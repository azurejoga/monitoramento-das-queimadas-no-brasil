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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec6da8ff-cd9f-37bb-9b3a-293b4eda3d86 | -3.19684 | -50.56225 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7755d15d-2438-340b-a6b4-c538082c1755 | -2.55934 | -48.94522 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8b7180e-c019-3c47-b490-dcfdb8c815ca | -3.16781 | -48.61435 | 2026-10-08 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c6c363c-90a4-3100-acfc-43b8ce8a8126 | -3.27579 | -50.40246 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77cc2e96-8563-36a2-bdf6-0249a271ebd7 | 2.32707 | -50.87627 | 2026-10-08 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48e53eb5-a0e6-35e9-8321-11654fed355f | -3.05218 | -51.22333 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| be86fc70-ca34-35a4-8e56-44994dccc469 | -2.56589 | -50.67731 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4afad417-6c39-3d8a-aafd-2b6bc6744973 | -2.03508 | -55.63257 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c38f410e-6aae-342a-b8e1-0a9770fe27da | -2.86154 | -49.63256 | 2026-10-08 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 532e5ecb-3919-3186-8f9a-8bf0b965149f | -2.87901 | -49.56408 | 2026-10-08 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d13e6e0-da67-35fc-9b94-e6f94ebb5507 | -3.24139 | -46.96373 | 2026-10-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 10bd2c06-1058-3c02-8f44-a49eb480b2b6 | -2.10284 | -52.06388 | 2026-10-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90370dff-9a97-3953-8543-367684db3ab1 | -1.29523 | -54.55619 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b0a2000-f500-39cf-9b8c-21996698292e | -2.15449 | -51.97859 | 2026-10-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15debdf6-c8e5-38ae-8ffc-7999d14aa430 | -3.19024 | -50.56123 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d3ff764-aa70-31d7-96c0-888b4838361e | -1.39994 | -48.92303 | 2026-10-08 04:44:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ff4c024-d713-3bfd-bd39-42497ed121d7 | -3.19621 | -50.54461 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81916b8a-2538-3123-8120-3eecad9009aa | 4.42998 | -60.93254 | 2026-10-08 04:44:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 485d72eb-d45e-3ccb-9c76-2471bc67a86e | -3.1736 | -50.44624 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0494b52c-0a28-322d-aa60-eb60b8714f6e | -3.2012 | -50.5559 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fd7f5b47-4dec-3246-bcdb-d0e731fab78d | -3.20343 | -50.56327 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7bef78d8-123a-3e32-84b7-5c0009beae51 | 1.68974 | -55.64526 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2a40e56-92ee-3b21-b7de-ed2dfafe8bab | -1.83257 | -55.04592 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39e7ebda-3c62-360a-98c4-8868e9da7f08 | 0.44305 | -60.53531 | 2026-10-08 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69a35162-865c-35be-a3fb-4eacbfc60364 | -3.19185 | -50.55095 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12e8e56a-d340-3975-a47b-7011d6151c2c | -1.60125 | -55.15838 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 667a07f0-df39-376b-b384-75d91252ceea | -3.18855 | -50.55045 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f1ae246-0c64-3358-9c7a-30c38c69eabb | -1.5238 | -54.81586 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0b738a7b-3f94-304a-9f97-c27a07f9388d | -3.26483 | -50.40779 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff4c9aa7-db42-33dd-88be-0356ecf9fbdf | -1.82971 | -54.9952 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6b0375bf-3b32-3886-a277-83414974a74e | -3.2923 | -49.50992 | 2026-10-08 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2e3b74c-519b-3ce3-9983-0faf3a023ea6 | -2.83326 | -48.57204 | 2026-10-08 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99646dfd-d008-3625-ab77-407378e23202 | -3.27249 | -50.40195 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c50fdf7b-16c4-3310-a86a-25088bac6080 | 1.69896 | -55.61807 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fb664a3-4776-36d2-a51c-e9ef48125f5b | 0.9473 | -50.20427 | 2026-10-08 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1edcc04a-7996-3b60-8d19-ddc9ae430af4 | -1.52408 | -54.81304 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f43b4bc-ccac-3a7a-8bd6-8e30af51c94b | -3.18419 | -50.55679 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 402237cd-533d-3d01-b4e7-68af4240dc0a | -0.16482 | -50.40675 | 2026-10-08 04:44:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fef57811-8a5e-3b09-a2ba-49741381fea4 | 2.12191 | -50.82317 | 2026-10-08 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 520daa36-6c82-328d-b20d-3c532ee8c1bd | -1.05785 | -53.59172 | 2026-10-08 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ff13a57-f375-3c21-9a08-479be3e82efb | 2.00024 | -55.87415 | 2026-10-08 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc1cecc5-1ec3-3a0d-9d27-d9a9a7cb34d1 | -2.96079 | -51.04581 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1941b6fc-6283-3199-8214-34b80729d2dd | -3.18365 | -50.56021 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c85451f-8ec8-3f83-81ab-2ffbbb6d1093 | -1.40164 | -48.93412 | 2026-10-08 04:44:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01553920-de64-314e-a615-1d9cf4bdf670 | -3.16984 | -50.60006 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d01eb4fa-8241-3310-a2f8-1f69e77f6baa | -3.16325 | -50.59904 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 92056081-1d71-3846-a947-59be722a1640 | -3.20726 | -50.56035 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 991b00d4-cd1e-36dd-8579-611bbc4d4d67 | 1.03788 | -50.0212 | 2026-10-08 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acb538b9-9c5a-3702-838a-2b79ed43fb69 | -2.56205 | -50.68023 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed0e6d99-cd94-339e-b19c-f1af722f3d03 | -1.68821 | -47.57385 | 2026-10-08 04:44:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b959304c-eca8-32aa-bee7-c7fb508c369d | 1.70638 | -55.60838 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f9b040b-0aa9-3339-a387-56a66c3a001a | -1.11649 | -54.09114 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3fc9278-a041-30fe-bc65-29e9d085dfac | -0.95354 | -52.33469 | 2026-10-08 04:44:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8835ed5e-805f-3252-a763-ecdc6b777115 | -3.20833 | -50.55349 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1cd4e23c-c698-3618-9585-ec4c17a8ab05 | -1.10464 | -54.1652 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 069a6fce-5bf8-3807-9af5-087fb677d540 | 3.85527 | -61.32313 | 2026-10-08 04:44:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fac2f955-a1a1-366b-96d3-7deeab989545 | -3.27915 | -50.03373 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4f6843e-27e3-364d-aea2-5a1394a062d3 | -2.23675 | -51.92794 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a9c9fe8-bd3c-30df-bdcd-d3777b1d0173 | -1.51043 | -54.82405 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c00991df-eb3a-30e2-8f56-cf89f766071a | 1.65895 | -55.79811 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc6bc026-0e45-37c0-85f0-c8e346c13bcd | -2.98485 | -51.24135 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05f36a84-83ed-3adb-a445-0ae4bb92c189 | -1.72257 | -55.44385 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 06580b13-0939-3dd2-8004-1deb392bee7f | -3.29658 | -49.12712 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 644d8c0f-bb74-30c9-bf3d-5d4b03743e36 | -3.4207 | -48.33543 | 2026-10-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34a89845-b68b-37f3-b83d-1efb25c69bb7 | -1.19435 | -54.13888 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3d0d07e-4511-389c-9114-551d481dc857 | -3.09632 | -51.37611 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b7811c8-a148-374c-9d35-1ae8fb516b44 | 0.44698 | -60.54192 | 2026-10-08 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61b93d08-eba2-3030-b85b-04310c64a473 | 2.43808 | -50.82265 | 2026-10-08 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81f0c7c0-fe97-3ab4-a64a-a157216411fc | -1.77103 | -55.03236 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c1e35a0-36ec-304d-86f8-28eafe166e4b | -3.18472 | -50.55336 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd408812-1ef7-3f22-bf5d-56f74fb95148 | -3.18962 | -50.54359 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26faecd2-37c8-3497-9b62-438054c2f4f4 | -3.12564 | -51.14621 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fc82570-9b25-3372-8f91-fdb8a981d8dc | -1.52573 | -54.54781 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ceab9b1-072c-35d6-8d82-9e031f70437f | -3.20227 | -50.54905 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f01d4296-8eab-331e-949e-0b2f848428aa | -1.4524 | -55.24995 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89ef95f1-d868-3327-b4b1-3b426ff19b52 | -3.261 | -50.41071 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 169947ec-2b1e-332c-8906-cd478de96a42 | -3.26813 | -50.4083 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 243698fe-f182-352a-b645-d14f29b44dca | -3.27745 | -50.02288 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf66aee1-d189-3ff2-9953-f0547a612bd2 | -3.15867 | -48.58274 | 2026-10-08 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c7944fd-718b-34e9-98eb-b9e63a095ac6 | -2.50041 | -48.13755 | 2026-10-08 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a353260-5127-39cf-9dfa-b824b7aaa046 | -2.21783 | -53.70086 | 2026-10-08 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1a6b16ac-0f64-31a0-a0c5-6596123cd3f7 | -1.50017 | -54.83812 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 190412de-22e9-3e30-8eba-05131afe8d68 | -3.18089 | -50.55628 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78994e41-e5e3-3de8-b7e2-0348eb543db3 | -2.78946 | -51.68037 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bce767a6-82ff-3c49-80d7-b8fa8513f865 | -3.18204 | -50.5705 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2254fb93-830a-3333-a842-377618f96ec8 | -3.21163 | -50.554 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b208e337-4014-37f6-a80e-f23ac6c22819 | -2.09944 | -52.06337 | 2026-10-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 447be0eb-0eeb-33a8-b2ab-6f6d2c41c5b4 | 1.32853 | -50.90136 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71dad37f-d525-39ba-b8d9-18a14e190533 | -1.28456 | -55.41641 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c6bae45-383d-3733-9e34-626e107cca54 | 1.74362 | -55.59005 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d95224b-0168-3d31-8c77-7c11d1eec291 | -3.19193 | -50.57202 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f51c02bd-ce03-396b-b528-5b07945908e1 | -1.11403 | -47.73441 | 2026-10-08 04:44:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 542c9964-ae1e-34f5-82fb-81253bce90cf | -3.20174 | -50.55248 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dd00193a-be54-3ae8-871e-56afc62ed181 | -3.13744 | -51.02786 | 2026-10-08 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bbc505c-4918-3bb7-a1d8-1d906a9cb7ef | -2.78667 | -51.67632 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30a56ac2-b4da-306d-a4f8-a5f2a030ec64 | -3.16701 | -50.44522 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95710833-9ffd-3184-8bdd-e5a53f9e3833 | -1.49733 | -55.65938 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca9deb08-e53f-3ae9-8a20-86bb22e7190d | -3.20013 | -50.56276 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 84a853b8-45d7-3f69-a604-2a7343f1ce43 | -3.23837 | -46.9588 | 2026-10-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 810ddf62-d791-39a3-86dc-44ee41013d8a | -3.19514 | -50.55146 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README78.md)
