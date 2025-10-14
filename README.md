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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23be233a-c647-3bc2-8be8-d239ed21d055 | -10.4782 | -57.4818 | 2025-10-14 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 95c96269-a0ab-3931-b975-88ea3c45c1b3 | -13.006 | -50.8909 | 2025-10-14 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| f559598f-ffd1-30cc-ae1e-0ae03908eb63 | -7.1652 | -46.524 | 2025-10-14 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 5b206535-8e72-38a9-8276-a919820ccdd5 | -13.0064 | -50.8694 | 2025-10-14 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 215.9 |
| fc348623-ae85-3765-88bf-28c589c7cfb2 | -8.4844 | -46.134 | 2025-10-14 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 246.0 |
| 08088354-76d4-38b5-98ee-efccfbfbdc63 | -5.0994 | -43.1977 | 2025-10-14 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 9b599839-38df-3766-8937-78828d667aee | -8.5032 | -46.1321 | 2025-10-14 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| f5798d7b-b857-3ec7-98b5-3b0b828052b4 | -8.4847 | -46.1115 | 2025-10-14 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 211.3 |
| 3ed98c5b-9217-3acb-ae6c-31a7f177d0d1 | -10.4594 | -57.4831 | 2025-10-14 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| c1f7f35e-44b0-3ec8-bc86-758560f5c954 | -13.0067 | -50.8479 | 2025-10-14 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 205d10d6-0f40-3955-a71b-9277b3c60042 | -13.5145 | -50.3084 | 2025-10-14 00:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 3250a78b-d0d7-3f1a-a114-6b125922fa4d | -5.1181 | -43.1964 | 2025-10-14 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 834d3c02-abeb-3e55-8f94-8bea957eea95 | -11.7601 | -61.0743 | 2025-10-14 00:00:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| dab07962-9c83-3ea8-a2dc-4e52fd21a388 | -5.4937 | -43.0761 | 2025-10-14 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 508fcb8d-3825-3d45-9d68-690c4a57c1af | -4.6696 | -43.1326 | 2025-10-14 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| caaaccb9-c28d-30d6-a69f-c3054d215ae7 | -12.9872 | -50.8718 | 2025-10-14 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 93a0389c-c592-3aee-b7b5-a57ae890dea9 | -5.2513 | -45.2316 | 2025-10-14 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 69a65fc9-f5aa-3232-94b4-5b3643fc0281 | -5.494 | -43.0526 | 2025-10-14 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 5c5c7429-d8f6-311d-9904-de8c4fccafb0 | -4.6694 | -43.1559 | 2025-10-14 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 8ebc7604-fdce-321b-8bec-290776833018 | -8.5035 | -46.1096 | 2025-10-14 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.0 |
| eddcb6a6-8f0b-305f-944e-7833ee39567b | -11.779 | -61.0731 | 2025-10-14 00:00:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 0b05668e-9ac4-368f-bc55-5a351e4fa9d1 | -5.0994 | -43.1977 | 2025-10-14 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 35e477de-4d54-3744-9223-06a813ce0930 | -4.6319 | -45.7863 | 2025-10-14 00:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 2f267102-3321-333b-818a-ce8e02abf97a | -13.0256 | -50.867 | 2025-10-14 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 1e38d25d-dc88-31b1-a049-09307ffe4d61 | -10.4594 | -57.4831 | 2025-10-14 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| e9d59582-b1af-3903-8a7c-7a943f8f42ed | -8.4467 | -46.1378 | 2025-10-14 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| f45e9d25-b463-3431-baa3-57b1db8bbfa5 | -11.1174 | -46.0967 | 2025-10-14 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 2ac278ea-ce4c-3bc1-a7ea-5512b51a4480 | -4.6883 | -43.1314 | 2025-10-14 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 3165d603-39f7-398a-b744-813a1a1cf7b7 | -13.006 | -50.8909 | 2025-10-14 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| e1b8bebc-8054-32d4-bc62-baf49851086e | -13.0064 | -50.8694 | 2025-10-14 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 176.4 |
| ee486213-683c-35da-9857-326a30cf208a | -13.392 | -42.6978 | 2025-10-14 00:10:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 81.7 |
| eb216b1e-f984-3ffc-8761-060c70bd5ebc | -4.6698 | -43.1092 | 2025-10-14 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 330c2adb-aa5a-376f-843f-2e5019bfc5ec | -8.4464 | -46.1602 | 2025-10-14 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| dd18b360-a09b-3354-bd2a-26aad72f5bbd | -5.494 | -43.0526 | 2025-10-14 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 902832e1-0ac5-3a73-b699-2c71b11e3ad1 | -11.1178 | -46.0739 | 2025-10-14 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 9be913ab-94b2-32f2-8e17-5c63a482aefd | -4.6696 | -43.1326 | 2025-10-14 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| ea0a6f1a-4e66-32da-b24c-83b7b7e34fff | -5.5125 | -43.0747 | 2025-10-14 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| f97593d4-0a4c-3e8c-ac8c-69ed1a740c40 | -4.6509 | -43.1337 | 2025-10-14 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| f658fab4-4c51-39d2-88b3-dd19d2dacbbc | -13.5145 | -50.3084 | 2025-10-14 00:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 103.6 |
| d1cfd330-915a-3a7f-b5a4-f52b52908b5d | -5.4937 | -43.0761 | 2025-10-14 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| dc2781ca-8586-3521-8d99-afe0882396ac | -11.7601 | -61.0743 | 2025-10-14 00:10:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 583c9288-130c-39fa-80a7-ebe7db5ac2ed | -5.0992 | -43.2211 | 2025-10-14 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 7e0d0da8-d86b-3b4a-b87b-8ef1c3ef9f2d | -5.1181 | -43.1964 | 2025-10-14 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| ea73d58d-c5ce-37c3-baad-3aae7dca7e14 | -13.0252 | -50.8885 | 2025-10-14 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b4c9e85d-bf02-395f-8666-e42096e632ad | -10.4594 | -57.4831 | 2025-10-14 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| a588d860-096f-3bfd-b5c4-5509bbfe1e84 | -5.0994 | -43.1977 | 2025-10-14 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| a98dd992-abae-30bb-bb9c-99f44b0f67d1 | -13.0067 | -50.8479 | 2025-10-14 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 125029d0-f8bd-35fb-ac19-ee99111d9a7a | -13.006 | -50.8909 | 2025-10-14 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 5bb43467-40e6-3f9f-bc6a-6b43276789d9 | -4.6696 | -43.1326 | 2025-10-14 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| c1e5ab86-5e6e-39a2-96b8-5717ed32a697 | -13.0064 | -50.8694 | 2025-10-14 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 1045ed4d-62d7-30d5-87d0-4fef1aaebf79 | -13.0256 | -50.867 | 2025-10-14 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 133.3 |
| e1da0cbe-7bbf-3fac-8a14-b917318b74f0 | -13.0252 | -50.8885 | 2025-10-14 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 60f4707f-9f69-3d45-867d-b739200d2c31 | -4.6694 | -43.1559 | 2025-10-14 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| db8db873-6e0c-30ba-8b32-fc58c4908fbc | -13.5145 | -50.3084 | 2025-10-14 00:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| b6fccad1-0b9e-32e8-8772-316a465f6644 | -5.1181 | -43.1964 | 2025-10-14 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 0272e3f2-5826-3deb-8ae4-173db39cfd98 | -5.0992 | -43.2211 | 2025-10-14 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 754a9a56-2715-34ac-b4c8-d8f1ed362059 | -4.6509 | -43.1337 | 2025-10-14 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 22380a57-54af-3fc6-a8ee-4c733dbdeed1 | -5.118 | -43.2198 | 2025-10-14 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| eae5493d-5b77-3e9c-84d2-e216309802a5 | 1.1135 | -50.9776 | 2025-10-14 00:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e03362b7-9632-3d92-a16b-ba9732a8d2d2 | -4.105 | -50.0436 | 2025-10-14 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 6a16ccb2-79bc-3d64-adf4-e3d5fb9c04f6 | -4.6883 | -43.1314 | 2025-10-14 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| c5e48fb5-d09a-33d7-bcc4-873e335e5867 | -7.1652 | -46.524 | 2025-10-14 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 12fcc5bb-14ed-31cd-85d9-377f81dffaa9 | -11.7601 | -61.0743 | 2025-10-14 00:20:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 42ef62ca-431b-3970-91b0-a134e514c496 | -4.6698 | -43.1092 | 2025-10-14 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| a7f804b7-d35d-36f8-855d-a8045cd86212 | -13.0256 | -50.867 | 2025-10-14 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 74add3d2-b768-3cb3-af8b-3a918666a69f | -13.5145 | -50.3084 | 2025-10-14 00:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 17c5ddf2-d876-3393-9f41-89bf160721d4 | -13.392 | -42.6978 | 2025-10-14 00:30:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 60.4 |
| 97f13a73-517d-3d0b-bfb4-6de05af09a90 | -4.1048 | -50.0647 | 2025-10-14 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 82e98f56-0100-3141-b032-7161d89ff0b8 | -7.1652 | -46.524 | 2025-10-14 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 29880bb4-2df5-3b7f-ac6f-767d935c67a6 | -4.6698 | -43.1092 | 2025-10-14 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 95c837db-e3a7-3a3d-bafd-9f9f0c9c0ae9 | -4.6509 | -43.1337 | 2025-10-14 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 050750d6-96d8-3ba2-aa9f-7f9f5ac7d086 | -8.5035 | -46.1096 | 2025-10-14 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 20f72992-8e5e-39d9-8a23-d7c45a98c924 | -13.0064 | -50.8694 | 2025-10-14 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 4ad40292-c182-3b8e-897d-eff013b858ae | -8.4847 | -46.1115 | 2025-10-14 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 6e12dc6c-aa4f-3df5-9e95-f0bcec04a62b | -4.6696 | -43.1326 | 2025-10-14 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 26113b76-c786-3bfe-b7a3-cfffc50d0e92 | -13.006 | -50.8909 | 2025-10-14 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| db201d0c-338c-3881-ac45-3ff0cada6126 | -5.118 | -43.2198 | 2025-10-14 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 30e46151-1f7a-34e5-bda4-fa1a42688af8 | -4.6883 | -43.1314 | 2025-10-14 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 60f83958-b347-3e12-a636-9b5ca2a31fa1 | -13.0252 | -50.8885 | 2025-10-14 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e82e7fa6-9ed4-3385-b611-1cde62b443fb | -8.4844 | -46.134 | 2025-10-14 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 3060dd2f-8454-3fcf-a439-af21ab133e9e | -5.1181 | -43.1964 | 2025-10-14 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 7a781950-b72a-3303-9475-fb7a4da6fff6 | -4.105 | -50.0436 | 2025-10-14 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 06d8bc66-5ba5-399e-a999-3f113bf72822 | -5.0994 | -43.1977 | 2025-10-14 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| f07032a9-2144-337b-9ab4-3d7e9d785371 | -5.1181 | -43.1964 | 2025-10-14 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| df26de0b-4752-3ccd-a3a4-cecf9ccd96b2 | -4.1048 | -50.0647 | 2025-10-14 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 79913dd3-a327-3412-a54c-9482e1cf3a19 | -7.1652 | -46.524 | 2025-10-14 00:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| aa657b7d-8873-3e0d-b2c3-bd9043c2bc54 | -4.1235 | -50.0428 | 2025-10-14 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 7257d59d-42c1-3e56-802e-e4c634c110d7 | -5.0994 | -43.1977 | 2025-10-14 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 5b555408-185c-38c6-bc1a-da4497489673 | -13.0256 | -50.867 | 2025-10-14 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| d34e767c-56b7-3971-bd6d-f90095084766 | -13.0252 | -50.8885 | 2025-10-14 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 4b41fe98-7495-39ba-916d-67d71a54e481 | -4.6698 | -43.1092 | 2025-10-14 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 36c0ea99-451c-379a-99b2-05bcfc5f475d | -13.0064 | -50.8694 | 2025-10-14 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 583ad514-53ce-35e5-91fa-b84b57fd3fb2 | -4.105 | -50.0436 | 2025-10-14 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 46500c7b-032b-39c1-a4b6-142bd614c1e8 | -13.5145 | -50.3084 | 2025-10-14 00:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 1571b108-19c1-3bd4-abc4-2bb52075d6c6 | -4.1233 | -50.0639 | 2025-10-14 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 9ff97227-17db-3c67-b663-c991b32146a0 | -10.1023 | -36.3642 | 2025-10-14 00:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 9cfb06a5-4428-3b6d-83d9-502934a215e0 | -7.8086 | -46.02 | 2025-10-14 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 1a119dfb-57f8-34df-b57e-7ffcd41ace70 | -4.6696 | -43.1326 | 2025-10-14 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 0268c182-cca2-3c50-8bcb-f1a2df008612 | -5.0992 | -43.2211 | 2025-10-14 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 25eaedf1-3c01-345b-876e-7cdf2230e6ae | -4.6694 | -43.1559 | 2025-10-14 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |


[Clique aqui para ver as próximas entradas](README2.md)
