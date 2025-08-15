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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 956ac087-d1e6-3042-b25f-be9d337f2750 | -9.1706 | -59.6762 | 2025-08-15 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| cc483b74-6dd9-30ce-9282-d01db07e7559 | -13.4759 | -56.6537 | 2025-08-15 06:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b5b86de2-eee0-3bcc-8e6a-924094691939 | -9.1892 | -59.6752 | 2025-08-15 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 0b4c524d-c04f-3f43-a21a-ab4e950060b7 | -9.4994 | -60.5278 | 2025-08-15 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| d533649b-93f8-358f-814c-e43e1024df7c | -13.4566 | -56.6757 | 2025-08-15 06:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 70321801-18f4-3bbb-ae5b-7776525dcb09 | -5.455 | -60.1391 | 2025-08-15 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 853ecd93-aa76-3eb3-9d00-f5b271b07e58 | -9.1708 | -59.6568 | 2025-08-15 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 981b927c-675f-3024-ae72-06643011e7a5 | -6.9302 | -59.5497 | 2025-08-15 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| e57e1af4-3b08-394f-a5c7-af96e27d51c4 | -6.0807 | -59.9465 | 2025-08-15 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 7a088e52-561b-3dd0-84e1-57a69ee3fdc8 | -6.9303 | -59.5305 | 2025-08-15 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| dbffad89-ed75-3219-8f3b-b869473b62e3 | -9.1894 | -59.6558 | 2025-08-15 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 62a2116b-6373-346d-9382-62ce3b6e945d | -5.75786 | -46.67672 | 2025-08-15 06:01:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ec321b46-db27-3ec1-bc91-4f2e14f0c547 | -2.38413 | -47.65838 | 2025-08-15 06:01:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a3cbdf32-1029-3266-a05c-2cef37c3631b | -5.75935 | -46.6663 | 2025-08-15 06:01:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| d3d6da00-9a2f-3530-8672-9a03f042ae9a | -3.43205 | -49.03894 | 2025-08-15 06:01:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 74079758-d297-3989-ba8e-22cbf4d367e2 | -3.43073 | -49.0477 | 2025-08-15 06:01:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 07e494e5-eeb6-381b-b4be-54901a074f50 | -3.42194 | -49.0464 | 2025-08-15 06:01:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| af324aa2-e0d6-3202-9afc-b2e49872d477 | -4.58927 | -43.31694 | 2025-08-15 06:01:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ffe1953f-c367-3b2c-9b54-3ecc5604c2e8 | -4.59628 | -43.30752 | 2025-08-15 06:01:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e807ce37-5a92-330b-8457-738447ed96dc | -2.90541 | -48.30213 | 2025-08-15 06:01:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7b685cae-0498-38a1-a89d-64addc12f6b6 | -4.22266 | -47.21382 | 2025-08-15 06:01:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 88a3837f-72f8-34e7-a9a2-b7a4e6da632c | -5.75612 | -46.65916 | 2025-08-15 06:01:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4f591665-d6c4-37a7-9871-dd90bf214c9b | -5.75458 | -46.66959 | 2025-08-15 06:01:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8d8d64c8-6581-3075-ac3d-c2c60f207307 | -8.31068 | -45.01918 | 2025-08-15 06:03:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5df38954-16ed-3674-8524-fb6f08cb21fd | -9.18676 | -45.33349 | 2025-08-15 06:03:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9685fb69-1d6c-38c1-80c2-cdd4dc6a5895 | -6.9328 | -59.54309 | 2025-08-15 06:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 8ef6cec0-06cc-330e-8f28-de2a53704b21 | -11.3441 | -55.40768 | 2025-08-15 06:03:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 5803b0c0-8c14-3a50-8fae-dbc1e64155a9 | -7.07463 | -59.22227 | 2025-08-15 06:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| c0dcea50-a11d-3d42-adb3-ebc102bb9fb2 | -12.59266 | -46.96343 | 2025-08-15 06:03:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d88d06f1-98ef-3bdc-9507-d49c882a2125 | -9.7245 | -48.02804 | 2025-08-15 06:03:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7dd3448e-7b79-3c4f-bf7c-45cec4c2fd14 | -7.8593 | -48.2319 | 2025-08-15 06:03:00 | AQUA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 93b61c5f-f065-3155-af95-d1315b60b9d6 | -6.93967 | -59.50445 | 2025-08-15 06:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 091a57df-fe0f-302f-8285-9f4352313d47 | -12.58233 | -46.96238 | 2025-08-15 06:03:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 39ca87a3-32d8-3d01-b5d2-1a0d94e14ab1 | -11.34148 | -55.42301 | 2025-08-15 06:03:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 781b57e8-93ca-3bec-9746-cff7f98a404a | -12.75858 | -44.4124 | 2025-08-15 06:03:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| a296bf22-602a-37ff-a66d-61f11685cece | -9.50218 | -60.51952 | 2025-08-15 06:03:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| c7252f9f-8c8d-3983-bf35-e056c87f15df | -6.88822 | -59.14183 | 2025-08-15 06:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 49940f66-9521-343f-83a2-e66aaa9febf7 | -9.18869 | -45.31905 | 2025-08-15 06:03:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 4a6906e1-8a71-386f-90f3-bb78831a5d14 | -11.35278 | -55.42481 | 2025-08-15 06:03:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 0a44b9ae-df79-3fae-9b98-ed985231d33b | -12.58575 | -46.93719 | 2025-08-15 06:03:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 139b1f8d-4881-3f9f-924b-8318598d47a5 | -6.92792 | -59.53728 | 2025-08-15 06:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.9 |
| c8d88fce-2d49-39f4-b3c8-9fdc6d3d8367 | -6.68979 | -58.84146 | 2025-08-15 06:03:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 322b8a10-560f-3c5e-8ace-0f309629b2fc | -12.57551 | -46.93533 | 2025-08-15 06:03:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 42ae7096-20b6-31eb-b6cd-a13c5529ef61 | -11.35537 | -55.40955 | 2025-08-15 06:03:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 03ad6903-dbad-3467-90b0-db21e59f96c7 | -9.16241 | -59.67242 | 2025-08-15 06:03:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 9e1b85ab-2d62-3ca6-91c7-c3668366685e | -6.69694 | -58.83799 | 2025-08-15 06:03:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 4a2a0a96-ef68-3efc-8dbb-86c30256c653 | -7.86066 | -48.22256 | 2025-08-15 06:03:00 | AQUA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e502c481-6de4-3f5b-803a-341155a12975 | -7.08487 | -59.19498 | 2025-08-15 06:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 27ff6a71-a484-348b-8e11-b69b90ba824f | -6.90619 | -45.20559 | 2025-08-15 06:03:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 26f1fc3d-7a86-3cca-a9cd-24b143dd93c9 | -11.34444 | -55.40196 | 2025-08-15 06:03:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| f1d10cee-1c7c-33b2-abe3-ac734df59b22 | -9.50488 | -60.52481 | 2025-08-15 06:03:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 54ffdff3-89a9-3671-8c17-f785e5b251d6 | -6.96144 | -42.86734 | 2025-08-15 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.6 |
| 5016aac9-9856-3f87-a8db-0c3c074035d0 | -12.57379 | -46.94805 | 2025-08-15 06:03:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2b4f7fdb-9b2d-355f-97c4-1d11ce946100 | -6.69572 | -58.80764 | 2025-08-15 06:03:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 276b6c6f-0cb0-3477-aa84-6148b2423c49 | -8.31269 | -45.00433 | 2025-08-15 06:03:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| cac46fd3-d945-3447-b996-5169833f208c | -11.34194 | -55.41731 | 2025-08-15 06:03:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| f4fd9548-e76a-3d51-b3c8-0bf8460ed241 | -12.58402 | -46.94993 | 2025-08-15 06:03:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 4bcf23ec-69d2-3a2c-94c9-e84f5b564591 | -6.93449 | -59.49883 | 2025-08-15 06:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 6287e954-af50-3247-b724-ccb19ab3b9ae | -6.70262 | -58.80406 | 2025-08-15 06:03:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 47591935-8337-3b36-8611-b755b0142377 | -9.15505 | -59.66599 | 2025-08-15 06:03:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 873b91fe-1fe0-3013-bb47-5d3023f60cc5 | -15.38659 | -55.7777 | 2025-08-15 06:05:00 | AQUA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| e831a411-bd3f-35b8-a27b-61581b81f505 | -15.89126 | -50.17555 | 2025-08-15 06:05:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3063cc12-d572-3c39-9215-a9fefca584f7 | -13.47528 | -56.66021 | 2025-08-15 06:05:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 08cb71ed-fd09-347e-b15a-6952f751ccd7 | -14.06071 | -46.29439 | 2025-08-15 06:05:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a8796535-33db-38d0-91be-f413fa719ea0 | -13.31401 | -45.22048 | 2025-08-15 06:05:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| c58a85ef-844c-398a-a949-681c3ef01333 | -15.89261 | -50.16616 | 2025-08-15 06:05:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 410134f2-d2be-3aa8-b5a5-81a802c87d42 | -13.46031 | -56.6754 | 2025-08-15 06:05:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 2de2653c-14c7-306d-b8bc-96e1ea5fe49c | -14.06786 | -46.3255 | 2025-08-15 06:05:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ff536c9d-c4f9-3f11-8f67-68f7d7ff9e9d | -14.06981 | -46.31072 | 2025-08-15 06:05:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 09e67287-cb04-3788-809f-10a1f89f74f1 | -13.46337 | -56.65792 | 2025-08-15 06:05:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 215.2 |
| 02d43a40-e477-3253-9673-c02105b5977f | -16.30022 | -52.91496 | 2025-08-15 06:08:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4e73450e-0233-3dd3-b203-b7650b2b7ece | -16.47258 | -51.97899 | 2025-08-15 06:08:00 | AQUA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dc4b2686-0ca7-3cf0-98e1-90dd721b7213 | -16.29868 | -52.92469 | 2025-08-15 06:08:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 7833bd52-9d4c-3b58-9ea9-a530f13512d1 | -16.37611 | -50.89729 | 2025-08-15 06:08:00 | AQUA_M-M | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d2d38481-daec-3a40-8706-7904597c5c0b | -5.92252 | -59.92577 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3107547-0dcb-3920-9569-4fc196d6f8ad | -6.08215 | -59.95433 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fa3baf6c-2852-3666-8f3d-5b74ec13d436 | -5.45329 | -60.13299 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b6f47ff6-1761-3465-ba38-666fd53fa741 | -6.72615 | -58.82679 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b022641b-1ce7-3a20-884b-9e335fc3eac8 | -6.07852 | -59.93439 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1fa3a9f-4e64-3b64-b3a7-d32193909e29 | -6.69329 | -58.82815 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4a50b4ba-760f-3cd6-8722-8f30314fd128 | -6.10561 | -59.92312 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f0d85d7-fd2b-32d3-b499-e3c49b34469e | -6.66536 | -58.81863 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4fb22ea4-149a-3d77-a9c2-7ea2c45c8705 | -5.92344 | -59.94037 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79bf9de2-1902-3a8a-8ce9-26361fd5f553 | -6.0752 | -59.95853 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d671f62e-f1d9-3439-9dae-6e88d38d0d32 | -6.67129 | -58.82563 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd42078d-355f-3923-82ff-da60d5a9e7a5 | -6.69926 | -58.83507 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e7d40e40-e3f7-34d7-805e-fbeaece7ca17 | -6.6985 | -58.84097 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 50e1f526-b5f0-316a-af6b-ade1a1e933ec | -6.7245 | -58.8388 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 23eebdae-6a58-37a5-a179-eff0065963d5 | -6.07024 | -59.94822 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8cbea97c-8700-3452-bc5f-c970a4bb4eb6 | -6.69409 | -58.82195 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5cf7de70-b9cf-3f4e-9708-73e6a30e52bf | -6.09111 | -59.93562 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7f938ee-3e94-37c4-9f46-a9894df9dd74 | -5.92743 | -59.9366 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d7095f3-3883-39e0-9e8c-56280d479015 | -6.10494 | -59.92796 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 389a5afa-d249-3139-a681-1058807e9573 | -6.69154 | -58.82845 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d1f382ad-c3f3-397c-bfb6-d6b87b110535 | -6.64434 | -58.82158 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1adb40dc-ad32-31ec-8cc7-1cef51c3a4af | -6.6925 | -58.83422 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cf1ca39c-48d0-397d-8ab0-ae236c3e589c | -6.107 | -59.91315 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47fadb39-29b2-3f29-8765-07bc2d58370e | -6.65781 | -58.82367 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bd673048-a814-371a-9caf-538d250cd29b | -5.45926 | -60.12984 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a0cd0a02-0d90-33ba-93d9-2abd5bbc89f9 | -6.69829 | -58.82937 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README65.md)
