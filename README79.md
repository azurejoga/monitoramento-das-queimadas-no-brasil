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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a32b898-8cc4-3c51-b30b-8d974f1dec1e | -3.54682 | -52.07008 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6721e759-1ce0-388c-8020-af46ceb63ca5 | -2.61965 | -51.75808 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e96aa4d-d807-3608-9e1b-a52dd9be1da0 | -1.63201 | -53.86914 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fde0c6d6-07f9-3246-ad6f-acf390fb828f | -2.60772 | -54.2413 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aec67df5-5562-3d78-8e2f-abf6162e850b | -1.37304 | -53.63115 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d220ce15-067d-368a-a987-4434622a8d38 | -3.49184 | -53.8091 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72cfd122-00d8-38c3-81ea-2e85412a332c | -2.75233 | -54.01272 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49349d5b-cabe-3b83-8a17-d940eae38cfa | -2.65479 | -48.78156 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d9bd0f3f-fe46-387d-b9a0-4ffee68a82ec | -3.27945 | -50.6475 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0ad3d83-b321-3cbc-9e33-d5ea9f005c75 | -3.24912 | -50.77255 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1558d85-fa97-35e5-9342-ba160a05c5fa | -2.22524 | -46.39328 | 2024-11-29 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7995c14-85b0-3837-af1a-1f1e23ffa2fa | -3.24863 | -53.64402 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a19f598-8394-377f-bcc2-61c2d5d629cd | -4.18968 | -50.67585 | 2024-11-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2344e39b-315c-32ec-8205-b0db147b0b02 | -2.69727 | -51.98217 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e55dd5e0-ee2c-37b8-bebd-31f084208bb1 | -3.63712 | -54.44546 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2eeb952e-627c-3bba-857b-7c0c8d0af6f2 | -3.50059 | -53.79638 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aed0f0e5-be71-3d08-8f61-e19b98e430d3 | -3.49407 | -53.81648 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 885b82b2-1dce-3e35-8d80-6327948c0fb2 | -2.71309 | -54.13374 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c40d6e9-7374-35ca-b712-8e65bb14a635 | -1.62418 | -52.45688 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7248ac8-e818-39a6-9bf0-86c20dfe511e | 1.67494 | -50.66817 | 2024-11-29 04:57:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97650343-c606-3712-9ef2-761401d3d57c | -2.62283 | -53.9927 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5981e897-e71a-3073-b2ac-ad7018e07232 | -1.63676 | -52.26519 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0acac928-539b-3b5b-aab6-25e48cb319f2 | -2.61697 | -54.20382 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0b8b695-c0d8-3ff2-a595-86a519b6cba2 | -2.88948 | -55.22419 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8fff2a5-5c47-34d6-91ff-e1bd441cc0d1 | -4.19898 | -48.56778 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c3bf441d-7286-312c-a1bd-636c44174fa3 | -3.93995 | -46.72587 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c7e0159-f434-334a-a68e-6ad3f2a873eb | -0.76343 | -52.45898 | 2024-11-29 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 110906a0-69ba-36ae-b14f-666d110ac5fd | -2.78962 | -53.20937 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5397c1f-4e73-3600-8508-f16536e9b73c | -1.10756 | -52.34514 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48e03c8d-b1dc-3e3f-b0cb-5cbc9374e0b8 | -0.56486 | -51.70171 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc8a79a0-4d9a-39f4-ac4a-7cb19a2d89c4 | -3.29181 | -54.12946 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23140bd2-a64f-334a-8c09-cf970eca92c0 | -4.3129 | -48.20732 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 390e6433-5bcc-3d4b-8a7b-7b8ee670e744 | -1.55331 | -52.27771 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 261a707a-c1dd-3925-ba7b-4c1234dddfe2 | -1.63255 | -53.8657 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78bebdd8-a158-35f5-87cc-1da4bd45829a | -2.75901 | -54.12392 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2fbe2f0b-ff4f-3baa-8812-deebd7f75fde | -2.26249 | -53.46857 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13623faa-e191-3f24-bd9b-24aa0587b6c2 | -1.07223 | -53.64019 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0001fcf5-b222-37de-b470-d38b11000d96 | -1.59035 | -51.26632 | 2024-11-29 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55e5b05b-8332-3396-9e33-491efb9e4ad8 | -2.65773 | -48.78897 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| ba7543d1-7bcb-3f39-b0fe-146df18d7a32 | -1.65115 | -52.72063 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b312a203-651f-361b-a0b9-edd180cc15f3 | -1.15496 | -53.5686 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 346b2eab-7b14-3cb7-afbc-53233efbb868 | -1.69662 | -52.62536 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bb8b8bd-78e5-3449-bf58-3c6cfae5c378 | -1.50806 | -52.63486 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae1c61b0-e390-3254-adae-be029832b997 | 0.98073 | -50.26461 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f8057e6-650a-3480-b8c1-ce4f9a753db8 | -3.71158 | -51.79642 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cdd59545-693d-39f5-9482-362ae191d19d | -2.59299 | -53.96695 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 323af737-f511-3580-b64e-a191eb4294ad | -1.33374 | -51.87778 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64a2fb4d-dc8b-3ae1-9134-d39d85dfc097 | -3.77577 | -46.68839 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2801abb-89ab-392c-b92b-a1b130388129 | -1.26188 | -52.73093 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07b8b08e-9998-3b1d-b5cc-31061ce68469 | -3.36247 | -50.40274 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46269322-642a-3fd8-8f44-0b1d0b6b0274 | -1.46137 | -52.695 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 939d7d31-88d0-3c77-ace2-f82b2b69bcb8 | -5.22694 | -44.91666 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24f4614f-c5a7-3de3-abd9-0215f39d662a | -3.93287 | -46.51112 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4478f1c-90ba-38da-8307-d8187692c543 | -1.35222 | -52.52161 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fce980eb-9644-3bdb-8380-445b64ff9ea6 | -2.74526 | -54.03629 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c72ac01-6707-3374-ac03-aae69e642a22 | -2.47785 | -50.38638 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74397c60-ed6b-333f-a431-94a26c3463ea | -3.10858 | -53.97763 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43496f56-7569-30b3-a13a-31aec0176887 | -1.14539 | -48.33883 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67970b43-3329-3480-860c-7c539a654a85 | -2.88112 | -46.83937 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74f151cf-97d4-3da0-840d-7c7689afd90e | -1.50035 | -51.93997 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76af70c8-47aa-337e-ad78-829fd015fcb1 | -3.61854 | -51.36747 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f932fd41-b1e1-3406-9814-b60838b57584 | -1.60338 | -55.43627 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 722a9d46-4d71-34f5-981c-a9562c90ae89 | -1.59337 | -52.28387 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8cebafee-eb26-389a-936e-b1c5db7f4aef | -2.59493 | -54.21452 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75a4f14b-465a-31dc-9050-3c2872e3d56c | -3.78903 | -46.69555 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b08bba55-6c1c-3744-a472-19ef51615726 | -3.60751 | -51.44056 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc9125cf-78a8-3ff8-9828-abcea6eea826 | -2.61571 | -51.80626 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c16a71b2-13a4-3d86-a811-046145938c42 | -3.23754 | -51.55007 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 543f834e-5fa5-3639-8d79-433210457111 | -2.61805 | -54.19691 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49916003-1ea7-3658-aa4a-d2c05818aa07 | -4.09418 | -54.76323 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cba43a4b-33e1-3e19-9cce-a415ae8b0694 | -3.23319 | -53.63461 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3636bc4f-569b-30e4-8597-452b73c78e48 | -3.15183 | -49.431 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5341c0c-1f0a-3985-9e5b-4b327acfb662 | -2.80319 | -54.14486 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adb60eb3-750c-36ae-bdf2-17583711ce3a | -2.72699 | -51.74401 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14c68c2c-f962-36d6-bee4-e1fc6a066430 | -1.05876 | -52.419 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c1aa5a5-fc9f-33e5-b28e-c68e019da1e7 | -3.61693 | -51.36816 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea78b041-c762-30ac-90b3-f9d059b5aa16 | -1.14593 | -48.3354 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17ad8942-5931-3812-9099-5478bd165d6f | -2.59799 | -53.97829 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0e4fb926-c761-3e43-8010-11cb432b44e8 | -3.43646 | -51.20555 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46710e5d-41d3-3275-9bfc-7611b69c488b | -1.29813 | -51.72902 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 528a312a-5975-3e89-82f5-8688d10e0225 | -3.24417 | -53.62927 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae157380-b4fb-3998-bf73-d635cf9477ae | -2.97571 | -53.88959 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3719fb2-207b-3638-8dee-4fa4608e4a4e | -2.91384 | -51.7154 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cea27569-7e19-3a9e-a66a-489141b80866 | -2.29977 | -51.98498 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 898a2562-f4fd-3f2f-84bb-20a43352152d | -1.16424 | -53.68254 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5296040-2c67-3272-8797-c79c1222de6b | -1.40947 | -52.3059 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 362ac1de-314e-3344-8b54-1f4f2faafd04 | -0.94611 | -51.66092 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e07f8ca-9063-3235-bef5-e79fadf4f2c1 | -3.24481 | -53.93201 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8662d1ae-8006-3a84-8cc1-73ccce3cc45f | -2.60621 | -53.96899 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 909122fc-1e26-3fb1-8153-ade493f56b7f | -3.19347 | -50.82616 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a42545fc-5343-34b9-b9e3-7fc9c84f599c | -2.82604 | -55.58501 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08de7830-9b60-3d0e-8ecb-d369ed2c78ce | -1.65815 | -52.50137 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0f25ee5-f1c7-3b47-bba0-69ddfe387d9a | -2.8423 | -46.81907 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f34309a5-c883-39e8-a9ab-5a616d382fe3 | -3.114 | -53.11158 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fee66fdc-dd07-3958-9b41-3727b4c1b467 | -1.32293 | -51.74759 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12da88a2-e711-3d5c-99b4-06dd21cd4a78 | 1.45726 | -55.91036 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e13f8cf2-b6e1-338f-b591-76297edcfdd2 | -3.10272 | -54.03661 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 735295fc-46cf-3abb-93c5-a6185c1fce17 | -3.25194 | -53.64453 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7395262a-3234-328c-aebe-c09fd75452b2 | -2.8665 | -53.97824 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78c8c98c-af6c-38ab-835f-4233af6342fd | -3.4761 | -49.92827 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README80.md)
