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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58816ad5-99ef-3c21-8d43-fdbdb9a15522 | -6.78442 | -59.31223 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0471f897-553a-3b86-a0ce-8cc32f1a825d | -6.78392 | -59.31507 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f88fb5e-2bf7-3c4d-aed7-dacfacbb317a | -6.7837 | -59.31702 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 586050ed-b9f2-3a85-9fa9-d0f04350825e | -6.78322 | -59.31985 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4a3eb1e5-05f4-3aa1-9301-aa24e12d4e57 | -6.78291 | -59.32072 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 474e8104-056d-319f-b0e4-812c4cb5db96 | -6.78274 | -59.3227 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5211a450-04c1-3dd1-8862-e33d0e04a666 | -6.7824 | -59.32358 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d235c8b-2900-3230-aeab-f31cb6889dd9 | -6.77969 | -59.31036 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 28438121-c882-3c5f-bd42-9916f8382fff | -6.77944 | -59.31129 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 747d3ff9-bd5b-3cf6-85ce-3850fc8fcf63 | -6.77872 | -59.31606 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 021c0987-327f-3582-b28a-7a4a16cab68e | -6.77844 | -59.31695 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4cfbc6e2-042c-392b-ae6e-e80809e2a851 | -6.77824 | -59.31887 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 731ea637-7983-370c-be1e-7e6f7bf2fc9a | -6.77793 | -59.31976 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 11d4d175-e7c5-3906-9ea2-d9330717e090 | -6.77742 | -59.32262 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5df2f4d9-ef4f-32b1-9233-8c7c647acbbf | -6.77677 | -59.32751 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3e9e27e-d282-3d86-a493-388b4e4e1b9a | -6.77396 | -59.3132 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ed7a37bd-6eb3-3310-9ae0-557b712b8406 | -6.77325 | -59.31796 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ba1dd835-e11c-3be3-b7b4-a07a01c90a6f | -6.77294 | -59.31886 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c1d87c16-d6dc-3220-9243-505433b87869 | -6.77243 | -59.32172 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e3c2e361-fc54-3856-8002-4903657c6834 | -6.77192 | -59.3246 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b52394d8-104d-35f0-85c1-ed29d577966a | -6.76875 | -59.31419 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 153c8c35-93a9-310a-8381-41a31b50205b | -6.76826 | -59.31704 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5a83ea33-6147-3518-a48a-74b0508ee03b | -6.76677 | -59.32573 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a8c50df8-9a83-33d8-9bef-8383508b09eb | -6.76327 | -59.31612 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d8e7b36a-21a8-39d0-84d6-23b57bf5fcae | -6.76228 | -59.32191 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2651cdd1-16c6-3bf3-a0b5-50f687d0e915 | -6.76177 | -59.32487 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 863130c2-173e-3433-9448-758e671fbbd2 | -6.76126 | -59.32784 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc3f711a-05db-38f5-8e15-6b85860df6e8 | -6.75729 | -59.32099 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cd59b5bd-5af9-36d5-8858-c24e8fdd7180 | -6.75678 | -59.32394 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 21c4a5e7-a66b-3f8a-8004-7cd44037c667 | -6.75179 | -59.32303 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 241ca61a-5559-3c95-9186-f0d7cb53f1a0 | -6.75078 | -59.32889 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b544dd65-5a69-39ea-bd53-4b2632684f4e | -6.74579 | -59.32792 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 25effea2-a29e-390e-8922-025cb36c2861 | -6.74529 | -59.33083 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8cb6cb5-b107-384f-a1d0-9a10397ae6a8 | -6.73632 | -59.29343 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6971464-ce38-313c-942e-ac8c4c6c645e | -6.73582 | -59.29633 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18e68e6e-f479-3dc0-adec-b4baaef2e085 | -6.7343 | -59.30506 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7176c431-c308-3b44-b77e-d2a0bdf46a49 | -6.72681 | -59.31852 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00b44b5d-d3b6-368c-ba81-f8eddd794fa9 | -6.7263 | -59.32143 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e684ee28-32f2-37b9-80d7-fdfe80a8839f | -6.72334 | -59.3089 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efd9f9f6-47a6-32df-9fff-b33d96bf52b7 | -6.72283 | -59.3118 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 971c9d27-eec5-33d3-a05d-a7859a858c4b | -6.72233 | -59.31469 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3de16ef-32f5-3594-993c-3fb1d6db9792 | -7.15645 | -59.39287 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfa42735-5359-3b65-bb0d-1ba4110dac97 | -7.1515 | -59.39177 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74012534-e826-3f9b-b3e6-29d2fbb7fbee | -7.13838 | -59.37863 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30418888-5a7f-36ca-b61a-d2dde1d2f469 | -7.13762 | -59.38293 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94aeac03-2867-36a8-8b0a-574745149225 | -7.13339 | -59.37774 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 90d25bf3-d024-3d62-bf57-8eeea09a739f | -7.13264 | -59.38205 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5df6a014-4955-3852-9879-dcb18c20e04b | -7.09602 | -59.41431 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 326f5a05-f550-32cd-9080-646dffafb3b9 | -7.09154 | -59.41053 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0b8e7b14-82f2-372b-8076-e885508b2d9b | -7.09139 | -59.41162 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 075ef552-d04d-3fcb-9215-4934d2e673dc | -7.09102 | -59.41343 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 807e3016-1d83-3324-ac61-1a2952f56289 | -7.09089 | -59.41454 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6242ab95-c417-35bf-85d2-b06227c1ffd5 | -7.0905 | -59.41634 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e37f8ebe-9407-388b-bd51-f9d360c8eda7 | -7.08688 | -59.40783 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 59302dea-8776-3898-937e-2b849f4ac643 | -7.08654 | -59.40964 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 6b6340d1-9c31-3c45-9dd6-6723fcbbc986 | -7.08639 | -59.41072 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 23d1ec8e-9c03-3883-b825-6cafee439ca2 | -7.08602 | -59.41254 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 82c0095a-4ff3-39e9-bc40-af0c71e668ce | -7.08589 | -59.41363 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 76388c83-39a2-3aff-bf62-df3d518e7eb5 | -7.0855 | -59.41544 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| fcac5862-a2ce-3e95-8d42-b8396411937d | -7.08539 | -59.41654 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f29d7582-4af2-31d8-9a44-0f9f1ab704c0 | -7.08189 | -59.4069 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 5dec3fda-f94e-35a2-b82f-72b5dd2ac561 | -7.08155 | -59.40873 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 0c669981-dc24-3707-8053-aee9c191eb73 | -7.08139 | -59.4098 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| dd19b1f6-449e-32ae-9cf0-328b83ae0187 | -7.08103 | -59.41162 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 5b62dd89-f61d-380f-8a38-407b548fe3b0 | -7.08089 | -59.4127 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| b8eb8967-40e0-31c7-ac87-8ec98716714c | -7.08051 | -59.41452 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ec783036-1ca5-3568-9f87-1ad9e9355024 | -7.08039 | -59.41562 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| ebad6595-20ff-3739-8eb8-e80a5930a64e | -7.07998 | -59.41745 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 85af6b17-e114-3d75-9edd-bd43c2325ea5 | -7.07989 | -59.41856 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c44cf8c7-8551-3401-86eb-1c1ee0be4d55 | -7.07639 | -59.40891 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| eacf867c-3113-3a9f-8b6e-5ee092631795 | -7.07589 | -59.41182 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| c378cc7c-0f58-365c-bb04-85a523f5b083 | -7.07539 | -59.41474 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 4af8398d-8e10-3e8c-b784-f51d38c86121 | -7.07489 | -59.41767 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f7f9851-b648-3b2f-b4f8-de56d578eed4 | -7.07139 | -59.40804 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 977ac43c-3c6c-3200-a1ea-d6c17d22c5b6 | -7.07089 | -59.41095 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f545281c-ed96-3b34-85b6-efff85bf03ce | -7.07039 | -59.41386 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| eed7b7e3-4bd5-313b-b029-edc7685898a0 | -7.05887 | -59.42084 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0101c5f3-ee6e-3c3f-8039-5dd733985271 | -7.05436 | -59.41707 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 38775ec2-02ac-3a68-9963-66750fb086c6 | -7.05386 | -59.41997 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 33198978-5713-3040-a308-5962dad5c495 | -7.05335 | -59.42288 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ba55315-fc7f-3c1b-9946-ce75eeb6ee97 | -7.04986 | -59.41325 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 94e01530-67c7-3254-9052-43000d8b3bb6 | -7.04936 | -59.41615 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c6e106c5-0751-3e12-9a88-be02fa8ca3bc | -7.04886 | -59.41905 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0f70f9a5-0216-3f21-af78-a9ca6fc1006c | -7.04835 | -59.42196 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e2d099e7-8037-31b3-82ea-a448d2188542 | -7.04784 | -59.42488 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e15d1e6f-5758-32b8-aad4-6b8105f2bd92 | -7.04638 | -59.40363 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c39211f-da2f-3b16-a4f4-135b262c5a47 | -7.04436 | -59.41525 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 50e0bf12-38b7-32bf-8ba1-a4f8be4924a2 | -7.04385 | -59.41814 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5b93c5e8-34e5-346a-aae0-afe32c5fca3f | -7.04335 | -59.42104 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 120b9efc-0017-3dc4-bc0c-7087c6c08691 | -7.04284 | -59.42396 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e041550b-ae97-3b07-aca4-93d7dc4f228c | -7.04188 | -59.39989 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e29473d2-3fa3-36ec-aa6b-0b2c4e0915a1 | -7.04138 | -59.40275 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3272844-13d8-36f4-a70d-c84a846b294c | -7.04087 | -59.40565 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a89ab9b-459c-3cab-b48f-627196e1e38a | -7.03935 | -59.41438 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d526ebf-d234-3fb1-8160-179300caa841 | -7.03885 | -59.41725 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eabbd438-6872-3da1-a31b-3e8578de49cb | -7.03835 | -59.42013 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2379a1bc-b570-33a2-994e-8bf874a42b33 | -7.03746 | -59.36628 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b228aeb4-c785-3f16-8b95-9e5c2365325e | -7.03695 | -59.36921 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66021a85-0d88-3de6-876b-ceef8acadba7 | -7.03638 | -59.40187 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90be067d-3f07-30aa-9a11-f58b1677ef9f | -7.03435 | -59.41349 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README117.md)
