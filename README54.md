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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83a76f9d-57c5-313d-9246-66c0599fa31e | -2.78678 | -52.86787 | 2024-11-30 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f12eb40-9f44-3c7f-8be1-1c0d38a39589 | -3.09163 | -50.34688 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df8f25fa-2051-35c2-a34b-048be8eeace0 | -2.87122 | -53.98193 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 98cf3202-924e-3e64-a38e-a4b61bba316c | -4.02007 | -48.91523 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e96c8d7c-05ba-3e0e-a959-397b8ad2bcaa | -1.42985 | -54.88313 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cb43de9-5e67-3254-bcac-2bbe4fa17b76 | -1.14799 | -53.66665 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99e4a0d8-e62d-3cc8-a12c-d5204c2a3ba3 | -1.08616 | -53.63507 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6ef0fce5-c6a2-32ce-86d0-9ea73c00c3ed | -3.00939 | -53.22988 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10b6df57-4312-35e3-880b-b33a9f6b6dc2 | -2.42368 | -48.54907 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1829199f-dd28-31ae-b1e8-b19791c0cd8f | -3.10683 | -53.812 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 26d5247d-e675-3076-87e4-2c5f58a6f554 | -3.24978 | -53.64619 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 19d4f35d-ceb7-399c-9b26-ebceff0424dd | -3.29691 | -50.36019 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e5ee6a0-97e5-321e-b2d9-b29557a37e9b | -3.36377 | -50.38575 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f03d1798-e037-32e4-b55f-1132180b4110 | -2.6564 | -51.6827 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9c1666f-7378-3e46-b199-ea3fdf6c6bc6 | -2.44758 | -54.02199 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34e8819c-c4a4-3326-8b18-3111a09de3b8 | -2.50086 | -46.29188 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c6e9ff3-906a-3444-8886-edb74fbc6cb5 | -3.01899 | -49.53 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cd707e0-d8a5-3cf5-89eb-3458e9bb3266 | -1.36219 | -54.65099 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34210394-847f-354a-8f0b-cc8de4a71b50 | -8.84706 | -44.75589 | 2024-11-30 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24633eea-f301-3d22-8850-4d379a153720 | -2.32767 | -50.67482 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5115cc5-587d-3343-804b-ad3e66c15eea | -2.66467 | -48.79434 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1745240-67cf-3255-8488-6a00e7c9c845 | -2.84789 | -46.88694 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 137ed25d-4b39-32a9-b229-039e15dcf6cb | -3.84063 | -46.6533 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01bc607d-fc7d-32f2-a16b-5885337d5d8d | -0.82549 | -51.8571 | 2024-11-30 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c6e5baf4-79fd-3949-bdf2-6af3f350c64c | -1.99474 | -52.09719 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 01a5dd0f-1d35-32ea-a2da-170f807c9ad9 | -3.692 | -47.14559 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ef7bfca-e2ed-37d0-a110-54d41d52f197 | -3.11082 | -53.81259 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ecd9e1f0-4b80-34a9-afb3-9611959ec67a | -3.04412 | -48.5193 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8955810f-6e20-3e80-95f6-f560f57e018c | -4.86753 | -44.00826 | 2024-11-30 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ec706e3-2f25-340c-bcf3-efe272ad1dfe | -2.36294 | -50.51872 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79bf441b-e13e-35bf-96d1-f6578ccea93e | -2.40338 | -50.39479 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c629f9f4-3790-30ca-b558-abe42eb9755f | -0.81852 | -51.6144 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18a5deb6-0a28-364e-ace5-22413e979712 | -3.60319 | -49.99222 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60d9ad8b-9b82-3e27-b69e-5d9cdaf4874a | -6.9489 | -42.83903 | 2024-11-30 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| aa046aba-41ee-315f-bcf2-7a75aff62549 | -3.10285 | -50.31936 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94920c54-c47b-35dd-ba5f-ce52d35afb89 | -2.18364 | -53.66731 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 662cb799-0f6c-3187-979c-744e14faeeca | -2.62375 | -47.74566 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ad2fb57-5739-34dd-9730-d1a9e01bbf90 | -1.61572 | -52.35445 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 19ad9ad5-8295-375a-9717-d8d8e2185761 | -4.33564 | -47.57215 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a7d948a-a8c5-31f4-bbef-997d4aeb2fc1 | -2.30635 | -47.27565 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 704380c1-33e3-3f38-bbd6-d4db761f35e2 | -3.2 | -48.58986 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3c7db04-7514-34cb-af9b-d6aa69716581 | -1.83317 | -46.3 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2b5a000a-d53a-31e4-9ff3-d6ee497ca613 | -4.72853 | -47.22366 | 2024-11-30 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e84790eb-fee1-30d1-b906-468a30bae9ac | -3.30549 | -51.10695 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a5f79bb2-32aa-3dc2-8005-d3a1be70978c | -3.38773 | -50.10926 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a83e9cc-ab2c-303e-a350-b90b0064f504 | -3.6021 | -49.99922 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1044f8e-9053-345e-83d6-8582c707a509 | -3.41254 | -50.16428 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2b394d1-4741-3765-8417-2ad36d6a2c9b | -3.69009 | -50.08834 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6601157-efc9-39c2-a8cc-7e9b84b9f5d3 | -1.29968 | -51.72979 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b7b828fe-795c-377a-8106-f7b202eb79be | -3.10217 | -49.4551 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 878ee58e-060f-3969-877f-b0ccaa5a38c6 | -2.45567 | -46.54022 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99284c79-767a-311a-a73c-00109b6d61bb | -3.285 | -53.85134 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 656bbf18-1610-3561-b947-7244da6af937 | -2.03998 | -51.20334 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1898f9b8-af0b-3673-96cf-3815698ebbe4 | -2.36897 | -50.39318 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7b953a8-0bbf-3c44-a945-862b7a129ec3 | -4.0443 | -46.86016 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f30af8dc-1af7-3c91-8c4a-aea092d24568 | -2.26374 | -46.53555 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad43ac13-b169-3608-92d5-9d74ce741835 | -4.00324 | -48.2997 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef101904-ad14-3f06-a1c7-30e6085d14b5 | -1.35069 | -51.38675 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed05e9b1-fb24-3232-9271-c2fc5aac1065 | -1.04348 | -53.35619 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b98d0052-d577-325f-95e6-83f1f1ccc134 | -2.6958 | -51.98061 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e32a8e9-1c6e-38fd-8fc8-bc7c34eff9b7 | -4.08322 | -47.02095 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb9110ea-9ff2-3c3d-801e-dc33bde7d377 | -3.98642 | -46.64359 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| caa5338d-38bb-3bc8-9931-f5ab0bbf6507 | -3.94932 | -49.95361 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 14203729-abb0-362e-bfc8-f23f8e57ac8d | -3.5423 | -50.18425 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1a7592b-f168-3f9c-9107-195d46e8f500 | -2.6982 | -52.91278 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96e75d82-822f-310e-90ac-b91171ae6da5 | -3.0005 | -45.521 | 2024-11-30 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bb72cda-d763-387b-8551-d7aee5f4a4bd | -2.01565 | -48.06933 | 2024-11-30 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dc27aa2-c007-3914-a51d-102ec5c9b9b5 | -1.11821 | -51.90285 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5864d66c-848b-3391-8536-cea419d7fddd | -2.82641 | -45.29111 | 2024-11-30 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a5d1ac2-5041-39b3-af2b-4eeeaa12bcbe | -3.41699 | -50.15777 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d507a53-0363-385c-ad90-7fa28f3800f1 | -3.8495 | -52.31912 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf0a1e65-957e-38c4-bab4-cab26a5a3ee8 | -1.54814 | -53.06759 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac6f79df-dddd-3544-af59-f69a7bd52719 | -2.46831 | -46.57318 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9e1232e-0e73-3cc7-9bb5-9cde983d5102 | -3.47016 | -50.38013 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3647f05-e3e2-30d3-a0b6-0655ff13b7fd | -2.87359 | -53.99324 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91fc37d8-6c6f-3bc9-b128-9ca09d6bf10a | -2.16275 | -50.92078 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6b29cfe-9fd8-3f53-b1e7-56b8b28e0af5 | -4.10782 | -50.983 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b31160af-2f05-39bb-8c21-bb090899e8db | -1.28523 | -51.72757 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eaa828a4-41a9-3a68-961b-c496a21907ae | -3.81311 | -46.68195 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6080635b-ef09-3bc4-bc6c-6e42c32af25e | -5.12226 | -43.64068 | 2024-11-30 04:40:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f44a9db-92cf-397e-adad-5159e6828059 | -2.95896 | -51.69497 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0064820-ded8-3424-9fd5-c78e8626cfb7 | -4.12109 | -49.09639 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00f7e205-0812-310f-9576-433cf8e05f81 | -3.03473 | -48.51433 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b597aec-e187-36d1-9e59-48eeb211de5e | -3.50124 | -53.80696 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9669628c-e7ed-30fd-8c91-8af61d64a52d | -1.62677 | -53.88336 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dda6d117-88ac-3af7-97d6-c5ad4c554957 | -1.6849 | -47.92221 | 2024-11-30 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8aab847b-7ef2-3cf6-8399-48d459c27392 | -2.23245 | -51.79885 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7e3ef18-6d17-3b8b-8271-6bf8f977a033 | -8.31623 | -44.94962 | 2024-11-30 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9af2e76f-0973-3695-89fe-713eaf151ca6 | -2.42421 | -48.54564 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8dee9ca-40c1-320a-aba2-80e91f501827 | -3.04772 | -49.52102 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff72f488-6f28-3f31-93f4-a5a10e9eb67a | -3.24597 | -53.41847 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f9d4db4-0d57-319d-adca-e13afeaa54b9 | -2.02237 | -51.16958 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb1fe608-e41e-3cf3-a52f-dadfb7fc9383 | -3.60926 | -49.97522 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7cc331e-0aa1-3386-88db-caa951cf7d20 | -6.79622 | -39.45514 | 2024-11-30 04:40:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 018bc100-33ad-39b5-8532-917be87838ae | -2.62551 | -54.2184 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16c52684-0270-3ccc-8b3d-d6f406f2499a | -3.01652 | -54.04129 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbc55b8a-e2ff-35de-ac5c-1345583c139a | -1.31414 | -51.73201 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a0da53c-30c8-3408-8c27-8b595bb8d2f0 | -2.71224 | -48.59774 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e298109-c120-373d-8dc1-acb51b356ede | -1.28369 | -51.65645 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f701563a-0bc8-3afc-9f41-0a1a3a3ceb47 | -3.15111 | -53.83091 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README55.md)
