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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86c6efce-4b59-35a5-8420-4e34152708ee | -4.24589 | -48.67084 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3af8a34b-451a-3dfd-a3ea-76b240c9a503 | -1.57394 | -54.37655 | 2024-11-26 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8505aadf-28a2-3e9d-a00f-d846fabee94b | -4.76217 | -45.59535 | 2024-11-26 05:01:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c975e319-caa5-3f6d-9efc-5c5911413c91 | -2.23968 | -53.62341 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4ad0443-370a-35e2-ab6d-3b99ef12a71d | -2.25079 | -53.46556 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b57e5c7-f795-3491-a890-513d09f419dd | -2.79493 | -53.0147 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07da40e0-342c-35f2-963b-8a6fdbdeacf8 | -3.42657 | -54.02279 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c18b67a3-2eaf-35f9-a9da-423957da7d3b | -3.94499 | -47.98697 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a68e0c3-6b59-325a-9570-51f450855cde | -2.21202 | -53.79895 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0f6db9c-47ca-33bb-984b-79dbde02f47a | -2.97721 | -53.35275 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1e894bf-487b-34cf-b853-1e705f292359 | -3.11437 | -53.75777 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5094b686-2097-3fa9-a8e0-362d6512f5dd | -2.60668 | -53.96743 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83d14adc-484c-3ef7-b695-b517be41eac7 | -3.25003 | -53.28603 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c4e73351-b2ea-3911-9075-ca600f6c75eb | -3.51319 | -53.81954 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 35b2510d-036a-36e3-940c-55d2567bb067 | -6.93979 | -42.82941 | 2024-11-26 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 08b0c5bf-9ddc-3f33-a107-9bcbaeb7505d | -3.51368 | -50.21997 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40c0173b-a19e-370a-afc0-8af12c78d716 | -3.3442 | -50.51272 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a61d0b7b-1f9b-3ad7-b23e-e27045ec5eab | -3.11663 | -45.08088 | 2024-11-26 05:01:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 766d4280-133e-34e8-8c53-822173976ae1 | -4.23182 | -48.67319 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14d83eca-fd64-30c6-8d7a-0ca2366b0d70 | -3.97112 | -48.06585 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| c9e3bfde-6ae9-31b0-990c-08e7cf8ec496 | -4.53961 | -43.27612 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b25c134d-6887-3336-a2d0-7adc370a6cc4 | -4.53574 | -43.30277 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 83fe5de1-3607-397b-a5fe-9a5ce2cdd26b | -2.77179 | -48.57747 | 2024-11-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8906f903-a275-3a7f-afdf-518ddf34ca8d | -3.28751 | -51.13376 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 581094d8-87e2-3751-98b5-a3c7afce43c7 | -3.11604 | -45.0847 | 2024-11-26 05:01:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d6b645a-49e3-3610-8eb4-1f5c8455fd39 | -3.01892 | -53.41821 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53b4e852-6046-360f-9cee-3bb87c2b3a66 | -1.9914 | -53.29393 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50541073-0079-3141-a145-e8908d86bb17 | -4.13775 | -47.31834 | 2024-11-26 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbee2bed-eb9b-3a83-882a-5347bc312120 | -3.38722 | -44.18138 | 2024-11-26 05:01:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8d8771d6-4ff6-3ebe-b786-c655e048cf3d | -3.80606 | -51.26229 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8d5d93a-7fc9-30e8-b1d0-09feaacde307 | -4.54296 | -43.29831 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f46a6356-95e8-3c21-9e90-08362b173af9 | -3.07848 | -49.1987 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 26368691-abe1-32c8-8633-11e6515c6758 | -1.5767 | -54.3805 | 2024-11-26 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04042ba4-2cea-3d9d-9903-5d63eec75954 | -2.59802 | -54.0659 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e65ff00-dc8f-3576-9003-fe2c023eb5b8 | -2.8046 | -53.01997 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd79a379-4d51-32bd-b967-1f81f3dc6ba0 | -2.7972 | -53.0226 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40c96230-e3ff-32c6-a056-88c47d60eb4a | -3.49921 | -53.82108 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d96f9095-3e53-3f2a-af74-1847681feb5e | -3.50478 | -53.80748 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6808f9e5-f44b-38a4-bb9b-bd520eb1d4f6 | -1.8954 | -54.32107 | 2024-11-26 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffa73e4f-7d04-3e91-a282-e3672838cc15 | -3.71248 | -51.85542 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec76bc09-a53e-3b83-b557-01e6bffc5776 | -2.31111 | -53.59814 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab5b5796-d608-316e-9b3c-d9e064bb7598 | -1.95752 | -53.32214 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 979da989-ed63-338b-a8ca-a998e0e46024 | -3.98638 | -48.07996 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c92af361-57fc-3097-a895-5d4d4d4edbb0 | -3.96527 | -48.06194 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a5ee72ae-fa1a-35fe-89cd-1bd1b797fe5f | -2.80119 | -53.01945 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7808eafb-785f-3add-89b2-90180c2f7f4c | -4.37634 | -48.13055 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e3eff66-253e-3436-a141-3200e3ebaef7 | -3.9918 | -48.07544 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a71e5dd8-33d3-3adc-9a44-5a9c2f04c211 | -1.96032 | -53.32622 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86a131a9-f409-3ff1-ab29-79ef3872e881 | -3.38635 | -50.10505 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbc13f70-c5b7-3d65-ab5d-2ca8d705afb3 | -4.35803 | -48.57867 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 011c6bb5-7abe-3202-b7cb-ab47ae33a996 | -3.98712 | -48.07493 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cfadd5f-6f1f-3ab1-abd0-a2eb56e93241 | -3.16803 | -51.10101 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4ba84c0-357a-369c-babb-e350f7f092bb | -3.08034 | -49.21508 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8d7c20e-9ab5-3927-8588-473f8a33051a | -3.98492 | -48.08992 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c638d2ee-7dd0-3c14-a33f-13ea5b67c1df | -1.45768 | -55.18233 | 2024-11-26 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bc3092c-90e8-3f1e-8ecb-8deabba753fd | -2.80176 | -53.01575 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7df2141-044a-3c04-a625-52760c5fb4f1 | -3.15083 | -50.61831 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d8ebb5d-44b6-3ad2-aede-9c6cde496e6b | -1.98803 | -53.29341 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b8f25d01-1c74-3663-9986-4687d9207f3e | -3.38689 | -50.10154 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15ed59a6-c773-3d31-8776-55f9b8e9fc7f | -2.64529 | -51.77335 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a5b86dc-22c5-3025-8362-97f296a63ac5 | -3.50925 | -53.80089 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04b37085-eed2-34ef-a7d6-764680d3ee42 | -3.80538 | -51.26682 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a355f80-be0a-3453-99f8-8c358e9ec6e8 | -2.99286 | -51.45631 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fecb045-a382-3951-8069-48033517bd11 | -4.27317 | -48.61092 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3e71fc9-2e57-3926-b543-37309da17ed5 | -2.79322 | -51.6834 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f605271e-bfc1-3660-968b-647492717680 | -3.34615 | -50.75552 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 489f11ba-4b6d-3d35-b928-9e540a2d384d | -3.27905 | -50.01714 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f0f9b645-bb6d-38bb-88ac-287c274f6b82 | -3.3945 | -44.17345 | 2024-11-26 05:01:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bdd2754c-5b0a-3519-a33e-244528a52cd1 | -1.62803 | -54.46627 | 2024-11-26 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1aa5f38-1421-38f3-9948-ea6c9fefe14c | -2.60946 | -53.97144 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99451798-b83a-300b-aa36-82d133db49cc | -3.34092 | -53.33348 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9312340-ade0-3d0f-b6b2-acc5251c6d4e | -3.11592 | -53.70356 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 047733ba-83e9-3fd1-9210-40d8b7d07e37 | -2.69621 | -51.36735 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2c52301-87a7-3e30-9305-1495f47d39e2 | -4.09523 | -48.48243 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e16b995-a478-3bf3-b235-daa40e3e51df | -3.38795 | -50.09453 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2a9080b-3877-3a15-b723-79c232b705f5 | -3.97242 | -48.07812 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| b5c68675-1b78-3b25-b913-2c686d48e621 | -3.14 | -45.25576 | 2024-11-26 05:01:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 14f0ffec-db76-351f-83f2-473a82328676 | -2.16989 | -53.26628 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93ec7b35-86ac-3e81-a552-6df7c0b6b9b9 | -3.81161 | -51.37822 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ffa59e0-74cd-369e-9715-d47b690f355a | -3.16152 | -50.58252 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46ed2c3d-2f74-373e-9823-436bcef918d4 | -2.93676 | -48.82389 | 2024-11-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1947250b-52d2-3f5f-aacc-89d138abe375 | -3.98534 | -48.05462 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24a21d6a-63ac-384a-95da-d10424e06aee | -3.49752 | -53.80997 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e13cafd-88f4-340d-b017-8f1e74753758 | -3.49974 | -53.79581 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07a3dbca-7455-3196-9163-ccb982d36319 | -3.43999 | -54.06804 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6a8dac0-c2f7-336a-9ce7-f18efdefbd3b | -3.2922 | -50.53986 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71bbf3ab-2e7c-3146-936e-66f8013f59d0 | -1.89745 | -53.01443 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b86a726-60c9-399c-b704-7630bcc4f9bc | -2.63261 | -51.7724 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c60103c6-69a7-3632-8042-8cc0684921f4 | -2.69978 | -51.99017 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 06d358cf-6639-367b-93d8-4919dd76de2b | -3.71689 | -49.95524 | 2024-11-26 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5cbf97a-dd85-3d3a-8f7e-b8a4f762125d | -3.98859 | -48.06491 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4d4003c-0565-3e47-ae8a-949090271f3c | -1.76956 | -53.63017 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 327dd401-a93f-31c2-aef3-3428a3c11856 | -3.33106 | -50.05368 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a06bfef-4892-330e-a584-504aaef3bf30 | -3.27198 | -53.81844 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0abc78e1-a39e-3b5d-b469-6fca0a4cd466 | -8.05382 | -47.08593 | 2024-11-26 05:01:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e91a08b8-8d35-3311-a520-24f40979250a | -4.31797 | -47.52022 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67518205-dae6-303b-b547-b6a2ffc3d5fc | -3.98565 | -48.08498 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dcac3c6-b0c7-3a96-aaa4-66f3d6d6108c | -2.17371 | -53.80373 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4f079de-b44a-32ee-ae45-0299f606bc97 | -2.33045 | -53.86412 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 301f58d5-ac85-387f-8115-30fe39bc564c | -3.27121 | -50.62645 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README40.md)
