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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c09d272-e640-3b80-9767-c5b3aaba61ae | -16.04322 | -52.51934 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a8b32421-5c2e-3e6b-b482-49b74033fa8c | -12.28226 | -50.15741 | 2026-09-21 05:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ea65a4f-bf67-3094-a507-05b2330dc2eb | -12.27534 | -50.15657 | 2026-09-21 05:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd14c902-8230-3c45-b2a3-2226979a8d7f | -17.00019 | -56.52164 | 2026-09-21 05:44:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9ccda413-c98e-3993-800d-cab6476d24b2 | -9.42082 | -68.75833 | 2026-09-21 05:44:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60b278da-3307-386a-a119-ee2276c802de | -11.74779 | -54.56785 | 2026-09-21 05:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d61d9e0-c135-3fa7-83f9-3e9c82beedb7 | -16.01018 | -52.5318 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cba13dff-3de7-39e1-9237-8dad82e06f2c | 4.08182 | -61.40642 | 2026-09-21 05:57:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc260e24-03c1-3872-9a25-e3e2182a4be9 | 1.77473 | -60.23672 | 2026-09-21 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f403f44-0992-3311-9cd8-9973f320c745 | 0.78653 | -59.20244 | 2026-09-21 05:57:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bec71a68-e32b-311d-b99f-8cf3f52b3884 | 1.54519 | -55.80792 | 2026-09-21 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb52a9c7-8c6c-3455-a249-e24b8a67cb55 | 0.79229 | -59.20707 | 2026-09-21 05:57:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abb19c1f-13cd-3bd4-84f1-4d9350670044 | 4.53027 | -60.86204 | 2026-09-21 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b8ce366-595a-3e9b-ab4e-6722707a692e | 4.35658 | -60.99709 | 2026-09-21 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c454234-3fe2-3335-91ec-9349b5b13b65 | 4.08126 | -61.40296 | 2026-09-21 05:57:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69a93f72-e2bb-32a0-bd08-402d28bcd4d1 | 4.32381 | -60.69324 | 2026-09-21 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac0d5255-d0e8-3790-a15a-6d44cf91308f | 4.81444 | -60.32617 | 2026-09-21 05:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b496ab5d-c21b-35e9-89c8-09718cf10675 | 4.70311 | -60.89525 | 2026-09-21 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ca855c3-08ec-38d6-83cf-cb7b53b9e897 | 2.34475 | -60.91515 | 2026-09-21 05:57:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4599b8e9-1d24-3479-8ac5-fcbef01061a4 | 4.70248 | -60.89135 | 2026-09-21 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02e4cda0-1334-3a7e-b23d-9d5b542474e0 | 4.32807 | -60.69321 | 2026-09-21 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 453d2e61-3e5d-3db5-9c89-4c70111f5095 | 1.07888 | -60.67934 | 2026-09-21 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d3cb638-7df4-3b05-9c7b-8287f9f49a06 | 1.53844 | -55.80471 | 2026-09-21 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c49ce06-fe14-3d6b-9bcf-30341f0b5157 | 1.77214 | -60.2346 | 2026-09-21 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2758f8b-3dd9-3919-a0d3-8ed1a6d3d67e | 1.53773 | -55.80037 | 2026-09-21 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a166f4a-465b-327e-8bcf-2d130e4a3593 | 2.31934 | -60.91922 | 2026-09-21 05:57:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ce6309a-568b-3202-a81e-734b400bf26f | 1.54372 | -55.799 | 2026-09-21 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5aabce06-532f-3266-9617-4325798091b9 | 3.67942 | -61.86895 | 2026-09-21 05:57:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a0676c9-a466-35d3-9338-611faf974077 | 1.77026 | -60.23747 | 2026-09-21 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b9dbbd7-cc63-3286-bfff-8a6ddf2ac5dc | 4.70256 | -60.89573 | 2026-09-21 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9b1745e-cc10-3632-8785-4a98e630f258 | 0.79142 | -59.20167 | 2026-09-21 05:57:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02680ca6-627a-310a-948a-867080c1d218 | 4.5346 | -60.86272 | 2026-09-21 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6578ac62-652a-373d-afe6-5d4dde9e8c31 | 0.7874 | -59.20782 | 2026-09-21 05:57:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 606d528f-43f0-3253-a958-104f95c5f9a6 | 4.52606 | -60.86205 | 2026-09-21 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e89d92c-f48b-3867-a057-4710df2e30f4 | 1.53913 | -55.80886 | 2026-09-21 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5f94716-fcf6-30f9-b264-d43e59938f5c | 1.54453 | -55.80394 | 2026-09-21 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1efa3d34-9286-356e-8329-68b6999d912b | 4.7019 | -60.89183 | 2026-09-21 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63a4cbe9-a826-3292-bea8-353abf15ece4 | 4.81082 | -60.33056 | 2026-09-21 05:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f473de2-873c-3fda-9ace-6397d927332e | -3.53753 | -58.69508 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 108e9584-6558-3051-97f8-350d21b798ce | -5.01262 | -56.09022 | 2026-09-21 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef3f3c3d-0f63-34d0-b780-a7d44588abf7 | -2.91858 | -57.79395 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79a9c45b-7975-398e-a1d1-5feeb34f5bd9 | -3.06674 | -61.27939 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 913408c5-0676-3e1e-945f-fddb39d512b3 | -2.9114 | -54.19341 | 2026-09-21 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ebb85f49-d97e-3017-a133-397de67593df | -3.89923 | -60.59242 | 2026-09-21 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68389ddd-2453-3f66-a26f-5c5d1c3c3363 | -3.40565 | -61.30076 | 2026-09-21 05:59:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d4bfac5-8474-3c04-b787-d67dab6e760c | -3.54395 | -58.68904 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99bbbd87-0406-36b9-8cf4-36b7d793517b | -3.39109 | -59.53173 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b5ef770-587c-34fc-a8fb-73abcf023b69 | -5.77078 | -57.58938 | 2026-09-21 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3893ee6b-beac-3eee-9dc7-151b7abe3d21 | -4.35348 | -55.65094 | 2026-09-21 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a77b52fd-7700-3f76-a67e-b599ba939e34 | -3.75789 | -59.42402 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d677063e-85fd-39df-9674-954606e3136e | -3.49218 | -59.57441 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5dfaca24-adb4-393e-9605-19b99f92d1a7 | -2.9206 | -57.7933 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 052499ad-21db-3954-8f7a-128bfbc6470b | -2.87398 | -57.81916 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d40d9fc1-8e13-39be-8086-25a9f1f0e351 | -3.39812 | -59.58772 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4976cf5b-cbfa-3be6-bd9e-03e62ec9d0ce | -3.07056 | -61.28461 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c088637-8b40-3d8d-8437-caee1cf581ea | -2.60361 | -59.76176 | 2026-09-21 05:59:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dad51b1e-bc60-322b-9202-65aae9ef42db | -2.87693 | -57.7997 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49b4edad-668e-3be6-914d-0122e4286245 | -3.48627 | -59.6131 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6f48292-cae5-3046-9c5e-80d7cc7a3337 | -2.90192 | -54.18658 | 2026-09-21 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cd75a61-0ac6-38af-b113-f42cbafb0d47 | -3.33498 | -59.83119 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 064afcbb-5e6f-3dce-af12-aefa1224469e | -3.8246 | -59.33176 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb34c3c1-2e9b-3208-9e18-c5bd144aa9ab | -3.07861 | -61.16993 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb25c2e1-70cd-30a5-a5f6-b84826f2e2be | -3.34729 | -59.85394 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c69991a-4bb7-39ce-ae0a-60f56638ffe6 | -3.58459 | -59.06879 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 96fa7c21-f476-3783-b585-1ca306f44b4a | -3.43918 | -58.02063 | 2026-09-21 05:59:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da7b5dae-6fdf-3232-a424-d8c811f62299 | -3.48936 | -59.61444 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2851a8a3-8943-3a67-8671-05a8d622f080 | -3.48754 | -59.57067 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 205acd74-9240-314e-b987-5a74c70548e5 | -3.53803 | -58.69166 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e57dc181-944c-36eb-a3ab-5d7b0cd17d50 | -3.39372 | -59.53519 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ea5c5d9-f350-3787-b67f-d34fe3c06e07 | -3.07124 | -61.28009 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 02459afc-c220-3242-8417-21dea71f9983 | -3.13357 | -61.4008 | 2026-09-21 05:59:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 082e50cf-6e6e-392a-802f-4f17297e9905 | -3.66466 | -54.26678 | 2026-09-21 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd8d4d52-a92a-32df-be05-35314aacc2a5 | -2.90064 | -59.22769 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 57c51bb1-611f-3e9b-a989-ed174b38878b | -3.4898 | -59.61145 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6012d5a5-7d06-3c24-b064-5cdbe0590988 | -3.05324 | -61.27734 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39f9a63a-1aac-328a-a602-b71b6f8cd23e | -2.87065 | -57.80275 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbecc71c-006d-3088-a582-f5d8fcec1f6f | -3.48892 | -59.56164 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70cb1abf-5603-3a70-9c5e-a53db9217098 | -2.90257 | -59.224 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ed3ce140-3b60-3334-ad8f-33a42f924bfb | -2.91547 | -57.78854 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58ae9a61-080a-3064-bdbb-58bf8cebd934 | -3.59035 | -59.0663 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6360276d-6b72-3dba-9389-b5bb0d3b1034 | -3.43237 | -59.26184 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f56dff38-a5d8-3f65-9f7b-51cf7b656c4d | -5.7581 | -57.59234 | 2026-09-21 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01b75c06-fce0-3408-a4bd-53fabbdb7edd | -3.53531 | -58.69576 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc369031-54f2-3263-9a33-512060ef47ca | -3.05774 | -61.27803 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 913eb253-2028-3bcd-ba41-c4fbc8400182 | -3.7588 | -59.41781 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73538723-7cbd-3fcd-916e-f5a180866dbd | -4.35271 | -55.65631 | 2026-09-21 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0d486d1-0ab5-385b-a272-b30084ed3833 | -3.39693 | -59.5846 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d2a504e-cea2-388a-b46f-2e2bc7eedfe1 | -3.06742 | -61.27492 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3cb26982-1427-3f42-a5be-f931c887b9e3 | -3.54346 | -58.69244 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da69663e-cb56-345c-985e-d80e186a23ee | -3.04624 | -61.26255 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c8cf631-0a3c-3313-8867-4d6c638c152a | -5.76413 | -57.59306 | 2026-09-21 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f62ce61a-614b-3bd7-887e-3a830f02493a | -3.34688 | -59.85349 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 750216a8-0980-341f-b7bb-8962be038b53 | -3.05391 | -61.27288 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32b590db-9638-3818-9e69-5c8660b0efb0 | -3.47837 | -59.59665 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fdd7ef2e-47af-372b-95b1-63337324c923 | -3.42716 | -59.26109 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7ce247eb-418c-3241-8b20-37e605d2f97f | -3.48673 | -59.61009 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1f6922e-ce31-384a-b65b-192a2b2004b6 | -3.38306 | -61.2974 | 2026-09-21 05:59:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e16d4d2b-3d98-37ea-8fa5-c8cf80d2ed7e | -4.09054 | -62.08815 | 2026-09-21 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7feb041-e280-3859-9845-3e8753dc6e44 | -3.07574 | -61.28079 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95b18e3d-48e2-34f7-ba41-e16fe78fc7b1 | -3.81891 | -59.33419 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README104.md)
