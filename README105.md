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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17fad2a8-772e-3f9d-9a2f-106727b10a45 | -4.50319 | -59.55703 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3ffa7fa-f5c1-3682-b9b2-0c2752ddd6cd | -9.08791 | -60.97328 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 254f672f-cd9b-394d-806f-08c2d4fe617d | -8.92527 | -61.48385 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4faa9109-1baa-38d0-9d7b-3eb5bb55032c | -2.45323 | -49.22011 | 2026-09-23 05:23:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| affe628a-ea3b-3a2e-9063-c151a2054ad5 | -3.60392 | -60.57835 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 076f4df7-5037-3de8-be9a-701c1fb70e78 | -6.34239 | -49.87415 | 2026-09-23 05:23:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f4173087-f4ec-374a-9062-d98b8b1983ff | -3.07256 | -61.21008 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62048c04-52cc-3862-b851-d681a955641a | -9.0813 | -61.43012 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f9f7c91-4559-31ae-ab91-62fda86320fe | -3.64676 | -58.76807 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ef5ccb6-8ab3-330a-96ed-f0472e0510e1 | -3.46203 | -60.25977 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0e56f94-2bfc-36de-af3d-50c38816c5ef | -3.90433 | -59.71074 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a078b130-c45e-3109-88c1-0fc8540385e6 | -10.3119 | -50.48712 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4673496a-c45b-36b3-a1e1-7198c508388d | -7.88374 | -61.1801 | 2026-09-23 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6f8b68d1-a179-37cd-8a4e-7cc8efe1255c | -5.74146 | -53.46948 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0fb9d8a-15e2-3126-a6bc-970619c70a0d | -5.73729 | -53.46885 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f6b3443-b538-341f-ba0b-46987ac2b2a9 | -4.41642 | -55.4782 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5d3e3f0-5f49-3721-895f-66e67d9d501d | -11.78049 | -50.9839 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f9d5fa3-914f-3cf2-920e-e3a7dda5f682 | -9.11124 | -61.43888 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 411d0fb2-ebc0-3f80-8593-197beab4e884 | -3.80219 | -60.72037 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb8ecd5a-d6c2-396d-b8c3-42810a01ef6c | -4.13078 | -54.2498 | 2026-09-23 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 736a7119-a55d-30b5-a45f-1c20e48d2e9e | -12.51107 | -49.9823 | 2026-09-23 05:23:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9eda400a-fba3-3a6d-995d-6090e2c32d2a | -12.37856 | -50.15885 | 2026-09-23 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c699f92d-bc16-3f6d-91f1-a6c1b16ccb10 | -3.12143 | -61.46973 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3815728f-2d9d-395c-9379-80eadecfc128 | -8.92867 | -61.4844 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d466097-748d-36fb-9a37-e569a7bc155d | -3.7732 | -60.74667 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e11ede57-2bf6-3caf-b2b0-bee03cf02a35 | -10.25612 | -49.96613 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1a7be1a-fbb0-35a6-8541-d6a7a2fceaec | -10.45063 | -50.3659 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4156d3ec-c42c-3c74-b2ea-94cd829088ef | -8.49184 | -57.61447 | 2026-09-23 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 76fc6a50-76bb-3be7-9d32-8dbd0530fc15 | -8.22695 | -62.8363 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d19795a9-baf0-3801-84c6-f5d7826fdcdf | -7.83286 | -63.41467 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d262f25f-84b2-3e62-ac75-80786af3a38c | -3.38923 | -61.2901 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5507f5b2-f248-3c69-8b8c-d5855245f39b | -9.04364 | -65.42568 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80a9e4f3-68cd-3623-ab40-c6ede8b579bf | -2.41745 | -58.27106 | 2026-09-23 05:23:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3869d102-a15c-3a9d-b76f-bf80597ca2e2 | -9.14797 | -61.19029 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d5c1889-c26a-30fb-b940-e8fa18f35a58 | -8.30999 | -54.77502 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3be13748-955f-3060-886e-c222173d4547 | -9.54071 | -65.68732 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90335bc2-fbb6-3163-ae67-cb344e706079 | -9.32318 | -60.07552 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd769ca0-3d89-3277-9b70-e46d93712338 | -8.91442 | -50.89609 | 2026-09-23 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6a31193-6db2-35a4-9e3e-afd5e33bf8a2 | -3.962 | -59.3498 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6237a3e6-3d3a-35ad-8f0e-3aefe6997b35 | -3.50328 | -53.20609 | 2026-09-23 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 667ef40b-dce4-3ce8-86e3-d88379cf942e | -11.63624 | -50.97935 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f510b11-a338-3ed4-adde-a0e72e3d8e8f | -3.82091 | -58.89128 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59a92813-ebd2-3a77-82b2-938929a86864 | -10.27156 | -49.97997 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2cab8721-1931-38f3-a301-7e10acd92739 | -2.9597 | -54.09066 | 2026-09-23 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28eab99d-779f-3732-9d3c-725340fa092c | -3.6836 | -60.58282 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1ad8ed17-60c0-3ea8-80ac-c99b55eb6229 | -12.41061 | -46.978 | 2026-09-23 05:23:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7491400-b22b-3856-8bab-8dac420fce3f | -4.0505 | -56.31355 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cdec5e4-b53c-3c14-83d5-5babea3b7af8 | -2.62507 | -59.37937 | 2026-09-23 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd242d93-e48d-3707-b01a-14df06d5827f | -1.073 | -54.10154 | 2026-09-23 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 761b03a7-833b-3870-9749-1f42dfacf67a | -2.62173 | -59.37885 | 2026-09-23 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e1487f05-02cd-3064-b7ea-331697fa8f94 | -10.29651 | -50.52126 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f5f380ef-9441-3b35-aed9-b3b76bbf3107 | -9.55456 | -65.98566 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd3d439d-c464-30b2-8af2-51bf252e0774 | -2.70949 | -59.76743 | 2026-09-23 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3cf9c42f-46ac-3a55-861c-aaa84dc0f6a2 | -4.28165 | -48.61217 | 2026-09-23 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb4d47eb-3c7b-39a1-a16e-d39d359a009d | -9.15075 | -61.19446 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73d813ef-9ad5-350e-8e94-e386ecf15c2b | -3.38959 | -50.82576 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6520c591-d46b-3f3c-96ec-bbc3b40507c7 | -10.29687 | -50.51091 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2401686f-2491-34e3-97e4-46185b378010 | -3.60855 | -60.57141 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7443c832-f879-3e13-a57c-7c9f2fccd75d | -3.71088 | -60.10878 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9875bcee-2689-3f82-bd77-f8e9aa4b9019 | -11.11562 | -51.05301 | 2026-09-23 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| adf397cf-1215-3303-bf4c-00c404afd993 | -10.27862 | -50.52296 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec331ce5-0467-3a27-9b4e-f1c7db9055fb | -4.4533 | -55.07202 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32686e57-5915-32c6-a037-2e780e0755fb | -9.61094 | -63.52932 | 2026-09-23 05:23:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af198582-68d9-3347-9da1-4a3efe5932a3 | -3.77827 | -59.60441 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36f66ec3-5209-3f38-9674-595b3cce48a2 | -5.88965 | -52.10091 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3b36d32-9098-3e3c-b49f-2d3c3f08a4a3 | -9.55815 | -65.9906 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a68a7de-1f45-325a-b4bd-360c5c3817a4 | -10.58838 | -57.49652 | 2026-09-23 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68739531-794d-3a2a-a669-dfaa394b3606 | 1.17012 | -60.36429 | 2026-09-23 05:23:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f1d3588-2ec9-3626-a821-c9f617fbcd07 | -3.33642 | -59.86156 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a72186b2-bf85-3434-8182-3ebb8679fce6 | -3.78582 | -60.75645 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d1efc3b-de20-3d12-ab55-d714742aa7cf | -3.74679 | -58.86508 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52467db6-0894-363a-8aa8-c63e29ffbaea | -10.4872 | -50.29966 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e74a6d61-da2b-3829-9beb-17bfb1ee5c74 | -10.31056 | -50.4978 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6e2512e2-c3b0-31c4-ac9e-37292a040a7c | -10.29061 | -50.52408 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 042c42c6-9ba5-3ff6-8e5e-37652a17ccbf | -2.55287 | -49.1021 | 2026-09-23 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17abf728-45c9-3119-bc79-1abc2be1d483 | -5.47296 | -57.14256 | 2026-09-23 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80a52f03-93a2-3a54-9c9f-a25d307db619 | -4.15427 | -60.79435 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca8c448c-bd18-38b1-8876-fc9e3ef2afb2 | -11.64364 | -50.94431 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a704cbb-7c0d-3f04-b10f-16698b4fbb7c | -9.10046 | -61.44084 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25cfef8a-89b5-3c01-9efd-61f800700fed | -1.91916 | -58.26259 | 2026-09-23 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| a9998fb3-9177-36fe-bf0a-57c85945e153 | -10.28408 | -50.52367 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 5d94c6d4-c23d-3b40-98a3-3ddf826b6497 | -4.06262 | -59.83007 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07c34aff-1156-388b-a1e3-80f9d9a7ae15 | -5.34252 | -45.17118 | 2026-09-23 05:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df217158-4882-3a5f-ab97-5353d1d2ea81 | -3.93486 | -59.32768 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01a526f8-2c29-3e1f-8f50-7c14348a2703 | -2.97777 | -54.15152 | 2026-09-23 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5e80d6d-c4cc-35ca-8fa2-d00e6ec7a867 | -11.11519 | -51.05637 | 2026-09-23 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c3886f8-1a39-3de9-bf6e-b57c561257bf | -3.96026 | -59.99649 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19b6ed5a-4de6-3290-9e96-ba0235fd7169 | -4.42002 | -55.47886 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7ed8fe2-8069-39f2-9378-7dee002101b6 | -4.06718 | -56.22979 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0d609ab5-c260-3005-8624-a359eda38779 | -4.56398 | -54.93251 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86880c40-34df-334b-87e8-4c048a9848f3 | -3.72034 | -60.57339 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75291529-7703-3ba4-b016-d5311649d7e2 | -10.28928 | -50.53475 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3694ea63-2a8a-3367-8309-28e38a0f4eeb | -8.91664 | -61.49382 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e325436-9212-3f1c-9a33-1f263c3d30bc | -10.3042 | -50.50422 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 68eabe9a-3579-3e79-bf1f-cc131db755e3 | -3.45363 | -60.26635 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae0123fc-e189-35c7-ac8c-a10ba08a0784 | -2.91667 | -58.52935 | 2026-09-23 05:23:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5637031c-2c87-3367-9873-15c1916c064c | -11.63823 | -50.94363 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ab01c3c-843b-3a7e-835d-e816e47c244b | -12.41273 | -46.97169 | 2026-09-23 05:23:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1c91f5d4-d8e0-3d50-9d99-20eac1ab241c | -10.30422 | -50.49741 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fa078d5e-a99d-3f3e-9af8-82c797dd12e7 | -10.29194 | -50.51341 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |


[Clique aqui para ver as próximas entradas](README106.md)
