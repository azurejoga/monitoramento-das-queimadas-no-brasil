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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73abd834-1391-3645-9600-f64f7592257d | -8.0152 | -47.6656 | 2025-08-21 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| a1d8fc1a-e012-3dfb-9a17-15614bb3a595 | -8.1687 | -47.3658 | 2025-08-21 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 4a5e0fb5-8803-3621-92cf-25030f86a8b0 | -7.0354 | -44.6167 | 2025-08-21 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 6690085e-04ea-3e99-8858-ef22926eed31 | -13.1367 | -54.9171 | 2025-08-21 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 423.8 |
| 3ac7fa11-7cac-3327-a271-6d5a8a2f0d54 | -13.0317 | -45.1724 | 2025-08-21 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1038.8 |
| 94b72ffd-1d4e-3497-8daf-9da28f23d93e | -6.2924 | -43.8747 | 2025-08-21 14:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4797172c-e7b3-3370-8a05-a9a6d7837707 | -5.2518 | -40.7296 | 2025-08-21 14:00:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 114.8 |
| 25b1faa1-5644-3d86-85ff-38427a16e503 | -13.3349 | -54.4027 | 2025-08-21 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 1dba4e24-802e-3b36-b43d-fe3a28ce11ae | -13.0321 | -45.1492 | 2025-08-21 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 247.7 |
| 51eeb526-caa5-3d45-9408-4704437b86c5 | -5.2345 | -42.7193 | 2025-08-21 14:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 3cc3710f-b57a-3488-ac23-01bddc44b093 | -13.3154 | -54.4254 | 2025-08-21 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c86c9d31-d148-3d09-8cdc-35e6c76ae441 | -6.1 | -44.397 | 2025-08-21 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 02d0553c-cdda-373b-9698-e984f97ddc23 | -8.7756 | -45.4713 | 2025-08-21 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 221.1 |
| 752c6bfa-1c01-3e28-a35d-ac82cbae0f3d | -7.6296 | -45.2464 | 2025-08-21 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 1a247d7e-00a0-3f45-9385-acdf7957d063 | -6.2434 | -45.0704 | 2025-08-21 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 6bcf170b-8d11-3943-a410-c5caeeb4469d | -7.0166 | -44.6184 | 2025-08-21 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 20cfe945-e0e6-39e7-b4f3-5699aa54be40 | -13.051 | -45.1693 | 2025-08-21 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 233.1 |
| fe9c9177-b165-3276-bccf-cd915b3b362d | -13.1555 | -54.9357 | 2025-08-21 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 795b5bbb-62b1-3296-a309-2b878bf2dcbe | -6.2434 | -45.0704 | 2025-08-21 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| e7c92418-e4ce-3380-8b18-f317e7dfc8db | -8.7756 | -45.4713 | 2025-08-21 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 391e0130-9b1c-3abc-bdf4-c147af62d5cd | -13.0515 | -45.146 | 2025-08-21 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ff2a6fb8-89a4-35c3-94f3-f47bde8ffce7 | -13.1364 | -54.9376 | 2025-08-21 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| c330f409-b527-3652-aa8d-aa2d8610c5b2 | -13.0307 | -45.2189 | 2025-08-21 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 6c880827-de06-3a9b-83ae-8f09ce0b6aa2 | -6.7994 | -43.8544 | 2025-08-21 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| c6435ceb-5eac-3055-b012-740277c67560 | -4.7844 | -45.3057 | 2025-08-21 14:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| a82cd553-1a56-3215-acb0-864210007b5e | -14.7501 | -56.0356 | 2025-08-21 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 746fd498-fa46-360c-94c4-bf5d50476294 | -14.3321 | -52.0224 | 2025-08-21 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 095008ea-d90e-32c1-8ecf-f6e821a46d74 | -9.7241 | -47.9588 | 2025-08-21 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 6fafacc4-a530-3849-b52e-1fffc2482908 | -9.1712 | -59.5987 | 2025-08-21 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 1778fc9a-6799-38ea-9383-b2e185973b89 | -8.0152 | -47.6656 | 2025-08-21 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |
| aea473ef-f2ab-3f19-9f08-d6a3cdfad227 | -7.0354 | -44.6167 | 2025-08-21 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.0 |
| da7e3cf7-ad5d-34b3-8a30-6bb3867a4518 | -8.8552 | -62.3933 | 2025-08-21 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 11d88347-2cd3-3d29-8f55-8ef149f56d74 | -5.2518 | -40.7296 | 2025-08-21 14:10:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 6a997c69-809c-396f-a2d1-4d116fd2c129 | -8.8737 | -62.3925 | 2025-08-21 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 86.1 |
| acd505d3-2d47-3265-8d82-896a73d6ea3c | -6.2924 | -43.8747 | 2025-08-21 14:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 22e4718d-bd71-3be4-bf88-938c5d951d42 | -9.7052 | -47.9609 | 2025-08-21 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 427.0 |
| 8d5ad68e-1aad-32b1-9508-4e1fd06d7be5 | -8.7567 | -45.4733 | 2025-08-21 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 93d96d1f-e81b-3e89-9bb4-637d4a3c89ff | -13.3154 | -54.4254 | 2025-08-21 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 5ecc8723-75ca-37d6-94dc-be358695be78 | -13.051 | -45.1693 | 2025-08-21 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 246.3 |
| 8e20c71c-4cc3-3376-8349-72cf2152c1fb | -7.6366 | -46.2823 | 2025-08-21 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 28eb4416-4753-336b-bbb4-4dcdfbd5b9dc | -13.3346 | -54.4233 | 2025-08-21 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 128.7 |
| b168b861-6941-3cf0-bd4d-0accf58c1ffa | -6.4529 | -53.3669 | 2025-08-21 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 91af6e67-7eb6-35df-af77-b5189096338c | -13.3349 | -54.4027 | 2025-08-21 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 086eada5-1748-3a45-abf6-9f64211265fe | -8.8551 | -62.4123 | 2025-08-21 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 40565b4f-3601-3170-86dd-e20944e8a6cf | -15.9187 | -52.2089 | 2025-08-21 14:10:00 | GOES-19 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| cb33a7af-e3ae-3737-a1e7-3ed85663d778 | -7.5832 | -44.3819 | 2025-08-21 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 18b1eea4-21da-3c6c-b359-7db4fc4d6adc | -14.9999 | -54.8343 | 2025-08-21 14:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 71429c3e-1600-3a01-a21e-ab377f2c05ca | -13.1369 | -54.8966 | 2025-08-21 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 93c6698f-6201-3c78-8e68-0fe5a216886e | -4.7152 | -47.2216 | 2025-08-21 14:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 6c9f2635-8400-3ed8-acc8-ab56f5a7c009 | -13.0317 | -45.1724 | 2025-08-21 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1010.0 |
| fa681f05-a938-36ce-b353-36790e911ef5 | -7.241 | -44.7126 | 2025-08-21 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 60571f5d-18dc-345d-b066-67147fb47845 | -11.6028 | -50.3739 | 2025-08-21 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 08f218a0-ad37-3782-ad65-c5354979a2ba | -8.6343 | -62.1367 | 2025-08-21 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| fbdbb1e0-9e7f-39c5-8f57-a4b7daa2ccca | -14.3127 | -52.0249 | 2025-08-21 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 78598a16-64c2-3d7f-b309-e999094e6218 | -15.0193 | -54.832 | 2025-08-21 14:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 43cf5f39-09ce-3aad-abde-dbe7542ce995 | -7.6296 | -45.2464 | 2025-08-21 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 47937cdd-5df7-3f89-904f-2451a2b5d3f8 | -14.7504 | -56.0151 | 2025-08-21 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| aff9e58a-c826-35c7-b6a6-09946a988330 | -13.0505 | -45.1925 | 2025-08-21 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 202.2 |
| f7393d5c-fdd2-3c90-bf22-e326e3d7cfa9 | -8.7759 | -45.4486 | 2025-08-21 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 88b9d01a-4a6f-32f5-ad7b-8cdabe3f5891 | -13.1555 | -54.9357 | 2025-08-21 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 218.0 |
| f0bdc081-e14e-382b-9dcd-8264bcf82ce2 | -13.1367 | -54.9171 | 2025-08-21 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 300.1 |
| cbcafc06-7bae-349c-9599-ab73fb31015c | -15.9183 | -52.2303 | 2025-08-21 14:10:00 | GOES-19 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| a4382a50-6ca6-3217-a302-d1f70d814c9d | -15.0189 | -54.8528 | 2025-08-21 14:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| e35b552b-21e7-3bfe-b0b9-f610599d7acd | -7.6369 | -46.2599 | 2025-08-21 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 866a76fb-3f90-3195-95ce-9b76f9733a2f | -5.4062 | -42.3761 | 2025-08-21 14:10:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 0cd416ab-f628-37f0-82ea-7e054f24b48c | -6.4528 | -53.3872 | 2025-08-21 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| cf32c8d4-6d12-3328-9d35-2a631378a4c5 | -13.0312 | -45.1957 | 2025-08-21 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 596.6 |
| 40e21e68-9b09-3e9f-9efb-237720cd7dbf | -13.1555 | -54.9357 | 2025-08-21 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 5a139729-ebaa-3e1d-be86-f984de900ad7 | -6.1 | -44.397 | 2025-08-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 7f65b51d-6bf8-32f6-855c-6f06862706a1 | -9.1712 | -59.5987 | 2025-08-21 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 75c86207-47a7-3cc7-8501-a9c04c0a8b7c | -6.2924 | -43.8747 | 2025-08-21 14:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 5d003257-08a9-33f4-bfe8-0684fe2f7008 | -8.7759 | -45.4486 | 2025-08-21 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 714e36df-8202-3193-8d39-9754fd94f74e | -14.7504 | -56.0151 | 2025-08-21 14:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 9927ed8a-6ea0-3d8b-91a7-68a9b2d4a78e | -7.6296 | -45.2464 | 2025-08-21 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 10cbfb66-f3a7-3938-886c-e3c3621cc839 | -8.8551 | -62.4123 | 2025-08-21 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 00c22505-456e-3e7c-873a-9917495141e3 | -8.4967 | -48.2342 | 2025-08-21 14:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| e898b59d-370d-3b32-b140-ab2ac2d00d17 | -8.0152 | -47.6656 | 2025-08-21 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 25ff883b-c774-3b48-b2c6-6e2371a5d39e | -13.1369 | -54.8966 | 2025-08-21 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| acfcc0cd-4a74-3e19-9d2b-46e2da20fcf3 | -6.2753 | -43.7139 | 2025-08-21 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| ca2873d9-50ee-395f-8ba2-7c1617ed9ef7 | -7.0354 | -44.6167 | 2025-08-21 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.2 |
| ef8ab3da-1494-3ca6-970f-3e02a88cfc4a | -6.4528 | -53.3872 | 2025-08-21 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 6646e27b-7e17-315f-8ffd-99795851d7b2 | -6.5386 | -45.5224 | 2025-08-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 0e54b4a8-6df1-30c6-a1d6-29d541588c3a | -8.6343 | -62.1367 | 2025-08-21 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 889151ff-3858-35ca-816f-3c458825f234 | -13.0515 | -45.146 | 2025-08-21 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 34c85a6b-b563-335a-ac05-9ef001d75c60 | -7.6293 | -45.2691 | 2025-08-21 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 2cc9e52e-521f-37a8-a29b-3551bc6ed749 | -4.7844 | -45.3057 | 2025-08-21 14:20:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e31749ba-15a6-306a-a8bf-7b11fd72b5c4 | -6.7997 | -43.8312 | 2025-08-21 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 8b5b19b1-5459-35af-b99b-3dc1a69cb83b | -13.0307 | -45.2189 | 2025-08-21 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 1f777df8-6958-379c-ac97-aa7545dcbdf6 | -8.8735 | -62.4305 | 2025-08-21 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 92c3e9c8-b183-36a3-ab3e-ed33587b0c13 | -8.8552 | -62.3933 | 2025-08-21 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 559082f0-350e-3679-b923-c9fcc2659850 | -6.4158 | -44.6695 | 2025-08-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 46653124-f663-3449-8c9d-fecc47e35d78 | -8.7567 | -45.4733 | 2025-08-21 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 1d4b5108-d1b4-39be-8118-0c15753cc451 | -6.7994 | -43.8544 | 2025-08-21 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 70d5dfa5-944c-363b-8915-56a480ae3d46 | -8.6901 | -62.0963 | 2025-08-21 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c0784f00-707d-388b-bb7c-34013f86cb58 | -4.7152 | -47.2216 | 2025-08-21 14:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| fdb598fc-5f52-375d-8c2d-ff6fcded9404 | -13.0505 | -45.1925 | 2025-08-21 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 205.5 |
| 2ff8fe27-b394-32bf-a89f-0d3b304f39b7 | -8.7756 | -45.4713 | 2025-08-21 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 79241154-919c-3920-bcfa-f355798348c9 | -8.6344 | -62.1177 | 2025-08-21 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| cd22f462-e566-3937-8d2f-d4a03182fa59 | -8.8737 | -62.3925 | 2025-08-21 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 42f692b1-7c0b-3fa9-aae2-0a29975562f1 | -13.1367 | -54.9171 | 2025-08-21 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 299.8 |


[Clique aqui para ver as próximas entradas](README65.md)
