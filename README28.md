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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 235c0af4-e84f-33bb-b8f7-9fe83deb7990 | -2.66789 | -46.61336 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7b9ff273-45a1-3682-ada8-27bfa5cfac9d | -2.21649 | -50.70267 | 2024-11-20 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82c89dae-65c0-30c2-82cd-a60af692fedc | -2.62186 | -48.18403 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e46efd7-4792-3fe2-8af6-4889ca9cf4d2 | -1.42512 | -46.79947 | 2024-11-20 04:25:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6b69ece-5a6a-398a-9052-ace8c9794419 | -2.36368 | -46.18842 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 513f115a-192a-3acc-a2b4-8b3d693ae44f | -1.21259 | -51.75623 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14bf07ad-8c01-3f7c-803e-7621efd67f37 | -2.69074 | -46.22913 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c66b343f-4680-304c-bf77-339a10bced9a | -2.68933 | -46.84682 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49630c94-6d04-3db0-a181-c7219cbcb516 | -2.20828 | -49.73442 | 2024-11-20 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b72f3972-daa2-3e1c-a960-4b93685193bb | -2.26121 | -48.81117 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff2023b4-7a5d-32dd-bc04-0f3bc5e26549 | -2.75958 | -45.31062 | 2024-11-20 04:25:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16baca9a-8b5d-3feb-9aad-44ed41221f75 | -2.68527 | -46.24243 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2a020de-93fe-3ccf-b284-666893add943 | -3.36233 | -45.10752 | 2024-11-20 04:25:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e388b22-6bb3-371c-9b4f-c5cc45865be9 | -2.57934 | -46.54958 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10cbeb3f-c6f4-3266-b564-6cdc5569024c | -1.24685 | -53.36516 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2645c5d2-4879-36e8-8b20-cba8afa55a9b | -1.57613 | -47.657 | 2024-11-20 04:25:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 06c26c0e-d688-342c-b663-83d652d9c40c | -2.18739 | -46.40263 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4019890e-b71e-3987-bfb3-00fb63d6f12b | 0.14533 | -51.20977 | 2024-11-20 04:25:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80ebbc71-504f-3330-bae2-efa60853176c | -0.95269 | -51.71964 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ac899b0-c05b-35a0-adf3-61b0be59be63 | -2.55283 | -48.04727 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 135b1b9a-64d8-3aed-95b1-27cebe19b053 | -1.19734 | -53.67134 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 5d08f2de-b08f-3ffc-87fc-f7d91fbc061d | -0.96826 | -51.73061 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62f66570-52ac-3c3d-ac68-2ad1577b6511 | -1.24457 | -51.78343 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 407b628b-af96-3321-a3a4-112cb86d35b9 | -0.94757 | -51.7233 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed499180-9abe-308d-ac1b-ae8f87d379a6 | -1.74651 | -46.70002 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c84fd03-9faf-3813-ab97-e03b73adc986 | -1.47439 | -53.48115 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e0233c67-40e7-319f-9092-04507996eccc | -3.08929 | -45.96715 | 2024-11-20 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeb2a466-7cbd-3fff-a42c-db8dc5f79678 | -1.31099 | -47.8011 | 2024-11-20 04:25:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f59d2e35-d0d4-309e-90fd-452a06ebbe2e | -2.41789 | -45.81957 | 2024-11-20 04:25:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af82576f-3b9a-351a-90b1-1266d40fc342 | -0.63576 | -51.7285 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 772cb83e-f8c7-3871-ac84-640f19d4910d | -2.75558 | -46.07685 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35434682-51a0-38af-9646-f9da5806e22a | -2.28476 | -48.40823 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73e1f5e1-350a-3fbb-9e58-c2d8ea334664 | -0.81963 | -52.51114 | 2024-11-20 04:25:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9af1e53f-02c1-3906-8fcd-bf7a172f37ce | -2.30128 | -46.17528 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6d5ac98-f539-395f-b4c6-5434f73b29f8 | -1.70677 | -46.23468 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8daf81b-bf91-311b-949d-d309fc74f886 | -1.25413 | -51.78046 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b41e2a9-a498-371f-8ed4-bf1d1b70ee8f | -1.30657 | -52.40423 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 534ccc53-c894-3e8e-bd79-ec7147ea1f70 | -3.0874 | -44.29344 | 2024-11-20 04:25:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9e31a7b-c6a3-302c-8f09-2ba44db2fd63 | -2.69297 | -46.23655 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b4e1e2b5-93e0-37d7-8725-698623a66750 | -2.20101 | -46.31577 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c04a4644-59ef-3c13-bced-b752035097e8 | -1.22422 | -51.74027 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af9b6b94-2548-3503-ba8f-ad6577046c37 | -2.57428 | -48.43559 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c26dd864-8672-378d-8a2b-a3bf3a44c8ad | -2.97574 | -45.1214 | 2024-11-20 04:25:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8746636-8c34-36ae-8c43-4f1b89996efe | -2.65985 | -46.23143 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17d7a180-c094-3adb-9ba6-164e12773874 | -1.54777 | -52.27294 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e67e38ee-ba68-35a9-bbbc-e24c069b891b | -2.26283 | -48.40895 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| daa9599c-6375-3ad2-8c4e-9aa6b42afa32 | -3.84006 | -41.56641 | 2024-11-20 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7ce9ae00-fa53-3e83-b04a-73025f2c6f4b | -1.22989 | -51.79008 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ec1fffd-a92d-3b04-bc6a-2c229a29df1d | -0.94314 | -51.72261 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9124d82e-3c62-3712-8230-3a27f0f57b9f | -2.22137 | -46.46853 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9108c40b-3c25-35f7-9eca-75236f30c602 | -3.09098 | -45.97797 | 2024-11-20 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2850fa0f-1401-3bff-93cb-793944a5b740 | -2.00264 | -46.6028 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 141dc2eb-06b0-3298-81b5-e012a25d75d6 | -2.09351 | -48.37978 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fc964ee-5f69-33ff-ac3c-a32153138d51 | -2.84583 | -46.67364 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65abf889-a9e8-3fc1-a761-e95906643eee | -2.45181 | -49.14815 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc52c66d-efa6-3c31-8cb7-aaa3c4dcd671 | -2.61083 | -46.2628 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b56ac39-8b50-3990-ab10-bde6d188f025 | -1.92517 | -46.44729 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| afecf153-db38-3c30-b5a4-dd29b3add646 | -0.2922 | -51.50104 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61229924-363d-34d9-9ac7-330a02b0925e | -2.36134 | -48.60962 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea09c579-f28c-341b-9553-7ba0f6286662 | -2.70376 | -47.98381 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93252b80-ff1f-3f30-98aa-9345c545334c | -1.20164 | -51.76785 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 412d99ab-e0e4-3ebf-b96c-69dfa9b5a4ec | -0.24955 | -48.58855 | 2024-11-20 04:25:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53a4f6c7-6dcd-3eee-853d-02b3640dc70d | -3.17872 | -46.43712 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 29fb4c16-6634-38a2-ba33-3b27fb320d35 | -2.22197 | -46.48649 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94bc9de0-e8d7-3c19-8f71-6c8a3a881ac6 | -0.97482 | -51.7182 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4efb02c-407b-31e8-97fe-88559c8678e7 | -1.88795 | -52.62032 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60300ace-9843-35c2-aabe-b643cd7970e9 | -2.63802 | -46.84617 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76a3f571-a875-3430-bc4e-1d9d984c38da | -1.71009 | -46.23519 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b8a8a1a-b3f3-364e-816a-70deab670e98 | -2.65752 | -46.55091 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bb865581-aea2-3aa4-bb54-8001ef577571 | -2.35059 | -48.608 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68363b44-2a41-3b22-8dce-234a5d781b04 | -2.60139 | -46.19056 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 879fcbb7-c5bd-3c72-b394-6849a9d4b3cc | -2.21532 | -46.48547 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7cff7057-f526-38c5-bb18-a161ab14813e | -2.65364 | -46.55389 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72f5689c-2b76-395f-af29-4d325d985b96 | -2.55042 | -47.29043 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b39cce62-02b7-3e21-8a7a-30e7b3362218 | -2.26949 | -45.46225 | 2024-11-20 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6119018f-2242-3e31-a600-935ececcf9c2 | -2.67918 | -46.23795 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38fe2b8c-680d-3f1a-b751-a86e23ed8b6a | -1.72445 | -52.69673 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bfaff91-d30c-3747-9e81-4f4af6ea1a1a | -2.63748 | -46.13615 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef10215f-f280-309e-a8f6-3e4d1305a278 | -2.09445 | -46.38774 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bcd6656-9738-3f4e-8c62-34797e1f60b7 | -0.92888 | -51.64055 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7062f2f7-926d-3ab0-a1ea-84e2e76fd478 | -2.65296 | -46.14554 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5a720f9-c615-3ec2-8301-9dfbb60c1ba2 | -1.1091 | -51.75504 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1251b5b-07ae-3e35-88da-41c0dff87d3e | -1.22353 | -51.74458 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a30aa9dc-3988-34aa-a265-3db69a9c461f | -3.39194 | -44.43501 | 2024-11-20 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d49a2d9-8875-32d0-8e5e-09b3d3f7b010 | -2.84474 | -46.68064 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08075baf-61f7-361f-8ebc-05b335ed5083 | -1.63077 | -52.40267 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3db377c9-dee7-3b8e-947f-36c343a3b801 | -2.54583 | -47.28993 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2783a7a-c983-3325-a426-f195cb5117d6 | -1.20886 | -51.75122 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2b1b4413-7b76-3720-9167-3e1b4086fa04 | -2.67619 | -46.17032 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e5d1de6-4b4d-3132-96a5-46dd92096e55 | -2.56522 | -48.17191 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d34880a1-59f4-3971-bce3-fdebe52f2efb | -2.55993 | -46.54301 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 298eb11e-334f-3ea6-ad0a-9e55f301a31c | -2.44732 | -48.5521 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7d54d45-0a57-36fc-b2ef-7ae76e0edb5b | -2.83583 | -46.67209 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c61c5eeb-1e88-30b7-b9c6-f09108269285 | -1.26061 | -51.76809 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91829f40-658a-3ce8-923c-9a360cfffd17 | -2.22587 | -47.2257 | 2024-11-20 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cb9811a-f2da-3280-975e-ac50aaba590d | -2.28058 | -48.41169 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e079d0d4-6475-3528-bf3d-1c1b1569805a | -2.02016 | -52.40948 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8cfde5d-7f14-3b0c-9efd-1c52e85a5586 | -2.54078 | -46.2095 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d9b7ec9-2e6a-301e-bb12-7ca1bf54a7e5 | -1.29634 | -52.22856 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29407e52-a235-3688-92be-10f6f134de47 | -1.74806 | -50.47516 | 2024-11-20 04:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README29.md)
