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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0e405a1-5dcf-3e6c-b4a7-6854cfde88f8 | -10.9855 | -49.7562 | 2025-09-04 12:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| e5c47a7a-1dbf-3b3e-9647-cad444d81014 | -5.7 | -45.1786 | 2025-09-04 12:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| dd176612-7402-3bc0-8747-f5b935a7e520 | -6.3689 | -45.6483 | 2025-09-04 12:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| d95e1546-f15b-366b-b3da-cca383c8098a | -10.1644 | -46.2627 | 2025-09-04 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 65ebb4ee-1e90-3758-ae63-87d3a91e12f1 | -7.7036 | -48.7587 | 2025-09-04 12:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 4c265c01-b1fc-36b6-b6fd-bc984f920cb4 | -8.0417 | -45.3882 | 2025-09-04 12:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 39fb2e4b-1a54-3936-8ea8-8709840df1a4 | -6.2318 | -42.4278 | 2025-09-04 12:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 179.1 |
| 6fde65f8-c024-3df3-9ba9-7bef1ce4e55d | -6.2127 | -42.4532 | 2025-09-04 12:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 058fdbba-172a-3c27-85a5-b8c9c14e0251 | -17.0652 | -46.449 | 2025-09-04 12:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 97.0 |
| c157844d-eb00-3ec7-8eee-ac1164dbdb9c | -6.2315 | -42.4515 | 2025-09-04 12:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 289.2 |
| 65b4d7b0-c84d-3d7f-afe4-ca8d342d78c6 | -5.6963 | -45.6076 | 2025-09-04 12:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 449.6 |
| e78487fe-94ab-3144-bca6-4ed912dc82fe | -10.4658 | -50.3907 | 2025-09-04 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 54e1806e-771d-3f89-99e2-bb9ff7371fcb | -4.9049 | -41.7696 | 2025-09-04 12:00:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| b457a2d9-f4ca-3a04-b760-98991dcdbd03 | -5.6777 | -45.6089 | 2025-09-04 12:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 315.0 |
| a3df11a8-155b-3469-aaad-6d1133ff7e32 | -10.9855 | -49.7562 | 2025-09-04 12:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| e3cbe0ae-a057-349e-84a1-43b8ca1448c9 | -5.6963 | -45.6076 | 2025-09-04 12:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 344.8 |
| 05a0c196-2df7-3cc3-beef-a94895e5acf1 | -11.7385 | -47.7637 | 2025-09-04 12:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 167.9 |
| d8de82e5-c0ec-3c90-b19c-d5dd747f806b | -11.7389 | -47.7415 | 2025-09-04 12:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 97b9b2cb-3270-323b-bb3d-dba7bbba7e55 | -7.7039 | -48.7371 | 2025-09-04 12:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 86762590-b610-3671-877d-d9d416fac141 | -17.0652 | -46.449 | 2025-09-04 12:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 0fe680d1-c277-37a5-a234-13cd4ad36d59 | -13.8651 | -47.9734 | 2025-09-04 12:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 8e7f26a5-bfd0-318f-8028-10b55347a28a | -6.2318 | -42.4278 | 2025-09-04 12:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 320.4 |
| cfdfdc25-7367-3198-a7f2-d67fda2145de | -11.853 | -51.453 | 2025-09-04 12:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| e5e7a501-a02e-38d3-983b-91f859fd7d24 | -8.9031 | -45.82 | 2025-09-04 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4bec3392-6c2f-3ea3-b67f-eeb7fecff8ad | -13.8457 | -47.9764 | 2025-09-04 12:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 13efc4bc-ebb2-37dd-bf68-1c7d2c5c8b00 | -5.8525 | -57.7722 | 2025-09-04 12:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| ea3b326a-4ab3-33b7-bbaa-099c35a84366 | -6.3689 | -45.6483 | 2025-09-04 12:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 996d3131-096f-3bb6-8959-81a24bdcd29f | -7.6849 | -48.7602 | 2025-09-04 12:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 4edf4084-9634-3881-b982-f19ad20a8be8 | -11.6231 | -46.6614 | 2025-09-04 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a7c65c4e-cda3-3171-8783-6ecb6592e026 | -7.6851 | -48.7386 | 2025-09-04 12:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 95263c2b-1811-3e72-a0fb-4a4311e0fa24 | -6.2127 | -42.4532 | 2025-09-04 12:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 159.8 |
| 27421d51-59d3-3104-8402-997b452e1dbd | -6.3692 | -45.6258 | 2025-09-04 12:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 5e4fdf88-c301-3c48-bc67-2f05018e689d | -4.9049 | -41.7696 | 2025-09-04 12:10:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 83a6746f-993b-35f8-bd1c-064932e30af1 | -7.7036 | -48.7587 | 2025-09-04 12:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 245.7 |
| 007aec70-1f75-3709-a5e5-5e45f900da71 | -8.0417 | -45.3882 | 2025-09-04 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 74a3d218-3b0a-3cd7-b8ae-689672da1aa0 | -5.7 | -45.1786 | 2025-09-04 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 4922ae84-b834-3f54-9fa4-0f4b77af63f9 | -7.7034 | -48.7803 | 2025-09-04 12:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 8bc4e96d-0bb0-3053-8060-c595dbf21437 | -6.213 | -42.4294 | 2025-09-04 12:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 129.3 |
| 696e4b0f-e1c4-34b4-bf87-84c00b9a55d8 | -6.2315 | -42.4515 | 2025-09-04 12:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 414.1 |
| 69a05248-2a7b-382d-85eb-63a2c115b4fc | -8.3641 | -48.3334 | 2025-09-04 12:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 5e870287-1210-39fa-baed-9c940ca55075 | -8.0799 | -45.339 | 2025-09-04 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 5a6f00f8-1d5c-3dc0-86f5-450623111968 | -7.6854 | -48.717 | 2025-09-04 12:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 83.5 |
| f9e2a287-bb92-3156-ae77-f7b6493998bb | -7.94576 | -44.94469 | 2025-09-04 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 8aabb348-98f6-37c8-843f-d525db5dcd3f | -6.50127 | -44.08096 | 2025-09-04 12:14:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2aa9adfd-8877-38aa-91fc-a036460a3004 | -4.95286 | -42.06923 | 2025-09-04 12:14:00 | TERRA_M-T | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 28.9 |
| b9f60b79-3596-3895-88c2-f3bbdb1a3e4d | -6.36307 | -45.63604 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| eeb80c5b-da88-3f48-b76c-910b175de0d1 | -5.82483 | -46.3586 | 2025-09-04 12:14:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2b1e2cbf-3fd0-32d5-baf2-f87c88f795bf | -6.68462 | -38.22527 | 2025-09-04 12:14:00 | TERRA_M-T | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 79fb6df5-f415-3179-8325-9ef93f54d586 | -7.69374 | -48.72648 | 2025-09-04 12:14:00 | TERRA_M-T | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 536a53ac-8a26-32d7-be0a-be65d79fe949 | -7.67541 | -46.70656 | 2025-09-04 12:14:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 671467f6-890c-3cf7-a312-8ab7c594df1b | -7.90539 | -45.2295 | 2025-09-04 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 3ba759de-3ee1-34b1-ae70-80f79d9455a9 | -6.03951 | -46.66275 | 2025-09-04 12:14:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3e521f90-312e-333f-9ada-9eb368a8201e | -7.04577 | -43.26981 | 2025-09-04 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 564cf7ec-a7ab-34b2-b0d9-ce2d429e9dca | -6.07968 | -43.28849 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2d7b0c62-74e2-32b6-8c4b-ba3645c51e92 | -6.21882 | -42.44107 | 2025-09-04 12:14:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 5694d3f3-12c7-3b49-9595-658e6b1a0a28 | -6.15675 | -43.32632 | 2025-09-04 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 34a03a6c-3624-35a2-8fc0-c46e217e0226 | -6.31 | -44.38836 | 2025-09-04 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7af3794b-5305-3c9c-a5e9-502a914196e2 | -4.31629 | -39.31667 | 2025-09-04 12:14:00 | TERRA_M-T | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 9117349d-f70e-3dcd-b54b-8d6a3b20d97b | -7.30545 | -39.63285 | 2025-09-04 12:14:00 | TERRA_M-T | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 51.1 |
| 0247b91e-e4aa-3904-aab7-3d7de11084ac | -7.30295 | -39.65291 | 2025-09-04 12:14:00 | TERRA_M-T | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 751fa671-aec0-3f04-afc5-59833268c6c1 | -6.73627 | -42.24448 | 2025-09-04 12:14:00 | TERRA_M-T | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| f85312c3-b730-373c-a7d6-23194cb25940 | -6.99939 | -46.60321 | 2025-09-04 12:14:00 | TERRA_M-T | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7480e02c-51d1-3249-9175-ba319ba3b844 | -2.65234 | -42.70259 | 2025-09-04 12:14:00 | TERRA_M-T | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5e7eda0c-7c0b-3409-89af-cdec3a5fdbd2 | -5.7001 | -45.1773 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 29e9081a-6be7-3260-aed9-5d9c644cce70 | -6.25522 | -45.16439 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 11af0eb1-a665-3891-bd68-11ef0d2476c8 | -6.22736 | -42.45427 | 2025-09-04 12:14:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 233.4 |
| 4a820ebc-c4d0-3b94-8e90-601d22a4056d | -6.92787 | -46.89756 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a602a9f8-ab7d-3b0d-934f-b945443c5258 | -8.03832 | -45.39922 | 2025-09-04 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 5d355b23-657b-34d8-9d09-da6ae70dbe3b | -6.22503 | -43.56302 | 2025-09-04 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| de72797c-1596-3d31-a841-be86b860e762 | -6.26435 | -42.41087 | 2025-09-04 12:14:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 9f009c44-ba3e-3630-9c53-f13ba04ded63 | -6.55185 | -43.90426 | 2025-09-04 12:14:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c7c3682a-97ea-3c58-b28f-284ceeb19ebe | -6.22896 | -42.4425 | 2025-09-04 12:14:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 818.8 |
| 931c49be-4d3f-35ae-943d-24dc2ee3fa7d | -6.23056 | -42.43072 | 2025-09-04 12:14:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 44.6 |
| 4ccc84ee-fa27-3d7c-be6c-8abf0cad3ab0 | -8.08432 | -45.33179 | 2025-09-04 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 41339560-4604-30b3-82f0-45f6a944463e | -6.67873 | -48.40171 | 2025-09-04 12:14:00 | TERRA_M-T | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bcca10d9-73fe-3437-8090-dd940ad7d438 | -6.37317 | -45.62844 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d774fdef-4469-39ec-8e3f-39b78a1e9753 | -6.16782 | -43.31705 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 10f072ba-00e5-39dd-8465-05881ea71d03 | -5.03516 | -45.12306 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| a242ebd0-4178-3df0-a578-165ddb4cc078 | -5.70138 | -45.1684 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e36a44b0-40a3-3b13-83d6-7e11b92b7afc | -6.2171 | -45.0495 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3dec0111-5b0b-3ca0-ae95-14d5f86e343a | -6.00474 | -44.72441 | 2025-09-04 12:14:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bc895943-e72c-32c9-bb33-e27ad3fcd221 | -6.26023 | -43.3144 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 6347c1e5-3f21-3b09-98e1-3a296861f9f0 | -3.45158 | -44.1358 | 2025-09-04 12:14:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8325ef43-0c84-38d9-9f0e-776efcba28ee | -5.98534 | -44.98962 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7977486a-0228-34b8-9709-c8fdf1617990 | -5.2505 | -44.45208 | 2025-09-04 12:14:00 | TERRA_M-T | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 82f824a8-6b46-3b88-bbc3-d06ea08f6d55 | -7.25018 | -43.85904 | 2025-09-04 12:14:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| bf1991d3-a33f-3719-a23a-1256ac828e4e | -5.68572 | -45.60589 | 2025-09-04 12:14:00 | TERRA_M-T | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 201.9 |
| b20bedaa-70ce-3406-87c4-5f14642bc905 | -6.16633 | -43.32755 | 2025-09-04 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8e1a573e-9b71-3379-8dc8-0b60badb1daf | -5.64541 | -43.12979 | 2025-09-04 12:14:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 5dbf9886-0bd6-39b4-9727-f020bc062ca7 | -6.29423 | -43.58924 | 2025-09-04 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f6aee4a4-5cd3-3078-87e7-83d5a35afd3d | -8.0907 | -45.35104 | 2025-09-04 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 638efea0-3f4b-3e6a-bbeb-e19cebcbcb47 | -6.2963 | -43.50571 | 2025-09-04 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 20c2444f-8760-3a9e-ab03-86d6690a8c58 | -6.34717 | -43.38145 | 2025-09-04 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 95b89561-2f5f-32e0-9d26-12803f7588c2 | -6.26539 | -45.15669 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 36449a0e-3023-3a41-a1d6-922c789da8a9 | -6.00345 | -44.73353 | 2025-09-04 12:14:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9b14a4b8-f17b-3791-b26b-0d664b3e9eeb | -6.35164 | -43.7676 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ba8902a2-bbbe-32d4-8291-814a2144f50a | -6.24777 | -44.83224 | 2025-09-04 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f6e7f2b5-bcee-3351-a4c3-c34f807c33cb | -7.54971 | -45.72049 | 2025-09-04 12:14:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 52950884-0a15-3c8c-b227-f99aea8a6767 | -6.37191 | -45.63728 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 87af4c08-73c7-3932-a9d2-45d1460a6477 | -6.15823 | -43.3158 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 53.6 |


[Clique aqui para ver as próximas entradas](README98.md)
