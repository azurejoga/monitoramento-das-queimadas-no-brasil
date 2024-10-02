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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa0f43b9-b04b-33b7-b715-a2ca206e997d | -21.640301 | -50.7672 | 2024-10-02 00:28:32 | METOP-B | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ebb15dd-e137-3d71-970a-f854ff02e9d3 | -21.6427 | -50.780899 | 2024-10-02 00:28:32 | METOP-B | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d220f213-45d5-3971-b65a-d8164f5d017e | -19.7318 | -41.632801 | 2024-10-02 00:28:33 | METOP-B | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4b6075f-ba85-3d0e-ab87-6a8c2444fc9f | -19.733801 | -41.641201 | 2024-10-02 00:28:33 | METOP-B | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd393b7d-4de7-3260-a316-ca0de62fabd3 | -19.735701 | -41.649502 | 2024-10-02 00:28:33 | METOP-B | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cb8f6b73-2079-3662-8422-1bc782a065e0 | -21.6329 | -50.782799 | 2024-10-02 00:28:33 | METOP-B | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2248352c-f832-31c5-99d4-d0795b09e90d | -21.620701 | -50.771099 | 2024-10-02 00:28:33 | METOP-B | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5c7ab8aa-223c-31dd-a3d2-d856aa6e5998 | -21.623199 | -50.784801 | 2024-10-02 00:28:33 | METOP-B | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 21bb4485-3383-35fb-b83a-9688d7a0df64 | -21.625601 | -50.7985 | 2024-10-02 00:28:33 | METOP-B | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 66f898cf-5201-38d6-9242-11639e430e8c | -21.611 | -50.772999 | 2024-10-02 00:28:33 | METOP-B | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 19b1391d-601f-3410-ba97-51e6d45dc7ef | -21.6134 | -50.786701 | 2024-10-02 00:28:33 | METOP-B | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 69042830-ab0f-395f-a297-14c368c77f1b | -21.615801 | -50.8004 | 2024-10-02 00:28:33 | METOP-B | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b4057ef-3209-33cb-8f94-4e08f3bc4099 | -20.2955 | -44.0238 | 2024-10-02 00:28:33 | METOP-B | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b799cc8-416a-3fc1-8860-aa64f6e84fd3 | -20.2971 | -44.031101 | 2024-10-02 00:28:33 | METOP-B | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 411b4c71-9219-3848-9149-a7dbb10c6670 | -20.287399 | -44.033501 | 2024-10-02 00:28:33 | METOP-B | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b713c93c-7f7a-33e2-aae9-d57d883aa06b | -21.564699 | -50.739899 | 2024-10-02 00:28:34 | METOP-B | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f59569ef-a763-371e-bca4-91bae5f12da3 | -21.567101 | -50.753502 | 2024-10-02 00:28:34 | METOP-B | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dc86fb43-c61b-31d6-867b-65caa529dcb2 | -21.555 | -50.741798 | 2024-10-02 00:28:34 | METOP-B | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d14118d8-bf0e-3a7f-946d-b9e1546dd1f7 | -19.7638 | -41.991199 | 2024-10-02 00:28:34 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0fd41ae8-bb56-3170-bb50-5c730da180ac | -19.765699 | -41.999298 | 2024-10-02 00:28:34 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1b6a7584-2dc5-3b0d-934c-051fb234a38a | -19.754 | -41.993698 | 2024-10-02 00:28:34 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 264d8ec3-dacd-33df-94de-f7e33f4c4cb2 | -19.755899 | -42.001801 | 2024-10-02 00:28:34 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 51eabd87-33ce-3e92-bd94-0fb168184bfd | -20.5368 | -46.269699 | 2024-10-02 00:28:36 | METOP-B | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 00e0f663-7443-37e3-8ded-fda387794ec7 | -21.440201 | -50.949402 | 2024-10-02 00:28:36 | METOP-B | BENTO DE ABREU | SÃO PAULO | Brasil | 3506201 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 69469bc2-9fae-38e0-b352-053695fd5f61 | -21.442699 | -50.963299 | 2024-10-02 00:28:36 | METOP-B | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4748b475-34c4-3315-8b4c-cf752865d89e | -21.430401 | -50.951302 | 2024-10-02 00:28:36 | METOP-B | BENTO DE ABREU | SÃO PAULO | Brasil | 3506201 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cb286ed4-284f-3b09-8b40-b6c273ce0296 | -21.432899 | -50.965199 | 2024-10-02 00:28:36 | METOP-B | BENTO DE ABREU | SÃO PAULO | Brasil | 3506201 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6d8d9c99-98a4-3e6b-9111-bf8d73c3d087 | -19.894899 | -43.149799 | 2024-10-02 00:28:36 | METOP-B | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0d7505b8-2c63-3f32-ad95-3cb6599e6a27 | -19.896601 | -43.157299 | 2024-10-02 00:28:36 | METOP-B | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a68141d-8d9c-3e42-9e0e-22f9ae8fc39e | -19.885099 | -43.152199 | 2024-10-02 00:28:36 | METOP-B | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b1ffe422-70b3-3641-bc5b-044d82bf9624 | -19.875299 | -43.154701 | 2024-10-02 00:28:36 | METOP-B | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8327d640-68cf-3d42-9918-22bc17697977 | -19.877001 | -43.162201 | 2024-10-02 00:28:36 | METOP-B | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dec70b5c-9019-378a-8475-fae664c0de40 | -20.5173 | -46.2742 | 2024-10-02 00:28:37 | METOP-B | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 41ad107c-c815-3ac1-ab58-9a2f8251a31e | -20.523899 | -46.256302 | 2024-10-02 00:28:37 | METOP-B | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9e36283a-725b-31d0-8f74-df0875627a24 | -20.525499 | -46.264099 | 2024-10-02 00:28:37 | METOP-B | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5fd8c7e6-b2ba-3f40-b865-55b8d88d3221 | -20.5271 | -46.2719 | 2024-10-02 00:28:37 | METOP-B | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c7257c00-8769-3f31-b4ef-e636bc0c2b1e | -20.5287 | -46.279701 | 2024-10-02 00:28:37 | METOP-B | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 43c82ee8-3dd8-3f20-9abb-8b58b20f973b | -20.515699 | -46.266399 | 2024-10-02 00:28:37 | METOP-B | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 08e98b6c-f62a-3e99-a9f0-8f9b0da2b60f | -20.523701 | -46.305401 | 2024-10-02 00:28:37 | METOP-B | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eb931201-66c1-3384-bcf9-cc3b723b8c72 | -20.525299 | -46.313202 | 2024-10-02 00:28:37 | METOP-B | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ef9590f6-b489-35d2-b7ac-294c4850486c | -20.526899 | -46.321098 | 2024-10-02 00:28:37 | METOP-B | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 244a6163-9222-3c44-b6ee-f5da79352d48 | -20.5123 | -46.299801 | 2024-10-02 00:28:37 | METOP-B | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| afa69a08-25f4-3afc-aef3-b0bb0bec7567 | -20.513901 | -46.307598 | 2024-10-02 00:28:37 | METOP-B | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0dceb3ef-6a66-3add-88b0-d7c7cc600d49 | -20.515499 | -46.315399 | 2024-10-02 00:28:37 | METOP-B | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f14f70de-8f01-353d-a0b6-09d2a985d659 | -20.517099 | -46.323299 | 2024-10-02 00:28:37 | METOP-B | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1fed7db8-31ee-39b6-90fd-0386322add8b | -20.5187 | -46.3311 | 2024-10-02 00:28:37 | METOP-B | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 921224bb-709b-3eee-bfba-f3da4bf89bf1 | -20.627701 | -46.7649 | 2024-10-02 00:28:37 | METOP-B | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 525610e3-965b-3203-beb2-160a4a69bf88 | -20.6294 | -46.772999 | 2024-10-02 00:28:37 | METOP-B | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fa6d2ee4-8c2c-3e44-baf8-dbc8f83fca4b | -21.4207 | -50.953201 | 2024-10-02 00:28:37 | METOP-B | BENTO DE ABREU | SÃO PAULO | Brasil | 3506201 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aa1e17ee-7e63-3922-bbeb-771dc4d16f15 | -21.423201 | -50.967098 | 2024-10-02 00:28:37 | METOP-B | BENTO DE ABREU | SÃO PAULO | Brasil | 3506201 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 57614cb1-9bb2-3401-9ff7-617deb0978b9 | -21.4109 | -50.955101 | 2024-10-02 00:28:37 | METOP-B | BENTO DE ABREU | SÃO PAULO | Brasil | 3506201 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8e7fb31c-d3a5-3762-b994-1ab69395ff20 | -21.413401 | -50.969002 | 2024-10-02 00:28:37 | METOP-B | BENTO DE ABREU | SÃO PAULO | Brasil | 3506201 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 95058812-a6ed-32ec-a414-b6f16ef741c0 | -19.429501 | -41.3601 | 2024-10-02 00:28:37 | METOP-B | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 45f89464-0430-3551-affb-e3f23f3b23a9 | -19.431499 | -41.368698 | 2024-10-02 00:28:37 | METOP-B | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b5d70c15-e993-3b80-becc-09438eba427a | -19.421801 | -41.371201 | 2024-10-02 00:28:37 | METOP-B | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9a666ad3-9f27-33d9-9ece-19b0f7b8887e | -19.4238 | -41.379799 | 2024-10-02 00:28:37 | METOP-B | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c883b3f9-7c8d-33bc-b444-9a9f8a8ff972 | -20.952999 | -49.1077 | 2024-10-02 00:28:39 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7e369f5a-0eb0-3fcf-afe6-d1737d27c94b | -19.6691 | -42.927399 | 2024-10-02 00:28:39 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d1f643cc-d465-35f0-a04a-934f751b25b2 | -20.011499 | -44.514999 | 2024-10-02 00:28:39 | METOP-B | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b60d3b4d-9669-33e1-8813-d9dc1f3fa4e0 | -20.0131 | -44.522202 | 2024-10-02 00:28:39 | METOP-B | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3134e5b7-f45c-39d3-b278-a22e61f24a36 | -20.0002 | -44.509998 | 2024-10-02 00:28:39 | METOP-B | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b619d33-e6c1-3344-9270-dcc51bddcff0 | -20.001699 | -44.5173 | 2024-10-02 00:28:39 | METOP-B | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 53b4fb10-7add-31b0-8d65-2b1b145e0331 | -20.0033 | -44.524601 | 2024-10-02 00:28:39 | METOP-B | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 17f7a2df-1668-301f-8071-6df22c2f4c31 | -19.993601 | -44.526901 | 2024-10-02 00:28:39 | METOP-B | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3ed736be-7cb3-321f-a02a-4ba4390a5fbd | -19.5116 | -42.870499 | 2024-10-02 00:28:41 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 45568feb-35d7-3cbc-b378-b55c52e4b0d4 | -19.500099 | -42.865299 | 2024-10-02 00:28:41 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bca6378b-f495-31cd-bded-431215aac856 | -19.501801 | -42.872898 | 2024-10-02 00:28:41 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3868a826-cbf1-3fd3-bf68-287405e9ee69 | -20.6504 | -48.692001 | 2024-10-02 00:28:42 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 31ac9f4a-a8ed-39c7-b78f-1a9559409453 | -19.746201 | -44.242599 | 2024-10-02 00:28:42 | METOP-B | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 039f7f35-a829-3e06-ac9d-1d745a369235 | -19.747801 | -44.249901 | 2024-10-02 00:28:42 | METOP-B | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5afd3c90-bbb5-37c3-9472-b3a21e4e443c | -19.611601 | -44.099098 | 2024-10-02 00:28:44 | METOP-B | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d4aad0e5-a634-39b6-bbda-34dd6b71adad | -19.6133 | -44.1064 | 2024-10-02 00:28:44 | METOP-B | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 72b5c326-63a6-3b02-9c2e-0f47343c43c3 | -18.960199 | -41.519501 | 2024-10-02 00:28:45 | METOP-B | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f25cfdae-915f-3438-9e2c-6c8cd6751964 | -19.243799 | -43.328499 | 2024-10-02 00:28:47 | METOP-B | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0660cf40-d06a-309e-9da7-c21c5a5f5255 | -21.3529 | -55.636799 | 2024-10-02 00:28:50 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 24adf730-bed6-322f-bb14-512515ef9975 | -21.3571 | -55.6651 | 2024-10-02 00:28:50 | METOP-B | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 89f1dcad-150e-35b8-a47e-edc45605a92f | -21.343201 | -55.6385 | 2024-10-02 00:28:51 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cd7d636b-f105-34d3-95de-33c77e0e2845 | -21.347401 | -55.666698 | 2024-10-02 00:28:51 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| aef12047-e3b3-39f0-a4e5-e394fbf43ec6 | -19.392599 | -46.386398 | 2024-10-02 00:28:55 | METOP-B | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8a63f0aa-5a03-315e-8557-765c4beeedbf | -19.394199 | -46.3941 | 2024-10-02 00:28:55 | METOP-B | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ba64c257-b20e-342a-a051-f8f0a54a10ac | -18.514 | -42.218399 | 2024-10-02 00:28:55 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 143f832d-5319-3c26-834e-02352c677005 | -18.5159 | -42.226501 | 2024-10-02 00:28:55 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 26263637-9e30-3d88-a754-7e49136054e4 | -18.517799 | -42.2346 | 2024-10-02 00:28:55 | METOP-B | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ebe1ceb-36cd-3ca6-b1ed-7a06a9c30b2b | -18.504299 | -42.220901 | 2024-10-02 00:28:55 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6a8029b7-bf9a-3d6e-aae1-439c3f08a598 | -18.506201 | -42.229 | 2024-10-02 00:28:55 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5780c2a9-758d-3547-8426-c4798f6bc3b5 | -18.508101 | -42.237099 | 2024-10-02 00:28:55 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| daeeeb5e-714a-307d-889c-b2e916d238b1 | -19.473 | -46.874699 | 2024-10-02 00:28:56 | METOP-B | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 16e88d29-3f62-33d5-a6fd-bd5a2794de44 | -19.474701 | -46.882702 | 2024-10-02 00:28:56 | METOP-B | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 411c4a68-8598-3466-a0a0-ba0fd769c77c | -19.243099 | -46.852001 | 2024-10-02 00:28:59 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 04bdf12a-d251-3d67-a5b1-40f988beeaef | -19.244699 | -46.859901 | 2024-10-02 00:28:59 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 37970451-b7a7-3663-9212-3d74cab49b65 | -18.5198 | -43.366501 | 2024-10-02 00:28:59 | METOP-B | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cbf340f1-6043-3aef-86fe-36bb2091df2f | -18.5215 | -43.373901 | 2024-10-02 00:28:59 | METOP-B | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 219f3c71-4a42-3f82-abc7-0941d4f9db95 | -20.091999 | -51.315399 | 2024-10-02 00:29:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8a14f286-d015-396e-8009-8948f9917073 | -20.0945 | -51.329399 | 2024-10-02 00:29:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0b7e0f57-001d-3e57-a44a-d6dae30894ef | -20.097099 | -51.343498 | 2024-10-02 00:29:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| aaedf596-4806-3a2d-becc-8cbdfcdcb64a | -20.082199 | -51.317299 | 2024-10-02 00:29:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3ccdbef9-d3b0-330a-ab37-bee8e952cc26 | -20.084801 | -51.331299 | 2024-10-02 00:29:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4389192a-68e3-30d6-a228-5cd7e1c52576 | -19.231701 | -46.846401 | 2024-10-02 00:29:00 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1dccaa08-f205-3ecc-92d0-faf631c80eff | -19.233299 | -46.854198 | 2024-10-02 00:29:00 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8109f711-c6d3-370f-a4ef-d574a7d97c5d | -19.2349 | -46.862099 | 2024-10-02 00:29:00 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
