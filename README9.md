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
| 9b48eabc-3893-36ae-bdac-19f4c41dee7d | -17.71618 | -46.78046 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6296b03-8738-3f48-8e38-4f1db34fa566 | -22.78934 | -49.34848 | 2026-06-30 04:23:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 636979ba-9882-33b4-ae3a-7e08725d3ba4 | -16.20175 | -59.32056 | 2026-06-30 04:23:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3102d726-fc41-31a5-b3dc-a4db0d29ee56 | -20.97213 | -49.74677 | 2026-06-30 04:23:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a6985153-d036-310b-985e-4bc5af98546f | -19.85948 | -46.37473 | 2026-06-30 04:23:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96f3d4cb-bcda-34df-8fef-03b30917e8b2 | -22.78995 | -49.3447 | 2026-06-30 04:23:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74a41b26-eae4-3473-93d6-4bef407dfe32 | -17.44219 | -47.16644 | 2026-06-30 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee07af2c-1e60-35c6-baba-437f0555f72c | -18.24681 | -53.85155 | 2026-06-30 04:23:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f95c9559-3506-3ce1-ade8-1a931889f20f | -17.91184 | -52.7217 | 2026-06-30 04:23:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c1a7912-8ddd-3477-bf78-c4b574216d4f | -22.80446 | -49.33968 | 2026-06-30 04:23:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fccc25a-354b-3597-a6c1-62813fe16ff8 | -18.24272 | -53.84269 | 2026-06-30 04:23:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04e881e4-f320-378b-a24f-846d3a4dccce | -17.91256 | -52.71789 | 2026-06-30 04:23:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20320ded-da4d-3d1e-bc9f-1d6bbbb14386 | -20.78206 | -42.75164 | 2026-06-30 04:23:00 | NOAA-21 | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 78a9461c-2331-3f9c-b79a-e915ae740ce6 | -17.71562 | -46.78407 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0040b83-f51f-33f5-934e-7f7f3f18c7a5 | -22.79328 | -49.34533 | 2026-06-30 04:23:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb4eca00-23ad-3eb4-85e5-d17363f8df84 | -17.70901 | -46.78295 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b1453608-438b-3101-bcc7-1fb6b95377f2 | -17.43889 | -47.16588 | 2026-06-30 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 01bbe0db-e91c-37b6-9bff-8ecb215d2879 | -18.24337 | -53.8461 | 2026-06-30 04:23:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 65ef8410-3860-3ac3-9f02-f8081fb9b787 | -17.79016 | -42.51305 | 2026-06-30 04:23:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8d98c9f3-d6a0-31a2-b6b6-e0e71cb581f1 | -16.19546 | -59.31903 | 2026-06-30 04:23:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0824804f-4b85-3223-8aab-08e278673569 | -18.24768 | -53.84706 | 2026-06-30 04:23:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87daf000-f562-3ae6-91d6-c721c97cb1dc | -17.71012 | -46.77573 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49153e05-71de-379a-8f04-673bed0af12e | -21.31536 | -48.5402 | 2026-06-30 04:23:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84e92fef-2158-32d2-aa7c-adbd483a949a | -21.53421 | -45.06865 | 2026-06-30 04:23:00 | NOAA-21 | SÃO BENTO ABADE | MINAS GERAIS | Brasil | 3160801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1449ab90-90b3-3595-a7ae-73240021bb59 | -17.44549 | -47.167 | 2026-06-30 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7fd24c1-3104-3eb4-984a-3dd66d8799fc | -19.74073 | -44.00261 | 2026-06-30 04:23:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 286ef24b-0060-373b-83cb-52ba6e70ab42 | -22.78663 | -49.34408 | 2026-06-30 04:23:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfbd4baf-0e75-3d32-bf25-a78df7666113 | -22.79266 | -49.34911 | 2026-06-30 04:23:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5abad293-f331-374a-b182-810e6de8f612 | -17.44275 | -47.16285 | 2026-06-30 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 84e3a485-3ceb-3f7a-b3d5-8ff96775b970 | -10.9401 | -43.0355 | 2026-06-30 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 839fb88c-d71a-3e09-98d2-45cbf47d4d75 | -10.9397 | -43.0593 | 2026-06-30 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 26bdb5e2-df85-3d63-85d6-4f689202cb26 | -10.9209 | -43.0384 | 2026-06-30 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 64632387-b8f5-377d-9d88-7a493e9230af | -10.9593 | -43.0326 | 2026-06-30 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 3766f27b-d6a5-327f-a98f-0cb708aed165 | -10.9405 | -43.0117 | 2026-06-30 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 0002125e-7680-3f49-b64a-b86ca39f6190 | -10.9401 | -43.0355 | 2026-06-30 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 217.1 |
| d2e7c0eb-f420-3263-b184-d4112db42129 | -10.9593 | -43.0326 | 2026-06-30 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 75d57bea-56f0-3c8d-af4e-71b228ef2a2e | -10.9397 | -43.0593 | 2026-06-30 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 83b59f0a-bed5-335b-a5e1-79924f9b85b3 | -10.9209 | -43.0384 | 2026-06-30 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ac627b96-eebd-3ec7-985e-b9650f9f0844 | -10.9397 | -43.0593 | 2026-06-30 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 0bbe0a4a-e3c7-39fe-95ff-a2d37824ea50 | -10.9401 | -43.0355 | 2026-06-30 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 292.3 |
| f5cf1206-bd89-3384-a463-57ad7dd79998 | -4.8442 | -42.92826 | 2026-06-30 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a489af24-14b8-3c9b-8058-9c65f6ef7b00 | -9.74914 | -49.02837 | 2026-06-30 04:55:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff1128e9-2cd9-38e0-b9c3-a93f031acb26 | -9.32938 | -58.01443 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23f16b39-e64f-3e32-9603-363d29c422f9 | -7.63769 | -50.02744 | 2026-06-30 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe38c9bf-b626-314c-a099-8367d5b88315 | -10.2996 | -57.12574 | 2026-06-30 04:55:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d65e9030-d108-314c-9bc5-5c071891cb8b | -8.70686 | -50.71226 | 2026-06-30 04:55:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbcd4d71-bf2b-3f79-8444-f781f7062310 | -10.78488 | -54.10551 | 2026-06-30 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc917fcd-0be4-33f3-a54f-15d89cbac197 | -9.81539 | -46.47215 | 2026-06-30 04:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afa5c617-fd0d-3574-9db6-9dab7f03c52a | -6.9212 | -51.94608 | 2026-06-30 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f53a82f-67e2-3ac2-a8dc-14d86a38bd99 | -10.12623 | -52.41174 | 2026-06-30 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbd92907-95a7-3ecc-9295-c702a89a6648 | -9.17123 | -58.06888 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbef4698-f4b5-30d0-9f7f-9f2663f6ab3d | -6.89982 | -43.69109 | 2026-06-30 04:55:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60cddcec-49c4-3302-ae11-471cb7a6a624 | -6.50079 | -42.23697 | 2026-06-30 04:55:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8fa011e2-a9c2-3a07-9502-23363bd9c8fa | -10.3815 | -49.5943 | 2026-06-30 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81d50bdf-7e30-3713-a249-cb20abfc3423 | -9.12685 | -58.26739 | 2026-06-30 04:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a2b226a-7008-3b2a-8c7e-1b7970fe34f1 | -9.19038 | -46.63406 | 2026-06-30 04:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03a22065-9885-36b6-abd1-c0adffb4c0c8 | -8.98865 | -45.72684 | 2026-06-30 04:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8db1fbf2-f17a-302c-8ce1-652d7276ae43 | -10.38503 | -49.59484 | 2026-06-30 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad1510d9-134e-3fea-9c99-93e8b1a3a953 | -10.94159 | -43.04911 | 2026-06-30 04:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 116a51d9-cd1d-3448-830d-6bd1b1e6a7dd | -9.19854 | -45.32454 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43f9c6bc-eaff-3448-bd04-3ce7ac8dba37 | -11.91727 | -43.39395 | 2026-06-30 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 97f99c2e-334b-304a-a745-c369baee5b77 | -9.32216 | -58.03022 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f28657b2-3fde-3e60-9b53-3d63b45301dd | -9.2 | -45.32661 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fd2f561-93f3-38b6-bdc6-d7f093c14c4f | -9.18509 | -45.32266 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c6468ef-21d3-3ad7-973c-1aca0f35633b | -9.60367 | -56.93499 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 17f74137-a2a6-3c2b-bba1-d3dd024e3c9f | -10.69653 | -49.6066 | 2026-06-30 04:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1b15e5c-f30c-3d27-b146-dd170a4d8fdf | -9.18893 | -45.32779 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5a650a3-ebcd-37e1-8122-e1ac5f69246f | -7.63826 | -50.0238 | 2026-06-30 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 753df405-7d3d-3cc2-bc39-f228b41c1069 | -11.91114 | -43.39996 | 2026-06-30 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6ac7075-e4db-35c7-b321-932226724ede | -11.91269 | -43.40055 | 2026-06-30 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aba2c17c-6832-3131-b26e-1d6191a0ecb3 | -9.75211 | -49.02624 | 2026-06-30 04:55:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c0835ec-5c73-3f81-bd4f-474095826b47 | -9.60089 | -56.9272 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3f4aa39a-35a4-34c9-9650-0ee5a55c8f9c | -10.13733 | -52.40635 | 2026-06-30 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abb73ba9-6174-32a2-a816-582913ef289f | -6.89907 | -43.69645 | 2026-06-30 04:55:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23377d6c-6bb7-3f73-b3e9-92701891af08 | -9.58949 | -56.92154 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd18926e-829b-390e-864d-6678f3dc310f | -6.69013 | -51.95984 | 2026-06-30 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15fe9c1c-6f42-3548-984d-2a213e4a8eef | -11.91888 | -43.39453 | 2026-06-30 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d6236c9e-521e-3fa3-9817-28a8104f8e5d | -10.7184 | -51.66433 | 2026-06-30 04:55:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6fd51ad-07b8-3146-b1a0-713882981e7a | -11.91687 | -43.39729 | 2026-06-30 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a50db382-8173-360e-b224-9d27962e05fd | -8.35692 | -46.82061 | 2026-06-30 04:55:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b916cb9-c498-3f50-942f-460f64dfbf9c | -9.6089 | -56.92863 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fa0412b0-e64d-37e5-b12d-c04d505ab334 | -9.60211 | -56.92017 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 04290c7c-c3e5-3bdf-96ea-63b50cb9d42a | -10.38563 | -49.59088 | 2026-06-30 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 581e6455-1001-306b-977d-4b8092f0139d | -10.71785 | -51.66787 | 2026-06-30 04:55:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96281621-edb3-36b6-815e-992ffd4c77d2 | -10.52909 | -48.15779 | 2026-06-30 04:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a5ee2cd-3d09-3b90-8ea7-1f62c00041ac | -9.91348 | -46.29531 | 2026-06-30 04:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e293351d-d0d6-3af7-bb8b-f8a57c87592f | -7.63487 | -50.02328 | 2026-06-30 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d85edb40-4410-349d-82f1-1b2b79e8139c | -8.20715 | -49.86538 | 2026-06-30 04:55:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fdef94d-5215-34c3-9165-06d1197c9d06 | -10.53289 | -48.15836 | 2026-06-30 04:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ce0c88c-ceb7-31d1-97ce-ae5ee43a8a2b | -10.93213 | -43.03752 | 2026-06-30 04:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e1a7236e-a8a6-3197-a05a-0672430699ff | -9.60169 | -49.32306 | 2026-06-30 04:55:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e293bc2-3af2-342b-83b3-e2dbd6b31db9 | -9.14314 | -58.25247 | 2026-06-30 04:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0389c59-d796-30e4-a7a4-43060385fa5c | -9.32649 | -58.03098 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4db0322a-61d5-3c5b-b6e0-9bb76afea8f0 | -7.47441 | -44.73634 | 2026-06-30 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04d3942e-dd0e-3fc2-a42e-efaa77e4d54e | -11.91844 | -43.39787 | 2026-06-30 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d2c6be65-6d8b-39d9-9c42-48ed62a07350 | -9.74493 | -49.02513 | 2026-06-30 04:55:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72ba9f38-8d42-3b14-8d5c-479ae6fd3a6d | -9.08535 | -59.39762 | 2026-06-30 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dce4bfdd-ca02-3042-b201-4dd12f761374 | -7.84852 | -47.16793 | 2026-06-30 04:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c560101-d4f1-3ab9-b705-b21c5d2e14c1 | -6.5066 | -42.23433 | 2026-06-30 04:55:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 963dc928-aadb-3074-89da-27c9cbd1cd4f | -9.32506 | -58.01364 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README10.md)
