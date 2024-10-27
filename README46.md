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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a9c39af-382b-373f-a5f6-1c9774a39638 | -2.68202 | -48.64221 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f445be8b-d3c3-3278-baeb-f57a63d18a4e | -2.66155 | -48.13389 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a8f52cf6-15c4-356e-8c73-b02d4c954137 | -2.65866 | -48.12936 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f1acb8d-6638-3916-ae5f-d2e54c90ab74 | -2.65803 | -48.13333 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 74badddd-e08d-30a0-bbc1-d80fe0eca8ec | -2.6574 | -48.1373 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b5db56e2-2ab3-38d0-98fc-ce8becb08820 | -2.65513 | -48.12881 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54babff0-669d-31b4-b71d-3653d19b781f | -2.6545 | -48.13278 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33c9081f-209a-36dc-aafc-a964c7d27f27 | -2.65387 | -48.13675 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd604d52-b9ec-3510-a802-9871d75c9cac | -2.64353 | -48.55958 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 834e8df5-8b0d-329f-b285-6df4adf8e2e3 | -2.63994 | -48.559 | 2024-10-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c08dc82-541a-3957-b5b7-b9911feda4f7 | -2.60922 | -48.37165 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2627f44-7118-3e3b-96c0-019c0eec6e1a | -2.58569 | -48.1549 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8cd141f-20d7-3075-89e6-7728881d5660 | -2.58216 | -48.15432 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07dfdeb6-c691-3618-af80-08e9e08635f3 | -2.579 | -48.44606 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bf1e1a0b-ab00-3118-9874-16abd38706ce | -2.56825 | -48.12779 | 2024-10-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 370b9f3a-2366-3139-b475-494d86c3bf22 | -4.36281 | -48.5962 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29eb78ed-e2d2-371d-8257-000d6d456026 | -4.36092 | -48.60819 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb0917bc-72e8-338d-b523-486b2f8568f2 | -4.35738 | -48.60763 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbc01945-fe6f-3ec4-8f71-ea7af1d8428c | -4.33879 | -48.63318 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a432921-b86a-38fa-bf13-beaf8bfe3dba | -4.33815 | -48.6372 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b732b079-f80b-364b-867f-ce8a4d321f4a | -4.30235 | -48.65633 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 515fc809-beb8-3690-b5d4-dc8e40221388 | -4.3001 | -48.64767 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a518a6c-4599-371c-a92c-a39b6cee4613 | -4.29945 | -48.65172 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3074c08-0a13-3bce-a0be-874a7a156533 | -4.29591 | -48.65113 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0b745d6-ca8c-340e-8b28-c449fddc8cd4 | -4.29301 | -48.64653 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7e392b1-1d84-36d1-9348-3f2404d69fc9 | -4.28946 | -48.646 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e081d216-5acb-3eb6-8b75-9abd1f9a9dd5 | -4.28114 | -48.56278 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d1ea5cb-facd-31c5-b3d5-ba64bd0fc86e | -4.24686 | -48.55033 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e0fce63-fed7-3cc4-adfd-496632cd607d | -4.23853 | -48.55714 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 296ce326-aa73-3f31-8c63-2887d4227014 | -4.23499 | -48.55657 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9500221-ebd6-3b1a-94bc-2e8f8b7509e7 | -4.17 | -48.59952 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46b53b66-975a-3ddc-977d-1085978a4ee4 | -4.16934 | -48.60355 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40fe9f8b-35b5-365d-809d-ff83b6545fd3 | -4.10225 | -48.50372 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77a0e72b-fd31-3f55-9f34-81739240d986 | -4.10161 | -48.50772 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d484966a-37a4-3118-8896-092bdb0d53d7 | -4.09807 | -48.50716 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a890f984-41af-364c-a48f-a142a1ad77c4 | -3.96369 | -48.94183 | 2024-10-27 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e2ed462-afa0-323a-b7e2-22f2b5d12e90 | -3.90087 | -49.07832 | 2024-10-27 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d37b298f-0cfa-38f0-8556-e8f94f185379 | -3.84508 | -48.95849 | 2024-10-27 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3cd89f7-e3ce-383b-a20d-3158934d8e7f | -3.82979 | -48.89186 | 2024-10-27 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c8685f3-e77b-3b19-8e58-b5ba0556cd8d | -3.82258 | -48.89069 | 2024-10-27 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d72874b6-07e2-3e95-88c1-24fc4314bb3d | -3.82189 | -48.89492 | 2024-10-27 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7efe148a-349e-318f-8289-883707a7637b | -3.81964 | -48.88591 | 2024-10-27 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf6c9bd5-094e-3241-ad4d-62ffe13a8a09 | -3.81897 | -48.89011 | 2024-10-27 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc17c136-5bc1-3d39-9946-235a7f759c49 | -3.81829 | -48.89433 | 2024-10-27 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbb9e0f8-e4b4-3264-b21e-f4396f0303ae | -3.81603 | -48.88535 | 2024-10-27 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 016b737e-d2b4-3975-83ce-befd9798bde5 | -3.81535 | -48.88955 | 2024-10-27 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71b332df-49ce-387a-8288-1483f758008d | -3.81467 | -48.89376 | 2024-10-27 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0d23c4d-313e-36d2-b7cf-1350117c29f1 | -3.8131 | -48.88058 | 2024-10-27 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c7e05ac-7b77-395f-8ae7-4598672f253f | -4.2082 | -48.04269 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 567e364c-641e-3af1-b71b-7423e9075f63 | -4.20414 | -48.04594 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39c5d529-7790-32c9-8a25-22fee1170f1e | -4.20352 | -48.04981 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59200093-8f14-3e65-b5b0-bbafc5c06d01 | -4.13925 | -48.29583 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbb210ad-2b20-3e44-a167-b1a4249d1ec1 | -4.13513 | -48.2992 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7fb8911-0686-34ac-9d31-08ec085710e1 | -4.09849 | -48.23766 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3faab292-d23d-3377-9f68-43eecf5bbf0d | -4.09702 | -48.23791 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a082e449-cbba-3b65-ab63-a1a2f5c34843 | -4.07672 | -48.29838 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7e1c534-1283-37be-b0b5-bd1513e9a23d | -4.07258 | -48.23406 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2f15ba8-ede1-3c0d-bebe-8332cfa83055 | -4.07136 | -48.24173 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fc4b127-7d45-37a3-a23c-9f251c76a013 | -4.06971 | -48.29732 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53c098bb-0a1f-3c2b-9bd4-59835ebb8940 | -4.06787 | -48.2412 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e07be8c-678f-3a8a-9925-35380dd9355e | -4.06682 | -48.29288 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 959e4b41-d2a8-3785-89fb-eedabd0991ab | -4.0662 | -48.2968 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae246607-4b23-31eb-bb82-709aa8390d4b | -3.93654 | -48.36155 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eea3181-403d-349b-b1c6-5c271c4b4a87 | -3.93303 | -48.36098 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 515cee00-a7c2-32c9-9d5b-aa0ee8e43376 | -3.93267 | -48.34066 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0724612-1f47-3d72-972f-dea65be362d8 | -3.93204 | -48.34458 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f954d5e-3d60-3629-84a0-d7b3994fe1de | -3.92916 | -48.34007 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4609e02-ec00-36a1-a2a3-8606352172ee | -3.92853 | -48.34401 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25438c55-7436-3245-a4ee-1b67a428a9cc | -3.9279 | -48.34795 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e49dc56d-b774-3afe-ada0-559d70a7ed61 | -3.92502 | -48.34347 | 2024-10-27 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 287265f7-c9a4-3ef7-a62b-326cff55c40e | -3.90461 | -47.94519 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e5b2656-45a1-3081-9d31-6b7d3bfb0017 | -3.77053 | -47.72864 | 2024-10-27 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cc788db-890b-344a-b634-8444701ee51c | -4.95569 | -48.64918 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4a9fb05-0dfb-3511-a8c5-192bed568f01 | -4.95504 | -48.65317 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f08dca2-20cc-33d4-afa2-1b5f9d90d4c6 | -4.93618 | -48.56905 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7758910-6938-3698-b2cb-be3bf72883dc | -4.89449 | -48.55484 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ced5af48-50f7-3f6d-96e1-b74264a34553 | -4.89205 | -48.72868 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5661aa62-fe8f-39ea-85ad-1df885d670de | -4.82317 | -48.0988 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7bb2ddd-7024-3d04-aa25-9edd18ad2b22 | -4.81644 | -49.13644 | 2024-10-27 04:23:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1db7123-6d5e-3b19-8dbe-d2058629063f | -4.57863 | -48.02545 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bff277cd-48ef-3ed1-bdfa-7162db56bba6 | -4.57802 | -48.02923 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aea179aa-feb5-33a5-b840-e6304f19ad6c | -4.5758 | -48.02112 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 830a5898-ea47-3733-993f-4f8ef5a490bf | -4.57518 | -48.0249 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e353aaac-a8c4-3fa3-ad87-02300b3bd57f | -4.57457 | -48.02869 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e857db69-87eb-3f85-9d00-c312ef835e83 | -4.57395 | -48.0325 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 672240e2-525a-3309-b1fe-73a80b872488 | -4.57174 | -48.02436 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b89c0302-f4bc-3e9d-99c0-0165a84dc37c | -4.57112 | -48.02815 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a721367d-d0d5-3bf5-aaf7-6bd7ea0b1cf9 | -4.5705 | -48.03197 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e82f301-e38c-36f0-b3aa-ec3b0314043d | -4.51339 | -48.2181 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46564b1e-58b5-3c74-a3ad-b12cb5f745be | -4.50931 | -48.22138 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2da8729e-61f9-3db5-8f65-cc6c1a0c82db | -4.50584 | -48.22081 | 2024-10-27 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5a2866d-eae1-3bdd-bfd2-30ad57feef0d | -4.95633 | -48.6452 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32cc8165-9106-37e1-9f41-747c30c81399 | -4.95216 | -48.64861 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ce2a4ec-a346-3eb6-9a0c-fc6581bd85e3 | -4.89206 | -48.72941 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb9790e8-a50c-3d22-bfd9-748ed5bfc94a | -4.89098 | -48.55429 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4e17dde-f4a2-3b26-bb0d-db9911d5e8d9 | -4.86805 | -48.56255 | 2024-10-27 04:23:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe981782-ed71-352a-bc5b-c5e5e6ac0313 | -4.86742 | -48.56645 | 2024-10-27 04:23:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b3a329d-ce23-34ea-b55c-701193dcf0b6 | -4.84157 | -48.61489 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 175c8d4f-77eb-3b33-86ba-48bde335c4ec | -4.84093 | -48.61888 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea6302e0-8d0f-36c1-875e-1eb2999cf317 | -4.83741 | -48.61832 | 2024-10-27 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README47.md)
