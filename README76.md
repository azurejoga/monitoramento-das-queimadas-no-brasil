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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3001ddda-fa46-3736-8aaf-a90d33b00be1 | -3.07656 | -54.17522 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ee46d7d8-8122-3e08-8fe9-23d142a03eb4 | -3.07353 | -54.16685 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac7afbfa-a999-33bc-86b7-ed7030395710 | -3.07295 | -54.17073 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5c245318-e127-3d4c-9309-61a8cb7835bb | -2.33757 | -53.90753 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cec17102-5103-35e4-a934-95cfaefc2ad4 | -2.33715 | -53.90717 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a45a312f-cd79-3f27-b232-cfef90c3b488 | -2.33336 | -53.90684 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1409b6f7-9f5c-34f9-923c-6f9dde7997f1 | -2.32016 | -53.93618 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0f68483-4eb0-3a71-a441-84842a5578b5 | -2.28429 | -53.80402 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4683a954-158d-3768-a3ad-1d13404521c2 | -2.28055 | -53.77132 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5c49b55d-9be1-349a-99e5-950f63e2b7b4 | -2.28005 | -53.80337 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caee6929-78b4-35ab-b4ff-a5724374e81d | -2.27996 | -53.77526 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fb615d88-54ba-359b-ae37-fd0332833bc7 | -2.27946 | -53.80722 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6445f347-3bb1-31b4-9605-f15b9932f5a8 | -2.27936 | -53.77919 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 312f05e4-62cf-3cf3-9c79-a41b7ea88bf5 | -2.2757 | -53.77461 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cdeea6a6-19ef-3b9a-983f-bc5451126986 | -2.27511 | -53.77854 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aaab9e46-bf56-3459-b4e4-d25370c0cb7a | -2.27452 | -53.78245 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b16944bc-20c5-38c9-93ec-9c50ef103004 | -2.27393 | -53.78635 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 82dd3c4d-ccad-3b2f-a173-4185599fbbc7 | -2.27334 | -53.79025 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 186d33cd-e273-32d3-b150-b627d9a172dc | -2.27146 | -53.77395 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8e8defdf-e56e-3f6e-81fb-af8b5c08353a | -2.27086 | -53.77788 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b2f2eb66-c615-3c77-809a-ecbe0e85f5e0 | -2.27028 | -53.78176 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 803e9801-c536-34a0-b7fd-9f8229dbef61 | -2.2697 | -53.78564 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 6daaf217-193c-3ddb-93c6-2e1117549ec2 | -2.26911 | -53.78952 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| ba233a31-88b2-35f0-8d22-7ece6e4affe2 | -3.58973 | -54.56569 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c35b4ef4-9782-3756-b7a9-b784c14c3e77 | -3.58769 | -54.66184 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a5ef587-0c8a-3e08-ac6c-3c9ac770f723 | -3.58562 | -54.56506 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5765288d-ec2c-3bad-afac-d7a2f57dce6f | -3.5836 | -54.66128 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e314f7c7-1c60-345d-9b56-e01c39cfdf27 | -3.57026 | -54.66661 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b894efa-c2c4-3f96-8f63-576e41a8609c | -3.56916 | -54.67384 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12e8c099-d318-3b37-ae33-b7941c876325 | -3.56861 | -54.67748 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec2cc656-de48-3e48-a50f-8c975173bfec | -3.56618 | -54.66598 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df887305-2b12-38b6-b9d2-c12182be1141 | -3.56563 | -54.66961 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb68f63b-7604-3390-ad70-8b5eaf0ce7b6 | -3.54753 | -54.76188 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37264b8e-3d21-3bc7-a999-b772eeab2a82 | -3.54346 | -54.76137 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3547268d-2be5-353d-812b-8b3081693254 | -3.52724 | -54.67525 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ea0b879-173e-379a-8bae-ca87b62b2d28 | -3.5267 | -54.67892 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17c6dee4-5118-3b3d-b8b4-07d73571fca7 | -3.52263 | -54.67823 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cdcfeee-ae2f-3e15-816b-14856a6cdccc | -3.47667 | -54.57534 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0955be7e-eca3-3301-bab9-8cf173d271c3 | -3.47312 | -54.57105 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aa1c024-de8b-3feb-bd03-e5226c76ddac | -3.47257 | -54.57471 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79eca108-5fd1-3574-80d7-ebb8d96b184c | -3.42935 | -54.58345 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e35aeeda-41c5-3bbb-a713-1e4178e030a6 | -3.42881 | -54.58706 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c152d91-4fb8-3494-be48-db6597707429 | -3.42605 | -54.58357 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a9d59aa-c062-3dc6-ac52-939cedc32975 | -3.42548 | -54.58719 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31def8e0-a445-3208-a471-cba9d59c7e0e | -3.42524 | -54.5829 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5cbcfd9-6f15-30db-95e5-1e307f452da8 | -3.42471 | -54.58653 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64c9977e-f9d7-35d8-8ee8-2d5f17bfcdc0 | -3.41148 | -54.48748 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 959cba3d-27bb-3ee1-9068-19e799a67541 | -3.41091 | -54.49117 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1ea68119-1f8f-35a2-8dd8-78c4464724fc | -3.41035 | -54.49485 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8d794f65-b2b9-377f-9bcb-e08c55407bf7 | -3.4068 | -54.49051 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ccd173f-e840-3582-8f68-6d1096ad3d2d | -3.40624 | -54.49419 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 594bdda7-cda7-31ce-a211-d760c184fbbd | -3.15804 | -54.95905 | 2024-10-28 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e09a6cf-ac73-3b70-bc9d-9d40ee48f25a | -2.95423 | -54.68378 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d44576a0-e7ea-30aa-9b94-44400d774e97 | -2.95072 | -54.67971 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f586548a-28a9-3703-b347-de6fd9e6a154 | -2.95018 | -54.68322 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c15ca94b-38fe-38da-8351-6f1ded7a9e55 | -2.45776 | -54.67966 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 502f36cb-b198-3f41-9afe-b3d7005a92ce | -2.93712 | -54.35726 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e2d8f94-bc90-3d26-9fb3-1c3bacb1f74a | -2.87573 | -53.96558 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f205c29-4fd4-39ea-a3b3-d15318342c8c | -2.87542 | -53.96548 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 936c5ac3-fcd7-39ec-a6b2-70f35c2d7083 | -2.8715 | -53.96493 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfb0c0a8-1739-355c-b753-1e00060491af | -2.8133 | -54.09026 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2aa6892-fa34-3644-a449-d560521632d1 | -2.81097 | -54.10549 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b13318be-afec-3487-af01-7f37ad1f1649 | -2.80678 | -54.10485 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41084a62-ec23-31d7-8d9a-25ffc028497f | -2.80434 | -54.09278 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42d253a6-9656-3e74-8cfe-a609ef55aa1f | -2.80259 | -54.10421 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 996be731-c2cc-35f6-a3fb-d94944485746 | -2.79031 | -54.15659 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c5fc747-30ab-3c97-b68f-864c1deadcf0 | -2.76568 | -54.0359 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a33af00f-2386-3d09-8d3e-0914f794a29d | -2.76147 | -54.03524 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c392c58-d099-34c0-b75b-ef936345f8b2 | -2.7531 | -54.03514 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 953d6e69-a010-30db-86b2-57d6e8c22861 | -2.75249 | -54.03781 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8abef4c3-c17c-37b4-a28c-0551479c12d4 | -2.74889 | -54.03451 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72a1feef-0b37-363a-9f00-5f79de8fe1f6 | -2.74886 | -54.03329 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47c2006f-9574-3883-ab01-aa9f55c72226 | -2.74829 | -54.03716 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 877ac12b-2d76-3323-89b7-1eea4e9743d7 | -2.6453 | -54.29211 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 25eaee89-609a-35b5-9f30-6917aafe3003 | -2.64474 | -54.29579 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 006814e8-4e2a-35ee-a1a6-47a99c9b71eb | -2.64118 | -54.29145 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7185a410-7de9-3b24-88aa-35954ea17da2 | -2.64062 | -54.29514 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aab57401-1351-32b4-8c8c-ac729cd27abe | -2.64006 | -54.29882 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17d92a07-00c0-3a0e-a40e-7df355c8cda1 | -2.63594 | -54.29817 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a4e8c4a-9ad0-32a4-b482-8a50de4b0959 | -2.63539 | -54.30184 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3db56c4-2272-3122-8285-48f1fd87f653 | -2.61072 | -54.00677 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49f1e70f-2ed0-3414-9c2a-9bad11e6dfa5 | -2.56942 | -54.02391 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b5fc8a5-6811-36d4-aa30-282e6a63eaaf | -2.56856 | -54.17022 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fffe8ec6-012a-3cd6-ad16-58157dccde02 | -2.56799 | -54.17398 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e836925b-f6b6-3819-8b51-6cc08bf6045d | -2.56638 | -54.01563 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c27bd303-d37d-3244-98ab-21b106d6c43b | -2.5658 | -54.01945 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2273be3c-88bf-3273-af0f-d8998870441a | -2.56523 | -54.02327 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f45c0380-611b-3064-9740-6b983a0dd58c | -2.56275 | -54.01118 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f12ac9f7-23f8-3193-bc29-f532799e31ce | -2.5616 | -54.01881 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4822d4ed-3c8c-3363-9738-f3401220895c | -2.55855 | -54.01054 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 147d8c4a-a931-3cbd-8747-7b5626fff1c2 | -2.55798 | -54.01436 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d2c53cc-0dd9-3d75-951b-0301d5705c15 | -2.5574 | -54.01818 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e98d830-43e6-34cc-9155-466233f3a3a0 | -2.54291 | -54.00014 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b3f8f74-d0bc-378d-a136-137241281429 | -2.5428 | -54.00127 | 2024-10-28 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d7a7d62-38c0-35b6-bc83-179c88ef79a4 | -4.11399 | -54.28852 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4a632d6-17e7-3775-99bf-a781705db581 | -4.11378 | -54.28955 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf8b2272-2911-38bd-a5df-11eca81999d3 | -4.11343 | -54.29229 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a45943a-9998-3f10-9223-4400bc89d948 | -4.10086 | -53.94234 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a21d4b6f-ff41-37b5-b737-e4949c07bdc7 | -4.09714 | -53.93762 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6ace28e-79d2-31c2-8d61-5ac6287b9818 | -4.09652 | -53.94182 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README77.md)
