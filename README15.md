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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04a5439e-64af-36f6-be23-b0b9375faad1 | -10.10426 | -36.19448 | 2026-09-17 03:00:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 573b80a8-e275-3447-88a3-dc3c11dd09c3 | -2.6965 | -57.6278 | 2026-09-17 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| c78acdda-8023-30a9-83b7-086daebd9dbc | -9.112 | -45.7294 | 2026-09-17 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 235.9 |
| 47948996-34e0-3569-9604-05ff7acf984d | -9.1123 | -45.7067 | 2026-09-17 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 2af6c9b9-3387-34ab-9bbe-2744eb8fd9be | -5.647 | -44.8192 | 2026-09-17 03:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 982228bf-29f5-33f9-b65f-af1528506ade | -9.628 | -45.3521 | 2026-09-17 03:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 6234cab0-e95d-3647-b4bd-7aeb248fa5bd | -5.7756 | -45.0826 | 2026-09-17 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| eb6dae55-9272-3ab1-83bd-bfadde94d220 | -9.0931 | -45.7314 | 2026-09-17 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| f503a476-487b-317d-89b4-58ff0981c365 | -3.4757 | -54.7171 | 2026-09-17 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| dee097ec-c3c4-3cdf-b597-acf891c2a229 | -5.7754 | -45.1053 | 2026-09-17 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 292.9 |
| 15deb29f-3c0a-344c-aefd-6329c188b333 | -5.6472 | -44.7964 | 2026-09-17 03:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 8d112554-3783-38a4-8b32-fffd81a38946 | -3.4757 | -54.6972 | 2026-09-17 03:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 79dc1e0c-b1ad-358a-80ec-d589261870d6 | -2.9582 | -50.3149 | 2026-09-17 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 4f21b01a-fa82-355d-a40e-ecb94fd7d81c | -9.4946 | -45.4134 | 2026-09-17 03:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 4a404a9a-407c-3695-8735-33d11a45171e | -5.7567 | -45.1067 | 2026-09-17 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 7312d227-f650-31e1-8092-6e6f10fe14ac | -5.7752 | -45.128 | 2026-09-17 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 7be26cee-347f-3d7b-a828-b4e2f7c28e41 | -9.6091 | -45.3544 | 2026-09-17 03:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| b3a75cc5-97b6-3aaf-8019-7df3d35de277 | -2.9581 | -50.3359 | 2026-09-17 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| b88fd003-d271-3ae0-b180-6dd9ac5fd0c7 | -2.9766 | -50.3354 | 2026-09-17 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| e5cb9157-f6ac-3a27-87bd-6ee4d9f648a5 | -5.6285 | -44.7977 | 2026-09-17 03:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 69cd9462-7930-3729-a53f-f0bb06fe126b | -2.6966 | -57.6084 | 2026-09-17 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| a9004a93-f4ba-345d-8fe8-f6825eefeed7 | -12.46 | -50.84 | 2026-09-17 03:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 04871dbc-2e07-39e0-8a2d-6827cdebbbe7 | -5.76 | -45.09 | 2026-09-17 03:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07f80dd1-a973-30d2-b40b-c4989ec528df | -12.49 | -50.85 | 2026-09-17 03:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98bacd3b-f18f-3313-b02c-ec59b814f5e3 | -5.64 | -44.8 | 2026-09-17 03:15:00 | MSG-03 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60b088b8-b933-3ee9-ab0a-3ea29c4885e0 | -12.46 | -50.79 | 2026-09-17 03:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d2e0d1bd-40e5-3d47-88b9-37a38534d1be | -8.4796 | -57.6478 | 2026-09-17 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4509abbc-ee84-3f88-9ed8-cc6b29639116 | -3.4757 | -54.6972 | 2026-09-17 03:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 9e5998fd-5514-3d99-ace5-01c046468747 | -2.6965 | -57.6278 | 2026-09-17 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 6602636f-ea7a-37f1-a903-4fb97ba2ffe8 | -5.7754 | -45.1053 | 2026-09-17 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 311.0 |
| 677ea6c7-899f-3e8b-9328-3d6511f57830 | -2.9766 | -50.3354 | 2026-09-17 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| a8119d73-fec2-35a9-8d8f-49b1d1e07197 | -9.1123 | -45.7067 | 2026-09-17 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 63346972-d5c5-3cde-b302-ea68bad2dacf | -9.131 | -45.7273 | 2026-09-17 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 4aae27d2-87f1-3009-912e-923954589322 | -8.4982 | -57.6468 | 2026-09-17 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 12eab07d-6f2a-3b41-9695-c5e5ddc61825 | -9.0931 | -45.7314 | 2026-09-17 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 2fd2e99d-5b31-398c-835c-204b6008a47e | -9.112 | -45.7294 | 2026-09-17 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 340.3 |
| 1ef198f4-742b-3eea-be05-57f000230a0a | -2.6966 | -57.6084 | 2026-09-17 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| cc0c4698-23ce-3df2-8347-50e8b1cfdd1b | -2.9582 | -50.3149 | 2026-09-17 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| c89e489f-9709-38d3-ad57-00c6a62d042b | -5.7567 | -45.1067 | 2026-09-17 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 3bf50d41-e500-3a74-93a0-9ccbc8f7830c | -2.9581 | -50.3359 | 2026-09-17 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| fee23f7f-72f7-3fd3-a6e7-136811623f73 | -5.647 | -44.8192 | 2026-09-17 03:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 394e8e4d-c2dc-3bac-bc4e-c1cbab3ef9e5 | -3.4757 | -54.7171 | 2026-09-17 03:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 294e01ff-435b-3c8e-85f8-c3141e4daa6f | -5.6472 | -44.7964 | 2026-09-17 03:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| da2f1658-95c7-3dbc-8fd6-d0be3af8a0e1 | -5.7752 | -45.128 | 2026-09-17 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 11d136c0-57df-3c74-87c9-00da15da358c | -5.7756 | -45.0826 | 2026-09-17 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 565e5674-8c58-3522-8476-4978f2401598 | -3.4757 | -54.7171 | 2026-09-17 03:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 2f9fbabe-4c69-3cb8-9b17-6f17a1a2e9a2 | -9.0931 | -45.7314 | 2026-09-17 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 123732d8-95df-3e8f-9665-37d6b7986d0c | -2.6965 | -57.6278 | 2026-09-17 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 57ce261a-452e-368c-8f5d-9b8d38f40d1d | -9.112 | -45.7294 | 2026-09-17 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 299.2 |
| dc13a8c3-213d-3930-a78b-562d1e7cf19c | -9.0934 | -45.7088 | 2026-09-17 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| b1ccb9ff-bad6-3ba3-8928-1a88cc1a2963 | -8.4796 | -57.6478 | 2026-09-17 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| fbebc370-3d96-390c-a072-869849dc2da3 | -8.4983 | -57.6271 | 2026-09-17 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 3ccd7364-b825-3a2b-b814-e242525a3f6f | -8.4982 | -57.6468 | 2026-09-17 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 6f371e3e-c19d-3222-bfd4-ffe8f55e9f06 | -9.1123 | -45.7067 | 2026-09-17 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 9a5ad50b-1fbb-3710-b842-50dc2090047d | -9.131 | -45.7273 | 2026-09-17 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| b5b0d9ab-cd2f-37d5-b744-58c216dc4f8f | -8.4797 | -57.6282 | 2026-09-17 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b624e809-a3a7-3ba7-9dd4-699c92153d81 | -4.80788 | -42.89004 | 2026-09-17 03:34:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bf1ddbf6-73fe-3760-bed1-97f89beccde0 | -4.55635 | -42.95149 | 2026-09-17 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e58b2b4c-4bb8-3ef4-a6ec-5d9338ca0311 | -4.80896 | -42.88405 | 2026-09-17 03:34:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 72cc5739-facf-3d5b-beea-8c2a3b422bc8 | -4.56313 | -42.94773 | 2026-09-17 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 197f3e6a-af28-3238-8c96-f6448426016d | -4.54963 | -42.94488 | 2026-09-17 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fb3efe20-fafd-33af-90e1-3d0d1d574c10 | -4.5507 | -42.94407 | 2026-09-17 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3d0fa3db-11f4-3d16-b53a-73ec7f4b9647 | -4.55745 | -42.94547 | 2026-09-17 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 92297946-9d6d-33c5-9a89-1c3e26752546 | -4.55638 | -42.9463 | 2026-09-17 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 61ceceed-e82f-35b3-9d40-49949e4f4a2c | -5.62488 | -40.85237 | 2026-09-17 03:34:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a11e342a-23ea-3dab-a37e-726ce9453465 | -4.5496 | -42.95012 | 2026-09-17 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4e77a9d5-5c2a-3c3c-8311-a87186481fc4 | -4.55532 | -42.95234 | 2026-09-17 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 65e8b5fa-3330-357f-9b02-c6d691b3c6ec | -4.54857 | -42.95094 | 2026-09-17 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| da7592b8-5510-3f03-85d4-ff0fc4aef890 | -7.46203 | -42.10558 | 2026-09-17 03:36:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b18d0145-2afe-32b0-b9d4-272336ede335 | -9.31142 | -40.24905 | 2026-09-17 03:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2e70195a-0970-331c-96b2-c86cedb280c3 | -11.27183 | -43.46144 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f6d59e0-1956-310a-9120-4daa151c13ae | -11.20555 | -42.82346 | 2026-09-17 03:36:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f53ffc08-9d8f-3cda-a101-05bd6f273090 | -9.61821 | -45.36266 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0d91c391-06e5-3aa0-bdd9-1cf09aacf81a | -10.54824 | -44.8576 | 2026-09-17 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86a0b32d-9768-3fd2-876e-e84d02eae702 | -8.39794 | -42.21219 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 499c4eef-79ad-39fe-9fa1-bda26d24e2b9 | -6.93778 | -41.70391 | 2026-09-17 03:36:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3184bca6-3823-3300-ae02-d229503f8e63 | -11.275 | -43.47786 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7b16b1f-bc6e-32be-9e79-1646e27083b0 | -7.37088 | -44.48486 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd3073cf-ad34-3d06-be3a-1bfaca78e074 | -7.94742 | -44.8337 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f77b954-ce0d-3f26-91e3-8b8165c0a99b | -9.31205 | -40.24573 | 2026-09-17 03:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7163283d-8823-36ff-b1c0-67d5bc5ea572 | -9.95341 | -45.30999 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc615f61-aec8-32a6-8f45-1d5a0c983d6a | -8.38635 | -42.20732 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 14bc7c54-98dc-39f8-a6e3-282e4b8d6934 | -9.94924 | -45.29385 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd7a50a4-b4ab-3cbf-861e-c2d63efc8d32 | -7.72668 | -42.49504 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 53139624-8b0d-3d91-9d97-07850e3f3c65 | -7.18891 | -41.81142 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c23ad99f-899b-3312-a8c8-b8d1f51d6546 | -7.03978 | -42.06584 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a574cc1d-02b1-30b3-9c0b-07250ded6f68 | -6.31737 | -40.1527 | 2026-09-17 03:36:00 | NPP-375D | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ed92fb43-99ab-3774-b519-cfad74401bd3 | -5.2962 | -43.64023 | 2026-09-17 03:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e3b99a3-91be-3854-9037-9b95f3c1b6f7 | -10.03879 | -45.56907 | 2026-09-17 03:36:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ea785e70-5473-39ee-898c-fb0a8ae8f1a9 | -10.04027 | -45.56189 | 2026-09-17 03:36:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b3ec73ea-bcf5-386b-8dca-30f0f9a83e7c | -5.28724 | -43.6365 | 2026-09-17 03:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13774a7a-7c85-3e8b-ad7b-c6dd6a35d6b5 | -7.03472 | -42.03547 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ee40bc7e-3d92-3ca0-b78c-5a0151f48313 | -7.71953 | -42.49841 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7083fc52-a5d2-38a8-b57f-7d7074d7b7e6 | -7.14297 | -42.15519 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 68fc6cd3-c860-3daf-b2ad-0abc3dfba461 | -8.2654 | -42.18193 | 2026-09-17 03:36:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 619bc483-3f7b-3389-9cca-0f31abdc04f9 | -7.10981 | -43.10443 | 2026-09-17 03:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 69653b46-c62f-3e3c-9ee9-d5a2ad9fd115 | -7.03164 | -42.075 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ff0d4a99-a0ef-39f5-adc0-673594d25be9 | -8.39332 | -42.20386 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d8ac11f8-d5f6-3e36-b93c-782deb3d8ca1 | -9.47223 | -45.44643 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d66b8135-4c75-31b1-a5cc-da5992df0134 | -7.8121 | -44.85927 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README16.md)
