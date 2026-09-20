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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35a41c0c-34dc-3324-b99a-032476cf531f | -8.23811 | -62.84323 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bec9883b-20af-3f7b-927a-434892dbf506 | -10.87777 | -54.09352 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5cf8657-4676-3525-b276-14bf16d12976 | -11.2259 | -54.06648 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| da865720-de9a-3812-9caf-1156148fdb12 | -11.23224 | -54.07485 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3a41dbc7-e6d3-3487-b23e-29868ef10d87 | -8.20068 | -62.85597 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33fba64d-5d10-3425-9f69-d02577c19298 | -11.09513 | -54.02255 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4edf7ef3-c3f2-3f4d-8f5d-64f32d6ed315 | -11.11064 | -54.02994 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 20665e57-aceb-36ca-8bcc-26d5adfc3d5b | -8.85776 | -68.51132 | 2026-09-20 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63cefc8f-7751-3b19-8bc3-a736776cb4af | -8.64446 | -62.49098 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 94f8c70c-ffb6-390a-af60-e1e3d4066f06 | -11.13378 | -54.01872 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 65402bfd-59b6-3b74-88bb-5631a6d20f83 | -11.10149 | -54.03045 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 2672c64d-c354-332e-9384-f07cd181045b | -9.03298 | -60.3653 | 2026-09-20 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fb31fc9-4ad3-3482-b28b-bc816cc035bd | -8.85647 | -64.23228 | 2026-09-20 06:01:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7265a7fd-a6a1-3b60-a9c3-8bd7da35dc4e | -10.87859 | -54.08662 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f90d80e-163d-37e0-9a1a-ef7efa26d997 | -8.60924 | -54.59607 | 2026-09-20 06:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| deb3616c-8257-350c-8486-57fce1b1d54b | -8.17673 | -62.80188 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45ac313f-0530-3a6f-bf47-c9ae19d92efe | -10.86211 | -57.14783 | 2026-09-20 06:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 696e3bbd-607c-3080-a204-84d075c450c7 | -9.1982 | -60.75557 | 2026-09-20 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3696e58c-f609-3fd2-87d0-1a12d5a84868 | -9.93205 | -60.73204 | 2026-09-20 06:01:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18cc3135-2f5f-3d76-bb05-4f95715cacac | -8.80098 | -60.79682 | 2026-09-20 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c39fb592-92b9-3045-bcb8-a2c7e133d621 | -11.21517 | -54.07118 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cc2a3abe-d285-34ba-bf4c-1a5714448e08 | -10.87407 | -54.08404 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 185838ae-545d-374e-895d-893c29f6dd3f | -11.05003 | -54.15963 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfee091e-1a31-3a47-b0ee-64a7b60d2555 | -10.87945 | -54.07937 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 202d15d6-624d-3b17-8201-cfa779df69d9 | -11.74062 | -54.55333 | 2026-09-20 06:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25af8ad9-758d-323c-8c29-9181e598d78d | -8.66562 | -66.80257 | 2026-09-20 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fda50f9d-8a3b-3923-90e5-d1353b10c5da | -11.7399 | -54.55999 | 2026-09-20 06:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 734f3756-1bf8-348b-b1e8-650d4792f652 | -9.39423 | -60.35189 | 2026-09-20 06:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e87a565d-84de-3f15-9b67-bd7915be3c35 | -11.21788 | -54.07302 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4dcde8da-4ac6-3fb3-a8b2-8461b68f773f | -11.10067 | -54.03746 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 316b3145-97e8-3050-9a2e-4b0af42fe4b4 | -10.38436 | -68.98754 | 2026-09-20 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 222f2071-763a-33a2-8e0d-b5ac9e9ef08c | -11.04564 | -54.15762 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 78b6e110-27e8-3560-9578-3a20582613fe | -11.01667 | -54.13509 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4de6f7c5-66b2-3485-909f-82404ecb6357 | -10.90566 | -53.9815 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad239d74-7867-3ee1-b024-b6eb23fe6df1 | -11.08632 | -54.03552 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 817e0687-07b6-318e-90c8-90a502a82db4 | -8.61194 | -54.60945 | 2026-09-20 06:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 18d2b2c2-0509-3fdd-b365-b02b9d65e8f2 | -11.11782 | -54.03086 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6bf35021-e48b-39cd-97d8-621d6aa822f3 | -11.0935 | -54.03644 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0d1c974e-01e0-3a00-b9ae-e0347f850165 | -8.22558 | -62.84961 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f098f3f9-7ce5-307c-8ace-f46bbe3da1dc | -10.23435 | -68.75681 | 2026-09-20 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e17c1b56-eb57-3b89-9004-57ff2a8e2a4b | -11.03772 | -54.1639 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d0ed296a-c7e5-37fd-9d8c-f0d9dfdcac4b | -11.09549 | -54.035 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| d2eea51a-32ec-3b5e-9513-9814640d395a | -11.03848 | -54.15699 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6a8c9680-dace-3097-9ff7-f5471910eceb | -8.2342 | -62.84264 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e1b95b1-30e3-3c78-a31c-01761fbf6ff9 | -10.57321 | -68.66956 | 2026-09-20 06:01:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8d2478e-5359-3fa2-b755-7bfc1a2b57e2 | -9.93302 | -60.73032 | 2026-09-20 06:01:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df765381-440c-3d1e-85f9-0edd01ec49cb | -10.8356 | -68.70482 | 2026-09-20 06:01:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4772ec3a-5415-3b90-a678-3fedc4572667 | -11.11586 | -54.03229 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 568d38ca-b024-3e22-9dd2-9a9be30a4806 | -9.67664 | -54.32011 | 2026-09-20 06:01:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b75746bb-90ce-31f7-ad94-8e6a07590647 | -8.18063 | -62.80252 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e8fafe6-269f-3c35-ada5-4070bb3a0c76 | -10.87145 | -54.08567 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e49f019-2548-3694-8e5d-cc46820a03b0 | -10.21194 | -68.75693 | 2026-09-20 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dd7a8a3-8de1-31f6-931d-738b6d6dfe77 | -11.03569 | -54.15849 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8d46c2c7-1588-3d3f-831b-447a726732cd | -11.21706 | -54.08033 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f11c003d-dc07-3c8f-b991-a806031619e6 | -8.22177 | -62.84581 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42a272c6-272f-3081-8b9d-aca0359c79d0 | -11.20631 | -54.08454 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| be13090e-0a4a-344b-a498-8a5b2a22c735 | -11.11861 | -54.02391 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| c344ca6e-5a6c-353e-b1c7-8ada47e7677c | -11.04285 | -54.1591 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fc3bc7e3-3299-36a7-a359-4bfa889c120d | -9.0283 | -60.3647 | 2026-09-20 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34589b68-a55c-3fc1-ae13-abf99490930d | -11.01748 | -54.12799 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c129484d-1869-3197-8738-0576f992d630 | -10.56495 | -68.51842 | 2026-09-20 06:01:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44301fad-03c4-376b-86f2-f7c8751b4b50 | -10.75252 | -55.99699 | 2026-09-20 06:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5273bc2d-2033-3947-bf67-d7c4a5ee316f | -11.21072 | -54.07193 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fb4889f2-9d2c-3db1-90d1-158fd393509b | -11.08713 | -54.02865 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 865f04b4-05af-3520-a619-21e83c88038c | -11.72056 | -54.55908 | 2026-09-20 06:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0205745-2fee-3536-bd92-491a3aef69ef | -9.93797 | -60.723 | 2026-09-20 06:01:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af56287c-e080-3eab-96f6-9c9097faf2bd | -10.87063 | -54.09258 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0ad8dcb-d659-3be6-9cdb-79160df7d242 | -8.1975 | -62.85048 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74fab343-98b9-3d0e-8f54-888b11cdb674 | -10.98412 | -68.45621 | 2026-09-20 06:01:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e3b3763-32fc-3a33-bbfc-31ff24a74f5c | -11.04839 | -54.17369 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a996459-650a-329a-8f84-becf2482ab80 | -9.09892 | -60.49519 | 2026-09-20 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c00d491-b3b9-3eaf-99f1-0976d28aa94e | -8.79647 | -60.79612 | 2026-09-20 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 32fecbcc-71d0-3a55-925d-934ee637cee1 | -11.22423 | -54.08128 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3448cbc2-5fa4-3598-a51c-c681c6e945f3 | -11.04756 | -54.18081 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dafa7158-ea4d-3424-9889-bbebbdfd5921 | -11.10231 | -54.02354 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| b2eb49c4-c12d-33d2-9535-626363987c0f | -10.88032 | -54.07205 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fbe64d72-0350-3535-8bb5-bdca84897b22 | -10.87348 | -57.15356 | 2026-09-20 06:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30089029-f9c5-3bf7-91d6-9163bc691dfb | -11.09627 | -54.02804 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c7de8e1d-decd-355e-9434-d6ac4202a901 | -8.80162 | -60.79228 | 2026-09-20 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f44de498-35a8-3571-b627-2630ad961ecf | -10.05557 | -68.4464 | 2026-09-20 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 174cf7a4-11d0-352d-9927-ed338b4368cf | -8.22639 | -62.84146 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0dd6b78-dd3a-3601-832f-2d717c8b252b | -11.04488 | -54.16454 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 34964b73-bef6-3076-8fc5-0d4459ecc378 | -11.10266 | -54.03604 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| dcf43a5a-457e-30c5-a3ff-bff7b8e5b4c4 | -8.80033 | -60.80137 | 2026-09-20 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 607b270e-2f02-3196-8af5-f47a60ea6c50 | -8.61674 | -54.59101 | 2026-09-20 06:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5281f5f8-6ba2-3723-a525-b72bb69cdda5 | -11.74867 | -54.56237 | 2026-09-20 06:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53034721-48ed-3678-9c07-8a08981d4ca4 | -11.05048 | -54.17937 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4cf71c16-2bcf-3332-861c-e14c3e527cc9 | -11.10422 | -54.02213 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| af657a25-4393-3ff1-8a47-736c95ce9723 | -9.93271 | -60.72715 | 2026-09-20 06:01:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebbdc387-ab08-30a6-b60d-fc7d749a291f | -9.94257 | -60.7237 | 2026-09-20 06:01:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d36e18e7-2250-35e5-afd6-5c42b2bd00f9 | -11.08831 | -54.03405 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 54913922-dabc-33c1-912f-558686db26c2 | -10.87401 | -57.14924 | 2026-09-20 06:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f4b9ed2-9d75-3aa2-a949-5f95705d3610 | -11.09704 | -54.02108 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| d844cf1e-dee2-3f3a-bc78-e24c88f4c97f | -11.94952 | -55.9231 | 2026-09-20 06:01:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f45103bb-906f-38b3-8e91-4ae979e2d4db | -11.1258 | -54.02474 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7af7493c-02d3-3461-a33b-97d65530c252 | -8.61355 | -54.59706 | 2026-09-20 06:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 679ff002-2c56-398b-88cd-c17640ba3d8c | -10.92527 | -53.95295 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5dba0f56-0f32-39ce-8579-cfe5cc24549a | -11.71278 | -54.56495 | 2026-09-20 06:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff591f16-7aa8-34f1-bc7c-c5b6fc38e38c | -8.20531 | -62.85164 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e41283a6-96fc-39d8-885b-979cdfa7c1f0 | -10.86161 | -56.17802 | 2026-09-20 06:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README105.md)
