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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcf65319-38cf-35c8-a0c6-722044aa24f7 | -1.98594 | -46.48134 | 2025-12-03 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 338f8552-c1e2-3f26-b601-51a03922582f | -3.23552 | -45.58188 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1819543-224a-3def-89b9-3e5cd1b9a73c | -2.57274 | -49.09852 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7174fb0c-e631-370c-b00d-b52918ce377c | -2.39051 | -49.39278 | 2025-12-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 307605df-bc2c-36ce-a872-1b01b4d5baa6 | -3.25368 | -45.57018 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c60e2a29-e3f5-3bb0-af07-1dd94b7ecb3e | -1.87207 | -46.35695 | 2025-12-03 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 544e4824-d6e7-3d32-8430-db18a9a9e64a | -3.23848 | -45.58659 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0842d910-a6b6-3106-8a7f-a0953d175b58 | -3.25023 | -45.54406 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b62a1cb8-9205-3819-803d-bfadc27bcdd0 | -3.37955 | -50.32042 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7498064a-a1da-3e0d-a48c-eb56724baae4 | -3.23838 | -45.53982 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd36cfc7-97a1-3da7-bd97-8ec5e4d8c5cc | -3.2562 | -45.55353 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 571c3d19-25c6-30dc-be91-6a8a31e5ab36 | -2.66998 | -49.49745 | 2025-12-03 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d39aed0f-39b1-3dc2-a7e4-ad9918d68af2 | -4.42414 | -45.94654 | 2025-12-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79e28dc7-c3d4-32eb-83d4-4c625da38f51 | -3.22599 | -45.57192 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b607d68-dfa7-3e51-adfa-5db814f87480 | -2.70234 | -49.31363 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02130d2c-bf97-3aa7-91e8-838cf7ad7533 | -2.69437 | -51.79488 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 378d0603-0822-3161-b007-ce59d116aa46 | 1.99104 | -55.71336 | 2025-12-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8754cdea-b98f-392a-9dc1-f72359a83773 | -2.8333 | -50.46266 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a24a960-6c0a-33dd-bcd2-4af3399f25df | -3.36589 | -50.75706 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15e41aa9-a6f4-306b-8d93-795ebd1ac4d0 | -3.62722 | -50.24146 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9eb2e0f-5b33-3530-938e-757437c69b32 | -3.38794 | -47.27949 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d36cd4df-04b6-30c7-a614-09c7363d9d76 | -2.73999 | -49.33367 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cf31ac4-cc25-3224-94a9-96e4042f177b | -3.06155 | -49.51665 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08817024-f7e9-354a-911d-2efb5bc9d039 | -2.24053 | -48.31002 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bc26c07-e323-30c3-817d-1374e2139264 | -2.83668 | -46.71881 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdeb3bc6-17aa-344a-abc1-0c8b8fb909ac | -3.23814 | -45.55072 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9edc0668-46b6-3456-822c-c45565a30467 | -3.24772 | -45.56073 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b58b2ba1-1e88-30b5-9c4a-f030e331281e | -1.89347 | -46.28739 | 2025-12-03 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0caccd6-5f00-3008-930f-c6230e8312a5 | -3.03634 | -50.24114 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3431f879-7d08-3041-a392-8f84960a4c53 | -2.46817 | -48.11693 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e7e3cbe-14ca-3af8-a7f6-79c0dea6006c | -3.45816 | -49.99952 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69125b3e-5bed-3c79-a023-e5a79dc54d40 | -2.62682 | -49.23094 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a716eea-28bf-3bb6-a1ba-d2cd3a07a318 | -3.23617 | -45.57774 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 73d5bc38-9c40-3902-80c9-81eb6b214a37 | -3.23675 | -45.58454 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25731ce6-db56-3254-9832-f48d2c38c883 | 0.48057 | -51.15213 | 2025-12-03 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 11e8c4d1-0853-3367-846c-bc116e494ec9 | 1.97458 | -55.73954 | 2025-12-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5b6d204f-bff9-346f-ba74-40751224e7dd | -2.35558 | -50.10941 | 2025-12-03 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 97e16ce0-dc9f-3408-88c1-ab5278c30f81 | -3.22136 | -48.60897 | 2025-12-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01321125-5b90-332a-a06a-f9d94f7f6615 | -3.24411 | -45.56016 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 815fcce8-ee93-35f9-bb81-84d9f6f872e3 | -3.24005 | -45.55283 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a053f065-79cc-3bba-a5b7-d9822b8a79ab | -2.92255 | -48.23376 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fa573332-7e56-3718-ae0f-7d01116f1d03 | -3.23737 | -45.58038 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47362e61-353e-3537-af64-2718a055f0ef | -3.24432 | -45.54922 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7babc006-2890-3944-9f38-88965dcbad58 | -3.23811 | -45.56529 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f325d917-905e-310a-855c-d2f34238b9f3 | -3.25007 | -45.56962 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0552a44-fe7b-3f95-8f1b-a66faa593d67 | -2.38718 | -49.39226 | 2025-12-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02ada333-6477-3c87-b8c0-22a96bc73a0c | -3.47662 | -51.3633 | 2025-12-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab630057-ce7b-32bd-96bf-877a51dbf5ca | -2.62629 | -45.13951 | 2025-12-03 04:38:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3f8272e0-8973-3be6-86b3-eb7c08954386 | -2.881 | -50.4701 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53f84bd5-bc5c-3a65-87a8-f375e06c19cb | -3.6106 | -50.36768 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e400f7b4-9ed0-394c-887b-f8175885383e | -4.66296 | -49.37179 | 2025-12-03 04:38:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8403c77-770d-37ec-8996-7c8693173960 | -6.22838 | -47.33173 | 2025-12-03 04:38:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0138c602-b2fc-3ce4-a969-3b18e0ed2432 | -3.24882 | -45.57792 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42947e77-af33-380c-a05a-0858267ed7db | -2.89286 | -53.29873 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 523642a9-8427-3113-8eb9-273af96634b3 | -6.28517 | -39.68532 | 2025-12-03 04:38:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ea608e19-df0b-30d9-a908-085b8b51c40a | -3.23127 | -45.58547 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85800a44-066f-3f2f-828a-6af8e9bc8b2a | -3.24285 | -45.5685 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4ac40b9e-c8cd-3fe8-8acf-4395f5b275aa | -3.21752 | -48.6119 | 2025-12-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a1cce56-a3b0-3ba8-840a-ad0e310cede9 | -3.24042 | -45.57415 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d91cbda1-4e96-357d-951f-2b2e90026c60 | -5.18646 | -44.80061 | 2025-12-03 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18a4edad-a05b-3b66-b5ac-2bb95a185b16 | -2.38773 | -49.38878 | 2025-12-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f51afc94-f47c-3bc4-bfd3-cf43f9220f71 | -2.89321 | -53.29581 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 469068af-a377-3cb5-8568-ba5742b6813d | -3.31185 | -42.50523 | 2025-12-03 04:38:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b227ae77-7871-3ddc-a3dc-34e73525ab3d | -3.36932 | -50.75759 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55e43abf-2556-31db-a5c7-27a66d1d08bc | -3.93501 | -47.56098 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6ed5d04-4eba-32c2-b35d-70e64d9e439c | -3.03373 | -51.09692 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3f75d4a-aaea-3fd7-b9dc-c7fbafb33799 | -2.3844 | -49.38826 | 2025-12-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65acdab7-c4e8-317d-a6d5-3136b69898e8 | -3.43187 | -50.03537 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 418b3e30-db2c-32d8-8363-7b4d45bcd993 | -2.59488 | -48.9572 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 308cbcc4-287a-331a-986d-5fd3fb1f31b3 | -2.80337 | -52.90248 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f734de8-01cb-39e4-8906-83397be5c13d | -3.23385 | -45.56889 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| a983b243-e809-3ac3-8645-e17e660a1d05 | 1.98239 | -55.72361 | 2025-12-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40d8850b-b270-39fd-b6d1-8cf703ac0713 | -3.2407 | -45.54868 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e89483ce-68a9-3887-a83e-ee3d397fe1ab | -3.2211 | -45.57967 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 709c6ae1-c7d5-33a0-9ce6-f5009e8b1126 | -5.85502 | -39.94443 | 2025-12-03 04:38:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 787a1800-f5f7-3be1-9856-7f26eb6d81c8 | -2.60202 | -49.25903 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17c5344f-c0eb-3d2e-8197-15cbd5b770bc | -4.51111 | -44.65102 | 2025-12-03 04:38:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e043e2d5-07fc-392b-910e-b0323d671ab2 | -6.26012 | -37.2375 | 2025-12-03 04:38:00 | NOAA-21 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9d81b8be-0240-3f42-b80e-1e14fa17e132 | -5.85453 | -39.94791 | 2025-12-03 04:38:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a66c6b6d-b7ba-3177-8307-eb79a54f2ed9 | -1.9791 | -46.48027 | 2025-12-03 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 883ff4bc-aa8d-33fe-a49f-b82d56be44bd | -1.53417 | -47.21654 | 2025-12-03 04:38:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e371782-ef71-3885-9699-1347280eff45 | -3.23283 | -45.55174 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17836c4a-e81c-3337-b176-6a5df5485b76 | -3.24661 | -45.5435 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12100f81-02d2-396d-97e6-2cde7fd6b794 | -3.27494 | -50.75473 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fe95e15-a5ae-343a-8854-cb25d4106de9 | -5.03371 | -41.01287 | 2025-12-03 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 81b58b37-95a8-381e-8d0d-cf3f6d28102f | -5.02866 | -41.01265 | 2025-12-03 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5970b6a6-97e8-3300-b9a1-31ba949ac4aa | -3.05014 | -48.4199 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 778c2181-0c70-3efd-a647-46895a6f70ce | -3.242 | -45.54036 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bb074b4-ee16-3e8a-957e-2032960d758f | -1.91178 | -54.08439 | 2025-12-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a78bdfc3-a8a2-3112-b9e5-d2f9e6990628 | -3.5657 | -42.70975 | 2025-12-03 04:38:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07985378-f1d7-3d09-ae53-f64159bb902d | -3.84174 | -50.89942 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dab8eedf-5dc1-3740-875f-6450fe71bdd8 | -2.89632 | -53.30142 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 93b28153-8591-342c-af3d-7b71f87021f9 | -3.2405 | -45.5596 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 03c60a78-576e-3ca9-b6a7-5f9988a6467c | -3.24561 | -45.54091 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 229ce91f-340c-3e60-ad0d-b2b38a81ca82 | -3.23487 | -45.58603 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 385ad9b0-ce90-3f09-a1cb-b7ae427fed71 | -2.90978 | -48.72885 | 2025-12-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a77b4d3f-dfca-3774-9cc8-eef278dd58af | -3.85312 | -47.06448 | 2025-12-03 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45c8f828-9d4b-3451-8dbb-5fb6683736b7 | -2.92963 | -45.46101 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f425623-eec8-3a1b-b84e-800e8581803b | -3.84114 | -50.90315 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 598a4dc5-ea4d-3266-8940-35e2f033b583 | -3.23377 | -45.57982 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README15.md)
