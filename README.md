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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b99665d-69bc-3a19-bbd5-f247b6ef3c8a | -6.22814 | -43.37612 | 2025-04-28 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 698b07f6-e33d-3239-90ae-2d0021e7d066 | -6.2391 | -43.38531 | 2025-04-28 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a6455e1b-f7d0-3826-b4c4-02883de2aee8 | -11.97158 | -44.15989 | 2025-04-28 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 578490d2-1e46-3b4c-bd32-0ca05afe061b | -6.23769 | -43.37481 | 2025-04-28 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 84def688-c243-3788-b1cc-d6022f50edf9 | -10.96223 | -40.88142 | 2025-04-28 00:11:00 | TERRA_M-M | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f96b29ea-0c6d-3a0d-8a6c-359962d9a42c | -6.2387 | -43.369598 | 2025-04-28 00:24:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 633fc6a2-8110-3bb7-8db6-c9ce21eb8df9 | -11.9741 | -44.151299 | 2025-04-28 00:24:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84ab1fc7-1c4f-3f5d-be4b-923572d00ec5 | -6.229 | -43.371899 | 2025-04-28 00:24:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f872b65-2519-3af3-90b3-9ec770698c73 | -6.2258 | -43.3587 | 2025-04-28 00:24:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 821465cb-d8e5-38b3-8416-4d912bb02c5e | -11.9717 | -44.141602 | 2025-04-28 00:24:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e72657ff-6537-30ff-8828-ae5299fed96c | 3.7619 | -61.282398 | 2025-04-28 01:14:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| df9ddcdb-0236-30ad-9dc4-41ee2e6c2ba8 | -9.81457 | -38.17569 | 2025-04-28 03:04:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dfd1ba1a-6d06-349c-b6a2-d4014d05e0b0 | -19.4584 | -40.86179 | 2025-04-28 03:08:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 12072b6a-9654-335b-a827-ec39af840ce2 | -19.45773 | -40.85937 | 2025-04-28 03:08:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5c01e551-2b5e-33db-9dcb-5d65180bbc26 | -19.46403 | -40.86011 | 2025-04-28 03:08:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fa050b03-ddd0-3641-893e-9c24ee66073a | -19.46307 | -40.86425 | 2025-04-28 03:08:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 58a4f07b-d39d-37c7-929b-15d17eba0a1f | -6.22977 | -43.37598 | 2025-04-28 03:30:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 93b54f8d-2c0c-39fc-9a64-a8255350bd9f | -6.23378 | -43.38185 | 2025-04-28 03:30:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2bc9fecd-28ce-3a66-85a1-fa11d3930c1f | -6.23992 | -43.38309 | 2025-04-28 03:30:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bd3373d-72e7-3296-be95-465735909912 | -6.22942 | -43.37101 | 2025-04-28 03:30:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d8023fbe-9ee9-3cce-9c9c-868ae1354e29 | -6.22852 | -43.37584 | 2025-04-28 03:30:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1a81b599-370a-3d63-b4a5-b1eab1b6bbcd | -6.23506 | -43.38201 | 2025-04-28 03:30:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d013e619-b21f-348d-894a-0390e2206b49 | -6.23063 | -43.37115 | 2025-04-28 03:30:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 197fd09d-1023-3fa9-8bae-425d71f3cc4d | -6.23468 | -43.37698 | 2025-04-28 03:30:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3e0175b1-aef6-3b34-a98c-0c04f980dfdf | -8.60905 | -36.6417 | 2025-04-28 03:30:00 | NPP-375D | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 61f9a1f4-6685-3d8a-8388-5d1bddd63753 | -10.91288 | -37.14002 | 2025-04-28 03:32:00 | NPP-375D | NOSSA SENHORA DO SOCORRO | SERGIPE | Brasil | 2804805 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 53c583e7-df0e-32df-bd91-c1124bab361b | -10.9629 | -40.88249 | 2025-04-28 03:32:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f035bbdb-ee4b-3f83-895e-a413b6be4752 | -9.81536 | -38.17242 | 2025-04-28 03:32:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c6f06be7-c85d-3739-8e6a-619a286f7b04 | -19.46215 | -40.8616 | 2025-04-28 03:34:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 88f6c6cd-8dbb-35bb-933f-6ce1edf17c63 | -19.45975 | -40.85662 | 2025-04-28 03:34:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a3e6331d-fc32-35e7-a407-6143309672a0 | -19.45795 | -40.861 | 2025-04-28 03:34:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 5c470fed-39ad-3d6b-9029-593d85e2e392 | -19.45904 | -40.86029 | 2025-04-28 03:34:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 44c6097a-382d-3f7b-b61c-7a325be07388 | -19.46253 | -40.86457 | 2025-04-28 03:34:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3988b697-ccc1-3435-884e-ee96813292f8 | -19.46324 | -40.86094 | 2025-04-28 03:34:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9e8c23fa-591a-30df-8807-3041d77722c0 | -18.04032 | -39.92654 | 2025-04-28 03:34:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 161eaae3-7390-315b-9676-387598e7eb7f | -19.45833 | -40.86396 | 2025-04-28 03:34:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 10a126f7-dc92-3974-b5b3-37c01dbb34eb | -19.46283 | -40.85798 | 2025-04-28 03:34:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e901d9ab-89d0-3d19-a77c-6dadb372ef28 | -6.23704 | -43.37842 | 2025-04-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2da349c3-75a7-3efa-a0ef-6ad1bb5f38fa | -6.23642 | -43.38208 | 2025-04-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11516c97-7562-3495-9e2d-33b95b845faf | -8.61002 | -36.6409 | 2025-04-28 03:51:00 | NOAA-20 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f15f436c-e3ad-3d10-8922-b563904c5138 | -6.22549 | -43.37277 | 2025-04-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0dd7e743-7143-316c-8ec7-7bb41d3003f2 | -7.17825 | -44.87215 | 2025-04-28 03:51:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2efc0ac7-d65d-3c25-b38f-18bbf713d0a2 | -5.79537 | -43.62424 | 2025-04-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99eacc68-a315-373b-a6db-21ff3e55dd6f | -8.07283 | -34.97612 | 2025-04-28 03:51:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e98cdabc-428b-303f-a088-276a5a7ce96b | -7.04559 | -36.73056 | 2025-04-28 03:51:00 | NOAA-20 | ASSUNÇÃO | PARAÍBA | Brasil | 2501351 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1396823a-84dc-33b9-8420-a3f93d404f64 | -6.27972 | -45.27171 | 2025-04-28 03:51:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45f2f44d-eb37-386f-bf22-321f1cc85cfc | -6.23298 | -43.37776 | 2025-04-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0373c44-4e0c-34f7-939d-7ff871b8e83d | -7.52616 | -39.95674 | 2025-04-28 03:51:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6cc8c51b-a30c-307f-9c41-1da2ba2bb212 | -7.14139 | -40.93332 | 2025-04-28 03:51:00 | NOAA-20 | VILA NOVA DO PIAUÍ | PIAUÍ | Brasil | 2211605 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 898d8a59-c7c5-3c9f-b1ec-d9b2b0ddb2e5 | -5.87722 | -43.93817 | 2025-04-28 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9051f499-f7b1-3502-949b-f851a99aab74 | -7.1775 | -44.87647 | 2025-04-28 03:51:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07091220-6a9a-3a8a-8cea-1ea7db19c9f7 | -6.22892 | -43.37708 | 2025-04-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| bba9dbfc-adb2-363c-a9bf-adabead666d0 | -6.22954 | -43.37347 | 2025-04-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 514b34c5-baf3-3f28-a10a-a677fa97ec90 | -10.62596 | -40.51329 | 2025-04-28 03:53:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e12a7b59-41ed-30ac-9163-c6ea9bf6c580 | -10.62654 | -40.5097 | 2025-04-28 03:53:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8759ef75-a4cb-3a40-810d-fdcfec97f55f | -9.8147 | -38.17321 | 2025-04-28 03:53:00 | NOAA-20 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f7f23ee0-b2f9-31ed-be26-43a5b774e3bf | -12.07329 | -45.65659 | 2025-04-28 03:53:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d3dfe6e-62fa-3c75-9042-da745d44478e | -10.91106 | -37.13799 | 2025-04-28 03:53:00 | NOAA-20 | NOSSA SENHORA DO SOCORRO | SERGIPE | Brasil | 2804805 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6d86c110-5b0c-39fc-a6fb-bc59afb659d1 | -12.17635 | -44.34471 | 2025-04-28 03:53:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 745767e5-a02b-39de-811e-0aa6689b919b | -11.96739 | -44.15791 | 2025-04-28 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 14523735-6cec-3e19-b3db-bd2470e28e9a | -12.2784 | -41.92401 | 2025-04-28 03:53:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 41cb8526-9d24-391c-91cd-4f99d3e052ee | -10.69381 | -37.04698 | 2025-04-28 03:53:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b493b823-413f-315b-9c33-df6ae3943a77 | -9.34499 | -40.64262 | 2025-04-28 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a22bd1aa-f3f0-311c-8536-6c5fb65e380a | -9.34559 | -40.63894 | 2025-04-28 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 24776139-2185-334e-9688-ee16d403e7ff | -19.45987 | -40.85975 | 2025-04-28 03:55:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 558900be-59c2-3094-9bcb-ef96c97bbccf | -19.46286 | -40.85955 | 2025-04-28 03:55:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 36ceddca-331a-3ef7-a115-a43ec34c67ca | -20.41766 | -43.55352 | 2025-04-28 03:55:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b2fdbb61-c013-3b09-a2cb-914063d4bcbc | -16.34724 | -43.69426 | 2025-04-28 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebefa515-c5fd-3c9e-ba16-8e8cfc3cd765 | -19.46044 | -40.85606 | 2025-04-28 03:55:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5100b3ed-1025-3782-9192-5a40002b6226 | -19.46229 | -40.86325 | 2025-04-28 03:55:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| eed20230-709c-3203-a31e-12c42ed3760f | -21.17751 | -43.98048 | 2025-04-28 03:55:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 93a99d64-1b56-3b33-841a-44fdfdfd853f | -21.91099 | -42.26171 | 2025-04-28 03:55:00 | NOAA-20 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c938bca3-c153-32fa-8c22-ca043e63e0d9 | -19.45929 | -40.86343 | 2025-04-28 03:55:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c2626f47-730e-31b4-857b-6bc864684dd5 | -23.01836 | -45.50883 | 2025-04-28 03:57:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f2d7cda2-1e4b-3dd0-ba34-dd9b75f31833 | -23.01477 | -45.5081 | 2025-04-28 03:57:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 56713c37-f9af-354f-85aa-8ed37313ffdf | -6.28169 | -45.27006 | 2025-04-28 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cee01775-8a8f-3eab-b155-36fc3cf824f0 | -6.23231 | -43.37714 | 2025-04-28 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9bbe5de7-2630-36c2-bdf6-ec3c6ec0a4a9 | -7.18094 | -44.87664 | 2025-04-28 04:44:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bfe476b-0c2a-3d06-8c1e-784c84127aac | -5.87948 | -43.94124 | 2025-04-28 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 25d82a3b-14ac-3362-b145-755749a863ae | -6.22827 | -43.37135 | 2025-04-28 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 23969dcc-55b0-3dc5-9265-57ed1fe8b927 | -6.23635 | -43.38291 | 2025-04-28 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 27728545-ac39-3858-9749-fdab3d0e765c | -6.22755 | -43.37644 | 2025-04-28 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 710c1a38-6f3e-32a6-8f73-367014aacd6c | -6.23305 | -43.37199 | 2025-04-28 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c87336e5-2169-38ce-9503-7989c8eeb416 | -6.23707 | -43.37788 | 2025-04-28 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3c5b1481-ed31-3a78-829d-0b66f30fc177 | -11.97089 | -44.15908 | 2025-04-28 04:46:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f26b3103-aea2-3e62-a6cd-de254e7f6836 | -12.17707 | -44.34425 | 2025-04-28 04:46:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ba90d7c-6feb-3f3e-9627-41967c9a081a | -11.96861 | -44.1587 | 2025-04-28 04:46:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5dea98f-7606-3c35-a6b8-54d85f59a64d | -11.40745 | -52.94923 | 2025-04-28 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c005184-e6e2-383b-a5eb-ff7e58670b9b | -11.40412 | -52.94868 | 2025-04-28 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dd6c370-c4a1-3588-9586-5e8a16c21e1c | -12.07587 | -45.65679 | 2025-04-28 04:46:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c897b635-e4cf-31ce-bbe0-01ba42efb133 | -20.47996 | -53.67455 | 2025-04-28 04:49:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c166cd48-99fe-38b8-ae5b-5214d262a5e1 | -6.23799 | -43.37637 | 2025-04-28 05:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1bf13411-04c6-3d00-a395-17cb513898a3 | -6.22955 | -43.37025 | 2025-04-28 05:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6cf96dfd-495c-3b71-970f-e30c02fd14dd | -5.87889 | -43.93595 | 2025-04-28 05:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 919ead03-f980-396b-94e0-3ebe90feb0bf | -5.87806 | -43.94216 | 2025-04-28 05:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f837879-b091-3ff4-8ca6-b0338f3aa244 | -5.88072 | -43.94049 | 2025-04-28 05:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6a293b8-3de9-323f-b2e5-90111f2920f8 | -6.22859 | -43.37736 | 2025-04-28 05:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3ca52f65-1d2f-3a93-9c99-f41180c57175 | -6.23074 | -43.37536 | 2025-04-28 05:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 205ffbf6-5c3b-3840-9ab3-e046be1a4303 | -6.23583 | -43.37843 | 2025-04-28 05:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8c75ce42-31c3-3a6c-a750-1a6d4b489684 | -6.23168 | -43.36811 | 2025-04-28 05:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |


[Clique aqui para ver as próximas entradas](README2.md)
