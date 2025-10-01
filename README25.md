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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de29aaff-42b8-34fe-af93-16ec329056ef | -14.03154 | -47.96692 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 128d1d33-d579-3d69-a29d-a99b6ad3dad5 | -15.07295 | -45.08033 | 2025-10-01 03:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f06037a-64f7-3d11-925a-690706bb6473 | -15.61361 | -46.9129 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85a30ebf-037c-3d6a-9c25-b9367a425de8 | -20.03341 | -44.53731 | 2025-10-01 03:32:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4b5a54c1-9aff-3857-b421-b016b701bd6a | -14.66771 | -48.13979 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 805d84af-3de4-3641-a2ad-71d0bc957c3f | -14.72783 | -46.82993 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a758390-6453-3a4c-9da0-460a02c969f6 | -18.38991 | -43.44511 | 2025-10-01 03:32:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61d339e4-d661-3f49-8aa6-6d0a5b88a1e3 | -16.86148 | -44.27567 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 131307dc-2df3-35de-a073-0d55f20c2f44 | -14.71142 | -48.14316 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 32ef6020-d4dc-3bb6-b39f-9a69d30f99a9 | -15.60629 | -46.91523 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07193067-2ea0-3d25-8d6b-ded415a87602 | -14.75919 | -45.75843 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91551300-2cc1-39be-8a3f-724a19634ab5 | -14.67197 | -46.96033 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 730a4dfa-1aed-3c33-befc-3a610ceca083 | -19.80556 | -44.0729 | 2025-10-01 03:32:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 8e3b3928-716b-3da2-bebd-46416c90731c | -15.76214 | -43.67769 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c20a9631-44ac-3de4-81e5-4d29fe9118ea | -14.61164 | -48.30871 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b56bd49b-0a84-399c-8a20-f123cd995a6d | -13.91554 | -48.09131 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c0688ab-4113-3257-a6eb-93c38468ddcf | -14.89414 | -48.13832 | 2025-10-01 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f50c259c-dab8-3f36-b2ed-74a9fa1e6f01 | -15.73393 | -41.74435 | 2025-10-01 03:32:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 82811004-579a-39e4-9d8d-a369b9d9fe95 | -14.59177 | -48.29712 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80bf331f-1875-3dd7-a92f-445fda286bf9 | -17.80861 | -43.42592 | 2025-10-01 03:32:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4353152c-f225-3e2d-921d-858933ee4876 | -15.77848 | -43.70675 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 878cadbf-445a-3a90-9805-2d1bf66fdf03 | -14.87899 | -48.32073 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a9653d75-54c1-3a24-81fb-e585bb35c299 | -15.5347 | -45.22453 | 2025-10-01 03:32:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dea4dcc7-831d-342c-802d-fe28e80f0dee | -14.60827 | -48.3238 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 994abdff-ef8e-3498-9aa1-a1c6f9919807 | -14.79792 | -48.3364 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b9bf24d3-1ecf-3cbc-8ea9-cf9d06f3ff4f | -18.42109 | -43.81498 | 2025-10-01 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f20ea54-1f24-3bf5-a27f-42a5938ea6f0 | -20.48194 | -43.94714 | 2025-10-01 03:32:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 426d08df-f5c0-32de-9a5e-83175a47fd84 | -14.35467 | -45.92479 | 2025-10-01 03:32:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 54e4d613-be35-3500-b8ed-3202d1717cc6 | -15.7606 | -43.73965 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76a10123-df8d-3aa8-be33-96bc1079dae6 | -14.39297 | -46.22166 | 2025-10-01 03:32:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e22c5df9-01d4-3d47-ad80-b3fea3e78d7b | -15.1242 | -46.45959 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a5b2a7f3-34d6-33a8-9b13-6c2d20996427 | -19.45995 | -44.28577 | 2025-10-01 03:32:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3f6f8d9-f5d5-395e-b865-f037b619ebfc | -14.35299 | -45.90171 | 2025-10-01 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b47b8eb-c9f7-32d1-9cea-25cbaec72899 | -14.44538 | -46.35482 | 2025-10-01 03:32:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4646e54b-728a-302c-8f88-08cb24701d00 | -20.12502 | -46.34148 | 2025-10-01 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 46505586-4848-38aa-bd87-c05afb558fdf | -14.43716 | -46.36094 | 2025-10-01 03:32:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| deffe7ef-a92c-3c42-afa6-59d1fe030a73 | -15.41889 | -47.05991 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e13135f-8570-32c9-8740-8aa0ffaa6350 | -20.63395 | -46.22741 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| acac8c06-d59c-375a-b6b6-87bce07597cc | -19.7671 | -42.1445 | 2025-10-01 03:32:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| de807aba-c36b-3c76-9d7e-13c982a099a5 | -14.89254 | -48.11222 | 2025-10-01 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5aff353-8ae3-37cb-950a-a81822ad3277 | -14.73136 | -46.83463 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ea64adf9-b8de-328a-844d-f99b460f1fa3 | -19.16232 | -44.53124 | 2025-10-01 03:32:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6afcdd21-2b1c-338d-9191-7b67d9ec48d1 | -14.35537 | -47.1334 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 87886b08-5f95-3bad-98f4-173bcdf9c35c | -15.93815 | -48.11906 | 2025-10-01 03:32:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 206d6fac-1bc2-355b-a4f6-e04853adcc75 | -14.9033 | -48.13022 | 2025-10-01 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fd2c790a-ec71-3501-8102-cb08a8436c9e | -14.35581 | -45.91938 | 2025-10-01 03:32:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1d7d5847-01ca-3d6a-acef-d185b1146d16 | -22.11463 | -44.705 | 2025-10-01 03:32:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c2303054-572f-3c6b-99de-d7b0d940497a | -15.75741 | -43.72792 | 2025-10-01 03:32:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d4d46e3-29e0-3f6e-9f49-b560b908c7fc | -14.39416 | -46.21611 | 2025-10-01 03:32:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8ef998e9-6960-3799-a7d0-ee47daab1b09 | -20.62199 | -46.20049 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 872166e1-df1e-358b-8131-cd1f15ff47f3 | -17.97275 | -45.02459 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ad82465-c75e-3059-942f-785d5f66d097 | -15.63194 | -46.25995 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4da35f30-f632-3a40-8012-d44e395e0c5e | -14.89454 | -47.2173 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 447ffc89-53b4-3f4e-ae87-47100a817e25 | -14.71591 | -48.15619 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1e324413-9e4e-3ea3-bded-cc4873fcd232 | -14.55069 | -48.24717 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b3dc8563-a156-3f25-9448-bf712cf4894b | -14.67067 | -46.96634 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec16f72a-f721-3e1a-a5cb-c06d8335ad09 | -15.93724 | -48.11824 | 2025-10-01 03:32:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc7576ac-dff9-3127-8f78-b11c837d56c0 | -15.29046 | -46.20206 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0eaa99d0-b193-38ca-a885-3ffa56aed924 | -14.37562 | -47.1374 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f8fdf45-819e-3a62-afc1-6c016bdd33c8 | -14.6971 | -46.97243 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a600c4c3-3032-32e4-baf7-07f0e19f0391 | -18.70951 | -43.17847 | 2025-10-01 03:32:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b75d2d4d-33fa-3fc2-aea0-d0e64733a0e2 | -22.06608 | -43.0766 | 2025-10-01 03:32:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c0b61e0d-895b-3a2b-89f1-cca422aff347 | -14.70736 | -48.12831 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d48e2625-799d-3c35-b6a1-cdeeaf4eb2ae | -15.4373 | -43.64509 | 2025-10-01 03:32:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 39165ca9-da8d-3392-8ebb-1626e7c6c9e9 | -17.96169 | -45.02183 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50764660-1b44-3dd9-af95-35dd5ae7dd3a | -14.72057 | -48.16848 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b8b9d12-61c9-3380-a399-d88d5b44f6d8 | -20.6923 | -43.3718 | 2025-10-01 03:32:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| da4991e9-3e6f-3715-b9d2-da66c1711aab | -15.48443 | -45.90559 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2fccd0a6-036f-37b5-9b54-3b4c569d65e8 | -15.4122 | -47.059 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7bc0a98-7c33-3d54-b23c-31777b6eb158 | -14.68061 | -45.28363 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df042220-8773-31af-8eee-3723bdf9356a | -17.95956 | -45.01427 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6a2948f-d25d-3a40-ba50-1a234f92b225 | -15.47241 | -45.87134 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c3e4279-3dda-317f-b807-16d8ca58afc2 | -14.51898 | -48.37692 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52a5aa94-4805-3d15-8380-a5d05f4da2d7 | -18.89739 | -47.21402 | 2025-10-01 03:32:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 248c7ee4-37fd-37fa-a9fc-61aa32454113 | -20.61757 | -46.22728 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c29c49b5-ff76-398a-a6df-3b9227abae4d | -20.63521 | -46.22169 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e0168a9-137b-3437-867c-1426b2ab7f25 | -17.97188 | -45.02863 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c232f99c-6d5b-3bfc-b179-969dcd68d9cd | -14.90139 | -48.13894 | 2025-10-01 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 501c610a-1b6f-30eb-90d4-12537227b1fa | -15.48723 | -45.91768 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 868a7e4b-c31d-30cb-bf28-5dd59b88004f | -13.92874 | -48.11144 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43cb7ce9-7203-3622-a0e6-a8d9cfaef925 | -14.34557 | -45.90582 | 2025-10-01 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a165880-010e-3338-9a74-8ea7a98c037b | -14.95973 | -46.88164 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d67066b4-1dc1-3896-bea5-64c3d31201d7 | -22.25435 | -43.4309 | 2025-10-01 03:32:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4d9b8501-22af-38a2-955b-14d2e74d8577 | -15.41906 | -42.02098 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3654be84-89b3-3798-af07-7944635a7853 | -14.52056 | -48.3698 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f340729b-d614-3d05-af6f-8a20ef23cd6c | -20.52726 | -43.45184 | 2025-10-01 03:32:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8183c0af-058a-305f-b21c-4c2afc91d076 | -15.12592 | -46.45722 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e9766fe-5976-397c-87d3-dc55ff600dac | -16.42824 | -42.41023 | 2025-10-01 03:32:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 025ddd15-6db5-3c4c-b144-4745cb71a3d4 | -14.6101 | -48.31559 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 617a3485-df34-370d-8420-ed96acf5a753 | -15.44192 | -43.64979 | 2025-10-01 03:32:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43aba303-34da-379e-b640-f6ca4acbd2cb | -15.77208 | -43.68353 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5bccab73-6a3e-3948-a417-1ae30d53d08f | -20.63131 | -46.21944 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a6b7b616-d646-3ea1-a482-77058e246bf5 | -20.02161 | -44.54157 | 2025-10-01 03:32:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2d891323-d582-3c76-864f-a54ab8e17c41 | -14.37383 | -47.13544 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90a292d9-579e-3efb-b241-e7ace1a53350 | -14.67854 | -48.2427 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54f07158-9f14-343d-be2e-0b43df92e425 | -21.03993 | -45.68239 | 2025-10-01 03:32:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d128450-98ae-39f9-8fab-cf2e90f6bb66 | -15.92511 | -48.14456 | 2025-10-01 03:32:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d979a68b-9bfb-34a2-8e0c-dec4ba5c9af7 | -14.67858 | -46.96185 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 138e2b6c-6175-3e84-a7d1-3bd0fb3db958 | -20.62455 | -46.22286 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ea20a2ce-a97c-323b-b621-13381eecdb46 | -20.62165 | -46.22903 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README26.md)
