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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7eb3c473-4cf1-3924-b8f5-1629e231b02c | -12.6677 | -54.677502 | 2024-09-26 00:55:32 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34b68650-a7cc-37cb-8f5e-483d774afc9a | -12.6546 | -54.664101 | 2024-09-26 00:55:32 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51a90e14-3cdd-3180-963e-c0e3de44ff5f | -12.6562 | -54.671799 | 2024-09-26 00:55:32 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3bfd10f-4723-3422-9cf6-a9aa2141eb05 | -12.6579 | -54.6796 | 2024-09-26 00:55:32 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 125eeac5-00e6-36ac-be26-c4f2c5a95140 | -13.0357 | -57.280201 | 2024-09-26 00:55:35 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 219696e6-da57-34e6-a01e-cc2e67fc2b6e | -13.0379 | -57.291 | 2024-09-26 00:55:35 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7cc23dd-633e-3007-8a53-c9f5319fdab0 | -13.026 | -57.282299 | 2024-09-26 00:55:35 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d768ef9-37a9-3dce-8959-c9447ba9c9d3 | -13.0282 | -57.292999 | 2024-09-26 00:55:35 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93b0dc5f-06b0-3f2f-9a06-e999e1906bce | -13.0303 | -57.303699 | 2024-09-26 00:55:35 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3119f75d-8330-3ba9-8010-0bd28d1f14e7 | -5.212 | -47.9577 | 2024-09-26 00:55:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 63a16c6e-800c-3b06-b28a-1a01bbcfadfb | -5.2306 | -47.9566 | 2024-09-26 00:55:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 3c3985f8-debd-3ef2-b6e9-68510540f58c | -5.943 | -52.1241 | 2024-09-26 00:55:40 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 89388c54-6a9b-31a1-aca9-2627af2b84be | -11.2149 | -50.279499 | 2024-09-26 00:55:40 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13a62ca1-2634-36ba-aa5e-7698b1ce63ac | -12.5932 | -56.961601 | 2024-09-26 00:55:41 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2cfab68d-6ddc-3ad9-afe0-6c425ec6a992 | -11.0126 | -50.163399 | 2024-09-26 00:55:42 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 964eae0a-f0df-3002-973c-d84d297ddde9 | -11.0046 | -50.173599 | 2024-09-26 00:55:43 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7bd25ee4-39d1-3284-b2a2-d95c02f828cf | -11.1209 | -50.812099 | 2024-09-26 00:55:43 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3baf00b0-ba67-3b2c-a311-8aa4acbab731 | -11.1227 | -50.8195 | 2024-09-26 00:55:43 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| df91ffb7-2a8e-3b26-95e8-baaca4f602e5 | -6.5772 | -60.0437 | 2024-09-26 00:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 5b9f8f52-23ca-39a4-92d0-69a857969e37 | -10.9368 | -50.1483 | 2024-09-26 00:55:44 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2733137c-9308-3253-8d9a-07846488f804 | -6.7839 | -59.3245 | 2024-09-26 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f8168a73-f4b9-3e31-96da-7c9ea6762b87 | -6.784 | -59.3052 | 2024-09-26 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 20cc875d-1dca-39fc-a64b-beb38142e5b5 | -6.8023 | -59.3237 | 2024-09-26 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 72ec3b60-cccc-39d6-867b-0791c358f8f5 | -6.8024 | -59.3044 | 2024-09-26 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 93fc6698-6fe5-3dfe-a9eb-e7e0b751c726 | -6.8384 | -63.1457 | 2024-09-26 00:55:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 5eea5570-f695-379c-8f99-a3b7f32fae7f | -6.9305 | -63.1241 | 2024-09-26 00:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| a2d3e13b-5819-3bfa-b60d-fefd529373ca | -6.9306 | -63.1053 | 2024-09-26 00:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 3a9dedc5-0dfc-308b-80eb-b57bef19c89e | -6.949 | -63.1048 | 2024-09-26 00:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| cf5111b8-51d4-39f7-9b24-db2d8e1e282a | -6.9681 | -62.9349 | 2024-09-26 00:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 3b5d5b45-6aa1-3e95-b285-1bf1821d4970 | -6.9682 | -62.916 | 2024-09-26 00:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 0e039673-ddfe-3797-ae54-fadb8753dd3a | -10.8029 | -50.105301 | 2024-09-26 00:55:46 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a23fc9fd-cb22-31de-84f5-5346e5b34419 | -10.7932 | -50.107601 | 2024-09-26 00:55:46 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa2e322a-bf2c-3b99-aa50-f3173d7c9760 | -10.795 | -50.115501 | 2024-09-26 00:55:46 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eac67a07-ade8-3cc0-91f2-a352f0787588 | -11.0811 | -51.450001 | 2024-09-26 00:55:46 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82fe2a21-5315-3f30-b5bc-aea783590ff6 | -11.0616 | -51.409199 | 2024-09-26 00:55:46 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f1e7f5e3-1a95-3f56-84d8-c25d565fd32b | -11.0632 | -51.416401 | 2024-09-26 00:55:46 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 62ce5f13-9683-377a-b1fb-38340aaa221c | -11.0648 | -51.4235 | 2024-09-26 00:55:46 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 804e3229-d89b-3fe5-9475-db61c02fb8b1 | -11.0534 | -51.418701 | 2024-09-26 00:55:46 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ab368217-1ebc-33b1-aaed-27b617b449a1 | -10.6395 | -49.8909 | 2024-09-26 00:55:47 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c58410dc-7c1b-3822-b229-72d137722f50 | -10.6414 | -49.898998 | 2024-09-26 00:55:47 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03b02fbe-0d5a-3e11-84ea-8a93fed2aa4b | -7.3637 | -55.5134 | 2024-09-26 00:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 180.5 |
| 1146429b-dfdf-3432-b1bc-bca0318b6b86 | -7.2905 | -61.106 | 2024-09-26 00:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 127.9 |
| e095bcd8-1be8-361e-b0ed-850e653f3a25 | -7.2906 | -61.0869 | 2024-09-26 00:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| b66c2a32-16c6-34f9-8d99-d314c00ff5d7 | -7.3452 | -55.5145 | 2024-09-26 00:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| ab20f4af-bf70-31ae-9cd8-3042f45cca98 | -7.3636 | -55.5334 | 2024-09-26 00:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b9c3c5c0-83d4-35a9-8592-8ea1e293db9d | -7.3639 | -55.4935 | 2024-09-26 00:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 75c33c46-7385-3269-9051-579e515de4ce | -7.3823 | -55.5124 | 2024-09-26 00:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 164.5 |
| f4d7b6cc-c249-3edb-ae9d-99f8d454b42e | -7.3824 | -55.4924 | 2024-09-26 00:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 973883a7-720e-3ff6-b139-81c6e6e97018 | -10.8602 | -51.159599 | 2024-09-26 00:55:49 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6cb8005a-9363-3b79-96e5-4cfb70267684 | -10.5094 | -49.7756 | 2024-09-26 00:55:49 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a786265-3e57-30bc-b37f-3ed851f9995c | -7.797 | -54.7263 | 2024-09-26 00:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 9b6385dd-814b-34f0-81a0-165377f30bc5 | -7.8154 | -54.7453 | 2024-09-26 00:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 4ae35d96-b96e-3de6-8253-c574b7760511 | -7.8156 | -54.7252 | 2024-09-26 00:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 39846d1c-15b0-3836-8104-b5d6566d7539 | -10.9364 | -52.085602 | 2024-09-26 00:55:51 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4edc5fa1-9331-3077-8221-e69a83b30690 | -10.938 | -52.092602 | 2024-09-26 00:55:51 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0c31c5a-f9db-36fa-a8c3-1a64b7544f26 | -10.6761 | -50.986401 | 2024-09-26 00:55:51 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a7ee9f29-bcbf-3b32-bf7c-fafde68577f9 | -11.3188 | -54.041698 | 2024-09-26 00:55:52 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb80ada1-5496-3585-92f8-a84c0edb96d0 | -11.9815 | -57.164001 | 2024-09-26 00:55:52 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a6fb84e-8bb8-3ff3-95d1-9adb04f7a4d6 | -10.6133 | -51.117199 | 2024-09-26 00:55:52 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d7b7a7a-b8f5-30a2-859d-4a45c1fe3d04 | -8.1757 | -61.3946 | 2024-09-26 00:55:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 2e7e1b3b-d690-37e0-a030-5c6792c55c8c | -10.6001 | -51.104801 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 73d47bf9-8cd4-3f21-9e63-fcce8fbc3977 | -10.6018 | -51.112099 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3aa3047f-b41d-3eb6-b61a-7e121332c7ec | -10.6035 | -51.1194 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4828f3dd-b483-312b-b128-c1b01fe4b20d | -10.4873 | -50.748199 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 463ec9d3-589c-3dcd-92a3-c9b9fcce1729 | -10.489 | -50.755699 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d5469cd-5a79-3472-be45-a9c604878caf | -10.5691 | -51.104401 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 11305184-6918-3aaa-8515-b4757ac9425c | -10.4913 | -50.810501 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 702a927e-1f0a-3670-84c2-ace17e7ee172 | -10.4931 | -50.818001 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 84c7b577-df67-3a4f-afba-7a5b599f3c8e | -10.4948 | -50.825401 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2425b501-300a-31e6-a501-6610fbe15898 | -10.4965 | -50.832901 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 719f7096-2db0-38a1-8a92-13f3d83e1293 | -10.5576 | -51.0993 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46f05e5d-534d-35ba-90ce-bfe4cfec8bae | -10.5593 | -51.106602 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e7f552b7-27d8-39c6-897a-09e1ae181593 | -10.4694 | -50.760201 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b66a29c-10cd-37ef-89dd-045942ae8d23 | -10.4815 | -50.812698 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fbb29327-b3db-3d70-bd09-595ef79678b8 | -10.5478 | -51.101501 | 2024-09-26 00:55:53 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a539d07d-45eb-32b0-9fe3-fadd2d416349 | -8.3153 | -55.0157 | 2024-09-26 00:55:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 53a64a91-022d-35b9-b04e-bf1923784822 | -8.3155 | -54.9956 | 2024-09-26 00:55:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| f6c963ed-3009-395a-bb66-8fb6b1753e25 | -8.3521 | -55.0736 | 2024-09-26 00:55:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 075e0e9c-a023-38e7-811a-304b03071b0e | -8.3522 | -55.0535 | 2024-09-26 00:55:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 0bb0c9e5-cb45-3789-a82d-408851fe501e | -10.4596 | -50.762501 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 28066eb0-0a3f-3d8b-bedc-e6dd234e9792 | -10.4614 | -50.77 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a2801ec3-18b5-3de6-9321-9eaa669b7fef | -10.4631 | -50.7775 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a9ffac0-804a-3697-91b5-567b7e88a98e | -10.4648 | -50.785099 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bdc6c96d-6390-351f-8bca-57aa4cb568e5 | -10.4666 | -50.792599 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10b2ad9f-80db-30e0-9437-92265837a083 | -10.4683 | -50.799999 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d50f7f9-a8a4-32e6-91a4-008b8d349131 | -10.47 | -50.807499 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b583a90-9c96-3686-ad0c-879a9bf9aa94 | -10.538 | -51.103802 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65f3851e-f2c7-3f0f-907e-0071399d9f72 | -10.5397 | -51.111198 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b98758b1-995e-3610-80b1-ef84267040f8 | -12.272 | -59.202702 | 2024-09-26 00:55:54 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6a77077f-f6cb-3da8-a7a2-140d0e9d433b | -10.5316 | -51.1208 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 69af6e57-711a-3ff2-859e-02a5b1da1fb4 | -10.5122 | -51.171501 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63788334-6b7c-3ed8-a799-cd2a2fd28e03 | -10.5139 | -51.178799 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b100473-2e82-3ab9-b3e5-6c5dc92724a6 | -10.4975 | -51.151798 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5c28455-0c99-3651-99d7-8b7d8adcd78f | -10.5125 | -51.217499 | 2024-09-26 00:55:54 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28eebde9-c7cc-34d1-930c-0cf05716cb2d | -8.5542 | -63.1814 | 2024-09-26 00:55:55 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 9029a49c-192c-35dd-866b-9078a7ef5d9a | -10.4893 | -51.1614 | 2024-09-26 00:55:55 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f422d9d2-a060-3d54-934b-ddf4037789b1 | -10.491 | -51.1688 | 2024-09-26 00:55:55 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f1477fb-a416-3e95-9af3-f5f0e0552848 | -10.5027 | -51.219799 | 2024-09-26 00:55:55 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44a30265-bff8-3783-a27f-ce5f78a600f9 | -10.5044 | -51.2271 | 2024-09-26 00:55:55 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 283102fe-27b1-3109-aa64-953a0ed20517 | -10.4879 | -51.200199 | 2024-09-26 00:55:55 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README23.md)
