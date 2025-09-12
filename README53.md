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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 162679fd-1889-3bfb-8e01-f03f7c76ce00 | -19.09728 | -44.65751 | 2025-09-12 04:08:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd7d2679-5500-3c58-b041-755b7e309e20 | -19.19841 | -48.01359 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d6297de-cb61-341d-b7db-e343c0e2d04b | -21.26946 | -43.86338 | 2025-09-12 04:08:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 5b85e156-1643-3338-9980-3c147eeb881a | -20.35491 | -48.40001 | 2025-09-12 04:08:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2cb4924-e30b-3fdb-a67b-5391747b825d | -17.38403 | -52.9563 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1657e795-e379-34b7-861a-3aef2a3cfc43 | -20.66676 | -44.25932 | 2025-09-12 04:08:00 | NPP-375D | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d57b1610-5b40-3eb9-b724-35210d31df21 | -22.61469 | -46.41589 | 2025-09-12 04:08:00 | NPP-375D | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 116fde30-4ab2-31c4-aba6-01a61dd7b8fb | -23.11477 | -47.50539 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 166c5ce8-61aa-3078-9bb9-11d1ecbdf581 | -23.3802 | -47.23384 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 54966f79-3be0-3e40-a10f-9c6d4561bd58 | -18.65748 | -47.65012 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cb00ac2-8643-305c-88dc-27a415e136e7 | -18.61963 | -48.25802 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e2e18c01-e0e1-3788-8718-674625d9ec52 | -20.01258 | -46.92214 | 2025-09-12 04:08:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 441e1ebf-7fd0-3c31-b75e-81d51287a423 | -20.27797 | -42.88771 | 2025-09-12 04:08:00 | NPP-375D | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4ac5ce4d-a5e9-36d2-8abf-d2736bbef2bd | -20.15042 | -47.38238 | 2025-09-12 04:08:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24e955d6-4889-3b9d-81c5-c78c67f96501 | -18.60361 | -47.18017 | 2025-09-12 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8e28b7d-6323-3888-bfc5-915a2c925c8e | -23.1401 | -47.15236 | 2025-09-12 04:08:00 | NPP-375D | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e6608b2d-5be9-39c4-b75d-12e4d60408f7 | -18.61628 | -48.25322 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1a0da106-9b9d-30cc-b6ab-a1f8676bbcee | -18.34567 | -49.33001 | 2025-09-12 04:08:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8ed048d-180b-30d5-83ee-8a011af11967 | -21.32188 | -45.01048 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e653322f-6af0-329f-952e-db0d89fe6cb0 | -22.65836 | -53.11988 | 2025-09-12 04:08:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8e9b30d3-1c37-30e4-af1c-1798729dcce4 | -19.93581 | -43.87163 | 2025-09-12 04:08:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 62a8c30b-61d5-3911-8027-90d11a799168 | -23.14403 | -49.65917 | 2025-09-12 04:08:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 092ca96e-0069-3a35-94ff-37ecec1b6a08 | -22.65462 | -53.10879 | 2025-09-12 04:08:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8bad036d-3eab-31c1-8b4b-1f11eaa7672a | -19.97462 | -47.59805 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d73ddf7b-f6b1-375b-9aee-fa43125b05cf | -20.11364 | -42.35459 | 2025-09-12 04:08:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| df49ecaf-c306-341d-b9a6-09debe9271ae | -21.70583 | -46.25381 | 2025-09-12 04:08:00 | NPP-375D | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5cf75e9f-228e-3c36-8841-3611150ba60c | -19.99695 | -46.9236 | 2025-09-12 04:08:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22b486f1-1cd1-3d3c-ab8d-cadfe76941f0 | -23.3545 | -47.14698 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6f9406c0-2f6e-3c38-86e5-baab8f5ed207 | -20.20523 | -44.55439 | 2025-09-12 04:08:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fc25f04a-7c0d-33b8-b6ef-bf1af66b5279 | -20.1101 | -45.26812 | 2025-09-12 04:08:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bd1a7a2c-215d-3262-b4cf-72e47df02dbf | -22.18009 | -49.73277 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 8e9757c9-106a-37ce-ba29-02dbc193d83e | -21.19753 | -47.53207 | 2025-09-12 04:08:00 | NPP-375D | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 30.5 |
| a5a8fec6-a38d-3ae5-b46c-f031f0971e85 | -19.7557 | -46.08958 | 2025-09-12 04:08:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46d1fd38-defb-375a-9edb-9b15e90bfaed | -23.14439 | -48.2593 | 2025-09-12 04:08:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a72c1deb-f9b6-3f5c-ae3a-9528cb6423f9 | -19.66554 | -45.85867 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3763367b-154f-31a5-b9cb-a35cfc3622c2 | -21.00138 | -46.0581 | 2025-09-12 04:08:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 32aad2d4-6198-3c04-94e0-6098f157ef9d | -22.45491 | -46.14777 | 2025-09-12 04:08:00 | NPP-375D | BOM REPOUSO | MINAS GERAIS | Brasil | 3107901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| edfa6601-43ec-38c9-a3f0-bdf0601c0617 | -22.3361 | -48.81718 | 2025-09-12 04:08:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f0efb0a-fb98-3878-949c-83c2c6babaef | -21.32594 | -45.00717 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d4ba90bc-5c10-36dc-a6c9-df49aa9fcd56 | -21.96601 | -47.55391 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05f06fa7-e21c-3986-b670-463428711d3b | -21.96314 | -47.54845 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50a2fad3-e64f-3a95-9140-f3c5930689de | -24.16732 | -51.03625 | 2025-09-12 04:08:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ffd66a24-43ce-3357-b7c4-99be773e2aea | -21.62682 | -46.79642 | 2025-09-12 04:08:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a79f6235-a35f-3fa8-8a9e-077d9df2a6c9 | -23.56629 | -45.84828 | 2025-09-12 04:08:00 | NPP-375D | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 882c1278-056b-3ae9-89cb-6462da8892ca | -20.3535 | -48.40741 | 2025-09-12 04:08:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e72aab0f-91c3-3dea-ac82-ef444d933a72 | -21.18535 | -47.53458 | 2025-09-12 04:08:00 | NPP-375D | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 140f639b-e3e9-380c-8fe8-f66f3929545a | -20.00437 | -46.92505 | 2025-09-12 04:08:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9926f504-97e8-3b03-9bcf-58190352f32e | -23.39474 | -46.71292 | 2025-09-12 04:08:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 42fab435-d858-3567-98f4-2b4cb56c836d | -18.8191 | -46.8775 | 2025-09-12 04:08:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7343f78a-0eb0-36a8-a435-9612670a10a9 | -23.39789 | -46.86077 | 2025-09-12 04:08:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 52ade781-fb4e-3654-bf96-18e00158321e | -18.623 | -48.26279 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 78356fd4-9c8e-3603-9023-43844468dc0d | -23.13763 | -46.75211 | 2025-09-12 04:08:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c094492e-7d85-33be-a083-1ad752d30e69 | -23.84253 | -51.07907 | 2025-09-12 04:08:00 | NPP-375D | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b588ca27-3bd4-3e43-90de-3758361668ab | -23.11842 | -47.50618 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| d2440706-6631-3787-9fce-6edd7b9d5992 | -18.62726 | -44.2653 | 2025-09-12 04:08:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad609c4f-01ae-3b5a-8481-e7b66769cb35 | -22.65179 | -53.10091 | 2025-09-12 04:08:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4c3a27b3-5850-3156-b2fa-7d79fef9455f | -17.37417 | -52.9201 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13bea273-c50e-31f5-a02c-94cdf993e3f2 | -22.40265 | -46.75166 | 2025-09-12 04:08:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 1cfc43b4-0bd5-3e38-8241-c0358b3596fc | -22.52413 | -45.0967 | 2025-09-12 04:08:00 | NPP-375D | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| cc13e7b6-0fd0-3153-9dd4-fb47af754af8 | -23.46773 | -47.66236 | 2025-09-12 04:08:00 | NPP-375D | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bc8c08d3-cf62-3a17-8f3e-7a9d58191fd7 | -23.14377 | -49.65265 | 2025-09-12 04:08:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 9e5060a8-c27b-3357-a673-b24f7f4f5953 | -21.96429 | -47.56329 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a0e21dd-f2e9-3e60-a2a4-d93562646212 | -18.97723 | -47.90218 | 2025-09-12 04:08:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25396db0-af63-32db-99c0-946a39eb97f8 | -23.32537 | -46.55109 | 2025-09-12 04:08:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8a819706-4d63-3774-b0b8-88f53822ed7d | -20.17278 | -44.62347 | 2025-09-12 04:08:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be56e45f-6b0f-3795-835c-ccabe3e65713 | -20.98652 | -46.98518 | 2025-09-12 04:08:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58e7106d-f7df-3f0f-9878-5a618f6e7de6 | -18.75278 | -47.61954 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3cfa06a-7404-3434-8e6c-0c0bddf90df5 | -19.95563 | -44.45817 | 2025-09-12 04:08:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d3f285da-ad97-3b0a-94eb-507c824aa337 | -23.43296 | -47.02429 | 2025-09-12 04:08:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 569aaa6f-0350-34c7-8643-f4fe185569c3 | -22.8545 | -47.34458 | 2025-09-12 04:08:00 | NPP-375D | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 156f2f1b-4dbe-324a-8e62-c65d088baa25 | -19.88314 | -41.41457 | 2025-09-12 04:08:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 755d2826-7ee1-34e3-92e3-afadcdeb705b | -18.65646 | -47.65556 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9616bcbf-ede9-3db2-843c-178235cb28b6 | -20.26738 | -42.12369 | 2025-09-12 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| bd9bca10-d30d-31c3-b2d1-82cf6d9e6f94 | -22.522 | -45.08852 | 2025-09-12 04:08:00 | NPP-375D | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2c20c9f6-b9e2-3aff-9630-bebe3c845786 | -22.69883 | -46.22334 | 2025-09-12 04:08:00 | NPP-375D | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 24845e66-30db-3b79-8482-bbb11802a37e | -19.99323 | -47.62706 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50c582c7-9d4f-3bc9-b144-d58e753442c4 | -22.65544 | -53.10876 | 2025-09-12 04:08:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a246bda9-a3d9-31a2-8e02-9a2aa38345cb | -23.71861 | -47.45716 | 2025-09-12 04:08:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 416a8ca7-9a98-3b77-a360-6fdb4d636d28 | -23.28122 | -46.47406 | 2025-09-12 04:08:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e0dac00e-0c87-398c-a3a6-44db9e9b935c | -19.98934 | -47.62648 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f63ef39f-11c0-3052-8d95-730ac6cb4d2c | -23.11029 | -47.50917 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e95c93b1-906a-3cec-84ff-0012fe424e31 | -19.66113 | -44.90686 | 2025-09-12 04:08:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| fac69f1a-2cb6-37b0-bafb-849bec20e98b | -21.32122 | -45.01439 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c6dab22c-103e-30cd-bf1f-36656f182b15 | -22.66857 | -53.12252 | 2025-09-12 04:08:00 | NPP-375D | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 69eca0a0-3d5f-34e1-a93a-2e7b262c1f4f | -23.11272 | -47.50711 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| bd9c399b-a216-3355-997f-b80e424c9314 | -18.648 | -48.14987 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b4a60e5a-5009-3d8e-93e1-c36f2a4c00c7 | -17.83725 | -52.05353 | 2025-09-12 04:08:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cb5a69f-978c-3119-93d5-b3690df6e4bc | -19.64097 | -41.588 | 2025-09-12 04:08:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 551c05ea-8032-3375-be1f-d727167efe61 | -23.65328 | -45.49931 | 2025-09-12 04:08:00 | NPP-375D | CARAGUATATUBA | SÃO PAULO | Brasil | 3510500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc811536-dfd7-3761-8acb-a97e3ca5cbb4 | -23.32248 | -47.3261 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d4603f5d-968a-35e5-b326-9574d973d1fa | -23.49548 | -47.26063 | 2025-09-12 04:08:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 46e21656-32b3-357a-b4ae-d359315d56fb | -22.66564 | -53.11138 | 2025-09-12 04:08:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d19fc58-b117-327b-818c-614b6290530c | -23.3261 | -47.32687 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fc808b73-8f7f-3969-bca9-ec1ed2123d49 | -23.14953 | -47.47193 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 11a7799f-5ba2-3e77-bf06-4f1ccc66170a | -23.3041 | -51.12645 | 2025-09-12 04:08:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0c5c7886-3c26-3c26-bece-b99b4e1eb4a4 | -20.0089 | -46.92125 | 2025-09-12 04:08:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d936a52-7644-3a29-adb0-524897ff7a1b | -20.00066 | -46.9243 | 2025-09-12 04:08:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 19f7cccd-13a5-3623-9f0e-6c551832aacd | -18.67818 | -47.67069 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6dcea6ab-42f5-3b7f-b61a-27b8ad30285c | -22.62544 | -53.09427 | 2025-09-12 04:08:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 4d9c0e11-cf62-3d80-bdd8-13416791c05c | -22.68355 | -45.5241 | 2025-09-12 04:08:00 | NPP-375D | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README54.md)
