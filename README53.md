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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 619db2bb-a459-3b51-a398-860b8eaeee49 | -3.07043 | -54.37523 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbe576de-c588-34ab-a388-45218a6219d2 | -2.24856 | -48.7486 | 2026-10-01 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d7c510e-d98d-3d35-a0cd-fa36f367062b | -4.38918 | -54.8313 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d37a4037-c8d2-3308-9ae0-ede12f15c3ff | -3.29234 | -45.93673 | 2026-10-01 04:32:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| baa605e3-b233-3fd3-9c50-f8d196dbbd95 | -3.1736 | -54.09935 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 9c388616-1535-3853-bee6-62c5ef3160c9 | -3.1072 | -48.67644 | 2026-10-01 04:32:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01e689dc-ed93-3def-b801-b40ec858e273 | -2.90327 | -54.14755 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e0dc6b02-e89e-37a7-8ca6-ec1b44d5165a | -4.27234 | -50.74106 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb557e08-c96d-31c9-a068-248314444814 | -4.29244 | -50.7916 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 51e31966-bacb-375d-9546-49a374024e79 | -6.70619 | -45.9811 | 2026-10-01 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95f3ae4e-3975-3cf0-80f0-4067148f3dde | -4.29671 | -54.80374 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 913b680c-56e1-3ff1-988f-4f2ce841f3d9 | -4.3046 | -50.76737 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d938f439-5a88-3054-b275-2457f8d82fbd | -3.34493 | -42.40595 | 2026-10-01 04:32:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fbcabaa5-aa9d-372b-bd44-1ceb08b4ad70 | -4.28365 | -50.79541 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 077e85eb-d033-3183-a16e-a823801e97f4 | -4.26666 | -50.75066 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8c5be9fb-cfb1-3a09-8ee9-a573d27aeb70 | -2.22111 | -46.0712 | 2026-10-01 04:32:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08bbb13a-62eb-34d8-a8a2-3ad035915536 | -4.30606 | -50.78325 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3d9d2a5e-6c6d-33fc-ad59-b7e5bb48f89d | -4.0575 | -51.1015 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4244d19e-6e86-347d-8058-15ee2b886d02 | -4.31315 | -50.78971 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 11346bed-d328-3e55-bc3f-ee560d181028 | -4.27074 | -50.75999 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 2e4545fe-81b8-3149-8f64-8bad5d509e30 | -2.97759 | -51.05153 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40e10aa7-ac48-36d5-9112-1039db1f8352 | -4.02345 | -54.20141 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 415fcf57-a23d-3051-bd2e-f311d2425ae4 | -4.25884 | -50.75803 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| da05f7cc-c530-379a-8908-ec64a5336e4e | -3.58955 | -54.55661 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e595dd66-2195-37f8-810c-3919eb699b01 | -4.27741 | -50.78387 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 11ad057d-9849-35fd-bc15-667f944b6817 | -6.19226 | -44.85336 | 2026-10-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e72e8ba6-43fc-3540-8d22-9a07144b2b1a | -5.11999 | -56.01185 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9fca85b-80fd-3c30-99ee-1a9cf3991c4b | -4.27544 | -50.74684 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 6a5182c1-7a11-3107-8e1a-1cf2afcf0ffe | -3.25162 | -48.77412 | 2026-10-01 04:32:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a931c27f-9bc7-35e8-92dd-5f043876bd91 | -4.25966 | -50.7529 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 10201523-20cf-3eb4-908c-85cc98577623 | -5.43019 | -43.44948 | 2026-10-01 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b75a2fd3-7460-3eed-9f81-c3ea330b1183 | -3.01355 | -53.88422 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b3f60bb-ebe2-3df0-ac85-4243fc53e748 | -3.15984 | -54.08807 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a3d2f73f-9b6b-3741-9d84-fb2812260ab1 | -3.10119 | -50.28862 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d85ba05d-5eb7-32ec-b7bf-8dc7d718f48d | -3.93192 | -45.41672 | 2026-10-01 04:32:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 444139f1-7f16-3f60-8742-91d4fe257e8c | -3.95266 | -49.05085 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3180c80a-51b7-39be-b7ba-5db1dae30e28 | -3.173 | -54.09487 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8e5d8494-0f0d-3205-89a1-0ed386a3cef4 | -4.06097 | -51.10583 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49fef0f0-d402-3534-b7d3-074955a12400 | -1.41986 | -48.9 | 2026-10-01 04:32:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da637d88-d04f-34e9-b3a9-5a15a8a2d7e5 | -2.29567 | -48.75608 | 2026-10-01 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6be74a9-3e59-3183-b3a9-868def041a25 | -3.29955 | -53.86193 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c4592998-a8c4-3641-a67b-0c7c99ce5fed | -3.10902 | -50.28993 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5dee78d3-6eda-3067-96d3-25a8389adcb1 | -1.46119 | -48.91863 | 2026-10-01 04:32:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 658f9d4b-2294-3433-82f1-2178fb025fef | -2.37778 | -50.40963 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61b6c7e4-225e-3bb8-b055-f33bbcb80d6e | 1.87611 | -55.64469 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 470eaaf2-561b-303f-9127-b596241ed0db | -4.30629 | -50.75715 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e3a7f7d-7b31-35f1-9137-7fdceebaf8ea | -3.10749 | -50.27446 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 247b21a5-74a8-37f1-aecf-80746f0f2e73 | -2.44309 | -49.22038 | 2026-10-01 04:32:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d95f742e-5d66-3700-aeed-87bd270d2878 | -4.28864 | -48.60915 | 2026-10-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46c31054-a422-3844-b055-3a90ed2a541f | -5.74386 | -45.16597 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| be576ca1-e8fe-36fb-8a6f-ebba87bdee90 | -5.74161 | -45.15838 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a9afd2e4-2ec0-3a4b-8a75-865c26a2e972 | -7.02265 | -45.27989 | 2026-10-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2115932d-181b-3731-9b37-4774c6d93b0a | -3.18653 | -49.25158 | 2026-10-01 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c86d8c52-0278-332f-932b-628c12ce0f30 | -3.10071 | -48.67123 | 2026-10-01 04:32:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a79f874b-72cf-3031-8820-5f5a604fe5bc | -4.27568 | -50.79421 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| d7aa50e2-9f30-37a1-992f-d0c7689f555f | -4.29583 | -50.77112 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 912ad924-d8d3-39ca-9212-84e4291c0cc6 | -5.25104 | -43.57759 | 2026-10-01 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40f3a89c-e0bb-3f1b-aed8-8bbc6a5ed6dc | -3.98777 | -49.03949 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64ff24c7-6325-3a30-99ff-295d795aa95a | -3.1043 | -50.29421 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fad4f851-f608-3002-8da3-eb1087abb9c3 | -4.30689 | -50.77818 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b776458c-add3-3140-af71-8131dbe8f33f | -0.44436 | -52.00689 | 2026-10-01 04:32:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13ac697a-60dd-3112-bd0a-b161ed177573 | -4.26496 | -50.76078 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| aaa887cf-3404-3e6b-874c-b72dc552296b | -4.1288 | -46.87502 | 2026-10-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddad2ad2-2bd2-3a8b-89d8-47d95c165794 | -4.26945 | -50.78263 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 08276f4d-100b-39f6-9b4c-49cece0664bc | -1.83022 | -54.99354 | 2026-10-01 04:32:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ab84ed7-f5f2-3d5b-b219-daec3eb4b8b7 | -3.59419 | -54.56075 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88eacaf0-9af6-3ba5-98ae-a7bee4cb91aa | -4.29662 | -48.62657 | 2026-10-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d071653-8611-3039-a109-4d680d280e22 | -3.38022 | -50.95867 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bb152ad-88ac-3f39-9f3e-32aa4051b473 | -4.28052 | -50.78968 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 384b1211-285e-3f33-b35e-4e8b177652e2 | -4.26581 | -50.79075 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3480fed-ecb6-3777-9395-5efbc4def6d1 | -2.90756 | -51.32345 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 824476a5-587f-3069-9b6b-3ff05e09fdf6 | -2.91177 | -51.32413 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 023cbe8f-9ed7-3bfa-94e1-62cf7fc8e350 | -2.83072 | -50.46826 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3a8b3201-d2f8-3a72-b92c-5021ddd05305 | -4.63818 | -50.62235 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38e13148-abe8-3571-be28-c1e1c3920242 | -4.15824 | -48.8965 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7636fc66-766d-30e2-8f0b-a14b5267ac19 | -1.44709 | -54.46376 | 2026-10-01 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d174f254-f499-3cfe-a1b9-5c3224a39ba6 | -4.30293 | -50.77751 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d669d484-0910-3319-9326-8c08d4f0e4a9 | -3.25814 | -52.59193 | 2026-10-01 04:32:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 931de65c-695f-3a67-a6aa-b4485b62b0d6 | -2.89767 | -54.1497 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d8eaa371-800a-3452-8793-bc8411ba2e96 | -4.63429 | -50.62158 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a162647d-a429-3324-aa34-a84ba218cf68 | -1.83083 | -54.98994 | 2026-10-01 04:32:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1bfcd07-05c8-3e6c-9b10-a9da21dbb11f | -4.25648 | -50.73857 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 470baf94-37dd-3eb7-816d-0d372d1bfae9 | -3.29054 | -53.85461 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 8fa10e40-2b99-3875-a482-ade8b274e0eb | -3.95735 | -48.12725 | 2026-10-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 01d927ac-1e57-3b7c-b893-03a7d103d5be | -6.38716 | -45.80615 | 2026-10-01 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0526974f-f866-3227-a394-a30a696602b2 | -2.96823 | -51.03104 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8e58c4c-4aa2-3566-8c75-eaed9bb8fa0e | -6.32169 | -44.44424 | 2026-10-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdf61d0e-4a94-3056-8c73-fe606d2b0ac1 | -3.29458 | -53.86108 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f6bee087-d4a8-3a0d-9ed3-8c2c32406c17 | 1.79075 | -55.65461 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43901d2f-9616-3f57-a055-439a77c952c8 | -4.29526 | -50.75005 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f5a44bc-df88-3ee0-ba8e-ecffc10de471 | -4.25733 | -50.7335 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b169bd01-d748-3841-b5ba-048e13a6cf14 | -3.01394 | -51.46834 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75e2acec-2b74-36b2-8b85-1f4750e23535 | -3.93469 | -45.4207 | 2026-10-01 04:32:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02d67c82-c5b3-3f69-9a0b-0aebb44abe77 | -3.03093 | -53.87245 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43fc0451-c3d1-3fae-b6a6-59cd8c1aa57b | -3.37616 | -50.95796 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9213d0f-9f69-3c08-9a1d-27f4f2881291 | -2.41932 | -49.29826 | 2026-10-01 04:32:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7c53bae-1e43-334c-80ca-2b10402391c0 | -3.8495 | -55.80839 | 2026-10-01 04:32:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64104a5e-d9e5-3102-96e2-9bd349a95aca | -4.29102 | -50.77555 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| f159f34f-51d3-3fc8-8aa5-d236dc2bd443 | -5.57855 | -42.73378 | 2026-10-01 04:32:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 114c11e3-60b2-30c1-9db5-6b6a01e520bc | -4.29751 | -50.761 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |


[Clique aqui para ver as próximas entradas](README54.md)
