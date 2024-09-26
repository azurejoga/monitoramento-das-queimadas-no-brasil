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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d885dad5-6a40-37ea-b735-ce948d5618c2 | -12.82616 | -62.69527 | 2024-09-26 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9d7b8e83-9f2d-3493-bbc9-8cbdf7e069c6 | -12.82528 | -62.7 | 2024-09-26 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ba58ce2f-df01-3a90-bcfb-0a4f864dabae | -12.58853 | -62.57477 | 2024-09-26 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cac36500-4762-3031-b3c3-ee9955a9cd16 | -9.02929 | -63.3163 | 2024-09-26 04:59:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 869268e6-ba7d-32b8-b73d-c41e37d1786d | -9.02876 | -63.31926 | 2024-09-26 04:59:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dad4a74-65fa-30a4-b7bb-a4978dcf952b | -8.92071 | -63.2881 | 2024-09-26 04:59:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9b323043-8938-36e0-a218-0379965d665b | -8.92016 | -63.29111 | 2024-09-26 04:59:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab8a9b45-8a49-37a8-bfa6-dd6ddce26f26 | -8.91564 | -63.28717 | 2024-09-26 04:59:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8759ca0c-f2bf-3159-8d38-dcc8b95fa743 | -8.91509 | -63.29019 | 2024-09-26 04:59:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07ce3e99-80f8-32ab-8077-ec021bc43ed7 | -8.90465 | -63.67279 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f9d66ed9-10b4-36ef-8dc6-d71b9a54255e | -8.90408 | -63.67598 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b9178bbb-1144-337a-81a6-72f1ee13df6a | -8.84381 | -63.71151 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d976370f-0e1a-3302-9ad6-423e498cc190 | -8.83858 | -63.71057 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb11ab12-e884-3807-b11f-2e8befb7fb15 | -8.83799 | -63.71379 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1eab99aa-a9b3-38e8-9529-f8b4c9b33517 | -8.83394 | -63.70646 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4d774fe-2752-3cee-80e3-5e1034462747 | -8.83335 | -63.7097 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe0aec00-4e19-33a7-a401-a73b40922c9b | -8.83275 | -63.71296 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acc22ea4-6ee6-383d-95f8-a338447be3d1 | -8.83215 | -63.71621 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bd18a61-682d-3538-919c-803effaeaa57 | -8.83156 | -63.71948 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9307c8f1-4540-3ea0-8ec0-61f969f03730 | -8.82929 | -63.70239 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f23fc777-c9b1-35e0-8fb0-ac4ac11739e3 | -8.8287 | -63.7056 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 94ca4f63-4cc8-3841-a8f7-3644895d0ce7 | -8.8281 | -63.70885 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| af029740-f746-3b7b-a166-61ba31bd2cea | -8.82751 | -63.71211 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f07c0fb-c4f8-3f4c-8de5-af6dba24788d | -8.65899 | -63.13945 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4624cd5f-ef7e-382c-8e04-28ac5586f6d3 | -8.65499 | -63.13262 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b734de8-c279-3a07-af2b-779239a88645 | -8.65394 | -63.13854 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf6a0024-6e96-347d-8abb-90416a20a55a | -8.65341 | -63.14152 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0a02b52-da28-372e-9033-af833e322b76 | -8.55877 | -63.1821 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc5c2fe5-6d6d-395f-a51e-62d6a2c4bf66 | -8.55824 | -63.1851 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4074f85-3b12-3c7d-aea3-178b8b58f6e1 | -8.55771 | -63.18811 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a547a38-cace-3c47-97b0-93f00191b7a9 | -8.55716 | -63.18289 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4aad1f8-399b-3b32-aed0-df224c865ce4 | -8.55661 | -63.18589 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43e43edb-eccf-3c56-b249-5db70be19986 | -8.55605 | -63.18889 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a62f659-44bb-368c-ac46-7b15332e5f3d | -8.5537 | -63.18119 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 418a402c-0950-322b-a800-8398b67715ec | -8.55317 | -63.18419 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9280bcb4-ed41-32a5-b68d-c9d195cf3084 | -8.55264 | -63.18719 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7495c98a-3955-38d9-bb9e-8c1cb7cab3c2 | -8.55264 | -63.179 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73d954c3-e240-3b39-af74-37ba68626cd0 | -8.55211 | -63.1902 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5189b65c-7d07-3057-8666-0d9fe3a594d5 | -8.55209 | -63.18199 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c755e110-9ac5-3152-8a51-4d52f67aef3c | -8.55154 | -63.18499 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ba09f8d-f565-349b-8870-8a1fbdf407ae | -8.55098 | -63.18798 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0acb6d53-17a6-30fa-a0c1-cc7201113445 | -8.55043 | -63.19099 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9429257e-653a-3105-a6eb-12d8151f642c | -8.54863 | -63.18028 | 2024-09-26 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d03d33d-79e2-3ed6-aa7f-c1ddb53fc3f0 | -8.47732 | -62.65553 | 2024-09-26 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2a504e5-a5eb-36ef-a952-1ba41bb4b9b8 | -8.47633 | -62.66108 | 2024-09-26 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f90802d-3fbc-3630-b980-b8c4b95b3c43 | -8.47341 | -62.64915 | 2024-09-26 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 780cfd99-771e-3772-b54d-593f5692072a | -8.47142 | -62.66024 | 2024-09-26 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01ee6f71-1d08-3520-8e91-dc57d533f954 | -9.03437 | -63.31721 | 2024-09-26 04:59:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c647512-8320-3755-9119-2e06603eeee6 | -9.03383 | -63.32018 | 2024-09-26 04:59:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d21e3fa5-14a4-3ba1-89c0-c7f2ff697c13 | -10.69382 | -63.47774 | 2024-09-26 04:59:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7680f1c8-ae07-3bb7-9b44-2e57a1c9d391 | -10.69328 | -63.48063 | 2024-09-26 04:59:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 287fc31d-d44b-33e0-a711-67e84884a9dc | -10.69272 | -63.4836 | 2024-09-26 04:59:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be990131-01ae-3907-bd4b-985aae628d04 | -10.6883 | -63.47968 | 2024-09-26 04:59:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa15887a-3481-3c04-9c31-6f30df1cdc4a | -10.68775 | -63.48263 | 2024-09-26 04:59:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24e17cc4-3cc3-3dc8-8633-dec9941b3de6 | -11.77096 | -64.26518 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 917c366c-0108-3575-94ff-73d1ca706f85 | -11.76642 | -64.26101 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21e0efbb-db42-39f6-adfa-2d806d2e74db | -11.76414 | -64.27299 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06f828a5-a263-3292-9d4a-71683b9b2b97 | -11.76348 | -64.27649 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0071244-1fa3-394e-a2cc-3601726f9ca2 | -11.75192 | -64.22537 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 074dfd97-0628-39f8-97a9-9ad441372cd7 | -11.74762 | -64.27569 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa978a37-ad74-3590-a93f-21523a39318f | -11.7464 | -64.22643 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aab4da4a-4180-3b7d-b757-c0cec801c811 | -11.7418 | -64.27817 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8943e2c-be7b-3fa5-b1b1-bda56e5e6a94 | -11.73659 | -64.2775 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90be8c83-eafb-3a93-8d8e-8175a37430bf | -11.72225 | -64.26876 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9dc9049c-90f6-39e4-a94a-bfcd2d1d5ad6 | -11.71704 | -64.26811 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 662ad71a-ff9f-3e67-947a-1db16742ef0a | -11.7062 | -64.2599 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22eac966-6855-3773-af0e-717a097ced1a | -11.7056 | -64.26308 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 048da5db-53db-3f86-a969-b7e69d46b932 | -11.70164 | -64.25573 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7bf1f2f-a42e-32d1-bfce-1f892f5596dd | -11.70105 | -64.2589 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1321d6b-f982-333c-848d-5de7f264b040 | -11.68388 | -64.06879 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b912f961-a665-325d-ad75-fcda465d1dd9 | -11.67887 | -64.06742 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e8ffad3-14f3-3ad7-b302-5a72b95d4022 | -11.67275 | -64.07189 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 563cdffb-5998-3e81-9d56-6d531e6ab43a | -11.6714 | -64.07893 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6c460ff-58c0-305f-8e1d-6c27f3040675 | -11.66774 | -64.0705 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d253221f-91e5-3305-add8-c5edfe043ab5 | -11.66646 | -64.07716 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 242cee97-5ba1-33dc-8471-f2b8694aca07 | -11.56705 | -63.97369 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a430c20-103e-36f8-b333-bacadc073993 | -11.56267 | -63.9498 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa21e337-120e-3fc4-8df2-793d91519ae8 | -11.56157 | -63.94754 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84ab43dc-a830-3620-843e-a7e5c962af02 | -11.561 | -63.95055 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0cfcbd83-c2fb-3ebd-a582-5e63011fcd8c | -11.55762 | -63.94881 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff20c2cb-5ab1-3516-a53f-fa1196917d96 | -11.55594 | -63.94957 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a985e5ec-33dc-3790-ab4c-c2cd6cc050b5 | -11.55537 | -63.95255 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e43cf59-cf13-39be-9728-444e95e84c1e | -10.86487 | -64.17831 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2819f871-5203-30e1-9d5c-98dae94cbc79 | -10.85915 | -64.18011 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfaeba8d-4ded-38c1-a198-173abbb73c33 | -12.50655 | -63.90364 | 2024-09-26 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 588aadc5-b45c-33ac-b211-a82d70840bc6 | -12.50601 | -63.90654 | 2024-09-26 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4675b07-10ca-3f6b-91a2-b5e46de35267 | -12.48842 | -64.02721 | 2024-09-26 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbc41146-8ee0-372e-8d8b-e15a03dc4c54 | -12.48787 | -64.03017 | 2024-09-26 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b959013e-d6f1-35fe-a82d-d77f963afb00 | -12.48175 | -64.03511 | 2024-09-26 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f0115fe-ca6c-3964-8e04-c9e5978554c2 | -12.47451 | -64.04597 | 2024-09-26 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38626c87-d372-3b91-a9ce-7c9b55be0f5f | -12.46895 | -64.04792 | 2024-09-26 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 340911d9-4b5d-3c7d-9855-776f49db1ffa | -12.4279 | -64.23622 | 2024-09-26 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 757bbc49-2bc9-3923-8362-f4d00ebbd716 | -8.63871 | -64.24192 | 2024-09-26 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 379cdd04-47a5-3008-af1d-f53a2e6e185d | -8.63393 | -64.23737 | 2024-09-26 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60013caa-1d72-3d14-94a1-928eba83a308 | -10.09446 | -64.47202 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7fcd35e-6d28-3fa7-8032-ae60b2a08bae | -10.0891 | -64.47095 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ce4c1fd-c04b-38e3-b227-ed115bea17cf | -10.08375 | -64.46981 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34e41e3a-8d8a-35b5-a4f1-94a4f9aa3836 | -9.76448 | -65.28952 | 2024-09-26 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f32cdd20-e213-3421-b5c0-90fc96a70608 | -9.76373 | -65.29353 | 2024-09-26 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36f03a9e-d02a-331b-b330-5effc2cc8eb9 | -9.76297 | -65.29756 | 2024-09-26 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README141.md)
