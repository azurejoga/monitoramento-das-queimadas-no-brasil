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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd8fa9e7-8fc0-3b7c-a605-0110d518ca43 | -11.73225 | -48.18703 | 2025-07-24 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b08c33b6-d9b8-39aa-9761-6557225f3c4e | -12.42079 | -43.48485 | 2025-07-24 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a0554cb-bfae-3602-bd16-229608a6ecc0 | -11.13129 | -48.63464 | 2025-07-24 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 174af015-5faa-3bff-aea5-b625d3033967 | -11.77361 | -47.40009 | 2025-07-24 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d3bc138-99d9-3b85-903d-181692ec7a8e | -14.1726 | -45.34088 | 2025-07-24 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 882aba5d-8dbb-3d23-aa89-91131b1f1b70 | -12.42024 | -43.48846 | 2025-07-24 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2ae3869-3d8c-313a-a8d6-985ff4659398 | -23.00719 | -47.39602 | 2025-07-24 04:17:00 | NOAA-21 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ee6e62f0-921a-31a9-8536-9d15acce5c24 | -15.27961 | -47.13 | 2025-07-24 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e97d0cb-cebf-3e36-b83b-eccfe61c5d15 | -11.95255 | -58.76469 | 2025-07-24 04:17:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d980479a-17af-348c-916d-cc5002bfda1c | -13.70914 | -45.6904 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| be655728-5d4c-3bfb-b138-2684cd3d72fa | -13.6987 | -45.67036 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4c3e9dff-c975-3229-9ef5-df7f4ba97175 | -11.11753 | -50.4805 | 2025-07-24 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 95bb2fb1-a427-3346-8687-d2d8fcd0fc7e | -16.08988 | -45.16877 | 2025-07-24 04:17:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad116bdf-a097-3d94-b965-d2245053b9c3 | -10.62678 | -45.24115 | 2025-07-24 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56d81ada-2466-3a8d-92d0-6512f88b3fe0 | -23.01536 | -48.9103 | 2025-07-24 04:17:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9cdd5d00-ec55-3d55-bade-c74de6ec7a49 | -13.70979 | -45.66487 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 817fe3ea-f715-3e82-a878-66be989b6fc9 | -23.92249 | -49.09931 | 2025-07-24 04:19:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f5f2b36-96f7-3e80-9120-7df84c0cfd63 | -19.45432 | -47.25363 | 2025-07-24 04:19:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faa40a10-b921-3fed-b887-1cc681124faa | -17.57317 | -47.50649 | 2025-07-24 04:19:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a5df92d-7ec8-36ea-978d-c2ccb23d1282 | -19.05974 | -48.33416 | 2025-07-24 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f4a9f55-9357-37a4-a194-4e3d4d67653b | -19.45697 | -47.25423 | 2025-07-24 04:19:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ea65f7c-4852-3a6f-bda7-1a6c423a7a04 | -24.11152 | -48.57308 | 2025-07-24 04:19:00 | NOAA-21 | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3871183e-2a89-3779-bbca-870afc3af54d | -18.83106 | -41.98497 | 2025-07-24 04:19:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cba601e7-458d-3045-ad6d-6fa9a4cb1dfc | -19.90639 | -44.99746 | 2025-07-24 04:19:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c46f6068-8545-37c3-b133-e90a3193b4d1 | -18.88175 | -47.96574 | 2025-07-24 04:19:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7eb67bb7-9311-3e0c-a1ff-46b3e970b769 | -24.69933 | -50.24401 | 2025-07-24 04:19:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6ee53381-6503-31cd-bfb8-252a85e52f78 | -19.0588 | -48.33714 | 2025-07-24 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a530e0d-d728-336a-8f88-5581429c35c6 | -24.00712 | -48.50236 | 2025-07-24 04:19:00 | NOAA-21 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b3b75bff-5f50-3c3c-af7c-19d217f1262b | -18.11453 | -44.63368 | 2025-07-24 04:19:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9467628-8758-33c2-a00a-de5144cc1a72 | -24.11214 | -48.56923 | 2025-07-24 04:19:00 | NOAA-21 | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8c79a51f-56f3-37e6-a4eb-ebe967c1c5c0 | -18.11789 | -44.63424 | 2025-07-24 04:19:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58f14e20-07f0-3bf9-abfa-4e36015a4a74 | -17.76532 | -48.26642 | 2025-07-24 04:19:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01082d85-8321-3a09-92f5-bcae14c86aab | -18.85399 | -47.96443 | 2025-07-24 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f7d4eb86-2951-3014-844c-86b2397ad2d3 | -17.80902 | -52.66283 | 2025-07-24 04:19:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9caf7461-6391-315a-a075-b0103c6e71dd | -18.879 | -47.96124 | 2025-07-24 04:19:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1dd89b68-0708-34e7-936c-00ed762cbe41 | -17.57254 | -47.51028 | 2025-07-24 04:19:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95a781ce-c8a1-3fbd-9749-92cf4d041b5e | -18.26996 | -51.14151 | 2025-07-24 04:19:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cc988af-1788-357a-99ed-5eba15914a06 | -24.58662 | -52.82184 | 2025-07-24 04:19:00 | NOAA-21 | CAMPINA DA LAGOA | PARANÁ | Brasil | 4103909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bdc6dd64-00ab-3775-9197-c586bbe47a39 | -23.36164 | -50.82573 | 2025-07-24 04:19:00 | NOAA-21 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9c0cf87e-df1a-381e-bfc2-db0037dcdb67 | -19.05908 | -48.3381 | 2025-07-24 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 122a4164-9691-3a10-afb9-5afeb1cbe613 | -18.85463 | -47.96059 | 2025-07-24 04:19:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| be942d2d-969f-37b9-8eac-0341449ebd91 | -19.90696 | -44.99366 | 2025-07-24 04:19:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e1463986-bf55-351b-97aa-b7aee438ff94 | -17.61098 | -46.69386 | 2025-07-24 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f87bc947-161c-35f9-9e31-f973d55622c4 | -24.05781 | -49.83509 | 2025-07-24 04:19:00 | NOAA-21 | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b29076b3-4874-3801-b8a9-e9568de5d814 | -18.8506 | -47.96382 | 2025-07-24 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c96d5d29-be81-3b39-8a2f-b36da74e6527 | -23.92184 | -49.10323 | 2025-07-24 04:19:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11b709a6-ed77-3a47-8e1e-bd6256534463 | -19.67336 | -43.23466 | 2025-07-24 04:19:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0d1f5c6b-ce1c-3b2e-bc7c-9493dcf8ed78 | -18.87836 | -47.96511 | 2025-07-24 04:19:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8bae8ff8-83f0-34bd-8c9d-b4124cdc9e03 | -17.56915 | -47.50969 | 2025-07-24 04:19:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e91e07b-079c-3f9a-9e41-2e738a07fa7a | -3.1648 | -49.4648 | 2025-07-24 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| f7131b95-2e27-3da5-b320-28f43a019992 | -3.1833 | -49.4429 | 2025-07-24 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| d504f2a4-b32b-3228-8329-76a2fb4af40e | -3.1832 | -49.4642 | 2025-07-24 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 5d3a411a-e83a-33b3-8191-12db399962d7 | -7.2594 | -43.0881 | 2025-07-24 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| bd31267e-e1d1-33c9-ba77-2f417c6a506a | -7.2597 | -43.0645 | 2025-07-24 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| c092f69d-5f46-37d2-9e42-95d3d0b55c01 | -7.2408 | -43.0664 | 2025-07-24 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 10697e25-a9f5-3e66-829b-f9c48410d39e | -3.1649 | -49.4435 | 2025-07-24 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ff9ad97f-1304-3f4a-8226-a483c38645e2 | -4.0569 | -42.5118 | 2025-07-24 04:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 52.8 |
| 12a2dee5-953c-371a-8896-e28ea9097777 | -7.2597 | -43.0645 | 2025-07-24 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.7 |
| 18cbeb78-fde0-3ca1-8615-924e3e026d7e | -7.2408 | -43.0664 | 2025-07-24 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| a4597c80-5bef-332f-8559-22664ebfb9d8 | -3.1833 | -49.4429 | 2025-07-24 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| c5d04d59-9351-31d8-8acb-4676a6291a36 | -3.1832 | -49.4642 | 2025-07-24 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 7cc59d12-96f9-3bb7-8301-ca39f3ff75a3 | -3.1649 | -49.4435 | 2025-07-24 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| c984b491-3cb5-377a-98c7-0d814dc5108c | -3.1648 | -49.4648 | 2025-07-24 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| b9bae262-73e9-334e-abae-fc2c25d376bd | -7.2594 | -43.0881 | 2025-07-24 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 5356a97b-a20f-3327-a012-145b9d72582b | -3.1833 | -49.4429 | 2025-07-24 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 8eb7bce0-4397-3a40-9cf1-059461e969b0 | -3.1648 | -49.4648 | 2025-07-24 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| f7c3faf2-2b30-3a04-bb1b-2aaea13e977a | -7.2597 | -43.0645 | 2025-07-24 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 9c9a6276-cf11-3787-bd79-9e9cc79ad4d8 | -3.1832 | -49.4642 | 2025-07-24 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 8646098b-eef2-3325-a804-b41d44243c1f | -3.1649 | -49.4435 | 2025-07-24 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 48d2bb49-2a48-343d-90cc-842aa2f5b70d | -7.2594 | -43.0881 | 2025-07-24 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 2b00aa01-b383-3b9e-9217-006135a79471 | -3.17578 | -49.45269 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| eac95815-082a-3035-931a-ffd37bac62f3 | -5.68604 | -43.67135 | 2025-07-24 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2efe1f0-ab86-31ef-87d4-ea0d1c78b6fb | -8.51717 | -44.67776 | 2025-07-24 04:40:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 025faaf5-5330-39da-90a3-08d98ed8bbde | -0.74908 | -47.75614 | 2025-07-24 04:40:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 408e98e4-c4b2-3de6-8892-de890eeaf64a | -6.91525 | -38.5598 | 2025-07-24 04:40:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 47d778ff-c3bd-3f0c-bf68-4dcd612e6425 | -3.35534 | -47.16149 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01abe0ec-05cf-32d8-b8b7-eb8bf6a29b6b | -3.04937 | -47.37624 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c414b134-f36c-386e-b206-79380cf23f46 | -4.8085 | -43.21382 | 2025-07-24 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 80946409-e4ed-3457-9120-67f575a95274 | -6.96502 | -44.37066 | 2025-07-24 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaf2253b-138f-34f0-a580-ec06a54fa991 | -3.04149 | -49.44239 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 991fbd3e-b086-3b28-93f4-531b0f6c9ade | -4.10313 | -48.20525 | 2025-07-24 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c12877b-f59c-33ac-94c8-003790b67f58 | -6.21083 | -43.73413 | 2025-07-24 04:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| efb385c3-225c-37c7-a7f2-55195877ad78 | -7.2476 | -43.07299 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 9806dc77-da44-3b42-8579-8ee319042e96 | -7.45817 | -49.40046 | 2025-07-24 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f798bf81-d4f7-3e19-8836-806711d2939b | -4.0507 | -42.5104 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4f27c8f3-66e6-3332-9bc9-53fab46cef08 | -3.17467 | -49.45967 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e24daf0b-bd9d-3b33-92ee-dbfd5a0d0abd | -5.5034 | -51.13968 | 2025-07-24 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66d93334-598f-3751-8b19-a56e8dac5d16 | -5.47839 | -42.14782 | 2025-07-24 04:40:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8cced120-e652-3688-be0b-5bd53a3e7366 | -6.97207 | -44.37936 | 2025-07-24 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e546d71-c0f8-368f-8735-6e9ca8868f15 | -6.13567 | -42.96185 | 2025-07-24 04:40:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b12d7062-9681-3aa0-9dcf-ca0ff3d17948 | -5.88754 | -45.19369 | 2025-07-24 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51d2ddb5-65fb-3b06-a717-25db30708e90 | -6.38963 | -45.31438 | 2025-07-24 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 723420a4-d356-35cc-a4c5-c6a803188f0b | -3.46299 | -47.6752 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fce1e49d-938f-3400-8f33-af5b1b65f921 | -3.79621 | -41.00523 | 2025-07-24 04:40:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d0f500ec-4635-33ee-af75-70724acc22b2 | -3.17522 | -49.45618 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e3ca3d2b-9e6d-318d-8bd8-b99852a652ba | -3.93792 | -41.49319 | 2025-07-24 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c2b3f286-abb1-3179-87a2-73745d574d77 | -6.82929 | -43.06026 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d82be27-dbed-35f3-82ad-201a6fa25b32 | -3.07826 | -52.43383 | 2025-07-24 04:40:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7af75a86-b066-3c7f-b107-517b290a598c | -7.45762 | -49.40393 | 2025-07-24 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da83c533-0755-36ed-8ca1-15061c784dda | -3.9752 | -47.881 | 2025-07-24 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README14.md)
