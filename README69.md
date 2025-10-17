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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73656e29-8d7b-3002-8581-6fd68e00beac | -11.97753 | -46.55533 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1afd91a-8a71-3757-a140-6edc0a13146d | -14.15422 | -44.31482 | 2025-10-17 04:21:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a48d7a2-29f3-3c59-a6a3-1ffcbf8f1a96 | -15.57765 | -44.426 | 2025-10-17 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dcb54cea-e3c7-39a8-834e-4ecd3c899f49 | -12.43512 | -51.30619 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc130182-6c9f-32c7-b57d-4999a9c172c8 | -12.17261 | -45.06558 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 899229fe-4474-37a7-bab8-aabfba9c05be | -16.55123 | -52.43969 | 2025-10-17 04:21:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d42eb08f-ed3b-38fa-836c-113dd83226b5 | -13.3884 | -47.20829 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 416c2f30-28c0-3f23-a399-c0e6fac8c2b6 | -14.93724 | -46.71498 | 2025-10-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53443c76-db8e-396d-a060-9c19fa76edd3 | -13.43163 | -48.60482 | 2025-10-17 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e9a9b83-145a-3e1b-ae25-53b1ef3025a6 | -13.93474 | -48.69314 | 2025-10-17 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5a6618b-1282-3ab6-9f6d-03162088a3fb | -12.16154 | -45.07118 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83f63572-ede5-373d-bd83-61cb83fb5214 | -17.35703 | -39.42267 | 2025-10-17 04:21:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ef3aef72-8476-37c4-b124-99885a3c9bb2 | -14.23558 | -54.89943 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e250fcc-11ec-37e1-b89f-06ff656e79c4 | -12.96805 | -47.09039 | 2025-10-17 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 765439ec-6fae-3c73-8940-00d401daa0a7 | -14.33171 | -51.42574 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca31693d-61ff-3ec1-8c51-97d6f717dfde | -14.33433 | -51.44055 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| b34b9d4e-b3b0-33f9-ad05-348b7427206e | -15.03039 | -47.30734 | 2025-10-17 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c533c5f3-662d-3ba7-bdbf-08f4730382d7 | -12.78583 | -44.87914 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62fb9695-6a5d-3b2c-ba99-3cbf53f7bd65 | -16.69194 | -52.89073 | 2025-10-17 04:21:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8c5dfdd-d62c-3757-b27b-c01f05b319d2 | -13.26043 | -47.11359 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e4246d44-00ea-3024-b742-6adb486e6f69 | -12.29724 | -47.11193 | 2025-10-17 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa7b239f-afa7-3843-9bc9-7cfd2e6c2600 | -14.9378 | -46.71144 | 2025-10-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 76f251fc-d06c-3081-b456-7e6be5655ab3 | -12.43577 | -51.30254 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce849c8e-17b2-3a99-9200-f0ffc2738e41 | -12.06097 | -47.98355 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 912818c9-12f2-3ad3-abc7-25eee0e21219 | -13.7321 | -48.21442 | 2025-10-17 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cb577c1-257b-3cc4-8bf1-bcda1b4338af | -15.05175 | -46.61377 | 2025-10-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f93b033-289a-335a-a91b-e4d3bb09d182 | -15.04526 | -52.99112 | 2025-10-17 04:21:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 163e2469-8e27-38a2-ba52-002978338ea8 | -14.23987 | -54.90157 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bed2c30f-225b-3204-9196-d462eac057b3 | -11.06187 | -47.59827 | 2025-10-17 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| defb8cda-9778-39e5-8edc-c30c6e9a59b3 | -16.77467 | -48.81145 | 2025-10-17 04:21:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d32a601-712d-3316-9883-9e9a4e7533f2 | -11.95472 | -45.35366 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| da5e89ac-8d4d-3833-8696-24c6559c42d5 | -13.74228 | -48.2163 | 2025-10-17 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7851024-578e-3777-8f34-caa95981dbc5 | -13.45061 | -44.28743 | 2025-10-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc06602f-3804-3ec3-814d-e24eef4f5d30 | -12.96038 | -47.9426 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 462a99f2-4bdb-3ec0-9eb1-b0b15a5b8167 | -11.35975 | -45.26571 | 2025-10-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 161c5a19-104b-3e41-8497-82ddb4edb197 | -11.36239 | -49.2561 | 2025-10-17 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28a29f81-2cad-38c7-b36a-43babbed7cce | -12.77635 | -44.87394 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df1909dc-ef2f-39f5-bd41-9ade75ef0747 | -11.18711 | -51.75701 | 2025-10-17 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4b769ed-3aaa-35cb-8991-8680de8eb674 | -14.32853 | -51.45035 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| df7604fa-4145-3050-bc76-ef3015b89b59 | -11.47869 | -45.09028 | 2025-10-17 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8bb6bdd-0d2a-3339-bbc6-b63036c7b80e | -14.35292 | -51.46671 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13b90da0-e196-3bfb-af51-7a0363dd8ead | -14.99554 | -42.64349 | 2025-10-17 04:21:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ec6dc571-55b4-3db1-a41a-88ddbbb0ebda | -13.69079 | -44.67036 | 2025-10-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbd77dec-7220-3e8c-a6f1-38b4dacdb55d | -14.3339 | -51.45868 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 87005d0f-0ea4-33f0-b2fe-7d2445e366fa | -13.24149 | -47.1253 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd8cbd81-e2a4-3d01-ae2e-1c10186945da | -12.78083 | -44.88944 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 24508080-6312-3992-92f3-2f8c66f9e5b3 | -14.23884 | -54.90905 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a29d20e8-a0d2-3136-8829-26448ac6567f | -11.5438 | -49.9235 | 2025-10-17 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df9a5ae9-f175-338e-b530-5210e1c93ce8 | -12.17538 | -45.06969 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5bd0c65-acbd-3e97-97ad-01415c4b512f | -12.16432 | -45.0753 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c204509-b799-33bf-8070-e1b31580c6b6 | -13.5775 | -48.49043 | 2025-10-17 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd550f44-eb7c-3035-bc85-4c726fc439da | -14.33737 | -51.44655 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5d80a12b-75a0-34c9-b98e-df26e1f71278 | -12.04539 | -54.2462 | 2025-10-17 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 330ff5de-9cd0-3dea-bbfd-c0aa157e5c2e | -12.77969 | -44.87447 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8063699c-509e-3bba-b03b-428fca61fafd | -13.24497 | -47.10368 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f9fe906-5b5e-3944-881a-6268fbe99571 | -17.96994 | -39.88306 | 2025-10-17 04:21:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 32fa8382-cdcf-3c8e-b3b2-fe1dccc700d1 | -14.3404 | -51.46803 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 9b57649c-8841-3256-985f-664c4c6b428e | -13.04141 | -43.22083 | 2025-10-17 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e4a734fd-5a00-3e9b-9f81-ba5c8987decb | -15.78421 | -41.49103 | 2025-10-17 04:21:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d04e1595-23b9-3621-aec4-96a41ee02c1d | -11.78329 | -43.73955 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 475d278b-5843-3868-8874-5aa2b3fba339 | -11.54211 | -51.40191 | 2025-10-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41eb0713-d766-3c6c-a111-c7d5b17a165e | -11.61656 | -48.78742 | 2025-10-17 04:21:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04eed4eb-c38e-3df9-940c-eeb275f2b7dc | -13.27698 | -44.48533 | 2025-10-17 04:21:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1e5dd4a7-f752-39dd-911d-b7df9222158b | -11.5641 | -46.90615 | 2025-10-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 817a49f4-95f5-3b8c-9afb-5cf862a4b2c0 | -12.78807 | -44.88688 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15781730-4719-36d6-bcec-0b5ae594af76 | -14.34133 | -51.44728 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.5 |
| aefc9076-58c4-3ffe-aef1-83fce798603f | -14.9319 | -48.53006 | 2025-10-17 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c338c72d-fee0-3dca-80ab-04697d3a6a68 | -18.21592 | -46.05839 | 2025-10-17 04:21:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 676a241d-e962-3897-8b29-08cc3244cfdf | -10.98151 | -47.8989 | 2025-10-17 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c0f4f59f-87a5-3623-94ad-d68abd1323ec | -14.33376 | -51.43695 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dfc0b914-0a27-35e3-aee9-e4c865c7b9ba | -16.81029 | -53.92271 | 2025-10-17 04:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e1762181-ea17-3e56-8bb6-32ba081e1714 | -16.39981 | -41.95542 | 2025-10-17 04:21:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 8d0ddb74-d09e-30ad-a88e-b958fb4d03c3 | -12.7719 | -44.88064 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bd9d791-6d1d-3623-8021-59d685476012 | -13.73735 | -42.51674 | 2025-10-17 04:21:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 51b4c038-359f-37c7-af49-48942c2846ba | -18.73219 | -47.46391 | 2025-10-17 04:21:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f151d98f-4686-3414-8949-43e2f54d0da0 | -14.8701 | -52.43252 | 2025-10-17 04:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6ea916c-69bd-3d38-83cb-6e256af90a48 | -11.58748 | -44.0645 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4f38f9e3-61a5-3839-870e-1f8f91099406 | -13.51129 | -47.16328 | 2025-10-17 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31df909f-efcd-3e67-a1c9-d2d517f529de | -13.27673 | -43.13748 | 2025-10-17 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 238ff4c7-c6dc-3eca-9a58-10517490c189 | -14.72008 | -48.30061 | 2025-10-17 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5eb0f7a-854e-320c-9160-2113ab1ba214 | -13.4425 | -47.9657 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f26d6c5c-fe98-3e0a-95a2-3ba8a9ecec08 | -10.97962 | -47.91052 | 2025-10-17 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db2b5bc2-fff5-3fa4-a702-8db8e5c2c3fc | -11.59315 | -44.07298 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0651383f-7724-3ff5-860e-66d4d128011e | -11.86197 | -44.73837 | 2025-10-17 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecd7f02b-d66d-3765-b90c-51dc51c20a71 | -14.33185 | -51.44744 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 434d604e-4264-3c68-b4cc-d04f672d54d2 | -13.0195 | -43.83913 | 2025-10-17 04:21:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06d2b6af-6aa6-3b2d-89c2-c1f6863c4d6c | -12.14079 | -43.26845 | 2025-10-17 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76c79080-329c-3b16-964c-3e70c72ec937 | -11.59427 | -44.06556 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1afe11e8-8535-34cf-8160-d74a7bdb784b | -12.43237 | -51.29817 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92c85be6-a40a-3dd2-9392-0dca4b2227e9 | -15.78431 | -43.65125 | 2025-10-17 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce55541c-ae08-3463-bea2-1322432e8185 | -10.10347 | -56.76979 | 2025-10-17 04:21:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9e08206b-14fd-3416-a28d-a05e0f754f72 | -14.17231 | -47.93629 | 2025-10-17 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0a12baca-b9df-3fbb-9e0d-e6ceb63fc321 | -14.87281 | -52.44133 | 2025-10-17 04:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f9f62f2-88c3-3c75-8f7d-ee13ffd7066e | -15.06104 | -46.61892 | 2025-10-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 757f3da0-6ebc-381d-ba75-605fff53ccd4 | -12.43635 | -48.70839 | 2025-10-17 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e75d861-4934-37b3-934b-ec26d93d0172 | -13.43021 | -47.95593 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c549e916-ec04-31cd-9359-f148acc3ca74 | -12.16376 | -45.0789 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7bcad5e-5664-3df3-82ad-78eb808a5265 | -16.19873 | -43.68246 | 2025-10-17 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25aa5f86-d703-3f36-afe0-1c875e6f964c | -10.95012 | -49.77729 | 2025-10-17 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| b5df36b3-28d9-3149-a934-028b04f4e5fa | -15.02651 | -47.31038 | 2025-10-17 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README70.md)
