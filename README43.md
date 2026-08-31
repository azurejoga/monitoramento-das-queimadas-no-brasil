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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02853cb2-b6ae-3d4d-a44a-05fdbbb9ae27 | -3.96914 | -60.02466 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f04dce8-6646-323d-b9a0-fab3c9bfa27d | -5.9618 | -57.68533 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 70b499f6-8505-3803-bd84-9212ff07fb5e | -7.84801 | -56.54877 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb918c91-ace5-378b-863c-7852c3b43447 | -6.12004 | -57.68141 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0869cdd9-ebb5-3e1d-a065-6f6e320d05f4 | -1.2496 | -55.69911 | 2026-08-31 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a977b11-e6a3-301a-94fc-4779130b6c59 | -1.60444 | -54.39759 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7309251d-6dc9-3c08-a4b9-9213338c5cdf | -6.86668 | -58.94813 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c6ca86d-c392-3286-a7a3-58edc6ba17d1 | -7.50141 | -55.33342 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e6d3979-09cd-35c7-8218-cac7f8ed4314 | -6.9058 | -59.49704 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37b9fc67-0076-3150-bf01-1a9a99052b18 | -7.35202 | -55.18085 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d99118c6-f7bc-3d2f-86f0-2808efc50bab | -6.49434 | -53.26076 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 032b102d-4c54-36d0-bc20-e71067f012b1 | -8.23499 | -49.04531 | 2026-08-31 04:57:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd3d6c80-d067-322e-a4cb-bb6843932b07 | -7.34024 | -60.59979 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a3f9491e-288b-3a3e-86ef-3a6318c12e22 | -3.97085 | -55.64953 | 2026-08-31 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 312f747a-e0a7-3d1e-a07d-03af6ad67e23 | -5.25668 | -55.90966 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6373db9c-b182-318a-ae00-dc54a8c050fb | -7.74247 | -44.73817 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1bcdfd4-8756-3509-aa1f-1893d55056af | -6.88863 | -59.45077 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b513c51-4778-32c5-b535-d25b8f831140 | -1.59801 | -55.04651 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d4fa7b1-439a-3d0d-bd39-12cb31544a2d | -7.25714 | -60.63338 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6cdd77b1-fbd7-3421-84ed-7e42c8ec1167 | -7.39693 | -55.17712 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdbd755e-6fd3-3e02-9b00-aa95f6064059 | -6.11935 | -53.86435 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abba2f13-a079-398f-b8c1-3e63b7fa8d96 | -5.8793 | -57.77928 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1ff9a8c1-7531-3db7-b805-fd690f14f80c | -3.17856 | -53.16051 | 2026-08-31 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5afc22ce-5451-338f-a74d-1f8405a5770e | -7.11906 | -42.75697 | 2026-08-31 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 21ae476a-c7da-3871-b23e-58c3700cbf86 | -1.59721 | -54.40007 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 636a99d5-b0f5-3c9d-9111-0e308ac98754 | -7.63934 | -46.7303 | 2026-08-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 92a52683-fb40-359e-b3c6-1c58bda4868b | -7.30372 | -60.58066 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1611944-6b9a-35a7-b0e6-2ea1f7627d25 | -5.24257 | -55.88859 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be448432-cbcb-3f99-8d42-90aaeb184179 | -6.40395 | -45.43135 | 2026-08-31 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da868d79-ace3-3b5c-9e59-0aaa3b4f575c | -5.60458 | -44.00429 | 2026-08-31 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3daa8e70-3047-31a3-810a-ce90cf70a988 | -7.05678 | -52.71609 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee1ed9e6-d32d-30ff-a24b-1a752339719e | -7.52079 | -55.34006 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 800ae3a9-fe23-37bc-82e5-62e50a7fe71e | -7.28234 | -60.65356 | 2026-08-31 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98d2bbff-424f-34b0-afb3-497f277993cd | -5.48158 | -57.15334 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2715d4cf-e85a-3826-86b1-f297c6f7479c | -7.52245 | -55.32958 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40b22695-8d2a-35d8-8878-9eff72395242 | -5.88972 | -57.75757 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b5c4800-8bbd-39d8-ae75-67bea959a48f | -5.24363 | -55.90382 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| a581f808-0989-3612-8418-14bee945afa4 | -6.88353 | -59.4069 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07ee21f7-0f7c-3504-ad6a-36eb23ded33c | -7.34816 | -55.18382 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2773a5e-90e1-3bff-b32c-3d919125d4c6 | -7.61367 | -55.29078 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12e77a84-4a65-3ed1-972e-00dbc00e6ee5 | -7.97817 | -44.29231 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36effe67-3192-3b7a-8932-9ca241475462 | -4.8541 | -55.83519 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4986d63-2952-3fdb-8b88-b23f4fa194a6 | -2.54216 | -48.24614 | 2026-08-31 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6b64b14-ba4a-3fda-8641-9e4c2ebee2b8 | -7.50694 | -55.36303 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c197dd1a-7a05-3337-a2f1-37b02d2de6ed | -5.24198 | -55.89227 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 13ca2494-775a-336a-b281-e31906869aa0 | -7.91871 | -44.24821 | 2026-08-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8b6449a9-081e-3060-9545-d36edcc0e8ea | -8.21691 | -54.93725 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 885846de-02d7-37b0-a4a7-13307e03bf5d | -3.76396 | -59.335 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2b3d856f-4ac6-3d61-8d45-ec1d60055b47 | -6.25062 | -55.41531 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61a42fc7-1350-3d7a-9dea-e4a1fcb5cf1d | -6.25761 | -53.65178 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 935db8fc-6069-3db2-b567-0b2236630819 | -7.25929 | -60.63285 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10629bde-9c52-33f2-bb9f-92c4a0dc0107 | -8.14336 | -54.97177 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9421c368-2bbe-3032-954e-fa0a6e8dc099 | -5.48516 | -57.15395 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97ffbae5-1f36-3caf-885c-eab773fe2873 | -6.9217 | -55.70821 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 496199f1-96f0-3195-ab69-20fdf72264d9 | -6.79057 | -58.99665 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a58dff2-1802-3aa3-aabe-1cd36437e2e8 | -6.60368 | -58.60969 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9593722e-2954-3092-93ac-e832789b41a0 | -7.41436 | -44.25354 | 2026-08-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b99b65d-32dd-32d6-9e1d-ce5a1a49f21c | -3.97143 | -55.64585 | 2026-08-31 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77db2965-db69-312b-b9e8-dcfe3dc6ff12 | -6.7402 | -56.33887 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5240165f-6967-3265-9775-6790d8257cd3 | -5.25386 | -55.90542 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e6b36dd1-ae3a-3324-8d56-363a276d0261 | -3.88687 | -59.4054 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c199c6b2-f54b-3fad-bab1-4637a015f055 | -7.11142 | -42.76608 | 2026-08-31 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fb9161fd-34f9-3405-ad84-a6fcfa4f1e63 | -6.11896 | -57.68705 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8a5bfd3-c51e-3818-947a-3ae8601b581c | -3.54067 | -49.47169 | 2026-08-31 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 920b9ce9-e5e6-39c5-8058-764ff1900316 | -3.4659 | -51.89178 | 2026-08-31 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e91a5d33-a468-3460-a2bc-267763ebf84d | -4.13787 | -56.32561 | 2026-08-31 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e76e3712-a1f4-3b13-bde8-b199a78e1fe3 | -6.92671 | -55.71997 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd52a0fd-546e-37f5-8695-73f1e6c4d6c7 | -5.95012 | -57.68786 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a364b722-31c0-39a5-ae4a-96cf05c1d6e4 | -3.61854 | -55.47836 | 2026-08-31 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0bef539-b592-333f-b012-7623a1fe24af | -4.95811 | -55.84401 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 909c7ab4-ed0e-3610-b14d-eb87e17c1826 | -7.05962 | -52.7203 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a6fc971-3cd1-3222-95e7-dbbe63c96015 | -3.41868 | -43.37561 | 2026-08-31 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9f0a8de-06cb-3c09-bea4-4c1e74c55067 | -7.61937 | -57.61869 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7396d342-5b5b-3590-855a-5de7c4bd3bd0 | -7.61422 | -55.28728 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dce71ff2-fcd6-3559-9498-48de69858d4b | -4.16153 | -60.69575 | 2026-08-31 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69b67a3c-acc5-36ae-89b1-ec5eeb4a50b6 | -3.62057 | -60.55048 | 2026-08-31 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26e03ebb-e9f4-3674-bf51-c956c9bf8408 | -4.96949 | -55.83831 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33d407bb-8d2b-3aa1-86e0-f662f456aca8 | -6.23109 | -55.4958 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d094c4a7-4cae-3f22-aa18-8dd5f0e34d6d | -5.73282 | -49.13425 | 2026-08-31 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0bc4f6ba-10ca-3160-82ae-4945bfaec1f2 | -5.96251 | -57.68098 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9aa01b48-0f91-3125-b952-d4f2c10dea77 | -7.52909 | -55.33064 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d35ae2e-ba8a-3051-96ed-659bf13db64b | -7.48426 | -55.31274 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fbd1f32-3df2-377a-b19d-46ea030bf763 | -5.8945 | -57.75495 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28437130-2621-3029-971d-0699b707ff78 | -7.97748 | -44.29499 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86fb9774-b653-3fd9-9a89-35f8d293a514 | -7.52854 | -55.33414 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf80afee-804f-3732-8cbe-cb027c2bcb4c | -4.15467 | -60.70895 | 2026-08-31 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69758036-051b-3428-a907-6fc0a7c31f1a | -6.62915 | -53.17999 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 11dd2ce9-10e1-3011-9983-88956752f66c | -6.72533 | -56.34417 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7625635-03fd-34da-9f48-f8a298235340 | -6.90188 | -52.83838 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dca125be-e090-38cb-b34e-790c61ee179f | -4.09595 | -50.42617 | 2026-08-31 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ca5e190-9926-30e0-b743-82b4f647579c | -1.40672 | -60.33305 | 2026-08-31 04:57:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e07a0b0e-493a-36c5-a964-910137a7ae69 | -7.28896 | -52.36077 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b957540c-b165-33dd-bf42-c13d378e0d6c | -8.07918 | -45.47236 | 2026-08-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 930c1300-56d6-357b-ad01-be811c92b66e | -7.53131 | -55.33817 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04342324-a665-3c61-8130-dd6420748cff | -6.39466 | -45.49807 | 2026-08-31 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fbcfcb3-7221-35a7-ba87-780cf00267e9 | -7.2844 | -52.36761 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb30b00e-2423-3a8b-a8c8-ccee36c2b54c | -6.16084 | -53.48627 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebd90860-8660-3d2f-a2bb-dcf2c43b0745 | -4.8581 | -55.832 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0f1ff5b8-57b2-3584-ba4d-41feb251c0c6 | -4.23115 | -53.49843 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 711fe4d3-e533-333f-893f-d51d044e0c66 | -6.90809 | -59.49108 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README44.md)
