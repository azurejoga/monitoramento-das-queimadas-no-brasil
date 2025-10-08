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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af643b36-a21d-3b1f-be66-e5f3612142cd | -13.22002 | -51.65002 | 2025-10-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e67d24b-9431-3ad1-8360-19ebfc265d3f | -12.88258 | -54.74024 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d6b6b682-4982-3425-ae65-6b65c7c37b5e | -17.16666 | -56.6042 | 2025-10-08 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e2c57cc2-9409-38aa-884e-1f8d39bf61e6 | -12.8439 | -62.16331 | 2025-10-08 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8870d89f-34cc-3bbd-a7cc-01341555301d | -13.21366 | -51.6492 | 2025-10-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8e40b5e-c8e1-3fd3-a48e-0db36a5a18cc | -17.93452 | -57.50961 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 752a671d-9d29-3169-8bc9-0f6a1b9c01c7 | -17.93682 | -57.52286 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 72b190ea-45d0-3380-8819-265a2fa4aa3a | -18.02309 | -51.15129 | 2025-10-08 05:31:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8717b46f-b98c-3fc1-85c3-a1498fc71660 | -17.85236 | -57.64922 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 175ebde6-7120-3b00-bee1-392d4d78ec10 | -14.23972 | -60.16816 | 2025-10-08 05:31:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0c919ac-11ab-3ea7-8bd1-92eefc9e9348 | -15.22126 | -56.75276 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 89e2c984-d9f2-32e9-b063-9550ad4e2f62 | -13.45853 | -60.97876 | 2025-10-08 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a93d6c61-e027-3949-94a6-8b215a82db1a | -12.64412 | -50.55973 | 2025-10-08 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad2d7c5e-1e3a-3df0-b220-4eeb9fcd43c3 | -17.84365 | -57.64435 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5a28c2b2-810b-349e-bbf6-b6db1b48f955 | -12.39833 | -61.75158 | 2025-10-08 05:31:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 588d76f1-d513-30b3-bc77-eac9bdde5f1a | -21.33593 | -55.63214 | 2025-10-08 05:33:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f73e3a8-3409-3867-8400-835abe161522 | -21.33719 | -55.63058 | 2025-10-08 05:33:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47b01d5d-6b93-3981-bb31-24b0665e6e23 | -21.33628 | -55.62864 | 2025-10-08 05:33:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c330d9f1-c3ab-3b82-8b5c-0aafe1a96cfa | -6.69398 | -58.80919 | 2025-10-08 05:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c868e9de-846d-3b72-a950-832f827e7d95 | -6.69699 | -58.81612 | 2025-10-08 05:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cbb1f72-caa5-3180-88d5-bb1153f60168 | -6.62733 | -62.88213 | 2025-10-08 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f0118e0-a1d9-36b2-a682-1bd72f80b552 | -6.6231 | -62.88149 | 2025-10-08 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cde1f50-fc17-363c-bd38-52b6cc1b5a97 | -6.69345 | -58.81296 | 2025-10-08 05:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1611c35-0b1b-329f-9cd8-bbfec0cc0101 | -6.6919 | -58.81152 | 2025-10-08 05:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ac69a10-6884-356f-9970-7a6f165717c8 | -8.1959 | -62.87191 | 2025-10-08 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a109a763-8d01-3cff-99eb-3b4ec31d26de | -6.68732 | -58.81589 | 2025-10-08 05:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c5dc2bc-b66c-3616-b858-e35e0360c588 | -6.69139 | -58.81529 | 2025-10-08 05:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88311651-21a5-3fea-8548-4b1a56f62015 | -7.47725 | -63.61907 | 2025-10-08 05:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5327b8cc-e21d-3e69-bb9d-cc0e239e972d | -6.68785 | -58.81214 | 2025-10-08 05:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 336b73d3-7683-30c5-82bc-c476ddef56a6 | -6.69291 | -58.81673 | 2025-10-08 05:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7e37c14-06c4-31a6-b27a-74a68cfa1e16 | -6.6975 | -58.81234 | 2025-10-08 05:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba201065-b13a-3e2c-af5c-21ff677afdee | -6.69905 | -58.81373 | 2025-10-08 05:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86ee30d8-cf80-34ca-bbdd-54275ef9c926 | -15.98171 | -59.53774 | 2025-10-08 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a64a5f58-52d2-3737-b8e6-02ae1539db0d | -10.97533 | -59.02507 | 2025-10-08 05:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e85fba1e-eeab-3954-803f-006fd92d8dd3 | -12.40231 | -63.8817 | 2025-10-08 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfab2167-a308-3085-b681-9fd301a483a9 | -12.40343 | -63.88874 | 2025-10-08 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec0b2ba0-29f5-339f-857a-2ec258da5efb | -12.39685 | -63.88937 | 2025-10-08 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a853532e-d901-3c43-8490-c286e34e52af | -14.85068 | -59.65863 | 2025-10-08 05:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c02e316e-5dad-3716-b702-6a05eb990973 | -15.12582 | -59.03067 | 2025-10-08 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1257cada-d1c7-3e7f-9590-808b4b3ba7ee | -11.33259 | -56.20433 | 2025-10-08 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d5b01c1-95d9-3c4e-bc2b-4bab5702ffe5 | -12.40173 | -63.88584 | 2025-10-08 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8252cce8-9bda-3db7-8882-0ea57a8ccda4 | -12.39742 | -63.88524 | 2025-10-08 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2b6cf86-3ff3-3fdf-b03d-99de5d33663f | -11.3396 | -56.20502 | 2025-10-08 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 185ba2a6-3bc3-37be-9ce3-bc2855d1eb42 | -15.993 | -59.54636 | 2025-10-08 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bfeacd1-029b-3168-8ce2-cbb43c461e53 | -13.46282 | -60.97971 | 2025-10-08 05:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9a39c6c-bcc0-3398-b349-070d26c10cad | -12.39311 | -63.88467 | 2025-10-08 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20c7aa00-92a4-301f-9f8a-55b092f0e2c4 | -15.98132 | -59.54132 | 2025-10-08 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8a97220-01c4-3bd9-bf07-52279f21db03 | -12.39799 | -63.88111 | 2025-10-08 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25e0f719-8d66-33ff-b5f6-e312eba17002 | -14.23984 | -60.17002 | 2025-10-08 05:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a6311e6-2556-3654-b5e4-e76210567528 | -14.2403 | -60.1661 | 2025-10-08 05:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb24a764-8cad-32d3-8357-04bac3fe65b1 | -11.34161 | -56.20627 | 2025-10-08 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed630acf-6f03-3c9b-8632-6ce4dd0d5463 | -15.11968 | -59.02972 | 2025-10-08 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c9e2f32-69b6-3354-8acf-f502de0bd581 | -15.99942 | -59.54343 | 2025-10-08 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91529620-4f49-342d-a388-af52a0a3bc38 | -14.85666 | -59.65873 | 2025-10-08 05:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d20bebd9-858f-391e-b4f9-0cfb83ec0ea3 | -12.40116 | -63.88998 | 2025-10-08 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ecbc846-7fcb-3da0-b5a2-f5224482cb3b | -11.33462 | -56.20547 | 2025-10-08 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de4484c8-b9c4-3ab7-a237-bef2b5ac2e7d | -10.97482 | -59.02914 | 2025-10-08 05:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90852cbd-65a1-3123-82b7-bd32a4f9bc37 | -17.8644 | -57.65017 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| fceddf5a-9eae-3faf-8df8-fb2ec747aca9 | -17.94437 | -57.53319 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b3a56c56-dd9c-3b19-a4f8-85daffe319e1 | -17.93222 | -57.51195 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8fe4afc0-26a7-35c4-befd-10156f04ab4e | -17.86488 | -57.64453 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| acc43448-daa9-3bf8-ab07-c82adadd3da8 | -17.86543 | -57.64571 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8b8387d3-d913-3c3a-a863-984ed38ec610 | -17.93723 | -57.53465 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a7faad4d-064c-3086-be5d-946169c06048 | -17.82347 | -57.64818 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6e43a361-1d64-34a8-8437-efe509408de3 | -17.97473 | -57.50728 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 27bd196b-cd45-3809-a9e3-5def1a720266 | -18.04736 | -57.55098 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c0c371d2-e62b-3c06-9523-72403ed01cde | -18.05498 | -57.54395 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5cd98a6b-212a-39c5-871e-6bd36d6e4a3f | -17.27149 | -58.12302 | 2025-10-08 06:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 08a03ad7-e244-3741-9fb6-bae2ea46dbe6 | -17.83109 | -57.64077 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 21d43dae-d366-3f21-b799-747292e0f123 | -17.85102 | -57.6512 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dd2fb239-978f-37ea-a179-f4d1c5fe6bc7 | -17.27873 | -58.11775 | 2025-10-08 06:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e0c715b0-fb17-3495-b19c-37c85ac5457a | -17.84452 | -57.64616 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0c6dcfce-f2f6-3296-8416-462db41ed643 | -17.30393 | -58.06599 | 2025-10-08 06:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 25335dd7-a4fb-300e-8121-21366478ba15 | -18.05568 | -57.53606 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7ce13b83-51b4-391b-8a27-2e0fdabedd3f | -17.30069 | -58.0652 | 2025-10-08 06:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 412a7438-dd05-33bc-9c8b-501e231cb353 | -17.85795 | -57.64415 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2bc075ea-0ba3-3dc8-baeb-a4e8efb854b8 | -17.86531 | -57.63952 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f5d8b134-6371-3b09-a394-d2748ebd09ed | -17.97414 | -57.51385 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4847dcbf-2e37-364a-921b-2d3b2275f8b4 | -17.93786 | -57.5276 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4eac43a1-2544-3192-95a0-3da784857813 | -17.85051 | -57.64994 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bbd2a869-203d-385b-95a5-42f859cca1ed | -17.82424 | -57.63956 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f283678c-e809-3a1d-9348-a2f809251a83 | -17.30335 | -58.07199 | 2025-10-08 06:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 323fa56e-4425-3b8d-93ed-fb55639106e7 | -17.87224 | -57.6398 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2a3d9cf5-3f82-3466-8c02-bdd1cbcf10fc | -17.30015 | -58.07122 | 2025-10-08 06:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| aa4e6da0-8b9c-372b-936e-976d803b7520 | -17.97356 | -57.51212 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 27c923bf-30be-3df4-ad45-edde143f8ab8 | -17.8659 | -57.64061 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 99d68d87-741d-317c-9a49-1541710a2b92 | -17.93134 | -57.52204 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 956ce309-a487-3e77-b4e9-ace08c95e66e | -17.97411 | -57.50554 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d7fc00b6-c4a8-3c48-ba08-7d324aa31342 | -17.94355 | -57.54245 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 39d613e8-9f4b-3b3f-bd54-4eed304f966e | -17.8585 | -57.64542 | 2025-10-08 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ed466ef2-a35d-3826-ac9d-fbd74909556e | -17.26483 | -58.12231 | 2025-10-08 06:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6e016eca-6860-38a6-bcea-4b5708a42736 | -4.47603 | -49.71148 | 2025-10-08 06:29:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8917aa4d-5b30-3e17-abab-0bb04651e711 | -5.14917 | -46.08291 | 2025-10-08 06:29:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 222.8 |
| fc860e0d-4cfd-3e24-a101-a88630484366 | -4.03499 | -45.35087 | 2025-10-08 06:29:00 | AQUA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 2f176944-774e-3e05-a15d-1f69d2feced8 | -9.17806 | -47.78584 | 2025-10-08 06:29:00 | AQUA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| aac375e8-934f-332a-a448-99fd797ec5f2 | -3.10413 | -47.79848 | 2025-10-08 06:29:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 843c5097-0147-31d8-bb63-378d9c2afe01 | -5.14548 | -46.10971 | 2025-10-08 06:29:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 40.2 |
| b5fdffba-9e77-3a59-aa69-c8cea4b6d8fe | -10.22919 | -52.69322 | 2025-10-08 06:29:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7fe071f3-75e9-3080-8c7c-6bd8a237da8a | -4.03682 | -45.32549 | 2025-10-08 06:29:00 | AQUA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| f4b0f792-105d-367b-b103-e92101e6b3c5 | -4.03935 | -45.32085 | 2025-10-08 06:29:00 | AQUA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |


[Clique aqui para ver as próximas entradas](README96.md)
