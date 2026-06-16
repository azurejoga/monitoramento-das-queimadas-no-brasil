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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6e73d93-cbd9-3223-b729-b867b06fe7f9 | -6.18227 | -48.50468 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 805a1529-5f50-331c-85be-0ce255e82a8d | -8.94145 | -46.9633 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3013646-a8be-32a6-b247-d3882a51e2a4 | -7.36041 | -49.86322 | 2026-06-16 04:36:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b78d4c5c-0d7e-337e-9f3d-ec7071320833 | -5.83629 | -43.4837 | 2026-06-16 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 225c1d7d-df9d-311a-9952-e9871f9ae2e1 | -6.01256 | -47.10851 | 2026-06-16 04:36:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90c51ee3-8cdf-35ad-b8a6-f1645f0eac3c | -8.27999 | -48.21793 | 2026-06-16 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e813e3ce-ee7b-3654-b187-5237028be5b8 | -13.54238 | -47.85641 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c34d452-f173-3ec5-9746-bd7b5bd7c94d | -10.49558 | -53.58476 | 2026-06-16 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52532193-e484-3d79-85c0-5cc4ed4bf18a | -10.81653 | -56.60942 | 2026-06-16 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 282ba4a4-c631-3435-a016-7fb2287dddd5 | -11.55383 | -52.77441 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 72b25627-c289-3eda-88a0-56cde30e97be | -12.15032 | -48.46235 | 2026-06-16 04:38:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98571dec-fbce-3e5c-be60-3f9e03b70669 | -10.15393 | -56.5967 | 2026-06-16 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 46f74f88-8439-3bd4-a3e8-0890e07d07c7 | -9.32326 | -45.47604 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db69cd30-cd96-3a18-a10b-150ee5e230c4 | -8.66222 | -49.16875 | 2026-06-16 04:38:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 273a5b9c-bff5-3c95-8303-6635ab3bdaac | -11.5109 | -56.1317 | 2026-06-16 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 099318c1-0624-3f9f-a750-021c657f0850 | -11.35689 | -51.38514 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44fdb95a-afb0-392b-b5b3-66a52bf8fff6 | -11.90068 | -57.78703 | 2026-06-16 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f54f66d-4759-3107-bb7d-49588a1b5b0b | -14.84976 | -43.36857 | 2026-06-16 04:38:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 83affa14-fe7a-36c7-b87a-dc17dbb16ba6 | -15.07057 | -55.81527 | 2026-06-16 04:38:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e827067-db5a-352e-9c05-57fb2c80f7e6 | -12.58439 | -54.16813 | 2026-06-16 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98de2959-f293-35ca-8ac5-de0ed72dcbde | -14.1006 | -59.46023 | 2026-06-16 04:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 874c6144-1b00-3fd0-ba2f-69197d0f55bc | -11.47697 | -57.12212 | 2026-06-16 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ad1ffb70-5b51-3f8a-905d-6107df278874 | -11.78958 | -57.00026 | 2026-06-16 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4bf0ce9f-6bd6-3c11-8e78-0efa03170c02 | -12.59491 | -52.91781 | 2026-06-16 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bf03066-235d-33a3-a108-834587fbfa17 | -10.54927 | -47.03064 | 2026-06-16 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4788a451-c7bb-3531-97a0-62150529e9c0 | -9.32984 | -45.48128 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| faaf945a-2434-39df-8fb7-f903022d13c3 | -10.80431 | -54.17435 | 2026-06-16 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d381f3f7-6671-3fe3-8a29-3368d4818314 | -9.32922 | -45.48544 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c158746c-b688-3200-b241-3e1f0311a96a | -9.21287 | -47.33692 | 2026-06-16 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df0e65f3-32f2-388c-8fa4-036cda493106 | -11.91501 | -57.04383 | 2026-06-16 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32c975f3-9319-37ac-8a9f-fdc1cee0d341 | -8.82685 | -48.81873 | 2026-06-16 04:38:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38da5377-ffde-315b-8183-8d120b32b1b3 | -11.6225 | -55.18569 | 2026-06-16 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a4973db-f752-3e0e-9e10-d426c62ce0e6 | -12.80688 | -54.86134 | 2026-06-16 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 715246a5-dcc6-31d1-9f73-1a4f93e9ece2 | -10.77054 | -54.10442 | 2026-06-16 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6c32ebf-8ca7-3a3e-bfe4-dde61d9cfba3 | -11.48007 | -57.10527 | 2026-06-16 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b97262a4-e815-3757-95a9-6ea1ed498b1c | -9.22496 | -48.58017 | 2026-06-16 04:38:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ac3addc-eeae-3d43-9835-26a23c94bd7f | -11.45594 | -48.08231 | 2026-06-16 04:38:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc325b0c-68d0-3630-b95a-731479ed3170 | -9.68992 | -47.03962 | 2026-06-16 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e724807-f8c7-34eb-b411-ced6927bc2e0 | -10.29362 | -44.08201 | 2026-06-16 04:38:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8be71229-26f8-3102-b740-5df310b85a88 | -11.71963 | -54.48661 | 2026-06-16 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f65dceb2-c6f8-3a3e-85ef-0fc9a3d5f1fa | -11.71832 | -54.49409 | 2026-06-16 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82a9e8c0-9e48-33f8-abf7-2aa343d72b53 | -11.90935 | -55.91209 | 2026-06-16 04:38:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6667a073-777b-370b-9c78-5935381e9b46 | -14.71766 | -42.94527 | 2026-06-16 04:38:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 07d1508f-43bc-3b76-9b72-9e100c83dc21 | -13.55431 | -47.8465 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44351566-7df0-394d-9385-bd15f9870543 | -9.3723 | -48.42117 | 2026-06-16 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d924b6b5-32b2-3a14-bbdd-3d76ac4c39bb | -12.13148 | -48.25871 | 2026-06-16 04:38:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea0cb070-daa8-301a-b91c-560c58c27ae4 | -11.54568 | -52.77757 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1d649e8a-e196-3e65-9a32-a0f7d7719cd5 | -13.53899 | -47.8559 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4616d258-80e3-30da-830f-912cccd55e75 | -12.91797 | -54.21976 | 2026-06-16 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60c0ee1a-86d4-3a4c-ad7c-45772389f46a | -10.49951 | -53.58545 | 2026-06-16 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2e14af5-8015-3dce-a591-cfe8afc037bd | -11.99033 | -45.14856 | 2026-06-16 04:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 03edcd19-6398-3538-9154-51dd9bcf0041 | -9.22331 | -48.5692 | 2026-06-16 04:38:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73cc2912-db57-30e1-9a02-62b074b0c40f | -13.83825 | -46.17536 | 2026-06-16 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7adec65-327c-3ee2-b910-ad3a695e2488 | -11.55 | -52.79676 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a44d98b-4941-32c5-b4fd-b022e9416b4f | -9.36101 | -46.49201 | 2026-06-16 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2926768-13ad-39de-82e6-dba3b4539f02 | -9.37285 | -48.41768 | 2026-06-16 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec196790-a4f3-3adb-b056-d33964482c5d | -13.55144 | -47.86542 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11a3a0b3-e8f7-3681-b9db-fae349baff20 | -11.59098 | -55.33905 | 2026-06-16 04:38:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aeaf8fdc-0258-3d5f-b329-ef2356d3da55 | -10.14813 | -56.6012 | 2026-06-16 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b288bd14-918c-3eb1-8e33-836ef5d93ef5 | -11.59023 | -55.34328 | 2026-06-16 04:38:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 97605fc5-9317-3362-b271-2f9811613ac3 | -12.67329 | -54.58027 | 2026-06-16 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2771fdf9-ff38-3e26-86a9-e14c1eb1cdc6 | -13.54522 | -47.86065 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5897c330-fe91-32ee-a457-4b0c7ade95ec | -9.69928 | -48.60991 | 2026-06-16 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2063c6e1-81f7-3a46-b55c-5fd3560fab0e | -11.35365 | -51.4046 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 034e9cdc-649c-37a2-8e74-abd6e0f0b30a | -10.01837 | -46.40555 | 2026-06-16 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35d35c7f-8cf3-3552-9b6c-b7a6ca410a0b | -13.53955 | -47.85216 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c8ede4d-33f4-339f-be22-2cd7d1e93cb3 | -13.56333 | -47.85577 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f59f732-c759-357f-a719-e946cce4879b | -12.4463 | -44.75043 | 2026-06-16 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 445889fa-bd22-3ce5-95ba-e665bce89455 | -11.55077 | -52.79227 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0060b073-7034-3793-b332-10c11d4958d7 | -15.06634 | -55.81463 | 2026-06-16 04:38:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d00ce321-23a3-3d0b-bed2-504f60dbf47a | -10.56064 | -47.0248 | 2026-06-16 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 689d2fdb-4811-328a-8324-1b9254c05bc5 | -9.35757 | -46.49149 | 2026-06-16 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60caaa7b-921d-3617-95a2-c14d86ba8b99 | -13.54805 | -47.8649 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8447aab-4256-38b6-a6df-0ad201cfd0a6 | -14.10133 | -59.45662 | 2026-06-16 04:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcd2e236-79be-3e8c-b7a5-a80fdfbc517b | -9.46234 | -48.3895 | 2026-06-16 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6c0cee5-3289-3db8-a45e-cc9ffdb8b429 | -11.58666 | -55.33823 | 2026-06-16 04:38:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 613ae6ce-0b7e-3fc5-b230-27ca344111a3 | -13.56276 | -47.85948 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e89eca4-8582-357a-8f14-e772ba749aca | -9.69597 | -48.60938 | 2026-06-16 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9396defe-532e-30fe-b8c6-cfd639a0ee56 | -9.22386 | -48.58712 | 2026-06-16 04:38:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee790f7b-1c22-3d01-a818-314886d723eb | -13.53408 | -49.89821 | 2026-06-16 04:38:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d14c4d0-e488-3c1a-a430-2c9855001dd2 | -11.48126 | -57.11119 | 2026-06-16 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| aec84c44-8a9f-35d8-baad-a334e97db53a | -11.64741 | -52.86277 | 2026-06-16 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 978083b2-275f-34b8-8049-ba67fd9516a2 | -14.85856 | -43.36983 | 2026-06-16 04:38:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| af034f16-46a3-35d2-8d16-c39628e39c8f | -12.85062 | -44.37506 | 2026-06-16 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 98ea46d8-ff99-3685-b97d-c1509df6fe6f | -14.10206 | -59.45301 | 2026-06-16 04:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 621797ba-c3f4-3d83-9edc-7108cd4d2bf4 | -9.21623 | -47.33744 | 2026-06-16 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c26e4a1-f77a-3039-b22c-b23604639dc2 | -12.91706 | -54.22489 | 2026-06-16 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 21c1a706-cc3b-3f89-bfcb-6939fa864b21 | -11.20001 | -49.68327 | 2026-06-16 04:38:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b784a240-5a5d-3f75-9faf-196822711615 | -8.97979 | -47.98 | 2026-06-16 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c48cf7f4-3ed4-3a14-84a7-920af4563a47 | -9.31967 | -45.47549 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02b4233c-0c04-3408-9178-7cd289f0d8b2 | -8.97648 | -47.97947 | 2026-06-16 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c245d08-e1f5-3f4d-be48-d45085fe244f | -11.78631 | -54.01213 | 2026-06-16 04:38:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b25daa66-6d62-34ec-ab4c-71f15a39a580 | -9.74008 | -47.87407 | 2026-06-16 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13a091d5-2577-3697-9c46-5e254dd6fdd3 | -9.78983 | -48.07661 | 2026-06-16 04:38:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 932fed53-e3d5-3866-8d58-c8c8581332e5 | -10.14715 | -56.60661 | 2026-06-16 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f92a932c-bd2e-3122-b62b-3da89204fa62 | -13.5554 | -47.86221 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 927fd39e-5687-33fa-854d-7a0b9681650b | -10.51028 | -44.86103 | 2026-06-16 04:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f518c23f-5d4d-3a08-9ac2-8f0d2ea0c7bf | -14.71944 | -42.94352 | 2026-06-16 04:38:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8d4bc4ea-b9f5-3777-bc4f-9badb0d03439 | -9.33826 | -45.47403 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bf0ecbd2-8950-328a-ab22-04ed918a972c | -11.16744 | -49.24878 | 2026-06-16 04:38:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README11.md)
