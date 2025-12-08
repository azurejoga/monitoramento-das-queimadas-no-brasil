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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48f8784e-f888-3cc5-8597-3f4237916ab9 | 3.40144 | -51.25602 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8b6cf696-ec6e-3a5f-9594-480fc5dd1748 | 3.40433 | -51.25165 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e24a1eb7-78d0-3250-bdb8-7c7cfbbb6471 | 3.56847 | -51.29918 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccd2abad-7f8e-3de1-ba52-1f9705b69c2e | 3.66903 | -51.38755 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d1b7e77-1b6b-33c9-97e8-2af583ce7d96 | 3.67254 | -51.38702 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aac5e30b-5ee3-33f7-84a7-94f88ad3f582 | 3.41129 | -51.2506 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bdb3f08-a25e-3546-be99-b2747c978257 | 3.42173 | -51.24902 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 170209fb-5081-3c99-bc4c-53589952c530 | 3.42066 | -51.25364 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89ffa1bb-aa9f-3cb1-a249-4112e1e87391 | 3.42233 | -51.25286 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3bad3733-5a42-3e25-a7d5-def183b678de | -0.64668 | -52.37885 | 2025-12-08 04:44:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e91cc675-d398-35a0-9d8b-c70f651f0979 | -0.80774 | -51.94481 | 2025-12-08 04:44:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fc730c6e-4b83-3931-90ad-53a23edfbc3b | -2.2308 | -45.77464 | 2025-12-08 04:44:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6caea64-2d4f-37de-adff-72850d55a8cf | -2.08237 | -52.05151 | 2025-12-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a03c870-00cd-31dc-b8bb-876327266d94 | -1.89487 | -46.46113 | 2025-12-08 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6ae2084-50d9-3e8e-a819-01a469c4798e | -0.93647 | -46.91333 | 2025-12-08 04:44:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fe9277c-2e5d-36aa-873d-f4fae517b52d | -3.0838 | -47.76017 | 2025-12-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d49a247c-4d2d-36d6-860f-4c49ab38ae40 | -1.9409 | -46.67531 | 2025-12-08 04:44:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51c9c22c-2191-357f-bcc1-1bacabb7a853 | 0.76571 | -50.80283 | 2025-12-08 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12fb32d0-d93b-30c7-8c54-1e3511193dcb | -5.0904 | -40.24002 | 2025-12-08 04:44:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b38a039-ec11-314a-a019-0b34382cfe5a | -3.3319 | -42.14037 | 2025-12-08 04:44:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 183dde8a-d6f0-3f43-8bee-ce8db6762ae3 | -0.37788 | -51.95707 | 2025-12-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f638020-1330-377f-bcd7-572ff2518814 | 1.66509 | -50.65655 | 2025-12-08 04:44:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f73fab1-7f50-3d46-801c-491f1e22b59e | -2.10603 | -45.96086 | 2025-12-08 04:44:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92e08f0e-83df-3574-b81d-b7d8a5c1ab4e | -1.891 | -47.89664 | 2025-12-08 04:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b799baf-68da-3632-9805-fab8be26d2ed | -2.164 | -47.8754 | 2025-12-08 04:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84ec4c0a-4a9d-387b-a469-101170444aef | 3.29818 | -60.83818 | 2025-12-08 04:44:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69ba2091-2b80-3627-87ac-fcb4465420a1 | -1.11762 | -46.54733 | 2025-12-08 04:44:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0d3f9c4-73a5-3fbc-b76e-070535ee3438 | -0.80716 | -51.94855 | 2025-12-08 04:44:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dabf177b-9119-3c7d-8982-40b1d52028b0 | -1.00087 | -52.31697 | 2025-12-08 04:44:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a06c04f0-2961-35ed-be41-dc3e3559760f | -2.63547 | -46.95744 | 2025-12-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c8cf8d3-7d6d-3fb1-ab75-4884685d98a9 | -2.63909 | -46.958 | 2025-12-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 547a783e-c96b-3703-b0cc-05526b5feb1c | -0.9621 | -52.32742 | 2025-12-08 04:44:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b290209f-aa2b-3aaf-a42d-4c022e020704 | -3.65593 | -47.1672 | 2025-12-08 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26746a6c-3d28-34e5-8d55-11a31f32b968 | -1.46722 | -45.95726 | 2025-12-08 04:44:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4599c435-6eba-3d43-a07b-ba197df04f3c | -5.08863 | -43.65585 | 2025-12-08 04:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdfd0541-ad50-3386-9681-33c7a08ddb54 | -2.70071 | -51.66639 | 2025-12-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1155e8ff-85e3-396d-bce0-c7d352492655 | 1.68696 | -50.62033 | 2025-12-08 04:44:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d52a58c5-fae5-32cd-b2e0-c0a44b9e48c0 | -2.55078 | -47.31817 | 2025-12-08 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7973f72e-ca28-332e-a316-e235ca18eb22 | 2.33933 | -51.64965 | 2025-12-08 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66221d2a-d672-3ca2-a2a1-f274b860ac2e | -2.25612 | -46.11972 | 2025-12-08 04:44:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8371717-291e-3a9a-8253-c4c97e28b994 | -2.11055 | -46.61973 | 2025-12-08 04:44:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acf07ec5-afef-3693-8585-61f190438787 | -1.9886 | -46.41752 | 2025-12-08 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d82be63-4043-3771-aa80-ae876b909443 | -3.8447 | -47.83073 | 2025-12-08 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d21ca9a2-3fd4-3b31-9630-2aa06a461cc6 | -4.1113 | -50.43973 | 2025-12-08 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a9cdf1a-32d7-3e5f-a61d-8032c8cb1fc4 | -0.98269 | -52.97543 | 2025-12-08 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef44374b-dae7-359f-a086-4f148cfa27f9 | -2.17638 | -46.13547 | 2025-12-08 04:44:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dfbf16d9-7dc2-3cfe-98d9-df2201c42bcd | -0.38422 | -51.96193 | 2025-12-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 357544d7-1f9d-3288-8855-fd28f7a14c25 | -0.13032 | -51.74194 | 2025-12-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee5046d8-17f9-33f9-aeed-578870514a58 | -3.65955 | -47.16776 | 2025-12-08 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0b6b427e-300c-3339-9d36-9d70e87dcfbe | -3.546 | -43.96143 | 2025-12-08 04:44:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9bd6263-543f-3461-9b12-3c4bf3fd975b | -1.36045 | -47.69828 | 2025-12-08 04:44:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 577e7b95-487d-32b8-8b01-39f7f7a8a79e | -0.90236 | -47.34369 | 2025-12-08 04:44:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fec44f34-2b27-3f9b-83d8-3b92584081b6 | -1.76146 | -45.86065 | 2025-12-08 04:44:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0716d3a3-f9a6-3bdf-9683-6fcf16332fb7 | -1.09771 | -48.14719 | 2025-12-08 04:44:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3e37e5b5-5b80-3ed0-af2a-e5954045e9ff | -0.07696 | -51.61218 | 2025-12-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c776f396-57cd-31c5-92c6-69c79bfbeebe | -0.38314 | -51.96128 | 2025-12-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 86363233-c90b-3279-9f1a-7787d1dc7040 | -1.89032 | -47.89649 | 2025-12-08 04:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdb87bf3-a529-3647-b34a-42e392bc1e3e | -0.13376 | -51.74246 | 2025-12-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f857d575-078b-3757-83c5-f4e086a430b7 | -1.00025 | -52.32084 | 2025-12-08 04:44:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1acec160-c577-3207-bd78-7c1167b92d04 | 2.37469 | -51.69228 | 2025-12-08 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96de7809-174e-31c7-becd-15efc73ba02b | -2.63845 | -46.96219 | 2025-12-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ef1fe4c-3e21-3938-83d7-368ff309798c | -3.39391 | -44.16313 | 2025-12-08 04:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fbb67c3d-2bf1-30eb-8411-9e1973dcb041 | 1.76926 | -50.60422 | 2025-12-08 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5241c21-4700-3084-aad3-4778dfc9eee9 | -2.25684 | -46.11512 | 2025-12-08 04:44:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad88eb6c-9c40-3f53-a825-3608de41ee6c | -2.03101 | -45.81743 | 2025-12-08 04:44:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ab02ead-19ee-38cc-b3f0-30157866adb7 | -1.3639 | -47.69882 | 2025-12-08 04:44:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b1c00e7-0614-390d-b45a-c4662717603b | -1.45351 | -45.94574 | 2025-12-08 04:44:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 105bea9e-2ed8-341c-9850-5b1500dbbc51 | -2.7329 | -44.00795 | 2025-12-08 04:44:00 | NOAA-21 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c77cc970-4be9-3775-bee7-de7f7e92d58a | -4.47073 | -42.99184 | 2025-12-08 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1fc662a9-a2e8-3337-b8f0-0a62fb313426 | -4.47021 | -42.99231 | 2025-12-08 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ad82818a-d5f2-34fb-ade5-de5bdaee46b6 | 0.07944 | -49.89272 | 2025-12-08 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7600306c-c4b4-3b85-8f4b-f347632e82be | -0.38075 | -51.96141 | 2025-12-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0eeb0bb-4710-3155-8d2f-f700e9646be5 | -2.36023 | -47.68916 | 2025-12-08 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4974a6f0-eaab-31ec-9e5f-45a58161bdf3 | 1.3927 | -50.6586 | 2025-12-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 319465ec-2400-3fab-9340-9bc72a00b889 | -2.63781 | -46.96634 | 2025-12-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 569645b3-1efe-32c0-a687-e0c1ca1c5544 | -0.30943 | -51.69675 | 2025-12-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35610e60-3e8e-330f-a978-33613295b355 | -0.81522 | -51.94211 | 2025-12-08 04:44:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88be6b64-1388-3481-8bba-1ebf75c5a42b | -2.38511 | -51.9136 | 2025-12-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3dbc680-c75e-3e10-b150-146708650436 | -1.89625 | -46.45903 | 2025-12-08 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e89b5e6-5de7-3909-bec7-8b6993be78a0 | -3.27159 | -44.40342 | 2025-12-08 04:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aee29bfc-a22f-3bc7-8985-57afc6a39c2d | -0.38134 | -51.9576 | 2025-12-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a2eeca7-92d2-3301-8108-2523ba243a2d | -5.08792 | -43.66071 | 2025-12-08 04:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dbf4e2e-5773-3d9b-b8a1-530f714e873a | 2.74535 | -50.89628 | 2025-12-08 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b57d7760-0e54-342d-bbda-3f0420944481 | -3.33692 | -42.14114 | 2025-12-08 04:44:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 44920772-b16b-3818-b96b-f5f59d17ac62 | -1.91345 | -47.36431 | 2025-12-08 04:44:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33107043-4c45-375b-b0e9-2a0a7359b10c | -3.81552 | -50.63243 | 2025-12-08 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06be355e-8df2-3b56-85bf-bfcd07fbd1c4 | -1.73786 | -45.65819 | 2025-12-08 04:44:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1721b2b8-ab9a-363b-9bb9-117c5dec3df3 | -1.73713 | -45.66298 | 2025-12-08 04:44:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54f7ce8f-270a-37d2-956e-797b0a2062b5 | -1.12226 | -47.7394 | 2025-12-08 04:44:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7eef335a-4664-3d5c-b5a1-2209a320657e | -3.34011 | -45.87066 | 2025-12-08 04:44:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8937857-525b-3fa8-8a15-99a5c955410b | -3.33185 | -42.84299 | 2025-12-08 04:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 24db4d32-0520-346f-9435-ccf0159d2ee2 | 3.20308 | -51.24237 | 2025-12-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efeb1f74-8722-3763-9ff3-8480a500181d | -0.98629 | -52.97605 | 2025-12-08 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e174d14c-19e2-3355-b8d9-18b4289a3d9d | -3.81226 | -51.75234 | 2025-12-08 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 200d0237-6126-31b1-9402-3d98796ad95d | -3.84822 | -47.83127 | 2025-12-08 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aba387d4-63b2-3197-b4e8-ff60cef8496b | -3.2214 | -46.24612 | 2025-12-08 04:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3af0568-2887-342e-981d-f08e1b989032 | -2.95417 | -48.07026 | 2025-12-08 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2798db3c-f540-3110-96d8-68ba89e8359f | -1.67475 | -45.86632 | 2025-12-08 04:44:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97805156-c266-3fbe-8301-cdf2316515fd | 0.83914 | -50.22628 | 2025-12-08 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a47ef2e-8a06-374c-9929-40f81c515fd0 | 3.20159 | -51.24247 | 2025-12-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
