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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7961253f-0d3d-3b1d-ae30-10b0b66cd4e0 | -17.791599 | -43.276699 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b98880d0-9096-352f-a588-7c106d88c688 | -17.795 | -43.292999 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a3780569-5ce7-3e87-85f6-830c9c586b18 | -17.7966 | -43.301201 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a14b9fcb-9120-3546-997a-70d7ef273228 | -17.811199 | -43.2724 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e9ea0832-75ab-3487-b61c-08632bcf658e | -17.803101 | -43.2827 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6486faa0-e5fc-3662-929a-b28d0c725e0d | -17.8064 | -43.299 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4eb4bafa-daef-3c70-9f4a-bf1977e25dfa | -17.8081 | -43.307098 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cce33800-0ab7-3f27-b285-5d46f599e83d | -17.793301 | -43.284901 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 688fdca4-c4c7-3c28-bb8d-d1e0864e7927 | -18.052401 | -44.363201 | 2024-09-28 00:11:25 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b830853c-2c29-31a1-8ecc-656f33f5e287 | -18.054199 | -44.372398 | 2024-09-28 00:11:25 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3a516355-0da2-336d-9f2f-1ba0e56537dc | -18.056101 | -44.381599 | 2024-09-28 00:11:25 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b925b2be-4eb8-3774-81c2-a953e45f122d | -18.0445 | -44.3745 | 2024-09-28 00:11:25 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 241a1bdf-1c37-3a68-96de-8a114c10b17d | -18.046301 | -44.383701 | 2024-09-28 00:11:25 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 000dbd72-b81e-3381-9948-9e12489016a2 | -18.0121 | -44.314499 | 2024-09-28 00:11:25 | METOP-B | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 54101069-a700-349f-a0aa-a8503fe0e258 | -18.013901 | -44.3237 | 2024-09-28 00:11:25 | METOP-B | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 748ee701-59a8-3ffc-98ec-633bed04cea5 | -17.7735 | -43.2383 | 2024-09-28 00:11:26 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| be168e9a-d4c8-3283-9319-720374359fc8 | -17.7852 | -43.2952 | 2024-09-28 00:11:26 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b1a776ff-a6ab-3ebb-92b5-849cc6783fcc | -17.945101 | -44.234402 | 2024-09-28 00:11:26 | METOP-B | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fda5ac05-ec70-3527-a886-d84a17cb8c2e | -17.946899 | -44.243401 | 2024-09-28 00:11:26 | METOP-B | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 643c91cb-a6df-332b-a463-b8adeea5e42f | -17.775101 | -43.246399 | 2024-09-28 00:11:26 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f1d7d26a-51d5-3fad-89c1-6267a5d06071 | -17.7768 | -43.254501 | 2024-09-28 00:11:26 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dcbb1bce-29f7-3d01-bdcb-ae441897944c | -17.7785 | -43.2626 | 2024-09-28 00:11:26 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b4938977-5061-3029-a7c7-bd179d39a8c0 | -17.7801 | -43.270699 | 2024-09-28 00:11:26 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0a47420d-a447-3c06-9d4f-de3299bbdb28 | -17.781799 | -43.2789 | 2024-09-28 00:11:26 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ba6c25a7-1de3-3a67-9f19-0fd957812eed | -17.783501 | -43.286999 | 2024-09-28 00:11:26 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 305aef9e-c468-38e5-96b1-a995706706f5 | -17.7703 | -43.2729 | 2024-09-28 00:11:26 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6c35c6f4-6652-354e-8f62-0d091769402b | -17.771999 | -43.281101 | 2024-09-28 00:11:26 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1e05ed08-78e5-396f-90ff-36f8a25d7d96 | -18.0005 | -44.460999 | 2024-09-28 00:11:26 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 173edb84-2127-3788-9106-a2c5a5b72c57 | -17.435499 | -42.597801 | 2024-09-28 00:11:29 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| aa2d8ee3-9733-394c-a634-f5b8466daa1f | -17.437099 | -42.6054 | 2024-09-28 00:11:29 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 19929fa4-5ca1-3760-b513-ab25a89d44ee | -17.4387 | -42.613098 | 2024-09-28 00:11:29 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 922bd01d-34c8-3777-8cb1-f7f74496ba96 | -17.760201 | -44.330898 | 2024-09-28 00:11:29 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9a761a85-e990-3807-914b-38680fd1cfb6 | -17.830999 | -44.429901 | 2024-09-28 00:11:29 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 51a6b62f-5d7b-30e6-b92a-4f9089eaba48 | -17.832899 | -44.439098 | 2024-09-28 00:11:29 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6754b346-1319-3dc8-bd71-d2ed98daaf8e | -17.836599 | -44.4576 | 2024-09-28 00:11:29 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dc57f82e-cdd9-3d14-a313-0d2fd02ce35d | -17.8384 | -44.466801 | 2024-09-28 00:11:29 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2e59bc55-698a-3006-9467-9bcd7efce0f8 | -17.816999 | -44.4618 | 2024-09-28 00:11:29 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 132c3452-ac9f-3a29-98da-d01fac302c0d | -17.750401 | -44.333 | 2024-09-28 00:11:30 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 51f06e66-5ba1-3668-a51b-56713c65b5e4 | -16.9722 | -41.200401 | 2024-09-28 00:11:32 | METOP-B | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0fba4119-acde-30e6-bd20-5ef30c3f3443 | -17.8389 | -45.872799 | 2024-09-28 00:11:33 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fd86bf2b-f19a-36a5-a88a-9e8b114e50d0 | -17.841 | -45.8839 | 2024-09-28 00:11:33 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e55f32d5-0017-3dad-9d8d-5feaec8e8c31 | -17.739401 | -46.307999 | 2024-09-28 00:11:36 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 83ee694a-d7c5-3605-acff-4c62ef36320b | -17.041901 | -43.216099 | 2024-09-28 00:11:37 | METOP-B | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f1250ffc-f38d-3567-9944-c4c2ca1b0867 | -17.043501 | -43.223999 | 2024-09-28 00:11:37 | METOP-B | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6f74f032-9c0c-3ac8-89f8-c9159dd57ce7 | -17.033701 | -43.226101 | 2024-09-28 00:11:38 | METOP-B | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5ac432af-5fd4-3d58-b7ec-c73aba97e9ba | -17.032101 | -43.218201 | 2024-09-28 00:11:38 | METOP-B | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 78bc8d9e-d044-35a5-bea6-c1c040144a39 | -17.0354 | -43.2341 | 2024-09-28 00:11:38 | METOP-B | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3d8b12c7-9589-34c1-850f-449a47122a60 | -16.8839 | -45.308399 | 2024-09-28 00:11:47 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7c6cb33f-5634-3b3a-9a28-988f6db3566c | -16.8859 | -45.318401 | 2024-09-28 00:11:47 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 38f03380-0dcd-308f-b0fb-f3b759d9b753 | -16.874201 | -45.310501 | 2024-09-28 00:11:47 | METOP-B | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| db0f0056-987a-377c-8b4c-6b8d217163ec | -17.002001 | -45.909401 | 2024-09-28 00:11:47 | METOP-B | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2fd287e7-8b77-36ac-aa17-cf78b269c92e | -17.1429 | -47.605701 | 2024-09-28 00:11:50 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1e11dc7e-3185-3de6-8be2-4de2bcc3776d | -17.1455 | -47.619598 | 2024-09-28 00:11:50 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 85f4ec84-d427-3997-98da-74bec48227f8 | -16.2644 | -43.861801 | 2024-09-28 00:11:52 | METOP-B | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 457aefff-9d17-3411-bd73-3963f00ea9f3 | -16.0355 | -43.5975 | 2024-09-28 00:11:55 | METOP-B | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fc0c3b72-0c73-342e-b9f1-302c448a9be1 | -16.0371 | -43.605499 | 2024-09-28 00:11:55 | METOP-B | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 644c4725-df1b-3fbf-8bae-2bec12731b5d | -16.8307 | -47.667599 | 2024-09-28 00:11:55 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ea300e4e-c4e3-3ebe-929b-e5b96ef77ef1 | -16.8235 | -47.683399 | 2024-09-28 00:11:55 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9a66fd4c-bedf-32e1-bc37-afbec5d1d6d6 | -16.826099 | -47.6973 | 2024-09-28 00:11:55 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 021182d1-1940-34d3-94fc-11757c1b33c9 | -16.577299 | -46.918598 | 2024-09-28 00:11:57 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 50f818d2-3046-37fc-8351-41cf6dd0120a | -15.774 | -43.5718 | 2024-09-28 00:11:59 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b85f18ac-56c9-3a9f-88ba-09854d7224f8 | -15.5126 | -43.546799 | 2024-09-28 00:12:03 | METOP-B | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6058b7e0-46b9-36f8-bcae-ba11a72362c5 | -15.5142 | -43.554699 | 2024-09-28 00:12:03 | METOP-B | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c5f277e4-c886-3aac-8175-607524737a06 | -15.5028 | -43.549 | 2024-09-28 00:12:04 | METOP-B | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3c0ef974-d87b-3fc6-91a1-4ea9f9d0c718 | -15.5044 | -43.5569 | 2024-09-28 00:12:04 | METOP-B | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 90f62e1b-7cfc-3bd6-b828-70553b1c641f | -15.9295 | -47.3494 | 2024-09-28 00:12:09 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3768e211-664b-3f7d-9439-7594ef88f137 | -15.1935 | -43.833199 | 2024-09-28 00:12:10 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 07fe5bc6-7045-393b-9ec0-3077e86538b2 | -15.1952 | -43.841202 | 2024-09-28 00:12:10 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dbfa6ceb-51f9-3829-a880-20b2a386b249 | -15.4094 | -47.441002 | 2024-09-28 00:12:18 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7b3c1ccd-d711-365f-9d82-bf5bdc5f28f8 | -15.3997 | -47.443001 | 2024-09-28 00:12:18 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3efe7898-34c8-32f1-bf5a-5ff9e8b190d1 | -15.4804 | -48.022202 | 2024-09-28 00:12:19 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9983c32b-44a6-35cc-96a9-df9a260ece02 | -13.367 | -42.0261 | 2024-09-28 00:12:33 | METOP-B | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d8945c55-4320-328c-b072-dc4920e0a9b1 | -13.3685 | -42.033199 | 2024-09-28 00:12:33 | METOP-B | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a69d058f-fdb6-36ef-a32f-0f6560a3d2c1 | -13.3701 | -42.040199 | 2024-09-28 00:12:33 | METOP-B | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 18777e77-2d90-3d87-9fe6-a2965509f1ce | -13.3716 | -42.047199 | 2024-09-28 00:12:33 | METOP-B | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1de2d11c-7c85-34e0-a5aa-651401cdc9ad | -13.3603 | -42.0424 | 2024-09-28 00:12:33 | METOP-B | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8c15151e-18f7-387f-8820-e9a2021b595e | -13.3489 | -42.037601 | 2024-09-28 00:12:33 | METOP-B | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f7aa3ad9-5158-39b1-b678-809d70f69531 | -13.3391 | -42.039799 | 2024-09-28 00:12:33 | METOP-B | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 899172a8-94cc-3194-bc0c-56bc2701df20 | -13.3407 | -42.046902 | 2024-09-28 00:12:33 | METOP-B | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b539e50b-ae24-33ad-be7b-d70f8aa55698 | -13.3422 | -42.053902 | 2024-09-28 00:12:33 | METOP-B | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 20f8caf8-796d-3997-84db-c6c05a744672 | -13.5504 | -43.436001 | 2024-09-28 00:12:35 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a5006e6-89f3-381e-9c3f-c18927a7f597 | -13.4453 | -43.760201 | 2024-09-28 00:12:38 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a148217c-a786-38a8-bcd2-f20ba1211403 | -13.4469 | -43.767799 | 2024-09-28 00:12:38 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6559fab5-17a2-35b4-ab9f-d99a50565962 | -13.4485 | -43.775398 | 2024-09-28 00:12:38 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b478b8d-aa23-3677-9e9e-21f8c0aae2c4 | -13.0065 | -42.2118 | 2024-09-28 00:12:39 | METOP-B | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f3abce98-05d5-3453-8213-a86aba3f1049 | -13.4375 | -44.012402 | 2024-09-28 00:12:39 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e488345-fc33-35a1-af84-6511a0bd1481 | -14.8367 | -51.3536 | 2024-09-28 00:12:39 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 948927f4-0257-3a60-b18b-e69a1dba9fa0 | -14.8408 | -51.376598 | 2024-09-28 00:12:39 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 724edc1a-3f9b-3a91-af49-6036cec6d6a8 | -13.4496 | -44.4086 | 2024-09-28 00:12:40 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aa566c14-ea59-3c70-b1ab-09f54b505b6c | -13.4514 | -44.416698 | 2024-09-28 00:12:40 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b3f53508-9b3e-344f-a432-4d1de8811dbb | -13.4416 | -44.4189 | 2024-09-28 00:12:40 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f57b9f45-b27c-3da6-872e-4097456bcfa2 | -14.827 | -51.3554 | 2024-09-28 00:12:40 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d9ff2e2-1dab-33bb-949c-6dcd97260a1f | -14.8311 | -51.378399 | 2024-09-28 00:12:40 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e8b53769-2d83-3c8d-8efd-2b83b4abe2c7 | -14.8173 | -51.357101 | 2024-09-28 00:12:40 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c02744d4-9a75-3c72-94c0-8c5440c1ed2d | -14.8214 | -51.3801 | 2024-09-28 00:12:40 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a48f42a1-d995-3283-bbc8-6b7b1eebfc56 | -13.1682 | -44.580399 | 2024-09-28 00:12:45 | METOP-B | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28ff3d4d-3a22-3824-8ec4-8284871e1e3a | -13.17 | -44.588501 | 2024-09-28 00:12:45 | METOP-B | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6451c504-d868-3cb9-ac00-0c0c745a9caa | -12.7443 | -43.459499 | 2024-09-28 00:12:48 | METOP-B | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12b769ff-08f4-3150-bbe3-bc54f06a6a97 | -12.7329 | -43.454399 | 2024-09-28 00:12:48 | METOP-B | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cd952747-78a4-37f7-94f0-4fc9d5189f88 | -12.7345 | -43.4617 | 2024-09-28 00:12:48 | METOP-B | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
