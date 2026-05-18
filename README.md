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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94feeba1-cbd0-3bdf-abe8-f047df9b4b1a | -14.87982 | -46.82882 | 2026-05-18 00:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2fde3a55-02c8-363b-806c-d722e20afea4 | -9.07336 | -44.31314 | 2026-05-18 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 19b2d8cd-28e3-39e8-b20f-c06e1ce8aba3 | -11.44758 | -54.10147 | 2026-05-18 00:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 2764e952-44be-38f0-8fe3-d91d114c3ef0 | -12.0786 | -51.25801 | 2026-05-18 00:11:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 87f2c610-d8f5-31be-8c62-306c4f5950b8 | -11.44092 | -54.09066 | 2026-05-18 00:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 19c2cab7-5146-3ca3-8a15-8d9bc0cbfe76 | -12.37935 | -50.04582 | 2026-05-18 00:11:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2379ca5d-b672-3208-99eb-452e20eecfd3 | -11.84481 | -43.9623 | 2026-05-18 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 981c5fbc-2a77-37c1-b83a-89756ef1512c | -10.40606 | -44.94855 | 2026-05-18 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 30f965e4-1aa0-3dd0-ba1d-4ec7b5dc9d2c | -10.40422 | -44.93646 | 2026-05-18 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c2dcf49a-2c0b-3049-aa12-1592054c0e76 | -11.44314 | -54.10847 | 2026-05-18 00:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 84bb5467-1f8c-310b-b8fc-8856b68b0f27 | -11.88052 | -43.81047 | 2026-05-18 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2990eadf-88f0-3b2b-8dd8-477e5a10883c | -12.06457 | -45.28039 | 2026-05-18 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 936547ef-94f8-3fdc-8b13-46f67d1a67cc | -11.44549 | -54.08358 | 2026-05-18 00:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 42354aa6-0a4c-3169-9849-fe470a081667 | -12.05488 | -45.28193 | 2026-05-18 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ddda3312-248a-3be4-9453-01e3250eec4c | -11.4572 | -54.098 | 2026-05-18 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 70fa69b6-11f0-3a05-9577-792ac0bf1542 | -11.4383 | -54.0998 | 2026-05-18 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 532b4e63-5428-3686-b042-d0ca9dd5048b | -11.4572 | -54.098 | 2026-05-18 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 77ecb3eb-55fa-3e80-a75e-f83e473d6c93 | -4.36924 | -37.89744 | 2026-05-18 03:38:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97efe96d-95d8-3e3f-b55a-420ded5577e4 | -11.84412 | -43.96025 | 2026-05-18 03:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5ca8141e-0dfb-31a5-94b7-c898af8bd45e | -11.84282 | -43.96692 | 2026-05-18 03:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74dce6e9-9d35-3e95-98cb-a5b20fc5c82a | -10.03731 | -38.19865 | 2026-05-18 03:40:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 32603c07-9e8b-3d29-882a-9ac4fc8cc4cc | -11.84347 | -43.96358 | 2026-05-18 03:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92ce0978-2986-37a1-af40-5512669304db | -12.06457 | -45.28062 | 2026-05-18 03:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce7546b6-29cd-3a6a-a080-3fa2b3976497 | -10.40977 | -44.93818 | 2026-05-18 03:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bb1f12e-035e-3004-8550-9cda66e13326 | -12.05809 | -45.28337 | 2026-05-18 03:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3389f9d7-4db6-3ec4-9b6f-f642ef7fdef1 | -14.48688 | -46.51822 | 2026-05-18 03:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ffefd811-493b-3ddd-a259-a6ff32f3115a | -14.05661 | -44.48267 | 2026-05-18 03:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d581120-5ceb-3482-bdb5-793379585c2f | -11.87916 | -43.80728 | 2026-05-18 03:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 464cc37b-eea3-36a8-8b90-3ed667a19dba | -11.87979 | -43.80402 | 2026-05-18 03:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afa9f615-3f4f-3272-a150-dcef4099f1e1 | -9.22011 | -43.12933 | 2026-05-18 03:40:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b97135df-a65f-39c8-9a4b-c245d64bf501 | -14.48594 | -46.52267 | 2026-05-18 03:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5839a60b-d477-3e27-9f90-5ea06483e615 | -14.05726 | -44.47939 | 2026-05-18 03:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cdcafbd9-8833-341d-a73d-bf51b38c2714 | -10.40325 | -44.94107 | 2026-05-18 03:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8636a2ef-2354-3eb2-b19e-60a616657630 | -20.35083 | -40.87688 | 2026-05-18 03:42:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ebf599c0-f16a-3df3-b900-b98d9157bdb0 | -20.35184 | -40.87481 | 2026-05-18 03:42:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e229ec92-01d2-3a8a-98af-87afb1552e5d | -4.36814 | -37.89536 | 2026-05-18 04:25:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 00872401-5d19-31b2-8a76-2710681df136 | -4.36737 | -37.90078 | 2026-05-18 04:25:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 94b27c82-7f38-3b01-8f69-c969d5ce766f | -12.06828 | -45.28051 | 2026-05-18 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8d00965-dc26-3a91-b843-83068adbe7aa | -11.84292 | -43.96701 | 2026-05-18 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d879bbaa-f179-3b64-a936-12782c111e97 | -12.05738 | -45.28277 | 2026-05-18 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e120bdb-3a8c-34d2-9cc3-744712d72575 | -12.06082 | -45.28331 | 2026-05-18 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd4ee1ce-526f-3a7e-b332-5beda73067a1 | -12.45151 | -54.47453 | 2026-05-18 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e742a9d-60a8-3d7a-b673-69696dfb1730 | -10.91218 | -54.12203 | 2026-05-18 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d20a5a6a-f07c-394c-b347-e5d79fb9ed79 | -14.05939 | -44.48348 | 2026-05-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9d06cd5-87cc-31ff-83d8-41cb8874d740 | -10.40638 | -44.93804 | 2026-05-18 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c2925972-507d-32f4-9dc5-bd5ea850fe12 | -11.44229 | -54.09146 | 2026-05-18 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c01bcc67-eca3-3d8b-97b9-4e8b21e08719 | -11.45382 | -54.09176 | 2026-05-18 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dc9e10e-55f4-33de-9b56-3efd545ea1f0 | -12.44617 | -54.47828 | 2026-05-18 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7077594b-6338-347b-9749-ec02ecd36d7d | -10.04146 | -51.68409 | 2026-05-18 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63098126-6721-35a7-bd19-436985dcabec | -10.91671 | -54.12288 | 2026-05-18 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d09e404c-6dbc-30d4-907a-bce49da00f9b | -14.41614 | -44.36356 | 2026-05-18 04:27:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d74f84f-0e25-394a-bbb5-463105fd08f5 | -12.06427 | -45.28383 | 2026-05-18 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bea6287-1ec1-358c-aed6-37398d632de5 | -11.45043 | -54.09773 | 2026-05-18 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de6aa194-156a-3602-8d50-93a24dcee19d | -12.44701 | -54.47366 | 2026-05-18 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5d08259-05ba-3590-90c7-43fb1422bc21 | -11.44514 | -54.10148 | 2026-05-18 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c9855d0-6cbb-3469-b99b-a82ee8cebe95 | -10.91301 | -54.1246 | 2026-05-18 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f6f1dd7-21a3-3107-ab66-bc81a2e39af4 | -11.45124 | -54.09316 | 2026-05-18 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c244f0a-6253-3484-a6b4-9afabbbfc0d3 | -10.04117 | -51.6861 | 2026-05-18 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf719d4a-52d9-3834-9a7f-c637c241dac2 | -12.06483 | -45.27998 | 2026-05-18 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9654bcc9-71cf-3915-bf3a-33e2e4a0e01b | -11.31032 | -54.04033 | 2026-05-18 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c772f694-970f-3730-97ce-438c7c3894d6 | -12.06139 | -45.27945 | 2026-05-18 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41a08f4a-162c-3477-9a4e-8cd7069be76f | -12.07768 | -51.25442 | 2026-05-18 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9eb26d1e-35b0-3394-ac64-87784dfcf37e | -12.37667 | -50.04316 | 2026-05-18 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84699381-68c9-3e65-94a5-b77ec752b9c5 | -11.44677 | -54.09229 | 2026-05-18 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 08697435-b533-398e-b0b2-ce3fd9560709 | -9.32175 | -50.40213 | 2026-05-18 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae6f4fee-78f3-3048-bd11-1c39b97dfdd5 | -11.84354 | -43.96268 | 2026-05-18 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7439bd7b-7de7-3c8b-a4a9-12170ae97ffb | -11.84719 | -43.96323 | 2026-05-18 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 98a9369d-9edd-3808-b6fb-297ebe43e863 | -8.67493 | -43.95076 | 2026-05-18 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c980556-5e11-342b-94c4-0020eec7fcd1 | -14.06001 | -44.47911 | 2026-05-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 861abbed-8a59-331b-b789-bc9edebbecaa | -10.85913 | -44.54635 | 2026-05-18 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfb52d7a-ff02-3396-a1ec-e574ca768b31 | -11.88445 | -43.8078 | 2026-05-18 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b1fcd5e-0f2e-3744-8ec1-fc64235a395b | -10.91301 | -54.11731 | 2026-05-18 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 016a80b5-0ad5-3bf4-ac1c-4e55dd2327a8 | -10.91387 | -54.1199 | 2026-05-18 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5210b05-5db9-3c44-be7b-ddd473b4ba99 | -12.37795 | -50.04339 | 2026-05-18 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b61671d-b670-3a2d-95f0-bdff6a614414 | -11.44596 | -54.09686 | 2026-05-18 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54bd0c1f-ed02-3d36-91ed-a489fa294e37 | -11.45298 | -54.0963 | 2026-05-18 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d106f444-e095-3604-aa10-36fc446165a9 | -11.88077 | -43.80725 | 2026-05-18 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd7f32a8-7e33-3798-92a2-82e0de8b1092 | -11.84657 | -43.96756 | 2026-05-18 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e417ede-8602-38c7-9ddf-84a7737ccb29 | -10.40982 | -44.93857 | 2026-05-18 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0872ac81-9248-30a2-83c4-b5c3e2dfa007 | -7.71633 | -44.55519 | 2026-05-18 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f0141c8-dd72-3349-81e8-4fc1d1b62cb4 | -13.30998 | -47.51664 | 2026-05-18 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3b06358-80c7-3be7-a85a-fbfab83b6198 | -7.71577 | -44.5589 | 2026-05-18 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0043c11b-3d0d-39ed-8d7d-b022f033669e | -18.77076 | -47.08871 | 2026-05-18 04:29:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| caa35633-7d7a-3a3a-a2b6-26fdf091aa4e | -14.31495 | -47.17231 | 2026-05-18 04:29:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af71a697-52be-36cb-b6d8-147fdd95db78 | -14.8836 | -46.8242 | 2026-05-18 04:29:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fccd334-052e-369f-9935-42c498c6aa2e | -14.07742 | -53.43945 | 2026-05-18 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7b5a18b-d80f-359f-92b0-8e7f7d8ee6dd | -14.07675 | -53.44326 | 2026-05-18 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20e37a0c-9c6d-3c42-8072-f30412fbb5e5 | -14.08056 | -53.43943 | 2026-05-18 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0792f7a-1086-3a27-b062-2bfad96b5eda | -14.07986 | -53.44324 | 2026-05-18 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bfabe5c-36ad-39b9-8451-3eb42d802741 | -15.42251 | -52.19873 | 2026-05-18 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a73becd-bfd1-3dcd-a7ed-78da6bdeb965 | -17.35712 | -47.80996 | 2026-05-18 04:29:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d61a2f52-181e-3efe-831a-300ff3b75071 | -14.08152 | -53.44019 | 2026-05-18 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 609d6556-ad45-35f1-836a-4326a8cf463f | -7.91959 | -48.26867 | 2026-05-18 04:59:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63c451c4-ea30-38d6-a066-bfe994a89a7a | -10.91233 | -54.12166 | 2026-05-18 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 348a2acd-6bae-3ec9-b01a-42a141045721 | -11.45418 | -54.09486 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eef50af6-31be-302f-8f4f-1f12fdf9cc29 | -11.47925 | -52.91705 | 2026-05-18 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5cfe284-f0d3-34e0-8d2c-3c25bc7f6266 | -11.4464 | -54.10082 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84cadeaf-5abe-35f4-ad80-c66e4128f6d3 | -11.84692 | -43.96756 | 2026-05-18 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b37b06fc-2ce6-3775-bd72-a920d4054e3c | -11.8474 | -43.9637 | 2026-05-18 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 52f6f566-cdcd-33b2-805b-f1027d089cc7 | -10.40898 | -44.93708 | 2026-05-18 05:01:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
