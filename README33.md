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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc69d5b6-85b6-33ee-b7aa-2a2c8d567bf8 | -8.36182 | -48.30583 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de8e199b-248c-3812-948f-a5ea99387288 | -6.09485 | -43.29055 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 60cb2af0-b8eb-34db-a4b5-b4db3f8bbb80 | -8.38357 | -48.28799 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8018378c-2629-3e6d-b473-dd5d45680450 | -6.27253 | -44.51174 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb6c9d87-c571-3d0e-a1b5-3c717a4b261e | -7.9645 | -46.50695 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9169ec7d-b1f4-33cc-9c4f-ca8fe4ce8d30 | -7.89787 | -46.46112 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57f5e610-a3b1-3a77-8266-5d3a60565eb6 | -8.0093 | -44.78625 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4878a3b-e5fc-39dc-a5ed-97569a8a3bd0 | -6.72537 | -42.265 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8eaef23b-21a1-37dc-9cfc-e5ddef97374d | -8.88531 | -45.83126 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 39358e01-5819-30a3-be6b-b4f7b9d340e3 | -6.33986 | -45.66047 | 2025-09-03 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7eedcf6-b86c-357f-90f4-d4631a2c9154 | -5.80992 | -43.22775 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 642e57a0-de23-398a-89e9-bc8cf18355b2 | -8.87548 | -45.83383 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 258af90a-8426-3ddb-800d-e959f23fc406 | -6.9534 | -43.27359 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c7890ee4-6737-346d-8f5c-1b1570d7946c | -6.72677 | -42.24847 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8f3f547d-de89-3979-b8db-9d865edec4f4 | -8.87201 | -45.74805 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ccfc33a-9ffb-3456-82b1-fff7344502b9 | -5.80014 | -43.23677 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f79b1547-4d6d-3fb8-a848-39e3c78c9987 | -9.18794 | -45.18995 | 2025-09-03 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5c403df-3851-31d1-b79a-e745b2e25041 | -8.83857 | -45.77308 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f675c91-97b8-3aec-a3c2-2b2aad52d1f5 | -6.79632 | -44.0854 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 514b19e1-95f1-3ee6-aaf6-4c02274f6f6d | -7.71587 | -50.25433 | 2025-09-03 03:53:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd05be7b-5025-391b-bc04-6fff9f642de8 | -8.07632 | -47.61295 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2160f17-3051-3d31-9357-4f83b2c65503 | -7.48119 | -44.83669 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c59499ee-a633-3cba-96e6-140d3db4ee56 | -5.77756 | -45.28328 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7d3cbd0-69b6-3a91-8328-e572775a121d | -8.97775 | -44.45811 | 2025-09-03 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aef6f7bc-39ca-3871-ad02-d4463e9801a5 | -5.78174 | -46.46132 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cae4f1f-aa72-36fc-b661-b624f597b965 | -7.48894 | -44.82339 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b31b3f95-a6bb-3abe-b263-4967cd1e1970 | -6.23156 | -43.40022 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d496dfe-3dda-3699-8b4f-6d8b1c71c257 | -7.62606 | -46.54709 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65aae5e6-18d0-323c-9bdf-b67684d78d54 | -5.78674 | -46.46212 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e144cf7f-e474-3f0b-80b4-703d4fd150ad | -8.08487 | -45.50312 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8d732381-6d32-362a-92f6-e02ad9fc897a | -6.27091 | -43.51302 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9425ff53-498e-3652-805c-55f0b52c5bb8 | -6.26648 | -43.291 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f5853fb-c01a-35e1-902b-92bbb17755e3 | -7.12995 | -44.57067 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6bbec3f9-8026-368e-83be-7ab10aa2961d | -6.12201 | -43.28461 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ed237b1-14b1-36af-8d94-7dda4d6ab2d3 | -6.93063 | -45.55773 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70b4dfa2-908d-3eed-9ca1-8494e297490c | -5.93848 | -43.03839 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ce1d1865-1bb0-3969-82f9-bb6d9032d9ba | -5.90105 | -43.35563 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec8e713e-47ce-39c9-ae88-b79b01bcc93e | -6.72908 | -42.25784 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 98114d11-1ca8-32b6-bf1b-ae892a0c22cd | -6.27322 | -44.50769 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1241f876-995e-341d-8645-3503f9812674 | -5.84204 | -43.23298 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24ad99a2-91af-3ec0-b1d9-24ee55f9c6d2 | -6.34664 | -42.5614 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0da12b4a-a90f-3789-9772-84dca196fdfe | -6.30357 | -44.75252 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 387ce92a-5035-37e2-9386-c7d757759fbd | -8.46813 | -43.61405 | 2025-09-03 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50997490-7ffb-37ed-947e-ac3d7b0bc72c | -8.88658 | -45.79748 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be59200d-59a8-3bdb-a8db-8634f9ae751e | -6.47619 | -45.41156 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf8c4f50-2689-3b80-b4ea-ce8c5e151020 | -7.01941 | -44.35452 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc285077-ecb2-3482-a01b-f13a25a0cfed | -7.31555 | -44.27318 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9259f99c-7d39-31a7-8386-a117ef71ac0f | -7.92994 | -46.53388 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5504aea6-d236-383d-9207-ce7c95d1dc0a | -6.27038 | -43.31687 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d44c99df-cc58-331c-aeec-abbde2106893 | -6.36565 | -43.01236 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a44ecd27-b7ee-329e-a48f-a486e40b8892 | -6.25667 | -42.62982 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2595341b-a57e-34ec-9693-79062ecefc8c | -6.54272 | -44.56498 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a309a2d-a638-3c1e-bb15-4a79fc62e0f5 | -6.67401 | -45.9227 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9d6cfe1-799a-3d1d-9424-dee5a50c9c6f | -5.69121 | -45.9471 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9bb1e350-7859-3939-a6a0-eaed456f8882 | -6.26725 | -42.66115 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5368eb25-0c20-337f-b2ec-f3b0d642470e | -7.00378 | -43.21409 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 23aa1146-f2b6-3e49-9695-666efcb3adf8 | -9.19582 | -45.19585 | 2025-09-03 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2ce28186-d159-33eb-85e7-e82d1acdb538 | -6.99664 | -43.25193 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 25075730-262b-35c5-94ef-87a04ea87c93 | -5.84844 | -43.00014 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7a5225f0-fe14-39d7-ae98-3b44d090f80c | -6.72833 | -42.27025 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2a68647d-bba2-350f-9b74-ed388c02e5c0 | -7.94166 | -46.55268 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 659342cf-693f-3d02-a9cd-4e3e48feea51 | -6.33599 | -45.65488 | 2025-09-03 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0c72501-7f78-39fd-9f25-ee1c56734e8d | -7.48981 | -44.81189 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e74febdf-4f98-3055-aaaa-2b519afaf09d | -7.92806 | -46.54467 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 55132b34-3ce5-3d2f-927c-1f6cbefdda7c | -7.93314 | -46.53546 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94d268f9-5e38-30fb-9720-9d075971b431 | -6.98578 | -43.10287 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01813aa4-a5ba-3dca-979b-210eaea51e58 | -6.12772 | -44.13967 | 2025-09-03 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c580f4a-3678-3774-a972-47cf79e3cc84 | -6.85222 | -45.55001 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fb278ee-682b-3eb5-b3bd-fde4d9527a62 | -6.17577 | -43.30819 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5cb3c472-6dc0-383c-b422-6cc408b8befb | -8.38178 | -48.28796 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 680aa0f5-f8f4-3707-b9a3-7a272f13aa68 | -6.46691 | -45.41051 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58858eae-a594-3288-973f-eec606067d07 | -7.00273 | -43.21632 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 082662f6-953c-399e-a6b3-e94aade76248 | -7.98261 | -48.42595 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c362810-ce75-3e38-9206-5148a25ca742 | -7.50035 | -45.34895 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e48d4d80-3bf9-3a94-ae8f-cebf8a2551cb | -7.01873 | -44.35841 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4907d028-49ac-3eae-b7da-81d30ec4e15e | -6.50786 | -42.18836 | 2025-09-03 03:53:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6460d81b-b01d-3eea-a9a3-fb1804374929 | -7.00305 | -43.43054 | 2025-09-03 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75edf74e-9fcb-321e-bdef-db9992cec7e8 | -6.94294 | -43.28754 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cba1f4cf-35d0-3398-95a1-6ae7bf0a8d26 | -7.91042 | -46.4463 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 556d293c-039a-3c60-9a89-21fb09bb145d | -6.03335 | -46.01645 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee6c2a2c-c420-3c51-96cf-d98878c4da9c | -6.69897 | -48.40496 | 2025-09-03 03:53:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| beddc325-e3a9-3424-8ed4-662d7ef80f79 | -7.49828 | -45.33447 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79eba854-bcb6-3b41-abf3-3a2b64c69269 | -8.88821 | -45.78822 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c05b7f20-92bf-3f9c-8181-093f7e733dc7 | -7.96311 | -46.50764 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df4b3fa1-6fdd-3708-ac7b-c3a096fe178f | -6.87282 | -45.56819 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 788a8f14-f55d-34bd-988c-ea92c27f5c42 | -6.35025 | -45.65601 | 2025-09-03 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38bccc1b-4bba-3a6e-9f8d-b48325fa4a2b | -6.47153 | -45.41113 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ad54b8a-1dd5-39dc-9605-bd89f237f5a0 | -6.72911 | -42.26558 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a688eaf7-4de9-393d-9d2e-7133ca39d925 | -5.62924 | -45.18959 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae458bc0-21b6-3aec-9d28-0d3ced03ebd5 | -7.01854 | -44.36293 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40820bd6-ff05-3f6d-926d-a4552aa4c180 | -6.93112 | -44.26368 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5c7b0f1-2749-3061-a24d-6ce1335ecae4 | -8.08385 | -47.60117 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51ac4793-629b-3e59-9374-7226c957a3ee | -6.97128 | -44.35839 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5574480f-6fad-31b1-8631-1bc79ea2d8b8 | -6.14196 | -43.31296 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a41b90d9-dbf2-359b-83a8-15cab594cc75 | -6.76386 | -45.71127 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e45ab740-a51d-3a83-98c3-d4a4259de955 | -8.12631 | -49.91385 | 2025-09-03 03:53:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 50898421-b1de-35a4-a1ac-1df85bd35cc5 | -6.7762 | -45.87455 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aa40242-442f-3f48-a4f6-2e38250d5a6a | -6.27687 | -44.51249 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ee71eb7a-07ad-3ca4-a22d-6abc488b384e | -6.65248 | -43.95613 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dc5df2d-48cf-3ea0-8b91-2a543628fd3a | -9.16161 | -45.20552 | 2025-09-03 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README34.md)
