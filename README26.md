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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1c67155-25be-3a13-b4bc-72563f927a58 | -12.14597 | -47.06894 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba271b56-bcfe-3502-970c-71e3116486ac | -11.2801 | -46.56606 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc6d1499-c8c4-3c9d-bdfd-932915bd5a96 | -11.66781 | -50.1923 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5b9568f5-0885-3738-9684-9c35e7901da0 | -10.86551 | -45.36772 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30c2a132-6faf-38a5-95b4-00e3cbe1a581 | -11.3064 | -45.17424 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 31071e0e-22c9-3f20-a690-dea422f65ced | -15.35789 | -47.04181 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 030f959a-9c87-31d6-a69c-d3c0cbbf6173 | -11.68503 | -46.73743 | 2026-09-02 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4ba3618-b809-3174-9a59-e08db6ac126d | -11.68447 | -46.74099 | 2026-09-02 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8410ead-c44d-3f5a-8508-e03290bfe7dc | -8.12568 | -54.95439 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0f941051-e0d6-3cf6-970d-fe56f7db8744 | -11.81721 | -46.06974 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57af4ce1-2867-30d5-9b42-322ecf3a6786 | -10.79552 | -44.76301 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 96788f6b-bc24-360b-809a-4501df36348f | -10.96612 | -50.48714 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| f3207338-3f91-320f-8fe3-193b23d2edbf | -9.9372 | -53.99629 | 2026-09-02 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dec1ca6a-667b-3126-9f26-ff7dfc3aaee4 | -14.96856 | -48.11502 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52afba1b-e9f7-35d6-b92f-1c2062d6cd8c | -9.72381 | -48.14054 | 2026-09-02 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5ba3252-2728-36d7-a837-ae6e83ee49ce | -12.0745 | -47.13067 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76c403cf-08f5-33ce-8ce3-dcdb6aac9ab6 | -10.89526 | -45.35084 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6232d64b-9795-3089-aab7-bcc69b84dff6 | -12.07899 | -47.12404 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03e152ce-f8bb-3221-9464-7ca11bc2bf9e | -9.47189 | -57.03171 | 2026-09-02 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21ca9219-5ad2-311d-98b1-896f056d7bdf | -12.13045 | -47.05906 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7c38ef25-112e-3362-b4e1-3d6ee2887565 | -9.9483 | -53.99212 | 2026-09-02 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4645172d-2f24-334f-94ca-462009697b04 | -12.15207 | -47.0736 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8efea85-2f0a-33ca-a4ae-f1b2ad6e43d1 | -9.18811 | -59.45826 | 2026-09-02 04:21:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4dd8e57c-6c31-38eb-a200-ada3a5511aa5 | -15.16273 | -47.28733 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f42a9780-1cb9-336f-a234-556314670d41 | -12.14686 | -47.12784 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0f0de62d-6fac-3bdf-9790-9d8d85de7f6f | -9.47104 | -57.03607 | 2026-09-02 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d4c209e-6fa4-3b54-8c7b-9bcf8e33b22b | -8.48384 | -54.71157 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| adf73d08-8bca-3f4e-8392-ffb73ec74cfd | -11.72399 | -47.64291 | 2026-09-02 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56d7b9d1-b0dc-36f2-b000-37170496b071 | -14.97742 | -48.12411 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18954994-ba31-37da-85ae-b328b908992c | -8.11385 | -54.95693 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2284968-9a5d-3b6d-baf7-83a31d73811d | -12.35338 | -45.68084 | 2026-09-02 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33069a36-2854-3698-b89c-d4e71b456f2d | -12.17539 | -47.07745 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 681dcae6-0f1f-3703-a4fe-23d5e8ad4976 | -8.4651 | -54.72268 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec13d2aa-7e09-353d-a4e9-0fb823656677 | -15.35402 | -47.04483 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed6baee2-5f60-38fe-bf2c-0af611f8e7b9 | -9.63561 | -45.71176 | 2026-09-02 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 718c89c7-ef3b-3b1d-8df0-8ef40f5e5704 | -8.70811 | -52.36092 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9eb8eb4f-463f-31b6-8c54-610fa616ee6d | -12.14759 | -47.08022 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3044e2ba-a601-33b6-bd8a-d621a44dc154 | -12.15077 | -47.1248 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32ab4734-25df-3d6b-bb4d-cfdc55834ef6 | -11.01925 | -48.38561 | 2026-09-02 04:21:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3491761b-f24a-3247-9281-d72bf30c1a87 | -14.05236 | -48.40799 | 2026-09-02 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40cbc714-2abc-368c-a114-bbd1ad9bd140 | -14.99446 | -47.97675 | 2026-09-02 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32484604-efe2-3936-8f3d-bf11105be47c | -9.70479 | -47.20457 | 2026-09-02 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91ed9f63-82ff-3df1-8c23-655658f53dae | -10.75241 | -47.97915 | 2026-09-02 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cf173b7-7ca9-3697-ad10-84fbbc2d0fd9 | -15.65539 | -45.90236 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 088901e8-c672-3e77-b6f3-70dddad0fa28 | -10.86497 | -45.37123 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31826830-dd7b-35a0-9862-6138acd0f9da | -13.19084 | -44.07246 | 2026-09-02 04:21:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e49c6950-7966-3092-b0b7-887b24b7a38d | -8.4339 | -54.72756 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9304892c-45e0-3903-b34f-539517acf37b | -11.66238 | -50.19865 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84ffd365-2f4c-36b9-97d4-6373fff7a167 | -9.95331 | -53.993 | 2026-09-02 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e481e74-ad5b-36ac-949b-655898163ff6 | -11.33311 | -50.62594 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 80961e11-08b2-3b99-b4b6-96021d11679a | -10.04308 | -48.69271 | 2026-09-02 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7f75f25b-a49d-3ced-b768-a1a9401522c2 | -11.75366 | -50.55011 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae1605ce-fff7-3b16-a323-7f1b8911b822 | -12.12321 | -47.06154 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a19ec1ab-a52c-3bad-9093-8c2c8dda5b52 | -8.43102 | -54.71276 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e7b7965c-b5d9-38c4-88d1-84328e605904 | -15.36753 | -47.68945 | 2026-09-02 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 86820e8b-50b6-3232-81ca-f8874f759a61 | -10.74895 | -47.9787 | 2026-09-02 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 907af2dd-09ce-30b1-9eec-4c73da4e06d4 | -8.26664 | -54.96111 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 96f4c24a-c5ad-3a00-a3bc-0f2bb59bb2de | -10.31221 | -50.04316 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21ad4c06-6891-3b0a-a77c-e4df6d5e9196 | -8.49802 | -50.30042 | 2026-09-02 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 753b0566-4623-320b-bf8f-6b72b9f86eee | -12.13438 | -39.41178 | 2026-09-02 04:21:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f55148df-4755-3603-9bf7-e3fbdf950282 | -10.349 | -49.96566 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb5c45e0-cae1-3835-a85b-80b430e24804 | -12.46519 | -41.31576 | 2026-09-02 04:21:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1fac9269-1d71-3cc5-acdc-4f18d0b53727 | -13.39645 | -51.38136 | 2026-09-02 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7ed6cc86-0640-361b-b762-d7e801e157ba | -12.14181 | -47.13805 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3a97db9f-275f-3307-970e-86ed27da48f6 | -9.39806 | -51.68053 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c355adcd-3ca6-3aaf-a4dc-d8df1b067ba8 | -11.81776 | -46.06622 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 22b8cdcd-a275-33eb-94b5-646d938c2d7b | -9.39824 | -51.60308 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5857876b-9434-34e8-b536-d6cd01563e81 | -8.24725 | -49.4969 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccffae96-45b4-3350-a460-ec34038b3235 | -10.75583 | -54.06302 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8a79ee2f-bf46-3212-8b4e-416f45747de3 | -8.43453 | -54.72408 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a59002b0-943a-3dab-9f85-043c1ec30e25 | -12.14987 | -47.06591 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6f43ddc-3c58-340b-b3f5-a36a30a9512d | -12.14637 | -47.10938 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c7971c6-0fcf-3318-b451-f473fca41423 | -11.82824 | -46.06431 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7c8fde97-b0b9-39cb-81fe-31194cf54030 | -11.89895 | -45.07724 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a023fc8d-d61b-36ae-8572-1bcb3afcebcb | -12.1891 | -40.40722 | 2026-09-02 04:21:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b62888f4-ad50-37f7-ae32-63a224b9bed7 | -13.41306 | -43.87929 | 2026-09-02 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b62f3a56-ac5f-3dbc-94df-e699007932f5 | -11.31298 | -45.1535 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1a58bbd-5e59-3939-857b-1bd31fd96b18 | -12.148 | -47.12067 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a023900-e68d-375e-ad92-ac3ff0153454 | -15.42956 | -41.80699 | 2026-09-02 04:21:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2b2ea21e-0ce8-3acd-b76e-d36d1f06eff0 | -11.29419 | -45.16504 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4cd24fa0-0020-3b18-a36d-df1d940f5c83 | -12.08969 | -47.10005 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 456c2bf0-369a-377f-99d4-3f404c0d54b6 | -11.3592 | -45.40676 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b585e7fe-a5c2-386d-a314-44d1be44500c | -16.21445 | -41.80316 | 2026-09-02 04:21:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8bbaa371-0e41-3a83-b096-385548c93117 | -11.83483 | -46.04379 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e66f88da-5650-30e3-9e38-0c42af8a8546 | -8.50263 | -50.2976 | 2026-09-02 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6fe7a66-a011-3a22-abe3-010a7dfcf71a | -11.30036 | -45.19149 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1492c569-58e3-389c-9230-cee0baae939d | -10.70542 | -46.19881 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 28d557ff-5e43-3221-92eb-e727a7f4bfc0 | -9.39737 | -51.68451 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 351d9b1e-7fd8-3013-97d8-66a88a865e3f | -10.78162 | -44.76445 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 443c282f-c3ec-3e45-8487-88115613cd64 | -8.9073 | -50.57173 | 2026-09-02 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8d5f7bc-3181-38dc-82f8-5f4d1b2570f9 | -11.6708 | -50.19524 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13920cba-243c-3751-95cd-fe435b512c86 | -13.3876 | -51.38515 | 2026-09-02 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a222457-b279-3581-900b-fdadd7e61cc5 | -10.7844 | -44.76856 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d7365c8-1803-31a7-b071-56ec93436449 | -8.4335 | -46.89817 | 2026-09-02 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e227dc2-c4d1-3ac3-a3cb-16df8c79388c | -11.30911 | -45.15649 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f22f2ba6-bfdf-3398-ad6f-a64b38015060 | -8.46574 | -54.7192 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2d32b5d0-2f40-3f76-ab71-4d83c6eebd81 | -9.69404 | -47.20661 | 2026-09-02 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb23443a-1005-3c0d-92ff-8960de6c1482 | -12.10873 | -45.01479 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ae2cfc4-ca98-3c41-b173-8099ca0c81d1 | -8.4586 | -54.71388 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8253760b-e669-311f-bc51-3e4120a81d7d | -15.65204 | -45.90182 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README27.md)
