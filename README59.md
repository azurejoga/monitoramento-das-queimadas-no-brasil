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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1332db83-50c4-3ac4-a10d-c812149e1ef4 | -9.50352 | -60.51148 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ade89c9a-e324-3e84-b90c-18adcb1c0423 | -13.1287 | -57.16134 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be7cebd9-f0da-3f40-867f-5637de256733 | -13.48139 | -56.65997 | 2025-08-15 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |
| f85237d5-be95-39e8-9c10-fa08b04ab536 | -11.36099 | -55.41611 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ccd26a7-9005-321c-a86b-09e290e3a9ff | -9.1611 | -59.67134 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d5ec4ad-97df-32b7-8cb3-ec42dbd3340c | -9.15874 | -59.68875 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98464a2b-917b-31c7-bfe2-91e9b62ec66b | -10.01076 | -58.42553 | 2025-08-15 05:44:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 47391ac0-f4a3-38cd-8266-f02593241ae4 | -9.52733 | -68.29512 | 2025-08-15 05:44:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d13925c-6c49-3ce8-86c5-08c1346cb834 | -9.50448 | -60.53534 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4de2d7d2-8625-3df5-98a6-1fbffcb74415 | -9.935 | -60.48119 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c1812bd-4f3c-3b86-b85c-92d22d7545f8 | -9.50705 | -60.54754 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 42a80be7-7595-35d8-ab19-1c08919d8968 | -8.94557 | -62.23599 | 2025-08-15 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 134ba3fd-4725-35ce-8082-3d21465df2e7 | -9.63231 | -63.09151 | 2025-08-15 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3f355fda-b0a0-3066-908b-7a014f461866 | -11.34336 | -55.40907 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fcb3924e-12a6-3c6e-9f82-fca65f8f79a6 | -11.35546 | -55.41083 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 37c8d2fb-4131-3f24-84cf-99496d43c53a | -7.60259 | -63.52646 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c93adca-8a58-308b-95ba-2077550ed66c | -8.32008 | -70.07221 | 2025-08-15 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79a53063-4ff4-37b4-9c11-5f54f35b1e95 | -8.10756 | -61.21207 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 552091e9-1ea6-37cd-b8c3-d4caf9a1ed9c | -9.17817 | -59.67834 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1fb2ee35-d142-375a-a41e-5b03128b2235 | -9.15992 | -59.68006 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7e9295c-734c-3671-bed5-5b2b8eae8fe2 | -10.04472 | -64.89772 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca8b0885-c716-3184-b75b-dab65d003203 | -13.12827 | -57.165 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94ae3062-0505-38dd-93c9-8b009de2a119 | -9.26374 | -60.77232 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 864b9af0-61de-3a46-aa4c-44a4ceef225e | -10.3634 | -67.71085 | 2025-08-15 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e453b9c-cb6e-33b1-bd87-09bb3beb26b7 | -7.9624 | -61.76165 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c29836df-a41c-3be7-be71-b025cb61d1a9 | -9.17698 | -59.68704 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6542090c-e2bc-3e77-a491-2c1157a09dbb | -7.87792 | -61.81046 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a5a4adc-9758-3238-8d87-e99d3f1cf170 | -9.61169 | -67.28667 | 2025-08-15 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9726eb0e-3ea8-3ed3-bf41-05762809d98f | -13.11166 | -57.16279 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1074c1bb-e7c8-3467-947a-805f7e6ca45f | -11.94634 | -62.83512 | 2025-08-15 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d18c9e9-66a8-36a9-82ae-64bd6d7f7d87 | -9.15168 | -59.67437 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 70036d23-3aa4-3a43-8543-c9bed77edf09 | -11.41014 | -58.54168 | 2025-08-15 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48f09ed6-2184-3e50-bae6-b0ff6fdc88bd | -7.61952 | -63.52485 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d0fb767-e64e-35b7-8ec8-c5a3ad940dde | -13.11726 | -57.1671 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f18413b3-09a5-316b-9e27-4ea48c7b8d79 | -9.01318 | -59.54184 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d91f8d51-689c-34f3-8e08-02f2f7e428ec | -7.96118 | -63.46494 | 2025-08-15 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 993f4bf1-8ebf-3758-8388-2a67bad3df78 | -9.47621 | -63.92601 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9b563c9-47e4-3185-bf99-4c8b2f31e0f9 | -7.80823 | -61.33912 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93c0cbc5-cec7-3af8-848f-0aeac52c0cc0 | -9.83514 | -60.76039 | 2025-08-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3993edf7-a562-360e-9050-523b633c5c62 | -9.15816 | -59.69308 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21e5673b-fc83-3433-83b7-77b5cb8be882 | -9.16315 | -59.68945 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f9508e9-9ca6-3161-afa2-be8987862c74 | -9.62971 | -63.09645 | 2025-08-15 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37d7078c-ba20-31a1-8f2a-ad119de08483 | -7.87725 | -61.8151 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea0fdc70-e27a-3995-90c0-46724ee0f2b2 | -8.48105 | -64.04144 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8fe9185-0655-3a7e-8030-890af699e0fe | -7.53934 | -61.34483 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c81d0964-c22c-3192-bfba-1302b8d0f005 | -9.17936 | -59.66966 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fd2c57c1-0557-3629-95c4-9269f3392156 | -8.11419 | -55.58084 | 2025-08-15 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d46f357-29ec-3e8b-9120-22f47b49ff94 | -11.83353 | -55.21129 | 2025-08-15 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23ef2829-22e3-3a25-8ab2-0e87e43ca409 | -9.17316 | -59.68202 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bf5a8a9-a00b-318a-a800-6d62d4c4f4a4 | -7.94655 | -61.76402 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28b3c080-1e31-38c7-a5a7-37c607e31106 | -13.47371 | -56.66434 | 2025-08-15 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f6e2e460-62cd-31f7-8909-68c0c9120df0 | -10.35488 | -64.44339 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97694937-6fd0-3601-8674-bb03efaacb78 | -9.34717 | -62.583 | 2025-08-15 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 49476ccf-4cb9-34a5-a38f-daf7eda88b33 | -9.50298 | -60.51539 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73c3e3ad-caf0-32b4-a743-50ca0ae0e043 | -13.11903 | -57.15253 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7936a75-6e7f-34fb-9890-74e7bc3cf801 | -9.19765 | -59.66779 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15615e6c-72fc-35a0-b9a9-dc528606f110 | -8.29523 | -64.01804 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6beb6e1-7c9b-3fcd-9b03-2fa949f5c5f3 | -9.16816 | -59.68572 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 524afcf5-fe95-38f3-b115-eaf6ba76f535 | -9.27606 | -60.77417 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6897ef85-e921-33b4-9b13-99e1bfbd0967 | -11.34778 | -55.42376 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bb60d536-220c-3f93-8f70-d7ce9ea03d44 | -7.8029 | -61.3484 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c16902d-b00f-3e74-bc2c-6c393403249c | -7.8817 | -61.81104 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98e3693f-e2fa-3b81-971e-0ca05cb5a9d8 | -13.11172 | -57.16637 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4122419-7e7f-3b16-b8be-b884aafcd78d | -10.05016 | -59.11521 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f1ae12b-d824-3bc7-808f-531f39a90662 | -11.35935 | -55.42986 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8d333d1d-08ac-331d-b71e-a1c1879f056e | -13.47996 | -56.66077 | 2025-08-15 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| d9504b13-f1ad-3657-8a9f-55444152d961 | -9.83046 | -60.76353 | 2025-08-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb7be4f1-585c-3289-835e-951602eb963e | -10.11739 | -57.77038 | 2025-08-15 05:44:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f114fd7d-0939-352d-befc-03fb15939942 | -11.35989 | -55.42533 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e45dc52e-5901-32cf-9eba-c7872af20a1c | -9.50082 | -60.53092 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 1ca982d3-5935-3294-8482-76d4dec36e71 | -9.18259 | -59.67901 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d1f92c2-354d-384b-a7fd-83db98db9882 | -9.18641 | -59.68399 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed0e9270-4cd9-3359-9de0-3ff239650808 | -13.11845 | -57.15259 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 507dabad-63d0-3ef7-a8d4-9176d7f45b16 | -7.88236 | -61.80643 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 824011c3-5915-345f-ba86-e86a2e339f40 | -9.24172 | -64.25034 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b105dc88-bf7c-3dfb-bed5-e2355107c1e9 | -7.88036 | -61.82032 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11a2928a-40ce-31fe-b40d-e44c248ed1d5 | -9.15072 | -59.42654 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10c8d7e5-1d1f-33fa-bab0-36794c210ff6 | -13.11948 | -57.14891 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a6d1f13-4477-327b-a73d-e796f7154616 | -8.10581 | -61.19633 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cdbd18e-b3cf-3861-8aca-b8266cec5d75 | -9.50136 | -60.52705 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0893f55b-6617-3b54-850a-cb5ccd3db96f | -9.21154 | -59.66521 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6b5ab5c6-7541-36bf-860c-b7f840668586 | -11.31723 | -55.20566 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 783c7ac8-4e7d-374d-9649-3de251e8897d | -9.51814 | -58.35517 | 2025-08-15 05:44:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc605941-6e60-3c31-9666-6152ce43b492 | -9.90184 | -60.44157 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecffb6c5-7cbc-33aa-9323-1ff3e9672e45 | -11.94505 | -62.83753 | 2025-08-15 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f89040e6-aec2-3f8a-bbc3-624bfd991a3b | -7.94929 | -61.7454 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| daee37f9-a184-3b4d-9b46-ac68d4bd71a2 | -8.91626 | -60.7308 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d3abb8e-9a63-3f56-87e5-94f2fa50a4bb | -8.92088 | -60.7277 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf99ff70-011f-3ff1-b4b0-8ad4b485ca8a | -11.35436 | -55.42009 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 18801b7e-f286-3b28-a647-6090e5996888 | -9.90174 | -60.44002 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1f8a231-4b60-3270-b448-0c5354c1c310 | -9.18436 | -59.66603 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 82c92ea6-2a81-38ae-b22a-b0ac66dcdd79 | -11.41562 | -61.48799 | 2025-08-15 05:44:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 409f4a73-3152-3efe-9f74-8437b0e80f7e | -8.10829 | -61.20701 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3747151c-c671-3ec7-8400-396f05bb9f3e | -10.37399 | -69.11032 | 2025-08-15 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0968b5f-b4f2-3ad8-ac99-cec307428ec0 | -7.58767 | -63.46164 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f33ec593-b51f-3199-965d-42f18bcda6f8 | -9.16875 | -59.68137 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c91fd1ac-4859-3178-809c-9330206e993d | -7.60605 | -63.52699 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7cd6ac2-6553-3c4b-800b-48eaaf3a5dc0 | -8.68484 | -62.45918 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9b0a2ed-6b16-32d3-9cb0-5a801a6beac9 | -9.34739 | -60.33053 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d735cb45-066c-3de9-9ba2-c500a92a7234 | -7.53617 | -61.33939 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README60.md)
