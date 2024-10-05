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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed9ef785-af68-3cdc-974b-646aa48bbe37 | -1.15967 | -53.78405 | 2024-10-05 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 036e89f7-a773-3bc7-ae1b-c83106566dec | -1.12346 | -53.6364 | 2024-10-05 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df245a81-1499-3399-906b-0a17cf4e7d22 | -1.05868 | -47.93082 | 2024-10-05 04:12:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 23d57439-f10d-3232-ba91-cfd18a13b5c7 | -1.05801 | -47.93499 | 2024-10-05 04:12:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0e1a468a-844d-30f6-926c-e047c5c26d83 | -1.05431 | -47.93014 | 2024-10-05 04:12:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58bd5bbf-70b7-3cc7-8302-3c5d46fac7e2 | -1.05364 | -47.93431 | 2024-10-05 04:12:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78a6c774-327f-3825-9f21-5e2e7ffdf5b0 | -1.03753 | -48.7019 | 2024-10-05 04:12:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c023135b-1806-39f2-8e48-dfeb3491b3a7 | -0.73538 | -48.04422 | 2024-10-05 04:12:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d40f368d-b405-39ec-81a3-ca39e93ae4df | -0.73096 | -48.04354 | 2024-10-05 04:12:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1b2a098-2588-3ee4-b1a5-88dac660a7ff | -0.25426 | -48.77442 | 2024-10-05 04:12:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 040de798-49f5-38e4-98cc-930e01968460 | -0.2528 | -48.77092 | 2024-10-05 04:12:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a6f007a-02f8-32e3-9ee5-4a5a2564b0ad | -7.09564 | -44.44071 | 2024-10-05 04:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 453a8407-aae9-3056-8cbf-d51373200248 | -7.09482 | -44.44048 | 2024-10-05 04:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9f155a08-e8df-347f-8c3a-e962ba3222cf | -7.05949 | -44.40174 | 2024-10-05 04:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f069bcb-cfc2-3e23-8dc1-a8377f7c75b8 | -7.04315 | -44.41737 | 2024-10-05 04:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ae6ecc6-53cb-3a09-829e-e067f976cdf1 | -7.01511 | -44.39817 | 2024-10-05 04:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 183d0237-797e-31d3-b82b-86cbd7aeb949 | -7.01453 | -44.40175 | 2024-10-05 04:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8bbf0fa-daef-38b5-9555-449368a66c61 | -7.01173 | -44.39766 | 2024-10-05 04:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4887bf3-c92b-38c3-8afb-6c2cd3feac2e | -6.98623 | -45.73103 | 2024-10-05 04:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8089b94b-2094-3f61-84fd-e95438a47f5a | -6.98559 | -45.73498 | 2024-10-05 04:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0415e8e5-ef7e-3ac0-b601-6f9a196c50cf | -6.88336 | -46.14055 | 2024-10-05 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f105debd-806b-3624-a979-dbe8bd7db88a | -6.88268 | -46.14469 | 2024-10-05 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5dedb25-88e2-3b4b-acc2-61ff64314e70 | -6.88042 | -46.13586 | 2024-10-05 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 805ebab8-5f13-3d8c-93a7-ec8a16c60445 | -6.87975 | -46.14 | 2024-10-05 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2de0894-4d53-38bd-af29-2bf207cf835c | -6.87907 | -46.14415 | 2024-10-05 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2c1e899-777a-3d0f-834d-5faac476f19c | -6.76158 | -46.29313 | 2024-10-05 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff762a83-1f88-38f2-aee9-78e3904c144f | -6.76089 | -46.29733 | 2024-10-05 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 557ac115-7427-3e39-a221-dbbaf9bac853 | -6.76021 | -46.30154 | 2024-10-05 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f70d284f-5768-3f6b-a6fc-9ceb7636b65f | -6.75726 | -46.29675 | 2024-10-05 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6ef9c3f-1e88-3613-8a87-bcd9c0f5fecb | -6.75657 | -46.30097 | 2024-10-05 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96ad053c-3607-3471-af0d-54203a27fbab | -6.75362 | -46.29617 | 2024-10-05 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48f8c5ba-14d3-3dad-bc17-658525ebd83b | -6.75293 | -46.30039 | 2024-10-05 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ede50416-7948-38bc-bb60-cbb2e01597b3 | -6.74929 | -46.2998 | 2024-10-05 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02e39e21-94f8-301d-a9bf-d7b3b9c69b0d | -6.7124 | -46.06394 | 2024-10-05 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9934851-b03b-352e-a775-3740660977ff | -6.71174 | -46.06806 | 2024-10-05 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35e1eed0-c894-311b-8cb1-84d6669c9886 | -6.71166 | -47.2349 | 2024-10-05 04:12:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fababb6-e792-3b0a-9d0f-5145fd712e61 | -6.71008 | -44.53142 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0e6d18c-67d8-31c5-be43-1aa6cac381c4 | -6.7095 | -44.53508 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af602be6-c564-3e69-b7ea-037bee19794a | -6.68249 | -44.83478 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eff6e5a1-0c3e-3b10-8dce-b78e7fbb31a0 | -6.67455 | -44.51463 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cda85384-8b3f-370a-9251-4761262ec743 | -6.67116 | -44.51411 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f157ed4c-cdcd-332b-b2c1-4cd709414533 | -6.67057 | -44.51775 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0bbbe44-b28d-3689-a359-cb85cc873551 | -6.66718 | -44.51724 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2189b22b-867c-3e05-8702-6ac751ce918a | -6.66387 | -44.05778 | 2024-10-05 04:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e95d80ca-3af4-3ec1-9b54-b7385ef3c5f2 | -6.66039 | -44.51621 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b33cf093-5638-3da4-9fb8-00554589e8bf | -6.62442 | -45.33078 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cabe0406-fb2d-3bf7-856a-286965412bd9 | -6.6238 | -45.33463 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0b811ca-2156-3e34-99fd-76d5b3b860fa | -6.58079 | -44.17912 | 2024-10-05 04:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5913d068-9119-3482-8cf5-36816b14f6f3 | -6.57743 | -44.17855 | 2024-10-05 04:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0be761dc-e384-3926-b2c1-e6263f0f0c8f | -6.57463 | -44.17445 | 2024-10-05 04:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd19190f-8671-38f0-8b8e-c37588a6598b | -6.5723 | -44.2326 | 2024-10-05 04:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e39d32df-97e7-3fda-9e16-b1f4cdab7bee | -6.57173 | -44.23619 | 2024-10-05 04:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26d5f93f-0888-35da-98be-e20af57f75cb | -6.56836 | -44.23566 | 2024-10-05 04:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c244fe34-4f6f-3d25-abd9-2e2d779fd532 | -6.56749 | -44.61636 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c9ec995-0bec-34da-9053-bd96e933dbce | -6.50295 | -44.14846 | 2024-10-05 04:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd424a6a-6624-3e9e-b38f-fe1bffbce717 | -6.43361 | -44.03585 | 2024-10-05 04:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 268c3ad9-99b8-38c2-925b-4bb864cfd392 | -6.42068 | -44.07365 | 2024-10-05 04:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f477837-8dc9-3b9a-97f2-852989b2a8c1 | -6.34586 | -45.69655 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 323aa51b-a993-3e45-bd4f-d7a1f5446620 | -6.34521 | -45.70065 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7950060-e1ab-3c56-90d2-10942a7a8b9f | -6.34231 | -45.69604 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7f50016-83f5-3efd-b9d4-0be441417e70 | -6.33875 | -45.69553 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1da07b17-1439-3ce5-9667-69e817956dc0 | -6.33809 | -45.69968 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d23a4700-537d-3534-98cc-e2ff8e6e6f79 | -6.33583 | -45.69104 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c6b678a-ce95-37b0-836b-573ac573ec97 | -6.33453 | -45.69921 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc0c736f-03f4-38a0-98cf-c9d8c25dcfdb | -6.33227 | -45.69061 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 05229167-c430-397e-bff3-a675fc4fe62f | -6.3287 | -45.69016 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a0a8ef68-4ac1-3f3b-85dc-695ea25b60e3 | -6.31462 | -44.77633 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 972cbc1f-cba2-3d56-a2da-765ce394cf48 | -6.29884 | -45.87549 | 2024-10-05 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3533db6-bea5-33e9-8c5d-83d34d5b47be | -6.20988 | -44.31924 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1f95c96-e53d-37b3-a5cc-ec4fc049123c | -6.2093 | -44.32286 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b52b57e-fcdb-34cf-9a9f-e2ae16d0446f | -6.18403 | -44.13496 | 2024-10-05 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d317a35b-6c7e-3814-95cb-35e5285bfd4a | -6.18345 | -44.13854 | 2024-10-05 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cebb22cf-4200-32d6-8d46-31dfafd54eed | -6.18226 | -45.43653 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| caf0385c-c416-30f7-96e1-d7dee5333093 | -6.17939 | -45.43209 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 77801ba5-cc1b-3e54-9fd1-2345e2470311 | -6.17894 | -45.4328 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f434d7a5-2422-3861-8c10-4a809e2bd92b | -6.17875 | -45.43596 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 56825150-84fb-3534-bf84-2ba78690cb4d | -6.17832 | -45.43668 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 30fc4764-dbf2-3e4c-ab08-e2a203bf3a48 | -6.1777 | -45.44059 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8365d801-cd83-3855-9a45-60e5fae0ec71 | -6.17524 | -45.43542 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 96e0178d-2299-3953-beba-c4eacee6e778 | -6.17481 | -45.43614 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| deeb22b3-d9e9-367f-8810-0ea3e4d8deb1 | -6.17459 | -45.43932 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| bc5e2da3-d248-34f3-aceb-91ec83fc90e2 | -6.17418 | -45.44006 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5bb4e78b-eb29-36c0-ad84-eb0a175ba661 | -6.17116 | -44.12912 | 2024-10-05 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5ce19d3-b47e-3e6f-8512-dec0dc65a804 | -6.17066 | -45.43952 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b3b52e1-ce14-3ef9-8ab9-a0fb2db5d877 | -6.17058 | -44.13273 | 2024-10-05 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30a5dff2-1c7b-3dab-863f-66f4ad9e0d94 | -6.16983 | -44.12849 | 2024-10-05 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b4ac775-1363-346f-9343-c8905ac2dc16 | -6.16926 | -44.1321 | 2024-10-05 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 647c6f34-0428-335a-86d7-c371abe23cfa | -6.16869 | -44.13571 | 2024-10-05 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d590e2ec-3f2d-35cb-96ac-1c2e84433147 | -6.16533 | -44.13515 | 2024-10-05 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fd2b51c-f01f-36e3-8ff8-0f5f1a66db45 | -6.16362 | -44.14599 | 2024-10-05 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2cfaca0-959b-3b38-bead-044b9c883d62 | -6.08605 | -44.69916 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a26305b7-de62-3568-910c-6820a095df74 | -6.08545 | -44.70287 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff8e27c5-0ba6-35ca-9bdb-a62e475c96f3 | -6.08263 | -44.69863 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c991b2c-1cf1-38f9-87f1-cbed1a18d41e | -6.08202 | -44.70233 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 033c1724-c17b-3b5f-9188-a593c40c22d8 | -6.07898 | -44.70167 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47404819-8a51-30d5-9219-dd298c19e631 | -6.0786 | -44.70179 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0167f485-df82-32fc-ba0d-3f5fbe7f130d | -6.0784 | -44.70538 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f96a93c5-cceb-3ba0-8620-12ba88045909 | -6.078 | -44.7055 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a95fb71a-536c-38bb-9a26-cc0c3f402a89 | -6.07556 | -44.70114 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd0b5f21-7004-3e32-93f3-a03dec097812 | -6.07214 | -44.7006 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README57.md)
