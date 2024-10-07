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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b7015ad-231f-3a83-b439-e32161eb3185 | -10.918 | -46.6642 | 2024-10-07 14:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| fffe953d-5d75-3518-973c-f6f77291efb5 | -10.9187 | -46.6192 | 2024-10-07 14:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| defb07c3-4e18-3266-ba09-a1ddae355dc5 | -10.9294 | -49.6978 | 2024-10-07 14:06:08 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| f399789c-66e4-36d1-b24d-63723fd09af3 | -11.0991 | -54.0285 | 2024-10-07 14:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 64cf7672-3711-341b-bb23-7b35c4b30e30 | -11.2783 | -43.388 | 2024-10-07 14:06:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 60be0c23-276a-39c8-81ea-c72d71a95b8f | -11.2971 | -43.4088 | 2024-10-07 14:06:10 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 3a6e5bfd-7058-3b81-a86a-ee8d7521a5f4 | -13.8943 | -44.6058 | 2024-10-07 14:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 9de12555-3092-3465-9a89-1be4cfbf5693 | -13.8749 | -44.6093 | 2024-10-07 14:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8f15e5d6-df99-3f06-ba45-1a07531d6f8d | -13.8948 | -44.5823 | 2024-10-07 14:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| fa833d04-2bae-37be-baac-ec26e3078ce7 | -14.1068 | -45.5705 | 2024-10-07 14:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 593c7dc6-2dd0-3502-ae13-cd8469d9d0a2 | -14.1268 | -45.5439 | 2024-10-07 14:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 155.9 |
| ed4b23df-2163-3f38-91fa-f63da7472caa | -14.5287 | -44.9365 | 2024-10-07 14:06:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| fcea7b1d-d638-3e95-9b11-ce59d92b93e0 | -14.6805 | -45.1191 | 2024-10-07 14:06:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| fa03bfee-c4d1-3f18-8184-1e4f5581e5a1 | -14.8021 | -53.9224 | 2024-10-07 14:06:30 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a76c4c30-4a7b-3904-a43b-d46a7832035d | -15.0422 | -51.24 | 2024-10-07 14:06:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| e3d9e1f3-f55c-39cf-a980-6de51c40c57a | -15.71 | -47.1463 | 2024-10-07 14:06:34 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 9ceb794e-4b4a-34d9-9e01-5262263a83ea | -16.6259 | -55.2142 | 2024-10-07 14:06:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| d12c312b-de47-3da1-9276-a7b02656a041 | -16.9098 | -47.1493 | 2024-10-07 14:06:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 4a74b4ae-22d6-3269-b7a4-b5a4a303460e | -16.8899 | -47.1532 | 2024-10-07 14:06:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 7c5ea9fa-9164-30ff-8dc4-8239d4132bba | -17.1437 | -51.6989 | 2024-10-07 14:06:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 666b3233-18cb-3016-a887-7407d745b608 | -17.5525 | -43.7577 | 2024-10-07 14:06:43 | GOES-16 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 182.8 |
| e21b8c9d-6a01-3a05-9f35-e992554a2336 | -17.5325 | -43.7624 | 2024-10-07 14:06:43 | GOES-16 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 0b1833b0-6930-3b4a-b1b2-999122a66c85 | -17.5532 | -43.7332 | 2024-10-07 14:06:43 | GOES-16 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 751800c0-bc83-3141-a8c3-05847d817fe6 | -17.6882 | -53.0573 | 2024-10-07 14:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 9d0201dd-7846-3c36-86eb-37f8c70bf162 | -18.301 | -47.1425 | 2024-10-07 14:06:48 | GOES-16 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 2b4df05c-1a10-3690-ad91-dbce5c37cc53 | -18.3211 | -47.1382 | 2024-10-07 14:06:48 | GOES-16 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 8b5e5ca4-4080-3315-856c-b2d819e98e15 | -18.8882 | -54.58 | 2024-10-07 14:06:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 4ed73988-181d-3921-a57e-ddf27d378d3d | -18.8886 | -54.5587 | 2024-10-07 14:06:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 65d5aa26-8f02-3200-87ea-edece7f9598f | -18.8899 | -54.4947 | 2024-10-07 14:06:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 115.0 |
| a28344b5-156d-31af-a99b-3aa08b228280 | -18.8903 | -54.4733 | 2024-10-07 14:06:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 2b4174a5-a64e-3b63-b093-233477b54b04 | -21.4152 | -57.2472 | 2024-10-07 14:07:05 | GOES-16 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 2d4eb3c4-42e3-38fb-a857-3224e593e371 | -7.7684 | -43.0833 | 2024-10-07 14:15:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| d29f50de-31b4-374e-a2df-149c0dc0cc32 | -8.1759 | -43.6957 | 2024-10-07 14:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 42a00840-8445-3134-8069-cc5004e8d1d4 | -8.8189 | -45.0566 | 2024-10-07 14:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 46ef9aec-3fce-3fe9-92de-63341e1151e8 | -9.5248 | -45.9543 | 2024-10-07 14:16:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 6f0e500b-5e25-392b-bca2-0bb36455646c | -9.5251 | -45.9317 | 2024-10-07 14:16:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 2ab2da65-1b74-3739-9182-790869dd96c3 | -9.9505 | -44.0908 | 2024-10-07 14:16:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e1acee07-4efc-3436-9473-8858c879220b | -10.8996 | -46.6216 | 2024-10-07 14:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| dd24593d-d192-32f7-bc37-4afeb9a7e1e8 | -10.9187 | -46.6192 | 2024-10-07 14:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a0cbf40d-20c9-301d-b773-8bdda0e376f8 | -11.0991 | -54.0285 | 2024-10-07 14:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 144.4 |
| a3dc4cfe-70e0-3c3c-872e-1a9a9bd93630 | -11.2591 | -43.3909 | 2024-10-07 14:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| bf01830a-da78-3f93-a3b0-d18b49a1bb56 | -11.2783 | -43.388 | 2024-10-07 14:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| b5915e66-fec4-3801-883f-6f138a32534b | -11.2975 | -43.3851 | 2024-10-07 14:16:10 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| cd70dfcc-474b-3230-bc40-f1e150e9bf7e | -11.2467 | -51.3918 | 2024-10-07 14:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 0a3a51b4-e96e-3e25-aa34-a58f5286c3a5 | -11.9865 | -50.1572 | 2024-10-07 14:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 6fb25458-a407-3057-8719-61931ff3d5f7 | -11.9299 | -50.1209 | 2024-10-07 14:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 8d219e78-fb6c-3e37-bd54-c698a7c7d83a | -11.9303 | -50.0993 | 2024-10-07 14:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 5095db1e-d5af-3a3f-a9b3-b6f806062e50 | -11.9862 | -50.1787 | 2024-10-07 14:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 5019e5d3-0161-33d5-b572-9f21a4d9ef23 | -13.8749 | -44.6093 | 2024-10-07 14:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 5e1ff803-6b95-3503-a2aa-597d8f0362eb | -14.1083 | -45.5008 | 2024-10-07 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| cad754de-87b2-33b3-bac6-0c1b60155390 | -14.0378 | -45.1648 | 2024-10-07 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 10a188f3-30a5-30a1-ab8a-bc17996bf2f7 | -14.0893 | -45.4809 | 2024-10-07 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 2a7a0f25-c87a-35b7-880e-6742e3cc7de9 | -14.0703 | -45.4611 | 2024-10-07 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 83ab1944-e0fd-3ab2-97e7-ec14e4ead397 | -14.0698 | -45.4843 | 2024-10-07 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| edf4384a-d0ea-3631-8fe7-25fad30b59b6 | -14.0188 | -45.1448 | 2024-10-07 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| bb24092d-d6db-36e1-b35c-a2395abf3547 | -14.0382 | -45.1414 | 2024-10-07 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| b0b70a53-81f7-3001-9fbd-4c4767c17efa | -14.0387 | -45.118 | 2024-10-07 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| b1ae1248-b919-358c-801d-8d8677b30e50 | -15.0422 | -51.24 | 2024-10-07 14:16:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 08d0f0a3-ddde-3996-8871-80e660b53e40 | -15.71 | -47.1463 | 2024-10-07 14:16:34 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 44464fa0-bdbd-3bf1-8ef2-eb262a62eb95 | -16.8899 | -47.1532 | 2024-10-07 14:16:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 990c6e6c-6d37-3163-b9d8-f411b96e44ea | -17.6882 | -53.0573 | 2024-10-07 14:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 225.9 |
| 80d2ca6d-bac1-39f4-861f-d17c7a8603a5 | -17.6679 | -53.0819 | 2024-10-07 14:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 187.6 |
| 446789dd-201e-3576-8312-f4301db31f9c | -17.7931 | -53.7462 | 2024-10-07 14:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 2c5696eb-d1e7-3a8d-be3d-b45582205f13 | -18.301 | -47.1425 | 2024-10-07 14:16:48 | GOES-16 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 112.2 |
| baf71905-df31-3e83-ae11-e78250caa9ee | -18.8882 | -54.58 | 2024-10-07 14:16:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 8cfe66f1-7144-36c6-a9ed-e0c735c8a67b | -18.8886 | -54.5587 | 2024-10-07 14:16:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 0d31ce2f-61a3-38cb-a5b9-d5d9529b7382 | -18.8899 | -54.4947 | 2024-10-07 14:16:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 4bc5121c-15d0-3046-bc72-d90206087b11 | -8.1759 | -43.6957 | 2024-10-07 14:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 791d98ba-3426-333d-8586-80b03e6cf781 | -8.7996 | -45.0815 | 2024-10-07 14:25:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 8f9d4d72-8048-3a5b-b62c-a0f200ef4984 | -8.8189 | -45.0566 | 2024-10-07 14:25:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| fbcb620f-bc7c-33a0-a4de-e9d493c3fb7a | -9.5248 | -45.9543 | 2024-10-07 14:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b610710d-620c-38ba-95eb-8da93b05cbab | -9.9505 | -44.0908 | 2024-10-07 14:26:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| d756ee1b-24d6-3d18-8e81-d3da510710ba | -10.8805 | -46.6241 | 2024-10-07 14:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 4808842f-7886-3f27-8bf8-a7601ccfae95 | -10.8032 | -53.5417 | 2024-10-07 14:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| b09d3027-e074-32fe-a936-983e143a5be7 | -10.8996 | -46.6216 | 2024-10-07 14:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| a1198eab-2e6a-38ce-a007-95964b64e3de | -11.0805 | -54.0097 | 2024-10-07 14:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| a3090be9-a9ec-3f01-b985-aef2493769f4 | -11.0802 | -54.0302 | 2024-10-07 14:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 161.1 |
| e4f3476b-6145-3ca4-a18a-80709469237d | -11.0991 | -54.0285 | 2024-10-07 14:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 324.2 |
| 6d7fed0a-f992-30b7-acb9-4ab3c24282fd | -12.0033 | -50.3057 | 2024-10-07 14:26:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| c8c88fc7-bb75-3b7f-8a07-73a5dcf35630 | -11.9862 | -50.1787 | 2024-10-07 14:26:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| c82e3e69-641d-3a24-9645-698fc775a9cc | -12.4882 | -47.5285 | 2024-10-07 14:26:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 7334fae3-bcbb-3dee-a5bc-efce1983ee6b | -14.0893 | -45.4809 | 2024-10-07 14:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| d6803816-b4ae-30d4-8715-1eac83274d96 | -14.8021 | -53.9224 | 2024-10-07 14:26:30 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 42308244-f90c-3319-b4df-a36b0bca881a | -15.0422 | -51.24 | 2024-10-07 14:26:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| d4db0277-b8c5-37b0-8302-662dc251de9a | -15.71 | -47.1463 | 2024-10-07 14:26:34 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 115.1 |
| a08d4286-f150-3f4b-823f-57f9ed99376d | -16.8899 | -47.1532 | 2024-10-07 14:26:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 107.3 |
| e63e2507-4b0b-350a-8577-b62e8c83ae89 | -17.1437 | -51.6989 | 2024-10-07 14:26:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 5dfb44ff-8fbc-388a-afbe-a9f729f2d794 | -17.6679 | -53.0819 | 2024-10-07 14:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 37cbc2f2-c248-390a-b213-5cc164d6faf3 | -17.7728 | -53.7705 | 2024-10-07 14:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 3dfe349e-bca5-3cda-9239-221e57a21c6f | -17.7666 | -53.088 | 2024-10-07 14:26:46 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 266.5 |
| 50572c70-b68f-3180-9840-63de5549785c | -17.7926 | -53.7675 | 2024-10-07 14:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 142.2 |
| ffffb700-b3c2-3c74-9a4b-563d29f8d37b | -17.7931 | -53.7462 | 2024-10-07 14:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| a4869033-0251-3a5e-bd62-1ac4fcd6a580 | -18.301 | -47.1425 | 2024-10-07 14:26:48 | GOES-16 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 104.1 |
| de7be988-1d56-3882-b5e3-2c996bd3b0d7 | -18.8899 | -54.4947 | 2024-10-07 14:26:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 9540f0f4-4b91-33ae-a206-f266a8dc66bd | -21.4152 | -57.2472 | 2024-10-07 14:27:05 | GOES-16 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 8e1b0040-7ea5-35f3-8e95-44cc96103860 | -7.2377 | -45.0096 | 2024-10-07 14:35:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 3c76f2b0-a17e-380d-b671-6418420b2bcc | -9.5248 | -45.9543 | 2024-10-07 14:36:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f022bbdf-956e-3ab5-b6e9-6abc5c4f3a39 | -9.5251 | -45.9317 | 2024-10-07 14:36:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| b464df04-4b50-3773-a61c-36338d1ad865 | -9.9505 | -44.0908 | 2024-10-07 14:36:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 094c0983-618a-3df0-8805-60eee6cf7008 | -10.8032 | -53.5417 | 2024-10-07 14:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |


[Clique aqui para ver as próximas entradas](README154.md)
