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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| faa94861-5ca8-3981-9743-c14319d6bf43 | -3.9902 | -56.26585 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9d448db-b2ff-367a-ae57-15f42e438a76 | -2.80563 | -52.09013 | 2026-10-07 04:19:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2487bb9-c4b9-3767-be7a-b68000b011ec | -6.58483 | -53.03246 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d5c74d6-f32b-3e3e-9864-673b016ccd97 | -3.29453 | -54.07035 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4f96c6de-b0af-3eee-8206-1eed232370de | -3.2685 | -54.0356 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| e0e5d928-e41d-3491-942a-e2cff94000f0 | -1.52145 | -46.89413 | 2026-10-07 04:19:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4c191127-ddbd-3c64-9c7f-26d5b7e4f75a | -1.28717 | -54.56236 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 495669db-e8d4-394c-b8da-3614a4361eba | -2.95782 | -51.04726 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 127de0bc-743a-3b57-b99b-c199ec3f4be7 | -5.97878 | -40.94517 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 3fa73891-c76b-37e6-8a84-1c8f0c81e546 | -3.51339 | -54.67212 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 64dc376e-dea4-3cbc-af46-92fc26b80239 | -2.13311 | -54.80289 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4a7fbb29-3370-3f8d-b002-92b70285a01a | -8.04266 | -47.81479 | 2026-10-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46d81031-757c-3e36-962e-38941fd9278c | -7.2717 | -45.5742 | 2026-10-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fdd9b013-bdbb-3d51-b09d-ccd70e4f1dce | -5.97364 | -40.9327 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eabab929-3fa1-302a-b187-2dfb7087c93f | -6.93523 | -46.59358 | 2026-10-07 04:19:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faee7127-fc39-3dd6-8b5d-d837721970d1 | -3.04172 | -54.26524 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfba1b3f-d84b-3644-bf19-b53af178e03f | -4.35044 | -43.79838 | 2026-10-07 04:19:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c103375-fc2c-3eac-a148-9078f54f878b | -3.07223 | -54.25703 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b62629a-889c-3487-b503-c8b1c6756709 | -3.48935 | -54.61967 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25b5b222-37e8-3458-9a3e-2b0d70e91951 | -7.84952 | -44.20643 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d20d6463-bc99-3171-abb6-9200f7ef1b80 | -7.4027 | -45.63349 | 2026-10-07 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7d9a833-d58e-3613-9ec8-0f859db51e7d | -6.40792 | -52.71702 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c9b29c6-45f9-371d-ab7b-c777b3b570b6 | -3.29246 | -54.07335 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 22d44452-13b3-3801-9dc9-f7fd5fb0f001 | -3.28169 | -54.03303 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 872f4b8e-a432-39fd-8d9f-654943ac8304 | -3.26679 | -54.04563 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 3b8deb16-c715-34de-91fd-99363a04344d | -4.24178 | -42.66296 | 2026-10-07 04:19:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66a78986-b33e-3d95-a7ab-2921de2e0f6d | -4.2618 | -46.38288 | 2026-10-07 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c17385cc-c3d9-3d5f-9c5b-7f05ace43d20 | -3.28625 | -54.04375 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5257a860-f453-3de4-99cf-6a24c28b63cb | -7.81662 | -46.86677 | 2026-10-07 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 057c17b7-c3be-3c32-9ded-dd29167d5e5a | -3.61264 | -55.28297 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 28c9aeb9-82b8-3c22-92d8-e0721ea1befa | -2.77395 | -54.08871 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5c25dafd-b7a7-3b5b-b7b0-91030ba78d64 | -5.97415 | -40.95217 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| edd6a06c-e93d-3ccf-8a6a-b227648477b5 | -3.10275 | -54.15523 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbe6fcc0-9a26-3d97-9d25-448d7b0d15d7 | -3.19971 | -42.957 | 2026-10-07 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9668cc34-0bd9-3b4f-ae84-8985f474859e | -3.34526 | -54.17556 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 73e37cb2-ec67-3984-a246-00de8bdce294 | -5.72319 | -45.15252 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee193ae7-ab7c-3f59-aa71-57dc41c39189 | -4.18371 | -51.13763 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9978f6f2-b110-3ec4-9ca3-e6aa3894954d | -3.02785 | -53.90053 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8564bcf7-559f-36c8-90c3-7cdbe5926373 | -8.21059 | -46.34859 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6f585e3-7ade-3a53-89e9-83b1de5da3b1 | -3.28774 | -54.02758 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d8ac705d-b6de-3b8e-ac53-392c9f0b841d | -3.51044 | -54.65664 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cbd4eb47-1e36-328f-933f-5cb44f9049f2 | -2.77607 | -54.09282 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 134ad842-4666-389b-a6a3-6e257288c7da | -3.17563 | -50.44296 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c44ab97c-a328-3d2d-a788-5c6d9f778eac | -3.26207 | -50.40664 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f6cf557-9088-3a20-90ff-77f678ef06a7 | -3.56055 | -54.48433 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d48e3b2-98e3-3efd-9043-f80a797548ad | -2.93403 | -54.15578 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7a15ea1d-26b2-36de-be29-3ab58ad23a37 | -4.25237 | -50.7302 | 2026-10-07 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97bc7ce3-026d-32d6-9487-02866a24bc2b | -3.28495 | -54.01376 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0e3eb7dc-9400-3be3-8039-4cefc1e88381 | -4.16063 | -55.16787 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82d2ab5c-2beb-344c-96dd-fe4f8b676bed | -2.94114 | -54.15192 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8cff8c7b-e58f-3fb7-a0df-f6355d12bceb | -3.51429 | -54.6668 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f8f451ec-afad-370d-ba97-f90b40a2fdfb | -4.25511 | -46.37733 | 2026-10-07 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb2df07b-1b3a-3394-bb09-cb9d596b2afd | -3.58472 | -54.30991 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbb6e195-88d7-3a26-b843-7c1e1f12f9ae | -7.87862 | -44.19329 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d2e6de06-6d25-3d6a-b8b4-0a46a1dd62c3 | -7.09678 | -45.57345 | 2026-10-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fae18a7c-19e7-3546-84a8-59a33e68951e | -5.23305 | -48.39743 | 2026-10-07 04:19:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4143d03e-5056-3db2-9a01-162c044d12c9 | -8.03807 | -47.81886 | 2026-10-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c274e5a-dccf-3903-94e7-e7035021d582 | -2.76439 | -54.08553 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1e8e1435-1a66-3155-864b-2f9256adf66a | -7.20995 | -44.29372 | 2026-10-07 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e16b5cc6-f351-3583-bb6a-92e6780344fb | -8.63415 | -44.8895 | 2026-10-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 286be2b3-fcfa-3344-9738-9d2d5a0f3861 | -7.09804 | -45.24013 | 2026-10-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 769e4f9f-7e24-326c-b6db-7b3a21a98c7d | -3.27508 | -54.07205 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e8cd714d-ee02-32a0-bd9e-4316927eb01b | -3.48572 | -50.08939 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 966a0b47-a33a-3e29-b48b-35dd676e9088 | -4.92566 | -55.87386 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c3b4c908-21ec-3919-bca4-42c128dab6ef | -3.50856 | -54.66724 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| df4dd8d3-91e0-3e9d-ae0c-cc3c9ce19f2c | -3.00127 | -54.12292 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f9e44f89-406f-305c-aac6-2859d363c957 | -3.05583 | -54.21967 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f5143cc-5063-3154-a0fe-ea74fadb797f | -3.11125 | -53.77576 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 320b55e8-391d-3bec-9a8c-54dd5941dcfc | -4.45426 | -47.91794 | 2026-10-07 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| bea6bc42-05b5-3530-8c6c-38c57240c3ec | -3.27139 | -54.05613 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ec16c34f-c063-336e-a428-3609bd23a9b5 | -3.28605 | -54.03716 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| eb683785-a6ae-3233-84e5-9d9cab616374 | -6.57287 | -46.19258 | 2026-10-07 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fadec79-148c-3e48-9555-632fd2d82bcd | -3.08222 | -54.2743 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6b8f7108-a926-3d2d-b44d-0b7176a64823 | -5.97069 | -40.95163 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c10610db-7a74-39be-8ee7-545b5aefd7d2 | -3.03792 | -54.26772 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51d68299-f18c-33c6-84ef-eae5ba591aaa | -3.0569 | -54.23336 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46812768-9d0e-3330-b84e-bc349f6513a3 | -3.72413 | -51.21185 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5492ac28-382c-3817-83e5-8f8f513e084c | -1.25896 | -49.05751 | 2026-10-07 04:19:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c748ae73-71d7-3b8a-97fa-711abf6427f5 | -3.71038 | -51.13821 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea3086bb-233c-384e-8375-ea821baf38c9 | -3.01832 | -54.13615 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c13494b-d289-3e1e-a16d-ede1f5126202 | -3.16586 | -50.44118 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a8d4ff4e-a841-3926-b548-3075750310dc | -4.13755 | -54.92386 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7292ea27-7af8-313d-8a96-a1d4d32cf751 | -2.99599 | -51.11799 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 681fc498-323e-3d36-adf8-cd5140459f94 | -3.27092 | -50.79258 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f4e8061-e7f6-31c1-8c31-c4ddbfdd4c20 | -6.34892 | -42.5697 | 2026-10-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a91ae540-50d1-3fbe-9b52-a1dc04ec4217 | -7.10488 | -42.53389 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b01b5b0d-6eb0-3c7e-b1b9-47b8f3dfa9c0 | -2.1511 | -51.97786 | 2026-10-07 04:19:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 388d9994-ec62-35bd-946c-5fd3f4b1789e | -3.52518 | -54.64148 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ddf77a17-6a9a-3732-8a57-0e2a81cc9a5b | -6.92298 | -43.66582 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 9d0e2908-c454-3f8c-9a85-0ea74cd19522 | -5.21119 | -45.80989 | 2026-10-07 04:19:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01673591-131a-3935-b102-712549143fbc | -4.12013 | -50.8147 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f426459-bda5-3a43-92c4-ae81f98a54c2 | -3.22273 | -54.3045 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ffb12b1-3385-369e-bfad-b146acd5b45e | -3.06962 | -54.17585 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7e81084-2f3e-3d81-b908-94b7f2c38de1 | -8.43986 | -46.40895 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 557ddf5e-aba9-3928-9c59-d16cd5c7fb18 | -3.055 | -54.22465 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3b41713-7b55-3bba-ab11-bb1bafa9a27f | -4.36631 | -43.90885 | 2026-10-07 04:19:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 12b927b5-85d1-36d4-8a9d-8bfedc2e831a | -2.76188 | -54.10067 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 8fac3134-739d-3dd9-b3c0-a627ca6a7c4c | -8.03426 | -47.81821 | 2026-10-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5abc096-e337-3d88-8339-632980c338a0 | -3.07676 | -54.26835 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cac71b15-7bf9-3736-b6cb-c8628ab87db2 | -4.13847 | -54.91869 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README57.md)
