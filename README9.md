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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1433c89e-80dd-3d0e-a09b-8c684dcf0ad4 | -6.27931 | -48.52476 | 2026-05-31 05:25:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2aff5f1c-b8c8-37dd-b4b2-eac56e5d579d | -12.54326 | -57.18003 | 2026-05-31 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 322bc890-da6a-3e3e-a815-b36a635a169c | -11.62331 | -55.18769 | 2026-05-31 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45852cdd-5e1e-3d30-b53f-390b90094ab0 | -11.62563 | -55.17122 | 2026-05-31 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30fb99dc-fe01-3fbd-a014-e99029184742 | -15.78566 | -58.66264 | 2026-05-31 05:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d7d27bf9-fcf7-3514-94e7-bfd26d9cce0f | -11.62387 | -55.18331 | 2026-05-31 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc52d299-dd63-3797-96fd-8967c5c2ce00 | -12.54463 | -57.16984 | 2026-05-31 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d30c2b6b-e270-3727-bfb0-5f6d9422e4bf | -10.71189 | -56.24584 | 2026-05-31 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4ce2c5b-3121-3ee9-87e7-8811c1a44be5 | -15.79069 | -58.65389 | 2026-05-31 05:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6c0688ee-54bc-3a0f-9fcd-36915327cb4c | -10.70786 | -56.24512 | 2026-05-31 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02d0354b-91b7-335e-a8f2-e506e712f9c4 | -12.54374 | -57.1736 | 2026-05-31 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e1bd034-36b3-395e-8939-7519fde231de | -16.2179 | -59.66141 | 2026-05-31 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9f2068f-e8a1-3014-9714-89a5ffde69c2 | -11.63004 | -55.17183 | 2026-05-31 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f67d0933-e219-3883-a3c8-f27f1da0cd63 | -13.70251 | -52.97984 | 2026-05-31 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7ec46c6d-d81b-362e-8130-44156bb44831 | -14.7667 | -52.67325 | 2026-05-31 05:25:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98deb8db-b041-3eae-8183-fa315ffc6d78 | -11.80145 | -57.01144 | 2026-05-31 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4ef6c9b-d3d8-307c-a0dc-fa77b1f67e69 | -14.12683 | -58.92933 | 2026-05-31 05:25:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d257aee8-10cc-3eee-a756-0678e3281ced | -13.7033 | -52.97335 | 2026-05-31 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8a104bb6-31b4-3759-9511-b323cfc44779 | -13.7029 | -52.9766 | 2026-05-31 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 953b32c3-0fbb-33ab-9f8b-b0254bd9c70d | -15.78192 | -58.66208 | 2026-05-31 05:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a5a10d4c-2333-3ddf-b59f-97c3c98826c5 | -11.62944 | -55.17625 | 2026-05-31 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcd7b30e-f751-37bb-a663-102e50301fd1 | -11.62443 | -55.18001 | 2026-05-31 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79f5ee37-f4bd-31dd-905a-0741adae2e68 | -11.62384 | -55.18437 | 2026-05-31 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 757f7961-27af-3ba2-a4bb-45d6a687eedc | -10.47443 | -62.45228 | 2026-05-31 05:25:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cb42e3a-7b27-3400-aa42-1c80c04d7044 | -11.62624 | -55.16674 | 2026-05-31 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74633ef8-5b7d-35c5-834f-2beb970306d7 | -14.12261 | -58.93301 | 2026-05-31 05:25:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1e4a337-4729-39a9-8604-fe8258b6c3d6 | -11.80074 | -57.01643 | 2026-05-31 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84adf50d-ef5f-340a-a965-d1bac29e4d13 | -6.80208 | -59.04523 | 2026-05-31 05:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2f3daa12-ead0-30ab-a17c-169f9aaccad2 | -7.50181 | -55.00979 | 2026-05-31 05:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 268f1443-0e08-399a-91f2-09858c864dda | -7.50255 | -55.00413 | 2026-05-31 05:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f8709da-602b-3f6f-a866-0333dcd2fc62 | -6.80313 | -59.04486 | 2026-05-31 05:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 30967eb8-33a1-315a-916a-546cc424eedd | -7.50834 | -55.01109 | 2026-05-31 05:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1522880-6e2d-3957-941f-b04ffbaf62ea | -9.4318 | -62.1484 | 2026-05-31 05:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b393bb4-d221-3a62-aa0e-9d7672c5cb2b | -10.70935 | -56.24488 | 2026-05-31 05:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85833fa7-3f0d-3d91-b186-ee1d4511fb51 | -10.47539 | -62.45214 | 2026-05-31 05:57:00 | NPP-375D | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e1a9f68-943e-3b97-adee-5fa8647e27ea | -7.19343 | -59.83807 | 2026-05-31 05:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4390f0a-4faa-3cfc-98c2-4de3decd1f52 | -15.78485 | -58.66083 | 2026-05-31 05:59:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c589a44c-8e2c-3327-9279-fcc4d7b6e296 | -15.78366 | -58.66253 | 2026-05-31 05:59:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d56d1499-452b-347e-9847-71ec087565f6 | -14.12062 | -58.93544 | 2026-05-31 05:59:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c2e3e7a-28f7-3536-bbe8-d6e356ccc4c9 | -15.78411 | -58.65828 | 2026-05-31 05:59:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d7bf7943-739c-3047-ae4e-b7dc4ec04835 | -14.12106 | -58.93176 | 2026-05-31 05:59:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a28e2d7-619f-3338-8e04-59c937b30c57 | -15.78534 | -58.65658 | 2026-05-31 05:59:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bc30d67a-b1b5-3fab-baa5-f5b919c72e49 | -10.0723 | -51.6769 | 2026-05-31 06:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c3044cfc-7486-3d4a-8836-4367bdf3bc12 | -10.0725 | -51.6559 | 2026-05-31 06:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 6a8d5f47-0c6f-3a4b-bd48-d379c8ac4358 | -10.0723 | -51.6769 | 2026-05-31 06:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 4b7de92e-73ed-31b7-99e7-d5c019d962d6 | -10.0725 | -51.6559 | 2026-05-31 06:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 3117ee8e-73ea-31a1-9398-a58960a0f6f9 | -7.9556 | -71.45663 | 2026-05-31 06:18:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6461eb7-90a9-38aa-9ced-95a729870157 | -10.0725 | -51.6559 | 2026-05-31 06:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 87524beb-afdf-390b-8c75-51518a3c8fae | -10.0725 | -51.6559 | 2026-05-31 06:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f45ebde0-5922-3e2d-b1bb-e8e22abbbb09 | -10.0725 | -51.6559 | 2026-05-31 06:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| cc19bd47-4520-33ca-9007-7db3f947cbec | -10.0725 | -51.6559 | 2026-05-31 06:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a27ac982-b51d-39cb-8ae9-c46dddb6ccb0 | -10.0725 | -51.6559 | 2026-05-31 07:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 6795aec0-bd44-3557-8f85-08235332187c | -10.0725 | -51.6559 | 2026-05-31 07:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| fa940a1f-cce9-3ebc-9efc-32cdfca8813b | -10.0725 | -51.6559 | 2026-05-31 07:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0c687e5b-5dbf-3735-b8ea-acc973840bd0 | -6.80051 | -59.04078 | 2026-05-31 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 36575f9a-f9af-325d-bd87-453039c2ceb9 | -6.79708 | -59.04447 | 2026-05-31 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6e5e754a-2161-3b52-b9db-75f111113eea | -10.0725 | -51.6559 | 2026-05-31 07:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 103c0854-3ab5-311e-b2b4-998c8ef483e0 | -10.0725 | -51.6559 | 2026-05-31 08:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ed48456b-81a6-350b-b86d-d9c725509979 | -10.0725 | -51.6559 | 2026-05-31 08:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5100300b-4190-3f0c-a8d3-a12bcfa02223 | -10.0725 | -51.6559 | 2026-05-31 08:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 16c9e4aa-c772-3346-8f66-d0036c70afe8 | -21.0843 | -40.97668 | 2026-05-31 11:19:00 | TERRA_M-M | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 20d79077-a0f8-34b5-bad9-b146a5dc767e | -12.537 | -57.1814 | 2026-05-31 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 60063b93-6645-39aa-9456-578fe6a741b3 | -12.537 | -57.1814 | 2026-05-31 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| ecb4d6cf-2736-3ae8-8269-cc664ad8a3e4 | -12.556 | -57.1798 | 2026-05-31 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| e56ce036-f1d7-379a-ba75-8adbcd1d2405 | -12.537 | -57.1814 | 2026-05-31 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 6c5deff1-9063-3d30-b7e1-59055dc51575 | -8.5347 | -51.57519 | 2026-05-31 12:53:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| fcf38f65-d741-3ea5-84d0-22923f471056 | -11.79096 | -57.01467 | 2026-05-31 12:53:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| dc886b1d-cd89-326c-953f-8c25ab29159a | -12.55375 | -57.15781 | 2026-05-31 12:53:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| f642200e-429d-3608-9277-ef4ae1280515 | -7.50602 | -55.00013 | 2026-05-31 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5cf39e6f-076b-355c-9249-2cc953068b6e | -12.55165 | -57.17522 | 2026-05-31 12:53:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 206.5 |
| e78a6447-a077-396f-b0b8-fab74796ae4b | -11.7976 | -57.00916 | 2026-05-31 12:53:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| da6f74f5-56e9-3791-b3ca-00d3d6c41c71 | -14.12345 | -58.93406 | 2026-05-31 12:55:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4effebcd-4ba7-319d-8a57-dc4171623c61 | -12.556 | -57.1798 | 2026-05-31 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 1b808686-9769-3933-91dd-a77782cc1ead | -12.5372 | -57.1614 | 2026-05-31 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 9b7f38f4-355f-3122-b7a3-d172a4b2fabe | -12.556 | -57.1798 | 2026-05-31 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 2e7f0f39-234c-360d-bb63-7d06612b096c | -12.537 | -57.1814 | 2026-05-31 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 24079368-c62e-3fa0-868e-f6db4861d1d7 | -12.5562 | -57.1597 | 2026-05-31 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 3d255048-d5e7-33be-ba52-cf408e184165 | -12.537 | -57.1814 | 2026-05-31 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 6cdfe353-cea9-3fff-91fb-d8a7910c8ee3 | -12.5372 | -57.1614 | 2026-05-31 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 0e047b6e-6531-324c-98a9-b674ce2d5ceb | -12.556 | -57.1798 | 2026-05-31 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 647be6bb-c7e5-3a3b-a604-ac346191b065 | -12.5562 | -57.1597 | 2026-05-31 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| fd2d574b-1344-321d-8e8d-ed3cf62227c6 | -12.537 | -57.1814 | 2026-05-31 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 7d0fd23e-5ff3-33c9-8b01-3bf8232e898d | -12.556 | -57.1798 | 2026-05-31 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 2af03c7b-1949-390b-b6d5-ca8a2580e05b | -12.5372 | -57.1614 | 2026-05-31 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 4c53f373-18b5-39ee-aad1-3f87d26f4063 | -12.5562 | -57.1597 | 2026-05-31 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0b84a8cc-c843-329d-a579-8cf860f12b78 | -12.537 | -57.1814 | 2026-05-31 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 07ba96cb-dfef-3f35-a047-af9eb69b8cb4 | -12.5372 | -57.1614 | 2026-05-31 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 36456f05-133a-3ecc-8418-f0bb0cf90ca1 | -12.556 | -57.1798 | 2026-05-31 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 43a2b795-a48f-3954-a91a-415b60e03060 | -12.5372 | -57.1614 | 2026-05-31 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e583b4b2-4311-3b4a-97b3-bd0c341fd910 | -12.5562 | -57.1597 | 2026-05-31 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 8d587e85-a1bb-312e-b840-a651a06cb932 | -12.556 | -57.1798 | 2026-05-31 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 9e245a80-31f4-3daf-a8bf-ffbaefd91713 | -12.5562 | -57.1597 | 2026-05-31 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 3ec10285-a0b9-3f7c-8154-336b55f864ce | -12.5372 | -57.1614 | 2026-05-31 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 53791fe0-5d27-3a48-ab1e-2280639c7ff8 | -12.556 | -57.1798 | 2026-05-31 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |


