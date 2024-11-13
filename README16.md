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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56497886-62f8-3c32-91ee-ecced762c08a | -4.06932 | -45.8711 | 2024-11-13 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f9d73167-23b0-337e-bf4e-b713bbdbeae3 | -4.04868 | -48.26502 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1171c4be-af14-34a5-a1f6-8d4b08cfef27 | -3.8411 | -46.02027 | 2024-11-13 04:04:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e287b9a-d9cb-361f-8ad9-16e191017583 | -1.84552 | -46.28548 | 2024-11-13 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b91ef34c-11b5-37c7-9f62-53fff681dfd5 | -2.37561 | -45.85153 | 2024-11-13 04:04:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46ef0bc5-fc74-39f1-ba8f-14a859f1aa11 | -4.20066 | -42.33318 | 2024-11-13 04:04:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1832d3ad-1112-386b-9550-722535155a8e | -2.206 | -53.74702 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c94f79e8-6e26-325f-b3bd-9f845745ed69 | -3.14591 | -53.24985 | 2024-11-13 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 20230cba-049a-3627-bdb1-4df18796816c | -1.46543 | -52.30709 | 2024-11-13 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 31671c2f-9feb-388d-a59c-3322df9af303 | -3.52099 | -49.95689 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cebb0681-3791-388b-a5ce-08aebadedbc0 | -3.95125 | -45.77801 | 2024-11-13 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a4864198-dad4-3071-aa89-08b0b97d8601 | -2.60412 | -46.17292 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c680051-9a44-3d76-bbbf-3e53000247cb | -4.05054 | -48.31164 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92274cbe-d00b-3b72-98c9-f58044f1617c | -3.34947 | -48.96886 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 5557a80a-10c4-337b-852d-50494a6bc9ba | -3.34958 | -48.96994 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d3befdb6-a329-3e1e-aeb8-f72e8c618b83 | -3.49544 | -50.83464 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0802d73a-a537-35d2-a3b7-6df1f8d4d648 | -2.77654 | -50.30177 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b55f9cff-1241-33ff-ac4f-91ee86fcbd49 | -3.54527 | -51.59713 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f426250b-bfff-34bf-a46c-e92acef8e7e8 | -5.80187 | -35.58387 | 2024-11-13 04:04:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5af427f4-cb8e-326c-97a0-293dfa763d98 | -2.45919 | -48.82453 | 2024-11-13 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86471015-69b3-3df2-8d83-c1410982b34d | -3.14987 | -54.48769 | 2024-11-13 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 024ef77f-c5e6-3596-b82b-53d877895a35 | -3.54962 | -43.47483 | 2024-11-13 04:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05bad76f-1766-3ed6-a3ab-21046a3acf94 | -4.41478 | -43.99653 | 2024-11-13 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2d3c6a9-904e-3692-9088-e396bd69ea79 | -2.97824 | -51.24813 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0bf5dbc-db37-3629-9f5e-4db46248b4fc | -2.73347 | -49.18698 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d01064b-aafd-366d-84fc-8ffebc5ed6ae | -2.27648 | -48.81212 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| baf40035-2255-331b-a2e2-0c11a3fed4b1 | -3.06544 | -50.33461 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 3f0b3414-f41c-31fc-a8fd-4c7a4adbefba | -3.17021 | -50.45209 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 572b741c-98ff-3bfb-9df1-3e1aa5dae820 | -3.24894 | -46.17815 | 2024-11-13 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9472faf-d12a-34dd-99be-a0e31656236e | -2.24142 | -53.74654 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1b0123ff-cc11-3e4d-b8a7-f5b62e7c334d | -2.16414 | -50.65691 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca3f868e-ae75-3378-8651-07a94653a9d0 | -2.72706 | -45.29651 | 2024-11-13 04:04:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6a24d18c-1845-3a7e-ae4b-8801506669d7 | -3.35351 | -48.9755 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d49e5d9a-6cb1-3556-b94e-258c4aae3937 | -1.84617 | -46.28152 | 2024-11-13 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 653c9b53-aa39-3fec-ad2e-a2af64635a78 | -2.21176 | -53.75492 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| edf534b0-ee57-373d-8c20-1744cb4ec842 | -1.82857 | -47.80948 | 2024-11-13 04:04:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51526a75-cc2f-39cc-8f9a-c4b5c075a52d | -2.72784 | -45.29161 | 2024-11-13 04:04:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 46628436-020e-3041-95cc-54e7e593b4e3 | -4.07778 | -44.75533 | 2024-11-13 04:04:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51c52b1d-42ef-33eb-9a1f-68372f931c18 | -4.13369 | -46.63267 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c3c6b6d-9713-303d-ab8b-640cce3bda8c | -2.6239 | -46.82121 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85f0ed74-d837-34c9-904f-ac8201579a0a | -2.31568 | -50.68536 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58648311-c82b-3990-929c-10bb0e4a41ea | -2.56132 | -49.11404 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3dcf83f4-6a66-35a5-864b-b8f1725d3820 | -3.05267 | -50.34347 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94bb083d-600f-329c-b616-60511b77388e | -2.93944 | -48.31786 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5956fa68-9160-3a21-9102-1ecb7ab377ad | -1.2785 | -47.91016 | 2024-11-13 04:04:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7df3ff40-a403-3c04-b9cf-300ab6bb7576 | -4.12716 | -46.86018 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0c808bf-c1e5-3926-a940-27d12981b196 | -4.77064 | -43.11802 | 2024-11-13 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19cbc2b4-c877-3a4a-99a0-2e3d3c3e23c7 | -3.94514 | -48.17956 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 853dd372-b46a-3428-bc1d-bccb59d63b2f | -4.06534 | -45.87039 | 2024-11-13 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 13a2b530-5253-3309-8a4f-638defcb7f7a | -1.65171 | -52.55237 | 2024-11-13 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b92866f3-b485-36cd-9ee6-367f0ddf4ec6 | -3.33604 | -48.98847 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e87e491-1d7a-383c-ad19-7d237315aac7 | -3.07523 | -50.34356 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 239eb82f-8ff4-37fe-92fb-9f7b41a47fde | -2.61117 | -48.25326 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 822596ac-5e7c-3383-9e4e-147c5e6cac59 | -2.12354 | -50.69016 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d31860a5-af26-34f0-a709-04e1c4663f20 | -4.67627 | -44.57841 | 2024-11-13 04:04:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ddd8c9f4-3b3c-3b71-b757-d9c537332b13 | -2.62759 | -46.8191 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e6705d6-4287-387c-84c1-6f44cba095ae | -3.10223 | -54.30216 | 2024-11-13 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 089f6618-9ae9-3894-9f04-a4d7dadb32d8 | -3.39756 | -52.47893 | 2024-11-13 04:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d590bb1d-f8c2-302b-8a8a-3da58b72bd00 | -3.03209 | -48.08135 | 2024-11-13 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| bca9a648-aedf-3a58-8d65-9472e4da58d4 | -5.24764 | -37.69408 | 2024-11-13 04:04:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0c62d6ae-a9cf-3d90-b422-b8082fb97a1d | -2.78263 | -50.2991 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cef7cc87-2187-3185-befe-7504eef0b40c | -4.19787 | -42.3291 | 2024-11-13 04:04:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f85079fb-213d-3e27-b6af-b433a511c137 | -1.0332 | -48.85068 | 2024-11-13 04:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dad0f11e-d6cd-32d1-b389-1478cd773091 | -2.66067 | -46.81456 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ca6797d-18b1-3b77-8d56-6a38b6005335 | -3.04778 | -50.33895 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ac6a03c-7844-330d-b2dd-694e17fff9e9 | -2.98878 | -51.03909 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 406babf8-c02b-3326-865e-d3a58bd31de6 | -3.94819 | -48.19003 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 89626050-4516-3251-84bb-4b7fcdeb1610 | -3.35552 | -48.96509 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 11dcd8a7-01eb-3fa6-8e9c-2aebde5a0c8b | -3.84161 | -46.02012 | 2024-11-13 04:04:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9b159c7-52ca-3496-b063-889c956195d6 | -3.76179 | -50.70201 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4b8403ca-ea9f-3d34-b8f3-e896134d4d76 | -3.85399 | -49.11716 | 2024-11-13 04:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25ee0901-16ba-3c3e-bb68-edbd99a372d2 | -2.30882 | -45.07359 | 2024-11-13 04:04:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7127a6f-64cd-3f5e-95d1-db2f5eddfe6e | -1.00744 | -47.17732 | 2024-11-13 04:04:00 | NOAA-20 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0775b7b-dcba-36fc-9a1e-94fb37647227 | -3.34449 | -48.96801 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 9ef26c92-6e9c-3c92-80a0-78d8ef8bebcc | -2.12288 | -50.6941 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a52d13b5-2ff2-320c-9d67-dc098615fca0 | -2.99386 | -51.04416 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7879cfbe-c04d-343e-92fb-fb31ae0b1638 | -3.92028 | -44.3185 | 2024-11-13 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39f8156c-2f3f-3b10-8940-8756699ff79f | -2.72392 | -45.29097 | 2024-11-13 04:04:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e6d43b5-6fac-3a37-8270-48654bb9e74b | -3.35132 | -48.95746 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| a7b18e88-5431-3ef4-a89b-be139a0e6f36 | -2.63756 | -46.16184 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05b82e44-f4ac-3f66-a7d7-72f68b28d349 | -3.33856 | -48.97298 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1326ef30-c5b0-3dd3-a0c1-25c0a9a033c4 | -1.3947 | -51.1094 | 2024-11-13 04:04:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5577739-aead-385c-b65f-307cb78fcff7 | -3.24978 | -43.26517 | 2024-11-13 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7b101829-a239-37bb-91cb-b7c84bdd8ae7 | -3.33764 | -48.97869 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5ecc50a-5e3c-3885-b692-28bb48caa9b2 | -3.76142 | -45.08211 | 2024-11-13 04:04:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03b42403-c4b1-3a96-926b-21c504e8a655 | -2.62457 | -46.81713 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99b662aa-a9f6-3208-bcbf-db67e20918ad | -3.35261 | -48.98228 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9868bdb0-5032-3bfe-83cc-9963708b8474 | -5.79778 | -35.58371 | 2024-11-13 04:04:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aaa3082b-58ca-3ffc-a21b-5b1b0913b5b1 | -2.66364 | -46.82365 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20b7f51d-6c3c-328a-90d5-1753ff4f168d | -3.78863 | -50.10173 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad183e48-4a44-300a-a24e-f1fcfb1cb237 | -3.34666 | -48.98711 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45db24e4-c3f5-3b40-b17d-8b63e81bb559 | -2.11718 | -50.69317 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70b7ff41-dc0d-3879-94bf-dd5e482799e8 | -3.14152 | -54.49391 | 2024-11-13 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f595bcd4-bbf6-3c03-bed7-bba1f314560d | -2.97774 | -51.24615 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28faf9b9-6f40-35f2-899d-f75c4f9ce09f | -2.71258 | -47.73083 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1cc2c7d-f132-3e59-8125-437a3a5468ab | -1.8299 | -47.81016 | 2024-11-13 04:04:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fe3c30f-b6b8-31dd-8019-19c8f0b08e60 | -3.06305 | -50.34888 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2288f177-0c02-3785-b9e5-a38e3e199f8c | -3.02362 | -50.97804 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53dfaa58-5fb4-3913-b63a-f1d0bef539b4 | -3.05656 | -50.22038 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e096fed-d3b5-361f-a483-7c034a3e10e3 | -3.4201 | -51.06118 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README17.md)
