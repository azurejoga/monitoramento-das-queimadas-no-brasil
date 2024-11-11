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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ccd49ae-033c-3fa1-87b7-ecb844446c98 | -1.3873 | -52.376 | 2024-11-11 01:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| c39fece4-2f3f-3011-8870-80ba5136170b | -3.9483 | -48.1724 | 2024-11-11 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| fbfff330-489d-3f1b-9661-83963894fe24 | -4.1246 | -43.5833 | 2024-11-11 01:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 644bef28-0dce-385e-821f-e9243ea6e022 | -23.9169 | -54.04668 | 2024-11-11 01:53:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 9de3b133-a668-31c6-bfa0-7814c1679b5d | -23.92908 | -54.04395 | 2024-11-11 01:53:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 31.8 |
| beafec1e-ac0a-3d2f-80ac-b01fa39de384 | -16.08896 | -60.10418 | 2024-11-11 01:56:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b349bc74-14ee-3601-a075-42277b79491c | -17.5997 | -57.49883 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 40831e1c-ad42-3449-8aae-7e02f8d1be7d | -17.59122 | -57.51477 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| 3c7bbffb-785a-3f7d-aadc-3eed8f0057b4 | -17.62546 | -57.42976 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 7b8aa8bb-cc15-3a04-a20d-745bc49d7194 | -17.28772 | -57.48685 | 2024-11-11 01:56:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 87414cc9-1899-37f9-9ed1-bfbe09670f4b | -17.59313 | -57.43566 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| e20fd6bd-06a5-36a0-974d-9d304466fa3d | -17.62018 | -57.53168 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.0 |
| 8cd2c23d-ccc6-320d-9737-8c529f89dee9 | -17.29002 | -57.50099 | 2024-11-11 01:56:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 83f56093-421e-3ac7-b490-5aaf682b3c10 | -15.96889 | -59.32292 | 2024-11-11 01:56:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| c64e5c5f-9be6-34a7-8454-a8939df04c1b | -17.63317 | -57.54361 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 62f6a4e3-2a83-3c8d-aa40-b7859fa64353 | -17.63929 | -57.51387 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 2c0533ea-16a7-391c-a982-3cccd74c0210 | -17.60194 | -57.51281 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| d936c7fa-e566-3aec-8988-5112c245d3b3 | -15.9839 | -59.35519 | 2024-11-11 01:56:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 8806086a-0156-33b1-8369-445979aa82a6 | -15.97066 | -59.33426 | 2024-11-11 01:56:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 3f8e4985-ea67-3428-b207-300b44c66923 | -17.25297 | -57.47856 | 2024-11-11 01:56:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| dff4d3cf-0b01-39c7-bb28-f26a087213a4 | -17.59346 | -57.52871 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 164.5 |
| 5d39d2b7-5235-3307-ad75-fa195dbde3a0 | -17.24451 | -57.49469 | 2024-11-11 01:56:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.0 |
| 3b2b09ea-1612-3461-bc23-79cfdb56ac77 | -17.61709 | -57.53871 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| a1353bc0-b507-3b52-b8cd-2eff0d211be7 | -17.62248 | -57.54556 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.0 |
| 90b9d60d-c56d-3a22-8e23-e035c7c88144 | -17.61266 | -57.51085 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 4fdb626c-4688-37bd-8d0f-7b282f6c8d86 | -17.62778 | -57.44386 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 27a83b86-1680-38d2-95ab-b21815da6ba5 | -17.63088 | -57.52973 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 72047832-b9ef-32c1-85bf-44291caa85e1 | -17.30081 | -57.49902 | 2024-11-11 01:56:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| e6dd5c43-3e4a-3863-b354-8ef389617de4 | -17.28541 | -57.47268 | 2024-11-11 01:56:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| e3a596ba-e57a-34de-a8bb-1394415e9c23 | -17.29852 | -57.48488 | 2024-11-11 01:56:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| a486500e-7094-3ef8-9628-95ce5c4ed745 | -17.25532 | -57.49273 | 2024-11-11 01:56:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.7 |
| 88ea55c9-40c9-3f39-ad4e-0af24ca36999 | -17.61179 | -57.5475 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 5ffc94c0-9391-3b7c-9bca-13453e954bde | -17.5907 | -57.44262 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| cfce47b4-7a22-3ee3-91e7-c8e48ea6c124 | -17.24213 | -57.50142 | 2024-11-11 01:56:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| e0bfbd0e-4c08-3514-945d-769897dee8a6 | -15.98035 | -59.33229 | 2024-11-11 01:56:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 17d9e612-784f-3e77-98b5-c73be0ebc6f6 | -17.60484 | -57.50578 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 18f6dbc9-a1d7-3604-afd2-2ae3c55fe0c7 | -16.94652 | -57.65968 | 2024-11-11 01:56:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 730cdb22-734e-32a3-bb4f-0ed1b63c6163 | -17.6039 | -57.43369 | 2024-11-11 01:56:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.8 |
| bbb3d974-027a-30f4-a91d-b86850e59e96 | -13.48928 | -60.66951 | 2024-11-11 01:58:00 | TERRA_M-M | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 2af8bd60-1400-3062-b196-9dcbfde6e7e8 | -13.48277 | -60.66658 | 2024-11-11 01:58:00 | TERRA_M-M | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8b37fb4d-6c4b-372e-85fb-52b575c86f3b | -3.2352 | -50.3065 | 2024-11-11 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 6c176c29-7b90-3adf-bebc-8b8ef4889387 | -3.2427 | -53.0722 | 2024-11-11 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| a44a9263-1c4d-3675-8379-b330094ba6c2 | -17.2933 | -57.4857 | 2024-11-11 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.0 |
| ca65592c-f4ed-39bf-ad2f-a5006aec2793 | -3.2023 | -45.2482 | 2024-11-11 02:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| df83a63b-57ba-3e5e-9bc3-e18c4473f23a | -3.2428 | -53.0519 | 2024-11-11 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 980ea80b-b7ea-3139-ab16-19498c320f46 | -17.6086 | -57.4276 | 2024-11-11 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| cfdf59b5-c520-30cb-8c8b-2eb532cd3de7 | -3.2243 | -53.0727 | 2024-11-11 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 011150ac-c193-3892-af5e-5bc98b88b14f | -17.2936 | -57.4652 | 2024-11-11 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.4 |
| a04e0470-4068-38bb-9401-81a975cd53bd | -2.2298 | -53.6623 | 2024-11-11 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 50a5b5b8-0a00-3ca7-b946-0205f44abd79 | -3.0296 | -50.9607 | 2024-11-11 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| fcaa4e49-df2e-30d5-a980-27f7c787ae7f | -3.6217 | -50.587 | 2024-11-11 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a9fa3bb4-331e-3170-9d2c-7a57fdcca840 | -2.3029 | -53.8221 | 2024-11-11 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| e27697eb-56e4-3784-bcf2-a06ebffeb4f8 | -3.1983 | -50.2867 | 2024-11-11 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 232c5647-1575-3e65-aa2e-43112f776c38 | -3.2588 | -53.6994 | 2024-11-11 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b350911d-7079-37a9-80d0-3c20de71cab1 | -4.0294 | -46.9484 | 2024-11-11 02:00:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a07fa059-0cfa-30ca-b2c5-06b9ea8a1c00 | -2.8508 | -49.432 | 2024-11-11 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 951e2fc8-85e9-31c0-b50c-fa137db5b3d4 | -3.1458 | -54.4659 | 2024-11-11 02:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 85c10b1f-e414-319f-83ea-c727b36e63bc | -1.626 | -52.5362 | 2024-11-11 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ed7a3b01-bfe7-3fe3-b405-1ad546eef02c | -2.3212 | -53.8217 | 2024-11-11 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7f460377-a83b-348c-b3c5-afe54da0cf0c | -3.0295 | -50.9815 | 2024-11-11 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b89ca2fb-c325-30d9-93f0-27fc127b7176 | -3.2388 | -45.3818 | 2024-11-11 02:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| bf7b4a87-eea9-35b4-a5ad-fc322408dccf | -17.313 | -57.4834 | 2024-11-11 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| f254101b-4ccf-3e6a-88a8-c94b915576ab | -3.0213 | -53.2607 | 2024-11-11 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 004de1f2-a1c0-3a83-b7ad-59d804ed9371 | -3.0214 | -53.2404 | 2024-11-11 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c764e99e-853c-31d8-ade7-abde9d11f47c | -1.4057 | -52.3758 | 2024-11-11 02:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 38f567d7-056f-3264-acd9-70c7fcc0945c | -3.2168 | -50.2861 | 2024-11-11 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ca5ea702-244b-3d01-95f2-c073914b362c | -2.8508 | -49.4108 | 2024-11-11 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e447025d-6f46-3688-bb81-a5663e9c364c | -1.6444 | -52.536 | 2024-11-11 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ec60a476-f9d3-3edf-9450-a35e23da7024 | -3.1458 | -54.4859 | 2024-11-11 02:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| ce025bb3-719a-3c27-9bc6-fdf13c4d8ff3 | -2.189 | -48.3815 | 2024-11-11 02:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 8d11d05c-94d8-302b-9dd4-232d36ab3934 | -3.2024 | -45.2256 | 2024-11-11 02:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| dcc391f5-1e0b-3524-9f69-a306f1302edd | -2.1891 | -48.36 | 2024-11-11 02:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 994be6b8-4794-3a29-8704-cde6fb0ec516 | -4.0293 | -46.9703 | 2024-11-11 02:00:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5418ee3d-b2eb-398f-8f7d-3dbc97acb7cf | -3.221 | -45.2249 | 2024-11-11 02:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 6e19b71e-9deb-3feb-8b98-670f05ad53ed | -3.2244 | -53.0524 | 2024-11-11 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| fe51ed22-144f-3f00-b5d6-bc3f6725f2a9 | -3.2209 | -45.2475 | 2024-11-11 02:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| b9be3bca-29b2-3f58-8751-85d9af9e85ac | -3.5346 | -45.7061 | 2024-11-11 02:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e3b1037c-d68b-3f2d-8df2-14f5ade32e83 | -1.4057 | -52.3553 | 2024-11-11 02:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 4e1fd402-4edd-3dfe-b167-71f19d6326d3 | -2.76 | -49.32 | 2024-11-11 02:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 063a3d82-309c-37d6-8633-a921b95b6c4f | -2.76 | -49.37 | 2024-11-11 02:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33bd14f3-7f16-35dd-802f-cd48bd472e5d | -3.14253 | -54.48107 | 2024-11-11 02:00:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d7e70929-d407-300b-98bd-a774165e1174 | -3.14302 | -54.48833 | 2024-11-11 02:00:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 5ee2d3b8-abd9-3243-baa0-035e6f5cfdcf | 3.18766 | -64.20561 | 2024-11-11 02:02:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b88dc6e8-3124-35a7-a4ef-fc8d8f43aee7 | -3.0295 | -50.9815 | 2024-11-11 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2344731f-1a8c-3819-ad7f-7d6883387b11 | -2.2663 | -53.7422 | 2024-11-11 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 406f9848-391b-38cf-80a7-40135f47015b | -17.2933 | -57.4857 | 2024-11-11 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.6 |
| 7135f3ca-13e3-3707-824e-846e116ae9e2 | -4.0293 | -46.9703 | 2024-11-11 02:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| f6c19df4-9b2a-383d-a2b4-82c63fe76874 | -3.0213 | -53.2607 | 2024-11-11 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 96c8c654-c13b-3793-8dd4-8d1ddf11bc1e | -1.4057 | -52.3758 | 2024-11-11 02:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| bc8cc486-238d-3e73-b7bb-c097718a3b02 | -9.4762 | -35.8792 | 2024-11-11 02:10:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 124.7 |
| 00ff3307-1bdd-33d2-8a06-b31354d0748b | -3.2243 | -53.0727 | 2024-11-11 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| dd1f4b88-7e87-3e7f-9b29-e676f1409e0b | -2.1891 | -48.36 | 2024-11-11 02:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 87d9c9e4-85fc-37ff-9bef-12d572ee76d5 | -4.0294 | -46.9484 | 2024-11-11 02:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 0b739339-267a-3676-9b61-b3a60e6749a4 | -3.221 | -45.2249 | 2024-11-11 02:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 3222e0f7-6eb9-3814-9e4a-0b0fbd0e6421 | -3.2603 | -48.7368 | 2024-11-11 02:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 378ec728-1e5f-37f7-8539-5cfb2268a40e | -4.1116 | -45.6346 | 2024-11-11 02:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5090e95a-fc41-3ef3-b9c9-d7a6c3ff4dae | -17.2936 | -57.4652 | 2024-11-11 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| c4b02a2e-9560-3416-b955-6707fbc25c75 | -17.2737 | -57.488 | 2024-11-11 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| 61c98588-725d-3d9b-881c-5d4448bafca2 | -3.2427 | -53.0722 | 2024-11-11 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 43d8d7a8-517e-393c-b5f4-0961ddd9c899 | -23.9312 | -54.034 | 2024-11-11 02:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |


[Clique aqui para ver as próximas entradas](README21.md)
