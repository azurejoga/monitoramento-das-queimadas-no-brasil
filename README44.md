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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 213e7f4b-4af9-3069-9e51-0fe9a8316667 | -1.2964 | -51.741 | 2024-11-18 07:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 6dd129d6-9e67-39da-848e-68c84d6ae708 | -1.2964 | -51.741 | 2024-11-18 07:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 77a166a7-706e-3919-99a9-d4072b442e61 | -1.2964 | -51.741 | 2024-11-18 07:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 0a242204-d457-3633-b460-f75335d44a07 | -1.3148 | -51.7408 | 2024-11-18 07:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a4629434-7fb2-3274-a6c2-b7181c8ffc5a | -2.5847 | -51.7181 | 2024-11-18 07:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| d5735552-73b1-3d3c-b459-135b92646e6d | -1.2964 | -51.741 | 2024-11-18 07:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 909e6ebd-e693-38c5-a2f1-e640cfb9a0c2 | -1.3148 | -51.7408 | 2024-11-18 07:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f328b8c2-782a-315d-8709-9b0fa3706183 | -2.5847 | -51.7181 | 2024-11-18 07:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 3114b207-d33b-3b75-9b33-ebd82155ea66 | -1.2964 | -51.741 | 2024-11-18 07:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 10579197-bc1d-3fa8-bd3a-da16d4a0df19 | -1.3148 | -51.7408 | 2024-11-18 07:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 086e64fc-d333-3211-a81c-44b2b15c48a3 | -17.6063 | -57.5715 | 2024-11-18 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| c6b12ac1-1843-3ad2-8dd9-2dd02a21b114 | -17.6059 | -57.5921 | 2024-11-18 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 6c845c76-1861-35bb-91e8-88e009a7ee61 | -17.6256 | -57.5897 | 2024-11-18 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 9f49ce75-8f0b-36e1-80f5-7a3760427666 | -1.2964 | -51.741 | 2024-11-18 08:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 01756337-b4e9-3787-b47b-fc0e5bf7edf3 | -17.626 | -57.5692 | 2024-11-18 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 6d859cd1-2566-3972-a71b-0c008a03ad67 | -1.2964 | -51.741 | 2024-11-18 08:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ed17f1ea-408b-32e9-9cec-fd28e30aaed9 | -17.6063 | -57.5715 | 2024-11-18 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 0d07b7ce-f3d2-3139-8307-9f28442968d8 | -17.626 | -57.5692 | 2024-11-18 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| d28c9c0e-5a78-337c-9892-c4533ace5dc8 | -17.6063 | -57.5715 | 2024-11-18 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| ea05c73b-ca8c-3ad4-baf3-4e4bd564e552 | -17.626 | -57.5692 | 2024-11-18 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| c69d4406-ac1e-3ec1-b21c-0eb7d0cdea48 | -17.6256 | -57.5897 | 2024-11-18 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| f5e27e99-c20d-312e-9499-be8ea33ad59d | -0.8597 | -47.5605 | 2024-11-18 10:50:00 | GOES-16 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 739dfa94-fa1a-3b84-83e5-0a4ca3bb6c4d | -6.39 | -44.76 | 2024-11-18 12:00:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c3efa19-fac6-3197-9d7f-04ce0bd8e909 | -6.39 | -44.71 | 2024-11-18 12:00:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3885047a-5b5f-39fb-9995-a48d5ced9957 | -7.0976 | -39.267 | 2024-11-18 12:30:00 | GOES-16 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 752bb872-cce9-3cbf-b538-e3615d7b326b | -6.9424 | -42.8126 | 2024-11-18 12:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| d0c45f99-b8ba-33f5-b0c7-d0bf4d521bbc | -6.9424 | -42.8126 | 2024-11-18 12:40:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| b5532303-d277-37c0-b418-eab86d16de54 | -3.8846 | -43.1544 | 2024-11-18 12:40:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 6d86cc88-c5c5-38aa-85ec-092bca4d0575 | -7.1941 | -39.1301 | 2024-11-18 12:50:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 136.9 |
| 535d88dc-e003-3ae7-b1fb-6dfa8a2611ee | -6.9236 | -42.8144 | 2024-11-18 12:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| e56478b9-3ccd-3f10-bee8-e40d53dbe928 | -3.8846 | -43.1544 | 2024-11-18 12:50:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 83976e20-883d-3c94-991a-4e6fcb14f179 | -6.9424 | -42.8126 | 2024-11-18 12:50:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| ef030e97-42b6-3ced-930e-a1f2970d9a7d | -6.3964 | -44.7396 | 2024-11-18 12:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 587.6 |
| d5509250-655b-33fc-ac27-99c5696f7aad | -3.086 | -42.371 | 2024-11-18 12:50:00 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 589d9dd5-6329-344b-af77-5ca1369f355e | -6.9236 | -42.8144 | 2024-11-18 13:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 45e74a4a-8d09-3709-9235-1ddf4c408cd3 | -7.1941 | -39.1301 | 2024-11-18 13:00:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 108.8 |
| ce8de037-a68b-39eb-b729-4119e7760d6c | -6.3964 | -44.7396 | 2024-11-18 13:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 553.9 |
| e5117125-8da9-37be-adef-f8aa3e4f26e3 | -6.9424 | -42.8126 | 2024-11-18 13:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 6c7e120f-15f7-3c40-9365-3e30327827e6 | -7.8865 | -44.2134 | 2024-11-18 13:00:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 0f181427-87ff-3ccf-b87f-d493b9c45f00 | -3.8846 | -43.1544 | 2024-11-18 13:00:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| cd583162-44bc-3ca3-a7eb-b88bf1073b99 | -6.39 | -44.71 | 2024-11-18 13:00:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f398059-99ff-3a6e-adb9-38ce6e6fb279 | -6.39 | -44.76 | 2024-11-18 13:00:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bbcebcf-cfc5-3756-8619-6a6f7e989a68 | -4.447 | -42.8889 | 2024-11-18 13:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| fade4819-741a-3303-9301-abba0fdaf474 | -6.9424 | -42.8126 | 2024-11-18 13:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| c1acc507-b790-35ff-bf2c-d37bb1e6814d | -7.8865 | -44.2134 | 2024-11-18 13:10:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 84de6eb2-d81d-3a0c-b6f3-2406a05660f4 | -3.8846 | -43.1544 | 2024-11-18 13:10:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 28f2d648-1ace-3a1f-b47f-a9bd0a9e1240 | -6.3964 | -44.7396 | 2024-11-18 13:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 482.1 |
| 2f7942c3-3f9c-3823-ab60-b5bb13dfb3c7 | -3.3096 | -42.4791 | 2024-11-18 13:20:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b70c67b7-3b68-37ca-a38c-72cc406eb18e | -7.8865 | -44.2134 | 2024-11-18 13:20:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 2c3c90d1-6905-3411-b26f-82c27157dd1b | -6.9424 | -42.8126 | 2024-11-18 13:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| 7f6f0d4d-abd2-3b73-922c-e9d2ccbe5482 | -4.9059 | -44.022 | 2024-11-18 13:20:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 1623ce3c-386d-3363-b022-ff7f670e2fee | -3.8846 | -43.1544 | 2024-11-18 13:20:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| d4878a41-7584-32e5-89c9-56a9f0eff653 | -4.447 | -42.8889 | 2024-11-18 13:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 9b5c6920-9fe5-346e-8e67-a13694a921aa | -4.6775 | -44.6089 | 2024-11-18 13:30:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| fcc33d40-5d60-3afc-8e39-7275ca4c1518 | -3.1986 | -42.2716 | 2024-11-18 13:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| e3f232ee-5ef3-3017-b634-b3a87efaa1b0 | -4.3968 | -44.7389 | 2024-11-18 13:30:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 7ebf15a0-e2c6-36bd-8a3e-b3731bdd4f9c | -3.8846 | -43.1544 | 2024-11-18 13:30:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| f9b08588-c0ae-3cf5-8356-4985ba41afbf | -6.9424 | -42.8126 | 2024-11-18 13:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 0b0ff032-13e8-34c0-8ee4-d34413b0cdc2 | -7.8865 | -44.2134 | 2024-11-18 13:30:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 587dafb6-176c-3c2a-a811-05b268885049 | -4.4468 | -42.9123 | 2024-11-18 13:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| d9238b19-bab7-3a46-9985-4b175829335f | -4.447 | -42.8889 | 2024-11-18 13:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| da940ef3-15af-3625-85c4-e5ae87a1b02f | -6.9236 | -42.8144 | 2024-11-18 13:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| c502797f-d860-3e74-9400-60f243a02fd0 | -6.9424 | -42.8126 | 2024-11-18 13:40:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| cabff506-ea90-30f1-8f0d-83d9d34fd816 | -3.5374 | -41.8517 | 2024-11-18 13:40:00 | GOES-16 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 126.9 |
| 76d69204-2f16-3762-ba33-131d5906b551 | -4.6775 | -44.6089 | 2024-11-18 13:40:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| b48ce83c-6486-360e-8cd2-b7d8fb00a341 | -3.8846 | -43.1544 | 2024-11-18 13:40:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 9c926b11-2f21-390c-87ba-c1028978d022 | -9.4883 | -47.2339 | 2024-11-18 13:40:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 71e0b380-7080-314c-8353-dde80a70c3c2 | -4.4468 | -42.9123 | 2024-11-18 13:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 6d7f8eb3-0b15-34b2-8952-d66e66284d80 | -6.9236 | -42.8144 | 2024-11-18 13:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 03e0897b-45b7-3311-ba87-e9c208106fe1 | -3.3531 | -41.358 | 2024-11-18 13:40:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 129.0 |
| ec07f21e-04c0-3faf-8f1b-dc04285ce029 | -4.3968 | -44.7389 | 2024-11-18 13:40:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 735ec1b1-5733-307c-aa09-1a865e4bc89f | -4.6775 | -44.6089 | 2024-11-18 13:50:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 67eff095-83bc-355c-8135-e2a68bac8f70 | -6.3964 | -44.7396 | 2024-11-18 13:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 563.7 |
| 87a9f543-badf-3571-abb9-0f4851b2db0c | -5.2848 | -43.4179 | 2024-11-18 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 1db4ef5e-23f2-3791-9be9-80d196ce8ce0 | -4.3968 | -44.7389 | 2024-11-18 13:50:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ac9af475-7519-3edd-8409-fdb41ef17dcc | -3.3531 | -41.358 | 2024-11-18 13:50:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 106.8 |
| 1d334d46-010e-31ce-bee3-774906ae4672 | -7.8865 | -44.2134 | 2024-11-18 13:50:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 3ce3bdd1-fbcb-3e2f-a8b2-2e5259631c63 | -3.8846 | -43.1544 | 2024-11-18 13:50:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| f92bfed2-e77a-32b8-a210-01b9b52d8d87 | -6.9424 | -42.8126 | 2024-11-18 13:50:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 30686a4f-b46e-37c5-99bf-7a7aa1d0a436 | -6.9236 | -42.8144 | 2024-11-18 13:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| c4a1ab99-11e9-36ec-80ff-20c3de503f27 | -7.8865 | -44.2134 | 2024-11-18 14:00:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| b1eb9cef-a413-3f73-9ec3-c505f5e19a12 | -21.3645 | -54.8207 | 2024-11-18 14:00:00 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 1d5b47c5-e0a6-361d-8470-fba6ff1cc542 | -6.9236 | -42.8144 | 2024-11-18 14:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 550ca146-4e20-313a-90b7-217c259b2e44 | -3.5374 | -41.8517 | 2024-11-18 14:00:00 | GOES-16 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 7779a69a-3908-3ca3-a6fc-d935e6a97378 | -2.879 | -42.7327 | 2024-11-18 14:00:00 | GOES-16 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| e6c304d7-ec5a-3118-9632-56e0aface281 | -4.4468 | -42.9123 | 2024-11-18 14:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 8bf1b973-0aa0-3172-949e-95990546d91c | -4.4038 | -43.7064 | 2024-11-18 14:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9ae62826-bfaf-3597-a097-eec68a07677e | -8.2668 | -43.9651 | 2024-11-18 14:00:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 4c857698-11b7-3b41-9280-4c06fd1ab0f3 | -4.3968 | -44.7389 | 2024-11-18 14:00:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 5b08b47d-f1c1-3542-a554-8a5fd1bda427 | -3.8846 | -43.1544 | 2024-11-18 14:00:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 58f2c5ba-adb8-3a4e-ae60-e662c16db8a6 | -6.3964 | -44.7396 | 2024-11-18 14:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 602.9 |
| 63a9a50f-e950-3d92-bee0-3fe3235b2c9c | -6.9424 | -42.8126 | 2024-11-18 14:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 2df47ed4-6756-3784-a8d6-750e5de0cfed | -6.42 | -44.72 | 2024-11-18 14:00:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7967e094-046f-3565-a1ef-5991e2ffeeab | -6.39 | -44.76 | 2024-11-18 14:00:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57d907e4-3300-35cf-926d-7d35b38e62d3 | -6.39 | -44.71 | 2024-11-18 14:00:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85192a51-3f21-3f9e-8c32-2254cac5b9b2 | -7.8865 | -44.2134 | 2024-11-18 14:10:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 5fea074b-7c0a-373d-8e94-76dc97fbe1fe | -4.4468 | -42.9123 | 2024-11-18 14:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 04b363de-659b-3856-a2eb-412104c2b405 | -3.5375 | -41.8279 | 2024-11-18 14:10:00 | GOES-16 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 20734fcd-3c07-358c-a019-95a09028774f | -20.4055 | -55.0023 | 2024-11-18 14:10:00 | GOES-16 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 5cdba307-4170-33b4-8f26-2e0f44b27a86 | -4.3968 | -44.7389 | 2024-11-18 14:10:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |


[Clique aqui para ver as próximas entradas](README45.md)
