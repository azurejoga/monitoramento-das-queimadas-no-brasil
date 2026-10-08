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

## Dados Diários - Página 259

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20947400-f970-3c5a-92b9-45b1ff86a586 | -17.28258 | -43.89762 | 2026-10-08 16:16:00 | NPP-375 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 654ebc99-1c8f-3ef2-a23a-b86961ef8c49 | -14.52904 | -41.67214 | 2026-10-08 16:16:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 399ce5e6-ff01-3be0-97b0-42d13b3c70dc | -14.46025 | -40.81456 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 55d100e5-317a-3439-8ad1-f5643752f74e | -15.8273 | -45.41214 | 2026-10-08 16:16:00 | NPP-375 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 31c6c02d-f9d4-3ca8-9233-1f633774aa83 | -16.48798 | -41.80925 | 2026-10-08 16:16:00 | NPP-375 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| f833660a-4586-3253-8feb-cf3b966231b9 | -16.15391 | -43.11561 | 2026-10-08 16:16:00 | NPP-375 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 89920e68-be10-3fc6-bfc5-dfcbd9282070 | -14.49441 | -40.82381 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 129a82f6-ddbb-3f92-baac-2c8555287e7b | -16.84604 | -40.57646 | 2026-10-08 16:16:00 | NPP-375 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7d5c958f-e7e9-3655-812c-813e9bb5eafd | -16.01257 | -40.66349 | 2026-10-08 16:16:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 4dfc0685-f6a5-3cf5-9d8c-5470a9e8bd92 | -15.40039 | -44.33066 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 51cc8dbd-11c6-3153-9bd8-dbfa6782acb1 | -14.1412 | -40.79249 | 2026-10-08 16:16:00 | NPP-375 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| ee402c45-bf34-3425-ab8c-0ed29efecc7f | -15.39981 | -44.32584 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6abb18a3-3bf7-33c6-9c46-4b253ca7c0e5 | -14.93475 | -48.09578 | 2026-10-08 16:16:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 79d782e0-8520-3103-8a38-3a3307aa6d43 | -20.63992 | -43.32304 | 2026-10-08 16:16:00 | NPP-375 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 156ee664-02f9-3201-b4d5-d51d6744f98c | -15.96616 | -40.69589 | 2026-10-08 16:16:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 240cc302-5978-3638-af66-a2206e7c5605 | -20.08132 | -42.70689 | 2026-10-08 16:16:00 | NPP-375 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| fa6756a0-7053-3878-82ee-14e03fed8b97 | -14.44805 | -43.92706 | 2026-10-08 16:16:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 44.2 |
| fddcd917-e73a-3951-af9e-0a5f20e4b6a8 | -14.07936 | -40.21077 | 2026-10-08 16:16:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 84c6d81b-0549-3b5a-8027-32cc59c2db68 | -17.12376 | -39.51221 | 2026-10-08 16:16:00 | NPP-375 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0cad59ab-44d8-3998-8063-66f8740ea8b9 | -18.98357 | -44.4574 | 2026-10-08 16:16:00 | NPP-375 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 002ee37f-4f28-3333-8b93-df19e1926a2c | -14.62947 | -40.77784 | 2026-10-08 16:16:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 36e916bb-177b-3064-b090-dce67ede41e0 | -17.78559 | -44.00182 | 2026-10-08 16:16:00 | NPP-375 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9b97e93-697e-3fb1-b924-e7aaf81b5a33 | -14.78924 | -42.83191 | 2026-10-08 16:16:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 5448b5d1-1512-34ec-87ca-d23c5a72814e | -18.05478 | -44.59642 | 2026-10-08 16:16:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 05af7c07-9b0f-36e5-814c-fdf5030cc680 | -15.51268 | -42.65399 | 2026-10-08 16:16:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 78adb010-ab0d-389d-90c8-07aec32a430d | -18.04928 | -41.66817 | 2026-10-08 16:16:00 | NPP-375 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 481559bb-c0f7-397c-a347-2a1062fb6ef6 | -14.73693 | -40.29145 | 2026-10-08 16:16:00 | NPP-375 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2aafbe76-1bbd-39e2-bf49-3d2bea61780f | -20.58584 | -48.46157 | 2026-10-08 16:16:00 | NPP-375 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8fd61969-777a-37c5-b0c4-b88114b70364 | -18.5533 | -43.62682 | 2026-10-08 16:16:00 | NPP-375 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 07733c70-244c-3050-ad08-dd3060083c64 | -15.95664 | -41.0989 | 2026-10-08 16:16:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.0 |
| d4115901-0efe-3a87-b885-8f3609d420c1 | -15.57435 | -44.53121 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| f1717f25-ed32-3f08-bff4-b8c71aca6741 | -16.35301 | -44.72064 | 2026-10-08 16:16:00 | NPP-375 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| db47fa36-b361-3690-af79-a6644d9316be | -17.11435 | -41.34228 | 2026-10-08 16:16:00 | NPP-375 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 1582d17b-aa36-3550-b5ed-c9ad96583e15 | -15.03863 | -42.49556 | 2026-10-08 16:16:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 413f6904-0662-3c5a-8289-c822a8ada384 | -18.35712 | -42.77049 | 2026-10-08 16:16:00 | NPP-375 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.7 |
| 5c01e207-2f04-369e-814c-26a680e4419f | -15.1274 | -41.38377 | 2026-10-08 16:16:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 223.7 |
| 19cdcf04-f731-3472-a328-cfe462161ab0 | -14.43843 | -40.79179 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 521b1c0c-221b-310e-8b10-6cf7f4c45db6 | -16.74203 | -40.43397 | 2026-10-08 16:16:00 | NPP-375 | PALMÓPOLIS | MINAS GERAIS | Brasil | 3146750 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 8e6e6c7d-3e3b-3272-9b59-d6d79935bdfe | -15.51727 | -42.65702 | 2026-10-08 16:16:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 83b1722c-1246-3364-b978-2b3b74c72148 | -18.81402 | -41.88902 | 2026-10-08 16:16:00 | NPP-375 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b9a52340-33eb-3c7c-bd23-f49aff61cdf4 | -14.46389 | -40.81397 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| c26ee5f5-2d80-3721-8a6d-236c7d4809a4 | -14.52495 | -40.33329 | 2026-10-08 16:16:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d1c0a0a6-4ac6-3624-85d2-a2c63030f8f0 | -14.58529 | -40.72711 | 2026-10-08 16:16:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 17e4602a-ca6c-3d89-bd76-1141c0b1246e | -15.70688 | -40.59531 | 2026-10-08 16:16:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 00d84e15-0118-3317-8c24-838a7fe73c7d | -17.96153 | -47.70275 | 2026-10-08 16:16:00 | NPP-375 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 13edb0d9-aefd-332c-abfd-9e976a4dd89d | -15.55904 | -44.52259 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f0a66cd4-173a-3ab1-8e59-f56323ba4e0a | -16.0024 | -50.03977 | 2026-10-08 16:16:00 | NPP-375 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a16a654-b963-33a7-a932-82fa01b7ebbf | -16.15704 | -43.64016 | 2026-10-08 16:16:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b62a1328-2687-32cd-8a23-3b05f55aaf81 | -15.1338 | -44.05664 | 2026-10-08 16:16:00 | NPP-375 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9784b036-3ca3-3e18-8f1f-83dc8bb9c4e0 | -14.91784 | -48.10436 | 2026-10-08 16:16:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5eb06e49-2252-383f-acfc-854c73ca4c33 | -14.79461 | -41.61374 | 2026-10-08 16:16:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| e0ffc79d-7a63-3ca7-871d-7be3c37b9725 | -17.33885 | -41.38516 | 2026-10-08 16:16:00 | NPP-375 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 45dd0fd9-bc05-3560-ae5e-be10f23b6f1b | -15.60976 | -41.78032 | 2026-10-08 16:16:00 | NPP-375 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 647c4d70-a388-3727-bc80-6a1514984624 | -17.95775 | -42.77351 | 2026-10-08 16:16:00 | NPP-375 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 5bd9f1df-668f-357e-883e-f74a623dd1bb | -16.12712 | -43.74721 | 2026-10-08 16:16:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 27.8 |
| d0704592-e0e9-34a4-ae75-351043d4ecdb | -16.51097 | -43.14506 | 2026-10-08 16:16:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3e67718c-7417-38e6-b25a-2ca63e3a6b89 | -14.55978 | -44.07202 | 2026-10-08 16:16:00 | NPP-375 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 2a6ba132-01da-3321-b6a4-3386ba0f30a4 | -13.85295 | -40.64275 | 2026-10-08 16:16:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e88c31ac-6169-37a6-a837-1b45ff03dab2 | -14.73507 | -40.29523 | 2026-10-08 16:16:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 543c27e5-23a6-3264-8dd7-8811dfaeab36 | -17.84888 | -42.16432 | 2026-10-08 16:16:00 | NPP-375 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a34555c8-31b7-33e1-a263-827b1a7cb55e | -15.62718 | -40.12988 | 2026-10-08 16:16:00 | NPP-375 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 738b589e-46f1-3d06-8303-60c85cd7f18a | -18.82538 | -46.92818 | 2026-10-08 16:16:00 | NPP-375 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a8a4089f-676a-35e0-ae44-40d936985aa4 | -16.93933 | -42.07863 | 2026-10-08 16:16:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 309c3791-877b-3e61-b674-8bc5160c0d64 | -14.75583 | -39.81377 | 2026-10-08 16:16:00 | NPP-375 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 89fb28c5-ee9e-327c-831d-2bc20e4d9320 | -15.6015 | -40.50654 | 2026-10-08 16:16:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 44f8efa4-f4db-3efd-883d-1c28a7733b35 | -18.26211 | -42.17894 | 2026-10-08 16:16:00 | NPP-375 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| de5262a0-9d81-3f3a-abec-77000b330491 | -14.42595 | -41.13671 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c91b837c-2edf-3aac-bd64-433ad9ee66f8 | -14.73448 | -40.29113 | 2026-10-08 16:16:00 | NPP-375 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| b23371e1-69e7-352f-8602-3fbf7e762905 | -14.41502 | -41.28871 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 1df3e94c-71bb-39c0-b954-e46a43a5bf32 | -14.68192 | -43.12716 | 2026-10-08 16:16:00 | NPP-375 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 70dd43a9-99a9-322d-8aee-53ab74af5229 | -14.61789 | -41.74006 | 2026-10-08 16:16:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 43256601-8b60-33b5-9fa2-8aeb0368312e | -14.73635 | -40.28734 | 2026-10-08 16:16:00 | NPP-375 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| d671a73a-dfc5-32d5-a7c6-6522f5933b7a | -14.56036 | -44.07655 | 2026-10-08 16:16:00 | NPP-375 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 54e104fc-d5d8-3a27-ae9c-53d834e8a9b3 | -15.35013 | -39.64433 | 2026-10-08 16:16:00 | NPP-375 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3a374bcd-1bd9-3159-b846-101c54ca0081 | -16.20402 | -41.37234 | 2026-10-08 16:16:00 | NPP-375 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a12d1e1f-fc88-34b8-bab7-f1f0699f910d | -15.03815 | -42.49188 | 2026-10-08 16:16:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 0b05161a-05c8-3ada-8937-44415ce2152a | -15.20253 | -47.97967 | 2026-10-08 16:16:00 | NPP-375 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 440f6602-76ce-3984-8188-c4c2b664fd55 | -16.92685 | -42.11064 | 2026-10-08 16:16:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 757ff567-3dbb-3c4f-84e0-d97ecdfb15f0 | -15.54503 | -43.1735 | 2026-10-08 16:16:00 | NPP-375 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 21.9 |
| ebc1b450-6b5c-3bb0-ac9c-a1e21a6c1248 | -17.94543 | -42.31832 | 2026-10-08 16:16:00 | NPP-375 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 73de0512-eeee-347c-8404-93da974d6914 | -14.49535 | -41.89926 | 2026-10-08 16:16:00 | NPP-375 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 91d9fdfe-6c40-3893-b45c-bffff2461635 | -15.68315 | -40.77793 | 2026-10-08 16:16:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 1bfd82e1-cb59-3634-9b9f-0caeaf54e852 | -14.4662 | -40.72628 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 1c8f6dfc-444c-3fe4-8538-5dff3811910f | -17.10729 | -41.34872 | 2026-10-08 16:16:00 | NPP-375 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.2 |
| 41281fae-4c4b-3b3b-a33e-32455e7ba913 | -16.4524 | -41.27168 | 2026-10-08 16:16:00 | NPP-375 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 42eb283f-6445-3d60-9d2e-a258be2c5f4e | -15.60585 | -41.78093 | 2026-10-08 16:16:00 | NPP-375 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| a66eb5c2-729b-3ed6-b894-d94b6e098b3a | -14.9696 | -48.19394 | 2026-10-08 16:16:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 34a8b20f-1f14-3fc1-ac8d-f4665daa1e76 | -16.85229 | -40.56666 | 2026-10-08 16:16:00 | NPP-375 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| d452c7dd-e72a-3f23-bcdb-ab566f463d4b | -14.34425 | -42.0145 | 2026-10-08 16:16:00 | NPP-375 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| e07e53c1-9b53-3222-824c-8be564e9b572 | -14.76577 | -39.80837 | 2026-10-08 16:16:00 | NPP-375 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 83756a6a-187b-3a5a-bfa2-ccbc519e0145 | -17.85526 | -41.54049 | 2026-10-08 16:16:00 | NPP-375 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 1e3c1fed-6ea5-3c40-bf7c-43ad69625e83 | -16.49195 | -41.80872 | 2026-10-08 16:16:00 | NPP-375 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 52df75d0-ecb8-3110-9278-9cb36b617660 | -14.95555 | -41.79545 | 2026-10-08 16:16:00 | NPP-375 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 83f3ebfa-22fd-310a-8a3c-975d90294d3e | -16.91143 | -40.89314 | 2026-10-08 16:16:00 | NPP-375 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 831ced74-4ddc-3de7-bf2f-40de7fc7f120 | -14.96581 | -41.52105 | 2026-10-08 16:16:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| dd4c7f3d-19c0-314e-b568-e5d7e3115d73 | -15.65543 | -47.8311 | 2026-10-08 16:16:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4381aace-3777-3e16-99f1-bbb7508d5196 | -16.84862 | -40.59562 | 2026-10-08 16:16:00 | NPP-375 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ebb451c2-af7a-33a0-9484-be34571e3ec7 | -15.57373 | -44.52613 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a025b9f0-a292-35f5-920d-feaf0bf937d1 | -16.7633 | -40.9916 | 2026-10-08 16:16:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| ea44fc2b-a640-3543-87d9-45251409abaf | -20.59179 | -48.45542 | 2026-10-08 16:16:00 | NPP-375 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |


[Clique aqui para ver as próximas entradas](README260.md)
