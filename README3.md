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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d91b0b3a-4698-358d-8482-16e5e872bbce | -11.79353 | -47.37666 | 2025-05-16 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0aa2c4f-8f2a-35b2-a174-5fab65bd2611 | -11.79743 | -47.37733 | 2025-05-16 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 60bdbee6-5ea6-39bf-867c-24e88986e531 | -11.62984 | -48.47565 | 2025-05-16 04:08:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e9dd9b1-da57-3d28-b60d-c763f554330b | -10.00851 | -47.84261 | 2025-05-16 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e964d94-9657-31aa-a12f-93b7b7202133 | -6.65798 | -43.19225 | 2025-05-16 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4e45b04a-d1af-3002-8543-1fae65d9fcdd | -10.35353 | -47.98001 | 2025-05-16 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 691e3b00-132d-36a9-958d-1baf94bc6a73 | -11.79267 | -47.38169 | 2025-05-16 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ef7df69-5599-3200-a5b3-7e9747ae89af | -9.45242 | -40.39814 | 2025-05-16 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0c5ed9c6-658a-37cb-90a2-d17a1f25400f | -11.80047 | -47.38303 | 2025-05-16 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a6065f1d-44ae-3466-8d63-047c60a19a89 | -10.02731 | -48.70107 | 2025-05-16 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d77005ca-63c2-3ba6-ba5b-932e2d3d70a8 | -6.71905 | -47.58951 | 2025-05-16 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87ce0168-7849-3405-965e-f233b066cdc2 | -7.0801 | -44.39269 | 2025-05-16 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c5716e0-2c96-3fcd-83b9-3a1042f200ba | -12.31892 | -44.50588 | 2025-05-16 04:08:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9503f93-4d81-3a72-a744-9c559fc8a2e0 | -8.83374 | -44.21207 | 2025-05-16 04:08:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05c772ca-bb17-3ceb-a1fc-f1bea27e7953 | -8.90127 | -44.78271 | 2025-05-16 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6bd38d7-4796-391d-8b8e-4e4b6e397be2 | -11.63517 | -48.02679 | 2025-05-16 04:08:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd281ead-5b1e-35cd-a348-ef7bfa1c67b8 | -9.45014 | -40.39023 | 2025-05-16 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| efdb6571-9fbb-38f6-87ca-97ff2788a5f3 | -9.45185 | -40.40184 | 2025-05-16 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3bf24d2d-243c-3e2f-bdde-7c805a8be3f1 | -6.98241 | -42.78387 | 2025-05-16 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a2a58dd0-39c4-3261-a68e-eb28cdcfc346 | -12.31831 | -44.50958 | 2025-05-16 04:08:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 250dae2b-11d3-3a19-aa74-dcd8635c5cf8 | -9.36775 | -48.40123 | 2025-05-16 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| feca6457-6abb-3989-8b31-91c2cdbae24f | -10.06511 | -48.08375 | 2025-05-16 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b63512c-af56-3a83-a2aa-d22629450785 | -13.40962 | -44.14595 | 2025-05-16 04:08:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee4c2d6e-f443-37c5-94f7-3e698af2b920 | -9.4237 | -49.33712 | 2025-05-16 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fb67377-a414-3dd3-abe9-b86cff740096 | -11.78617 | -47.34953 | 2025-05-16 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c7f5fa05-8d91-3365-afdd-4ec3e05ae5eb | -11.16773 | -48.67706 | 2025-05-16 04:08:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a96d8a1f-f2bd-37d8-be1d-9faa75bf8f6e | -10.35903 | -47.97292 | 2025-05-16 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b98e877-7e82-3b28-9ba0-1def7c31a27a | -7.54858 | -45.8685 | 2025-05-16 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ebee1a8-3114-3917-844f-6b9b0d5e425f | -11.56556 | -47.87517 | 2025-05-16 04:08:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6506abf3-cbc1-392d-873c-3b3810c5603a | -10.6348 | -48.0927 | 2025-05-16 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8681536-2b01-3932-aead-6a393d0c10cc | -10.46592 | -54.98088 | 2025-05-16 04:08:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9f3de57-1be3-34b2-b639-03658ac4dbfa | -11.07309 | -47.29705 | 2025-05-16 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6e7db3f-be5d-3344-bf22-9be89a4786d0 | -6.35016 | -44.64176 | 2025-05-16 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e50778a-2eff-3c57-bf17-362fdfb07cc0 | -7.0456 | -37.23794 | 2025-05-16 04:08:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2e7f698d-206c-3695-b6c7-5966498e2538 | -11.41955 | -54.33119 | 2025-05-16 04:08:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aecfb102-d643-3b0f-a319-8ac4c89786a5 | -10.24312 | -49.1697 | 2025-05-16 04:08:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed049c0e-1203-3266-ac5a-3c8c406868f9 | -10.51493 | -42.39496 | 2025-05-16 04:08:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6977f199-f913-3529-aa5f-13cd150ca641 | -11.16582 | -48.67994 | 2025-05-16 04:08:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e880f755-404e-39d2-a407-4aa5b36f395d | -7.0737 | -44.38753 | 2025-05-16 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caecfd2b-47a3-3972-82ec-950794a138a8 | -11.62946 | -48.47225 | 2025-05-16 04:08:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5e61eca-b9dc-3507-9f2c-9851b0ac5589 | -10.36319 | -47.97355 | 2025-05-16 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c6e54c5-d7e0-39c5-87c0-4869bc86d66f | -10.3542 | -47.97616 | 2025-05-16 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e732af4-9df1-377b-9b99-16e467fc812c | -8.43096 | -46.63945 | 2025-05-16 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f621fa3c-a2a0-3398-a9ba-8e4214d05488 | -11.58248 | -47.61491 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c8d0ce8-ee0c-3dc8-8335-4aaf664f1762 | -12.16317 | -48.80426 | 2025-05-16 04:08:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27d9acae-ed77-367c-a3d3-ca8113db3678 | -11.30474 | -54.01471 | 2025-05-16 04:08:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa16aa99-3368-322a-bbfa-3342b2175357 | -11.58186 | -47.61841 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 546791ed-4222-3914-b822-edf7db0c76f7 | -7.54781 | -45.87313 | 2025-05-16 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6331c7b5-176d-339b-a5e4-1a77b38eed93 | -12.34622 | -49.95832 | 2025-05-16 04:08:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c2b4070-cea7-3e51-92f6-82fa8dd45159 | -11.42569 | -54.33243 | 2025-05-16 04:08:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 348f9e2a-cf7b-33a9-8e1c-a4889cf4b184 | -11.61207 | -48.01521 | 2025-05-16 04:08:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12a4268d-6d3a-3e14-bfee-f9babac0181a | -11.58291 | -47.87096 | 2025-05-16 04:08:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d66cdf71-e109-343d-9b6a-e31bcdb38af8 | -9.36846 | -48.39706 | 2025-05-16 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b7a06da-bc6f-3b74-b696-ceb6f4d75b1c | -7.07306 | -44.39153 | 2025-05-16 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c3994f3-84bc-3d07-a5ce-034e9aeb8b8f | -12.33944 | -50.33046 | 2025-05-16 04:08:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4da3b4e5-435a-305d-800c-0aa8aa8dce9c | -11.06905 | -47.41217 | 2025-05-16 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1046203f-d7f8-353b-9704-d82f5bd6e45a | -10.50813 | -46.18733 | 2025-05-16 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a2a7c82-252f-3058-ab48-247df55b6787 | -7.28027 | -43.28005 | 2025-05-16 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9afbecaa-4678-38e5-b537-574373e33a59 | -10.63896 | -48.09337 | 2025-05-16 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6177129-1d0f-358e-8f84-1f2651a6ebff | -11.58644 | -47.61566 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6144ca57-9fa5-360c-9ade-45fa3e0b5b00 | -10.96356 | -49.42212 | 2025-05-16 04:08:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94eb8849-210e-3905-917d-60152a74e3f0 | -7.60448 | -43.33908 | 2025-05-16 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d90878ef-4654-3cf3-bbbb-99892cda939e | -11.55561 | -47.61274 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1cbea0f-4a05-3276-94b4-fa739ea873d1 | -9.30398 | -44.8262 | 2025-05-16 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| caca7139-a909-376e-8e1a-642f2eef4309 | -11.58325 | -47.61055 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ec7f618-d514-3e02-8ba8-6580ceed0240 | -12.34708 | -49.95348 | 2025-05-16 04:08:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7a99c40-e9d4-3d38-a4b5-6e68d9b1251c | -7.32101 | -43.24184 | 2025-05-16 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73233997-b240-38f3-bf85-ffe48851107b | -12.37128 | -47.32309 | 2025-05-16 04:08:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57a8f128-3cc5-35cb-8667-c846f3d45638 | -7.54703 | -45.87782 | 2025-05-16 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8d45ee4d-ecbb-34a5-b9fb-5309ddc6c4b1 | -11.58521 | -47.62262 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08b3e1ca-6e28-35be-8fa1-dc44e8114a28 | -10.00438 | -47.84191 | 2025-05-16 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 842e4144-2a08-30a8-978b-c743f48cfc58 | -8.42788 | -46.63379 | 2025-05-16 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 974e423c-15a1-3525-9c5d-41fe11fa8637 | -11.30565 | -54.01008 | 2025-05-16 04:08:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15b8e56b-9b89-3c82-9207-6905489d5b99 | -11.78531 | -47.35452 | 2025-05-16 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52a02af8-8d23-3a2b-a7e1-37ab358dd040 | -10.34783 | -47.67599 | 2025-05-16 04:08:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 045344c0-6e00-34dd-86e5-1ad1ad2d294b | -11.57929 | -47.60982 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 904c029a-60e3-33a9-a1cc-9c56bfae6ad7 | -7.7453 | -46.3278 | 2025-05-16 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 869b6bb9-31ce-34c4-aa92-8f604edc4e0a | -11.79005 | -47.35023 | 2025-05-16 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 029cd871-4a66-3f87-8e89-1ff78b71e79a | -9.44958 | -40.39392 | 2025-05-16 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| a6446d1c-4259-3d5a-8138-2c174891cbf0 | -11.16657 | -48.67582 | 2025-05-16 04:08:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5e4dc352-ab56-35b4-9834-c6ae364cf583 | -7.425 | -43.46724 | 2025-05-16 04:08:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa2ce879-d244-35a5-a6b0-8aaf768174a3 | -11.57852 | -47.61418 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 71990044-1ef8-39e1-9a0a-d36d46090e6c | -9.44902 | -40.39762 | 2025-05-16 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b588dfbd-6afb-32f4-9228-f5cd4538ce32 | -11.58582 | -47.61917 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 61c05c82-e2ef-301f-aeab-08faf5de073c | -10.50696 | -46.18595 | 2025-05-16 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b917be36-5694-358b-8de1-07a92258ddd6 | -7.28365 | -43.28058 | 2025-05-16 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18fca438-d589-3e87-86a1-e9b70bd9753b | -9.37387 | -48.40107 | 2025-05-16 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c91a81fc-9f58-3834-86e2-bc92e163a5ba | -12.16244 | -48.80831 | 2025-05-16 04:08:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a8ac65d6-aec5-37b8-b17f-45edd2260ead | -7.07658 | -44.39211 | 2025-05-16 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7df1de8a-28ec-3cb9-b8a5-e948286d2533 | -10.34524 | -47.97863 | 2025-05-16 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1a98751-2324-3f5c-9795-6285b603a53c | -11.55622 | -47.60918 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9c331da-04f8-3b15-b29f-0376310f9b42 | -7.42441 | -43.4709 | 2025-05-16 04:08:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 019a6937-8b19-32b5-9ddc-61fd633311d9 | -6.71836 | -47.59354 | 2025-05-16 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 746c76b1-8cb1-3760-a429-475ff19b3173 | -12.37264 | -47.32584 | 2025-05-16 04:08:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73e00158-1d8a-3282-9947-b4051d8b8b61 | -10.00591 | -47.84262 | 2025-05-16 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b3142d4-c872-34ea-a6da-f9e9cd0f69d2 | -11.51525 | -48.57838 | 2025-05-16 04:08:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c53b21ef-96a9-3b73-9be4-301f3199b7f8 | -12.34595 | -49.96095 | 2025-05-16 04:08:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 422d13c5-31c0-359b-8125-8149bb29da82 | -11.03024 | -48.80222 | 2025-05-16 04:08:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af3011cc-fa04-3f0c-b82e-6c609f77282a | -7.53857 | -43.39506 | 2025-05-16 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0e1cf92-9e44-3c88-8c6c-90e4ab8e1d58 | -11.78142 | -47.3538 | 2025-05-16 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README4.md)
