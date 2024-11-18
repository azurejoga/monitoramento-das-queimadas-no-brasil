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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65120877-4b37-3b3b-a325-88474b449e02 | -3.3116 | -45.6929 | 2024-11-18 04:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 103.7 |
| a2ba5f37-9fa0-3324-af25-33b26115e6fc | -1.2964 | -51.741 | 2024-11-18 04:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 250c0157-1533-3b4e-b20b-329778e97e2a | -2.36986 | -53.68587 | 2024-11-18 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 211e3730-d33c-3a9e-88ee-79e0e7c6791e | -1.76699 | -50.74893 | 2024-11-18 04:10:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0075e23-4ecb-3015-a7fa-d0c7530a8e16 | -1.20441 | -51.76713 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4c0d028-cb9c-371f-8e1b-918b9ec0cb40 | -2.55434 | -47.2857 | 2024-11-18 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc71ee27-c69d-3e77-9123-3827e8d1967f | -2.46938 | -45.62003 | 2024-11-18 04:10:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16878f14-2f1a-316d-bb56-035d5b4c1443 | -1.90257 | -46.4516 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8f25f302-deea-384c-95fe-8d10c46a75a3 | -2.62724 | -46.83894 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95573922-a64e-3d07-83b9-8001b70e6981 | -2.90873 | -46.83721 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acbe2d83-f609-35cc-ade5-290e559425ac | -2.2551 | -49.05167 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe69c2f7-f6fc-37bf-b119-23cf8ac91412 | -2.66483 | -46.22552 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2803baa6-9d1a-31c5-a8bf-5dc2fff1bc44 | -3.23228 | -45.55314 | 2024-11-18 04:10:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97b1c908-f10d-376d-a218-239d5c164ee2 | -2.9632 | -49.20599 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 547362b8-3826-3e3a-8a8d-fffa91a04e56 | -1.2032 | -51.7746 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c41b608-02da-3ddf-aa29-af327903aa6f | -1.30267 | -51.75175 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| fa4b3355-4745-3f07-b2d0-45d36f3ec3f1 | -1.76159 | -45.69104 | 2024-11-18 04:10:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74559592-ed32-38d0-8644-f4c659d5722a | -2.25588 | -49.04697 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcb6c576-8e27-35ab-8a9d-4d744fecdf26 | -2.09526 | -46.39632 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| baed5965-625d-3733-b7f3-e26edf2db887 | -2.58483 | -51.72769 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 671b2210-f6ce-3215-bb3b-0da36cf1d261 | -1.30449 | -51.74059 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 4bec7e37-cd87-3490-a073-84004163f654 | -2.97793 | -45.74107 | 2024-11-18 04:10:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0745dee-c55f-328c-b5bf-ad996b03cfdc | -3.67388 | -44.7098 | 2024-11-18 04:10:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c98a51fe-2339-3460-a6e8-67eacce042be | -1.29394 | -51.73506 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 39e0509f-76ff-3a2c-b537-ef42968f45d1 | -2.05991 | -46.54367 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f7275ae-023e-3296-9b7e-a9562761b277 | -2.07288 | -45.59195 | 2024-11-18 04:10:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36da47c8-2c71-3842-8ea0-0e03ca09058e | -2.20338 | -46.29951 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84ff4497-c535-3549-828f-9003d5715630 | -1.43846 | -53.38538 | 2024-11-18 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 854b4139-4bd3-35c5-af80-68011f1e3f67 | -2.7946 | -45.94968 | 2024-11-18 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 325e608b-86a7-3f9e-9cb2-ee7ffd393b78 | -2.83571 | -46.66365 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2896912d-792f-3f21-8cf8-12bc6a5781be | -3.1749 | -46.60202 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 151568eb-ebb3-355e-95c7-93906cea6d1d | -2.67512 | -46.81625 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7af02933-76f5-3207-ad79-9dd4e7413255 | -2.10538 | -46.43209 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 83bf6971-aa3d-3c2a-a130-e77b567f30f1 | -1.70609 | -46.23796 | 2024-11-18 04:10:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc67a167-3e2d-39b6-9b1c-323e391d8647 | -2.36195 | -48.57005 | 2024-11-18 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef6766ba-1a47-3e4c-88a2-52d6122b65e0 | -1.15552 | -49.11988 | 2024-11-18 04:10:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cb577f3-8588-33c7-b2b1-85fa6c5622c4 | -2.17292 | -46.39148 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c86ceb7-5d60-3910-b194-f0996eb07c89 | -3.27101 | -43.2202 | 2024-11-18 04:10:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16ba2cc6-8fab-3c2c-a0e9-2d30e435dabf | -1.70842 | -45.83279 | 2024-11-18 04:10:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 96008120-a08e-3e15-984a-f8a79baaf7b6 | -3.23296 | -42.08022 | 2024-11-18 04:10:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6771b96-66f9-3add-a477-6b4de5d86ad7 | -3.22933 | -45.54838 | 2024-11-18 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c19f4979-c68e-3cde-b62a-fde791ac71a6 | -3.09073 | -45.96849 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca5caae0-1b7a-3c27-8724-c7363e4f5450 | -2.50624 | -47.24508 | 2024-11-18 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fe6ad62-8d2c-3e78-ba29-c74ef764984d | -2.64973 | -46.22311 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 560a094a-58c3-3671-bea8-b3f6baf9e9da | -2.58008 | -51.71824 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 33c6a594-9530-34f8-bfa6-4d96d3f444ba | -2.14411 | -48.95205 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f15bd372-a689-34c0-a9f2-4ada678b42ed | -2.96026 | -48.00933 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3579e750-2447-37de-8168-dd2363281e9d | -2.95695 | -48.00385 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f5325a7-1cfb-35ab-be8b-abd176ff37c9 | -1.43682 | -53.3867 | 2024-11-18 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c20cc839-de7b-3011-a2f3-31a99a97eea5 | -0.94082 | -51.7262 | 2024-11-18 04:10:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d09f11a-8f75-3135-ac0b-d2a4ae99a39b | -2.28307 | -53.63113 | 2024-11-18 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a45dd70-1f88-35c3-9503-068a835236fd | -1.43603 | -53.39145 | 2024-11-18 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9ffafb7-d1e7-36bb-9239-b04538a51294 | -2.83031 | -46.6727 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f4bb9a52-3c76-3e46-a4fd-a74e2a81b5a6 | -2.57347 | -51.72443 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72ab1030-727f-3b3e-90c2-63ff1d3d9c6d | -3.16798 | -46.59602 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 42e0fbc6-e210-330f-a11f-88d9cc336e80 | -2.33918 | -48.90874 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e646fc69-236b-30ea-9775-5c38c68b281e | -2.58661 | -51.71708 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1ae8d1d1-93e0-36ab-a418-0b4fef3d2f68 | -1.30389 | -51.74429 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| c2fbdd46-a7f9-39dd-8368-cd58bb045418 | -2.25087 | -49.04807 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5da38c69-ab39-3ea3-bf07-306232988e1b | -2.83881 | -46.66911 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b819dadf-07e7-3723-8c9a-77b172d9f1c0 | -1.70167 | -45.82709 | 2024-11-18 04:10:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 0baee5c2-ca2d-39ec-befb-d8a07c915137 | -2.65047 | -46.21851 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e37e2f3a-c314-372a-b2a9-13c586049be0 | -2.94696 | -48.3295 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c4ff2e0e-98ca-302a-bc0f-fb0dbe5c19d4 | -2.64595 | -46.2225 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dd4fcf5-a025-3b5f-b864-1ff5e109f62d | -2.82721 | -46.66724 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7ed294e2-3d5d-37a8-ac31-ebefff2b0e2c | -1.90164 | -46.44935 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6d4ac0b9-94fa-3efb-ae92-7ecb6cbff6b7 | -2.46639 | -45.61517 | 2024-11-18 04:10:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80c4aa27-5c8b-3d43-a2d6-e45c6ed37658 | -2.83108 | -46.66786 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5c4e88a4-273f-3995-8b99-15a425ea102d | -2.57837 | -51.72892 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a53f2792-4b82-3b46-bde7-3345e1b2d39f | -3.31128 | -45.69361 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 71d32fa7-a6f7-3870-be00-4b3d9707f1e4 | -3.3106 | -45.69785 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2bdc7bf8-027f-3231-ab94-a2ebd856811b | -1.14299 | -51.69537 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a713a7d-49a8-3080-83d2-cf84091dbd60 | -2.97742 | -49.11754 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 981ee838-7a48-3155-94a1-f2082bad3cbe | -1.80853 | -46.53434 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff431d4a-9c64-308d-abbc-ad66a0b49eae | -2.94198 | -48.33291 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d6fcb74-94b5-371b-9232-c064d66d2238 | -2.19513 | -53.67147 | 2024-11-18 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d0877c92-f9e2-3287-9a9b-4e60e49644c7 | -2.69107 | -45.70693 | 2024-11-18 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35c69d0d-c59d-3bca-a290-7ace0d328c91 | -2.64792 | -46.55467 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb1ff13c-26bc-3272-a110-22fb76eb7fd5 | -1.1777 | -49.14618 | 2024-11-18 04:10:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4742b1d-8a9a-35c6-9be7-05568b978ed1 | -2.54912 | -47.29224 | 2024-11-18 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7df4f2b2-e086-3414-83d5-27ddb5bb241c | -2.68065 | -46.22343 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 491d2813-6f33-3f30-b41b-409d2baea25d | -3.31075 | -46.04523 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4179d089-4cee-3966-bca7-c4749afb328c | -2.1566 | -50.70602 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c62d4d4-ac38-3b4d-af6b-3b228fb8ce4a | -3.30697 | -45.69727 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d61ba606-fbc4-3609-a6b7-64a92b9fed84 | -2.33528 | -49.13456 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46792968-0bd6-32b5-9764-c07c03b7e533 | -3.20604 | -46.47419 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2268fb80-f8a1-3651-b674-bd1fdd9ac87c | -2.94266 | -48.32879 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8996ef9-5ef0-380f-82c3-7b30e7e8a209 | -1.76801 | -50.75047 | 2024-11-18 04:10:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a878c96-21bc-3428-a6a6-ba1fd8a36f94 | -3.57291 | -45.20789 | 2024-11-18 04:10:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64cff10f-1b22-3959-8f48-b2b599d15d4c | -2.46273 | -45.61459 | 2024-11-18 04:10:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d720f68-6405-3f15-b7dd-0793ae96eefa | 0.61905 | -51.77377 | 2024-11-18 04:10:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3b7a0949-e38b-39d4-a115-0f8832743b99 | -2.79389 | -45.95409 | 2024-11-18 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b788922-3c30-316e-aaba-cab2626dc318 | -3.21108 | -46.68363 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de99f90e-6b86-3dd8-a0da-8aacc74de7b6 | -1.20259 | -51.77834 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4047f9fe-4881-32da-a52b-978b93b82069 | -2.10923 | -46.43273 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b084864-9063-34ec-909d-4b39cd17d261 | -2.95667 | -48.00473 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3be3338-a35d-3548-9211-a314b733af96 | -2.23371 | -46.46748 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c979c03-70e4-3e13-906e-19c2cf02f491 | -2.10048 | -46.33867 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b4523e8-1790-3681-a8db-03d0302412a4 | -3.14126 | -45.34956 | 2024-11-18 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d708f193-6b25-3951-9cd1-93c7cae20dcd | -3.50501 | -48.23019 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README19.md)
