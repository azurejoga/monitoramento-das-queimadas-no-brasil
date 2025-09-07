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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08484893-8169-3bde-a291-b65a58280086 | -11.316 | -46.54157 | 2025-09-07 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e985931-482e-3ba5-abec-9538e8c61bf4 | -10.3839 | -44.96608 | 2025-09-07 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 23230e46-42a7-3b49-b024-fa3e0e4577ba | -9.83994 | -46.55009 | 2025-09-07 05:12:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 80b40797-64d3-3b0f-84aa-9eb333d5183a | -11.59395 | -47.1626 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fcd9058-340d-3338-b375-830c462dad7b | -13.01763 | -48.08472 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd2bf899-4134-3d11-837e-d91963731778 | -13.82412 | -46.2787 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8a8f0792-9575-3c94-9fd4-0e78e00d1964 | -11.58358 | -47.76331 | 2025-09-07 05:12:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 998aec91-393c-346d-9bdc-077ead025ab9 | -10.1573 | -48.74687 | 2025-09-07 05:12:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2b816bf-2d35-3a12-a2ff-f8914f02e75e | -13.03288 | -48.07882 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7e5821e-4b84-3220-94ca-ccb6afc1b083 | -11.85511 | -58.57592 | 2025-09-07 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8055eb4d-bd65-3163-bdba-5a8286090d7d | -12.61953 | -56.98603 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee7c7f7a-2f6f-34e2-b719-d15e5ba1d26e | -14.4513 | -48.45824 | 2025-09-07 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb1cc75f-7a04-3162-b04a-fe795dade0e1 | -8.07267 | -52.33796 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f03a17f6-f4b2-3786-ad1b-15e1d9d9b41f | -10.57053 | -61.25244 | 2025-09-07 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d34bd4c0-67a6-3d2e-93f2-87b68482c8e0 | -11.50052 | -55.51196 | 2025-09-07 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3ad7094-0c36-3f6f-931f-2a0f97559c61 | -11.0447 | -54.17505 | 2025-09-07 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4bd85de9-cb7d-380c-b575-d5142769539a | -9.3772 | -58.94998 | 2025-09-07 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bcf026b-7ad7-3894-ab8c-b3136aac0f3b | -10.46396 | -53.61251 | 2025-09-07 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9eae762-9b3a-3e0c-be4a-b226dce4d3d1 | -11.32567 | -46.57072 | 2025-09-07 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0f236a9-6d7e-340a-afcd-17dab03d5047 | -13.01294 | -54.84578 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14e84840-fe03-3d4f-8c1b-310fb2b2cf6a | -10.17496 | -46.24081 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb59d5d6-08b4-3c64-9cc0-03823df65c45 | -9.46638 | -56.04581 | 2025-09-07 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da9c2ca4-2fd1-3723-977e-f916228e8b21 | -9.45489 | -56.05187 | 2025-09-07 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c055325-2445-354d-903c-0ed4e0217c3b | -8.35263 | -52.55729 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ed626f8-1941-30db-94bf-c3d7da4399b0 | -13.01448 | -48.08136 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52f0b357-5f79-3fb8-8419-bce4fb04fcbc | -8.34599 | -52.54493 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e0eb2c6-4e2c-3808-8c7b-37daf380b48f | -8.05099 | -52.37031 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63159f1f-9b21-36ff-9068-05d05f061095 | -10.72074 | -48.59482 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c06cd030-a2f1-3e9e-91f8-0a163ff4fd9f | -8.38388 | -52.53413 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56dd142b-931b-362c-b1be-b42e097871be | -12.93418 | -54.77382 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 6fdcd6f8-b1b8-32ec-8322-fc170fecf1be | -12.87656 | -47.98952 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95ed013d-d53f-3b85-ab67-8ac11315aa08 | -9.96568 | -55.04297 | 2025-09-07 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1e3ebfd-d73a-338d-b610-0922a7044c8e | -11.16825 | -59.15763 | 2025-09-07 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 824b7abe-5791-3015-af7a-f27e0fd0d600 | -13.04844 | -48.07883 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f68e3ea6-91ca-3c83-ae8f-6be485d270dd | -12.82077 | -52.94153 | 2025-09-07 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b7287bb3-e73d-3d11-aec5-60d046d5478c | -13.03045 | -48.07788 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 979c399b-b172-38b1-84b8-2674095723a5 | -12.80731 | -48.01349 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| bb82755a-6a16-3274-94a8-2dc010ea17c4 | -9.97776 | -51.6591 | 2025-09-07 05:12:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a0d16a1-21df-383a-af11-db1fc1186e41 | -12.92908 | -48.03632 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50f492e0-a35d-3231-9fc1-86cb57745239 | -11.21271 | -55.02539 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb9de5bf-9e56-3bd0-b7b9-9798597cf3ea | -13.28796 | -51.77346 | 2025-09-07 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c9fe259-b4f1-339b-ba85-f00557437c1f | -13.00893 | -45.22218 | 2025-09-07 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6411fbb5-5dae-37ce-a333-df8888c8561d | -11.17887 | -55.05172 | 2025-09-07 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3102526-d21b-359d-aa12-05f25a34884f | -12.938 | -54.77441 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 1536c27b-5d2f-3849-ad86-0587e4b698f9 | -8.07289 | -52.38072 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6d89d177-e09d-3f20-931d-ab5e063f10d4 | -13.83718 | -46.24924 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 72f4fd4f-08aa-3ceb-a8de-61fa70944307 | -11.0509 | -54.17237 | 2025-09-07 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 7e5747c9-1590-36e8-80ca-d5a578d1f5cf | -8.62817 | -54.64985 | 2025-09-07 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e86c4246-1173-3dc0-b4ee-3fac5d81fe9d | -12.94879 | -54.7809 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c9dd1ab2-2ef0-38a6-b75a-491aa61bc11d | -11.22007 | -55.02647 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50f93b1a-7578-3900-838d-5ba42313cacf | -10.17432 | -46.24629 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3355a80a-5005-3186-995f-234b040f8803 | -12.93932 | -54.76477 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24603373-a428-313c-b675-89aa48ee3663 | -8.06781 | -52.38668 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f0eebd99-5437-35f5-81aa-84ea394edc74 | -10.46 | -53.61189 | 2025-09-07 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a6b2591-0387-38d7-bdbd-0f954ddcf536 | -13.00087 | -54.79826 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c782452b-7f87-3ea3-ae17-2e0e9a4803af | -12.61667 | -56.9817 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8647501a-b236-3d09-9fae-43624e51aefa | -9.45858 | -58.80116 | 2025-09-07 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed5ae8b0-2350-3fb2-8941-c82574956f5a | -11.16494 | -59.15712 | 2025-09-07 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57ce9a4a-e566-3a85-8464-b02e575920a3 | -12.47515 | -53.8608 | 2025-09-07 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 543e767e-5784-38f2-943f-e689ea787679 | -12.82551 | -48.01283 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3c1c28d0-c91a-3324-8f8e-ab65c1d6e33e | -13.03081 | -48.07468 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f19a02dc-c91f-31fc-ab88-8e7b724ae81f | -12.80427 | -48.01194 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f20f09e9-0781-33f8-ac55-3fb63ae5e972 | -12.72034 | -56.56477 | 2025-09-07 05:12:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| a8b023ca-456e-301d-89be-9c46ffb30769 | -9.74712 | -48.97089 | 2025-09-07 05:12:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eef44670-0cd2-3c80-9bc2-646dcc5aea39 | -12.83109 | -48.01698 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d65f24a4-c6ec-3911-bece-8a74c27f857e | -8.6918 | -54.67276 | 2025-09-07 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 222ff290-39e1-3580-8563-2da37cd2383f | -13.0051 | -54.82334 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6991a7a6-374c-3f42-a6d8-84c386dbbea6 | -11.14025 | -48.38541 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f046ff63-6631-3c69-8eb2-ebd1a5fad57a | -11.14556 | -48.38923 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a8332bc3-addd-31fe-ab72-83cfa839c733 | -11.09428 | -52.06048 | 2025-09-07 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab4b062c-908b-3e91-8dc3-911688f24fd8 | -12.62637 | -56.98711 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07de34c1-d6e4-3f0c-96c8-aa4213fd023c | -11.81374 | -57.63085 | 2025-09-07 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1af2e38d-beaa-3ced-be73-59c827017f05 | -13.0138 | -54.84411 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d09ebe14-6112-3327-9b11-980f2c0fdd90 | -11.49209 | -55.51925 | 2025-09-07 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09936ecb-342e-385f-828d-9fe74d68cffc | -13.67175 | -46.95861 | 2025-09-07 05:12:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 25d52fb5-32df-3c1b-9116-395021701077 | -11.61351 | -47.15658 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6162161a-0872-3450-acb6-92573a441219 | -12.94497 | -54.78034 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 93c1b069-5296-3f9a-ae08-b1f4abe3929e | -10.58095 | -61.23323 | 2025-09-07 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 694caa1f-65eb-3fee-867f-0191d9a5c2d9 | -11.00677 | -52.04542 | 2025-09-07 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07affd4b-f46d-366b-bd33-f72b386bcbc5 | -10.4962 | -53.57604 | 2025-09-07 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 660a723e-743c-3922-a544-c200134bd9e7 | -11.61855 | -47.1584 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3ff8f55-4020-33b2-997e-38dd1947b627 | -12.8172 | -56.52234 | 2025-09-07 05:12:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e8ae0f6-7591-38d6-af2e-f498b1a20f2a | -11.58067 | -47.76403 | 2025-09-07 05:12:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6df06946-3af3-3c57-8dfc-77593ed347f4 | -10.15619 | -46.2225 | 2025-09-07 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ee6b777-8180-3c8f-9055-7a2e2e661a87 | -10.88367 | -55.72078 | 2025-09-07 05:12:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2991cb0b-6b5e-3be5-a6b7-b1bccf31b1b2 | -10.32806 | -46.38917 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 385c0605-b317-3da7-83f1-3faf0f2891c4 | -10.73303 | -48.59657 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d832eee-0e1d-38b5-acac-d07f1d6090ca | -9.39238 | -54.76688 | 2025-09-07 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ad6f36b-dd85-3036-881d-0b6bd01f0963 | -13.01619 | -54.82187 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13facb17-2cd3-36b2-8b2e-e43052c1610d | -11.30831 | -46.53862 | 2025-09-07 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a79bf01f-0cee-31e5-bf4b-ee8df8a5f071 | -9.3949 | -54.74957 | 2025-09-07 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4779ffd-4108-31b0-8110-03fc5f7452b1 | -13.66014 | -46.95994 | 2025-09-07 05:12:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01044ce4-60c0-39c0-95d1-a4556ebe41b2 | -10.33513 | -46.40224 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f55d3509-7896-3885-bb4a-26f9459a411c | -13.05698 | -48.05656 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e6aa0a4-993c-3989-8578-a9e7d752d1cb | -10.72813 | -48.58066 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eacb7e7f-193e-32da-91f5-ee396f79d4bc | -8.38028 | -52.52972 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f936183-4761-35dc-8c16-4fd1c8f29ff2 | -12.62295 | -56.98657 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 009e2ab2-7989-3f56-a200-0da3272deae7 | -8.36325 | -52.5615 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 14649017-a7a0-3faf-9efe-854319163c65 | -10.72034 | -48.59816 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f537329-e9d7-3ffe-9258-3fb3d81b3a85 | -13.82131 | -46.27242 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README72.md)
