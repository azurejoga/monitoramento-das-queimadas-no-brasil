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
| 4e2f7e73-06d2-3533-b364-79c0546b82d6 | -12.99957 | -49.81318 | 2026-09-14 04:55:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3eceea28-34b0-378f-b442-b39b90451e80 | -15.26571 | -42.7974 | 2026-09-14 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40c797b5-1925-3ba0-b10f-c5a3e7a9f6a7 | -14.17556 | -47.39814 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f8bdc2c-d67b-3de1-a78f-43a7ac4d2453 | -13.77696 | -48.80763 | 2026-09-14 04:55:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 792f0794-aabc-3834-8a8d-8359a9fa523c | -14.1786 | -47.43937 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d252243-671d-373d-aeeb-a0b79b4e9377 | -13.32405 | -51.71357 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e06a905-3cab-3be0-a8db-a2f7d033f301 | -13.98868 | -54.062 | 2026-09-14 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d07a5119-31fb-3c4d-b6d1-43f6c63d1c91 | -14.81529 | -48.15187 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ae329db-251c-3657-b0d8-bf839e9cf6ff | -13.77826 | -48.79826 | 2026-09-14 04:55:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 299e97fe-5915-3ead-9e23-4078ecf676e5 | -13.29649 | -51.31672 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a3d0959-2cd4-31ac-8aa9-fdd2dce365ca | -13.78016 | -48.81242 | 2026-09-14 04:55:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2c6e974-854e-35aa-93bf-788965566384 | -14.19733 | -47.42586 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ef33dd9-f81a-3928-9725-91f0ab4ff8e4 | -14.18019 | -47.39523 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b7093f4b-88ee-3064-be50-1830914f070c | -13.62765 | -47.89648 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5a35a3be-4635-33b7-b24c-21c4b94e9b9a | -15.27775 | -42.80318 | 2026-09-14 04:55:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5362542f-aee0-3653-9cf4-1763f8500ef5 | -13.58356 | -47.89054 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b9f27f32-3c50-38fa-a806-84c80107f9e7 | -15.24806 | -42.79895 | 2026-09-14 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| deec82c0-4407-32a5-884c-56abb50dab4d | -13.62271 | -47.9027 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10c53828-4604-38df-b4e7-a56635f05910 | -13.43813 | -48.47849 | 2026-09-14 04:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb564da5-f747-3e0b-a4e4-2e9dcc4079d2 | -13.45939 | -48.46729 | 2026-09-14 04:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d21b48a4-d5cd-300f-a03b-3b8b290827b0 | -14.8457 | -48.14985 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be6ec74e-76e9-3885-a86c-be02d14ce262 | -14.81238 | -48.15482 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ac5a9f8-a290-3cd0-9431-b530079e43f6 | -13.78844 | -48.80856 | 2026-09-14 04:55:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35e9d61b-e8ad-332a-b70d-81c86670b098 | -13.58612 | -47.90167 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05067ffd-b407-3e7b-a4d1-006c19d1be12 | -15.0549 | -48.55117 | 2026-09-14 04:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc841030-c768-3b8f-87c8-36fc47c8e1ad | -12.66616 | -54.65759 | 2026-09-14 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3b3a9b2-945d-3e74-816d-816b3d922f00 | -14.81686 | -48.15185 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd332cbb-9651-3286-a13c-513e98b1e489 | -14.18851 | -47.39651 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9e2b8575-5e19-36b0-9919-da2d5a45d6a0 | -13.29987 | -51.31726 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a34e6e69-f51d-3cb0-9d09-14da54d2706e | -15.2782 | -42.799 | 2026-09-14 04:55:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe373479-1730-360f-a82e-9f202b591382 | -13.78399 | -48.81268 | 2026-09-14 04:55:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e90d2f4-9399-3452-a013-185c78feca5a | -13.57102 | -51.46102 | 2026-09-14 04:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c971ac01-be18-32ba-b3af-10d816c45b41 | -13.32065 | -51.72106 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5619bccf-e5d4-398d-a02a-85c82fe89fd2 | -14.19318 | -47.42519 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c4804be-4f51-3365-a85d-5643d481d752 | -14.82135 | -48.14874 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 395068ab-3dc4-396f-b53b-59aa32e2ac24 | -13.78275 | -48.79388 | 2026-09-14 04:55:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97264d09-150f-34b4-9c0a-98bf2231e1a8 | -13.44262 | -48.47453 | 2026-09-14 04:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a4c33b4-4341-3310-b196-3279566afbd7 | -13.55988 | -42.41482 | 2026-09-14 04:55:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b6b51666-1c3d-3aaa-920c-50ebd9ad455b | -14.84221 | -48.14545 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb974d91-e98a-3257-b2b4-084e36d5efb7 | -13.58257 | -47.89783 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8224bcce-a305-3c48-95b7-1021024a6ca0 | -13.56765 | -51.46049 | 2026-09-14 04:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77a68081-4d54-36af-b2e2-865d979e9f5b | -14.17082 | -47.4342 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c5fb560-0c06-36e4-a8bd-bea4fe96a6bc | -12.76497 | -48.81225 | 2026-09-14 04:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db19a26e-b903-3670-94d3-c42bd28dbda9 | -14.87056 | -49.95253 | 2026-09-14 04:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2f58668-2e53-3f3d-baa7-08f4f3279096 | -13.99309 | -52.52258 | 2026-09-14 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3dc406f1-a6c8-3826-8c1d-186b7818db33 | -14.17189 | -47.4261 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f4f165c-f6a8-3bc4-82c3-5cedbf252a99 | -13.30381 | -51.31411 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d243566-0bc1-3270-a9b9-a1b9fea97141 | -13.28973 | -51.31565 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9c0b029-b932-33eb-9150-f6c4e6a2fac5 | -14.17244 | -47.42191 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cfac35d-64cd-3379-9bf9-2f2d98a3c8e7 | -15.06132 | -48.56249 | 2026-09-14 04:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd86517d-1140-30e5-be69-d5c8615f00a2 | -13.32295 | -51.72083 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef584e2d-e428-34f0-a565-c16f0d44f02a | -14.18067 | -47.39165 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 193fcef8-2a38-30cb-a57e-3685c00ae758 | -14.17029 | -47.43818 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d4259d9-df4f-372e-b924-a45dde57707d | -13.29705 | -51.31303 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c826c127-bd8f-36a1-89c6-d60045f9c992 | -13.58954 | -51.86721 | 2026-09-14 04:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b230ea3e-58a3-3d33-9565-7ece5cc68a6e | -13.6267 | -47.90332 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4eed33a1-44c3-39b5-8d2b-bbe3ce6109d4 | -15.24877 | -42.80204 | 2026-09-14 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 009d6771-4edf-36c9-97ef-bf05ba1c2a4e | -13.5862 | -51.86667 | 2026-09-14 04:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c418c07-7005-3745-be08-215a57f97f55 | -13.98631 | -54.07652 | 2026-09-14 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb660653-7db3-33bd-a63a-e5a772169434 | -13.43881 | -48.47367 | 2026-09-14 04:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f46148a-53ee-375d-bd12-4e1159b0fdd3 | -13.59055 | -47.89912 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23034a29-2bbd-3cff-8370-ab1b8c33bab5 | -14.87119 | -49.94817 | 2026-09-14 04:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a56ccff1-78e8-3443-9f58-419a16a61a2f | -13.98572 | -54.08015 | 2026-09-14 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cdd952c-3da5-32cb-8f93-f16b608f03f5 | -12.68888 | -54.66932 | 2026-09-14 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfbd82e6-b467-38ab-87da-a9329f77061c | -12.68546 | -54.66872 | 2026-09-14 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86235b9a-28a0-31ae-ae70-1eba688a726b | -15.00355 | -48.5174 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ebb358dd-3fb5-371c-9959-b9cad6046fd0 | -13.62814 | -47.89297 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c0af4b49-65ca-3dfc-a943-113dfaf6afec | -13.61819 | -47.90584 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b4b02f2-2f38-3484-b81d-54485bce8175 | -15.25165 | -42.77512 | 2026-09-14 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dc85a41-1219-3d26-a8cd-1d8cdc6bdf8c | -13.59499 | -47.8965 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70f6b2b8-568a-3ed7-be06-aba5b185e01e | -14.18754 | -47.40382 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be8a77d1-1236-3249-b552-118559fd05c2 | -14.87183 | -49.94383 | 2026-09-14 04:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6388b94-6460-3403-8839-8284af5ca062 | -13.56088 | -49.90026 | 2026-09-14 04:55:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f678a93b-0631-3e13-8ac8-75492477a7d4 | -13.59511 | -51.87551 | 2026-09-14 04:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 71626b0d-088c-3e59-b422-a294f6f94e0b | -13.55419 | -42.41338 | 2026-09-14 04:55:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 976cdcba-567b-3769-a8ef-ba97ed939f20 | -14.17445 | -47.43879 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcdef4cb-2131-3bd0-bd6f-a77389057ce1 | -15.04224 | -48.58489 | 2026-09-14 04:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46ed2623-3aa3-328e-b8b6-1516fa67cb5c | -15.08591 | -48.32729 | 2026-09-14 04:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ab160945-228b-3f53-9304-9dc67caa40db | -13.28635 | -51.31512 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fad8b177-1275-39df-a7df-195b9edb0f2f | -13.59101 | -47.89583 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2bc3477-3700-3ab6-945c-4723a510ce01 | -13.59252 | -47.88476 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 752b0659-4928-3251-bd67-588aff953f53 | -14.81637 | -48.15556 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1843298e-4843-37ae-a1f0-43cab7d5696c | -13.56445 | -49.90081 | 2026-09-14 04:55:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9dfa9968-6a3e-3a71-9ce1-03365c316cc5 | -14.84619 | -48.1462 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abb95061-ebd3-3757-8543-e5ecb9ee66fe | -14.84171 | -48.14911 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8543b3d-75a3-3a9d-8c21-fe1dc390cc45 | -14.81191 | -48.15839 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43e5772e-be56-31b5-a4a4-0b32ea4d4452 | -13.30325 | -51.3178 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8103ab39-80eb-3f33-807c-981e7098ccba | -14.91392 | -44.67096 | 2026-09-14 04:55:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84d323ea-c209-34eb-9c2e-84ca422921ed | -13.35755 | -51.71893 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73ab4373-8e1f-36aa-bfa7-041e730cfff5 | -13.30776 | -51.31095 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b733658a-272d-397a-a2d1-043b55e7a670 | -13.78078 | -48.808 | 2026-09-14 04:55:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77a1cf2d-e7c9-3a04-8d70-810961ebd719 | -13.63213 | -47.89364 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fdf0632d-1b86-38b8-8820-b0d31634bb3b | -14.18435 | -47.3959 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 708aa187-e2c5-3e03-b724-931c2f146a19 | -14.83281 | -48.15463 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24707608-ad53-3c31-9bf7-d73dc921d46d | -15.08519 | -48.33251 | 2026-09-14 04:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b2e642f-0c55-3791-a1b4-abd9b1835d95 | -14.83329 | -48.15107 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2948b0ec-9818-36a9-a693-1c74f05925b0 | -14.81081 | -48.15472 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31217fb4-ea07-3b97-8f3f-8f9f81ec75fe | -13.32685 | -51.71775 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e006eda2-a5f4-37e1-bf82-7a18c08e3cff | -13.37878 | -51.73712 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7aa7d5e3-cf11-3b91-8848-4fae4a3363c2 | -13.65031 | -52.93248 | 2026-09-14 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README51.md)
