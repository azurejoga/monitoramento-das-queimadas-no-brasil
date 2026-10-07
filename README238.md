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

## Dados Diários - Página 238

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0729eca7-d1ab-39e6-b974-74dbc47c7fbf | -1.27192 | -55.8686 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 35bcc976-fbab-3386-aafb-32608a647521 | -3.18836 | -50.54936 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 6ab447b4-65e5-3632-baef-e36dc1ac4bce | 1.75753 | -55.58004 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 11df7ed5-9220-3acf-b6a7-7a4d7c8da942 | -3.10845 | -53.77525 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8b9ef7dc-f228-3281-af9b-11e1ba356353 | -2.79594 | -57.66876 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 00a88144-ec5d-3ba3-94ee-31a52a0155f7 | -1.79465 | -57.12091 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 17ef0883-a97e-36e7-9b6e-8a0175116fe0 | -2.89672 | -57.1969 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0f0e0f40-af81-3a30-8aff-d896f7be4ae5 | -1.2619 | -55.71354 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c734df04-5cc0-33d5-9cad-b6f02206896f | 1.80445 | -55.53197 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b8f257ca-8b0f-3388-b2ca-b86501cd7b70 | -2.57076 | -50.67861 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c658cfde-954e-36c0-b4c0-ac1ba7a664a6 | -2.80274 | -54.08073 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 60a98a4f-a291-3fdb-a92d-cee5a57b5711 | -3.12047 | -53.78346 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 8e0d363b-b9ec-3513-8b4f-1561d20316a4 | -1.12412 | -54.11841 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a4d633d4-9c72-3299-b0b2-f9a9b105be3c | -3.99413 | -56.24405 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5953abb5-524c-3b45-ae4a-6e71c0343c20 | 1.48196 | -50.76606 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d022d8c1-09e5-377d-8f83-8d510df3aeb4 | -3.10031 | -53.71463 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ca8f9f8-14ba-3956-8e2b-55575f221ca6 | -3.05064 | -57.52499 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8838e4e7-0b3a-3676-90f7-9d5540d3cd3c | -3.85248 | -50.41146 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eed0d280-c485-3031-b7cd-677135ac0b04 | -1.53289 | -46.29416 | 2026-10-07 16:39:00 | NPP-375 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 50ae7664-e177-343f-a441-56bec48d8027 | -3.05064 | -54.15515 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4cd6fd22-ec7e-31e8-8d64-bd8e4cc27061 | -3.08109 | -54.25037 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6153a2e6-b686-3a98-bdb0-9a22dcf43ef0 | -3.51336 | -54.66849 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 374ed668-ba75-35d8-82ee-ce554b0cb5ec | -3.26387 | -54.03948 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| d52381d2-1489-3797-9be2-a9135f8db24e | -1.83034 | -55.72491 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 07cf2d04-5017-31aa-82ed-3518f964f233 | -3.28501 | -54.03293 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fae56a19-444d-3f3a-84c9-9aa0080a44c7 | 2.12004 | -50.82897 | 2026-10-07 16:39:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 618b55c9-c8f9-36b1-bc83-8ef8c0682415 | -1.79944 | -57.10928 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| efcf878f-868d-377c-b7bf-e79708593c00 | -3.05151 | -53.16626 | 2026-10-07 16:39:00 | NPP-375 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 949cbf98-5664-34a0-9350-543ee4f1e692 | -3.59323 | -54.56792 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| b8488872-2a3e-34c6-91c5-dd514a1027ad | -2.97335 | -56.62752 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c1e14144-f504-3ecd-ad04-96d72aac21f6 | -3.70332 | -50.64774 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 51881bbe-f8d6-356a-935e-05697b59f6a4 | -2.77042 | -54.08533 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e8433f64-8b5e-31ba-aa30-602c18da5387 | -1.51921 | -54.51167 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 26d74a95-1d62-3602-8f73-e10e56f36164 | -3.29534 | -54.02807 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5b0f8dbc-fa88-3703-842b-a8f1d671774f | -0.22535 | -48.96355 | 2026-10-07 16:39:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a543315-e5c6-3a59-9b9c-5b9326ef1d46 | -3.10613 | -54.155 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e65cc70a-e7d5-3e46-99a0-0f6e590dd22c | -4.06446 | -55.3209 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| d42e9c84-8317-3669-a89d-6c2da4f491d1 | -3.07943 | -54.27708 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2c88ed75-8bcc-390d-878d-9120a92ee5e7 | -3.06382 | -54.21112 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74492183-8f2f-3c50-ac41-f4e505df0a47 | -0.80035 | -49.17532 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ae2a27d6-d350-3a7e-aa9f-3634b685ae88 | -2.7865 | -57.65177 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d34e0b45-de08-3ea8-9b9b-7a47d292ab38 | -1.79811 | -57.10088 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7d7a1036-e5ba-37d4-9f77-a19183f87605 | -2.96776 | -54.08765 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65f33fdd-2675-33dc-a523-a309335e4173 | -1.89069 | -56.25272 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 613c3c93-3df3-36da-9eb5-a5ab9ddce645 | -3.78675 | -50.75002 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| a0d9c754-30aa-3a1a-9d4d-33cb627a0279 | -1.27857 | -55.85824 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| e3e96c90-9862-3cff-ab15-02b56bb421df | -3.05399 | -54.02551 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| d30c1f0e-65f2-37fd-8fe4-53a8bd68d11e | -3.26977 | -54.04211 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| cdd1b46f-e623-3f94-ac7d-6c167f98a973 | -3.28725 | -57.02009 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 03856ae4-810a-3443-bde9-f75a0fbd32f7 | -3.29104 | -54.07426 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| a69a1114-dbe0-37c8-91d7-ec942119edf3 | -3.18469 | -50.55391 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| fee25d27-ba63-3b91-b3ca-a5980c4a3044 | -1.75532 | -54.99566 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c5384ec0-0c55-3e10-bd7f-1eddddc572ef | -3.21338 | -57.87473 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| f8083774-9c5c-36b3-9cfb-c577d091f310 | -3.26311 | -50.41222 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f2e37694-fbe7-3b5a-8249-0c8610f4a2e0 | -3.29484 | -54.02468 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 27bbd6dd-4d51-37f3-8fc7-33ec6cfdfb35 | -3.0556 | -44.44668 | 2026-10-07 16:39:00 | NPP-375 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| bdff9e41-face-35d5-9e9e-cba15a610693 | -3.30362 | -53.86136 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| f35f9b91-d38a-342a-b1c9-2bcfff8f6fa6 | -2.94609 | -54.10563 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b3ed77ef-28f0-379e-bb0a-0160ab8a74e2 | -4.10158 | -52.06036 | 2026-10-07 16:39:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 780dbbc0-4c53-36ca-b6aa-e13236f00515 | -2.76453 | -54.08274 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 7191b254-4537-3c09-84f4-bc96d39f9564 | -3.28792 | -54.01513 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 63d5551d-b88d-3840-b36d-39b2ad396fc6 | 1.92352 | -55.70135 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f7f03197-5434-369a-9945-5846015ad156 | -3.26143 | -50.40075 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d13ed63b-7ad1-3109-8de5-d664bd9770f9 | -1.82315 | -45.38641 | 2026-10-07 16:39:00 | NPP-375 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 389bb3d9-ff2d-3881-9a18-a8a985901c71 | -2.87852 | -54.17167 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6321bf32-7532-3999-9a33-63d82a422593 | -3.29885 | -54.05196 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| c2b82267-1181-3b61-9ff3-cce94bf51420 | 1.08865 | -50.73232 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 235285c1-4494-3dd4-a8a4-443750075033 | -2.64374 | -56.54114 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0cf0f91e-4578-39fa-8cd3-53952f89d802 | -3.85789 | -50.41861 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| afc8d332-3737-39c6-9c80-6ee98c1bd6ff | -3.20019 | -53.95509 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b1904f9-f6e1-366d-ba9b-561e2c612e1a | -3.2791 | -54.03027 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ba088a9e-313c-3e4b-8877-4fec37386f03 | -3.20476 | -53.8757 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 314826cc-4bd2-3d9b-b586-16f314ff6004 | -4.15771 | -55.15277 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 80ff973e-da18-3d88-9824-17dab08ebe01 | -2.78534 | -51.68334 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6fccacf2-67c7-3d5b-96eb-5746b4e6f21c | -3.30445 | -54.69672 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5f323a62-c261-3a2f-86c5-cdd0bff3026d | -2.98076 | -54.13856 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 71d78c14-f45a-3e20-86b0-fef6b060eee8 | -2.98535 | -54.05735 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 05fff8ed-b510-319a-a3c1-aabd0eddaa9b | -3.29834 | -54.04854 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| b52fe127-fd54-3d44-ab42-5176fb0c3f85 | -2.79686 | -54.07816 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 5b1269cf-5654-3b03-918c-226a61c657eb | -2.46474 | -46.01956 | 2026-10-07 16:39:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 28fcfb96-8361-3a89-9681-c0945563016d | -1.76485 | -54.9827 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2444274e-0c68-3b65-8c30-471af320d133 | -3.81544 | -52.19864 | 2026-10-07 16:39:00 | NPP-375 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 785921f8-aec9-3a1e-a5b9-a59cb14d7e96 | -3.13122 | -54.36316 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 71ed7472-a0c1-3a01-83d7-3b08484d59c7 | -3.47665 | -50.08371 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| ae26b7ae-d6c1-3872-9431-5300911e6aef | -3.48926 | -54.6221 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7c1bdec0-d210-3a33-91ed-8b6686cdfdba | -2.4797 | -56.09445 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 38d6ac12-3a74-3ddf-a1ec-ebd37bd5ed08 | -1.37115 | -47.74802 | 2026-10-07 16:39:00 | NPP-375 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 6a1407d7-6a44-3a86-bcdb-51cfd1c2bf1a | -3.6495 | -55.45785 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| afb56937-f576-3162-8d8b-daa4af60a869 | -3.07139 | -54.1452 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 48ad4ef1-a852-3c4f-ba64-af76939d1253 | -3.95036 | -56.05012 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e455cbd7-a37a-367b-873d-8f86dcf00287 | 1.87964 | -55.72493 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 54958738-3bc9-30c2-895c-b3d2b519551b | -2.50306 | -56.12446 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 7aed1ca9-0843-3c79-ba29-e716a63b49f6 | -3.53556 | -58.4228 | 2026-10-07 16:39:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 790138da-bd72-32a8-93bc-f9c3ee6b6dd1 | 1.90003 | -55.70516 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3dedda0e-51b9-349e-853a-816b91e3c89b | -2.79837 | -54.08825 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| dec37e6b-afd9-3685-9455-24c06564fd82 | -1.21795 | -55.85767 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d52dc2f-a22d-3ffd-9f25-24e6c7007380 | -3.22918 | -54.30158 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 67aa4582-f46b-3093-8b19-2da930da915a | -3.287 | -54.04655 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 331b2db6-d573-368e-be42-f380358d8452 | -1.52024 | -54.51856 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 180d69f4-0d63-3646-be55-e929acdd275a | -3.1071 | -54.16158 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |


[Clique aqui para ver as próximas entradas](README239.md)
