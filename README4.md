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
| 847aac58-53a3-312a-8be7-ebffc374ae11 | -6.2863 | -53.3555 | 2026-08-26 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 41a585fb-5135-3ac9-80f1-c8830c261870 | -13.2839 | -51.4755 | 2026-08-26 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 3ac745aa-ba51-3438-a54a-b4320658469b | -6.6225 | -58.5189 | 2026-08-26 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| c9d95f5d-ff55-38de-aba9-33597b1d5028 | -6.6226 | -58.4995 | 2026-08-26 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| b9a19551-2104-3e06-8367-f224ed8b4830 | -10.7784 | -54.0368 | 2026-08-26 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 190.5 |
| d2beff35-3f65-3cb6-946e-3841640fc212 | -7.5104 | -61.3832 | 2026-08-26 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 50326afe-3144-3561-8f2e-beef27ff67fa | -6.2676 | -53.3768 | 2026-08-26 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| da551602-8475-327e-90b4-e3954c9da549 | -13.2469 | -51.3949 | 2026-08-26 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 6c0a836a-43da-3962-94b1-d85a2169c677 | -6.2675 | -53.3972 | 2026-08-26 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| ca4323cb-4350-3afd-a41e-e224919a8e02 | -6.2491 | -53.3778 | 2026-08-26 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 4f577854-a5fa-310b-b001-55b50502b866 | -13.2647 | -51.4779 | 2026-08-26 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 018bfe35-3b56-34cf-9652-f80da20fdb9d | -15.6742 | -53.8955 | 2026-08-26 01:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| c3f83cbe-c162-39f5-8f49-749126422950 | -7.5289 | -61.3825 | 2026-08-26 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| abf68b43-1d3c-3684-8b9d-0c21f41e1bba | -13.2451 | -51.5016 | 2026-08-26 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f58c7efe-978d-3a8c-a891-8dad6c69437e | 2.58 | -60.6973 | 2026-08-26 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 803f4166-a2ee-328d-96dc-18ed5963af08 | 2.5983 | -60.697 | 2026-08-26 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 03ababd2-bfbc-364a-a8b9-db66cabb8118 | -7.3034 | -49.5414 | 2026-08-26 01:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 06fd20eb-5462-3b9f-8ccf-ccca87d35fe7 | -7.7481 | -44.7561 | 2026-08-26 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f4985395-db12-3512-ae27-4c13c9650af1 | -13.2835 | -51.4968 | 2026-08-26 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 154.3 |
| f526c3fe-ca64-356d-8c56-35859c742d1b | -10.3727 | -45.0537 | 2026-08-26 01:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 24c84e7d-6305-3f59-8c22-289f78d094b7 | -10.7596 | -54.0384 | 2026-08-26 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 298.9 |
| 29f0a2f7-da25-3e6a-b928-1b56fc411a63 | -13.3027 | -51.4944 | 2026-08-26 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 38f3e176-1daa-3846-af62-99512862eb9a | -13.2465 | -51.4162 | 2026-08-26 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 8c1637a5-6a86-32b2-b04c-438938751ddd | -11.4302 | -44.5382 | 2026-08-26 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 525d3dae-dcbb-3cc1-854f-9def333ddb95 | -9.6024 | -55.1078 | 2026-08-26 01:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| f8f3c247-40bd-30a7-9e69-c68d639e4b14 | 1.4918 | -55.9443 | 2026-08-26 01:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 65c9b0d2-1427-387d-8734-54800d9977b9 | 1.4734 | -55.9642 | 2026-08-26 01:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b3ebf8c8-4657-3393-ac1a-a8990289b891 | -6.2677 | -53.3565 | 2026-08-26 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 8a93d5c4-4a97-305d-a075-fc29656ababb | -7.767 | -44.7543 | 2026-08-26 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 604b0476-534a-319f-833f-b119ebf35bea | -6.6409 | -58.5181 | 2026-08-26 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 97c03c2f-4272-3865-b5fb-e919cfa86994 | 2.5983 | -60.697 | 2026-08-26 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 57fb53e1-4391-348e-902f-bf1f80104f53 | -15.6742 | -53.8955 | 2026-08-26 01:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 4d124539-f4b6-3d6b-a5e4-46a352b75cff | -13.2839 | -51.4755 | 2026-08-26 01:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 23ce58f9-20b3-38d8-a8f2-a42ff8fbc794 | -6.2491 | -53.3778 | 2026-08-26 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 75314de7-430d-3e48-bbbf-317711763e26 | -10.3723 | -45.0767 | 2026-08-26 01:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 978ddb2d-e948-30e0-a23c-9f3d51b2daea | 1.4918 | -55.9443 | 2026-08-26 01:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| fbe6d943-52f3-3158-a090-9b2c21cc1eb0 | -15.6936 | -53.893 | 2026-08-26 01:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b3a4ba1b-cc0c-34e1-b054-a2d875652842 | -9.6022 | -55.128 | 2026-08-26 01:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 4117c462-c58e-3edd-a8b5-44061b53bdd8 | -10.7787 | -54.0163 | 2026-08-26 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.4 |
| bdaf3e4a-0e6e-37f2-ae15-7315f6735166 | 1.4917 | -55.9837 | 2026-08-26 01:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 0c81493a-8b70-3530-8667-96653e902cdc | -13.2465 | -51.4162 | 2026-08-26 01:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 536159de-4833-3fea-9286-d7fed02a8163 | -13.2277 | -51.3973 | 2026-08-26 01:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 219.1 |
| d30e26fd-977b-3996-8f71-2620022891a5 | -13.2469 | -51.3949 | 2026-08-26 01:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 8edc67e4-82e4-3706-b16b-87d9e3c912ed | -10.7784 | -54.0368 | 2026-08-26 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 210.5 |
| f13c7c3c-faf6-323c-bd2a-00825e8e21d4 | -6.2676 | -53.3768 | 2026-08-26 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 181.2 |
| ea9442c7-7197-380b-a022-a5eb73b3845d | -6.1286 | -57.8198 | 2026-08-26 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| aea779d6-391a-3fbf-83ed-4a99113602bf | -10.7409 | -54.0196 | 2026-08-26 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 84cd3d21-ee3f-3796-9c05-ac746fe4a9e0 | -9.6024 | -55.1078 | 2026-08-26 01:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| b388c3ef-ead6-361b-97af-45ed91486240 | -10.7598 | -54.0179 | 2026-08-26 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 222.6 |
| 5f4fc099-cbcf-34c6-b283-e16737008cbd | -9.0304 | -50.7817 | 2026-08-26 01:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 4cf4dba9-4781-38fc-8b10-3df2b89377e1 | -10.7596 | -54.0384 | 2026-08-26 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 338.2 |
| 0e95344a-619b-33fd-807c-6f57b0841e3b | -10.3727 | -45.0537 | 2026-08-26 01:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 50e88962-7d0d-3712-bce8-c55c3dbd73ca | -13.2835 | -51.4968 | 2026-08-26 01:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 6e97685e-3666-35ed-9419-613ceb977bdf | -6.6595 | -58.498 | 2026-08-26 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 09757295-7814-3e39-9dd0-05294a27df66 | -6.6226 | -58.4995 | 2026-08-26 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 1c7cb7e6-591d-3360-94b1-f5156acedd9c | -6.641 | -58.4987 | 2026-08-26 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 62c5007d-bd39-3007-81a7-f377e8997005 | -6.2863 | -53.3555 | 2026-08-26 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| efb415af-24d2-31ca-adc6-8ec129314127 | -6.6225 | -58.5189 | 2026-08-26 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 68c6502f-9d7e-33d2-8904-137c8f6a541d | 1.4917 | -55.964 | 2026-08-26 01:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| afdfae34-9bc7-3ec0-84e7-0f1522e2a98c | -7.5104 | -61.3832 | 2026-08-26 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| b1114ce8-4648-3588-9a8e-2d62f4a6cd39 | -7.5289 | -61.3825 | 2026-08-26 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| e5b2114b-2790-364c-b377-9d1a4ac8ae3b | -6.2861 | -53.3758 | 2026-08-26 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 5926014f-d8f7-314b-a6f8-25f8ed7d46c9 | -15.8797 | -48.3379 | 2026-08-26 01:10:00 | GOES-19 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 20306f24-78ab-346f-a82d-50a3fdfefcdd | -13.2273 | -51.4186 | 2026-08-26 01:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 48cbfb28-9f96-3dc2-a344-6dd6eb647865 | -7.08 | -59.17 | 2026-08-26 01:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a74d6bd-7687-31a2-8a46-bf38ea70bc6a | -7.05 | -59.24 | 2026-08-26 01:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a07652c-28a4-3d09-9dd2-e8d5030b37cd | -10.77 | -54.04 | 2026-08-26 01:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86ff9e7e-9a09-30dc-9713-c538a15d50de | -7.08 | -59.24 | 2026-08-26 01:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80ff43b6-6de1-3199-91b3-b4f1451e2fc8 | -6.2861 | -53.3758 | 2026-08-26 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b41f556e-2ede-327a-9031-4b4e7601b672 | -13.2835 | -51.4968 | 2026-08-26 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 30f8c73d-b843-381f-a4a5-10d874dc796b | -10.7784 | -54.0368 | 2026-08-26 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 231.8 |
| b2c4ec35-b5e0-3bdc-8e43-8ef08c03a79b | -13.3027 | -51.4944 | 2026-08-26 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 097991ef-f5fc-3692-886d-bf77db3da940 | -10.3727 | -45.0537 | 2026-08-26 01:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 136.3 |
| b4332231-4aae-395d-a1d5-3c2d663d198a | -6.6225 | -58.5189 | 2026-08-26 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 49d7321c-619a-3e29-aca4-ac1d02a7504a | -10.7787 | -54.0163 | 2026-08-26 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| e60a0260-cadc-3afe-98ee-4ea866098b84 | -7.767 | -44.7543 | 2026-08-26 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| e842b886-e6b7-33eb-8199-a61352081a83 | -6.6409 | -58.5181 | 2026-08-26 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 121.8 |
| afdecd52-939d-37d2-a4f6-1390396dcd92 | -7.5288 | -61.4015 | 2026-08-26 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 9b02f305-4b3f-3f3c-a0ce-120351c921b2 | -9.6024 | -55.1078 | 2026-08-26 01:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e7dffa1c-a842-3c44-b13b-019e5087a522 | -11.4302 | -44.5382 | 2026-08-26 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 9ab42cb1-aa05-3bca-935b-90a90a518e31 | -13.2465 | -51.4162 | 2026-08-26 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| ade99004-6524-3a80-b3df-6a4e45b867a9 | -9.0302 | -50.8029 | 2026-08-26 01:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a762c8da-b391-33e0-b25d-55fd0cc4f1a4 | -7.5289 | -61.3825 | 2026-08-26 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 224.2 |
| 992a60a0-a39d-3a8e-a998-7c9122487a80 | -7.529 | -61.3635 | 2026-08-26 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 957a8c62-2614-37f4-8819-b3369958fd6a | -13.2277 | -51.3973 | 2026-08-26 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 46438da3-120d-3373-8bb7-d52bfa8fddbc | 2.2333 | -60.7018 | 2026-08-26 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 88b31181-c65a-37c4-8b21-9fcc2d38bc69 | -6.6226 | -58.4995 | 2026-08-26 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| f844d450-f8dc-3c49-8fc0-4b9b8a54d759 | -10.7598 | -54.0179 | 2026-08-26 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 181.9 |
| 89cc1388-3415-354c-9c33-01369fc064ff | -6.6595 | -58.498 | 2026-08-26 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 011771a1-a4c7-37fa-8a26-12f9dcac738e | -2.5042 | -48.1366 | 2026-08-26 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| e76846b5-1504-33c0-b553-8cd61a99b076 | -9.0304 | -50.7817 | 2026-08-26 01:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 00925394-2ca2-3898-8836-35510db6bf32 | -10.3723 | -45.0767 | 2026-08-26 01:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| be41627d-e0ee-3bd5-9696-ca07d41ad69b | 2.58 | -60.6973 | 2026-08-26 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| a7b29d3d-2ef1-3283-8ed7-3abb1b293bdc | 2.5983 | -60.697 | 2026-08-26 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d485a769-efed-3a82-81cd-859cd077485c | -6.6594 | -58.5174 | 2026-08-26 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6d827db1-49c8-3b59-89fe-f312726a6f23 | -6.641 | -58.4987 | 2026-08-26 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 0cccfbae-30a0-354b-96a2-d93af78fed48 | -6.2676 | -53.3768 | 2026-08-26 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 166.5 |
| bfdec5ad-725e-3b67-9666-f14e32747acb | -13.2839 | -51.4755 | 2026-08-26 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 108a1b2a-3a5f-3f0e-a84a-a5472d059dad | -7.5104 | -61.3832 | 2026-08-26 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 150.2 |
| d8d3b27b-aa59-3d88-bb9d-d42f7ffd7439 | -13.2469 | -51.3949 | 2026-08-26 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |


[Clique aqui para ver as próximas entradas](README5.md)
