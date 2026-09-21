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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4027360e-5a38-3ac0-a294-eb901c9e8843 | -5.8369 | -53.47597 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11939445-290c-3a73-b173-99957cfc0f0f | -6.34176 | -55.29763 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 102129df-38f8-372d-9edd-b3b047a824e6 | -6.75145 | -59.06504 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93214d49-c019-3e52-b393-7142c26c94aa | -5.21545 | -56.11042 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 823a3a5c-dbcd-3b4c-a4b7-68781c6c4139 | -9.55309 | -66.03593 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c7a235a-7ad0-3e1d-8fcf-d54097b8a72b | -8.17078 | -54.77013 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8835abea-5e11-3962-b5c9-0c138728995f | -8.79523 | -60.7995 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e9d4a0c-4708-3a3f-be3f-aa2c8a6ec382 | -10.73626 | -50.78336 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bed437c-a13a-3927-a893-77eba6ab9250 | -11.05022 | -54.15935 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e4ea376-6ee2-3954-9784-10512a68adfc | -10.46808 | -50.27864 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d797dc7f-bf54-3e2d-8495-651ba52cde36 | -6.3023 | -60.0133 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a5c5300-3d6f-3af5-8ce6-c25bb44dc365 | -6.00736 | -57.67673 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e8bf993-5ddd-37dc-992d-827461f4d58e | -11.8053 | -49.81513 | 2026-09-21 05:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 284347e3-8c32-3788-bf1c-8f6eef4fb710 | -10.41976 | -51.86419 | 2026-09-21 05:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 06ce3ba4-c830-3739-8154-eca58c209097 | -11.02 | -54.14236 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16504b43-9165-3754-a0c3-7ac6ad1ac345 | -6.30948 | -59.94449 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d697fae-5699-33e3-a329-f1698dc8767f | -6.20995 | -53.56063 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff826e59-3546-3d25-bba5-dcd994e27193 | -9.55449 | -66.02747 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 142d0505-64a4-3dd6-a8b3-c8e4351ca9cd | -9.67992 | -54.33797 | 2026-09-21 05:42:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76bea760-2a7f-3cbd-ad7c-aa8a7e5f792c | -6.46527 | -59.99036 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3345e81b-f999-3151-92bc-3024e0497f43 | -10.47482 | -50.2795 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0afdf5e1-ac6c-3cbf-bbbb-c717b9f04471 | -6.72492 | -55.07421 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7011ccb6-11d6-3bdd-b027-7f3672ff45e1 | -6.15395 | -57.7925 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 099cd808-c179-3c27-b8b3-eb7635a78b45 | -9.97229 | -50.2622 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc584d2e-781d-3644-8f5a-3cba4349b537 | -9.18768 | -60.76637 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9296e6dd-df97-3e97-9243-3a305f582e69 | -11.03105 | -54.1403 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69c62371-a41d-32ae-b044-44533878c2d9 | -11.03091 | -54.15054 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d6b4096-4340-36f4-8c45-07f9f840b2b1 | -5.82476 | -55.70867 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f8e37b2-a2b3-3a91-8a6d-c5033ede980c | -9.55882 | -66.02385 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68514996-b1ce-398f-bc00-e0faf380b41c | -5.85612 | -53.48848 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| db68be3b-3bb2-3bfb-9d1f-42eec205b202 | -10.76568 | -50.81527 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a437fde2-d59d-32f8-a39e-8657304d3273 | -6.44389 | -59.96757 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 752b7290-765b-3ad8-869d-4f13a079606b | -10.8783 | -54.09446 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b318cbb-06d8-3326-b587-64e1799986a7 | -7.24774 | -55.61147 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 15e01321-fde1-3302-bad3-6459c21849d9 | -6.44909 | -59.98004 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93e8ad6a-4069-3071-a30d-8ba2c4823a89 | -5.97882 | -57.78614 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5193fd6d-d53c-3d15-9604-6180cbc790c7 | -9.03252 | -61.65831 | 2026-09-21 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb081897-d3ac-3c62-ba77-700a66738d33 | -6.1363 | -59.95379 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e706fbe-dc24-3ab1-8797-e8cf986ea32b | -9.17207 | -60.30404 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd07317d-f644-32e2-a9bd-fa4e515b1644 | -5.83602 | -57.54443 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 640d2c39-5b2c-3780-9978-071b8d5943bf | -5.89779 | -52.09249 | 2026-09-21 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 359fc362-1afb-3967-a6f1-2b95cb9a7be7 | -8.2341 | -71.04966 | 2026-09-21 05:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3c3bbf2-af4b-301e-9789-e99ae198fbdf | -6.74583 | -59.42397 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7ea7b82-7068-3608-a8f7-75039d041bc5 | -10.67145 | -58.83416 | 2026-09-21 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b923d488-2d05-3dd2-ad65-656f19e0eec8 | -6.07864 | -57.63015 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12b6356f-69e8-35a6-a475-fefae5a97209 | -11.12984 | -54.00443 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a720f990-4410-34ef-b48a-d9892b575fd1 | -10.20564 | -53.91497 | 2026-09-21 05:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6fe0520-3262-35c7-87d6-9d1f5f5101e6 | -6.04122 | -53.27831 | 2026-09-21 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b9b7422-1568-3ad3-b887-daacbc8b6c3e | -9.02626 | -49.82612 | 2026-09-21 05:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 283d9cd9-d03f-38ec-b1f1-d3b27816b625 | -6.41564 | -56.10482 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ee5f9c8-de0b-3def-adfa-5ec0edc46ec3 | -6.30312 | -59.93964 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e11261d-612e-3f80-8484-681c86091cb4 | -10.8681 | -54.08973 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4357c5d1-905e-3e44-9492-2ff4e7127e95 | -5.83472 | -53.49118 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d4685a6-c0dd-3bfa-96a3-01d4ac48e5fc | -7.58875 | -57.66843 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25f09eef-6558-3d93-952b-7b4396f75bb8 | -10.37957 | -48.91915 | 2026-09-21 05:42:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 72dff726-f3aa-3328-9325-781389c52ebf | -9.28156 | -60.62841 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ced1c0e0-175a-35c3-9e08-a93eedbb6d43 | -7.99717 | -70.90743 | 2026-09-21 05:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3af8322b-a18d-348c-b584-d471ba74de09 | -10.80386 | -50.77488 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 9c2142e2-aef6-35fa-b499-2f008ba08079 | -10.74149 | -50.7953 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee771cba-54f0-33d4-b314-baf82ba7362b | -9.03755 | -61.6481 | 2026-09-21 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3265677d-5907-367a-80ac-5db328109fb4 | -6.9594 | -71.75777 | 2026-09-21 05:42:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27ceaab0-7309-3fe0-a512-de909c346a6d | -9.12372 | -58.91938 | 2026-09-21 05:42:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b642476-4dad-3202-9488-07ebaacede5f | -6.19554 | -57.77906 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afcb8c94-d42a-3f97-91c1-7201349f6c2c | -10.39687 | -50.22164 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50bb727f-9b40-39a4-80c7-7f6637c126d2 | -9.5552 | -66.02322 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d9f95dd-30c9-3790-b905-38a77d14084d | -5.82566 | -53.5178 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c43357a-d3dd-358a-bb18-7a4156d2edda | -6.38169 | -60.01721 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0bc6dd8e-cdba-3914-bef1-869c7a79f3a7 | -10.8712 | -57.16317 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f934b3c-2109-3870-8e7e-2ad539bdaa38 | -8.18457 | -54.76213 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba243b6d-c69e-3876-9673-544cfc2dcbc3 | -6.19627 | -57.77421 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb273feb-599c-33f6-bc3c-e1a448776005 | -11.13519 | -54.00521 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28434d3a-d2c8-3a96-982e-0bec56b9eb56 | -6.1566 | -57.95816 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0122b61-21c4-3267-b707-9091b2c39986 | -8.86752 | -68.80911 | 2026-09-21 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b430d00-0044-3968-8f6f-8a11f17d93a1 | -10.09093 | -50.26536 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c0183196-cb6f-3fc1-88e2-69b44acf2eaf | -6.99095 | -61.35163 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e845acd7-adc6-3f89-acac-d27c73270c5f | -5.84355 | -53.53902 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24e5c8be-0872-3ff5-82e0-007d251bd89c | -10.45964 | -61.31435 | 2026-09-21 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca99d9e1-0d16-3db4-af14-9fab646c4f4d | -8.16846 | -54.77084 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f51b3b9a-562b-3eb2-bfe8-df5ff5be6b09 | -7.12277 | -48.43908 | 2026-09-21 05:42:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 08840a58-d26a-3b68-8fcb-ee2f3694af37 | -8.85535 | -62.36145 | 2026-09-21 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad95d23b-68ce-3ec3-8d66-1adb8485ed99 | -7.58558 | -63.04349 | 2026-09-21 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 462a499a-d8b9-30e7-86d0-6c2c933057fa | -9.02551 | -49.83231 | 2026-09-21 05:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a31dbc7-fc00-3613-a72d-872fb2c3e7dc | -6.31211 | -60.01863 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 555a92b5-7b7e-3b54-ba14-c6b101df9a8d | -9.61357 | -65.36398 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f9d3ae1-2e67-390a-b232-484e4462c043 | -5.87865 | -53.63673 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4eb9fd57-69cd-3ac1-a10e-2bdecf248810 | -6.72421 | -55.07903 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8bbad25-7c12-35fe-afaf-93389bbddae7 | -7.886 | -62.53968 | 2026-09-21 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ce9399a-bc82-3340-8a4d-26c8f8b6cef6 | -6.72582 | -55.08097 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 091d271f-3fa2-396b-814a-81c477ac1fff | -7.86284 | -62.53947 | 2026-09-21 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2eff484-2649-3075-80d3-c20f0f585732 | -6.72915 | -55.09129 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26abb7e9-e1e1-3667-8adf-96882ff03019 | -8.53882 | -54.69415 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01acac1b-ebfe-34c4-883f-fed8c5b8e153 | -6.99485 | -61.34863 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3484d5e-d188-3298-a685-8f5f622cd156 | -6.1577 | -57.71409 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e2ba1f0-9549-36a8-b5a8-46919b277670 | -7.54696 | -61.31795 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38038fc8-0623-3c5f-a1e9-4217f929202f | -10.08566 | -50.25269 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e5a8631-83da-32d5-800f-b3f750c0b0fe | -6.41425 | -55.01479 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce702204-75ce-396b-b1f2-6950cf670b32 | -8.17333 | -54.77156 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c439ac2b-14a4-337f-9723-8f2a4e4cb7dd | -6.96417 | -71.75878 | 2026-09-21 05:42:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cdfce34-c99a-33de-a491-46e36ceb3330 | -6.35107 | -57.88948 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04e645a5-4e09-3d0f-8e98-483313081bc2 | -5.87676 | -53.63317 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README95.md)
