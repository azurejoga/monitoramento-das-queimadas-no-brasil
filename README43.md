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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c42dfac1-9a0f-3bd0-9dff-47095dadd2b6 | -6.47676 | -42.18553 | 2025-09-13 04:06:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ffb26b14-05ae-359f-b809-5e850dd350a4 | -5.72569 | -43.19095 | 2025-09-13 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 608f1b6c-b73b-3b7f-bff3-7a3b1906d556 | -6.24078 | -43.41256 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba59c5c3-3212-397c-9e7f-f7caee118c32 | -5.10731 | -46.07048 | 2025-09-13 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34d4cbcf-09ab-3e88-8365-91816e0f9a3a | -7.45872 | -44.44248 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f93eca56-ed57-32a7-9598-5befaa485b78 | -4.54557 | -43.73035 | 2025-09-13 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6df2445c-9e3a-3e61-a1f1-b0ba2d5a1566 | -5.95241 | -42.78654 | 2025-09-13 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 49110b95-11db-36b0-a693-a5f5ae853972 | -6.99816 | -41.63927 | 2025-09-13 04:06:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ed64aa75-7ad0-3d2a-b413-701f5582619c | -6.38955 | -45.65889 | 2025-09-13 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c0ac7e7-947c-3e7a-81e0-6ab695987985 | -6.44163 | -42.61951 | 2025-09-13 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 58c218bb-bcd2-3930-8db1-644ac314825b | -5.9502 | -42.77884 | 2025-09-13 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a627c77a-7cfd-32e2-89bf-0ad710ccbc2a | -7.54724 | -42.52517 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3be359d9-055e-317f-92ef-991316cc97a3 | -6.45406 | -41.75148 | 2025-09-13 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06d71cd4-e7bb-382a-826d-0606c20be509 | -6.39108 | -45.64963 | 2025-09-13 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 042d6951-b8a8-325a-95ec-c58ebdfbe21e | -7.43706 | -44.39806 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11cb7d4f-3e52-37c4-872b-99d3ee0e71b4 | -7.70618 | -44.83318 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2715682-1ce8-3348-bc02-6f3e76c8dbcf | -7.57264 | -42.64447 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 85dd82d0-0ccb-3ae2-97c2-b7a515747197 | -5.40418 | -45.93044 | 2025-09-13 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ab78fcb-8940-3281-86c9-cc435f635e89 | -3.79568 | -47.58 | 2025-09-13 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06517028-795e-3d41-914a-1abf49c896c9 | -5.65997 | -42.6198 | 2025-09-13 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0fd6343e-08fd-37df-93ce-3c6a4c2db998 | -5.20501 | -44.31328 | 2025-09-13 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bff0c69f-88e2-38df-b103-70fdf8aa6ccd | -5.34999 | -47.29324 | 2025-09-13 04:06:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0fb8705-8d15-3748-91b0-ba0f5a8a52b3 | -7.52207 | -44.67547 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 077fe602-da7f-34c1-8d83-92d9b979170d | -7.45519 | -44.44193 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 448f4bda-8959-3763-9c2b-1dd59b5a5719 | -5.95509 | -47.22516 | 2025-09-13 04:06:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d285d8fc-c567-3d52-90eb-7cc32bba3474 | -2.85768 | -49.50354 | 2025-09-13 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a54b254-c0ee-3ff1-8a4d-a493529e836d | -6.80408 | -45.63813 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c11398f-ba43-36cb-8dc2-abe55ad30377 | -6.31883 | -44.58637 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b39cc211-f228-311a-ada4-e35a8720b1a5 | -5.68404 | -43.36319 | 2025-09-13 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d6100f2-a8df-3b28-82c7-4b5251633eae | -5.7542 | -39.12974 | 2025-09-13 04:06:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 11d763ba-dc9b-32ec-be80-76a28913cf89 | -6.2895 | -44.23646 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93f19aa8-8e1c-3e90-b57e-5b0675d24f83 | -3.79496 | -47.58435 | 2025-09-13 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 201edc94-79dc-36c5-820b-08046307b601 | -6.55693 | -44.77649 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 791962c5-4188-3618-b416-1e8cd74ada45 | -6.85171 | -45.65587 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c12126aa-cafd-3443-8b7d-2e9a5e9052a7 | -5.64961 | -43.89511 | 2025-09-13 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7955ae49-e74b-3ea6-acc3-ead76012f54c | -5.64336 | -45.94051 | 2025-09-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f5f9ef3-8bc0-374c-90a1-242dfbf557ca | -6.85551 | -45.63266 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f989581b-18fb-336c-b1cb-733b317878c6 | -7.23351 | -44.42368 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d92b816a-dfa2-3e81-a0f2-d5dd1f76f963 | -6.17542 | -41.12664 | 2025-09-13 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 852c97a1-a8da-3f37-908a-674b4c4e0a01 | -7.97927 | -43.65757 | 2025-09-13 04:06:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12b9c51e-ec02-31b1-99e3-4ae2d44e7528 | -6.69189 | -44.12101 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a100a767-4f64-3ecc-b4f0-0be8ca6c0c93 | -6.3283 | -42.22316 | 2025-09-13 04:06:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b16d70e1-4cfd-36f3-82a0-ba7cd0612c8f | -5.54128 | -46.42087 | 2025-09-13 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b849c7b4-67b2-3281-843b-ec51c52930b6 | -5.93044 | -46.54034 | 2025-09-13 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a204eed2-2a6f-3804-8f73-661be42ccc70 | -6.69725 | -44.13721 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 030172fe-4aee-3d40-9d78-52bd3da4badd | -7.06028 | -44.68295 | 2025-09-13 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8c2f5e9-92ef-3a41-8f4d-9960eff158cc | -5.5974 | -42.90121 | 2025-09-13 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e18198cd-ad52-3b80-909f-7720b7af7ff0 | -5.08674 | -41.16007 | 2025-09-13 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a64991c-60b4-3964-8262-acba81f33f5b | -6.98728 | -43.80377 | 2025-09-13 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3970a92d-26eb-3555-9d8b-a07bb72ebf8f | -6.21425 | -43.44645 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1cb938c4-93e0-3e59-bc1c-d7558b4bedff | -5.72004 | -43.1825 | 2025-09-13 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 058ad977-1629-3d2f-88ad-21b2c9c6fa9d | -7.39384 | -44.35145 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dca02e10-c29b-3e92-a438-e87e623b959a | -7.43639 | -44.40206 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ac45a57c-a54d-391c-a952-ef9a724de3cf | -5.20435 | -44.31738 | 2025-09-13 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99d8b14e-a055-34f9-9f77-84966ee3203f | -7.55931 | -42.64233 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f3beb134-db9f-363d-9001-041c79213cd4 | -7.11581 | -44.89127 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 422ab475-cc3d-38c0-9f47-4a7080fb1b07 | -6.79462 | -43.41263 | 2025-09-13 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 64c2c219-2e02-3379-b908-acddde9767c6 | -5.41952 | -43.41452 | 2025-09-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36c3bb0c-4741-39ad-8071-55337b37407d | -7.40409 | -44.3327 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1339636a-5c0a-3424-aa97-b85e87b48f83 | -3.72064 | -38.63174 | 2025-09-13 04:06:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5d912d8f-e9be-366f-9c10-d8da93fa41f7 | -7.70197 | -43.85497 | 2025-09-13 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ac08d35-5082-3238-89ee-063bbecff81e | -5.53179 | -43.04402 | 2025-09-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27f7c142-02bc-336a-858a-07a19eab43e5 | -7.43574 | -44.40606 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d35f15d7-a16c-3e0c-bdf8-be8f25cdfedc | -7.45808 | -44.4464 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc4332c9-6875-388e-8e67-7d709ee213fa | -5.37889 | -43.43195 | 2025-09-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95cbae7a-0ab2-3751-b338-ee228c7c6a73 | -7.50648 | -44.6812 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 537017f6-5ee8-3e67-8ad8-bc12e5d93d67 | -3.22302 | -47.63158 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 193a6f63-2876-3ba6-94cc-d84a8261db7a | -6.10143 | -45.94312 | 2025-09-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04937578-e325-3cb0-8b15-b3b5c0993662 | -3.24098 | -46.78705 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 6ebc2ea4-654a-3a34-9444-d23412b35d6a | -5.30137 | -43.06006 | 2025-09-13 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b046df6-d0b7-321f-b1fc-a169e8c6a836 | -7.41897 | -44.35445 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7332170e-8815-39fc-ad87-dc56894799df | -4.94419 | -37.93357 | 2025-09-13 04:06:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 85253acb-4bd3-3b80-9441-789ef6832707 | -6.88125 | -45.64147 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea6c7dcc-03b6-309d-ba38-384e2acf673a | -7.54318 | -42.65781 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ae04a356-40d8-35dd-8387-d3e3e19cc8bf | -7.32746 | -44.42579 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7733d5e-fe4d-3e5c-9207-af9fc3b5700b | -2.65427 | -48.8003 | 2025-09-13 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4712dbf7-5d7e-3742-8490-fa94c4bc0b2b | -5.41151 | -42.83458 | 2025-09-13 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e52ab1a2-9053-3436-80ce-6f35ea94e52f | -3.23668 | -46.78634 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d704ec31-3891-3667-8e7f-1922caac2ac8 | -5.41825 | -44.82096 | 2025-09-13 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e0f11f4-68f2-383b-86eb-6a033e8cb713 | -6.67734 | -44.16674 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e87d3e15-d393-3c52-a598-eba6bcd44c65 | -5.49298 | -42.15495 | 2025-09-13 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e438635-d0bd-3ca9-9099-f7122e88da15 | -7.41611 | -44.34992 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e19162f3-2624-31db-b161-72bb7b502381 | -7.43508 | -44.41004 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47f75aa9-fb3a-3a08-94b1-1cffde846ff4 | -7.63431 | -40.45464 | 2025-09-13 04:06:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c4e314c8-89be-3d38-a966-f34e759fe35f | -7.40345 | -44.33666 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c2bafbf-9980-33b3-adf6-41ea55a17873 | -6.20784 | -44.24862 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1dabbfdf-5463-3ac0-a016-6706d8e35875 | -3.66469 | -52.17398 | 2025-09-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df526a53-1035-33ee-b43b-ed8c04de0d65 | -5.94347 | -42.77776 | 2025-09-13 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c4673b24-bf01-367e-849d-e62fe2ac95da | -6.27891 | -44.23459 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8b856e2-767e-3870-ae50-76230326a1ca | -6.2882 | -44.24444 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee894ee4-7aeb-3df2-976c-ff04a52e8384 | -6.31523 | -44.58581 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a836920-76bd-3073-aaf8-5deeb6e59bf3 | -6.44358 | -41.75336 | 2025-09-13 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 78354e91-2d4d-3e14-8c6b-7bea6a3886ed | -5.65833 | -42.60857 | 2025-09-13 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0c13b059-b858-36d0-8e67-a4623c90bc4c | -5.40474 | -42.83354 | 2025-09-13 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8ce29d4d-a2f3-345e-ae86-4b5112446f07 | -7.44057 | -44.39867 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c4dbfd3b-5ede-3ce6-8a85-fb5bb3b6936b | -3.79678 | -48.63934 | 2025-09-13 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3718feba-00d0-3d54-9959-ef889e3b7357 | -7.06385 | -44.68362 | 2025-09-13 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d62cb41f-9d46-3d9e-a81f-a9139004e890 | -4.08115 | -48.04513 | 2025-09-13 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f29a266b-2f1c-3869-8c5f-757c6ee6c809 | -5.49536 | -42.67797 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1758d110-36e9-3988-98cc-60f642bec9cf | -5.95551 | -47.22565 | 2025-09-13 04:06:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README44.md)
