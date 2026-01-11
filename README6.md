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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53368e27-3e25-3adb-b2d2-36451c6093bd | -2.97178 | -54.33185 | 2026-01-11 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b346b2e-7c58-3489-91dd-7fa38ec118cf | -2.87135 | -45.21211 | 2026-01-11 04:38:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbff4850-f7b6-325b-b29d-20311ae70946 | -2.86791 | -45.21158 | 2026-01-11 04:38:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b231222-419a-3e6f-9833-f8ab7e7d1d3f | -4.14115 | -38.2715 | 2026-01-11 04:38:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 843b5e79-f0ac-3a69-8bf2-3f953f0285a5 | -3.55621 | -43.65469 | 2026-01-11 04:38:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e207592c-c845-3318-8d1b-7ffc2fde04d0 | -2.0712 | -54.37006 | 2026-01-11 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6d460a9-e090-3688-81c4-1ea14e57bcef | -4.40757 | -40.6949 | 2026-01-11 04:38:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11fc3be7-8c7f-3082-9e45-d2d058c41548 | -6.63877 | -46.54202 | 2026-01-11 04:38:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f12dfaea-a807-310a-8b41-6e505cee6aba | -3.55926 | -43.65969 | 2026-01-11 04:38:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fddc016-3b9d-3f1e-9dfa-dd2bd0826719 | -5.49746 | -40.73739 | 2026-01-11 04:38:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6c5c3279-57cb-3109-bb6f-af52ce0e5a36 | -9.47444 | -46.07763 | 2026-01-11 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4292b038-1819-3f72-96ac-5bb764537b4f | -1.62425 | -55.37858 | 2026-01-11 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aeb6a7e6-293b-3bd2-8f17-6f5e45f06460 | -9.04477 | -46.9936 | 2026-01-11 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07945349-ca3b-37be-b49a-d8f97bb3c9d3 | -6.76471 | -46.67237 | 2026-01-11 04:38:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c5380aa-73b4-3445-89fe-32bf735a97c0 | -3.94028 | -40.70077 | 2026-01-11 04:38:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 80557af5-3561-3806-9558-275a22cc1271 | -6.68669 | -44.70492 | 2026-01-11 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5baab1b-2f4d-35ce-bace-e69b040b36e8 | -7.5958 | -45.8871 | 2026-01-11 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9c8f090-eef8-3436-acf2-d1454d025c34 | -4.07024 | -47.12069 | 2026-01-11 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4351fa28-94ae-30cf-b740-fc1c26106d04 | -4.81742 | -45.23609 | 2026-01-11 04:38:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f81acab2-a249-350b-a662-ac368ff8ccff | -2.87077 | -45.21584 | 2026-01-11 04:38:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88dcec3e-6b2b-3e9c-9a62-fda24bc7fbe6 | -4.14164 | -38.26816 | 2026-01-11 04:38:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 86a891ae-f601-3a4e-b768-567d5c51b0b9 | -3.94057 | -40.699 | 2026-01-11 04:38:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7383ab02-db2c-3809-b21b-d4162f137923 | -9.47797 | -46.07816 | 2026-01-11 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e07ed1c4-2ccc-37f7-8b9d-1da0ea808b3b | -5.2467 | -37.5 | 2026-01-11 04:38:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6b3794e9-fc2b-3b83-8531-0721b3bcf689 | -7.3744 | -42.79695 | 2026-01-11 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c541ba2-49d7-36c8-951a-d7b1b5033c13 | -5.49798 | -42.16292 | 2026-01-11 04:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8330e4c5-7573-3e72-aea7-4d9454a3c637 | -9.97265 | -36.36488 | 2026-01-11 04:38:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 68eb988d-d9f5-3a44-9561-ccb452a80ed2 | -9.04421 | -46.99728 | 2026-01-11 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97ecc929-5d5c-3ce8-bae0-b6ccb2af0862 | -4.65104 | -45.79523 | 2026-01-11 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b6366665-10ce-3ff8-ac78-65f51c7e1ebf | -5.12932 | -46.12606 | 2026-01-11 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66a6392e-d3b8-3826-9d15-462d5a20ba2f | -2.06644 | -54.36935 | 2026-01-11 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22f7ad09-71de-33f6-a26d-6c2bd448cf9d | -3.71165 | -47.2059 | 2026-01-11 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5380cd46-bcce-316d-a000-457927f15b53 | -5.49914 | -42.15511 | 2026-01-11 04:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c0ec272c-4dee-3047-8802-6654ebf0befb | -5.28789 | -45.82663 | 2026-01-11 04:38:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 893bdb6c-c43e-3b02-9f4e-a693d91b3ccc | -5.49856 | -42.15902 | 2026-01-11 04:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 00f110a4-c240-340c-92e5-418be04b65d1 | -1.29605 | -53.69544 | 2026-01-11 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e78ae39-016b-35cf-9cca-ddd9a50c18c8 | -5.8563 | -44.94754 | 2026-01-11 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f73230c-90e8-347b-aa10-1e7150edc13e | -2.1906 | -52.01564 | 2026-01-11 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91bc0a7d-cfbf-3086-8152-bdd987391bb5 | -3.55552 | -43.65916 | 2026-01-11 04:38:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9424bb23-a687-34a9-a39c-dec8bcced1e1 | -3.93601 | -40.69832 | 2026-01-11 04:38:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0087f852-5cde-377d-a3ff-3a0335fa575d | -5.23632 | -43.85834 | 2026-01-11 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea0eff5e-37d2-3d99-884b-294351db00fe | -9.05157 | -46.99469 | 2026-01-11 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef55f6e1-0261-3832-933c-bae288940b8d | -7.41422 | -48.95057 | 2026-01-11 04:38:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52d887f4-2f8d-3f10-90e5-ccfe7eb2865c | -2.86849 | -45.20785 | 2026-01-11 04:38:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 471ef599-ffc7-37aa-be62-c2e80c395a98 | -7.41088 | -48.95004 | 2026-01-11 04:38:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 897f38ef-91da-37b1-b852-96b036dc4fc2 | -9.04533 | -46.98993 | 2026-01-11 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c331d0a3-3e2c-38dd-a04e-0caf924ac407 | -5.52817 | -42.85129 | 2026-01-11 04:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aa0f8421-5739-34fc-bcf8-43a234261367 | -5.5287 | -42.84776 | 2026-01-11 04:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e9b238c5-2f7c-338d-8ee1-71abbfeb674f | -3.94096 | -40.69611 | 2026-01-11 04:38:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 220de269-78eb-3a8a-9e91-eaa0420d9208 | -7.49079 | -45.58281 | 2026-01-11 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4ece7b6-46a3-3395-ac5d-f11140b68d05 | -3.46166 | -49.86528 | 2026-01-11 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efe43638-53e9-3562-9125-f1a56122fa76 | -2.93621 | -52.30993 | 2026-01-11 04:38:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec46f6a5-e4a4-3d70-973b-cc0ac272a022 | -2.18714 | -52.01145 | 2026-01-11 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d76e7f9-7cff-3fe4-9432-26af33957189 | -5.24611 | -37.5041 | 2026-01-11 04:38:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 517c3625-ef3a-3203-b03a-0ed5bff81207 | -2.89028 | -45.22651 | 2026-01-11 04:38:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a90f068a-e6e4-328f-8519-d4b568f1c858 | -4.64821 | -45.79094 | 2026-01-11 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f26ba95-40bf-3a5e-8500-a11f620da732 | -5.49434 | -42.15841 | 2026-01-11 04:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 36742d93-785a-3ae4-8d90-6d11d5684567 | -7.59522 | -45.89096 | 2026-01-11 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae1d18b1-abe7-399e-9d1e-3bbb3ca08614 | -2.56632 | -45.845 | 2026-01-11 04:38:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 440f596a-c1d9-3218-99d8-58da241402c2 | -5.293 | -43.74044 | 2026-01-11 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07efe3a8-ad96-37dd-8af6-2036d7720872 | -4.26042 | -48.84177 | 2026-01-11 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d8c45b2-44fa-3f1f-be13-856a05f52cdd | -5.46157 | -45.28669 | 2026-01-11 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3f12e81-2f90-3762-8c68-7236ceed16ce | -6.64397 | -44.68994 | 2026-01-11 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf74c68e-c444-32f6-9740-9a8280a61ed5 | -3.49623 | -41.70969 | 2026-01-11 04:38:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 841ed463-6693-3afd-8135-c2661389dcdc | -7.49139 | -45.57883 | 2026-01-11 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf8d44c5-63fb-3faf-ae2c-6bd4d6a1500c | -9.05101 | -46.99836 | 2026-01-11 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92090612-9b85-3e9d-acd0-e2a369e93d1b | -9.04817 | -46.99414 | 2026-01-11 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d3a6675-1c5b-351e-87d7-86f930e9c098 | -5.17884 | -44.75506 | 2026-01-11 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e511847a-b09d-3176-9242-b89db64c627c | -5.28446 | -45.82607 | 2026-01-11 04:38:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e62b3644-5e4c-3b2b-8ffe-f81176fe3113 | -3.91585 | -45.00921 | 2026-01-11 04:38:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac9ef06e-0a5e-3a3a-ada1-1e7e14234c83 | -2.56688 | -45.84143 | 2026-01-11 04:38:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdc731d6-0e00-3da5-9325-63059218970c | -2.90665 | -46.7356 | 2026-01-11 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b694a71-c5a1-392d-9217-d867ab8e0db6 | -2.87072 | -45.23874 | 2026-01-11 04:38:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7dbeed5-0d1e-3699-b8a4-d7e689c5bb5d | -5.01699 | -41.87281 | 2026-01-11 04:38:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 207433ca-a5cf-3ae7-a5bb-3e5e12708f39 | -3.67597 | -42.05969 | 2026-01-11 04:38:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3a2e2818-1a55-3054-a2f1-8fe60d624226 | -4.70618 | -44.48275 | 2026-01-11 04:38:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7c30022-bcb3-3b7e-8894-6563625791a3 | -5.12989 | -46.12239 | 2026-01-11 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70fe57c3-7a42-3786-b961-a0fe442c25f9 | -4.70681 | -44.47859 | 2026-01-11 04:38:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04502d30-44bc-3911-9aa0-1fb7c668564d | -4.65162 | -45.79152 | 2026-01-11 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27497283-828c-387d-9e18-4d8ca34111f5 | -7.37856 | -42.79753 | 2026-01-11 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 747154ec-1a60-3065-98e8-33caaaad707f | -2.8713 | -45.23502 | 2026-01-11 04:38:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b894734-39c0-3778-b1c4-b3579bd82028 | -12.90753 | -52.52773 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93e15d86-57fc-3a35-93bc-23a44530ec37 | -12.90825 | -52.52354 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 728ca63b-bfd0-3dc7-8f27-ef61e5ef0de1 | -13.6695 | -53.94931 | 2026-01-11 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01f30449-e284-323f-a04a-6c4b957c7e8c | -12.91005 | -52.52982 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a2a69c93-5908-3ba6-8b9f-ae5bfd6dd7ad | -13.66654 | -53.9437 | 2026-01-11 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bac4386-530f-37af-9a7b-979297394e15 | -12.90716 | -52.52498 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 00469d6d-e21a-30f1-a74e-eac0c1a64173 | -13.4309 | -43.85563 | 2026-01-11 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c2ae05a-ca71-302f-a4e4-4f50c21332e4 | -16.09939 | -56.7568 | 2026-01-11 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d349813-6f6f-323f-8954-b1c62b9eea92 | -12.91471 | -52.52902 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 222521a2-0056-35bd-901a-3a8dba291a92 | -13.40982 | -43.75493 | 2026-01-11 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e133ac14-a50f-379d-b0ba-0c49b8366569 | -10.76938 | -45.01638 | 2026-01-11 04:40:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c703d034-97d2-317d-9095-7dd1def11fe4 | -13.62471 | -50.62661 | 2026-01-11 04:40:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29e56216-c3f9-3b50-9367-d435021ae95d | -12.90287 | -52.52853 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b08d913-923d-3349-9d68-2ad7cf32b6af | -12.91364 | -52.53047 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 32452d5a-4919-385d-8a47-e49b545f993d | -13.67036 | -53.94443 | 2026-01-11 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b865e95-d16d-3d83-9636-104cd733da00 | -12.91039 | -52.53257 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea029090-70fc-35a9-9b15-639cf72c140d | -15.9141 | -48.83036 | 2026-01-11 04:40:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6b3fd7b8-e77c-3b5f-b7c6-2e9bbc5f179f | -12.9068 | -52.53192 | 2026-01-11 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8640d710-1728-39fa-9b97-8eda12a61caa | -13.4403 | -43.6892 | 2026-01-11 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README7.md)
