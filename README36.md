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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b8006ce-0973-331c-bf14-b0513dc11738 | -12.2893 | -43.7258 | 2024-10-10 02:16:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 81c6c2c2-50c9-3d5b-bb66-d79d4ce80ab2 | -12.973 | -46.216 | 2024-10-10 02:16:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d11d2dde-b49c-3c0a-81d7-ea79d5110c53 | -12.7056 | -63.0606 | 2024-10-10 02:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 107.8 |
| e2244744-57bc-37ae-9892-0139b50a3274 | -12.7058 | -63.0414 | 2024-10-10 02:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 38970857-f910-35cc-b893-fc085fd73967 | -12.7245 | -63.0595 | 2024-10-10 02:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 7b8ffff4-d28c-330c-9697-f87a983e90d3 | -12.7247 | -63.0403 | 2024-10-10 02:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.5 |
| fcfa2b19-851d-39e0-8389-c49341dd1a44 | -12.9255 | -51.1361 | 2024-10-10 02:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 6fa5c330-2b10-3408-99e3-95c5342e33d1 | -12.9447 | -51.1337 | 2024-10-10 02:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8f361ac2-2614-364e-93e4-c255cf8d87f1 | -13.7346 | -60.6079 | 2024-10-10 02:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c72f9f95-deb6-3a57-9024-45d542e5a41e | -2.6533 | -53.3506 | 2024-10-10 02:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 5ca74c9f-ad2b-33ed-970b-f66a7705494f | -2.6716 | -53.3704 | 2024-10-10 02:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 3fc96748-38ca-36e4-acde-46d4e0f0bc80 | -2.6716 | -53.3502 | 2024-10-10 02:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 368.6 |
| efa1d692-9b59-3c7b-87b6-2fe968fcbf42 | -2.6717 | -53.3299 | 2024-10-10 02:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 156.0 |
| e3115979-2e04-3df0-9095-fe8928c25ad0 | -2.69 | -53.3497 | 2024-10-10 02:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 21387d6b-1b09-3550-be0e-3e9dc5fc2c46 | -2.6901 | -53.3295 | 2024-10-10 02:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 8fe8e2c8-60a4-30f0-bdab-b96e97d24d23 | -4.0814 | -51.0292 | 2024-10-10 02:25:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| a8364aec-ff2e-30e7-ae7a-876758668649 | -4.0961 | -48.2739 | 2024-10-10 02:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 03aac177-c3f4-3acf-aebe-bd01c2daa764 | -4.0962 | -48.2523 | 2024-10-10 02:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| bdaec8dc-a675-39e1-896a-199772735b17 | -4.1146 | -48.2731 | 2024-10-10 02:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 207.2 |
| a9cd91dd-d22a-3496-8c83-94ca260e201b | -4.1148 | -48.2515 | 2024-10-10 02:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| 85e09424-5c46-344d-b846-b5cc86695bde | -6.5218 | -60.0649 | 2024-10-10 02:25:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 6b9c33dd-cbad-3801-9ca5-c27999192f25 | -6.7654 | -59.3252 | 2024-10-10 02:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 7d464c0b-7baa-3df5-b97b-af6963a80aab | -6.7655 | -59.3059 | 2024-10-10 02:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e7731d43-b82a-3825-a244-7ff6f052f1d6 | -6.7839 | -59.3245 | 2024-10-10 02:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 8e09d0a2-93f3-3bae-9abc-6e1428e2230c | -6.784 | -59.3052 | 2024-10-10 02:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 0e27e390-61aa-37f8-899d-4efcbc6b765a | -9.0084 | -61.6253 | 2024-10-10 02:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f9ac86fd-07c0-35d4-adec-14cb86a2ee85 | -9.027 | -61.6244 | 2024-10-10 02:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e54e0643-e02c-34a6-95da-16c1f60b86f5 | -9.0271 | -61.6053 | 2024-10-10 02:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| d3d6f9f7-3975-30f1-8e64-23b8626a309a | -9.0656 | -61.3934 | 2024-10-10 02:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 165a1eea-2315-3450-960c-27bc7861a166 | -9.0841 | -61.4117 | 2024-10-10 02:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ccfffba9-d7f5-3559-a53d-67a65f4a7211 | -9.0842 | -61.3925 | 2024-10-10 02:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| c06ec504-9987-31e0-a4ff-97e9b7cd87c2 | -9.1035 | -61.2769 | 2024-10-10 02:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 25856033-85de-3b7a-8f85-6475e4bf5f97 | -9.1221 | -61.276 | 2024-10-10 02:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 186.2 |
| f43dd107-c700-3255-9a8e-d8e8bdd6aa28 | -9.1407 | -61.2751 | 2024-10-10 02:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 3c498444-a354-3809-bfa6-ef64d9016877 | -11.0252 | -57.2436 | 2024-10-10 02:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 479b9efa-556b-39b9-adc1-47311fb8227b | -11.0254 | -57.2237 | 2024-10-10 02:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 166.3 |
| dec60e0b-d56b-3e9c-88f7-b8a2df93530e | -11.0256 | -57.2038 | 2024-10-10 02:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 156.2 |
| 868ccb5f-3be6-32c3-8355-fd2d5e897863 | -11.0443 | -57.2222 | 2024-10-10 02:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| a4d14e2c-1a54-3600-bed0-932477208ff4 | -11.0445 | -57.2023 | 2024-10-10 02:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 9a1f3ade-77d3-39c8-9994-d24a3a6c1dfc | -11.277 | -60.4067 | 2024-10-10 02:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7eec0de2-98c8-3e6b-8c44-8fe41094abaa | -11.8188 | -58.8459 | 2024-10-10 02:26:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 7ac1897f-eb77-3886-bef1-30c681174414 | -12.2893 | -43.7258 | 2024-10-10 02:26:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| e5292fc1-fa7f-3b53-a744-b81da71026a4 | -12.973 | -46.216 | 2024-10-10 02:26:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 4f7a4f21-6b8d-32e2-bb32-829e0faf981f | -12.9255 | -51.1361 | 2024-10-10 02:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 150fd06a-2a65-3dcf-8f8f-1891e17180ed | -12.9259 | -51.1147 | 2024-10-10 02:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| fbae5e26-52e7-3a2a-8af1-1f9f25ecf434 | -12.9447 | -51.1337 | 2024-10-10 02:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 153.4 |
| ca3643ed-54c1-3610-8037-a5f915172a0c | -12.9451 | -51.1123 | 2024-10-10 02:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 9f1cee9f-24f1-3667-80af-4267417cc68d | -17.6668 | -56.3059 | 2024-10-10 02:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 0543c00e-c0ff-3dbe-984f-0931c32ae349 | -2.6532 | -53.3708 | 2024-10-10 02:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 54014f84-32c4-306d-a0a5-9d6f6c5690a9 | -2.6533 | -53.3506 | 2024-10-10 02:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 0bd852b6-b6ed-319f-9b16-1d72204ac987 | -2.6716 | -53.3704 | 2024-10-10 02:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 53d4d7d0-8c17-3a55-869f-6e3eaf94c23d | -2.6716 | -53.3502 | 2024-10-10 02:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 343.8 |
| ca1c20a8-ce63-3e34-83d7-0a6851133a29 | -2.6717 | -53.3299 | 2024-10-10 02:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 72c6ff2b-8d17-3ed7-894f-18ded3012202 | -2.69 | -53.3497 | 2024-10-10 02:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| ee88bf54-5047-3750-979b-ccc05a921132 | -4.0961 | -48.2739 | 2024-10-10 02:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| caba1587-4b9a-37d3-8ec7-951bc31f4fad | -4.0962 | -48.2523 | 2024-10-10 02:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| e795e766-d46a-3501-aa0b-de221f613588 | -4.1146 | -48.2731 | 2024-10-10 02:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 234.2 |
| a3a0b351-0d69-3dd5-abfc-17cb040ee239 | -4.1148 | -48.2515 | 2024-10-10 02:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 147.3 |
| a8e8f6fc-cd1f-3b3b-af03-e271204df160 | -6.5218 | -60.0649 | 2024-10-10 02:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 9e8dee38-4740-3a20-a51d-f13e8229375e | -6.747 | -59.3259 | 2024-10-10 02:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 7aba8eb1-ba55-384f-8b81-5a008ff840c2 | -6.7654 | -59.3252 | 2024-10-10 02:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 42b16922-ca0c-39e3-b233-ce13ae09531c | -6.7655 | -59.3059 | 2024-10-10 02:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 7fe12e98-31f4-3d6e-821f-920e11fabb12 | -6.7839 | -59.3245 | 2024-10-10 02:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 5c36f17e-ea38-368e-9b59-d85572fdbb0b | -6.784 | -59.3052 | 2024-10-10 02:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 9bb10d8a-9a10-3a6b-98b4-0375f7c2ef94 | -8.1475 | -42.9717 | 2024-10-10 02:35:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.0 |
| 89442c7c-a6ce-3a74-940a-c7097a657e16 | -8.1478 | -42.9481 | 2024-10-10 02:35:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 7c2e2738-307f-31bc-abe9-bdf14343a80e | -9.0084 | -61.6253 | 2024-10-10 02:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| badd3b3a-aa6d-3c95-af17-6fa070d90914 | -9.0085 | -61.6062 | 2024-10-10 02:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 7f4af105-14ac-37b6-8efe-898017dfb0cf | -9.027 | -61.6244 | 2024-10-10 02:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 94d1c8df-420c-3b2a-9c1f-0a29dde290ed | -9.0271 | -61.6053 | 2024-10-10 02:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| deb8187f-eb12-332f-a192-290e691f72dc | -9.0656 | -61.3934 | 2024-10-10 02:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 83c405e1-5798-3157-b6c1-31bce64cf442 | -9.0841 | -61.4117 | 2024-10-10 02:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 3998b9d8-e4e5-3c7a-8cb0-5d6d6d6703a2 | -9.0842 | -61.3925 | 2024-10-10 02:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 9e6cbbfd-af97-34ee-98a6-5e5e16752cbc | -9.1035 | -61.2769 | 2024-10-10 02:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 382f75f5-cf51-303d-8c2e-fbe2d951ad4c | -9.1221 | -61.276 | 2024-10-10 02:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 08547e75-40d6-3aed-abf5-cbdd011f5004 | -9.1407 | -61.2751 | 2024-10-10 02:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 8cd817be-0d7a-38c0-855f-6180b923c936 | -10.363 | -55.8755 | 2024-10-10 02:36:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 497fc9c3-5a84-3a7f-836f-6540947bffdf | -10.3632 | -55.8554 | 2024-10-10 02:36:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 4442a783-effc-31eb-8676-8e4c6371069a | -11.0254 | -57.2237 | 2024-10-10 02:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 142.0 |
| a61a39b3-cb24-396c-8fa2-7ebb97e235ec | -11.0256 | -57.2038 | 2024-10-10 02:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 129.0 |
| f9d53932-9c75-33ff-8a85-d1f4150056d4 | -11.0443 | -57.2222 | 2024-10-10 02:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 3fc6530c-8b67-3ab6-8e30-ac3f10afa4d3 | -11.0445 | -57.2023 | 2024-10-10 02:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 86426e31-4b8c-34fe-bf80-607b13212a14 | -11.277 | -60.4067 | 2024-10-10 02:36:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 353819a4-0ebd-3ba1-bb2c-2623abaf1eea | -11.8188 | -58.8459 | 2024-10-10 02:36:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| aa1e6048-b4de-3b76-bb33-a92dae9f7649 | -12.973 | -46.216 | 2024-10-10 02:36:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 97.4 |
| e1ea2f96-375c-351b-969a-54f44fb97d21 | -12.7056 | -63.0606 | 2024-10-10 02:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 6216a50c-730f-3522-88f2-4027f696e99c | -12.7058 | -63.0414 | 2024-10-10 02:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d3ec6769-3bca-3d64-bd86-c8e8191cbb9e | -12.7245 | -63.0595 | 2024-10-10 02:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| a2ca6877-8357-33e5-9cc1-03af143cd87d | -12.9255 | -51.1361 | 2024-10-10 02:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 6d5e944a-c434-3a8d-b65e-870185335bea | -12.9259 | -51.1147 | 2024-10-10 02:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 5a270455-a426-3a4d-807b-77e7da9fbcf5 | -12.9447 | -51.1337 | 2024-10-10 02:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 176.6 |
| b9454bba-9bf7-3275-8126-38e648d03b2a | -12.9451 | -51.1123 | 2024-10-10 02:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| a5a14d54-92df-318d-abb2-bf3ea788435a | -17.6668 | -56.3059 | 2024-10-10 02:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.8 |
| cdcc3873-7119-3025-8174-9e6d4601cd1c | -17.6865 | -56.3033 | 2024-10-10 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 83e241b5-3a2f-3c00-8f42-c7c6c2d8d953 | -21.5795 | -46.08 | 2024-10-10 02:37:05 | GOES-16 | SERRANIA | MINAS GERAIS | Brasil | 3166907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.2 |
| 5874aa12-c76b-3982-95f0-6acfc871803a | -2.6716 | -53.3502 | 2024-10-10 02:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 367.6 |
| c470ab7e-6fb6-30cb-9e3b-807ae4d6f0da | -2.6717 | -53.3299 | 2024-10-10 02:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| dda880fe-ffd6-390b-bdf2-322083a04f6c | -2.69 | -53.3497 | 2024-10-10 02:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 7cb0da17-222e-34bc-bb4e-4170ab672aa6 | -2.6716 | -53.3704 | 2024-10-10 02:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 1f823647-1e2c-30b6-ac28-339421d7e13f | -2.6533 | -53.3506 | 2024-10-10 02:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |


[Clique aqui para ver as próximas entradas](README37.md)
