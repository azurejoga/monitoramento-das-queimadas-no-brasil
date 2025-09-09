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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d583a7d9-5fcc-3e7f-bca6-dee5d0ce4b28 | -18.0045 | -45.63808 | 2025-09-09 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 072a893c-8023-3e2e-beda-e9e10ee8a09f | -15.54585 | -48.36859 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a5337be4-9c53-3650-a1df-0eced9740be6 | -15.26437 | -53.80247 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0a21dfa-4bbc-31d2-967d-63584cb953a3 | -15.50933 | -52.76614 | 2025-09-09 04:36:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 625e0341-a154-30f9-8763-efa01cedc932 | -17.48631 | -43.33617 | 2025-09-09 04:36:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3bf05ea-92bd-3bd2-8af3-9b637361ab75 | -16.90236 | -45.80792 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e0d565e-febd-30e4-98fc-1ebf3237db59 | -14.77617 | -48.10375 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3f7d6fa-e044-3377-9e1b-c8ac31f9489e | -14.3732 | -60.30181 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f7cdd5e-1b08-3953-beab-404215647865 | -15.09457 | -50.09819 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5e40db9-b962-389d-b242-119c146094e1 | -17.27009 | -46.6852 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 916d370c-99f3-31a7-a881-c2f5ac04c286 | -17.29531 | -46.74994 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 960d58e3-e6c8-383a-abe0-0c9fbe46572b | -18.45819 | -49.54832 | 2025-09-09 04:36:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6125aa6b-24b9-3563-9079-d1c3cf047af0 | -16.43009 | -49.28823 | 2025-09-09 04:36:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77561f6b-dac5-3ad1-b617-69f981e75ffd | -16.50936 | -50.62103 | 2025-09-09 04:36:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f969b85f-3e78-36a9-94d4-4f04e9ff4d08 | -16.29531 | -45.688 | 2025-09-09 04:36:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03cf9d2e-dce0-3c0d-b9d3-5d20dc7656d7 | -15.24131 | -53.76682 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a17f62f7-616b-330b-9a28-90c38b38efc6 | -12.90258 | -62.08582 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 958a5196-89dd-3b60-b42b-fca5a9a55c76 | -18.76811 | -48.19825 | 2025-09-09 04:36:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee28d6f1-e454-3aba-ba6d-937c9ba816a1 | -16.06288 | -50.47559 | 2025-09-09 04:36:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b90d22aa-a5c2-3993-876b-afb0d47f4507 | -16.69749 | -48.63441 | 2025-09-09 04:36:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e98d4c7e-320d-30a7-8dd2-4bfd1db4e5c9 | -15.78186 | -56.41205 | 2025-09-09 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 363f6f66-d59c-3449-ad68-15580631c774 | -20.33992 | -42.24585 | 2025-09-09 04:36:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c25b189f-f247-391d-95d1-6e42f09cf2c1 | -18.83181 | -49.68885 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 718a2575-4bc3-3197-aa0a-06c3d6272780 | -15.71075 | -53.55048 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 941f6913-0e86-3784-bf6e-cd0f7e37aab6 | -14.70559 | -60.25294 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 968064e9-edfe-33e2-a5ef-d4f3ce7fad6d | -14.52664 | -53.96059 | 2025-09-09 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 162382d7-1c6d-39f9-9b5f-cb7170e047b2 | -17.34417 | -43.59125 | 2025-09-09 04:36:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f30d978a-20e1-34f7-a445-b7d86b9a4a87 | -14.73712 | -55.90987 | 2025-09-09 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8b0970aa-36bf-3be4-b431-bc2009dd7fb7 | -19.35528 | -47.94555 | 2025-09-09 04:36:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb2e159c-2fc7-3f25-bd7d-10d6f790210c | -16.07335 | -50.47368 | 2025-09-09 04:36:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d95620b7-a906-33c9-9fb8-3b928f5d4e07 | -18.15126 | -43.38929 | 2025-09-09 04:36:00 | NOAA-21 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93eb2b55-866a-355c-b51f-4c7a0df68a86 | -17.58827 | -50.15712 | 2025-09-09 04:36:00 | NOAA-21 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8283e4c3-a03e-3330-af04-4a3cf1755f77 | -17.72944 | -44.49676 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 37ecdfc0-ce2f-39a1-9202-572c4072ad1a | -15.26148 | -53.79724 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4100e68b-e45c-3c96-aaba-3cb5e1e050cb | -15.77367 | -56.41908 | 2025-09-09 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0b5528ab-989f-336c-9e31-ea5774ae4b2e | -17.15426 | -44.44846 | 2025-09-09 04:36:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b22d0440-eed4-3fbb-9ea2-42ec7b57e3e3 | -18.4621 | -49.54511 | 2025-09-09 04:36:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9868329-a3b8-30d9-a183-7ba485fd2dbe | -17.239 | -50.23941 | 2025-09-09 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5cb74e52-ff40-3563-9507-2edcdba72a71 | -15.10733 | -52.34919 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c4a2053-7149-3382-97a3-b40b02f023e8 | -14.67549 | -48.19186 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6aa15ee-c3b5-36e1-b63a-e1cc44709a06 | -17.15048 | -44.44408 | 2025-09-09 04:36:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3526a2e-2f6b-3aa6-84dd-95a169e60ee9 | -15.5065 | -52.76149 | 2025-09-09 04:36:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8da09a5b-c423-3838-b175-17f4061e6217 | -15.50368 | -52.75684 | 2025-09-09 04:36:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ddc6936a-4c7e-3e22-abb6-c3fa37bfc2bb | -15.78298 | -53.54809 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f72920c0-6fab-3815-8f43-18329127d268 | -16.90031 | -45.82309 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| efc6b50d-9da5-32ca-94c7-ae6efc4b63b6 | -15.83286 | -52.26062 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 31569845-e679-32c8-8a1d-038519547731 | -15.82604 | -48.94843 | 2025-09-09 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 26.5 |
| eea34b66-3840-3718-beda-d28535d82d01 | -15.26714 | -52.36422 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c72fd633-2c53-3d3b-a22d-4e6514d6bb46 | -18.47105 | -49.55421 | 2025-09-09 04:36:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5331e82-e7f0-3678-b943-35b37d193f52 | -14.44047 | -53.23906 | 2025-09-09 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2079301b-48fb-394b-9823-49ddefd40b59 | -15.74903 | -53.52879 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b56dfddd-2cae-3ada-a7bf-7c5304e66907 | -19.8807 | -48.19249 | 2025-09-09 04:36:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13ebac05-9a6e-349f-ab33-08e43ac4da3e | -16.07497 | -50.48496 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7164ae3-c215-3bf0-9576-06ce3205f8fc | -18.47049 | -49.55796 | 2025-09-09 04:36:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a7e9727-e8b2-3207-85b9-671a43cabc46 | -12.86993 | -62.11341 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f8e4099-91f9-3418-94e4-3057bf14524e | -17.29662 | -46.71287 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79010213-0962-3e98-9b21-aef6109ffe1d | -15.78672 | -53.52646 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 81b2ad4b-3681-358c-b544-29952de9b764 | -14.35662 | -60.31351 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6de23792-01d9-3451-b796-8f889b659484 | -16.42564 | -49.29499 | 2025-09-09 04:36:00 | NOAA-21 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 441d072e-11da-3c92-943d-9c0f7d614861 | -15.24521 | -53.83283 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 453b2e16-a4a6-3854-9685-da2642bf5224 | -15.53012 | -48.16818 | 2025-09-09 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48b411e5-6f85-3c34-b6e4-84aa18dad392 | -15.39405 | -54.235 | 2025-09-09 04:36:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27692d7f-39ff-366a-9090-3a2cd7814b97 | -14.36605 | -60.30794 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f9df394-5756-3c5e-8f6e-61d0f43db5cf | -14.55046 | -48.75762 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8153224c-af7b-3990-a14a-b37690c5a637 | -15.2216 | -44.0372 | 2025-09-09 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 843e4479-5372-3ced-a2fb-59461f262ac5 | -15.09788 | -50.09874 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c4e3bf5-a90c-358a-a398-d1944316aa87 | -18.83404 | -49.69683 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 95705824-affa-350a-9c86-776c34b78279 | -18.45712 | -49.5411 | 2025-09-09 04:36:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a361caf-e58b-3c63-8d89-ef274f08385f | -16.43189 | -49.29541 | 2025-09-09 04:36:00 | NOAA-21 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e74613bf-3865-320d-bf4c-a066c7bba349 | -14.44408 | -53.23974 | 2025-09-09 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 89068e4f-a4a3-3417-a119-ed253ee3a270 | -17.59158 | -50.15768 | 2025-09-09 04:36:00 | NOAA-21 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 545439e6-9205-35d4-9bb2-3ce495e829d7 | -16.34767 | -52.94658 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98c5b1eb-b7ac-3e1f-bf32-13b47380553f | -19.57909 | -47.39613 | 2025-09-09 04:36:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d88fa17d-98df-3bcc-9bc2-6f7577c7f407 | -18.82512 | -49.68773 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 1df4c6cc-5f30-3fb9-bea1-0c9ae37f5d02 | -18.82233 | -49.68344 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| be686a1d-0466-3d48-aa65-20f7bb150418 | -14.77184 | -47.77641 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fb7aabf-8ff9-36b8-9db3-e4838f643e9b | -17.26267 | -46.68402 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94501189-d8fc-3eb6-bb97-c04ebb7e74ab | -14.41365 | -54.05056 | 2025-09-09 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 74deb7e7-1edb-35c1-9a65-a56537c49c28 | -17.68502 | -52.26425 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6330f85-bcbc-3af6-a126-a351ecb5b09c | -18.02658 | -47.12866 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37e1cae8-6021-34c5-8a84-10aa754a54c6 | -16.35251 | -52.93921 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27311b36-4d53-3dd2-b6e2-cd6ede3678b1 | -17.08474 | -49.22723 | 2025-09-09 04:36:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8eaabd1-95ed-326b-9d07-f8355400ebaa | -18.67013 | -47.5514 | 2025-09-09 04:36:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5de8bdc7-e655-394d-83b4-3bd1d8ebc8ef | -17.28741 | -46.69716 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fd99628-dda6-37cb-86ba-93b9342c02f4 | -15.26325 | -53.79411 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f80f393d-9e8a-3c87-b073-825835d1092c | -15.82339 | -52.27535 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 82412516-05cd-3290-9022-8bbf497a447c | -16.07715 | -50.49266 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 259bb9d2-fb49-30cb-89d7-fc04bf4ca853 | -19.78906 | -47.99218 | 2025-09-09 04:36:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdcbf14b-136c-327b-b976-691c9665b17b | -18.96716 | -48.34971 | 2025-09-09 04:36:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c8beff3-50c7-3978-90c7-cc3aff9e9303 | -17.30279 | -46.72305 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9871f092-2235-31e2-977a-26810b7489bc | -18.47328 | -49.56224 | 2025-09-09 04:36:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5dae301-6c60-3508-b211-433ba0546852 | -15.54446 | -48.63207 | 2025-09-09 04:36:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ad4fe26-aa85-34f7-867a-947a29ae01a1 | -14.5399 | -48.75957 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f05acaf0-4259-3d7e-ab26-bf0ed59bad58 | -14.36384 | -60.30679 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8c182cc8-0882-376c-ba01-26f0aba3920e | -18.46769 | -49.55368 | 2025-09-09 04:36:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e940833e-f6c4-3eac-a724-0d98c1d1d0cb | -19.97395 | -49.69534 | 2025-09-09 04:36:00 | NOAA-21 | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 640e1f1d-f76a-3b65-8530-e617097b8fb7 | -15.09127 | -50.09765 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb755d53-191c-343e-834f-743bae33b524 | -15.82127 | -52.26677 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 427917e4-4149-3269-809a-8681ad6ab4e0 | -15.27542 | -53.80457 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b8c28b8-f7ab-3554-b271-f021c9b041f3 | -15.53516 | -48.39382 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README55.md)
