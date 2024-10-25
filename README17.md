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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ca68390-ab1d-3c9a-be0b-7edbc0dbba20 | -2.6482 | -49.2465 | 2024-10-25 02:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b54bde72-fcab-3cb4-b13b-67a25f881721 | -2.796 | -49.2424 | 2024-10-25 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 13a84da0-625f-3d54-9719-f1bc796b1086 | -2.8144 | -49.2631 | 2024-10-25 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 99e45c61-df96-35a2-be04-9d4211c31c7a | -2.8145 | -49.2418 | 2024-10-25 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 4a4c14ec-3d0b-31ff-8b68-7db85158af15 | -2.9578 | -50.4198 | 2024-10-25 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 558ba99b-4520-35a9-9109-722b158351a0 | -3.2135 | -46.8063 | 2024-10-25 02:15:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 258a9787-369b-397a-b415-a88d96bd72b5 | -3.2136 | -46.7843 | 2024-10-25 02:15:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 8672bdf5-567b-361d-b84b-3fd7d9be0089 | -3.9396 | -46.4229 | 2024-10-25 02:15:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 9edc037e-6298-3261-bdf8-4ec26eb720f9 | -4.2429 | -48.5474 | 2024-10-25 02:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 323f8dc1-f492-327a-af30-8796a62341e0 | -4.5045 | -48.2117 | 2024-10-25 02:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 13393e1f-20b2-37c5-ae5c-c25f4e19777f | -4.58 | -48.0132 | 2024-10-25 02:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 63476d31-023e-36f5-be80-dcf51195153b | -4.5986 | -48.0123 | 2024-10-25 02:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| c06ee207-edf0-31b3-8540-8ce1a980d520 | -6.5219 | -60.0457 | 2024-10-25 02:15:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| c3ddb769-f200-39bb-b280-a6f775dd2f83 | -11.902 | -56.4135 | 2024-10-25 02:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 24fe5b64-81ea-3c1a-8d94-0f48a99d8ae9 | -11.9822 | -63.9213 | 2024-10-25 02:16:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 4da42097-cc91-3c31-a18b-612c911c7689 | -11.9824 | -63.9022 | 2024-10-25 02:16:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 127.1 |
| c4b9defa-3b0d-3ad4-b4a4-281c9ee6bf55 | -12.0011 | -63.9203 | 2024-10-25 02:16:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 3e3e0c52-2534-3f9c-a129-f7696f925821 | -12.0012 | -63.9013 | 2024-10-25 02:16:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 134.0 |
| fc88762d-d566-3f2a-981c-48253acaf14f | -12.0632 | -63.1537 | 2024-10-25 02:16:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 95b3ca16-a708-3a7a-9070-012d0d5b6057 | -12.0634 | -63.1346 | 2024-10-25 02:16:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d2e73f29-bf3d-3ce3-98a7-29927e4d4d51 | -12.4589 | -63.1895 | 2024-10-25 02:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 6ef45537-cc38-3803-bba8-943543d92b1d | -12.4591 | -63.1704 | 2024-10-25 02:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 87432409-ba6e-316b-aba1-51fa10d583ee | -12.478 | -63.1693 | 2024-10-25 02:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 72f6851a-22dc-32cc-b72f-3ce69265beb1 | -14.1339 | -44.3037 | 2024-10-25 02:16:24 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f557078b-da00-3965-9f03-230b3b033a26 | -16.94 | -57.5268 | 2024-10-25 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| b4406e30-7a18-3abe-9058-1be1ea4ea300 | -16.9596 | -57.5245 | 2024-10-25 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.0 |
| 34a15b32-a57f-33b7-a7dc-b428059701b2 | -16.9792 | -57.5223 | 2024-10-25 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.8 |
| d5bfc936-a2ac-3177-84c9-feef8ce358d4 | -17.0184 | -57.5178 | 2024-10-25 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| 4016fab5-9abf-350b-be92-f3db759f4f7f | -17.0381 | -57.5155 | 2024-10-25 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.8 |
| 0dff2b28-c14f-39f7-b208-3f0fa5cf0573 | -17.039 | -57.454 | 2024-10-25 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.9 |
| 749bfb2b-6133-3a04-b83d-537056b0a846 | -17.0583 | -57.4722 | 2024-10-25 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| c3281111-f719-30c8-a6e2-2664c6cfd15b | -17.0586 | -57.4517 | 2024-10-25 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.5 |
| c462d590-a6b5-37d4-b809-7bd7002e056a | -17.0786 | -57.429 | 2024-10-25 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 252010a5-2a45-3bf5-a4d0-1b5f5e52e950 | -17.2537 | -57.5108 | 2024-10-25 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.6 |
| 6ca54629-7d15-323a-907a-9cfddd3d0ede | -17.7453 | -57.4933 | 2024-10-25 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 49446a6c-d89f-3f90-a966-900b9d50a4df | -17.7644 | -57.532 | 2024-10-25 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 8692b40d-6f8a-355b-913d-9b522df65ed4 | -17.7671 | -57.3673 | 2024-10-25 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.3 |
| ffe6d4ce-407f-3d7f-8392-ca983b52d3b6 | -17.8038 | -57.5273 | 2024-10-25 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 22cd9063-b764-3668-95e8-e79b093c44ed | -17.8042 | -57.5067 | 2024-10-25 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.8 |
| db9784f0-7920-3fa8-a8d5-b8a20ace281d | -17.8239 | -57.5043 | 2024-10-25 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 056bb830-5405-3230-a8e6-b01c307eb105 | -17.9272 | -57.224 | 2024-10-25 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.0 |
| 28abc9dd-1905-34b5-a474-2406d69e7514 | -17.9268 | -57.2447 | 2024-10-25 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 0356f764-8c48-39cf-a9f2-48aba53a09dd | -17.9473 | -57.2009 | 2024-10-25 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| c2b3a54b-5472-30a3-b3b9-a180635221df | -18.0431 | -57.3745 | 2024-10-25 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 440ccf02-de22-3823-b2ba-8903424561a6 | -18.0434 | -57.3539 | 2024-10-25 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 5d5efbbf-de5a-32dd-96c2-5450414dfd76 | -18.0438 | -57.3332 | 2024-10-25 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| ef9e6ff0-eb6c-3d50-9620-5140e5d484e8 | -18.0441 | -57.3126 | 2024-10-25 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.8 |
| ee008511-317c-351a-8e98-522783756eb6 | -18.0452 | -57.2506 | 2024-10-25 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 5a29a219-0692-372f-bfbc-1c8633768125 | -18.0844 | -57.2663 | 2024-10-25 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| f75139c1-645d-3607-a698-7db418ce8575 | -18.0847 | -57.2456 | 2024-10-25 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| bf25de6d-702d-30b9-84f6-c6f231a45dc2 | -18.1042 | -57.2638 | 2024-10-25 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 639ee7b0-8c53-39ca-a916-508b7245ad22 | -18.3401 | -56.2168 | 2024-10-25 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 73b20213-98c4-3cbe-9da6-8735c937bc5b | -1.0446 | -47.602 | 2024-10-25 02:25:11 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 96766df5-e566-30bc-a6ca-ae522def5db1 | -1.0445 | -47.6237 | 2024-10-25 02:25:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 6ca99e2e-2a4b-3303-9000-3330f333c1d2 | -1.211 | -47.5999 | 2024-10-25 02:25:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8836a589-e19c-3432-b62b-783122af8f57 | -1.1925 | -47.6002 | 2024-10-25 02:25:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 73b9a1ec-2140-3261-a534-99e9af620a3d | -1.1834 | -53.6569 | 2024-10-25 02:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 0e417ad2-874d-3231-bea2-caeb5a657a0d | -2.6482 | -49.2465 | 2024-10-25 02:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9feaa766-386e-3970-afd3-d604315e7170 | -2.6297 | -49.247 | 2024-10-25 02:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| bdd42276-b7e6-352c-b886-22a1f321f82d | -2.8145 | -49.2418 | 2024-10-25 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 49cbedfb-d5d2-3ea2-bf3f-bb1ef0dfd9fe | -2.8144 | -49.2631 | 2024-10-25 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 676891bd-a838-377c-8d8d-dfad06891774 | -2.796 | -49.2424 | 2024-10-25 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4d9e09c2-ca66-38dd-9ae7-4c5b306741ab | -2.796 | -49.2636 | 2024-10-25 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 6c503c37-0994-3da8-ab3d-4d66b5c12851 | -2.9578 | -50.4198 | 2024-10-25 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b5efda57-ec73-3935-8e70-d654cf9e9770 | -3.2136 | -46.7843 | 2024-10-25 02:25:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a75e5b47-4d34-3033-882b-8cc4451e6081 | -3.2135 | -46.8063 | 2024-10-25 02:25:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| bc4da6c7-a184-3503-ab20-60d7e2d54cfa | -3.1949 | -46.807 | 2024-10-25 02:25:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| f4c0e450-438d-3233-931a-eb6e993e0f9d | -3.9581 | -46.422 | 2024-10-25 02:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| dff2cdcd-c64c-3147-9186-0321a8a2f82b | -3.958 | -46.4442 | 2024-10-25 02:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| bfddf742-434b-318b-b3be-d8035f6e168f | -4.2429 | -48.5474 | 2024-10-25 02:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 5660a919-88f8-38b4-92d9-ab6d2836585f | -4.5231 | -48.2108 | 2024-10-25 02:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ceef988f-4631-30f5-b232-f2cb8aad169d | -4.5045 | -48.2117 | 2024-10-25 02:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 45ec2676-a116-3d00-b2fb-444e046e47dc | -6.522 | -60.0266 | 2024-10-25 02:25:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cbf9f439-d04a-3413-a9f8-20657fb7af25 | -6.5219 | -60.0457 | 2024-10-25 02:25:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ae42c46e-6fdb-39eb-9502-a9a0711bf0f4 | -12.0013 | -63.8822 | 2024-10-25 02:26:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 59bed3f7-dc1b-31a0-878e-e1a8340d3801 | -12.0444 | -63.1547 | 2024-10-25 02:26:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| e3fc2671-7837-30e4-b201-dfae09eeb44b | -12.0632 | -63.1537 | 2024-10-25 02:26:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| f01909a9-ba4f-37e4-9e1c-40dedb28b344 | -12.0012 | -63.9013 | 2024-10-25 02:26:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 147.0 |
| dd5aee5c-e458-3225-bb3b-27d9ebafa4c5 | -12.0634 | -63.1346 | 2024-10-25 02:26:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 3b28b8cd-8a07-39f1-bc7a-176fbc37869e | -12.0011 | -63.9203 | 2024-10-25 02:26:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 354395f8-8859-31cc-a761-f66a137d2dd8 | -11.9824 | -63.9022 | 2024-10-25 02:26:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 63a62590-2224-3b9c-88d0-2f5cc0062c85 | -11.9822 | -63.9213 | 2024-10-25 02:26:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0b38823c-5931-310d-a1e4-eb59c6a77fe3 | -12.4591 | -63.1704 | 2024-10-25 02:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 0ae87c3c-d67e-30a8-b356-be8bc3a55fe4 | -12.4589 | -63.1895 | 2024-10-25 02:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b5b6962d-b0f7-3836-bbb0-700dadf4cbc3 | -12.478 | -63.1693 | 2024-10-25 02:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 03ef97b6-78ec-378b-af12-d5b28d7a2761 | -12.3782 | -63.8821 | 2024-10-25 02:26:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 2de1cf84-442f-3d19-a91e-e30ac0b60cda | -14.1144 | -44.3072 | 2024-10-25 02:26:24 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 36c99c11-ed6e-3f62-aba0-6f71fca39117 | -16.94 | -57.5268 | 2024-10-25 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 7913aef8-4171-32a5-8745-82dfe75a17c4 | -16.9596 | -57.5245 | 2024-10-25 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.5 |
| 7890d98a-8c27-3e0a-8bdf-f130f65827af | -16.9792 | -57.5223 | 2024-10-25 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |
| 5e6ba553-7adf-304a-9942-e9123ebb6c67 | -17.0014 | -57.3561 | 2024-10-25 02:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 56d1a835-89b9-3520-8986-c10973bf138c | -17.0381 | -57.5155 | 2024-10-25 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 41b0f34c-9e4a-3a32-9605-492af6a858f2 | -17.039 | -57.454 | 2024-10-25 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| a27f31ba-31b4-399c-bcb9-0fa328f9a24c | -17.0586 | -57.4517 | 2024-10-25 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.3 |
| dffed56c-7ea6-3849-ae77-fd510c5cba63 | -17.0786 | -57.429 | 2024-10-25 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| aa86b27c-81a0-3288-8f5a-ed85b597fd74 | -17.0789 | -57.4085 | 2024-10-25 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| f3160da6-46b6-3cd0-b844-f3aa63155f34 | -17.2147 | -57.4949 | 2024-10-25 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| 01a3c5bd-a0b8-3a51-97e9-5634d54d257a | -17.2537 | -57.5108 | 2024-10-25 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.4 |
| b63fdb16-945e-3ceb-a5a8-e863bf44f4b2 | -17.7644 | -57.532 | 2024-10-25 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 246ad63b-38fb-3b9d-b410-11aa1b98ca1c | -17.7671 | -57.3673 | 2024-10-25 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |


[Clique aqui para ver as próximas entradas](README18.md)
