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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb5be097-93b5-31d3-b1b1-bd3cde2ae123 | -11.35928 | -52.96086 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 8df68eb3-9269-3766-bc39-a79cfede39cf | -8.55171 | -45.98265 | 2026-05-26 05:18:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 78c7f989-2f3e-3fb5-add0-8d4f2c8a3506 | -11.3584 | -52.9514 | 2026-05-26 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 143670b5-57ed-3f6f-b19e-f4eb1ad7dca9 | -11.73912 | -54.8068 | 2026-05-26 05:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b845a3ea-cabf-3444-baab-2d9eee9171de | -13.58329 | -47.53656 | 2026-05-26 05:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eba8d395-b08c-365f-b6f0-74e7c0ac16a5 | -11.91819 | -57.03545 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4f5044e-6b02-3489-b7d9-843b24650e17 | -13.69616 | -55.67439 | 2026-05-26 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef3d7018-5095-3c66-a619-639b40a89872 | -15.56156 | -58.64878 | 2026-05-26 05:21:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03b06825-3b62-3f06-804a-6c3314c859f4 | -13.66147 | -55.30005 | 2026-05-26 05:21:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1f62e0e-02f8-306b-a5e2-f1d3e60da9c2 | -11.55318 | -56.9398 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cc33437-b6eb-3e87-91d4-bc716eedc5ff | -12.44908 | -54.45535 | 2026-05-26 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0331a92-b90e-3462-b4c6-258965c5f9be | -13.58661 | -47.53513 | 2026-05-26 05:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 348b728b-bb7c-3d50-96b9-72cc6608513e | -12.46223 | -54.45316 | 2026-05-26 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1a012973-8b08-3000-8f6a-dbb92c79ff75 | -12.4617 | -54.45718 | 2026-05-26 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5056c9ff-03c1-39e0-b367-073e3080f9c3 | -11.79563 | -57.00597 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13c1b535-3eab-3021-bbaa-d9e3691fdd45 | -11.55082 | -56.93095 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 127224da-9df6-33a6-9021-f9216feb5b16 | -11.54601 | -56.93875 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56bd889c-0963-38d6-a720-6a3dd5514e2d | -11.55677 | -56.94032 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78569c5e-1ad5-35d5-8107-bb43acf4faa2 | -10.14793 | -65.17857 | 2026-05-26 05:21:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfea96b1-abfe-305a-9f11-4c552324b4e9 | -11.79504 | -57.01015 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 463eb0e5-d0e7-3e7b-a6b5-330797a8bd5c | -11.56097 | -56.93668 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b564b03f-7a10-3548-b21f-908d8a9f0d92 | -11.54959 | -56.93927 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac475011-c031-3f50-93cc-306c60da73ba | -11.57292 | -56.33965 | 2026-05-26 05:21:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c2f10182-902c-3c69-92e2-e1b35c1f64e2 | -11.96906 | -56.81027 | 2026-05-26 05:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7a57a65-ab39-3cd7-9e21-932020d510c8 | -12.14063 | -64.26684 | 2026-05-26 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddcadacc-d6c3-3bd6-9254-2507cc116b94 | -11.40251 | -57.54798 | 2026-05-26 05:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65c0551e-6377-38df-a1ea-dc7e69200cbe | -11.96605 | -56.80547 | 2026-05-26 05:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 197e50c0-1c32-34b3-b242-802b61d40d72 | -13.86008 | -57.68065 | 2026-05-26 05:21:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 526121a9-502d-3919-8dd1-838848006555 | -10.15206 | -65.17921 | 2026-05-26 05:21:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b135d269-4df2-3bfd-94c8-2a2a2b901bad | -11.91461 | -57.03489 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 764f85aa-5784-3c2e-8617-5f692ca7a0bf | -11.40309 | -57.54406 | 2026-05-26 05:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bde536c2-dded-3044-8ff7-9ede22457478 | -13.6579 | -55.29582 | 2026-05-26 05:21:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72d1fb20-ed71-328b-943a-b85cbbc618ad | -12.05746 | -57.42265 | 2026-05-26 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18bdbba1-cf72-3090-9252-3b87b33f1017 | -12.44927 | -54.44896 | 2026-05-26 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e7b4090-ad6c-395a-b5ce-1ef7d9c22c5f | -12.54528 | -57.22377 | 2026-05-26 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bee038a-af1a-3fa4-9641-2e3dde0232fb | -16.1705 | -58.48121 | 2026-05-26 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 186fec14-110a-396b-93eb-b9376772a394 | -11.97268 | -56.81082 | 2026-05-26 05:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cd1c567-3441-3cfe-9c69-e6503a93bf42 | -12.17057 | -56.45027 | 2026-05-26 05:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 568ca7c3-8b17-3104-a0a0-c58088ee5384 | -11.54723 | -56.93043 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e48f8750-a159-32e4-9557-78239b7b644f | -11.94946 | -54.09742 | 2026-05-26 05:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e6d794f-6dd0-3834-aa10-c7487b3c4383 | -11.63844 | -58.24964 | 2026-05-26 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80d93a7c-1a9a-3feb-9f35-30544a0a504b | -11.55911 | -56.93891 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b35a9b01-375d-3d1d-bcab-05dc3bfa2df7 | -11.5597 | -56.93473 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4711481-4ff1-3073-9dfe-1f7e0263d9bb | -12.30291 | -57.40013 | 2026-05-26 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f501dcd9-68ea-32b0-8de7-2518ed086761 | -12.1727 | -56.45263 | 2026-05-26 05:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0c2e2f4-d5d2-3f48-9e2f-f74d6f106916 | -12.45013 | -54.44726 | 2026-05-26 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 819e1cb2-4a80-379b-9398-d1fb68d12e37 | -12.14018 | -64.26886 | 2026-05-26 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2027366d-e09c-37d7-a85a-5749c08fa659 | -11.3996 | -57.54353 | 2026-05-26 05:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4f2b304-bf6c-3de8-8383-42990c0a3e69 | -10.14434 | -64.88665 | 2026-05-26 05:21:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88ca71a8-5367-30d3-b62f-0e60a09f76a2 | -11.9733 | -56.80657 | 2026-05-26 05:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b39beab6-61e6-3a6d-a0ad-dd7db38ce16d | -12.45236 | -54.45764 | 2026-05-26 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef74a75a-7ad4-3347-bf76-61ae401e8aeb | -12.4496 | -54.45131 | 2026-05-26 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eca83025-5d5e-3b2a-9731-5fdd7e7b3b7e | -12.05394 | -57.4221 | 2026-05-26 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c036636a-0be3-31cc-9512-703fe7ee1d1f | -11.96967 | -56.80602 | 2026-05-26 05:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca959da0-bec7-333a-9359-2a0cef4fd874 | -11.5502 | -56.93512 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4cf7396-3df6-33f1-b277-5a068c5a5845 | -13.65741 | -55.2995 | 2026-05-26 05:21:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81430241-6131-383f-a0dc-77cee32501ef | -11.55379 | -56.93564 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 450afe7b-1d2d-3fe7-844f-d25fc8b0c325 | -13.65385 | -55.29526 | 2026-05-26 05:21:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3743d050-8c4a-3081-88b7-7033f743bddc | -11.78898 | -57.35222 | 2026-05-26 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ec479b6-848e-3cf1-9524-d38cb58f2a28 | -11.73861 | -54.81045 | 2026-05-26 05:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c5af94f-6073-39e4-a63c-fbf778570b43 | -11.94518 | -54.09682 | 2026-05-26 05:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6548dbf9-e02a-3234-aad2-4e948870c0e7 | -12.05452 | -57.41808 | 2026-05-26 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8996d0f-9b7c-398f-ba84-acf265b8b11a | -11.55738 | -56.93616 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90bd2f59-6497-3f76-b28f-0a9716c2f1fa | -11.54662 | -56.9346 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ddd69b00-c57f-311b-bde7-6d0249056e6e | -11.39903 | -57.54746 | 2026-05-26 05:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75a888fb-f3f1-33f3-8e49-83e61bbc0ec9 | -11.91759 | -57.03962 | 2026-05-26 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cbf89d6-8585-321b-9e53-95e0ccfb01aa | -11.96544 | -56.80972 | 2026-05-26 05:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 10b2fe13-82fd-383b-894b-c1243d245cd6 | -16.17108 | -58.47717 | 2026-05-26 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 80893fec-2031-3981-9833-52e9a573884e | -17.95649 | -54.46441 | 2026-05-26 05:21:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6297b670-81f0-3b35-afb8-b19becaf7136 | -12.44871 | -54.453 | 2026-05-26 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0636d68b-9b9d-3b0f-9f6d-f10d706911eb | -19.76113 | -54.08045 | 2026-05-26 05:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0c232cd0-4c4e-32a7-b067-94ac584fdd17 | -21.95297 | -57.59314 | 2026-05-26 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81bbbf08-0da1-3fbb-837b-f4eaa87cc4b5 | -21.26505 | -49.47569 | 2026-05-26 05:23:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 67943a8d-6661-36c4-a977-4f9f764e19f1 | -21.28958 | -56.10252 | 2026-05-26 05:23:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31f4d862-1946-30f3-8ca3-2e2a3bd9b010 | -20.19405 | -49.56793 | 2026-05-26 05:23:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6269950a-fa6b-3503-b829-c03ee2624201 | -20.19451 | -49.56253 | 2026-05-26 05:23:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 035d00d4-9b0a-3992-93f8-e6157327a0c1 | -19.76172 | -54.07513 | 2026-05-26 05:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 77bf755b-37a3-3721-bd04-9e209b731853 | -19.76592 | -54.08092 | 2026-05-26 05:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a427a35c-4af2-3456-9df1-7b6bbdb4a34f | -19.76651 | -54.07562 | 2026-05-26 05:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b48b176c-ccbf-3670-88c4-20735758403a | -21.95274 | -57.59422 | 2026-05-26 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d4ec14f-ab61-3721-aee9-c2b6b69ff980 | -11.3584 | -52.9514 | 2026-05-26 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 73d097b5-b61e-38ae-a38a-577bc7e99f1e | -11.3773 | -52.9496 | 2026-05-26 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| af76fdc7-dc8c-3bc0-a370-4666e096a915 | -11.3773 | -52.9496 | 2026-05-26 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 28f43a3c-2f0d-3f9a-afd7-a3b9ec6a16ca | -11.3584 | -52.9514 | 2026-05-26 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| b1d1f869-15a6-333d-b378-30abb75ddec1 | -11.3773 | -52.9496 | 2026-05-26 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 6fad74de-5309-3aa7-bc84-fd37865327b3 | -11.3584 | -52.9514 | 2026-05-26 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 2812e51b-0c2b-331f-b129-2e8094ec119a | -5.20383 | -56.04529 | 2026-05-26 05:50:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16569ef1-a49b-3997-ab95-3d59b8b358ed | -5.2062 | -56.04529 | 2026-05-26 05:50:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95820ba6-91ce-3648-90be-881cf897baea | -12.05667 | -57.41703 | 2026-05-26 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3b2ff12-8535-3b44-ac6f-3df76832acda | -6.52652 | -55.06843 | 2026-05-26 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 638381ec-bc4e-3c3f-89dd-fc055022c12a | -11.2211 | -53.83049 | 2026-05-26 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5500342d-16b6-3e39-936b-3453bc359633 | -11.96618 | -56.8066 | 2026-05-26 05:53:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd2b0e46-5df8-3d24-a998-89aef0e7d289 | -9.0322 | -63.33579 | 2026-05-26 05:53:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 728c5f03-e858-3139-8bf5-c1732cd8c8ab | -6.52707 | -55.06437 | 2026-05-26 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9d7ea3c-5d15-3ee1-8189-b31c5fae3d99 | -11.17548 | -55.91625 | 2026-05-26 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13b7cd03-329e-381b-a1d0-33ff5b45e6c1 | -11.17112 | -55.91814 | 2026-05-26 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 51268e99-cad9-36cf-9477-af7bc86bf4a1 | -11.97181 | -56.80736 | 2026-05-26 05:53:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84b146b0-3b20-3465-a172-72d67cf6c6e1 | -11.54245 | -56.94179 | 2026-05-26 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07b3b4e1-447e-3ce4-99a3-9d5e3c12fc78 | -11.54848 | -56.93882 | 2026-05-26 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ccd61f0-e515-3043-985e-2f9d55384bad | -11.97135 | -56.81111 | 2026-05-26 05:53:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README13.md)
