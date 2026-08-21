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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f0601a6-9982-3ebf-b0ef-8cbddeeb22eb | -11.38306 | -50.71807 | 2026-08-21 04:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| e21deb93-a5d8-3474-820b-c69521cd7b35 | -12.26595 | -43.164 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| c3555a88-5da2-3b21-88aa-fecde4d0b50c | -12.00318 | -53.42994 | 2026-08-21 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dc7279ea-9dd2-3cce-a47f-0a43613f8554 | -12.94981 | -56.63214 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86e151cb-bbbc-3f94-862f-9550a7a32820 | -14.57561 | -53.01146 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc47ca38-9e86-347f-9b44-2cdf0c8187de | -12.52214 | -54.7667 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 440a5029-903d-31e4-a4aa-fdbb17e7a3f7 | -14.22258 | -51.92551 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e416eca-c832-31f5-864e-4f4bd6a64642 | -13.40294 | -54.38778 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ab96dc0-ce58-39b9-99ea-5b6045acd269 | -14.55077 | -53.01831 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72557110-2412-37ef-8903-c26c49489b80 | -13.44517 | -51.79229 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb680295-fbe6-30fa-aaf6-e0474648ce5c | -17.95058 | -44.39378 | 2026-08-21 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d96c589-09e4-3610-897f-51c16ca5810f | -14.30882 | -51.89852 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36b09669-981a-3280-9895-b08a78375684 | -11.2047 | -55.05116 | 2026-08-21 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2fb067f-4d5d-3251-92ce-c36344e0762b | -14.09955 | -58.80993 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d79a9251-9e09-3af2-bfb0-c15c97681167 | -13.40138 | -54.37602 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 40db676e-a90d-380b-8bbe-1efcb3fcea73 | -14.31272 | -51.89544 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 64e0e762-c66a-3851-a059-673a7f2de9de | -13.09262 | -58.18559 | 2026-08-21 04:49:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8278d4b1-34c4-3a1f-8e1b-e0fd1d4acbb3 | -12.73702 | -48.47613 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67619dbc-a479-34fd-b1b6-179fd0b05d43 | -17.95023 | -44.397 | 2026-08-21 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d87fc38-e15f-3ba6-9ea3-19eca8948354 | -14.32344 | -51.90859 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e217f0a-09fb-3ffe-856f-692c426b2cbf | -14.45327 | -51.81342 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf76d4e9-dfcc-34c1-9348-5b4bcf5c759c | -11.17879 | -54.0206 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8ad701c8-67ba-3f38-8ad3-2088469a3dbe | -15.44113 | -41.38846 | 2026-08-21 04:49:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| ae4b09e5-a893-32ec-80b5-3e7849193391 | -15.14782 | -48.68534 | 2026-08-21 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da76b08c-8ebf-3fc8-851f-ba61a2e7b17f | -14.20877 | -52.87857 | 2026-08-21 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63f02d2e-ff8c-3050-8d07-fd48f44b7ef7 | -12.26631 | -43.16094 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 7174a6cf-2825-3c99-8c94-ab75ce9284a2 | -13.44131 | -51.81751 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1aaf2bba-fe3c-37e2-aa89-5a22577c87bf | -14.09012 | -58.86205 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1561dc7-8ce2-37f2-baff-68c950ef6eac | -14.0939 | -58.81711 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e27d21fb-879f-3552-9f1d-15b9af9d4e96 | -13.39522 | -54.37118 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| df308f8e-0f27-3443-866e-7f50cde3c1b5 | -12.91602 | -56.62616 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 9e6f6107-5ff4-3fb0-854d-a01fcb5eec42 | -12.71682 | -48.48211 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6aabe910-dd45-39f8-ab4a-1b9403977ed9 | -12.25559 | -43.17706 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5e318324-f35a-3c57-bf71-4b2a83000034 | -18.03311 | -44.61589 | 2026-08-21 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34a60701-7b69-3f79-8c2e-ecb09adf3479 | -14.32733 | -51.9055 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c3eb348-8d3d-3646-acdb-0a62de4ee56f | -14.07526 | -58.87173 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78c70ed3-7a36-33b2-977f-238d4c2f956e | -15.71412 | -47.79188 | 2026-08-21 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c6d4417-6457-3a7d-904c-6960be68dd1c | -13.39122 | -54.37434 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 659046a3-8cce-3265-9e21-ab8b0dd19613 | -13.66863 | -51.79752 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed576560-3d25-336d-96f9-02b4da25bd54 | -15.68452 | -53.76651 | 2026-08-21 04:49:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aba44495-fd31-3ffb-9f85-9cd6074e69c6 | -17.33379 | -43.62425 | 2026-08-21 04:49:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8594b205-81a9-3f4f-9920-fd55233da4e0 | -13.41124 | -57.02444 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a68e390a-8846-3262-8ded-6caa74f896f7 | -14.72195 | -47.13955 | 2026-08-21 04:49:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0120bf1d-3318-3d19-90af-3508cb6170b4 | -11.2126 | -55.0692 | 2026-08-21 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d09d8af8-17c7-3810-8884-30c0e268f147 | -14.99821 | -52.67546 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8c1c27d-d35e-32b5-9283-de9a09900f5d | -13.40016 | -54.38348 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96b55ab1-bc61-3df7-9889-5fc8ac6aa1d8 | -11.20116 | -55.05057 | 2026-08-21 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20596b0f-206c-31cf-919b-3bb0037d63b6 | -15.81719 | -56.45693 | 2026-08-21 04:49:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8077563-1a28-327b-bd98-d0ba7e600187 | -14.24418 | -52.14301 | 2026-08-21 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b13c774e-28c5-3d0e-9048-69e9ea7ae7e1 | -12.81038 | -48.42096 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 4ae823ae-eb82-341e-b449-8e21e5dcc2c1 | -13.3799 | -54.3729 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 32c4adb2-ed10-3059-bb26-1d88377f34f9 | -12.74649 | -48.46397 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c59c509-a5ca-3908-9dca-03a81fa05990 | -12.49857 | -54.75887 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 55ee0394-ba81-3fd8-8ccb-e4f92c7694ae | -14.08517 | -58.86528 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0143f99-fc5a-33d9-a700-3d234c3d7403 | -12.25023 | -43.17646 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a351dcf7-2931-382c-99ed-59fb3e3e7791 | -12.75372 | -48.46646 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a0f7ec2-9407-3b35-a177-1e17d2fb32b4 | -12.50831 | -54.76442 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9893e04-8380-31d3-b017-3e2cb2eb2d4b | -13.40199 | -54.3723 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 58a5fc9e-0d66-3afa-b299-da5cc5e41ca5 | -13.43908 | -51.80976 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f80bee0-792b-3330-9fd0-e9bb711751b6 | -13.15482 | -42.4153 | 2026-08-21 04:49:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 524d4dca-4454-31cc-9881-b0180f61c9f8 | -14.42705 | -52.9394 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fee7b08d-e492-34ed-8e01-59f762df5117 | -12.93184 | -56.62416 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d42f56c-f7b9-3158-8955-88134e9a71e6 | -13.39921 | -54.36803 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f29e09a2-e8bb-3306-9d05-3183196d5c30 | -12.23011 | -43.16329 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a63c2a4-65ec-3f6e-8d4f-4c8ee945dda4 | -12.74461 | -48.47712 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ccc25346-55ea-3ac3-9b3c-5d5e49d11815 | -12.75078 | -44.53729 | 2026-08-21 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78a58aca-4f17-3ad1-8c3e-6ef4dff9a804 | -11.20905 | -55.06861 | 2026-08-21 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a12ae684-8606-347f-adef-fbc8d91a01e7 | -12.845 | -48.45095 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5bf3a65-c17c-3aa7-9ac4-e5a83a1afd9c | -11.20553 | -55.04813 | 2026-08-21 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4695eaf-efdc-3e72-ad5b-7436ee02c41f | -14.08021 | -58.8685 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 642c8058-40be-3979-a141-2a03d0b94528 | -12.51775 | -54.75012 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5ad2dbf-5626-3166-a62d-b7fdb4c9df2d | -11.07981 | -50.95473 | 2026-08-21 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2d6393c-623d-3b6d-be8a-b8de84d4331f | -14.45804 | -45.61002 | 2026-08-21 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 96056cec-a35b-3044-84e7-9a1d07f1b915 | -13.39183 | -54.37062 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 60455d93-7da0-3f49-bc23-3a93343dd9c5 | -12.25364 | -43.1762 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 40bf79c6-ccab-30be-bcff-51aeeaef12bf | -12.83367 | -48.44872 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5a6d55a-70f5-34b4-9604-68735131adf3 | -16.49802 | -55.18311 | 2026-08-21 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c86c85da-7ea3-3831-a098-37786e523262 | -12.92353 | -56.62749 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 945e010e-fdae-3c9b-9386-9b29c9e46558 | -11.67903 | -54.57315 | 2026-08-21 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d93c16b-74c5-354c-9c81-7a7b0f2401eb | -12.75431 | -48.46222 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79d2f847-954a-32a0-adf1-ddf5f8750867 | -12.85913 | -48.4334 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 193c7414-f497-3080-a5e1-8cf3509b9c37 | -13.3866 | -54.38123 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 701e8efa-3d2b-3958-b276-9fe8a6c47a5e | -11.16178 | -54.01778 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ef0e3f73-bde6-392f-b1b1-16c699550eae | -11.68155 | -54.55769 | 2026-08-21 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc976927-501d-3fd4-8c8b-90f4c864bed7 | -14.32678 | -51.90913 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 692a8d3b-5d6b-343e-befb-19d412de8f96 | -12.86261 | -48.43129 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a28747c4-3723-3694-bda2-386fd5fabfd0 | -10.92071 | -57.17551 | 2026-08-21 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 317b0e05-a1a2-3a8a-b92b-b9144da178d9 | -13.43684 | -51.80204 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd48d857-31db-30cb-a60d-3a235eea4b58 | -12.50169 | -47.8456 | 2026-08-21 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afa691e3-fdb4-3c37-9dda-f8dd1a319a35 | -11.66412 | -48.35564 | 2026-08-21 04:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da5c1301-97bc-396c-9c13-07b883f248da | -13.39955 | -54.38721 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 6bfba2bd-8e41-37b1-860f-22a502e8354f | -12.79702 | -48.40534 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| de29e57e-62f2-36f5-b2be-f803b9af0089 | -12.72503 | -48.47877 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 72cea386-39ce-3935-9f9f-ebd71aba7c0e | -14.10232 | -58.81869 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f61e3030-caf2-331f-8e36-f6e8676fa846 | -13.38329 | -54.37346 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| eb83f806-d26d-3977-aa8e-a9ac25034321 | -11.21364 | -53.99966 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42c15fff-55cb-3ba5-9165-5f432c27f986 | -13.39338 | -54.38235 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 08e022da-7e47-34c3-977f-c14d190513bc | -14.56514 | -52.99152 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e93784c-2433-3a87-bee3-1ae0a9ee725d | -15.16721 | -48.77387 | 2026-08-21 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d745b34f-abb7-3ee6-b494-64ab8ea951f4 | -12.26797 | -43.16497 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |


[Clique aqui para ver as próximas entradas](README51.md)
