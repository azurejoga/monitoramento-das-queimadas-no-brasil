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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a02e26ec-5f4d-32cb-89c3-174af6995561 | -11.55336 | -63.73805 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ce0a70d4-c992-30dd-b503-e10b456127d5 | -11.5218 | -63.71342 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ccdbbd54-fa63-3cab-bc97-70c22d492986 | -11.51269 | -63.58608 | 2024-10-03 02:09:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 03211801-5a10-3488-b0a3-fcd6fba59424 | -11.5035 | -63.58746 | 2024-10-03 02:09:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ffd15b4c-2a61-3171-b55b-09d24ec88acd | -11.49857 | -63.61806 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9f06cb07-76c2-3f9f-9b39-2951e6417e65 | -11.45829 | -63.34276 | 2024-10-03 02:09:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 99f3b0ae-f514-30eb-b036-73cb2e323ba1 | -11.45683 | -63.33284 | 2024-10-03 02:09:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2eed2219-20ec-3c00-bbba-ed46beee602c | -10.99829 | -63.9185 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f973bcbd-dada-3ead-ba28-9a12f229e8da | -10.91122 | -63.88908 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4a35a472-25f4-3668-adce-e73ce124800d | -10.90988 | -63.8798 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 65e87a55-8f3c-3a4b-be92-9b29e1258eb2 | -10.89579 | -63.91126 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c048cf05-a90a-3202-bb27-24b09b2f27d9 | -10.89443 | -63.90186 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 5e7ac7b4-89e7-34ec-9efb-e6d6d9076c1b | -10.89303 | -63.89223 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 30.0 |
| a34ca7eb-0bf7-38b3-b420-a783f7af649b | -7.38219 | -64.67422 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 38302880-3f2c-3f33-98e6-61919abab388 | -10.87475 | -63.89469 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 75eb23e0-e340-3502-b322-b9de6f4fe27b | -10.87335 | -63.88509 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 78d7e062-ff9d-3a9f-ba50-8053a7c9fd59 | -10.8642 | -63.88636 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 90faffe8-2062-3ee6-85e0-4aa37265b009 | -10.85365 | -63.87803 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c6b3024d-6033-3d94-b1a8-a82c56a841bc | -11.65008 | -64.21803 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c3ad9c20-30e1-3701-90e6-a0fdd7688654 | -11.64883 | -64.01803 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 99b8550e-6dc5-31dc-b6de-f5c9595b7fa6 | -11.64115 | -64.02879 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 636599ee-beef-3530-8324-606386ef5e14 | -11.63347 | -64.03946 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 20.4 |
| ff542b90-d28c-379f-951f-5bd52e8fbd03 | -11.63211 | -64.03009 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 0d1da8ff-5446-37eb-99fd-f2504ca1d4ff | -11.62393 | -63.97363 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 91babaa7-9e26-3f17-a165-c80e4429242c | -11.62357 | -64.09835 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 26f10b15-8830-3dd4-bf9b-a816d85bfce1 | -11.62308 | -64.03143 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 28bd8a93-ee41-391a-91a0-d9555d774be5 | -11.62256 | -63.96421 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f3e1a513-259b-3a51-a26a-f544957764e8 | -11.62119 | -63.95478 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| bfbcf86e-2c7a-3cc9-9091-d8335f793370 | -11.61527 | -64.10592 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 852fad3a-363b-3c15-ac17-d476f2bb488d | -11.61261 | -64.08723 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a362ae0b-4515-36c3-abc5-8dd4059d5569 | -11.61077 | -63.94669 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4b138f5d-d884-3153-b666-483893c7e055 | -11.60924 | -64.19255 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| db86e245-f8ae-31a9-acbf-c045b79f00cd | -11.60791 | -64.18324 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fb7f5787-f091-304c-b8b4-3ea1dcbaa547 | -11.59892 | -64.1846 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e09b3eee-4464-390d-b53e-a8cf2882ea6b | -11.59127 | -64.19528 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eda755b7-1100-3ebf-8677-30b8b68141c4 | -11.54719 | -63.95306 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fe116f11-9258-3684-a44e-70df4891c73c | -10.98693 | -63.96849 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 85c52429-c062-30fb-a765-89733b98c59c | -10.98558 | -63.95922 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 9919938f-8884-3691-be22-a616cb71f3ce | -10.98421 | -63.94978 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 233bb199-6d98-331b-9db3-c530e15f7408 | -10.85228 | -64.18478 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4b7a5666-cffa-3c22-8a77-d3aba7c66437 | -10.85093 | -64.17538 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b8dd6b7e-ab16-3c6c-81ef-3c107f5f4ed0 | -10.83829 | -64.21572 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e0f1f91-7658-3892-bc12-bc16974ceb4d | -10.83693 | -64.20632 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b2359ef7-893a-3ad4-a7fa-bdb47fe0b735 | -10.83557 | -64.19685 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 140b8703-1390-35e6-b56b-620c8d0bc9af | -7.46663 | -64.68439 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 48982a19-866d-3f0a-a2da-2b5277e628c7 | -7.46102 | -64.45155 | 2024-10-03 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1aee4b29-1aa6-37d9-818c-66089407a71f | -7.38356 | -64.68368 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6dc6023a-1c91-30bf-b5b5-bdba3bc72c29 | -7.28869 | -64.66486 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dbbdff78-7711-35e0-b388-e482b8b8ae0d | -7.28732 | -64.65537 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cd7896e5-3b69-3cbd-9fba-63fb0e79a00c | -7.67503 | -64.98094 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cb7eaacf-402f-3329-853c-d3354b4e3e9f | -7.48613 | -63.98891 | 2024-10-03 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fce57d2b-8188-3fa6-a674-9eb1ada04575 | -7.45963 | -64.4419 | 2024-10-03 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 1a6115e0-faa2-39c7-abe7-422fb2378545 | -7.45044 | -64.44328 | 2024-10-03 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 29ba4f9c-98c5-3f8e-967c-e54096460a62 | -7.29782 | -64.66352 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 176ae8f6-4d26-3f16-a1cb-7bc440ed9ca2 | -9.44672 | -64.54041 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 67f1c997-2653-375b-854f-31034e1c646f | -9.42868 | -64.54311 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b9f23963-80f6-3e12-90f4-dec937da0058 | -9.31768 | -65.37965 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9529fa02-9567-3f91-9126-be0df8f64b91 | -9.30674 | -65.37799 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9fa7215b-e3be-3499-8eea-5d8575d6e89a | -9.30548 | -65.36904 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| ff5ee867-d01e-3fe5-b9f3-eb6844286d02 | -9.30422 | -65.36008 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 084b2784-9f15-3ec5-a5ff-1a0080c79198 | -9.29285 | -65.34344 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ca167ec6-6b1f-36eb-9b17-60a442069189 | -9.24599 | -65.60278 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fd80a6df-af06-3b91-90de-cb2a04faab10 | -9.04697 | -64.45246 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f8a40ad-5c0a-3650-9d88-9c3af2dafc25 | -9.04562 | -64.44305 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0fb4e7cb-5f60-3de3-8baa-13c42e7e9996 | -8.7429 | -64.19505 | 2024-10-03 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| dcf63369-3723-3df5-9892-435b3e9bda62 | -8.74152 | -64.18539 | 2024-10-03 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 684293f7-2144-3e9e-b900-05e5ce836f7f | -9.17657 | -65.55829 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2bcdea53-5ff2-3163-8239-7bfc58c0ba25 | -9.02247 | -64.4753 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2c565a16-9977-3ce6-9043-4e5f75faf8e9 | -9.02112 | -64.4659 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 377bcae9-28c1-3257-89ad-4d22e47525ff | -9.44804 | -64.5497 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7fae8107-0c7a-3b73-b9b6-1023812c435f | -9.43903 | -64.55111 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 62a92b4a-069a-329b-a1ef-2c5dfd095f5d | -9.4377 | -64.54179 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 492f9c06-f071-3b5d-9f5d-452960c454df | -9.99583 | -64.77004 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 227a579d-0077-3e01-a545-44d6c3f12ec0 | -9.96903 | -64.774 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0dbb0022-ac43-3eac-942b-6ba8a1548ec4 | -9.96006 | -64.78127 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| c072eae0-5809-364a-b8e0-fececf48677e | -9.95877 | -64.77213 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3a342665-1dc8-33ca-8c18-494765719468 | -9.94239 | -64.91388 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4d8bf33c-31fb-3362-a347-f3f9126577db | -9.9411 | -64.90481 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2e9d4d96-b999-3726-b8b4-025ab4bb1bcb | -9.93067 | -64.76699 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 644ab8f5-c97a-347d-9ed7-4485601a39e9 | -9.85281 | -64.8685 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e3403d55-54b0-38c2-b37f-568f08429078 | -9.81094 | -64.95806 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4b0467b0-6158-307c-bb4e-97a465580991 | -9.54569 | -64.33172 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d617ed37-03d2-3542-8611-b374dc1f9913 | -9.37579 | -65.47151 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ff658751-dd11-3576-9b5f-5a291e9d3920 | -9.99453 | -64.7609 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 149c36ae-3386-31cd-a1f0-7a9f3439cd17 | -9.9869 | -64.77135 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a8cff864-4dad-3e3e-9142-ce8b6703012f | -9.81985 | -64.95676 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4ebd9e18-a196-31d3-a5d7-d9adb88cbffd | -9.71056 | -65.75925 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 16ccd16d-dbb5-37f8-bff7-2db6b1746bec | -9.68508 | -64.72215 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 005c3e10-73a9-32f7-b284-86ceac6de638 | -9.59729 | -65.67283 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bd2a5e87-7388-3841-8f50-6212fc1b3b47 | -9.3934 | -65.53274 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 857c4079-66dd-3a06-8ae2-ff4ec6bda7a4 | -9.3808 | -65.50725 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 61413aad-9d9c-33d3-ad5d-2f07d88aa772 | -9.36534 | -65.79725 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ab2599db-4b6f-3aa8-973c-7d265d470b72 | -11.62965 | -64.98723 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 73ce76b2-b98a-3e2a-bbfc-105e1f70b4c9 | -11.62206 | -64.99754 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 01089336-c77f-31d3-94b3-261062010b47 | -11.6208 | -64.98854 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2e83636d-52a6-3a8c-9617-d4345e8995dd | -11.61447 | -65.00786 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ce335aba-5633-3fd5-bcf6-f5d3bd3e0c55 | -11.61321 | -64.99886 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 0a42fe59-9a0c-377a-adca-a4c815eacd34 | -11.61188 | -65.1826 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e0e81495-516f-3b2b-96fc-46904af7677b | -11.60811 | -65.15565 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ab466f5f-7ca1-36f3-b862-3d04e4af9168 | -11.60685 | -65.14667 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |


[Clique aqui para ver as próximas entradas](README53.md)
