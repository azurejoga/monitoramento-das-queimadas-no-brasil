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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3957e4f-2f2b-38d5-9dcf-1721f366149e | -6.74979 | -59.15982 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9acf18c-a895-3a3a-a028-bc08781e3545 | -7.60463 | -60.95893 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da2d2983-e3d3-3289-924b-e99c586d152e | -8.56054 | -54.75024 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f3b1c4a-e47d-394b-9066-dab940c36157 | -8.55441 | -54.72975 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 11b3cbaa-348f-3f12-82bc-3d9bb0b56e0b | -9.15948 | -59.70648 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4fca4b1-e9c7-3553-a89c-6451ba9fc651 | -9.42587 | -60.43789 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 083a5395-d27b-3f88-a3d2-38238b98139b | -8.55821 | -54.73469 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48fb2e89-4c2b-3d14-b1fe-dbbd93b66665 | -8.56673 | -54.73756 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a95a21b2-cb1a-3d91-973d-0ba40cdf2519 | -8.56348 | -54.72834 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a54829e6-5c01-343d-8c96-4843cf7dc119 | -8.90002 | -60.56498 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76d27fe4-5bc4-3418-8d7b-e50292936789 | -7.43394 | -59.7996 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cafa0054-3655-30d6-bc9a-ed4e332b1c07 | -6.78879 | -59.44592 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63db4849-f26c-3d57-a9a0-4c2fe04017b8 | -6.91018 | -62.90445 | 2026-08-19 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91b8c558-39eb-3ce7-8df5-0cc218a75f92 | -7.54151 | -55.59215 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c60042a0-2fe1-3d49-bae6-ccaa9cea2b3c | -9.20499 | -59.47245 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30c6b930-fea8-3a73-85bf-7329561551a1 | -6.79269 | -59.44286 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c9a5a7e-6daa-30b3-bf9a-31d94b3e5ae0 | -7.05054 | -59.84181 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 46273aa6-6dc5-37cc-96fa-614f68d65f5d | -8.57704 | -54.69444 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24bd421b-ee58-36af-9d4d-9481aceb69ce | -8.5621 | -54.77054 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6b6a1f02-f9fd-3159-9082-482b2d59e1e1 | -9.39807 | -60.57445 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af6b284d-6a06-32b8-97a3-09c0edbc63cb | -8.08179 | -61.36556 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36c6fa7e-a9b1-348b-bc44-4f9a6dc15003 | -6.74393 | -59.03188 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ee522ca-9f55-3c54-a78b-f86ae4ac3505 | -3.47843 | -59.35182 | 2026-08-19 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1df14c89-4d9a-3003-a9bb-fbed7c8e0ac6 | -6.75317 | -59.16037 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9940e22-ffb1-3e3c-b2cc-058036a0b412 | -8.5732 | -54.68946 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0665c9cd-7614-3e09-a9ed-beab816c22a7 | -9.39637 | -60.56337 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f0919996-234f-3585-97b4-975e06b39028 | -6.75097 | -59.17489 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f546e618-ff7c-32e7-bd0e-1fe118e27689 | -6.79439 | -59.45411 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ae3d1ba-e97e-3403-80ef-64cea61acbce | -9.42362 | -60.43031 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 67080ece-40d6-3f9f-a5c3-9b8801c25948 | -8.56494 | -54.7509 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 342cdd2b-a5ad-36ab-99a6-5a4dc4a402c3 | -6.85966 | -59.03105 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c21466a4-20d9-3872-a367-9a9b8d879140 | -9.39953 | -48.2408 | 2026-08-19 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f3ad769-50d6-3131-be69-36c239db0b4b | -8.64257 | -62.83195 | 2026-08-19 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00b398ff-6120-358d-9701-418d3261abbb | -3.22148 | -61.25805 | 2026-08-19 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3a758bf-3ce3-350e-ac97-a2546440012c | -6.87427 | -59.03268 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4899cc2e-e038-3562-bce4-8861d2ebaee5 | -11.0901 | -49.918 | 2026-08-19 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75882604-5cd4-3a90-9fca-363989870e38 | -6.88786 | -59.03473 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82bdcc56-e956-3eb9-80b6-f41658f8cb60 | -6.8432 | -59.00232 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b6c9c96-1b90-3a85-9288-2566723acfa4 | -6.95243 | -59.04467 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba0006d3-c008-3644-a56a-c675489a0863 | -7.56684 | -55.56189 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cddc98df-53fc-31ba-b04d-15e9826ed1ef | -8.53374 | -54.74875 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7b276c6-8e8a-33f6-8e61-3560f6d2ffb9 | -8.58376 | -54.74464 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c70954e3-4c37-3d9f-99b0-f5ea43e4383d | -9.17883 | -60.82748 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad245e70-73f2-3ace-91db-c52e8cd6e97b | -9.05559 | -57.0699 | 2026-08-19 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee50060f-8e86-32ef-b5c0-13458fc89acf | -8.53497 | -54.74003 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d002b477-c01b-38bc-b3ec-9cdc14eac7c1 | -3.10129 | -61.22117 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83db35f3-0d08-3e14-a3c0-746226d65a35 | -9.11066 | -60.3887 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3988a556-be8d-35d2-a232-6f0a0d328eec | -6.89411 | -59.03941 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bd552e8-373d-331b-8479-fcebf17b2c43 | -5.92659 | -61.31516 | 2026-08-19 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 131e3c85-01dc-3125-83c3-0940182876a7 | -7.10528 | -59.77059 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4367a75-929a-3630-956d-6c2ab37bc403 | -6.89154 | -58.94123 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d48d39c-c03d-3d1d-908d-28b64fc42db8 | -8.18729 | -55.005 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0b3fb9a1-1ead-3c26-bae4-9fc7f3a986ae | -6.88225 | -59.04887 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24731bbc-075d-38f3-b26c-e6694da4011a | -7.60206 | -61.23553 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba8aa0e9-4ec2-3219-a8db-19954ecb2109 | -6.65394 | -56.43097 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d831b5ea-7a21-316f-9331-8bd3be6d4d2e | -8.21729 | -55.02744 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cc84956-69a3-3981-97d9-e49b1c8b64e8 | -8.58148 | -54.695 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a40669b0-7efd-3fe8-942c-15a19f7d8900 | -8.56711 | -54.7669 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 028fb8f2-eaf1-3496-ada7-3062c08baf2a | -8.58642 | -54.75818 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 206a4d77-7269-3afc-b762-54ba61940272 | -8.55881 | -54.73043 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f1f3df2-2ebe-3b10-9594-7a236c988188 | -6.86022 | -59.02738 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fadb1125-798b-376f-afaa-dad335a077e9 | -9.40309 | -60.58604 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42c87022-60e1-306f-9261-e756fca99390 | -9.4075 | -60.57952 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97c18635-eff7-3bb3-a862-3089f63738fa | -4.01106 | -48.06113 | 2026-08-19 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 16332a3c-fc86-319e-a441-3aaa73e135e3 | -3.67873 | -47.65237 | 2026-08-19 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 05e3a9fe-38fd-3e19-9a1d-4c3058a8e972 | -6.69505 | -58.94199 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0d635319-0b5d-3362-a0f4-dad1ef7f86c4 | -9.42354 | -60.40856 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68c850dc-871e-3e24-bd41-e9ac1dd2823a | -7.04999 | -59.84533 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49db85c9-be21-36c4-85cf-c09a27a63863 | -11.16685 | -49.62248 | 2026-08-19 05:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b422187c-5c39-397e-a778-802083c93859 | -8.56832 | -54.75842 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ff5edb06-9a63-3173-a2c9-450de56bf26d | -7.05666 | -59.84634 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e29502ec-6d3a-3897-98f5-bca8dece551e | -6.78543 | -59.44539 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7547e68a-9a3c-3bd4-973a-4d5adc3fefec | -6.84829 | -58.9918 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4a0bf16-bfc5-3039-a3a3-fcb7cffb6545 | -3.43035 | -51.51607 | 2026-08-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32986626-d5ec-3fae-a164-fecf9a6ac3da | -8.57436 | -54.74765 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea38f9aa-4a89-3346-a5c0-c6bb38f62f7f | -6.70583 | -58.93979 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f76db6bf-5855-3468-bf98-cc4f03f45df6 | -6.76837 | -59.15148 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1090838c-d3d4-3cb0-9b3d-deff588f2875 | -9.42145 | -60.44444 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a7cff1ae-69d6-3b46-9e7a-b9e63858b6bb | -7.60517 | -60.95547 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32163a62-aa1f-3d4d-a565-50eef9e0bad4 | -9.42858 | -60.42022 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e5170e4-d118-315e-b4fe-c62bbab91d42 | -6.87545 | -59.04782 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3753fd22-57e4-3360-9634-b9acd41777c8 | -8.5629 | -54.73266 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81a6b378-5ac5-348c-b5cc-c559a812dd6e | -8.56232 | -55.25091 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b874577-c396-375e-8eb4-aabaf066c695 | -2.76485 | -48.57267 | 2026-08-19 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29855413-fe63-35da-8dfe-ab068b0d61f0 | -6.86067 | -59.0306 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 675a5f5f-f1db-34da-8625-ed54beeb4379 | -8.58878 | -54.74084 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c777b48-40e7-3eda-9cf0-45283b75dc05 | -8.90231 | -60.59404 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c474bd1d-6cb8-3983-9f07-ad9486893d68 | -6.74563 | -59.04336 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64a17236-5417-325d-a931-9626e4811c1f | -9.3908 | -60.5553 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b170336b-eb66-3ce6-8573-2e1b4a6c4567 | -8.56827 | -54.72727 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9cf793ac-7ec4-30d5-9e4e-1321f7db7002 | -7.53688 | -55.59519 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c10db2b2-0e36-3eaa-aa61-366ac0e7e4a2 | -8.58437 | -54.74014 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa407415-403a-3019-bcd3-82ac71f68a1b | -8.58524 | -54.76683 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31342020-6471-33d1-9ac9-c12e9599ba0d | -8.64597 | -62.8325 | 2026-08-19 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5e3932e-0d76-3e69-9d56-dab7903a1b93 | -8.55013 | -54.76 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0106f6a-227f-3db2-9ced-4aba722878fe | -8.18783 | -55.00122 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 170b623a-ae19-3744-9e54-de9b9673e81c | -8.54879 | -54.73766 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbc269a2-5755-3042-85c8-6bd071d13cf7 | -6.68523 | -59.0751 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9d3d5dc-6cee-3389-914c-7d955ee5f1f6 | -9.39861 | -60.57092 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1bde86a-c94c-3067-84bc-8cb3794c3e85 | -6.86012 | -59.03427 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README51.md)
