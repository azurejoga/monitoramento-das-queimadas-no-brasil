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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11625125-3624-30a3-9f6a-1dc9f59c1863 | -12.4767 | -54.4302 | 2025-06-21 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| c72d1b11-05fa-31b3-afd7-ffeaf0fd63eb | -7.21821 | -43.07437 | 2025-06-21 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 1e599718-394e-3c66-8615-2998c2bab337 | -9.33285 | -40.21921 | 2025-06-21 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 40.1 |
| ada50dc3-8680-346f-8159-0b4fe1e6842d | -9.32923 | -40.2184 | 2025-06-21 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.5 |
| abf1cf8f-a5c1-3df2-a56b-aaa7d8a0d393 | -7.22539 | -43.07567 | 2025-06-21 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 0462f219-fb0c-3890-969c-85c69f681f2e | -12.76207 | -44.41234 | 2025-06-21 03:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6ac07be-3e3e-3ee0-8a12-df771f11b11e | -7.21959 | -43.06723 | 2025-06-21 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| b81e0267-406f-3730-b097-aaaea12004b0 | -12.76911 | -44.41397 | 2025-06-21 03:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edf142b2-3156-3252-b100-615bfb2bcdf7 | -7.21604 | -43.07402 | 2025-06-21 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 3bf96551-0b46-3ebf-baf9-9daa920760ac | -12.76472 | -44.41506 | 2025-06-21 03:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d4b6abb7-089e-339d-a083-2f8459d4488d | -9.33587 | -40.21529 | 2025-06-21 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 304cd486-5c49-37a8-bb82-347277d79889 | -9.33002 | -40.21413 | 2025-06-21 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 2e18faff-033f-3f33-aee4-7b1000bb72d3 | -9.33367 | -40.21495 | 2025-06-21 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 3da0dc14-6f27-3967-a73a-cce44a87bd0f | -12.26568 | -44.60329 | 2025-06-21 03:19:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5eebb691-d341-3e39-8a8a-b8494b419310 | -7.22679 | -43.06844 | 2025-06-21 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 69326d92-c6ba-3858-acbd-1c6c415011f1 | -9.33508 | -40.21955 | 2025-06-21 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.5 |
| fa5eacb7-6278-3d10-baa1-8f9d5061d4ed | -7.21239 | -43.06601 | 2025-06-21 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 2c949317-98bd-39ca-b9b2-41737ac97eb7 | -7.21737 | -43.0669 | 2025-06-21 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 1878e80c-c2d6-3f26-a5e9-196e8f8a053d | -4.5244 | -47.9943 | 2025-06-21 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 54f62ece-7632-3209-b815-f6ca5c4f4686 | -11.7791 | -57.2445 | 2025-06-21 03:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 72a65a10-3478-3d40-b6f1-249ea7a7abc7 | -4.5614 | -48.0141 | 2025-06-21 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| f1d37ced-353e-3c22-b663-7f45fb1fcea0 | -7.2219 | -43.0682 | 2025-06-21 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 809698d3-db6b-3396-ae19-00b7810c2735 | -12.4767 | -54.4302 | 2025-06-21 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 244ec1ef-096f-3797-8681-504aaaf1b6f5 | -10.4564 | -47.0347 | 2025-06-21 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| f8a833e1-d6b4-3aa6-aea0-3f9283ae2de9 | -11.8666 | -54.6535 | 2025-06-21 03:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 3102bc7e-b821-3ab0-ab21-d773ab723ebc | -11.8663 | -54.6739 | 2025-06-21 03:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 8bd1ad11-e92c-334d-b856-ba1c44ee5162 | -11.798 | -57.243 | 2025-06-21 03:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 20446a87-b998-3006-9b6d-8b4f61c91e47 | -11.8853 | -54.6722 | 2025-06-21 03:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 024df99a-50b4-3eb7-a66c-151d3e1d3030 | -4.5243 | -48.016 | 2025-06-21 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 97ca8880-b1cd-3daa-b95e-3462d336771a | -3.9671 | -48.1283 | 2025-06-21 03:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e0a6edd0-389c-32ae-9533-8931611facfe | -9.4648 | -57.8449 | 2025-06-21 03:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| a2429855-4119-3d6d-8478-80481184814c | -4.5429 | -48.0151 | 2025-06-21 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 236.7 |
| f03b79ee-00bf-36dd-ae10-496bccc20e58 | -4.543 | -47.9934 | 2025-06-21 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| be42680d-d819-3d08-802e-8865f01af581 | -17.57976 | -43.80079 | 2025-06-21 03:21:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a6478aa-cad0-3600-b1c9-ed5f4ef42aca | -21.69368 | -41.25772 | 2025-06-21 03:21:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 05f9e694-2f9f-3262-b7ef-a2fd2e68f900 | -15.76946 | -43.26658 | 2025-06-21 03:21:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 293a1134-4027-3a37-a32e-9cf0ad30272a | -17.57852 | -43.80634 | 2025-06-21 03:21:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed662ed7-c85d-323e-8382-b82afd0e8798 | -15.76828 | -43.27204 | 2025-06-21 03:21:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 500a840d-02fa-377e-adc1-7f6544b8c3dc | -22.78637 | -42.01721 | 2025-06-21 03:23:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 56fdc4e5-59fb-3d2c-9b58-698225390bf7 | -22.67739 | -42.85773 | 2025-06-21 03:23:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0a05ef0c-cab5-3f83-ab56-ad6daf573e19 | -22.78568 | -42.0204 | 2025-06-21 03:23:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2570ccfd-8a90-3be6-96a5-333238157431 | -9.4648 | -57.8449 | 2025-06-21 03:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 72f566cd-03f2-3898-81c6-d00e76c40ca4 | -4.5429 | -48.0151 | 2025-06-21 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 252.7 |
| 303cdc6d-3831-35b7-9054-0f026731ef7f | -7.2219 | -43.0682 | 2025-06-21 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 3a6114da-707d-340b-9175-0496c21e0adf | -11.798 | -57.243 | 2025-06-21 03:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| af241384-7a2c-3d78-b97c-de397c492751 | -11.8855 | -54.6517 | 2025-06-21 03:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 6b9311a5-d666-32d9-906e-d1462e63f785 | -4.543 | -47.9934 | 2025-06-21 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 89097208-e86a-317b-b4d3-38290718587c | -11.8853 | -54.6722 | 2025-06-21 03:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 98ac96b4-3a0c-38ac-86be-fbb1dd753854 | -11.8663 | -54.6739 | 2025-06-21 03:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 746b0adc-8445-363a-9119-000eca389b65 | -4.5427 | -48.0367 | 2025-06-21 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| fed6ab38-d07b-3c60-882f-80164a0aa0e2 | -12.4767 | -54.4302 | 2025-06-21 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 7de6b712-02c1-39bc-becb-8b70439dd772 | -4.5243 | -48.016 | 2025-06-21 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| d24eea1f-e519-37ba-b03f-88cab880e9e6 | -11.7791 | -57.2445 | 2025-06-21 03:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| b8732b1b-78a4-3e0a-a4e7-3ec195a82285 | -11.8853 | -54.6722 | 2025-06-21 03:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 125.2 |
| dd4a5f8d-403a-36de-b286-9052a37925f2 | -4.5243 | -48.016 | 2025-06-21 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 13ea5aa0-ca95-3605-b8d9-dcc3ab115976 | -11.798 | -57.243 | 2025-06-21 03:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 108bef49-1363-3e27-9ee6-407718e0fc2e | -11.7791 | -57.2445 | 2025-06-21 03:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 34b20014-d2eb-3fad-a044-11b66713f9c4 | -10.4564 | -47.0347 | 2025-06-21 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 5df627b5-af71-3488-becc-b050866beea9 | -11.8855 | -54.6517 | 2025-06-21 03:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d8e62eba-9d3f-3707-83d1-49fa6d55bca7 | -12.4767 | -54.4302 | 2025-06-21 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 4b6e1300-0dcc-3113-a26c-87cb632f491a | -4.543 | -47.9934 | 2025-06-21 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 05ee08e7-b30e-3e06-b044-bae74b1af5de | -9.4648 | -57.8449 | 2025-06-21 03:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| d115cc52-8f88-33f9-8a56-815a47cddfa7 | -4.5429 | -48.0151 | 2025-06-21 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 235.6 |
| dfc200f4-c966-3441-9000-5a19a02a8d70 | -11.8663 | -54.6739 | 2025-06-21 03:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 737919b8-a6fb-3935-9fe8-51d60f86c178 | -4.54314 | -48.02076 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| d56bda45-3a33-34ba-aa0a-f6168a1b8023 | -4.37533 | -48.08388 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 815a8d78-7337-37f2-99dc-8ee12642e295 | -7.47547 | -34.84239 | 2025-06-21 03:40:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 61327070-4abb-3c07-85e6-230ba72e62d9 | -5.7506 | -43.05604 | 2025-06-21 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 75279b30-c90b-3fcd-b52f-b3b76f317c32 | -7.15542 | -43.20539 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6b225f0e-c655-3d42-b64d-8544f8c521e3 | -6.86733 | -44.41869 | 2025-06-21 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31812081-6bff-3d94-897f-064609ecb632 | -7.15446 | -43.21087 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ccbf9e7e-15a7-3482-b475-9cd510807cc4 | -5.77489 | -45.90403 | 2025-06-21 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e306f535-d54d-3ea0-aa66-4a57598fc558 | -5.10757 | -43.14532 | 2025-06-21 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d37f8e1-3df7-36fd-910f-5f8238aedae1 | -7.21427 | -43.0624 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| f374837e-d1bc-3c05-96b1-3f60b70cf355 | -4.53622 | -48.01975 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 02b1e7d0-0c4e-36d6-8f2a-6e3809500905 | -7.21814 | -43.0685 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a987c5e6-3b7f-3ce4-8aa5-f7d8ecb1d49a | -7.37732 | -34.88408 | 2025-06-21 03:40:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 57891910-0362-3b80-924c-00625936b626 | -4.3774 | -48.07541 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d63103f-d35f-3d9f-9425-fc12d6ee2375 | -6.41906 | -45.31579 | 2025-06-21 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 083e1fec-8958-3ef1-9564-c06233fdd7e1 | -7.22299 | -43.07391 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| ca26a15b-163b-3f8d-b8fd-e409122f012c | -3.96392 | -48.13062 | 2025-06-21 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| daed08e8-b60c-34f3-8ab6-79b5209af584 | -7.21908 | -43.0678 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| d46da895-c55a-3831-bdc7-91c9f29a2fa1 | -3.62297 | -47.51971 | 2025-06-21 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c2c0d71e-f167-3729-abd0-d4a95b02c84d | -4.53749 | -48.01343 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5bb470d2-066a-381f-b8eb-87c7c96b3acd | -4.53151 | -48.00655 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| dd70f889-df56-3765-b5e6-8be593c5b588 | -4.54329 | -48.02091 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| fdc8c478-877f-3951-be1d-361327c5cb33 | -4.52934 | -48.01947 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 0292be9f-83de-3216-ad28-e361a97ca044 | -4.37856 | -48.06887 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bade3f6-5d27-3da3-9e68-7caa17ffd833 | -7.21332 | -43.0677 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4f1e2824-9764-3a3c-8b59-f79035693481 | -7.22296 | -43.06928 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 1a686559-4fee-3989-8c10-68f323664901 | -4.37657 | -48.07708 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e8f8658-bd80-3c5a-94bb-395d279ad75f | -4.5443 | -48.01431 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1a804901-89ff-35cb-b83d-b7f3037e846a | -4.53637 | -48.01986 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 5b362a30-b446-3dec-8df4-5131a444a43c | -4.52918 | -48.01939 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 94e14650-39ea-3b47-8606-70fc5f745991 | -3.96275 | -48.13734 | 2025-06-21 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 2068677b-e136-3824-b792-1b51ebd24a15 | -4.53738 | -48.01333 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 90428a59-ff23-329d-9cf5-04b16aac3ecc | -4.37622 | -48.08215 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff0eacb8-5844-3a37-9426-b167e6b8180e | -4.5385 | -48.00713 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| c12434ea-fb51-3dfb-bc81-bace5add29ff | -7.21909 | -43.06319 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 7dd20c2d-7c3d-3fa6-9c1c-32921acaaa98 | -7.21999 | -43.06249 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |


[Clique aqui para ver as próximas entradas](README8.md)
