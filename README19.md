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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f80a787-b852-3d3e-927d-1acce4c0c2c1 | -12.56344 | -57.76083 | 2024-12-12 04:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 013dbb49-260a-3678-bab9-3033fb06718c | -13.68907 | -54.76284 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5df0be18-c3d3-3848-bceb-33202578b979 | -18.04186 | -52.99167 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc7d576c-743e-385e-98b1-ceebcf71df62 | -19.36177 | -49.19775 | 2024-12-12 04:18:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f27d1c5a-789d-345f-85b6-ce7fcb29b49e | -18.06502 | -52.96761 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4b4e7d12-570c-3650-a486-d579edaa6297 | -18.06946 | -52.96854 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf2acb4d-ba40-33ce-a2e2-bf20d096b090 | -14.75508 | -52.6599 | 2024-12-12 04:18:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bcd9c380-9c4c-3f19-ac1c-71e1613800de | -12.57005 | -57.76228 | 2024-12-12 04:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b366a8f7-8fca-39d8-9b47-d2a095331fbf | -12.53647 | -57.72449 | 2024-12-12 04:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b2a37d5b-60e0-3d51-9ac3-c39a05380e45 | -12.91967 | -55.05481 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 155bd244-1c00-3a50-bbe5-10e1590ff297 | -17.74448 | -56.32236 | 2024-12-12 04:18:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 50ca5b05-9eef-3ebd-9071-8b4cab66fe48 | -18.0365 | -52.99539 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 476ddf92-d86b-38fe-b80f-8fec8ca18915 | -13.68975 | -54.75936 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afd6a07b-e14b-30cf-89f1-86931406463e | -12.92388 | -55.05136 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc539b30-ac16-3ae3-a07d-3eb0c2beafa1 | -14.75234 | -52.64893 | 2024-12-12 04:18:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 225f53d4-2b8e-36f2-b00f-0db6aa234c2d | -13.6938 | -54.76747 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 51094edb-4f51-3d7a-aaef-6c72a0dfcc70 | -12.92465 | -55.04755 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2297eedb-db94-3c3c-97fb-fb1622cef628 | -13.32402 | -52.41381 | 2024-12-12 04:18:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4100adfd-a1ba-3097-8a45-f07dec95dd31 | -15.09549 | -59.63281 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 553be00a-53c0-36fb-84b7-abfb5fd35402 | -12.92311 | -55.05519 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4862a460-9f66-30de-a95b-5767c454fc1f | -18.06147 | -52.96201 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cc237cbb-61c1-3c48-b255-49b4ecab1c6c | -12.91906 | -55.0464 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c854544-1969-3f8a-a2f4-889ee1c2f8e8 | -15.09387 | -59.63992 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07fd6529-7fd8-34ec-b24b-d75d9f2f4124 | -6.9344 | -43.5401 | 2024-12-12 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 116.8 |
| ecc4fc63-090a-3f25-afbb-e5210504eaae | -5.9185 | -48.0449 | 2024-12-12 04:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 47ec637d-67e1-3537-bef1-080154e9435b | -6.9346 | -43.5168 | 2024-12-12 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 227.7 |
| 3591a3e0-d1d1-3a6e-9e06-c3275eeb3b3c | -3.2503 | -46.8709 | 2024-12-12 04:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 5f05e3ac-ef53-3ea6-80ae-7a91bd4bba80 | -5.9371 | -48.0437 | 2024-12-12 04:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 3d61a882-90de-31df-be6d-e88157b7834b | -5.9183 | -48.0667 | 2024-12-12 04:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| cbd3bc03-622c-3524-beca-fe638c1780ed | -5.9369 | -48.0654 | 2024-12-12 04:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| a00d3c9b-35db-327f-bd6c-91e9b398c398 | -6.9156 | -43.5418 | 2024-12-12 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 40e73c3f-8487-328e-99d3-8e46aac5326d | -3.2502 | -46.8929 | 2024-12-12 04:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 9233c9fb-af07-354e-9af2-0beb92831035 | -14.7461 | -52.6471 | 2024-12-12 04:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 75c00eb1-f59c-3cc0-9510-cb2557a5e272 | -6.9158 | -43.5185 | 2024-12-12 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 190.3 |
| 214d6478-7c97-38cc-b544-04fc998f0453 | -1.8788 | -54.6908 | 2024-12-12 04:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| a6f1af67-fd40-3209-8fc4-d67b705a1bf5 | -12.5682 | -57.7579 | 2024-12-12 04:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| aaa6d98f-2318-38fe-90da-65c14f2dc481 | -23.33959 | -46.77371 | 2024-12-12 04:21:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5c0e48be-7735-33ef-9190-2cdfcdc50e88 | -21.79233 | -55.98671 | 2024-12-12 04:21:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e390950-a183-3a2c-878c-e951e8df9577 | -22.31402 | -49.75657 | 2024-12-12 04:21:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 26823f23-0a51-3ad1-98a6-1e2dd43352e5 | -22.09853 | -48.35422 | 2024-12-12 04:21:00 | NOAA-21 | DOURADO | SÃO PAULO | Brasil | 3514304 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46a995c3-91cd-3013-b1e4-4413969ae9c3 | -22.67682 | -42.855 | 2024-12-12 04:21:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5ae3b646-9c09-3601-8acf-5795e4acc0f3 | -22.80648 | -49.33457 | 2024-12-12 04:21:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01ac6791-d3bc-370c-adc8-7b391d577940 | -21.28773 | -49.18089 | 2024-12-12 04:21:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c7dfebb6-713c-397a-a058-4e1c7526dc80 | -20.73089 | -54.42421 | 2024-12-12 04:21:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e519d0dd-5d65-3524-8262-505df8fce1d4 | -22.78806 | -43.75719 | 2024-12-12 04:21:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fd857a16-aba7-310e-9abe-7ca4094ae11c | -22.80947 | -49.33482 | 2024-12-12 04:21:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8806ed20-6239-319f-8d87-5268d9dc6abd | -22.5416 | -48.81468 | 2024-12-12 04:21:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc9cba59-fe9a-363e-8835-0911da3153c3 | -21.44614 | -46.64755 | 2024-12-12 04:21:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| aa0bd6b0-5489-342c-a1c8-ea1089e0f738 | -29.95135 | -51.61317 | 2024-12-12 04:23:00 | NOAA-21 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 34f97d70-ae13-392a-b2a1-768783f82f81 | -31.03106 | -50.78973 | 2024-12-12 04:23:00 | NOAA-21 | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 1fcfe7c5-56b9-3375-8705-bbe25d1b7c5a | -31.02771 | -50.78898 | 2024-12-12 04:23:00 | NOAA-21 | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 7bb15f58-82a5-3779-b646-422df15a82a1 | -29.87306 | -51.15704 | 2024-12-12 04:23:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 88fcf1da-094e-3d4a-b133-88728ce496dc | -29.94952 | -51.61454 | 2024-12-12 04:23:00 | NOAA-21 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 9a2ad6a5-7984-389d-b44b-f6c0345dbef9 | -29.63862 | -54.17269 | 2024-12-12 04:23:00 | NOAA-21 | SÃO PEDRO DO SUL | RIO GRANDE DO SUL | Brasil | 4319406 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| f4f5fa2a-00e9-30ea-9bea-7ba6c78af08a | -29.78917 | -53.35263 | 2024-12-12 04:23:00 | NOAA-21 | RESTINGA SÊCA | RIO GRANDE DO SUL | Brasil | 4315503 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| fc0ea07f-b733-3431-9913-afec42f07812 | -6.12566 | -42.52195 | 2024-12-12 04:29:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 41.1 |
| 0e05d388-4420-38b5-a4ce-0637ea525d3b | -6.12949 | -42.52776 | 2024-12-12 04:29:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 40.9 |
| c21169ea-1d40-35d1-bd76-8b93cbc32f5c | -6.9158 | -43.5185 | 2024-12-12 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 173.4 |
| d09b4573-f778-3d51-9e4d-e612f94d17e0 | -3.2503 | -46.8709 | 2024-12-12 04:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 92b276cc-7f0f-33d7-8c15-f2eaca52b7e1 | -12.5682 | -57.7579 | 2024-12-12 04:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| ce61da28-7453-306b-861c-4d5a932c7457 | -14.7461 | -52.6471 | 2024-12-12 04:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9adecd09-9740-3281-9613-d5d8712c7843 | -3.2502 | -46.8929 | 2024-12-12 04:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 32d9d25c-432c-3f3a-9756-4ed75553a5e3 | -6.9346 | -43.5168 | 2024-12-12 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 205.0 |
| 219745b2-3672-3989-b649-935582ea4083 | -6.9156 | -43.5418 | 2024-12-12 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| d172d4bc-482c-3ecb-acff-cd94c3d2ca76 | -6.9344 | -43.5401 | 2024-12-12 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| fe2f086b-8ed9-32ce-a77a-760238eb9e61 | -14.7655 | -52.6446 | 2024-12-12 04:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 8526b271-1867-324b-ba0f-02c8c8c159d4 | -9.69436 | -36.17231 | 2024-12-12 04:31:00 | AQUA_M-M | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 86c9274a-dcc7-3247-ad7f-6055e455511e | -9.79056 | -36.21648 | 2024-12-12 04:31:00 | AQUA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 13a596c9-5930-3426-bf66-f38c723fecae | -5.70949 | -46.51008 | 2024-12-12 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca2fa83b-e82c-339f-acae-07c31018b670 | -6.09803 | -44.04599 | 2024-12-12 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 531fbd37-73f1-36c7-83fb-7548dfd37cb1 | -2.47231 | -47.08846 | 2024-12-12 04:38:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad46cfb6-3fdf-3c15-8b4a-7349a3c93c4c | -4.18966 | -42.4342 | 2024-12-12 04:38:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b016f7d6-bd73-3d0f-b808-ab33d3046908 | -6.12721 | -42.55189 | 2024-12-12 04:38:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 56a70390-b48c-3030-a570-432b897f198b | -4.83075 | -44.21649 | 2024-12-12 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 332172af-6b2f-30ce-975a-47a3098a1de4 | -6.91819 | -43.5116 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f6c88249-ca1f-368d-9b52-e9d706d4004a | -3.41652 | -44.45634 | 2024-12-12 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4bbb7c05-5d9a-32f5-8d26-e1fea6e5c44d | -2.95638 | -47.89625 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a65f3f0-e6b3-32d3-9313-bbbba62c9462 | -4.10251 | -46.60902 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37bc8efc-951d-3f6e-9766-50856c8575e3 | -6.91701 | -43.51987 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3fd4222b-ba72-3add-86f0-739b9e8f43cd | -3.98054 | -46.90598 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70af314b-f576-3f6f-b5ee-b5f093d5adf4 | -7.89051 | -42.44517 | 2024-12-12 04:38:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e93cecb-47b3-3932-bd3a-6a5ff2ae5b4e | -5.29103 | -44.91452 | 2024-12-12 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 756b2c9c-b0d4-37a7-a363-08027f3ba2cc | -3.98344 | -46.88736 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90eb0be1-ec5c-377b-bf6b-341865fcdda2 | -3.83348 | -41.57347 | 2024-12-12 04:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 786f97da-d2a4-3405-9e64-08dd328da055 | -3.00593 | -48.05077 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06acec06-32db-3500-9123-c149ab8920b9 | -6.92135 | -43.52052 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 6e8197bf-a620-3ccd-93a2-58e72de6f976 | -3.15043 | -48.53085 | 2024-12-12 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43737319-d590-38d2-9c75-f10fc74bd333 | -4.60643 | -46.49545 | 2024-12-12 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71b2cbee-921c-39be-b2ad-04ef229d18f7 | -6.9407 | -43.54017 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f1a42b6-770a-3bdf-97a3-dbf453882284 | -5.35093 | -44.20026 | 2024-12-12 04:38:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 003efc27-8484-379e-a4bd-931fec82325c | -4.0286 | -46.81242 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11ea2b37-20a6-313e-9468-d19957b18c27 | -4.62828 | -46.46974 | 2024-12-12 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eca0cebb-fb46-3bd6-adfa-123b47c9e16f | -6.05961 | -44.04847 | 2024-12-12 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7b37d78f-d933-360c-b62d-2823cac16555 | -4.09653 | -46.67098 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7871fb80-ea62-39f8-b492-e7690f88adf9 | -3.00532 | -48.03285 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2028c731-6372-3492-86e4-3459dbc887eb | -4.60705 | -46.49146 | 2024-12-12 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b9e75e7-ab06-3710-b434-43e7d63d39b8 | -1.63712 | -55.10447 | 2024-12-12 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fe908c0-efce-32a9-8dd5-dab6ede9c9ba | -2.78758 | -47.63677 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 572e38be-89bd-3a3a-bbe5-86f9f8399104 | -6.92868 | -43.50033 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c4dfedd9-7b35-356c-aef9-2a65b5c6a6d7 | -4.56671 | -48.47527 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README20.md)
