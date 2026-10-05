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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffc29496-fa72-3f71-9e72-2f1c4845f9eb | -13.51711 | -61.12759 | 2026-10-05 04:42:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d61bb7b2-d9e7-35b5-b5e6-a951e6ebe967 | -13.5037 | -61.1244 | 2026-10-05 04:42:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42f697d9-5fa4-3024-95d7-ebf6578533ae | -16.67558 | -41.84715 | 2026-10-05 04:42:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 30ca5565-a15c-326f-aab8-d904eb7e4691 | -13.51166 | -61.12597 | 2026-10-05 04:42:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dca46c1b-c526-3f5d-bfab-a56869e157c4 | -13.50495 | -61.12441 | 2026-10-05 04:42:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32c1c7ff-6195-3a50-a1f7-d4a4bfebfc09 | -16.68006 | -41.84784 | 2026-10-05 04:42:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e40f023e-02b5-3e1a-a1d5-5309c86d0b9c | -7.4442 | -63.5589 | 2026-10-05 04:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 1e3533bd-0314-3c52-9c55-bc21fc7a6ed5 | 0.50307 | -60.60545 | 2026-10-05 04:55:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f413a421-6c6f-36cf-98da-608a83e63b12 | -1.0978 | -54.10449 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7723c841-b998-3a39-b571-d2d67832ce93 | -1.09407 | -54.19606 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c77ce201-2f5b-3865-a473-698a26059817 | 2.07668 | -50.89443 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 159da505-3182-3a29-8c2f-2146211f4477 | -1.05351 | -53.58894 | 2026-10-05 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc1f945d-71f3-3d96-b246-800d02c91812 | -0.36862 | -52.04071 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0419f68b-69e0-3b7b-895f-93449c3df049 | -0.39459 | -52.02746 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ec684067-6a75-3745-a9d7-e9337dc96090 | 3.1059 | -60.63243 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7acef664-db3b-3939-b37f-97f594685ed8 | 1.86976 | -55.80933 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 084d24aa-78d8-3704-b6c2-495c7a1b3cf2 | -1.09718 | -54.10841 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a29d928-61b3-3a04-bc1e-a43f5b6a07f5 | 1.85777 | -55.81121 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73dc93d7-acbc-3f6c-a513-25451906125f | 3.11003 | -60.56547 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2f60f91-208c-360c-882f-9afa90ae7b6b | -0.38963 | -52.0373 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2cb40ea-cb00-3b3b-88b1-b81db8f98515 | -1.13344 | -48.89082 | 2026-10-05 04:55:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e8632ef-7091-38fb-ae45-75cbbe60fed3 | -1.46216 | -53.59881 | 2026-10-05 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 442658d0-5572-33f5-925c-69fefa978472 | -0.40013 | -52.0354 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 67126260-c61c-3c26-b195-d198be5cdd1b | 1.72484 | -55.64962 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a586828-ab8a-363b-95c9-ac5b3a687b0e | -1.10276 | -54.14118 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5249196a-95ad-361b-a519-be8e33ea5cc2 | -1.08606 | -54.11065 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b193585d-faba-3019-ae66-8b83d07ca00f | 1.86922 | -55.80587 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2e21c1c-4a82-3016-a5f3-450231cfc430 | 0.44196 | -60.53441 | 2026-10-05 04:55:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad69c46f-802e-3e3e-b426-ecc5eba19f1e | -1.12991 | -48.89027 | 2026-10-05 04:55:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ae09b78-642f-34d6-832a-f40af5ee80a5 | -1.46157 | -53.60251 | 2026-10-05 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf2b8fae-bdca-34a7-8c9d-8d3fbb88aa8d | 1.89848 | -55.78362 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1109c309-289b-3c74-a921-1702ed130cce | -0.40289 | -52.03938 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4345f71f-9c7c-333e-8a48-39779405ff92 | 1.72957 | -55.65405 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 28156f0c-1908-333a-b103-dc9f49fb285b | 2.34989 | -50.75262 | 2026-10-05 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbe53ed4-2c4c-3307-96b7-a251bed933ea | 3.36092 | -51.34572 | 2026-10-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6908ca6-011b-3fb2-bc4e-2c9f44e4968e | -1.17141 | -49.25074 | 2026-10-05 04:55:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e0044b6-4703-38e4-b5b9-5f80feee3344 | -1.33508 | -54.22775 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b95a083e-e1a6-3684-90b4-6738842bc05b | 1.86576 | -55.80996 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dd9a4af1-6505-3c2c-ae89-483f38d88cb4 | -0.3924 | -52.04127 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e260456f-8ca4-301b-a2b6-c815db48d473 | -0.49147 | -49.10254 | 2026-10-05 04:55:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47dad9aa-1d92-391d-9f72-8fd35eb8a533 | 2.10394 | -50.74599 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 153aae4e-546a-3c5f-8e99-5f732aaf993a | 0.4425 | -60.53785 | 2026-10-05 04:55:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 89b10794-a417-3551-9768-b2a12c2a4a41 | 0.44303 | -60.54129 | 2026-10-05 04:55:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 270deb98-a5c3-3d08-9c78-70fbc761e193 | -1.10006 | -54.11288 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcc7c4b6-67a8-3fc3-8105-0add4dd9281b | -0.39514 | -52.02401 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9217969f-b217-3829-bbbd-84ea20eecbab | 2.39885 | -50.76253 | 2026-10-05 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fe563bf-a843-3866-b4b3-4d3c793fa27e | -1.19415 | -53.38793 | 2026-10-05 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fde5a0a1-e7b3-3c0d-bc72-a0a84580152d | 3.36037 | -51.34225 | 2026-10-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c35aabf5-697c-3b89-9c7b-967056ab32c5 | 2.3532 | -50.7521 | 2026-10-05 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7cbbb3c-f4bf-359d-a0d5-1a59ebc16d86 | -0.38901 | -52.01913 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2bb7a9cd-6ba6-3c39-a135-19514aa0888c | 1.86523 | -55.80649 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1133ef88-69e1-378e-ad51-bebeeda0582e | -1.10068 | -54.10896 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bef1ea1-2691-32c6-b83c-7094f390eb20 | -0.3802 | -52.03189 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2110f8e-9e7c-32db-ab87-10b1424b09c6 | -0.33601 | -52.03206 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2b5596a6-0a4c-3e78-9e5c-55f1380e3042 | 1.82574 | -55.5497 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c287b92a-66a7-369f-94c9-82a2bc79381d | 1.8519 | -55.82634 | 2026-10-05 04:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d04973e-84f2-3185-96f2-f7ebfbeec743 | 1.8764 | -55.77293 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe2713cc-5891-3eff-9a2a-6580c7f6741e | -1.32868 | -54.22266 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4735c07-7a60-35ca-9a0b-3cf35894d544 | 1.04081 | -50.02237 | 2026-10-05 04:55:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 577fa9ef-f7ca-30a8-9ac8-b0f86a8aa68e | 3.1046 | -60.60531 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cb3d73c-c250-380f-bc49-7f869596e9b5 | 1.73195 | -55.64331 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25845b35-ea12-36af-a2be-fdf0aa4360c6 | -0.38792 | -52.02604 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cfc0da26-8773-358d-8a18-e15fe302d14f | -0.39018 | -52.03385 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6daa38e3-9306-3107-8a58-8d7e41e00bec | 2.08826 | -50.88207 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a1285c7-6c00-3cf5-93ad-5eb5009813b9 | -1.10213 | -54.14511 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a7a486d-164e-3344-b785-b7c1b3759c74 | 3.102 | -60.6056 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 628bc714-c938-3499-b439-262d6bfebdaf | 2.0855 | -50.88602 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dde5dd1-409e-3b75-b4db-7dbc74b72944 | 1.72168 | -55.65533 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de57ac91-e169-346a-bcbc-53625b9e6096 | -1.31052 | -54.22378 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b32acb9-e029-3af0-9387-149de7e3137a | 1.72801 | -55.64394 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d578a316-4318-39eb-98d7-b8cb99896d27 | 3.10534 | -60.6286 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46c1969a-e150-31fb-9481-f6e812befad0 | -1.17488 | -49.25128 | 2026-10-05 04:55:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d18d862a-db11-31bf-8bef-512bc5da1d33 | 2.09156 | -50.88156 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56739b76-5f33-3843-9261-b3fdfb67b095 | 1.60615 | -55.79461 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca59d14f-eb80-329e-a1ed-3337cf3a6d13 | 2.00674 | -50.92632 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e91a97b4-a421-3362-9743-970c83212730 | -0.49495 | -49.10307 | 2026-10-05 04:55:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15a04c20-63be-30fc-9089-5b61dcf1a89c | 1.85484 | -55.81879 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2f4df9be-7611-3f53-aee4-77f6864ebd64 | 1.85884 | -55.81816 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0101d87f-56cd-3945-a9f3-320b8dd95660 | 1.75172 | -55.61453 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b2c88d5f-db31-38a5-ae05-05efb0219277 | 1.90301 | -55.78645 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d54f393-d8d5-3b99-bd30-bf9c26dde97b | -1.19755 | -53.38845 | 2026-10-05 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c40a8eb4-ffd9-3538-b1fd-bc118f681259 | -1.86988 | -50.60499 | 2026-10-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb26402e-a78a-3925-80e3-c7957fa67450 | -1.13282 | -48.89477 | 2026-10-05 04:55:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b765d0b5-7270-3ad2-90ea-4a55c8965fb4 | 3.10402 | -60.60148 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14b3caaa-7e13-31d4-8312-bc7f31ca85d8 | 3.10305 | -60.63295 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d2aa192-4bf5-3bc9-982f-a55d07c21227 | 2.0921 | -50.88498 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9911755c-fddd-3a0d-9e2c-31ec0f112491 | 2.01005 | -50.9258 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81bc6a31-14d0-38d3-95fa-9628c76ba6a9 | -1.45191 | -53.59712 | 2026-10-05 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 347a78f8-8708-369d-9758-a4d3ab1a00a7 | -1.97249 | -48.91502 | 2026-10-05 04:55:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebcff272-b827-3cbe-ac49-5b2298174c5e | -1.21669 | -54.53951 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7568c493-0852-3d0f-8884-9f315934804c | 3.10246 | -60.62911 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e8ea8a4-1a4c-38af-8119-2a0d4406a2df | 2.10448 | -50.74942 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7332e7f-4f7d-30b5-b9e1-f91ea35f7dd2 | -1.09944 | -54.11676 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85504433-0a9f-3118-a64c-5fab332a2cb5 | 3.10367 | -60.6171 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 132e00d6-f51a-33ba-81bd-b3091e7b424e | -1.21604 | -54.54355 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f11f0ecc-2f5b-3624-b23c-8040066afb28 | -1.09368 | -54.10787 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88caaffc-c333-3230-a0eb-b4a3c3c8d9db | 1.60415 | -55.7967 | 2026-10-05 04:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea983d5f-cb5c-350d-9a96-9e4ce624d49f | -1.0943 | -54.10396 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ee15254-e428-3501-82e5-c0782595fb54 | -2.10074 | -48.22747 | 2026-10-05 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4799425b-bacb-3a3d-a5c1-7e8442027b01 | 3.10144 | -60.60178 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README30.md)
