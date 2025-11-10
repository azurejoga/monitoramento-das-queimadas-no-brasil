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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc266746-bffb-3fbb-981c-9f51578a8b9a | -5.11981 | -44.72932 | 2025-11-10 03:27:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a9c67f16-69eb-3d56-9552-b07e7197558f | -4.0183 | -40.89902 | 2025-11-10 03:27:00 | NOAA-21 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7f25f9e0-a748-320f-8d96-c252668d280c | -4.15251 | -38.48165 | 2025-11-10 03:27:00 | NOAA-21 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a037662c-4cfc-3075-90a4-577723116c33 | -5.8423 | -38.35005 | 2025-11-10 03:27:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d972b4c3-fea4-355f-80f5-147068bd877a | -6.11276 | -38.16524 | 2025-11-10 03:27:00 | NOAA-21 | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2cf3cc6f-7c1b-3282-9f15-0db69f4518a6 | -7.64352 | -35.15215 | 2025-11-10 03:27:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d8519a95-388b-32d2-98e5-cf08815ebae3 | -3.77182 | -43.98019 | 2025-11-10 03:27:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 821265c7-a7bb-31bf-994f-2e96ffc72d37 | -10.45432 | -44.94403 | 2025-11-10 03:29:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 58a3030e-6de9-3dee-bfaf-4eff8bebafca | -10.46071 | -44.94505 | 2025-11-10 03:29:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 44c6f9d6-4f27-3636-9d7c-09810ac7dd07 | -8.04426 | -39.69611 | 2025-11-10 03:29:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c269a17b-ede5-3bb0-9d9b-19120cd64b1d | -11.53248 | -44.0291 | 2025-11-10 03:29:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edea0ff0-616d-3e93-bc5a-d53565cd21f3 | -9.31218 | -41.05427 | 2025-11-10 03:29:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fe6f7629-4c70-3ed2-8966-486784807eab | -10.46175 | -44.93977 | 2025-11-10 03:29:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0de891c9-daa6-3299-a6c7-9dc0e0ee9ddb | -9.87165 | -37.57164 | 2025-11-10 03:29:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 144cf5e4-79d9-3950-a74f-19e7bfd67835 | -11.90996 | -43.82779 | 2025-11-10 03:29:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad7403b9-6f48-316c-9cc1-8f986ec6c0e3 | -11.91077 | -43.8236 | 2025-11-10 03:29:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2601de80-1756-3339-873c-3ebb9c86639a | -12.53577 | -38.00199 | 2025-11-10 03:29:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4073dbf5-e0a8-3480-afd4-5da35a497b93 | -8.70602 | -41.13175 | 2025-11-10 03:29:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 89ee5917-88c1-3651-9263-0c58a1adc76e | -11.22033 | -41.54708 | 2025-11-10 03:29:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 200d4592-6d71-3d8d-9c65-e732a90412ce | -12.31198 | -37.91976 | 2025-11-10 03:29:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c833d5af-ba0b-3058-a88b-24fdbde6d449 | -9.81593 | -36.47537 | 2025-11-10 03:29:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 3e0254f3-e068-3bbf-a485-0f775d32e363 | -11.22089 | -41.54409 | 2025-11-10 03:29:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2664f915-a7ed-3a9a-a3d5-39744489a515 | -8.04608 | -39.68584 | 2025-11-10 03:29:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee5a2ce9-8af8-3631-a713-4080ac63aa53 | -11.16671 | -43.57243 | 2025-11-10 03:29:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd63a0c9-4dab-3378-af70-7422b98d4447 | -7.05165 | -43.94494 | 2025-11-10 03:29:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe825be4-1fbd-3cb7-b30e-ad393a8a6d75 | -9.9124 | -44.21471 | 2025-11-10 03:29:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2a9549a-e40e-30ab-b161-f25725d6ac59 | -8.65631 | -38.14241 | 2025-11-10 03:29:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a860b811-1c00-3610-810e-51257c6cbea6 | -7.98553 | -38.66963 | 2025-11-10 03:29:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0710c961-26c8-32f5-b25c-6fc798cf215f | -11.17249 | -43.57348 | 2025-11-10 03:29:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 919e99d1-5344-302b-9799-73ebe4abb09d | -9.23988 | -40.62683 | 2025-11-10 03:29:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 07bc28be-3550-3717-be4a-e09a308bd72f | -11.16012 | -43.57554 | 2025-11-10 03:29:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| faa3ac2e-f7b1-34c8-a0f9-605824c4a13b | -12.53969 | -38.0027 | 2025-11-10 03:29:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5d0c0ffb-005b-3487-8e41-3e83c41ee44d | -11.19966 | -37.77172 | 2025-11-10 03:29:00 | NOAA-21 | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c1387583-3d6e-375c-8d88-d1b028d2935f | -9.31162 | -41.05726 | 2025-11-10 03:29:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7472bba3-66e6-37c8-83bd-5fadb3b89bcd | -7.41498 | -40.0715 | 2025-11-10 03:29:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 63724249-4808-3730-b3a5-906408d62107 | -8.71115 | -41.13274 | 2025-11-10 03:29:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8de24407-3e66-3b48-bcc5-887330c3d021 | -8.04045 | -39.69018 | 2025-11-10 03:29:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c8036c61-bf76-3bf0-82f3-538a4b4151a6 | -7.41315 | -40.06934 | 2025-11-10 03:29:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 384c737d-03c9-3b99-86be-073a3290cbdb | -7.9855 | -38.66807 | 2025-11-10 03:29:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d81790b2-78de-30ca-98d1-d8555e6493ac | -9.81966 | -36.47601 | 2025-11-10 03:29:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| daa3793a-1185-348b-9ad9-0b7adc1f2a86 | -7.41597 | -40.06597 | 2025-11-10 03:29:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 928c3bdb-b250-32b0-8ad0-a22668010c41 | -4.1943 | -50.6281 | 2025-11-10 03:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 2f4f9e11-7004-3276-9c1c-c555a8d207d8 | -4.2128 | -50.6273 | 2025-11-10 03:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c034cd2d-8b27-36c5-9505-deb4cb685bc7 | -14.69428 | -46.6067 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5d9eda5e-8130-3db9-9f26-7add5504df16 | -14.69155 | -46.58817 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f3915be-7179-32be-8efa-fe91c9d2baae | -14.70101 | -46.60993 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 261f8f2e-d18e-3b90-b3e5-641bb2e5b941 | -14.71042 | -46.59758 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4cc30f1-be5a-3a64-9f06-38966ed5c168 | -14.70263 | -46.59967 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c351aee-4d61-3dac-a2af-835e392c63d2 | -14.70404 | -46.59324 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e05e3453-fbaa-33c7-82ed-31f585423a1f | -14.69639 | -46.59972 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3df72f37-bf6c-39d6-b9eb-515c57f80aca | -14.69551 | -46.60112 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 70712b8a-eb31-31df-b4d1-8847c305bc4f | -14.69422 | -46.57798 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5b286716-4153-3099-b8b1-780b25f7aeb4 | -14.7014 | -46.60525 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 323d42a9-e329-3b0f-9d88-d236cfdc5e6f | -14.69521 | -46.60527 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 42003b94-ce70-3468-ab04-c655aad6cf07 | -14.69877 | -46.58625 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 17fe558d-f354-3f5f-980b-6b76a2ded9b8 | -14.69331 | -46.58016 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f00913fe-ec8a-3637-894b-288936aa1a8a | -14.70349 | -46.59826 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2b17287b-5942-3bee-87ca-6d0211ad4e76 | -14.70232 | -46.60374 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92fa00cd-e352-3a4f-b64c-71023593c45d | -14.69249 | -46.5861 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8113a97f-dd2f-337a-b7c6-4af4ac6701ec | -14.70826 | -46.605 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92dd6ea7-525d-36b5-8901-11292f8dfa2a | -14.69777 | -46.59323 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7d85a91d-c249-3d87-b6ec-bd232d67828f | -14.69678 | -46.59531 | 2025-11-10 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8838912e-ae05-3b8e-a4d6-f416baa7b8ec | -21.96506 | -49.8121 | 2025-11-10 03:34:00 | NOAA-21 | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d45dfeb1-63fa-3fcf-b3c4-11ed3cf3f41d | -4.1943 | -50.6281 | 2025-11-10 03:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5c7fa35f-39c1-390d-8cfc-352aeac443c4 | -4.2128 | -50.6273 | 2025-11-10 03:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 54bea257-40cb-34d7-a395-8a28b3500597 | -4.2128 | -50.6273 | 2025-11-10 03:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a9b909a3-a583-31a2-84aa-028f12a04bca | -4.1943 | -50.6281 | 2025-11-10 03:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 821df9ca-42ca-3727-9584-727a6dbcdcf5 | -4.70934 | -45.65354 | 2025-11-10 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ff5c4d7-b186-3a95-8f97-96cbc0335ae9 | -5.9256 | -43.93535 | 2025-11-10 03:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eaa1d8d4-a1cd-3f88-a279-6562aaeafee0 | -4.09514 | -46.28254 | 2025-11-10 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f56ec8bf-deab-3b34-9939-017aa61a68aa | -3.94795 | -47.05568 | 2025-11-10 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6a516a3-3759-3d56-98be-d7b63ffc5ba4 | -3.69482 | -50.183 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 028a8b15-a103-35da-abaa-fb3f8f12f6ee | -6.87449 | -40.73404 | 2025-11-10 03:57:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 31dad364-8272-3825-9305-2003e24de1c9 | -2.47977 | -48.36613 | 2025-11-10 03:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c192a4ac-82d4-3c60-b8f1-a6a73ff63a46 | -4.26713 | -40.8597 | 2025-11-10 03:57:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| de32ca66-ab47-3564-b35e-254b208c2282 | -4.68109 | -45.84816 | 2025-11-10 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6a8eccc-d926-3b34-93a9-4669637a62b8 | -3.90831 | -50.03184 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 04598533-adfc-3d96-832c-b4e66576b6fb | -3.32884 | -49.922 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d966f14d-56a8-3ef4-8223-607f25e7c276 | -3.69607 | -50.18791 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a7e0e66b-c97f-361c-968c-6a7e0bc97e24 | -4.63547 | -49.59325 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 03d6a61e-89c3-3a0c-a899-24e491f95bb5 | -4.81001 | -46.72345 | 2025-11-10 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7cf8a067-8363-3ff9-9b2d-3537aef05f88 | -5.04861 | -49.55909 | 2025-11-10 03:57:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b34de5dc-55bb-39b7-a6b4-80f984c46dcb | -6.14963 | -43.4827 | 2025-11-10 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d9174e36-51b2-3b87-b265-7ec0ba5e50f6 | -2.94665 | -51.57499 | 2025-11-10 03:57:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 567501da-49ac-317e-adf6-ffa99be152f6 | -3.40351 | -50.45584 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 468cbdae-93aa-3877-adb7-3bb404533cb6 | -4.58564 | -45.54369 | 2025-11-10 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c14d0d53-2e30-3257-8616-bb111c1f9d54 | -4.86922 | -37.44901 | 2025-11-10 03:57:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c97d9c5c-31a0-31b1-a01e-474caf369a31 | -4.07292 | -44.13035 | 2025-11-10 03:57:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85979a06-2f73-3f42-ab85-f7d98ec5c246 | -2.84584 | -48.65271 | 2025-11-10 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 591369bd-64d6-320b-b6ba-699451217eb4 | -3.80211 | -51.0943 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9ff1d129-46b5-3388-9447-60b8e7f38b30 | -9.23955 | -40.6268 | 2025-11-10 03:57:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5ab2c987-dcc2-3d37-9990-28f28dd16c35 | -9.81655 | -36.47593 | 2025-11-10 03:57:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 121cbd21-cc85-39bd-8f0d-6ed53769b39a | -7.05198 | -43.9475 | 2025-11-10 03:57:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6e8069d-1b5a-3121-b910-2730a702fa40 | -4.209 | -50.62736 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| c2d40214-acae-372b-83f6-eec3bc147990 | -4.20222 | -50.62648 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b00df46f-ae7c-3a8e-af45-9efe1cbc26cc | -7.4151 | -40.06701 | 2025-11-10 03:57:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e6f6554a-ed87-3f06-be72-8322c98c3427 | -4.09463 | -46.28556 | 2025-11-10 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 56e12225-ac41-3bfb-ab0e-61bef3594db0 | -2.84661 | -48.64813 | 2025-11-10 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b22bcc9b-e9f2-37ff-a33a-b1129e467310 | -3.69284 | -50.19418 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 19f48c77-629b-393d-b974-de211c3f1a29 | -2.96176 | -45.07733 | 2025-11-10 03:57:00 | NPP-375D | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README5.md)
