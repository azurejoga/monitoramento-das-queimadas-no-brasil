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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46f599a1-1045-3baf-a8d5-0135e5094471 | -22.7433 | -44.8035 | 2024-09-27 07:47:11 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.0 |
| c11712e2-78d9-3711-b16c-d9582e0e0484 | -8.9793 | -67.3728 | 2024-09-27 07:55:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| d41f1fbb-b922-3995-85aa-b7a694aa55e8 | -8.9977 | -67.3909 | 2024-09-27 07:55:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 477ddb48-d8af-391c-a992-506444ebc8ae | -8.9978 | -67.3724 | 2024-09-27 07:55:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 211.0 |
| 68405315-749f-35a0-9445-4b0de96f693b | -8.9978 | -67.3538 | 2024-09-27 07:55:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 766cdee7-2c9a-39f2-9df6-fb1ec00ffd31 | -9.0162 | -67.3904 | 2024-09-27 07:55:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 768853bf-ed9c-394f-8237-7c2042fae813 | -9.0163 | -67.3719 | 2024-09-27 07:55:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 94630403-623a-3b4d-a936-0085dd8dbab1 | -10.0139 | -53.4464 | 2024-09-27 07:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 08c2b9a9-9ab8-3467-a6f2-4ad60bcc38e3 | -10.0327 | -53.4448 | 2024-09-27 07:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ab746ef2-0c26-3bdc-924b-4efd1a2459a6 | -11.1951 | -53.8965 | 2024-09-27 07:56:11 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 0b6d0b1a-c68f-31a3-a2d2-689c8f6e4e9d | -12.7868 | -54.0275 | 2024-09-27 07:56:20 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 2e10a9df-ccf9-358d-9df8-d8299ab450f9 | -14.8443 | -51.4616 | 2024-09-27 07:56:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 5a6650c6-db0a-3177-9cf3-fda51de7b917 | -14.8447 | -51.4401 | 2024-09-27 07:56:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 776697c0-c372-39d7-8214-872e0ba6acf1 | -14.9224 | -51.4292 | 2024-09-27 07:56:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 677dded0-62b7-3a6a-a83e-ac71ad564f91 | -14.9228 | -51.4076 | 2024-09-27 07:56:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| e273c057-e9da-3bd4-b7ae-e6ada15aa768 | -14.9418 | -51.4264 | 2024-09-27 07:56:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 04b341b1-bef7-361e-8373-876b22fcfd53 | -7.5888 | -60.5785 | 2024-09-27 08:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 153.6 |
| f724aa75-f76d-344d-b21f-3a0e9284299a | -7.6072 | -60.5969 | 2024-09-27 08:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 2b065072-37e9-392f-9efe-f6ef78cca612 | -7.6073 | -60.5777 | 2024-09-27 08:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7ff1e067-4147-3081-adb9-7725a562ffa6 | -7.5703 | -60.5984 | 2024-09-27 08:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| aae1238b-1543-34ca-99d5-9cff8cdee560 | -7.5887 | -60.5976 | 2024-09-27 08:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.7 |
| cd30f4e6-6781-33ba-8d73-e4c6400a6b83 | -8.9977 | -67.3909 | 2024-09-27 08:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 1933011a-1e6f-3ba5-9d44-a7e384fe7199 | -8.9978 | -67.3724 | 2024-09-27 08:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 217.8 |
| 0fb92821-ee6c-3633-b5ff-ea1db3780454 | -8.9978 | -67.3538 | 2024-09-27 08:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 4038efd8-bae3-3e0e-ac32-26f2fd832837 | -9.0163 | -67.3719 | 2024-09-27 08:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 3eca47d8-acd3-325f-9e52-47149f8941ac | -10.0139 | -53.4464 | 2024-09-27 08:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 034ccbfc-547f-3556-bc9c-3d7ececcc2c7 | -10.0327 | -53.4448 | 2024-09-27 08:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| aae5028a-3a51-34d8-b77e-c109c9ede57a | -10.0329 | -53.4242 | 2024-09-27 08:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 59844772-3f5a-326b-94f2-81dc6cec5584 | -10.0515 | -53.4432 | 2024-09-27 08:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 2c3e75f9-7fdf-34b4-bb81-045d3636d51c | -11.1951 | -53.8965 | 2024-09-27 08:06:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| d3966b41-2994-36e3-8a51-14395cb1437b | -12.7868 | -54.0275 | 2024-09-27 08:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 38f6f3b0-2100-3c05-b4bd-eeccf917d5a7 | -14.8443 | -51.4616 | 2024-09-27 08:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 2e173b20-818e-33bb-ae2e-8ac06fdd5d35 | -14.8447 | -51.4401 | 2024-09-27 08:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| dfc13c35-9e52-3814-bc49-380fdcaa1db5 | -14.9026 | -51.4534 | 2024-09-27 08:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 02622259-a4f6-3578-b2c4-08f3a0a73b85 | -14.903 | -51.4319 | 2024-09-27 08:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 336cc7cb-98b6-3bad-9378-a43d1d64d990 | -14.9034 | -51.4104 | 2024-09-27 08:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 6da82969-d41e-3c2b-b9ac-e52c796a5322 | -14.9224 | -51.4292 | 2024-09-27 08:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 135.9 |
| f2d67be2-7ce5-385c-97c9-0c14d193af80 | -14.9228 | -51.4076 | 2024-09-27 08:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 4c363355-cee5-3dbe-8308-f47d46320f1c | -14.9418 | -51.4264 | 2024-09-27 08:06:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| d6c29868-9246-334f-99fd-fad1e027000c | -7.5703 | -60.5984 | 2024-09-27 08:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 831dba96-a06f-3cf4-94fc-80e9d8945393 | -7.5704 | -60.5793 | 2024-09-27 08:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 2f96fcb2-98ee-3be6-a18d-098505932394 | -7.5887 | -60.5976 | 2024-09-27 08:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 169.1 |
| 66455dd8-7456-3817-bd78-b41b2d8a5a6e | -7.5888 | -60.5785 | 2024-09-27 08:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 178.9 |
| de1f436f-395c-35f5-a959-eb1da6c6f350 | -7.6072 | -60.5969 | 2024-09-27 08:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 28628d3c-c6fd-3c7f-bdc9-3a2090966f87 | -7.6073 | -60.5777 | 2024-09-27 08:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 1f2e5c5d-845a-368d-8eaa-a0037b5138c3 | -8.9793 | -67.3728 | 2024-09-27 08:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b0000bfc-e23a-3478-9ea9-8e416310a44b | -8.9977 | -67.3909 | 2024-09-27 08:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 9a1b0a9c-f53a-3c76-a9d4-197c3801f0b1 | -8.9978 | -67.3724 | 2024-09-27 08:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 204.6 |
| 7faf1836-7c78-3443-a4f2-579e15f85b7f | -8.9978 | -67.3538 | 2024-09-27 08:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| be58954a-73e1-3cc9-81bf-c6b20fa8b182 | -9.0162 | -67.3904 | 2024-09-27 08:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f47fdabd-9680-3e1f-b3d8-23880c437e21 | -9.0163 | -67.3719 | 2024-09-27 08:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 52769bb5-2296-3e1d-91f2-42c429a59d19 | -10.0139 | -53.4464 | 2024-09-27 08:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| c7b033ff-881b-39c3-9272-9cc7bb3f1844 | -10.0324 | -53.4654 | 2024-09-27 08:16:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 05a83885-9143-3e4d-bbfd-bab69a835591 | -10.0327 | -53.4448 | 2024-09-27 08:16:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 9083021e-27e4-35ed-93d8-680670fae6d4 | -10.0329 | -53.4242 | 2024-09-27 08:16:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 3006240b-a68e-3cdd-9f0e-943b160d0330 | -10.0513 | -53.4638 | 2024-09-27 08:16:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 338327c9-d729-30ae-a8cc-2b1eb5addd36 | -10.0515 | -53.4432 | 2024-09-27 08:16:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 23c506ce-fc16-3bdc-8c5f-07e0252cdc22 | -12.7099 | -54.0769 | 2024-09-27 08:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 128e6ba9-ec4e-35ec-8ff8-93568f053eef | -12.7868 | -54.0275 | 2024-09-27 08:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 85eb21c8-24f8-3425-ab92-a0d02298f077 | -14.8253 | -51.4428 | 2024-09-27 08:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ad39f2b8-71e2-3d5e-8977-4a251cda477d | -14.8443 | -51.4616 | 2024-09-27 08:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 9adba11d-06e0-3498-8cb6-481f149c429b | -14.8447 | -51.4401 | 2024-09-27 08:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 212.9 |
| 4e277ebc-4c03-305b-b723-22b60d57d53b | -14.903 | -51.4319 | 2024-09-27 08:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 165.8 |
| e4650e9b-ce74-3362-8634-d793555d7a28 | -14.9034 | -51.4104 | 2024-09-27 08:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 291.7 |
| e37c56ba-1118-38ab-90a6-fd126dc4234c | -14.9037 | -51.3888 | 2024-09-27 08:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 665fe43b-d346-38e1-998b-744546b350f0 | -14.9224 | -51.4292 | 2024-09-27 08:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 187996dc-b6c7-3c29-a9ae-ab1348fddaa7 | -14.9228 | -51.4076 | 2024-09-27 08:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 77d85fd0-9219-3c79-ae57-9ff4eb493823 | -14.9232 | -51.3861 | 2024-09-27 08:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 5ab3a089-71eb-3295-9556-40e00051d002 | -16.0993 | -51.9465 | 2024-09-27 08:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 2ab72ea1-b91b-343a-b48b-3d40ef07c70f | -6.253 | -62.4671 | 2024-09-27 08:25:42 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6e13e1d7-210d-3e08-9e3d-1d638da96b91 | -7.6073 | -60.5777 | 2024-09-27 08:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 344e0f63-cc55-3f37-9814-7bb96b59e7a0 | -7.5888 | -60.5785 | 2024-09-27 08:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 170.5 |
| 3fa696ec-b192-3024-8629-1e2c0db7df7f | -7.5703 | -60.5984 | 2024-09-27 08:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| cd264d52-f03d-3b34-a3fb-4ac89ef474d7 | -7.5887 | -60.5976 | 2024-09-27 08:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 165.4 |
| 2db9a683-6634-397f-bd0c-b26a29f1b0d8 | -8.9977 | -67.3909 | 2024-09-27 08:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 08ec5e04-fa35-33a9-8592-312f11a4e475 | -8.9793 | -67.3728 | 2024-09-27 08:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 103f5ed4-d449-32cf-9a0f-2b0cb531e9fd | -8.9978 | -67.3538 | 2024-09-27 08:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 8018442d-886d-3b4c-9bc5-b5f1686eada0 | -9.0163 | -67.3719 | 2024-09-27 08:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d777a77a-24db-3b95-bae6-01f26a2a445b | -8.9978 | -67.3724 | 2024-09-27 08:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 207.7 |
| be04e360-ee9e-37ca-9ea9-b3a7f4513d75 | -10.0324 | -53.4654 | 2024-09-27 08:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 6718e451-1a1e-300b-a1ac-f59b6075409b | -12.7868 | -54.0275 | 2024-09-27 08:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1372c918-2143-36ff-bb4e-ad826dbff360 | -14.9224 | -51.4292 | 2024-09-27 08:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 776de3d9-adf5-3a90-9ea8-5e89419b6f97 | -14.9034 | -51.4104 | 2024-09-27 08:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 62422f57-acd0-3085-aadb-9894a0487533 | -14.903 | -51.4319 | 2024-09-27 08:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 18e9096c-9a3e-3de7-9805-b5168b842900 | -14.8447 | -51.4401 | 2024-09-27 08:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 66875173-641f-3ab4-8f9f-5032c7f40598 | -14.8443 | -51.4616 | 2024-09-27 08:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 1cd7d6fd-b83c-3610-9174-bbacdf21277b | -14.9228 | -51.4076 | 2024-09-27 08:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| f45d656c-bf4d-3a8a-aa38-4e33d17b2e33 | -7.6073 | -60.5777 | 2024-09-27 08:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| bd0d7888-3be7-3b1f-8b27-9836311fa9b7 | -7.6072 | -60.5969 | 2024-09-27 08:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 7042b67d-b526-3539-ac50-c5ba02029d1a | -7.5888 | -60.5785 | 2024-09-27 08:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.2 |
| b3ecb743-7402-3526-91e5-384c52660872 | -7.5887 | -60.5976 | 2024-09-27 08:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.4 |
| adc3eed2-11b7-3e5d-9b26-391641ae49fd | -7.5703 | -60.5984 | 2024-09-27 08:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| af4aca05-a35e-320b-b124-8440379dc539 | -7.8156 | -54.7252 | 2024-09-27 08:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 0ab82bb5-d5ad-3bed-8966-24249947db48 | -8.9977 | -67.3909 | 2024-09-27 08:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 3d2b8de3-0c27-34fd-a132-4a068ee84445 | -8.9978 | -67.3724 | 2024-09-27 08:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 221.7 |
| 5eebbb9e-f6a7-3afd-bf50-b0a186942caa | -8.9978 | -67.3538 | 2024-09-27 08:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c0c427e4-619f-3222-947d-093a73bd3b24 | -9.0163 | -67.3719 | 2024-09-27 08:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| c7dda038-3c9e-3674-bf34-e9394882b3c5 | -9.417 | -51.4426 | 2024-09-27 08:36:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| b82f5ee5-0b44-3dca-b7cc-91a13e53dc44 | -10.0327 | -53.4448 | 2024-09-27 08:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| ee5f1ec7-a174-3eb2-ad4e-c2c3c3fd6a05 | -12.7868 | -54.0275 | 2024-09-27 08:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |


[Clique aqui para ver as próximas entradas](README131.md)
