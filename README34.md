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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 121c3427-7752-3b39-b3bc-44c736fc7195 | -22.0077 | -49.709 | 2025-10-07 04:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.1 |
| 6d9946f1-de4d-35f0-aa71-847e8d62e1f5 | -13.5072 | -43.6594 | 2025-10-07 04:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 63cce84d-0509-39b3-beef-3d300ab7f649 | -10.8731 | -51.0289 | 2025-10-07 04:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 12e4cc34-d644-3c50-ae0d-4c05b34ba9c2 | -4.6873 | -45.8504 | 2025-10-07 04:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 6ec2fb73-24e2-369f-982e-f0beada718be | -3.1012 | -47.0301 | 2025-10-07 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f5d72eea-6eed-3d06-8345-ccd6d814f668 | -14.7575 | -46.0566 | 2025-10-07 04:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 5b66de50-5c95-3881-8e5a-39cbab351d8e | -5.4937 | -43.0761 | 2025-10-07 04:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 1c6e7629-2286-3ee6-af7b-a6cb39bd5c78 | -3.1013 | -47.0082 | 2025-10-07 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5c227302-bca3-3bec-9c28-f90d4d2d50fd | -5.5125 | -43.0747 | 2025-10-07 04:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 907a4155-f7e6-3ad7-89c6-c95e3dd9ba74 | -8.5395 | -46.2406 | 2025-10-07 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 5b585b23-de3c-352a-8cca-90542e608fcd | -13.5067 | -43.6832 | 2025-10-07 04:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| cad253af-2388-3427-a1e5-04620b0705e7 | -10.4291 | -50.3091 | 2025-10-07 04:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 4ce1140f-1911-3241-a65a-d98b8b888ec1 | -3.0827 | -47.0088 | 2025-10-07 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8ef8784b-7518-36d3-a3f3-fb02111623f1 | -4.6875 | -45.828 | 2025-10-07 04:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 6b08f5fe-0807-31de-bc45-9d39b2c5c2e6 | -18.157 | -53.37 | 2025-10-07 04:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 66.4 |
| a6fe7a15-b5dc-324c-a5c8-e07500c97b69 | -13.541 | -42.9835 | 2025-10-07 04:10:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 132.6 |
| a1bfbaa7-cceb-3db2-94b9-607e19e69e67 | -13.5405 | -43.0077 | 2025-10-07 04:10:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 5bf21812-6df9-3793-ae26-2a9be8964d20 | -14.7775 | -46.03 | 2025-10-07 04:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 0f128dbb-328c-33cb-be3b-8c1961dd7200 | -15.81136 | -43.67179 | 2025-10-07 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9587678b-7a1c-3786-a947-6beb7e7b1e01 | -15.28526 | -46.33253 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 339bbcec-1354-3552-b798-b66d7a743dab | -14.93073 | -51.47229 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac17e7a4-8b03-3e0a-ac30-147d1a030daa | -15.50006 | -46.8253 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f33b9e1b-dac9-3f6d-8af2-5a123b082cff | -11.38534 | -54.34626 | 2025-10-07 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be965f0b-87df-34ba-b9be-5e8a8483eda4 | -12.13607 | -50.87239 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 80d50454-c872-3b04-aa58-6998c5534235 | -15.36047 | -47.30721 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 95007042-44b5-34da-ac8b-fb22035bf05e | -15.08768 | -46.66302 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5fe5a53-16e7-3b34-ae1a-ffc4b21febfa | -13.72629 | -48.19922 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b433c22d-be9c-3a35-8919-9cc8efb4f665 | -13.51242 | -47.23843 | 2025-10-07 04:10:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41d8dfa7-aa60-3d7d-b651-0ae30d805b95 | -12.91541 | -54.73141 | 2025-10-07 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e502a76f-c16f-34d4-be01-58713316b6a9 | -18.04115 | -43.14316 | 2025-10-07 04:10:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1cde0e74-2d20-3edd-96f1-03661b35f27c | -13.63972 | -48.7093 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45213379-1463-3e3e-b8c3-1c1f2e74a7e4 | -18.28679 | -45.46085 | 2025-10-07 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| deb2f9d6-a651-36d7-89b8-7d39cdefef58 | -13.26661 | -47.57674 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33fe5d67-fa83-3920-9ed4-b47081432194 | -15.61933 | -52.54953 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51712c8a-180f-3021-9428-b08c0f94af54 | -14.27643 | -45.843 | 2025-10-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e8798da4-3ce8-32dd-8ec6-35698da9df64 | -18.83877 | -48.2939 | 2025-10-07 04:10:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8b3a543-fb78-3cd7-8df9-873cdbc7aadd | -12.72748 | -47.93647 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 01646bcd-7f2d-3701-b92f-16b99ef4a1a5 | -14.91565 | -51.44676 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c9bbcb13-38ee-3810-a486-81054af736ae | -14.76186 | -46.05162 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 53f11000-2bc0-3a3f-bdaa-8e6b125d660b | -13.7395 | -47.94187 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2280efee-239f-3eef-957b-15cb258d05cf | -14.24788 | -54.2464 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6341f8b0-9b8a-3e2a-9045-63671de901f6 | -13.24395 | -47.79663 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0fb99af-824c-3779-8daf-16038c9ecace | -11.21151 | -54.98417 | 2025-10-07 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 503d76b5-9906-36ca-9896-3ae5db4aa6b4 | -13.24042 | -47.23672 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ead7f328-1e9a-30e3-9da5-d7f725cce58a | -13.25571 | -47.17059 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bdab6a2-b599-33c3-906b-6778f5d36726 | -14.90524 | -46.85261 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ec44a5f-ccd0-37e5-9163-78fd0ef0ed18 | -17.56139 | -50.44571 | 2025-10-07 04:10:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 81651cd9-031a-3fdd-92d3-64d0c737ccf6 | -17.17162 | -43.45302 | 2025-10-07 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0202564a-0cb1-3133-a885-60b671f8479e | -16.13705 | -46.17765 | 2025-10-07 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43cfd123-0b7f-3676-89fe-8116c4d9492a | -14.7032 | -48.33917 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3702cf9-99ca-3647-8140-07ff0ae30746 | -13.07938 | -47.83699 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 298f09a0-878d-397f-91f4-ea5136dac2fe | -13.08774 | -47.81314 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e53713f7-9484-3019-b53e-435339d1f292 | -15.27207 | -46.34655 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32df62d2-5700-3e0b-b296-f67bc940c986 | -20.32096 | -45.11592 | 2025-10-07 04:10:00 | NOAA-21 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 607ac756-8a16-3ace-aa8a-a8f6886aa657 | -14.77098 | -46.06146 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 5541e1c6-468c-3844-be3c-4fd2d9c1a231 | -14.76535 | -46.05222 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8da8919f-7f0f-3147-8ea7-9d776abbd86d | -13.07552 | -47.88292 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 683ca0aa-220f-3283-930d-600d50eaaada | -19.86068 | -42.58775 | 2025-10-07 04:10:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 860e915f-a98b-325e-a277-b1cc3bb1aede | -13.85865 | -44.41564 | 2025-10-07 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4a274e6-7892-39f6-857f-8c690a7306a6 | -14.97152 | -49.95086 | 2025-10-07 04:10:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e8df2b7-87c5-3684-9bfa-a6bc4995b320 | -16.30657 | -42.05577 | 2025-10-07 04:10:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f6091cc9-efdc-3151-87ee-13c055253d13 | -13.09691 | -48.01286 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1dc2beb5-f6e8-38b1-8f93-ebba6272f4f4 | -13.64861 | -47.28667 | 2025-10-07 04:10:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0de7e3f4-bb61-3d4c-8d9e-35c35b02893d | -14.906 | -46.84822 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32b60a06-2574-3210-a968-f6f7eb28826c | -16.02155 | -51.05529 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3931610-1ad4-307a-b254-59073f9ad804 | -20.47909 | -44.07393 | 2025-10-07 04:10:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d037497-81d0-39c4-94e8-aecad5f30c84 | -15.80806 | -43.67124 | 2025-10-07 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b9f71bd-7598-30f1-9e45-a5efa3140e36 | -13.5382 | -42.99952 | 2025-10-07 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 105.4 |
| f4b8c8e6-13e6-3d58-babe-d61ac5df0764 | -13.39583 | -47.59785 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43c8fb38-627b-3f60-bf4e-0741d6c675e3 | -13.38324 | -47.53416 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43dc9264-7f45-3528-b6bb-755605aaa558 | -15.27624 | -46.34326 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 760f0786-4282-3407-82b0-b37d7e3aa3d5 | -13.23956 | -47.24166 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f68b2bac-de9d-3879-96d0-8036ec692606 | -12.15725 | -50.89351 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6678901f-b110-3df4-9469-97a211a5e00c | -15.36193 | -47.29886 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 361ac6aa-2bdc-3ae5-b1ae-d76ff17e82b6 | -15.61556 | -52.56841 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b32b3d1c-fafb-35cc-aad7-3f72d87951d6 | -16.01798 | -51.04918 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9d9b7a3-aabe-3923-bfbd-8ee7ef7dad91 | -13.22793 | -48.4562 | 2025-10-07 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4ccf3ecf-7c1e-3d94-8d7b-8ea4446b18ae | -18.11437 | -53.35416 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d93fd534-73b3-377d-9e6f-ce0d9161e6dc | -12.36216 | -54.1681 | 2025-10-07 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 770cd00a-eaa8-3c30-9dd7-2ec2b42a8dbe | -15.17059 | -52.77799 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 677d4064-afdf-3ca7-bdef-5b67f22dcbe7 | -14.77083 | -46.04088 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 17fbb742-e237-360c-8bf8-3f19f7fed8d7 | -14.49832 | -46.91991 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e98c3675-562b-3f29-8516-965820119dd5 | -15.49936 | -46.82943 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a1c4466-c8d0-319b-ac81-ff6a39302a44 | -18.28086 | -45.45955 | 2025-10-07 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0b2ce19-5a73-3dca-bfec-aa14c85651c6 | -12.16211 | -50.89444 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cae1c68f-4c88-314f-b101-28faff235bd1 | -13.72157 | -48.06523 | 2025-10-07 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26852b6d-1ed6-35b2-873d-bc34407ea72c | -13.35458 | -47.56235 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dfa0aa2-1bc7-33ee-b731-665ff5f72aef | -14.73172 | -46.01755 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69aa8413-efa4-3d87-9dd3-fac315ee22ab | -18.27299 | -45.46579 | 2025-10-07 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15eca917-3437-3601-a51d-57f9340d3f58 | -13.36536 | -47.25668 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9a6f778-d8d6-321f-bcaa-810f5f431ae0 | -13.77458 | -43.94096 | 2025-10-07 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a62995b1-f8b3-3575-87cb-99f02f9605b2 | -14.73868 | -46.01881 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 15a9ed83-52b5-328d-8beb-de8e09c9528f | -12.99734 | -46.79197 | 2025-10-07 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67876906-50a0-33fb-b535-1436545219e1 | -20.41071 | -43.35273 | 2025-10-07 04:10:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 792a6301-6c43-30cd-8788-f1d4e8e65961 | -19.2591 | -44.11715 | 2025-10-07 04:10:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1a69335-f835-3ffb-b641-12973be7252c | -13.34349 | -47.18137 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 536a7811-548d-328d-80b4-2760d870992e | -20.10139 | -44.1883 | 2025-10-07 04:10:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e2af08d2-6d4e-3727-93c4-832b07c393e0 | -14.34951 | -42.34628 | 2025-10-07 04:10:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d3cc27fb-5d8d-31ea-b04c-5c6ca21c31aa | -16.30806 | -42.05143 | 2025-10-07 04:10:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 00a33db7-bbcd-396e-ada2-9178099ecdc9 | -17.95893 | -44.4052 | 2025-10-07 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README35.md)
