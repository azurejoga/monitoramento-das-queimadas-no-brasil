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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7c6930c-53fa-3ab3-b0b9-4098c78d22f1 | -8.7766 | -69.53162 | 2026-09-30 01:17:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9036d6f7-62c1-3e6e-abb2-1c63e64d7cc2 | -9.71992 | -67.08526 | 2026-09-30 01:17:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2d640b74-8949-3ea5-8040-e67e81e474b8 | -9.09481 | -67.7561 | 2026-09-30 01:17:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 432ae633-1d93-3e7e-8817-bc77eb5cea0c | -9.16765 | -60.79443 | 2026-09-30 01:17:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 32ddc326-a281-3ed9-809d-17fdae8cea42 | -9.08595 | -67.75739 | 2026-09-30 01:17:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 6cbd49ad-ee73-3f06-a41e-f765c07d5ec3 | -7.42739 | -64.32828 | 2026-09-30 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 9b74e521-4c37-3a6b-a46e-047465e19ace | -9.10606 | -67.83696 | 2026-09-30 01:17:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e425301b-bb9c-3ee9-9f13-cc4b31e15623 | -7.42944 | -64.34231 | 2026-09-30 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 2662c28a-a826-302d-8f3b-7a5b4e15a468 | -7.72527 | -72.46452 | 2026-09-30 01:17:00 | TERRA_M-M | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 14.3 |
| d9025183-2e6b-39f7-9918-117fe20012e4 | -7.43147 | -64.35629 | 2026-09-30 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a00b31d2-d7b7-36f3-a941-df2c086fcac2 | -7.43124 | -64.33638 | 2026-09-30 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 110.6 |
| d7d712ee-3ef7-385a-9eb6-64879d5af63c | -10.84748 | -60.76767 | 2026-09-30 01:17:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| dbb40053-88dc-3982-9259-e5e34330e4fb | -7.72691 | -72.47694 | 2026-09-30 01:17:00 | TERRA_M-M | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 39.2 |
| b089d439-1728-3492-8b59-54ea2007f872 | -8.77783 | -69.54074 | 2026-09-30 01:17:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 04e66a75-e939-3573-a3d2-6dc5ce4e649b | -9.0872 | -67.76638 | 2026-09-30 01:17:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d1f75ee0-a38f-3932-a7f1-233f3ac4e59f | -9.16334 | -60.80182 | 2026-09-30 01:17:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 050b40bf-11af-3da9-a263-3dc68ac9fef2 | -19.8858 | -49.6022 | 2026-09-30 01:20:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 140.1 |
| db14aa87-d3de-33e9-b9f3-79cc4d1ecfeb | -19.9061 | -49.598 | 2026-09-30 01:20:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.9 |
| 69743c8e-8f21-324f-bcbe-bfca2e241cf5 | -11.6395 | -43.5455 | 2026-09-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 6e3032b6-5f1b-31bb-ab1d-2f56d65a78d1 | -2.9924 | -51.045 | 2026-09-30 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 9f72122a-d04f-32d9-a2d4-a4acf4f0af4a | -19.9067 | -49.5752 | 2026-09-30 01:20:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 154.1 |
| c13a731c-5aab-309d-bf5d-960d592536bc | -2.9925 | -51.0242 | 2026-09-30 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 10b2000c-f54f-3b0e-a269-bf2467d669a9 | -2.9739 | -51.0663 | 2026-09-30 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| befeeb9f-a05f-36a0-bfd5-f7ffd997d3d7 | -7.8486 | -45.8138 | 2026-09-30 01:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 453f29a2-c81e-30a9-987c-45ed3f022d7b | -9.9407 | -50.1449 | 2026-09-30 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 2b7aadcc-c35b-3987-9c48-fada43db9290 | -7.8483 | -45.8363 | 2026-09-30 01:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 1ef34dc7-6a9a-3c9a-b92c-d7d11ce407fc | -11.8488 | -50.4526 | 2026-09-30 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| c11fa68b-7c4b-37bd-8b24-58d856151dea | -7.8297 | -45.8156 | 2026-09-30 01:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 12f40450-e8d6-3a1b-af40-9c33c2ab4466 | -15.6256 | -43.2199 | 2026-09-30 01:20:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 89317c7e-5137-3a97-bab1-b037d0e69bf3 | -12.3085 | -47.9539 | 2026-09-30 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 3a768085-adc8-345f-8f40-9cc29b2767b8 | -11.83 | -50.4333 | 2026-09-30 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 6cd2d568-66d2-3d1a-a808-0a79f65685f3 | -5.1621 | -55.9931 | 2026-09-30 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 66f502c7-2fda-30fb-aea5-7ec3474ec0a4 | -3.2314 | -46.9376 | 2026-09-30 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 221.9 |
| 8d71d11f-7d41-3de2-85c3-ff03dc2f1076 | -11.64 | -43.5218 | 2026-09-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 193.3 |
| 9035a793-e1f7-339b-980d-f50b2e0cf5ff | -2.9082 | -54.0907 | 2026-09-30 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 3302fdf3-e25f-3d7e-849c-c4a264a56d26 | -6.895 | -43.7066 | 2026-09-30 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 27a97874-c521-3e3b-9d2b-3dc203dc62de | -7.8109 | -45.8173 | 2026-09-30 01:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 6343394c-b434-3923-9f17-acfa03f89c88 | -11.8297 | -50.4548 | 2026-09-30 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| bd6f83b4-f789-38c7-9884-90e94a88dfee | -2.974 | -51.0247 | 2026-09-30 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| cf8fee95-d6bc-3c56-b804-632499cf92f3 | -10.0779 | -63.0804 | 2026-09-30 01:20:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| b5c78cc7-07c8-3fa5-8983-eb4c47fdde47 | -4.4507 | -47.9112 | 2026-09-30 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b5a43e8c-9e72-3548-886e-3a22caffa8a3 | -5.7561 | -45.1747 | 2026-09-30 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 10482f48-6d4f-3826-8e52-d9679f0f1285 | -11.8491 | -50.4311 | 2026-09-30 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| c77ca010-615f-381a-981a-8de6fca99b5f | -15.625 | -43.2442 | 2026-09-30 01:20:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 87.6 |
| b4a383e4-9107-34e1-a711-91031dfa9786 | -3.2313 | -46.9596 | 2026-09-30 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b69962a3-894c-3c8a-9b3f-6ef5ab57c8ce | -13.3267 | -43.9523 | 2026-09-30 01:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 7c0f821d-fe7b-3734-a6c2-3c068b54eb68 | -9.1626 | -60.7948 | 2026-09-30 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| a837aa91-5fc1-3653-a172-aeb489552f93 | -11.699 | -43.4416 | 2026-09-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 84dab81c-89f6-362b-9138-a54a8b4075c2 | -11.4307 | -43.4358 | 2026-09-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 632e148b-444f-3595-892d-87e3b434b9a3 | -7.8107 | -45.8399 | 2026-09-30 01:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 0a55479f-6af4-3707-bd34-2fbe0934101b | -11.6207 | -43.5248 | 2026-09-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 302989f2-2c50-3784-8a2f-22934753f07a | -3.2129 | -46.9383 | 2026-09-30 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 4b0a0f36-30cb-3243-ad90-8612711c9b0c | -2.9739 | -51.0455 | 2026-09-30 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 8ae2837f-0526-3cd4-9e8a-ac615b093cef | -7.8295 | -45.8381 | 2026-09-30 01:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| ecba99d5-295f-3b29-879e-a8d917c10000 | -13.3262 | -43.976 | 2026-09-30 01:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 95d40d8f-27d2-312f-87e2-ab37fa519721 | -11.7182 | -43.4386 | 2026-09-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 91e38c17-4060-3638-94ac-5b2c58952f28 | -18.2827 | -53.0496 | 2026-09-30 01:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 1895bf34-4105-345e-8cf1-fc0ec64d93ac | -3.3801 | -50.95 | 2026-09-30 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| c3ee81c2-6693-33c8-9532-b3ffc0cac2fa | -4.4506 | -47.9329 | 2026-09-30 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c2ba2936-bf8b-39c7-bc12-4628746d94dc | -11.1775 | -44.7832 | 2026-09-30 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| a897e397-83d8-36cc-9a73-dfd87fc1299b | -11.9548 | -50.9957 | 2026-09-30 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b2ca924d-035b-3ef8-a8e1-eefdbff9403a | -3.2315 | -46.9156 | 2026-09-30 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| cf537956-2ce6-3d7a-8cd6-f9abcc8d93f6 | -19.8864 | -49.5795 | 2026-09-30 01:20:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 268.7 |
| 347904c2-c6f6-3365-a446-53206532145d | -18.2831 | -53.028 | 2026-09-30 01:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| c047f4e9-fba9-354e-8984-b29f8be99afb | -11.1779 | -44.76 | 2026-09-30 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 196e4536-5bab-36e1-b31d-c782d1e65979 | -18.2831 | -53.028 | 2026-09-30 01:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 930ecdb2-ed37-3513-9725-f2c65696e101 | -12.2706 | -50.2735 | 2026-09-30 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 14b09d73-20fc-3ed4-a3f2-7e5fa08cce4d | -15.6256 | -43.2199 | 2026-09-30 01:30:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 76.2 |
| b86f3a93-9192-3384-9771-08dfdfb589ec | -11.8488 | -50.4526 | 2026-09-30 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| a8e5a491-f64c-3651-80fb-1d5d6caca2d4 | -3.3801 | -50.95 | 2026-09-30 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 98a9ff2c-af65-37ad-9c3e-84d17732b721 | -19.8869 | -49.5567 | 2026-09-30 01:30:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.3 |
| fb7105cf-9549-3fd9-87b1-1d39595794fd | -7.8109 | -45.8173 | 2026-09-30 01:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| e7565a2f-8ae2-3db2-a79e-71819cd34db0 | -7.8483 | -45.8363 | 2026-09-30 01:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| b52e08d9-b875-3468-89fa-6b160d096a6c | -2.9082 | -54.0907 | 2026-09-30 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| e4cb6bc4-d075-3bb9-971c-6085704ff26b | -7.8295 | -45.8381 | 2026-09-30 01:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 6fb1c379-2866-3c97-86ab-27ed6f0b80f6 | -11.7182 | -43.4386 | 2026-09-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 6a0bc829-dba3-3f31-834a-68fd721d7e52 | -19.8858 | -49.6022 | 2026-09-30 01:30:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| 6a22bbd5-49ed-3eb7-9a17-13fb8880b21a | -5.0215 | -43.5754 | 2026-09-30 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| b7122485-610f-318c-8d3e-570f0f129745 | -15.625 | -43.2442 | 2026-09-30 01:30:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 2d8ed24f-aaa6-3bd3-bcc7-62993a362f72 | -12.3277 | -47.9513 | 2026-09-30 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 4bc74002-c8b3-3b5c-b216-3d19953ae803 | -12.3085 | -47.9539 | 2026-09-30 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 157.1 |
| aa68c483-b8c9-3238-80dc-afc721034729 | -3.2314 | -46.9376 | 2026-09-30 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 210.4 |
| 7a98ec0f-6698-3ac8-8a28-1b4243c91631 | -19.9073 | -49.5525 | 2026-09-30 01:30:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.0 |
| 9c5da099-00fc-3855-a58d-ef3164e4dcff | -3.2313 | -46.9596 | 2026-09-30 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a56c763d-a2b3-394d-ba60-4f99029bd1fd | -19.9067 | -49.5752 | 2026-09-30 01:30:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 147.8 |
| a685d0d6-2ad1-3a2e-9b22-dc0707c25054 | -11.1775 | -44.7832 | 2026-09-30 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| def231f9-7c12-3d91-8ff3-15f72288ec62 | -5.1806 | -55.9925 | 2026-09-30 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b0d16296-ad8b-37f0-91f0-1b14c451f28c | -11.83 | -50.4333 | 2026-09-30 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 083c9930-1e8b-310d-8d29-ffac2b454e57 | -4.4507 | -47.9112 | 2026-09-30 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8d83a9f1-d4c6-344a-b594-d73951b62cf2 | -18.2827 | -53.0496 | 2026-09-30 01:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| ce182c21-ae8b-3607-8a2e-652275f80243 | -7.8486 | -45.8138 | 2026-09-30 01:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 2daa5c69-42a2-3b6d-9628-cde5dde74998 | -10.0779 | -63.0804 | 2026-09-30 01:30:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 3a246a33-6d86-37af-a4ec-2d7d409145d1 | -21.3977 | -45.3069 | 2026-09-30 01:30:00 | GOES-19 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.4 |
| ae16b0db-92d7-3193-9b7c-d9125a9e42c3 | -2.9739 | -51.0455 | 2026-09-30 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| a9f479ff-9a7e-30d0-bb83-01e3e97d953b | -2.9924 | -51.045 | 2026-09-30 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 388eb818-e5b8-32dd-be9a-45dfae6a4140 | -22.0892 | -46.9756 | 2026-09-30 01:30:00 | GOES-19 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 98.1 |
| e779837f-1497-3655-be40-be5486267dbb | -6.9138 | -43.7049 | 2026-09-30 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 8083e1d6-88c1-3012-9edf-7069b3defdfe | -11.699 | -43.4416 | 2026-09-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| a9584a53-2002-37d6-b8df-7f724ee4c6e6 | -3.2129 | -46.9383 | 2026-09-30 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 282c8374-3310-3ecf-a7b3-69298f46364b | -6.895 | -43.7066 | 2026-09-30 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |


[Clique aqui para ver as próximas entradas](README6.md)
