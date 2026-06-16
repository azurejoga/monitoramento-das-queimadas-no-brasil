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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee7c10b3-4a2a-3ef4-8470-2326313ab59b | -9.32686 | -45.47657 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 415c3ba2-56af-3333-8c9c-86bfb87ac466 | -12.85111 | -44.37153 | 2026-06-16 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| b9b60e80-b60f-3a35-b49f-3603ceb31f79 | -10.63827 | -51.80046 | 2026-06-16 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5d5d117-7067-3aa1-bc1e-a4f522ca00ab | -10.1491 | -56.59583 | 2026-06-16 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0c3e753a-7a5a-3bcc-a6b4-11345654f9af | -9.34545 | -45.47511 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b044dfd7-e743-3b13-9a4d-cfbe757669ac | -12.84662 | -44.37448 | 2026-06-16 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 6273d56c-29fd-3dd7-9b18-0c743fdb28da | -9.22717 | -48.58765 | 2026-06-16 04:38:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad1923ae-5972-35d4-9c1e-624f258d91e1 | -10.90359 | -54.13269 | 2026-06-16 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fe23c9b-c294-3da5-910b-6879bc341f32 | -8.85452 | -50.19012 | 2026-06-16 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 596d25b9-20d5-3587-9ffb-18e9a468896a | -13.21226 | -45.48651 | 2026-06-16 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0061f2bd-c5ee-3e9a-b1bf-8a61b78101a7 | -11.55307 | -52.77886 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ec33d1ba-989a-3f5a-b0d6-53a080e5f875 | -12.44677 | -44.75161 | 2026-06-16 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f21313a-5d71-37fd-a96d-fd4073e84f0b | -11.91601 | -57.03839 | 2026-06-16 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdf3549a-f148-33d8-b71c-87768e7768ae | -9.20896 | -47.33997 | 2026-06-16 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d73a1137-5313-3a01-8b0c-9ebf489f22e7 | -13.54465 | -47.86436 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fffd63b3-ae6c-392b-9313-d2c62098ecbb | -14.78266 | -50.63142 | 2026-06-16 04:38:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc60b53e-6576-3ea1-9c36-382038ef3301 | -10.58837 | -51.77593 | 2026-06-16 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b612fe1-f58a-3511-95a4-d4b8036fedfc | -11.31421 | -54.46402 | 2026-06-16 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df789c66-9196-3162-b5d0-100f971a6097 | -9.36159 | -46.48821 | 2026-06-16 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36dbca28-f9b4-3bb8-bbd0-1b07e0fb5a0a | -12.92494 | -54.22633 | 2026-06-16 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 618f46a7-6762-31df-8584-0113930fddfd | -12.8021 | -54.8643 | 2026-06-16 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69ded1f3-4161-350e-aa34-94f3d1f57df4 | -10.57482 | -57.31648 | 2026-06-16 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31a05895-496e-3bd3-be04-88e0ef086ba5 | -16.63827 | -46.86022 | 2026-06-16 04:38:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5da0b09c-1d01-33e9-bead-ac359f8583f3 | -13.55088 | -47.86914 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6cd0594-62be-3b8f-82d8-aa277420bff1 | -14.10674 | -59.45777 | 2026-06-16 04:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd373a8b-3830-3266-8f4c-e31585847b9d | -9.21567 | -47.34102 | 2026-06-16 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89b915ea-8942-3916-93c1-b4817826afeb | -12.92191 | -54.22048 | 2026-06-16 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 69b6f806-ef14-3d3f-805a-ea95e4572626 | -13.54749 | -47.86861 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f272d681-b331-389b-9aab-e45881d3b5a5 | -9.36847 | -46.48927 | 2026-06-16 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48759a4c-60be-3db6-ada1-ea54c68bfcab | -10.71035 | -49.66452 | 2026-06-16 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74c2934b-f5b7-3a9b-9af1-0f313d522743 | -9.37014 | -50.53699 | 2026-06-16 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 679e5abf-d0cd-3e9b-8240-6038b1abd2a9 | -9.38333 | -48.43721 | 2026-06-16 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39e845e6-7584-3eb7-87c9-db4deeed6055 | -11.34953 | -51.4079 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85ca2c9b-87c1-3e84-b76f-758e1d58f73c | -13.54295 | -47.85266 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c39a11c8-df50-3c05-8898-b362e59bf761 | -9.2632 | -48.57498 | 2026-06-16 04:38:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9a7150b-7856-3989-973b-a85cc02e2bfc | -11.91381 | -55.91297 | 2026-06-16 04:38:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f743ec4-6fcd-3f42-8151-92893ea5f38c | -10.13592 | -52.402 | 2026-06-16 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a46177b-7016-360e-895d-ee4da058a6bc | -10.13962 | -52.40263 | 2026-06-16 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 355f4099-c0cf-3af3-adb9-824206b89cfe | -10.0863 | -52.18227 | 2026-06-16 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7b8c281-4638-3a41-b86b-f59c945dd7a7 | -10.90296 | -54.13633 | 2026-06-16 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26868a56-f148-3e48-814e-cb5f8b8a6bca | -9.20776 | -47.91233 | 2026-06-16 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc050068-11f1-375f-9753-aae9e1ca2937 | -11.54591 | -48.26788 | 2026-06-16 04:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 94e51245-3306-3ff1-a2dc-56d20ccd6e05 | -13.55711 | -47.8509 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4147913-8688-38b8-a788-0392aa33f797 | -11.59172 | -55.33484 | 2026-06-16 04:38:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 492cdda7-9505-309b-b0df-e8a675a6c1ce | -10.15198 | -56.60749 | 2026-06-16 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d1c37775-b5b5-336f-bb47-d40317c6957c | -10.58481 | -51.77532 | 2026-06-16 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a328f43c-d939-391b-8c7d-a823bf84f4c8 | -9.62843 | -49.01311 | 2026-06-16 04:38:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1df3efe3-dcee-3d1b-8322-a02fa70c107e | -11.7906 | -56.9948 | 2026-06-16 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e88ad40f-adfd-3572-8347-8391df5aaa6e | -9.26596 | -48.57899 | 2026-06-16 04:38:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fb06315-b221-3052-8a5e-72018b1a11e0 | -12.14644 | -48.46537 | 2026-06-16 04:38:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41d74620-d3b4-3714-8c8b-b94f69981574 | -9.36503 | -46.48874 | 2026-06-16 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b4df1a1-d899-3f59-9e2e-e46e17708791 | -12.02744 | -47.80605 | 2026-06-16 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6ff8fbb-b5d1-3022-8d59-58d098ce1d55 | -9.37356 | -50.53756 | 2026-06-16 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcd8664f-f4e3-3833-abd4-f74c28c17d0f | -10.08614 | -52.18358 | 2026-06-16 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9664515-50a4-31c8-8a42-89cb9ad7e25e | -13.56163 | -47.86695 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd5530f4-c1c8-383f-802a-1e82ea8d0e44 | -12.67733 | -54.58104 | 2026-06-16 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d62e8bd-30d5-39cb-b773-e9d632d8bc76 | -8.97702 | -47.97597 | 2026-06-16 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29b438b8-3ffc-3100-9353-8336befb12e2 | -11.59605 | -55.33565 | 2026-06-16 04:38:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae7cfc75-443b-3665-8bc7-ba82790d8149 | -9.22992 | -48.59166 | 2026-06-16 04:38:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91078850-9eb0-3def-913a-201cf14dfb61 | -11.48232 | -57.10567 | 2026-06-16 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e47b4e6e-b35c-3e46-a51c-9a2e06d08101 | -12.92099 | -54.22561 | 2026-06-16 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a699564e-374e-350b-9366-9d89fe19cba5 | -9.26651 | -48.57551 | 2026-06-16 04:38:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3e04198-3a70-3246-a0b6-9a3ca0568388 | -12.90825 | -54.22862 | 2026-06-16 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f74208c8-06c7-312b-879c-31b8f5ca9bf2 | -9.96685 | -48.33419 | 2026-06-16 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65081561-2aea-3b9c-b14b-9bd463e7af8c | -12.13482 | -48.25924 | 2026-06-16 04:38:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ca332d75-a592-32a6-bf7c-239c18364409 | -11.78235 | -54.0114 | 2026-06-16 04:38:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0218146-f354-3913-b6e5-c52a613d41d4 | -12.9043 | -54.22791 | 2026-06-16 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49ae4aef-c2e8-3940-bac7-3b1b9b756dc4 | -11.47904 | -57.11084 | 2026-06-16 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7f83169d-5a52-37b2-b465-b78480b4cf28 | -11.47801 | -57.11647 | 2026-06-16 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eef31292-9216-30d8-bcf6-14e455486ff7 | -13.56051 | -47.85142 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d7d5d95-225e-3aca-a293-e39cf959c470 | -10.35774 | -54.09797 | 2026-06-16 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0215a1c-9199-3911-ad10-162d89b6f36a | -11.26153 | -47.52059 | 2026-06-16 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e802c547-23c7-3bc1-9450-4eec6a728b97 | -13.5656 | -47.86368 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bde9102-d105-31c8-9ed0-48e2ce7b0c1a | -9.26903 | -50.6594 | 2026-06-16 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d22d931-72a2-3cf3-95fd-0720fc19c54e | -9.34483 | -45.47928 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 067bdf4d-e864-365d-92c4-af6078a15339 | -17.80321 | -46.70433 | 2026-06-16 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d8c88d7-97fb-3b8c-a6e7-dbf4af9ab1c0 | -16.45153 | -53.65477 | 2026-06-16 04:40:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31ee4615-0545-332c-a163-f7b3ce88b785 | -17.60225 | -46.67826 | 2026-06-16 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b8e5431-0d6f-3286-a9e2-064efbe5968d | -20.8188 | -45.17389 | 2026-06-16 04:40:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ea86a99c-205d-36d7-9ac1-b6e236fc3734 | -17.80757 | -46.70024 | 2026-06-16 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e2a3192-53c5-3055-a805-4a848d3c6724 | -17.80385 | -46.69965 | 2026-06-16 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35d6eb18-2a42-3d94-9988-3729bf1d4762 | -28.32706 | -51.19481 | 2026-06-16 04:42:00 | NOAA-20 | MUITOS CAPÕES | RIO GRANDE DO SUL | Brasil | 4312617 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 476c35fd-7f43-39db-b8da-7bf5a9d5167b | -12.8548 | -44.3625 | 2026-06-16 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 11fa6d02-628e-3392-9482-5c636334fdb3 | 4.50726 | -60.78051 | 2026-06-16 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3adee93b-7a46-3089-8437-97a627ca6581 | 4.50663 | -60.77629 | 2026-06-16 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7249497-e484-3a99-a3ab-df234ed6f864 | -11.27021 | -53.95979 | 2026-06-16 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fdeff85-8424-314a-8a59-33e2e830befe | -10.57571 | -57.31824 | 2026-06-16 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aec01123-89bb-3dc0-98e3-cbc922172315 | -11.55515 | -52.77546 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cc6d953e-2031-3a68-aa40-13033e513e56 | -11.54176 | -52.78379 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eca654a5-5ca6-3904-bf7c-ad0403b1ace5 | -11.55437 | -52.78178 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ad83fc91-7df2-398d-b860-f4a2bf5cc7da | -11.35785 | -55.81875 | 2026-06-16 05:23:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9c3e854f-0ce1-3de7-adac-9b8216d1bd9e | -11.5966 | -55.33434 | 2026-06-16 05:23:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d8cbe0b-1eda-38f9-bfbf-fb0c96866298 | -7.80989 | -61.4698 | 2026-06-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a8873b2-fec7-34fd-b7a7-89d237f45534 | -10.82087 | -56.60858 | 2026-06-16 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf3056ab-273d-353c-9302-fbf48098a504 | -10.14877 | -56.60264 | 2026-06-16 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 23c85f93-b59f-3755-9202-62c1770a04f5 | -11.78591 | -54.0121 | 2026-06-16 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae65e80b-c4bf-32d9-a7ed-0508bf2241c8 | -10.82175 | -56.60754 | 2026-06-16 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a55a28ec-2d74-3f85-966e-e0fcc63a9cf2 | -11.58733 | -55.33736 | 2026-06-16 05:23:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 779aa766-fef6-3145-a0d6-f696fa2b87e4 | -9.26734 | -48.57508 | 2026-06-16 05:23:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bbbdcbac-1149-365b-8e75-2fa429cc3553 | -11.59603 | -55.33859 | 2026-06-16 05:23:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README13.md)
