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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3afdc03-65db-3faf-b9a4-5335483ed0ef | -9.5367 | -54.792801 | 2024-10-10 01:05:49 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bcf3b2bf-650e-3c6c-8839-e3fd3118726e | -9.9268 | -56.7243 | 2024-10-10 01:05:50 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5358ddb3-6925-38ac-8900-64c5c189b197 | -9.9284 | -56.731499 | 2024-10-10 01:05:50 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79375ad3-0097-32e0-bb41-5db43d155cd4 | -7.5753 | -46.785301 | 2024-10-10 01:05:50 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2dfedb7-81b9-3167-a7f1-ffec7fcc8e4f | -7.5656 | -46.7878 | 2024-10-10 01:05:50 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68d2e313-af5b-3cdc-b54a-88cc24225307 | -7.5707 | -46.808102 | 2024-10-10 01:05:50 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3e82eb3-97ce-3151-89d8-ac773421912c | -10.405 | -59.1264 | 2024-10-10 01:05:51 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7fc9f5eb-ee0f-3555-815c-dc0fcfb7aea4 | -10.4069 | -59.135201 | 2024-10-10 01:05:51 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d5f4acd-3157-383e-b0e0-6dcc9b0f1833 | -7.3694 | -46.127998 | 2024-10-10 01:05:51 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd263986-0e1f-37e8-b79a-eab678656630 | -8.3146 | -49.9645 | 2024-10-10 01:05:51 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf6263de-fae1-3f1d-8399-eafb4180e6c7 | -8.3175 | -49.976601 | 2024-10-10 01:05:51 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a539f10-8566-3d15-b44f-4047bd513575 | -8.9824 | -52.782799 | 2024-10-10 01:05:51 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfedff97-ef41-3af2-8028-bba3fbe57439 | -8.9843 | -52.791 | 2024-10-10 01:05:51 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90aaca31-be85-3d7b-8bac-e788df1ddae4 | -10.3952 | -59.128502 | 2024-10-10 01:05:51 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1efb8661-72df-3f76-99ed-0e613407b63d | -10.3971 | -59.137299 | 2024-10-10 01:05:51 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1532b073-c315-3416-9378-8248eca5f4c6 | -8.4931 | -50.7948 | 2024-10-10 01:05:51 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06727487-02b1-3d55-a52c-7737afa9edc7 | -8.959 | -52.771099 | 2024-10-10 01:05:51 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 993ca3b0-e687-3612-94e3-9d46f52d9440 | -8.9473 | -52.765202 | 2024-10-10 01:05:51 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43d37005-5021-3805-98ce-e906fe9c77b4 | -8.9316 | -52.786098 | 2024-10-10 01:05:52 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b261a9c-d85a-367e-972d-2521befeffe3 | -8.494 | -50.972099 | 2024-10-10 01:05:52 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b000e9d-2097-39ba-953b-7985d76df67a | -8.9218 | -52.788399 | 2024-10-10 01:05:52 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2ca31fa-8446-347a-bc9a-f789f75b820a | -8.9237 | -52.7966 | 2024-10-10 01:05:52 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d43843a-b45b-3e30-b9f1-5097367f50b5 | -9.9894 | -57.668201 | 2024-10-10 01:05:52 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fdf1d560-6214-3c50-87ca-24694d8e32d8 | -10.1066 | -58.210098 | 2024-10-10 01:05:52 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b700838-3bd3-369d-8edb-a65a63a341a2 | -8.2325 | -61.1823 | 2024-10-10 01:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 5d901dc9-1f80-3a30-9c81-edab77f9600e | -8.8616 | -52.973301 | 2024-10-10 01:05:54 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57f0018f-da6c-3968-aa65-aa6c3ecdfa75 | -8.8635 | -52.9813 | 2024-10-10 01:05:54 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc02ca08-4077-3cf9-b994-35fae859db10 | -8.8765 | -53.0373 | 2024-10-10 01:05:54 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7b81800-934d-3d5e-b960-516e01ddee46 | -8.0621 | -49.644798 | 2024-10-10 01:05:54 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 976636de-5c72-38ce-add6-4a3298737fac | -8.0652 | -49.6576 | 2024-10-10 01:05:54 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afc03a14-a631-3e90-9ea4-f63aaa55434b | -8.8537 | -52.983601 | 2024-10-10 01:05:54 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f8fd286-fede-30f0-b89c-f62511fb2da1 | -8.8555 | -52.991699 | 2024-10-10 01:05:54 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b60dbca3-6b7c-3c17-9448-29e724d7cb70 | -8.8592 | -53.007702 | 2024-10-10 01:05:54 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e467d9a4-ee84-3231-a768-922a8bb21867 | -8.8611 | -53.015701 | 2024-10-10 01:05:54 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9412a87d-4cdb-3908-9921-17e4eae17461 | -8.8667 | -53.0396 | 2024-10-10 01:05:54 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c063b9f9-887c-3b73-a875-841786140d00 | -8.855 | -53.033901 | 2024-10-10 01:05:54 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d65c07e-93ab-341c-b675-5a8559665ab7 | -8.8569 | -53.041901 | 2024-10-10 01:05:54 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b60b566-f697-3d47-851f-7ee69524c793 | -9.6418 | -56.691002 | 2024-10-10 01:05:55 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1143c7ec-b11e-3776-b43e-0eb0cd39bffd | -9.9502 | -58.103699 | 2024-10-10 01:05:55 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f68b84cf-666f-323b-80dc-2a490f144b12 | -9.5806 | -56.460999 | 2024-10-10 01:05:55 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d0c166f-888f-3ba8-b006-b283d177e091 | -9.5821 | -56.467999 | 2024-10-10 01:05:55 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5cd98042-35bc-36a9-a131-33e5e49628fc | -9.9421 | -58.113701 | 2024-10-10 01:05:55 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99a27aa7-c653-32b2-a284-f270e0a38bb7 | -9.6543 | -56.934399 | 2024-10-10 01:05:55 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90da77ce-f3ad-3b98-8b65-46ca380fe5f5 | -9.6559 | -56.941601 | 2024-10-10 01:05:55 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bfec6c0e-2643-37a7-9494-1e5fb34807b3 | -9.9094 | -58.104401 | 2024-10-10 01:05:55 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1a61f4b-e595-380f-b095-7aefb9141dbc | -9.911 | -58.112202 | 2024-10-10 01:05:55 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 795cbf2b-0d61-3d22-8f19-9b80579dc429 | -9.9127 | -58.120098 | 2024-10-10 01:05:55 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a18979f-e6e1-34cb-8c15-04b9c2cf7393 | -9.8178 | -57.729599 | 2024-10-10 01:05:55 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2e573e9-71de-3597-a933-0775976fba3e | -9.8995 | -58.106602 | 2024-10-10 01:05:55 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86f08334-0947-3f3c-8cc7-21ddeea08d4f | -9.9012 | -58.114399 | 2024-10-10 01:05:55 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bcb44bad-17ee-3b3f-b655-e5751161e860 | -8.6843 | -63.1009 | 2024-10-10 01:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9548429c-0c1b-36ef-ad73-ffc7cf7721a0 | -8.6844 | -63.082 | 2024-10-10 01:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 9b76e809-9d72-350f-9ce4-f7c803519af4 | -9.8897 | -58.1087 | 2024-10-10 01:05:56 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89012034-ceac-384f-a901-3e6716f6bd12 | -9.8914 | -58.116501 | 2024-10-10 01:05:56 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb7602d7-5cdb-3c6a-b1c8-8f6ae68d2fdb | -9.6834 | -57.207802 | 2024-10-10 01:05:56 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 036eeec9-2737-3f84-add1-43be07e9b5aa | -8.9111 | -62.353 | 2024-10-10 01:05:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 150358ae-79f2-3197-93d2-09c2ef2c7151 | -10.4221 | -60.965199 | 2024-10-10 01:05:57 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 164c6946-651f-323e-b41b-e0c84d572cd1 | -10.4244 | -60.976601 | 2024-10-10 01:05:57 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb27594a-1c17-38d6-a96b-18eb1f9cd70b | -10.0612 | -59.339802 | 2024-10-10 01:05:57 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fbe19748-eb15-3e83-a072-c92319936998 | -9.7298 | -57.844299 | 2024-10-10 01:05:57 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18e49cba-e933-32c2-98a4-a35fec401856 | -9.7314 | -57.851898 | 2024-10-10 01:05:57 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bcdcfee4-2ff2-3101-8eb7-d8c6471374f1 | -9.7331 | -57.8596 | 2024-10-10 01:05:57 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea939702-3e3d-33a8-a218-a7f94306b1e0 | -8.9898 | -61.6261 | 2024-10-10 01:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ede85474-c090-3038-82d5-f633721afe2d | -8.9899 | -61.607 | 2024-10-10 01:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| d4d8fae5-46f0-3365-9404-2ec8a4f5ead5 | -9.0084 | -61.6253 | 2024-10-10 01:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 4cbe85ce-5084-3eb4-abf7-3e9f7e074661 | -9.0085 | -61.6062 | 2024-10-10 01:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2ad0edaf-8a34-387b-bc08-a21e788111a7 | -9.027 | -61.6244 | 2024-10-10 01:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b94734ec-d239-3c21-9459-880198052751 | -9.0271 | -61.6053 | 2024-10-10 01:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 66c42865-f50d-3bbe-a451-1382d7f8d544 | -9.0656 | -61.3934 | 2024-10-10 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 1e0cc8f7-ed01-3196-821e-09ae461263a4 | -9.0841 | -61.4117 | 2024-10-10 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 1a9ef1d7-c6e0-3650-872a-a9f3ca4ff35a | -9.0842 | -61.3925 | 2024-10-10 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 86b86742-4363-3669-82e7-f5e36691bd80 | -9.0843 | -61.3734 | 2024-10-10 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| dcada770-20b6-3c16-98f7-2b145124a828 | -9.0857 | -61.1629 | 2024-10-10 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 07719700-4ae9-3b81-a97a-385c999b5208 | -9.1028 | -61.3917 | 2024-10-10 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 0288f97b-eecf-397f-983e-61dd0476f865 | -9.1035 | -61.2769 | 2024-10-10 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f7aa9982-7b57-36c9-b66d-4de10fba0046 | -6.4908 | -44.313999 | 2024-10-10 01:05:58 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d96570a-5de4-3cfb-9d88-8abcf9795a74 | -10.3721 | -61.216999 | 2024-10-10 01:05:58 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 047529f5-917c-3a99-9eb5-297bd7644cd3 | -10.3746 | -61.228802 | 2024-10-10 01:05:58 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6669e45-7aba-345a-abe5-82813378dcf9 | -9.1221 | -61.276 | 2024-10-10 01:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 849ca166-8814-362b-9773-6f9463e75d68 | -10.3599 | -61.207199 | 2024-10-10 01:05:59 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07dae6e8-e02a-3f1b-9589-0aae29c4278b | -10.3624 | -61.219002 | 2024-10-10 01:05:59 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47bfbcf6-d06c-3749-a6a7-ae548268c312 | -10.3648 | -61.230801 | 2024-10-10 01:05:59 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 921a9754-c6df-32b4-94cf-5da59a5ff21d | -10.3672 | -61.242599 | 2024-10-10 01:05:59 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b7802fe-2b73-34d6-94c4-57909ec199e3 | -10.355 | -61.2328 | 2024-10-10 01:05:59 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 593e9b73-a5eb-3937-8230-286a637a4dcc | -7.6164 | -49.420502 | 2024-10-10 01:06:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcf233c2-a3e4-3fe9-b810-ed84b1d3c9b8 | -7.6066 | -49.422901 | 2024-10-10 01:06:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69ebed1a-07f8-31b6-80da-ecfe982bc982 | -7.6099 | -49.436401 | 2024-10-10 01:06:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9727bf50-3c93-3dd1-bb13-49f78213b6d0 | -7.5872 | -49.384899 | 2024-10-10 01:06:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 687debd2-0196-3023-8bcc-5e00357cbac6 | -9.5452 | -57.8927 | 2024-10-10 01:06:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7843b756-e840-3e96-afb8-5103fad2157c | -9.4633 | -63.1451 | 2024-10-10 01:06:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ef51ad73-291c-3bc0-94bd-0bed8a1561c3 | -9.4818 | -63.1632 | 2024-10-10 01:06:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 86.9 |
| d1e77bd6-5172-3776-a408-f12fad850dbe | -9.4819 | -63.1443 | 2024-10-10 01:06:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 249.7 |
| 1eb45c71-ea42-325d-8769-5b2e61cbcdbc | -9.482 | -63.1253 | 2024-10-10 01:06:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 42740f19-db12-32c2-8f17-41870185d901 | -9.5005 | -63.1435 | 2024-10-10 01:06:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| e0a57a17-ad71-379a-8c70-103cd1d189fe | -9.2705 | -57.200298 | 2024-10-10 01:06:02 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf951f72-011b-3711-be3f-eff77217f532 | -9.2721 | -57.2075 | 2024-10-10 01:06:02 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79637314-4419-34ef-a5db-9568cc52723d | -9.9105 | -58.1313 | 2024-10-10 01:06:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 61181025-4aeb-34f7-b9b3-b519431b9bed | -8.698 | -54.821899 | 2024-10-10 01:06:03 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a97ee31b-f039-378b-899c-c600375c73d4 | -8.6996 | -54.828899 | 2024-10-10 01:06:03 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab6c583-a259-343c-b2d8-ac1800e037c4 | -8.6107 | -54.5737 | 2024-10-10 01:06:04 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README23.md)
