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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c65d0ddd-c7f7-3424-a59f-244f0e87a52b | -11.2563 | -51.300098 | 2024-10-08 01:00:47 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f9a457aa-40be-3a8e-9863-ee2efc674438 | -11.2579 | -51.307098 | 2024-10-08 01:00:47 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e87db929-d124-33e9-8f28-cdf186911bd5 | -11.2403 | -51.274502 | 2024-10-08 01:00:47 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5e1e02b3-810f-32c6-a98a-783201cad05e | -11.2418 | -51.281399 | 2024-10-08 01:00:47 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c168e682-2aad-3c46-aa3f-897968fd5939 | -11.2434 | -51.288399 | 2024-10-08 01:00:47 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d6e2ca2-9b6e-3f22-84a7-76c00652e459 | -11.245 | -51.295399 | 2024-10-08 01:00:47 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 708185a3-0222-3b4a-8f9f-b12227e53c2d | -11.2465 | -51.302399 | 2024-10-08 01:00:47 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 211f04c1-01d5-319a-a14c-38cd4a35ee7f | -13.3889 | -61.932301 | 2024-10-08 01:00:48 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| af3f8765-99bc-3766-8466-a137723d6030 | -13.3942 | -61.9617 | 2024-10-08 01:00:48 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 82759792-e20d-3677-8989-7096f0d62552 | -13.3792 | -61.934101 | 2024-10-08 01:00:48 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 764d1916-20fc-3c99-a58d-a4abdca829fa | -13.3846 | -61.963402 | 2024-10-08 01:00:48 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 742634f5-eccc-32db-be7c-3d4fb712f881 | -11.207 | -51.3554 | 2024-10-08 01:00:48 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6cecd999-1afb-3e82-b071-b92ef1c0d839 | -11.2085 | -51.362301 | 2024-10-08 01:00:48 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4bce79e4-788b-38e4-97a5-1fc205f9a3c8 | -11.2101 | -51.369301 | 2024-10-08 01:00:48 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 300389b7-e440-33f7-9f1f-28f36c68cef8 | -11.2117 | -51.376301 | 2024-10-08 01:00:48 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d015132-de26-3c5f-b352-659116cc3bff | -11.2133 | -51.383301 | 2024-10-08 01:00:48 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 750c8aef-8204-3709-9503-f69d7e9522ab | -11.2003 | -51.371601 | 2024-10-08 01:00:48 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b832f73e-d6b9-3e3a-a457-575dae3a6733 | -10.5241 | -49.098499 | 2024-10-08 01:00:51 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40abc134-257d-31b0-951f-ec60ece6b941 | -10.5258 | -49.1059 | 2024-10-08 01:00:51 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5673186-c606-3090-b614-dcb179598e71 | -10.4115 | -49.4128 | 2024-10-08 01:00:54 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd18927f-c23f-3f0b-b67f-b97d3628575f | -10.4132 | -49.420101 | 2024-10-08 01:00:54 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df64a6e6-6b38-35fa-882d-fe85646b70d9 | -10.4149 | -49.427399 | 2024-10-08 01:00:54 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f7d43eb-98e0-3f88-8a96-51a4f6149a2e | -11.1163 | -54.016499 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96b414e0-2bb1-3366-81d7-0fbad3c140b3 | -11.1181 | -54.024799 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2e26398-2a09-3c53-9fbf-902d137f9d47 | -11.1199 | -54.033199 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ada84be6-e735-3a9f-8006-bc3c939989a1 | -11.1217 | -54.0415 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6b8ab2b-5860-3a83-9115-15d6cf4dfe6c | -11.1028 | -54.001999 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e30df436-b55c-312e-a2a6-bb22b54951d1 | -11.1047 | -54.0103 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01f80923-0ece-3ae8-8b60-449f60f32829 | -11.1065 | -54.0186 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76f3d2d6-db4d-36b7-9cda-3e190dfcf5af | -11.1083 | -54.026901 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3bff7db-f48c-3dba-a690-f0c92004d7e7 | -11.1101 | -54.035301 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0cea0f70-1e27-35b3-a010-09efcd0f08b5 | -11.1119 | -54.043598 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 729133e3-7365-383c-bb01-11e54e265e30 | -11.1137 | -54.051998 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b05b2cf0-c6d3-3332-98d8-b2b9ab7e11da | -11.0949 | -54.012402 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2ca77b6-e1f1-3430-92d2-fdec8a9a22cc | -11.0967 | -54.020699 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23aa9de4-ddee-32a9-9b40-fd2d8f2a8927 | -11.0985 | -54.028999 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87e9197c-7101-3a3f-ad4c-91817454b82f | -11.1003 | -54.037399 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d769d03a-36cc-300c-9999-43517e76fa1a | -11.1322 | -53.995602 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0d8be8b-d2f3-3b8c-a550-802288085971 | -11.134 | -54.003899 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef8b2f6c-e9fd-3869-afbf-69d6b826430f | -11.1358 | -54.012199 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 952114a0-9874-37c1-8c7d-eea2de495a3c | -11.1376 | -54.0205 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a814e3f7-b74a-3ef0-a2f7-b9f893f287f2 | -11.1395 | -54.0289 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0938960b-80ad-3db3-8da5-001f3c392321 | -11.1224 | -53.9977 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a18b47be-c10c-396e-92e7-09d28e40f2cc | -11.1242 | -54.006001 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a3310f3-e8e0-3689-97ea-26d701b5cef8 | -11.126 | -54.014301 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90d19f0d-944b-310d-84aa-5305bb0dac50 | -11.1278 | -54.022598 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a426601-91a0-317e-8c85-91d0a9d2eda8 | -11.1297 | -54.030998 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3cf9e1c-8d03-3376-93ef-530f60bf2810 | -11.1315 | -54.039299 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d74baf3-1033-30ea-829e-d708d5049d37 | -11.1145 | -54.008202 | 2024-10-08 01:00:59 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f002873-7213-37ab-a291-17e7c6b5ccf0 | -11.0015 | -54.244202 | 2024-10-08 01:01:02 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e927637b-65d7-3ce0-b3b9-186fa9526d14 | -11.0033 | -54.252701 | 2024-10-08 01:01:02 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1766adad-993b-39dc-aef8-dbfb58aa5965 | -10.9935 | -54.254799 | 2024-10-08 01:01:02 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53031408-8260-35a4-969d-f6d6cdba335f | -11.4862 | -59.077499 | 2024-10-08 01:01:10 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 048786b8-7b86-398f-81ed-245d5bb4b49f | -8.1394 | -44.396999 | 2024-10-08 01:01:11 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 15945438-9fdd-3dca-bcb4-a7707d5b1059 | -8.143 | -44.411499 | 2024-10-08 01:01:11 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f296a6d6-b244-30d7-9d82-8bf68a592b44 | -8.0084 | -44.367699 | 2024-10-08 01:01:13 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b5a00855-8659-391c-995a-017aa448f50c | -8.5304 | -46.580601 | 2024-10-08 01:01:13 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09b1e7a3-25bc-3147-be6e-c8ddb9c170df | -8.5329 | -46.5909 | 2024-10-08 01:01:13 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 487c48b7-25bb-3494-9c24-c82aca23577f | -10.6288 | -55.8997 | 2024-10-08 01:01:13 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 651ff485-6868-31c9-a7ee-53cd2369645b | -10.631 | -55.910099 | 2024-10-08 01:01:13 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8630522c-ba99-3d50-b75f-3a7d9f5965ea | -10.6332 | -55.920502 | 2024-10-08 01:01:13 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7c3bd20-88b3-3ac9-97e6-44b22fbdeba7 | -10.6576 | -56.036201 | 2024-10-08 01:01:13 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c74e7ca-7e0b-3230-be72-2c80f2575bf5 | -10.6599 | -56.046799 | 2024-10-08 01:01:13 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6797dfe2-265d-38b1-9f97-17effdfdacf5 | -10.619 | -55.901699 | 2024-10-08 01:01:14 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e866fe2-d790-3331-a8d6-dde57eff1d04 | -10.6212 | -55.912102 | 2024-10-08 01:01:14 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 413a8092-5b5e-31c6-8e41-d54866ea48a5 | -10.6234 | -55.9226 | 2024-10-08 01:01:14 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14709c77-1b45-3d19-86af-4cf2c7fe4d94 | -10.2137 | -54.300301 | 2024-10-08 01:01:15 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92534a8e-c81d-34b0-bb73-b03898a7aeb6 | -10.2039 | -54.302399 | 2024-10-08 01:01:15 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b95b90b5-c19f-3214-89cd-1b3f9190f8dc | -7.8574 | -45.343102 | 2024-10-08 01:01:19 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1967ba4-8007-36e8-a9d6-3e4b60d83043 | -7.8605 | -45.355701 | 2024-10-08 01:01:19 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7aa87eb-42e6-3f12-918a-99e082bb23b3 | -10.1362 | -55.174099 | 2024-10-08 01:01:19 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ceca541a-6092-343a-a70f-6dc3567a89fb | -10.1382 | -55.1833 | 2024-10-08 01:01:19 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d54b33d-3b8a-374a-8787-6ac914621e97 | -10.1402 | -55.1926 | 2024-10-08 01:01:19 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04224b11-d0cc-3504-bcd6-d266ed593139 | -10.1284 | -55.185398 | 2024-10-08 01:01:19 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28eb6646-61e5-33b8-9e04-6272e0281c1b | -10.1304 | -55.194698 | 2024-10-08 01:01:19 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66b0341a-0b34-376e-a801-f2f5fe509f0b | -10.1324 | -55.203999 | 2024-10-08 01:01:19 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba643912-cffa-33dd-ba25-232c326ae413 | -8.6034 | -48.832802 | 2024-10-08 01:01:21 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 169b9213-88d2-37d9-a1db-60955b3b3f3a | -8.6052 | -48.840698 | 2024-10-08 01:01:21 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1370d0b5-5c40-3944-91f7-58da8116649b | -7.2774 | -44.954201 | 2024-10-08 01:01:27 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54296d5d-8bf4-3ac0-a0a1-56bcb94aa1c9 | -7.2807 | -44.967899 | 2024-10-08 01:01:27 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6ae360f-7b8a-3372-b899-aa59142f9758 | -7.2676 | -44.9566 | 2024-10-08 01:01:27 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18fdba64-2d67-34f1-a659-1981371de8b3 | -7.1019 | -44.576199 | 2024-10-08 01:01:28 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d49c06b8-cb45-35e9-9763-eb57ec8a7411 | -7.0885 | -44.563999 | 2024-10-08 01:01:28 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f26076a-3094-3b47-b952-821ca081e4e9 | -7.0921 | -44.578602 | 2024-10-08 01:01:28 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65d12877-ba6d-314a-8fef-d8af9e9ea876 | -7.5287 | -46.577801 | 2024-10-08 01:01:29 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7f6dd7c-0ab3-38f4-bd11-94cd09e2688b | -7.5313 | -46.588501 | 2024-10-08 01:01:29 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dce4bede-39f7-3bfc-85d1-e74876f79eeb | -7.5189 | -46.5802 | 2024-10-08 01:01:29 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cf13d59-686a-36ea-8f2a-ffdc3f4833c8 | -7.5215 | -46.5909 | 2024-10-08 01:01:29 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90a8830a-3ef5-35af-bf9c-d3f9cb933454 | -8.1608 | -49.4547 | 2024-10-08 01:01:30 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06752abe-37e6-3d23-9bde-a4176c3b662f | -8.1626 | -49.462299 | 2024-10-08 01:01:30 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa3bde59-40db-3607-a432-2fe14ad3e8c4 | -6.7005 | -43.951801 | 2024-10-08 01:01:32 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ea902ab-d09f-303d-929e-8c8fc664eb47 | -6.5757 | -44.154202 | 2024-10-08 01:01:35 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22b64e46-6473-3641-8e55-479001bc7215 | -6.5796 | -44.170101 | 2024-10-08 01:01:35 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d74da771-76ca-3f68-ab70-8a5171740123 | -6.9024 | -46.078201 | 2024-10-08 01:01:37 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcaeb5e7-52e4-3448-8b2d-9f76845ac1ae | -6.8927 | -46.080601 | 2024-10-08 01:01:38 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b024208c-06e9-390d-aeba-4ef9a8d39808 | -9.3519 | -57.489399 | 2024-10-08 01:01:40 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7dc6b6c6-a174-3da0-8d27-91cf58551fd0 | -7.4972 | -49.4417 | 2024-10-08 01:01:41 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 420b8fe5-970b-3f8b-a179-b7f430c4784e | -8.6159 | -54.922798 | 2024-10-08 01:01:43 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e825cb98-774c-320c-86b6-29a3e7de8b26 | -8.6178 | -54.9314 | 2024-10-08 01:01:43 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17f444ba-a1a8-3657-87bb-24cdbaa22d3e | -6.6624 | -47.0937 | 2024-10-08 01:01:45 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README19.md)
