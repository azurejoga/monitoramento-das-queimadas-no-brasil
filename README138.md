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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f377a3c-e665-368a-9de5-37c70663fd03 | -11.0867 | -45.6459 | 2026-10-07 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 589624ea-4155-3fa6-9344-238a38ad3496 | -3.0191 | -53.9071 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 017ef588-3c2e-3895-b1c5-0cb6ddf87e5a | -3.0375 | -53.8865 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 793da07e-0a2a-3cf0-a5ce-213330a4f45a | -9.0282 | -69.4217 | 2026-10-07 15:10:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 618bd500-9344-3b55-8847-034372555650 | 3.5646 | -61.3435 | 2026-10-07 15:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a0d68cb7-6478-32a8-af9e-aa15200e470e | -3.2576 | -54.0418 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 191.9 |
| f8e62013-257f-3a35-9f25-edf82c3d1496 | -2.9739 | -56.6278 | 2026-10-07 15:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 8372d418-e264-31fb-a995-8d43fa21ddff | 1.7671 | -55.5859 | 2026-10-07 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 2fde7cb5-2a4a-3b76-8cce-9a9700ad84c0 | -8.9873 | -65.4379 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 12b7bcfa-dd3e-3046-8b49-904643096144 | -10.5281 | -49.9778 | 2026-10-07 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| c02543f5-bcc7-3900-820b-59490f602920 | -2.1361 | -54.4471 | 2026-10-07 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 5d843b7a-11d6-338c-b5e1-f4bab88b41ad | 1.8038 | -55.5458 | 2026-10-07 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| cbd37a89-4896-3fc8-ac52-3cd509d6a594 | -6.0447 | -53.49 | 2026-10-07 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d665ea07-494d-35b7-9fe6-86c4bfa7537c | -1.4752 | -54.7759 | 2026-10-07 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| f253dbac-7a1d-37ee-bc57-b22d3bc3b258 | -10.9762 | -45.4094 | 2026-10-07 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| ab57faec-3c93-3a0a-b3da-d29608c588f8 | -8.3391 | -72.6012 | 2026-10-07 15:10:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 114.3 |
| af2da1f4-7c6d-3fe1-95e8-6f1d7f518d37 | -7.3846 | -55.2124 | 2026-10-07 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 3d5bba18-7faf-3298-90da-55f037c0cd4e | -7.1813 | -55.1237 | 2026-10-07 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ea120c3b-d135-3405-8cbb-f777c6dd9623 | -3.3134 | -53.8592 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 1b3b67e6-83a2-3236-9979-688608b33811 | -8.6106 | -67.0486 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| edaab6b7-8d31-3cfd-b5eb-9e6b99436929 | -2.9271 | -53.9295 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 795bce98-8905-390b-8377-be30e2197d45 | 1.8768 | -55.7227 | 2026-10-07 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| fd52e262-5333-32b7-99fe-c0f8d5f0a32c | -7.2 | -55.1026 | 2026-10-07 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 314.0 |
| a8a0ab48-082f-3f98-8c58-f70be134f1e8 | -6.0075 | -53.5122 | 2026-10-07 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 7dcf1838-f532-3bfd-a903-e2885dd75c68 | -8.7866 | -47.5713 | 2026-10-07 15:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 24e1e4c0-d06b-3003-8a61-5addc5abf868 | -9.0058 | -65.4373 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f83fd7fa-aeb3-393d-a718-53c90c9e0246 | -3.295 | -53.8597 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 159.7 |
| d492ce8f-923b-3042-b68d-fbbd848fc32d | -0.4136 | -52.0151 | 2026-10-07 15:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 56.7 |
| cdf4c355-1529-3e56-893f-d8ef1a544cd6 | -6.3283 | -55.3276 | 2026-10-07 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ebeb6e36-28e6-3b53-90eb-7d6e57887ab5 | -5.7319 | -41.6589 | 2026-10-07 15:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 204.4 |
| b3e9738f-45a4-3de3-85f1-883371ab0642 | -11.1051 | -45.689 | 2026-10-07 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 219.8 |
| 288dcda1-7c71-30cf-b8ef-335a721effd1 | -2.4245 | -56.5402 | 2026-10-07 15:10:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4666f897-e0dc-3677-bb0e-22c2fb458025 | -11.8415 | -47.3048 | 2026-10-07 15:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 5fe61492-0af4-3fdd-b79b-3b3db3c8533b | -2.0447 | -54.3085 | 2026-10-07 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 9a76e752-f827-39bd-bdbb-5072751f2e33 | -3.2761 | -54.0011 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 54cb98eb-56ae-3a49-8e76-702197415976 | -2.998 | -54.7492 | 2026-10-07 15:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 04e39e7d-56ec-3637-9e2d-b7356fa6c4ba | -3.2951 | -53.8395 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| c13e2a7d-d951-3ce0-a2b4-ce772c59d168 | -2.76 | -54.02 | 2026-10-07 15:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7db40caf-a528-3553-84a6-31aaf4061058 | -3.9 | -44.12 | 2026-10-07 15:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3dc581f4-84f1-3fad-9f02-b81ef469a9a0 | -16.03 | -39.87 | 2026-10-07 15:15:00 | MSG-03 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6ae267c3-35a5-34e3-925c-ce5d5a550d9a | -5.72 | -41.75 | 2026-10-07 15:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c507088f-5d39-3974-a68e-c48e528e9b19 | -7.86 | -54.98 | 2026-10-07 15:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 670ca439-bac7-35e3-81e9-a3e91d4d6758 | -5.5 | -42.8 | 2026-10-07 15:15:00 | MSG-03 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d186505-658f-393e-a0df-fda9fa96483a | -2.76 | -54.08 | 2026-10-07 15:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4955f9a6-dd9a-3b8d-a006-d4971525a298 | -3.29 | -54.01 | 2026-10-07 15:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95e3fe98-76de-38b7-995a-949a22a58e8a | -6.22 | -52.82 | 2026-10-07 15:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a769e406-d415-3c97-9ae3-312b129a2be9 | -16.03 | -39.82 | 2026-10-07 15:15:00 | MSG-03 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47e45b61-90a0-33ae-ad99-9a087ac62cc9 | -16.06 | -39.83 | 2026-10-07 15:15:00 | MSG-03 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 44fec159-e6c3-3557-83d6-8375d54e4275 | -5.73 | -45.18 | 2026-10-07 15:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1006a6a-7407-309c-be6f-2a893765bc11 | -2.79 | -54.03 | 2026-10-07 15:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5691a93e-4280-3ba4-ae94-df16b1a74002 | -3.9 | -44.07 | 2026-10-07 15:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11492964-0a8b-3054-895c-20f43b9c6416 | -2.79 | -54.09 | 2026-10-07 15:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d433812-5d0c-3c88-a48c-5ef8f8e2dcd2 | -5.5 | -42.85 | 2026-10-07 15:15:00 | MSG-03 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 04eefda5-dd48-3e4a-8467-54be332723e3 | -3.87 | -44.12 | 2026-10-07 15:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0865a75a-b6f3-32e7-89f7-6e24f93a7361 | -7.86 | -54.91 | 2026-10-07 15:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a956e53b-9c81-312f-866c-438c529c8b9d | -5.99 | -40.93 | 2026-10-07 15:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ccf9b7ce-e377-3f9f-abcf-2ffb197144b6 | -5.73 | -45.14 | 2026-10-07 15:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b713322-84b9-32b7-9d83-b310d1e523c6 | -3.84 | -56.0 | 2026-10-07 15:15:00 | MSG-03 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a7e01e9-e07c-3b0e-bd20-666b72aac194 | -3.29 | -54.07 | 2026-10-07 15:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba151eae-f9a6-3873-995d-bd511cc7062d | -9.81702 | -38.40198 | 2026-10-07 15:16:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 7d541487-681d-32e1-bac0-80515582d8d6 | -10.30794 | -36.41252 | 2026-10-07 15:16:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| e5cbae40-3b78-3480-bff4-c4ebecbff7b5 | -6.76281 | -37.04242 | 2026-10-07 15:16:00 | NOAA-20 | VÁRZEA | PARAÍBA | Brasil | 2517100 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4aad82f2-9177-3e1f-9e96-b6bdc8eb54a1 | -9.88499 | -37.21074 | 2026-10-07 15:16:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 61f9a413-7f38-368f-834f-226cc61cf2db | -6.93651 | -38.2846 | 2026-10-07 15:16:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 4aee666f-913f-312a-b488-f09c301bbc25 | -6.87174 | -39.09517 | 2026-10-07 15:16:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 0e90b5b6-a521-3e32-985d-3554cf0cbbd3 | -5.64525 | -35.83831 | 2026-10-07 15:16:00 | NOAA-20 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 95df1b96-24e6-3742-8c92-bb5d06ad934a | -8.79257 | -36.87658 | 2026-10-07 15:16:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 46232981-622b-33e1-8f15-459ebc9f39d4 | -8.95387 | -37.61 | 2026-10-07 15:16:00 | NOAA-20 | MANARI | PERNAMBUCO | Brasil | 2609154 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 062926b1-bab5-3da7-8f13-90ea12f2ba79 | -6.6234 | -37.88297 | 2026-10-07 15:16:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 69e2f806-8fea-3e77-b4a9-35cc68a5c6bb | -6.86908 | -39.09604 | 2026-10-07 15:16:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b0e085f4-345c-30e5-bbbb-72571160bdc0 | -8.95168 | -37.6115 | 2026-10-07 15:16:00 | NOAA-20 | MANARI | PERNAMBUCO | Brasil | 2609154 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e544de35-efdf-39f1-8aa9-e281c51487c6 | -7.6852 | -37.8762 | 2026-10-07 15:16:00 | NOAA-20 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 52.5 |
| d52b8316-a1eb-3962-acd9-20606b245ed1 | -5.64605 | -35.84001 | 2026-10-07 15:16:00 | NOAA-20 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f65bdb03-251e-3471-9f63-c2597ad20cd2 | -9.88573 | -37.21674 | 2026-10-07 15:16:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 90c5df4f-28c6-3e1d-9bff-d6aa56bd2bcc | -6.45181 | -37.63024 | 2026-10-07 15:16:00 | NOAA-20 | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 35e595c9-d188-376f-87a5-719f0a885e0d | -6.18083 | -38.47731 | 2026-10-07 15:16:00 | NOAA-20 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 805743e9-2734-378e-8302-8962a262c378 | -7.2679 | -35.0367 | 2026-10-07 15:16:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ae97a9f8-ae1c-3594-a6e5-73c279818fa1 | -6.82062 | -38.53196 | 2026-10-07 15:16:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 63333a2b-028d-34ef-926e-e15f8108b9c5 | -6.55355 | -35.50873 | 2026-10-07 15:16:00 | NOAA-20 | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c7fae9f7-4601-3e92-8e30-d101da5b6520 | -6.93679 | -38.29194 | 2026-10-07 15:16:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 08665118-ac9b-3406-b33c-a75fc45d9f2c | -9.88909 | -37.21067 | 2026-10-07 15:16:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 4be54d54-8121-353a-bb37-49704cd1f308 | -6.75926 | -37.04589 | 2026-10-07 15:16:00 | NOAA-20 | VÁRZEA | PARAÍBA | Brasil | 2517100 | 25 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 0982c80f-76d6-3360-9dff-c003fb07a413 | -9.25673 | -37.43951 | 2026-10-07 15:16:00 | NOAA-20 | MARAVILHA | ALAGOAS | Brasil | 2704609 | 27 | 33 | nan | nan | nan | Caatinga | 7.3 |
| be900247-61b7-397f-ab21-59711411c44d | -8.79623 | -36.89711 | 2026-10-07 15:16:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| a2414625-202e-3d51-baae-2c7a76f9bba5 | -6.45051 | -37.6284 | 2026-10-07 15:16:00 | NOAA-20 | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 434ee584-54cd-3bee-92b1-29d6f2991c82 | -8.79535 | -36.89802 | 2026-10-07 15:16:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c8ccbae5-f601-31ed-8971-f18808862ee9 | -9.25334 | -37.43997 | 2026-10-07 15:16:00 | NOAA-20 | MARAVILHA | ALAGOAS | Brasil | 2704609 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 356e7989-5744-36ea-baef-19d5777f9a77 | -6.76351 | -37.04758 | 2026-10-07 15:16:00 | NOAA-20 | VÁRZEA | PARAÍBA | Brasil | 2517100 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b979e20e-ec40-342f-985b-e4aa2ec24803 | -9.26004 | -37.43908 | 2026-10-07 15:16:00 | NOAA-20 | MARAVILHA | ALAGOAS | Brasil | 2704609 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d70573ee-76c6-37d9-bbfd-e26f9c4c7354 | -6.45079 | -38.55085 | 2026-10-07 15:16:00 | NOAA-20 | BERNARDINO BATISTA | PARAÍBA | Brasil | 2502052 | 25 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 28898d0a-60bd-3231-802e-ec76f2d83c31 | -6.43168 | -38.13529 | 2026-10-07 15:16:00 | NOAA-20 | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5617fd42-ec5e-373d-bddb-ba8e578003ca | -6.62265 | -37.8773 | 2026-10-07 15:16:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c3d665ae-fdde-3275-b73c-b7cd03cbce6b | -6.6035 | -37.88638 | 2026-10-07 15:16:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 82e5f775-bca2-3028-a82a-bc0e23330d5a | -6.93729 | -38.29082 | 2026-10-07 15:16:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 097052d9-7d1a-3695-9918-f2cec9c05dd7 | -7.26272 | -35.04086 | 2026-10-07 15:16:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 8c259d37-667f-394c-a64b-7c50685bbc15 | -7.67836 | -37.8764 | 2026-10-07 15:16:00 | NOAA-20 | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 17.2 |
| b8fa9d3c-baad-35a0-85e2-4e5bd491ef53 | -8.07371 | -38.22812 | 2026-10-07 15:16:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 14.3 |
| a4c74dda-c77e-33c9-b30a-9b6774ae22bf | -6.93596 | -38.28569 | 2026-10-07 15:16:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 13.7 |
| d3c1a011-3852-3204-9cc8-2b52c5809f01 | -7.26446 | -35.0397 | 2026-10-07 15:16:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 7cff9887-0289-398f-bea6-fb6a31c0c4f2 | -6.61609 | -37.87894 | 2026-10-07 15:16:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 10.2 |


[Clique aqui para ver as próximas entradas](README139.md)
