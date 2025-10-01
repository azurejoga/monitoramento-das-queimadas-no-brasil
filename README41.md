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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1d05d17-0bc7-3c04-b4e5-be0b0f59a491 | -7.39276 | -45.93229 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbaee61b-2f2e-3ed8-b046-b9860c4f978e | -5.64712 | -43.9353 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ee066a5-94e8-3b82-95cc-564be82fb188 | -6.63541 | -42.03933 | 2025-10-01 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4553457c-c107-38a9-8572-3c988e13364c | -7.47683 | -47.26857 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa34950f-e22d-31c6-b76d-c7d5437748af | -4.40128 | -50.84786 | 2025-10-01 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e9ebd821-5901-3c62-9895-66edff89daed | -6.7217 | -44.59676 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be4e9586-007c-3b07-b9c0-7a422870f57e | -6.447 | -44.45793 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1d9eccf-404b-36c6-afa4-994cd9ad1f71 | -5.38571 | -43.58056 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f4108324-457c-3ad4-b22f-9c1396c7b47e | -6.03431 | -43.60936 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 706d52e9-cbae-3997-bf34-cd30733497c1 | -6.54931 | -44.12664 | 2025-10-01 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35882cff-571c-36f7-94c2-303daeaf3b8a | -5.9355 | -43.54383 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f76c7a6-e48a-333a-8111-3862daa0aa38 | -5.9835 | -45.71834 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0928442f-855f-34a1-8982-dee127207173 | -8.80578 | -48.78246 | 2025-10-01 04:19:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc028e26-c6e3-3963-8c2c-ea827ad30577 | -2.26812 | -47.84936 | 2025-10-01 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| b38dea42-646b-39f2-b04a-16e88dd96a76 | -7.02166 | -44.45953 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 485e1149-718a-3945-8431-4b039113c8c7 | -5.11018 | -43.07145 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 424365a6-276c-3674-aa85-b0696d085777 | -5.64265 | -43.92041 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 1aef25f0-d307-388b-9950-ccb657c12247 | -7.34641 | -45.23306 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e4d2d24-69ee-3220-95e0-7097713d96f2 | -5.4097 | -41.33016 | 2025-10-01 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c4a57b8c-1f99-398a-ac89-5525c3db2b32 | -5.99304 | -43.43693 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cf58da9-4db4-3f52-ba32-e18f30c3298d | -5.64095 | -43.90947 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 80af26df-9ba4-3966-8d6f-75f9e0e32fdc | -3.46859 | -50.08669 | 2025-10-01 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e5ae24ba-8694-313e-b874-c8e35770823f | -5.64257 | -43.89904 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d66f2062-eacf-39c1-a54e-2b0007001c85 | -7.48158 | -47.27662 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b344ede0-8fd1-3e3c-a34d-eb5a54e5bfd7 | -7.47967 | -47.27293 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0386d41-4f0c-334e-8fbe-ce9e48833707 | -9.77234 | -46.23285 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6ae1a342-e326-348b-a3ce-6c8588a0a46b | -5.46656 | -43.07824 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e27782d3-7725-33d6-b506-b7a023483e96 | -3.10515 | -47.0125 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e67d3a42-6b32-3001-8711-1119760a3435 | -6.04645 | -42.45346 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4a148633-5e5e-3ec4-b18e-c604711cd3de | -5.80403 | -43.73494 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f2c3f933-3a60-3562-9e1a-f0a654ea3c95 | -6.47742 | -46.4869 | 2025-10-01 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7e68896-3131-30bb-883d-6a9fe7d7bb13 | -8.90046 | -45.04463 | 2025-10-01 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 87e4f26a-18f4-3992-bd05-efe23169ff27 | -5.88781 | -48.12067 | 2025-10-01 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ec4fa205-7b79-3039-8dbb-b706c0159447 | -8.97511 | -50.26485 | 2025-10-01 04:19:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc0db92c-4fb7-3206-a403-75531bdd7e34 | -6.56353 | -43.40022 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50071f3b-0e41-3e5b-9050-2c9323aa3356 | -5.15462 | -46.41036 | 2025-10-01 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4577d855-8f0a-31b2-93f4-228b001a44c7 | -6.04762 | -42.44591 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d5eff111-5b1f-301f-877a-b2160f5f7048 | -4.95157 | -42.66262 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3322208-b437-3009-bc67-45fc022593a9 | -7.475 | -47.28002 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 291a50fc-98f8-3055-b41f-a32d95ac54e8 | -3.9362 | -41.59001 | 2025-10-01 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 256bbea1-11ab-3e7e-9703-2bf7b4ace57d | -9.32658 | -45.69245 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8bce904-3e06-3c96-aa0e-bca9f68bfb78 | -8.58914 | -44.72846 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cef72559-632d-3a25-8555-7d7a390083a6 | -7.02612 | -44.47433 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80305ddd-338c-3d0b-95d6-2a7070f2f7ea | -5.94567 | -45.87154 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b668d28-d9c1-3297-a0eb-7fbe85f44846 | -7.46625 | -46.47689 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3869cb3d-bfaa-3acc-adf4-e24240cf90a4 | -8.89218 | -45.03267 | 2025-10-01 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb4bc41d-3553-322f-b80d-5af88e933530 | -5.93839 | -45.89597 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f7c4672f-3b5b-37e7-96db-c5f0c5e48151 | -5.15391 | -43.73703 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 536a90e5-7973-3fb5-86cf-5b49169603ad | -10.21591 | -43.03949 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f9363ab6-27ab-3208-a8b0-bb00359b4f01 | -8.7517 | -45.92796 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7da044cc-1b76-381c-867a-c9564852f2cd | -2.2719 | -47.84996 | 2025-10-01 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 02627be0-ccb1-3e6b-94e5-cbdddec89a54 | -2.65197 | -48.50653 | 2025-10-01 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad7a0aad-42a7-3e14-b2c6-28cadd1548ec | -5.76909 | -43.30031 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 55ac7638-99ec-3311-b907-a16dc78a2610 | -3.45934 | -50.08941 | 2025-10-01 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9794028-46b5-312d-8976-ed0c6387699a | -5.85509 | -43.40429 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 7e029afb-6f1b-33c4-906e-acf2a2f063a8 | -5.95403 | -45.86199 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5d56eaa-5dea-3e12-9aa8-f960cce2ad96 | -7.80769 | -50.04093 | 2025-10-01 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b2bd6c7-d6bf-3ca9-b4e9-1e09693aa3b0 | -7.46178 | -47.274 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f317379-3111-33cb-9ee7-1e636df61bd2 | -4.80899 | -45.33055 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f53c0af-9963-36a2-b680-04c4c01d0f20 | -5.28259 | -42.76851 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ae9d3c1-5378-31d8-b267-d88f9c45040a | -7.39355 | -44.6073 | 2025-10-01 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e971a60-e20e-355b-9abd-e74ff1299f1b | -5.95235 | -45.87262 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 824dfffd-1f47-3631-8a9d-78c5a06428d4 | -9.80176 | -45.93997 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d7a6ee9-e3fc-32b3-8809-fcba9f6d47c8 | -8.53444 | -44.61988 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cb1f69b-8273-3a4a-b656-5bd8db66719f | -7.19642 | -47.6148 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3018662b-fe66-3b82-89ad-62ad94df567b | -6.9802 | -44.39985 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3bdb24e-a19c-3dd2-8cd1-116ddea8ba48 | -7.05319 | -46.42123 | 2025-10-01 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44c6a76f-39ca-38ea-a469-20b19f8ddb5c | -6.84566 | -44.84568 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12839cb7-c1ec-35fe-bf36-d03be3f4510c | -3.54193 | -51.15567 | 2025-10-01 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 931bf372-296b-364f-abb7-e5ecce8249b8 | -6.118 | -43.22175 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d1f5208d-8748-3e28-8fcf-8eb24166e9c6 | -5.82369 | -42.85456 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 02d2ac24-690d-3854-94c3-7f6fdc9aecac | -7.78943 | -42.51007 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 78f025f6-81dc-3f5d-9234-a447aa852cbe | -6.11519 | -43.2176 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cf7fcba6-9d03-339c-aeb1-ba55d903c1e8 | -6.14143 | -44.73399 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0711dbbe-5bd0-3b2e-875c-357047579c17 | -5.70288 | -42.65937 | 2025-10-01 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7fb89236-d001-3f60-918e-6a7824446c4f | -6.11216 | -43.39311 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdd7ef3b-f65e-3d0a-8c59-dd7e23a1c6f0 | -4.09759 | -44.81274 | 2025-10-01 04:19:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3199e38-ac55-3df9-812b-a054d99f8da8 | -6.63557 | -51.19114 | 2025-10-01 04:19:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b740a2a-cc1e-332e-a6f7-42ac65813813 | -8.58806 | -44.73541 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb4a018f-e58c-3c13-8979-13c11fa1ea9f | -5.89723 | -43.3088 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 640946c5-108f-398b-84ee-4b0a03b266f7 | -5.64211 | -43.92387 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| b90ad1bc-b41a-3f17-bd21-20cbb5bfe16a | -9.44466 | -45.48352 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21ae82a7-2add-32a6-9aab-b5425b05161a | -9.93663 | -43.6497 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7f52b97-b338-3e87-98ab-654b1e02c349 | -5.53463 | -43.87172 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6f0887a2-cda0-34fe-b1b6-681a0c38fd16 | -5.4484 | -44.64195 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4cf5daa-bdca-349b-a74e-40a41bb55c06 | -3.94031 | -41.5866 | 2025-10-01 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 361c7c99-ecaf-31bd-bd85-29dcfaeb0433 | -9.47159 | -45.48423 | 2025-10-01 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65da2e00-9b7e-305a-b958-dd43922ff64a | -6.8329 | -44.62483 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9567ea7e-9dfe-3e36-80a3-24d7c5c8296d | -8.54229 | -44.67832 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8a92bc0-b0a4-3bc3-83a1-be3643297f04 | -5.94457 | -45.83516 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af2804e2-b2de-3af0-acc1-b8542290b74f | -6.89029 | -44.53833 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90cd09ce-04b4-3d92-8abe-ffd0a7119953 | -9.93892 | -43.65771 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab6e3364-4e07-3cab-9f90-eb18ff537f00 | -7.82611 | -47.06065 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 79058c74-201f-3570-a35b-494ef5209aa5 | -5.48684 | -37.3798 | 2025-10-01 04:19:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6f3ed00a-f70f-3d92-a4bd-fb8ff1739e06 | -6.40052 | -43.52851 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70f3eb7c-80d8-3e2d-bd5d-90759956ec0a | -7.76913 | -45.76991 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52ccec40-5a1e-392d-b575-65d82bf3b21c | -3.98765 | -44.31925 | 2025-10-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4206e31-a2af-3380-95d4-b55e08678636 | -6.28046 | -44.06307 | 2025-10-01 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a62b8a2-8185-3f9f-b065-c78c295d4dce | -4.15831 | -50.22654 | 2025-10-01 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baca9cd7-270d-33f4-b123-e2658f071e4e | -6.36275 | -44.58176 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README42.md)
