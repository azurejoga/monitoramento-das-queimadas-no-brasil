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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d36222ef-38c8-3d88-8dff-74630267ce9b | -8.2919 | -55.365898 | 2024-10-11 01:40:03 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91195221-bae9-360f-8910-78eb5d0e89da | -8.2948 | -55.377701 | 2024-10-11 01:40:03 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc1e8be1-b7e4-33c0-89fe-13c71ba76d5e | -8.2822 | -55.368301 | 2024-10-11 01:40:03 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2720765-167f-3c9e-b825-401b45f74b23 | -8.2851 | -55.380001 | 2024-10-11 01:40:03 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4ccdbb7-90c0-3a09-b336-00e5122ffbeb | -9.2165 | -59.773102 | 2024-10-11 01:40:05 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 088c0d75-8ed3-31c5-b7aa-5330aaeb01eb | -7.9693 | -54.764999 | 2024-10-11 01:40:06 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73ccc90a-788e-3b0b-9efd-d72b0b48d9f3 | -7.8333 | -54.715302 | 2024-10-11 01:40:08 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d50b392-7a4b-3102-b824-171d655ea984 | -9.5175 | -62.922199 | 2024-10-11 01:40:12 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 961349ca-9936-36c5-9625-0b83a93335db | -9.5191 | -62.929699 | 2024-10-11 01:40:12 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e5f0a9c8-8bc9-3209-9f11-c913b9f2a714 | -9.463 | -63.140499 | 2024-10-11 01:40:14 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1b27dac5-d548-3829-a8ec-bb2633fe18c5 | -9.4647 | -63.148102 | 2024-10-11 01:40:14 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f5ce926c-ebd6-327e-b10e-59efe27a68c4 | -9.506 | -63.381699 | 2024-10-11 01:40:14 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 56f53d07-60d1-3800-b7c8-d5f2c57f864f | -9.4945 | -63.376099 | 2024-10-11 01:40:14 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 32be0aae-0654-381e-8b02-c8b8be15309d | -9.4962 | -63.3839 | 2024-10-11 01:40:14 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 55114cc9-f3e3-301e-b339-8b41987ed856 | -9.5088 | -63.4879 | 2024-10-11 01:40:14 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e8eb2045-d42c-3001-8092-397c44343fde | -9.7504 | -64.878601 | 2024-10-11 01:40:15 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 62ca5793-9b33-3102-b505-4c1b2e1ba6d3 | -9.7524 | -64.887901 | 2024-10-11 01:40:15 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7a46f483-f35e-395c-aed5-f3ab686f42b8 | -9.7406 | -64.880699 | 2024-10-11 01:40:15 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4da73b5c-bd27-3c66-8191-11d2b58b84cb | -9.7288 | -64.873497 | 2024-10-11 01:40:15 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 44dcebe9-cf88-3522-876f-9d63cb2b3665 | -9.7308 | -64.882797 | 2024-10-11 01:40:15 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 12842448-7456-3992-a01b-d73fb5c55298 | -8.1174 | -58.031502 | 2024-10-11 01:40:16 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e19cc1b2-7278-344a-b7b3-f909af09fa26 | -8.1193 | -58.039799 | 2024-10-11 01:40:16 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e98685c-2a39-3af2-9801-f4d7fc345238 | -9.169 | -62.649899 | 2024-10-11 01:40:17 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5c3eb9df-743e-34b1-a57b-4d788cf9759d | -8.1095 | -58.042099 | 2024-10-11 01:40:17 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1f83386-7a19-3741-8440-ae47657a840b | -9.6449 | -64.959702 | 2024-10-11 01:40:17 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d3d3e6f1-77b2-3098-932f-1f22718d794a | -9.647 | -64.969002 | 2024-10-11 01:40:17 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7c6c1f-efb0-3535-ab84-ed21b68a7cca | -9.649 | -64.978401 | 2024-10-11 01:40:17 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 836cd422-eba7-343f-a30f-19a2c95d91d2 | -9.5601 | -64.614799 | 2024-10-11 01:40:17 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9b9e2f31-de76-34f8-8c66-32e2b6231766 | -9.5621 | -64.623802 | 2024-10-11 01:40:17 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a371b37f-7473-3cf7-9be6-5f3e3a3b63df | -9.5719 | -64.810898 | 2024-10-11 01:40:18 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 601bff54-38f9-311f-ab4c-38b24aee654e | -9.3466 | -64.340401 | 2024-10-11 01:40:20 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0a686a29-dd26-31f8-898f-d8a537f4a4fb | -9.3485 | -64.348999 | 2024-10-11 01:40:20 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 43a432f4-bbc1-3246-80f4-2fbc42e89225 | -8.8148 | -62.9991 | 2024-10-11 01:40:24 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a7415036-bc43-39fa-959e-5886f0bb8acb | -8.6229 | -63.245998 | 2024-10-11 01:40:28 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4a02609a-764e-3cdf-80e2-88f387cab507 | -8.2213 | -61.5051 | 2024-10-11 01:40:28 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c1497df-ab4a-35a0-b86c-6ab8369ad411 | -8.0602 | -61.2953 | 2024-10-11 01:40:30 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ecd33914-bf00-37e4-8b17-46c079fd2761 | -7.9284 | -61.259899 | 2024-10-11 01:40:32 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 936892aa-be61-3d72-a339-ad8d9c9a1fa6 | -7.9299 | -61.2668 | 2024-10-11 01:40:32 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26c5e5a2-7a92-3924-aee8-fcad3eec11e5 | -7.9315 | -61.273701 | 2024-10-11 01:40:32 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5338b8f0-8bb5-3037-ad26-8a175685dd3b | -7.8217 | -61.1539 | 2024-10-11 01:40:33 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9facf152-9f75-3b5b-aa1d-edae694cb66a | -7.8233 | -61.160801 | 2024-10-11 01:40:33 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ec58231-0a03-35fb-b295-218ba3e4c718 | -7.8249 | -61.167702 | 2024-10-11 01:40:33 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdbdca1b-24ab-3b54-ae99-fe72848b5125 | -7.8276 | -61.224899 | 2024-10-11 01:40:33 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 713fb550-bab1-36e3-a640-342e0576f049 | -6.5623 | -56.0158 | 2024-10-11 01:40:34 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7278490-f10d-3c2e-8dc8-bdd3539b3068 | -7.7727 | -61.345699 | 2024-10-11 01:40:34 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a300e7ef-b503-3563-93b2-49d1dd7b58d6 | -7.7743 | -61.3526 | 2024-10-11 01:40:34 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c172fe3-9b06-37ab-9e5d-280cd16f1b2a | -7.2046 | -59.065701 | 2024-10-11 01:40:35 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5cde58e-ccff-33a5-802f-8102d90b4219 | -7.2064 | -59.073299 | 2024-10-11 01:40:35 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a88be0e-77a3-364c-a8e6-db01404a4222 | -7.1464 | -59.302299 | 2024-10-11 01:40:37 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db8ff52c-2405-3a37-b9a1-cec424baee7f | -7.102 | -59.288799 | 2024-10-11 01:40:38 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60bb6a4c-1c11-361d-8cec-440473efdd1d | -7.1037 | -59.296299 | 2024-10-11 01:40:38 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9de18b9-10c4-32a0-afa5-13d69277de25 | -7.0834 | -59.253502 | 2024-10-11 01:40:38 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0853377e-52f6-39c7-8301-542ad46ecc18 | -7.0851 | -59.261002 | 2024-10-11 01:40:38 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26ee6316-c288-3212-9b1f-e12e065e5da9 | -7.0753 | -59.263302 | 2024-10-11 01:40:38 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdd0347d-f1d8-3bc5-aaee-08ace65c5fbe | -7.0872 | -59.402401 | 2024-10-11 01:40:38 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5540354-af04-35f6-80a8-58a21321b8c2 | -7.0889 | -59.409901 | 2024-10-11 01:40:38 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73fa0320-d45b-3fc2-aa46-fd999fcd5d12 | -7.0756 | -59.397202 | 2024-10-11 01:40:38 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c701625-b6c2-3a12-bd1a-5b5a6c2f6d1f | -7.0774 | -59.404701 | 2024-10-11 01:40:38 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00cab562-ccf0-379b-b0cc-5be00736f0b2 | -7.0791 | -59.412102 | 2024-10-11 01:40:38 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59cec142-39e6-3878-81ba-8f21578ec089 | -7.0658 | -59.399502 | 2024-10-11 01:40:39 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cee6d95c-2310-3ad7-b1a9-efd454f4edef | -7.0676 | -59.406898 | 2024-10-11 01:40:39 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 02f3f37c-6de3-3df1-a563-5a00eb7c7791 | -7.0457 | -59.357101 | 2024-10-11 01:40:39 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f083ee54-76d5-38e6-8a3e-4ce7196fc0f7 | -7.0474 | -59.364498 | 2024-10-11 01:40:39 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7592a60a-4669-3dc6-afe1-e541a079bfe1 | -7.0376 | -59.366699 | 2024-10-11 01:40:39 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d71bc36-a104-366f-8e15-35f6f1820999 | -7.0463 | -59.403999 | 2024-10-11 01:40:39 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da255409-6251-32af-98a1-d136e29ba0d4 | -7.048 | -59.4114 | 2024-10-11 01:40:39 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8695396-a945-315d-8770-d5e72b2e0e43 | -7.0302 | -59.4235 | 2024-10-11 01:40:39 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93a7d7ca-eab5-3546-bc0e-82b70f7eef24 | -6.9384 | -59.207401 | 2024-10-11 01:40:40 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f00b6603-e93c-38a8-833d-bdc7dffb0e29 | -6.9685 | -59.468899 | 2024-10-11 01:40:40 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78b1cb6f-b598-32f2-aa83-4049475ef5bc | -6.8592 | -59.089199 | 2024-10-11 01:40:41 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6044106c-a500-3bde-9d57-51e0ca32622b | -6.8154 | -59.034599 | 2024-10-11 01:40:41 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a657cb76-a200-31f5-99ec-0f8f8d414a2a | -6.8173 | -59.042301 | 2024-10-11 01:40:41 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1fdbf233-7ae3-3242-9a2a-41d5759a9c9b | -6.8077 | -59.133499 | 2024-10-11 01:40:42 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce2ae4dd-7dbe-3857-9e84-9bb5f2088274 | -6.8095 | -59.141102 | 2024-10-11 01:40:42 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca8a878a-572f-3089-95b4-cc179bd38702 | -6.7861 | -59.306301 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5afa261-3d96-3bf7-b542-52a40ab6c738 | -6.7878 | -59.313801 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9003c17f-0dbf-3872-94f9-68ff1467ff77 | -6.7764 | -59.308601 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3426d0c3-8860-3aad-8988-0d9bc4d10616 | -6.7781 | -59.316101 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2fa3a56-a3db-3e81-8440-723b7a2321c4 | -6.7666 | -59.310799 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81dc3498-ec2b-3455-9203-00da16021d2b | -6.7683 | -59.318298 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7cfe21af-5294-3969-a2b3-b0987beaa774 | -6.7701 | -59.325802 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f62021ea-b7bc-3016-9a58-5a085e7c253b | -6.7585 | -59.320599 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4384ebd0-1fe7-3e7f-bb07-91853ed31f69 | -6.7603 | -59.328098 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| edc80933-1121-331e-8303-0cc1ca636ecc | -6.7399 | -59.285099 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce830c8-8c89-3343-8b1e-cc0efeffab03 | -6.7417 | -59.292702 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2483d5b8-6ca3-3aeb-8a58-3362ba58d86d | -6.7487 | -59.3228 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 878f68e1-919a-3b94-a8a9-dda1ec724325 | -6.7505 | -59.330299 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e093ded9-6991-3247-8e44-b57fc84f3b39 | -6.7523 | -59.337898 | 2024-10-11 01:40:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a54970ee-352c-33a1-b3cc-b11579841646 | -6.7256 | -59.312401 | 2024-10-11 01:40:44 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b51ce9a8-698c-30af-a856-046af83aac87 | -6.7985 | -59.624802 | 2024-10-11 01:40:44 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 866ee430-aa14-3a36-8d1f-18d1db934d0b | -6.8002 | -59.632099 | 2024-10-11 01:40:44 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f0d9466-8337-38b8-a548-1a8734927c81 | -6.8019 | -59.6395 | 2024-10-11 01:40:44 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 770e45c2-abc2-3f0a-91f3-8ccac0c54f18 | -6.7904 | -59.6343 | 2024-10-11 01:40:44 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fe88892-8dfc-3e75-8d5e-f56fefb1b039 | -6.7921 | -59.641701 | 2024-10-11 01:40:44 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75b2228d-2921-3d71-9fbf-a20e0c6aac97 | -6.7363 | -59.6236 | 2024-10-11 01:40:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6ac76dc-e253-3b3b-8892-39b970691799 | -6.738 | -59.630901 | 2024-10-11 01:40:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3284390a-5bd5-35fb-8657-f5a382a46b03 | -5.8022 | -55.727798 | 2024-10-11 01:40:45 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26092e7f-3727-38f6-8ead-d1b67a702c2c | -5.8052 | -55.739899 | 2024-10-11 01:40:45 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d794c65-aa76-3c6a-b220-9a41e494af7b | -5.8081 | -55.7519 | 2024-10-11 01:40:45 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ecdeee2-72f8-3bac-8a13-d523d2799a08 | -6.735 | -59.662498 | 2024-10-11 01:40:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README25.md)
