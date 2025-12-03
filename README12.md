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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f7d82ae-4034-36e4-9372-50c237def22e | -3.2345 | -45.56473 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| a4815c8c-8527-3466-bcf7-b9e007dad9e5 | -2.35501 | -50.11301 | 2025-12-03 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbb9bac6-2ea6-3e76-ad47-0d1e07b0e321 | -2.9396 | -53.28295 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e6f216a-1eb3-3543-a46a-23eb1c003a39 | -2.69848 | -49.31658 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aaae453a-4e2b-3160-b5c6-0c3c07b06e73 | -2.78982 | -47.42865 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 620dc967-0f01-3bb5-a3f6-7621470c5a96 | -4.40324 | -41.4521 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5c71dc03-f725-39d0-a496-c8c83fe21422 | -2.4123 | -48.64658 | 2025-12-03 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30d375b6-67ff-3341-afc0-a442de19eda1 | -3.86793 | -40.64557 | 2025-12-03 04:38:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bfed1075-fc68-3097-b55b-79c101cdda41 | -3.25729 | -45.57074 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8f5faa3-21a2-3343-9bc8-67f6f651b372 | -3.73468 | -49.86608 | 2025-12-03 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8075902-81d5-39c8-b888-a2e6ea1a381a | -3.22083 | -48.61241 | 2025-12-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a698eb4-1e25-3a59-b2f4-3855f2c0d9d4 | -3.77336 | -50.13636 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff3dcd68-a151-3600-be62-c618f2efcfc0 | -3.32185 | -42.49813 | 2025-12-03 04:38:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b66ee5b-d05a-39a9-a5d2-cb9491869475 | -3.90871 | -50.31815 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cccd9aca-37f0-30fe-8092-60010883e40b | -3.36291 | -46.85481 | 2025-12-03 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3275f92-7242-3fb5-a6fe-38e844021fe7 | -3.9177 | -50.31641 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 278dacc0-5f57-33c9-84eb-455946d40f31 | -2.04206 | -46.59524 | 2025-12-03 04:38:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b29c5053-6ec7-3a7a-a03f-105e582c24f4 | -3.29438 | -50.09371 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 852eeb36-1b8c-3abe-9c5c-be030ca8dda4 | -3.67363 | -48.93335 | 2025-12-03 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22f73af4-66e5-3e1d-84c1-fc0282e4ad9a | -3.30748 | -42.50452 | 2025-12-03 04:38:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 61e630d0-9731-3f10-817d-44d9779e7c4c | -3.86332 | -40.64196 | 2025-12-03 04:38:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| be8a96d1-bec1-35d8-912d-c7d1f3ed874f | -3.43271 | -49.23444 | 2025-12-03 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f2c6701-39c8-3089-a47d-02edc1142345 | -4.43008 | -45.95573 | 2025-12-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a7b5a94-59e9-3278-82cc-926fe784dca4 | -3.23116 | -45.53873 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f04fd548-be9d-374d-b31f-17172bc26f86 | -2.02658 | -47.89619 | 2025-12-03 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b2b7960-3552-3d5a-9e65-c6bf7e807081 | -3.0621 | -49.51317 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2e6b244-c6f1-38d7-9ba7-a9086ba5d36c | -2.63694 | -48.03712 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e03bc09a-02bb-317f-9d43-06b9188b3456 | -3.2452 | -43.29106 | 2025-12-03 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c710ec3-ac85-3cc0-993c-01cf366a2c50 | -3.23089 | -45.56418 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 41f35924-6a8d-3acb-82bb-f122589a962f | -3.32122 | -42.50239 | 2025-12-03 04:38:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bdb84dd-9ecb-3440-8278-45a773653b60 | -3.22432 | -45.55895 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41dadbc0-bab2-395e-8330-13fc5f35fd58 | -2.92309 | -48.23032 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96ed0a40-1d57-3695-bc38-62c2444aacc5 | -2.88817 | -39.90666 | 2025-12-03 04:38:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 171fc4bf-a5ef-38ce-93c3-3a0819fb5597 | -1.98652 | -46.47762 | 2025-12-03 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eccce044-d578-3876-8ec6-3e2bc8380c35 | -2.84329 | -51.06061 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b92573ea-ce69-30d3-9b5a-da7da8c288e0 | -1.14872 | -48.09309 | 2025-12-03 04:38:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 95198149-2d2b-3aec-b02b-9219acd98c8a | -2.98023 | -49.51419 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8c893b8-1383-3ba6-beec-611274384060 | -3.66789 | -50.48794 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4aea7c45-0611-3fc3-9704-74e96e61d90c | -2.62196 | -45.14325 | 2025-12-03 04:38:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dae6a8dc-b9fe-317f-ac78-ba81cf8e094c | -2.85183 | -46.73621 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5ece307-7478-341f-a65e-59ae23eede69 | -3.67529 | -50.44081 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27071485-8510-3c84-a207-ea4957f193fd | -4.58359 | -45.9272 | 2025-12-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a7c3d6b6-e340-31fc-abd0-aeb18be93acb | -3.23439 | -45.57567 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a3c90ac3-3740-31fd-831c-65716fa15954 | -2.69902 | -49.31311 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73c8e32e-8c02-3de5-bc13-c9d60419187b | -3.56436 | -42.70715 | 2025-12-03 04:38:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1747f3d9-867a-3c5f-ba48-b5379abd80ea | -3.24577 | -43.28733 | 2025-12-03 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23d741a0-01cc-35ae-9fe9-230769952b81 | -3.23412 | -45.54343 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df2da641-0094-388f-ba67-88cb00524ed2 | 1.99602 | -55.71247 | 2025-12-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fd1c227-8637-3636-a7dc-39f16ceaf57c | -3.25792 | -45.56657 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b710120b-1732-36ef-bc2c-f713f15cc070 | -2.92819 | -45.46238 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d17d72db-568a-320b-8f8a-c4c11ad4d870 | -3.24599 | -45.54766 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93f781cf-9e2a-3109-ad66-0ed019ea5893 | -2.91978 | -48.2298 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7837610c-c163-3e64-8874-a0dd63052dba | -3.85028 | -47.06026 | 2025-12-03 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa6d0e66-a0b8-3d29-bf0f-2c7089c87a56 | -2.70566 | -49.31414 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9bcc14b-977c-34f3-bbe0-bf6f012cc108 | -3.24277 | -50.15888 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7ad7b152-10ce-3125-8b58-1ed03395a956 | -2.9891 | -49.52271 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f7a5f1f0-2354-37f7-8ceb-334bc26caa1f | -3.22744 | -46.8686 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4094775-fc34-3dda-ac70-15a17be48296 | -2.63912 | -48.54539 | 2025-12-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 110e6b90-b66b-3c9b-9bfd-cdff981e4125 | -3.60722 | -50.36716 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8965cd9-587c-39ae-99ea-11d9d2227d8e | -2.896 | -53.30437 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0f09ca3b-8085-3f7c-9fcb-4fe001ee24ef | -2.35896 | -50.10993 | 2025-12-03 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c409ecef-8994-3348-8b90-90e3328da409 | -2.34756 | -47.16396 | 2025-12-03 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 806e4cae-332a-38a3-b7d4-c7b36169c860 | 0.75781 | -50.81274 | 2025-12-03 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e765234-6cf6-3889-be79-cd63200a8564 | -3.37675 | -50.31627 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b01c228-3fd9-30d4-95f3-cc0f62b7a4f1 | -2.62761 | -48.05336 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4414743b-cb04-3c1b-adb4-fb58ec2ee8de | -3.23681 | -45.57359 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 267bbfba-1598-3e29-aa19-73f6fad9e773 | -3.85894 | -50.50245 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f8afc38-9ded-3a0b-83a2-0bbdbe6c0ee4 | -3.22895 | -45.57663 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9461669-e017-3946-b7e5-cdb913fec6a9 | -2.95624 | -47.36711 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92aea763-9a86-3d8d-b574-2e321c1e34f3 | -4.40802 | -41.45369 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6b8b87a9-a21c-3cec-812e-1902d67d260f | -2.72566 | -54.44142 | 2025-12-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a08421f2-cb93-3c04-b9f7-cde4c7f8e8d4 | -3.86364 | -40.64166 | 2025-12-03 04:38:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b1b10c68-a5a1-3cfc-9b99-dcebc00dadac | -4.57935 | -45.93082 | 2025-12-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddc768a2-abd5-33a1-a3a7-ea14da4928c4 | -3.38589 | -50.00655 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b79554e-1b31-3caf-9fca-0b0f48a7ee7b | -5.67215 | -39.60103 | 2025-12-03 04:38:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b8130ffd-69d1-3234-bc55-447676a3e979 | -3.86823 | -40.64524 | 2025-12-03 04:38:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8cca5cd4-0421-3f21-b006-369f7b854ef7 | -2.6364 | -48.04058 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e586c44e-7269-3b31-ab52-d4069b9f2c64 | -3.01207 | -50.26328 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8842265-b749-3ec8-91ac-9c8ce0cabed6 | -2.20421 | -47.99791 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ff30a9dc-253f-3e69-8655-946d6d7c5e3d | 2.87855 | -60.26164 | 2025-12-03 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8d77aa66-da65-30fe-b64e-7b2a2bc5ec19 | -3.23941 | -45.55698 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 13b9fcd1-0ca5-3a9f-99bd-b70631539168 | -3.23515 | -45.56058 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 010076ae-78bd-3a61-b747-d893fecbea89 | -3.78072 | -50.00322 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8df027c7-113c-39cd-bfca-ed95cce1be00 | -3.25243 | -45.57847 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8eb8355-9661-304b-ac28-40003f7f48f4 | -4.34359 | -49.9515 | 2025-12-03 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a89bc188-267e-39a3-8c32-2771545bf728 | -3.22496 | -45.55481 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c303aeb1-af8e-35d9-ae92-f10e7e2babda | -3.00869 | -50.26278 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 379cba95-9e08-3cb4-94fa-1bbb00db51af | -3.51901 | -47.20396 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edb25599-b577-3e18-bfce-171b67bd274d | -2.93877 | -53.28807 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3a86a80-c65c-3a8e-8df3-3081be784852 | -3.25557 | -45.55769 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5df4442d-512a-3748-b7ea-f485444eb19d | -3.22303 | -45.56724 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95683116-9f33-3261-beaa-60f54b2260a3 | -2.96015 | -47.36409 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82eeb7f3-f83b-36dd-bd0b-745508a91ef7 | -2.03987 | -46.42806 | 2025-12-03 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6c72fa4-27d3-3989-877a-c62c93f2c348 | -3.53145 | -49.9856 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43f933d9-47ea-3a7c-abb0-3d724a10bff6 | -3.22986 | -45.54705 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9c9fe13-76c3-32b9-b823-5404b69246c6 | -3.44506 | -45.39199 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6d3a59f-cc45-3d2b-bf0a-f71fdf8b69da | -6.26081 | -37.23215 | 2025-12-03 04:38:00 | NOAA-21 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 682c5971-cac9-3cef-ba56-494b518fbf5e | -4.76232 | -46.08238 | 2025-12-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2835dafa-f6f1-361a-91d6-0d99271cde1d | -3.566 | -47.17733 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 244ed915-f4dd-3dfd-88b2-38b2a970feee | -3.9884 | -46.75774 | 2025-12-03 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README13.md)
