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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93cd8fcd-72a4-31ca-9a63-b7f970f904ab | -6.14059 | -50.93613 | 2024-10-29 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a451f82-2ec4-3417-91af-3cbc0cd1f653 | -6.06001 | -51.15555 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 456f98a9-581b-30f8-a462-2230d528f0eb | -6.04343 | -51.14509 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52a07b3d-c5a0-3fda-b97f-b5c141dfaf25 | -6.02791 | -51.08938 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f08e85c0-2205-3ee1-9e30-e29f9ca1e42c | -6.02733 | -51.09299 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daa051f9-5f50-360a-a24a-c3087db6b77f | -6.02392 | -51.09257 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dde1f315-8938-34f2-988b-6f9303dbcc9a | -5.94529 | -50.86007 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5a65279-fa08-389a-a124-8a2335f09f5d | -5.94193 | -50.85948 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e410d1cd-931e-3754-a687-db73eb60a840 | -5.94135 | -50.8631 | 2024-10-29 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89066e20-ec30-3617-bae7-85e200597f0a | -5.57498 | -51.04497 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca1a1b6d-6482-3f59-9127-f086d1a90bd3 | -5.54169 | -51.01337 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5d61b30-88be-363d-a090-b75832e36e71 | -5.39062 | -50.96672 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9c5619f-3c4f-363f-a2a2-47a2547f0094 | -5.03089 | -50.95529 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0de51ade-19dd-349a-9e7c-091877aaaa64 | -6.81822 | -50.57143 | 2024-10-29 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a3e4d9c-ec42-3f8d-976d-b19cab46413c | -6.84243 | -50.42007 | 2024-10-29 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c691c47-002d-33bc-b928-52c50026ef98 | -8.53342 | -50.29421 | 2024-10-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5012b43a-5cf5-3708-9881-055c6aa65d8d | -9.34093 | -50.65379 | 2024-10-29 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17ad9c48-ccce-3b7c-8bf5-c2014ff4dda5 | -9.25294 | -50.71501 | 2024-10-29 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db1b7a0c-6b21-37db-90f3-32191f65a8e3 | -9.24962 | -50.71447 | 2024-10-29 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29d55f61-56b0-37ad-9c88-00c99678da89 | -10.55078 | -51.74763 | 2024-10-29 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc27a347-e65f-3677-b681-e3ed570955f3 | -10.34961 | -51.41557 | 2024-10-29 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a95a01f-ebcc-3cb2-8950-406ab595dd7e | -3.42386 | -59.96032 | 2024-10-29 04:40:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f95d753-a087-30cc-b54f-be7ef0d8086f | -3.95984 | -52.19118 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3b47681-7c03-31f9-b52c-3450a4a94fa2 | -3.929 | -52.12233 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92f1a5ea-7966-3b7c-8fa5-f7e5bc264c4f | -3.8951 | -52.19481 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05f304a1-44e7-36fa-a2c9-9508cc5a714c | -3.86177 | -51.69981 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1bfcd4c-b4fd-36c3-939c-c94c239a3823 | -3.85822 | -51.69923 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fb4e355-2248-3119-a9b6-b12201d885b2 | -4.67162 | -50.98248 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75be3d63-5faa-37a9-b911-4ae0c520e881 | -4.6688 | -50.97822 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59ee5be3-637c-3e64-a523-2d45ed1c8f87 | -4.6686 | -50.97843 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bca7152-dc26-3468-9c1b-794786e48b1f | -4.6682 | -50.98194 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 899ff8d0-ffb3-3eef-9fb5-3d039bb557ee | -4.66801 | -50.98215 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13856d3e-f8e7-3549-8f5d-ff2dec306123 | -4.6676 | -50.98566 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fc694b0-a9f3-3027-b8ac-0402902bc843 | -4.66743 | -50.98588 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e7d12fc-bcfa-3e2b-8be0-879a0f1315f5 | -4.53712 | -50.96577 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afd6f129-dbfd-3647-ace7-b10a6870fd63 | -4.53653 | -50.9695 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 631a9ca2-f479-3d70-8963-a861b5b9fc43 | -4.53074 | -50.98384 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e894254-7458-35b2-80c5-e34fc5efb3b5 | -4.53015 | -50.98757 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0a26541-e85b-3273-964e-05f380e837aa | -4.4798 | -50.99494 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a5df534-31f0-3de1-a20f-2d18d0aae104 | -4.4792 | -50.99867 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e886e1d-a219-3f32-84de-f3701e97d774 | -4.47697 | -50.99068 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a6aa0aa-f6b6-390a-a9c7-574a05667297 | -4.47637 | -50.9944 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eb8afe0-c83d-3d75-8d8a-6af0ebcf02d0 | -4.47577 | -50.99814 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 219610d5-6831-362b-8e04-c208fc898b95 | -4.47234 | -50.9976 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56ed7295-21a2-3610-840d-4d6ca3f03649 | -4.46832 | -51.00078 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a619cbe-446f-3a73-88ad-0a4df40ab0d2 | -3.96074 | -52.20859 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b614f20f-a4ca-3be9-8391-de5ddea1fa72 | -3.95916 | -52.19532 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eb3ce1f-40f5-3bdb-ac11-28a69cd6367c | -3.92537 | -52.12177 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef2a9cef-4229-3264-9458-696118419fbb | -3.86241 | -51.69581 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27de43a1-9121-367c-93e9-c05a5f08345f | -3.86155 | -51.81585 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4549fd4-0cd1-337c-b9bd-2d02e0989f0c | -3.85886 | -51.69522 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70370748-b92b-388a-80af-6e613d713cc9 | -3.84073 | -51.90065 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7d9e2dd4-83b2-318e-90c8-5a79673b8c8b | -3.84066 | -52.20807 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2fabb19-8487-3ed7-a10a-983c53228c1e | -3.799 | -52.00011 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 78d5d0f8-0663-3bc1-80f3-feaca4dc4957 | -3.79674 | -51.87684 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00b6aae5-e808-3a7d-bd45-fab49580d90f | -3.76279 | -51.66044 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eeaff38-b39b-3a5c-88a9-fc341b8f320d | -3.70144 | -51.83793 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 088f0dfd-98fc-365d-a3f8-a6c5cbc86019 | -3.69786 | -51.83739 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e870f035-ca97-3dd9-a778-60b2b9437cbc | -3.69427 | -51.83684 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88640d4d-546a-3246-ace2-65cffffd27ed | -3.69362 | -51.84091 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b980b3b-ee89-3d84-900f-aed0a59df6f2 | -3.69296 | -51.84498 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 371d8536-84e4-3202-89c6-e2333224d671 | -3.6923 | -51.84905 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8771f7b7-821e-3d93-84ba-e69b4afa1f86 | -3.69164 | -51.85312 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6c4171de-69ed-3b33-935d-71d4b84392aa | -3.69069 | -51.83628 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e3ef80f-4a10-30cc-a41a-f14a04ff5626 | -3.69003 | -51.84036 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92b9aff9-5c5f-35a5-b6bf-08b8b4888adc | -3.65651 | -52.04738 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e44bd98a-c589-30c0-9a03-ff7a028ecc9e | -3.6972 | -51.84146 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0520856f-20f3-39f8-9408-b028c7f9e6ae | -3.68871 | -51.8485 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f17b405a-5e76-353e-952f-0956107a1961 | -3.68806 | -51.85256 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1ffb711-9680-3bca-b45c-27690ee6e2bc | -3.66192 | -52.15225 | 2024-10-29 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e0e542c-b381-3aa2-bf49-1d8a11926e26 | -4.05077 | -51.08564 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa7a5aae-d988-37b2-8714-059bf102892f | -4.03516 | -50.87573 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ac5160c-a335-31ab-b351-8586f6f97129 | -4.03456 | -50.87945 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93d5c41d-730e-3f09-9ab3-9ada1b08747c | -3.97589 | -50.93936 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a2242a5-53c2-33fb-95dd-c806a4178082 | -3.93386 | -51.24771 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c4ddc0c-7d92-329f-b992-43e6ec573366 | -3.9128 | -51.20115 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 006db34f-1dd7-30a4-88be-8e04ac5d1b6d | -3.90994 | -51.19678 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c24b6b0-438e-3066-8b55-13f015f87047 | -3.90933 | -51.20062 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e649f8b3-c907-3ec5-996e-78b91f167bc3 | -3.89036 | -50.99182 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96c2e32a-6861-3fbc-aec2-1c6556df527e | -3.88811 | -50.98368 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77f43305-59bb-3a4f-a43a-5a2b8b8eabfb | -3.88439 | -51.02958 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| da30e922-72cf-3a2e-b71a-d46811f92ac0 | -3.87162 | -51.41282 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85c3d165-ae62-3034-81f1-0e27953f1d4d | -3.86744 | -50.89204 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea81549c-58c3-3f24-91e2-e30566a72a2a | -3.86401 | -50.89149 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 243aa34b-cab7-3c2f-b166-a026931c94fb | -3.84558 | -50.98483 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ce79b1e-d515-3860-a21e-7df5179bcc79 | -3.84498 | -50.98858 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c25fec78-948b-3298-a91b-30359a762ba0 | -3.83102 | -51.36717 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37cedad3-74bd-37a7-9c24-1f07c3cf6d77 | -3.8304 | -51.37107 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 501579bc-ad76-3a34-af77-7ee177f58693 | -3.81319 | -51.07655 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| abffe3f5-c07a-3d05-9c6d-1729ae78a555 | -3.80974 | -51.07597 | 2024-10-29 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ee150f3-1a1f-3286-ab2c-4f6d0aefc91e | -3.79995 | -51.38204 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc04a8fe-e5ea-38c1-afb9-9f15b8f1941a | -3.79646 | -51.3814 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73c38722-4be7-3084-a512-d7fd09f38469 | -3.76878 | -51.39717 | 2024-10-29 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c226edb7-9b6f-35c6-8e9d-1d1e8fe53623 | -6.26336 | -51.70327 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c10d57bc-a430-3029-818d-48a1c82b700d | -6.26398 | -51.69942 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab2b884d-6ea2-3332-960c-996ef0f81a70 | -5.73019 | -51.45614 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a30550d1-3e8e-3aa0-94b3-8c5a78f0b480 | -5.69689 | -51.66257 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ede78d33-e703-3258-b0a9-5b0b6c179d10 | -5.69274 | -51.14277 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30ef9269-daff-366b-8659-aada61c72566 | -5.50964 | -51.42918 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28d413d8-313a-3d62-b817-991c359728bc | -5.41479 | -51.56329 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README64.md)
