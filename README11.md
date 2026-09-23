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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80113d4f-7455-3e5f-8c6e-66d4938687a1 | -3.579 | -50.0303 | 2026-09-23 00:36:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 403fae55-8f48-39c2-bd0c-4d2c1df188b1 | -12.7832 | -50.884602 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7285d3dd-2247-3476-9dfa-5f6f9b26bc11 | -6.1162 | -59.8713 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c360c3c1-99fb-37fb-9a58-f37cebd68e90 | -4.442 | -55.071999 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 962cd6d1-94ab-3859-a36d-49569ade247f | -10.6052 | -53.973099 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f9dac3c-a66e-3d88-a98c-baae6db2df62 | -6.3476 | -57.757099 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3f18cdf-45c5-3f87-a081-98fd10d74ed5 | -5.1104 | -48.790001 | 2026-09-23 00:36:00 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 072cd9bb-1232-3fac-9af8-58066f613992 | -6.3624 | -58.285999 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10448986-aded-31e4-b05a-c4f7f9069e2a | -6.2939 | -57.746899 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe732a1c-2f5a-355e-925d-651cf2a43aaa | -3.6318 | -58.9174 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dabf03e1-da63-3730-9e00-867729e6a936 | -7.4559 | -61.368999 | 2026-09-23 00:36:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb46f6a5-a814-3f84-a735-7eae772b197e | -11.6911 | -50.941799 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5f32dc03-ee80-3d90-8055-dbdb8c016107 | -8.242 | -55.232201 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6e0c76f-d057-31af-a5f3-bd162ddc31b9 | -11.7009 | -50.9394 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7b71b3ac-9d37-3f09-8995-82979de0a4b2 | -3.4968 | -53.202499 | 2026-09-23 00:36:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9114802-7112-36ef-98fb-cc465e39e1bd | -6.6712 | -58.564999 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b354549-ed4e-3543-81f4-9deda50a25b7 | -3.6813 | -60.568298 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d720e49e-934b-3b85-a1e6-f4890ee96fb3 | -10.8774 | -56.232201 | 2026-09-23 00:36:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca16e940-7c17-35df-ae59-8fd23fccb493 | -9.1509 | -59.482601 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 230342f8-8725-3e13-9e90-31d8be8e56b8 | -6.3049 | -59.935902 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50bca5f6-72f5-38b1-b652-813be4dff03a | -8.2231 | -62.823101 | 2026-09-23 00:36:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ae02377f-678e-383b-9f52-47570bff9f80 | -5.8708 | -52.070999 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c76c30e2-e97c-32b1-a7d7-9fe37accd3a5 | -11.7796 | -50.067799 | 2026-09-23 00:36:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a58ba190-c53d-3861-b60e-f468b6ba85c8 | -8.2367 | -54.666401 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 256eba88-f6ab-3be5-8629-34d758c88161 | -6.6768 | -55.060699 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1082bb4-af49-315e-becb-9debe226635c | -11.6958 | -50.961201 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ec34b625-fa59-373d-90af-746afd6a045f | -3.384 | -59.419601 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d34cf891-2fb2-37a6-aa9d-9b65ff389059 | -2.4651 | -57.8979 | 2026-09-23 00:36:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac417c28-8840-3207-9140-86e2b86327f1 | -3.8607 | -58.882198 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a276efa0-f0f1-308e-83e2-c37f866d51ca | -3.0822 | -61.1549 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 807a4b18-7e06-37f7-abc3-b17d3c57f031 | -5.235 | -48.201801 | 2026-09-23 00:36:00 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e5afabfa-14e8-35ce-930d-668b7e49e915 | -3.6795 | -60.559898 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af30dc3a-cd48-34e6-a8c6-789b5a042d38 | -6.3223 | -43.9506 | 2026-09-23 00:36:00 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8828ec70-9480-3fad-a6d1-ce58c44c7e8c | -6.6063 | -59.906101 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a494aaf-2a22-31bc-a21b-5e6fce458cce | 2.7297 | -60.672401 | 2026-09-23 00:36:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 82abf7ed-64d5-315b-8402-ea2a064ef07e | -6.1192 | -57.748699 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba87383b-7d49-335d-9987-d909405c135c | -10.6926 | -48.7141 | 2026-09-23 00:36:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 309b7e97-c0bd-38ba-9430-bcbadb79e5b3 | -9.5736 | -48.445702 | 2026-09-23 00:36:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd48628b-689f-31a6-bf48-91dcf8f9bd23 | -6.7829 | -48.696301 | 2026-09-23 00:36:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c9c5e0bb-8105-3f28-b014-68b647fe0884 | -6.0813 | -57.624802 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faeb3a95-0d1c-3136-aaa9-3191e806067a | -6.1005 | -57.6646 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10f50064-a959-3cfd-96ba-2c87000f17dd | -2.8545 | -57.797199 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a63c09be-91ac-37b8-b87f-21aa9b1ab558 | -2.4666 | -57.9048 | 2026-09-23 00:36:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd6dde33-7729-349a-a220-e17439ddef4c | -6.0871 | -57.696899 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e973555b-6582-3f02-8aec-acd5b4c23c00 | -12.402 | -46.976799 | 2026-09-23 00:36:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a415843c-0986-35e7-b54c-80a1354898d6 | -3.4947 | -53.193298 | 2026-09-23 00:36:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b54d3a3c-b3af-3d29-980d-c6c3d7ecca22 | -4.4497 | -55.015999 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55a08c7e-bfb6-3f6b-a3a1-0d660da13817 | -3.1895 | -59.700298 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 573f02fc-8589-33b3-a9cf-50bd83a2e69a | -6.7455 | -55.090099 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d9298f-fa34-35a8-9e8e-6056fd2b6613 | -5.3411 | -45.186699 | 2026-09-23 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d41a8022-8a79-3044-b761-938c1ae9c071 | -3.4799 | -59.572498 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0c4aa83-e861-3812-ada0-9296621944f6 | -3.6953 | -60.5387 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 073db1b9-c174-36ea-94ca-6bd81da7f701 | -9.9391 | -48.4641 | 2026-09-23 00:36:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cbef5e3a-3132-3734-a705-372ba54f3550 | -3.5794 | -59.050999 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6a471c7-b680-3edd-982f-80f31d27853a | -6.6077 | -59.959202 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef0fcde3-0a48-3088-b56f-bcaea5a608e8 | -3.2489 | -53.959801 | 2026-09-23 00:36:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65993926-e76d-31ee-a867-baa4c4af4fe4 | -3.1834 | -56.8358 | 2026-09-23 00:36:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 542379d0-bf7b-3784-be2a-eca584a30dd4 | -6.345 | -57.883701 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89fb8ba3-d947-3c58-a430-3920843e7ba4 | -5.1773 | -56.173401 | 2026-09-23 00:36:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae5305a9-e4cf-31dc-88bc-bea1600e422a | -10.5449 | -57.433201 | 2026-09-23 00:36:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15d14e1c-4064-3e18-bd2e-28a8edb1853e | -5.8077 | -57.736801 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b36cf18-9009-3399-a01f-aac11145093b | -3.2147 | -46.954102 | 2026-09-23 00:36:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2127f773-3c22-384f-97d4-01686853e964 | -10.5889 | -53.992199 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 391e3e8b-2681-339f-9879-2859fcf4180e | -10.7023 | -48.7117 | 2026-09-23 00:36:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0e19344-4de3-3631-b24b-e3a9a151b65e | -4.562 | -54.920399 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9123f6db-a775-30de-b2f4-725513d90d34 | -6.7587 | -63.128601 | 2026-09-23 00:36:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0a067e7-908d-3197-b5dc-3c932074c67c | -11.4553 | -47.353802 | 2026-09-23 00:36:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 503fea5e-53b5-3ba5-91b7-97582131fcc3 | -11.6934 | -50.9515 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e2ff527b-4489-3807-a91e-de173f3414b1 | -10.2675 | -50.2216 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e0aab5a-0f79-33bf-b634-8a0a6df0f08f | -12.769 | -50.868 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a7bc2ec0-15f7-3188-bd0f-f30a921a47c8 | -6.5882 | -51.311401 | 2026-09-23 00:36:00 | METOP-B | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b58ec71-9da7-30b9-aed0-573eca6a7025 | -8.9209 | -61.481602 | 2026-09-23 00:36:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fb02f1d9-3846-386a-b7e7-5006b32c8ba7 | -6.7324 | -55.078098 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74cff315-01c4-3ed0-b8cd-0922b112dd52 | -6.3031 | -59.927502 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1147bcac-1b2c-3d8c-ae1c-79024f0fcefa | -5.4559 | -60.137798 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fac3af9c-1629-33de-9c34-eb28c25d2a05 | -3.7928 | -59.361198 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa5f81fe-b92e-3454-af4c-97835c962d5a | -4.0626 | -56.2127 | 2026-09-23 00:36:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67afcf3e-bd57-3e35-9e2f-293b86840c8c | -3.0435 | -61.257702 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1f558f3-537d-3220-8325-1187ffba9d8b | -3.4388 | -60.402302 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da6e864f-9b97-3507-9150-fccd51a1b386 | -2.9645 | -50.385601 | 2026-09-23 00:36:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c89c553-048a-326a-a051-6e19cf0fb3bd | -12.7907 | -50.8727 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5639a5b3-4c86-3b86-bf8b-6748f1d9bcf1 | -6.2563 | -55.432301 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22f512fd-e4aa-3c37-8ddb-8ae16b9c2347 | -6.6662 | -58.542702 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6adccf3-40a0-38b0-a52b-8436dd8f8735 | -6.8903 | -55.318199 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3908cc4d-2381-3ce8-9f7a-cffba3a89382 | -4.3026 | -55.590599 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5795396d-28ca-3d0c-b7f4-bb5e98711bfb | -6.6596 | -58.5597 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a6ae4142-6436-30e5-b5dc-7fd5dd2626ed | -6.6777 | -58.547901 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| edd92895-796e-3d08-9bfb-9d3866ea5c22 | -2.7412 | -51.5411 | 2026-09-23 00:36:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b132f3ea-86af-3936-a077-7291f9120adf | -3.78 | -60.735199 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9bec7828-2baf-3e32-ad7f-cd6f1ce2455e | -4.5133 | -54.978199 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2eae82c4-75c0-389e-ab45-ff7195604785 | -5.6547 | -60.2015 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c52e3e2-7dd7-31ce-88cd-6cca4ed71e4b | -6.4529 | -54.983299 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 221a1f9f-bf34-3c2f-8914-3319b28601c8 | -3.6501 | -57.076099 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ffffe23-2c32-3f61-aec6-364e0c3d228b | -13.4318 | -46.244301 | 2026-09-23 00:36:00 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b03eac30-6ebe-3358-b14f-71fe20e7ec5d | -8.1862 | -54.715801 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d3a9d12-bbd6-3c2f-bdc4-6db17b888c33 | -2.7636 | -57.0299 | 2026-09-23 00:36:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38900536-afdc-37dc-b73c-3a291f5f9be1 | -9.9671 | -50.260101 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dcc638e5-f264-3bae-9e12-fbfe3ce193af | -8.4852 | -57.605499 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eac0f4a-5b17-3bbe-a2dd-c7a3c99297aa | -7.7216 | -61.224701 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94b33089-7042-3938-9f83-91cec115cf71 | -8.1732 | -54.794201 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
