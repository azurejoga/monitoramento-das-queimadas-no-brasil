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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4c649ad-7efb-35fb-91c9-5c989b66f7c0 | -12.6907 | -44.96544 | 2025-09-10 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 252828b5-ebb7-3f1c-8456-6d393ec48adc | -12.01834 | -50.99789 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7e75d17a-e570-3368-8475-304b787faf18 | -11.20567 | -54.99305 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b788755c-6ef1-3159-a13f-6629602d0d4f | -12.95893 | -54.76151 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b3d3b01-dfee-3556-bc98-90dcd0a2c17c | -15.48853 | -49.49221 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1949161-3d94-3f42-b1b5-9428fd2d4050 | -15.19629 | -53.82409 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67cb6abb-dfba-3c86-8ae4-f59b6913346d | -11.92185 | -51.07299 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 847fa947-9fff-3e38-a8f9-99811a156e06 | -18.46504 | -46.47233 | 2025-09-10 04:44:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6200cc2-f7f4-3aa7-8ac8-9d64d874f39f | -15.52024 | -48.38782 | 2025-09-10 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71901e80-604c-3fa9-a9d4-3983e3e75395 | -16.46772 | -50.67196 | 2025-09-10 04:44:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6ca36fc-b15b-31d7-85b8-eaa9a5dde3de | -15.48109 | -49.38496 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9e6802e3-b753-3d71-a179-635698a0b0b8 | -13.97293 | -48.24839 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae6b33b1-a86d-3f61-a483-f431aff5cd3d | -12.96266 | -54.76221 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfe57455-dc08-3d6c-9570-fc7ab2f72ba9 | -15.28196 | -53.78959 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3ac0650-2a4e-33cf-b55c-de9951152074 | -12.83742 | -52.93965 | 2025-09-10 04:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f9bf93d-1ce9-35ea-bd2b-f4bd8e049d65 | -11.94079 | -50.76822 | 2025-09-10 04:44:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1c250ab5-12dd-3a9f-a086-19f88f059ad8 | -16.61687 | -49.778 | 2025-09-10 04:44:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c878f4cc-b618-35b8-9c48-211a0862b6d8 | -16.57428 | -47.78894 | 2025-09-10 04:44:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a999d16-d152-392e-ae64-0d5310fefc40 | -18.34892 | -49.34076 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa760f17-43e9-397f-9c40-bb11fb932bfb | -13.94315 | -48.26266 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6d70bc5-29fe-3cca-b13c-2c520ada4b07 | -11.21651 | -55.00003 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf0b4611-ad28-3d30-b6ff-0025a113d6dd | -13.12786 | -47.18948 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e02b9ef3-05ec-3da4-869b-28c4d345133e | -14.36643 | -47.31812 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37ff8921-d2f2-38f6-ad03-65b0dc441e56 | -13.97586 | -48.22811 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca4f93e2-a469-3781-a76f-a523924bad71 | -18.4536 | -49.56346 | 2025-09-10 04:44:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 40e59efd-8106-3a49-bf29-5a1c627992ec | -16.51877 | -55.14428 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 60550e05-fbc3-34a5-ab79-83699fea2739 | -15.16303 | -47.95543 | 2025-09-10 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 479abe84-2fdd-3cfe-8f44-e7634b6eaf1a | -15.96116 | -49.61953 | 2025-09-10 04:44:00 | NPP-375D | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73bd4572-db56-31c5-a6c5-6827005a49fa | -19.51429 | -45.01844 | 2025-09-10 04:44:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ef935ec-f984-37d0-8866-5cbea8ca5bfd | -13.15391 | -45.28611 | 2025-09-10 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b946003-c6f8-3ad0-ab97-92a4055998f6 | -12.94395 | -54.75879 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2056812b-cd28-3bb4-89dd-dd26bc3eca44 | -16.34669 | -52.93688 | 2025-09-10 04:44:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a20511f-96bc-31f0-8b8b-e45d6f131c82 | -13.00219 | -48.03847 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8d1ed9c-5f46-3907-a9d5-7a032929af70 | -17.27913 | -49.2099 | 2025-09-10 04:44:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3b8d57b-3d33-3f1d-ba21-fb7c2892d895 | -18.45673 | -46.47064 | 2025-09-10 04:44:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c43dc370-eb25-317c-bae3-73768fb4a215 | -13.4376 | -51.83483 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c92aa836-bf91-36ef-a3a1-28970e40a933 | -14.39343 | -48.57224 | 2025-09-10 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c6411e3-70fd-3f65-97c9-cfd27e20d0c2 | -15.22514 | -44.04251 | 2025-09-10 04:44:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcaa2be4-b4b1-3b1c-bf2a-f392ee86cea3 | -16.47221 | -50.66515 | 2025-09-10 04:44:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab7e6eb9-1a47-3a86-9ad7-95a9da2b4ad9 | -18.12906 | -51.72746 | 2025-09-10 04:44:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35d820b3-a5be-3a7e-b3cd-66a5b6dbe489 | -15.1322 | -52.39059 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d89c7db6-909e-3bf9-b0ad-0491863a9938 | -14.88834 | -55.86797 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 819ac50e-1e94-302c-b351-5fb14b2e8595 | -17.24004 | -46.07854 | 2025-09-10 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 433beaf8-e748-3257-9bbd-c0575d3f1bf5 | -14.93001 | -50.10428 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9eaae34a-b904-359e-ade2-179b51a65c9a | -19.68426 | -46.17437 | 2025-09-10 04:44:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ace39b6-3d4d-3741-b98f-c12a8f1b17e3 | -14.92719 | -50.10009 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85c7c52d-9672-3ff3-b856-5387d5f2cc4c | -11.22124 | -54.9958 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f1f96a1-ff5b-3981-a1ec-ec6917e016e5 | -12.0205 | -51.02727 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cbe58e9c-6aa8-36dc-b482-d9bd8a9215c4 | -17.58481 | -49.82293 | 2025-09-10 04:44:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b775534-5558-3338-8c0d-4c28ac445517 | -15.90412 | -50.18484 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f9b384f2-bfa2-35aa-b0cc-1b17a315b4bb | -14.38835 | -47.32626 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe9dfd4a-6055-344e-af09-cdbb76f645a9 | -13.79342 | -46.29737 | 2025-09-10 04:44:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f21d4062-6375-3fc7-94a2-bacac938f71e | -19.46258 | -43.7063 | 2025-09-10 04:44:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3f731cd-3239-3e93-b0c7-411230e85cf1 | -15.52085 | -48.38361 | 2025-09-10 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b21605c-5013-3738-a29f-5ce49a618dcc | -12.68736 | -44.96676 | 2025-09-10 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6553bc96-59a9-38b9-905c-6fd2cd613441 | -15.13162 | -52.39418 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 87eef95c-49d7-35c9-a22b-8e2110f9fa02 | -14.43249 | -52.9519 | 2025-09-10 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f7e3c6e-82da-33d9-b70a-31f72093d0a7 | -12.03659 | -51.03354 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43ed4bb5-0c12-35dc-86e9-7fc48b0e7a02 | -16.32491 | -52.92163 | 2025-09-10 04:44:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea86b829-1ccb-3a95-84e4-1e3b41da30e7 | -15.69645 | -49.89986 | 2025-09-10 04:44:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ee579eb9-ef79-32ac-8ff1-d7c7d81567de | -12.99034 | -48.01981 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30cf5c95-1dab-3a9f-b1d0-7dbed87e8c38 | -18.45008 | -49.56282 | 2025-09-10 04:44:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6267367a-d547-3fc5-9fc3-04365b3bbc29 | -15.11439 | -48.03315 | 2025-09-10 04:44:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb5f4e5b-bec1-3863-b973-1cddd9ce5f0d | -14.46268 | -53.3368 | 2025-09-10 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2920fbf0-39e9-330e-95a0-d76ebb296ccc | -16.6209 | -49.7747 | 2025-09-10 04:44:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8fa2ff2-7d1c-385b-9fb8-ac271306479a | -18.03843 | -47.15023 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d4f3acae-d13c-336d-ad69-fb2e9c6194ed | -15.60742 | -52.75385 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b483e70d-ee89-3d15-95ba-1b0c2996f702 | -12.92792 | -54.78428 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b1432cf-05b1-3bbb-bbbf-e35cb9ee6243 | -13.01472 | -48.03837 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd5b3999-e82f-31c0-8b37-47ef4a0ab7ce | -16.28033 | -45.68567 | 2025-09-10 04:44:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b94f5cd-cf2f-3bfc-b24c-1e254bfd6217 | -19.91401 | -46.15314 | 2025-09-10 04:44:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6c994cb-89e0-38f7-a07f-c370eb056730 | -14.36346 | -47.31194 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e4f75bf-beef-32a0-abad-27318458f23e | -12.04325 | -51.03464 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bf6571ea-d560-3d2c-bc93-2f9e823d69f5 | -13.8228 | -43.85725 | 2025-09-10 04:44:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 815f8517-d8b9-3b79-b957-40e847ddcd54 | -15.4972 | -52.91735 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20f62d0e-05f9-3d1d-838a-4aea686436cd | -14.3566 | -47.30604 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 342a57a6-8203-34dc-a0b2-8e2e442d6031 | -15.76107 | -56.41872 | 2025-09-10 04:44:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa2f9712-54aa-3030-8ca2-2751dd5782d9 | -15.80801 | -52.26982 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 166f4c3f-bd8a-30c7-bc5e-eb723fa6c41b | -14.57551 | -51.40366 | 2025-09-10 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46bdd395-4e75-33f9-9901-d0a2475ff7bd | -14.38601 | -47.31574 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f70fef8f-3069-3ddb-840c-ba2bf773702a | -15.21574 | -44.04121 | 2025-09-10 04:44:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1f7d5b8-e9ef-39af-b2a6-4665ec7b3e5b | -19.73039 | -47.90366 | 2025-09-10 04:44:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c09d255f-7f95-34af-bd69-49ead44b7ee9 | -12.35301 | -63.64096 | 2025-09-10 04:44:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d91276bc-6a5a-3db1-a62b-64e540b0a130 | -15.80032 | -52.25348 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0dd62b5-e7b7-3257-a68b-d34051fc9e57 | -16.73283 | -48.5569 | 2025-09-10 04:44:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 070aac00-0792-3f5f-a300-38721eea4220 | -14.31745 | -47.31097 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0dd7090-c449-3a90-af40-199a0c770e45 | -16.32093 | -52.9248 | 2025-09-10 04:44:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95bb4bd5-4c34-3208-9cfd-0f7b38e90b39 | -16.70891 | -47.65253 | 2025-09-10 04:44:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5233b103-25de-3229-9474-3d28c626bb7f | -18.90244 | -48.99407 | 2025-09-10 04:44:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60344ba9-a77f-36fb-9d36-a28d0064d8d6 | -19.1714 | -48.78669 | 2025-09-10 04:44:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2754d985-b7cd-338f-aa0c-cabb439f9554 | -18.00675 | -49.39404 | 2025-09-10 04:44:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e87422da-e838-3a9b-a4a0-e967697f6c0c | -11.59429 | -52.21146 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0937cb28-418f-3450-8bd9-d5f1e9813f97 | -15.81469 | -52.27096 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0f3cb01-fcc5-30e3-9dbd-807971830471 | -15.48166 | -49.38114 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3643cbe-5558-35d1-8ced-495ee550fa71 | -12.41246 | -47.50173 | 2025-09-10 04:44:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcce1ef7-2a2d-334c-977b-bc0555efc78a | -13.17678 | -47.24794 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16b733f0-f000-3318-8dd5-836c774c108c | -16.57363 | -47.79358 | 2025-09-10 04:44:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 55157ccb-9c5d-38f1-a6fa-36a12dad9cb4 | -15.80991 | -52.23653 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b71684d-161f-35e0-9643-de901fd63231 | -15.47276 | -53.04354 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c19a85b6-da2c-3d82-8c89-8c9bc3625164 | -19.91355 | -46.15546 | 2025-09-10 04:44:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README73.md)
