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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8825252a-55af-32a5-be71-877ceccf7f52 | -18.35183 | -47.25945 | 2025-11-15 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02e71def-8b87-33c1-8844-33f6ee671a3e | -17.02478 | -43.37849 | 2025-11-15 04:08:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e9e891b9-c9b6-3fbf-8153-8ead8acd7ce2 | -14.63575 | -43.82808 | 2025-11-15 04:08:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09603062-acf1-3719-aa65-41ee3313b7cc | -16.81318 | -39.68463 | 2025-11-15 04:08:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ebaa433b-fc4a-3d75-abfd-30f3391e10dc | -15.52475 | -43.88447 | 2025-11-15 04:08:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 476a112a-bd30-39e8-8508-70989771db1d | -14.6537 | -46.5688 | 2025-11-15 04:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3a278e3-642e-3efb-a91b-900522c05b98 | -17.29624 | -46.82979 | 2025-11-15 04:08:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fad1eda0-2f55-3d54-9296-9cd671809738 | -14.85716 | -52.85902 | 2025-11-15 04:08:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abe79677-6d1c-3378-bec8-6ac7ae17eeed | -19.511 | -45.87165 | 2025-11-15 04:08:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2dd67519-a184-3151-84e7-b1d203945f74 | -18.30844 | -46.5983 | 2025-11-15 04:08:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 213731fa-6e72-3dc2-b65c-e9854e44cf65 | -17.15905 | -43.07944 | 2025-11-15 04:08:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa92a7f6-79af-3873-b083-9310b0a2ec7c | -19.08192 | -46.65285 | 2025-11-15 04:08:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8618a643-ebb2-3bf0-b694-c40451dd8b93 | -14.69125 | -46.6087 | 2025-11-15 04:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a186cbf-1f57-34d4-b25c-f9a6e23b2c4d | -17.02417 | -43.38216 | 2025-11-15 04:08:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e0fa7436-8d49-3264-b487-8ccd95acd4d0 | -18.60257 | -43.9889 | 2025-11-15 04:08:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98bad637-1beb-34dd-9472-19fe863afcbb | -17.67385 | -42.62749 | 2025-11-15 04:08:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 8b846d3f-52c2-352a-b3be-ff3d38db4e42 | -19.51035 | -45.86991 | 2025-11-15 04:08:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92a21ce9-f6fa-34ff-b744-e8e4340c253f | -18.59921 | -43.98831 | 2025-11-15 04:08:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a42202b6-7517-3a9f-a494-6be275574faa | -18.32899 | -47.18792 | 2025-11-15 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db279c09-ad09-3ac1-b9e1-172b72b4c068 | -16.66479 | -43.52858 | 2025-11-15 04:08:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c2d4bdc-8cfb-3d47-8603-72e9250b4131 | -19.19284 | -47.87242 | 2025-11-15 04:08:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d99f5e70-385e-3e6a-835f-c933c9067438 | -14.65976 | -46.58024 | 2025-11-15 04:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ae857d8-ad0c-3726-bf1b-27967ac47bd1 | -17.1614 | -43.07947 | 2025-11-15 04:08:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| acb2a222-325b-3518-b2ab-dcf8a2856502 | -17.01725 | -39.5914 | 2025-11-15 04:08:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 38a08624-2b93-3cf5-869a-07a7848f978b | -15.87876 | -45.20024 | 2025-11-15 04:08:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5d89b97-33d8-3099-b808-a8424df8d4c9 | -17.83681 | -50.81768 | 2025-11-15 04:08:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8fd433ed-7bd5-3f63-b71a-e53fba77cf09 | -15.46176 | -39.24019 | 2025-11-15 04:08:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 34671366-5e55-3c5f-b741-0d0e28841749 | -18.33282 | -47.18871 | 2025-11-15 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa5fdf25-775c-36e3-864e-d017fc323ddd | -13.63601 | -47.01091 | 2025-11-15 04:08:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 77c3b0f2-3449-3ba3-8500-193eb043cda6 | -17.24489 | -42.66599 | 2025-11-15 04:08:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d3f4fec-2f1d-38ea-a211-937ecb874a30 | -14.85808 | -52.8546 | 2025-11-15 04:08:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db5542bf-7d76-3909-9c48-85a38a8e009d | -15.47171 | -43.18893 | 2025-11-15 04:08:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 683dae41-5a47-321c-bebf-5826623eeaec | -16.60978 | -43.41262 | 2025-11-15 04:08:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9aa1256e-2518-399d-8c0b-8dbc4a9cb90e | -16.30334 | -43.80822 | 2025-11-15 04:08:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e9419c3-4591-3385-bf5a-ebd425e9bca1 | -4.7342 | -47.1547 | 2025-11-15 04:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c6846f99-fe3e-383a-ae34-b2c101a1b42c | -4.5381 | -43.2107 | 2025-11-15 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 6b329c0f-1545-39ee-bb35-8fca5c4410be | -5.2397 | -44.3448 | 2025-11-15 04:10:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 0ced5441-9824-3526-b250-83351dc66e6f | -11.849 | -49.2 | 2025-11-15 04:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 11755ec4-e315-3434-ba86-3cba121c828d | -11.8486 | -49.2218 | 2025-11-15 04:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| a265bad7-3887-339e-a934-12ca23adc648 | -22.16409 | -45.10474 | 2025-11-15 04:10:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0577d6f6-50b2-3081-aaf4-496cae7e5e67 | -5.2397 | -44.3448 | 2025-11-15 04:20:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 557a383c-52c7-36bc-a6cd-e2eb97517f8b | -4.7342 | -47.1547 | 2025-11-15 04:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 47bbcc26-b185-3380-9b3b-b143120d96b1 | -11.849 | -49.2 | 2025-11-15 04:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| bfbbb353-2352-3a60-bb50-dbda083a2170 | -11.8486 | -49.2218 | 2025-11-15 04:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| cda2ff35-891d-3837-9148-c4f480807ac2 | -4.5381 | -43.2107 | 2025-11-15 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 4f32db04-5a28-34e7-8f77-7487b57f019b | -1.04931 | -48.9469 | 2025-11-15 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 002ecceb-d86f-3050-8607-53c6e8ef1549 | -1.67689 | -46.92011 | 2025-11-15 04:23:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86bc3585-c709-3b01-b21d-4a575700aa9a | -1.79269 | -48.07012 | 2025-11-15 04:23:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54c585fc-1429-31d3-b7a0-2019932e8c83 | 0.51334 | -50.92416 | 2025-11-15 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f73d0cf9-ce7b-39a9-a855-da5b084d0f04 | -1.67971 | -46.92429 | 2025-11-15 04:23:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edb54b1f-8711-3690-ae01-56eb99f3b78c | -0.70539 | -48.64512 | 2025-11-15 04:23:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e86bec12-5129-3b29-aaee-b790606cdbe3 | 2.34344 | -51.65091 | 2025-11-15 04:23:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd21eeed-af3b-38fe-bf30-1af6f72cad35 | -1.05188 | -48.94901 | 2025-11-15 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d9ccfb9-8568-34b4-93ed-473561ded266 | -1.05258 | -48.9445 | 2025-11-15 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ca6b343-b436-315b-b203-da220f0602ab | -0.70169 | -48.64453 | 2025-11-15 04:23:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fe871f1-0b77-3d4b-a538-45a4309e1941 | -1.49418 | -47.8069 | 2025-11-15 04:23:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09f70bc9-e67a-35f8-9f4d-d45adb38fac9 | -1.59111 | -45.67575 | 2025-11-15 04:23:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03706f44-0fdf-3c2e-a1f9-801e7e213899 | -1.67631 | -46.92376 | 2025-11-15 04:23:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86509a8c-eaeb-3078-a734-dba2925377d5 | -0.36812 | -51.76982 | 2025-11-15 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0f99286d-a37f-3168-bd89-3b915d1ed2af | -1.05004 | -48.9424 | 2025-11-15 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6751b2f-f090-31c9-be20-0c9afbd444a9 | -1.29514 | -49.05621 | 2025-11-15 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b0b3390-b1fa-3f1a-aa6c-4efe2e800120 | -0.70099 | -48.64892 | 2025-11-15 04:23:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b4356a9-efd8-3ddd-b82f-a25e3762e675 | -1.05379 | -48.94299 | 2025-11-15 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3eb83b99-91ed-3b33-b63d-8f9a09c1a9a5 | -1.11175 | -52.59767 | 2025-11-15 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 06191be4-3bea-3163-9454-b1aa163bccbb | -1.68028 | -46.92064 | 2025-11-15 04:23:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d570953a-8c1f-38d2-ab0e-d81ee8041b5b | -1.4905 | -48.67672 | 2025-11-15 04:23:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4eee17d1-bc7b-322a-8197-9ba4091325f9 | 0.50898 | -50.92485 | 2025-11-15 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e891bac-a1bb-3cad-93fc-878871e0f6b3 | -0.86561 | -47.30912 | 2025-11-15 04:23:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df62f2aa-2bea-3c28-b52f-1ce729abec66 | -1.29211 | -49.05105 | 2025-11-15 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b387f65-e009-3506-ad66-c8370954edca | -1.05306 | -48.9475 | 2025-11-15 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a81b2c9-2308-3ea8-a5df-dce0a7bb766c | -1.49769 | -47.80746 | 2025-11-15 04:23:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 715dad47-2c90-3f0f-a0bf-dfab919a3249 | -2.50114 | -43.24742 | 2025-11-15 04:23:00 | NOAA-20 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fbcf0035-d5f4-3a5c-98d8-f491abcff377 | -1.29891 | -49.05681 | 2025-11-15 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3e902b3-b0df-3ce5-b1f1-28f70537a190 | 2.33873 | -51.65172 | 2025-11-15 04:23:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 774a5b67-6c60-3aa1-8f5f-0e83b17d3918 | -1.10698 | -52.59684 | 2025-11-15 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e30f6d5c-9bd5-32d5-9dbf-1b938aab31bb | -9.81292 | -44.22634 | 2025-11-15 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 765a4405-9ad9-33b6-8d8e-f208580aa9e8 | -5.5252 | -41.77153 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f4c6feed-a110-3bef-b194-f7cc9a2c8f40 | -6.67963 | -43.76653 | 2025-11-15 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41b38354-41f4-3ef1-b08e-d0a9f76a47fd | -3.28247 | -53.82471 | 2025-11-15 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca3513aa-d353-3036-a315-16bb14040289 | -3.38351 | -47.19269 | 2025-11-15 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2212d0bc-9fdc-3d67-8b56-91c1732a0671 | -4.58281 | -43.40282 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16049d7a-6feb-3bf3-867c-abd44fb033dc | -7.384 | -48.65012 | 2025-11-15 04:25:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11ab64c0-af7f-3a2f-b7dd-d5bd948dcdf8 | -4.42468 | -47.59645 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af5f5095-f3f8-372b-99cb-4a478cf2ef68 | -6.0384 | -45.80929 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d806fe5d-1a5d-3c71-8633-ec319321b73c | -5.33418 | -43.03594 | 2025-11-15 04:25:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34e03735-1b09-3544-8dc6-42bedd54b6aa | -4.25366 | -48.20072 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c7717577-ab90-3be0-87bb-63e0418258b5 | -4.42001 | -43.35209 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db28bf04-7d2e-381c-9c60-64cc36ec1d72 | -5.43033 | -42.58092 | 2025-11-15 04:25:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ce363b85-a308-3b8d-92f9-a8293489fa21 | -2.74181 | -45.29745 | 2025-11-15 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7841a79-af65-3d29-9ec0-48916a7dbbe9 | -6.46005 | -45.65514 | 2025-11-15 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73ec2dc3-3fd4-39f4-87b2-24b04c68ac8b | -4.25555 | -46.31845 | 2025-11-15 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55b58a41-2221-336e-80b6-152ad270c261 | -4.22382 | -51.20034 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc63783c-2296-398c-9c9c-760ed358b595 | -4.07319 | -44.13393 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 973824ba-5f8d-3ba3-853b-cde350664b43 | -4.43518 | -42.99921 | 2025-11-15 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77d803e8-a036-3a02-95c9-cfc9ff24e7cd | -5.23494 | -44.34758 | 2025-11-15 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 86111041-ac56-393c-893c-5d54bdca5432 | -3.19842 | -53.01439 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac8fdcc2-d41b-353d-b802-571bb52cef90 | -7.10882 | -42.73062 | 2025-11-15 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| df401283-e5b0-3e86-b644-78dfced93b78 | -6.7374 | -42.95998 | 2025-11-15 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 385be86d-c743-3f68-b97a-86d8c9206716 | -5.36195 | -44.90281 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fdb84fc-7f3b-3698-8700-c2fc238cdb67 | -4.02609 | -42.47579 | 2025-11-15 04:25:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README32.md)
