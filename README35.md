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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b8a7e88-4f5a-3c86-b339-16f3ed86f6e3 | -11.79167 | -38.26229 | 2024-10-13 03:23:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0cc0bd71-fed4-35de-b6f2-1d0daee88570 | -12.78228 | -38.49941 | 2024-10-13 03:23:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6df5616b-cb39-3109-a6d8-66ebd8175211 | -11.11 | -43.33668 | 2024-10-13 03:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 8058466b-f75f-358c-a022-ff5e08c9809c | -12.7778 | -38.49847 | 2024-10-13 03:23:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 97e8767b-af32-3444-b188-9d83e6178b12 | -13.03536 | -39.92542 | 2024-10-13 03:23:00 | NPP-375D | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ce82bc69-b5fc-38c4-b360-ee31d0b34df4 | -14.71264 | -40.36244 | 2024-10-13 03:23:00 | NPP-375D | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ad8ba23e-8ff4-3960-a24a-ef5e0b06fc9a | -14.71158 | -40.36801 | 2024-10-13 03:23:00 | NPP-375D | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5ee87cff-6a2f-313b-9532-61afc15ddc96 | -14.52147 | -40.34119 | 2024-10-13 03:23:00 | NPP-375D | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 37bce0a1-2f00-3b27-8564-3b0872b2bcfa | -14.52093 | -40.3404 | 2024-10-13 03:23:00 | NPP-375D | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8e956f69-d829-3ed6-a41f-497a9320d79c | -13.28191 | -41.91195 | 2024-10-13 03:23:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ca87f7f5-b740-3839-8157-bc2b22d7a837 | -12.39604 | -40.56166 | 2024-10-13 03:23:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d97bb3bd-1016-3dd6-b3d0-df7df4e9e130 | -15.31974 | -41.89455 | 2024-10-13 03:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f591f563-ef76-3a7e-a80e-5d7130902972 | -15.31901 | -41.89814 | 2024-10-13 03:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 89cf638b-a42b-3fdd-87d3-a4e9bd1d0306 | -15.31827 | -41.90175 | 2024-10-13 03:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b45c777f-55af-3ed4-b055-8f2a48072e41 | -15.31436 | -41.89355 | 2024-10-13 03:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 04389d0f-fef6-30bf-abec-fd707ce53a73 | -15.31364 | -41.89709 | 2024-10-13 03:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| d7475523-331d-36cf-bcad-68cbd4cfcfc0 | -15.31294 | -41.90054 | 2024-10-13 03:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 0c300e0b-b7de-380f-a665-184b5a5f8f86 | -15.31225 | -41.90394 | 2024-10-13 03:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a80e2ee9-2068-3bf7-84d2-7d3eec90f5fc | -10.51194 | -42.51097 | 2024-10-13 03:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 6ce69d56-3ded-3418-84bb-b98596961fcf | -10.50678 | -42.50514 | 2024-10-13 03:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 154a5d91-ef94-310d-8dff-dfb490e15dca | -10.50587 | -42.50983 | 2024-10-13 03:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 2709a68d-54ac-3965-a999-316b7e7e2ef1 | -10.50497 | -42.51451 | 2024-10-13 03:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 75820b8d-8dc3-399d-a60c-56d910947dd8 | -10.50406 | -42.51919 | 2024-10-13 03:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 7d90b34a-0759-379f-a46c-089cd5db2e12 | -10.50162 | -42.49929 | 2024-10-13 03:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b96e4fd2-ac49-3354-b88c-e7dfb3941cd0 | -10.50071 | -42.50398 | 2024-10-13 03:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 037015d4-0217-3135-9fc7-c58d17dffe45 | -10.4998 | -42.50866 | 2024-10-13 03:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 152a849b-10bf-3d03-81f1-b77a785fef89 | -10.4989 | -42.51333 | 2024-10-13 03:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0406b188-93df-3d9a-aef8-a689d34190ef | -10.498 | -42.51799 | 2024-10-13 03:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b1a303dd-57f8-3c36-8cd4-6a2d83edd940 | -10.49555 | -42.49813 | 2024-10-13 03:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| db3a9f65-2a64-3537-afa9-246cae80406d | -10.49284 | -42.51211 | 2024-10-13 03:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 74609dab-e73b-3536-b0ce-4d9c5414a26f | -12.115 | -43.18753 | 2024-10-13 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 385c5831-1932-3914-b467-fefa971151bb | -11.65747 | -41.73594 | 2024-10-13 03:23:00 | NPP-375D | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 13ed8c09-8030-3ae3-8414-d7abe9567cfb | -11.65414 | -41.73127 | 2024-10-13 03:23:00 | NPP-375D | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 74a740ec-f5ec-39a1-80cf-aef4ca2e4034 | -11.65337 | -41.73511 | 2024-10-13 03:23:00 | NPP-375D | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e177d44d-1f6e-334b-9742-5326307bccc0 | -11.65256 | -41.73088 | 2024-10-13 03:23:00 | NPP-375D | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5db4f691-3f5a-3533-9014-6d8bd9cebf93 | -11.65183 | -41.73472 | 2024-10-13 03:23:00 | NPP-375D | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e7549779-00f5-397c-8475-2488918fc053 | -11.04224 | -42.01817 | 2024-10-13 03:23:00 | NPP-375D | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c11afaa8-77b7-3c92-ab78-dbb92a221f46 | -13.65575 | -43.09597 | 2024-10-13 03:23:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63d832d2-1fa9-37e5-b389-989b8c21a428 | -13.64983 | -43.09459 | 2024-10-13 03:23:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 06ffae70-e893-3ac3-ac4f-e5f375eb22cf | -13.1437 | -41.97589 | 2024-10-13 03:23:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c9579f8a-191d-3f3e-a179-72fa187aa295 | -13.14293 | -41.97972 | 2024-10-13 03:23:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 968024d3-5733-3e18-baf6-8be502bb1dac | -13.14215 | -41.98364 | 2024-10-13 03:23:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 18fe5f28-8e49-3e9a-a975-ed96309d86df | -13.14042 | -41.96317 | 2024-10-13 03:23:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6d709ca8-82eb-3829-af4a-430893b483d8 | -13.13967 | -41.96692 | 2024-10-13 03:23:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 53fcedd3-49b6-30a1-97aa-9d91cd9de06a | -13.13892 | -41.9707 | 2024-10-13 03:23:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e87a23a2-ec55-3ef3-8b0c-9dd536ff86ed | -13.13813 | -41.97463 | 2024-10-13 03:23:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fcd6e948-7037-3f35-a371-a0a32593d91c | -13.13732 | -41.97865 | 2024-10-13 03:23:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1fa56dbb-28e4-33e5-adcb-5a61be1c4bf4 | -13.13652 | -41.98267 | 2024-10-13 03:23:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 69b370be-b839-3c4e-acdb-73b89ce739fe | -13.51414 | -43.48464 | 2024-10-13 03:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3abb96a8-af57-3960-a1e3-8c271f59df18 | -13.50806 | -43.4833 | 2024-10-13 03:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a0037b5-4b96-30e7-b8d0-5d7b97699ff5 | -11.10897 | -43.34171 | 2024-10-13 03:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 2998a11f-cb04-3117-8d96-09d6996e6147 | -11.10824 | -43.33567 | 2024-10-13 03:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 7df784aa-8b6d-3098-8349-0d46ab4742a6 | -11.10725 | -43.34071 | 2024-10-13 03:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 231fea39-56ee-326f-99c8-1fd9c04e2f9d | -12.12478 | -44.74355 | 2024-10-13 03:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfb84881-dfe6-389f-9ab3-7d1ff895c193 | -12.11808 | -44.74202 | 2024-10-13 03:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cc56aeb-1626-3914-a038-8f20d4a46730 | -11.73658 | -44.48566 | 2024-10-13 03:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a14bd761-d2be-3952-80bb-2bbbe01074b5 | -13.46414 | -43.66481 | 2024-10-13 03:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e152b4d-81c7-32e3-9899-85bbb4e674da | -13.45798 | -43.66346 | 2024-10-13 03:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eef9c120-e082-3e77-8c87-083d0c4f7e3a | -13.85963 | -44.40942 | 2024-10-13 03:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| abaf2dee-0da9-3521-9dd2-0c90277cf88c | -13.85851 | -44.41475 | 2024-10-13 03:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2d975e35-4ff7-3740-9006-7a1fb9b2123a | -13.78501 | -44.34632 | 2024-10-13 03:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae145398-2a8e-30ef-a54e-eb0e054e5b90 | -10.92701 | -44.67258 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a50e660e-3eef-3ebd-85e9-e547b5b123e6 | -10.92687 | -44.67229 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 02de95d0-b0ee-382c-aba9-6cb897dc8149 | -10.9257 | -44.67883 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 76f50e47-e160-3490-9087-f607b566422e | -10.9256 | -44.67856 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| bf23d397-804c-35eb-acd1-688df837b748 | -10.71442 | -44.49245 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a96bd384-40d5-3004-9646-40d38772e481 | -21.6261 | -43.4646 | 2024-10-13 03:25:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8adf5276-4e5f-333b-b90b-14abc6579d01 | -21.62536 | -43.46799 | 2024-10-13 03:25:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 428a1cdd-d95b-376a-9eaf-dbad16ec99cc | -1.733 | -54.173 | 2024-10-13 03:25:16 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a15b645d-f439-312d-84cf-477952db7d1b | -3.0956 | -53.0559 | 2024-10-13 03:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 3777bde0-7feb-3bde-8ec7-74822431b199 | -3.0957 | -53.0355 | 2024-10-13 03:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 843e26ec-6618-3bac-bef6-2781ff1443f8 | -3.1141 | -53.0351 | 2024-10-13 03:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| c8798092-21c7-3d20-a05c-44f2ecc38c70 | -3.1791 | -50.476 | 2024-10-13 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 891929b4-f672-32eb-8495-1c18a7187987 | -3.1792 | -50.4551 | 2024-10-13 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 824d7a3f-cc26-3a35-9af6-473a6ae92bdc | -3.1976 | -50.4545 | 2024-10-13 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 288ac7b1-be7e-3a59-b7a4-eba99c9cb885 | -4.1148 | -48.2515 | 2024-10-13 03:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 1ed1c88e-ebb3-3286-afea-53081a329cf8 | -4.1149 | -48.2299 | 2024-10-13 03:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 31503f0d-eb97-3550-b0a5-c79e979d9460 | -4.3985 | -44.4881 | 2024-10-13 03:25:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b1c3ad5c-5e6c-3d8f-96e8-e2751e6b594c | -5.1238 | -60.3397 | 2024-10-13 03:25:36 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 71eaaf04-4030-3ced-b7b4-69e7bf8a7b08 | -5.1239 | -60.3206 | 2024-10-13 03:25:36 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 03eb5c4f-9883-33b7-9716-b8a66daef2bd | -7.6815 | -47.3213 | 2024-10-13 03:25:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| f75f6c08-4227-3741-a314-cea1763a4d39 | -9.7359 | -64.2295 | 2024-10-13 03:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1d0267ee-39a1-3f27-a4cc-4f974c90a137 | -10.5097 | -42.5023 | 2024-10-13 03:26:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 655e3d78-003f-31cc-bcd5-b974bc95fea8 | -10.5283 | -49.9564 | 2024-10-13 03:26:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b0507bca-5361-3acd-bf69-c25d25e121ca | -10.9311 | -44.6789 | 2024-10-13 03:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 998882ba-84ee-3eba-851d-a9ba2b8ab841 | -11.7308 | -64.9769 | 2024-10-13 03:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2aef638a-2498-362b-a696-ec95898e1083 | -12.4792 | -63.0159 | 2024-10-13 03:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 1f8cc494-4201-33ef-8ba2-3fc7bb902db2 | -13.7153 | -60.6289 | 2024-10-13 03:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 8a18f163-ae4e-3475-8d74-5ff372294056 | -13.7155 | -60.6093 | 2024-10-13 03:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 3dd0b057-55cd-39d4-aeea-93ec8ad34796 | -13.7346 | -60.6079 | 2024-10-13 03:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 910f2978-96ba-36fa-a262-4bd21bf261fc | -13.7348 | -60.5883 | 2024-10-13 03:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 21c22323-ce8c-37de-b7bd-69fafe313ba1 | -15.3244 | -41.8911 | 2024-10-13 03:26:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.5 |
| 8b0cbebf-0dbc-3fcb-b960-4b582ea38799 | -17.2639 | -42.6527 | 2024-10-13 03:26:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 2c79110d-c595-3ac9-aa9c-cefd97d6d0ce | -17.1758 | -57.479 | 2024-10-13 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| b1203198-b154-36c2-a00f-1c1a6931174f | -17.1761 | -57.4585 | 2024-10-13 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 41285798-3c17-3793-b421-030f160fad57 | -17.1954 | -57.4767 | 2024-10-13 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 40a20b75-135b-34df-bb48-cd45d100231c | -17.1957 | -57.4562 | 2024-10-13 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| d1e96586-20cc-3157-84db-5315f5a94314 | -17.6277 | -56.2902 | 2024-10-13 03:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 1c89988e-705f-38f9-8df1-db2aed0a2e85 | -17.628 | -56.2694 | 2024-10-13 03:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 73549c96-c007-3358-ab3d-d28b6ba4b695 | -17.6474 | -56.2876 | 2024-10-13 03:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 217.8 |


[Clique aqui para ver as próximas entradas](README36.md)
