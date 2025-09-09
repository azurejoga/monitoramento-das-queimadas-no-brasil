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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92b7fe9c-5075-388c-8b6e-1882b5a23d35 | -15.2769 | -53.80895 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2360a29e-a9d2-333f-b15b-7a745b05ede4 | -13.04686 | -48.02924 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4781a7f0-e00e-3144-93c7-8f51fd058e96 | -7.82299 | -63.57666 | 2025-09-09 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27f474f6-5b13-3bad-8edc-15af9f8c58da | -13.96109 | -54.01549 | 2025-09-09 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9dacea0e-6ee4-38a5-8b81-66c15bbd9651 | -15.2712 | -52.35265 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2cb527a-3809-3c19-9998-da36deacdba9 | -12.86791 | -62.10729 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44832bd0-854f-3151-bf88-bdb8116ce1a3 | -15.26106 | -53.81042 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce3f24ef-76c9-3c02-9755-c8bda30f5b63 | -12.88906 | -47.98048 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4e4d766c-e337-3159-a4c0-51f1bd76bcfe | -12.96409 | -54.76188 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecd41f68-bf88-3552-b3a0-d47f209c9ca6 | -12.81053 | -56.51375 | 2025-09-09 05:23:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a860ea0b-2d3d-30e8-a8de-fcdfd6a37e45 | -13.01807 | -48.02704 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1c3cb4eb-52b9-3e62-9053-8707d82c693b | -15.25699 | -53.80046 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e97ca84-fe1a-3ec7-a0a6-aa7cd45bfed7 | -13.93405 | -48.23923 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 28e7ba47-f835-3446-9b44-95f1af297370 | -5.42443 | -51.53889 | 2025-09-09 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f30d0086-5321-3e7c-983d-dad640b4977a | -7.40384 | -61.62969 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d23c79a0-8ac5-3953-88d5-85d118695221 | -13.04372 | -48.02846 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0f37b6f9-1f0f-3031-810b-272b3c67ba8e | -14.44419 | -53.23808 | 2025-09-09 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddae0e45-721b-3196-a966-7764f8a8ebda | -8.06262 | -48.63522 | 2025-09-09 05:23:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4c1107ec-0580-34b7-937c-00de84d095ec | -15.82558 | -52.25565 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bf35b04-e596-3b93-8393-1d491e3af2a6 | -8.08807 | -54.75028 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84482783-5748-35e9-a807-41e8516ed000 | -15.77754 | -53.53677 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b47a8fd0-58ee-3276-9014-7e70adb5008e | -13.29748 | -51.73184 | 2025-09-09 05:23:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04e08540-6f5b-34ce-a55f-611e54dd3c88 | -12.88283 | -62.09888 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 018398b7-6066-3026-b8ce-3f64f71a075b | -14.72238 | -60.24232 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddbc8592-8208-3b87-89bb-52ffade85eb2 | -13.93615 | -48.2491 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 941040be-3107-3ccf-af64-a6026997b67a | -15.24407 | -53.77654 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0698a9c0-6537-3c06-a975-a64c44f4e99f | -12.88394 | -62.09182 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0264ae5-4fbf-30bd-b8af-3d67d3d2812f | -7.12136 | -60.73198 | 2025-09-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f33adc6d-9bf9-35d6-a942-cd9372828c28 | -15.82229 | -52.27441 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0345b4c1-2c52-358f-91fb-926566398afa | -15.82426 | -52.25688 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2739ab56-eaa7-31d7-bf62-5d7496c3bcb9 | -15.87368 | -52.34754 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cea6909-5e16-3b2c-8b98-2d9f4af907d2 | -5.01255 | -48.47281 | 2025-09-09 05:23:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3fb7a66c-cb3a-3ee4-ab27-20fbc4e7966c | -12.9532 | -54.7536 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f8b0429-d18d-385d-863a-d4060cbf65a1 | -13.94346 | -48.24832 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e06e0f1a-1a51-366e-bc7f-41aa347836d7 | -14.52689 | -53.96519 | 2025-09-09 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3382a85-da3a-359f-9434-655139c0ba4e | -15.78237 | -53.54122 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f600c5a3-18b3-3a8d-8faf-4604e51e7b75 | -8.23154 | -49.54074 | 2025-09-09 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aec5d5ff-47fa-3a9d-8abc-b4012a0059bd | -15.2721 | -53.80531 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 691f8b4c-e876-3625-b0b1-b0f47e16b5f3 | -16.07512 | -50.49089 | 2025-09-09 05:23:00 | NOAA-20 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eeed8f77-d503-3a46-8381-8a3600cfd0cc | -14.52726 | -53.9622 | 2025-09-09 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18cd78f8-b03b-38e6-99fc-5c542ea21062 | -14.9164 | -55.84085 | 2025-09-09 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aeb49db9-c598-38c0-8747-0cc8f8f1334f | -8.0355 | -48.63953 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0c2e8c40-5112-3a1a-b320-92d72d74e0bc | -6.40401 | -58.21087 | 2025-09-09 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 779f491a-d3b4-3f1e-bc87-515ada11969b | -9.27905 | -56.89398 | 2025-09-09 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ac9e836-8810-340e-b2d9-8bde147dad8c | -12.87896 | -62.10186 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fc3db4b-440b-321b-b959-35264a4e5c02 | -6.54802 | -54.9895 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c0625ad-0813-3f14-86f1-e2b2475c7fd3 | -7.3355 | -49.56553 | 2025-09-09 05:23:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a36cb80-5077-31f5-89bf-1dc4c12a9172 | -14.54165 | -48.76105 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c4ef51a1-521a-30e2-8999-6ceb20fe1510 | -8.03477 | -48.64523 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6359bdb6-cc3a-3ebb-b09c-6eea9bb6df04 | -7.83674 | -61.62029 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d82ec4a-af98-3bea-b663-226f940be2ad | -14.71432 | -60.24904 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8536bb54-3061-3a7d-886d-71d14e83beda | -14.5431 | -48.76138 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7eaf556-5354-36d9-babd-b29d46a783e4 | -12.89941 | -62.08012 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 185b5e80-70be-3291-b80e-3f4649df226e | -7.40107 | -61.62564 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e5ed35a-7f52-367d-bfde-d954b003e541 | -8.09122 | -54.75941 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd7a8084-79bb-3831-a9a1-a8a2afe807f0 | -14.52116 | -53.97022 | 2025-09-09 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 156d9224-3d45-3068-b160-c937da39d4f3 | -12.9559 | -54.76917 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa7ebcf5-3c31-381c-99ee-94506840e45c | -12.41538 | -63.89502 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b22546f6-55e3-34d8-b012-c7c932590d51 | -13.29173 | -51.7311 | 2025-09-09 05:23:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| caac17af-11f5-3bae-9ead-9e247f4126f3 | -15.27837 | -53.79647 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecee268e-fe5d-3d2c-9842-309e48a0fc44 | -15.25038 | -53.81248 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9920ce9b-fae3-3cc5-8f1f-fb6ab8ca31fe | -5.00006 | -56.04969 | 2025-09-09 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 334f7c4e-f7ca-3902-b57b-759af78cd849 | -7.4858 | -54.95036 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b2dd717-1428-32f7-94a4-97ad904cdbd4 | -12.90597 | -48.00108 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1351dcd6-c6f7-34ab-9b9c-46b7d4e73011 | -5.50022 | -60.13543 | 2025-09-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 703b9ec4-5508-3b32-93eb-5f9c2525267a | -12.8701 | -62.11489 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef85b47c-b28c-3b4d-858e-0c1030637305 | -15.76621 | -53.54211 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbcebe7a-5091-37bb-aacf-7776a3fdff95 | -15.78371 | -53.57357 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6c2d87b-21fd-3b12-a593-6d63a39a92b1 | -10.33731 | -47.73696 | 2025-09-09 05:23:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 780ac321-0e56-3e05-a2be-1e7ce5c4925d | -12.43715 | -63.93382 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d17a89e-b810-3533-8281-712148bdbb89 | -15.26142 | -53.80729 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4984e05c-435a-329d-932d-ff1f4e22833d | -15.50884 | -52.7674 | 2025-09-09 05:23:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d9611da-738e-3ad2-b204-2eef89f94209 | -15.27357 | -53.79282 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a6af18b-35a9-3bee-bec7-63176f478f29 | -15.53117 | -48.40109 | 2025-09-09 05:23:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 422946d1-4830-31b8-bd61-126118b64a34 | -14.53465 | -48.76038 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bc165e6-27a4-3762-aa73-250f94053b86 | -12.90216 | -62.08419 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74f735c1-856e-3596-87de-3a911381682f | -14.35626 | -60.31154 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5542b991-d1eb-394c-9768-141f880ac2fc | -4.40658 | -48.9502 | 2025-09-09 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16562b07-45e0-39f0-b8f3-f614ae065e3d | -13.04307 | -48.03447 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 328c9ba2-de9a-311b-8803-9ec961a7e4da | -14.36027 | -60.30829 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85d6e18a-62e8-3e44-9859-555781e8bdbe | -13.94058 | -48.24596 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 538bfd24-3699-3d27-b371-e9d6746079ed | -15.71799 | -53.54286 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69beeb21-5207-3fac-a0cf-aaff9b061e4b | -7.3424 | -49.56486 | 2025-09-09 05:23:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2331c36-1cf1-3242-b879-8bfb2fd43bb7 | -12.94602 | -54.80814 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e72c525-7f75-3f48-8c84-d745168cc0e6 | -15.26731 | -53.80165 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1b5fbf8-8333-354c-b401-4affe689b8f8 | -15.77673 | -53.54368 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5498ddd2-cc0e-3ff1-9a5b-cfbc677e72ca | -8.05604 | -48.63475 | 2025-09-09 05:23:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f44e636f-f246-3828-9dc3-361fec87e68c | -15.7572 | -53.52756 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8159fbad-661d-317e-9946-4a155ccf74bf | -12.18999 | -53.88274 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9cdde39-e04d-3401-a8e0-714569ba0d16 | -8.48099 | -48.26962 | 2025-09-09 05:23:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 222e818d-3ad6-39b8-9a9c-5f9973f3f30a | -15.78878 | -53.53223 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6719062-a5dc-3a5b-b4ae-a23c92b2f47e | -14.36697 | -60.3046 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd9b4aea-f7f6-315a-87ba-6413439e1c01 | -12.87397 | -62.11191 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1ba0673-6dd5-31cf-85b4-352194ffe180 | -8.40681 | -49.09665 | 2025-09-09 05:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5b0b01c-4cf0-30a7-9d54-cd0c2d61fa39 | -12.19909 | -53.88956 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| be69ab75-c8b3-33de-ad55-01b4412b878d | -12.41943 | -63.89182 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e10e74e8-fe84-323b-971d-6a930992e2ea | -11.12887 | -62.83105 | 2025-09-09 05:23:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ee4e186-bcc8-3fa6-8369-e4005b9c4faa | -15.27319 | -53.79599 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe5876f7-27eb-3f38-9621-f45c8e0eefc5 | -12.6273 | -56.97087 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 996cc482-8c2d-3c75-9cdb-c4563419e1cd | -12.90272 | -62.08065 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README61.md)
