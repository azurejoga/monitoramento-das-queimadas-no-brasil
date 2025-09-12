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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03cdb74b-7747-3b9e-856e-83302f214549 | -15.90869 | -51.79585 | 2025-09-12 05:21:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 4eec7c0b-07ac-3b26-839d-ef6ff54acfe8 | -15.87953 | -48.18594 | 2025-09-12 05:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a59ab360-2812-32fa-b0fb-18689fdcc3a1 | -14.42498 | -52.92814 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5d75d4e9-9b62-3b02-999a-262705f5f3d4 | -16.61604 | -49.8032 | 2025-09-12 05:21:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9ae92d28-bf44-3d3a-8ec7-0381b6ac883c | -17.83268 | -52.04795 | 2025-09-12 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3246f600-9f32-37f1-8bbd-a0c7a0b43ef9 | -14.50496 | -53.91449 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f6a74438-3b06-3a4d-a8cc-7fd58d1085b0 | -17.13408 | -48.49847 | 2025-09-12 05:21:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8258caa6-f47d-3389-a2ba-de459a476f82 | -16.23342 | -48.45414 | 2025-09-12 05:21:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1300656f-9e7d-31fc-b7bf-c3116c2481ba | -15.53463 | -48.54434 | 2025-09-12 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7bdce792-843b-3182-8fd6-6b8e3c8c9ed5 | -14.94197 | -50.08436 | 2025-09-12 05:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0d75f7ed-1f7b-317f-a0f1-11fcd336f5e5 | -15.10806 | -52.46486 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc9827f9-c215-34c5-bba9-b0a175aca157 | -14.32734 | -54.13353 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c366b99f-20c2-3821-9828-9f4d9f85524c | -14.50438 | -53.9193 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8d0cf4e0-9792-39eb-b771-380a9b08ef26 | -15.14062 | -50.15209 | 2025-09-12 05:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 20b5f0ba-880d-3eee-86c4-db47462aee97 | -14.3868 | -52.95618 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 58b54993-abd2-327a-bda6-ab0b1bdf8676 | -12.92571 | -54.80803 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd55cf11-3f25-3a26-8a34-95cb7d4bacc8 | -15.86847 | -48.33912 | 2025-09-12 05:21:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a246d40d-2b46-3b79-9eb4-2e15555be345 | -12.76854 | -61.4469 | 2025-09-12 05:21:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f34d66fa-f0d1-36b2-9940-170bef279497 | -20.30464 | -49.24329 | 2025-09-12 05:21:00 | NOAA-21 | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f7d1cc2-551f-3611-8bcb-4524660f1618 | -12.99111 | -54.76874 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4340c399-a9fe-393e-be9e-a9f0bcab9374 | -16.25294 | -52.6508 | 2025-09-12 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40014e96-8dfd-3779-826d-4e2d15cf8a79 | -15.12774 | -48.59661 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5f3ce0d-b9a2-364d-ba09-e8382598bbb3 | -13.89424 | -48.23532 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b4132432-acb8-37a0-94a5-4c3cd8e01417 | -13.43751 | -56.41187 | 2025-09-12 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5233fcb1-bb5c-32d0-acdf-b7199689e6ad | -17.38438 | -52.93877 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b2c89011-47fc-35b9-bae1-3f0736b0ea8d | -15.7901 | -52.23159 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| de857f78-240e-3ef1-b55b-20b53ef7ac4a | -14.45425 | -56.40723 | 2025-09-12 05:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 791316c5-ba7d-3892-b735-0d0ca579f353 | -20.01807 | -47.6376 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8d44d3b3-7d8b-33a7-b123-980046b9765a | -13.27582 | -51.72013 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e628d7af-6a17-31a4-9ff6-c6636b3ba1ba | -17.3716 | -52.91522 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1ac997b-2310-3eb7-9fd2-25d4d9d3fbda | -15.78913 | -52.23081 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7e2db27-3913-3c68-a5ea-41792dd8226f | -18.68526 | -47.67659 | 2025-09-12 05:21:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02540969-31cc-363c-9bcb-c359fc0669a7 | -12.92411 | -54.78773 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7342a79-632e-350b-9787-7af1f5714058 | -15.60182 | -52.73324 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fb3e2ca-b6b7-30e5-b332-8aa96b1906d0 | -13.89486 | -48.22969 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7245c258-6b1f-39b5-b9bf-5fd2e4899241 | -13.9075 | -48.22871 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9dd1b3ad-f0c9-3829-bcad-3436d8797336 | -12.92255 | -54.79951 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fcced61-a9fe-3ba4-8494-fbc240163f93 | -12.42024 | -63.88657 | 2025-09-12 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 875e224a-ead3-3e6a-8fbb-a1115c4e0fea | -13.44518 | -56.66513 | 2025-09-12 05:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98522f62-a622-3727-9155-fa9c3784b368 | -13.27696 | -51.71949 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b350bad-36de-30c6-b6ed-ecd4ae44fd72 | -15.14108 | -50.14782 | 2025-09-12 05:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 741b05df-dbca-3b82-a28b-f5de6498316a | -15.54068 | -48.54992 | 2025-09-12 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ca4c1f5-bcb2-3be3-8142-1889b84f0179 | -16.2526 | -52.65377 | 2025-09-12 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32025eb1-a22e-322f-917a-06ce9db5a18e | -15.13019 | -56.3507 | 2025-09-12 05:21:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b309e96a-7681-3a6c-a91f-d36b9433411f | -14.26554 | -54.78233 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03c734c7-c6fb-3777-8271-cc7445c10d35 | -14.21376 | -58.59607 | 2025-09-12 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65bc709e-1374-3812-a45f-a62c78b2ae80 | -14.55494 | -54.52683 | 2025-09-12 05:21:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcbb5223-b369-3c6a-b23b-48c14206a128 | -17.38403 | -52.94183 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8c5fad4-50d8-3faa-932d-3aa1fa0cbd08 | -20.23708 | -49.2549 | 2025-09-12 05:21:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 191b7020-67e3-3d0d-b94c-78fa2f665381 | -14.92593 | -55.83667 | 2025-09-12 05:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58d6eb27-fa47-315b-8b09-e6b3daddf2db | -15.61147 | -52.73785 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd07f457-7d37-3458-ba5e-737e8bbfd8f2 | -14.40479 | -52.93098 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60b8edb0-fce4-3a27-aa6e-56f45cd5bbf3 | -12.9283 | -54.756 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4ab6cedf-4890-3c6a-8d63-76485d148d07 | -16.27206 | -50.07218 | 2025-09-12 05:21:00 | NOAA-21 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e0431b42-9f93-3dbb-a430-faf638b80014 | -13.90235 | -48.27894 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 3de95453-13b4-3e24-a069-a8ebbdd3d6ed | -15.12052 | -48.60078 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8ee924f-3cf0-3222-8a39-7094049dc3b7 | -12.95156 | -54.74285 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 371b1302-5042-3710-9838-47c360c12a17 | -15.12626 | -56.35014 | 2025-09-12 05:21:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4818607d-4d59-355c-bc7c-862e9c3c4d6c | -15.11838 | -48.09857 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f633c658-1284-3abd-9075-2ae4da130412 | -12.77187 | -61.44745 | 2025-09-12 05:21:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88852ae6-79ab-362a-978c-b2c1ade009e3 | -14.46268 | -56.40341 | 2025-09-12 05:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03c46d23-39b2-392a-812a-1b6f543df97c | -14.71955 | -55.60925 | 2025-09-12 05:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f418a1eb-7bec-3aab-b359-0c76f1742dc8 | -14.44008 | -48.42899 | 2025-09-12 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 080991b7-b478-3782-ab57-7da178fc3a68 | -19.95426 | -49.27354 | 2025-09-12 05:21:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e8e594e5-51b4-3acb-a270-7d3317d97634 | -15.10938 | -52.46572 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b369bb7b-1b7d-3d36-b279-43b4b1afeeb2 | -19.34872 | -56.71013 | 2025-09-12 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3ea82ab5-ab03-3c16-a562-cb0fba799f48 | -13.27138 | -51.71321 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 547c0297-084a-38d9-9f36-dd136e3d61fa | -18.75772 | -47.62736 | 2025-09-12 05:21:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4016ba5-e0fd-3b65-bc61-5835eb4431c0 | -14.39993 | -52.93018 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a63f533-91a3-3640-9bd8-d31e378c325d | -14.26609 | -54.77817 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f87b286d-f53c-370e-a448-e408cc8fcd4a | -12.9246 | -54.75141 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 82c1cc08-b5b8-3a0e-9000-e3c414fe3800 | -15.69501 | -47.02098 | 2025-09-12 05:21:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f38a21c8-56a3-33fa-8ae1-0e2f0ad5711c | -15.0863 | -52.44287 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c83eb92-e1d7-3586-8951-758d154c0399 | -13.23574 | -51.7449 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d89aac0-0fd2-3e79-bd37-c22ce2914303 | -14.41037 | -52.92601 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1e53f57-e960-312e-b16e-6200f34da7bd | -12.95578 | -54.74347 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adbaf0fc-f736-3e48-a64f-7722ae0ffd93 | -15.11836 | -48.62129 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 02d46bd4-fe8f-3687-8e5a-a13cee9e1bcd | -15.26702 | -51.47742 | 2025-09-12 05:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b0f95ed-8dad-3d56-8876-61a10f622165 | -13.90287 | -48.27779 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 5c1aee38-99f4-3876-9016-feeed2feb475 | -15.78871 | -52.23433 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3daea0b-c0ce-36b9-a2be-5ca169a12d13 | -15.13368 | -48.60305 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 586f1793-e58f-3102-83ba-eb2923e54cef | -13.91327 | -48.23724 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2bcfb9d-369f-3dbe-9cda-f908538ca162 | -12.91779 | -54.77055 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83f53bd4-51a0-3bbb-a728-df6f9a748c99 | -17.37729 | -52.91043 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b2633c7-5fe4-36a5-abe9-a4eab1b5b93b | -15.24285 | -53.83576 | 2025-09-12 05:21:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ec5b3e5-5227-30d4-9562-8166e095b82f | -16.27853 | -50.06859 | 2025-09-12 05:21:00 | NOAA-21 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8a8fe71d-f96b-3136-8f2f-44e0661d5e77 | -20.30515 | -49.23722 | 2025-09-12 05:21:00 | NOAA-21 | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f892c5e0-9b56-3369-94ac-20460fb85d57 | -12.93728 | -54.75313 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8caa18e-dbf0-3971-a434-6465b5a89d73 | -18.77845 | -48.53959 | 2025-09-12 05:21:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6f77c366-6f05-3167-a5c4-59494f020506 | -12.91512 | -54.75808 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 69ce26f0-1c0b-3057-a4e8-656891a7eff3 | -16.62305 | -49.79525 | 2025-09-12 05:21:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d05ceb97-5678-39dd-b41a-411a66f6e1ef | -12.96793 | -54.74922 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06d7fbcd-76a9-3225-bbdc-b04f89e874fd | -12.93781 | -54.74911 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 17d65373-6852-3e50-8027-819776674b8b | -14.50381 | -53.92398 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 380b2882-0442-3604-8830-1dd0e17778a9 | -14.4055 | -52.92527 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92bce621-7901-3464-9661-2597d0d491c1 | -19.9964 | -47.63609 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5b73777d-cd4a-3c3e-bde6-84cdf0af0dda | -15.10581 | -48.01946 | 2025-09-12 05:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9c92f2a7-ad1f-34cd-8350-7ebd1c0c3cdb | -15.69131 | -47.02479 | 2025-09-12 05:21:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 244bf393-6f9d-3680-bd2e-a2f4b66d9b33 | -14.94019 | -50.08286 | 2025-09-12 05:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 14bbd6d8-b7bb-39c8-a206-a0c378714591 | -13.2762 | -51.71706 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README111.md)
