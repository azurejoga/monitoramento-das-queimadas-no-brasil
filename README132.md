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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10873497-a80e-3297-8361-0141f3d39b2e | -11.16572 | -47.27667 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 53832876-f30c-3999-bac5-9d0b263173fb | -12.25861 | -47.80562 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1812899e-a341-321c-8d07-386833014bbf | -13.52827 | -47.27827 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd03ccd1-5e4c-33fd-9785-51a09f7a04f4 | -14.96684 | -46.89746 | 2025-10-02 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a289928a-d08b-32bb-b945-5b9ca42d5e9b | -13.69723 | -48.63012 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba9eee5a-4ec0-3b66-98bb-e37fb31b2700 | -10.42152 | -48.30602 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dafbfdfc-2039-351e-8111-5657f20d1141 | -8.94662 | -48.71799 | 2025-10-02 04:51:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1291b7e6-7d14-3838-bd85-9c63feb6a246 | -14.40925 | -46.08009 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4bf9e070-d81b-3775-ac06-209cb696977e | -11.60272 | -47.22584 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a111947-6618-3a21-96eb-27ed830229ed | -14.48353 | -48.40986 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 019388d4-d1a9-32a7-80a4-72aa6ebf69fb | -14.42211 | -46.09941 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa0f22cd-473a-3910-a811-4f79e37e1721 | -14.90129 | -48.3351 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b50c0b16-5bd5-3bdd-bf34-5a3208da3d3e | -13.40578 | -47.78095 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c2ad1ab-65c1-3fe7-9ba0-69acdd33bfd0 | -10.83585 | -45.37409 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32e8c25c-6eea-3d2c-ba98-3fe061351c32 | -12.05369 | -48.77146 | 2025-10-02 04:51:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eba82334-58bf-3a89-93d0-dbd38293bf19 | -11.84667 | -48.04467 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 421c3b85-e268-30a3-bcca-efb8f13827e9 | -15.39942 | -49.19083 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89fa4a8e-baa8-3836-aa51-5d842d316da4 | -15.2117 | -48.00455 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17160dee-3f52-3c0b-a5c6-7e0f76d49982 | -14.86652 | -48.28268 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d8b4bb7-b7b5-3373-91a3-882ed499cf2a | -15.28084 | -49.30058 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7439f35e-3f7b-3c7d-a87c-4c29e16f0544 | -16.36658 | -47.06891 | 2025-10-02 04:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f498077-17c0-3d41-ba14-426732aee68e | -12.8103 | -47.02057 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 15d7816a-a190-3603-9849-67e9fb29de4f | -11.8583 | -48.02219 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55a1ab82-e7c0-35c7-9579-48b5188af4f4 | -15.8019 | -43.73312 | 2025-10-02 04:51:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2523fb00-5444-3b85-9674-c7102f60fe39 | -11.8746 | -45.03275 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c76b546b-d408-3689-9a0a-3c673d8bf096 | -9.64398 | -62.84508 | 2025-10-02 04:51:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4718c60b-99e7-3a58-8429-5475b1e587d2 | -11.26208 | -47.65748 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b5a2eb0-6b8f-3719-bdfe-847d3ef0608a | -11.79977 | -45.00238 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db80b484-59a7-374c-8ef1-0bf0010851cb | -12.22655 | -43.76413 | 2025-10-02 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b88e45c-b258-39a6-a54a-7a61867340a2 | -13.80486 | -47.52861 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f8a2e527-910a-3dae-84c7-92943b26f637 | -10.24823 | -50.30383 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 90b4023f-25b6-3994-90ac-b135ae8de913 | -11.4703 | -45.11459 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18a5241f-49c9-3c9a-8bdb-24c1b33c37bb | -10.23981 | -50.31106 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 61a37b2b-d12f-37cf-b20b-5f97e4a81d07 | -13.28795 | -47.25335 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0b87da76-e226-3f45-892a-faaca0189e7c | -11.35815 | -44.97266 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4dd7d2e0-0403-3b51-9743-205ac46a107e | -13.21583 | -47.34895 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 13e172f7-4767-3f9a-aa7a-5f8aca339ebb | -11.84985 | -44.98024 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b44d281-db59-3300-8f48-3148650d6a75 | -13.78493 | -47.99834 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e91007e-bd58-3fc1-9a98-2cb576c370f1 | -12.9078 | -47.1683 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ab2b94b-2e4f-347b-b920-d1794824a6b2 | -14.90169 | -47.18328 | 2025-10-02 04:51:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 088b6d40-6b0b-3b92-89f8-95bdadc813b0 | -11.77077 | -46.83356 | 2025-10-02 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 98791a31-2980-3442-95df-08db4f7c4571 | -13.15679 | -47.83713 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9d86389-4fdf-330b-8132-0f4348320bf7 | -14.90043 | -48.12631 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb0eb171-0fcf-32c5-8877-82ec4fdbc412 | -14.41736 | -46.13942 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d60c39f9-de17-381b-84e3-5c1a1bba6bae | -9.91676 | -43.72112 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 737b9870-0aa6-3e82-97b1-e3cbeb3b37ab | -10.86479 | -47.82212 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37be7ebd-efbc-3283-92b7-add855b4a08e | -11.68123 | -46.97665 | 2025-10-02 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fee9975d-2b65-3f47-9492-c1e0477c3b93 | -14.85968 | -48.30125 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c63afb0a-6f36-37f5-ae0c-a3e48e95e626 | -12.6739 | -48.57401 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 36bad1f1-2e86-3c2d-a8bb-615cd4fc21e6 | -12.75043 | -46.90451 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ebadd19f-5dab-31f7-8094-3d927e289a02 | -16.03471 | -50.89577 | 2025-10-02 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8259195f-97b1-3335-baf5-38822a1abcea | -14.31249 | -45.99338 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8d9e75c7-027e-3f3a-a6f0-350c0bf06c8b | -9.94743 | -43.65524 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e36344c1-ccfc-35b5-a190-4d2a0e824650 | -14.3568 | -45.96314 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6968d9a-6f3b-37ac-af0c-b69fd3c2dcad | -11.74737 | -46.82845 | 2025-10-02 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c1061ac-b364-34fe-aec1-22ca5f124e33 | -11.19102 | -47.19019 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 794f50ee-00d4-35c6-a7b7-c95a38014923 | -13.00548 | -45.21431 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66ff51b2-eea3-38b0-8245-6197ab443864 | -11.6004 | -45.05536 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa1e9776-53a8-3993-a8c5-ddfce9f6af45 | -12.51144 | -46.84018 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 82d8e509-7ea3-329e-be73-4d65dbabb855 | -13.2099 | -48.50158 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e02a79c-ab49-3b4d-aa4d-4a5bcc23c55b | -13.17844 | -47.84041 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aec749ea-bdf9-34f3-8948-5458d47e9f6b | -9.44873 | -45.47453 | 2025-10-02 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c63ad574-d863-33ca-b433-68d8357a6f0f | -11.35926 | -44.94142 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70d85e92-2cb9-3fca-a38d-67cdc5313803 | -11.08603 | -47.80947 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af900841-f3f8-30a7-b7f8-089bc649bca8 | -14.89269 | -48.3339 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48c73049-9b7a-3e7d-ba07-dbf077e8a98b | -13.69674 | -48.63377 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41f8319b-3f2a-38c5-a5ce-45651b00e43e | -10.22144 | -48.22409 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3a8ad53a-012d-32f3-bda5-48dc5a29033a | -11.14572 | -54.12922 | 2025-10-02 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73ce74cf-f1f8-3439-9897-bcc7335a35d9 | -10.0644 | -48.18882 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11403bb8-0ba2-306d-b22b-eb9ec2dcc102 | -11.17675 | -47.26359 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1778212c-6ccc-3997-b984-55d65b0902c8 | -15.31326 | -46.29834 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e181cc9e-b8af-33f9-9dde-18fe7464300c | -15.14658 | -48.02249 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 724b68d4-6499-3721-b345-3a66ade6afdb | -11.81295 | -45.02283 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1ecde7e-a7a0-3a3d-86ea-0cbe76b9d33f | -11.58633 | -50.16661 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0d4ec5cc-a50b-3c31-998c-37af07606ff6 | -14.48351 | -48.44317 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8baeed90-67bc-3374-9697-f1635b8a5249 | -14.91256 | -47.23758 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81c444dd-62e3-3999-b51b-5cd7600aca56 | -14.4178 | -46.08567 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ee39d283-878e-3480-9c33-ed0d16433e54 | -11.47209 | -44.97571 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f250555f-60af-3178-8543-33500882a12b | -10.20577 | -50.26762 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 18bfdd50-909f-3099-9e78-2638662f3b4c | -15.41211 | -47.04192 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e80b9b3a-ae2b-3b67-9b4f-35192c6d1857 | -13.52138 | -47.25985 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c23e63ed-fe32-32cd-872b-95f00109a0ca | -12.51157 | -46.84296 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67da23db-6d9a-3500-802c-cc47c2afa583 | -11.59156 | -47.64077 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 23d3e5dc-9e8b-3708-8789-ca7d71d091e5 | -11.36083 | -44.97085 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa13090b-0bda-3316-8d38-54f8ec89b3af | -13.86766 | -47.94921 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a1146a7-eedd-3548-87c9-77eff9d9cf81 | -11.9994 | -46.57896 | 2025-10-02 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d200537-e824-347e-b855-d29db3903db4 | -10.6674 | -48.56963 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae9a0f8b-f64b-3d94-a1d8-eebccbc104ec | -10.84104 | -46.62531 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db1508b8-66c1-328e-9a4a-101d05f23aaa | -10.33024 | -45.26423 | 2025-10-02 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 246f60af-6677-3936-8f9f-d855254e44d1 | -9.79333 | -45.95036 | 2025-10-02 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0bfcd56-8faa-3583-b0b0-12cfd78814c8 | -14.547 | -48.22564 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d9d309a-499b-3180-aec5-3267a51972d1 | -13.29889 | -46.9933 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5d111f8b-32b5-38c9-8931-c6a4ac5391b0 | -11.87042 | -45.02451 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ed390312-e690-3361-b6c5-c03048468f35 | -14.47293 | -48.42478 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d23d22dd-a46e-35c3-a567-11652a567811 | -9.92596 | -43.73648 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 372c02e9-5c67-3db7-9ef3-b2f516b8e22f | -15.25685 | -49.29443 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2477165-2675-3462-b8be-e6646bd01693 | -13.3575 | -48.11097 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c16c9d2-33d5-3530-8be7-8d889db614ea | -12.28224 | -45.37469 | 2025-10-02 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb0a81d8-d45a-32c9-8ed1-13282791192d | -15.24162 | -48.73081 | 2025-10-02 04:51:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cca4ad4-1f4a-33a1-8358-1ce0496f1c71 | -9.83279 | -48.26756 | 2025-10-02 04:51:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README133.md)
