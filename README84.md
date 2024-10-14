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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 164ef2d7-3533-3d28-9ec7-d9ee2c247279 | -6.73117 | -51.23572 | 2024-10-14 04:44:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed3844be-83e0-34a4-b7d5-342634668c88 | -7.78676 | -50.22071 | 2024-10-14 04:44:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bd60853-3676-3f10-8456-9437987c6117 | -7.78621 | -50.22426 | 2024-10-14 04:44:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 433bb1ec-422c-3144-9c78-716fda8fb87e | -9.36035 | -51.07965 | 2024-10-14 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 646b0cf5-63f1-3181-9baf-fbd5f41ec084 | -9.17321 | -51.49464 | 2024-10-14 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f023628-e474-3dcd-91ab-443207e7942b | -9.17044 | -51.49061 | 2024-10-14 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da617f04-f17e-371c-887d-5880dd987157 | -9.16989 | -51.49411 | 2024-10-14 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08c01ed7-3cc0-302c-824b-3fee75437be1 | -9.16657 | -51.49358 | 2024-10-14 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba448769-9081-37b5-9139-406449ef1965 | -8.10332 | -51.09604 | 2024-10-14 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21b6a5ac-f349-3af0-9a99-3d1123abc560 | -8.10278 | -51.09953 | 2024-10-14 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 625923b6-2c53-39a8-a5f4-c18cdada2edf | -2.22684 | -50.68008 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d13c3937-5dd1-36de-8144-a3f22303fd3a | -2.02191 | -50.86686 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cec501ce-7886-3d41-a705-09247523b957 | -3.562 | -51.43959 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88a988b6-1060-3fd4-927e-fa4aaf3e4f4d | -3.54189 | -51.03608 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8b07baf2-3b02-32b4-b437-40fa58244ad1 | -3.53855 | -51.03556 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d920ec49-db38-37aa-b8bd-d33b561dd75c | -3.34472 | -51.64057 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a8623ad-a17a-30f9-a11b-1aed55e8bbec | -3.34415 | -51.64416 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9a2c8f25-ec8d-3058-9b67-817e2c2d343c | -3.34076 | -51.64365 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a62b5af4-198b-37dd-a0d3-572907f831a2 | -3.33811 | -50.80377 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a6f7a1a-052a-3fd3-8582-4f6ab498ec40 | -3.28104 | -50.94833 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d1c7ca0-56c6-3568-951c-b8c2b6b220ac | -3.28049 | -50.95182 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e99b8ea-b844-3dfa-8560-4b04e2a8b971 | -3.25608 | -50.76602 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 287e004b-0067-3556-9ba9-c6533e244925 | -3.25553 | -50.7695 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db72d5c2-aafc-3a44-b0dc-c8c58b1d2f39 | -3.2522 | -50.76897 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10aaf748-088c-3759-ba79-c7003a6d79b1 | -3.25165 | -50.77245 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3adf2f26-c866-39ae-8cc2-36f0676b54e5 | -3.24322 | -51.73174 | 2024-10-14 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0291a52f-d2d7-333d-9da9-d21749187b2e | -3.20088 | -51.02892 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9eba3a48-7cc2-3502-bf2d-6e52bbb0ee51 | -3.19754 | -51.02839 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4919596a-d9c6-37b2-b19a-7bdef0d745d2 | -3.08497 | -51.38349 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 818ad5d3-7b2d-31f7-bbd9-f9d978cec375 | -3.08441 | -51.38704 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2ee064e-23a4-3b5d-83f0-2da50566fb3d | -3.0816 | -51.38297 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e289b101-10a9-3c9a-95d1-767578f6fbc4 | -3.07593 | -51.17877 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86547e0b-f931-333f-b26a-5eef25908929 | -3.07257 | -51.17826 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1105d1a-f671-3bef-a51b-41cf8f0f4a3b | -3.06866 | -51.18126 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7f227e2-8cfc-3184-849a-c803b101987a | -2.99862 | -51.24279 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb2a6555-093f-3b64-813a-3c914975ed1f | -2.92805 | -51.84732 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b01b2b9e-1862-30bc-ad53-59ee576a36d4 | -2.90991 | -51.93875 | 2024-10-14 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b86d7e1-34fa-30bf-b974-3fa7b0caa434 | -2.90932 | -51.94244 | 2024-10-14 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d6e0ea4-b1b9-3936-b283-5570f3eebc75 | -2.8997 | -50.70713 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a63b0434-151f-33ca-ba81-2f234da3818e | -2.89915 | -50.71061 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 61a47784-0ad4-3ed8-b35c-4dbfce3ae21a | -2.81683 | -51.33842 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c8ff7f0-fdd9-327e-8a3a-a83ca1ea7501 | -2.78476 | -51.36627 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6b09acb-dd89-3ac3-97ad-1a217433d420 | -2.63151 | -51.75627 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b57b2bc-20e7-305a-b392-f9fe1604dfd7 | -2.63092 | -51.75993 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6179eb1-1f6a-3d79-9c88-7676f3715ee6 | -2.62809 | -51.75573 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99aae6f6-61c4-355f-8bc2-cd854dd80422 | -2.62751 | -51.75939 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f13f69f5-3e02-3672-afca-b1568484edbe | -2.5843 | -51.85423 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3e9d91d-4493-390c-8c34-fab19556551e | -2.58371 | -51.85792 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7069135-976a-3e5a-ae32-382043fd02e7 | -2.58163 | -51.8544 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c5dca9b-9335-39de-b170-4836ae0d181f | -2.58105 | -51.85809 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f77753a4-2692-3cec-9b1a-cef1b9f4c3da | -2.58088 | -51.85369 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f7cd7d5-57a2-3f71-99c2-a658256e1e61 | -2.58029 | -51.85737 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2c74c4e1-ed4b-3d4d-a6f1-ad2a53762de3 | -2.57878 | -51.85017 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa40fe8d-91df-3742-95a7-d01be40752ce | -2.5782 | -51.85385 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f94bc942-b75e-3ad4-82a8-2d0083c93e1b | -2.57762 | -51.85754 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2892f0cd-d767-33de-b6d4-e6b16f414b05 | -2.5742 | -51.85699 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5849e6d-7f54-3642-a732-fe632810c6fa | -2.39805 | -51.1824 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76830177-2531-3493-95f1-11ad1629f660 | -2.37528 | -50.48956 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e818df62-3fce-30c7-b8e2-89377473a6ba | -2.27571 | -50.65202 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a71a7f9b-0f5f-3192-af15-5cf5a98ef148 | -4.64104 | -50.93048 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 666ae8ae-7beb-347b-91a7-ff6114f724e6 | -4.64049 | -50.93395 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c65b763-5589-3d3f-b10b-1b59a0f5a557 | -4.61724 | -50.95163 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 930bfab8-1fb8-39c8-9728-bc765dd47450 | -4.61392 | -50.95111 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7410b60c-5932-39e1-b6fe-14e60b7c5881 | -4.61059 | -50.9506 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c16231f8-c41c-3a2d-9478-a759760df816 | -4.27404 | -50.9585 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 012c1e21-6de8-3a80-86ea-ad76916aaee4 | -4.26683 | -50.96093 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2d7d903-b45c-3008-8335-5753241e5a9a | -4.2646 | -50.95346 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05a52a8a-b0c8-346c-8813-376f1b1106d2 | -4.26405 | -50.95693 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 988d761c-5ede-3577-98e9-cef874ee6ab6 | -4.14719 | -51.09861 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31f3e21b-4405-36fc-afd5-c2032ce4797b | -4.12496 | -51.10942 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cd5d4c0-da42-33f9-9b9b-9f6aab3c9402 | -4.12441 | -51.11289 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41f80b5d-3548-3dd1-ac44-ea3ac5455f74 | -4.12385 | -51.11639 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52ee1d1e-6136-3d9c-97a6-acff4338d899 | -4.12107 | -51.1124 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 789397df-63c9-374f-a0ef-aea479a4c2f5 | -4.1066 | -51.11732 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c4d6559-8b03-3e8b-b3e0-dad010d22486 | -4.08986 | -51.12184 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2c47ea9-855f-39a0-9ceb-ff016fb2e97b | -4.08931 | -51.12534 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 110d57eb-0102-39cd-982d-252e6dafc135 | -4.07312 | -51.07624 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81622ae0-5070-3bfb-b04d-860ec11476bc | -4.06978 | -51.07573 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd2a6a13-851d-37dd-aed7-7707d6c3a355 | -4.06645 | -51.0752 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 074d0b24-47d5-30a7-bb92-66d51312ca0a | -4.03925 | -51.11737 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ad452f5-ad72-3517-91da-6aea4ec77533 | -4.03923 | -51.09597 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4473f5a-e8a0-33d6-a181-63f823e343f3 | -4.03867 | -51.09946 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99e6b482-0ff0-3357-a1aa-ecc20bab3a41 | -4.02481 | -51.20847 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa3d50fa-2c29-3c00-be40-fb709e417548 | -4.0236 | -51.00056 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2517ef1a-ed63-39d1-9e8f-50e3b2341724 | -3.93151 | -51.05069 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89537f8c-baf7-32ba-a08c-4469e6ff3c86 | -3.92872 | -51.0467 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c4ea225-b74d-319e-9b49-1e8314d55f7e | -3.92817 | -51.05017 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 515048fa-5f83-3d45-80a9-b0a95cf4fd2b | -3.92382 | -51.22879 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27410b98-d9aa-3fd3-8f00-62f310db2109 | -3.92047 | -51.22826 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ed640e3-f8ef-3444-a0f3-91314e7ca2cf | -3.91991 | -51.23177 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf214873-ef72-31fd-94de-984ee891e73a | -3.91093 | -52.21043 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 892988ec-d0b5-318a-bd94-68a53e910f05 | -3.89904 | -51.91138 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc1584d5-a7b7-3b7b-8d96-c48a01f9b259 | -3.86998 | -52.26865 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 27972cc8-6983-3489-a6cc-0a6ca71b81a1 | -3.86655 | -52.2681 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fbcd58f2-21ba-3251-883b-8391a0206aa7 | -3.83543 | -51.3847 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72e1a85c-9d0c-32be-8756-579aaf358bef | -3.83209 | -51.40593 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9db360d-393c-3a47-ab7e-31a200131002 | -3.83158 | -51.87527 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ac5c2a6-975e-3656-a72d-28ce12296ca8 | -3.83153 | -51.40947 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c76a789f-7b14-329f-9328-b9ada74b14ed | -3.82873 | -51.4054 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2773f494-2540-3057-a091-7273fc70d46a | -3.82817 | -51.40894 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README85.md)
