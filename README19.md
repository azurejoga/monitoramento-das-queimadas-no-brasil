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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57548e35-8dd3-3264-91c8-92b7b710d1af | -13.52094 | -48.11486 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d21c4c5-659b-352d-8772-810d4ed4b273 | -16.05359 | -48.0799 | 2025-10-10 03:42:00 | NPP-375D | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c4ff938-203e-36b7-97d8-238cfacd36de | -17.9903 | -44.96037 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b88e7742-67cb-3d7a-92d7-ec5b2982ed9c | -13.84155 | -45.82602 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8d84d31-fd44-3804-a1f0-4c066c73695f | -15.08832 | -46.61219 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a988ac4-0457-35df-8120-f498e0ee8212 | -17.94168 | -45.01974 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b7db043-728d-3e08-aedd-f294d05a9b9d | -13.32402 | -47.74671 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58fc8b80-0dfe-3e1f-a0b7-add618469f9d | -13.83669 | -45.88038 | 2025-10-10 03:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f9b97e9-8dc7-36ba-823d-bc482b1d884c | -13.35367 | -47.60384 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41283df9-2343-3a2e-ab7b-ce84ba96198b | -15.73698 | -43.95058 | 2025-10-10 03:42:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1706b30-e41a-3fe8-893f-5512b6fde0e2 | -15.09008 | -46.60357 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09cf45f1-2400-3e4a-9c0a-e525161025a2 | -17.2119 | -47.6567 | 2025-10-10 03:42:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 25d0f5c2-3540-316a-9149-247f38931a62 | -15.23717 | -46.38175 | 2025-10-10 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abe47d9c-8e33-3049-9664-bc4c02cf288e | -15.2383 | -46.37643 | 2025-10-10 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e394aba-f493-3434-a15c-619a745d1936 | -13.84483 | -45.8394 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 9afa35fc-8450-3221-86ce-1bde9d717809 | -14.26301 | -45.87164 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a45904d3-80a5-349d-a5db-5a3453747ef8 | -15.32869 | -43.19181 | 2025-10-10 03:42:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1d6a907e-7f88-323c-b58f-d48afa1a3ec3 | -15.46444 | -48.53238 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b26c610c-fb13-3671-b2b2-b40e3e497cd8 | -13.84248 | -45.85337 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 4263a9d8-9293-3c09-8417-05eb083dfc6e | -14.27196 | -45.88601 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9789221e-ceb2-368e-8358-27cdb4eac8f9 | -15.09489 | -46.60991 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e650187b-2804-361e-b72a-3b167830808a | -14.92763 | -46.78117 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 681aa043-313b-3eef-95a3-0fd06dc62bf3 | -13.28208 | -48.01369 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e24f4370-4ba3-3925-a06b-7aba0ce04f2e | -14.27252 | -45.88778 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4be9320b-8f1b-3321-8f9f-948fd4aded10 | -16.0524 | -48.08541 | 2025-10-10 03:42:00 | NPP-375D | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b33965e7-8cb0-3b14-a067-fd6bf2ade104 | -16.17257 | -42.86357 | 2025-10-10 03:42:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9673bab5-5ff4-3ad6-bec6-acacf93b6279 | -18.64297 | -43.93516 | 2025-10-10 03:42:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7147f253-5a5b-3bf8-9ce4-0382b2c23ad3 | -15.43026 | -47.98738 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50cdb542-9152-3b14-84f1-67638feabc2b | -13.84015 | -45.83582 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e97fff1a-f5ac-3595-bf17-0c5420d9f069 | -14.38037 | -46.00377 | 2025-10-10 03:42:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cd50ec7-d280-35f8-bdf1-06d7e8b2532d | -16.26533 | -47.1592 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc93c26b-378b-3c26-9b19-2e7a911a78cf | -15.09424 | -46.58328 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a78c855b-f2fc-323f-85c6-48d9e559d378 | -14.9329 | -46.76811 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 80f61a8b-1e87-3d56-8796-04c91d996949 | -21.71945 | -52.42291 | 2025-10-10 03:45:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b20c4a61-6ccd-39d7-ab79-4e8ffd2f31c9 | -20.22782 | -46.43205 | 2025-10-10 03:45:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5763ded7-7696-311b-b6b7-79c3521ff8eb | -20.23443 | -46.42691 | 2025-10-10 03:45:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94515937-57e5-3bc0-bace-9a1ea9af2fa8 | -20.22467 | -46.42125 | 2025-10-10 03:45:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24b39b8d-adbc-3a1d-ba63-7e1f2cc345ff | -20.22399 | -46.42442 | 2025-10-10 03:45:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd98115f-a940-318d-af5e-5638158cddee | -21.72421 | -52.42499 | 2025-10-10 03:45:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec9afb0f-da34-3f87-aa9d-a6cbd5c90649 | -20.23375 | -46.43006 | 2025-10-10 03:45:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea6fd174-7d81-3225-b25f-661800bed794 | -21.72657 | -52.42473 | 2025-10-10 03:45:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f65ecb29-6baf-3caf-84dc-0697f7108471 | -20.2285 | -46.42891 | 2025-10-10 03:45:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51484b92-eed3-3879-8d69-edf5550eb477 | -10.1707 | -44.5959 | 2025-10-10 03:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 78fc148e-b87e-3ebf-8120-6fb6f289427c | -12.629 | -45.0749 | 2025-10-10 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 6dcd1b35-27cf-3706-91b3-5d99729b8057 | -17.9376 | -45.0148 | 2025-10-10 03:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 126.1 |
| d3b9e954-e88e-379b-8e85-32c6a3e6d0e4 | -4.8595 | -42.7688 | 2025-10-10 03:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 066431be-fa49-380f-849f-96cd086175a5 | -12.6294 | -45.0517 | 2025-10-10 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 416b8ac3-5be3-35eb-b260-1aade60f536e | -7.5428 | -44.6156 | 2025-10-10 03:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 3d489b3d-161e-34ec-be60-9052df5c4560 | -4.8408 | -42.77 | 2025-10-10 03:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| ed8c70d9-1cd1-3050-8a03-81a5b9cf4689 | -14.8869 | -48.2362 | 2025-10-10 03:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 3242bd51-c3f5-30b4-9042-7e1943a109a1 | -17.9175 | -45.0194 | 2025-10-10 03:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 45763362-280e-3314-ba5c-1493722e6bef | -14.2744 | -45.911 | 2025-10-10 03:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f0e0327c-551d-31b3-9f83-bb3f3a8cd3e4 | -4.5515 | -46.6801 | 2025-10-10 03:50:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 0303f09a-418e-3ce8-b7e1-5234922856b4 | -3.43731 | -44.91803 | 2025-10-10 03:57:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| edca152e-2862-3600-ad77-e63520a3373e | -3.19168 | -41.4874 | 2025-10-10 03:57:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6f79d9b2-0d34-3c75-904a-9d6c31b26655 | -2.67589 | -48.41218 | 2025-10-10 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22f5a730-9ba1-3326-94ff-636d57d34e36 | -4.51307 | -37.81398 | 2025-10-10 03:57:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 21211fd9-b787-30f0-9d57-24bdea1e2904 | -3.57104 | -43.51185 | 2025-10-10 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d4f18bb-5f86-32c9-9624-ef1563d94b34 | -3.05454 | -40.81469 | 2025-10-10 03:57:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 49ac1bd2-25d3-3c61-8e5c-bc0415d66859 | -3.97872 | -44.16222 | 2025-10-10 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98e1552b-ddcf-3aea-93c4-b9c21d8956e7 | -3.3596 | -43.3797 | 2025-10-10 03:57:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac7ce5d0-cbb7-3634-85bd-58ccaf93c4d1 | 2.16887 | -50.72072 | 2025-10-10 03:57:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f550c9b9-04c4-37e7-b84b-66ffa28838a0 | -2.87973 | -50.7387 | 2025-10-10 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ac3ead5-d915-3815-89bb-dc1a8fbda5ef | -3.96726 | -44.15683 | 2025-10-10 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15063025-3218-323b-ae37-d933dda044e6 | -4.03817 | -42.52253 | 2025-10-10 03:57:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1355bb83-8dd6-3818-a2a0-936a07191fac | -2.4905 | -47.57506 | 2025-10-10 03:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70c941de-9353-3394-b7c7-673d85ddf8d9 | -4.0425 | -42.51888 | 2025-10-10 03:57:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8c8b3d53-918a-35d0-a679-e619f5ff4aa8 | -5.46273 | -35.66888 | 2025-10-10 03:57:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4a918fe6-5eeb-30bc-98d3-3a5b90dad1e9 | -3.62526 | -43.10542 | 2025-10-10 03:57:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0284508c-bea8-3116-acfc-1617f02e3b9e | -3.18679 | -41.48711 | 2025-10-10 03:57:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a7096fae-83ba-3245-b9b7-fb082b9b3ca4 | -3.97128 | -44.15746 | 2025-10-10 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 958558da-a206-3e00-82dc-9ab127f9c905 | -4.59994 | -37.73081 | 2025-10-10 03:57:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2022b65a-f019-349a-9d25-3076e2a9ff3d | -2.68487 | -48.39167 | 2025-10-10 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82e91bff-31c7-3a77-b87e-75b139da9c89 | -3.00012 | -48.73989 | 2025-10-10 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cd1bd0d-132c-3c2e-8f89-85fe9d54b1e7 | -1.40427 | -46.71256 | 2025-10-10 03:57:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec8dadf6-9acc-3275-82ec-3d1df40bc2aa | -4.9325 | -38.75433 | 2025-10-10 03:57:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7cbaedd1-af13-35d5-b535-708f0205aee3 | -3.47741 | -41.08781 | 2025-10-10 03:57:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3b9a79f4-08da-3a75-b374-7d3adfdb64c3 | -4.44296 | -40.77405 | 2025-10-10 03:57:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63fdbb06-0c4f-3a0f-b999-d3c1f5ae9ce5 | -2.67647 | -48.40865 | 2025-10-10 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9b4fc61-8f5d-314a-9698-eb773b7a5c4b | -2.67531 | -48.41568 | 2025-10-10 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f15a95a9-b712-3ac8-b282-fbf0c9ba815c | -2.491 | -47.57199 | 2025-10-10 03:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d93ba19-c50d-3c37-b585-57ccdda18108 | -4.5234 | -40.7131 | 2025-10-10 03:57:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6cf420fb-583b-3467-accf-4d3dfe509a7e | -3.31854 | -40.02365 | 2025-10-10 03:57:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 269c1035-accb-3512-bf9e-c9ac48246c85 | -3.14544 | -44.43131 | 2025-10-10 03:57:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78327739-dc94-32d4-956c-abc49b20b3d9 | -3.66842 | -44.40157 | 2025-10-10 03:57:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a4b0e2c-fb9b-34c3-8367-f1d18ba8056a | -2.68135 | -48.4131 | 2025-10-10 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cc2be3f-9e1d-3aed-912b-fcecfcb745ad | -4.4435 | -40.77065 | 2025-10-10 03:57:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b1a38c67-2a58-381f-8a4c-5e5efe3fdac5 | -3.96267 | -44.15966 | 2025-10-10 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ed7e013-beb8-3071-a93e-0dffda4b818b | -2.9245 | -48.30922 | 2025-10-10 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f211cc1b-c17e-3ac8-b964-20fddb60fd6a | -3.18818 | -41.48687 | 2025-10-10 03:57:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ce61136b-8582-3b31-bc3d-6eb9171443fb | -2.4915 | -47.56891 | 2025-10-10 03:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5eeca23e-3a8d-3baa-903c-050f5842a4ad | -2.92507 | -48.30574 | 2025-10-10 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b2aed966-1785-3219-8b09-0a8a18d5c3f8 | -3.47398 | -41.08728 | 2025-10-10 03:57:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60f5843b-f9f5-3fec-9934-dffc57332f7e | -3.19029 | -41.48764 | 2025-10-10 03:57:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 76b60ebc-9997-3cfe-8257-f12545362f11 | -3.97185 | -44.15398 | 2025-10-10 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0cad34cb-92d7-3ec5-a459-9a06267a76e4 | -3.06449 | -44.24483 | 2025-10-10 03:57:00 | NOAA-20 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca0bb20b-79c7-3793-93b5-001080d87fda | -2.92393 | -48.3127 | 2025-10-10 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8bc7278b-c8d3-3562-8d18-d986baea6e86 | -2.99949 | -48.7436 | 2025-10-10 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d8b2c66-1515-3f1f-b891-5f4a6eacba6e | -3.66784 | -44.40521 | 2025-10-10 03:57:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2994659-278f-33df-bf3f-d0b8f695a037 | -4.93304 | -38.75085 | 2025-10-10 03:57:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |


[Clique aqui para ver as próximas entradas](README20.md)
