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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd02a440-eeee-363e-bb86-d76c5dd75e8d | -2.30937 | -47.90846 | 2024-11-30 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 49fe057e-959e-3900-a862-bba3eb8265eb | -2.20055 | -48.34511 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 32fcee2e-bdae-3929-bfd5-58968f9f7fed | -3.00267 | -53.23614 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e430e1f9-eafd-3c64-bfdf-61f20c2ec752 | -2.75281 | -54.12186 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 571f1047-df7f-327e-8500-3cdf67e3bd47 | -3.5462 | -50.18124 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c6f525c4-0d5a-360a-a41a-3dbddd8ff542 | -1.76157 | -50.85591 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05a80ee7-63e5-37b6-ad80-86f41ee551ab | -1.19876 | -53.87227 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c99d2479-5d43-3007-b2a9-7de744d41e83 | -3.32869 | -46.61038 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50f70158-d636-3070-a84a-3f763c9a87c3 | -2.02416 | -50.77293 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8f6cd5a6-1c00-37da-a0c4-c9b698789ecf | -6.92654 | -45.20403 | 2024-11-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5a39989-b07b-35e8-89f2-ff206716450e | -2.6586 | -48.78989 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56388ec3-13e0-3f7d-8388-abece4fe3446 | -3.77592 | -46.69197 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cd95ac3-f3bd-3372-89e2-77a93bf974f9 | -1.99477 | -53.29339 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d015333-b4b6-3ff0-b90b-93483fe63aff | -4.01604 | -46.99915 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8ad8b1ec-fbdb-3927-b3fa-70afb36f1cf8 | -2.69726 | -46.12067 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08dafaa6-c727-32e4-bb5a-83dd8589acf5 | -3.095 | -50.3474 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 686140d4-6648-3901-b509-934690a75055 | -1.32104 | -51.66521 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b79fa467-ad02-3479-aa2e-50ec3037a7a8 | -3.97055 | -48.09361 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ce70c8cf-db4f-33fa-97f4-e9f4a2b5d6e1 | -3.50032 | -50.49472 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a94f5ff0-66f7-3863-b589-75bfce7b599f | -2.58027 | -47.03158 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f7401ec-4151-3b80-b639-562d48e119d8 | -2.086 | -46.41607 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 337f30a2-0cab-3aae-980c-eb15d69e07f1 | -2.65529 | -48.78938 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70b104bb-d495-3362-b98b-3ecccfa142d0 | -4.17568 | -48.61428 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d53e28a3-6bbf-3fee-98ef-42d97da37e05 | -2.29549 | -50.58731 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87f9fe37-b74c-3b22-b5da-d2874916599f | -2.78409 | -54.21383 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56e8bfdf-5ae2-31aa-a24e-7d3657391e86 | -3.97116 | -41.5212 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9c08a48e-3f2b-33b1-8dbf-c4c57d4d2ba9 | -3.28506 | -48.76502 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed964c01-3d41-36dc-ab6a-6b1bbc60fde6 | -2.05992 | -51.19055 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfd613ab-eb52-3344-b49a-51a2c23a6e9a | -6.82402 | -46.77064 | 2024-11-30 04:40:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f40217bb-a825-3cb3-9222-63a086b38dda | -3.87431 | -46.66658 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8ab8ad3-7e46-3b5d-81d8-5b1152a38970 | -3.08841 | -51.40869 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 92463668-b1e9-31ac-a7d7-4f0786d667ab | -2.72542 | -46.24481 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f20af58-3f01-3419-bfe4-0db6d0c03f42 | -3.73345 | -54.23055 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 05eb9c9b-522a-35f6-879b-1d19c45f4cf5 | -3.24059 | -53.92307 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cf36186a-517a-31a0-938f-91aafb0f8a32 | -2.08118 | -46.46986 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0de5e39-3b29-390d-965c-8f865e230fea | -3.24818 | -50.62537 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df5cb220-cc08-35f3-a3f6-f141ab026f9b | -2.80064 | -53.05064 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e009beef-00cd-38df-aa38-57f94355758e | -1.39777 | -52.00791 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d60b0b3-b553-3075-ae53-a6c14d5b2bdf | -2.72028 | -48.67636 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbbdf825-3ff0-37b7-aa4a-649b2d7b62c3 | -5.87825 | -42.3237 | 2024-11-30 04:40:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 9e0b68a1-c98f-33b8-afd6-3335acf29140 | -3.83956 | -46.56567 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 011a4b66-7a83-389f-acbd-8f03d1247455 | -3.64998 | -51.4115 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aadd4583-f806-34ec-a60b-6a1df8dcbd1c | -4.01552 | -49.00963 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| caa18e3b-dd7d-3cfd-93b4-9195988be36f | -3.79526 | -50.13388 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83f85c79-208b-3f58-b39b-2dbebde7d4d9 | -4.15156 | -43.80568 | 2024-11-30 04:40:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a27cf08c-e771-38e4-b225-28f6c3133a9c | -3.09539 | -51.40982 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3dc13af1-868e-33f0-af36-ed1f3fdf25f9 | -2.20109 | -48.34167 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79673a34-34c3-3dc5-8efa-21f37677f68f | -3.25844 | -53.6424 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8b9cc234-daa7-3c03-954e-137a7b65b8d3 | -1.21247 | -54.19167 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8882307d-3c4b-3a7d-a691-b9f6d6806856 | -3.38849 | -50.31657 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 039f46e7-9bea-30ed-b4d5-d37e83a6a99a | -1.74945 | -52.65533 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f988f6d-54f1-35e0-bf84-dc9692726867 | -2.72944 | -46.26551 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e539c2e1-f14f-3b44-812b-caba2bf637dc | -3.10981 | -53.10733 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dda029ed-2ddd-313e-a3ca-ffa90b3591d8 | -2.82984 | -54.08554 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3f8875d3-0a78-31c8-8af1-594ee9f3a8d0 | -2.23083 | -53.62873 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc1379af-efcd-3207-baa5-5a32c5f694a0 | -3.23312 | -50.31393 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 472eda2e-48c6-349d-9c8e-4733f58c34b6 | -2.62256 | -54.21026 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd44c553-46fe-3dad-b860-f294246e33b8 | -6.00927 | -57.83963 | 2024-11-30 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbb4525b-ebe9-3a3a-9d32-c3dcf18e0612 | -3.49933 | -53.84397 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb1898a1-1706-3240-917e-8147b3a5f20e | -2.29015 | -50.68834 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1c31ecc-4c08-383c-8fbf-ee6927d79039 | -3.93916 | -46.69598 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d6a7b97-ea52-3d6b-b057-cec2382ccfd8 | -3.37551 | -50.42048 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e8bb742-fd8c-37c8-a5ad-e10082b4667e | -2.97257 | -53.28821 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 464d2f8a-842a-3ba4-ba81-8412cbbe4203 | -3.30531 | -50.37247 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6647d9a8-c12d-37f0-b8f7-1bba15886d14 | -2.46427 | -46.57643 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 912cd4da-e65b-37c8-b794-38edfb6f8f49 | -3.4979 | -53.82764 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13983db9-c452-3b8b-8e9d-237e48cdd1e5 | -1.23438 | -51.80669 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 04231754-2834-3cd4-a8d3-4e5414d6d75a | -3.70457 | -45.69164 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c04ac615-0a8f-3f32-9d46-089d64338a63 | -2.66029 | -48.80069 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e380f8a-6696-3185-a5f3-7ae3545f1d0e | -1.64961 | -52.40527 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a3abdf32-8f34-3d5a-8b59-3cb74648bc1a | -2.36644 | -48.54729 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d73399fb-3ba0-3ec4-80a6-dd99668bb6e2 | -3.07135 | -51.25703 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ac48585-d309-34ef-a10b-6343414403f4 | -3.06067 | -51.30233 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77238bf8-c5df-3bd3-8840-ee1ba26874f6 | -1.24854 | -51.78739 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb515604-1549-366c-9588-d52ac7385f3d | -2.60416 | -53.98298 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b604d2a-9697-3324-8a16-e45b739b8348 | -2.29505 | -50.52351 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d9d85f0-83e2-3834-a7c0-943da95b3535 | -2.27945 | -53.77175 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a730374-3338-3213-a0cb-4aaecbc6cca6 | -3.74162 | -51.83652 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 352a6b04-f912-3efc-ba71-d5805924d5cd | -3.46233 | -54.20193 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a27c1d4-46ec-321d-af7b-c2c9eb08c620 | -2.01319 | -46.29995 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38f88ebf-88fa-31cf-b475-11891bb79df0 | -2.18089 | -48.38437 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93cd4058-a7ec-3929-85bc-cc275404e2a6 | -3.97511 | -46.74079 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c7293de-9f50-375d-8afe-8d9ad49ed77f | -3.05549 | -49.53638 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb4f49e2-924b-360f-8bb6-0adf15fd8ae8 | -2.6685 | -48.79142 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4667d8d3-6808-3079-a01c-551e9adcb838 | -3.35926 | -46.666 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1dcbb5a-0555-332e-93f3-a68c072f0f32 | -2.00159 | -47.39314 | 2024-11-30 04:40:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6aeea694-5c06-3c96-bf8e-455fffa61728 | -3.97397 | -46.725 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4c48459-519d-3014-b170-13163a0d4c10 | -3.983 | -43.3891 | 2024-11-30 04:40:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48160e02-3118-3042-b6c6-df655e9ecb02 | -2.77117 | -45.92143 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edd86cfe-86e3-3da1-a738-8481f7bd2e14 | -1.50221 | -48.02447 | 2024-11-30 04:40:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 697c277a-aa29-30c5-a262-4fd32d55afb6 | -3.48597 | -50.21537 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 440f6826-13b0-3c9e-8b3b-b9ede2f6a2f9 | -2.71442 | -46.19893 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3839d68-4c31-3c9b-8602-96109eb5b466 | -3.11663 | -49.49271 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e4a72a4-fb2c-3f3a-bdc8-3085272faec1 | -3.47387 | -50.53104 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8503fc4d-081a-3b12-8a5b-a00a1973ea5e | -3.44139 | -50.02463 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ff2ef224-79af-3250-aec0-9d7790e5f4a9 | -2.65551 | -51.71135 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ac9fade-5a23-375c-b621-e6921d97df9d | -3.93417 | -47.97983 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a48e2c47-f449-31a5-9070-501ac8a9998f | -3.34106 | -53.2094 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6094a704-679f-3385-9d22-5c9c5eba53c3 | -2.22738 | -53.62469 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f68c9db6-2775-3a9d-94c0-ddf5fbc5fa65 | -2.59603 | -46.56536 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README28.md)
