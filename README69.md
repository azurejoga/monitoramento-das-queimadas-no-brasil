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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d67083d-716a-3f47-bd79-c5022d0518a5 | -1.61752 | -54.92373 | 2024-10-10 04:17:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4016662c-23ae-3a53-bba7-7b99e3690cda | -1.52094 | -55.41657 | 2024-10-10 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a7d1f23-5dec-39e0-8140-116df9d4784f | -1.52009 | -55.42176 | 2024-10-10 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09d4082d-7935-337e-8e05-0757feeeb084 | -1.25554 | -55.70306 | 2024-10-10 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d4e4ad8-3b94-318f-a0a3-6e93be922a39 | -1.24988 | -55.69637 | 2024-10-10 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b2971f7a-4bfe-3a76-846b-ea2d8fbe40b9 | -1.24902 | -55.70164 | 2024-10-10 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bca5d893-fe3b-30ab-b171-30ccbba9495c | -1.24812 | -55.70716 | 2024-10-10 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7326ca04-6506-389e-9fed-f5d4cdbcc6f5 | -1.76678 | -54.97598 | 2024-10-10 04:17:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdd05e75-1a52-3510-9006-d5d659d21ab4 | -4.8334 | -55.80321 | 2024-10-10 04:17:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba31e101-2c46-3290-a25b-f92e8f27914f | -4.83248 | -55.80844 | 2024-10-10 04:17:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fc353c6-b5d0-3472-90aa-575f7cf09736 | -7.67603 | -54.83323 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b8ec5ac-7c91-3fdf-ba88-f6068a22f6ce | -13.39858 | -44.68859 | 2024-10-10 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 656e9492-8d40-3245-9b45-3d9863885c88 | -13.38165 | -44.68584 | 2024-10-10 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30a0d99b-bf67-3977-ad4e-4f9de79b5701 | -13.37882 | -44.68161 | 2024-10-10 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60ecbfee-fb23-3acc-9a54-ea449aad8c43 | -13.37826 | -44.68529 | 2024-10-10 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc6131a2-cfdb-31c9-a65d-7320176f74db | -13.37315 | -44.67317 | 2024-10-10 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e4607e6-1c12-3f85-9ba0-76be2cdf45d5 | -13.40381 | -46.91047 | 2024-10-10 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f1d278e-8db2-3e6d-80ce-2a1ab6e3ee6a | -13.09157 | -44.45935 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be4d53dc-a803-3081-8072-34c342506317 | -13.03446 | -44.94995 | 2024-10-10 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ebbab61-4e4b-3761-8b3e-5a73f2b7dd7c | -12.36302 | -44.73095 | 2024-10-10 04:19:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b077781-b793-3732-8d5c-c216efddacff | -12.71157 | -45.46466 | 2024-10-10 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 75402076-da8d-3ea0-bf4d-42e5d696c827 | -12.71102 | -45.46821 | 2024-10-10 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3eff158-fba1-389f-b98c-46d8e7b373f1 | -12.71047 | -45.47176 | 2024-10-10 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0415153a-e2eb-35bb-827b-961107bb4e5a | -12.70824 | -45.46412 | 2024-10-10 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a78d8e2-32b8-3ea3-963e-88b6e1a0d2d4 | -12.70769 | -45.46767 | 2024-10-10 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| edbd3bf9-5011-3992-a08e-323785f3bb04 | -12.70714 | -45.47122 | 2024-10-10 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a0c382b-ed30-39ec-b1ef-d1858498af15 | -8.53999 | -45.47735 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89d4427b-b4cd-31f1-94f3-65ceeed3308f | -8.53223 | -45.46173 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d611f8f1-5218-39b8-a97b-7ddd5854c6d8 | -8.53167 | -45.46524 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfc5ce72-a4bf-33f5-ad4f-2318eb854780 | -8.87413 | -45.86259 | 2024-10-10 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9780bd41-5e6c-3970-8078-efe71dba2d88 | -8.87136 | -45.85849 | 2024-10-10 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec6bbed0-c2e2-3412-aa11-2594a0e592b5 | -8.86746 | -45.86148 | 2024-10-10 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ddf74cc-6247-3447-ac71-b6a2d65a9998 | -8.57958 | -45.77887 | 2024-10-10 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 559076bd-1ec1-3d15-b3a3-f876ba2e9bf0 | -7.63125 | -45.27525 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 491144d8-6c37-320f-8177-b3aeb37300da | -7.62903 | -45.26775 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3607e664-b1c4-3d20-8a17-892aa8f4a211 | -7.62847 | -45.27124 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 132f7670-035c-3f4d-a502-ad66f5724f0f | -7.6257 | -45.26723 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c005377-afe8-383f-8ee8-ba9a40210384 | -7.62515 | -45.27071 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 440beacb-426f-3980-be09-e951bf888180 | -7.61468 | -44.86215 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45c63cd8-c54e-312d-8a31-aa5b84522b63 | -7.61464 | -44.84076 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3daed548-0566-3a81-b766-d8ec3ffe965c | -7.613 | -44.8512 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b069ae83-9c03-3638-9915-bcd684fc6b5e | -13.00383 | -46.25248 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45b7d36f-9d44-3cc3-8107-8fe7ac124ae0 | -13.03333 | -48.67235 | 2024-10-10 04:19:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 514447e9-782d-3990-abbe-a65311dd9242 | -3.214 | -42.70665 | 2024-10-10 04:19:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d7a2dc5-b3b0-30e6-ab30-9c69332c4134 | -13.26121 | -50.28327 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e3ed4e0-70ed-3323-8ac7-8b219b413c29 | -13.2574 | -50.28257 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e2049ca-d7ad-3081-b735-94a2566b9d36 | -7.21378 | -44.14265 | 2024-10-10 04:19:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3b4c0b9-2701-3915-87d7-738aece3d835 | -7.21323 | -44.14615 | 2024-10-10 04:19:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3af29bcc-bb5f-310f-9812-9f6628bb333c | -7.20504 | -44.00137 | 2024-10-10 04:19:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7db04fe8-4716-349e-8f46-5ca5a6a09729 | -9.94302 | -44.07153 | 2024-10-10 04:19:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c0cd5aa-9acc-329c-aa7c-d946e08dabf0 | -9.9402 | -44.06741 | 2024-10-10 04:19:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd082dfe-4577-3622-85eb-148882f9edd0 | -9.93738 | -44.06329 | 2024-10-10 04:19:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84ed33bf-17d0-3334-a8b4-2c2f3259ed1d | -9.51084 | -44.06818 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7532ca9-72e7-3f80-b63c-0e7532b3833b | -7.61245 | -44.85467 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d55d7652-56ee-331a-8a7d-092b35a28fd4 | -7.6119 | -44.85815 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| caa45dd7-54e1-3385-a8f2-4323090f3754 | -13.8382 | -44.54645 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8237f61-65be-3b16-9810-16a0d082cfd3 | -13.83534 | -44.54217 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 127dee07-1058-324a-9fa2-c725ad0f91b9 | -13.82405 | -44.57101 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 114d52c5-0bf9-39e4-bd5d-e10ceed93bc0 | -13.81225 | -44.62655 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0334c82-ac13-3d0a-9745-bf27b9cad139 | -9.44545 | -40.54469 | 2024-10-10 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1f9948b6-e23e-375b-88a1-4acfc8794412 | -9.44474 | -40.54977 | 2024-10-10 04:19:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 59d56032-e234-3be1-bc1b-964c309c9b51 | -13.85237 | -44.52179 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4818b9ab-4d2f-3b43-aa9d-2e8ae52aaece | -14.4398 | -43.18036 | 2024-10-10 04:19:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 43f6f6b6-e168-3138-b4d3-098ea2a0643c | -14.43953 | -43.17778 | 2024-10-10 04:19:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d2bb5cbe-b70f-366f-b9f7-bff8ae626a4b | -13.48762 | -43.46103 | 2024-10-10 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c30583e6-3c63-359a-9ba8-200bb01f7095 | -13.85919 | -44.52287 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8063d78c-d12d-35ef-95c8-60785f1b9f1e | -13.40324 | -46.91404 | 2024-10-10 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9645169-311b-3067-bd85-00167027bdaf | -13.38971 | -46.69893 | 2024-10-10 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 91ed4328-28d9-34f8-b7ef-bb1f54c44005 | -13.38914 | -46.7025 | 2024-10-10 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8acff2e-b133-3d81-a29c-f7f91c14a453 | -13.85184 | -44.54859 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe80420d-9bd6-32cf-8b21-80dc47887949 | -12.70436 | -45.46713 | 2024-10-10 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 256443b9-e1cf-3b79-96ca-28adffc61bb3 | -10.84651 | -42.86077 | 2024-10-10 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe409e8d-580f-3c04-81e5-477b434b35ce | -10.82975 | -43.78959 | 2024-10-10 04:19:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 992219a0-06e3-3a41-bc6a-eb9480ec08b1 | -11.524 | -43.99311 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4573fd09-24b3-3c9d-9597-437aec59dbc7 | -8.40146 | -44.74417 | 2024-10-10 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4950953b-3676-3d49-be49-997be75e7386 | -8.35845 | -44.1263 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 405377ce-d20e-3ca4-ab7e-bc82c2b43ba8 | -8.35736 | -44.13337 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 449c6e64-84e1-323b-8f0a-b0d91611c7b8 | -8.3562 | -44.1187 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b450bef-f5df-37a7-92e3-fa5ac8c10916 | -8.35456 | -44.12931 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1207cb85-05f1-3ef8-83cd-5611305597f9 | -8.35158 | -44.09293 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 850fc792-8e18-333f-b168-d44c9b10e778 | -8.35103 | -44.09646 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9840da94-99d3-3688-bfab-96a77b10333a | -8.35048 | -44.1 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42b5e3bd-3957-37f0-92d3-746733fdb763 | -7.75174 | -43.8292 | 2024-10-10 04:19:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 036cfe06-9b64-3b48-8ea4-087ebf48ac5f | -7.63235 | -45.26828 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5cd0445-ca73-39e2-825f-79d12e166c7c | -7.6318 | -45.27177 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5ac77405-29d9-3ce0-9807-ec0599658bc6 | -8.14082 | -44.44165 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 594061fa-866a-3919-9d56-c3ff9a36e434 | -8.13367 | -44.46558 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 792cfb64-a6e5-3f06-a41a-3e7dd6abfcad | -8.13089 | -44.46156 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9fc858b4-0934-391a-8561-e56e1ce0a912 | -8.13034 | -44.46506 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1443283b-3a55-3887-9c1f-b48187ba5c1e | -8.06015 | -44.78271 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 592c31d6-11da-386e-b66c-892d949d9b19 | -8.05961 | -44.78619 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 197520c5-860b-33ff-83ad-81704e97b709 | -8.05683 | -44.78218 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02569e5a-1fd8-343f-acfd-07cbbf4eca4b | -8.00301 | -44.37017 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9d69edc1-4d81-3c56-b0cc-36eaa25b557d | -8.00247 | -44.37368 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a085c52e-a1da-35fc-be79-a28d1d521044 | -8.00192 | -44.37718 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4454a1bc-0083-3fab-97a3-ff3d10529485 | -8.00138 | -44.38068 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd0dbeeb-aebf-3f36-9e6f-19b3eb0ec183 | -8.00083 | -44.38417 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0cebd02-cf56-3782-86a0-f72615c58ffd | -7.61136 | -44.86163 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 541e0343-96c9-3aaf-bab8-4883ad40b1b7 | -7.2045 | -44.00488 | 2024-10-10 04:19:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1788d31a-ec56-3170-851b-8b6a9123b276 | -7.1929 | -43.8445 | 2024-10-10 04:19:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README70.md)
