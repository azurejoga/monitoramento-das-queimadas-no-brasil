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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84fc7ebb-95c9-3945-8f55-c6a2eebcbfbf | -15.05554 | -56.39286 | 2025-08-23 05:23:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7fa45057-c5c5-3487-93a3-3f62b2ab23f9 | -25.57355 | -51.0592 | 2025-08-23 05:23:00 | NPP-375D | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 8029fc31-be97-3bee-a8a8-e74438d0ee37 | -17.88368 | -53.20427 | 2025-08-23 05:23:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 436269ac-1d37-3d0d-800d-26a23ba31e7d | -14.77424 | -59.65879 | 2025-08-23 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2592ee69-5af3-3b1f-b46e-311f66b5cdbd | -15.03294 | -56.38462 | 2025-08-23 05:23:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a24ee367-2bfc-33bc-8668-70371d212483 | -14.8123 | -59.63509 | 2025-08-23 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d2d7154-d78d-323f-ad53-ff2466daffcb | -14.81341 | -59.6278 | 2025-08-23 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 536fba26-28c2-356a-b0c9-710b6a7a5b1e | -25.56962 | -51.05585 | 2025-08-23 05:25:00 | NPP-375D | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 52457c77-05e5-3b53-a30d-b61a35bc1298 | -23.74401 | -51.1032 | 2025-08-23 05:25:00 | NPP-375D | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 702f033e-c324-3b2c-a14a-047ab2250ecf | -25.57543 | -51.06158 | 2025-08-23 05:25:00 | NPP-375D | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7eb90a4a-8e3c-3268-bcad-8fed46db0352 | -23.7379 | -51.10302 | 2025-08-23 05:25:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1c28828a-57c7-31b7-ab0d-2c5073868b27 | -25.56922 | -51.06116 | 2025-08-23 05:25:00 | NPP-375D | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| aee8cb74-d55e-3ee8-a16e-4f88aa657f09 | -25.57582 | -51.05646 | 2025-08-23 05:25:00 | NPP-375D | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e7ad4571-3b59-34a3-a571-f2e0dc5aa192 | -9.9492 | -60.2141 | 2025-08-23 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f14093a1-d787-3b68-bc61-ddb9301e1e57 | -9.9681 | -60.1743 | 2025-08-23 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| b6d50b6c-9503-3a0e-ade7-2996b965d511 | -9.9678 | -60.213 | 2025-08-23 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 1b554b40-660b-3c06-854e-a6d76a63b766 | -17.5979 | -46.5715 | 2025-08-23 05:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 46.7 |
| e38a2fbd-c161-3c39-b381-7ba47985bff5 | -12.9921 | -45.2252 | 2025-08-23 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| d1efbd4d-b536-3b68-a721-f313bc650af0 | -5.7615 | -57.5807 | 2025-08-23 05:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e8b77518-790f-3fbe-9b1d-06a53db2bcf1 | -9.9493 | -60.1947 | 2025-08-23 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 227.5 |
| 55ad8455-2ea8-3645-87cc-098a073eeb4f | -5.7431 | -57.5814 | 2025-08-23 05:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 89602790-46ec-3667-99fb-83ba3791ba97 | -9.9495 | -60.1754 | 2025-08-23 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 28c54ffd-9b4e-3227-bb3b-56c41cb88283 | -15.0761 | -48.4957 | 2025-08-23 05:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| c59f529f-03ae-3555-99bd-742b38aeb9a0 | -15.0756 | -48.5181 | 2025-08-23 05:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 49e8369d-1316-3660-a9e5-730b46b98010 | -12.5418 | -45.6189 | 2025-08-23 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| baaf74f3-cca7-39de-8cf0-d543c44e518e | -5.7429 | -57.6009 | 2025-08-23 05:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 5033a8f3-8278-3073-8529-744f2ab849d4 | -5.7614 | -57.6002 | 2025-08-23 05:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 0f521102-7a82-323b-87f8-354d25ca9ea7 | -9.968 | -60.1937 | 2025-08-23 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 201.5 |
| 9fe5c9e5-a4e6-3dfb-810a-7ed0804fdb38 | -6.6044 | -44.5624 | 2025-08-23 05:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| bb3fe4e9-0316-30d7-ad42-dadd3ce3b7a6 | -17.5985 | -46.5481 | 2025-08-23 05:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 6250bea9-0e5e-38e2-8e53-490154676aab | 3.79619 | -60.96077 | 2025-08-23 05:38:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d587a41-9aaa-393e-a90d-b72f6bc6dcfd | 3.80739 | -60.9201 | 2025-08-23 05:38:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 705519b1-4dae-3043-b710-ef49091d1991 | -9.9681 | -60.1743 | 2025-08-23 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 09d9ff9c-5b36-314f-8803-87ee9a99e073 | -5.7429 | -57.6009 | 2025-08-23 05:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| d4d8ed38-c59e-390d-9bfb-e636283a3703 | -9.968 | -60.1937 | 2025-08-23 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 6a27fc11-02c8-36e8-a120-dff27a022dd3 | -5.7615 | -57.5807 | 2025-08-23 05:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 82cb3468-081e-300b-a3f4-dc9a78a6b9ba | -9.9492 | -60.2141 | 2025-08-23 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 58ae7fbd-2545-3982-ace9-46e365f81389 | -12.9921 | -45.2252 | 2025-08-23 05:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 3741bf6d-d3be-35d2-82dd-6387ca670d09 | -15.0756 | -48.5181 | 2025-08-23 05:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 28a8bf1a-43d2-3c37-898e-bd83df7f1201 | -9.9678 | -60.213 | 2025-08-23 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 77919554-9212-368e-9024-769c9621ae69 | -17.5979 | -46.5715 | 2025-08-23 05:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 36b99651-9bed-3093-8faa-4dd07aa028b1 | -5.7431 | -57.5814 | 2025-08-23 05:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a99be20f-a6ac-3c08-a12e-d2c3e4c25366 | -7.0352 | -44.6396 | 2025-08-23 05:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| fc8718b1-091e-39a1-9430-5d774550dfc9 | -5.7614 | -57.6002 | 2025-08-23 05:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| bcac6ed1-bd7c-3b49-ae30-cb4877f647a5 | -9.9493 | -60.1947 | 2025-08-23 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 185.3 |
| ce2d01b6-2951-3b55-b458-088ce9326b58 | -17.5985 | -46.5481 | 2025-08-23 05:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 77eb86f0-e10f-346d-919a-d088957b5f3b | -9.9495 | -60.1754 | 2025-08-23 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d7a612bc-1928-3d7f-acca-14491a238021 | -2.93349 | -53.6963 | 2025-08-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9294e02c-84b8-3524-957b-8862d2072db9 | -1.69823 | -55.1933 | 2025-08-23 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ac52f3f-13f3-30b1-b333-1991d8d03b46 | -1.69875 | -55.1899 | 2025-08-23 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b26f9afb-be4f-3186-a0a2-0531eb688948 | -2.93284 | -53.70075 | 2025-08-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b5ec4f9-ed8a-348b-9721-47beac44779d | -3.55182 | -62.07862 | 2025-08-23 05:40:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2017f1e0-f7de-3356-9534-972bb592cee8 | -5.1431 | -60.37915 | 2025-08-23 05:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f58431d7-0c9c-324b-872b-dcf2d9c8c405 | -5.88942 | -53.63709 | 2025-08-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e4c53dc-b7bd-3df8-8113-0eb33c3985f4 | -2.92748 | -53.6954 | 2025-08-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26e877dc-f9e5-36fe-85bf-509c2d922c50 | -6.06196 | -53.87889 | 2025-08-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96762e4e-a1df-3bb8-9ab5-b61fe4d2f745 | -5.87827 | -53.6252 | 2025-08-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e05775e7-9802-3dd8-b5c5-8205d3852dde | -6.05508 | -53.88293 | 2025-08-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3eaeca8-3fcf-38a4-91e0-b082f66c40e9 | -4.23039 | -54.92872 | 2025-08-23 05:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84c0dedb-c7c9-3a97-8fc2-83d4758dad2d | -5.14782 | -60.37471 | 2025-08-23 05:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ded984b-d6f7-35ee-bee4-30abb254ab30 | -5.87758 | -53.63015 | 2025-08-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c38e263d-73c6-3872-9602-be684d349e9c | -5.82964 | -52.07515 | 2025-08-23 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 486cf115-512d-38ca-86ce-16f663f02d34 | -2.93033 | -53.70263 | 2025-08-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c857f44c-b6e9-34da-a5c4-9597ee8fe0fb | -6.06061 | -53.88863 | 2025-08-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67142123-6c64-3b49-8c1e-baa808427d8d | -6.06128 | -53.88378 | 2025-08-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6cb5089-9022-35b2-aa18-ff8b83add59e | -1.55499 | -54.54447 | 2025-08-23 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2814082-d01a-33e5-9991-158bcbcbb30b | -5.87895 | -53.62024 | 2025-08-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90cdb299-7915-3e3e-a90c-14cad94358c2 | -3.13458 | -58.04626 | 2025-08-23 05:40:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab8439e9-1cef-3d20-8a13-73905d2cd6fc | -2.93101 | -53.69818 | 2025-08-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bd52d904-9467-31c2-8814-009b2df26358 | -6.27788 | -52.82889 | 2025-08-23 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dda348f6-18cf-3cab-a3ae-049e548d76ea | -2.92684 | -53.69986 | 2025-08-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3215485a-20b8-3ee1-8aa7-5f301a65451b | -4.23097 | -54.92478 | 2025-08-23 05:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 842fc47f-cb0b-31f3-bad1-97cb8f6a8010 | -5.83054 | -52.06872 | 2025-08-23 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3faba04d-a832-3ed0-ba63-374780d20a9d | -6.06746 | -53.88474 | 2025-08-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da5be5be-8d94-3624-a350-d9e64d19c33c | -4.55841 | -55.96657 | 2025-08-23 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b21a061a-91c4-35d8-8824-62d9d87e935b | -3.13527 | -58.04184 | 2025-08-23 05:40:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ceae738-ece7-320f-95b6-4c7f1d2163d4 | -1.55557 | -54.54063 | 2025-08-23 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d9ef21c-0226-3897-8ae5-77eb0e5d5619 | -4.91384 | -62.3231 | 2025-08-23 05:40:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7048c12c-ede9-3ac4-b59d-cd249c6c3bcf | -2.93219 | -53.70522 | 2025-08-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 839a50e7-63d8-34aa-825d-212157a2b8c2 | -8.87969 | -62.43925 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 647b0471-628e-36da-8723-30290a72352d | -7.04468 | -59.83479 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7117b02-a99a-3657-a8cb-8740258cd256 | -8.88032 | -62.43491 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6db10c3-7ac7-3400-ba2c-6b2c398b59e6 | -8.88844 | -62.40495 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b9fc459-68f3-3d76-ace1-77c0b265daed | -9.16663 | -59.60349 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98b551ea-9223-3b0b-ba05-c1b463c3c0bd | -9.17417 | -59.70861 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| efd32e7b-e906-3156-a865-12d6c2186809 | -7.05311 | -59.83596 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7db5bbea-fa08-38b8-b8b2-da97003a9fb1 | -9.38662 | -60.50896 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69552aaa-ac2f-3aae-bdfb-ad24d8283f68 | -7.73545 | -67.0727 | 2025-08-23 05:42:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e1066f2-1cba-35d5-8453-9de07bf4795b | -8.86439 | -62.39462 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64f12c2c-d08e-3a88-8148-b273fae7f468 | -9.94904 | -60.17726 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27d7c4ec-cb4b-3e78-aec1-66419f347d1e | -9.94213 | -60.17765 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c1d5318-1cf9-310f-bf84-cfdfc18cb0d5 | -9.20444 | -59.45465 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2200204-55c0-3a05-a8d3-3a3226637fc0 | -8.87517 | -62.42292 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 099e83f7-8fca-3c9e-becd-0081eeae1453 | -9.1955 | -59.45348 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a679c92-9465-34ac-8abb-7d01e09c8195 | -9.23013 | -59.7555 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a28d164-1b5c-3d93-8b6e-8ccfefd1852a | -9.16486 | -59.67826 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e013fe5-472b-3057-9056-c3b17cdc94b5 | -5.87296 | -57.75519 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 297c8c4b-9597-3678-a415-b65ad13904a5 | -9.52655 | -60.55166 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53ee7616-d5b5-385b-a933-946772cb1bf7 | -6.13398 | -62.62023 | 2025-08-23 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ab7d751-1eaf-35d2-b085-0a549fda836d | -9.23073 | -59.75125 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README74.md)
