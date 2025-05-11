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
| 0af2854c-8d22-327a-8576-a1f9c1370b01 | -20.18829 | -46.71025 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6efe0e2-0cd6-3618-872b-17108bc47405 | -19.50821 | -40.6484 | 2025-05-11 04:04:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 594682db-6225-372b-86ec-3b8146fedad8 | -19.43841 | -44.34041 | 2025-05-11 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5478a78c-990a-3275-b2e0-ebd9f3c7cee9 | -20.99527 | -51.79356 | 2025-05-11 04:04:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1e71a9f4-2bf6-3c7c-9346-baa5456cc55e | -14.66784 | -45.13282 | 2025-05-11 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db7eac7f-c483-3c5f-9af8-c7d8e144f06f | -13.48324 | -52.97237 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 13bfe76a-eb4a-31cc-bb90-2a6a72330f98 | -21.5424 | -45.40019 | 2025-05-11 04:04:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d1576f62-0b25-322a-8904-065c652758f8 | -15.56929 | -47.85444 | 2025-05-11 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d7316f8-b3a1-3c89-8f76-13cbd499df4b | -20.35042 | -40.35922 | 2025-05-11 04:04:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 22cf93c0-aa75-3a1d-8fd9-ae84787ea54e | -20.41643 | -43.55257 | 2025-05-11 04:04:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7e62b811-7ed2-378a-af8a-42374f48038e | -20.17697 | -46.81618 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6dd63bda-23eb-375d-8455-67d845ee5d39 | -20.17419 | -46.81057 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d12c810-6e0e-3942-97af-2479b1451cbe | -13.04813 | -53.71656 | 2025-05-11 04:04:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 92e8a3d8-ed4f-3f51-8896-04fb7ae6d369 | -14.21788 | -54.56409 | 2025-05-11 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fde69d1-c89f-3534-8aba-ee9d5c1d5cd7 | -17.46225 | -44.71845 | 2025-05-11 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 845cf188-476d-312c-a8f0-16a669e87235 | -16.10541 | -47.54757 | 2025-05-11 04:04:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 699cf56e-3636-366c-b7dd-204b1b2252cd | -13.04595 | -53.72701 | 2025-05-11 04:04:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 69ca7edc-abbc-3b74-8888-52fff8f3286c | -20.17617 | -46.82067 | 2025-05-11 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 307a6d3f-cbd2-3292-8a88-099a04ec84a6 | -13.47536 | -52.98002 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0d5ea462-1430-3a64-b4d2-71e39f3aea7f | -20.57815 | -44.57584 | 2025-05-11 04:04:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fa1cda95-4561-3269-a07c-c6c15d0b35c1 | -13.4873 | -52.97527 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a610bcd2-b4da-35b4-93dd-24548f7f30c0 | -14.66062 | -45.13153 | 2025-05-11 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a50a954b-1e66-3913-b3d6-80b0cea71d59 | -20.59901 | -47.61418 | 2025-05-11 04:04:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c0a8f62a-0c39-3417-8f4d-aa4449a2d141 | -13.47723 | -52.9711 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b2d55fa4-1f49-39df-9335-62fef2448385 | -13.47818 | -52.96658 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 999cb177-006f-368c-a607-b7db2c0a0853 | -14.21917 | -54.55822 | 2025-05-11 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83203c51-62f3-32ad-b133-07ad5eb13dff | -14.67218 | -45.12922 | 2025-05-11 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7eb56ddc-8f73-3b8a-bb9f-0eb0a1a9abb9 | -20.12002 | -46.88014 | 2025-05-11 04:04:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 295a2afa-b454-38b5-9209-052d70eb1b5d | -22.12945 | -44.46211 | 2025-05-11 04:04:00 | NOAA-21 | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d3c9d136-1d5e-3edb-b27b-32ff642e4ad9 | -20.12058 | -46.88224 | 2025-05-11 04:04:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1768a578-9582-37de-b13b-bc6d43f66df4 | -13.48232 | -52.97677 | 2025-05-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8260a0d0-5589-3fdd-aa2e-8a7b708cbe98 | -13.04704 | -53.72178 | 2025-05-11 04:04:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0e0c4f20-46cc-39d7-abfe-e1fb101235e2 | -14.66349 | -45.13647 | 2025-05-11 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1d75a0e-a058-3dd5-860d-5c06b49d0a98 | -24.24338 | -50.73921 | 2025-05-11 04:06:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 60d0938f-34f3-3e4d-92dd-2ef7e77f770f | -25.19138 | -49.32469 | 2025-05-11 04:06:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8fd7a4fd-e29a-3d59-8a33-b0d29bce71c4 | -23.98656 | -48.91806 | 2025-05-11 04:06:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53200294-3f41-3310-a6ff-67cd9c9ed71c | -30.70424 | -53.8254 | 2025-05-11 04:08:00 | NOAA-21 | LAVRAS DO SUL | RIO GRANDE DO SUL | Brasil | 4311502 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 4232d3cf-4b7f-3bdf-b718-f7eb0cfbd8cb | -30.70986 | -53.82156 | 2025-05-11 04:08:00 | NOAA-21 | LAVRAS DO SUL | RIO GRANDE DO SUL | Brasil | 4311502 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| 6c0ac47f-3585-3e99-966f-c92c1dc54e0d | -6.5631 | -51.1126 | 2025-05-11 04:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 80d2af6d-6c62-3a03-851e-6418fae9a3fb | -2.38599 | -51.89373 | 2025-05-11 04:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4e74e6b-9899-3d8d-aff5-34e1e527f615 | -2.38527 | -51.89815 | 2025-05-11 04:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d18e054c-7217-33f8-b835-c167b6c4ef56 | -9.67571 | -49.72413 | 2025-05-11 04:27:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a1111a6-5f7b-307a-a53d-5bf620669713 | -8.46635 | -49.61631 | 2025-05-11 04:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1466b2ea-21bf-3944-acba-baf84823adc1 | -11.61369 | -48.00843 | 2025-05-11 04:27:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8986ae0f-200f-32cf-8ed5-996245092bd1 | -12.1138 | -47.98771 | 2025-05-11 04:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98adb21d-5c64-3308-9f50-62bcf17faa4c | -12.32774 | -45.70047 | 2025-05-11 04:27:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fc54264a-639a-31eb-ad85-eecff7ea5653 | -11.11911 | -43.3391 | 2025-05-11 04:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dba3d6dc-b07b-3b60-83b2-1cc3132f2b4b | -13.02348 | -43.59595 | 2025-05-11 04:27:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb8a5afb-ba55-3d16-9fa7-3640596823c7 | -10.71714 | -46.70301 | 2025-05-11 04:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5bf38c4c-015d-31a6-9aa2-58cfb624cb51 | -11.40296 | -52.94965 | 2025-05-11 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79967546-9add-3b57-9821-d956275805f7 | -10.49789 | -42.39693 | 2025-05-11 04:27:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0646b82e-bf3f-3bcd-8244-9705877d5a40 | -12.10771 | -47.98309 | 2025-05-11 04:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23624b1a-2071-3799-83b6-a4d692999505 | -12.11104 | -47.98363 | 2025-05-11 04:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92396968-a335-33e8-89d9-9621e9dc06bf | -11.60702 | -48.00734 | 2025-05-11 04:27:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13da7a8f-3010-3d3b-a72b-6eab75c525eb | -10.50189 | -42.39751 | 2025-05-11 04:27:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fae385d1-9cd8-3277-b718-038129ba2467 | -9.66084 | -45.23299 | 2025-05-11 04:27:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ffb57f7-5c12-36a9-a4a2-6201e5428ee6 | -9.67925 | -49.72475 | 2025-05-11 04:27:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a89c928f-091a-3bdc-8523-2664758a99cc | -12.1116 | -47.9801 | 2025-05-11 04:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3bf2450-a440-3f73-a0e4-7dd68fd92e7f | -9.60945 | -42.13763 | 2025-05-11 04:27:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 855ab56a-7f82-361a-b755-4408ee14adcd | -9.60777 | -42.14054 | 2025-05-11 04:27:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 33276663-ca7e-324c-b5a2-3671de61604d | -12.58606 | -48.33516 | 2025-05-11 04:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a75bcbe4-184e-317e-8b51-a6df9e97a829 | -12.76638 | -47.98889 | 2025-05-11 04:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 602f99f6-66ae-39c6-ace3-1776bc54b6a4 | -12.32831 | -45.69667 | 2025-05-11 04:27:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c398f6a-9e49-3793-9b01-50f160d1f660 | -12.48514 | -43.73317 | 2025-05-11 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02641623-8002-3d92-af9e-bf861b637f70 | -8.46992 | -49.6169 | 2025-05-11 04:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c8c586b-2bdf-326f-844e-d5f1f844be07 | -11.39396 | -48.70308 | 2025-05-11 04:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e03ab914-108c-3ec5-8905-283f9e2253b2 | -11.13728 | -54.22787 | 2025-05-11 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa48ae8c-07e7-354c-9bdc-196aa6c02adf | -11.3995 | -52.94509 | 2025-05-11 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20038eb4-bf5a-36ca-8909-49e8db18709e | -12.61294 | -46.74203 | 2025-05-11 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 06012c3c-b359-3bf9-b2b7-deabbce29be0 | -8.89916 | -44.7813 | 2025-05-11 04:27:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f60fb449-cd26-3032-907d-9484564e8901 | -11.39602 | -52.94056 | 2025-05-11 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d6af53e-ecc1-35fb-b94f-fd6ee2c2840f | -12.61574 | -46.74619 | 2025-05-11 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a1d2b44-f2e1-3d35-a596-f813cf1e2429 | -10.62307 | -46.36807 | 2025-05-11 04:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32cde9f9-133a-36e3-b7b7-50bd070e2c10 | -11.77938 | -48.69923 | 2025-05-11 04:27:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e764eb9e-e65c-3fe3-877b-b0f61c5b8f61 | -13.01964 | -43.59539 | 2025-05-11 04:27:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 838acb16-a067-3048-9a5a-3ba21870cf09 | -11.40016 | -52.94133 | 2025-05-11 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21a7bf57-15a1-3499-9786-0f62ed6bd9b3 | -12.79056 | -46.92567 | 2025-05-11 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06177aab-022f-3261-b7e6-8354f759c134 | -11.61035 | -48.00788 | 2025-05-11 04:27:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0ddf740-c469-373d-86c2-32d695757765 | -6.70958 | -42.12509 | 2025-05-11 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e0448f78-7739-3ada-8d43-6b163e2ebe76 | -9.60854 | -42.13531 | 2025-05-11 04:27:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ab4065cb-0688-3df3-a534-36351bfd7017 | -12.59274 | -48.33626 | 2025-05-11 04:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34d951de-35dc-3311-ba44-9ad3ec7b2fca | -9.57197 | -49.10384 | 2025-05-11 04:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d45bfbf-f7db-3f49-ae83-ee514477199a | -9.56851 | -49.10327 | 2025-05-11 04:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27e64eed-010e-3d2a-98e2-3b1e67a54c32 | -11.56343 | -47.87309 | 2025-05-11 04:27:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e16ae22e-ca08-311d-9c1f-afb64168202a | -9.67638 | -49.72013 | 2025-05-11 04:27:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f019cd3b-8be9-3225-9394-973d56620977 | -13.48499 | -52.97243 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60c5afcf-20eb-3edc-a563-d0c7ac23c6f8 | -13.0481 | -53.72193 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9088a041-3e29-3b40-8b5a-52af6f4a0674 | -13.98142 | -56.81225 | 2025-05-11 04:29:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 225eb2d5-867a-3082-8358-4ba6236c74d1 | -16.67989 | -43.88483 | 2025-05-11 04:29:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2837a802-bb28-3499-8fa1-4fa74f4f319e | -13.04865 | -53.72675 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 56fb39c3-5d77-32a1-8cf8-8bbde110a63f | -14.21513 | -54.58252 | 2025-05-11 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 981275fa-62cb-3f58-b9d0-836ef6fe9887 | -13.60133 | -48.94524 | 2025-05-11 04:29:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5409908f-b5f5-3c23-a6bb-fa91d3fe8760 | -13.48561 | -52.96891 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 39a292c4-9512-3be2-802a-2146aad47675 | -13.0424 | -53.72906 | 2025-05-11 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1af1e6fd-d211-3e83-b787-927b0062bd5d | -17.04408 | -49.06008 | 2025-05-11 04:29:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8d25ae46-f97e-3053-b0c7-b16069e1fc24 | -14.65082 | -45.13752 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2932590-5a38-3843-90e0-9549709cc081 | -14.67099 | -45.13002 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bdbc8147-bf79-3ba7-9f1b-2890e09cdb7b | -13.47975 | -52.97866 | 2025-05-11 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8383abad-087e-3bcc-b9c0-5f9dc1269eb9 | -12.72514 | -54.97184 | 2025-05-11 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe22e554-db9d-3016-8abf-e59b9c19f04b | -14.66225 | -45.13493 | 2025-05-11 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README4.md)
