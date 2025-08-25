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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a98f1b78-0877-3267-a512-117c2d4cb1d8 | -6.9169 | -62.99393 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10b6b9e9-0f9f-31df-8858-ebd3a615f414 | -8.89517 | -62.4516 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4684cde9-59b9-356e-9257-06d418d0c445 | -9.0797 | -66.06114 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1207a428-a46a-3f50-ac7f-712164ec0ade | -8.94478 | -62.13302 | 2025-08-25 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecce1a63-728f-3676-a5b6-81e2d4e336ac | -9.6474 | -59.63749 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7f3679a0-ae33-356c-9232-152742658ce6 | -8.98896 | -65.40693 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ffff7c29-df02-3490-a924-8de0951ed9dd | -8.58543 | -62.63564 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 161a5827-9f5e-348a-82b0-2c457e968300 | -8.5903 | -62.60029 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f33ecc9-6e43-31f5-8536-d00e3b4c20ae | -8.89324 | -62.44377 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff624147-a1b7-3d12-9e00-820ee3f6f909 | -9.15165 | -59.47299 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a0eccff-34aa-3a2b-a01f-c5b10e9113bb | -9.16163 | -60.82327 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea8f99f8-808d-3ba1-a717-d67eeda7d395 | -8.90105 | -62.45427 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d46c9c8-0448-3d79-8a33-4eb1407a9bae | -8.65656 | -63.4306 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3214e36d-632f-3ef8-a895-b2961fd5f9ef | -8.87518 | -62.46272 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3220aa70-f346-303c-b2eb-d5bcde1ebedc | -7.56187 | -63.86185 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0d119e6-8518-32c9-b223-89404a354950 | -9.23491 | -60.92545 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57dee1d0-a5b4-3a88-86be-af3c4884ae85 | -8.9883 | -65.41145 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c20b0073-ce3b-3572-b40a-b8d4f17af51f | -9.05102 | -65.72218 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a55be4a-424b-3d18-a1b8-078f220bd459 | -9.15311 | -59.4618 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e8fce66-8306-3403-828b-f8bff6774fec | -8.88549 | -62.45488 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b62596d2-18b0-3465-9747-e99fac56f90c | -9.15757 | -62.3539 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5004ecbc-c193-37b5-928c-fbd2880ea810 | -8.88871 | -62.39914 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe832225-8391-3129-b947-d18173b99ee0 | -8.89388 | -62.46077 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f55d4fb2-922b-32f0-a4d0-6058dce686d8 | -8.69949 | -62.88075 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d430df87-f6f0-3284-b829-93f57cacc486 | -9.17849 | -59.61102 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4b60c19d-0743-3845-9461-ec76d2b9373b | -9.15744 | -59.5151 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cd703853-6f01-36bd-b81e-f44c2abdad94 | -9.0171 | -65.38082 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d16e9ba6-0ca9-3e25-b6c2-062c6c849315 | -8.90099 | -62.44308 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c36dae0-6b72-3573-b5df-8d5decaf8f85 | -8.10557 | -62.85874 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b18fbfe7-3a46-3214-a03c-03a990d470b3 | -9.2598 | -59.77065 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a090235b-ef44-396f-a870-521bbf46c280 | -9.20177 | -59.47411 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17a1c3b1-6646-39b9-994f-41d3b7cf7929 | -6.7939 | -58.64858 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f507d550-56ce-384f-9cf9-c73bbb0fe6f0 | -9.16374 | -59.46709 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b271be8-7238-3423-bcf4-5d464beb931f | -8.23222 | -61.38811 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a169978c-b617-3cb7-87db-cfc4b07d2036 | -8.6814 | -62.88246 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9239215-aa7d-3fb1-bb52-63a6dd697db7 | -9.1618 | -59.48188 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b7a8e2e-6f68-3bac-9a99-290652f4f893 | -9.17348 | -60.77273 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b616fced-87b5-3471-9430-9a4a3ffc633f | -10.41473 | -64.41304 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 141764e3-2f2b-3b55-a24b-82900c190837 | -8.90486 | -62.44831 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c5c0b73-b704-34fb-a55c-ee10f7949fc4 | -9.17076 | -59.45669 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2d762311-83cf-3cef-8fc5-e861bd798f28 | -8.66189 | -68.67056 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 416cc38f-22ff-3ee2-9229-a8d2ff68a281 | -8.63047 | -62.63768 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd47c846-959d-3879-828d-993cd394e35e | -8.91565 | -62.41422 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c6981e7-122e-3f14-9cd3-2fc26971f310 | -8.14406 | -62.86876 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7646c070-83c6-33cb-98e4-6906bf4cc4a8 | -9.00964 | -65.39621 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| abae6d2e-ec30-3aab-80c3-b336e3896d6c | -8.89131 | -62.41355 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b33603f-de6e-3886-a7d9-2997755c4e5c | -9.01645 | -65.38537 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85b49d16-b4c1-373e-8dd5-c04a6a2987b0 | -7.91076 | -63.08409 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ec1e2ad7-08ad-3ea3-963a-806277d471ba | -8.88032 | -62.42604 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3e1eab5-1fc2-3da9-bcee-7f60e78b2e92 | -9.20032 | -60.91939 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49f26971-4030-36ab-959a-61541c847ada | -9.1671 | -60.82106 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0c6ae9d-066b-3066-a9b6-17b80482103c | -9.2538 | -59.63831 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8258e99-2daa-3cb3-8f42-06025c8a99f4 | -9.03026 | -65.71013 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bca9588-b8fd-3ea0-a186-558047e00c94 | -8.97644 | -65.41427 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| b369e2c9-2642-3ec7-9d34-f47b96acb3c6 | -9.01955 | -65.39047 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd9048f1-cdb1-34ba-8514-39171444e140 | -8.23605 | -61.43183 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 721681cd-a5d0-341e-8cdb-03df7973a4a5 | -6.83678 | -58.95048 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 51e00042-6a44-3cc6-af53-97a2351448ca | -6.92112 | -62.99457 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a57fd20b-0a83-36b5-95d0-0b170c552197 | -8.89837 | -62.43983 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05467762-0eb6-3bf4-b9bc-ba2b4b0d8537 | -9.16868 | -60.80906 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 027fde04-5c5b-3256-8079-248242b466d3 | -9.06035 | -60.62054 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 280676a8-a522-3ad9-aec3-0199544e41d3 | -6.93128 | -62.98399 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd7d806a-56f6-3d58-94d2-a98397168fda | -6.91211 | -62.99726 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd97371e-0993-3f08-8698-b8a294082569 | -8.22259 | -61.38679 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 965b650e-9703-3157-af11-d9d6e168d3bc | -7.55431 | -63.85712 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 273d96ee-8eec-33f9-8ab9-24dae6fdadc4 | -9.19464 | -59.6192 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf9722d9-adb2-34e3-8b6b-383028ed78bc | -8.10383 | -62.87133 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b94dd9f0-7ee6-31be-bf7f-5296936a6c50 | -9.16881 | -59.47158 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0a9e0c9-c545-39e4-9e7e-fc8918bee0ae | -10.25941 | -59.10252 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c1261f16-7d6d-3907-a7f3-0e26ace0b891 | -9.1911 | -59.46893 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70c5d604-525c-3f47-8e7b-c8934e2a3fc4 | -6.3402 | -58.19111 | 2025-08-25 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 094bb400-2b56-3bbb-8ecf-c08ee5a9be8c | -13.05913 | -56.9177 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 11f09813-e637-320f-b67d-028e5cf0f72e | -8.232 | -61.42566 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f149ac6-cd50-33cc-87b5-e891853da0e6 | -9.26436 | -59.76901 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d677dab-f4b7-371a-a74a-228c5bfe5ec3 | -9.20455 | -60.92603 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 88ad53cb-a16f-3c98-9d2a-c9e40a18d043 | -7.90025 | -63.06611 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| b467f4d1-88d4-3cbf-ad73-92ef7f98d51a | -8.51186 | -63.87725 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91c421ca-66d4-3f3c-b425-e5da78c883c0 | -10.24424 | -59.66672 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e07b3fab-023f-3519-8e05-7ce4cd66308c | -9.00883 | -65.70253 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23e65782-938c-35eb-9d85-57aec11a5f45 | -9.62117 | -63.96925 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c473793-d078-3c5f-8bb0-2fbb8b39adc6 | -9.15023 | -59.48392 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0eab69d-3923-33dd-bff4-56020b81f20b | -9.81147 | -64.26846 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9822a524-0f9e-370b-b598-7dc987a52cf6 | -9.18092 | -59.45986 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9897bd02-bfa3-340f-93dc-aab34be27619 | -9.03506 | -65.72861 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f04c232a-12d5-3949-bf06-265f01bd16fb | -8.70341 | -63.96319 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 442bb445-5f32-3017-9ce2-0b3f4df21cd6 | -10.03157 | -59.35763 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8122703a-8c5e-3aa6-9e06-5d119df8d413 | -9.19223 | -60.78778 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 738e683a-acc8-320d-9b10-629765833e60 | -9.01619 | -65.70364 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e8065a0-b49e-330f-80fe-16eb7a272bdf | -6.80117 | -58.63773 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46b6e23a-b144-3293-b3ee-9fc9f43e22e1 | -7.91618 | -63.0766 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9743de9f-ecd2-3d90-81c6-2c25e8e88cfc | -9.18089 | -59.46576 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 11c4d7b8-3077-330b-9125-978ccf85b193 | -9.09916 | -65.72285 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d8605b0-4af3-3acf-b914-95bd5b429b87 | -9.23995 | -60.92621 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b26c0d8-4e7f-34dd-894b-bdf6e62948ea | -8.89568 | -62.42537 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fe80069-03c6-300c-9c74-06a3aaedc35b | -9.20576 | -60.91715 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef51879a-1236-3a03-881c-97c61e8274e1 | -8.86674 | -62.4241 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0be6ee0c-4943-3721-b191-ed41678d947a | -8.8837 | -64.19017 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0061c157-dd7b-3791-854e-efe5b96b4c6f | -9.07003 | -65.72063 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfb4d5a2-7a57-35a5-aea0-19b8761e3a70 | -8.89259 | -62.43718 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4b8e3150-c0a4-3abc-8af9-884ee96a0472 | -10.32953 | -67.36389 | 2025-08-25 05:55:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README86.md)
