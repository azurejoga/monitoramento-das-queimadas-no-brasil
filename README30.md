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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6ad06da-93be-392b-a7a0-5a342dba6b9f | -6.784 | -59.3052 | 2024-10-10 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 12c72e18-8a24-3734-9175-d80b3bb7bda7 | -7.1346 | -59.3099 | 2024-10-10 01:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 5ff18b39-25e3-384c-9f30-3b9f1005e675 | -8.6844 | -63.082 | 2024-10-10 01:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 38987e3a-8b5f-3911-9977-931949f152a8 | -9.0085 | -61.6062 | 2024-10-10 01:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 352a6842-b998-35c5-a1f7-9ea1c2fb9ba5 | -9.027 | -61.6244 | 2024-10-10 01:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e8113ce3-0ada-3d3d-8853-505397347d02 | -9.0271 | -61.6053 | 2024-10-10 01:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 25e0ec2a-21fb-3b76-8956-5a79af64229a | -9.0656 | -61.3934 | 2024-10-10 01:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 85dd2e3c-e5fe-3171-9dad-cc5439ae7e68 | -9.0841 | -61.4117 | 2024-10-10 01:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 9dcb3622-b458-38b0-8aa5-be41ca3e8d93 | -9.0842 | -61.3925 | 2024-10-10 01:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.2 |
| ce885916-0e21-3d4c-800c-cd7797798ff8 | -9.1035 | -61.2769 | 2024-10-10 01:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| b3e199d6-3530-3a4e-a736-6d4d836046c2 | -9.0084 | -61.6253 | 2024-10-10 01:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 64bcdc31-f156-3240-b358-d2711d026058 | -9.122 | -61.2951 | 2024-10-10 01:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 595e43d6-88b1-3da7-91bd-7f55c7d89796 | -9.1221 | -61.276 | 2024-10-10 01:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 318.4 |
| 21a1e474-d3be-3860-ae6b-c4553e6bb670 | -9.1223 | -61.2569 | 2024-10-10 01:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| ce7a3645-7b5b-3628-a81a-d3218ac741b2 | -10.4287 | -60.9979 | 2024-10-10 01:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f599a17c-329c-3dc6-8f9a-01f228f93d13 | -11.0254 | -57.2237 | 2024-10-10 01:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 142.1 |
| 3d6eab40-dbcd-3139-b4f0-e4058fe035c5 | -11.0256 | -57.2038 | 2024-10-10 01:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 4eae035e-7413-37ee-a8d9-1dfc4274d2a9 | -11.0443 | -57.2222 | 2024-10-10 01:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 199.6 |
| 927e2ef5-67b3-3988-a8a1-bec02a19fbad | -11.0445 | -57.2023 | 2024-10-10 01:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 173.2 |
| b6931f2d-fb6f-3c6a-bb79-8ea51f651ae5 | -11.2582 | -60.4079 | 2024-10-10 01:46:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| c1b1ff6d-746c-39b1-a309-4149ac235ba0 | -12.2888 | -43.7495 | 2024-10-10 01:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| c68c3835-e539-32aa-9443-b53f2752d9b7 | -12.2893 | -43.7258 | 2024-10-10 01:46:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| a2499fbc-1be5-3c1f-bf9e-0151c52d4f3b | -12.3987 | -54.5816 | 2024-10-10 01:46:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 9e5eb5a1-07f8-354b-8b05-a78e80c3d259 | -12.3989 | -54.5611 | 2024-10-10 01:46:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 127730b0-635f-322d-b58a-9523d2164c75 | -12.4177 | -54.5797 | 2024-10-10 01:46:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 6deef25f-78a8-318d-9860-469581cdf50e | -12.418 | -54.5592 | 2024-10-10 01:46:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| c21ae28a-aee9-3c2b-a439-38ca179f3d0b | -12.7245 | -63.0595 | 2024-10-10 01:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 4b9bd102-98b3-3da3-8d0d-981922a5c39b | -13.1845 | -51.7004 | 2024-10-10 01:46:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 9e776e32-4823-3dc3-808a-b06dc925249b | -17.0549 | -45.2808 | 2024-10-10 01:46:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 8e027804-b6b2-3fab-9ade-1b0a8a59af3d | -6.39773 | -52.72012 | 2024-10-10 01:54:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 1b26aeec-36c9-3756-805c-dbf73f8431cb | -6.39604 | -52.72749 | 2024-10-10 01:54:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| bb051927-20d8-34db-8c86-62e9f8a8ebf3 | -3.32506 | -53.22183 | 2024-10-10 01:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 60a2b1c0-70f1-3695-acb1-125211810bd3 | -3.32482 | -53.22895 | 2024-10-10 01:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 94452975-46d2-33c3-91f1-0437b799a976 | -3.25462 | -54.18285 | 2024-10-10 01:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| abad2ae2-a957-37e8-93f8-e3b505b572d2 | -3.2482 | -54.18948 | 2024-10-10 01:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| a32adc08-5818-3b22-a3fa-b5a1c13475c7 | -6.47404 | -56.0313 | 2024-10-10 01:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a6656b21-211b-3dec-a683-e93336abbb7d | -5.12211 | -56.01248 | 2024-10-10 01:54:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 3d79e891-0808-3557-a0e0-04aa7e63ca3f | -6.47783 | -58.44398 | 2024-10-10 01:54:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 55c81c04-27d1-3d2f-9cb0-9ef71ffcece8 | -6.4757 | -58.4299 | 2024-10-10 01:54:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.9 |
| dbf638d5-5d44-3523-9de3-2cd697179eff | -6.8153 | -58.99265 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 15847dc9-9cef-3fa5-a6f4-50e382e64f08 | -6.53076 | -58.42118 | 2024-10-10 01:54:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 14ae2520-24dc-3508-8a0f-fa03177c858c | -6.51767 | -58.40886 | 2024-10-10 01:54:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 807d06a1-c951-3692-99a8-da86adc07277 | -4.29458 | -60.01272 | 2024-10-10 01:54:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7d2e87a7-d0c7-30e6-b0e8-720e63a8015f | -4.28637 | -60.01974 | 2024-10-10 01:54:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d43fe6ce-a094-34fd-b3b2-f205835a0243 | -4.28443 | -60.0142 | 2024-10-10 01:54:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7dd7ccab-f8dd-37a7-9d0d-95e18c847d67 | -4.26778 | -59.88812 | 2024-10-10 01:54:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c498bd11-0239-33a2-a619-72ef6930d63c | -4.26674 | -59.89479 | 2024-10-10 01:54:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7356dcbd-7d27-320a-9cf8-65952704f2a7 | -4.25254 | -60.00053 | 2024-10-10 01:54:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 92b45d81-fe15-39ab-9b50-f1e9a7f33f74 | -4.25083 | -59.98861 | 2024-10-10 01:54:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4ad428c2-5cef-3796-992b-57aeead76b81 | -4.21016 | -59.99461 | 2024-10-10 01:54:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 5b3ff7e7-e010-37ba-8253-ce23462a0c47 | -3.89606 | -58.80443 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 321b0f64-ec5e-3a9b-8806-8457a0fe7cdc | -5.18399 | -60.28212 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3057ad52-82fa-3f6e-b360-956320de38a0 | -7.47337 | -60.61273 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 922110e7-6c31-3d5a-8b6a-e5699b2cf93e | -7.47193 | -60.6027 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 64ceb04e-7e46-384b-bdb6-6369eef74297 | -6.91432 | -59.79428 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 750829a4-56ab-3d6b-800a-b84ff77830bd | -6.78054 | -60.05827 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 237fbb9a-d9e5-3052-990b-73caa6bd2205 | -6.77894 | -60.04745 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| aa4fb2c2-627e-3bbc-814f-95d72e09964b | -6.77742 | -60.05398 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 25f0af9e-a2ea-3f40-b449-ef0f691783cf | -6.77586 | -60.04309 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ccc3e614-7165-3242-aa16-6acb4673471d | -6.76766 | -60.05547 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| fd67f907-6650-353f-be29-1132fe0a63aa | -6.71711 | -60.11867 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f8a3f2c7-57d3-3be1-8ee9-1109d6b1b09b | -6.71554 | -60.10796 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 48a085fe-6791-3a3d-bf67-3e193f1aeaab | -6.65626 | -59.77567 | 2024-10-10 01:54:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ebf0925a-b8b7-3a75-b986-24eb11022f88 | -6.60842 | -60.00658 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 11338127-b416-39eb-95b0-6f4bec19da62 | -6.6068 | -59.99562 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e0073d54-ac80-3eed-a7af-7a3cde18941b | -6.54852 | -60.02189 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a1482b02-5389-3130-9da4-e9769dcb4588 | -6.5469 | -60.0108 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 5cfcd0f5-a938-3647-bf37-fc15695066cf | -6.54529 | -59.99973 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0659e196-0bd7-3100-a85c-c38488a5355a | -6.53708 | -60.01219 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7ba66476-3a74-3bcf-b02b-ac3bc34c88d1 | -6.52557 | -60.07022 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9343a331-ca18-3865-8cdb-b16cd7939545 | -6.52396 | -60.05935 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 94d88c49-00b8-3b92-9f0a-697cf59066f4 | -6.51416 | -60.06069 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 2c639feb-c7c9-30d9-bf76-accb66a6c00c | -7.15181 | -59.39033 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 74a81b9b-cf57-3b90-b3c6-b840404338ff | -7.14942 | -59.30508 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5f95ad0f-ed07-344d-957c-c204e00e0986 | -7.14202 | -59.38565 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fc58d7a9-2a7b-37e6-ad34-0e5329418423 | -7.1403 | -59.37368 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 64b0810e-80c5-3ed8-b197-4927990e9eb6 | -7.1399 | -59.38014 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 9e4d0a7c-c04f-317b-b832-746042a13644 | -7.13922 | -59.30662 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 837bbe7e-9999-3c5d-a106-81dce0a6f50f | -7.13187 | -59.38721 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 39cc4246-688b-3dcb-98af-c2efa34cd6f6 | -7.13014 | -59.37527 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| fc04bbc1-51f1-323d-a450-c4fac6fa0fce | -7.12988 | -59.30151 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ba627570-ba45-33a7-91ef-abe86040d7f9 | -7.08465 | -59.4186 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 967aa4cb-5129-3b6c-8123-92d7395e3f47 | -7.08367 | -59.27137 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| d78a1de7-6792-38ea-af7d-3f2f71267fdf | -7.08288 | -59.40673 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 337.4 |
| 00163f09-4b43-33be-99f4-ae04385e3852 | -7.08187 | -59.25918 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| e7e2d36a-5d67-379b-b00c-6c8091ec5486 | -7.07628 | -59.43195 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 91f35cd8-c918-370f-be3e-fb5e49ad3087 | -7.07451 | -59.42013 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 6903d40f-b089-3c2e-aa0a-ecd796256e01 | -7.07343 | -59.27296 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| de570135-c0ec-3e21-a81e-8dca3f19d053 | -7.07274 | -59.40825 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 302.6 |
| 0040151b-fab8-32fb-a5d7-a5f2f2dd6984 | -7.07163 | -59.26081 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e475db86-8eb8-3106-b5e1-456085c88f85 | -7.05445 | -59.41737 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| afdd1c44-742f-39f6-9fd6-d2783aa1c983 | -7.05423 | -59.42314 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 7fef5b42-2c04-3f83-bb7f-65ed5cb27b70 | -7.05244 | -59.41127 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| a505d0c6-e596-39c7-ae20-e4840a4ce327 | -7.04431 | -59.41891 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| bbcc51fa-2b96-3e16-848d-f6daff78eea1 | -7.04259 | -59.40701 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 55a58d59-88b2-3080-8c69-d0baa065d6c3 | -7.03739 | -59.37115 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 6503dfed-3e71-3018-93fe-6f23151297b9 | -7.0359 | -59.43231 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 11299afc-1437-3db9-a402-a89a5433887c | -7.03566 | -59.35921 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 64adb43d-b075-389c-924e-5a45e5ea35f1 | -7.03417 | -59.42044 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 68e7d47d-c116-3dd6-9654-a0ebe817080d | -7.02577 | -59.43386 | 2024-10-10 01:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |


[Clique aqui para ver as próximas entradas](README31.md)
