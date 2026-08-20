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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75f4523a-0da5-339c-8558-53693f4cdd0f | -23.62547 | -48.28241 | 2026-08-20 04:04:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63da2768-808b-3e08-a54e-e7920fe632c2 | -20.5272 | -45.37748 | 2026-08-20 04:04:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 98589ea5-1d6d-3326-883b-7910a3d21b49 | -19.46321 | -46.8166 | 2026-08-20 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3faa12dd-25c1-33b9-b583-43dc69127f4a | -16.38625 | -49.23354 | 2026-08-20 04:04:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 418dc624-a3e4-30f2-b6ee-8a84796f6658 | -17.94442 | -44.40543 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 158d6d01-c43c-3cb1-8d6a-b80ad6d258a6 | -20.35044 | -41.54961 | 2026-08-20 04:04:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bb98d750-685c-3eda-bcf7-177196d6ae97 | -17.33273 | -43.62742 | 2026-08-20 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 9d32605d-b8b9-30b5-977e-2c1c39c6e7ef | -18.03959 | -44.62328 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ff4a5174-b60b-305f-9d17-007b77d48a63 | -15.70963 | -53.7776 | 2026-08-20 04:04:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66345d4f-9a65-31d3-954c-d7fd2f305b5e | -20.28361 | -46.46089 | 2026-08-20 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46748bc9-fab1-3624-a8ae-f53f61968fe9 | -19.65915 | -45.90834 | 2026-08-20 04:04:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| af8ce1ca-da6f-32bf-9122-1ef4a883ba48 | -18.79103 | -48.55393 | 2026-08-20 04:04:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06433e6d-9306-3ca2-8309-4a7fef1fe942 | -18.17798 | -44.7077 | 2026-08-20 04:04:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4269970-1a31-3c3d-ab0d-370b23a6a1a7 | -18.03265 | -44.61644 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 35.1 |
| a6c382e1-ff7f-307b-95c3-147ad2778b3d | -17.33185 | -43.63234 | 2026-08-20 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b83a5334-9fb4-3f5f-a8e1-798164f98bc1 | -21.58741 | -45.89328 | 2026-08-20 04:04:00 | NPP-375D | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 02e05a80-b72a-3ec8-8e57-91d73da338f2 | -23.42081 | -46.95044 | 2026-08-20 04:04:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| a6cf2746-ab26-3620-bdd1-0de9dc6eb4ed | -21.14225 | -43.90866 | 2026-08-20 04:04:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 364eeaa5-26e6-3d76-ba5a-6bdd08186806 | -21.35999 | -43.6983 | 2026-08-20 04:04:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6c691836-0b04-38fa-a7f8-5160387150c6 | -19.71435 | -46.22636 | 2026-08-20 04:04:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94f4f82b-4971-3bef-aca7-d00eaabe0549 | -18.55734 | -48.28923 | 2026-08-20 04:04:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d29f00d9-db6b-3ae5-8718-1f441d338348 | -21.61836 | -49.01912 | 2026-08-20 04:04:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0722d8f9-8608-31a7-94fd-b9fa82627c8b | -15.7092 | -53.77642 | 2026-08-20 04:04:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d78b841d-71bb-3087-a19e-90d88271b9f5 | -18.22513 | -43.57852 | 2026-08-20 04:04:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a0713c59-3e44-3845-81b2-5d4e732b386d | -20.76309 | -43.41329 | 2026-08-20 04:04:00 | NPP-375D | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 565f8722-c4e4-3586-86ad-0abb75f5d11c | -19.3926 | -46.41034 | 2026-08-20 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24b44497-dcfb-3aed-b29e-b52dfb764dbc | -23.62659 | -48.28038 | 2026-08-20 04:04:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b6a1f2b-8a5f-3a7d-ad7c-2b5c245eeef4 | -21.10941 | -45.61199 | 2026-08-20 04:04:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3af0d871-d3f9-3ffd-b82c-5e39a67152ff | -19.78506 | -42.06487 | 2026-08-20 04:04:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 82b6597e-bd18-3f2e-afc6-6e4420da2d3b | -18.03067 | -44.61935 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| b02dac25-1c7e-3daa-80a3-6432ccec3c70 | -15.71642 | -53.77802 | 2026-08-20 04:04:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59e34b8a-d623-3015-974e-9c16727abfdb | -21.87065 | -46.57244 | 2026-08-20 04:04:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a9f700e5-a390-3ae0-96d0-1c87c86d25fa | -18.88084 | -41.09129 | 2026-08-20 04:04:00 | NPP-375D | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| d7dc04de-e345-3ec8-8746-6cd2710726ec | -16.38677 | -49.22923 | 2026-08-20 04:04:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7241cc2-206a-3448-995b-27430fced55f | -17.92777 | -44.42984 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 186ce3cd-908c-3da6-a31e-306fd97d370b | -18.70517 | -46.4534 | 2026-08-20 04:04:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82a5c929-b191-3694-ba0f-2de13d346f01 | -20.89551 | -50.50615 | 2026-08-20 04:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4c2f43a9-8ef0-3909-86cf-9a286ed8becd | -18.0356 | -44.61484 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 1a7bb3c9-80d1-3b03-aa4a-b285c935eee6 | -15.3863 | -52.72969 | 2026-08-20 04:04:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2d20246-d612-3a6f-821e-413ba7783607 | -17.93473 | -42.80111 | 2026-08-20 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a7bef56-bfe8-3462-8ecd-d562953f217e | -19.71766 | -49.12521 | 2026-08-20 04:04:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e2ed3fe-35bb-3ac8-a7e9-f68eed6ba79b | -17.94052 | -44.40451 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5e1a95e6-13e4-3706-bf5d-201338fae2f0 | -18.03563 | -44.62246 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 94dad3d0-f530-322b-b94f-ffaf583a1edc | -16.38699 | -49.22991 | 2026-08-20 04:04:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a885629e-3a7d-3331-a841-bc49583e2b35 | -23.42001 | -46.95448 | 2026-08-20 04:04:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| bb224c37-71dd-3dbe-88cb-df8c20f079dd | -19.43358 | -42.51665 | 2026-08-20 04:04:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e6dea6f5-286b-3097-bcf0-3ea76cf4d787 | -17.32981 | -43.62175 | 2026-08-20 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32e58306-f74c-3749-bc45-af16737ec290 | -20.88661 | -45.4213 | 2026-08-20 04:04:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4d104fd7-2ad4-32ba-a768-10c8cc61f669 | -20.80589 | -43.8603 | 2026-08-20 04:04:00 | NPP-375D | CRISTIANO OTONI | MINAS GERAIS | Brasil | 3120409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 863d6e07-c8dc-3c10-9c1a-30fdc50be7fc | -21.71808 | -47.14119 | 2026-08-20 04:04:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22398750-51d5-3336-95e7-984f4a66c9ed | -21.87562 | -46.56927 | 2026-08-20 04:04:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0f0c9bc5-a56e-341b-a996-fa11d8a06690 | -21.87643 | -46.5651 | 2026-08-20 04:04:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d7a8e3eb-21b1-3559-8f02-db2b2b777001 | -19.43708 | -42.51733 | 2026-08-20 04:04:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 12609a63-8e3d-3ed9-b9de-d233363a9f17 | -20.29332 | -46.45668 | 2026-08-20 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1c42ee8-be4c-3885-8b6b-543945323451 | -21.35895 | -43.70017 | 2026-08-20 04:04:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a2b806dd-a28b-391e-aba9-6429ab24d4ab | -21.61464 | -49.01942 | 2026-08-20 04:04:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31a2e9f1-c721-372f-91e4-2319087ee325 | -17.32894 | -43.62667 | 2026-08-20 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40d07767-3ff5-30ac-a55a-71df4df9bdc5 | -20.00766 | -45.74036 | 2026-08-20 04:04:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d50af900-0091-3b5d-9bb4-2ba9d9755f38 | -23.47091 | -46.28396 | 2026-08-20 04:04:00 | NPP-375D | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d81f04c0-f14d-382a-8052-e246a1d6ef7f | -20.9017 | -50.50399 | 2026-08-20 04:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7c149423-1762-3c3a-a518-42aaded6755a | -18.88021 | -41.09506 | 2026-08-20 04:04:00 | NPP-375D | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 32338c36-0547-33c7-8d7b-6b8ac7c2f07c | -20.82877 | -42.81616 | 2026-08-20 04:04:00 | NPP-375D | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a6d83952-8bd2-3a54-b97d-7ac22445dc96 | -19.65995 | -45.90422 | 2026-08-20 04:04:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a3fe7fcc-90d7-356a-afa8-84991b9cfef0 | -17.93368 | -44.24293 | 2026-08-20 04:04:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82279df7-7877-388e-84dd-ea12a797d2ba | -19.77227 | -46.04193 | 2026-08-20 04:04:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 167629c1-1c9a-35c5-bf9c-ef1a45d1c5ad | -19.94916 | -44.25898 | 2026-08-20 04:04:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ae55ff07-315f-331e-b01e-335101076c12 | -20.00543 | -45.73846 | 2026-08-20 04:04:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91b5566b-b1af-3c21-b1d1-8f32f4724154 | -18.03369 | -44.62537 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| cca2d73e-398a-34a7-9674-1b776bf081dc | -19.67639 | -42.10718 | 2026-08-20 04:04:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 759b9069-d172-34af-b0aa-3d4cf864f282 | -21.87146 | -46.56828 | 2026-08-20 04:04:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6bfff00c-02c5-3c1f-949c-6bf5de85ca2d | -21.44996 | -48.51723 | 2026-08-20 04:04:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a01eba9b-3aa6-3077-9e3e-0617909c1a2e | -17.77441 | -49.13268 | 2026-08-20 04:04:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8a42640-c3a4-3229-949d-94904b0b43fd | -21.37801 | -43.74321 | 2026-08-20 04:04:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 94e7b404-5368-32d3-9d29-cc61a953e11d | -20.68994 | -45.2673 | 2026-08-20 04:04:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 80878ecb-1fb9-3d0b-a77f-cb64348f5fd9 | -19.94815 | -44.26089 | 2026-08-20 04:04:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a8780252-71ca-3b90-880f-89ef1b3c1599 | -17.93834 | -42.80178 | 2026-08-20 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c968a8b-c39e-3c71-8ef4-b651353585c8 | -21.11011 | -45.60823 | 2026-08-20 04:04:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fa53e431-21ce-3317-975c-cd2c4a04ec52 | -18.85085 | -47.14402 | 2026-08-20 04:04:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd48459d-b233-3bea-b852-28a6b99cdf94 | -15.71685 | -53.77919 | 2026-08-20 04:04:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a70381c-6851-3d77-b524-dd3a389bc8f9 | -20.96802 | -44.12124 | 2026-08-20 04:04:00 | NPP-375D | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b0877ef2-bc3a-31c3-ad2e-df676a15f609 | -17.93847 | -42.79859 | 2026-08-20 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2abd277-5b9e-3cc2-a546-d0fa1574cefa | -17.33738 | -43.6233 | 2026-08-20 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 29a1eee2-3ea6-37a9-a599-28a3b604e249 | -18.03465 | -44.62009 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e453acf6-6a00-36ee-b9dc-fbc16dc9b46b | -21.61953 | -49.0205 | 2026-08-20 04:04:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3e26aaa-597c-35e4-917a-708a40c7da11 | -19.24347 | -42.1937 | 2026-08-20 04:04:00 | NPP-375D | IAPU | MINAS GERAIS | Brasil | 3129301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| fda3a750-446c-38b8-a812-8cc7d1ebe26a | -18.71601 | -43.21231 | 2026-08-20 04:04:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ba2b7c9f-ce5a-33e8-8e4f-500b5fc6d06c | -18.03662 | -44.61721 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 199de116-77c1-3728-a377-efade5448ef8 | -18.84343 | -47.1407 | 2026-08-20 04:04:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9db900d8-4296-374c-9cff-1f66b68aa0a2 | -17.88803 | -40.06395 | 2026-08-20 04:04:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ecbe4ed8-1ac4-31fc-bd6b-e5e7834a1d4f | -20.2832 | -42.87518 | 2026-08-20 04:04:00 | NPP-375D | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0274fa46-310e-3439-8e50-71d598f8823a | -20.29933 | -46.68388 | 2026-08-20 04:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fabc86f2-152f-3252-9a24-5c01790c3e60 | -21.87886 | -46.5526 | 2026-08-20 04:04:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 79007662-6a6f-3e4b-be95-233b97c27bd6 | -17.95898 | -41.93561 | 2026-08-20 04:04:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 37a2dc1c-238f-3659-a224-cc5539ad1f6c | -21.71284 | -47.14473 | 2026-08-20 04:04:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c69596c-a818-384e-b406-b9c4c500a94b | -17.33652 | -43.62815 | 2026-08-20 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 50.2 |
| c71f9b5b-340e-313b-9407-b621fac677f2 | -18.85262 | -47.14248 | 2026-08-20 04:04:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cb76d5b-85b0-32ee-80ee-a027fbc85fb7 | -20.9009 | -50.50759 | 2026-08-20 04:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eecdaf13-cb01-3177-9bc8-d1fddb6f6f02 | -19.717 | -49.12839 | 2026-08-20 04:04:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5695e5c-6730-3e29-af33-abe6cb91a9fd | -18.03463 | -44.62774 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38cbb57a-cbf6-3c14-887a-5ea40077ca93 | -20.29465 | -46.45909 | 2026-08-20 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README29.md)
