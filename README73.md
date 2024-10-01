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
| 0346d296-4b97-367f-8d57-88733da5c3a6 | -17.78469 | -42.89531 | 2024-10-01 04:14:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 626fbce2-2c2c-358d-9017-7dd0a08eb4b2 | -17.77887 | -42.8101 | 2024-10-01 04:14:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8118779-a185-3861-972d-18aefad4ab85 | -17.77592 | -42.80542 | 2024-10-01 04:14:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34f83741-d53c-3f37-adfe-f72d80a360e1 | -17.77357 | -42.56448 | 2024-10-01 04:14:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3bff5973-6736-3cef-824e-9edb7bdc99ce | -17.72513 | -42.34816 | 2024-10-01 04:14:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b3b50d5-91e8-3852-9906-d792e22f2a3d | -17.72451 | -42.35256 | 2024-10-01 04:14:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8ee6642-4805-36ec-8c86-1ac80b14bd13 | -18.34448 | -42.76471 | 2024-10-01 04:14:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 36372483-371f-3e98-bf07-26f8380ff4c0 | -18.85018 | -42.56665 | 2024-10-01 04:14:00 | NOAA-20 | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 38241b3a-be5c-3f4b-a389-cf709ca04887 | -18.53577 | -42.65643 | 2024-10-01 04:14:00 | NOAA-20 | CANTAGALO | MINAS GERAIS | Brasil | 3112059 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 02e0897f-764e-3258-8fd3-3be1819cd167 | -14.42565 | -43.43637 | 2024-10-01 04:14:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a33abf6-945e-3424-bac9-291df22a6050 | -15.44756 | -43.62501 | 2024-10-01 04:14:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dc08e3c7-098c-3459-bb4f-73176257b8fd | -15.77263 | -43.58067 | 2024-10-01 04:14:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f93c062c-8fad-34dc-90ed-0f0bd88f342b | -16.34931 | -43.69693 | 2024-10-01 04:14:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b52da6c-c5f4-32f3-9e54-e649428defb2 | -15.91235 | -42.67153 | 2024-10-01 04:14:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 45c3fd8c-fb6a-3afb-aebf-32427cb6b2d6 | -15.44811 | -43.6213 | 2024-10-01 04:14:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c9ac6ba6-e36a-36f2-926a-1e6e95ff5cd3 | -17.99759 | -43.68913 | 2024-10-01 04:14:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f72379a6-707c-3007-a99a-16bf114a399f | -17.63017 | -42.99337 | 2024-10-01 04:14:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab39fd0b-d43a-3a36-abe2-6e122cec9e6a | -17.61382 | -42.9824 | 2024-10-01 04:14:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a027eca-0a90-381d-8525-45d26edc90ce | -16.86907 | -44.12253 | 2024-10-01 04:14:00 | NOAA-20 | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8cbd5be5-301d-3dad-baf6-7f33f2613ad9 | -17.78196 | -43.29523 | 2024-10-01 04:14:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bcde248-fe12-3a96-af9e-407158aea828 | -17.0958 | -43.80491 | 2024-10-01 04:14:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9846dbca-fa45-32ee-9371-7e39d551cf1e | -17.61439 | -42.97845 | 2024-10-01 04:14:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c2789e8-8453-32e3-947c-b92b8a24795d | -17.28308 | -43.19653 | 2024-10-01 04:14:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02f4df16-5857-3350-9e1c-318fe6b957f0 | -17.27903 | -43.19999 | 2024-10-01 04:14:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00fa42e3-dca1-3a07-92ff-0b214b11a686 | -16.68142 | -43.88303 | 2024-10-01 04:14:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b017d639-3e18-34a7-93d5-c5101e953493 | -18.66714 | -44.26684 | 2024-10-01 04:14:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eafa5d34-5741-3bf9-a1bf-2b9dfc60d1f3 | -18.66376 | -44.26628 | 2024-10-01 04:14:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bd414e8-4f42-3aac-aee9-71dfa67333ac | -18.6757 | -43.68369 | 2024-10-01 04:14:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ff024bb5-a31b-39ff-a7d0-939c09c6b09b | -18.37588 | -44.0154 | 2024-10-01 04:14:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d5e0c3b-6fca-35ce-896d-06d044b156b1 | -18.37194 | -44.01854 | 2024-10-01 04:14:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2be0bae5-db3d-33a2-a3f5-e09af703497e | -18.67709 | -43.68082 | 2024-10-01 04:14:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 58f78f3e-63aa-3722-9d52-e7bcddb2c109 | -18.5355 | -43.47208 | 2024-10-01 04:14:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 18cb6b8f-8eb3-32f6-87fa-7fbd8df3f50c | -18.6765 | -43.6848 | 2024-10-01 04:14:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 549fb9a8-b67f-3656-93ff-a35803eaece8 | -18.53606 | -43.46817 | 2024-10-01 04:14:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4bbd1f6e-2d7e-3fae-8051-fc67e8bd8626 | -14.17538 | -46.46823 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74b0bbcd-86be-39fc-8a17-6cf6f635050b | -12.15699 | -44.69503 | 2024-10-01 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c7ffb62-3e03-38a3-b3aa-b8ebccd351ab | -11.2587 | -43.38295 | 2024-10-01 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1311958a-6060-3453-8f89-a551e079d48e | -11.25592 | -43.37888 | 2024-10-01 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b8f79aa-cf66-3a0a-ba64-04afd89c3352 | -11.25538 | -43.38242 | 2024-10-01 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d69c3bda-7b52-3936-a50e-d1899615f7be | -11.25429 | -43.38949 | 2024-10-01 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dfb06d73-df0c-3f90-9fbe-63f74073d131 | -11.25096 | -43.38896 | 2024-10-01 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 54ee5de3-8b5c-32fc-bfe1-516d29a6945a | -11.25042 | -43.39249 | 2024-10-01 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ce52cfc-ec12-3047-b14d-c6f2628e6279 | -11.24819 | -43.3849 | 2024-10-01 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4a8463d6-0745-3ef6-be6b-81a0b7c6ee64 | -11.24764 | -43.38844 | 2024-10-01 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b7bc14b9-e64c-3e16-987e-421110884c45 | -11.2471 | -43.39197 | 2024-10-01 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ff75c99-dae5-32fb-8710-78851148f231 | -12.98776 | -44.72583 | 2024-10-01 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2701508-f588-3bb5-93fc-1066f30601b1 | -13.45151 | -43.77756 | 2024-10-01 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5ef0818-5ac1-3dd9-8a14-d86b4c582674 | -13.44818 | -43.77702 | 2024-10-01 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00797424-9bcb-320a-890a-bf85615cb104 | -13.44353 | -44.02462 | 2024-10-01 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8d62ac3-d6e2-3e2b-813c-9cfd8de1d260 | -13.44021 | -44.02408 | 2024-10-01 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90545a63-4432-301b-b233-0445ae24ffde | -12.43497 | -43.74357 | 2024-10-01 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82bc5a4f-6ded-34fe-ae31-880a857e1706 | -14.60736 | -44.83536 | 2024-10-01 04:14:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d52f51a-a816-3a8a-91ee-e341405eb0d5 | -14.55485 | -44.86753 | 2024-10-01 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4b7defe-43c4-381f-b7bb-c79494de13f8 | -14.55433 | -44.84922 | 2024-10-01 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7366eebb-7006-3bc3-9cdf-7cfc449cd1f1 | -14.55429 | -44.87108 | 2024-10-01 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec098f66-ca48-3aff-96b5-bf083fb0330b | -14.54771 | -44.84813 | 2024-10-01 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 312456dc-74fc-3ad3-9bc2-5974fb2dae3f | -14.49869 | -45.07302 | 2024-10-01 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3978d2e7-f002-341c-9769-491258226872 | -14.49541 | -45.24391 | 2024-10-01 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1f39c77-cfe5-368e-8800-9e6ab8b7e61b | -14.49266 | -45.23979 | 2024-10-01 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87b0d7a0-45b1-3dac-8dd3-d9a574360315 | -14.48992 | -45.23568 | 2024-10-01 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5165a030-e7b8-32c9-847a-024b0034ec94 | -14.48717 | -45.23157 | 2024-10-01 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e4c5d035-20df-320e-9157-cafa4a7ef09a | -14.10151 | -44.40039 | 2024-10-01 04:14:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b67ed00-518d-3757-b0f9-0d90caf750de | -14.0982 | -44.39985 | 2024-10-01 04:14:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63596419-6326-37e5-b03b-458ea1a416a7 | -14.45248 | -43.86242 | 2024-10-01 04:14:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f1e7073-c9ca-3cc3-90d8-decf6b0cefbf | -13.98618 | -44.09351 | 2024-10-01 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 464400ca-0289-3103-b357-6e6e5c8dc54c | -15.4064 | -44.30285 | 2024-10-01 04:14:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 51e32e42-e3d5-3dab-84c1-1615eafad4d1 | -15.88663 | -45.05741 | 2024-10-01 04:14:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 765b9f43-277f-3bf1-ab01-e076251db98a | -15.88607 | -45.06098 | 2024-10-01 04:14:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aaa2ad0-2146-383b-8176-4de788b74f75 | -15.88551 | -45.06456 | 2024-10-01 04:14:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef61f5d6-003d-3c20-9807-74c3cd051fc4 | -15.63809 | -45.16994 | 2024-10-01 04:14:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7f73ef8-bdae-37ac-b980-73434021b986 | -16.89306 | -45.30943 | 2024-10-01 04:14:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9984031-661e-3135-83df-40af3a896d1c | -14.16922 | -46.46328 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02cd38a2-f225-3df2-b420-86e76436d0a1 | -10.87421 | -44.79321 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32944bc6-43b1-3490-bd7e-851a93399c62 | -10.87364 | -44.79675 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d086dece-c7fe-3f3e-ad63-975dd55d95ce | -10.87252 | -44.80382 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b81e9acf-dc92-3bce-b62b-5c1b69c07898 | -10.87195 | -44.80736 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16a17097-a35b-3dc1-8782-52c13b971738 | -10.86919 | -44.80328 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc730fa3-1596-36ba-8c63-65e51290d0ae | -10.86863 | -44.80681 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fad6aa1-1414-31c3-9797-ff9e98692316 | -10.86587 | -44.80273 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6be55df-8e0f-349c-9b10-9e5734ccb281 | -10.86367 | -44.79511 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f6ff5f6-ac29-3bd2-8c33-b55c90093ad1 | -10.86311 | -44.79865 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2fdfeda-20df-3610-8d4e-9f10763ef043 | -10.86035 | -44.79457 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3fd8ffb-ba7e-3e22-a995-ef5141ed76bd | -10.85979 | -44.79811 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 100bcc13-8dba-3659-ab51-c082b32b895d | -10.70914 | -45.90651 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dfb54bb-1e65-3624-93b4-1e6394c0552b | -10.69069 | -45.86889 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd9a042b-b66a-3aec-9507-82dd92cf482a | -12.09701 | -44.98614 | 2024-10-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88cfefaf-3282-3ef3-b381-5efb0c2472ef | -12.09645 | -44.98963 | 2024-10-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e149fca3-0682-3d85-acae-8245f49d21a0 | -12.07134 | -44.95629 | 2024-10-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 350644c7-6d70-35d9-b455-83f0e3627e0b | -12.07078 | -44.95983 | 2024-10-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6bd083ff-074d-33f3-aae8-1d7b921ac9a1 | -12.06802 | -44.95574 | 2024-10-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e7b1664-57b3-372c-a08e-d97e9219dc6d | -12.06746 | -44.95928 | 2024-10-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28b0ffbe-e576-3e12-92d0-4bf66ef256e0 | -11.78683 | -45.43357 | 2024-10-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdc719ed-45d2-33a4-958b-ba661017dee1 | -11.29002 | -46.15221 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81054da6-1dd5-339b-bf33-44d827cd65a9 | -11.26638 | -45.6505 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 8bc64fd3-a245-3618-bdcc-b328e57248c3 | -11.2646 | -45.66154 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f51ac578-0a02-3323-8d67-07ad42b0aa6e | -11.264 | -45.66522 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0e8b319-d408-36a8-9d5e-473fecfa5e8a | -11.263 | -45.64995 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94ade0ab-86e5-346f-936e-a8558fc237ea | -11.26241 | -45.65363 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecea6375-d83a-3720-b959-8e8674fbe43e | -11.26181 | -45.65731 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c49d423c-98c3-3e7f-aaf6-8aa812e6c45a | -14.1726 | -46.4639 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README74.md)
