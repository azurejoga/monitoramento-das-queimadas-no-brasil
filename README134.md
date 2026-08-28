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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecbbb262-0af7-3e0c-bcc5-6eb12e4708bf | -22.85056 | -49.34059 | 2026-08-28 17:41:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0c13ab06-ffaf-3116-9564-a711b9d03da0 | -26.97247 | -50.67158 | 2026-08-28 17:41:00 | NOAA-20 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 534ad04d-14c1-3b61-9982-aed1f382ab8d | -25.98912 | -50.44024 | 2026-08-28 17:41:00 | NOAA-20 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| e0adb9da-b96c-33eb-a6be-5045ba8b4042 | -26.63951 | -51.42744 | 2026-08-28 17:41:00 | NOAA-20 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| b287e1dd-b1b2-3013-a4ec-20a8cc91c161 | -26.97202 | -50.6693 | 2026-08-28 17:41:00 | NOAA-20 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 77d027cf-8814-36c4-96d8-a99129a135d1 | -26.33352 | -53.07973 | 2026-08-28 17:41:00 | NOAA-20 | MARMELEIRO | PARANÁ | Brasil | 4115408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 1a6a4196-ca5b-3c30-a281-0ccb6d485daa | -26.37361 | -53.69302 | 2026-08-28 17:41:00 | NOAA-20 | DIONÍSIO CERQUEIRA | SANTA CATARINA | Brasil | 4205001 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 8bd9303d-c578-3236-a9ea-7777bab74120 | -26.6346 | -51.07795 | 2026-08-28 17:41:00 | NOAA-20 | CALMON | SANTA CATARINA | Brasil | 4203154 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| e90f87fe-0822-38ce-b34e-a0046286a6df | -26.63308 | -51.02637 | 2026-08-28 17:41:00 | NOAA-20 | CALMON | SANTA CATARINA | Brasil | 4203154 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 8b0d99cf-16b5-3195-a280-f83f3a2780e6 | -27.75828 | -50.48794 | 2026-08-28 17:41:00 | NOAA-20 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| bd0ac002-75b4-3153-9681-b641b35911fd | -25.91658 | -50.63603 | 2026-08-28 17:41:00 | NOAA-20 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 708362d2-3fbc-3552-bf5f-42c2e603e610 | -27.23418 | -50.66879 | 2026-08-28 17:41:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| b012af36-a789-352d-9200-133d8bf75223 | -25.21252 | -50.69394 | 2026-08-28 17:41:00 | NOAA-20 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 40.4 |
| 8f1dbacc-b8df-35a6-a12a-48805ea8c65a | -24.99584 | -49.37847 | 2026-08-28 17:41:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 43f4ce7a-ed33-39ef-9ac1-f112711a9e04 | -25.83559 | -51.6671 | 2026-08-28 17:41:00 | NOAA-20 | PINHÃO | PARANÁ | Brasil | 4119301 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 1d86b512-e30b-384e-92c4-6d62343b83f7 | -25.21371 | -50.69941 | 2026-08-28 17:41:00 | NOAA-20 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 6bb700bb-2f8b-3991-9037-7d6b68aa038b | -24.91141 | -50.94513 | 2026-08-28 17:41:00 | NOAA-20 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 0c5ae68c-4269-3b32-b292-9dc1c3a896db | -26.6509 | -51.08866 | 2026-08-28 17:41:00 | NOAA-20 | CALMON | SANTA CATARINA | Brasil | 4203154 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| e6328a4e-e211-35a2-86b4-192b04712f2b | -23.0621 | -47.4043 | 2026-08-28 17:41:00 | NOAA-20 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 091615f6-5d5c-373a-9455-4aa3ca26714c | -25.6422 | -50.49329 | 2026-08-28 17:41:00 | NOAA-20 | FERNANDES PINHEIRO | PARANÁ | Brasil | 4107736 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 360482df-880d-32d4-bf26-731f291d01a8 | -25.18401 | -49.16708 | 2026-08-28 17:41:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| f86e7e06-fe7f-3242-ad50-da94f5774d75 | -27.18729 | -52.8626 | 2026-08-28 17:41:00 | NOAA-20 | RIO DOS ÍNDIOS | RIO GRANDE DO SUL | Brasil | 4315552 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 58871a34-85a8-3417-9149-d9526dcfbe34 | -26.97312 | -50.67442 | 2026-08-28 17:41:00 | NOAA-20 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| b830260e-0963-312b-8b6b-b4a8e7478dde | -22.78545 | -47.62247 | 2026-08-28 17:41:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| a7ba8232-3b55-373c-a003-126f066e9683 | -24.92968 | -51.07897 | 2026-08-28 17:41:00 | NOAA-20 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 855d871d-052d-32e3-ada9-a216f4c138d4 | -26.63408 | -51.42332 | 2026-08-28 17:41:00 | NOAA-20 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 16c97fcc-cf6b-3ad1-b7ae-eb4767ddf800 | -24.81767 | -51.27402 | 2026-08-28 17:41:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 249e4c41-0938-3ce0-b19f-9f61071d8e50 | -23.06826 | -47.39563 | 2026-08-28 17:41:00 | NOAA-20 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| b51b0a07-27a3-36b0-b726-000a2af45aa5 | -25.92616 | -51.70858 | 2026-08-28 17:41:00 | NOAA-20 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 8e0bbf5b-5e76-3797-b5f4-01870092288c | -24.96465 | -49.3112 | 2026-08-28 17:41:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 7f0331b2-66dd-3a0b-a682-44b3df20bf53 | -22.77074 | -45.19744 | 2026-08-28 17:41:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d6ab3a08-898c-34e0-b704-bb47931f292d | -24.78691 | -49.56857 | 2026-08-28 17:41:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 76c0d88c-d714-31f3-83f0-4a2c83cba82d | -27.35074 | -53.02469 | 2026-08-28 17:41:00 | NOAA-20 | PLANALTO | RIO GRANDE DO SUL | Brasil | 4314704 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 91c3eb5e-6019-371b-9b42-ff24bd07ead4 | -25.46121 | -51.29886 | 2026-08-28 17:41:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 4ed0abbd-23ed-3440-a2fa-05c9bd1be597 | -25.18474 | -49.17038 | 2026-08-28 17:41:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| a1e5c44e-280e-39b4-baba-b3aadb83c8ef | -27.18871 | -52.86262 | 2026-08-28 17:41:00 | NOAA-20 | RIO DOS ÍNDIOS | RIO GRANDE DO SUL | Brasil | 4315552 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 78e4e213-a0b5-3699-913d-3726caf98832 | -24.67489 | -49.58202 | 2026-08-28 17:41:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ab8e6ba5-395d-3a49-8802-0771f5ad8052 | -23.06577 | -47.39301 | 2026-08-28 17:41:00 | NOAA-20 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 2046c108-85cc-3607-a2a6-7ba7f564ddae | -23.06349 | -47.40206 | 2026-08-28 17:41:00 | NOAA-20 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| cf96e8c9-6f0b-3a7c-a2bd-cea2b86a200c | -24.90649 | -51.26352 | 2026-08-28 17:41:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 39840c0e-5d50-3077-addb-7b664a91bbce | -24.81216 | -51.13331 | 2026-08-28 17:41:00 | NOAA-20 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 4ffadf79-7e21-3a76-8cc7-6b7f7eebe655 | -24.96599 | -52.61442 | 2026-08-28 17:41:00 | NOAA-20 | DIAMANTE DO SUL | PARANÁ | Brasil | 4107124 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c04eed60-2fb6-353f-a4d6-93d6a4e754b1 | -27.04112 | -52.75784 | 2026-08-28 17:41:00 | NOAA-20 | GUATAMBÚ | SANTA CATARINA | Brasil | 4206652 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0cf5d199-b382-33df-8d4d-7448ba4ac8f2 | -23.06231 | -47.39714 | 2026-08-28 17:41:00 | NOAA-20 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 4ad80e47-4101-3188-9790-3de36e55994e | -25.46017 | -51.29732 | 2026-08-28 17:41:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| d55ebf98-8542-313f-9121-ed682722875a | -26.05367 | -51.5956 | 2026-08-28 17:41:00 | NOAA-20 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| c29bc7ab-1520-3e9f-ab18-58c4ddda6e11 | -24.96847 | -49.65454 | 2026-08-28 17:41:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| df1965ea-7ec3-3c2b-a02e-5bbd62514515 | -27.34573 | -53.02012 | 2026-08-28 17:41:00 | NOAA-20 | PLANALTO | RIO GRANDE DO SUL | Brasil | 4314704 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 6ced6347-21da-3980-92af-108d66e603f5 | -23.88343 | -51.44733 | 2026-08-28 17:41:00 | NOAA-20 | FAXINAL | PARANÁ | Brasil | 4107603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 9e12fb09-0077-3829-bc31-0ee0240feb4c | -27.87839 | -51.34994 | 2026-08-28 17:41:00 | NOAA-20 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 73a6fd25-fc43-3294-add7-8af8e8883273 | -24.96388 | -49.30777 | 2026-08-28 17:41:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| abb457d8-998d-3d30-939b-bf72725c94ba | -25.20785 | -50.69518 | 2026-08-28 17:41:00 | NOAA-20 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 52.2 |
| 8af4accb-4628-3df9-b7d7-7fd8e111a4fe | -23.19981 | -46.98095 | 2026-08-28 17:41:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fcae9ac7-f947-31e7-b0f5-0416fbc3ed89 | -23.06805 | -47.40277 | 2026-08-28 17:41:00 | NOAA-20 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 797556da-786c-3aa8-bd27-aa5b88d91327 | -25.12767 | -52.45694 | 2026-08-28 17:41:00 | NOAA-20 | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 03d13077-c128-34db-bb17-69cf45b628e5 | -22.84704 | -49.34025 | 2026-08-28 17:41:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 26839941-a975-3be4-ac33-79aefe0cb164 | -25.92527 | -51.70422 | 2026-08-28 17:41:00 | NOAA-20 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 73514e64-4c44-37b8-98b9-512c459a2053 | -25.18816 | -52.71706 | 2026-08-28 17:41:00 | NOAA-20 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 3117fd62-67c8-3c20-8b86-2f0844714f85 | -25.18733 | -51.12661 | 2026-08-28 17:41:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 3947fd86-4a6f-32ec-9a1e-32c0a35d5f93 | -26.84301 | -51.02629 | 2026-08-28 17:41:00 | NOAA-20 | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 6ef443ee-cdf0-3f75-bc1d-1e2dacc3d51c | -25.92568 | -52.64549 | 2026-08-28 17:41:00 | NOAA-20 | CORONEL VIVIDA | PARANÁ | Brasil | 4106506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 62bd8be7-0401-3dd5-abc0-77d480f21904 | -25.07642 | -48.57899 | 2026-08-28 17:41:00 | NOAA-20 | CAMPINA GRANDE DO SUL | PARANÁ | Brasil | 4104006 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 552ccc9e-3617-34fd-90be-aaf6e2bc2141 | -26.88042 | -50.598 | 2026-08-28 17:41:00 | NOAA-20 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| bbd75b55-6d31-3592-86e7-e223c466b601 | -25.46566 | -51.29754 | 2026-08-28 17:41:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 7a092638-2905-3886-af92-abaa0c0391b5 | -23.06096 | -47.39938 | 2026-08-28 17:41:00 | NOAA-20 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| a7eebeb5-15db-3eea-9a75-18ad977ed4dd | -26.4799 | -51.38507 | 2026-08-28 17:41:00 | NOAA-20 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 62dc05e9-c611-37d9-bfc4-349fdfdd747f | -25.44084 | -52.69044 | 2026-08-28 17:41:00 | NOAA-20 | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d9ba7f5e-15be-30aa-b74a-090d7af0d462 | -27.82625 | -51.83216 | 2026-08-28 17:41:00 | NOAA-20 | SÃO JOÃO DA URTIGA | RIO GRANDE DO SUL | Brasil | 4318424 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d74fc5ac-a3a4-346e-bc02-17e77a3b268a | -24.64563 | -51.59259 | 2026-08-28 17:41:00 | NOAA-20 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| baab7260-4927-36c2-aaeb-762232586a4c | -27.32511 | -52.89402 | 2026-08-28 17:41:00 | NOAA-20 | NONOAI | RIO GRANDE DO SUL | Brasil | 4312708 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 4075a8d3-d924-3786-9295-62249a048f7a | -24.85256 | -49.22735 | 2026-08-28 17:41:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ff629ea5-9061-3bc7-9186-04d42d8d68a2 | -24.66976 | -49.58298 | 2026-08-28 17:41:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 23f40685-e5aa-3fbd-8692-f1a9437fb90e | -23.06692 | -47.39791 | 2026-08-28 17:41:00 | NOAA-20 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 1c6214c8-d438-3413-9aaf-2755ff2e9f9d | -24.90549 | -51.2615 | 2026-08-28 17:41:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 6168eca3-d9e8-3c82-a56c-a36245eec683 | -27.79881 | -52.13471 | 2026-08-28 17:41:00 | NOAA-20 | GETÚLIO VARGAS | RIO GRANDE DO SUL | Brasil | 4308904 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d8b12ebc-8332-3280-a5a2-dc1d135d1eb6 | -22.78867 | -47.62378 | 2026-08-28 17:41:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 3aa7e32c-c8d5-3c51-9773-184e38127f85 | -27.04703 | -52.42483 | 2026-08-28 17:41:00 | NOAA-20 | ARVOREDO | SANTA CATARINA | Brasil | 4201653 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8d0c7821-bbee-33f6-8f31-2adfd6dd11f0 | -22.84975 | -49.3369 | 2026-08-28 17:41:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9ab44a0b-775e-356f-8c32-6de8286eeee1 | -25.43667 | -52.6913 | 2026-08-28 17:41:00 | NOAA-20 | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 5b27bd5b-9608-3656-9d27-d282f7322c69 | -26.05272 | -51.59305 | 2026-08-28 17:41:00 | NOAA-20 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 1f122537-35d2-3609-bf3a-7eb4e632883d | -26.48093 | -51.39001 | 2026-08-28 17:41:00 | NOAA-20 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 0c9f1868-7c4f-3ead-9aba-ee60e5b3b12d | -22.73537 | -47.43379 | 2026-08-28 17:41:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d4bd1bcd-bfff-3565-a6de-7d92b269fed1 | -25.1302 | -52.07779 | 2026-08-28 17:41:00 | NOAA-20 | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 4dfbd722-5a76-3b8e-af52-ec98c0cf541c | -25.18679 | -51.12907 | 2026-08-28 17:41:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 90f66eaa-a34d-3bd6-a8e5-3037074ffb39 | -24.83902 | -52.01359 | 2026-08-28 17:41:00 | NOAA-20 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9fe2110a-398e-3d1e-8d83-d4cf7dc5bc0a | -25.18804 | -52.72058 | 2026-08-28 17:41:00 | NOAA-20 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 28390289-37ec-3861-ac55-3aef5e2414d9 | -26.37249 | -53.69059 | 2026-08-28 17:41:00 | NOAA-20 | DIONÍSIO CERQUEIRA | SANTA CATARINA | Brasil | 4205001 | 42 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| cd92444b-79ec-310e-90e7-6a8dd6ced850 | -25.21079 | -50.6908 | 2026-08-28 17:41:00 | NOAA-20 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| f8fe09d6-9103-3696-8de2-204c588adffa | -27.34683 | -53.02575 | 2026-08-28 17:41:00 | NOAA-20 | PLANALTO | RIO GRANDE DO SUL | Brasil | 4314704 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 0764e702-2fa0-3204-ade7-04be1ed892e0 | -24.8836 | -49.24453 | 2026-08-28 17:41:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 87608c8b-498d-3799-be4c-92988ae0339c | -26.10496 | -53.13664 | 2026-08-28 17:41:00 | NOAA-20 | FRANCISCO BELTRÃO | PARANÁ | Brasil | 4108403 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 38b8fc60-2ca7-3f42-81e5-8101cb13cfbf | -26.47655 | -51.39107 | 2026-08-28 17:41:00 | NOAA-20 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 30bf8281-9a33-3eb4-8fbb-5c4aa3e15c2d | -24.99695 | -49.35924 | 2026-08-28 17:41:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 82d23a6d-4beb-3a9f-a62c-3b652c3612d8 | -22.73741 | -47.43566 | 2026-08-28 17:41:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 01c321bd-507d-3cbf-b38d-eda62289721d | -26.47191 | -52.68691 | 2026-08-28 17:41:00 | NOAA-20 | GALVÃO | SANTA CATARINA | Brasil | 4205605 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 12f440de-ed78-3dd5-a127-676cfcad6c92 | -25.55986 | -50.57439 | 2026-08-28 17:41:00 | NOAA-20 | FERNANDES PINHEIRO | PARANÁ | Brasil | 4107736 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 95836c4f-8b90-348d-948d-9c015fab29f3 | -22.84787 | -49.34388 | 2026-08-28 17:41:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 13abc0d7-5c4b-371f-bb25-a7879792687e | -27.82212 | -51.83335 | 2026-08-28 17:41:00 | NOAA-20 | SÃO JOÃO DA URTIGA | RIO GRANDE DO SUL | Brasil | 4318424 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d5704665-a6a9-3086-9be1-c46aa2d958b2 | -22.85235 | -49.33877 | 2026-08-28 17:41:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 02563ac9-9abc-3064-a15c-d5d8b4b7ee4d | -23.20099 | -46.98582 | 2026-08-28 17:41:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |


[Clique aqui para ver as próximas entradas](README135.md)
