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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86929267-b09f-3339-b00e-d7a8ed5c42b1 | -3.12308 | -50.4243 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f040131-c6bd-308d-ad65-ec43b382dd52 | -3.07587 | -49.57804 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9955168-a8f7-3c76-9f6d-2d120a988943 | -3.07378 | -50.49676 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bfff2cb2-8edc-3b21-b9ec-0b77c2b24124 | -3.07319 | -50.50047 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e78bc9a7-105a-3f7e-813e-0c6c2bab8c37 | -3.07261 | -50.50418 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1621b68d-0124-3dea-912b-ff2ce8d8b06d | -3.07252 | -49.57752 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f807cad6-45c6-38bd-bdcd-e030b8129f0d | -3.07202 | -50.50788 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4c1bd53-d271-3f24-be75-afea58a85a97 | -3.07196 | -49.58104 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fa08c7f-ca54-3847-aea3-012d9fbe1619 | -3.07034 | -50.49622 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5687af22-70a2-3917-a13d-0780dafaeb0b | -3.06976 | -50.49993 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| caef925c-048a-3f7c-ad11-4fab9fa5019e | -3.06682 | -50.36324 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a2c3c75-60b3-3239-ba0b-fdd888ef77f2 | -3.06407 | -50.49141 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0084b6b-c453-3ea9-a731-a5f571587db5 | -2.96754 | -50.41602 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cbc936d2-e648-3d20-b087-a248b774d68f | -2.96696 | -50.41971 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f2788d84-820b-3eaf-a15f-f21eed895797 | -2.96579 | -50.42709 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2f556d30-1fde-3033-b20f-081bba63108c | -2.96412 | -50.41547 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36d6526c-4ec0-33de-941d-0fb2e53cafc4 | -2.96353 | -50.41917 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 45fdb2fe-3182-3767-bb51-927f00827fd5 | -2.96236 | -50.42655 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| baed0914-ce30-3fc8-bc2f-e23ac0b45657 | -2.96145 | -50.52147 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5034f0a0-3a45-3bd0-b08b-848101acddff | -2.96069 | -50.41493 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5728b8e7-69ee-3852-9866-ec49f602fee0 | -2.95952 | -50.42232 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1d8de77b-e738-3715-89b2-3e78617e9ec2 | -2.95893 | -50.42601 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2d8eae27-e22f-339c-b43e-802cc7e85dcf | -2.95835 | -50.42971 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f3189c0d-e4ab-3465-9c51-a6c279b47dd9 | -2.95742 | -50.52465 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f76962c7-2858-3e9c-ace4-fe08085a0c5e | -2.95609 | -50.42178 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 65c520f4-8444-36e8-aecb-415a922519a8 | -2.95551 | -50.42547 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e0f660aa-8297-3761-985a-f0d5cfb50b89 | -2.95457 | -50.52039 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8f2af9e-d715-3a03-b045-bbd2cab59bf0 | -2.95398 | -50.52411 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1738680-24ab-3a1f-9db7-45c82cda19ea | -2.95339 | -50.52783 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1bbe511-17e7-3ac5-bc05-cb3c825a42eb | -3.60888 | -49.89319 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fa17693-8dbd-34de-b77a-1f2094374b3f | -3.5103 | -49.61319 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c27916e5-b097-390f-b66e-6d491b405e00 | -3.5098 | -50.27849 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a9d85c1-8148-3220-af26-2f2c8cf7b720 | -3.50751 | -49.60917 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36ac351e-c362-3c8f-903f-2dc07947a640 | -3.5064 | -50.27796 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f4a4eff-ffa5-3f43-9a5c-6e121bedd2b1 | -3.50583 | -50.28159 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb727971-8e88-3143-83c0-185456e5069e | -3.48409 | -50.48434 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19aec274-58bb-36d0-a74e-2fbaf7edb313 | -3.48067 | -50.48382 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70cf2493-6e6f-3241-9f72-67c42853523e | -3.44937 | -49.82397 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a666a5a0-4232-3565-b211-70c6bfbc5c3a | -3.43797 | -50.35678 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 533aa8b7-1db2-3a79-bbdc-d924bdaa70de | -3.43789 | -50.35649 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f86bc26b-8a3b-34d6-8586-fa0fd8a26410 | -3.43448 | -50.35596 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3daef7d-f833-307d-a623-9d26d811c210 | -3.41964 | -50.38357 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ef0d142-2506-3f35-9f53-64eeb07920c9 | -3.41623 | -50.38304 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1078d26-c594-3903-89cb-c11fc7f9d38e | -3.41536 | -49.5302 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b9dc579-468c-367f-b614-a2a4b5ad8dfb | -3.41202 | -49.52968 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 437a6798-cbe3-3dba-9dc1-e00137d73d24 | -3.40868 | -49.52915 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b329a658-87a6-330e-9917-6bcb78b03d07 | -3.40612 | -50.33651 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b70917a0-0f11-317c-94de-a28cbdec7e51 | -3.40554 | -50.34015 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6c01bab-c245-3890-b501-60ed82d2373d | -3.40271 | -50.33596 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb18635c-5604-3980-a9e0-2ba9ee9f7c47 | -3.40213 | -50.33961 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8b93a32-d539-3c6b-bb5a-5be886d2597e | -3.3993 | -50.33541 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a69059fb-1f58-3d3e-b552-baf19a41ffd8 | -3.39872 | -50.33907 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a9bb671-9349-373e-8e60-256a8eb3201b | -3.3959 | -50.33487 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 182ffd56-e0b8-374d-b19b-dcbe1e02a876 | -3.39416 | -50.34579 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68a9cde6-bdd2-3fc2-8a3a-bcdc46f3443a | -3.39076 | -50.34526 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d30bc31-3736-32f1-9def-d94ca8be8076 | -3.38735 | -50.34472 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b40027ae-f862-3bd3-b5ad-966477e0b734 | -3.37637 | -50.39175 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a61072e3-3966-3393-b396-7207d1133cd1 | -3.37578 | -50.39541 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 164b632b-ff05-342d-b0d3-cc73f7074971 | -3.26454 | -49.1356 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6a1a3cc5-7b74-3ef3-a424-3e992f26052e | -3.23291 | -49.12 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca1b9505-c564-3d68-9ee6-24398207efb2 | -3.23068 | -49.11255 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b8ee243-335c-3510-9c5e-d9bf119707fe | -3.22348 | -49.11497 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d88dc5d1-9c81-3cd8-837c-15a562470961 | -2.8553 | -49.13537 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8c5dbde-d144-3537-b34e-8e4bad23669a | -2.81611 | -49.25399 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8328c7a-44bc-3df4-b6a7-533b70899c35 | -2.80889 | -49.25643 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64c599a0-b920-30d8-8177-3169d32968f7 | -2.80834 | -49.25991 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa82e060-4f1a-3505-9032-aab95efb4ee2 | -2.80831 | -49.23849 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b33e16db-0859-3ac1-990b-d0eb4d7b3bd7 | -2.80776 | -49.24197 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a081fd9-3647-301b-8615-dbca2320a86b | -2.80611 | -49.25242 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad2022ef-b9d2-3975-8130-d7e37fe013d7 | -2.80556 | -49.25591 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e7f2219-bd9b-35b9-8a0e-acd0073a2f3a | -2.80497 | -49.23796 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 450b1ac7-872a-3bfb-b7c0-59e6b3e79f7d | -2.80442 | -49.24145 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb25f9cc-500d-3fdf-a393-2b4027be8893 | -2.80277 | -49.2519 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84f837a1-a275-323d-8b44-16c64c0f635b | -2.80222 | -49.25538 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6141a14b-4d1b-34d6-b031-16778779d321 | -2.80054 | -49.24441 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e098842b-69e1-32cf-b431-06585feb910f | -2.79999 | -49.24789 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3030fa34-5607-35e5-aa36-f83be00a6f7a | -2.79944 | -49.25138 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ca433d3-c854-3232-9092-d78399b8093e | -2.79889 | -49.25486 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dc5d8fa-c616-3426-940c-aa84d7e302b1 | -2.79665 | -49.24738 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f81c088-68cb-3f5f-a9b0-b203a426f635 | -2.7961 | -49.25086 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 461ca8bd-6971-3584-b66d-573520c4b98b | -2.79555 | -49.25434 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbee0c9f-ed20-3aad-8944-73d7acbb88d2 | -2.79108 | -49.23936 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21e08b25-2ac4-3efa-b105-23a71964c160 | -2.78218 | -49.23083 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53f9bfce-46f9-3d33-8ecf-5282cc7793dd | -2.78065 | -49.34856 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 674eb0af-667a-3e9b-b305-9dc0d6c212d9 | -2.77885 | -49.23031 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70657651-258b-3c1d-942f-a3230d7c40fc | -2.75279 | -49.30841 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8333679d-38f6-35e9-88c2-a11175cff894 | -2.75224 | -49.3119 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 97f9fbf4-fd53-38ae-b664-43ea726129ca | -2.74945 | -49.30789 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1f380ca-3257-390a-ae29-506f06de789b | -2.7489 | -49.31138 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 961a68a1-9c1a-3fea-9644-0123dd19e842 | -2.69772 | -49.05744 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da3739a2-1e94-3a66-973f-909cff30694c | -2.69717 | -49.06091 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d97eea78-66cb-36fc-98e0-b3b95f51ae6a | -2.69662 | -49.06438 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 599dbca8-f6ce-3bd9-b61c-e9350ff99abf | -2.69494 | -49.05346 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32a06dee-8e3f-3c55-8b29-8eb2afba59e9 | -2.69271 | -49.046 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e60a26c8-25be-3ba9-a54a-7fa8006bd987 | -2.69216 | -49.04947 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b198091a-6698-3eaa-b9a8-63a6123cefed | -2.68938 | -49.04548 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90e58611-2000-3d5d-9cde-179227e3fff7 | -2.6866 | -49.0415 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d399230-a567-33bf-b280-878e04398b33 | -2.68605 | -49.04496 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 066828d8-c5c8-3eac-8e67-589d6bd0fe60 | -2.6855 | -49.04843 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a69f9b1-d317-3c3f-8866-7c73a4c83e9a | -2.68273 | -49.04444 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README62.md)
