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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45db476a-bb27-3147-81b2-52c1afd6d2f3 | -16.6385 | -55.188801 | 2024-10-02 01:23:54 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f90fd5f2-a575-35a2-a2a2-02e9148afb7a | -16.6401 | -55.1959 | 2024-10-02 01:23:54 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3b3013dc-00f2-346b-80ff-add46ed7835e | -16.7094 | -55.5033 | 2024-10-02 01:23:54 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b7d70847-7479-3761-b7cd-8deb2b3b187f | -16.711 | -55.510399 | 2024-10-02 01:23:54 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8467db04-11bb-39a4-bc4c-3555bdd01b8e | -16.805099 | -55.931301 | 2024-10-02 01:23:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a9f4283-5da8-386e-959e-5385eab16ec9 | -16.8067 | -55.9384 | 2024-10-02 01:23:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e7e4afb3-4d4b-3d2f-a403-ad2b0090b1ee | -16.838499 | -56.081402 | 2024-10-02 01:23:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1ca2784a-6e30-3b4e-8810-b4ae820da98a | -16.631901 | -55.205502 | 2024-10-02 01:23:54 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2218b7da-e190-336b-acac-9a2c5e2b1327 | -16.633499 | -55.2127 | 2024-10-02 01:23:54 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 648a03fa-1b99-3b42-bb9a-751b067848b6 | -16.7012 | -55.512798 | 2024-10-02 01:23:54 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 197622d9-5d36-3695-aa9d-228a1c6f28ce | -16.702801 | -55.519901 | 2024-10-02 01:23:54 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0ec550f4-8ad4-3cbe-afcd-4b7796428445 | -16.793699 | -55.926498 | 2024-10-02 01:23:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 059d4fff-f367-3c4d-baed-8e0b5f5b3a5f | -16.7202 | -55.9664 | 2024-10-02 01:23:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a2e3cd32-9a4d-3039-9f31-7ca4ba9bdbcc | -15.1046 | -49.4851 | 2024-10-02 01:23:56 | METOP-C | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b183099e-9455-31e9-b59c-c919c16bf0e0 | -15.0915 | -49.474499 | 2024-10-02 01:23:56 | METOP-C | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f60d868c-7199-3af4-97ce-5dde5a174960 | -15.0949 | -49.487701 | 2024-10-02 01:23:56 | METOP-C | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 20f0c1e2-f33c-35ea-9a1b-a75b5b4ee0de | -15.0983 | -49.5009 | 2024-10-02 01:23:56 | METOP-C | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 079a443d-6bd3-312f-8460-3c03012a3dcb | -16.6798 | -55.923302 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 67a041c4-2750-3c80-9eab-536eda9e3cd8 | -16.6814 | -55.9305 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0f9baff6-027a-3c83-8758-d68c609505c6 | -16.683001 | -55.937599 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ead06560-c196-3283-b318-376b733fec49 | -16.67 | -55.925598 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb3f8f0b-1148-392b-9b1a-cf58ff2aa192 | -16.6716 | -55.9328 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eac5d39c-5a56-3c26-bd55-fbb45a6a97f5 | -16.673201 | -55.939899 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 854a4bcc-33b2-3a60-a341-72dc0f049490 | -16.6586 | -55.920799 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5cbdabbc-b6dc-3a34-97ee-77726a2b36da | -16.6602 | -55.927898 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 140906d0-4804-3da7-b59c-48d416c6246b | -16.6618 | -55.935101 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c0650316-949f-37f1-b5d8-95477428238b | -16.663401 | -55.9422 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7fc92ece-e50c-3a26-82b0-56d1334cc1ef | -16.665001 | -55.949299 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2d9b5ceb-5dfe-35d3-b2f7-9ac073ceac23 | -16.6472 | -55.916 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b8e64f80-6787-3d12-9722-cd080a49a0e7 | -16.6488 | -55.923199 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cfc426db-9947-3880-a625-dbb57a6cf1d7 | -16.6504 | -55.930302 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6aed54f6-b588-3d7e-8f71-6cab2050a957 | -16.652 | -55.937401 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2470e35-e9cc-3192-ba86-d3f18f49677c | -16.656799 | -55.958801 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 874e5f3f-61e1-37a8-93c4-ee772373f04e | -16.6583 | -55.966 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a604ed1a-50cc-30a0-8fbd-16b3bae29656 | -16.659901 | -55.973099 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6c00247a-2bc3-3abf-8c82-02bb5591b0a4 | -16.6374 | -55.918301 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 516fb62c-f6eb-352d-b35b-119fb988b40c | -16.639 | -55.925499 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0c25c6de-4e53-309c-abd5-7bf25e60c7e0 | -16.6406 | -55.932598 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 91a4b297-7031-3136-97ab-851eb76eba51 | -16.6422 | -55.939701 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4abe99e9-669d-3900-9cd5-e25c1a79f0db | -16.643801 | -55.946899 | 2024-10-02 01:23:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 35f1aa44-7a1e-316f-a96f-c25032599469 | -16.627701 | -55.9207 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 61795f3c-9054-3ae4-af12-0f4b3f8e3a1e | -16.629299 | -55.927799 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f86cbde7-6a5e-3e98-bb09-53061f51dd59 | -16.630899 | -55.934898 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 87c37e10-088b-3915-99f5-c67c2373f0a7 | -16.6325 | -55.942101 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d6698828-c33b-32cb-b0cb-f7528ab3a90b | -16.617901 | -55.923 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88ebb274-9ddd-3cb9-a7e5-c847ca9249f2 | -16.619499 | -55.930099 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40efe6bf-7e79-3799-982c-baef484e8180 | -16.621099 | -55.937199 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 30a79a67-5b3b-3559-a47b-bd0121ae4860 | -16.6227 | -55.944401 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce82b007-1d65-3a6e-805a-83c7e0597cb8 | -16.608101 | -55.925301 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6aea43e6-0bd1-3fda-920e-10ebf1ff4b04 | -16.609699 | -55.9324 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a8c3856-aacc-371a-909d-5f0430c5253c | -16.6113 | -55.939499 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 112b7e14-331b-3c14-80b5-a6bce5880e85 | -16.624001 | -55.996601 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c6d0cd77-efcd-3193-bfb6-f71bbeb3f729 | -16.625601 | -56.0037 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2e2708ca-9ceb-3c0a-8977-74174bb75b9d | -16.611 | -55.9846 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5b8a5695-53ab-3741-9ad5-d0af0ff0b7fa | -16.6126 | -55.991798 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2d0edc5a-8bd2-3f55-8ded-40045dbc95b7 | -16.614201 | -55.998901 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 851d881c-cd78-3614-803e-209b5253df18 | -16.5996 | -55.979801 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 729f8305-f9d7-3cfb-849f-04a90da2d106 | -16.6012 | -55.9869 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ee503989-e242-30ce-9b50-a9fc55ec5401 | -16.6028 | -55.994099 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d1d95a3f-0929-3a49-bb2f-ccb51e210146 | -16.6108 | -56.0298 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6d29a37f-acd3-3fb1-bae7-d62a5667be6b | -16.612301 | -56.0369 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a2befae-e728-30a9-b00c-5f996bd12aa3 | -16.613899 | -56.043999 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 42bba783-c0ad-39ef-9f5f-254cd0820e33 | -16.601 | -56.032101 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2d6cbc8d-0570-3c15-b645-ff832254bc57 | -16.602501 | -56.0392 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 348f8c97-410c-325d-86f9-b7510b859d22 | -16.604099 | -56.046299 | 2024-10-02 01:23:57 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4237166d-8b66-3993-980e-acb80749e33c | -14.8023 | -48.7565 | 2024-10-02 01:23:58 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1cbae6dc-bf52-3955-9cbe-318314dad090 | -14.8062 | -48.771301 | 2024-10-02 01:23:58 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4ab2e0f6-6993-3287-88b1-49f369aa06b3 | -14.7927 | -48.759201 | 2024-10-02 01:23:58 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 04bc304a-20c3-39a8-9c2f-a9bb7b948199 | -14.7965 | -48.773998 | 2024-10-02 01:23:58 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a4b48162-5e3d-33e4-a05b-07eb289cc370 | -14.7869 | -48.776699 | 2024-10-02 01:23:58 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fb9c04ad-84cf-3004-a6fe-c9d3ec81c3e9 | -16.5928 | -56.0415 | 2024-10-02 01:23:58 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 12d8741f-3ca7-353e-a909-fac6988c96a8 | -16.5944 | -56.048599 | 2024-10-02 01:23:58 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e76392cf-f1af-3dac-b480-11ca5e68422e | -16.999701 | -57.962601 | 2024-10-02 01:23:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 930b16de-6ae1-3a05-889f-e07dc196b6b1 | -17.0014 | -57.970501 | 2024-10-02 01:23:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9597b071-81c9-3183-8132-46f68bfb3963 | -16.989901 | -57.964802 | 2024-10-02 01:23:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00eca52b-3dab-3027-b683-5e8496aafca5 | -16.9916 | -57.972698 | 2024-10-02 01:23:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4b05770-0169-3d2a-9cc8-4b9600f6f563 | -16.965401 | -57.945599 | 2024-10-02 01:23:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0bde8ecb-ccd4-3989-abb7-133b10d12aab | -16.9671 | -57.953499 | 2024-10-02 01:23:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2b4bfa51-ccca-3dbb-98cd-dcabd524f17d | -16.897699 | -57.6758 | 2024-10-02 01:23:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d47e6fed-3758-3874-a6e9-2c7a3a82b617 | -16.8993 | -57.683498 | 2024-10-02 01:23:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 89083cb1-f429-30ba-b326-7f66bf0988f8 | -16.9009 | -57.6912 | 2024-10-02 01:23:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9f2b1bd-6736-3b49-8a43-9898458056ac | -16.902599 | -57.698898 | 2024-10-02 01:23:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0fb76cca-8853-3e58-b6e1-ec4dedd49da7 | -16.9042 | -57.7066 | 2024-10-02 01:23:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b88f9238-db88-33e5-a4b6-4a64f049f176 | -16.905899 | -57.714298 | 2024-10-02 01:23:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 08ebc7ee-448f-3f8f-a633-a7411058b813 | -14.7772 | -48.7794 | 2024-10-02 01:23:59 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 20132ab4-3c9b-37f0-adbc-cfd4cab6595f | -14.7579 | -48.784698 | 2024-10-02 01:23:59 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 39153e8e-b6c2-358f-a435-765211c8051a | -14.7482 | -48.7873 | 2024-10-02 01:23:59 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d2195efb-2045-3c2f-901a-f90a70bd692e | -14.8028 | -49.037701 | 2024-10-02 01:23:59 | METOP-C | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 570c884e-15f7-35a2-afe8-a0940beb3212 | -14.8064 | -49.051998 | 2024-10-02 01:23:59 | METOP-C | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1482a001-7d79-39de-8311-2fd4cc17a624 | -16.887899 | -57.678001 | 2024-10-02 01:23:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 26b01bf5-c848-37e2-8abd-705f8d39c1c2 | -16.8895 | -57.685699 | 2024-10-02 01:23:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7b363e55-d15f-3501-b2ab-de55b918d7b0 | -16.8911 | -57.693401 | 2024-10-02 01:23:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 27ad235e-f86a-37ef-b4c4-e51b5b2b5b7a | -16.892799 | -57.701099 | 2024-10-02 01:23:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d004c36d-9de1-369e-a9f0-1c2a079a5a38 | -16.8944 | -57.708801 | 2024-10-02 01:23:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7bfcbdaf-13eb-36a9-8427-dcea66bb6c72 | -16.896099 | -57.716499 | 2024-10-02 01:23:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47af1b87-7872-3886-974d-b7250577c2a0 | -16.897699 | -57.724201 | 2024-10-02 01:23:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 29d4cd26-b82a-3a5c-a9d5-672a89f2cd49 | -17.038799 | -58.390999 | 2024-10-02 01:23:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3be6ca4c-4ef8-35a6-816f-e5d4c98a3983 | -17.040501 | -58.3992 | 2024-10-02 01:23:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8cdaf761-d92d-3d70-9f19-834b8a1d2560 | -16.8307 | -57.459 | 2024-10-02 01:23:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 75331386-37da-3fae-b788-ec80e56984f4 | -16.8323 | -57.466599 | 2024-10-02 01:23:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README25.md)
