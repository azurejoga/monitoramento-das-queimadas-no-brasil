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

## Dados Diários - Página 170

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5990aaa2-6284-307a-9e7e-00b7ca8a4619 | -13.93019 | -44.54501 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3170c0c-4615-3e6e-87a1-34b278e7da0e | -13.92959 | -44.55083 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bdcff8b-db16-386b-87e6-4e6c644f86ec | -13.92911 | -44.52541 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ee187b1-9887-3946-8b3f-90659aa2de00 | -13.92646 | -44.54972 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 35cc417d-bd3e-320e-b4a5-64cd250fb130 | -13.92474 | -44.53204 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e807de9e-9968-3929-bdad-4b1355724ac2 | -13.92411 | -44.5382 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7b26cba7-f147-3cb6-955f-d4607c1d8419 | -13.92105 | -44.53716 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5b1ad20e-7012-3440-85cb-791721d60205 | -13.91988 | -44.51317 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a25498a-2f65-3351-8c22-71b3e2e481bf | -13.91927 | -44.51908 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5841e0eb-0de7-39ff-b60c-4c3e439ade0e | -13.91865 | -44.5252 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f1254e1-c1f0-397d-8aa5-9b3d318b7346 | -13.91696 | -44.51221 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36c4b13c-d8ab-3ee3-90cd-33bd3292bfcd | -13.91632 | -44.51815 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74615538-afb8-33e9-97e4-b1f5ab8a520a | -13.91566 | -44.52423 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 046f4165-c4de-3af8-83b5-6f35cea8e065 | -13.91499 | -44.53047 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a107821f-4ce3-38ec-9fa8-03101dbbb1c2 | -13.9144 | -44.63298 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bc2f461-1b72-3389-9aef-26da61f78b5c | -13.91315 | -44.51254 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d755efda-667e-3d4a-84b5-4ceaffb6b5e3 | -13.91255 | -44.5185 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e55aa16c-2484-3857-945a-a525be841176 | -13.91129 | -44.53089 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b3d64fc4-d0cf-32da-89fb-eb38f8aaef4f | -13.91072 | -44.63199 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2896b80e-9ee7-32ed-8895-16c88c30aab4 | -13.91024 | -44.51161 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aab793e9-0434-3775-ab8c-059b14179ea1 | -13.90959 | -44.5176 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0358f0f5-0efd-3d2a-8aa2-b8ed255e0b5e | -13.90771 | -44.63245 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb0955d9-0753-3d69-b7d3-840cc42bf6b6 | -13.90642 | -44.51194 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 300c1375-e78b-3335-a419-537cc5f44347 | -13.90581 | -44.51796 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f70f8d2-29d2-371e-b5f8-149faf213624 | -13.9035 | -44.51105 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 46cc7295-67dc-3210-86a2-6accb49592ab | -13.90285 | -44.51708 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ed1882ee-164e-3fd4-83f9-9d610ac07c4b | -13.9022 | -44.52315 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0993a598-fc40-3252-9068-1d9a288868ee | -13.89969 | -44.51139 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b41183a4-dca7-3bbe-9eb4-b5d85043d217 | -13.89908 | -44.51745 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 94cf6371-5890-355e-a09c-052c77436b90 | -13.89413 | -44.66063 | 2024-10-09 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9848ad6d-60d1-3de2-af09-128ca8de8969 | -13.89134 | -44.66097 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 69f6a53e-3309-39e2-8893-07db23249363 | -13.88749 | -44.65978 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3a882e77-af63-35b0-9752-8c1f7facb8bc | -13.88686 | -44.66556 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 271538f7-8b81-38d3-8407-26f26de8d7ed | -13.88528 | -44.65433 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3bdca93e-873d-375c-b668-5c8680ed1264 | -13.88468 | -44.66021 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a1991ed2-59ce-340e-921c-e8ba4caadcf5 | -13.88409 | -44.66606 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 070b7762-4926-3f84-a30c-32e4d34b18ae | -13.88082 | -44.65919 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| acdd4340-1bfa-3ce4-8466-f6bf22338594 | -13.88018 | -44.6651 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 340962b1-fb81-32d8-a32e-768d7d9b47f9 | -13.87957 | -44.54453 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8d035395-7ace-3f88-b8b5-b17af0e0df12 | -13.87862 | -44.65358 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2f517eb4-cc9c-3223-8afc-0430a5e78cc9 | -13.87802 | -44.65957 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a09266a3-aec8-394c-afe7-444aa96cbcfc | -13.87742 | -44.66549 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| de64ad24-6bc6-33df-ba34-82cd606b2bfa | -13.87481 | -44.65244 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8608fe9d-821d-3d14-991f-f884c2755b80 | -13.87417 | -44.65839 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ef3cd921-e0a0-39ce-9e1a-2ab48b2a6351 | -13.8729 | -44.54356 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 07a97c0e-a14c-3327-8200-57a4722f6083 | -13.86559 | -44.54863 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0f9173b2-3537-38e7-947f-a3ed9665b0b0 | -13.86495 | -44.55466 | 2024-10-09 05:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ff676532-205f-3156-8bbc-89791be743dd | -10.80177 | -45.14803 | 2024-10-09 05:04:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49be2b98-9f96-32b8-96e2-0373c9a80879 | -10.80115 | -45.15299 | 2024-10-09 05:04:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bee834d-4201-35cd-a564-479933bcb8fd | -10.31152 | -45.42781 | 2024-10-09 05:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31fb3bc1-801f-3356-95d3-3ac7c304e17f | -10.31094 | -45.43245 | 2024-10-09 05:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a5391eb-0d17-3591-89f3-b8e9861a3b55 | -11.14053 | -45.3791 | 2024-10-09 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f73bcc2f-7258-383d-ad7a-f276f2a3310b | -11.12706 | -44.95464 | 2024-10-09 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3340fe8f-4f35-3816-afe0-1b04f4f0d95d | -11.1245 | -44.95263 | 2024-10-09 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 873447b5-6383-3542-98be-26da6300c863 | -11.12385 | -44.95802 | 2024-10-09 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 055f11a2-801d-3fc1-9ea3-13faff9a397b | -12.99756 | -46.23713 | 2024-10-09 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70d3481e-9968-3fe9-9dca-3580a93c76dd | -12.99494 | -46.23323 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec26ab29-4287-3612-bd87-94b26d198b95 | -12.99443 | -46.23758 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5ecdc96-6ef2-38df-8208-ea7c4b117378 | -12.99217 | -46.23112 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af79cffb-0d13-30de-935f-3743ecb07a57 | -12.99168 | -46.23551 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59251fe5-1bd1-3ea2-9bc7-ba1969b015e6 | -12.98965 | -46.22681 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d0d76e0-d529-31bf-a90a-b83a2ef7835f | -12.9891 | -46.23139 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 906fcf65-8ec5-3154-9fb7-5c583e1f47e8 | -12.98685 | -46.22444 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26c1586b-541c-3b41-b2d1-ab0e00c98ede | -12.9863 | -46.2294 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88b2e217-974f-3731-a9a4-2602370ec545 | -12.98378 | -46.22512 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29f57e0d-16c9-3eff-94da-a08c0827865c | -12.98237 | -46.21017 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18f5eb7f-d2a9-30ea-be4d-a3a524b8eb7b | -12.98192 | -46.21423 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b513dc26-8493-3e82-b00c-d2a4aa96177c | -12.97991 | -46.20647 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 320f43fc-52e9-34e9-bb34-cc27b17dc90f | -12.97944 | -46.2105 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 47abd32b-b5ed-34bf-9c32-12346bf713a7 | -12.97649 | -46.20847 | 2024-10-09 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5f5ac21-fa5d-3506-abc2-b9f958da2f44 | -12.37828 | -44.97476 | 2024-10-09 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9fd7968-c8f8-3032-851b-e39255200889 | -12.37765 | -44.98057 | 2024-10-09 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86426f47-52ab-3161-8917-e2c49f284327 | -12.205 | -46.72556 | 2024-10-09 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7edc44b6-5faf-3c28-be42-f705471685a7 | -12.20452 | -46.72959 | 2024-10-09 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e8d1996-114c-3cf7-a67f-c9f5cf81bf24 | -12.20403 | -46.72271 | 2024-10-09 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e467a8ea-3326-30fb-b56d-f3ecc3d1c860 | -12.20353 | -46.72673 | 2024-10-09 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2f33bbd-d9ea-3538-ad34-b411fba3e865 | -11.79467 | -47.38908 | 2024-10-09 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7ee6469-0a52-398f-a37e-11197a90321d | -11.79422 | -47.39259 | 2024-10-09 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ed9bd8c-8700-351e-a379-24bb21657d28 | -11.79065 | -47.3871 | 2024-10-09 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2ab64fa4-2aaf-3a32-b87b-1bf788ac9e0f | -11.79023 | -47.39066 | 2024-10-09 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 44c8b5c9-314f-32a6-833b-8bc76ca8a8ca | -11.78967 | -47.38475 | 2024-10-09 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bd5a802-bffb-3360-979d-70221eef4fac | -11.78922 | -47.38831 | 2024-10-09 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e9a471b-64dc-35c5-857d-623004c4d4a7 | -12.65646 | -47.03808 | 2024-10-09 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a0355b6-d58b-3d32-9d89-c73eea636b2c | -12.46035 | -47.31408 | 2024-10-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fc8dff2-c540-3858-ab0f-147e27c83bdf | -12.45991 | -47.31779 | 2024-10-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f39f12a5-1819-3a8f-a1e1-dc94c3422924 | -12.45438 | -47.31703 | 2024-10-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c83d80d-d283-3ccf-ad84-ff1386d1b13a | -12.3763 | -47.6752 | 2024-10-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d545b3c-8495-30bf-a17f-96910f4bc57c | -12.37588 | -47.67856 | 2024-10-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 842cbccf-087d-3202-9bcc-b913da482ce8 | -12.37545 | -47.682 | 2024-10-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b72d980-508a-3218-a042-4bd63f7ef8ba | -12.30991 | -47.21704 | 2024-10-09 05:04:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efd6b748-529b-3a4a-bfc9-c5c6b0ed9475 | -10.01089 | -48.84745 | 2024-10-09 05:04:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb546f06-c198-31e8-9ffc-ec1ac942f970 | -10.01013 | -48.85294 | 2024-10-09 05:04:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52a9ef42-e450-3e1c-82bd-fcba440ff57f | -10.00992 | -48.84745 | 2024-10-09 05:04:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 386b386a-0d2c-3584-af4a-9704827b07a5 | -10.7597 | -47.91602 | 2024-10-09 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ceaf49f2-ba08-320a-bcdc-7c97ecd60b9f | -10.75445 | -47.91566 | 2024-10-09 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e63b5459-2127-3e12-8ed0-bca8a7449709 | -10.49446 | -47.53612 | 2024-10-09 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cabbab1d-afe3-3751-acab-24f8d63db628 | -10.49367 | -47.53346 | 2024-10-09 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cef1dd63-c18d-3739-8eac-088a1d0865d5 | -10.49324 | -47.5369 | 2024-10-09 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b58adac-dfa9-3ec5-a7dc-e89cf77876d0 | -11.73776 | -48.41596 | 2024-10-09 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 745fc201-fe62-3bc6-9676-f40f36c4e7b7 | -11.13354 | -48.6347 | 2024-10-09 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README171.md)
