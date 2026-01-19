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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aec1ca2e-f393-38f9-9350-0aaaf51ebbe2 | -5.2797 | -37.7155 | 2026-01-19 00:00:00 | GOES-19 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 64c442ce-364f-3d06-bf73-bbfce01b4041 | -13.5742 | -52.4991 | 2026-01-19 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 10bb3de9-266e-3637-a92b-504b67358e1b | -13.5742 | -52.4991 | 2026-01-19 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 26a3a286-d3d1-3c49-92eb-dffdb8a8b875 | 1.1285 | -60.514198 | 2026-01-19 00:33:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 15eec0d0-a09a-3318-b91c-0f54f3175c38 | 4.4246 | -60.6516 | 2026-01-19 00:33:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e201a12b-4048-3b98-af0e-51e57328a309 | 1.1263 | -60.523602 | 2026-01-19 00:33:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5844bd1d-7d5d-3e35-8da6-848ad9c26549 | 3.9962 | -60.363899 | 2026-01-19 00:33:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1acdabcf-d135-3c61-bb66-a1352bb6c8f6 | 3.7802 | -60.985699 | 2026-01-19 00:33:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 253b9fed-61e5-309e-b73c-67e80ea05daf | -1.9576 | -54.0965 | 2026-01-19 00:33:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f5e2830-ff28-3f4a-bc1d-72483cbfead5 | -10.5531 | -56.340099 | 2026-01-19 00:33:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3016c5b7-97e6-359d-821b-73515e8970a4 | -13.5746 | -52.4935 | 2026-01-19 00:33:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b174b60a-ee38-39b0-a15d-804e5483c635 | 3.9942 | -60.372398 | 2026-01-19 00:33:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4ec77e11-97f0-34c9-987c-6052e6f5d0cc | -13.5762 | -52.500599 | 2026-01-19 00:33:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8a4a6ab-6fcf-319a-a45a-b18b398e172d | -13.568 | -52.509899 | 2026-01-19 00:33:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e142faf-8f50-38f7-9e3b-59c72ac5db52 | -13.573 | -52.4865 | 2026-01-19 00:33:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8fb5cc8b-b452-375e-8709-4287bb3ba650 | 4.4266 | -60.642899 | 2026-01-19 00:33:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 21e509d1-2446-3acc-baa4-a14c2352b632 | -10.5548 | -56.348 | 2026-01-19 00:33:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 143bbdb7-a1d0-374a-bf95-36e921950591 | -13.1212 | -51.722099 | 2026-01-19 00:33:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5c38a7b0-6349-3fde-8354-2c58d7e541af | -2.145 | -53.652302 | 2026-01-19 00:33:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc06d339-31f2-30b1-b760-0d8ab6f8e60b | 3.9982 | -60.3554 | 2026-01-19 00:33:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 81290264-331e-302c-9f2c-d9aba41011a3 | -13.5742 | -52.4991 | 2026-01-19 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| b44ff475-0d2d-3be7-94eb-53fc5fff0e31 | -10.0255 | -36.351 | 2026-01-19 01:00:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 4f2372c0-4078-3474-b2bf-0ce10cf322aa | -13.57119 | -52.49179 | 2026-01-19 01:06:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 35.1 |
| f0b5b6f1-0edf-3f9c-984a-0a78ca3966d0 | -13.57285 | -52.49817 | 2026-01-19 01:06:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 31.8 |
| e37017a3-88ec-3fff-a55a-f06d71e921d4 | -10.55096 | -56.33952 | 2026-01-19 01:09:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| bab45f2a-3f8d-3d9c-8167-a1f2cc68f116 | -11.95869 | -58.73618 | 2026-01-19 01:09:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e1a24ee4-6a0a-3086-8efc-025fc4ea4190 | -11.9574 | -58.72706 | 2026-01-19 01:09:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b0b97d3-3132-3a83-a71c-cf844509787b | -10.0255 | -36.351 | 2026-01-19 01:10:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 281.8 |
| f219a063-ad41-3f2a-aca9-8f486b4d4ca3 | -10.0057 | -36.3814 | 2026-01-19 01:10:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 185.2 |
| f89c03eb-1094-333c-96de-5ab6a1c1694d | -10.025 | -36.378 | 2026-01-19 01:10:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 270.3 |
| 876ca075-14a8-3173-9de7-ae9f02ec4969 | -10.2386 | -36.2857 | 2026-01-19 01:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 133.6 |
| 20820578-027a-3e86-b035-10a7c84fe0ab | -10.2579 | -36.2821 | 2026-01-19 01:10:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 102.9 |
| c690aa65-ea05-323d-9ed5-3853cbfa371b | -10.0062 | -36.3544 | 2026-01-19 01:10:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 194.3 |
| 87529eff-73e6-3ba0-aec5-18981c4e6885 | 1.1387 | -60.518002 | 2026-01-19 01:11:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 87d1939f-f9c1-3ba2-a9e8-21c637eaafb2 | 4.0097 | -60.365898 | 2026-01-19 01:11:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 01eb3155-849d-335a-993b-d4fa4bf992e5 | 4.4516 | -60.641399 | 2026-01-19 01:11:00 | METOP-C | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 53488416-9b29-386e-bfa7-0189adcf233f | -10.5509 | -56.339199 | 2026-01-19 01:11:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6394193b-7654-3cba-9f71-e86a5a89ae2a | -22.214399 | -42.015598 | 2026-01-19 01:11:00 | METOP-C | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aba3b1cd-b907-3a46-ace1-25f3bc0348df | 4.00228 | -60.36129 | 2026-01-19 01:11:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 13.2 |
| cd9780d6-728e-3959-bcb8-56e474727d63 | 1.13378 | -60.52379 | 2026-01-19 01:11:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b2966b5e-d3ae-32c0-b6af-51f22c5294a9 | 3.79045 | -60.98196 | 2026-01-19 01:11:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c451357a-fc99-3e12-9461-2940bd6452ab | 4.00087 | -60.37174 | 2026-01-19 01:11:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| acb5129a-4764-3d59-85ab-5ebbff77263f | 2.20522 | -60.70734 | 2026-01-19 01:11:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 52523ac1-75e3-3690-9c91-f4ea842e2d11 | 1.1351 | -60.51426 | 2026-01-19 01:11:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8025dfb-073f-3e0b-b5fa-e6b7377f1462 | 4.45501 | -60.6336 | 2026-01-19 01:11:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f20d662b-fe0d-3714-bc9c-ceb2a65ba509 | 4.45367 | -60.64348 | 2026-01-19 01:11:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 622a1b1c-2507-38c3-93c9-7a0bf7df5c19 | -6.9255 | -34.9239 | 2026-01-19 01:40:00 | GOES-19 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 69.6 |
| 5008379f-da79-3a74-855a-f35fccf72cf1 | -10.2386 | -36.2857 | 2026-01-19 01:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 109.9 |
| 01a9e00a-c299-351b-9dfc-6c64b3cc38ba | -10.2579 | -36.2821 | 2026-01-19 01:50:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 109.7 |
| 018c4c0a-8467-347b-8014-9951d011cb1a | -8.9461 | -35.1944 | 2026-01-19 03:17:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 694119ca-ea0f-3024-837e-cb89947911df | -8.49773 | -35.0231 | 2026-01-19 03:17:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7d463342-6148-3e85-b7c4-56b1f7a9d82c | -5.75382 | -39.80149 | 2026-01-19 03:17:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 49bd8730-707a-33d5-8d3a-2c99bcf1aeba | -5.6286 | -38.64467 | 2026-01-19 03:19:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cbe88a54-f8e2-353a-98e5-e761d965edfd | -5.27624 | -37.72089 | 2026-01-19 03:19:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 1de850f8-c8a6-3018-b49e-925e42f21062 | -5.99127 | -35.35017 | 2026-01-19 03:19:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 58d7aa9c-5ca3-36b8-b709-b5b7635995d9 | -22.87279 | -42.95961 | 2026-01-19 03:21:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a7f2ac88-2902-36f7-8e99-bee7bf65416e | -22.87197 | -42.96329 | 2026-01-19 03:21:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f679c9f8-75ac-34a2-a595-bd8449528f39 | -4.50386 | -38.48454 | 2026-01-19 03:46:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d984906f-2835-337e-a665-7d2b03a8369d | -4.29661 | -39.15007 | 2026-01-19 03:46:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 645d88c5-f75d-3d79-82bf-6f93e67f58f6 | -4.30048 | -39.1507 | 2026-01-19 03:46:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf62324f-ab28-3e09-b0cf-98826f64a882 | -6.85964 | -36.20977 | 2026-01-19 03:49:00 | NPP-375D | BARRA DE SANTA ROSA | PARAÍBA | Brasil | 2501609 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9276b787-ec06-3684-8744-3961420ddef5 | -5.44602 | -35.61213 | 2026-01-19 03:49:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7d9367af-e1f1-3ccc-a990-148cf2d27192 | -10.99643 | -37.3341 | 2026-01-19 03:49:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4bae8ad9-47a9-3672-a5a3-474eeb6bcc30 | -4.66166 | -40.56029 | 2026-01-19 03:49:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e38a336f-919c-3409-b7a4-e3d96ce5b476 | -8.94801 | -35.19452 | 2026-01-19 03:49:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f8fa594d-5558-3387-a3fd-bd40e31e339c | -5.75505 | -39.79891 | 2026-01-19 03:49:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4414422a-02c6-3147-8ee9-b97da92e299b | -10.2558 | -36.27736 | 2026-01-19 03:49:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1d7cac08-c3d7-3a0f-937c-a5d9b33b9a85 | -5.99462 | -35.34999 | 2026-01-19 03:49:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3c3037a3-ff64-305e-8e56-78917f598fb1 | -6.59759 | -35.32797 | 2026-01-19 03:49:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d9517ca5-bd26-3ee3-a97e-5f40d03ec5c6 | -5.99129 | -35.34946 | 2026-01-19 03:49:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f71aa960-6549-3c79-945e-2028f0cb93fd | -9.18642 | -36.06624 | 2026-01-19 03:49:00 | NPP-375D | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a3f0bf92-e703-3105-8366-6d9e902d114f | -5.27953 | -37.72172 | 2026-01-19 03:49:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c13fb642-9f23-3ac2-8131-1458878968ce | -5.27598 | -37.72115 | 2026-01-19 03:49:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c6d817be-7ae3-3a14-a384-0ef90db7be55 | -10.25524 | -36.28086 | 2026-01-19 03:49:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3731f34e-1c9d-3b81-aa10-b4bc28170912 | -5.75421 | -39.80401 | 2026-01-19 03:49:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5194d21d-dbea-3217-9baa-c11ca5206df5 | -7.7143 | -35.19496 | 2026-01-19 03:49:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 954a2a85-ea84-3a87-b8c0-47cc857250de | -6.85907 | -36.21329 | 2026-01-19 03:49:00 | NPP-375D | BARRA DE SANTA ROSA | PARAÍBA | Brasil | 2501609 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8e5accb-3d8c-3e90-a401-5da6b7a947f6 | -8.4989 | -35.02261 | 2026-01-19 03:49:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 21e4dc87-93cb-31b4-a644-7def9fcc35c9 | -8.49555 | -35.02209 | 2026-01-19 03:49:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e0d15664-4b3d-34ba-b7ae-74ac47cfa525 | -5.27299 | -37.72101 | 2026-01-19 03:49:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 72fb9bfb-18a2-3c11-90bb-294205660af1 | -10.25247 | -36.27682 | 2026-01-19 03:49:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e945d47d-1756-3eb8-af27-b7bbbbc00705 | -10.99701 | -37.33052 | 2026-01-19 03:49:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f3d87e7f-46a0-3756-9ade-c6f3bbe20ec7 | -4.66588 | -40.56097 | 2026-01-19 03:49:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ef495375-a7c6-3d63-a9bf-3e8cc5bd9bb6 | -5.44935 | -35.61266 | 2026-01-19 03:49:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67166c03-9ff9-3366-9365-e12cac74df11 | -20.22562 | -50.92142 | 2026-01-19 03:53:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 450850f3-6058-33d7-b6bb-164d5e329e2f | -29.77989 | -51.28131 | 2026-01-19 03:53:00 | NPP-375D | PORTÃO | RIO GRANDE DO SUL | Brasil | 4314803 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 7adaada6-1d6d-38c1-875a-b00ab2927887 | -20.22681 | -50.91629 | 2026-01-19 03:53:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d4cf3d5f-4cf1-3327-aa43-c07fad9cf69d | -22.87347 | -42.95924 | 2026-01-19 03:53:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 3b624c03-8bd3-3f86-8922-5e91fa3ebd4e | -29.77477 | -51.27968 | 2026-01-19 03:53:00 | NPP-375D | PORTÃO | RIO GRANDE DO SUL | Brasil | 4314803 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 1675c562-1972-329e-a153-5c98a4e80f8d | -22.87261 | -42.96398 | 2026-01-19 03:53:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3ec09591-fb88-3045-8d4d-a450ac46aa90 | -29.77393 | -51.28321 | 2026-01-19 03:53:00 | NPP-375D | PORTÃO | RIO GRANDE DO SUL | Brasil | 4314803 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| c0afe6a6-dab6-3a9b-b952-cce9cd482446 | -3.88365 | -38.43156 | 2026-01-19 04:08:00 | NOAA-20 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 96769caa-ea73-3f0f-953e-0519648c388d | -6.19479 | -35.26587 | 2026-01-19 04:08:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| baa9fa61-e52b-30f6-9ef0-9af9a0b52cf0 | -6.19417 | -35.27024 | 2026-01-19 04:08:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a6076209-b91f-33e8-98df-36988304b90c | -5.27317 | -37.7183 | 2026-01-19 04:08:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 29570ae0-c96c-3091-8c64-09a2b30092fc | -5.62615 | -38.64557 | 2026-01-19 04:08:00 | NOAA-20 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ddcf75f4-c50d-3b56-96ff-6e6ffdc68c04 | -6.85695 | -36.21041 | 2026-01-19 04:08:00 | NOAA-20 | BARRA DE SANTA ROSA | PARAÍBA | Brasil | 2501609 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| edee99e8-ed0e-3307-8ddc-ce7da9286242 | -5.27826 | -37.72142 | 2026-01-19 04:08:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d5d7bb41-3b3b-3389-bbdd-a69bd4eaca2a | -4.29859 | -39.14794 | 2026-01-19 04:08:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 71365d9b-67de-30a9-92ea-350b3b8ae80f | -2.43775 | -46.91106 | 2026-01-19 04:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README2.md)
