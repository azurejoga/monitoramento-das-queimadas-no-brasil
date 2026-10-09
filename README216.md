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

## Dados Diários - Página 216

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4727fa5-1e2a-33c8-94f2-d72f20cc4447 | -6.4162 | -55.19489 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ed9a8e6-3688-31c7-ba3d-3fc70d6f316a | -6.13009 | -53.05793 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 75a1b904-0825-3578-abc5-5d270cf531f6 | -5.94801 | -55.34212 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e2551de2-adb2-3dff-b2b8-008960930a49 | -4.73285 | -55.66208 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0834708e-c180-354a-8ad9-198e5a164523 | -12.21662 | -57.13006 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9739c6d6-23e2-33ce-9e54-7a09b4e64355 | -14.8745 | -50.29899 | 2026-10-09 05:25:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d31ff85-048e-3eb0-b4c6-3a4d21f7ca7c | -11.76006 | -58.28697 | 2026-10-09 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49be636f-383f-3f22-ab58-88b5e9c461bc | -5.98476 | -55.36431 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5150f67-f40d-313c-a9b7-deb02a5d80e9 | -7.6188 | -46.53805 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc0d7473-259f-3f41-b5cd-99ff8e3e0fa5 | -11.75125 | -61.06234 | 2026-10-09 05:25:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 38afd663-d933-3c0b-b75b-4d3e70c8a64b | -6.05161 | -59.92143 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcdfcb8e-abe6-35f5-874f-fcbd637ea558 | -6.72525 | -48.11634 | 2026-10-09 05:25:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14ae6f8e-0648-32da-b3bb-52e56bdf327b | -6.48764 | -55.3079 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 933f8966-0c54-3be5-ab8a-369e7349f352 | -10.85283 | -59.11547 | 2026-10-09 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6f46cd6-7939-359a-9da9-925f2855f1e1 | -6.4388 | -55.04437 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45a990a2-11be-3549-b7d4-788eb38a4295 | -5.82081 | -53.83284 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6c62fd8-16a2-3371-a739-6c21fe3b7638 | -4.03297 | -59.83977 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| faba0104-de99-3262-a776-cc6572a155bf | -5.88058 | -53.51811 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e25d9865-b93c-35bf-882a-20f6270e6ce4 | -5.81729 | -53.82855 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8547d15e-747c-3d0f-8bd0-4b4ebc687884 | -5.70527 | -53.48403 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1e1a11ee-6612-3cb0-a3b8-896fb9964dbb | -13.16489 | -54.34925 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b5dbf6eb-3e65-352a-b248-9b7f13ed09a5 | -4.12658 | -59.8909 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 578b069a-ffa7-3294-9d52-e5c9f17bcf78 | -6.0094 | -53.49259 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4deacfab-7749-335e-8bb2-6101024d83b1 | -6.37879 | -56.22453 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51f5f869-4d51-3bcd-8d1b-ba468777e7f3 | -12.21235 | -57.13386 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dfa917a-daea-3159-b51a-bb65b3b0e076 | -5.29031 | -60.09374 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2360317e-17e8-3226-b8aa-3581bd8c0361 | -5.96183 | -55.36541 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e3125c6-2579-38e7-983b-68bedcd24eaf | -17.82946 | -52.3474 | 2026-10-09 05:25:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 469b32ee-35c9-3252-96c5-e6fdf04cde27 | -5.94731 | -55.34668 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9c1cc2fa-ecf6-3d5f-bc89-61756383ef55 | -5.90346 | -53.89127 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f16c3d0-455f-311a-8079-5172567de6c3 | -7.51315 | -47.33791 | 2026-10-09 05:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce1f0618-c169-3b49-9c88-647e83f30ddd | -13.16813 | -54.35842 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ad2a714d-2315-3f00-af2c-dddbcdbc6531 | -4.29974 | -60.01713 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07ea1ae9-fe79-389a-96b3-9b3df2ca94ec | -13.15557 | -54.35232 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b225eb4-a0f6-30e4-a061-89c1500859fb | -5.95942 | -55.3666 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| db6018f8-bf3f-312c-8693-22c644b37a25 | -6.41542 | -55.19662 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00880f04-234e-3814-a84f-3ecca8ad8cf8 | -12.23378 | -57.08855 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 6dc2046d-9963-394d-901c-a448719e93da | -6.21337 | -52.88425 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d5826fc-a315-30a9-a432-373ac1465e18 | -6.44172 | -55.04761 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c99452f-45a8-3ffa-ab20-afc6abdc9084 | -6.40354 | -55.2739 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4ee84616-2a3c-3a69-b942-db9c41b617ca | -6.53121 | -55.38136 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddcf8c5d-7674-35dc-b621-7357ddb8a0b8 | -4.6937 | -56.22546 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46618a50-33fb-3e39-959e-e047791acae7 | -12.12538 | -57.16579 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c03fe517-3311-38d1-99dc-c986a6f98013 | -5.88205 | -57.72913 | 2026-10-09 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e7b869d-fa0f-399b-9d68-45c05c19696c | -5.85632 | -53.45223 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f65d9174-a21e-36b4-b130-7482e950004b | -6.11698 | -55.70153 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bda61f8d-9cbb-3c85-8616-185ac417f57b | -6.87233 | -45.91423 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1b3ab4e7-f590-314d-a9fa-07657335e68f | -13.46246 | -61.11307 | 2026-10-09 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 896c051f-31ca-3a3a-bfad-a8a09b6d66c1 | -4.74783 | -55.66044 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df535f43-b638-3472-95d3-16535860c96e | -12.22026 | -57.1306 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecbe22ec-a8fa-3158-bfc3-14852215f759 | -7.53086 | -45.87893 | 2026-10-09 05:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 97c3be46-dd2c-3d9a-8867-f70b058d6c73 | -6.83157 | -56.12036 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bf8034f-07be-386c-aec2-589d016b92b2 | -13.19757 | -54.37126 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 460d9084-3149-304f-95fb-b4a505c18cfd | -11.86074 | -57.36936 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2acafbe-90d4-36eb-b64c-25abc66d8388 | -5.96952 | -55.33925 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e5dc21d-cd22-3836-a4a1-e9e5877b4c13 | -4.1934 | -59.93819 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e61a51be-027d-3419-b5c8-9784fb4a6b0b | -6.88215 | -45.88897 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 80f3f7a3-daa0-343b-af85-b4ff810c3247 | -5.69452 | -53.45979 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df88fbae-f5d6-376d-aa83-24e9fd94f402 | -6.32036 | -54.80268 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b25b6efe-8c59-3ddd-9e0c-5825549b56db | -7.18935 | -52.63033 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f163b84-fc16-3a03-be0f-a7ca8eec8714 | -6.13009 | -53.05794 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3c2a44af-a63a-3160-b526-f44d327d9659 | -10.85227 | -59.11905 | 2026-10-09 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e8ef3fc-3b39-3565-ab1e-5608c833d463 | -5.69284 | -53.49878 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98fa41db-f8c0-31d9-b025-99be38f28d7f | -5.69037 | -53.45908 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9076cc37-087a-3638-a2e0-96368525c0b5 | -5.87307 | -53.48302 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4af877d2-06c9-375a-a996-f3b0d33035ab | -12.1978 | -57.13168 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a80410f-cf50-31c4-aea5-902065226bd5 | -11.97337 | -57.61238 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 246fe80b-1963-3f9a-8504-073badd88c63 | -6.23725 | -52.84724 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c374a11-8465-369c-8025-baccbd7a4ad0 | -11.7681 | -58.28041 | 2026-10-09 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a70d612d-fcb7-3648-9404-a155429c782f | -6.17159 | -52.8653 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b39b7d0-fc54-33ec-8a48-0391090f5105 | -12.21671 | -57.10363 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5596ac95-e548-34d6-9099-d2c951bb2cd4 | -5.2486 | -60.33265 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5a40660-e9a1-3547-84a2-4283f47c2b73 | -6.12481 | -55.70071 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 110790d9-6491-3178-bfef-e1af021810f5 | -6.45534 | -55.49452 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2aa3ede4-135e-3808-8260-e218dd8db3ef | -4.99143 | -56.94736 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e762becf-f199-39c4-b1c0-dfa76c002723 | -5.70885 | -53.48867 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f771c63-fb5e-3eb2-8e8c-88c0e0794d92 | -4.92024 | -55.85645 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5743d71-ec22-36bd-ba12-206b56925557 | -7.51382 | -47.33262 | 2026-10-09 05:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7616388d-ed2a-3d0a-880e-7df321c40c72 | -4.6902 | -56.22492 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f842ad0d-344a-3d08-a1be-24153e1640da | -4.07246 | -59.84221 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b833362-6617-3ed8-86c1-96696b48ebb9 | -5.92959 | -51.83371 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbb2398c-4c8a-33c3-b517-54fd0fd5fd06 | -6.13207 | -59.97057 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31c28f62-b9a8-3d79-8a7e-1fcde063763a | -6.30189 | -59.9725 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8fc741c-96fe-3125-bfc8-3d565d54bc5f | -5.0894 | -56.19427 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc519aba-a851-3e24-906d-a7049a10bbac | -6.32022 | -59.96465 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62e2db51-f46c-3682-8352-240c4e5c2c48 | -6.41542 | -55.19663 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d85dbd0e-e76a-33cd-8a91-b4ca2fe9c34d | -7.51315 | -47.3379 | 2026-10-09 05:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 555ac7b0-631e-31f2-bb2d-9ff84e6f7e77 | -12.1767 | -57.09454 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e5af6f7-756f-353c-8353-9d940d038f64 | -5.69094 | -53.4553 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2670a993-8c99-3a20-94f5-7ffc9e5c4ae1 | -6.35618 | -55.15496 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34654322-565d-3623-8ac0-76c53ac84c91 | -7.08795 | -52.68232 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffb53203-472a-32c9-ab6a-dbb1c294d2f9 | -6.11632 | -55.70578 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01b0f072-20f4-3dda-b2bc-54f922603706 | -5.88003 | -53.52179 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bc46b99d-dd31-3754-b6b0-4b0e143eaba9 | -6.10213 | -55.72525 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c390336a-233f-3e40-b390-66df7949f01a | -5.95772 | -55.34196 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1552a49e-fea9-3b2d-9d8d-44e720640b69 | -12.20462 | -57.08411 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ee546d4-c391-364a-8d05-41dd8e1b0386 | -6.09938 | -55.69455 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91cd1178-1262-3482-a8e6-d4fb42403993 | -13.15614 | -54.34803 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ea22071-993b-3fa3-bd04-edf1b78011cc | -6.38593 | -56.22555 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 467ab017-de10-3fe2-bddd-885ad4798f71 | -6.12545 | -55.69645 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README217.md)
