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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 479f692c-6133-3907-bb02-a38b25af9b46 | -10.912 | -44.6816 | 2024-10-14 13:16:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| a2d68303-8e10-37de-b8b8-9edb8477862f | -10.8925 | -44.7074 | 2024-10-14 13:16:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 70ca2540-e107-3e4a-86d3-6f0b3f02f670 | -10.9307 | -44.7021 | 2024-10-14 13:16:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 4029bfc9-32e2-392f-8ca9-8f349974e5f9 | -10.9717 | -44.5342 | 2024-10-14 13:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 970c411b-836e-3599-ae7d-8632aab8fff5 | -11.245 | -44.1924 | 2024-10-14 13:16:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 2ab1c356-75e7-347e-bd5d-bbd93d39be03 | -11.2258 | -44.1952 | 2024-10-14 13:16:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 1a8af8c8-bfc7-3983-b67f-366218400516 | -12.5962 | -44.7783 | 2024-10-14 13:16:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 274e7b22-ffd4-3205-872e-f5726f952435 | -12.6159 | -44.7519 | 2024-10-14 13:16:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 9c81cc18-a74f-3d7e-ab2a-b8c9856f531f | -13.3889 | -44.694 | 2024-10-14 13:16:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| f7597325-badb-3102-ba0a-a983faca6939 | -9.4888 | -45.8228 | 2024-10-14 13:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 19c70b23-33fc-3e9a-be7f-78308de60b15 | -9.4892 | -45.8001 | 2024-10-14 13:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 9a419322-b92d-3186-a2b3-8a19586dbd97 | -9.4368 | -45.4884 | 2024-10-14 13:25:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| e00026d9-4ef8-3a6b-bace-27ceba2dc6e9 | -9.4699 | -45.8249 | 2024-10-14 13:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 71c223c7-9cd9-35db-b67e-30926ebb1ec7 | -9.4175 | -45.5134 | 2024-10-14 13:25:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| ce991219-0753-3cc4-86f3-fbd9f4552337 | -9.4702 | -45.8023 | 2024-10-14 13:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 254.3 |
| dfac1fa7-b363-3b2d-95a5-9ce401fa5ab8 | -9.4365 | -45.5112 | 2024-10-14 13:25:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 283.9 |
| aed7122a-379b-36c8-8441-2b7ff79382ba | -9.8504 | -47.0162 | 2024-10-14 13:26:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 44da8639-5cc7-3357-a80c-f100d1a431f9 | -9.9777 | -47.3795 | 2024-10-14 13:26:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 1253d004-3b3a-3734-a027-fc0078313339 | -9.9414 | -47.2727 | 2024-10-14 13:26:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 17fec2ba-66f0-394c-a7b5-4b0eb2e1efa3 | -10.3493 | -46.5777 | 2024-10-14 13:26:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ac973115-6b0b-3de5-9367-e32fb4bf7e23 | -10.349 | -46.6002 | 2024-10-14 13:26:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| c2114d5a-641f-369d-b83d-bd3a064027ce | -10.4716 | -49.9624 | 2024-10-14 13:26:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 699208b9-0454-3bca-81bd-99e9f57ba5b8 | -10.9061 | -47.4253 | 2024-10-14 13:26:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| d09e72a6-a9ce-3419-885d-75c6ef5eaf36 | -10.9116 | -44.7048 | 2024-10-14 13:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 2403097d-170d-30eb-b657-2b4eeb0ee3d5 | -10.912 | -44.6816 | 2024-10-14 13:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e3990d46-433d-3e1b-846a-91974aab84c2 | -10.9717 | -44.5342 | 2024-10-14 13:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 890ebaa2-f278-3462-b9f3-ba04f93666c7 | -11.245 | -44.1924 | 2024-10-14 13:26:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| d1c70e87-8ba6-3991-9dd7-f250a571c48d | -11.2666 | -51.3263 | 2024-10-14 13:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 6e4c78e6-9b06-30a9-b4b3-5367a66ce5a0 | -12.1073 | -43.1861 | 2024-10-14 13:26:14 | GOES-16 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 30453aaa-4dab-36ae-9a0e-d5de718b818d | -12.4432 | -47.9133 | 2024-10-14 13:26:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 972e09af-5acf-3e93-8ff0-e10b701c26b8 | -12.6159 | -44.7519 | 2024-10-14 13:26:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 7a1f7f26-2daf-3596-85eb-02fed567e071 | -12.5962 | -44.7783 | 2024-10-14 13:26:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| f46dd9a2-4dab-3368-9e5f-5f3bc5ca03a7 | -13.3889 | -44.694 | 2024-10-14 13:26:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 381cf7ff-0a77-307a-9af5-b8f8cd9a294b | -9.4481 | -46.0308 | 2024-10-14 13:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 3e203d4f-105b-379a-bddf-77f2116a1b81 | -9.4175 | -45.5134 | 2024-10-14 13:35:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 2c056488-f146-30d3-a4e9-cec91459a9ae | -9.4365 | -45.5112 | 2024-10-14 13:35:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 154.1 |
| c333128c-79dc-3267-a61b-2be785593a70 | -9.4554 | -45.509 | 2024-10-14 13:35:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 2e7eca13-fdb0-3f6e-9f63-3859cedcb7ed | -9.753 | -45.8826 | 2024-10-14 13:36:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 49ad0bbb-1388-361d-a69a-7164230b91b8 | -9.707 | -46.4513 | 2024-10-14 13:36:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 7173e911-0361-345e-bf23-1d59461a74ce | -10.0443 | -44.1717 | 2024-10-14 13:36:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 63426c0e-a9d0-35a3-806b-f9345ee10c50 | -10.0435 | -44.2183 | 2024-10-14 13:36:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 7003a24a-d472-3e3a-ba34-7003f4ae8f56 | -9.8504 | -47.0162 | 2024-10-14 13:36:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 942fe238-0131-3ebb-9f8f-7e6dbd70238b | -10.0439 | -44.195 | 2024-10-14 13:36:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 2dd314d7-27c1-3d09-b0b9-fa433f82102e | -10.082 | -44.19 | 2024-10-14 13:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 0201d99e-61b6-3b3c-aa09-2ac6a9f882e2 | -10.0622 | -44.2391 | 2024-10-14 13:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 234.2 |
| 7f0a872a-bea6-327f-a503-439d7dcc10bf | -10.0633 | -44.1692 | 2024-10-14 13:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 19f26460-b1d3-3eae-8fc9-634a225003ff | -10.0738 | -47.2798 | 2024-10-14 13:36:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 029d15df-e898-3e38-a92d-d710a6f1ad48 | -10.1637 | -46.3079 | 2024-10-14 13:36:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 155.4 |
| cee0df69-f184-3ab7-a64a-f798eab2f8ee | -10.164 | -46.2853 | 2024-10-14 13:36:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 4048fc32-2550-354b-bdf6-7018579229df | -10.3493 | -46.5777 | 2024-10-14 13:36:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0fe217ef-cc91-37a8-bf7b-e51f0c641a77 | -10.349 | -46.6002 | 2024-10-14 13:36:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 9418e8ab-b4ab-33c7-9b4e-496ac8190518 | -10.4716 | -49.9624 | 2024-10-14 13:36:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 22e66ad7-cbc6-3378-b112-80ed335d7325 | -10.6605 | -47.3442 | 2024-10-14 13:36:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| e1ea8f45-91af-346e-8d99-8672615cf2eb | -10.6795 | -47.3419 | 2024-10-14 13:36:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| ec7e68c1-51d1-34e5-b926-9496f5d2e78e | -10.912 | -44.6816 | 2024-10-14 13:36:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 7ad6f8e4-028c-3759-bde8-bc29be290d0f | -10.9307 | -44.7021 | 2024-10-14 13:36:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| b7e20f87-10da-3d04-bdc8-4476ce0f5c89 | -10.8925 | -44.7074 | 2024-10-14 13:36:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d6e62c56-a960-32b6-93c3-c343410cd66c | -10.9116 | -44.7048 | 2024-10-14 13:36:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 89c76a96-78d0-3751-97a2-91277b72720f | -10.9311 | -44.6789 | 2024-10-14 13:36:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 9fbbebbc-87cd-3c77-8978-03a6e2bda4a7 | -11.245 | -44.1924 | 2024-10-14 13:36:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 6ed76785-f500-3ce8-ab9e-b3d828cfe5dd | -11.2258 | -44.1952 | 2024-10-14 13:36:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 4388679f-362a-3c8b-8167-9ab38a38500f | -11.4597 | -43.9499 | 2024-10-14 13:36:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 9e9a6a6d-c22c-3c7d-88d7-97a8d3122667 | -11.2289 | -51.3091 | 2024-10-14 13:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 8a8ccb4b-b230-39e2-a3ec-41a268f5ff9f | -12.5962 | -44.7783 | 2024-10-14 13:36:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| b641b72d-7a19-3c20-9f0f-d2ef862168fd | -13.3889 | -44.694 | 2024-10-14 13:36:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| dbc775e3-eaee-3640-bd3c-14bb6f9d43f2 | -2.4344 | -46.9195 | 2024-10-14 13:45:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b3573312-5d70-374b-a54c-4a936177c881 | -9.3149 | -46.0908 | 2024-10-14 13:45:58 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 919a8c2c-a946-3d18-b407-bce59a2d3fc2 | -9.4365 | -45.5112 | 2024-10-14 13:45:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 148.5 |
| d427a161-798b-3437-bff2-b688e13a228b | -9.4699 | -45.8249 | 2024-10-14 13:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 950673c6-4716-39e0-bec0-ad16c5f587a2 | -9.4175 | -45.5134 | 2024-10-14 13:45:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 22f2c318-11fd-3c5b-9f82-d63dbda2a412 | -9.4702 | -45.8023 | 2024-10-14 13:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 632fb001-d694-3a4b-8af0-af5c669f1b39 | -9.4892 | -45.8001 | 2024-10-14 13:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e0009918-e8b6-38ad-b9d0-cabc2f785e85 | -9.4888 | -45.8228 | 2024-10-14 13:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 44e0a350-0227-3c50-97db-7220c65ebdb8 | -9.9408 | -47.3171 | 2024-10-14 13:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 7e59ef62-88a6-3187-9dba-32e34bdce3a6 | -9.9414 | -47.2727 | 2024-10-14 13:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 14b29ecc-37cd-355c-8cd8-2a9914f70787 | -10.0439 | -44.195 | 2024-10-14 13:46:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 958dc310-fdb6-3864-a744-67acc96a449f | -9.8685 | -45.7556 | 2024-10-14 13:46:02 | GOES-16 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 03de71e2-b9e8-3b6b-a3f2-0e4ffe112f60 | -9.9973 | -47.3329 | 2024-10-14 13:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 0193350c-9c85-357d-ae3a-30d1cae45be9 | -10.0432 | -44.2416 | 2024-10-14 13:46:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f80d60ab-bd42-3a8f-8f51-98deb9c01756 | -9.9793 | -47.2684 | 2024-10-14 13:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 97243ca6-4753-3037-9960-6173dac25cd9 | -9.9411 | -47.2949 | 2024-10-14 13:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 90f82fa3-2714-3eb9-b621-03bfe8a6fa69 | -9.979 | -47.2906 | 2024-10-14 13:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 05ecfc3e-f37c-3146-8e73-f30a1eaf90ce | -10.0443 | -44.1717 | 2024-10-14 13:46:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 9c81d47c-220b-3779-a9e2-0c01282083e6 | -9.997 | -47.3551 | 2024-10-14 13:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 44b1faba-a2c7-3d5b-9745-dd1b7eb79709 | -10.0633 | -44.1692 | 2024-10-14 13:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 2b91d33d-caad-33b5-a766-6af176546164 | -10.0352 | -47.3286 | 2024-10-14 13:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 265.6 |
| b297f8a8-7608-33f9-be55-0212b26f4223 | -10.0738 | -47.2798 | 2024-10-14 13:46:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 6e1b042a-e1b3-3417-bef3-f024a3ddf523 | -10.0735 | -47.3021 | 2024-10-14 13:46:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 4259d80a-d788-3857-ad25-5f10f707f424 | -10.164 | -46.2853 | 2024-10-14 13:46:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e7cb9a35-e88a-37e6-a0d2-87b1fd1d7feb | -10.0163 | -47.3308 | 2024-10-14 13:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 265.0 |
| 4ab8934d-2ae8-3616-93f8-cd9d2b5e56e2 | -10.082 | -44.19 | 2024-10-14 13:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 02b7e4aa-4f12-33f7-9d14-c753d56e8407 | -10.183 | -46.283 | 2024-10-14 13:46:03 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| d0b7de50-d6a9-3516-a9b4-40ec839fa2d7 | -10.2635 | -47.2579 | 2024-10-14 13:46:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 9697cf69-bd19-3e61-b081-53d37f403d59 | -10.3493 | -46.5777 | 2024-10-14 13:46:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 1a1177c1-32d5-39d5-81d1-45851f32e1cb | -10.2641 | -47.2134 | 2024-10-14 13:46:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 34bf6f8a-d5a8-395e-88da-b4bb7f8555e2 | -10.9116 | -44.7048 | 2024-10-14 13:46:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 205.4 |
| fdb135ea-65b3-3b6d-858f-5fce92b52296 | -10.9311 | -44.6789 | 2024-10-14 13:46:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 9d73cce3-2642-3265-b806-d68d75315afc | -10.912 | -44.6816 | 2024-10-14 13:46:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 524abe5d-af7c-3253-aaec-fadf0373d5bc | -10.716 | -50.065 | 2024-10-14 13:46:07 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| f911e745-6b5e-3f58-b66b-d1f1e6745237 | -10.8925 | -44.7074 | 2024-10-14 13:46:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |


[Clique aqui para ver as próximas entradas](README134.md)
