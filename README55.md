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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7996b884-704b-3eac-a822-c3bc3edb8a22 | -5.72462 | -45.39843 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16ff7563-ecb2-33c3-8621-748b5fb64bf0 | -3.63566 | -49.20996 | 2025-09-10 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2899d9ed-34f7-3f48-a43f-ee7c85856049 | -5.58368 | -42.92059 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 606fbed4-3ad1-368f-90bf-f5a8bfc088e2 | -6.2433 | -43.42328 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b90530d8-fa89-3aaf-a258-bbc6eed101bb | -6.20542 | -43.50087 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32559ec4-e98a-34a6-bcd7-4b7e205f0618 | -5.5816 | -45.0386 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| a8702c14-d580-315d-88bd-fd87ab7ef523 | -6.2043 | -43.5084 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6828c9ca-9bb0-3596-95c9-3d7e7e7b3865 | -5.92939 | -46.17501 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cefc2783-98ea-3b59-95ae-dcb1bdf5a7d6 | -6.24269 | -43.42734 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fccbe405-55c5-37bd-971e-99e08a3ad83f | -6.25314 | -43.41641 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5b0dd0d5-dbc3-3c30-a6f5-31901e51b574 | -5.58935 | -42.91257 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 10afd56d-6874-3daa-99fb-166d38f2de92 | -5.58012 | -42.92211 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 61811af2-3b64-3fea-931f-3a45224a60fe | -6.48047 | -41.75526 | 2025-09-10 04:40:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9ca2eb96-4b22-3d38-90e3-19bd1a936c1b | -6.24576 | -43.40684 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a3423f24-4c35-3509-8d4e-03bbd9847cfb | -5.40709 | -43.46135 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| de9edc9a-a75f-35bb-83ed-1d58e8419825 | -6.2587 | -43.40876 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 95241a6e-c14d-34df-86be-fd8ac025fcf2 | -5.93931 | -42.78196 | 2025-09-10 04:40:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 11ded87a-7cfb-3bbb-82a4-53f3af456a12 | -2.91502 | -48.67463 | 2025-09-10 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6e99385-f649-39c7-a690-c2e9bb1fd9e8 | -5.79591 | -43.88768 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f470bf2f-687c-3118-abf0-6e461e060134 | -2.95136 | -48.59542 | 2025-09-10 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 461e4ead-086b-3079-9503-abfa1b57f64e | -5.67605 | -45.46489 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e9fd68f-a376-314c-8cda-5ec88bb867b2 | -5.57924 | -45.04098 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 621effb2-cdd0-3676-ab17-459a6b91f7f1 | -4.86913 | -42.7615 | 2025-09-10 04:40:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c7f6473-3242-3721-ab3c-55268889fbcc | -5.74369 | -47.4641 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7dba3e7-da9e-3d23-b335-f5fca6d0ebc4 | -6.2614 | -43.40354 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e3cbdc9-f41b-3b3d-9071-84948306a0ac | -5.22542 | -43.69913 | 2025-09-10 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0f7163b9-49d7-3f30-a340-dddc74823de3 | -6.17416 | -41.05318 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c1065c10-b99d-360e-a91a-2c4945fc1042 | -5.98115 | -43.70847 | 2025-09-10 04:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea66057b-7f4b-3f03-adb8-1845e81c8e6b | -4.49742 | -47.82226 | 2025-09-10 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a66efca-d53b-3fcf-a1de-fc5532da0edb | -5.56216 | -45.17717 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6172ab55-d3a8-312b-b928-7930bd62612b | -4.86975 | -42.75729 | 2025-09-10 04:40:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0186b1ae-c194-3b08-a8dd-326ad7b74389 | -5.72253 | -45.4121 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4fa85c9-7be5-3f0d-abaa-034f3de0ab33 | -5.71877 | -45.4115 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b63a6f58-51ac-36d7-893d-cffdbd633325 | -6.0568 | -43.32202 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| be60b209-2b49-3e76-bd00-98260820d8c6 | -6.26514 | -43.40818 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1042363-94b2-3329-93f5-b28cb10ae740 | -6.21819 | -43.50327 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14f5f0fa-7940-333d-966a-3df55d00ef01 | -4.24047 | -48.26859 | 2025-09-10 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbc1b279-a8fe-3cf7-90ee-84aeb7d1af50 | -6.35281 | -44.07092 | 2025-09-10 04:40:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a944b57-039b-355b-9543-46a65b56064e | -5.68142 | -43.35373 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d105c3e7-abce-3fc7-9290-de00d48e1700 | -5.57706 | -45.04272 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f3c67265-8f76-3942-993b-3e4bd727b4d3 | -5.64135 | -43.91806 | 2025-09-10 04:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 715bb4da-4351-38cc-a805-78515e97a448 | -5.96707 | -45.8068 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c4f380d-f32c-3290-b3dd-be2d5ffb7197 | -5.94561 | -45.72335 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6c05aa6-e750-317f-ac82-eeb46f2d9b40 | -6.05116 | -43.12151 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 44d1cc82-0417-3cc2-a783-836f01904dbe | -6.16676 | -43.37445 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e917bb31-fad6-3f02-abe4-c4359ae5066d | -5.83038 | -44.09789 | 2025-09-10 04:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cee6032c-6b32-32a3-8b63-868755dd4882 | -5.74141 | -45.2888 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58e2e419-b956-3e03-9fa2-5c25d62838fe | -6.18511 | -41.04886 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2fee2840-ec56-3cd8-9d51-0d7da8342a5a | -2.38524 | -47.71901 | 2025-09-10 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea35f7d1-7223-3b90-a042-a0fe8b36f4b5 | -6.2006 | -43.50387 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 494a994c-eebd-33dc-9f7e-53c10608aadd | -5.93739 | -45.95232 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67096601-61b8-360c-bfa5-e02f6c2ed851 | -5.72453 | -45.60705 | 2025-09-10 04:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc425a50-6816-3ad7-ba4a-2def41249e82 | -5.42162 | -42.80762 | 2025-09-10 04:40:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f0ce9af6-bbe3-3b0f-acaa-1480c7270350 | -5.66938 | -43.8996 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aab66fc-cf5f-3a96-b9ac-a0d9320509da | -5.72538 | -43.89287 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0ed13f1-40f6-38d6-93e5-e7d260b647a7 | -6.33943 | -43.54564 | 2025-09-10 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8596f9ed-7f74-3b32-858b-f1245766c16f | -6.0878 | -43.36289 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3e7c1a8-e01c-38dc-ad33-31b36c90612d | -5.52588 | -46.50007 | 2025-09-10 04:40:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a16875e-4e03-310c-8955-b803936490b7 | -4.42147 | -47.95543 | 2025-09-10 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 883cbe4e-1e25-3a1e-a5aa-84d9a780eb72 | -5.39352 | -43.44048 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62ef8047-15c5-3e06-84ee-caabba0a871c | -4.48624 | -42.92564 | 2025-09-10 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd886bd4-8b01-39b6-b2e0-423843adfd32 | -5.42073 | -43.42745 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bf19a76-a4d4-3c80-ab34-39ca916b2933 | -5.57572 | -42.92137 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| efb2a874-4355-34e0-86e1-fa5fffed110f | -4.36308 | -54.75848 | 2025-09-10 04:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 468eb69d-a58d-3718-a350-f8115545ca9a | -6.39782 | -43.50499 | 2025-09-10 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee63be8b-4f7e-3b2d-8f89-0d7a518130a1 | -5.73072 | -45.28255 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d31c2afc-e134-3912-ac44-a81104f563ea | -6.31752 | -43.41171 | 2025-09-10 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 724643f8-dfef-3887-a44a-80be187849d1 | -5.80632 | -45.29175 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d12196d-f27b-3d4a-8e46-3c045f6ca598 | -6.17101 | -41.04906 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 91ce8060-563a-3f07-92cb-8aabb079b18a | -6.05747 | -43.13937 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9798e6a0-cab6-3412-bdd7-f5b3e5b72b51 | -5.68202 | -43.3497 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b00e0626-714b-3175-9160-6ebffb039036 | -4.88188 | -44.96018 | 2025-09-10 04:40:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff4f7ef9-ff6d-3b6f-9305-7c7e520d34f4 | -5.63942 | -42.62844 | 2025-09-10 04:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5a758978-d996-3374-aea8-abbf9dea33a8 | -6.21173 | -43.36864 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2006dd95-564f-3a49-b54d-60166380d730 | -5.22773 | -43.68388 | 2025-09-10 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26e15294-c976-3426-b0f1-d625c08c73a6 | -5.79393 | -45.42529 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2944c19-9c54-3b21-9622-6b558d84eae1 | -5.46389 | -43.4296 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| cb283268-b9da-383f-925a-d45dc455dae2 | -5.9158 | -45.82125 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7710210-50e1-3afb-9102-c15c2dfb6ffc | -6.29138 | -44.22997 | 2025-09-10 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd52a6aa-7427-35e6-8a78-247c7c661607 | -5.77078 | -45.5278 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 375f4b6e-10c4-302c-85eb-7724b1187950 | -5.57845 | -45.03331 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17c42a5b-38e1-31a4-9463-b9b616d9db5f | -5.44529 | -43.467 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fcffd625-6d67-35d4-a6b8-fb38305a59de | -5.42096 | -43.45548 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ea597806-bd33-3522-9712-f77ab976ae70 | -4.80225 | -48.57016 | 2025-09-10 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad8411d3-35d6-3013-a68e-9fa058ba7101 | -5.961 | -45.797 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce9b43ad-458c-327d-89df-240bd307c5be | -5.66993 | -43.89586 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76183992-e046-38b6-8c70-10c716a06d9f | -5.20316 | -45.43176 | 2025-09-10 04:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcf67f1a-4e96-3c37-8ced-77bcb3e48086 | -4.72966 | -44.45913 | 2025-09-10 04:40:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f4e91ce-e519-3b9a-a47b-d404a933e7a6 | -5.12077 | -44.67247 | 2025-09-10 04:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5da747d-9510-3f63-9102-46fb94e17eb5 | -5.98593 | -43.70528 | 2025-09-10 04:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ef7b661-b003-3a94-9846-99638c8d198c | -5.30023 | -43.11598 | 2025-09-10 04:40:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9840c74-98b7-39c5-9254-c2c41f23f1fa | -4.97417 | -48.93852 | 2025-09-10 04:40:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63a71983-e24c-3b90-b0ab-9ac94df12ea8 | -6.16586 | -45.81974 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0e1062e-1839-3616-aebd-350dd392c24e | -5.58382 | -45.0368 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 4acf35de-d044-3ce5-bcfc-2017a3946a4b | -6.25708 | -43.40293 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ac89edf-3eb7-3ae9-b7d2-b3a56afc5ca3 | -5.46448 | -43.42569 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e7981a1b-08f3-3c11-81d3-e8ea8003bb78 | -5.37571 | -45.94805 | 2025-09-10 04:40:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55d2258b-3d42-3258-aa60-86be28e3eaad | -5.74712 | -47.46461 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1a6c509-e864-3915-aa40-17d9e3e7010e | -6.05369 | -43.13468 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bad26f30-9d58-3059-80e8-6db7c1b7bd4f | -5.74196 | -47.47516 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README56.md)
