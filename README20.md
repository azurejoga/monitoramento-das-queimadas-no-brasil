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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc7e714b-0247-3596-b74a-befb5bad4851 | -11.13864 | -44.48212 | 2026-08-07 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8f22aaaa-bf33-3896-8a39-34a5fc3bf55c | -6.95186 | -59.51937 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d09c47e-2c29-3482-bc67-4828872c5342 | -11.17929 | -54.86145 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 622f4361-b54f-3869-a9b0-cb9aefc13d7b | -6.54482 | -55.29446 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f477523b-f7c7-3c18-beeb-ca2183238297 | -11.17542 | -54.86444 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d62a92a4-5014-3009-8516-727fbd2521f8 | -12.00069 | -45.13591 | 2026-08-07 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f1009bf-cf15-3378-8fba-5740cc887e30 | -11.13176 | -54.9044 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68ba606f-3d74-3d78-b4ac-3e5235224ed1 | -6.63484 | -56.37652 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d157bc0a-46d7-37e7-b419-e67ca60907fd | -12.62624 | -46.89324 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0665596-61fe-3ca7-a30a-58e2f767980d | -12.87234 | -52.82211 | 2026-08-07 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dc78665-700c-3edf-ad7b-ca459fea0376 | -6.85518 | -58.9558 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e71d869-488d-3d2a-a0de-f80bf856dc14 | -11.14117 | -54.9095 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d07c1a7-8da2-3240-956f-9b28e8021fb8 | -6.8626 | -56.57364 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d391d131-94cc-3c49-b2ed-a39a588bce18 | -8.70854 | -62.87731 | 2026-08-07 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fc8c943-aa7f-370e-9503-7a37aac2afef | -6.70967 | -58.95687 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cbda06a3-1a0e-3cb4-afa5-bbaccdea7db9 | -6.60299 | -56.3562 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f01c60f5-2754-3693-a8bb-82e748192b11 | -11.13288 | -54.91899 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e965ef2c-b291-3e10-b7e5-f1581a083a97 | -11.14062 | -54.91301 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f19f1897-973f-3ae6-b321-e260feefda8c | -8.53984 | -49.55461 | 2026-08-07 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a45f3c1-91a0-3c13-90ae-5ff7d8919ce9 | -6.42064 | -55.79134 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50f75ea1-6e67-3b62-b94b-bd81acc0f502 | -14.43272 | -45.6654 | 2026-08-07 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47f50a9d-f7e9-34a6-9c83-839ab898f18f | -12.55464 | -46.95808 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 704016aa-e0a6-332a-9dc6-6cfe944d7c3f | -7.74689 | -45.02646 | 2026-08-07 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef2cc0f4-1a84-3a1a-be37-2c542763536d | -14.42645 | -45.66892 | 2026-08-07 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea558205-5e16-3dcb-a3e9-5e63238b09ee | -11.12735 | -54.91091 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d46ffd8-9268-3285-bc31-ad6e523faee8 | -10.63374 | -47.48962 | 2026-08-07 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b9dbdfc-567d-3544-8316-d4ed207d83a0 | -6.62115 | -56.37437 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d7a565d-964a-385a-997f-745f6e196f7d | -6.54719 | -55.15122 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b2512ca-4ee5-3be1-9a09-314b94b61872 | -6.54181 | -54.92905 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e567000-6b16-3897-894a-25f642cffe13 | -13.78274 | -49.72663 | 2026-08-07 05:04:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f45fdf6-6110-31f4-9ce0-9d8ead84f60d | -6.53334 | -55.15261 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 120ba2b8-dc38-3373-9ed6-82929e0a719c | -6.7316 | -58.58542 | 2026-08-07 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ef7fbd7-ccb6-348c-b6dd-12dafab6a1e9 | -11.1627 | -54.85878 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96ddfccf-2624-3f7c-975b-39ee6b126b36 | -10.92956 | -57.17245 | 2026-08-07 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b209b62b-1b7b-3c55-be8d-50153c3d9428 | -6.72781 | -58.58473 | 2026-08-07 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a2ed4a73-f7cb-3555-a77b-65e239f7cced | -12.01045 | -49.28005 | 2026-08-07 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73f6b5c6-9e74-30ff-a937-eb03f37a078c | -11.13452 | -54.88678 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2d2fa37-8904-3f52-921e-a0c7e4b34d8e | -11.14756 | -44.48215 | 2026-08-07 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3fc59f11-91d8-3b68-a6f8-55981df9892f | -5.98371 | -52.15455 | 2026-08-07 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fba45ad1-86ab-365c-a728-98350d420ca3 | -6.22762 | -55.61766 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1edf0eb3-cde2-3f9c-85a6-aeb918d3b518 | -13.96483 | -47.3695 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef212c53-861e-3217-b509-4d6937be3262 | -6.53905 | -54.92505 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f356cd7-67c4-31ea-be63-fd41f858b2f8 | -9.08759 | -59.48478 | 2026-08-07 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c4a2e0a-bb25-3d3e-86a3-b03982d8f9ad | -6.95126 | -59.52289 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ceb5723-899a-3413-8f06-1ef65f7b1808 | -11.17266 | -54.86038 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5916d00f-906a-3cf8-99f3-f0f24647d110 | -11.08531 | -47.80322 | 2026-08-07 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb993406-7dd0-3cd0-b0e2-be7cee304275 | -6.52979 | -56.54824 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98aa55ba-2ae6-3433-9792-3e2f37f2c75a | -11.16325 | -54.85525 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80d9be9e-c5a5-3bd8-b874-044b4079f1ba | -6.85435 | -58.96066 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe2ebead-8938-30d2-ab1d-4f91068ac259 | -12.57793 | -46.89808 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 528dc073-25bc-3e32-995c-8ab5a71b2b0f | -11.153 | -44.48754 | 2026-08-07 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b97d07c6-eb04-386f-9bb6-8f358027ca60 | -13.78359 | -49.72379 | 2026-08-07 05:04:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30956a22-a9ce-3e78-8d7a-cbca59fb18c2 | -11.14158 | -44.48133 | 2026-08-07 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a532a751-5575-317a-89a5-949d80c7e62c | -9.09147 | -59.48545 | 2026-08-07 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d3124df-b1ca-357f-bc7f-4cb35854075f | -8.37716 | -49.64791 | 2026-08-07 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8182d85-49ce-3775-a6d5-a03e9894dac5 | -11.14172 | -54.90598 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da1ed0a9-c90f-3ce1-b863-c4f052d2c247 | -13.93882 | -47.36858 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e6974ad-ba2a-3232-9524-42c19aa5a9ce | -6.53385 | -56.54503 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5828629f-2d55-39cb-a282-486016b55f3b | -12.5543 | -46.96082 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 235f2a78-27a7-3e64-80ad-5569a5289922 | -6.73084 | -58.59004 | 2026-08-07 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b104fbba-5c59-3fa5-bfc6-78b00bdbacb5 | -12.86578 | -52.81684 | 2026-08-07 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e91754a8-f362-371f-a78b-ab1c92f39125 | -6.54012 | -56.54995 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85ddddeb-ff90-30d5-9661-8278c900de21 | -11.13508 | -54.90493 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 574091e6-6b8d-36a5-aae1-470484cab22a | -11.14559 | -54.90298 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3fdf210-74d6-37df-8802-4162ce9a083c | -6.53668 | -56.54939 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ea78f39-7872-3eec-acd8-42ea5e9b2232 | -9.0923 | -59.48057 | 2026-08-07 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cef9eb2-c836-34d1-ab94-60612398044e | -6.6487 | -56.42097 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7d84c45-9060-393c-9969-0dcbeede5735 | -9.28941 | -60.94086 | 2026-08-07 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbd5e1d8-98e0-3827-b833-00e951da6a85 | -9.28586 | -60.93607 | 2026-08-07 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a98f59e-ae2a-313a-a3e8-8fb9d803d12a | -6.85916 | -56.5731 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e75c65ae-544f-34b5-8220-90a4ff1fc464 | -11.15275 | -54.85717 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75bbb719-f735-34bf-9cd4-e1c6982d32a1 | -8.46824 | -49.56311 | 2026-08-07 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f474bb7-392b-3464-a63a-bf8d5cb448ad | -6.90937 | -52.82853 | 2026-08-07 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 353ea579-ddaf-36e5-8e00-89b65d26f60b | -14.26906 | -45.29071 | 2026-08-07 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c6ee7db-d578-3c1f-94aa-37f0d87526c2 | -12.00507 | -49.2849 | 2026-08-07 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c30c7b5-f066-3fc2-869d-5a30d9f594c1 | -6.54134 | -56.54242 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9056e37-0b45-38c6-b088-0b9317f2ff5a | -7.75815 | -45.02855 | 2026-08-07 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e724a603-7331-3d12-a768-609d72351531 | -10.93286 | -57.17636 | 2026-08-07 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b87027aa-2580-3b29-9db9-ea70a5309288 | -11.15994 | -54.85471 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19950697-cb87-30c4-9a17-843cb24a2204 | -6.53041 | -56.54446 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d772485-dad7-37c9-ae66-632f9c8b1a5f | -6.90542 | -52.83162 | 2026-08-07 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d0e6c68-288f-3cf9-8b1f-785c888c6750 | -14.42551 | -45.67722 | 2026-08-07 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05980f22-4d4a-3b93-ac25-2e7db90ae5ff | -13.96288 | -47.38502 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ade86f04-9b19-3ff0-96a1-d21891921f9d | -11.13398 | -54.91196 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27e33960-9305-33b7-9b2e-cf850d8da863 | -6.55326 | -55.17727 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16744c95-e350-3977-80a9-087759e0883d | -11.17819 | -54.8685 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86515142-8c3b-39b7-b72f-82bc28ebfed6 | -7.74711 | -45.027 | 2026-08-07 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07040930-4faa-356c-825f-1c63d203aafb | -6.60761 | -56.3493 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55ed492d-8e59-3b2d-aeaf-5d0a93cc3dc7 | -7.75793 | -45.02804 | 2026-08-07 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38050851-4a1e-3979-9bc1-4feb6d7c268c | -6.61177 | -56.34595 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b72e6b9-4d4f-37cb-88fb-3543b2ec5210 | -11.17874 | -54.86497 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37a4d7d2-a04b-391a-9ddb-313c054503fb | -9.17956 | -58.07103 | 2026-08-07 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dfd3195-a9bd-3174-b037-c7e9fcbec6a4 | -11.17598 | -54.86091 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 979cf006-0e00-3f6a-a897-a4025e92fdbb | -11.19958 | -54.8396 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73a89a58-94cd-39cc-8735-523e01fee801 | -6.71356 | -58.95757 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b5855b6a-c255-3ee0-850c-fd9a31f91ab3 | -11.31911 | -45.20509 | 2026-08-07 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec4a46d7-fe17-3cf8-9d13-8ec76b4cdf8c | -12.56308 | -46.93251 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec530b7b-1c72-3003-a55a-bb914dad3573 | -5.68783 | -53.75594 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b95fea94-4e4a-38fb-bf94-07c04c8de679 | -12.54913 | -46.95996 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae9029ef-a5f1-3515-be09-f8d0774da1cd | -10.60719 | -52.22464 | 2026-08-07 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README21.md)
