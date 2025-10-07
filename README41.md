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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e15468a2-3781-3712-8e9f-a5c67d6e37e7 | -19.13115 | -46.43451 | 2025-10-07 04:10:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a7f2dc2-e624-3a19-822d-e22414097423 | -18.1628 | -53.36469 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7625b934-1bfe-368b-b7e8-4fb4c21b327e | -12.41584 | -50.26381 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e634bd74-54c2-367e-83b6-e4e24b669ac2 | -14.77298 | -46.04946 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 4ad11141-6c4c-3f0f-8ce1-05cb04bfcced | -13.33084 | -48.0384 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdac331a-b955-3f0e-aa4b-39e821542f14 | -13.78488 | -50.78303 | 2025-10-07 04:10:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c182d95a-b794-3730-8b76-a2bf39e42ccf | -14.00172 | -44.09632 | 2025-10-07 04:10:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfa53001-2fa2-3eee-a73e-6df82424225d | -19.93053 | -46.7254 | 2025-10-07 04:10:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c214cd3a-c54f-3b20-8a84-ccf5e7a9541b | -12.18779 | -47.78965 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42ee0fd6-108c-33dc-900c-de01a0901d97 | -16.29571 | -50.9843 | 2025-10-07 04:10:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 593c948d-7eb0-3553-a6cc-3949606dd481 | -16.38242 | -48.99752 | 2025-10-07 04:10:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9080d7c-ae81-3fcf-9cb9-09565d4e2f86 | -11.38437 | -54.35111 | 2025-10-07 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3456739f-fa12-3dee-9f18-685b9765db7c | -14.52016 | -46.92387 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccde406a-6c01-323a-9e6c-e03afbc30437 | -13.06387 | -47.92713 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b51ead5-a2db-3325-b425-c7f8b2e16195 | -16.00826 | -50.82396 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72b47ccf-fd4f-3e11-a3a4-ae7dd81b079d | -13.64485 | -47.28603 | 2025-10-07 04:10:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f127314-1535-382c-846e-0ba523a14bed | -20.12495 | -44.41078 | 2025-10-07 04:10:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b861982a-357a-325e-af7f-a599d0572cdb | -15.36539 | -47.32231 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3103a1e1-e9b1-3348-8e0e-84fc82d4d0e3 | -17.56563 | -46.07368 | 2025-10-07 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 624060a7-092d-3e0b-b3db-5fb54c6b440d | -14.77513 | -46.05808 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 19d13063-03c1-38f4-9215-0a5f4f5f871e | -14.75192 | -46.0253 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d07b940-ae6e-30c6-907c-dadcaea0905d | -14.75115 | -46.00859 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41c55f9a-bd59-3aed-99ea-53cf584225ef | -13.2654 | -47.18176 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 299a31eb-5a7f-35f8-aeed-359b35664f05 | -14.91323 | -51.40711 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 87beb0f2-8d3c-30b6-b6cc-eb60a1d99a29 | -19.7881 | -45.845 | 2025-10-07 04:10:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 57785d11-e7d1-34b1-b2b9-43c12db1c602 | -13.59316 | -48.68596 | 2025-10-07 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f7ebf3f-bc11-342d-88fa-31f20fe3d3b3 | -19.5837 | -44.63205 | 2025-10-07 04:10:00 | NOAA-21 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b6566ef-21f5-3ff1-9d0c-7266443cf89e | -19.87927 | -46.73676 | 2025-10-07 04:10:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76d3fea9-22a7-34b1-b229-df97819d7fcf | -15.05753 | -42.34015 | 2025-10-07 04:10:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 63.7 |
| a7193f6e-4242-3560-b5b1-632e22ba8bcf | -17.56968 | -46.07039 | 2025-10-07 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49fc0211-b351-3085-9a9b-16832c55a615 | -14.50196 | -46.92057 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2641c1a-b90c-3020-b92d-e05d5a6d4168 | -19.38407 | -47.42485 | 2025-10-07 04:10:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc3ceb0e-d3c6-3cbf-8351-fa7b5d7c6ee1 | -18.4023 | -43.22816 | 2025-10-07 04:10:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c6048062-bba6-3d25-a765-994a25eba554 | -12.37039 | -46.49951 | 2025-10-07 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4030f41c-6b9b-33d1-b641-197d20e110fc | -14.71133 | -43.959 | 2025-10-07 04:10:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e6c3f83-c0f1-3256-9740-91b73fbd300b | -17.57005 | -42.93487 | 2025-10-07 04:10:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92c94351-4e92-3e91-b65f-1aeb1ef76be5 | -15.98487 | -50.84868 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39a15b0f-77cc-372f-a889-58bb1b894fb4 | -13.72569 | -48.20259 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b56091f8-ff3f-3814-9b9e-c2aa24de71d7 | -18.97389 | -47.83078 | 2025-10-07 04:10:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4b2aabec-abb0-3335-8ab4-346fcb65bd34 | -14.28338 | -45.8442 | 2025-10-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 682f4b82-b46b-3b8e-a254-852ecf26995f | -18.84246 | -48.29456 | 2025-10-07 04:10:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 605687cf-4502-3ceb-9a1b-8f0c08b1210e | -19.6648 | -48.49815 | 2025-10-07 04:10:00 | NOAA-21 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff87a078-adec-3d1e-afb0-1b0c92d4b0b5 | -15.76457 | -47.77477 | 2025-10-07 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 298de7d0-5a90-3098-baa9-36b50a67cd05 | -14.92144 | -46.80192 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db72c837-4957-3e50-b0b6-2156b52ce498 | -15.99864 | -50.95361 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c75bd42-ad28-3697-96e4-7e3d7bb95579 | -14.92108 | -46.86863 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d6eaf52-ab83-331c-9802-f6bcc5517976 | -16.11453 | -48.94145 | 2025-10-07 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6a681e78-66b7-379e-9b78-133ea6760607 | -12.34477 | -47.05688 | 2025-10-07 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6667d197-aac7-3c7d-8355-68e300d1af77 | -13.28756 | -47.57026 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ed7fe52-856b-3446-8c71-6dc202b73ec5 | -13.26828 | -48.46492 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 000935a2-fb4e-3963-902a-a650851fca23 | -15.51012 | -46.83119 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a651143-a818-33ad-9e8d-ee4db15d2084 | -15.58428 | -52.55123 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6795f43e-f4b6-384a-84f4-38ae80bf43b3 | -13.39148 | -47.57744 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 372ef854-2911-3284-a514-e89e5202632c | -15.5602 | -46.83069 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d9cde6a-9612-30b9-ba11-a21b9c208801 | -15.99137 | -50.94248 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 276a26f7-961b-3ee0-abbf-a53506796f2c | -19.65348 | -43.89436 | 2025-10-07 04:10:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ebe1a81-49f0-37f0-8d33-48e1945c68cc | -14.7352 | -46.01817 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 5c1b63ad-10dc-35d8-96b1-a68de037b222 | -10.8105 | -56.23753 | 2025-10-07 04:10:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e3eec9a9-0860-3891-b8a1-f51871da953a | -13.25645 | -47.16628 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc50dedb-a50b-3f79-b22e-903ec1441f17 | -18.15702 | -53.36688 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95cf938a-a16c-36ef-a4c3-44ea67b00778 | -18.82786 | -45.40441 | 2025-10-07 04:10:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fad84112-748e-31cc-9c16-1a4f3a7cfb50 | -14.64222 | -52.53731 | 2025-10-07 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4fd844f-a332-34d4-856a-60beb44e8eca | -14.94394 | -46.82227 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4783d02-2247-3fdc-a734-4bc182a39fa1 | -13.72606 | -43.85995 | 2025-10-07 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f9dbed0-8abd-3c5b-b8b0-cd485b4b04cc | -20.28767 | -44.45728 | 2025-10-07 04:10:00 | NOAA-21 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 383ffd1c-7043-3870-9bbd-41dc60d1889a | -14.49681 | -46.92868 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dde08210-d8fb-3502-86b3-314916b91571 | -16.28674 | -50.98202 | 2025-10-07 04:10:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8135e7f6-e3d3-3604-8aaa-4138dbc8dbbf | -13.69055 | -41.33774 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f0b0056-21d5-39e8-9ac7-b4d7505c56f1 | -13.07153 | -47.88261 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e1fb8e0f-8402-3b2c-b6b5-90230d81c020 | -17.97866 | -44.98819 | 2025-10-07 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a16e2b6b-0e65-38fd-be4f-a10c14386f40 | -15.57659 | -52.56356 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e91c01c3-980e-3831-8814-ae1959ec7ce9 | -14.93196 | -51.43674 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94cc8688-f53d-318f-a7c2-f1d31e33e41d | -13.2587 | -48.06068 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ab225b53-b8ff-37a6-b361-4c71b7e0bc2a | -15.21937 | -49.31366 | 2025-10-07 04:10:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf11babb-cb73-3ef7-8acc-c41eb414758f | -14.76801 | -46.03629 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 24006ec1-c47a-3791-ab6b-f3398783091c | -17.02894 | -43.45209 | 2025-10-07 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17de4f2f-fa5b-3d3f-bde0-638dae2b41bf | -14.77165 | -46.05745 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 46.7 |
| e8687f5b-d447-3b5a-9443-3dcde6cfb61a | -14.72612 | -46.00829 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae40877b-aaee-3dd0-8dba-9d562c72358d | -12.94102 | -46.80978 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae65040f-9b37-32f7-b8a9-e794b676ba82 | -14.9071 | -51.43943 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19747e64-8427-3702-8a9a-1f52dfdea9f6 | -14.94755 | -46.82283 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c39be01-328e-36c7-94d0-303d8aad8e4e | -15.58244 | -52.54887 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e148772d-8333-391d-80d5-d227418fce82 | -18.78254 | -44.62094 | 2025-10-07 04:10:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8e4d26b2-e2b4-3b80-b249-34ba3241c060 | -13.67054 | -44.05907 | 2025-10-07 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 345d3337-7cf3-358e-903a-d7aacf666119 | -15.17326 | -52.76452 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 590afa2d-54e6-39e7-9c06-1cc16701cf26 | -16.04765 | -50.96867 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 118e198b-714c-3f9e-904e-7d107a31aaa7 | -14.92929 | -51.42504 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 99faab2b-97fb-38c8-8d2d-8039a410bc25 | -15.36173 | -47.32156 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de43be02-0f0b-339f-a574-6a2728b9590f | -12.98706 | -46.78545 | 2025-10-07 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a5982ed6-16a9-3892-aa52-62660269b419 | -13.37162 | -47.24282 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2d374ed-6924-3a7b-b080-9119ab11e610 | -18.16122 | -53.37229 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab68d292-3b7a-30de-9397-306b00953092 | -15.20547 | -46.37643 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5269faab-b364-3729-9f0c-76abf756bf73 | -12.94471 | -46.81044 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5a15251-68ba-3ae5-8a90-86b7ed0142c0 | -14.91383 | -46.8675 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f44652f5-a0a7-3296-bea7-a516c40de0c2 | -14.70349 | -46.00533 | 2025-10-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 152414e6-2c4e-3544-b2f1-0a12228f39f4 | -19.71103 | -44.11837 | 2025-10-07 04:10:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a25a278-b193-358e-96d8-419b65d5621a | -14.90827 | -46.83513 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e623927d-f82b-3afb-a9b5-064bf7bdb077 | -14.90886 | -46.85317 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae7b5b2d-830a-3b19-8a89-31bae1d17215 | -13.0823 | -47.86615 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4c06cf8-15e8-380a-a8ae-75dd8936f45f | -13.31394 | -47.7686 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README42.md)
