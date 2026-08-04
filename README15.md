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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a65ee80-6e35-348b-93f7-8c3fe12a8adb | -9.24909 | -60.33338 | 2026-08-04 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abf3e9d2-547e-3136-8d96-23e722b4d56a | -11.21078 | -54.83907 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f6a0f3c-5610-34e6-8ff1-b561c3f78a31 | -11.20853 | -54.85434 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 541b4931-08f1-3f99-8c2b-0704ab47ba30 | -7.24119 | -59.45193 | 2026-08-04 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff1a7e90-05b2-3c76-bbb3-ee8c90b1fcb7 | -8.98466 | -51.47095 | 2026-08-04 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6754de84-9887-35e1-8fd9-5ab1210ca0b7 | -11.7577 | -50.28761 | 2026-08-04 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a92d9ec2-32f1-3620-b82b-11ce42df2719 | -10.58848 | -46.77736 | 2026-08-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4ccae58-4c16-3944-8ab5-e625b305232d | -11.20622 | -54.84617 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2a4087d-92ca-309c-a5c1-f35f9571a40e | -11.19311 | -54.8636 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 1b6ff8f4-d2e5-3c2d-9228-29a8766cc56d | -11.25433 | -54.83013 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06ede7cb-da88-3b50-85d3-6c5d2ea1919f | -11.21197 | -54.85487 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 292f2bbd-5878-3593-81a0-1a79249a67aa | -10.56837 | -46.7723 | 2026-08-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97101cdb-9c0f-3c66-9e24-8a6884e6ca2c | -9.12315 | -48.3748 | 2026-08-04 05:06:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fa1b76c-cc28-3724-8b6d-7a3107821981 | -11.21597 | -54.85159 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91f968c5-a13b-3efa-8a38-d813a10b9ff2 | -17.98398 | -47.16583 | 2026-08-04 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91d0b844-6258-3214-a40f-17adb8f67e6b | -20.88642 | -57.75145 | 2026-08-04 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| fd21b49e-5c4c-3a6a-ae5b-c7ef8dfd57a3 | -20.84213 | -57.76072 | 2026-08-04 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 65c5c1f9-66d7-3c09-96a6-30abfba9c8b4 | -20.4733 | -56.73041 | 2026-08-04 05:08:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fa543739-04e4-330e-bd47-47f55945099c | -20.83373 | -57.72403 | 2026-08-04 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3366c969-936a-3596-a49d-6a3260867e9e | -16.52881 | -49.21844 | 2026-08-04 05:08:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5eae1055-e1ab-33e9-80ff-439d2800a036 | -20.83875 | -57.76016 | 2026-08-04 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b65324c1-0420-3e6e-94a4-4e5914edf3b1 | -20.83711 | -57.72459 | 2026-08-04 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f6a1e465-1f2f-3256-a1c8-1dbb8edb8480 | -20.83983 | -57.79946 | 2026-08-04 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 549ccb0e-ac7c-351a-835a-c156bfd7b955 | -20.83762 | -57.7678 | 2026-08-04 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 323146d5-3d5d-32a6-838b-baab54fe2ec4 | -20.88304 | -57.75089 | 2026-08-04 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a3e38c19-a18e-34a8-aa2b-7604fb5cfef1 | -16.52845 | -49.22168 | 2026-08-04 05:08:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b5cedf2-a1e4-33af-9a9c-d01cfdcf9920 | -17.97848 | -47.15976 | 2026-08-04 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 037afa77-ba8c-34b6-a2e3-d7980802530f | -20.8404 | -57.79565 | 2026-08-04 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e7b447b6-5684-3651-a069-1a05a04daa13 | -20.83425 | -57.76723 | 2026-08-04 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cb83d59c-0936-397c-8a99-866308be0ae1 | -16.53362 | -49.22232 | 2026-08-04 05:08:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 048cedeb-bd71-3e3b-a807-d4ef8a1faed0 | -8.3544 | -45.9897 | 2026-08-04 05:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| a482ddc5-7ad5-3572-aa55-7b821c4e03d2 | -11.2211 | -54.8754 | 2026-08-04 05:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 0938f969-d5f4-3ea9-8fb0-95635ff677a1 | -8.3544 | -45.9897 | 2026-08-04 05:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 7a6f21e0-814e-368d-ad7b-a099b195daf3 | -11.2213 | -54.855 | 2026-08-04 05:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| cf9c6a41-fe48-3105-9294-5ec67c18e701 | -11.2213 | -54.855 | 2026-08-04 05:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 3b29352d-9886-376d-a9d8-36ae0389cf51 | -8.3544 | -45.9897 | 2026-08-04 05:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 78a76e02-c7ff-3d96-9242-2d44dd067ba0 | -11.2211 | -54.8754 | 2026-08-04 05:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| dd9799d2-47ce-3208-b449-63e9eabadc1d | -8.3544 | -45.9897 | 2026-08-04 05:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| fff4ee3b-3df5-39eb-8c4b-ca97c5901143 | -8.3544 | -45.9897 | 2026-08-04 05:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 12b7750a-553c-3137-ae3d-5ae5b6284fb9 | 1.16249 | -60.66835 | 2026-08-04 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c43df3a-2b05-3056-a652-37c88bc25e54 | 2.53882 | -60.36799 | 2026-08-04 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87b555e7-a630-3af7-8d31-7c930767dac9 | -1.63915 | -54.46544 | 2026-08-04 05:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e65dad43-89b4-3cb7-9012-0c9e6e1b1883 | 2.53814 | -60.36379 | 2026-08-04 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a736ca8-8886-37e3-8a23-7c67543b8745 | -1.63228 | -54.46441 | 2026-08-04 05:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0c93c4d9-4dd3-3930-b359-120ac4627c85 | 2.53376 | -60.36449 | 2026-08-04 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88b5b50f-fcf2-360a-9a7c-70cc4aab923b | -6.54752 | -55.15927 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2cd17e4a-06ab-3948-81f4-f9a0451e57c7 | -6.53962 | -55.16476 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62ec4293-136d-3aa0-8c61-9e38ca8ced9f | -6.53874 | -55.17124 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dca9abe6-945f-3500-bba9-1952065d9f0f | -6.53768 | -55.16588 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e34fafd7-f608-33da-81de-d3ba3edf8204 | -6.5668 | -55.17535 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1ab6964c-fcfa-31e1-b790-0a98265a7e60 | -7.24157 | -59.45255 | 2026-08-04 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcbc82b6-f5fa-3ef0-8a59-4d81872fdf88 | -7.27211 | -64.78129 | 2026-08-04 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fc9149d-71da-34ba-97e2-13148a63ecca | -6.57364 | -55.1644 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e46789d-f6e1-318e-8be3-87a57fa97e07 | -6.54052 | -55.15811 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f47317f6-9909-3c5c-a44f-fd8439db28f0 | -6.54575 | -55.17231 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21a99735-15c8-3a83-a127-3a40a7fe03dc | -6.55977 | -55.17445 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5529eef0-77eb-3755-9f50-4660dafa0430 | -6.74322 | -60.01917 | 2026-08-04 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd485225-3a01-318c-aae3-35b9d97626bb | -6.54383 | -55.17364 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f4ed94e-e31b-33a1-8e6d-d74892c0e8e9 | -6.55367 | -55.16672 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd6c1228-ec56-395c-91a7-b9e21c591f5d | -6.56156 | -55.16135 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d8808995-6e53-3fae-ba3d-514d859b05c4 | -6.53853 | -55.15926 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f285459-bc48-3aa6-87de-ae18665d4df5 | -6.54663 | -55.16582 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e14c1e0-0917-3663-83d6-192b4cb4e939 | -6.57277 | -55.17109 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b32dc83e-b150-3e90-b065-2efd85470871 | -6.55276 | -55.17339 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b1ae7496-fa25-37d0-99aa-98bd8374677b | -7.23614 | -59.4518 | 2026-08-04 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2eb3d5e4-a69c-336b-9472-02b6da9d725d | -6.55172 | -55.16795 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7efd92f2-fcad-3800-ad35-a7fd9f184372 | -6.57451 | -55.15774 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f7cf06c7-ea2e-327e-a1d6-877057107aae | -6.56067 | -55.16784 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60c31b8a-dd37-3724-93b1-b41314f19374 | -6.55785 | -55.17581 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39f8540c-bc35-3ad4-bb79-0c494c1eccaa | -6.54552 | -55.16054 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46293911-4d00-3c18-85b6-714b34a08c15 | -6.57472 | -55.16979 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b34f82b6-dad7-3c17-a6ee-e7d7adb95467 | -3.92613 | -59.4045 | 2026-08-04 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0293ceb4-c3d9-35a4-9b75-d4a824272277 | -6.53155 | -55.15787 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22bdd030-0159-3079-9952-ada9f6a7c546 | -6.56861 | -55.16214 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ef9a16b-a9d6-3eb2-9860-5468137ddbf4 | -6.55257 | -55.16139 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c39ec961-e31f-3df4-8aa3-f4082922fd34 | -6.56487 | -55.17675 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3152999-d1bb-371a-9bf7-6583f4425a16 | -8.63598 | -63.77612 | 2026-08-04 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0dd2a98-5bd7-382b-9732-5663e5f4718d | -3.92566 | -59.40762 | 2026-08-04 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb29551b-56b4-308e-9c8d-5c72ed103d58 | -6.55873 | -55.16905 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5992bea-ce2c-3d80-b578-015119a2f1fc | -8.78 | -63.6425 | 2026-08-04 05:59:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbc4a71c-a742-36de-9b1c-5d41087836b6 | -6.53263 | -55.16351 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09837b86-551b-3857-b096-54474b8b3491 | -6.56575 | -55.17007 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c57be5a1-6a50-37b9-b6a8-6cb335c8e355 | -6.5666 | -55.16353 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 988c17ec-0c5f-33d6-abce-d3ab7e3b2565 | -6.5677 | -55.16874 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3bc9b3e-3e32-3521-ac7b-9766324dbea5 | -7.23566 | -59.45525 | 2026-08-04 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 062921a1-d7ab-36e6-867d-3f592f8f6211 | -6.54469 | -55.16699 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7efa4c71-8693-3d3e-a54d-883beb977061 | -6.57564 | -55.16306 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01dd4c10-c886-33b9-9210-cd57cd5c3ae0 | -8.94896 | -62.05536 | 2026-08-04 05:59:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19e0feff-f524-3ee9-bc0e-b4d54f4150dd | -6.74797 | -60.02289 | 2026-08-04 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c42e767-f165-34e2-b800-1de02e6d0c32 | -6.55084 | -55.17474 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e85f99e0-848e-31e4-bb38-07b6a271f461 | -6.57655 | -55.15643 | 2026-08-04 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 24bb29dc-3ede-34c3-b071-17382e0af72c | -8.3544 | -45.9897 | 2026-08-04 06:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| d486d1e0-8ad8-3019-824c-3f8ab05b5fcd | -12.02373 | -63.08814 | 2026-08-04 06:01:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7942e3a3-c95e-3bd6-8812-53ceb6f99334 | -10.92379 | -69.57484 | 2026-08-04 06:01:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9a06bf9e-ad5b-37d3-8baf-0347338bc7b8 | -10.81875 | -65.09327 | 2026-08-04 06:01:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3b1b4b1-b564-35ef-ac5b-096ae93ba492 | -11.91356 | -64.95787 | 2026-08-04 06:01:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2be78fd-789b-3004-a63c-7a2738d0412d | -10.82194 | -65.09881 | 2026-08-04 06:01:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e5bd0a7-e9f4-3d77-a7fe-f139317ce5a8 | -8.35709 | -45.98272 | 2026-08-04 06:08:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 7ffff1bc-5038-3462-b008-f3ceefd7f83b | -8.357 | -45.96866 | 2026-08-04 06:08:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 17290ad9-14c1-3e45-87b3-7b7ce72e6a7e | -8.3534 | -45.9894 | 2026-08-04 06:08:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |


[Clique aqui para ver as próximas entradas](README16.md)
