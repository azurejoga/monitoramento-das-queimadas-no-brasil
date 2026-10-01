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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a63443ca-2c95-3efc-8322-3d34429f7a50 | -3.12163 | -50.26148 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9550c4ec-45ad-3a91-a335-3269f92ae39d | -3.95879 | -49.45137 | 2026-10-01 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8af783e7-8447-3de3-b59a-1addc37498f0 | -5.73716 | -45.16494 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd962509-2afb-3298-bcb8-6956ac50c176 | -3.00451 | -53.87683 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2315416b-5270-3ec8-95e3-55ae4607c5c1 | -4.25569 | -50.75227 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| bca6e1fe-2bdd-3059-b4a5-39c7c9913a83 | -4.29777 | -54.79755 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62083f9d-76ad-37d1-b51a-db397e844073 | -4.27236 | -50.74985 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e0231418-7027-36c6-99c1-c2c0ce1097c9 | -1.14773 | -48.86523 | 2026-10-01 04:32:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41816445-1839-341d-a347-ad067399946e | -2.77847 | -51.37106 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91e9752c-664f-3374-b079-0709cdd903f1 | -6.24287 | -47.44243 | 2026-10-01 04:32:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1340292-2b81-359d-8c95-2b733403d571 | -5.17761 | -46.19637 | 2026-10-01 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 90a70438-026b-3d99-9fac-878263bfc28d | -3.01307 | -53.88707 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fa91aff-22cb-36af-a6a3-6765e73ea9f1 | -2.99234 | -51.03873 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae67c647-3c22-3af1-acd2-389bb582e002 | -2.4468 | -49.22097 | 2026-10-01 04:32:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a10e2b7-16fc-332d-a842-8c27fed66ced | -2.97467 | -51.04344 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88c12204-523f-3607-93fb-2e969108198f | -5.87022 | -50.16213 | 2026-10-01 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8913cbed-7f6a-3987-be17-10c714d14a22 | -4.24924 | -50.76705 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c9ccd17a-4ba8-3f8d-8cbb-f330f8615575 | -3.25521 | -48.77471 | 2026-10-01 04:32:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 529abb70-fea8-3cb9-8984-2b7624ce42fb | -4.85609 | -45.84528 | 2026-10-01 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88b2d269-a697-3af0-bc60-2d6522b10b7d | -5.73826 | -45.15787 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4933dc55-308d-3bae-8e8a-e5e15dd3a16f | -3.10599 | -50.25894 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0c39ca8-f750-3b95-946c-e91ecc4b5d5b | -2.98882 | -51.03438 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d7b7f871-b8c0-332d-9544-c379e92305ad | -5.74551 | -45.15535 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1c9cb2b4-44a0-3413-b1e4-61a0355f6872 | -3.54806 | -41.56605 | 2026-10-01 04:32:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 83ff889a-714b-39df-869e-a889fbbbfa3c | -4.2644 | -50.73984 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aea1894d-b23a-3028-b899-0ce5c3b068ee | -2.99353 | -51.03138 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3aad7b1d-32e9-3188-a8bd-3179a2e1ab0c | -5.40684 | -48.42241 | 2026-10-01 04:32:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85856438-7547-3a37-bc80-a360ae1c2c88 | -7.3959 | -42.65895 | 2026-10-01 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 124fe866-c487-363b-aa66-d202e51bb3e0 | -4.28505 | -48.5609 | 2026-10-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbe67822-3aee-33a4-97bf-0c9f8059b455 | -4.28138 | -50.78451 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 243.8 |
| ff569d06-c131-345d-9f0a-3f8cac322c78 | -5.11382 | -56.01421 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2758019-513b-33ec-856f-45760373b2b7 | -4.25926 | -50.77046 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ca823270-6d16-3a07-aa2e-597cffdf7422 | -3.16595 | -54.10569 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 722ad0a3-9a01-30eb-af2b-03c8e22262a7 | -5.75725 | -45.16802 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 086f28ce-9b53-3b78-8adf-c1d638c1717c | -3.1035 | -50.2992 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| eff36f45-2c5e-3cac-b8c2-568c8080a23f | -4.27206 | -50.76707 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| a3b14866-7c48-3233-b851-e6a1496229b5 | -5.10533 | -45.66457 | 2026-10-01 04:32:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d3cbda0-cb85-3b3c-8a99-754585f8629c | -5.43874 | -43.74442 | 2026-10-01 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea44fd21-6c8f-368e-a9e0-970e8b4316be | -4.03933 | -54.22957 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40221544-395a-3b53-9d6d-32c434d8bd3e | -1.9094 | -45.80971 | 2026-10-01 04:32:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3a2c9776-0abe-3f38-9c05-c067de1be342 | -3.30086 | -53.85738 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4a72b7f-d7a3-3568-a7b2-d748af0f553f | -2.44542 | -49.21924 | 2026-10-01 04:32:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d51cbc06-3218-3d4b-bfe0-b441c81a46ad | -3.12236 | -50.28189 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 249a16ee-6080-32de-8a51-6c32eafa93cd | -3.03318 | -48.41856 | 2026-10-01 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d0ef5a8-3cee-3dcf-8ba0-ad43d72145d6 | -3.00354 | -54.22522 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99532a25-fd75-3710-abeb-e62369def3ac | -2.96883 | -51.02735 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b27c26cc-fa5a-31fa-bcf6-90833a7be04f | -3.11301 | -50.26516 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cd667a6-811a-339f-af8b-d171e8b654a9 | -4.88835 | -48.37579 | 2026-10-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 87de926e-8b5f-3a80-a730-76059c79bbd6 | -4.26514 | -50.76951 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 96300b67-fe6d-3a0a-95f3-496afdcf01b6 | -4.27458 | -50.75199 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 6bdb3e54-7173-37fd-bb5c-29bde75d3fd9 | -5.29824 | -55.87048 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7516a88b-468e-36cc-9935-3444ea7d4e23 | -3.17312 | -54.10228 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 6488bf63-1576-39da-9c86-6179493bd2f9 | -2.96472 | -51.02668 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 10d22e0e-1c79-32a0-bcd6-5a46a4e62521 | -5.18037 | -46.20034 | 2026-10-01 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d7edfed8-0af4-3d06-914b-dcc5e854abd6 | -4.27602 | -50.76775 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 150.5 |
| e08b87f6-1bec-3830-a95f-b473cd63aa41 | -3.02594 | -53.87162 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 965c7dce-f69e-3b88-910c-edcce699a91a | -4.28251 | -50.75328 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3fb313b7-9dda-3fb2-b07c-2cb55045dc66 | -5.74216 | -45.15483 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 155892ef-4f2c-36ff-a53b-0f9461ddac28 | -4.27854 | -50.75263 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 835c4c1d-ce40-32b8-9a7d-f135df700ad2 | -6.75273 | -46.46061 | 2026-10-01 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfe72d11-2514-3f60-ac3d-c69af0bca908 | -3.85641 | -49.74087 | 2026-10-01 04:32:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0646fda-7564-3b0b-ae50-77d3de00d706 | -5.76116 | -45.165 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de65ba38-8a1e-3412-91ff-00c86f3028cd | -1.83063 | -54.99047 | 2026-10-01 04:32:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fa6ff86-c79e-3703-b407-b84f04912f5d | -4.14128 | -48.91047 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62be96b1-b155-386c-a091-f28fd20a2978 | -2.35025 | -45.85807 | 2026-10-01 04:32:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11910156-438f-3da2-a4c9-0a7a067112f5 | -4.12041 | -53.81248 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f3cd821-75d8-3ea6-8397-b29aeb0ef264 | -6.39048 | -45.80667 | 2026-10-01 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa9a86af-5bb5-3972-b784-26100d2b7b7f | -2.82987 | -50.47343 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 707f4a6d-6c0c-3a45-b76e-9e4a89510a7f | -5.92777 | -44.11544 | 2026-10-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44140399-228c-3055-962e-a719dea5818d | -2.9124 | -51.32027 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 233ed26d-33e3-345b-b0f8-3d45e39bdb0f | -3.14039 | -53.74087 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 45ce594a-8cbd-3bdd-bedb-eff3fae72625 | -3.2254 | -54.31411 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1a2ebcc-d499-3167-b0cc-631e20248f34 | -3.1811 | -54.10847 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 59c69f21-e1b2-36aa-9d08-3c47449f92a0 | -4.29641 | -50.79227 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6477cae5-6680-377a-b32f-40a6b267d4ff | -3.10269 | -50.30421 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebde845b-8763-3b75-b880-74673b1eb0d6 | -5.7634 | -45.17259 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f7dec2f-6a40-32d3-85a7-c98e5513f902 | -4.28337 | -50.7481 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4fc09466-bb45-3405-8c65-2674b3cdb368 | -3.59474 | -54.55751 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e3a7445-19af-3dba-97c1-c25b6e499726 | -4.29837 | -50.75584 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 645438a6-4fe3-3189-b188-ad6ee31cbbb3 | -3.95626 | -49.05145 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6657c0c7-e495-30fb-a2d6-38ee7a397519 | -3.54608 | -41.5672 | 2026-10-01 04:32:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 95d5c6f3-6d05-3ae5-a8fd-8d8e36a9ea45 | -2.98823 | -51.03805 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 26a798a7-77ee-3358-958f-780e5c695ec1 | -4.86049 | -45.83891 | 2026-10-01 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2c90da7-fe84-3692-b85f-e3007c51b4a1 | -3.17101 | -54.10657 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 133ca2bb-f6ea-3cce-86a6-55c7794fc72c | -3.01522 | -51.46049 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f9f9d368-ed4a-30fe-add7-2e96047651e8 | -4.30091 | -50.74049 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a70ec564-0f64-35c9-b989-908af1052337 | -3.16252 | -54.10346 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5e05bf3-8a8b-3f25-81fc-5e43852fb7b6 | -5.75277 | -45.15283 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f56c679f-9a26-3206-ab9e-91a75c39a153 | -6.42609 | -46.67825 | 2026-10-01 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2cc9425f-f05c-3302-9c57-0964ffd59ffc | -4.26526 | -50.74342 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d8efb4a-c1f4-310f-b992-b199f7b08500 | -4.29187 | -50.77046 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| d7dabcae-9b52-3e3d-8c14-da05b6f37bb1 | -3.17656 | -54.10457 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 94697a07-6290-3428-a4f5-44f11d88fb5a | -4.26032 | -50.77413 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d0ee35a0-f194-38a7-a195-03a1b99d4d8d | -6.72867 | -45.53619 | 2026-10-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea6408fc-4354-3c27-a6c0-2a3ad6e3dd90 | -5.76396 | -45.16904 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5cb6b58-0350-31e8-bd2b-68273b7fdd62 | -3.06991 | -54.37838 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 107d3ac2-2312-3abe-b1bc-fe806e13c513 | -4.29811 | -50.78197 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6dfff005-81a1-3a3e-b8f6-2b9e6d4ab035 | -4.26099 | -50.76015 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 561b7cbb-2ed3-33e7-b136-b1849eadf907 | -3.11213 | -50.29553 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5d6b3d1-08de-3e40-ac80-c921979e66f1 | -4.12603 | -46.871 | 2026-10-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README50.md)
