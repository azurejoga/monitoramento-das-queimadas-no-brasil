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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f99ba0e-dce5-3ff1-9534-4d3a4c4fae6b | -6.20024 | -43.33304 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dc6bfe59-c1ce-35eb-bf09-2383fc80d4dd | -12.04311 | -48.08258 | 2025-06-10 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7ec0db2-1ad3-35fa-9a92-217b67d711b8 | -10.22067 | -46.92944 | 2025-06-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa340851-aa0e-38fc-bc28-bb3150af3389 | -12.09908 | -44.74741 | 2025-06-10 03:47:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab3ac533-3598-347e-af44-b2299162f1b7 | -10.27478 | -47.60532 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dad2ce5c-e51e-3e8e-8ac9-d5fd22998c0a | -5.64974 | -43.60221 | 2025-06-10 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| eec9ceae-6d48-31d3-b3d2-86e7f6b79173 | -12.42175 | -47.80397 | 2025-06-10 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff81b3fd-759f-3ca5-9ee8-e43850fc199a | -8.96192 | -47.96419 | 2025-06-10 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a5cc897a-3383-3b7b-97fa-671eeb4a91e7 | -12.04799 | -48.07994 | 2025-06-10 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca8b6903-275f-32d7-9b03-9a00032f9551 | -12.20819 | -49.61877 | 2025-06-10 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aefafdc4-41f7-3403-b6cb-a2ab865b9594 | -12.27215 | -44.5884 | 2025-06-10 03:47:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f6c3353-43fc-38f3-afae-9185a048d6b1 | -10.21162 | -46.93157 | 2025-06-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86f94c6c-c8d7-3e09-8b0b-efcd8a1e32f8 | -12.04384 | -48.07875 | 2025-06-10 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e065bf62-b22d-37d7-b772-ea158d69c3b3 | -9.38948 | -48.43531 | 2025-06-10 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f48ce7c1-fd29-33b5-a8f0-e9fa74412a22 | -6.33587 | -43.74487 | 2025-06-10 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd3b46b8-3614-3881-971a-263da7fba72c | -10.65042 | -44.48154 | 2025-06-10 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1dca5f3-faab-3608-9816-6f82aa339064 | -6.20837 | -44.50803 | 2025-06-10 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f53e1296-fc95-3359-b66b-fed49d57989f | -6.83119 | -44.62835 | 2025-06-10 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dcd8f6a-14f9-3d24-9ccc-b46951cc4284 | -5.77996 | -43.61272 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7a1b548-a928-3039-a2fd-0bbfd2de9b66 | -10.21333 | -46.53867 | 2025-06-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4dc3b921-4392-3d7f-bfc9-7efc04164f74 | -12.21329 | -49.62492 | 2025-06-10 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 685bb5c1-2fa4-30ea-91f3-7ff75b413ba8 | -10.04381 | -48.66545 | 2025-06-10 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7e6eb00-a413-34e3-bcde-f73a97c7fb6c | -8.99978 | -49.19692 | 2025-06-10 03:47:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dfa5be71-e693-3795-a2a3-4bfce2e28863 | -10.27409 | -47.60906 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e00a169-4195-352f-9950-68c8de4f656d | -6.21448 | -43.33066 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb3a5b24-f7a9-3a32-9ce0-825863e5868c | -11.56389 | -47.43647 | 2025-06-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d964efda-2dce-3dc2-8341-0698d199942e | -11.57569 | -44.87833 | 2025-06-10 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5c00d7b-ea65-3f1a-be43-ee45c045a686 | -7.56795 | -37.81267 | 2025-06-10 03:47:00 | NOAA-20 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5d2cac1e-6ce4-3570-911a-e71146b12067 | -6.20619 | -44.51003 | 2025-06-10 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e436bd78-051a-3a80-97d3-070e9828e714 | -10.01061 | -48.6769 | 2025-06-10 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db552136-65c1-3bc1-97be-d564ee47aebc | -6.49172 | -42.85039 | 2025-06-10 03:47:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 6092b522-6035-3789-b535-6d9ca569672d | -6.21204 | -44.50523 | 2025-06-10 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 855ec31f-b9f3-3bc6-8843-57e90caf5e34 | -2.51776 | -43.25525 | 2025-06-10 03:47:00 | NOAA-20 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| df7ccf96-e51a-3a1f-b597-659b2090f906 | -2.51857 | -43.25018 | 2025-06-10 03:47:00 | NOAA-20 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b2d1024b-c8f9-37f1-88b2-3ee8014c8149 | -12.26615 | -44.59621 | 2025-06-10 03:47:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebaa66ac-94c8-3d59-b8a6-d8caf818086d | -12.27135 | -44.59273 | 2025-06-10 03:47:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc71d4be-6e19-3f04-b13f-d0496dc1e9dd | -10.21272 | -46.54193 | 2025-06-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cbb12ca-7118-323c-bd7b-b9f254edc85b | -6.71358 | -42.05009 | 2025-06-10 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf54b337-2670-3d92-aff3-eb79b9cb8be8 | -8.99725 | -49.19439 | 2025-06-10 03:47:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36afe89d-d98a-35fe-abda-1e2bb8aceb49 | -10.65172 | -44.48408 | 2025-06-10 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 081bfa0b-ad88-3e0b-9d64-61666294267f | -12.59954 | -45.73679 | 2025-06-10 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8695a94b-097a-378c-8ca2-f1784c07eb12 | -6.48974 | -42.85087 | 2025-06-10 03:47:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 4fb4e128-9703-3213-a785-507c39db3f7a | -10.04975 | -48.66676 | 2025-06-10 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ae701183-2a4b-35e8-b6aa-97d081a09e29 | -5.91714 | -45.52967 | 2025-06-10 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef7d35f4-54b2-3bf9-85f6-680ace25f8a7 | -12.21425 | -49.6202 | 2025-06-10 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0b164c3-59af-3216-b2ab-af975e3136a9 | -9.00074 | -49.19187 | 2025-06-10 03:47:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b7a3995-50d4-342d-ae11-3144fe3166ca | -9.20866 | -48.86299 | 2025-06-10 03:47:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efb68676-2911-363d-a0c2-11e0988a473b | -9.00352 | -49.1956 | 2025-06-10 03:47:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5866385d-ee31-360b-9c61-087798cbf5aa | -5.64595 | -43.59665 | 2025-06-10 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1d16d678-317b-3dbe-a03f-75ecb9d17721 | -10.21404 | -46.93528 | 2025-06-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d63c446-5d46-3e47-a387-ca28f8008a9b | -10.05061 | -48.66227 | 2025-06-10 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c9d2f748-1ee5-3e21-a74e-596890db8e9c | -13.24832 | -40.12528 | 2025-06-10 03:47:00 | NOAA-20 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2cdee5fd-3365-3462-9f58-73b136571a78 | -10.00461 | -48.67587 | 2025-06-10 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4346b48-9d0d-3b0f-8238-087f914bfff8 | -6.19379 | -43.33016 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 145d5e0c-5514-32ef-949b-550db97347a9 | -12.26632 | -44.59764 | 2025-06-10 03:47:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93ba274a-1b61-3f0d-9f9e-861762cb6e35 | -9.2078 | -48.86449 | 2025-06-10 03:47:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 98e7c380-9d76-3030-ae6e-34d14e4debec | -6.20743 | -44.51365 | 2025-06-10 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e2d308e-c05b-376c-85b2-f0e2d8a6f819 | -5.91302 | -45.52224 | 2025-06-10 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b34eed55-9859-375d-8582-506326912912 | -10.21098 | -46.93503 | 2025-06-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a384123-e5ab-38f6-8a33-5e68bc3a8364 | -6.32726 | -47.33873 | 2025-06-10 03:47:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52689047-01e2-3a9a-8511-0452df21d300 | -6.33144 | -43.74624 | 2025-06-10 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1084a0d-8a99-3a21-9421-876e0f7d55bd | -5.91247 | -45.52547 | 2025-06-10 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3590692c-2c9e-3111-a77b-d4e8f5274369 | -11.44789 | -37.76692 | 2025-06-10 03:47:00 | NOAA-20 | CRISTINÁPOLIS | SERGIPE | Brasil | 2801702 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a428c83f-b8f7-31db-b526-362ffa2390a2 | -13.65728 | -41.62117 | 2025-06-10 03:47:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| be69b8fe-7e9a-36fd-a6d5-9d753372de3b | -4.30786 | -48.07787 | 2025-06-10 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 31328f5d-3dc7-3304-9a6b-034b7c24a207 | -6.19204 | -43.32713 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 06a184ac-a2ef-3644-a336-a9fb0705a7f4 | -6.20102 | -43.3285 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3226edca-3249-3593-85a9-b2774cee152c | -13.37251 | -40.03112 | 2025-06-10 03:47:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e4afbb36-ab20-3ad0-a1fb-f77ab7f62d6f | -12.2254 | -44.1899 | 2025-06-10 03:47:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d453205-0c19-3cde-bd98-216bb50425ce | -6.70951 | -42.04929 | 2025-06-10 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a79dd25b-95b0-3e80-a053-ef9abdceb71f | -10.20811 | -46.53783 | 2025-06-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1699dafa-af62-3fc9-8eda-c57455a02e92 | -10.75378 | -44.45728 | 2025-06-10 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e98d14ce-de5f-3b52-85b2-2a137f852fb1 | -10.05566 | -48.66824 | 2025-06-10 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5fb2bd2e-d4e7-30b4-a5d0-61214deb7228 | -12.42601 | -47.80524 | 2025-06-10 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50ce6495-c0ec-35c9-badd-e02dd4972fb5 | -5.77374 | -43.62156 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 046d5bd6-4fe3-3a12-94a1-fef9a4d39aec | -11.58261 | -51.33846 | 2025-06-10 03:47:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80ae4672-a973-35ef-abb2-3b26308d02aa | -6.68308 | -43.97233 | 2025-06-10 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13fbecfa-2a54-3cf5-8b3d-37b4bb41ba30 | -4.8202 | -44.35726 | 2025-06-10 03:47:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91f49d40-73da-3ce0-9af9-2a3ddad4214a | -10.75654 | -44.45502 | 2025-06-10 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8883b8e0-94da-3728-a1da-12142a612734 | -11.89718 | -47.44891 | 2025-06-10 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0b37450-6590-334a-ab26-1e57a62933ff | -5.81414 | -46.48999 | 2025-06-10 03:47:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f41c5cde-d3da-3ced-9b35-46a3ae4f1544 | -11.62435 | -47.68399 | 2025-06-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b4ac6de-ca3d-3e7b-91e5-f6824b47dbb6 | -10.04889 | -48.67124 | 2025-06-10 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 74e92164-14a8-399d-aaa6-523cf7f3975f | -6.21526 | -43.32617 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3edc0dcb-7685-3f94-a1f1-aa1a0b5da3ff | -11.58941 | -51.33986 | 2025-06-10 03:47:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87fd7917-89a7-314d-a00a-1fe8214ef664 | -12.48831 | -46.84331 | 2025-06-10 03:47:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12da9065-d549-3428-8a03-58b644513884 | -6.33223 | -43.74152 | 2025-06-10 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d555be3-088f-3bdc-907c-f3c8c208218f | -10.75458 | -44.45277 | 2025-06-10 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6472993c-4465-3a19-9724-5db3b1d385c6 | -10.21469 | -46.93188 | 2025-06-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 644489d2-c196-31d8-8f5a-1a7ad0feba59 | -13.65514 | -41.61954 | 2025-06-10 03:47:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 416afb2e-7311-3e11-b31b-2f027fd1a5ff | -12.48608 | -46.84285 | 2025-06-10 03:47:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2f7cf12-758e-37df-8569-d6a01a3ca731 | -5.78295 | -43.62311 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 156da3c9-3235-31f3-937e-33ced149e6d2 | -10.21793 | -46.54282 | 2025-06-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea23cec3-4421-327b-99de-2bdb19ef88f0 | -6.21079 | -43.32536 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd3a3499-b88d-3c49-8c5f-2dc979f4725d | -12.22789 | -44.1889 | 2025-06-10 03:47:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcb3e85f-341b-3d07-97fa-7e612a635370 | -12.42718 | -47.805 | 2025-06-10 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25919be0-045a-34fd-95c3-76f124c125e4 | -11.56928 | -47.43746 | 2025-06-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 219aa1ca-f29d-3542-8933-b17c421c8fa3 | -6.19575 | -43.33233 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b48ee87b-1b11-3c4f-8d3d-8bc4a63fe3b6 | -12.29468 | -50.10751 | 2025-06-10 03:49:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 11e1215c-0453-387a-8b1d-8da034b9f74f | -14.21235 | -45.4874 | 2025-06-10 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
