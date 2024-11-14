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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 955d6d21-bdcd-33db-8a3c-4c439b9b00c2 | 0.81089 | -50.85659 | 2024-11-14 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16f2f919-dacc-3cea-b89a-c80c871c18e2 | 0.8505 | -50.20834 | 2024-11-14 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92868374-10a8-3674-86aa-34ede0d034a8 | -0.19412 | -51.50288 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 467c3c8b-7b4c-30d0-bf4d-bc7b2650df17 | -0.27592 | -48.83826 | 2024-11-14 04:38:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cacc16b-9bac-39fc-ae5c-17eb6f726c94 | -0.2086 | -51.50512 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e0e2cc1f-fd77-3d95-9e68-774f12047bae | -0.04091 | -51.74142 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed7c3260-40b6-3041-b75e-b6481f54ed76 | -0.19421 | -51.55011 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c14d9b27-3c63-39b6-bd19-e1bab5a06c43 | -0.19709 | -51.50763 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97dd6c64-a14e-3cd0-be6d-df67ace8579d | 0.25495 | -51.40445 | 2024-11-14 04:38:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db851fe5-ca64-329c-bdfe-40a4b0adf1f6 | -0.03543 | -50.77892 | 2024-11-14 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5640bf9-6beb-3db8-a179-fe37434f4159 | -0.20563 | -51.50038 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c3d3829-b5bc-3fc0-a1bb-dee7ca122d08 | 0.00538 | -51.12946 | 2024-11-14 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4353ecd-243f-35c0-8b88-f1b658d3217b | 0.10239 | -49.93533 | 2024-11-14 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6077de59-e1f5-31a5-b881-f9b99711a642 | -0.2073 | -51.63423 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60a5fbf0-e24b-3786-a0c9-8866a415d86b | 0.31431 | -50.97339 | 2024-11-14 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 21814517-67e1-3202-9096-f16ad656f2a6 | -0.10037 | -51.50257 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5e0c44c4-d660-38ac-acb2-01f10c3af255 | -0.09074 | -51.32698 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d14ec918-cf58-3a4c-914a-22af1689ff91 | -0.20136 | -51.504 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3cdea3a1-e48e-3c09-8599-20f642be2779 | -0.02364 | -51.65985 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb62df18-a766-3ca9-af7b-3fbceda435c8 | 0.65903 | -51.78174 | 2024-11-14 04:38:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e12854a-35aa-33e9-b959-0e8838ca274d | -0.03893 | -50.77945 | 2024-11-14 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33df49bc-2082-390e-b9cb-02a74a45e329 | -0.13117 | -51.54901 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b50f4852-fc37-3b63-aa23-5714a5adc670 | -0.20071 | -51.50818 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5bd04b4d-820d-37d8-9828-67b4edb8fcb9 | 0.44298 | -50.9393 | 2024-11-14 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a74f5fa-d312-3c85-980e-a841687eac80 | -0.05393 | -51.73023 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 519e6d04-2c7c-39aa-99c8-b6f093b43cf9 | 0.11749 | -51.33907 | 2024-11-14 04:38:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c1f7bea-9944-3e3d-84e6-30bab97cec3d | -0.20433 | -51.50874 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1df98f8a-87dd-337d-aff5-c5f2ece70832 | -0.1754 | -51.55155 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ddbed43-975f-3a69-a70b-bf110822ae47 | -0.10465 | -51.49893 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf05c321-4963-3124-aa60-3fe1b33ac53a | -0.03604 | -50.77503 | 2024-11-14 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baf76b68-0ec3-3faa-9695-7dca1f741062 | -0.04672 | -50.7528 | 2024-11-14 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a97754a-5932-39c2-ba38-e3078b39333d | 2.62346 | -60.41274 | 2024-11-14 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a2c6169e-82b7-3268-a7ad-b369cca082b8 | -0.05459 | -51.72592 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3a3194c-0705-3b5a-995f-10c4180e744b | 0.31494 | -50.97739 | 2024-11-14 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fb47fa23-ea11-3c96-a0b9-00e62ceb8a99 | -0.19049 | -51.50234 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3799ec2-57d4-3ff9-aa01-5525159c7da1 | -0.20368 | -51.51292 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2337e855-e4c1-300c-bd53-a9475118e22a | -17.5869 | -57.5533 | 2024-11-14 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 0e02c382-d0e0-3a85-989a-c3a4596f2349 | -4.5614 | -48.0141 | 2024-11-14 04:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 63769c6a-cda3-3e6f-844f-94f512339e35 | -17.5675 | -57.5351 | 2024-11-14 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 53b527b7-1760-37e3-9486-0cbeb2a04eab | -17.2543 | -57.4698 | 2024-11-14 04:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| b0a1b06e-c96f-3d56-9f48-1b0f11e49bb5 | -17.2347 | -57.4721 | 2024-11-14 04:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.3 |
| 7cca8cca-f1a5-326d-9152-bc265779a07e | -17.6066 | -57.551 | 2024-11-14 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 18250691-99c2-3c7e-911a-d44c85a87a5c | -17.5872 | -57.5328 | 2024-11-14 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 762630c9-5f8d-3087-b42b-9555e252dd7a | -4.5616 | -47.9925 | 2024-11-14 04:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| fd84e2b1-2447-3592-bcd9-c752b9861fcf | -1.8106 | -52.1652 | 2024-11-14 04:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 2f6609fc-d2fe-3fc0-93e7-f9169e283d3e | -3.15984 | -48.3642 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7985bb99-fe80-36d9-9e1a-44ed339dcba4 | -2.66611 | -46.99066 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92067018-3aca-32eb-9b8e-6a1b93b8ade3 | -4.44774 | -49.5915 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9a6ae7c4-63e4-3635-ac0e-3a8734d18604 | -2.3118 | -48.45726 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00708acd-e0e8-3f32-bd08-8045172abb33 | -4.26747 | -48.19416 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfb730f3-9cd6-30c7-a267-921034fdf74e | -3.0448 | -50.33565 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 280b8012-baa4-3c8a-972e-5ed8cfc6c0fc | -2.31418 | -50.66598 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e4e514c-5353-3dff-b7dc-f1bf9b5f484c | -1.57434 | -52.02428 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69d18237-0606-3a11-b79e-3533098c602f | -1.40387 | -52.38529 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd55e07e-a685-384f-be03-00b0f31434cd | -2.90706 | -48.30355 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ccb7e8e-ee6f-3680-b3d3-6be59c1d23ec | -4.05173 | -48.3143 | 2024-11-14 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff54cc3d-3825-3aec-8dbc-34ed69acb44c | -1.39751 | -51.13348 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c5aa3a5f-f9f6-3d2d-a134-0877293d444d | -3.26288 | -46.27908 | 2024-11-14 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a5f0e5c-8136-33a5-9839-31346a00a6bb | -1.6065 | -52.50142 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14179c21-26c5-3479-a2da-1630da35cb5d | -4.04466 | -45.71547 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 79d29059-5f0b-32e8-a41d-1c56d4510245 | -1.8174 | -48.00618 | 2024-11-14 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73e8bafc-af94-3e75-8f8f-43d9e6353851 | -2.16346 | -48.90502 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b8b0c25-944c-3a55-af2f-cbf63aeca222 | -1.54153 | -51.11501 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab3b3bfb-19be-311a-a2f1-b0276395c9f3 | -6.03098 | -48.04155 | 2024-11-14 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f28dc98a-f400-33aa-8199-4b43f6794b6e | -4.0187 | -46.2853 | 2024-11-14 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b15d8e2-b778-366d-9b6c-1c2141ddf5aa | -0.89698 | -51.73177 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5ad3fd3-fed5-3100-a641-d17370bcbc9a | -2.66629 | -46.80923 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94e26a37-228e-3422-a332-7ed554048590 | -2.62234 | -46.82146 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e76df2d4-54e0-3aac-8aa9-ae378410c0cd | -1.56701 | -52.02316 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87354bee-6bd8-34c6-b9ee-e2262efd4156 | -5.36364 | -43.54595 | 2024-11-14 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9aeab9e-3f0b-307d-9b4e-9885a7dae9c9 | -3.02385 | -47.99103 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c33c06f-55d8-3cb5-8854-528dd1d2df5a | -2.64493 | -46.17392 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 03f09353-d8b0-342d-a497-db49e4f4c7a3 | -2.59084 | -48.19413 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 726b1ce7-64be-3c1f-8663-984d6fbe759a | -3.02718 | -47.99154 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db61b4dd-f019-3c57-94b0-f0f2f6794f0b | -3.30104 | -45.67865 | 2024-11-14 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14564efe-ebde-3213-a799-3b738e6b2c1a | -4.16909 | -46.25034 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6323b7f0-c40e-3405-bcf9-1467468b6dd8 | -3.46486 | -50.30968 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4071f3a9-a15b-315c-adf4-8980abdfebd5 | -2.19364 | -48.38631 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4208e463-af8c-36fa-94a8-a6d82fea753d | -2.58845 | -47.01994 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96ae5b89-e3a0-3333-bab8-5f976d57db33 | -1.2235 | -51.75296 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 352ea56b-0c20-36b3-85af-75434082a997 | -5.3598 | -43.54718 | 2024-11-14 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9940a4b-96c6-3fe3-a817-8a771251406f | -4.28762 | -46.91896 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bab04cf1-2632-3fd4-88cd-c26ab39ce861 | -2.63961 | -46.18518 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6d132fd-f8df-368d-994b-4368c4e67aa8 | -3.09819 | -51.27805 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d063c6e-fc66-3513-a39f-4aa8f59ca6e0 | -1.3343 | -51.41631 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34f80151-28dc-33ca-af6b-6948deb884a5 | -2.85088 | -46.65635 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 708f20a6-9ba9-3625-8cd4-2e270629b9d2 | -3.88193 | -47.04716 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bbaf7f7-afa6-33f1-86b6-cc2eb27529c9 | -4.35094 | -48.59895 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d1bad06-aaca-30ac-a7b5-9c0476c9e6e1 | -3.23361 | -46.51789 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2907910-0014-320f-972d-d09a793fa1d4 | -2.66743 | -46.82454 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f180965-a1fb-3e65-996e-ce7164c1edf8 | -3.16538 | -50.45776 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b3caa8a-f00a-3ecf-a12e-2afdd8f2db32 | -1.61026 | -52.502 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6cd84dc-f207-361c-bd07-b0130918fd48 | -2.40274 | -48.5066 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90105637-6864-3ea6-9586-067654bd2d30 | -2.11945 | -46.53274 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 242a1327-53aa-388b-a3e5-767113187155 | -4.52458 | -46.48408 | 2024-11-14 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70e55cda-9b6c-3d52-afc6-e66862abf1b0 | -1.71612 | -48.63443 | 2024-11-14 04:40:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bb20067-a715-33c7-9136-b5591e90226b | -3.63812 | -50.59383 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7d8e8a90-5c1d-32ba-b8fd-c5912f4b85f5 | -5.55163 | -44.32635 | 2024-11-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db73e2b4-c58f-391d-8d25-908e92e9e21a | -2.79015 | -45.95894 | 2024-11-14 04:40:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f6bd85d-ad66-33cb-bf37-b40918e0f193 | -4.27555 | -46.90525 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README24.md)
