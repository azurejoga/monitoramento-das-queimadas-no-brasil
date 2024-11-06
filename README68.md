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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c67dfa1a-0a7d-3f1d-81c1-ca95425cdc27 | -2.93487 | -51.0503 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6e6c0fed-e3c8-39ad-9898-ce5676529501 | -3.0134 | -53.2341 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f996f3f9-9a68-3ba3-a3e6-c86382f035e3 | -23.93538 | -54.05635 | 2024-11-06 05:35:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f0e43a82-339e-3a38-8b71-961af2fa2801 | -23.94197 | -54.05179 | 2024-11-06 05:35:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 789c0fa3-8208-3e8e-b41c-32955a49ba8c | -23.97299 | -54.05494 | 2024-11-06 05:35:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 479197f4-abda-3d25-a747-41b169ba51ec | -23.92879 | -54.06092 | 2024-11-06 05:35:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7ea5d320-c962-3132-ae18-504bb00025e0 | -23.93499 | -54.06155 | 2024-11-06 05:35:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3cc6d70a-2997-359b-9fa9-130782994ad8 | -23.92841 | -54.06612 | 2024-11-06 05:35:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 02c75018-89f5-3136-a743-4c323fde7914 | -23.96678 | -54.05431 | 2024-11-06 05:35:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1c9b12f1-71a5-37ea-ae78-87e99999a291 | -23.92764 | -54.0765 | 2024-11-06 05:35:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e6a5846e-1b30-3ad3-9a8b-113940cd8b99 | -23.92802 | -54.07131 | 2024-11-06 05:35:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 715eb885-690a-3824-97d2-06e09dbe4b12 | -2.937 | -51.0673 | 2024-11-06 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a382c3f9-e6ec-31fb-a4a6-be7d232641da | -3.0396 | -53.2805 | 2024-11-06 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| d7593ab0-23ca-397c-93db-70e3f4cf3a95 | -3.9669 | -48.1716 | 2024-11-06 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 6e47f573-b196-310d-a510-85832bf1c716 | -3.1617 | -50.2038 | 2024-11-06 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 223a0b57-d4a7-3f27-9417-925ced2b34b0 | -3.0207 | -53.4227 | 2024-11-06 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c66bdc59-4975-3e24-8507-405a0855ca44 | -2.7244 | -54.1351 | 2024-11-06 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 408b77d5-d21a-3cf2-97b4-98de25b3261f | -6.1226 | -43.9809 | 2024-11-06 05:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| f24d738a-862e-3512-8f75-c70528612a3f | -2.8506 | -49.4744 | 2024-11-06 05:40:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 011b9c18-f4e7-3206-b801-19c972aac1d3 | -2.9186 | -51.047 | 2024-11-06 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| d4f84fd5-ee65-3bc2-8cbf-201c7a765e95 | -3.0397 | -53.2603 | 2024-11-06 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| c1dfb394-e5d2-3639-8f06-434f6d1576a5 | -3.0023 | -53.4434 | 2024-11-06 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 15a3c474-bef1-3b9e-8a68-45196503ebd1 | -6.5014 | -47.4813 | 2024-11-06 05:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 79aabf8f-dec2-3566-bd04-041db5678b44 | -2.7243 | -54.1552 | 2024-11-06 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 93c479d1-c01f-3c72-acd9-77e60497329e | -2.9371 | -51.0465 | 2024-11-06 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 6703494b-0ac6-3aab-96c4-c6a66b136b67 | -2.8423 | -51.7735 | 2024-11-06 05:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 878c9e48-d1f8-32be-b324-8c7515969791 | -3.967 | -48.15 | 2024-11-06 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 48826c11-fdfa-32ae-80d3-6a943761255d | -3.0023 | -53.4232 | 2024-11-06 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| cff2a5f1-0eef-3f51-8ba9-f876f564b578 | -6.4906 | -44.6862 | 2024-11-06 05:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c4c26859-b65b-3cbf-b50a-9c036d096084 | -4.1432 | -43.5822 | 2024-11-06 05:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 02c527da-13e9-3f3e-86d0-535584ce36c3 | -6.5094 | -44.6847 | 2024-11-06 05:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| a4315809-f0d1-3259-89bc-85a9a526c3fc | -3.0207 | -53.443 | 2024-11-06 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 2b838b2f-3c24-308a-9a8a-15e9d78cb5bf | -3.5446 | -47.3855 | 2024-11-06 05:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| ffcdad09-6cc2-3f94-a513-7fb977848116 | -4.1246 | -43.5833 | 2024-11-06 05:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d78dd90c-a3e1-37da-ad66-3fb861158261 | -2.8608 | -51.7731 | 2024-11-06 05:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 4b89c1f7-8cda-365c-97d4-5d40370f3c79 | -2.7244 | -54.1351 | 2024-11-06 06:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 3d36a47c-0437-3bd6-850b-2c2c3f13632a | -4.5614 | -48.0141 | 2024-11-06 06:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 096c023f-bb8f-3b26-9b3f-ff8d08d5602b | -3.9669 | -48.1716 | 2024-11-06 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 68788977-875d-3339-bbd9-0422c91fb098 | -2.9186 | -51.047 | 2024-11-06 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| e37edbc0-3f57-3396-8b94-d6d6670a8a00 | -3.1617 | -50.2038 | 2024-11-06 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 3567c83e-76aa-3823-ad31-e80b1219e199 | -3.0396 | -53.2805 | 2024-11-06 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e5e520aa-6e7a-3b9b-9e44-c373c4c21394 | -4.1432 | -43.5822 | 2024-11-06 06:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 1f75ba37-04da-366b-82e8-94e8e9ea0d35 | -2.8385 | -52.9201 | 2024-11-06 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| bb1118aa-1a77-306b-827c-e70e7e360750 | -2.82 | -52.9409 | 2024-11-06 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 28c39fb6-1828-3e04-8c38-a7da8f923cb9 | -2.8201 | -52.9206 | 2024-11-06 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 6d236df3-7cb2-3e92-8752-c0810272ea4d | -2.82 | -52.9613 | 2024-11-06 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 10cbdc3c-8028-344e-90c2-23c3996cd5a0 | -2.8202 | -52.9002 | 2024-11-06 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 6e406083-3ad6-3991-b8fb-4b5d94e381ff | -2.8506 | -49.4744 | 2024-11-06 06:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 23a0f657-1c48-3c2e-964a-d8623b6517f0 | -2.8423 | -51.7735 | 2024-11-06 06:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 4f291f0f-32c5-39cc-ab77-90ce025e6416 | -2.937 | -51.0673 | 2024-11-06 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 06caa07e-f801-3a45-b570-a92734f1e114 | -2.7243 | -54.1552 | 2024-11-06 06:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 8320751b-1fff-3e8b-b682-5cd8da342d4c | -3.967 | -48.15 | 2024-11-06 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| f2fbd194-e992-31aa-af1e-21d7e3adf8b9 | -3.2349 | -50.3695 | 2024-11-06 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 75f0c7ae-d2d1-3cf0-921d-679c8eccf721 | -4.1246 | -43.5833 | 2024-11-06 06:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| d0e1e0d3-bc03-3b33-98fb-49f1a80f856b | -2.9371 | -51.0465 | 2024-11-06 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| d8a55b00-1b8f-3530-a3b4-10227e861ec3 | -3.0397 | -53.2603 | 2024-11-06 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ba74bbbe-4c70-3d6d-af97-9d9369ed493e | -2.8386 | -52.8998 | 2024-11-06 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| f4fc6714-a044-3002-b463-c89a187febdd | -2.8608 | -51.7731 | 2024-11-06 06:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 70d50949-76cd-39fd-a949-b71962dd07cf | -0.74365 | -62.91019 | 2024-11-06 06:16:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcb92d1e-dc9e-30e3-a584-1d393b030ee8 | -4.1432 | -43.5822 | 2024-11-06 06:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| ccb12e2d-8399-31fb-bd2c-85b5e4c87183 | -2.9371 | -51.0465 | 2024-11-06 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| bbfb40ef-4153-38e0-acc2-d5f9b1c071da | -3.2349 | -50.3695 | 2024-11-06 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8501f539-a74e-3d2f-8d55-0e829f57ae3d | -2.8506 | -49.4744 | 2024-11-06 06:20:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| ec16ec4d-4b5b-3782-bed8-161dba8c0ce5 | -3.967 | -48.15 | 2024-11-06 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 5e3709ec-91c2-3864-8f89-092c8717fa91 | -3.1617 | -50.2038 | 2024-11-06 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 82bb2c26-36bd-3689-8b8e-1bdbc658c6c0 | -3.766 | -47.5945 | 2024-11-06 06:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 64522536-6c5b-33c9-a0ed-b123a95c627e | -2.8608 | -51.7731 | 2024-11-06 06:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 195fa983-5cc5-3d66-b773-d81e5db3139a | -3.0207 | -53.443 | 2024-11-06 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| bd406f5d-26cd-3d42-b4fa-f773147ccff9 | -4.5614 | -48.0141 | 2024-11-06 06:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 49a5a116-e9a1-32ed-9c0b-7f51bb19b8a5 | -3.2348 | -50.3904 | 2024-11-06 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 9001ad7b-0c3f-38b6-a536-20c71559dfcf | -2.7243 | -54.1552 | 2024-11-06 06:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 418e07ca-c0e1-342a-a33d-4e14a1416290 | -3.0207 | -53.4227 | 2024-11-06 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 4def37ea-c32e-3a1e-8b38-e3000b9a5a70 | -2.7244 | -54.1351 | 2024-11-06 06:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| c379fdf0-f638-37df-ab31-83acfa2f4323 | -3.0396 | -53.2805 | 2024-11-06 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c48f672f-0972-3737-b72a-b282718f3771 | -4.1246 | -43.5833 | 2024-11-06 06:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| bd68e642-cce8-3d61-bd59-817336b39ead | -2.9186 | -51.047 | 2024-11-06 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| b0c8c320-6712-36b5-8de5-21792b836e09 | -3.0397 | -53.2603 | 2024-11-06 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fba099e5-d38b-3270-a140-0ea016757fa4 | -2.8423 | -51.7735 | 2024-11-06 06:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| dc0fcd6f-2047-331c-b2f7-ca1976675ac7 | -7.36059 | -72.92619 | 2024-11-06 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08ddb886-65f6-381f-b226-380dce0ee6e9 | -8.03202 | -70.93042 | 2024-11-06 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f125cf8-61ab-3be5-b70c-bbbf257e1e1c | -8.07225 | -70.76338 | 2024-11-06 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67614d36-4a87-3345-ab17-0aa30b02d003 | -8.62133 | -69.72024 | 2024-11-06 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d87391a2-a121-33a9-a587-c457b8a98e92 | -8.76859 | -67.66074 | 2024-11-06 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9dea34b-a8b5-38b5-b30d-3b01cf9b5070 | -9.37637 | -68.68812 | 2024-11-06 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7333711e-76ab-3a6d-b96a-3757f1b62913 | -7.34481 | -72.75262 | 2024-11-06 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6dc413be-3f4d-3f54-a263-af1bc5fa359f | -7.35989 | -72.92549 | 2024-11-06 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 728c62a9-7524-3eb5-816d-4e232612b28d | -8.04234 | -71.28297 | 2024-11-06 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f5c1126-c408-30fd-b73b-07d7c3ea514a | -7.35933 | -72.92926 | 2024-11-06 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fac6a611-a9f1-3330-ba20-8e44554c5443 | -9.41103 | -68.71458 | 2024-11-06 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e409ea42-044e-3bc1-8bfc-2bbc0af50dae | -9.37783 | -68.68648 | 2024-11-06 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e13294a-648f-3d62-81ec-710bef53b1c1 | -7.36 | -72.92997 | 2024-11-06 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18f610aa-34da-391c-9364-ebe1b0fe9d18 | -7.35714 | -72.92567 | 2024-11-06 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85fd5919-78d8-32b0-91b1-7bbd01632141 | -7.35656 | -72.92944 | 2024-11-06 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc26dba0-8a71-3f5d-a3b5-4cf76cd2abf0 | -3.0396 | -53.2805 | 2024-11-06 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 41792af7-e62d-371c-beb4-b674b52e6971 | -2.8423 | -51.7735 | 2024-11-06 06:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 6541486f-5e34-30c9-8802-8105e05f1527 | -3.2349 | -50.3695 | 2024-11-06 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 6039c945-5e64-3920-837f-22dbfa41ea77 | -2.9186 | -51.047 | 2024-11-06 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| f77b0e7e-ed41-3157-a07b-d4d60e2d73c6 | 3.6 | -51.3168 | 2024-11-06 06:30:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 3b5a498d-8f4d-3fc6-8534-599d988e0070 | -2.7244 | -54.1351 | 2024-11-06 06:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| da5d0c9d-2ee7-3b59-ba6d-065f11d03d76 | -4.1432 | -43.5822 | 2024-11-06 06:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |


[Clique aqui para ver as próximas entradas](README69.md)
