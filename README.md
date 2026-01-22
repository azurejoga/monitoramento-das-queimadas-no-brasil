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
| 2af5a661-5ac1-3532-9685-fc284c319de4 | -1.2384 | -53.6967 | 2026-01-22 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 79ba631d-b8fa-3eea-8962-656444635559 | -10.0865 | -36.1782 | 2026-01-22 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 63.3 |
| 6e74441d-e023-3c12-bf9c-1c67ac562a2a | -1.2384 | -53.6967 | 2026-01-22 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| fd4cd70e-db44-3515-a6cb-ede0dcf1fa60 | 3.3485 | -60.1148 | 2026-01-22 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 3fdc56c7-1acb-352f-a785-2e539f1866f9 | -1.2384 | -53.6967 | 2026-01-22 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 90024c25-1d62-3af7-8207-561fe7972398 | -9.9467 | -36.4455 | 2026-01-22 00:20:00 | GOES-19 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 58.2 |
| eb68dbc1-1d7b-398d-a6f6-41bf947f0a4f | -9.737 | -36.3477 | 2026-01-22 00:20:00 | GOES-19 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.4 |
| a3f788b1-2b32-3f28-b5a7-f9ad062af144 | -9.9299 | -36.3141 | 2026-01-22 00:30:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.8 |
| a15383aa-46c4-31a2-a73d-de5b0d8df21f | -1.2384 | -53.6967 | 2026-01-22 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d2ab1086-de59-342c-8f86-acdfce1a79ea | -1.2384 | -53.6967 | 2026-01-22 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 67a28888-9d12-3538-98ac-2ce35457e2b9 | -7.6859 | -35.1779 | 2026-01-22 00:50:00 | GOES-19 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 49.6 |
| d34a5bca-1788-3c60-ade4-10884d33ee40 | -1.2384 | -53.6967 | 2026-01-22 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 63e44cec-10d5-39a0-913d-9d7d40989bcf | -1.2384 | -53.6967 | 2026-01-22 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| b9d7aeee-1c33-3797-a66c-650219498d85 | -9.7043 | -36.0296 | 2026-01-22 01:00:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| c7ddecb0-faf1-3982-b0d9-5bbd4aa1b304 | -7.6859 | -35.1779 | 2026-01-22 01:00:00 | GOES-19 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 81.6 |
| 81b781ab-53b3-3e89-8f64-a87dd71b2885 | -9.7236 | -36.0263 | 2026-01-22 01:00:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| c9a082ad-786e-3156-b46a-db255b2d665e | -29.30528 | -55.08887 | 2026-01-22 01:21:00 | TERRA_M-M | SÃO FRANCISCO DE ASSIS | RIO GRANDE DO SUL | Brasil | 4318101 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| def3ce39-570b-3fb8-a76e-b2fcaa12a573 | -20.34429 | -57.88449 | 2026-01-22 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| d4035298-59a8-3d6e-ae96-038824ac74c7 | -19.68538 | -56.88857 | 2026-01-22 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 4724c75b-5e94-3797-a479-e8f8643e3537 | -19.63313 | -56.97893 | 2026-01-22 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 30.5 |
| 1a04e462-f17d-39da-a3bd-05582d1d87e2 | -19.6276 | -56.98558 | 2026-01-22 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 31.2 |
| 9e90a615-8ec7-386d-b02d-f2df5b4d3fc9 | -20.31864 | -57.87984 | 2026-01-22 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 92af1d72-258d-3f56-835c-eb54011fa1e4 | -19.67161 | -56.98949 | 2026-01-22 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| abd16e7c-5175-38a1-8a88-b6094724d98f | -19.66517 | -56.88079 | 2026-01-22 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 23.4 |
| 9729cb85-2f66-334c-a1d2-36f6063fd2cb | -19.68012 | -56.89629 | 2026-01-22 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.0 |
| ca86115f-2c70-3a11-b2ba-acac9c81aebd | -20.35519 | -57.88238 | 2026-01-22 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.3 |
| dacc491b-daa9-3eaf-a3e6-cf9c2437b218 | -20.31996 | -57.87389 | 2026-01-22 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 46577d51-4b6f-3b7a-8a72-13197a3ee275 | -19.67707 | -56.87841 | 2026-01-22 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 24.5 |
| ba34e270-5a0f-3790-b385-1fdf51d27f4d | -19.6631 | -56.8912 | 2026-01-22 01:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 3f3b96c4-8039-37a8-a224-f665f3985314 | -19.6832 | -56.8884 | 2026-01-22 01:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 50.4 |
| 05ac0215-98e3-3153-a98b-de826ceed055 | -19.6631 | -56.8912 | 2026-01-22 02:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.2 |
| 27583f80-dac1-3377-91b7-2714777c7942 | -19.6418 | -56.9569 | 2026-01-22 02:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 49.5 |
| 657d4e5a-2999-39fb-9067-55fe285cd60f | -19.6213 | -56.9806 | 2026-01-22 02:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 66908efc-5a6b-3ac6-ab18-a57c492dfacb | -19.6414 | -56.9778 | 2026-01-22 02:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| a1bffbd8-701f-3dd9-8248-47c02535f3f2 | -20.3489 | -57.8615 | 2026-01-22 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 67e77c4e-1ebd-3623-ac87-f53f3a851e31 | -20.3687 | -57.8796 | 2026-01-22 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| f7e34ff5-1bc7-3585-b923-79b54ad04c7a | -20.3485 | -57.8824 | 2026-01-22 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.4 |
| 4735a4d7-2646-3e68-acfa-fe907e4218fd | -20.3485 | -57.8824 | 2026-01-22 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.8 |
| a3f651cc-582b-3e4e-8ba7-1432c46304a1 | -20.3687 | -57.8796 | 2026-01-22 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 56b946a6-1bf5-34bc-9e21-2f598b0f99c4 | -20.3485 | -57.8824 | 2026-01-22 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 58e5b684-39fc-327e-88f7-c5c3f666842c | -20.3489 | -57.8615 | 2026-01-22 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 10b51eb6-adf1-3866-9c28-2b303ecb02ac | -20.3485 | -57.8824 | 2026-01-22 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.8 |
| 6119c567-fa48-384e-9016-a0fdaa20d2d4 | -20.3687 | -57.8796 | 2026-01-22 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 7c9fd3e5-1a6c-34be-b496-ebb426207f82 | -7.7409 | -35.20798 | 2026-01-22 03:12:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 05137b6c-2fb3-30f2-a0a9-170d87534b11 | -7.74001 | -35.21317 | 2026-01-22 03:12:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 43dfe5e9-f2a7-3a1d-8e80-576da8feb6d4 | -9.67371 | -35.85548 | 2026-01-22 03:12:00 | NOAA-20 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 20556380-9f03-37ef-8063-dafdbd68e93c | -7.74124 | -35.20839 | 2026-01-22 03:12:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 568e0cad-8226-3646-a2a1-5464648701b3 | -9.67269 | -35.85755 | 2026-01-22 03:12:00 | NOAA-20 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 89730c7c-cab8-3d31-8968-01ea3de8d649 | -6.25991 | -35.26987 | 2026-01-22 03:12:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| e4518384-eef8-38fd-a291-50f8b5267a39 | -10.26957 | -36.50225 | 2026-01-22 03:12:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d33bf8fa-fb63-3ea8-9be2-565b37835e54 | -12.78025 | -38.50222 | 2026-01-22 03:14:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fbed9363-d455-3f4c-9677-918d6c2b0873 | -12.78096 | -38.49863 | 2026-01-22 03:14:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f68c41b4-3625-3c25-916d-267b087f4310 | -20.3085 | -57.867 | 2026-01-22 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| a55e7a8e-cae5-3e39-9aeb-c2aea7a47928 | -20.3485 | -57.8824 | 2026-01-22 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.3 |
| 80723f1c-18ff-3595-b9f0-32bafb7a7b00 | -20.3287 | -57.8643 | 2026-01-22 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 772b301b-b998-3414-8609-054d63497448 | -20.3687 | -57.8796 | 2026-01-22 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 7c83fdd2-52c1-3e58-adc1-175f8bb3b3a3 | -2.69412 | -45.61704 | 2026-01-22 04:01:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2a4f94d-0114-340b-9309-a982fbe677d6 | -9.1795 | -36.96544 | 2026-01-22 04:01:00 | NOAA-21 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6e18c948-b89d-3ce6-aa99-a404400bf816 | -5.90638 | -39.14777 | 2026-01-22 04:01:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b7917a2-6b40-3d50-a4f8-cf170e7400a3 | -2.69388 | -45.61861 | 2026-01-22 04:01:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a669881c-5c2b-35f8-8590-4850b4fdc8e0 | -4.35636 | -40.39593 | 2026-01-22 04:01:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2bd9dc59-4ea6-38b6-ac77-93f58f0142d1 | -2.51959 | -47.81501 | 2026-01-22 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14354654-ed08-3fb5-b9d2-3afe4b237211 | -3.60317 | -38.92942 | 2026-01-22 04:01:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65075952-726a-323d-9c98-e24535f90271 | -5.24629 | -38.57716 | 2026-01-22 04:01:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 86a1a140-6dba-3927-a552-f205d37ecdd2 | -2.51444 | -47.81422 | 2026-01-22 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f19cc41b-ae58-3f90-9e1e-d094501f031f | -7.48956 | -34.92492 | 2026-01-22 04:01:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2033981f-0e3d-3cf7-8985-6f6b34dd34fc | -1.67768 | -45.79873 | 2026-01-22 04:01:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40b3bb00-fffa-35ee-808b-8c220761f682 | -4.39579 | -37.92128 | 2026-01-22 04:01:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 16c9b78e-a3e3-31c7-80cd-f6bc754838d2 | -4.39394 | -47.08291 | 2026-01-22 04:01:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b635925-ffa9-3ad7-b089-c56e656a8d2d | -3.60648 | -38.92993 | 2026-01-22 04:01:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65a61b63-c98f-30ba-8dba-e19bb5a8b175 | -4.86425 | -39.00297 | 2026-01-22 04:01:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9f0cb7e8-fd78-35ff-a57e-cfe059bfa1f2 | -4.90858 | -37.41449 | 2026-01-22 04:01:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9d2b782a-3c48-36e1-867d-75120f6ec784 | -7.96272 | -36.07158 | 2026-01-22 04:01:00 | NOAA-21 | TAQUARITINGA DO NORTE | PERNAMBUCO | Brasil | 2615003 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f82a1873-e8d6-355d-be85-4604b4b3f159 | -5.77673 | -38.68763 | 2026-01-22 04:01:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5d33de64-3c36-385b-b95b-6ef91e42e7fa | -12.7825 | -38.49776 | 2026-01-22 04:04:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b2a59a54-9958-313d-b48f-79bdce748143 | -12.2909 | -38.9175 | 2026-01-22 04:04:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5e2d440c-ca15-3882-b7d9-dff97c36149b | -12.21172 | -38.98309 | 2026-01-22 04:04:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f4538107-f934-39ce-99eb-7e7d14af3df7 | -19.63878 | -56.96526 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 7d39ccc5-8c2b-3731-8972-66eba8fffd65 | -21.94373 | -52.91171 | 2026-01-22 04:06:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04c11294-5e56-3347-8e28-7dcd41c27e91 | -19.66838 | -57.00058 | 2026-01-22 04:06:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6ea5a7e0-eb95-3518-a96d-940cd32f6412 | -19.67928 | -56.88314 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7eae3ca7-eaa4-3545-ae06-590991e71e90 | -19.32183 | -54.02615 | 2026-01-22 04:06:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2aa7edd0-c6e7-34dd-a8b8-90d9c076f80e | -19.13494 | -54.53935 | 2026-01-22 04:06:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f15cfdd-b9b7-31b2-8a18-309042899bfc | -19.63457 | -56.96528 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| f53b78c4-35f9-3d19-9eef-e1e8e1efe537 | -20.34525 | -57.87864 | 2026-01-22 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0e0f2e47-d0f2-3981-b37f-ec9b9c93bf7b | -19.34396 | -54.17596 | 2026-01-22 04:06:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be4e9565-ce54-3850-bd6c-57dd85218495 | -19.32757 | -54.02721 | 2026-01-22 04:06:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00775056-2d91-35a9-81e7-c4e1665504f8 | -20.3271 | -55.92959 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d5d4770f-91e8-3b24-b5cb-7807898053d0 | -20.35212 | -57.8805 | 2026-01-22 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 16c2b829-f547-3829-9612-485e26810964 | -19.63304 | -56.97155 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 64876e83-4cd5-3e91-915f-1cd69c7a3087 | -19.62766 | -56.98235 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 8bec9682-2b12-3655-a586-b0bd9c70e84c | -20.9126 | -56.38628 | 2026-01-22 04:06:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31e47718-c838-321c-90ea-dccf3fde95d6 | -19.66904 | -56.88157 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b73db3df-53c3-3288-ab22-e8a2c9d98ad3 | -21.6189 | -46.92353 | 2026-01-22 04:06:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ee1f1fc-ea27-3e43-8972-baf6cd87a5d1 | -19.35336 | -54.67468 | 2026-01-22 04:06:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 219b8d0e-35e0-378a-ae9e-54bf5cfd3909 | -19.32846 | -54.0231 | 2026-01-22 04:06:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6acc624-2e8c-3f59-b57e-e06abbe4c342 | -19.63151 | -56.97782 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 05408d25-3c6f-3611-aa68-502c6d0df0ba | -19.67801 | -56.98996 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9f09994c-b37a-3d37-8a84-23f69b22d027 | -20.32957 | -55.93069 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2afc1157-ddaf-30ef-8f4d-4e4e253458f6 | -19.67268 | -56.88138 | 2026-01-22 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README2.md)
